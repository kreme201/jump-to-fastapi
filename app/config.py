from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

config = Config(".env")

DB_URL = config("DB_URL")
ALEMBIC_URL = config("ALEMBIC_URL") if config("ALEMBIC_URL") else DB_URL
