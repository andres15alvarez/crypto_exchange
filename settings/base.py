from datetime import timedelta
import os
from pathlib import Path
import dotenv


dotenv.load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


ENV = os.environ.get("ENV", "testing")
DEBUG = ENV != "production"
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "8f96a1f8ddd71d3a18d71a7a1b5c518ea806e4d6d8d6641c4a4e414d222034cf"
)
PORT = int(os.environ.get("PORT", "5000"))


# Database
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")


TIME_ZONE = os.environ.get("TIME_ZONE", "UTC")


# JWT
JWT_LIFE_TIME = timedelta(hours=int(os.environ.get("JWT_LIFE_TIME", 24)))
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")

COIN_API_KEY = os.environ.get("COIN_API_KEY", "")
