from datetime import datetime
from decimal import Decimal
from pony import orm
from models.currency import Currency
from models.user import User
from utils.database import db


class Transaction(db.Entity):
    _table_ = "transaction"

    user = orm.Required(User)
    from_currency = orm.Required(Currency, reverse="from_transactions")
    to_currency = orm.Required(Currency, reverse="to_transactions")
    exchange_rate = orm.Required(Decimal, precision=20, scale=10)
    quantity = orm.Required(Decimal, precision=20, scale=10)
    created_at = orm.Required(datetime, default=datetime.now)
