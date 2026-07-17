# hoover_bot k3s deploy

Manifests for running hoover_bot on the k3s cluster on host **yggdrasil**.

## How it deploys

`.github/workflows/deploy.yml` runs on every push to `main`:

1. **check** (GitHub-hosted) — lint (`black --check`) and `kubectl kustomize deploy/k3s`.
2. **deploy** (self-hosted ARC runner pod, `runs-on: yggdrasil-runners`):
   1. builds the repo `Dockerfile` with the in-cluster **buildkit**
      (`buildkit.arc-runners.svc:1234`) — no docker daemon,
   2. pushes `10.3.3.69:5000/hoover-bot:<sha>` to the in-cluster **registry**
      (nodes trust it as insecure via `/etc/rancher/k3s/registries.yaml`),
   3. applies the Discord token Secret (`hooverbot-secrets`, from the
      `DISCORD_TOKEN` Actions secret),
   4. pins `newTag` to the commit SHA in `kustomization.yaml` and
      `kubectl apply -k deploy/k3s`.

The runner pod uses its own in-cluster ServiceAccount (cluster RBAC), so there
is no kubeconfig or registry credential in the workflow.

## Manifests

- `namespace.yaml` — the `hoover-bot` namespace.
- `deployment.yaml` — 1 replica, `Recreate` strategy (a bot holds one gateway
  connection; two pods would double every handler). Reads `TOKEN` from the
  `hooverbot-secrets` Secret. Exposes metrics on `9090`; TCP probes on it.
- `service.yaml` — ClusterIP for Prometheus to scrape metrics (`9090`). The bot
  is outbound-only; there is no inbound Service/Ingress.
- `kustomization.yaml` — the single place the image `newName`/`newTag` is set.

## Secret

`hooverbot-secrets` (key `TOKEN`) is **not** committed. CI creates/updates it
from the `DISCORD_TOKEN` GitHub Actions secret. To seed it manually instead:

```
kubectl create secret generic hooverbot-secrets \
  -n hoover-bot --from-literal=TOKEN='<discord-bot-token>' \
  --dry-run=client -o yaml | kubectl apply -f -
```

## Manual deploy (equivalent of the CI deploy step)

```
TAG=$(git rev-parse --short=7 HEAD)
buildctl --addr tcp://buildkit.arc-runners.svc:1234 build \
  --frontend dockerfile.v0 --local context=. --local dockerfile=. \
  --output "type=image,name=10.3.3.69:5000/hoover-bot:$TAG,push=true,registry.insecure=true"
sed -i "s|newTag:.*|newTag: $TAG|" deploy/k3s/kustomization.yaml
kubectl apply -k deploy/k3s
kubectl -n hoover-bot rollout status deploy/hoover-bot --timeout=180s
```
