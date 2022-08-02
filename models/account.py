from datetime import datetime
from decimal import Decimal
from pony import orm
from models.currency import Currency
from models.user import User
from utils.database import db


class Account(db.Entity):
    """This model represent the account of the user in a specific currency."""

    __table__ = "account"

    user = orm.Required(User)
    currency = orm.Required(Currency)
    amount = orm.Required(Decimal, precision=20, scale=10)
    created_at = orm.Required(datetime, default=datetime.now)
