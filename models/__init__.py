from .user import User
from .currency import Currency
from .transaction import Transaction
from .account import Account
from utils.database import db


db.generate_mapping(check_tables=False, create_tables=False)
