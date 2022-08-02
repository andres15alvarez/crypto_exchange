from pony.orm import Database
import utils.database as database


def migrate(db: Database):
    query = """
        CREATE TABLE IF NOT EXISTS public."account"
        (
            id serial NOT NULL,
            "user" integer NOT NULL,
            currency integer NOT NULL,
            amount numeric(20, 10) NOT NULL,
            created_at timestamp,
            CONSTRAINT account_pkey PRIMARY KEY (id),
            CONSTRAINT account_user_fkey FOREIGN KEY ("user") REFERENCES public."user"(id),
            CONSTRAINT account_currency_fkey FOREIGN KEY (currency) REFERENCES public."currency"(id)
        );
    """

    db.execute(query)
    db.commit()


if __name__ == "__main__":
    migrate(database.db)
