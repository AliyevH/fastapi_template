from starlette.config import Config
from starlette.datastructures import Secret
from app.core.settings.base_settings import BaseConfig


class ProdSettings(BaseConfig):
    """
    Production configuration class
    """

    config = Config()

    DB_USER = config("DB_USER", cast=str, default="postgres")
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default="postgres")
    DB_HOST = config("DB_HOST", cast=str, default="db")
    DB_PORT = config("DB_PORT", cast=int, default=5432)
    DB_NAME = config("DB_NAME", cast=str, default=BaseConfig.project_name)

    DATABASE_URL = config(
        "SQLALCHEMY_DATABASE_URL",
        default=f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )


