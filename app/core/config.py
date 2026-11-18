
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "LLM Chatbot"

    app_env: Literal["development", "testing", "production"] = "development"

    debug: bool = True

    openai_api_key: SecretStr | None = None

    openai_model: str = "mock"


settings = Settings()
