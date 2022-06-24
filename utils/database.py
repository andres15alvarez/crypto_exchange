from pony import orm
import settings


db = orm.Database(
    provider="postgres",
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    database=settings.DATABASE_NAME,
)
