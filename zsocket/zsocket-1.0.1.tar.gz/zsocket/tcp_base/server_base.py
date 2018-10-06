# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    server_base.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import socket
import threading

from zsocket.commonlib import utils
from zsocket.tcp_base.client_base import Client_base


class Server_base():
    def __init__(self):
        self._port = 0
        self._wait_connect_th = None
        self._base_sock = None

        self._sock_lock = threading.Lock()
        self._is_listion = False
        self._password = None
        self._client_list = []
        self._max_client_count = None

        self._is_close_all = False

        self._client_connect_callback = None
        self._client_close_callback = None

    def listen(self, port, max_count=None, backlog=20):
        if self._is_listion:
            return

        self._max_client_count = max_count

        self._base_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._base_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self._base_sock.bind(('', port))
        self._base_sock.listen(backlog)

        self._port = port
        self._is_listion = True

        self._wait_connect_th = threading.Thread(target=self.__wait_connect_fun)
        self._wait_connect_th.setDaemon(False)
        self._wait_connect_th.start()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: None or str = None):
        assert value is None or isinstance(value, str), 'value必须为str类型或者None'
        self._password = value

    def close_listen(self):
        if self._is_listion:
            self._base_sock.close()
            self._is_listion = False

    def close_all_client(self):
        with self._sock_lock:
            self._is_close_all = True

            for client in self._client_list:
                client.close()
            self._client_list.clear()

            self._is_close_all = False

    def close(self):
        self.close_listen()
        self.close_all_client()
        self._base_sock = None

    def set_client_connect_callback(self, func):
        utils.check_value_is_func(func)
        self._client_connect_callback = func

    def set_client_close_callback(self, func):
        utils.check_value_is_func(func)
        self._client_close_callback = func

    def send_to_all(self, data):
        with self._sock_lock:
            for client in self._client_list:
                client.send(data)

    def __wait_connect_fun(self):
        while self._is_listion:
            try:
                sock, addr = self._base_sock.accept()
                if self._max_client_count and len(self._client_list) >= self._max_client_count:
                    sock.close()
                else:
                    self._create_client(sock, addr)
            except:
                pass

    def _create_client(self, sock, addr):
        client = Client_base()
        client._set_client_from_server(self, sock, addr)

    def _client_connect_fun(self, client):
        with self._sock_lock:
            self._client_list.append(client)

        if not self._client_connect_callback is None:
            self._client_connect_callback(client)

    def _client_close_fun(self, client, close_state):
        if not self._is_close_all:
            with self._sock_lock:
                if client in self._client_list:
                    self._client_list.remove(client)

        if not self._client_close_callback is None:
            self._client_close_callback(client, close_state)
