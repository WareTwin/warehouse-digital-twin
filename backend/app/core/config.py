from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "WareTwin API"
    app_env: str = "development"
    secret_key: str = "local-development-only"
    database_url: str = "postgresql+psycopg://warehouse:local-only-change-this@localhost:5432/warehouse_twin"
    access_token_expire_minutes: int = 30
    cors_origins: str = "http://localhost:3000"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
