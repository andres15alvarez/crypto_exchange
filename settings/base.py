import os
from pathlib import Path
import dotenv


dotenv.load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.environ.get('ENV' 'development')
DEBUG = eval(os.environ.get('DEBUG', 'True'))
SECRET_KEY = os.environ.get('SECRET_KEY')
PORT = int(os.environ.get('PORT', '5000'))

# Database
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')


TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')