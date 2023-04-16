# hoover_bot

> bot for organizing media links on Listen To This

___

## getting started

### setup env

`cp .env_template .env`

`code .env`

- populate values

### running with docker

> for debugging dockerfile
> `docker build -t hoover-bot --progress=plain --no-cache  .`

`docker build -t hoover-bot .`

`docker run --env-file ./.env -d hoover-bot`

### running locally

#### install pyenv

##### [*nix](https://github.com/pyenv/pyenv)

##### [windows](https://github.com/pyenv-win/pyenv-win)

#### install poetry

`pyenv install 3.11`

`pyenv global 3.11`

install [poetry 1.4^](https://python-poetry.org/docs/)

#### run program

`poetry install`

`poetry run python src/main.py`

___

## formatting

to format project, run the following command in the project directory

`poetry run black ./src`

___

## references

### [poetry](https://python-poetry.org/)

*package manager*

### [pydantic](https://docs.pydantic.dev/)

*[used to load environment variables in config](https://docs.pydantic.dev/usage/settings/#dotenv-env-support)*

### [discord.py](https://discordpy.readthedocs.io/en/stable/)

*discord api client and event handler*
