from clustaar.sqlalchemy.database import Database  # NOQA
from tests.fixtures import SubscriptionTable
from os import environ


def create_database(url: str = None, tables: dict = None):

    if "POSTGRES_ENV_POSTGRES_PASSWORD" in environ:
        user = environ["POSTGRES_ENV_POSTGRES_USER"]
        password = environ["POSTGRES_ENV_POSTGRES_PASSWORD"]
        db = environ["POSTGRES_ENV_POSTGRES_DB"]

        addr = environ["POSTGRES_PORT_5432_TCP_ADDR"]
        port = environ["POSTGRES_PORT_5432_TCP_PORT"]

        url = f"postgresql://{user}:{password}@{addr}:{port}/{db}"

    return Database(
        url=(url or "postgresql://localhost:5432/sqlalchemy_test"),
        tables=(tables or {
            "subscriptions": SubscriptionTable
        })
    )
