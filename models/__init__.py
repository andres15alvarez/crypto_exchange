from .user import User
from utils.database import db


db.generate_mapping(create_tables=False)