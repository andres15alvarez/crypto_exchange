from pony.orm import Database
import utils.database as database


def migrate(db: Database):
    query = """
        CREATE TABLE IF NOT EXISTS public."transaction"
        (
            id serial NOT NULL,
            user_id integer NOT NULL,
            from_currency_id integer NOT NULL,
            to_currency_id integer NOT NULL,
            exchange_rate numeric(20, 10) NOT NULL,
            quantity numeric(20, 10) NOT NULL,
            created_at timestamp,
            CONSTRAINT transaction_pkey PRIMARY KEY (id),
            CONSTRAINT transaction_from_currency_fkey FOREIGN KEY (from_currency_id) REFERENCES public."currency"(id)
            CONSTRAINT transaction_to_currency_fkey FOREIGN KEY (to_currency_id) REFERENCES public."currency"(id)
        );
    """

    db.execute(query)


if __name__ == "__main__":
    migrate(database.db)
