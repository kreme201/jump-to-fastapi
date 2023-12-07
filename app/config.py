import os

from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

config = Config(".env")

DB_URL = config("DB_URL")
if DB_URL.endswith(".sqlite"):
    DB_URL = "sqlite:///" + os.path.normpath(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), DB_URL)
    )
