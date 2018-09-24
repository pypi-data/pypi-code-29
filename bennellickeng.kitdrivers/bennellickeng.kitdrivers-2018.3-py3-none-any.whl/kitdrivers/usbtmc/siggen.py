from __future__ import print_function
from .usbtmc import Usbtmc
import time


class Siggen(object):
    class Function:
        SINE = "SIN"
        SQUARE = "SQU"
        USER = "USER"

    class VoltageUnit:
        Vpp = "VPP"
        Vrms = "VRMS"
        dBm = "DBM"

    class Polarity:
        Normal = "NORM"
        Inverted = "INV"

    def __init__(self, device_file):
        self.device = Usbtmc(device_file)
        self.name = self.device.get_name()

        print(self.name)

    @staticmethod
    def _channel_string(output_number):
        assert isinstance(output_number, int)
        if output_number == 1:
            return ""
        else:
            return ":CH{0}".format(output_number)

    def output_on(self, output_number):
        self._write("OUTP", output_number, "ON")
        time.sleep(0.1)

    def output_off(self, output_number):
        self._write("OUTP", output_number, "OFF")

    def set_load_impedance(self, output_number, z):
        self._write("OUTP:LOAD", output_number, str(z))

    def sine(self, output_number, frequency, amplitude, offset=0):
        self._write("APPL:SIN", output_number, str(frequency), str(amplitude), str(offset))

    def func(self, output_number, function):
        self._write("FUNC", output_number, function)

    def user_func(self, output_number, name):
        #self.func(output_number, self.Function.USER)
        self._write("FUNC:USER", output_number, name)

    def frequency(self, output_number, f):
        self._write("FREQ", output_number, str(f))

    def voltage(self, output_number, v):
        self._write("VOLT", output_number, str(v))

    def voltage_unit(self, output_number, v_unit):
        self._write("VOLT:UNIT", output_number, v_unit)

    def voltage_offset(self, output_number, offset):
        self._write("VOLT:OFFS", output_number, offset)

    def voltage_high(self, output_number, v_high):
        self._write("VOLT:HIGH", output_number, str(v_high))

    def voltage_low(self, output_number, v_low):
        self._write("VOLT:LOW", output_number, str(v_low))

    def polarity(self, output_number, polarity):
        self._write("OUTP:POL", output_number, polarity)

    def phase(self, output_number, phase):
        self._write("PHAS", output_number, phase)

    def burst(self, n_cycles, period):
        self._write("BURS:MODE", 1, "TRIG")
        self._write("BURS:NCYC", 1, str(n_cycles))
        self._write("BURS:INT:PER", 1, str(period))

    def data(self, output_number, values):
        self._write("DATA", output_number, "VOLATILE", ",".join(str(v) for v in (values)))

    def _write(self, command, output_number, *args):
        """Send an arbitrary command directly to the scope"""
        if len(args) > 0:
            parameters = " {0}".format(",".join(args))
        else:
            parameters = ""
        self.device.write_str("{0}{1}{2}".format(command, self._channel_string(output_number), parameters))
        time.sleep(0.1)

    def _read(self, length):
        """Read an arbitrary amount of data directly from the scope"""
        return self.device.read(length)

    def reset(self):
        """Reset the instrument"""
        self.device.send_reset()
