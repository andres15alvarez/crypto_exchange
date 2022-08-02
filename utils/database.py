from pony import orm
import settings

if settings.ENV != 'test':
    db = orm.Database(
        provider="postgres",
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
        host=settings.DATABASE_HOST,
        database=settings.DATABASE_NAME,
    )
else:
    db = orm.Database(
        provider="sqlite",
        filename=":memory:",
        create_db=True
    )
