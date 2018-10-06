# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    __init__.py.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

if __name__ == '__main__':

    import threading

    from zsocket.tcp_base.server_base import Server_base
    from zsocket.tcp_base.client_base import Client_base


    def server_client_connect_fun(client):
        print('服务端收到连接', client.remote_addr)
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


    def client_connect_fun(client):
        print('客户端连接', client.local_addr)


    def client_close_fun(client, close_state):
        print('客户端断开连接', client.local_addr, close_state)
        server.close_listen()


    def client_get_data_fun(client, data):
        print('客户端收到数据', data)


    def client_get_text_fun(client, text):
        print('客户端收到文字', text)


    server = Server_base()
    server.password = '123'
    server.set_client_connect_callback(server_client_connect_fun)
    server.set_client_close_callback(server_client_close_fun)
    server.listen(5555)

    client = Client_base()
    client.password = '123'
    client.set_connect_callback(client_connect_fun)
    client.set_close_callback(client_close_fun)
    client.set_get_data_callback(client_get_data_fun)
    client.set_get_text_callback(client_get_text_fun)
    client.connect('localhost', 5555)
