import os
import socket
import struct
from io import FileIO
from fcntl import ioctl
from random import randint


IFF_UP = 0x0001  # Bring interface up
SIOCGIFFLAGS = 0x8913  # Get interface flags
SIOCSIFFLAGS = 0x8914  # Set interface flags
SIOCGIFADDR = 0x8915  # Get interface address
SIOCSIFADDR = 0x8916  # Set interface address
TUNSETIFF = 0x400454ca  # Tun set interface
TUNSETPERSIST = 0x400454cb  # Tun set persistence
TUNSETOWNER = 0x400454cc  # Tun set owner
IFF_TUN = 0x0001  # Tun mode
IFF_TAP = 0x0002  # Tap mode
IFF_NO_PI = 0x1000  # Don't receive packet information


class Tap:
    """ An interface to a Linux tap device. """
    dummy_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, name='fond0', ip=None):
        self.name = name
        self.fd = os.open('/dev/net/tun', os.O_RDWR)
        self.tap_file = FileIO(self.fd, 'r+')
        # ioctl takes the name of the interface and flags as arguments, and returns the interface name
        ifs = ioctl(self.fd, TUNSETIFF, struct.pack(b'16sH', bytes(name, 'utf-8'), IFF_TAP | IFF_NO_PI))
        # Grab the string up to the first null byte, and use this as the name
        self.name = ifs[:ifs.index(0)].decode('utf-8')
        if ip is not None:
            self.ip = ip
        print('Using interface:', self.name, 'at', self.ip)

    @property
    def ip(self):
        try:
            raw_ip = ioctl(self.dummy_sock, SIOCGIFADDR, struct.pack(b'256s', bytes(self.name, 'utf-8')))[20:24]
            return socket.inet_ntoa(raw_ip)
        except OSError as e:
            if e.errno != 99: 
                raise  # Raise exceptions unrelated to getting the address
            return None
        
    @ip.setter
    def ip(self, ip=None):
        if ip is None:
            # Generate a random IPv4 address in the 10.0.0.0/24 subnet
            raw_ip = b'\x0a' + bytes([randint(0, 255) for _ in range(3)])
        elif type(ip) is str:
            raw_ip = socket.inet_aton(ip)
        else:
            raw_ip = ip
        # Assign the ip to the interface
        ioctl(self.dummy_sock, SIOCSIFADDR, struct.pack(b'16sH2s4s8s', bytes(self.name, 'utf-8'), socket.AF_INET,
                                                        b'\x00\x00', raw_ip, b'\x00'*8))

    @property
    def status(self):
        flags = ioctl(self.dummy_sock, SIOCGIFFLAGS, struct.pack(b'16sH', bytes(self.name, 'utf-8'), 0))
        return int.from_bytes(flags[16:], byteorder='little')

    @status.setter
    def status(self, status):
        if status == IFF_UP:
            flag = (self.status & 0xfffe) | IFF_UP
        else:
            flag = (self.status & 0xfffe)
        ioctl(self.dummy_sock, SIOCSIFFLAGS, struct.pack(b'16sH', bytes(self.name, 'utf-8'), flag))

    @classmethod
    def interface_status(cls, name, new_status):
        flag = ioctl(cls.dummy_sock, SIOCGIFFLAGS, struct.pack(b'16sH', bytes(name, 'utf-8'), 0))
        flag = int.from_bytes(flag[16:], byteorder='little')
        if new_status is None:
            return flag
        elif new_status == 'up':
            flag = (flag & 0xFFFE) | IFF_TUN
        else:
            flag = (flag & 0xFFFE)
        ioctl(cls.dummy_sock, SIOCSIFFLAGS, struct.pack(b'16sH', bytes(name, 'utf-8'), flag))

    def make_persistent(self, userid=os.geteuid()):
        # Assign persistence
        if self.ip is None:
            self.ip = None
        ioctl(self.fd, TUNSETOWNER, userid)
        ioctl(self.fd, TUNSETPERSIST, 1)


# def test(dict dummy):
#from libc.string cimport memcpy
#     from timeit import default_timer as timer
#     start = timer()
#     cdef Meta meta
#     cdef tuple remote
#     cdef int l = len(FAKE_FRAME)
#     cdef unsigned char[:] frame = bytearray(3+1518)
#     cdef unsigned char * c = &frame[0]
#     cdef unsigned char * fake_frame = FAKE_FRAME
#     for i in range(10**7):
#         memcpy(c+3, fake_frame, l)
#         meta = frame_metadata(frame[3:])
#         #print_meta(meta)
#         remote = dummy.get(meta.dst_ip)
#         #print(remote)
#     print((10**7*l)/2**20/(timer()-start))



