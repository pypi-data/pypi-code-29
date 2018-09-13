import sqlite3
import re
from enum import Enum
from ghostbot import StatusCode
from ghostbot.core import Basis
from ghostbot.utils.os import Hash, FileSystem as fs


class RDBMS(Enum):
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    SQLITE = "sqlite"


class Database(Basis):
    SQL_COMMENT = "--"

    def __init__(self, rdbms):
        super().__init__()
        self._rdbms = rdbms
        self._sql = {}

    def open(self, dsn, auto_commit=True):
        result = None
        try:
            if self._rdbms == RDBMS.MYSQL:
                pass
            elif self._rdbms == RDBMS.POSTGRESQL:
                pass
            elif self._rdbms == RDBMS.SQLITE:
                isolation = None if auto_commit else "EXCLUSIVE"
                connection = sqlite3.connect(dsn, isolation_level=isolation)
                result = Connection(self._rdbms, connection)
        except Exception as e:
            self.critical(StatusCode[310], e.args)
        return result

    def load(self, sql_file):
        result = None
        key = Hash.digest(sql_file, digit=8)
        if key not in self._sql:
            if fs.exists(sql_file):
                sql = []
                with open(sql_file) as file:
                    for line in file:
                        pos = line.find(self.SQL_COMMENT)
                        if pos != -1:
                            line = line[:pos]
                        line = line.strip()
                        if len(line) > 0:
                            sql.append(line)
                result = " ".join(sql).strip()
                result = re.sub("\s{2,}", " ", result)
                if ";" in result:
                    result = [x.strip() for x in result.split(";") if len(x.strip()) > 0]
                    if len(result) == 1:
                        result = result[0]
                self._sql[key] = result
            else:
                self.error(StatusCode[311], sql_file)
        else:
            result = self._sql[key]
        return result


class Connection(Basis):

    def __init__(self, rdbms, connection):
        super().__init__()
        self._rdbms = rdbms
        self._connection = connection
        self._connection.row_factory = sqlite3.Row
        self._cursors = []

    def begin(self):
        if self._connection:
            try:
                if self._rdbms == RDBMS.MYSQL:
                    pass
                elif self._rdbms == RDBMS.POSTGRESQL:
                    pass
                elif self._rdbms == RDBMS.SQLITE:
                    self._connection.execute("BEGIN TRANSACTION")
            except Exception as e:
                self.critical(StatusCode[321], e.args)
        else:
            self.error(StatusCode[320])

    def cursor(self):
        result = None
        if self._connection:
            try:
                if self._connection:
                    cursor = self._connection.cursor()
                    result = Cursor(self._rdbms, cursor)
                    self._cursors.append(result)
                else:
                    self.error(StatusCode[320])
            except Exception as e:
                self.critical(StatusCode[322], e.args)
        else:
            self.error(StatusCode[320])
        return result

    def commit(self):
        if self._connection:
            try:
                self._connection.commit()
            except Exception as e:
                self.critical(StatusCode[323], e.args)
        else:
            self.error(StatusCode[320])

    def rollback(self):
        if self._connection:
            try:
                self._connection.rollback()
            except Exception as e:
                self.critical(StatusCode[324], e.args)
        else:
            self.error(StatusCode[320])

    def end(self):
        if self._connection:
            try:
                if self._rdbms == RDBMS.MYSQL:
                    pass
                elif self._rdbms == RDBMS.POSTGRESQL:
                    pass
                elif self._rdbms == RDBMS.SQLITE:
                    self._connection.execute("END TRANSACTION")
            except Exception as e:
                self.critical(StatusCode[325], e.args)
        else:
            self.error(StatusCode[320])

    def close(self):
        if self._connection:
            for cursor in self._cursors:
                cursor.close()
            self._cursors.clear()
            try:
                self._connection.close()
                self._connection = None
            except Exception as e:
                self.critical(StatusCode[326], e.args)
        else:
            self.error(StatusCode[320])


class Cursor(Basis):

    def __init__(self, rdbms, cursor):
        super().__init__()
        self._rdbms = rdbms
        self._cursor = cursor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        return True

    def query(self, sql, params=None):
        result = None
        if self._cursor:
            try:
                if params:
                    result = self._cursor.execute(sql, params)
                else:
                    result = self._cursor.execute(sql)
            except Exception as e:
                self.critical(StatusCode[331], e.args)
        else:
            self.error(StatusCode[330])
        return result

    def execute(self, sql, params=None):
        result = None
        if self._cursor:
            try:
                if isinstance(sql, list):
                    for one in sql:
                        if params:
                            self._cursor.execute(one, params)
                        else:
                            self._cursor.execute(one)
                else:
                    if params:
                        self._cursor.execute(sql, params)
                    else:
                        self._cursor.execute(sql)
                result = self._cursor.rowcount
            except Exception as e:
                self.critical(StatusCode[332], e.args)
        else:
            self.error(StatusCode[330])
        return result

    def last_insert_id(self):
        result = None
        if self._cursor:
            try:
                row = self._cursor.execute("SELECT last_insert_rowid()").fetchone()
                result = row[0]
            except Exception as e:
                self.critical(StatusCode[332], e.args)
        return result

    def executes(self, sql, params):
        result = None
        if self._cursor:
            try:
                self._cursor.executemany(sql, params)
                result = self._cursor.rowcount
            except Exception as e:
                self.critical(StatusCode[333], e.args)
        else:
            self.error(StatusCode[330])
        return result

    def close(self):
        if self._cursor:
            try:
                self._cursor.close()
            except Exception as e:
                self.critical(StatusCode[334], e.args)
        else:
            self.error(StatusCode[330])
