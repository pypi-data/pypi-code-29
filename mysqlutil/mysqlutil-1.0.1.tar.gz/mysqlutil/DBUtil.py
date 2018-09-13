#!/usr/bin/python2

import pymysql.cursors
import Queue
import time
import threading
import traceback
import sys
import copy
import logging

FORMAT_LIMIT = 500


class DB:

    def __init__(self, conn_info=None, max_cached=5, idle_time=300):
        self.conn_info = conn_info
        if not self.conn_info:
            logging.error('need connection information')
            sys.exit(1)
        for k in ['host', 'user', 'password', 'db']:
            if k not in self.conn_info:
                logging.error('need %s configuration' % k)
                sys.exit(1)
        #
        self.max_cached = min(max_cached, 20)
        self.max_cached = max(self.max_cached, 1)
        self.idle_time = max(idle_time, 300)
        self.idle_time = min(self.idle_time, 1800)
        self.pool = Queue.Queue(maxsize=self.max_cached)
        # check pool
        t = threading.Thread(target=self.check_pool)
        t.setDaemon(True)
        t.start()
        #
        self.create_count = 0
        self.full_count = 0
        self.idle_count = 0
        self.closed_count = 0
        self.last_count_info = {}

    def create_conn(self):
        conn = None
        try:
            self.create_count += 1
            logging.debug('create connection')
            conn = pymysql.connect(host=self.conn_info['host'],
                                   user=self.conn_info['user'],
                                   password=self.conn_info['password'],
                                   db=self.conn_info['db'],
                                   charset=self.conn_info['charset'],
                                   cursorclass=pymysql.cursors.DictCursor)
        except:
            logging.error(traceback.format_exc())
        return conn

    def get_conn(self):
        try:
            return self.pool.get_nowait()[0]
        except Queue.Empty:
            return self.create_conn()
        except:
            logging.error(traceback.format_exc())
            return self.create_conn()

    def recycle(self, conn):
        if not conn:
            return
        try:
            self.pool.put_nowait((conn, time.time()))
        except Queue.Full:
            self.full_count += 1
            conn.close()
        except:
            conn.close()
            logging.error(traceback.format_exc())

    def check_pool(self):
        while True:
            time.sleep(10)
            self.check_alive()
            count_info = {'create count': self.create_count,
                          'full count': self.full_count,
                          'idle count': self.idle_count,
                          'closed count': self.closed_count}
            if count_info != self.last_count_info:
                logging.debug(count_info)
            self.last_count_info = copy.deepcopy(count_info)

    def check_alive(self):
        try:
            conn, last_time = self.pool.get_nowait()
        except Queue.Empty:
            return
        try:
            conn.ping(reconnect=False)
            if time.time() - last_time > self.idle_time:
                self.idle_count += 1
                conn.close()
                logging.debug('remove a connection idle more than %ss' % self.idle_time)
            else:
                try:
                    self.pool.put_nowait((conn, last_time))
                except Queue.Full:
                    self.full_count += 1
                    conn.close()
        except pymysql.err.Error:
            self.closed_count += 1
            logging.error(traceback.format_exc())
            logging.debug('remove a closed connection')
        except:
            logging.error(traceback.format_exc())

    def fetchall(self, sql):
        ret = []
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                cur.execute(sql)
                ret = cur.fetchall()
        except:
            logging.error(sql)
            logging.error(traceback.format_exc(FORMAT_LIMIT))
        finally:
            self.recycle(conn)
        return ret

    def fetchone(self, sql):
        ret = None
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                cur.execute(sql)
                ret = cur.fetchone()
        except:
            logging.error(sql)
            logging.error(traceback.format_exc(FORMAT_LIMIT))
        finally:
            self.recycle(conn)
        return ret

    def fetchmany(self, sql, num):
        ret = None
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                cur.execute(sql)
                ret = cur.fetchmany(num)
        except:
            logging.error(sql)
            logging.error(traceback.format_exc(FORMAT_LIMIT))
        finally:
            self.recycle(conn)
        return ret

    def execute(self, sql):
        ret = False
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
            ret = True
        except:
            logging.error(sql)
            logging.error(traceback.format_exc(FORMAT_LIMIT))
        finally:
            self.recycle(conn)
        return ret

    def execute_without_commit(self, sql):
        ret = False
        conn = None
        try:
            conn = self.get_conn()
            with conn.cursor() as cur:
                cur.execute(sql)
            ret = True
        except:
            logging.error(sql)
            logging.error(traceback.format_exc(FORMAT_LIMIT))
        finally:
            self.recycle(conn)
        return ret
