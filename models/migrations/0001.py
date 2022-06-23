from pony.orm import Database
import utils.database as database


def migrate(db: Database):
    query = """
        CREATE TABLE IF NOT EXISTS public."user"
        (
            id serial NOT NULL,
            first_name character varying(50) COLLATE pg_catalog."default",
            last_name character varying(255) COLLATE pg_catalog."default",
            email character varying(255) COLLATE pg_catalog."default" NOT NULL,
            password character varying(255) COLLATE pg_catalog."default",
            active boolean NOT NULL DEFAULT true,
            CONSTRAINT user_pkey PRIMARY KEY (id)
        );
    """

    db.execute(query)


if __name__ == "__main__":
    migrate(database.db)
