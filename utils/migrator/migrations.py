from os import listdir
from os.path import join
from typing import List
from pony.orm import Database, db_session
from pony.orm.dbapiprovider import ProgrammingError
from settings import BASE_DIR
from .migration_table import check_migration_table, create_migration_table


def check_migrations_completed(db: Database) -> List[str]:
    query = """
        SELECT name FROM public."migration";
    """
    try:
        with db_session:
            cursor = db.execute(query)
    except ProgrammingError:
        create_migration_table(db)
        with db_session:
            cursor = db.execute(query)
            return [name[0] for name in cursor.fetchall()]
    else:
        return [name[0] for name in cursor.fetchall()]

def get_migrations_to_migrate(db: Database) -> List[str]:
    files = listdir(join(BASE_DIR, "models", "migrations"))
    files.remove("__init__.py")
    files.remove("__pycache__")
    files = [f.replace(".py", "") for f in files if f.replace(".py", "") not in check_migrations_completed(db)]
    return files