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

    import threading

    from zsocket.commonlib.data_pack import data_pack
    from zsocket.tcp.server import Server
    from zsocket.tcp.client import Client


    def server_client_connect_fun(client):
        print('服务端收到连接', client.remote_addr)
        server.close_listen()
        threading.Thread(target=send_data, args=(client,)).start()


    def server_client_close_fun(client, close_state):
        print('服务端断开连接', client.remote_addr, close_state)


    def send_data(client):
        while client.is_connect:
            text = input('请输入要发送的数据:')

            if not client.is_connect:
                return

            if not text or text.lower() == 'q':
                client.close()
                return

            client.send(text.encode())
            client.send_text(text)
            client.send_pack(data_pack(text, 1, 2, 3))


    def client_connect_fun(client):
        print('客户端连接', client.local_addr)


    def client_close_fun(client, close_state):
        print('客户端断开连接', client.local_addr, close_state)


    def client_get_data_fun(client, data):
        print('客户端收到数据', data)


    def client_get_text_fun(client, text):
        print('客户端收到文字', text)


    def client_get_pack_fun(client, pack):
        print('客户端收到包', pack.data, pack.a1, pack.a2, pack.a3)


    server = Server()
    server.password = '123'
    server.set_client_connect_callback(server_client_connect_fun)
    server.set_client_close_callback(server_client_close_fun)
    server.listen(7777)

    client = Client()
    client.password = '123'
    client.set_connect_callback(client_connect_fun)
    client.set_close_callback(client_close_fun)
    client.set_get_data_callback(client_get_data_fun)
    client.set_get_text_callback(client_get_text_fun)
    client.set_get_pack_callback(client_get_pack_fun)
    client.connect('localhost', 7777)
