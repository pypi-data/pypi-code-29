from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData, create_engine


class Database:
    """ Class used for manage the database """

    def __init__(self, url: str, tables: dict = None, echo: bool = False):
        """
        Args:
            url (str): url (str): the url to connect to (ex.: postgresql://scott:tiger@localhost:5432/mydatabase)
            tables (Dict[str, Table]): use for add table on the db object
            echo (bool): when he is activate all query will be print on screen
        """
        self._engine = create_engine(url, echo=echo)
        self._metadata = MetaData(bind=self._engine)
        self._session = scoped_session(sessionmaker(bind=self._engine))

        if tables:
            for name, table in tables.items():
                setattr(self, name, table(self))

    def echo_turn_on(self):
        """ Turn on the echo mod for print request/query """

        self._engine.echo = True

    def echo_turn_off(self):
        """ Turn off the echo mod for print request/query """

        self._engine.echo = False

    def get_echo_status(self) -> bool:
        """ Gets the status of the echo mod

        Return:
            bool
        """

        return self._engine.echo

    def get_session(self) -> scoped_session:
        """ Gets the scopped session

        Return:
            scoped_session
        """

        return self._session()

    def remove_session(self):
        """ Removes the session """

        self._session.remove()

    def commit(self):
        """ Commit the session """

        self.get_session().commit()

    def save(self, obj):
        """
        Save an object in database

        Args:
            obj (object): the object to save
        """

        session = self.get_session()
        session.add(obj)

        session.flush()

    def setup_all(self):
        """ Creates all tables """

        self._metadata.create_all()

    def truncate_tables(self):
        """ Truncates all tables """

        #  The session is committed to prevent potential query still here/alive (in a db transaction).
        self.commit()

        with self.contextual_session() as session:
            for table in self._metadata.sorted_tables:
                session.execute(f"TRUNCATE TABLE {table.name}")

    @contextmanager
    def contextual_session(self) -> Generator[scoped_session, None, None]:
        """ A simple contextmanager wich contain the session logic

        Ex:
            with database.contextual_session() as session:
                session.wat_you_want

        Retuns:
            Generator[scoped_session, None, None]
        """

        session = self._session

        yield session

        session.commit()
        session.remove()
