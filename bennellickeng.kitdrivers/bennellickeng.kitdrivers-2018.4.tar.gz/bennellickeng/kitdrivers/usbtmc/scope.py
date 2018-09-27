from __future__ import print_function
from .usbtmc import Usbtmc
import numpy as np


class WaveformPreamble(object):
    def __init__(self, format, type, points, count, xinc, xorig, xref, yinc, yorig, yref):
        self.format = int(format)
        self.type = int(type)
        self.points = int(points)
        self.count = int(count)
        self.xinc = float(xinc)
        self.xorig = float(xorig)
        self.xref = int(xref)
        self.yinc = float(yinc)
        self.yorig = float(yorig)
        self.yref = int(yref)

    @classmethod
    def parse(cls, preamble_string):
        split_string =  preamble_string.strip().split(',')
        return cls(*split_string)

    def __repr__(self):
        things = "format: {0}, type: {1}, points: {2}, count: {3}, xinc: {4}, xorig: {5}, xref: {6}, yinc: {7}, yorig: {8}, yref: {9}".format(
            self.format, self.type, self.points, self.count, self.xinc, self.xorig, self.xref, self.yinc, self.yorig, self.yref
        )

        return "WaveformPreamble({0})".format(things)


class Scope(object):
    def __init__(self, device_file, quiet=False):
        self.device = Usbtmc(device_file)
        self.name = self.device.get_name()

        if not quiet:
            print(self.name)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        self.device.close()

    def get_freq(self, chan):
        return self._read_measurement([chan], "FREQ")

    def get_rmsdc(self, chan):
        return self._read_measurement([chan], "VRMS", "DC")

    def get_rmsac(self, chan):
        return self._read_measurement([chan], "VRMS", "AC")

    def get_vpp(self, chan):
        return self._read_measurement([chan], "VPP")

    def get_vavg(self, chan):
        return self._read_measurement([chan], "VAV", "DISP")

    def get_phase(self, chana, chanb):
        res = self._read_measurement([chana, chanb], "PHAS")

        if res > 360:
            return 0

        if res > 180:
            res -= 360
        return res

    def set_time(self, tpd):
        self._write(':TIM:SCAL ' + str(tpd))

    def set_time_position(self, offset):
        self._write(':TIM:POS ' + str(offset))

    def set_range(self, chan, range):
        self._write(":{0}:RANG {1}V".format(self.channel_string([chan]), range))

    def capture(self, input_channels):
        self._write(':DIGitize {0}'.format(self.channel_string(input_channels)))

    def get_waveform(self, chan):
        self._write(':waveform:points:mode raw')
        self._write(':waveform:source {0}'.format(self.channel_string([chan])))
        self._write(':waveform:format word')
        self._write(':waveform:unsigned off')
        self._write(':waveform:byteorder msbfirst')

        self._write(':waveform:preamble?')
        preamble = WaveformPreamble.parse(self._read_str(1000))

        self._write(':waveform:data?')
        # Offset to skip header and trailing newline
        raw_data = self._read((preamble.points*2)+11)
        scope_dtype = np.dtype('>i2')
        np_data = np.frombuffer(raw_data, dtype=scope_dtype, offset=10, count=preamble.points)

        scaled_data = ((np_data - preamble.yref) * preamble.yinc) + preamble.yorig

        timestamps = [preamble.xinc * x for x in range(scaled_data.size)]
        return np.transpose(np.array([timestamps, scaled_data]))

    def get_screenshot(self, annotation):
        if annotation is not None:
            self._write(":display:annotation ON")
            self._write(":display:annotation:color red")
            self._write(":display:annotation:background transparent")
            self._write(":display:annotation:text \"{}\"".format(annotation))
        self._write(":display:data? PNG, COLOR")
        header = self._read_str(2)
        assert(header[0] == "#")
        byte_count_len = int(header[1])
        byte_count = int(self._read_str(byte_count_len))
        image = self._read(byte_count)
        self._read(1) # Read trailing newline
        if annotation is not None:
            self._write(":display:annotation OFF")
        return image

    def _write(self, command):
        """Send an arbitrary command directly to the scope"""
        self.device.write_str(command)

    def _read_measurement(self, input_channels, quantity, *args):
        if len(args) > 0:
            optional_args = ",".join(args) + ","
        else:
            optional_args = ""

        self.device.write(":MEAS:{0}? {1}{2}".format(quantity, optional_args, self.channel_string(input_channels)))
        return float(self._read_str(9000))

    @staticmethod
    def channel_string(input_channels):
        return ",".join("CHAN{0}".format(input_channel) for input_channel in input_channels)

    def _read(self, length):
        """Read an arbitrary amount of data directly from the scope"""
        return self.device.read(length)

    def _read_str(self, length):
        """Read an arbitrary amount of data directly from the scope"""
        return self.device.read_str(length)

    def reset(self):
        """Reset the instrument"""
        self.device.send_reset()

def grab_CLI():
    import argparse
    parser = argparse.ArgumentParser(description="Dump stuff from the scope", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--device", default="/dev/scope", help="Scope USBTMC device file")
    parser.add_argument("output", help="Output base name. Extensions will be added as appropriate")
    parser.add_argument("--screenshot", action="store_true", default=True, help="Take a screenshot")
    parser.add_argument("--annotate", action="store_true", default=True, help="Annotate with base name")
    args = parser.parse_args()

    scope = Scope(args.device)
    if args.screenshot:
        image = scope.get_screenshot(args.output if args.annotate else None)
        with open("{}.png".format(args.output), "wb") as f:
            f.write(image)
