from threading import Thread
import socket

from kamene.layers.l2 import Ether

class SocketServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bufferSize = 4096
        self.packets = []

    def bind(self, port, ipAddr = '', listenCount = 1):
        self.socket.bind((ipAddr, port))

    def run(self):
        connection, connAddress = self.socket.accept()
        connection.setblocking(0)

        self.dataListen(connection)

    def dataListen(self, conn):
        packet = []
        while True:
            data = conn.recv(self.bufferSize)
            dataLen = len(data)
            if data:
                packet.append(data)
            if not data or dataLen < self.bufferSize:
                conn.close()
                packet = b"".join(packet)
                self.packets.append(Ether(packet))
                break


if __name__ == '__main__':
    socketServer = SocketServer()
    socketServer.bind(port=9090, listenCount=5)
    socketServer.start()



'''class SocketSelectServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.inputs = [self.socket]
        self.outputs = []
        self.message_queues = {}
        self.bufferSize = 4096
        self.packets = []

    def bind(self, port, ipAddr = '', listenCount = 1):
        self.socket.bind((ipAddr, port))
    
    def serverListen(self):
        connection, connAddress = self.socket.accept()
        connection.setblocking(0)
        self.inputs.append(connection)
        self.message_queues[connection] = queue.Queue()

    def dataListen(self, s):
        data = s.recv(self.bufferSize)
        dataLen = len(data)
        if data:
            self.message_queues[s].put(data)
            if s not in self.outputs:
                self.outputs.append(s)
        if not data or dataLen < self.bufferSize:
            if s in self.outputs:
                self.outputs.remove(s)
            self.inputs.remove(s)
            s.close()
            packet = b"".join(self.message_queues[s].queue)
            p = Ether(packet)
            self.packets.append(Ether(packet))
            del self.message_queues[s]

    def run(self):
        while self.inputs:
            self.readable, self.writeable, self.expectional = select.select(self.inputs, self.outputs, self.inputs)
            for s in self.readable:
                if s is self.socket:
                    self.serverListen()
                else:
                    self.dataListen(s)

            for s in self.writeable:
                try:
                    next_msg = self.message_queues[s].get_nowait()
                except queue.Empty:
                    self.outputs.remove(s)
                else:
                    s.send(next_msg)

            for sn in self.expectional:
                self.inputs.remove(s)
                if s in self.outputs:
                    self.outputs.remove(s)
                s.close()
                del self.message_queues[s]


if __name__ == '__main__':
    socketServer = SocketServer()
    socketServer.bind(port=9090, listenCount=5)
    socketServer.start()'''