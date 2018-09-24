import numpy as np
from .prologix import Prologix
import struct
import skrf
import time

class VNA(object):
    MIN_F = 300000 # The testset only goes down to 300kHz, so avoid confusion by not allowing the VNA to be set lower
    MAX_F = 6000000000
    VALID_POINTS = [3, 11, 21, 26, 51, 101, 201, 401, 801, 1601]
    VALID_IFBW = [10, 30, 100, 300, 1000, 3000, 3700, 6000]

    def __init__(self, ip, device_address=16, read_f_once=False):
        self.device = Prologix(ip, device_address, termination_char=Prologix.TERM_NONE, opc_before_command=True,
                               read_timeout=500)
        self.name = self.device.get_name()
        self._read_f_once = read_f_once
        self._frequencies = None
        print(self.name)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.device.opc_wait("WAIT", timeout=2)
        self.local()

    def local(self):
        self.device.local()

    def preset(self):
        self.device.write("PRES")
        self.device.opc_wait("WAIT", timeout=2)

    def start(self, f):
        assert(f >= self.MIN_F and f <= self.MAX_F)
        self.device.write("STAR {:d}".format(int(f)))

    def stop(self, f):
        assert(f >= self.MIN_F and f <= self.MAX_F)
        self.device.write("STOP {:d}".format(int(f)))

    def number_of_points(self, n):
        assert(n in self.VALID_POINTS)
        self.device.write("POIN {:d}".format(n))

    def ifbw(self, bw):
        assert(bw in self.VALID_IFBW)
        self.device.write("IFBW {:d}".format(bw))

    def avg(self, factor):
        self.device.write("AVERFACT{:d}".format(factor))
        self.device.write("AVEROON")

    def do_sweep(self, timeout):
        self.device.opc_wait("WAIT", timeout=timeout)

        # The SING command only does a single sweep, even if averaging is turned on.
        # Therefore, we have to use the NUMG command, with the same number of groups
        # as the averaging factor, if averaging is turned on, to ensure things work
        # as expected.
        self.device.write("AVERO?")
        avg_on = int(self.device.readline())
        numg = 1
        if avg_on == 1:
            print("WARNING: Single sweeping with averaging on is sketchy. Especially when measuring a two-port network")
            self.device.write("AVERFACT?")
            numg = int(float(self.device.readline()))
        self.device.opc_wait("NUMG{:d}".format(numg), timeout=timeout)

    def read_float(self, wait=0):
        line = self.device.readline(wait=wait)
        return float(line)

    def read_int(self, wait=0):
        return int(self.read_float(wait=wait))

    def num_points(self):
        self.device.write("POIN?")
        return self.read_int(wait=0.2)

    def read_frequencies(self):
        if not self._read_f_once or self._frequencies is None:
            n_points = self.num_points()

            self.device.write("OUTPLIML")
            raw_data = self.device.readlines(n_points, wait=1)
            frequencies = []
            for line_no, line in enumerate(raw_data):
                frequencies.append(float(line.split(b",")[0]))

            self._frequencies = np.array(frequencies)
        return self._frequencies

    def read_form3(self, wait=0):
        header = self.device.read(4, wait=wait)
        assert(len(header) == 4)
        if header[:2].decode() != "#A":
            raise Exception("Found {} instead of start of block header".format(header[:2].decode()))
        length = struct.unpack(">h", header[2:])[0]
        data = self.device.read(length)
        be_complex = np.dtype(np.complex128).newbyteorder(">")
        return np.frombuffer(data, dtype=be_complex)

    def meas_s11(self, timeout=10, skip_sweep=False):
        return self.meas_single_s_param(1, 1, timeout=timeout, skip_sweep=skip_sweep)

    def meas_s22(self, timeout=10, skip_sweep=False):
        return self.meas_single_s_param(2, 2, timeout=timeout, skip_sweep=skip_sweep)

    def meas_s21(self, timeout=10, skip_sweep=False):
        return self.meas_single_s_param(2, 1, timeout=timeout, skip_sweep=skip_sweep)

    def meas_s12(self, timeout=10, skip_sweep=False):
        return self.meas_single_s_param(1, 2, timeout=timeout, skip_sweep=skip_sweep)

    def meas_single_s_param(self, resp_port, stim_port, timeout=10, skip_sweep=False):
        assert(resp_port in [1, 2])
        assert(stim_port in [1, 2])
        # Hold sweep while preparing
        self.device.write("HOLD")
        self.device.write("S{:d}{:d}".format(resp_port, stim_port))
        self.device.write("POLA")
        self.device.write("CONVOFF")

        if not skip_sweep:
            self.do_sweep(timeout=timeout)
        else:
            self.device.opc_wait("WAIT", timeout=timeout)

        f = self.read_frequencies()
        self.device.write("FORM3")
        self.device.write("OUTPFORM")
        s11 = self.read_form3(wait=0.5)

        ntwk = skrf.Network()
        ntwk.z0 = 50
        ntwk.frequency = skrf.Frequency.from_f(f, unit="Hz")
        ntwk.frequency_unit = "Hz"
        ntwk.name = "1 Port Network"
        ntwk.s = s11[:,np.newaxis,np.newaxis]

        return ntwk

    def meas_two_port(self, timeout=10, skip_sweep=False):
        s11 = self.meas_s11(timeout=timeout, skip_sweep=skip_sweep)
        s12 = self.meas_s12(timeout=timeout, skip_sweep=True)
        s21 = self.meas_s21(timeout=timeout, skip_sweep=True)
        s22 = self.meas_s22(timeout=timeout, skip_sweep=True)

        ntwk = skrf.network.four_oneports_2_twoport(s11, s12, s21, s22)
        return ntwk

    def meas_z(self):
        self.device.write("POLA")
        self.device.write("CONVZREF")

        f = self.read_frequencies()

        self.device.write("FORM3")
        self.device.write("OUTPFORM")
        z = self.read_form3(wait=0.5)

        return np.vstack((f, z)).T


def grab_CLI():
    import argparse

    parser = argparse.ArgumentParser(description="Dump stuff from the VNA",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("device", help="Hostname or IP address of the VNA")
    parser.add_argument("output", help="Output base name. Extensions will be added as appropriate")
    parser.add_argument("--nports", type=int, choices=[1, 2], required=True, help="Number of ports on DUT")
    parser.add_argument("--nosweep", action="store_true", help="Don't perform sweep before grabbing data")
    parser.add_argument("--sweep_timeout", type=int, default=120,
                        help="How long to wait for the sweep to complete in seconds")
    args = parser.parse_args()

    with VNA(args.device) as vna:
        if args.nports == 1:
            vna.meas_s11(timeout=args.sweep_timeout, skip_sweep=args.nosweep) \
                .write_touchstone("{}.s1p".format(args.output))
        elif args.nports == 2:
            vna.meas_two_port(timeout=args.sweep_timeout, skip_sweep=args.nosweep) \
                .write_touchstone("{}.s2p".format(args.output))
