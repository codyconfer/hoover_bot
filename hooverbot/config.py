import logging
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Config(BaseSettings):
    TOKEN: str

    model_config = SettingsConfigDict(env_file=".env")


CONFIG = _Config()


def configure_logging(name=None) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    return logging.getLogger(name)
