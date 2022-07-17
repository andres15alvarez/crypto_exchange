from pony.orm import Database
import utils.database as database


def migrate(db: Database):
    query = """
        CREATE TABLE IF NOT EXISTS public."transaction"
        (
            id serial NOT NULL,
            "user" integer NOT NULL,
            from_currency integer NOT NULL,
            to_currency integer NOT NULL,
            exchange_rate numeric(20, 10) NOT NULL,
            quantity numeric(20, 10) NOT NULL,
            created_at timestamp,
            CONSTRAINT transaction_pkey PRIMARY KEY (id),
            CONSTRAINT transaction_user_fkey FOREIGN KEY ("user") REFERENCES public."user"(id),
            CONSTRAINT transaction_from_currency_fkey FOREIGN KEY (from_currency) REFERENCES public."currency"(id),
            CONSTRAINT transaction_to_currency_fkey FOREIGN KEY (to_currency) REFERENCES public."currency"(id)
        );
    """

    db.execute(query)
    db.commit()


if __name__ == "__main__":
    migrate(database.db)
