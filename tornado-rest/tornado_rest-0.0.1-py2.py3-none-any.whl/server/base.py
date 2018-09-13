#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : base.py
# @Date : 2018/9/4 10:10
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import sys
import tornado.web
from tornado_rest.db import pool
from tornado_rest.common import config
from tornado_rest.common.config import CONF


def initialize_database():
    pool.POOL.refresh(param={'connection': CONF.db.connection,
                             'pool_size': CONF.db.pool_size,
                             'pool_recycle': CONF.db.pool_recycle,
                             'pool_timeout': CONF.db.pool_timeout,
                             'max_overflow': CONF.db.max_overflow}, connecter='psycopg2')


def initialize_logger():
    pass


def initialize_config():
    config.setup()


def initialize_application(api):
    for name in config.CONF.application.names:
        if name:
            __import__(name)
            app = sys.modules[name]
            app.route.add_routes(api)


def initialize_server():
    initialize_config()
    initialize_logger()
    initialize_database()
    api = Application()
    initialize_application(api)
    return api


class Application(tornado.web.Application):
    def __init__(self):
        self.settings = dict()
        self.handlers = []
        self.debug = CONF.debug
        tornado.web.Application.__init__(self, debug=self.debug, handlers=self.handlers, **self.settings)

    def add_route(self, uri_template, resource, *args, **kwargs):
        self.handlers.append((uri_template, resource))
        self.add_handlers(host_pattern=CONF.server.ip, host_handlers=self.handlers)


application = initialize_server()
