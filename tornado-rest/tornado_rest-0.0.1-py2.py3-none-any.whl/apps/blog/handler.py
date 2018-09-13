#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : handler.py
# @Date : 2018/9/4 13:47
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

from tornado_rest.db.pool import POOL
from tornado_rest.common.base_handler import BaseHandler
from tornado_rest.db.models import IfDatabaseRole


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        session = POOL.get_session()
        query = session.query(IfDatabaseRole)
        self.write_api(query)


class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        session = POOL.get_session()
        query = session.query(IfDatabaseRole)
        self.write_api(query)


class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        session = POOL.get_session()
        query = session.query(IfDatabaseRole)
        self.write_api(query)
