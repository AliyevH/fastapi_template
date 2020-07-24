from starlette.config import Config
from app.core.settings.base_settings import BaseConfig


class DevSettings(BaseConfig):
    """
    Development configuration class
    """

    config = Config()

    DEBUG = config("DEBUG", cast=bool, default=True)

    DATABASE_URL = config(
        "SQLALCHEMY_DATABASE_URL",
        default="sqlite:///app.db"
    )
