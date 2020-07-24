import os

env_settings = os.getenv("APP_ENV_SETTINGS")

if env_settings is None:
    raise Exception("settings for app not exported: example: ```export APP_ENV_SETTINGS=dev```")

if env_settings == "DEVELOPMENT":
    from app.core.settings.dev_settings import DevSettings
    settings = DevSettings()

if env_settings == "PRODUCTION":
    from app.core.settings.prod_settings import ProdSettings
    settings = ProdSettings()

print(settings)
