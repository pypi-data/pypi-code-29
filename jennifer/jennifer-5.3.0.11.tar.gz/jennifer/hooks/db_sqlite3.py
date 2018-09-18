from jennifer.wrap import db_api
from jennifer.agent import jennifer_agent
__hooking_module__ = 'sqlite3'


def connection_info(database, *args, **kwargs):
    return 'localhost', 0, database


def hook(sqlite3):
    db_api.register_database(sqlite3.dbapi2, connection_info)
