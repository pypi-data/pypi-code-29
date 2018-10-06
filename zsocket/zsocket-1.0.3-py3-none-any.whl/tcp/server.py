# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    server.py
   Author :       Zhang Fan
   date：         18/10/05
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from zsocket.tcp_base.server_base import Server_base
from zsocket.tcp.client import Client


class Server(Server_base):
    def _create_client(self, sock, addr):
        client = Client()
        client._set_client_from_server(self, sock, addr)

    def send_pack_to_all(self, pack):
        with self._sock_lock:
            for client in self._client_list:
                client.send_pack(pack)

    def send_pack_arg_to_all(self, data, a1, a2, a3):
        with self._sock_lock:
            for client in self._client_list:
                client.send_pack_arg(data, a1, a2, a3)
