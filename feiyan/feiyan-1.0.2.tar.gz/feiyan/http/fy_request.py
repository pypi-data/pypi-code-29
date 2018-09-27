# coding: utf-8

import time
from feiyan.common.constant import HTTP


class FyRequest:
    def __init__(self):
        self.__url = None
        self.__protocol = HTTP
        self.__method = None
        self.__params = dict()
        self.__body = dict()
        self.__cloudToken = None
        self.__version = '1.0'
        self.__apiVer = '1.0.0'

    def set_url(self, url):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_protocol(self, protocol):
        self.__protocol = protocol

    def get_protocol(self):
        return self.__protocol

    def set_method(self, method):
        self.__method = method

    def get_method(self):
        return self.__method

    def set_version(self, version):
        self.__version = version

    def get_version(self):
        return self.__version

    def set_api_ver(self, api_ver):
        self.__apiVer = api_ver

    def get_api_ver(self):
        return self.__apiVer

    def set_cloud_token(self, cloud_token):
        self.__cloudToken = cloud_token

    def get_cloud_token(self):
        return self.__cloudToken

    def add_param(self, k, v):
        self.__params[k] = v

    def get_params(self):
        return self.__params

    def get_body(self):
        body = {
            "id": int(time.time() * pow(10, 6)),
            "version": self.get_version(),
            "request": {
                "apiVer": self.get_api_ver(),
                "cloudToken": self.get_cloud_token()
            },
            "params": self.get_params()
        }
        return body
