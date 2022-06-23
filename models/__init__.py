from .user import User
from utils.database import db


db.generate_mapping(check_tables=False,create_tables=False)