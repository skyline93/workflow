from pathlib import Path
from typing import Any

import toml
from pydantic import BaseModel, BaseSettings


class AppItems(BaseModel):
    home: str
    pyenv: str
    postgres_uri: str


class ScriptItems(BaseModel):
    sql_dir: str


class Settings(BaseSettings):
    app: AppItems
    script: ScriptItems

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                toml_config_settings_source,
                env_settings,
                file_secret_settings,
            )


def toml_config_settings_source(settings: BaseSettings) -> dict[str, Any]:
    encoding = settings.__config__.env_file_encoding
    return toml.loads(Path("config.toml").read_text(encoding))


settings = Settings()
