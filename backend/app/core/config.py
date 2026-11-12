from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI SupportOps"
    database_url: str = ""
    jwt_secret: str = "change-me"
    llm_mode: str = "mock"
    gemini_api_key: str = ""
    cors_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()