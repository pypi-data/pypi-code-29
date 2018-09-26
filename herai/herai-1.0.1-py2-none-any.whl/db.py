import sqlite3
import os


def setup_database():
    conn = sqlite3.connect(
        os.path.dirname(os.path.realpath(__file__)) + '/../brain.db')
    c = conn.cursor()
    # c.execute(
    # 'CREATE TABLE messages(
    # message_id
    # INTEGER PRIMARY KEY, input varchar(360), output varchar(360))')
    conn.commit()

    return conn
