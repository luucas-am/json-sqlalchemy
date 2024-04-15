from os import environ

from dotenv import load_dotenv

APP_ENV = environ.get("APP_ENV")

if APP_ENV == "TEST":
    load_dotenv(".env_test")
else:
    load_dotenv(".env")

DATABASE_URL = environ["DATABASE_URL"]
