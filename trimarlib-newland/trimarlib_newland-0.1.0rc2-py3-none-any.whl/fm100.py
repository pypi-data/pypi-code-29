import binascii
import logging
import threading
import configparser

import serial
import serial.tools.list_ports


class FM100(object):
    VID = 0x1EAB
    PID = 0x0C06

    PROG_MODE_ENTER = b'$$$$'
    PROG_MODE_ON = b'@@@@'
    PROG_MODE_EXIT = b'%%%%'
    PROG_MODE_OFF = b'^^^^'

    DIGIT_CODE_BASE = b'999000'

    STORE = b'99900020'
    ABORT_ONE = b'99900021'
    ABORT_ALL = b'99900022'
    ABORT_SETTING = b'99900023'

    CONFIG_CODE_BASE = b'9991'
    CONFIG_CODE_DEFAULTS = b'00'

    CODEID_DEFAULT_MAP = (
        (b'j', 'Code128'),
        (b'u', 'UCC/EAN-128'),
        (b'f', 'AIM128'),
        (b't', 'ISBT128'),
        (b'g', 'EAN-8'),
        (b'd', 'EAN-13'),
        (b'n', 'ISSN'),
        (b'B', 'ISBN'),
        (b'h', 'UPC-E'),
        (b'c', 'UPC-A'),
        (b'e', 'Interleaved 2 of 5'),
        (b'r', 'ITF-6'),
        (b'q', 'ITF-14'),
        (b'w', 'Deutshe14'),
        (b'l', 'Deutshe12'),
        (b'o', 'COOP25'),
        (b'v', 'Matrix 2 of 5'),
        (b'i', 'Industrial 25'),
        (b's', 'Standard 25'),
        (b'b', 'Code39'),
        (b'a', 'Codabar'),
        (b'y', 'Code93'),
        (b'z', 'Code11'),
        (b'p', 'Plessey'),
        (b'm', 'MSI-Plessey'),
        (b'R', 'GS1 Databar')
    )

    AIMID_MAP = {
        b']C0': ['Code128'],
        b']C1': ['UCC/EAN-128'],
        b']C2': ['AIM128'],
        b']C4': ['ISBT128'],
        b']E0': ['EAN-13', 'UPC-E', 'UPC-A'],
        b']E3': ['EAN-13+', 'UPC-E+', 'UPC-A+'],
        b']E4': ['EAN-8'],
        b']X0': ['ISSN', 'ISBN', 'Deutshe14', 'Deutshe12', 'COOP25', 'Matrix 2 of 5'],
        b']I0': ['Interleaved 2 of 5'],
        b']I1': ['Interleaved 2 of 5', 'ITF-6', 'ITF14'],
        b']I3': ['Interleaved 2 of 5', 'ITF-6', 'ITF14'],
        b']S0': ['Industrial 25'],
        b']R0': ['Standard 25'],
        b']A0': ['Code39'],
        b']A1': ['Code39'],
        b']A3': ['Code39'],
        b']A4': ['Code39'],
        b']A5': ['Code39'],
        b']A7': ['Code39'],
        b']F0': ['Codabar'],
        b']F2': ['Codabar'],
        b']F4': ['Codabar'],
        b']G0': ['Code93'],
        b']H0': ['Code11'],
        b']H1': ['Code11'],
        b']H3': ['Code11'],
        b']P0': ['Plessey'],
        b']M0': ['MSI-Plessey'],
        b']M1': ['MSI-Plessey'],
        b']e0': ['GS1 Databar']
    }

    QUERY_MAP = {
        'Product Information': b'99900300',
        'Hardware Version': b'99900301',
        'Product ID': b'99900302',
        'Manufacturing Date': b'99900303',
        'Product Name': b'99900304'
    }

    ENABLED_MAP = {
        False: b'01',
        True: b'02'
    }
    ADDENDA_2_DIGITS_MAP = {
        'disabled': b'05',
        'enabled': b'06',
        'only': b'07'
    }
    ADDENDA_5_DIGITS_MAP = {
        'disabled': b'10',
        'enabled': b'11',
        'only': b'12'
    }
    EXPAND_MAP1 = {
        'disabled': b'13',
        'enabled': b'14',
        'convert': b'15'
    }
    EXPAND_MAP2 = {
        'disabled': b'15',
        'enabled': b'16',
        'convert': b'17'
    }
    TRANSMIT_CHECK_MAP1 = {
        False: b'03',
        True: b'04'
    }
    TRANSMIT_CHECK_MAP2 = {
        False: b'11',
        True: b'12'
    }
    TRANSMIT_CHECK_MAP3 = {
        False: b'07',
        True: b'10'
    }
    DIGITS_COUNT_MAP = {
        10: b'03',
        13: b'04'
    }
    TRANSMIT_LEADING_0_MAP = {
        False: b'13',
        True: b'14'
    }
    CHECK_MODE_MAP1 = {
        'disabled': b'03',
        'enabled': b'04',
        'enabled+transmit': b'05'
    }
    CHECK_MODE_MAP2 = {
        'disabled': b'03',
        'enabled+transmit': b'04',
        'enabled': b'05',
    }
    CHECK_MODE_MAP3 = {
        'disabled': b'03',
        'mod11': b'04',
        'mod11/mod11': b'05',
        'mod11/mod9': b'06',
        'mod11+mod11/mod11': b'07',
        'mod11+mod11/mod9': b'10'
    }
    CHECK_MODE_MAP4 = {
        'disabled': b'03',
        'mod10': b'04',
        'mod10+mod10': b'05',
        'mod10+mod11': b'06'
    }
    TRANSMIT_START_AND_STOP_MAP1 = {
        False: b'06',
        True: b'07'
    }
    TRANSMIT_START_AND_STOP_MAP2 = {
        'disabled': b'06',
        'enabled': b'07',
        'ABCD/ABCD': b'10',
        'ABCD/TN*E': b'11',
        'abcd/abcd': b'12',
        'abcd/tn*e': b'13'
    }
    FULL_ASCII_DECODE_MAP = {
        False: b'10',
        True: b'11'
    }

    # used by Code128, UCC/EAN-128, AIM128
    CONFIGURATION_PATTERN1 = {
        'enabled': ENABLED_MAP,
        'codeid': b'05',
        'min_length': b'03',
        'max_length': b'04'
    }
    # used by EAN-8
    CONFIGURATION_PATTERN2 = {
        'enabled': ENABLED_MAP,
        'codeid': b'16',
        'addenda_2_digits_mode': ADDENDA_2_DIGITS_MAP,
        'addenda_5_digits_mode': ADDENDA_5_DIGITS_MAP,
        'expand_mode': EXPAND_MAP1,
        'transmit_check': TRANSMIT_CHECK_MAP1
    }
    # used by EAN-13
    CONFIGURATION_PATTERN3 = {
        'enabled': ENABLED_MAP,
        'codeid': b'13',
        'addenda_2_digits_mode': ADDENDA_2_DIGITS_MAP,
        'addenda_5_digits_mode': ADDENDA_5_DIGITS_MAP,
        'transmit_check': TRANSMIT_CHECK_MAP1
    }
    # used by ISSN
    CONFIGURATION_PATTERN4 = {
        'enabled': ENABLED_MAP,
        'codeid': b'03'
    }
    # used by ISBN
    CONFIGURATION_PATTERN5 = {
        'enabled': ENABLED_MAP,
        'codeid': b'05',
        'digits_count': DIGITS_COUNT_MAP
    }
    # used by UPC-E
    CONFIGURATION_PATTERN6 = {
        'enabled': ENABLED_MAP,
        'codeid': b'20',
        'addenda_2_digits_mode': ADDENDA_2_DIGITS_MAP,
        'addenda_5_digits_mode': ADDENDA_5_DIGITS_MAP,
        'transmit_leading_0': TRANSMIT_LEADING_0_MAP,
        'expand_mode': EXPAND_MAP2,
        'transmit_check': TRANSMIT_CHECK_MAP1
    }
    # used by UPC-A
    CONFIGURATION_PATTERN7 = {
        'enabled': ENABLED_MAP,
        'codeid': b'15',
        'addenda_2_digits_mode': ADDENDA_2_DIGITS_MAP,
        'addenda_5_digits_mode': ADDENDA_5_DIGITS_MAP,
        'transmit_leading_0': TRANSMIT_LEADING_0_MAP,
        'transmit_check': TRANSMIT_CHECK_MAP1
    }
    # used by Interleaved 2 of 5, Code93
    CONFIGURATION_PATTERN8 = {
        'enabled': ENABLED_MAP,
        'codeid': b'10',
        'check_mode': CHECK_MODE_MAP1,
        'min_length': b'06',
        'max_length': b'07'
    }
    # used by ITF-6
    CONFIGURATION_PATTERN9 = {
        'mode': {
            'enabled': b'01',
            'disabled': b'02',
            'enabled+transmit': b'03'
        },
        'codeid': b'04'
    }
    # used by ITF-14, Deutshe14, Deutshe12
    CONFIGURATION_PATTERN10 = {
        'mode': {
            'disabled': b'01',
            'enabled': b'02',
            'enabled+transmit': b'03'
        },
        'codeid': b'04'
    }
    # used by COOP25, Matrix 2 of 5, Industrial 25, Standard 25, Plessey
    CONFIGURATION_PATTERN11 = {
        'enabled': ENABLED_MAP,
        'codeid': b'10',
        'check_mode': CHECK_MODE_MAP2,
        'min_length': b'06',
        'max_length': b'07'
    }
    # used by Code39
    CONFIGURATION_PATTERN12 = {
        'enabled': ENABLED_MAP,
        'codeid': b'14',
        'check_mode': CHECK_MODE_MAP1,
        'transmit_start_and_stop': TRANSMIT_START_AND_STOP_MAP1,
        'full_ascii_decode': FULL_ASCII_DECODE_MAP,
        'min_length': b'12',
        'max_length': b'13'
    }
    # used by Codabar
    CONFIGURATION_PATTERN13 = {
        'enabled': ENABLED_MAP,
        'codeid': b'16',
        'check_mode': CHECK_MODE_MAP2,
        'start_and_stop_mode': TRANSMIT_START_AND_STOP_MAP2,
        'min_length': b'14',
        'max_length': b'15'
    }
    # used by Code11
    CONFIGURATION_PATTERN14 = {
        'enabled': ENABLED_MAP,
        'codeid': b'15',
        'check_mode': CHECK_MODE_MAP3,
        'transmit_check': TRANSMIT_CHECK_MAP2,
        'min_length': b'13',
        'max_length': b'14'
    }
    # used by MSI-Plessey
    CONFIGURATION_PATTERN15 = {
        'enabled': ENABLED_MAP,
        'codeid': b'13',
        'check_mode': CHECK_MODE_MAP4,
        'transmit_check': TRANSMIT_CHECK_MAP3,
        'min_length': b'11',
        'max_length': b'12'
    }
    # used by GS1 Databar
    CONFIGURATION_PATTERN16 = {
        'enabled': ENABLED_MAP,
        'codeid': b'03'
    }

    CONFIGURATION_MAP = {
        'Code128': dict(symbol_id=b'00', configuration=CONFIGURATION_PATTERN1),
        'UCC/EAN-128': dict(symbol_id=b'01', configuration=CONFIGURATION_PATTERN1),
        'AIM128': dict(symbol_id=b'02', configuration=CONFIGURATION_PATTERN1),
        'EAN-8': dict(symbol_id=b'04', configuration=CONFIGURATION_PATTERN2),
        'EAN-13': dict(symbol_id=b'05', configuration=CONFIGURATION_PATTERN3),
        'ISSN': dict(symbol_id=b'06', configuration=CONFIGURATION_PATTERN4),
        'ISBN': dict(symbol_id=b'07', configuration=CONFIGURATION_PATTERN5),
        'UPC-E': dict(symbol_id=b'10', configuration=CONFIGURATION_PATTERN6),
        'UPC-A': dict(symbol_id=b'11', configuration=CONFIGURATION_PATTERN7),
        'Interleaved 2 of 5': dict(symbol_id=b'12', configuration=CONFIGURATION_PATTERN8),
        'ITF-6': dict(symbol_id=b'13', configuration=CONFIGURATION_PATTERN9),
        'ITF-14': dict(symbol_id=b'14', configuration=CONFIGURATION_PATTERN10),
        'Deutshe14': dict(symbol_id=b'15', configuration=CONFIGURATION_PATTERN10),
        'Deutshe12': dict(symbol_id=b'16', configuration=CONFIGURATION_PATTERN10),
        'COOP25': dict(symbol_id=b'17', configuration=CONFIGURATION_PATTERN11),
        'Matrix 2 of 5': dict(symbol_id=b'20', configuration=CONFIGURATION_PATTERN11),
        'Industrial 25': dict(symbol_id=b'21', configuration=CONFIGURATION_PATTERN11),
        'Standard 25': dict(symbol_id=b'22', configuration=CONFIGURATION_PATTERN11),
        'Code39': dict(symbol_id=b'24', configuration=CONFIGURATION_PATTERN12),
        'Codabar': dict(symbol_id=b'25', configuration=CONFIGURATION_PATTERN13),
        'Code93': dict(symbol_id=b'26', configuration=CONFIGURATION_PATTERN8),
        'Code11': dict(symbol_id=b'27', configuration=CONFIGURATION_PATTERN14),
        'Plessey': dict(symbol_id=b'30', configuration=CONFIGURATION_PATTERN11),
        'MSI-Plessey': dict(symbol_id=b'31', configuration=CONFIGURATION_PATTERN15),
        'GS1 Databar': dict(symbol_id=b'32', configuration=CONFIGURATION_PATTERN16)
    }

    def __init__(self, port=None, *, baudrate: int = None, parity: str = None, byte_size: int = None,
                 stop_bits: int = None, logger=None):
        """Initialize instance of the FM100 object

        :param port: serial port to use. If string is passed, a new serial.Serial object is created (raising apropriate
                     exception on failure); if None is passed, an empty serial.Serial object is created (port is not
                     open until method is called). Defaults to None
        :type port: serial.Serial or str or None
        :param int baudrate: baudrate to be used by the serial port, no change is made if None is passed.
                             Defaults to None
        :param str parity: parity to be used by the serial port, no change is made if None is passed.
                           Defaults to None
        :param int byte_size: byte size to be used by the serial port, no change is made if None is passed.
                              Defaults to None
        :param int stop_bits: number of stop bits to be used by the serial port, no change is made if None is passed.
                              Defaults to None
        :param logger.Logger logger: logger to be used by the object, 'newland.FM100' is used by default
        """
        self._logger = logger or logging.getLogger('newland.FM100')
        self._port = None
        self._port_lock = threading.Lock()
        self._port_api_pending = False

        # assign port object to use
        if isinstance(port, serial.Serial):
            self._port = port
            self._logger.info('using user-supplied Serial object (%s)', port.port)
        elif isinstance(port, str):
            self._port = serial.Serial(port, exclusive=True)
            self._logger.info('using user-pointed device located at %s', port)
        elif port is None:
            self._port = serial.Serial(None, exclusive=True)
        else:
            raise TypeError('port must be a string or a Serial object')
        self._port.timeout = .5

        # configure port
        port_settings = {}
        if baudrate is not None:
            port_settings['baudrate'] = baudrate
        if parity is not None:
            port_settings['parity'] = parity
        if byte_size is not None:
            port_settings['bytesize'] = byte_size
        if stop_bits is not None:
            port_settings['stopbits'] = stop_bits
        try:
            if len(port_settings) > 0:
                self._port.apply_settings(port_settings)
        except Exception:
            self._port.close()
            raise
        finally:
            del port_settings

        self._thread_lock = threading.Lock()
        self._thread_cancel = threading.Event()
        self._thread = None

        self._callback = None
        self._callback_lock = threading.Lock()

        # code data format, used by dispatcher thread
        self._data_format_lock = threading.Lock()
        self._data_format = dict(prefix_sequence='',
                                 codeid_enabled=False,
                                 codeid=dict(),
                                 aim_enabled=False,
                                 user_prefix_enabled=False,
                                 user_prefix=b'',
                                 user_suffix_enabled=False,
                                 user_suffix=b'',
                                 terminal=None)
        self._reload_codeid()

    # ==============
    # STATIC METHODS
    # ==============

    @staticmethod
    def discover(limit: int = None):
        """Discover FM100 devices attached to the machine

        Gets all serial ports available and filters them by the VID and PID values. Returns a list of serial.Serial
        objects, returned ports are closed.

        :param int limit: limit maximum number of returned names, defaults to None (no limit)
        :rtype: list[serial.Serial]
        """
        if limit is not None and not isinstance(limit, int):
            raise TypeError('limit must be an integer')
        ret = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.vid == FM100.VID and port.pid == FM100.PID:
                dev = serial.Serial()
                dev.port = port.device
                ret.append(dev)
        if len(ret) > 0:
            if limit is not None:
                ret = ret[:limit]
            return ret
        else:
            logging.info('no device with matching VID and PID found')
        dev = serial.Serial(exclusive=True)
        dev.write_timeout = .5
        dev.timeout = 1
        for port in ports:
            dev.port = port.device
            for baudrate in [115200, 9600, 1200, 2400, 4800, 14400, 19200, 38400, 57600]:
                try:
                    dev.baudrate = baudrate
                except serial.SerialException:
                    logging.exception('failed to apply baudrate (%s): %d',
                                      port.device, baudrate, exc_info=False)
                    continue
                for parity in [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_MARK]:
                    try:
                        dev.parity = parity
                    except serial.SerialException:
                        logging.exception('failed to apply parity (%s): %s',
                                          port.device, parity, exc_info=False)
                        continue
                    for stopbits in [serial.STOPBITS_ONE, serial.STOPBITS_TWO]:
                        try:
                            dev.stopbits = stopbits
                        except serial.SerialException:
                            logging.exception('failed to apply stopbits (%s): %s',
                                              port.device, stopbits, exc_info=False)
                            continue
                        for bytesize in [7, 8]:
                            try:
                                dev.bytesize = bytesize
                            except serial.SerialException:
                                logging.exception('failed to apply bytesize (%s): %d',
                                                  port.device, bytesize, exc_info=False)
                                continue
                            try:
                                dev.open()
                            except serial.SerialException as e:
                                logging.exception('failed to open serial port (%s): %s',
                                                  port.device, e, exc_info=False)
                                break
                            try:
                                dev.write(b''.join([FM100.PROG_MODE_ENTER, FM100.PROG_MODE_EXIT]))
                                buf = bytearray()
                                while FM100.PROG_MODE_ON not in buf:
                                    tmp = dev.read()
                                    if tmp == b'':
                                        raise TimeoutError('PROG_MODE_ON sequence not received')
                                    buf += tmp
                                buf.clear()
                                while FM100.PROG_MODE_OFF not in buf:
                                    tmp = dev.read()
                                    if tmp == b'':
                                        raise TimeoutError('PROG_MODE_ON sequence not received')
                                    buf += tmp
                                logging.info(('device presence confirmed, port: %s, '
                                              'baudrate: %d, '
                                              'parity: %s, '
                                              'stopbits: %d, '
                                              'bytesize: %d'),
                                             port.device, baudrate, parity, stopbits, bytesize)
                                ret.append(dev)
                                break
                            except serial.SerialException as e:
                                logging.exception('serial port operation failed (%s): %s',
                                                  port.device, e, exc_info=False)
                                break
                            except TimeoutError as e:
                                logging.exception('communication timeout (%s): %s',
                                                  port.device, e, exc_info=False)
                            finally:
                                dev.close()
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
        if limit is not None:
            ret = ret[:limit]
        return ret

    @staticmethod
    def _hex_digit_code(digit: int):
        if not isinstance(digit, int):
            raise TypeError('digit must be an integer')
        if digit not in range(16):
            raise ValueError('digit must be in range(0, 16)')
        tmp = '{:02o}'.format(digit)
        return b''.join([FM100.DIGIT_CODE_BASE, tmp.encode()])

    @staticmethod
    def _validate_codeid(codeid):
        if not isinstance(codeid, (bytes, bytearray, str)):
            raise TypeError('Code ID must be a string or a bytes-like object')
        if isinstance(codeid, str):
            codeid = codeid.encode()
        if len(codeid) not in range(1, 3):
            raise IndexError('Code ID must be 1 or 2 letters')
        rr = [range(ord('A'), ord('Z') + 1), range(ord('a'), ord('z') + 1)]
        ret = []
        for s in codeid:
            if s not in rr[0] and s not in rr[1]:
                raise ValueError('Code ID must be 1 or 2 English letters, capital or small')
            ret.append(FM100._hex_digit_code(s >> 4))
            ret.append(FM100._hex_digit_code(s & 0xF))
        return ret

    @staticmethod
    def _validate_code_length(length: int):
        if not isinstance(length, int):
            raise TypeError('Code length must be an integer')
        if length not in range(256):
            raise ValueError('Code length must be in range(0, 256)')
        ss = '{}'.format(length)
        ret = []
        for s in ss:
            code = FM100._hex_digit_code(int(s))
            ret.append(code)
        return ret

    @staticmethod
    def _validate_prefix_suffix(sequence):
        if not isinstance(sequence, (bytes, bytearray, str)):
            raise TypeError('sequence must be a bytes-like object or a string')
        if isinstance(sequence, str):
            sequence = sequence.encode()
        if len(sequence) == 0:
            raise IndexError('sequence length must be greater than 0')
        ret = []
        for s in sequence:
            ret.append(FM100._hex_digit_code(s >> 4))
            ret.append(FM100._hex_digit_code(s & 0xF))
        return ret

    # ==============================
    # EXPOSED SERIAL PORT PROPERTIES
    # ==============================

    @property
    def port(self):
        """Name of the port to be used"""
        return self._port.port

    @port.setter
    def port(self, value: str):
        with self._port_lock:
            self._port.port = value

    @property
    def baudrate(self):
        """Baudrate of the serial port"""
        return self._port.get_settings()['baudrate']

    @baudrate.setter
    def baudrate(self, value):
        with self._port_lock:
            self._port.apply_settings({'baudrate': value})

    @property
    def parity(self):
        """Parity of the serial port"""
        return self._port.get_settings()['parity']

    @parity.setter
    def parity(self, value):
        with self._port_lock:
            self._port.apply_settings({'parity': value})

    @property
    def byte_size(self):
        """Byte size used by the serial port"""
        return self._port.get_settings()['bytesize']

    @byte_size.setter
    def byte_size(self, value):
        with self._port_lock:
            self._port.apply_settings({'bytesize': value})

    @property
    def stop_bits(self):
        """Number of stop bits used by the serial port"""
        return self._port.get_settings()['stopbits']

    @stop_bits.setter
    def stop_bits(self, value):
        with self._port_lock:
            self._port.apply_settings({'stopbits': value})

    @property
    def is_open(self):
        """Boolean flag indicating whether port is open"""
        return self._port.is_open

    # ========================================
    # CALLBACK PROPERTY AND INVOCATION WRAPPER
    # ========================================

    @property
    def callback(self):
        """Object to be invoked when the barcode is decoded

        The callback object is invoked with one positional argument (sender, instance of FM100 which scanned the code)
        and three keyword arguments:

        * data - the scanned code value,
        * aimid - AIM ID of the scanned code (optional),
        * codeid - CodeID of the scanned code (optional).
        """
        return self._callback

    @callback.setter
    def callback(self, value):
        if not callable(value):
            raise TypeError('callback must be callable')
        with self._callback_lock:
            self._callback = value

    def _invoke_callback(self, *args, **kwargs):
        with self._callback_lock:
            if self._callback is None:
                self._logger.info('no callback registered, args=%s, kwargs=%s', args, kwargs)
            else:
                try:
                    self._callback(self, *args, **kwargs)
                except Exception:
                    self._logger.exception('caught from callback')
        return

    # =================
    # PROTECTED HELPERS
    # =================

    def _reload_codeid(self):
        self._data_format['codeid'].clear()
        for codeid, symbology in self.CODEID_DEFAULT_MAP:
            self._data_format['codeid'][codeid] = [symbology]

    def _execute_command(self, commands):
        # validate commands to execute and prepare data to transmit
        if not isinstance(commands, list):
            commands = [commands]
        if len(commands) == 0:
            return
        for command in commands:
            if not isinstance(command, (bytes, bytearray)):
                raise TypeError('commands must be bytes-like objects')
            if len(command) != 8:
                raise ValueError('commands must consist of 8 digits')

        was_port_api_pending = self._port_api_pending
        self._port_api_pending = True
        try:
            with self._port_lock:
                # discard any pending data
                if self._port.in_waiting > 0:
                    self._logger.warning('discarding %d bytes', self._port.in_waiting)
                    self._port.reset_input_buffer()
                # enter configuration state
                txcnt = self._port.write(self.PROG_MODE_ENTER)
                if txcnt != len(self.PROG_MODE_ENTER):
                    raise RuntimeError('failed to send PROG_MODE_ENTER command (txcnt = {})'.format(txcnt))
                # confirm configuration state entered
                rxdata = self._port.read_until(self.PROG_MODE_ON)
                if rxdata[-4:] != self.PROG_MODE_ON:
                    raise RuntimeError('failed to enter programming mode (rxdata = {})'.format(rxdata))
                # send commands and receive responses
                rxdata = bytearray()
                for command in commands:
                    txcnt = self._port.write(b''.join([b'#', command, b';']))
                    if txcnt != 10:
                        raise RuntimeError('failed to send command: {}'.format(command))
                    tmp = self._port.read_until(command)
                    if tmp[-8:] != command:
                        raise RuntimeError('failed to receive response to command {}'.format(command))
                    rxdata += tmp
                    del tmp
                # exit programming mode
                txcnt = self._port.write(self.PROG_MODE_EXIT)
                if txcnt != len(self.PROG_MODE_EXIT):
                    raise RuntimeError('failed to send PROG_MODE_EXIT command (txcnt = {})'.format(txcnt))
                # confirm configuration state exitted
                tmp = self._port.read_until(self.PROG_MODE_OFF)
                if tmp[-4:] != self.PROG_MODE_OFF:
                    raise RuntimeError('failed to exit programming mode (rxdata = {})'.format(rxdata))
                rxdata += tmp
                del tmp
        except serial.SerialException as e:
            raise RuntimeError from e
        finally:
            self._port_api_pending = was_port_api_pending

        # process received data
        rxdata = rxdata[:-4]
        self._logger.debug('received data = %s', rxdata)
        # get response for each issued command
        responses = []
        commands_failed = []
        for command in commands:
            idx = rxdata.find(command)
            if idx < 0:
                raise BytesWarning('no response found for command %s', command)
            if rxdata[idx - 1:idx] != b'!':
                commands_failed.append(command)
            if rxdata[idx + 9:idx + 10] != b'&':
                responses.append(None)
                continue
            rsp = rxdata[idx + 11:rxdata.find(b'}', idx + 11)].split(b'|')
            if binascii.crc32(rsp[0]) != int(rsp[1], 16):
                raise RuntimeError('invalid CRC32 value for response to command %s', command)
            responses.append(rsp[0])
        if len(commands_failed) > 0:
            raise RuntimeError('failed to execute commands: {}'.format(commands_failed))
        return responses

    def _extract_codes(self, rxbuf):

        if self._data_format['user_suffix_enabled'] or self._data_format['terminal'] is not None:
            if self._data_format['terminal'] is not None:
                self._logger.debug('splitting data by Terminal sequence')
                data_list = rxbuf.split(self._data_format['terminal'])
                if self._data_format['user_suffix_enabled']:
                    # verify that each chunk ends with User Suffix, remove invalid chunks
                    validated = []
                    for data in data_list:
                        if data == b'':
                            continue
                        if not data.endswith(self._data_format['user_suffix']):
                            self._logger.warning('User Suffix not found, skipping data=%', data)
                            continue
                        validated.append(data[:-len(self._data_format['user_suffix'])])
                    data_list = validated
            else:
                self._logger.debug('splitting data by User Suffix')
                data_list = rxbuf.split(self._data_format['user_suffix'])
            # process each splitted chunk
            for data in data_list:
                if data == b'':
                    continue
                ret = dict()
                if self._data_format['aim_enabled']:
                    idx = data.find(b']')
                    if idx < 0:
                        self._logger.warning('aim id prefix not found, data=%s', data)
                        continue
                    ret['aimid'] = bytes(data[idx:idx + 3])
                    ret['data'] = bytes(data[idx + 3:])
                    data = data[:idx]
                    # verify User Prefix
                    if self._data_format['user_prefix_enabled']:
                        if self._data_format['prefix_sequence'].startswith('user'):
                            if not data.startswith(self._data_format['user_prefix']):
                                self._logger.warning('user prefix not found, ret=%s, data=%s', ret, data)
                                continue
                            data = data[len(self._data_format['user_prefix']):]
                        else:
                            if not data.endswith(self._data_format['user_prefix']):
                                self._logger.warning('user prefix not found, ret=%s, data=%s', ret, data)
                                continue
                            data = data[:-len(self._data_format['user_prefix'])]
                    # verify CodeID
                    if self._data_format['codeid_enabled']:
                        ret['codeid'] = bytes(data)
                    elif data != b'':
                        self._logger.warning('extra data found, ret=%s, data=%s', ret, data)
                # AIM ID is disabled, check User Prefix
                elif self._data_format['user_prefix_enabled']:
                    idx = data.find(self._data_format['user_prefix'])
                    if idx < 0:
                        self._logger.warning('user prefix not found, data=%s', data)
                        continue
                    if self._data_format['prefix_sequence'].startswith('user'):
                        # User Prefix precedes CodeID
                        data = data[len(self._data_format['user_prefix']):]
                        if self._data_format['codeid_enabled']:
                            # iterate through registered CodeIDs and extract it
                            for codeid in self._data_format['codeid']:
                                if data.startswith(codeid):
                                    ret['codeid'] = codeid
                                    ret['data'] = bytes(data[len(codeid):])
                                    break
                            else:
                                self._logger.warning('no matching CodeID found, data=%s', data)
                                continue
                        else:
                            ret['data'] = bytes(data)
                    else:
                        # User Prefix follows CodeID
                        ret['data'] = data[idx + len(self._data_format['user_prefix']):]
                        data = data[:idx]
                        # verify CodeID
                        if self._data_format['codeid_enabled']:
                            ret['codeid'] = bytes(data)
                        elif data != b'':
                            self._logger.warning('extra data found, ret=%s, data=%s', ret, data)
                # AIM ID disabled, User Prefix disabled, try to extract data based on CodeID
                elif self._data_format['codeid_enabled']:
                    # iterate through registered CodeIDs and extract it
                    for codeid in self._data_format['codeid']:
                        if data.startswith(codeid):
                            ret['codeid'] = codeid
                            ret['data'] = bytes(data[len(codeid):])
                            break
                    else:
                        self._logger.warning('no matching CodeID found, data=%s', data)
                        continue
                # all prefixes disabled
                else:
                    ret['data'] = bytes(data)
                yield ret
        # suffixes disabled, try to split data by User Prefix
        elif self._data_format['user_prefix_enabled']:
            self._logger.debug('splitting data by User Prefix')
            data_list = rxbuf.split(self._data_format['user_prefix'])
            if self._data_format['codeid_enabled'] and self._data_format['prefix_sequence'].startswith('codeid'):
                # related CodeID is at the end of previous chunk
                for i in range(1, len(data_list)):
                    data_current = data_list[i]
                    data_previous = data_list[i - 1]
                    ret = dict()
                    # get AIM ID
                    if self._data_format['aim_enabled']:
                        if not data_current.startswith(b']'):
                            self._logger.warning('AIM ID not found, data_current=%s', data_current)
                            continue
                        else:
                            ret['aimid'] = bytes(data_current[:3])
                            data_current = data_current[3:]
                    # identify current CodeID
                    for codeid in self._data_format['codeid']:
                        if data_previous.endswith(codeid):
                            ret['codeid'] = codeid
                            break
                    else:
                        self._logger.warning('no matching CodeID found, data_current=%s, data_previous=%s',
                                             data_current, data_previous)
                        continue
                    # extract code data (omit CodeID at the end)
                    if i == len(data_list) - 1:
                        # processing the last chunk, no CodeID to be expected
                        ret['data'] = bytes(data_current)
                    else:
                        for codeid in self._data_format['codeid']:
                            if data_current.endswith(codeid):
                                ret['data'] = bytes(data_current[:-len(codeid)])
                                break
                        else:
                            self._logger.warning('no mathing CodeID found, data_current=%s', data_current)
                            continue
                    yield ret
            else:
                # related CodeID is in the current chunk
                for data in data_list:
                    if data == b'':
                        continue
                    ret = dict()
                    # get CodeID
                    if self._data_format['codeid_enabled']:
                        for codeid in self._data_format['codeid']:
                            if data.startswith(codeid):
                                ret['codeid'] = codeid
                                data = data[len(codeid):]
                                break
                        else:
                            self._logger.warning('no matching CodeID found, data=%s', data)
                            continue
                    # get AIM ID
                    if self._data_format['aim_enabled']:
                        if not data.startswith(b']'):
                            self._logger.warning('AIM ID not found, data=%s', data)
                            continue
                        ret['aimid'] = bytes(data[:3])
                        data = data[3:]
                    # remaining data is the code
                    ret['data'] = bytes(data)
                    yield ret
        # suffixes disabled, User Prefix disabled, try to align data by AIM ID
        elif self._data_format['aim_enabled']:
            while len(rxbuf) > 0:
                idx = rxbuf.find(b']')
                while idx > 0 and bytes(rxbuf[idx:idx + 3]) not in self.AIMID_MAP:
                    idx = rxbuf.find(b']', idx + 1)
                if idx < 0:
                    self._logger.warning('AIM ID not found, data=%s', rxbuf)
                    break
                ret = dict()
                ret['aimid'] = bytes(rxbuf[idx:idx + 3])
                # determine CodeID
                if self._data_format['codeid_enabled']:
                    for codeid in self._data_format['codeid']:
                        if rxbuf[:idx].endswith(codeid):
                            ret['codeid'] = codeid
                            break
                    else:
                        self._logger.warning('no matching CodeID found, data=%s', rxbuf[:idx])
                        continue
                # locate end of code data
                idx_next = rxbuf.find(b']', idx + 3)
                while idx_next > 0 and bytes(rxbuf[idx_next:idx_next + 3]) not in self.AIMID_MAP:
                    idx_next = rxbuf.find(b']', idx_next + 1)
                if idx_next < 0:
                    # no more AIM IDs found
                    ret['data'] = bytes(rxbuf[idx + 3:])
                    rxbuf.clear()
                elif not self._data_format['codeid_enabled']:
                    # next AIM ID found, CodeID disabled
                    ret['data'] = bytes(rxbuf[idx + 3:idx_next])
                    rxbuf = rxbuf[idx_next:]
                else:
                    # validate next CodeID
                    for codeid in self._data_format['codeid']:
                        if rxbuf[:idx_next].endswith(codeid):
                            ret['data'] = bytes(rxbuf[idx + 3:idx_next - len(codeid)])
                            rxbuf = rxbuf[idx_next - len(codeid):]
                            break
                    else:
                        self._logger.warning('no matching CodeID found, data=%s', rxbuf[:idx_next])
                        continue
                yield ret
        # suffixes disabled, User Prefix and AIM ID disabled, try to align data by CodeID
        elif self._data_format['codeid_enabled']:
            while len(rxbuf) > 0:
                ret = dict()
                # identify leading CodeID
                for codeid in self._data_format['codeid']:
                    if rxbuf.startswith(codeid):
                        ret['codeid'] = codeid
                        rxbuf = rxbuf[len(codeid):]
                        break
                else:
                    self._logger.warning('no matching CodeID found, data=%s', rxbuf)
                    rxbuf = rxbuf[1:]
                    continue
                # locate next CodeID
                idxs = []
                for codeid in self._data_format['codeid']:
                    idx = rxbuf.find(codeid)
                    if idx > 0:
                        idxs.append(idx)
                if len(idxs) == 0:
                    # no more CodeIDs found
                    ret['data'] = bytes(rxbuf)
                    rxbuf.clear()
                else:
                    idx = min(idxs)
                    ret['data'] = bytes(rxbuf[:idx])
                    rxbuf = rxbuf[idx:]
                yield ret
        # suffixes disabled, prefixes disabled, unable to part data
        else:
            ret = dict()
            ret['data'] = bytes(rxbuf)
            yield ret

    def _dispatcher(self):
        self._logger.info('worker started')

        while not self._thread_cancel.is_set():
            # make sure serial port is open and no API access is pending
            if not self._port.is_open or self._port_api_pending:
                self._thread_cancel.wait(.5)
                continue

            # attempt to acquire port lock
            if not self._port_lock.acquire(timeout=.5):
                continue

            # keep receiving data until timeout
            rxbuf = bytearray()
            try:
                while True:
                    tmp = self._port.read()
                    if tmp == b'':
                        break
                    rxbuf += tmp
                del tmp
            except Exception as e:
                self._logger.exception('failed to read data from port')
                if isinstance(e, serial.SerialException):
                    continue
                break
            finally:
                self._port_lock.release()

            # inspect gathered data
            if len(rxbuf) == 0:
                continue
            self._logger.debug('processing gathered data (%d bytes): %s', len(rxbuf), rxbuf)
            for kwargs in self._extract_codes(rxbuf):
                self._invoke_callback(**kwargs)

        self._logger.info('worker returning')
        return

    # ==============
    # PUBLIC METHODS
    # ==============

    def open(self):
        """Opens the serial port

        :raises serial.SerialException:
        """
        with self._port_lock:
            self._port.open()
        return

    def close(self):
        """Closes the serial port"""
        with self._port_lock:
            self._port.close()
        return

    def start(self):
        """Starts dispatcher thread

        :raises RuntimeError: if thread is already running
        """
        with self._thread_lock:
            if self._thread is not None:
                raise RuntimeError('thread already started')
            self._thread = threading.Thread(name='fm100-dispatcher', target=self._dispatcher)
            self._thread.start()
        return

    def stop(self):
        """Stops dispatcher thread"""
        with self._thread_lock:
            if self._thread is None:
                return
            self._thread_cancel.set()
            self._thread.join()
            self._thread = None
            self._thread_cancel.clear()
        return

    def configure(self, source=None):
        """Performs device configuration

        :param source: source of the configuration data. Defaults to None, which means default configuration
                       (continuous scanning, security=4, beeper not muted, medium beeper frequency and volume,
                       user prefix enabled and set to b'\x02', AIM ID prefix enabled, CodeID prefix disabled,
                       user suffix enabled and set to b'\x03', terminal suffix disabled). Otherwise it may be a
                       dictionary or a path to configuration file
        :type source: None or str or configparser.ConfigParser
        """
        if source is not None and not isinstance(source, (str, configparser.ConfigParser)):
            raise TypeError('source must be either a string or a ConfigParser')
        if source is None or isinstance(source, configparser.ConfigParser):
            config = source
        else:
            config = configparser.ConfigParser()
            config.read(source)

        if source is None:
            self._logger.info('applying default configuration')
        self._configure_connection(config)
        if not self.is_open:
            self._logger.error('serial port is not open, skipping further configuration')
            return
        self._configure_scan_setup(config)
        self._configure_beeper_setup(config)
        self._configure_data_format(config)
        self._configure_symbologies(config)

    def _configure_connection(self, config: configparser.ConfigParser):
        if config is not None and not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')

        # serial port selection
        if self._port.port is not None:
            self._logger.info('serial port already selected')
        elif config is None \
                or not config.has_option('Connection', 'port') \
                or (config.has_option('Connection', 'port')
                    and (config.get('Connection', 'port') == 'auto' or config.get('Connection', 'port') == '')):
            for port in self.discover():
                self._port = port
                try:
                    self.open()
                    self._logger.info('successfully selected auto-discovered port: %s', port.port)
                    break
                except serial.SerialException:
                    self._logger.warning('failed to open auto-discovered port: %s', port.port)
            else:
                self._logger.error('failed to auto-configure serial port')
        elif config.has_option('Connection', 'port'):
            port_data = config.get('Connection', 'port').split(',')
            self._port.port = port_data[0]
            port_settings = dict()
            for i, (key, default) in enumerate([('baudrate', 9600),
                                                ('parity', serial.PARITY_NONE),
                                                ('bytesize', 8),
                                                ('stopbits', 1)]):
                try:
                    port_settings[key] = port_data[i]
                except IndexError:
                    port_settings[key] = default
            try:
                self._port.apply_settings(port_settings)
            except serial.SerialException as e:
                self._logger.exception('failed to apply serial port settings: %s', e, exc_info=False)
                return
            try:
                self._port.open()
            except serial.SerialException as e:
                self._logger.exception('failed to open serial device, configuration data: %s; error: %s',
                                       port_data, e, exc_info=False)
                return

        if config is None:
            return
        if not config.has_section('Connection'):
            self._logger.info('configuration has no "Connection" section')
            return

        # connection configuration
        kwargs = dict()
        for key in ['baudrate', 'stopbits', 'bytesize']:
            try:
                kwargs[key] = config.getint('Connection', key)
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "Connection.%s" option', key, exc_info=False)
        try:
            parity = config.get('Connection', 'parity')
            if parity not in ['N', 'O', 'E']:
                raise ValueError()
            kwargs['parity'] = parity
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "Connection.parity" option', exc_info=False)
        self.rs232_config(**kwargs)
        return

    def _configure_scan_setup(self, config: configparser.ConfigParser):
        if config is None:
            self._logger.info('applying default scanner configuration')
            self.scan_mode(mode='continuous', reading_time=1, interval_length=1, sensitivity='medium')
            self.scan_security(4)
            return

        if not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')
        if not config.has_section('ScanSetup'):
            self._logger.info('configuration has no "ScanSetup" section, not configuring')
            return

        kwargs = dict()
        for option in ['reading_time', 'interval_length']:
            try:
                kwargs[option] = config.getint('ScanSetup', option)
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "ScanSetup.%s" option', option, exc_info=False)
        try:
            mode = config.get('ScanSetup', 'mode')
            if mode not in ['interval', 'sensor', 'continuous', 'delayed', 'triggered']:
                raise ValueError()
            kwargs['mode'] = mode
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "ScanSetup.mode" option', exc_info=False)
        try:
            kwargs['sensitivity'] = config.getint('ScanSetup', 'sensitivity')
        except ValueError:
            sensitivity = config.get('ScanSetup', 'sensitivity')
            if sensitivity not in ['high', 'medium', 'low']:
                self._logger.error('invalid value of "ScanSetup.sensitivity" option')
            else:
                kwargs['sensitivity'] = sensitivity
        except configparser.NoOptionError:
            pass
        self.scan_mode(**kwargs)

        try:
            self.scan_security(config.getint('ScanSetup', 'security'))
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "ScanSetup.security" option', exc_info=False)

    def _configure_beeper_setup(self, config: configparser.ConfigParser):
        if config is None:
            self._logger.info('applying default beeper configuration')
            self.beeper_setup(frequency_volume='medium+medium', length=100)
            self.beeper_mute(False)
            return

        if not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')
        if not config.has_section('BeeperSetup'):
            self._logger.info('configuration has no "BeeperSetup" section, not configuring')
            return

        kwargs = dict()
        try:
            v = config.get('BeeperSetup', 'frequency_volume')
            if v not in ['high+loud', 'medium+loud', 'low+loud',
                         'high+medium', 'medium+medium', 'low+medium',
                         'high+low', 'medium+low', 'low+low']:
                raise ValueError()
            kwargs['frequency_volume'] = v
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "BeeperSetup.frequency_volume" option', exc_info=False)
        try:
            v = config.getint('BeeperSetup', 'length')
            if v not in [150, 100, 50]:
                raise ValueError()
            kwargs['length'] = v
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "BeeperSetup.length" option', exc_info=False)
        self.beeper_setup(**kwargs)

        try:
            self.beeper_mute(config.getboolean('BeeperSetup', 'mute'))
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "BeeperSetup.mute" option', exc_info=False)

    def _configure_data_format(self, config: configparser.ConfigParser):
        if config is None:
            self._logger.info('applying default data format configuration')
            self.prefix_sequence('codeid+user+aim')
            self.prefix_codeid(enabled=False)
            self.prefix_user(enabled=True, prefix='\x02')
            self.prefix_aim(True)
            self.suffix_user(enabled=True, suffix='\x03')
            self.suffix_terminal()
            return

        if not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')
        if not config.has_section('DataFormat'):
            self._logger.info('configuration has no "DataFormat" section, not configuring')
            return

        # Prefix Sequence
        try:
            self.prefix_sequence(config.get('DataFormat', 'prefix_sequence'))
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "prefix_sequence" option', exc_info=False)

        # CodeID
        kwargs = dict()
        for key in ['enabled', 'load_defaults']:
            option = ''.join(['codeid_', key])
            try:
                kwargs[key] = config.getboolean('DataFormat', option)
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value for option "DataFormat.%s", option', option, exc_info=False)
        self.prefix_codeid(**kwargs)

        # AIMID
        try:
            self.prefix_aim(config.getboolean('DataFormat', 'aimid_enabled'))
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "DataFormat.aimid_enabled" option', exc_info=False)

        # User Prefix and Suffix
        kwargs = dict(prefix=dict(), suffix=dict())
        for key in ['prefix', 'suffix']:
            what = '_'.join(['user', key])
            what_fmt = '_'.join([what, 'format'])
            what_en = '_'.join([what, 'enabled'])

            try:
                kwargs[key]['enabled'] = config.getboolean('DataFormat', what_en)
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "DataFormat.%s" option', what_en, exc_info=False)

            try:
                fmt = config.get('DataFormat', what_fmt)
                if fmt not in ['ascii', 'hex']:
                    raise ValueError()
            except configparser.NoOptionError:
                self._logger.info('no "DataFormat.%s" option, assuming ASCII', what_fmt)
                fmt = 'ascii'
            except ValueError:
                self._logger.exception('invalid value of "DataFormat.%s" option', what_fmt)
                continue

            try:
                v = config.get('DataFormat', what)
                if fmt == 'hex':
                    v = bytes.fromhex(v)
                kwargs[key][key] = v
            except configparser.NoOptionError:
                continue
            except ValueError:
                self._logger.exception('invalid value of "DataFormat.%s" option', what, exc_info=False)
        self.prefix_user(**kwargs['prefix'])
        self.suffix_user(**kwargs['suffix'])

        # Terminal
        try:
            terminal = [None, '\r', '\r\n']
            v = terminal[config.getint('DataFormat', 'terminal')]
            self.suffix_terminal(v)
        except configparser.NoOptionError:
            pass
        except (ValueError, IndexError):
            self._logger.exception('invalid value of "terminal" option', exc_info=False)

    def _configure_symbologies(self, config: configparser.ConfigParser):
        if config is None:
            self._logger.info('applying default symbologies configuration')
            for symbology in self.CONFIGURATION_MAP:
                self.config_generic(symbology, load_defaults=True)
            return

        if not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')

        for symbology in self.CONFIGURATION_MAP:
            configuration = self.CONFIGURATION_MAP[symbology]['configuration']
            kwargs = dict()
            for setting, values in configuration.items():
                if config.has_option(symbology, setting):
                    section = symbology
                elif config.has_option('DEFAULT', setting):
                    section = 'DEFAULT'
                else:
                    continue

                if setting == 'codeid':
                    kwargs[setting] = config.get(section, setting)
                elif setting.endswith('_length'):
                    try:
                        kwargs[setting] = config.getint(section, setting)
                    except ValueError:
                        self._logger.exception('invalid value of "%s.%s" option, expecting integer',
                                               section, setting, exc_info=False)
                elif type(list(values.keys())[0]) is bool:
                    try:
                        kwargs[setting] = config.getboolean(section, setting)
                    except ValueError:
                        self._logger.exception('invalid value of "%s.%s" option, expecting boolean',
                                               section, setting, exc_info=False)
                elif type(list(values.keys())[0]) is int:
                    try:
                        kwargs[setting] = config.getint(section, setting)
                    except ValueError:
                        self._logger.exception('invalid value of "%s.%s" option, expecting integer',
                                               section, setting, exc_info=False)
                else:
                    kwargs[setting] = config.get(section, setting)
            self.config_generic(symbology, **kwargs)

    # ===================
    # GENERAL PROGRAMMING
    # ===================

    def scan_mode(self, *, mode: str = None, reading_time: int = None, interval_length: int = None, sensitivity=None,
                  failure_char=None):
        """Configure scan mode

        Refer to FM100 Integration Guide for further details.

        :param mode: scan mode, possible values are: 'interval' (b'12'), 'sensor' (b'13'), 'continuous' (b'14'),
                     'delayed' (b'15') and 'triggered' (b'16')
        :type mode: str or bytes
        :param int reading_time: interpretation depends on mode, see FM100 Integration Guide
        :param int interval_length: interpretation depends on mode, see FM100 Integration Guide
        :param sensitivity: scanner sensitivity, possible values are: 'high' (b'52'), 'medium' (b'53'), 'low' (b'54')
                            or an integer in range(0, 16)
        :type sensitivity: str or bytes or int
        :param failure_char: character sent on scan failure
        :type failure_char: str or bytes or int
        :raises TypeError: if any of the passed arguments' type is invalid
        :raises ValueError: if any of the passed arguments' value is invalid
        :raises IndexError: if failure_char is passed as a string or bytes-like object and its length is other than 1
        :raises RuntimeError: if command execution failed
        """
        if mode is not None and not isinstance(mode, (bytes, bytearray, str)):
            raise TypeError('mode must be a bytes-like object or a string')
        if reading_time is not None and not isinstance(reading_time, int):
            raise TypeError('reading_time must be an integer')
        if interval_length is not None and not isinstance(interval_length, int):
            raise TypeError('interval_length must be an integer')
        if sensitivity is not None and not isinstance(sensitivity, (bytes, bytearray, str, int)):
            raise TypeError('sensitivity must be a bytes-like object, a string or an integer')
        if failure_char is not None and not isinstance(failure_char, (bytes, bytearray, str, int)):
            raise TypeError('failure_char must be a bytes-like object, a string or an integer')

        if mode is not None:
            if isinstance(mode, (bytes, bytearray)):
                if mode not in [b'12', b'13', b'14', b'15', b'16']:
                    raise ValueError('invalid mode')
            else:
                mode_map = {
                    'interval': b'12',
                    'sensor': b'13',
                    'continuous': b'14',
                    'delayed': b'15',
                    'triggered': b'16'
                }
                try:
                    mode = mode_map[mode.lower()]
                except KeyError:
                    raise ValueError('invalid mode')
            self._execute_command(b''.join([b'999001', mode]))
        if reading_time is not None:
            if reading_time not in range(16):
                raise ValueError('reading_time out of range')
            commands = [b'99900150',
                        self._hex_digit_code(reading_time // 10),
                        self._hex_digit_code(reading_time % 10)]
            self._execute_command(commands)
        if interval_length is not None:
            if interval_length not in range(16):
                raise ValueError('interval_length out of range')
            commands = [b'99900150',
                        self._hex_digit_code(interval_length // 10),
                        self._hex_digit_code(interval_length % 10)]
            self._execute_command(commands)
        if sensitivity is not None:
            if isinstance(sensitivity, (bytes, bytearray)):
                if sensitivity not in [b'52', b'53', b'54']:
                    raise ValueError('invalid sensitivity')
                self._execute_command(b''.join([b'999001', sensitivity]))
            elif isinstance(sensitivity, int):
                commands = [b'99900161',
                            self._hex_digit_code(sensitivity)]
                self._execute_command(commands)
            else:
                sensitivity_map = {
                    'high': b'52',
                    'medium': b'53',
                    'low': b'54'
                }
                try:
                    self._execute_command(b''.join([b'999001', sensitivity_map[sensitivity.lower()]]))
                except KeyError:
                    raise ValueError('invalid sensitivity')
        if failure_char is not None:
            if isinstance(failure_char, str):
                failure_char = failure_char.encode()
            if isinstance(failure_char, (bytes, bytearray)):
                if len(failure_char) != 1:
                    raise IndexError('failure_char must be a single character')
                failure_char = failure_char[0]
            commands = [b'99904200',
                        self._hex_digit_code(failure_char >> 4),
                        self._hex_digit_code(failure_char & 0xF)]
            self._execute_command(commands)

        return

    def scan_start(self):
        """Enable scanning

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        """
        self._execute_command(b'99900035')

    def scan_stop(self):
        """Disable scanning

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        """
        self._execute_command(b'99900036')

    def scan_security(self, level: int):
        """Set scan security

        Refer to FM100 Integration Guide for further details.

        :param int level: security level, integer in range(1, 5)
        :raises TypeError: if level is not an integer
        :raises ValueError: if level is out of range
        :raises RuntimeError: if command execution failed
        """
        if not isinstance(level, int):
            raise TypeError('security must be an integer')
        if level not in range(1, 5):
            raise ValueError('security must be in range(1, 5)')
        command = b''.join([b'9990012', str(level).encode()])
        self._execute_command(command)

    def beeper_setup(self, *, frequency_volume: str = None, length: int = None):
        """Configure beeper

        Refer to FM100 Integration Guide for further details.

        :param frequency_volume: beeper frequency and volume setting, possible values are: 'none' (b'30'),
                                 'high+loud' (b'31'), 'high+medium' (b'32'), 'high+low' (b'33'),
                                 'medium+loud' (b'34'), 'medium+medium' (b'35'), 'medium+low' (b'36'),
                                 'low+loud' (b'37'), 'low+medium' (b'40'), 'low+low' (b'41')
        :type frequency_volume: str or bytes
        :param length: duration of the beep (in ms), possible values are: 150 (b'42'), 100 (b'43'), 50 (b'44')
        :type length: int or bytes
        :raises TypeError: if any of the parameters' type is invalid
        :raises ValueError: if any of the parameters' value is invalid
        :raises RuntimeError: if command execution failed
        """
        if frequency_volume is not None and not isinstance(frequency_volume, (bytes, bytearray, str)):
            raise TypeError('frequency_volume must be a bytes-like object or a string')
        if length is not None and not isinstance(length, (bytes, bytearray, int)):
            raise TypeError('length must be an integer')
        commands = []
        if frequency_volume is not None:
            if isinstance(frequency_volume, (bytes, bytearray)):
                if frequency_volume not in [b'30', b'31', b'32', b'33', b'34', b'35', b'36', b'37', b'40', b'41']:
                    raise ValueError('invalid frequency_volume')
            else:
                frequency_volume_map = {
                    'none': b'30',
                    'high+loud': b'31',
                    'high+medium': b'32',
                    'high+low': b'33',
                    'medium+loud': b'34',
                    'medium+medium': b'35',
                    'medium+low': b'36',
                    'low+loud': b'37',
                    'low+medium': b'40',
                    'low+low': b'41'
                }
                try:
                    frequency_volume = frequency_volume_map[frequency_volume.lower()]
                except KeyError:
                    raise ValueError('invalid frequency_volume')
            commands.append(b''.join([b'999001', frequency_volume]))
        if length is not None:
            if isinstance(length, (bytes, bytearray)):
                if length not in [b'42', b'43', b'44']:
                    raise ValueError('invalid length')
            else:
                length_map = {
                    150: b'42',
                    100: b'43',
                    50: b'44'
                }
                try:
                    length = length_map[length]
                except KeyError:
                    raise ValueError('invalid length')
            commands.append(b''.join([b'999001', length]))

        self._execute_command(commands)

    def beeper_mute(self, muted: bool):
        """Temporarily mute beeper

        Refer to FM100 Integration Guide for further details.

        :param bool muted: True to mute beeper, False to unmute
        :raises TypeError: if muted is not a boolean
        :raises RuntimeError: if command execution failed
        """
        if not isinstance(muted, bool):
            raise TypeError('muted must be a boolean')
        if muted:
            self._execute_command(b'99900040')
        else:
            self._execute_command(b'99900041')

    # ==============
    # QUERY COMMANDS
    # ==============

    def query_product_information(self):
        """Query 'Product Information' field

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        :rtype: str
        """
        return self.query('Product Information')

    def query_hardware_version(self):
        """Query 'Hardware Version' field

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        :rtype: str
        """
        return self.query('Hardware Version')

    def query_product_id(self):
        """Query 'Product ID' field

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        :rtype: str
        """
        return self.query('Product ID')

    def query_manufacturing_date(self):
        """Query 'Manufacturing Date' field

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        :rtype: str
        """
        return self.query('Manufacturing Date')

    def query_product_name(self):
        """Query 'Product Name' field

        Refer to FM100 Integration Guide for further details.

        :raises RuntimeError: if command execution failed
        :rtype: str
        """
        return self.query('Product Name')

    def query(self, what: str = 'all'):
        """Query device information

        Refer to FM100 Integration Guide for further details.

        :param what: fields to query, possible values: 'all', 'Product Information', 'Hardware Version',
                     'Product ID', 'Manufacturing Date', 'Product Name'. Value may be a single property - a single
                     string is returned in that case; in case 'all' properties are queried (or their subset, when
                     passing a list of properties), a dictionary is returned
        :type what: str or list[str]
        :raises TypeError: if argument is neither a string nor a list
        :raises ValueError: if unknown property is queried
        :raises RuntimeError: if command execution failed
        :rtype: str or dict
        """
        if not isinstance(what, (list, str)):
            raise TypeError('what must be a list or a string')
        if isinstance(what, str):
            if what == 'all':
                commands = []
                for key, code in self.QUERY_MAP.items():
                    commands.append(code)
                responses = self._execute_command(commands)
                ret = dict()
                for key, response in zip(self.QUERY_MAP.keys(), responses):
                    ret[key] = response.decode()
            else:
                try:
                    ret = self._execute_command(self.QUERY_MAP[what])[0].decode()
                except KeyError:
                    raise ValueError('invalid proprty to query: {}'.format(what))
        else:
            commands = []
            for key in what:
                try:
                    commands.append(self.QUERY_MAP[key])
                except KeyError:
                    raise ValueError('invalid proprty to query: {}'.format(key))
            responses = self._execute_command(commands)
            ret = dict()
            for key, response in zip(what, responses):
                ret[key] = response.decode()
        return ret

    # ===================
    # COMMUNICATION SETUP
    # ===================

    def rs232_config(self, *, baudrate: int = None, parity: str = None, stopbits: int = None, bytesize: int = None):
        """Configure RS232 interface

        Refer to FM100 Integration Guide for further details.
        Each property is configured independently, i.e. each change is immediately reflected in serial port
        configuration - no manual adjustment is needed after execution of this method.

        :param int baudrate:
        :param str parity: possible values: 'N' - none, 'E' - even, 'O' - odd
        :param int stopbits: 1 or 2
        :param int bytesize: 7 or 8
        :raises TypeError: if any of the parameters' type is invalid
        :raises ValueError: if any of the parameters' value is not supported
        :raises RuntimeError: if command execution failed
        :raises serial.SerialException: if port configuration failed
        """
        if baudrate is not None and not isinstance(baudrate, int):
            raise TypeError('baudrate must be an integer')
        if parity is not None and not isinstance(parity, str):
            raise TypeError('parity must be a string')
        if stopbits is not None and not isinstance(stopbits, int):
            raise TypeError('stopbits must be an integer')
        if bytesize is not None and not isinstance(bytesize, int):
            raise TypeError('bytesize must be an integer')

        commands = []
        settings = dict()
        if baudrate is not None:
            baudrate_map = {1200: b'01',
                            2400: b'02',
                            4800: b'03',
                            9600: b'04',
                            14400: b'05',
                            19200: b'06',
                            38400: b'07',
                            57600: b'10',
                            115200: b'11'}
            if baudrate not in baudrate_map:
                raise ValueError('baudrate value not supported')
            commands.append(b''.join([b'999021', baudrate_map[baudrate]]))
            settings['baudrate'] = baudrate
        if parity is not None:
            parity_map = {serial.PARITY_NONE: b'20',
                          serial.PARITY_ODD: b'21',
                          serial.PARITY_EVEN: b'22'}
            if parity not in parity_map:
                raise ValueError('parity value not supported')
            commands.append(b''.join([b'999021', parity_map[parity]]))
            settings['parity'] = parity
        if stopbits is not None:
            stopbits_map = {serial.STOPBITS_ONE: b'31',
                            serial.STOPBITS_TWO: b'33'}
            if stopbits not in stopbits_map:
                raise ValueError('stopbits value not supported')
            commands.append(b''.join([b'999021', stopbits_map[stopbits]]))
            settings['stopbits'] = stopbits
        if bytesize is not None:
            bytesize_map = {7: b'51', 8: b'50'}
            if bytesize not in bytesize_map:
                raise ValueError('bytesize value not supported')
            commands.append(b''.join([b'999021', bytesize_map[bytesize]]))
            settings['bytesize'] = bytesize

        if len(commands) > 0:
            self._port_api_pending = True
            try:
                self._execute_command(commands)
                self._port.apply_settings(settings)
            finally:
                self._port_api_pending = False

    def usb_mode(self, mode=None):
        """Configure USB interface of the device

        Refer to FM100 Integration Guide for further details.

        :param mode: mode to use, possible values are: ('hid', 'kbw', 'keyboard', 0, b'0', b'00') or
                     ('com', 'serial', 1, b'1', b'01')
        :type mode: str or int or bytes
        :raises TypeError: if type of argument is invalid
        :raises ValueError: if mode value is out of range
        :raises RuntimeError: if command execution failed
        """
        if mode is None:
            return
        if isinstance(mode, int):
            if mode == 0:
                command = b'99902300'
            elif mode == 1:
                command = b'99902301'
            else:
                raise ValueError('invalid mode')
        elif isinstance(mode, (bytes, bytearray)):
            if mode == b'0' or mode == b'00':
                command = b'99902300'
            elif mode == b'1' or mode == b'01':
                command = b'99902301'
            else:
                raise ValueError('invalid mode')
        elif isinstance(mode, str):
            if mode.lower() in ['hid', 'kbw', 'keyboard']:
                command = b'99902300'
            elif mode.lower() in ['com', 'serial']:
                command = b'99902301'
            else:
                raise ValueError('invalid mode')
        else:
            raise TypeError('mode must be an integer, a bytes-like object or a string')
        self._execute_command(command)

    # ===========
    # DATA FORMAT
    # ===========

    def prefix_sequence(self, sequence: str):
        """Configure prefix sequence

        Refer to FM100 Integration Guide for further details.
        Any change made to data format is tracked and taken into consideration by the dispatcher.

        :param sequence: possible values: 'codeid+user+aim' (b'10'), 'user+codeid+aim' (b'11')
        :type sequence: str or bytes
        :raises TypeError: if sequence is neither a string nor a bytes-like object
        :raises ValueError: if sequence value is not supported
        :raises RuntimeError: if command execution failed
        """
        if not isinstance(sequence, (bytes, bytearray, str)):
            raise TypeError('sequence must be a bytes-like object or a string')
        command_base = b'999040'
        if isinstance(sequence, (bytes, bytearray)):
            if sequence not in [b'10', b'11']:
                raise ValueError('invalid sequence')
            command = b''.join([command_base, sequence])
            if sequence == b'10':
                prefix_sequence = 'codeid+user+aim'
            else:
                prefix_sequence = 'user+codeid+aim'
        else:
            sequence_map = {
                'codeid+user+aim': b'10',
                'user+codeid+aim': b'11'
            }
            try:
                command = b''.join([command_base, sequence_map[sequence.lower()]])
                prefix_sequence = sequence.lower()
            except KeyError:
                raise ValueError('invalid sequence')

        with self._data_format_lock:
            self._execute_command(command)
            self._data_format['prefix_sequence'] = prefix_sequence

    def prefix_user(self, *, enabled: bool = None, prefix: str = None):
        """Configure User Prefix

        Refer to FM100 Integration Guide for further details.
        Any change made to data format is tracked and taken into consideration by the dispatcher.

        :param bool enabled: whether User Prefix is used or not
        :param prefix: prefix value
        :type prefix: str or bytes
        :raises TypeError: if enabled is not a boolean or prefix is neither a string nor a bytes-like object
        :raises IndexError: if prefix length is 0
        :raises RuntimeError: if command execution failed
        """
        if enabled is not None and not isinstance(enabled, bool):
            raise TypeError('enabled must be a boolean')
        if prefix is not None and not isinstance(prefix, (bytes, bytearray, str)):
            raise TypeError('prefix must be a bytes-like object or a string')
        commands = []
        if enabled is not None:
            if enabled:
                commands.append(b'99904021')
            else:
                commands.append(b'99904020')
        if prefix is not None:
            commands.append(b'99904022')
            commands.extend(self._validate_prefix_suffix(prefix))
            commands.append(self.STORE)

        with self._data_format_lock:
            self._execute_command(commands)
            if enabled is not None:
                self._data_format['user_prefix_enabled'] = enabled
            if prefix is not None:
                if isinstance(prefix, str):
                    self._data_format['user_prefix'] = prefix.encode()
                else:
                    self._data_format['user_prefix'] = prefix

    def prefix_aim(self, enabled: bool = None):
        """Enable or disable AIM ID prefix

        Refer to FM100 Integration Guide for further details.
        Any change made to data format is tracked and taken into consideration by the dispatcher.

        :param bool enabled: True to enable AIM ID prefix, False to disable it
        :raises TypeError: if enabled is not a boolean
        :raises RuntimeError: if command execution failed
        """
        if enabled is None:
            return
        if not isinstance(enabled, bool):
            raise TypeError('enabled must be a boolean')
        if enabled:
            command = b'99904031'
        else:
            command = b'99904030'

        with self._data_format_lock:
            self._execute_command(command)
            self._data_format['aim_enabled'] = enabled

    def prefix_codeid(self, *, enabled: bool = None, load_defaults: bool = False):
        """Configure CodeID prefix

        Refer to FM100 Integration Guide for further details.
        Any change made to data format is tracked and taken into consideration by the dispatcher.

        :param bool enabled: True to enable CodeID prefix, False to disable it
        :param bool load_defaults: True to restore default CodeID configuration for all symbologies
        :raises TypeError: if parameters are not a boolean values
        :raises RuntimeError: if command execution failed
        """
        if enabled is not None and not isinstance(enabled, bool):
            raise TypeError('enabled must be a boolean')
        if load_defaults is not None and not isinstance(load_defaults, bool):
            raise TypeError('load_defaults must be a boolean')
        commands = []
        if enabled is not None:
            if enabled:
                commands.append(b'99904041')
            else:
                commands.append(b'99904040')
        if load_defaults:
            commands.append(b'99904042')

        with self._data_format_lock:
            self._execute_command(commands)
            if enabled is not None:
                self._data_format['codeid_enabled'] = enabled
            if load_defaults:
                self._reload_codeid()

    def suffix_user(self, *, enabled: bool = None, suffix: str = None):
        """Configure User Suffix

        Refer to FM100 Integration Guide for further details.
        Any change made to data format is tracked and taken into consideration by the dispatcher.

        :param bool enabled: enable or disable User Suffix
        :param suffix: suffix value
        :type suffix: str or bytes
        :raises TypeError: if enabled is not a boolean value or suffix is neither a string nor a bytes-like object
        :raises IndexError: if length of suffix is 0
        :raises RuntimeError: if command execution failed
        """
        if enabled is not None and not isinstance(enabled, bool):
            raise TypeError('enabled must be a boolean')
        if suffix is not None and not isinstance(suffix, (bytes, bytearray, str)):
            raise TypeError('suffix must be a bytes-like object or a string')
        commands = []
        if enabled is not None:
            if enabled:
                commands.append(b'99904101')
            else:
                commands.append(b'99904100')
        if suffix is not None:
            commands.append(b'99904102')
            commands.extend(self._validate_prefix_suffix(suffix))
            commands.append(self.STORE)

        with self._data_format_lock:
            self._execute_command(commands)
            if enabled is not None:
                self._data_format['user_suffix_enabled'] = enabled
            if suffix is not None:
                if isinstance(suffix, str):
                    self._data_format['user_suffix'] = suffix.encode()
                else:
                    self._data_format['user_suffix'] = suffix

    def suffix_terminal(self, terminal: str = None):
        """Configure Terminal sequence

        Refer to FM100 Integration Guide for further details.
        Any change made to data format is tracked and taken into consideration by the dispatcher.

        :param terminal: terminal sequence to use, possible values are None (or empty string - terminal disabled),
                         '\r' or '\r\n'
        :type terminal: str or bytes
        :raises TypeError: if terminal is neither a string nor a bytes-like object
        :raises ValueError: if terminal value is not supported
        :raises RuntimeError: if command execution failed
        """
        if terminal is not None and not isinstance(terminal, (bytes, bytearray, str)):
            raise TypeError('terminal must be a bytes-like object or a string')
        commands = []
        if terminal is None or len(terminal) == 0:
            commands.append(b'99904110')
        else:
            if isinstance(terminal, str):
                terminal = terminal.encode()
            commands.append(b'99904112')
            if terminal == b'\r':
                commands.append(b'99904113')
            elif terminal == b'\r\n':
                commands.append(b'99904114')
            else:
                raise ValueError('invalid terminal')

        with self._data_format_lock:
            self._execute_command(commands)
            if terminal is None or len(terminal) == 0:
                self._data_format['terminal'] = None
            else:
                self._data_format['terminal'] = terminal
        return

    # =======
    # SYMBOLS
    # =======

    def config_generic(self, symbology: str, *, load_defaults: bool = False, **kwargs):
        """Configure symbology

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param str symbology: symbology to configure, see :ref:`~FM100.SYMBOLS`
        :param bool load_defaults: whether to restore factory default configuration prior to applying other settings
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """

        try:
            symbol_id = self.CONFIGURATION_MAP[symbology]['symbol_id']
            configuration = self.CONFIGURATION_MAP[symbology]['configuration']
        except KeyError:
            raise ValueError('invalid symbology name')
        commands = []
        if load_defaults:
            commands.append(b''.join([self.CONFIG_CODE_BASE, symbol_id, b'00']))
        for key, value in kwargs.items():
            try:
                setting = configuration[key]
            except KeyError:
                self._logger.exception('%s is not a valid setting for %s', key, symbology, exc_info=False)
                continue
            if key == 'codeid':
                commands.append(b''.join([self.CONFIG_CODE_BASE, symbol_id, setting]))
                codes = self._validate_codeid(value)
                commands.extend(codes)
                if len(codes) == 1:
                    commands.append(self.STORE)
            elif key.endswith('_length'):
                commands.append(b''.join([self.CONFIG_CODE_BASE, symbol_id, setting]))
                codes = self._validate_code_length(value)
                commands.extend(codes)
                if len(codes) < 3:
                    commands.append(self.STORE)
            else:
                try:
                    commands.append(b''.join([self.CONFIG_CODE_BASE, symbol_id, setting[value]]))
                except KeyError:
                    self._logger.exception('%s is not a valid value for setting %s.%s', value, symbology, key,
                                           exc_info=False)

        if 'codeid' in kwargs or load_defaults:
            with self._data_format_lock:
                self._execute_command(commands)
                # remove symbology name from registered codeids
                for k, v in self._data_format['codeid'].items():
                    if symbology in v:
                        v.remove(symbology)
                        if len(v) == 0:
                            del self._data_format['codeid'][k]
                        break
                # update codeid for selected symbology
                codeid = None
                if 'codeid' in kwargs:
                    codeid = kwargs['codeid']
                    if isinstance(codeid, str):
                        codeid = codeid.encode()
                else:
                    # using default codeid
                    for codeid, name in self.CODEID_DEFAULT_MAP:
                        if symbology == name:
                            break
                if codeid in self._data_format['codeid']:
                    # codeid already used, extend list
                    self._data_format['codeid'][codeid].append(symbology)
                else:
                    self._data_format['codeid'][codeid] = [symbology]
        else:
            self._execute_command(commands)

    def config_code128(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                       min_length: int = None, max_length: int = None):
        """Configure Code128

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        self.config_generic('Code128', **kwargs)

    def config_ucc_ean_128(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                           min_length: int = None, max_length: int = None):
        """Configure UCC/EAN-128 symbology

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        self.config_generic('UCC/EAN-128', **kwargs)

    def config_aim128(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                      min_length: int = None, max_length: int = None):
        """Configure AIM-128 symbology

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        self.config_generic('AIM128', **kwargs)

    def config_ean_8(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                     addenda_2_digits_mode: str = None, addenda_5_digits_mode: str = None, expand_mode: str = None,
                     transmit_check: bool = None):
        """Configure EAN-8

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str addenda_2_digits_mode: 'disabled', 'enabled', 'only'
        :param str addenda_5_digits_mode: 'disabled', 'enabled', 'only'
        :param str expand_mode: 'disabled', 'enabled', 'convert'
        :param bool transmit_check: whether or not to transmit check digit
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if addenda_2_digits_mode is not None:
            kwargs['addenda_2_digits_mode'] = addenda_2_digits_mode
        if addenda_5_digits_mode is not None:
            kwargs['addenda_5_digits_mode'] = addenda_5_digits_mode
        if expand_mode is not None:
            kwargs['expand_mode'] = expand_mode
        if transmit_check is not None:
            kwargs['transmit_check'] = transmit_check
        self.config_generic('EAN-8', **kwargs)

    def config_ean_13(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                      addenda_2_digits_mode: str = None, addenda_5_digits_mode: str = None,
                      transmit_check: bool = None):
        """Configure EAN-13

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str addenda_2_digits_mode: 'disabled', 'enabled', 'only'
        :param str addenda_5_digits_mode: 'disabled', 'enabled', 'only'
        :param bool transmit_check: whether or not to transmit check digit
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if addenda_2_digits_mode is not None:
            kwargs['addenda_2_digits_mode'] = addenda_2_digits_mode
        if addenda_5_digits_mode is not None:
            kwargs['addenda_5_digits_mode'] = addenda_5_digits_mode
        if transmit_check is not None:
            kwargs['transmit_check'] = transmit_check
        self.config_generic('EAN-13', **kwargs)

    def config_issn(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None):
        """Configure ISSM

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        self.config_generic('ISSN', **kwargs)

    def config_isbn(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                    digits_count: int = None):
        """Configure ISBN

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int digits_count: 10 or 13
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if digits_count is not None:
            kwargs['digits_count'] = digits_count
        self.config_generic('ISBN', **kwargs)

    def config_upc_e(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                     addenda_2_digits_mode: str = None, addenda_5_digits_mode: str = None, expand_mode: str = None,
                     transmit_check: bool = None, transmit_leading_0: bool = None):
        """Configure UPC-E

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str addenda_2_digits_mode: 'disabled', 'enabled', 'only'
        :param str addenda_5_digits_mode: 'disabled', 'enabled', 'only'
        :param str expand_mode: 'disabled', 'enabled', 'convert'
        :param bool transmit_check: whether or not to transmit check digit
        :param bool transmit_leading_0: whether or not to transmit leading 0s
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if addenda_2_digits_mode is not None:
            kwargs['addenda_2_digits_mode'] = addenda_2_digits_mode
        if addenda_5_digits_mode is not None:
            kwargs['addenda_5_digits_mode'] = addenda_5_digits_mode
        if expand_mode is not None:
            kwargs['expand_mode'] = expand_mode
        if transmit_check is not None:
            kwargs['transmit_check'] = transmit_check
        if transmit_leading_0 is not None:
            kwargs['transmit_leading_0'] = transmit_leading_0
        self.config_generic('UPC-E', **kwargs)

    def config_upc_a(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                     addenda_2_digits_mode: str = None, addenda_5_digits_mode: str = None, transmit_check: bool = None,
                     transmit_leading_0: bool = None):
        """Configure UPC-A

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str addenda_2_digits_mode: 'disabled', 'enabled', 'only'
        :param str addenda_5_digits_mode: 'disabled', 'enabled', 'only'
        :param bool transmit_check: whether or not to transmit check digit
        :param bool transmit_leading_0: whether or not to transmit leading 0s
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if addenda_2_digits_mode is not None:
            kwargs['addenda_2_digits_mode'] = addenda_2_digits_mode
        if addenda_5_digits_mode is not None:
            kwargs['addenda_5_digits_mode'] = addenda_5_digits_mode
        if transmit_check is not None:
            kwargs['transmit_check'] = transmit_check
        if transmit_leading_0 is not None:
            kwargs['transmit_leading_0'] = transmit_leading_0
        self.config_generic('UPC-A', **kwargs)

    def config_interleaved_2_of_5(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                                  min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure Interleaved 2 of 5

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('Interleaved 2 of 5', **kwargs)

    def config_itf_6(self, *, load_defaults: bool = False, codeid: str = None, mode: str = None):
        """Configure ITF-6

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if mode is not None:
            kwargs['mode'] = mode
        if codeid is not None:
            kwargs['codeid'] = codeid
        self.config_generic('ITF-6', **kwargs)

    def config_itf_14(self, *, load_defaults: bool = False, codeid: str = None, mode: str = None):
        """Configure ITF-14

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if mode is not None:
            kwargs['mode'] = mode
        if codeid is not None:
            kwargs['codeid'] = codeid
        self.config_generic('ITF-14', **kwargs)

    def config_deutshe14(self, *, load_defaults: bool = False, codeid: str = None, mode: str = None):
        """Configure Deutshe14

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if mode is not None:
            kwargs['mode'] = mode
        if codeid is not None:
            kwargs['codeid'] = codeid
        self.config_generic('Deutshe14', **kwargs)

    def config_deutshe12(self, *, load_defaults: bool = False, codeid: str = None, mode: str = None):
        """Configure Deutshe12

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param str mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if mode is not None:
            kwargs['mode'] = mode
        if codeid is not None:
            kwargs['codeid'] = codeid
        self.config_generic('Deutshe12', **kwargs)

    def config_coop25(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                      min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure COOP25 (Japanese Matrix 2 of 5)

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('COOP25', **kwargs)

    def config_matrix_2_of_5(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                             min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure Matrix 2 of 5

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('Matrix 2 of 5', **kwargs)

    def config_industrial_25(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                             min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure Industrial 25

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('Industrial 25', **kwargs)

    def config_standard_25(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                           min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure Standard 25

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('Standard 25', **kwargs)

    def config_code39(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                      min_length: int = None, max_length: int = None, check_mode: str = None,
                      transmit_start_and_stop: bool = None, full_ascii_decode: bool = None):
        """Configure Code39

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :param bool transmit_start_and_stop: whether or not to transmit start and stop characters
        :param bool full_ascii_decode: whether or not to perform full ASCII decoding
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        if transmit_start_and_stop is not None:
            kwargs['transmit_start_and_stop'] = transmit_start_and_stop
        if full_ascii_decode is not None:
            kwargs['full_ascii_decode'] = full_ascii_decode
        self.config_generic('Code39', **kwargs)

    def config_codabar(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                       min_length: int = None, max_length: int = None, check_mode: str = None,
                       start_and_stop_mode: str = None):
        """Configure Codabar

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :param str start_and_stop_mode: 'disabled', 'enabled', 'ABCD/ABCD', 'ABCD/TN*E', 'abcd/abcd', 'abcd/tn*e'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        if start_and_stop_mode is not None:
            kwargs['start_and_stop_mode'] = start_and_stop_mode
        self.config_generic('Codabar', **kwargs)

    def config_code93(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                      min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure Code93

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('Code93', **kwargs)

    def config_code11(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                      min_length: int = None, max_length: int = None, check_mode: str = None,
                      transmit_check: bool = None):
        """Configure Code11

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'mod11', 'mod11/mod11', 'mod11/mod9', 'mod11+mod11/mod11', 'mod11+mod11/mod9'
        :param bool transmit_check: whether or not to transmit check digit
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        if transmit_check is not None:
            kwargs['transmit_check'] = transmit_check
        self.config_generic('Code11', **kwargs)

    def config_plessey(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                       min_length: int = None, max_length: int = None, check_mode: str = None):
        """Configure Plessey

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'enabled', 'enabled+transmit'
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        self.config_generic('Plessey', **kwargs)

    def config_msi_plessey(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None,
                           min_length: int = None, max_length: int = None, check_mode: str = None,
                           transmit_check: bool = None):
        """Configure MSI-Plessey

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :param int min_length: minimal length of message to be decoded
        :param int max_length: maximal length of message to be decoded
        :param str check_mode: 'disabled', 'mod10', 'mod10+mod10', 'mod10+mod11'
        :param bool transmit_check: whether or not to transmit check digit
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        if min_length is not None:
            kwargs['min_length'] = min_length
        if max_length is not None:
            kwargs['max_length'] = max_length
        if check_mode is not None:
            kwargs['check_mode'] = check_mode
        if transmit_check is not None:
            kwargs['transmit_check'] = transmit_check
        self.config_generic('MSI-Plessey', **kwargs)

    def config_gs1_databar(self, *, load_defaults: bool = False, enabled: bool = None, codeid: str = None):
        """Configure GS1 Databar

        Refer to FM100 Integration Guide for further details.
        Any change made to CodeID is tracked and taken into consideration by the dispatcher.

        :param bool load_defaults: whether to restore factory defaults prior to applying other settings
        :param bool enabled: whether to use symbology
        :param codeid: CodeID to be used with this symbology
        :type codeid: str or bytes
        :raises TypeError:
        :raises ValueError:
        :raises RuntimeError: if command execution failed
        """
        kwargs = dict(load_defaults=load_defaults)
        if enabled is not None:
            kwargs['enabled'] = enabled
        if codeid is not None:
            kwargs['codeid'] = codeid
        self.config_generic('GS1 Databar', **kwargs)
