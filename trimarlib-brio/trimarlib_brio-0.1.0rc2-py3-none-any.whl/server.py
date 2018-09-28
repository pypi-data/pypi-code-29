import configparser
import json
import logging
import queue
import select
import socket
import threading

import jsonrpc
import newlandlib
import sysfsgpio


class Server(object):
    class InboundConnection(threading.Thread):
        def __init__(self, sock: socket.socket, dispatcher: jsonrpc.Dispatcher, *args, **kwargs):
            name = '-'.join(['brio.Inbound', '{}:{}'.format(*sock.getpeername())])
            self._logger = logging.getLogger(name)
            super().__init__(name=name)

            self._sock = sock
            self._sock_lock = threading.Lock()
            self._dispatcher = dispatcher
            self._cancel = threading.Event()

        def stop(self):
            self._cancel.set()
            self.join()

        def run(self):
            self._logger.info('inbound connection processor started')
            rxbuf = bytearray()

            while not self._cancel.is_set():
                rlist, *_ = select.select([self._sock], [], [], .5)
                if self._sock not in rlist:
                    continue

                try:
                    tmp = self._sock.recv(64)
                    if tmp == b'':
                        self._logger.info('connection closed by remote end')
                        break
                    rxbuf += tmp
                except OSError:
                    self._logger.exception('failed to read data')
                    break

                try:
                    while b'\r\n\r\n' in rxbuf:
                        idx = rxbuf.find(b'\r\n\r\n')
                        if idx == 0:
                            rxbuf = rxbuf[4:]
                            continue
                        try:
                            js = rxbuf[:idx].decode()
                            self._logger.debug('decoded JSON string: %s', js)
                        except UnicodeDecodeError:
                            self._logger.exception('failed to decode received bytes', exc_info=False)
                            continue
                        finally:
                            rxbuf = rxbuf[idx + 4:]

                        response = jsonrpc.JSONRPCResponseManager.handle(js, self._dispatcher)
                        if response is not None:
                            with self._sock_lock:
                                offs = 0
                                data = b''.join([response.json.encode(), b'\r\n\r\n'])
                                while offs < len(data):
                                    offs += self._sock.send(data[offs:])
                                del data
                                del offs
                        del response
                except OSError:
                    self._logger.exception('failed to send response')
                    break

            self._logger.info('inbound connection processor returning')
            try:
                self._sock.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            self._sock.close()
            return

        def send(self, data: bytes):
            with self._sock_lock:
                offs = 0
                while offs < len(data):
                    offs += self._sock.send(data[offs:])
            return

    def __init__(self, *, endpoint=None, logger=None):
        """Initialize instance of the object

        :param endpoint: server endpoint, defaults to None, which means binding to 'localhost:60498'
        :type endpoint: str or tuple
        :param logger: logger used by the instance, defaults to None, which means using 'brio.Server'
        :type logger: str or logging.Logger
        :raises TypeError:
        :raises ValueError: if failed to decode endpoint specification
        """
        if logger is None:
            self._logger = logging.getLogger('brio.Server')
        elif isinstance(logger, logging.Logger):
            self._logger = logger
        elif isinstance(logger, str):
            self._logger = logging.getLogger(logger)
        else:
            raise TypeError('logger must be a string or an instance of logging.Logger')

        if endpoint is None:
            self._endpoint = ('localhost', 60498)
        elif isinstance(endpoint, str):
            ep = endpoint.split(':')
            if len(ep) == 1:
                self._endpoint = (ep[0], 60498)
            elif len(ep) == 2:
                self._endpoint = (ep[0], int(ep[1]))
            else:
                raise ValueError('failed to decode endpoint')
        elif isinstance(endpoint, tuple):
            if len(endpoint) != 2:
                raise ValueError('failed to decode endpoint')
            if not isinstance(endpoint[0], str):
                raise TypeError('invalid endpoint[0], expected string')
            if not isinstance(endpoint[1], int):
                raise TypeError('invalid endpoint[1], expected int')
            self._endpoint = endpoint
        else:
            raise TypeError('invalid endpoint')

        self._thread_lock = threading.Lock()
        self._thread_cancel = threading.Event()
        self._thread_acceptor = None
        self._thread_notifier = None
        self._thread_inbound_lock = threading.Lock()
        self._thread_inbound = []
        self._notification_queue = queue.Queue()

        self._gpios = []
        for id, pin in sysfsgpio.get_pins():
            self._gpios.append(sysfsgpio.Pin(pin))

        self._scanner = None
        self._scanner_last_code = None

        self._dispatcher = jsonrpc.Dispatcher()
        for method, name in [(self._read_io, 'read-io'),
                             (self._write_io, 'write-io'),
                             (self._scanner_info, 'scanner-info'),
                             (self._read_last, 'read-last'),
                             (self._help, 'help')]:
            self._dispatcher.add_method(method, name)

    def get_hostname(self):
        """Get hostname to which the server is to be bound"""
        return self._endpoint[0]

    def set_hostname(self, value: str):
        """Set hostname to which the server is to be bound

        :param str value: hostname to set
        :raises TypeError: if value is not a string
        """
        if not isinstance(value, str):
            raise TypeError('hostname must be a string')
        self._endpoint = (value, self._endpoint[1])

    def get_port(self):
        """Get port number to which server is to be bound"""
        return self._endpoint[1]

    def set_port(self, value: int):
        """Set port number to which server is to be bound

        :param int value: port number to set, must be a 16-bit unsigned
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is not in range(0, 0xFFFF)
        """
        if not isinstance(value, int):
            raise TypeError('port must be an integer')
        if value not in range(0xFFFF):
            raise ValueError('port must be an integer in range(0, 0xFFFF)')
        self._endpoint = (self._endpoint[0], value)

    def get_endpoint(self):
        """Get socket-compatible endpoint of the server"""
        return self._endpoint

    def set_endpoint(self, value: tuple):
        """Set socket-compatible endpoint of the server

        :param tuple(str, int) value: socket-compatible endpoint to set
        :raises TypeError: if value is not a tuple,
                           its first element is not a string,
                           its second element is not an integer
        :raises IndexError: if value's number of elements is different than 2
        :raises ValueError: if value's second element is not in range(0, 0xFFFF)
        """
        msg = 'endpoint must be a socket-compatible tuple of (str, int)'
        if not isinstance(value, tuple):
            raise TypeError(msg)
        if len(value) != 2:
            raise IndexError(msg)
        if not isinstance(value[0], str) or not isinstance(value[1], int):
            raise TypeError(msg)
        if value[1] not in range(0xFFFF):
            raise ValueError(msg)
        self._endpoint = value

    hostname = property(get_hostname, set_hostname)
    port = property(get_port, set_port)
    endpoint = property(get_endpoint, set_endpoint)

    def _send_notification(self, method: str, params: dict = None):
        obj = dict(jsonrpc='2.0', method=method, params=params)
        data = b''.join([json.dumps(obj).encode(), b'\r\n\r\n'])
        self._notification_queue.put(data)

    def _scanner_callback(self, sender, *, data, codeid=None, aimid=None):
        self._scanner_last_code = dict(code=data.decode())
        if aimid is not None:
            self._scanner_last_code['AIM'] = aimid.decode()
        if codeid is not None:
            self._scanner_last_code['CodeID'] = codeid.decode()
        self._send_notification('notify-scan-done', self._scanner_last_code)

    def _pin_callback(self, pin, value):
        params = dict(pin=pin.pinname, value=value)
        self._send_notification('notify-pin-changed', params)

    def _read_last(self):
        """Get last scanned data"""
        return self._scanner_last_code

    def _read_io(self, *args):
        """Get IO port state and configuration"""
        if len(args) == 0 or len(args) > 1:
            ret = dict()
            if len(args) == 0:
                for pin in self._gpios:
                    data = pin.configuration
                    data['enabled'] = pin.enabled
                    data['value'] = pin.value
                    ret[pin.pinname] = data
            else:
                for arg in args:
                    if isinstance(arg, int):
                        pin = self._gpios[arg]
                    elif isinstance(arg, str):
                        for pin in self._gpios:
                            if pin.pinname == arg:
                                break
                        else:
                            raise ValueError('pin "{}" does not exist'.format(arg))
                    else:
                        raise TypeError('pin must be referenced by index or name')
                    if pin.pinname in ret:
                        continue
                    data = pin.configuration
                    data['enabled'] = pin.enabled
                    data['value'] = pin.value
                    ret[pin.pinname] = data
        else:
            if isinstance(args[0], int):
                pin = self._gpios[args[0]]
            elif isinstance(args[0], str):
                for pin in self._gpios:
                    if pin.pinname == args[0]:
                        break
                else:
                    raise ValueError('pin "{}" does not exist'.format(args[0]))
            else:
                raise TypeError('pin must be referenced by index or name')
            ret = pin.configuration
            ret['enabled'] = pin.enabled
            ret['value'] = pin.value
        return ret

    def _write_io(self, pin, value_or_configuration):
        """Manipulate IO port

        :param pin: pin to manipulate
        :type pin: str or int
        :param value_or_configuration: value to be set (if pin is configured as output) or a configuration to apply
        :type value_or_configuration: bool or int or dict
        :raises TypeError:
        :raises IndexError: if pin is referenced by index out of range
        :raises ValueError: if pin is referenced by name and there is no such pin
        """
        if isinstance(pin, int):
            pin_obj = self._gpios[pin]
        elif isinstance(pin, str):
            for pin_obj in self._gpios:
                if pin_obj.pinname == pin:
                    break
            else:
                raise ValueError('pin "{}" does not exist'.format(pin))
        else:
            raise TypeError('pin must be an integer or a string')

        if isinstance(value_or_configuration, dict):
            pin_obj.configuration = value_or_configuration
            if 'enabled' in value_or_configuration:
                pin_obj.enabled = value_or_configuration['enabled']
        else:
            pin_obj.value = value_or_configuration

    def _scanner_info(self):
        """Get attached scanner information"""
        if self._scanner is not None and self._scanner.is_open:
            return self._scanner.query()
        return None

    def _help(self, name: str = None):
        """Return a list of available methods or a docstring of selected method

        :param str name: name of method whose docstring is to be returned, defaults to None - return list of available
                         methods in that case
        :rtype: str or list[str]
        """
        if name is None:
            return list(self._dispatcher.keys())
        else:
            return self._dispatcher[name].__doc__

    def start(self):
        """Start acceptor thread

        :raise RuntimeError: if server has been already started
        """
        with self._thread_lock:
            if self._thread_acceptor is not None:
                raise RuntimeError('thread already started')
            if self._scanner is None:
                self._logger.warning('no scanner device is used')
            else:
                try:
                    if not self._scanner.is_open:
                        self._scanner.open()
                    self._scanner.callback = self._scanner_callback
                    self._scanner.start()
                except Exception:
                    self._logger.exception('failed to start scanner thread')
            self._thread_acceptor = threading.Thread(name='acceptor', target=self._acceptor)
            self._thread_notifier = threading.Thread(name='notifier', target=self._notifier)
            self._thread_acceptor.start()
            self._thread_notifier.start()
        return

    def stop(self):
        """Stop acceptor thread, close all connections"""
        with self._thread_lock:
            if self._thread_acceptor is None:
                return
            if self._scanner is not None:
                self._scanner.stop()
            self._thread_cancel.set()
            self._thread_acceptor.join()
            self._thread_acceptor = None
            self._thread_notifier.join()
            self._thread_notifier = None
            self._thread_cancel.clear()
        return

    def _acceptor(self):
        self._logger.info('acceptor thread started')
        sock = socket.socket()
        try:
            ep = self._endpoint
            sock.bind(ep)
            self._logger.info('server bound, endpoint=%s', ep)
            del ep
        except OSError:
            self._logger.exception('failed to bind socket, aborting')
            sock.close()
            return
        sock.listen(8)

        while not self._thread_cancel.is_set():
            rlist, *_ = select.select([sock], [], [], .5)

            if sock in rlist:
                try:
                    nsock, remote_ep = sock.accept()
                    self._logger.info('accepted inbound connection from %s', remote_ep)
                    with self._thread_inbound_lock:
                        thread = self.InboundConnection(nsock, self._dispatcher)
                        self._thread_inbound.append(thread)
                        thread.start()
                except OSError:
                    self._logger.exception('failed to accept new connection, aborting')
                    break

            dead_threads = []
            with self._thread_inbound_lock:
                for thread in self._thread_inbound:
                    if not thread.is_alive():
                        dead_threads.append(thread)
                if len(dead_threads) > 0:
                    self._logger.info('joining %d dead threads', len(dead_threads))
                for thread in dead_threads:
                    thread.stop()
                    self._thread_inbound.remove(thread)
            del dead_threads

        self._logger.info('acceptor thread cleaning-up')
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        sock.close()
        with self._thread_inbound_lock:
            for thread in self._thread_inbound:
                thread.stop()
            self._thread_inbound.clear()
        self._logger.info('acceptor thread returning')

    def _notifier(self):
        self._logger.info('notifier thread started')

        while not self._thread_cancel.is_set():
            try:
                notification = self._notification_queue.get(timeout=.5)
            except queue.Empty:
                continue

            with self._thread_inbound_lock:
                for thread in self._thread_inbound:
                    if not thread.is_alive():
                        self._logger.info('thread %s is not alive, skip sending notification', thread.name)
                        continue
                    try:
                        thread.send(notification)
                    except OSError:
                        self._logger.exception('failed to send notification to %s', thread.name)

        self._logger.debug('notifier thread returning')
        return

    def configure(self, source=None):
        """Configure server and peripherals according to source

        :param source: path to configuration file or a dictionary holding configuration data
        :type source: str or configparser.ConfigParser
        :raises TypeError: if source is neither a string nor a configparser.ConfigParser
        """
        if source is not None and not isinstance(source, (str, configparser.ConfigParser)):
            raise TypeError('source must be a string or a ConfigParser')
        if source is None or isinstance(source, configparser.ConfigParser):
            config = source
        else:
            config = configparser.ConfigParser()
            config.read(source)

        self._configure_server(config)
        self._configure_scanner(config)
        self._configure_gpios(config)

    def _configure_server(self, config: configparser.ConfigParser):
        if config is not None and not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')

        if config is None or not config.has_section('Server'):
            self._logger.info('applying default server configuration')
            self._endpoint = ('localhost', 60498)
            return

        try:
            self.set_hostname(config.get('Server', 'hostname'))
        except configparser.NoOptionError:
            pass
        try:
            self.set_port(config.getint('Server', 'port'))
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "Server.port" option', exc_info=False)

    def _configure_gpios(self, config: configparser.ConfigParser):
        if config is None:
            return
        if not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')

        # configure defaults
        if config.has_section('GPIO'):
            gpio_default = dict()
            for key in ['enabled', 'invert']:
                try:
                    gpio_default[key] = config.getboolean('GPIO', key)
                except configparser.NoOptionError:
                    pass
                except ValueError:
                    self._logger.exception('invalid value of "GPIO.%s" option', key, exc_info=False)
            for key in ['ontime', 'offtime', 'debounce']:
                try:
                    gpio_default[key] = config.getfloat('GPIO', key)
                except configparser.NoOptionError:
                    pass
                except ValueError:
                    self._logger.exception('invalid value of "GPIO.%s" option', key, exc_info=False)
            try:
                gpio_default['repeat'] = config.getint('GPIO', 'repeat')
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "GPIO.repeat" option', exc_info=False)
            try:
                direction = config.get('GPIO', 'direction')
                if direction not in ['in', 'out']:
                    raise ValueError()
                gpio_default['direction'] = direction
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "GPIO.direction" option', exc_info=False)
            # apply configuration
            self._logger.debug('applying GPIO default configuration: %s', gpio_default)
            for gpio in self._gpios:
                gpio.configuration = gpio_default
                if 'enabled' in gpio_default:
                    gpio.enabled = gpio_default['enabled']

        # configure specific pins
        for section in config.sections():
            if not section.startswith('GPIO.'):
                continue
            gpio_id = section[5:]
            if gpio_id.startswith('P'):
                # locate pin by name
                for gpio in self._gpios:
                    if gpio.pinname == gpio_id:
                        break
                else:
                    self._logger.warning('GPIO referenced by name "%s" not found', gpio_id)
                    continue
            else:
                try:
                    gpio_id = int(gpio_id)
                except ValueError:
                    self._logger.error('unable to determine GPIO ID: "%s"', gpio_id)
                    continue
                for gpio in self._gpios:
                    if gpio.pin == gpio_id:
                        break
                else:
                    self._logger.warning('GPIO referenced by index "%d" not found', gpio_id)
                    continue

            # GPIO found, read and apply settings
            gpio_config = dict()
            for key in ['enabled', 'invert']:
                try:
                    gpio_config[key] = config.getboolean(section, key)
                except configparser.NoOptionError:
                    pass
                except ValueError:
                    self._logger.exception('invalid value of "%s.%s" option', section, key, exc_info=False)
            for key in ['ontime', 'offtime', 'debounce']:
                try:
                    gpio_config[key] = config.getfloat(section, key)
                except configparser.NoOptionError:
                    pass
                except ValueError:
                    self._logger.exception('invalid value of "%s.%s" option', section, key, exc_info=False)
            try:
                gpio_config['repeat'] = config.getint(section, 'repeat')
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "%s.repeat" option', section, exc_info=False)
            try:
                direction = config.get(section, 'direction')
                if direction not in ['in', 'out']:
                    raise ValueError()
                gpio_config['direction'] = direction
            except configparser.NoOptionError:
                pass
            except ValueError:
                self._logger.exception('invalid value of "%s.direction" option', section, exc_info=False)

            self._logger.debug('applying %s configuration: %s', gpio.pinname, gpio_config)
            gpio.configuration = gpio_config
            if 'enabled' in gpio_config:
                gpio.enabled = gpio_config['enabled']

    def _configure_scanner(self, config: configparser.ConfigParser):
        if config is None:
            return
        if not isinstance(config, configparser.ConfigParser):
            raise TypeError('config must be a ConfigParser')

        if not config.has_section('Scanner'):
            self._logger.warning('no Scanner section, no device will be used')
            return

        try:
            model = config.get('Scanner', 'model')
            if model == 'FM100':
                self._scanner = newlandlib.FM100()
            else:
                self._logger.error('unknown scanner model: %s', model)
                return
        except configparser.NoOptionError:
            pass

        try:
            if config.getboolean('Scanner', 'default_configuration'):
                self._scanner.configure()
                return
        except configparser.NoOptionError:
            pass
        except ValueError:
            self._logger.exception('invalid value of "Scanner.default_configuration" option', exc_info=False)

        scanner_config = configparser.ConfigParser()
        for section in config.sections():
            if not section.startswith('Scanner.'):
                continue
            scanner_section = section[8:]
            if scanner_section != 'DEFAULT':
                scanner_config.add_section(scanner_section)
            for option in config.options(section):
                scanner_config[scanner_section][option] = config[section][option]
        self._scanner.configure(scanner_config)
