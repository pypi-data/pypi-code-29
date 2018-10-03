#!/usr/bin/python3
# -*- coding:utf-8 -*-

from  aiohttp.web import RouteTableDef


class Routes(RouteTableDef):
    def __init__(self, *args, **kwargs):
        RouteTableDef.__init__(self, *args, **kwargs)
