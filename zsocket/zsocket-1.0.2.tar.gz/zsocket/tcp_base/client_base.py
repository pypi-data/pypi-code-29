# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    client_base.py
   Author :       Zhang Fan
   date：         18/09/29
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import socket
import threading

from ztimer import Timer

from zsocket.config import mconfig
from zsocket.commonlib import utils


class Client_base():
    def __init__(self):
        self._connect_state = mconfig.connect_state.close
        self._close_state = mconfig.close_state.close

        self._base_server = None
        self._base_sock = None  # type:socket.socket

        self._password = None

        self._remote_addr = None
        self._local_addr = None
        self.__check_real_connect_timer = Timer(self.__check_real_connect_timer_fun,
                                                mconfig.wait_connect_time, loop_count=1)

        self._client_connect_callback = None
        self._client_close_callback = None
        self._get_data_callback = None
        self._get_text_callback = None

    def _set_client_from_server(self, server, sock, addr):
        self._base_server = server
        self._base_sock = sock
        self._connect_state = mconfig.connect_state.wait_hello_msg

        self._password = server._password
        self._remote_addr = sock.getpeername()

        pwd = self._password or ''
        hello = (mconfig.server_hello_msg + pwd).encode('utf8')
        sock.send(hello)

        th = threading.Thread(target=self.__wait_real_connect_thread_fun)
        th.setDaemon(False)
        th.start()

        self.__check_real_connect_timer.start()

    @property
    def remote_addr(self):
        if self._remote_addr is None:
            if not self._base_sock is None:
                self._remote_addr = self._base_sock.getpeername()

        return self._remote_addr

    @property
    def local_addr(self):
        if self._local_addr is None:
            if not self._base_sock is None:
                self._local_addr = self._base_sock.getsockname()

        return self._local_addr

    @property
    def connect_state(self):
        return self._connect_state

    @property
    def is_connect(self):
        return self._connect_state == mconfig.connect_state.connect

    @property
    def is_close(self):
        return self._connect_state == mconfig.connect_state.close

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: None or str = None):
        assert value is None or isinstance(value, str), 'value必须为str类型或者None'
        self._password = value

    def set_connect_callback(self, func):
        utils.check_value_is_func(func)
        self._client_connect_callback = func

    def set_close_callback(self, func):
        utils.check_value_is_func(func)
        self._client_close_callback = func

    def set_get_data_callback(self, func):
        utils.check_value_is_func(func)
        self._get_data_callback = func

    def set_get_text_callback(self, func):
        utils.check_value_is_func(func)
        self._get_text_callback = func

    def close(self):
        '''关闭连接'''
        if self._connect_state == mconfig.connect_state.close:
            return

        self.__check_real_connect_timer.close()

        connect_state = self._connect_state
        close_state = self._close_state
        self._connect_state = mconfig.connect_state.close
        self._close_state = mconfig.close_state.close

        if self._base_sock != None:
            self._base_sock.close()
            self._base_sock = None

        self._client_close_fun(close_state)

        if not self._base_server is None and connect_state == mconfig.connect_state.connect:
            self._base_server._client_close_fun(self, close_state)

    def connect(self, ip: str, port: int):
        if self._connect_state != mconfig.connect_state.close:
            return

        self._base_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connect_state = mconfig.connect_state.wait_connect

        self.__check_real_connect_timer.start()

        th = threading.Thread(target=self.__connect_fun, args=(ip, port))
        th.setDaemon(False)
        th.start()

    def __connect_fun(self, ip, port):
        try:
            self._base_sock.connect((ip, port))
            self._remote_addr = self._base_sock.getpeername()
            if self._remote_addr == None:
                self._close_state = mconfig.close_state.cant_get_remove_addr
                self.close()
            else:
                self._connect_state = mconfig.connect_state.wait_hello_msg
                self.__wait_real_connect_thread_fun()
        except Exception as ex:
            print(ex)
            self._close_state = mconfig.close_state.cant_connect
            self.close()

    def __check_real_connect_timer_fun(self, timer):
        if self._connect_state == mconfig.connect_state.wait_connect:
            self._close_state = mconfig.close_state.cant_connect
            self.close()
        elif self._connect_state == mconfig.connect_state.wait_hello_msg:
            self._close_state = mconfig.close_state.cant_get_hello_msg
            self.close()
        elif self._connect_state == mconfig.connect_state.wait_check_code:
            self._close_state = mconfig.close_state.cant_get_check_code
            self.close()

    def __wait_real_connect_thread_fun(self):
        if not self.__check_hello_msg():
            self.close()
            return

        if self._connect_state == mconfig.connect_state.wait_check_code:
            if not self.__check_check_code():
                self.close()
                return

        if self._connect_state == mconfig.connect_state.connect:
            self._wait_sock_data_fun()

    def __check_hello_msg(self):
        data = utils.wait_sock_data_once(self._base_sock)
        if not data:
            self._close_state = mconfig.close_state.cant_get_hello_msg
            return

        try:
            msg = data.decode()
        except:
            self._close_state = mconfig.close_state.err_hello_msg
            return

        if self._base_server:  # 这个是服务端
            return self.__check_server_hello_msg(msg)
        return self.__check_client_hello_msg(msg)

    def __check_server_hello_msg(self, msg):
        pwd = self._password or ''
        if msg != mconfig.client_hello_msg + pwd:
            self._close_state = mconfig.close_state.err_hello_msg
            return

        self._connect_state = mconfig.connect_state.connect
        self._close_state = mconfig.close_state.close

        self._base_sock.send(mconfig.check_code)

        self.__check_real_connect_timer.close()
        self._base_server._client_connect_fun(self)
        self._client_connect_fun()
        return True

    def __check_client_hello_msg(self, msg):
        # 这个是客户端
        pwd = self._password or ''
        if msg != mconfig.server_hello_msg + pwd:
            self._close_state = mconfig.close_state.err_hello_msg
            return

        self._connect_state = mconfig.connect_state.wait_check_code
        self._close_state = mconfig.close_state.close

        self._base_sock.send((mconfig.client_hello_msg + pwd).encode('utf8'))
        return True

    def __check_check_code(self):
        data = utils.wait_sock_data_once(self._base_sock, 1)
        if not data:
            self._close_state = mconfig.close_state.cant_get_hello_msg
            return

        if data != mconfig.check_code:
            self._close_state = mconfig.close_state.err_check_code
            return

        self.__check_real_connect_timer.close()
        self._connect_state = mconfig.connect_state.connect
        self._close_state = mconfig.close_state.close
        self._client_connect_fun()
        return True

    def send(self, data):
        if self._connect_state == mconfig.connect_state.connect:
            try:
                self._base_sock.send(mconfig.data_tag_bytes)  # 发送标记
                self._base_sock.send(utils.num_to_bytes(len(data)))  # 发送包大小
                self._base_sock.send(data)  # 发送包
            except:
                self.close()

    def send_text(self, text):
        if self._connect_state == mconfig.connect_state.connect:
            bs = text.encode('utf8')
            try:
                self._base_sock.send(mconfig.data_tag_text)  # 发送标记
                self._base_sock.send(utils.num_to_bytes(len(bs)))  # 发送包大小
                self._base_sock.send(bs)  # 发送包
            except:
                self.close()

    def _wait_sock_data_fun(self):
        while self._connect_state == mconfig.connect_state.connect:
            tag = self._wait_data_tag_or_close()
            if not tag:
                return

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
            except:
                self._close_state = mconfig.close_state.close
                self.close()
                return

    def _wait_data_or_close(self, size):
        data = utils.wait_sock_data(self._base_sock, size)
        if data:
            return data

        self._close_state = mconfig.close_state.close
        self.close()
        return

    def _wait_data_tag_or_close(self):
        tag = self._wait_data_or_close(1)
        if not tag:
            return

        if tag == mconfig.data_tag_bytes or tag == mconfig.data_tag_text:
            return tag

        self.close()

    def _wait_data_size_or_close(self):
        data = self._wait_data_or_close(4)
        if not data:
            return

        size = utils.bytes_to_num(data)
        if 0 == size or size > mconfig.data_max_buff_size:
            self._close_state = mconfig.close_state.err_data_size
            self.close()
            return

        return size

    def _client_connect_fun(self):
        if not self._client_connect_callback is None:
            self._client_connect_callback(self)

    def _client_close_fun(self, close_state):
        if not self._client_close_callback is None:
            self._client_close_callback(self, close_state)

    def _get_data_fun(self, data):
        if not self._get_data_callback is None:
            self._get_data_callback(self, data)

    def _get_text_fun(self, text):
        if not self._get_text_callback is None:
            self._get_text_callback(self, text)
