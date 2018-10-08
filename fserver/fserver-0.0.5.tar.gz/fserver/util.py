import socket

DEBUG = True


def debug(*args, sep=' ', end='\n', file=None):
    if DEBUG:
        print(*args, sep=sep, end=end, file=file)


def get_ip_v4():
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    ip_v4s = [ip[4][0] for ip in addrs if ':' not in ip[4][0]]
    return ip_v4s
