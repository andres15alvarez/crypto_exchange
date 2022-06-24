from datetime import datetime
from pony import orm
from utils.database import db


class User(db.Entity):
    __table__ = "user"

    active = orm.Required(bool, default=True)
    first_name = orm.Optional(str, max_len=50)
    last_name = orm.Optional(str, max_len=255)
    email = orm.Required(str, max_len=255, unique=True)
    password = orm.Optional(str, max_len=255)
    created_at = orm.Required(datetime, default=datetime.now)
    # updated_at = orm.Required(datetime, default=datetime.now)
    # deleted_at = orm.Optional(datetime)
