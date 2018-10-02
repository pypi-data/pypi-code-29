from eqi_utils.config import keys
from eqi_utils.config.config import EQI_CONFIG
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import warnings
import cx_Oracle


class DBConnection:
    def __init__(self):
        self._engine = None
        self._session = None
        self._dbase = None

    def get_engine(self, recreate=False):
        if self._engine and not recreate:
            return
        username = EQI_CONFIG.get_mandatory(keys.DB_USER)
        password = EQI_CONFIG.get_optional(keys.DB_PASSWORD, None)
        if password is None:
            password = input('Please input db password')
        db_name = EQI_CONFIG.get_optional(keys.DB_NAME, 'RESLIVESRV')
        try:
            self._engine = create_engine(
                r'oracle+cx_oracle://{}:{}@{}'.format(username, password,
                                                      db_name))
        except cx_Oracle.DatabaseError:
            warnings.warn(
                "DB connection cannot be established. "
                "You will not be able to use DB related features.")
        return self._engine

    def get_session(self, recreate=True):
        if self._session and not recreate:
            return self._session
        self.get_engine()
        if self._engine is None:
            return None
        else:
            session_type = sessionmaker(bind=self._engine)
            self._session = session_type()
            return self._session

    def get_declarative_base(self, recreate=False):
        if self._dbase and not recreate:
            return self._dbase
        self.get_engine()
        if self._engine is None:
            return None
        else:
            self._dbase = declarative_base(bind=self._engine)
            return self._dbase


DB_CONNECTION = DBConnection()
