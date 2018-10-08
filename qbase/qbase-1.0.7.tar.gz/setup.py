#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-9-19 12:40:12
# @Author  : lijialun

from setuptools import setup
import qbase


setup(
    name=qbase.__title__,
    version=qbase.__version__,
    description=qbase.__description__,
    author=qbase.__author__,
    url=qbase.__uri__,
    author_email=qbase.__email__,
    packages=['qbase', 'qbase.common', 'qbase.dao', 'qbase.entity', 'qbase.enum', 'qbase.huobi', 'qbase.okex', 'qbase.threading', 'qbase.transaction'],
    py_modules=['qbase.app'],
    license=qbase.__license__ ,
    install_requires=[
        'requests >= 2.0.0',
        'pymysql',
        'pandas',
        'websocket'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)