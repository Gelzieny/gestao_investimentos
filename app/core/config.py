from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file='.env', extra='ignore')
  
  DATABASE_TYPE: str = "POSTGRES"
  POSTGRES_PRODUCAO_DB: str
  POSTGRES_PRODUCAO_USER: str
  POSTGRES_PRODUCAO_HOST: str
  POSTGRES_PRODUCAO_PORT: int
  POSTGRES_PRODUCAO_PASSWORD: str

  TOKEN_SECRET: str

  
settings = Settings()