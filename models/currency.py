from pony import orm
from utils.database import db


class Currency(db.Entity):
    __table__ = "currency"

    name = orm.Required(str, max_len=100)
    symbol = orm.Required(str, max_len=10, unique=True)
    from_transactions = orm.Set("Transaction", reverse="from_currency")
    to_transactions = orm.Set("Transaction", reverse="to_currency")
