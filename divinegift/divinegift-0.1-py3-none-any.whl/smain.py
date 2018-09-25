from logger import log_info
from sqlalchemy import create_engine, MetaData, Table
from string import Template
import json
import sys


class Settings:
    def __init__(self):
        self.settings = {}

    def get_settings(self):
        return self.settings

    def set_settings(self, json_str):
        self.settings = json_str

    def parse_settings(self, file='./settings.conf'):
        json_file = open(file)
        json_str = json_file.read()
        json_data = json.loads(json_str)

        dict_c = dict_compare(self.settings, json_data)
        added, removed, modified, same = dict_c.values()
        if len(added) > 0:
            for r in list(added):
                log_info('Added {}: {}'.format(r, json_data.get(r)))
        if len(removed) > 0:
            for r in list(removed):
                log_info('Removed {}: {}'.format(r, self.settings.get(r)))
        if len(modified) > 0:
            for r in list(modified):
                log_info('Modified {}: {} -> {}'.format(r, modified.get(r)[0], modified.get(r)[1]))

        self.set_settings(json_data)


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d2_keys - d1_keys
    removed = d1_keys - d2_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])

    result = {'added': added, 'removed': removed, 'modified': modified, 'same': same}
    return result


def get_conn(db_conn):
    """
    Create connection for SQLAlchemy
    :param db_conn: DB connection (user, password, host, port, db_name)
    :return: Engine, Connection, Metadata
    """
    engine = create_engine('{dialect}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'.format(**db_conn))
    conn = engine.connect()
    metadata = MetaData()
    return engine, conn, metadata


def get_raw_conn(db_conn):
    engine = create_engine('{dialect}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'.format(**db_conn))
    conn = engine.raw_connection()
    return conn


def close_conn(conn):
    conn.close()


def get_sql(filename):
    """
    Get sql string from file
    :param filename: File name
    :return: String with sql
    """
    file = open(filename, 'r')
    sql = file.read()
    file.close()
    return sql


def get_data(sql, db_conn, **kwargs):
    """
    Get raw aims data
    :param sql: File with sql which need to execute
    :param db_conn: DB connect creditions
    :param kwargs: List with additional data
    :return: Dictionary
    """
    #log_info('Get aims data from ' + sql)
    script_t = Template(get_sql(sql))
    script = script_t.safe_substitute(**kwargs)
    #print(script)

    engine, conn, metadata = get_conn(db_conn)
    res = conn.execute(script)
    ress = [dict(row.items()) for row in res]
    close_conn(conn)

    return ress


def run_script(sql, db_conn, **kwargs):
    """
    Run custom script
    :param sql: File with sql which need to execute
    :param db_conn: DB connect creditions
    :param kwargs: List with additional data
    :return: None
    """
    script_t = Template(get_sql(sql))
    script = script_t.safe_substitute(**kwargs)

    engine, conn, metadata = get_conn(db_conn)
    conn.execute(script)
    close_conn(conn)


def get_args():
    args = sys.argv[1:]
    args_d = {}
    for i, arg in enumerate(args[::2]):
        if i == len(args):
            break
        args_d[arg] = args[i * 2 + 1]
    
    return args_d


def get_log_param(args):
    log_level = None
    log_name = None
    for key in args.keys():
        if key in ['--log_level', '-ll']:
            log_level = args.get(key)
        if key in ['--log_name', '-ln']:
            log_name = args.get(key)

    if not log_level:
        log_level = 'INFO'
    if not log_name:
        log_name = None

    return log_level, log_name


if __name__ == '__main__':
    pass
