# coding: utf-8

import json
from feiyan import client
from feiyan.common import constant
from feiyan.http.request import Request
from feiyan.http.fy_request import FyRequest


class FyClient:
    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
        self.host = 'https://api.link.aliyun.com'

    def __client(self):
        return client.DefaultClient(app_key=self.app_key, app_secret=self.app_secret)

    def execute(self, fy_request):
        if not isinstance(fy_request, FyRequest):
            raise Exception('invalid fy_request instance')
        req = Request(
            host=self.host,
            protocol=fy_request.get_protocol(),
            url=fy_request.get_url(),
            method=fy_request.get_method()
        )
        req.set_body(json.dumps(fy_request.get_body()))
        req.set_content_type(constant.CONTENT_TYPE_JSON)
        return self.__client().execute(req)
