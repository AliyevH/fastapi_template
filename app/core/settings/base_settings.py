from starlette.config import Config
from starlette.datastructures import Secret
import os

project_name = "test"


class BaseConfig:
    project_name = "test"

    """
    Base configuration class.
    Subclasses should include configurations for testing,
    development and production environments
    """

    config = Config()

    INCLUDE_SCHEMA = config("INCLUDE_SCHEMA", cast=bool, default=True)

    SECRET_KEY = config("SECRET_KEY", default=os.urandom(32))
    SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO", cast=bool, default=False)
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool, default=False)

    LOGGER_NAME = f"{project_name}_log"
    LOG_FILENAME = "./logs/{project_name}.log"

    # Allow requests from anywhere (But limit it to hosts)
    CORS_ORIGINS = config("CORS_HOSTS", default="*")

    DEBUG = config("DEBUG", cast=bool, default=False)
    TESTING = config("TESTING", cast=bool, default=False)

