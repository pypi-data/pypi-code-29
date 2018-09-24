import os
import time
from fcntl import ioctl

from pyudev import Context

class Usbtmc(object):
    _USBTMC_IOC_NR = 91 # From include/uapi/linux/usb/tmc.h

    @staticmethod
    def from_serial_number(serial_number):
        """
        Return a usbtmc device from the given device serial
        number. Uses pyudev to lookup the device
        """

        def get_udev_leaves(device):
            """
            Utility to yield only leaf nodes found in this
            device's hierarchy
            """
            for child in device.children:
                if len(list(child.children)) == 0:
                    yield child
                else:
                    for l in get_udev_leaves(child):
                        yield l

        context = Context()
        for device in context.list_devices(subsystem='usb'):
            if device.get("ID_SERIAL_SHORT") == serial_number:
                for leaf in get_udev_leaves(device):
                    # return the first leaf we find
                    return Usbtmc(leaf.get("DEVNAME"))

    def __init__(self, device):
        self.device = device
        self.FILE = os.open(device, os.O_RDWR)

        # TODO: Test that the file opened

    def close(self):
        os.close(self.FILE)

    def write(self, command):
        os.write(self.FILE, command)
        # Reads straight after a write end up throwing a 'Connection Timed Out' exception without this delay :(
        time.sleep(0.001)

    def write_str(self, command):
        self.write(command.encode())

    def read(self, length=4000):
        try:
            return os.read(self.FILE, length)
        except TimeoutError as e:
            self.clear()
            raise e

    def read_str(self, length=4000):
        return self.read(length).decode()

    def get_name(self):
        self.write_str("*IDN?")
        return self.read_str(300)

    def send_reset(self):
        self.write_str("*RST")

    def _ioctl(self, nr):
        ioctl(self.FILE, (self._USBTMC_IOC_NR << 8) | nr)

    def clear(self):
        """Perform an 'initial clear' request"""
        self._ioctl(2)

    def indicate(self):
        self._ioctl(1)
