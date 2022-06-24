if __name__ == "__main__":
    from utils.migrator.migrator import migrate
    from utils.database import db

    migrate(db)
