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
> 
> `docker build -t hoover-bot --progress=plain --no-cache  .`

`docker build -t hoover-bot .`

`docker run --env-file ./.env -d hoover-bot`

___

## formatting

to comply with code standards when developing for this repo.

install and run [black](https://black.readthedocs.io/en/stable/getting_started.html) on `./src`

___

## references

### [black](https://black.readthedocs.io/en/stable/getting_started.html)

*formatter and coding standards*

### [poetry](https://python-poetry.org/)

*package manager*

### [pydantic](https://docs.pydantic.dev/)

*[used to load environment variables in config](https://docs.pydantic.dev/usage/settings/#dotenv-env-support)*

### [discord.py](https://discordpy.readthedocs.io/en/stable/)

*discord api client and event handler*
