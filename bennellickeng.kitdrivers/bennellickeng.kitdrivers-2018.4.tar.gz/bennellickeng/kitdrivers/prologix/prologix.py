from boltons import socketutils as su
import socket
import time
from warnings import warn


class PrologixConfigWarning(RuntimeWarning):
    pass


class Prologix(object):
    TERM_CRLF = 0
    TERM_CR = 1
    TERM_LF = 2
    TERM_NONE = 3

    def __init__(self, ip, device_addr,
                 termination_char=TERM_CRLF,
                 read_timeout=50,
                 opc_before_command=False):
        self.sock = socket.socket()
        self.sock.connect((ip, 1234))
        self.bs = su.BufferedSocket(self.sock, timeout=2)

        # The SCPI spec states that the OPC command should follow the command that is being waited on.
        # However, some instruments require the OPC command to be issued before the waited on command.
        self.opc_before_command = opc_before_command

        self.oob_write("mode 1")
        self.oob_write("addr {}".format(device_addr))
        self.oob_write("auto 0")
        self.oob_write("read_tmo_ms {}".format(read_timeout))
        self.oob_write("eos {}".format(termination_char))
        self.oob_write("clr")

        # Make sure instrument state is cleared.
        self.write("*CLS")

        # Flush the Prologix read buffer, as there may be stuff left over from a previous session
        try:
            self.bs.recv_size(10000, timeout=0.2)
        except su.Timeout:
            pass

        # Verify that the internal Prologix configuration state is as expected
        self._verify_config(device_addr, termination_char, read_timeout)

    def _verify_config(self, device_address, termination_char, read_timeout):
        def check_setting(setting, expected):
            self.oob_write(setting)
            actual = self.oob_read().decode()
            if actual != expected:
                warn(
                    "Prologix setting '{}' is set to '{}', but should be set to '{}'".format(setting, actual, expected),
                    PrologixConfigWarning)

        check_setting("addr", str(device_address))
        check_setting("auto", str(0))
        check_setting("eoi", str(1))
        check_setting("eos", str(termination_char))
        check_setting("eot_enable", str(0))
        # Don't check eot_char as the above check means that it's value is irrelevant
        check_setting("mode", str(1))
        check_setting("read_tmo_ms", str(read_timeout))

    def oob_write(self, command):
        #print("OOB write: {}".format(command))
        self.bs.send("++{}\n".format(command).encode())

    def oob_read(self, timeout=10):
        resp = self.bs.recv_until("\n".encode(), timeout=timeout)
        return resp.rstrip()

    def write(self, command, term=";\n"):
        # print("Sending {}".format(command))
        self.bs.send("{}{}".format(command, term).encode())

    def read(self, length, timeout=1, wait=0.0):
        time.sleep(wait)
        self.oob_write("read eoi")
        data = self.bs.recv_size(length, timeout=timeout)
        #print("Received {}".format(data))
        return data

    def readline(self, timeout=1, wait=0):
        return self.readlines(1, timeout=timeout, wait=wait)[0]

    def readlines(self, n_lines, timeout=1, wait=0):
        time.sleep(wait)
        self.oob_write("read eoi")
        lines = []
        for x in range(n_lines):
            line = self.bs.recv_until("\n".encode(), timeout=timeout)
            #print("Received {}".format(line))
            lines.append(line)
        return lines

    def get_name(self):
        self.write("*IDN?")
        return self.readline().decode()

    def local(self):
        self.oob_write("loc")

    def spoll(self):
        self.oob_write("spoll")
        return int(self.oob_read().decode())

    def srq(self):
        self.oob_write("srq")
        return int(self.oob_read().decode())

    def wait_for_srq(self, timeout=1, delay=0.1):
        start_t = time.time()
        while(time.time() < (start_t + timeout)):
            if self.srq() == 1:
                self.clear_srq()
                return
            time.sleep(delay)
        raise Exception("Timed out waiting for SRQ")

    def clear_srq(self):
        self.spoll()

    def opc_wait(self, command, timeout):
        self.write("*SRE 32")
        self.write("*ESE 1")
        self.clear_srq()

        if self.opc_before_command:
            self.write("*OPC; {}".format(command))
        else:
            self.write("{}; *OPC".format(command), term="\n")
        self.wait_for_srq(timeout=timeout)
