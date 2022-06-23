import subprocess
import os
import sys
from pony.orm import Database

from settings.base import BASE_DIR
from .migrations import get_migrations_to_migrate
from .migration_table import save_migration


def migrate(db: Database) -> bool:
    migrations = get_migrations_to_migrate(db)
    for migration in migrations:
        full_path = ".".join(["models", "migrations", migration])
        err = os.system(" -m ".join([sys.executable, full_path]))
        if err != 0:
            print(f"Error with migration {migration}: {err}")
            continue
        if err is None or err == 0:
            print(f"{migration}: OK")
            save_migration(db, migration)
            continue
