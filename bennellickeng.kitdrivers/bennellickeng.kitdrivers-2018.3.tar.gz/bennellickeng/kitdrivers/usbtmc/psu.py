from __future__ import print_function
from .usbtmc import Usbtmc
import time


class Psu(object):
    def __init__(self, device_file):
        self.device = Usbtmc(device_file)
        self.name = self.device.get_name()

        print(self.name)

    def output_on(self, output_number):
        self.device.write_str(":OUTP CH{0},ON".format(output_number))

    def output_off(self, output_number):
        self.device.write_str(":OUTP CH{0},OFF".format(output_number))

    def set_output_voltage(self, output_number, voltage):
        self.device.write_str(":APPL CH{0},{1}".format(output_number, voltage))

    def read_current(self, output_number):
        self.device.write_str(":MEAS:CURR? CH{0}".format(output_number))
        return float(self.device.read_str(6))

    def reset(self):
        """Reset the instrument"""
        self.device.send_reset()
