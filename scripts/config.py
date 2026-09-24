from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ceasa_base_url: str
    user_agent: str
    raw_pdfs_dir: str

    class Config:
        env_file = ".env"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()