from pony.orm import Database, db_session
from pony.orm.dbapiprovider import ProgrammingError


def check_migration_table(db: Database) -> bool:
    with db_session:
        query = """
            SELECT * FROM public."migration";
        """
        try:
            db.execute(query)
        except ProgrammingError:
            create_migration_table(db)
        finally:
            return True

def create_migration_table(db: Database):
    with db_session:
        query = """
            CREATE TABLE IF NOT EXISTS public."migration"(
                id serial NOT NULL,
                name VARCHAR(50),
                created_at timestamp DEFAULT now(),
                CONSTRAINT migration_pkey PRIMARY KEY (id)
            );
        """
        db.execute(query)

def save_migration(db: Database, name: str):
    with db_session:
        query = """
            INSERT INTO public."migration" (name) VALUES ($name);
        """
        db.execute(query)
