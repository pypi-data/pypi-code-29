from boltons import socketutils as su
import numpy as np
import socket
import skrf
import time

class VNA(object):
    MIN_F = 5000 # The testset only goes down to 5kHz, so avoid confusion by not allowing the VNA to be set lower
    MAX_F = 3000000000
    VALID_POINTS = range(1, 100002)
    VALID_IFBW = [1, 1.5, 2, 3, 5, 7, 10, 15, 20, 30, 50, 70, 100, 150, 200, 300, 500, 700, 1000, 1500, 2000, 3000,
                  5000, 7000, 10000, 15000, 20000, 30000, 50000, 70000, 100000, 150000, 200000, 300000, 500000]

    def __init__(self, ip):
        self.sock = socket.socket()
        self.sock.connect((ip, 5025))
        self.bs = su.BufferedSocket(self.sock, timeout=2)

        # Make sure instrument state is cleared.
        self.write("*CLS")

        self.name = self.get_name()
        print(self.name)

        # Set this once as it seems to be a slow operation (~6ms)
        self.write("FORM REAL, 32")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        # Make sure there is nothing left in the receive buffer
        try:
            self.bs.recv(10000000, timeout=0)
        except (su.Timeout, BlockingIOError):
            pass

        self.opc_wait("WAIT", timeout=2)
        self.local()

    def opc_wait(self, command, timeout):
        self.write("{}; *OPC?".format(command), term="\n")
        ret = self.read_int(timeout=timeout)
        if ret == 1:
            return
        else:
            raise ValueError("Unexpected response from *OPC?: '{}'".format(ret))

    def read(self, length, timeout=1, wait=0.0):
        time.sleep(wait)
        data = self.bs.recv_size(length, timeout=timeout)
        #print("Received {}".format(data))
        return data

    def write(self, command, term=";\n"):
        # print("Sending {}".format(command))
        self.bs.send("{}{}".format(command, term).encode())

    def readline(self, timeout=1, wait=0):
        return self.readlines(1, timeout=timeout, wait=wait)[0]

    def readlines(self, n_lines, timeout=1, wait=0):
        time.sleep(wait)
        lines = []
        for x in range(n_lines):
            line = self.bs.recv_until("\n".encode(), timeout=timeout).decode()
            #print("Received {}".format(line))
            lines.append(line)
        return lines

    def get_name(self):
        self.write("*IDN?")
        return self.readline()

    def local(self):
        self.write("SYST:KLOC OFF")

    def preset(self):
        self.write("SYST:PRES")
        self.opc_wait("WAIT", timeout=2)

    def start(self, f):
        assert(f >= self.MIN_F and f <= self.MAX_F)
        self.write("SENS:FREQ:STAR {:d}".format(int(f)))

    def stop(self, f):
        assert(f >= self.MIN_F and f <= self.MAX_F)
        self.write("SENS:FREQ:STOP {:d}".format(int(f)))

    def number_of_points(self, n):
        assert(n in self.VALID_POINTS)
        self.write("SENS:SWE:POIN {:d}".format(n))

    def ifbw(self, bw):
        assert(bw in self.VALID_IFBW)
        self.write("SENS:BAND {:d}".format(bw))

    def avg(self, factor, channel=1):
        self.write("SENS{:d}:AVER:COUN {:d}".format(channel, factor))
        self.write("SENS{:d}:AVER ON".format(channel))

    def do_sweep(self, timeout, channel=1):
        self.opc_wait("*WAI", timeout=timeout)

        # The SING command only does a single sweep, even if averaging is turned on.
        # Therefore, we have to use the NUMG command, with the same number of groups
        # as the averaging factor, if averaging is turned on, to ensure things work
        # as expected.
        #self.device.write("AVERO?")
        #avg_on = int(self.device.readline())
        #numg = 1
        #if avg_on == 1:
        #    print("WARNING: Single sweeping with averaging on is sketchy. Especially when measuring a two-port network")
        #    self.device.write("AVERFACT?")
        #    numg = int(float(self.device.readline()))
        #self.device.opc_wait("NUMG{:d}".format(numg), timeout=timeout)
        self.opc_wait("INIT{:d}:IMM".format(channel), timeout=timeout)

    def read_float(self, wait=0, timeout=1):
        line = self.readline(wait=wait, timeout=timeout)
        return float(line)

    def read_int(self, wait=0, timeout=1):
        return int(self.read_float(wait=wait, timeout=timeout))

    #def num_points(self):
    #    self.device.write("POIN?")
    #    return self.read_int(wait=0.2)

    def read_frequencies(self):
        self.write("CALC:DATA:STIM?")
        data = self.read_block()
        be_complex = np.dtype(np.float32).newbyteorder("<")
        return np.frombuffer(data, dtype=be_complex)

    def read_block(self, wait=0):
        header = self.read(2, wait=wait).decode()
        assert len(header) == 2
        if header[0] != "#":
            raise Exception("Found {} instead of start of block header".format(header[0]))
        byte_count_len = int(header[1])
        byte_count = int(self.read(byte_count_len))
        data = self.read(byte_count + 1) # +1 to read trailing newline too
        return data[:-1]

    def extract_single_s_param(self, name, freq, params):
        if name not in params:
            raise Exception("No {} data found".format(name))

        ntwk = skrf.Network()
        ntwk.z0 = 50
        ntwk.frequency = skrf.Frequency.from_f(freq, unit="Hz")
        ntwk.frequency_unit = "Hz"
        ntwk.name = "1 Port Network"
        ntwk.s = params[name][:,np.newaxis,np.newaxis]

        return ntwk

    def meas_s11(self, timeout=10, skip_sweep=False):
        freq, params = self.meas_data(timeout=timeout, skip_sweep=skip_sweep)
        return self.extract_single_s_param("S11", freq, params)

    def meas_s22(self, timeout=10, skip_sweep=False):
        freq, params = self.meas_data(timeout=timeout, skip_sweep=skip_sweep)
        return self.extract_single_s_param("S22", freq, params)

    def meas_s21(self, timeout=10, skip_sweep=False):
        freq, params = self.meas_data(timeout=timeout, skip_sweep=skip_sweep)
        return self.extract_single_s_param("S21", freq, params)

    def meas_s12(self, timeout=10, skip_sweep=False):
        freq, params = self.meas_data(timeout=timeout, skip_sweep=skip_sweep)
        return self.extract_single_s_param("S12", freq, params)

    def read_catalog(self, channel=1):
        self.write("CALC{:d}:DATA:CALL:CAT?".format(channel))
        return self.readline()[1:-1].split(",")

    def meas_data(self, timeout=10, skip_sweep=False):
        if not skip_sweep:
            self.do_sweep(timeout=timeout)
        else:
            self.opc_wait("*WAI", timeout=timeout)

        f = self.read_frequencies()
        cat = self.read_catalog()

        self.write("CALC:DATA:CALL? SDAT")
        data = self.read_block()
        full_data_len = len(data)
        assert full_data_len % len(cat) == 0
        chunk_size = int(full_data_len / len(cat))
        params = {}
        be_complex = np.dtype(np.complex64).newbyteorder("<")
        for i, param in enumerate(cat):
            start_idx = i * chunk_size
            end_idx = start_idx + chunk_size
            params[param] = np.frombuffer(data[start_idx:end_idx], dtype=be_complex)

        return f, params


    def meas_two_port(self, timeout=10, skip_sweep=False):
        freq, params = self.meas_data(timeout=timeout, skip_sweep=skip_sweep)
        s11 = self.extract_single_s_param("S11", freq, params)
        s21 = self.extract_single_s_param("S21", freq, params)
        s12 = self.extract_single_s_param("S12", freq, params)
        s22 = self.extract_single_s_param("S22", freq, params)

        ntwk = skrf.network.four_oneports_2_twoport(s11, s12, s21, s22)
        return ntwk


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
