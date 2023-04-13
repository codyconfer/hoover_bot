from pydantic import BaseSettings


class _Config(BaseSettings):
    TOKEN: str

    class Config:
        env_file = '.env'


CONFIG = _Config()
