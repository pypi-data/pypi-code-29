import pytest

from tests.fixtures.tables import SubscriptionTable, UserTable, Subscription
from clustaar.sqlalchemy.database import Database
from clustaar.sqlalchemy.table import Table
from sqlalchemy.orm.session import Session
from tests.utils import create_database


@pytest.fixture
def subscription():
    return Subscription(type="test", bot_id="0384038493", user_id="97546VCD6")


class TestDatabase():

    def test_init(self):
        database = create_database(tables={"users": UserTable})

        #  bot_idest way to know if database are liked to a db
        assert database._metadata.is_bound()

        assert isinstance(database.users, Table)
        assert isinstance(database.users, UserTable)

    def test_turn_on_echo(self, database):
        assert not database.get_echo_status()

        database.echo_turn_on()

        assert database.get_echo_status()

        database.echo_turn_off()

        assert not database.get_echo_status()

    def test_get_session(self, database):
        session = database.get_session()

        assert isinstance(session, Session)

    def test_commit(self, database, subscription):
        session = database.get_session()

        session.add(subscription)
        database.commit()

        results = database.subscriptions.get()
        assert len(results) == 1
        assert isinstance(results[0], Subscription)

    def test_save(self, database, subscription):
        database.save(subscription)

        results = database.subscriptions.get()
        assert len(results) == 1
        assert isinstance(results[0], Subscription)

    def test_remove_session(self, database, subscription):
        session = database.get_session()

        session.add(subscription)
        database.remove_session()
        database.commit()

        results = database.subscriptions.get()
        assert not len(results)

    def test_contextual_session(self, database, subscription):
        with database.contextual_session() as session:
            session.add(subscription)

        results = database.subscriptions.get()
        assert len(results) == 1
