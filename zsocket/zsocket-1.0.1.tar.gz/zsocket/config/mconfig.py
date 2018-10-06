# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    mconfig.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from enum import Enum


class connect_state(Enum):
    close = 0
    wait_connect = 1
    wait_hello_msg = 2
    wait_check_code = 3
    connect = 4


class close_state(Enum):
    close = 0
    cant_connect = 1
    cant_get_hello_msg = 2
    cant_get_check_code = 3
    cant_get_remove_addr = 4
    err_hello_msg = 5
    err_check_code = 6
    err_data_tag = 7
    err_data_size = 8


connect_state_describe = {
    connect_state.close: '关闭',
    connect_state.wait_connect: '等待连接',
    connect_state.wait_hello_msg: '等待欢迎消息',
    connect_state.wait_check_code: '等待校验码',
    connect_state.connect: '连接'
}

close_state_describe = {
    close_state.close: '连接已关闭',
    close_state.cant_connect: '无法连接',
    close_state.cant_get_hello_msg: '无法获取到欢迎信息',
    close_state.cant_get_check_code: '无法获取到校验码',
    close_state.cant_get_remove_addr: '无法获取远程ip地址和端口',
    close_state.err_hello_msg: '错误的握手信息',
    close_state.err_check_code: '错误的校验码',
    close_state.err_data_tag: '错误的数据包标签',
    close_state.err_data_size: '错误的数据包大小'
}

'''等待连接的时间'''
wait_connect_time = 5

'''服务器欢迎信息'''
server_hello_msg = 'zsocket_server'
'''客户端欢迎信息'''
client_hello_msg = 'zoscket_client'

'''服务器校验码'''
check_code = b'\xaf'

'''心跳时间'''
send_heart_beat_time = 30
'''检查心跳时间'''
check_heart_beat_time = 45

# 数据标记
'''心跳标记'''
data_tag_heart_beat = b'\xa0'
'''数据标记'''
data_tag_bytes = b'\xa1'
'''文本标记(默认utf8)'''
data_tag_text = b'\xa2'
'''包标记'''
data_tag_pack = b'\xa3'

'''控制码'''
command = 0xaa000000

'''一次最大允许传输数据大小'''
data_max_size = 4 * 1024 * 1024  # 4M
'''最大允许缓存数据大小'''
data_max_buff_size = 4 * 1024 * 1024 * 1024  # 4G
