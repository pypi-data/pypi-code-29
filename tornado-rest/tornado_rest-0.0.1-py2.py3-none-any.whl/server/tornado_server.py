#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : tornado_server.py
# @Date : 2018/9/4 9:26
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

from tornado.options import define
import tornado.httpserver
import tornado.ioloop

from tornado_rest.server.base import application
from tornado_rest.common.config import CONF

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(CONF.server.port)
    print("server serving on % s:% s" % (CONF.server.ip, CONF.server.port))
    tornado.ioloop.IOLoop.current().start()
