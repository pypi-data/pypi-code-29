import socket
import json


class Requester:
    def __init__(self, host, port=23400):
        self.addr = (host, port)

    def request(self, payload):
        s = socket.socket()
        s.connect(self.addr)

        payload = json.dumps(payload) + '#__EOT'
        s.sendall(payload.encode('utf-8'))

        data = ''
        while True:
            incoming = s.recv(4096)
            if incoming == b'':
                break
            data += incoming.decode('utf-8')

        return json.loads(data)
