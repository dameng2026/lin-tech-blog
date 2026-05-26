from pydantic_settings import BaseSettings
import os

env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), ".env")
print(f"Loading .env from: {env_path}")
print(f"File exists: {os.path.exists(env_path)}")

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    VERIFY_CODE_EXPIRE_SECONDS: int = 300
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 52428800
    ENVIRONMENT: str = "development"
    SITE_DOMAIN: str = "http://localhost:8000"

    class Config:
        env_file = env_path

settings = Settings()
print(f"Loaded DATABASE_URL: {settings.DATABASE_URL}")