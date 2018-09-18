# coding: utf-8
from oslo_config import cfg
from pymongo import MongoClient

CONF = cfg.CONF

opts = [
    cfg.StrOpt("ip",
               help="IP address of mongodb."),
]
CONF.register_opts(opts, group="mongodb")


def get_client(database, collection):
    return Client(database, collection)


class Client(object):
    def __init__(self, database, collection):
        conn = MongoClient(CONF.mongodb.ip, 27017)
        db = getattr(conn, database)
        self.client = getattr(db, collection)

    def insert(self, values):
        self.client.insert(values)
