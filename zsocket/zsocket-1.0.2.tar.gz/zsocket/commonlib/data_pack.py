# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    data_pack.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from zsocket.commonlib import utils


class data_pack():
    def __init__(self, data: bytes or bytearray = None, a1=0, a2=0, a3=0):
        '''
        构建一个数据包
        :param data: 数据(字节数组类型,或者字符串类型)
        :param a1: 参数1
        :param a2: 参数2
        :param a3: 参数3
        '''
        if isinstance(data, str):
            data = data.encode("utf8")
        else:
            assert data is None or isinstance(data, bytes) or isinstance(data, bytearray), \
                'data必须为str, bytes, bytearray 或 None, 你传入的是{}'.format(type(data))

        self.data = data
        self.a1, self.a2, self.a3 = a1, a2, a3

    def to_data(self):
        return pack_to_data(self)

    def to_text(self, coding='utf8'):
        if not self.data:
            return ''
        return self.data.decode(coding)


def pack_to_data(pack: data_pack):
    '''构建包(返回字节数组)'''
    # 消息头长度=参数数量*4
    head_len = 12  # 3 * 4
    data_size = head_len + (len(pack.data) if pack.data else 0)  # 数据大小
    data = bytearray(data_size)  # 数据缓存

    # 写入参数
    index = 0  # 指针
    index = utils.write_num(data, pack.a1, index)
    index = utils.write_num(data, pack.a2, index)
    index = utils.write_num(data, pack.a3, index)

    # 写入数据
    if pack.data:
        utils.write_bytes(data, pack.data, index)
    return data


def data_to_pack(data: bytes or bytearray):
    '''解包(返回包结构)'''
    a1 = utils.byte_to_num(data[0], data[1], data[2], data[3])
    a2 = utils.byte_to_num(data[4], data[5], data[6], data[7])
    a3 = utils.byte_to_num(data[8], data[9], data[10], data[11])
    le = len(data) - 12  # 消息头长度为12
    real_data = None
    if le > 0:
        real_data = bytearray(le)
        utils.array_copy(real_data, 0, data, 12, le)
    return data_pack(real_data, a1, a2, a3)


if __name__ == '__main__':
    a = data_pack('你好', 3, 2, 1)
    v = a.to_data()
    print(len(v))
    print(v)

    a = data_to_pack(v)
    print(a.data)
    print(a.to_text())
    print(a.a1, a.a2, a.a3)
