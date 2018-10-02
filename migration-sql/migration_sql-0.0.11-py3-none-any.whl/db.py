import logging
import subprocess
from contextlib import contextmanager
from typing import Optional

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from .schema_version import SchemaVersion
from .version import Version

log = logging.getLogger("ww.migration")


class DB(object):
    """

    Provides utility method to interact with the database server, including:

    - read/write the schema table in the *main* database (that is specified when instantiating the object)
    - drop other databases if necessary
    - kill process
    - use mysqldump to duplicate database

    The user and password used to instantiate this class should have enough rights to do all the above actions.

    """

    def __init__(self, host, port, username, password, name):
        """
        Instantiate the object given the database server information and
        the main database (i.e. object of the migration process)

        :param host: server host
        :param port: server port
        :param username: server username
        :param password: server password
        :param name: database name
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.name = name

        self._init_db()

    def _init_db(self):
        """
        Create database if not exist.
        Create the schema_version table that records all applied versions if not exist.
        """
        if not self._exist_database():
            log.debug("database not exist, create an empty database %s", self.name)
            self._create_database()

        if not self._exist_table("schema_version"):
            log.debug("schema_version not exist, create table schema_version")
            self._create_schema_version_table()

    @contextmanager
    def get_session(self):
        """
        Get the SQLAlchemy session to the database and close the connections after.
        """
        db_url = f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}?charset=utf8mb4"
        engine = create_engine(db_url, pool_recycle=3600)
        session_maker = scoped_session(sessionmaker(bind=engine, autocommit=False))
        session = session_maker()

        try:
            yield session
        finally:
            session.rollback()
            session.close()
            session_maker.remove()
            engine.dispose()

    def get_versions_to_apply(self, all_versions: [Version]) -> [Version]:
        """return what versions that should be applied to this db"""
        current_version = self._get_current_version()
        if not current_version:
            current_version_index = -1  # apply all versions
        else:
            current_version_indexes = [i for i in range(len(all_versions)) if
                                       all_versions[i].version_code == current_version]
            if len(current_version_indexes) != 1:
                raise Exception(
                    f"""the current version {current_version} must appear once and only 
                    once the schema version table. 
                    It appears {len(current_version_indexes)} times""")

            current_version_index = current_version_indexes[0]

        to_apply_versions = all_versions[current_version_index + 1:]
        return to_apply_versions

    def clean_dbs_with_names(self, names):
        """delete all the databases whose name match with names"""

        def match_name(db_name):
            for name in names:
                if name in db_name:
                    return True

            return False

        with self.get_session() as session:
            db_names = [_[0] for _ in session.execute("show databases").fetchall()]

            for db_name in db_names:
                if match_name(db_name):
                    log.info("drop db %s", db_name)
                    session.execute(f"drop database if EXISTS {db_name}")

    def duplicate(self, clone_name):
        """duplicate database content to another database using mysqldump"""
        db_connection = self.get_db_connection_command_line()

        with self.get_session() as session:
            session.execute(f"create database {clone_name} DEFAULT CHARACTER SET = utf8mb4")

        # copy data from original database to backup database
        duplicate_command = f"""mysqldump --routines --events --triggers --single-transaction \
        {db_connection} {self.name} \
        |mysql {db_connection} {clone_name}"""

        subprocess.check_output(duplicate_command, shell=True)

    def kill_all_process(self):
        """kill all the process that are currently using the database
        except the current one (which is also closed at the end)"""
        with self.get_session() as session:
            current_process = session.execute("select CONNECTION_ID();").fetchone()[0]
            session.execute("use information_schema;")

            # list of tuple of (process id, database used by the process)
            # for ex
            # [(168, 'information_schema'), (5, None), (4, None), (3, None), (2, None), (1, None)]
            all_process_on_current_db_query = session \
                .execute(f'SELECT ID, DB from PROCESSLIST where DB="{self.name}";') \
                .fetchall()

            # Kill only process that work on the current database
            all_process_on_current_db = [_[0] for _ in all_process_on_current_db_query]

            log.debug("current process:%s, all_process_on_current_db:%s", current_process, all_process_on_current_db)

            to_kill = [p for p in all_process_on_current_db if p != current_process]
            log.debug("gonna kill %s", to_kill)

            for process in to_kill:
                log.debug("kill process:%s", process)
                try:
                    session.execute(f"kill {process}")
                except Exception:
                    log.warning("cannot kill %s", process)

            log.debug("finish kill")

    def drop(self):
        """drop the current database"""
        self.kill_all_process()
        db_connection = self.get_db_connection_command_line()
        drop_db_command = f'mysqladmin {db_connection} -f drop {self.name}'
        subprocess.check_output(drop_db_command, shell=True)
        log.debug("drop %s success", self.name)

    def get_db_connection_command_line(self):
        """return the connection args to use with mysql command"""
        return f"-u{self.username} -p{self.password} -h{self.host} -P{self.port}"

    def _exist_database(self) -> bool:
        """Return whether the database exists"""
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.username,
                                     password=self.password)

        query = f"""SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA
        WHERE SCHEMA_NAME = "{self.name}"
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.rowcount == 1
        finally:
            connection.commit()
            connection.close()

    def _create_database(self, encoding="utf8mb4"):
        """Create the database, preferably after checking its existance with `exist_database`"""
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.username,
                                     password=self.password)

        query = f"""CREATE DATABASE `{self.name}` 
                DEFAULT CHARACTER SET = `{encoding}`;"""

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
        finally:
            connection.commit()
            connection.close()

    def _exist_table(self, table_name) -> bool:
        """Return whether a specific table exists"""
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.username,
                                     password=self.password)

        query = f"""SELECT TABLE_SCHEMA 
FROM information_schema.tables
WHERE table_schema = '{self.name}' 
    AND table_name = '{table_name}'
LIMIT 1;"""

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.rowcount == 1
        finally:
            connection.commit()
            connection.close()

    def _create_schema_version_table(self):
        """Create the schema_version table necessary for the migration,
        preferably after checking its existance with `exist_table`"""
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.username,
                                     password=self.password,
                                     db=self.name
                                     )

        query = f"""CREATE TABLE `schema_version` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `creation_datetime` datetime DEFAULT current_timestamp(),
  `modification_datetime` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `version_code` varchar(256) NOT NULL,
  `comment` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
        finally:
            connection.commit()
            connection.close()

    def _get_current_version(self) -> Optional[str]:
        with self.get_session() as session:
            schema_version = session.query(SchemaVersion).order_by(SchemaVersion.id.desc()).first()
            return schema_version.version_code if schema_version else None

    def __repr__(self):
        return f"<Database {self.host}:{self.port}/{self.name}>"
