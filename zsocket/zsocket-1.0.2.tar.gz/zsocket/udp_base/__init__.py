# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    __init__.py.py
   Author :       Zhang Fan
   date：         18/10/05
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

if __name__ == '__main__':
    from ztimer import Timer

    from zsocket.udp_base.server_base import Server_base
    from zsocket.udp_base.client_base import Client_base

    def send_data(timer):
        # s = input('请输入要发送的数据')
        # server.SendBroadcast(s.encode('utf8'))
        server.send("localhost", 6666, 'aaa'.encode('utf8'))

    def get_data(client, addr, data):
        print('收到数据', addr, data)

    server = Server_base()

    client = Client_base(6666)
    client.set_get_data_callback(get_data)

    t1 = Timer(send_data, 1, 3)
    t1.start()
    t1.join()

    server.destroy()
    client.destroy()

    print('end')

