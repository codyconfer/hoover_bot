import logging
from pydantic import BaseSettings


class _Config(BaseSettings):
    TOKEN: str

    class Config:
        env_file = ".env"


CONFIG = _Config()


def configure_logging(name=None) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s |  %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    return logging.getLogger(name)
