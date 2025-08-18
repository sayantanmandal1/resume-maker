import os
from pydantic import BaseModel

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg://resume:resume@db:5432/resumelab")
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "devsecret")
    BUILD_DIR: str = os.getenv("BUILD_DIR", "/app/build")

settings = Settings()
