# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    client.py
   Author :       Zhang Fan
   date：         18/10/05
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from ztimer import Timer

from zsocket.config import mconfig
from zsocket.commonlib import utils
from zsocket.commonlib.data_pack import data_pack
from zsocket.commonlib.data_pack import data_to_pack
from zsocket.tcp_base.client_base import Client_base


class Client(Client_base):
    def __init__(self):
        super().__init__()

        self.__check_heartbeat_timer = Timer(self.__check_heartbeat_timer_fun, mconfig.check_heart_beat_time)
        self.__send_heartbeat_timer = Timer(self.__send_heartbeat_timer_fun, mconfig.send_heart_beat_time)

        self.__pause_check_heartbeat = False
        self.__pause_send_heartbeat = False

        self._get_pack_callback = None

    def set_get_pack_callback(self, func):
        utils.check_value_is_func(func)
        self._get_pack_callback = func

    def _client_connect_fun(self):
        super()._client_connect_fun()

        if not self._base_server is None:
            self.__check_heartbeat_timer.start()
        else:
            self.__send_heartbeat_timer.start()

    def _client_close_fun(self, close_state):
        super()._client_close_fun(close_state)

        self.__check_heartbeat_timer.close()
        self.__send_heartbeat_timer.close()

    def __pause_heartbeat(self):
        if not self._base_server is None:
            self.__pause_check_heartbeat = True
        else:
            self.__pause_send_heartbeat = True

    def __check_heartbeat_timer_fun(self, timer):
        if self.__pause_check_heartbeat:
            self.__pause_check_heartbeat = False
        else:
            self.close()

    def __send_heartbeat_timer_fun(self, timer):
        if self.__pause_send_heartbeat:
            self.__pause_send_heartbeat = True
        else:
            self._base_sock.send(mconfig.data_tag_heart_beat)

    def _get_data_fun(self, data):
        self.__pause_heartbeat()
        super()._get_data_fun(data)

    def _get_text_fun(self, text):
        self.__pause_heartbeat()
        super()._get_text_fun(text)

    def _get_pack_fun(self, pack):
        self.__pause_heartbeat()
        if not self._get_pack_callback is None:
            self._get_pack_callback(self, pack)

    def send(self, data):
        self.__pause_heartbeat()
        super().send(data)

    def send_text(self, text):
        self.__pause_heartbeat()
        super().send_text(text)

    def send_pack(self, pack):
        if self._connect_state == mconfig.connect_state.connect:
            self.__pause_heartbeat()

            data = pack.to_data()
            try:
                self._base_sock.send(mconfig.data_tag_pack)  # 发送标记
                self._base_sock.send(utils.num_to_bytes(len(data)))  # 发送包大小
                self._base_sock.send(data)  # 发送包
            except:
                self.close()

    def send_pack_arg(self, data: bytes or bytearray = None, a1=0, a2=0, a3=0):
        self.send_pack(data_pack(data, a1, a2, a3))

    def _wait_data_tag_or_close(self):
        tag = self._wait_data_or_close(1)
        if not tag:
            return

        if tag == mconfig.data_tag_bytes or tag == mconfig.data_tag_text:
            return tag

        if tag == mconfig.data_tag_heart_beat or tag == mconfig.data_tag_pack:
            return tag

        self.close()

    def _wait_sock_data_fun(self):
        while self._connect_state == mconfig.connect_state.connect:
            tag = self._wait_data_tag_or_close()
            if not tag:
                return

            if tag == mconfig.data_tag_heart_beat:
                self.__pause_heartbeat()
                continue

            size = self._wait_data_size_or_close()
            if not size:
                return

            data = self._wait_data_or_close(size)
            if not data:
                return

            try:
                if tag == mconfig.data_tag_bytes:
                    self._get_data_fun(data)
                elif tag == mconfig.data_tag_text:
                    self._get_text_fun(data.decode('utf8'))
                elif tag == mconfig.data_tag_pack:
                    self._get_pack_fun(data_to_pack(data))
            except:
                self._close_state = mconfig.close_state.close
                self.close()
                return
