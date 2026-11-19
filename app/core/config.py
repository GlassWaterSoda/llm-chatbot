
from typing import Literal

from pydantic import SecretStr, Field
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

    openai_api_key: SecretStr | None = Field(
        default=None,
        validation_alias="OPENAI_API_KEY"
    )

    openai_model: str = "mock"


settings = Settings()
