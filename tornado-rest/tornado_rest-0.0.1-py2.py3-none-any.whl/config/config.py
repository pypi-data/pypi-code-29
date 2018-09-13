#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : config.py
# @Date : 2018/9/10 14:37
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

CONFIG_OPTS = {
    'language': 'zh_CN',
    'debug': True,
    'server': {
        'ip': '127.0.0.1',
        'port': 8080,
    },
    'log': {
        'path': '/var/log/project_name/server.log',
        'level': 'INFO',
        'format_string': '%(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s:%(lineno)d [-] %(message)s',
        'date_format_string': '%Y-%m-%d %H:%M:%S',
    },
    'db': {
        'connection': 'postgresql+psycopg2://postgres:@120.77.206.139/ihasy',
        'pool_size': 3,
        'pool_recycle': 60 * 60,
        'pool_timeout': 5,
        'max_overflow': 5,
    },
    'application': {
        'names': [
            'tornado_rest.apps.blog',
        ]
    }
}
