# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    server_base.py
   Author :       Zhang Fan
   date：         18/10/05
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import socket


class Server_base():
    def __init__(self, is_broadcast=False):
        self._base_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__is_destroy = False
        self.__is_broadcast = is_broadcast

        if is_broadcast:
            self._base_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def destroy(self):
        if not self.__is_destroy:
            self.__is_destroy = True
            self._base_sock.close()
            self._base_sock = None

    def send_broadcast(self, port, data):
        assert self.__is_broadcast, '非广播模式请使用send函数'
        if not self.__is_destroy:
            self._base_sock.sendto(data, ('<broadcast>', port))

    def send(self, ip, port, data):
        assert not self.__is_broadcast, '广播模式请使用send_broadcast函数'
        if not self.__is_destroy:
            self._base_sock.sendto(data, (ip, port))

    @property
    def is_broadcast(self):
        return self.__is_broadcast

    @property
    def is_destroy(self):
        return self.__is_destroy
