from pony.orm import Database
import utils.database as database


def migrate(db: Database):
    query = """
        CREATE TABLE IF NOT EXISTS public."currency"
        (
            id serial NOT NULL,
            name character varying(100) NOT NULL,
            symbol character varying(10) NOT NULL UNIQUE,
            CONSTRAINT currency_pkey PRIMARY KEY (id)
        );
    """

    db.execute(query)
    db.commit()


if __name__ == "__main__":
    migrate(database.db)
