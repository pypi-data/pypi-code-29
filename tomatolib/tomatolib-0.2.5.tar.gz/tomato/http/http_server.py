#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      http_server.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 11, 2018
    @desc:      Basic http server functions and router rules encapsulation
"""

import json
import signal
import logging
import asyncio
import functools
from aiohttp import web


class HttpServer(object):

    def __init__(self, host, port):
        self._loop = asyncio.get_event_loop()
        self._host = host
        self._port = int(port)
        self._app = web.Application()
        # self._app = web.Application(middlewares=[self.data_codec,])

    async def default_handler(self, request):
        req_params = request.query
        text = '''<html>
<head>
<title>Welcome to Tomato!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to Tomato!</h1>
<p>If you see this page, the tomato server is successfully installed and working.</p>
<p>For online documentation and support please refer to 
<a href="https://github.com/tangmi001/tomatolib/" target="_blank">tomatolib</a>.<br />

<p><em>Thank you for use tomatolib.</em></p>
</body>
</html>
'''
        response = web.Response(body=text.encode('utf-8'))
        response.headers['Content-Language'] = 'en'
        response.headers['Content-Type'] = 'en'
        return response

    @web.middleware
    async def data_codec(self, request, handler):
        """http简单解包与封包
           1.qs信息从request.query属性中直接获取（MultiDictProxy类型）
           2.http body内容如果请求头为content_type=application/json,
             则通过json标准库进行解析，并覆盖request.body，
             否则直接把body内容抛到业务层自行处理（默认是byte类型）
           3.对于response的处理，目前简单判断为dict则直接转成json格式str发给调用端
             否则直接按业务层返回值返回给调用端
        """
        request.body = None
        if request.body_exists and request.can_read_body:
            request.body = await request.content.read()
            if request.content_type == 'application/json':
                try:
                    request.body = json.loads(request.body)
                except Exception as e:
                    logging.warning('json format warning, errmsg[%s]', str(e))
                    return web.json_response({'ret': 0, 'msg': 'params error'})
        logging.warning('type[%s]', type(handler))
        response = await handler(request)
        if isinstance(response, dict):
            return web.json_response(response)
        else:
            return web.Response(body=response)

    def add_routes(self, routes):
        self._app.router.add_routes(routes)

    async def init_server(self):
        self._app.router.add_route('get', '/', self.default_handler)
        self._runner = web.AppRunner(self._app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, self._host, self._port)
        await site.start()
        logging.info('serving on [%s]', site.name)

    async def start(self):
        await self.init_server()

    async def close(self):
        await self._runner.cleanup()
        await self._app.shutdown()
        await self._app.cleanup()
