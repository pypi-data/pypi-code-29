# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    utils.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from zsocket.config import mconfig


def num_to_bytes(num: int):
    '''数字转换为4位字节数组(10进制转256进制)'''
    b1 = num // 16777216
    num = num % 16777216

    b2 = num // 65536
    num = num % 65536

    b3 = num // 256

    b4 = num % 256

    return bytes((b1, b2, b3, b4))


def bytes_to_num(bs: bytes or bytearray):
    '''4位字节数组转为数字(256进制转10进制)'''
    return bs[0] * 16777216 + bs[1] * 65536 + bs[2] * 256 + bs[3]


def byte_to_num(b1: int, b2: int, b3: int, b4: int):
    '''4位字节数组转为数字(256进制转10进制)'''
    return b1 * 16777216 + b2 * 65536 + b3 * 256 + b4


def write_bytes(data: bytes or bytearray, bs: bytes or bytearray, data_index: int):
    '''将bs写入到data中的index位置'''
    data[data_index:data_index + len(bs)] = bs


def array_copy(data: bytes or bytearray, data_index: int, bs: bytes or bytearray, bs_index: int, length: int):
    '''从bs的bs_index开始取长度为le的数据写入到data的data_index位置'''
    data[data_index:data_index + length] = bs[bs_index:bs_index + length]


def write_num(data: bytes or bytearray, num: int, index: int):
    '''将num写入到data的index位置'''
    bs = num_to_bytes(num)
    write_bytes(data, bs, index)
    return index + len(bs)


def wait_sock_data_once(sock, buffsize=1024):
    '''等待sock收到一条数据'''
    try:
        data = sock.recv(buffsize)
        if data:
            return data
    except:
        pass


def wait_sock_data(sock, length: int):
    '''等待直到数据获取完毕(sock对象,数据长度)'''
    assert length <= mconfig.data_max_buff_size, '超出最大允许缓存数据大小'

    data = bytearray(length)
    index = 0

    while length > 0:  # 还有length长度的包未接收完毕
        le = mconfig.data_max_size if length > mconfig.data_max_size else length
        bs = wait_sock_data_once(sock, le)
        if not bs:
            return

        le = len(bs)
        write_bytes(data, bs, index)
        index += le
        length -= le

    return data


def check_value_is_func(value, allow_none=True):
    assert hasattr(value, '__call__'), '参数必须包含__call__属性' or (allow_none and value is None)
