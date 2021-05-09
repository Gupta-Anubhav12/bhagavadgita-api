from fastapi import FastAPI
from pydantic import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    project_name: str = "Bhagavad Gita API"
    admin_email: str = "contact@bhagavadgita.io"
    debug: bool = False

    # Server
    server_name: Optional[str]
    server_host: Optional[str]
    sentry_dsn: Optional[str]
    secret_key: bytes = os.urandom(32)

    class Config:
        env_file = "config.env"


settings = Settings()