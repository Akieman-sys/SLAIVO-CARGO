from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    supabase_db_user: str
    supabase_db_password: str
    supabase_db_host: str
    supabase_db_port: int
    supabase_db_name: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()