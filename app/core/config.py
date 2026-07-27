from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    #project info
    project_name : str = Field(default=...,alias="PROJECT_NAME")
    project_version: str = Field(default=...,alias="PROJECT_VERSION")
    debug: bool = Field(default=...,alias="DEBUG")
    #Security
    secret_key: str = Field(default=...,alias="SECRET_KEY")
    algorithm: str = Field(default=...,alias="ALGORITHM")
    token_expire:int = Field(default=...,alias="TOKEN_EXPIRE_MINUTES")

    #Database
    db_url:str = Field(default=...,alias="DB_URL")

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = 'utf-8',
        case_sensitive = False,
    )

settings = Settings()


