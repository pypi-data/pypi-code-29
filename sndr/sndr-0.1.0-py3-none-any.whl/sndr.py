import socket
import json


class Requester:
    def __init__(self, host, port=23400):
        self.addr = (host, port)

    def request(self, payload):
        s = socket.socket()
        s.connect(self.addr)
        s.sendall(json.dumps(payload) + '#__EOT')

        data = ''
        while True:
            incoming = s.recv(4096)
            if incoming == '':
                break
            data += incoming

        return json.loads(data)
