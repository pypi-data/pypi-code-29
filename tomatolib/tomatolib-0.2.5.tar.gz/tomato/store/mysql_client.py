#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      mysql_client.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    tangmi(tangmi360@gmail.com)
    @date:      June 11, 2018
    @desc:      MySQL storage access class
"""

import logging
import asyncio
import aiomysql


class MySQLClient(object):

    async def _create_pool(self, **kwargs):
        self._host = kwargs.get('host', 'localhost')
        self._port = kwargs.get('port', 3306)
        self._user = kwargs.get('user')
        self._passwd = kwargs.get('passwd')
        self._db = kwargs.get('db')
        self._minsize = kwargs.get('minsize', 5)
        self._maxsize = kwargs.get('maxsize', 5)
        self._charset = kwargs.get('charset', 'utf8')
        self._autocommit = kwargs.get('autocommit', True)

        loop = asyncio.get_event_loop()
        self._pool = await aiomysql.create_pool(host=self._host,
                                                port=self._port,
                                                user=self._user,
                                                password=self._passwd,
                                                db=self._db,
                                                minsize=self._minsize,
                                                maxsize=self._maxsize,
                                                charset=self._charset,
                                                autocommit=self._autocommit,
                                                loop=loop)
        async with self._pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1;")
                (r,) = await cur.fetchone()
                assert r == 1
                logging.info('mysql connection success: mysql://%s:%s'
                             ';charset=%s, db[%s] autocommit[%s] '
                             'minsize[%s] maxsize[%s]',
                             self._host, self._port, self._charset,
                             self._db, self._autocommit,
                             self._minsize, self._maxsize)

    def __init__(self, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._create_pool(**kwargs))

    async def close(self):
        if hasattr(self, '_pool'): # TODO 临时方案，待资源管理重构后处理
            self._pool.close()
            await self._pool.wait_closed()

    async def find(self, sql, params=None, size=0):
        """find
        """
        async with self._pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                if params:
                    await cur.execute(sql, params)
                else:
                    await cur.execute(sql)
                if size:
                    rows = await cur.fetchmany(size)
                else:
                    rows = await cur.fetchall()
                return rows

    async def execute(self, sql, params=None, autocommit=True):
        """execute
        """
        async with self._pool.acquire() as conn:
            if not autocommit:
                await conn.begin()
            try:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    if params:
                        await cur.execute(sql, params)
                    else:
                        await cur.execute(sql)
                    affected = cur.rowcount
                if not autocommit:
                    await conn.commit()
            except BaseException as e:
                if not autocommit:
                    await conn.rollback()
                raise
            return affected
