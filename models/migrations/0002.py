from pony.orm import Database
import utils.database as database


def migrate(db: Database):
    query = """
        ALTER TABLE public."user"
        ADD COLUMN created_at timestamp;
    """
    db.execute(query)
    db.commit()


if __name__ == "__main__":
    migrate(database.db)
