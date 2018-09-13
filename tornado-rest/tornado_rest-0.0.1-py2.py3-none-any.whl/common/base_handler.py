#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : base_handler.py
# @Date : 2018/9/5 9:56
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import json

from tornado.web import RequestHandler
from tornado_rest.core.encoders import AlchemyJsonEncoder


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

    def data_received(self, chunk):
        pass

    def write_api(self, query):
        count = query.count()
        result = json.dumps(query, cls=AlchemyJsonEncoder)
        results = {"count": count, "data": json.loads(result)}
        self.write(results)
