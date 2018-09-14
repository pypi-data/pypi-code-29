import logging
import time

import psycopg2
from psycopg2.extensions import TRANSACTION_STATUS_UNKNOWN, TRANSACTION_STATUS_IDLE

logger = logging.getLogger("tap-utils")


class PostgreSQL:
    """
    Connection wrapper which perform re-connect in case if connection was lost
    """

    def __init__(self, db, user, password, host, reconnect_interval=5):
        self.connection_string = "dbname='%s' user='%s' password='%s' host='%s'" % (
            db, user, password, host
        )
        self._connection = None
        self._reconnect_interval = reconnect_interval

    def get_connection(self):
        if not self._connection or self._connection.closed:
            self._init_connection()

        if not self._connection.closed:
            status = self._connection.get_transaction_status()

            if status == TRANSACTION_STATUS_UNKNOWN:
                # close current connection and try to re-connect
                logger.warn("Transaction status unknown. Closing and re-connecting")
                self._connection.close()
                self._init_connection()
            elif status != TRANSACTION_STATUS_IDLE:
                # not idle - error or in transaction
                logger.warn("Transaction in error. Trying to rollback")
                self._connection.rollback()

        return self._connection

    def disconnect(self):
        if self._connection:
            self._connection.close()

    def _init_connection(self):
        while True:
            try:
                self._connection = psycopg2.connect(self.connection_string)
                # select statements are also starting a transactions,
                # we need to avoid this due to long-running essence of the app itself
                self._connection.autocommit = True
                logger.info("Connected successfully")
                return
            except Exception:
                logger.exception("Can't connect to postgres. Trying to re-connect in 5 seconds")
                time.sleep(self._reconnect_interval)
