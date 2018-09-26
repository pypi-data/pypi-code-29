# -*- coding:utf-8 -*-
import sys
import pymysql.cursors
import Queue
import time
import threading
import traceback
import copy
import logging

FORMAT_LIMIT = 500


class DB:

    def __init__(self, conn_info=None, max_cached=5, idle_time=300):
        self._conn_info = conn_info
        if not self._conn_info:
            logging.error('need connection information')
            sys.exit(1)
        for k in ['host', 'user', 'password', 'db']:
            if k not in self._conn_info:
                logging.error('need %s configuration' % k)
                sys.exit(1)
        #
        self._max_cached = min(max_cached, 20)
        self._max_cached = max(self._max_cached, 1)
        self._idle_time = max(idle_time, 300)
        self._idle_time = min(self._idle_time, 1800)
        self.pool = Queue.Queue(maxsize=self._max_cached)
        # check pool
        t = threading.Thread(target=self._check_pool)
        t.setDaemon(True)
        t.start()
        #
        self._create_count = 0
        self._full_count = 0
        self._idle_count = 0
        self._closed_count = 0
        self._last_count_info = {}

    def _create_conn(self):
        conn = None
        try:
            self._create_count += 1
            logging.debug('create connection')
            conn = pymysql.connect(host=self._conn_info['host'],
                                   user=self._conn_info['user'],
                                   password=self._conn_info['password'],
                                   db=self._conn_info['db'],
                                   charset=self._conn_info['charset'],
                                   cursorclass=pymysql.cursors.DictCursor)
        except:
            logging.error(traceback.format_exc())
        return conn

    def get_conn(self):
        try:
            return self.pool.get_nowait()[0]
        except Queue.Empty:
            return self._create_conn()
        except:
            logging.error(traceback.format_exc())
            return self._create_conn()

    def recycle(self, conn):
        if not conn:
            return
        try:
            self.pool.put_nowait((conn, time.time()))
        except Queue.Full:
            self._full_count += 1
            conn.close()
        except:
            conn.close()
            logging.error(traceback.format_exc())

    def _check_pool(self):
        while True:
            time.sleep(10)
            self._check_alive()
            count_info = {'create count': self._create_count,
                          'full count': self._full_count,
                          'idle count': self._idle_count,
                          'closed count': self._closed_count}
            if count_info != self._last_count_info:
                logging.debug(count_info)
            self._last_count_info = copy.deepcopy(count_info)

    def _check_alive(self):
        try:
            conn, last_time = self.pool.get_nowait()
        except Queue.Empty:
            return
        try:
            conn.ping(reconnect=False)
            if time.time() - last_time > self._idle_time:
                self._idle_count += 1
                conn.close()
                logging.debug('remove a connection idle more than %ss' % self._idle_time)
            else:
                try:
                    self.pool.put_nowait((conn, last_time))
                except Queue.Full:
                    self._full_count += 1
                    conn.close()
        except pymysql.err.Error:
            self._closed_count += 1
            logging.error(traceback.format_exc())
            logging.debug('remove a closed connection')
        except:
            logging.error(traceback.format_exc())

    def fetchall(self, sql, data=()):
        ret = []
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                if not data:
                    cur.execute(sql)
                else:
                    cur.execute(sql, data)
                ret = cur.fetchall()
            conn.commit()
        except:
            raise
        finally:
            self.recycle(conn)
        return ret

    def fetchone(self, sql, data=()):
        ret = None
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                if not data:
                    cur.execute(sql)
                else:
                    cur.execute(sql, data)
                ret = cur.fetchone()
            conn.commit()
        except:
            raise
        finally:
            self.recycle(conn)
        return ret

    def fetchmany(self, sql, num, data=()):
        ret = None
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                if not data:
                    cur.execute(sql)
                else:
                    cur.execute(sql, data)
                ret = cur.fetchmany(num)
            conn.commit()
        except:
            raise
        finally:
            self.recycle(conn)
        return ret

    def execute(self, sql, data=()):
        ret = False
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                if not data:
                    cur.execute(sql)
                else:
                    cur.execute(sql, data)
            conn.commit()
            ret = True
        except:
            raise
        finally:
            self.recycle(conn)
        return ret

    def executemany(self, sql, data_list):
        ret = False
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                cur.executemany(sql, data_list)
            conn.commit()
            ret = True
        except:
            raise
        finally:
            self.recycle(conn)
        return ret
