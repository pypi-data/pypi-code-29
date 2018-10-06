# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    client_base.py
   Author :       Zhang Fan
   date：         18/10/05
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import socket
import threading

from zsocket.config import mconfig
from zsocket.commonlib import utils


class Client_base():
    def __init__(self, port):
        self._base_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._base_sock.bind(('', port))

        self.__port = port
        self.__is_destroy = False
        self.__get_data_callback = None

        th = threading.Thread(target=self._wait_sock_data_fun)
        th.setDaemon(False)
        th.start()

    def set_get_data_callback(self, func):
        utils.check_value_is_func(func)
        self.__get_data_callback = func

    def destroy(self):
        if not self.__is_destroy:
            self.__is_destroy = True
            self._base_sock.close()
            self._base_sock = None

    def _wait_sock_data_fun(self):
        while not self.__is_destroy:
            try:
                data, addr = self._base_sock.recvfrom(mconfig.data_max_size)
            except:
                continue

            if data and self.__get_data_callback != None:
                self.__get_data_callback(self, addr, data)

    def send(self, ip, port, data):
        if not self.__is_destroy:
            self._base_sock.sendto(data, (ip, port))

    @property
    def port(self):
        return self.__port

    @property
    def is_destroy(self):
        return self.__is_destroy
