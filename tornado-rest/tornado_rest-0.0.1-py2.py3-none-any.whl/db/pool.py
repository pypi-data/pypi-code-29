#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : pool.py
# @Date : 2018/9/4 14:01
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.


from __future__ import absolute_import

import sqlalchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from tornado_rest.common.config import CONF
from tornado_rest.core import decorators as deco


@deco.singleton
class DBPool(object):

    def __init__(self, param=None, connecter='psycopg2'):
        self._pool = None
        if param:
            self.reflesh(param=param, connecter=connecter)

    def get_session(self):
        if self._pool:
            session = scoped_session(self._pool)
            return session
        raise ValueError('failed to get session')

    def transaction(self):
        if self._pool:
            session = scoped_session(self._pool)
            session.begin()
            return session
        raise ValueError('failed to get session')

    def refresh(self, param, connecter='psycopg2'):
        connection = param['connection']
        enabled_log = CONF.log.level.upper() == 'DEBUG'
        self._pool = sessionmaker(bind=sqlalchemy.create_engine(
            connection,
            echo=enabled_log,
            pool_size=param.get('pool_size', 10),
            pool_recycle=param.get('pool_recycle', 600),
            pool_timeout=param.get('pool_timeout', 15),
            max_overflow=param.get('max_overflow', 10)),
            autocommit=True)
        return True


POOL = DBPool()
