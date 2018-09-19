import logging
import os
import select
import threading
import time

from .utils import Event, pin2name, name2pin


class Pin(object):
    """Utility wrapper around sysfs GPIO interface."""

    def __init__(self, pin, direction: str = 'in', invert: bool = None, *, logger: logging.Logger = None):
        """Initialize Pin object

        :param pin: name or number of the pin
        :type pin: str or int
        :param str direction: initial direction of the pin, accepted values are 'in' and 'out', defaults to 'in'
        :param bool invert: flag indicating whether to use inverted logic, defaults to None which means no change
        :param logging.Logger logger: logger instance to use
        :raises ValueError: if failed to decode pin name
        :raises TypeError: if supplied parameter is neither an integer nor a string
        :raises FileNotFoundError: if specified pin is not available
        """

        self._thread = None
        self._thread_lock = threading.Lock()
        self._thread_cancel = threading.Event()
        self._input_changed = Event()
        self._logger = logger or logging.getLogger('sysfsgpio.Pin')
        self._event = threading.Event()

        self._config = dict(debounce=.1, ontime=-1.0, offtime=-1.0, repeat=-1)

        if isinstance(pin, int):
            self._pinname = pin2name(pin)
            self._pin = pin
        elif isinstance(pin, str):
            try:
                self._pin = name2pin(pin)
                self._pinname = pin
            except ValueError:
                pin = int(pin)
                self._pinname = pin2name(pin)
                self._pin = pin
        else:
            raise TypeError('pin must be an integer, a valid pin name or a string convertible to integer')

        self._path = '/sys/class/gpio/gpio{:d}'.format(self._pin)

        if direction is not None:
            if type(direction) is not str:
                raise TypeError('direction: expected str, got {}'.format(type(direction)))
            if direction not in ['in', 'out']:
                raise ValueError('direction: expecting "in" or "out"')
            with open(os.path.join(self._path, 'direction'), 'w') as fd:
                fd.write(direction)
        if invert is not None:
            if type(invert) is not bool:
                raise TypeError('invert: expected bool, got {}'.format(type(invert)))
            with open(os.path.join(self._path, 'active_low'), 'w') as fd:
                fd.write(str(int(invert)))

        try:
            with open(os.path.join(self._path, 'edge'), 'w') as fd:
                fd.write('none')
        except FileNotFoundError:
            self._logger.warning('pin %s does not support interrupts', self.pinname)
        return

    @property
    def pin(self):
        """Return pin number"""
        return self._pin

    @property
    def pinname(self):
        """Return pin name"""
        return self._pinname

    def register_callback(self, value):
        self._input_changed += value

    def unregister_callback(self, value):
        self._input_changed -= value

    def clear_callbacks(self):
        self._input_changed.clear()

    def get_value(self) -> int:
        """Read current state of the pin"""
        with open(os.path.join(self._path, 'value'), 'r') as fd:
            return int(fd.read())

    def set_value(self, value):
        """Set value of the pin

        :raises RuntimeError: if worker thread is alive
        """
        with self._thread_lock:
            if self._thread is not None and self._thread.is_alive():
                raise RuntimeError('worker thread running')
            with open(os.path.join(self._path, 'value'), 'w') as fd:
                fd.write(str(int(value)))

    def get_invert(self) -> bool:
        """Read flag indication logic inversion"""
        with open(os.path.join(self._path, 'active_low'), 'r') as fd:
            return bool(int(fd.read()))

    def set_invert(self, value: bool):
        """Set logic inversion"""
        with open(os.path.join(self._path, 'active_low'), 'w') as fd:
            fd.write(str(int(value)))

    def get_direction(self) -> str:
        """Get pin direction"""
        with open(os.path.join(self._path, 'direction'), 'r') as fd:
            return fd.read().strip()

    def set_direction(self, value: str):
        """Set pin direction

        :param str value: pin direction, accepted values are 'in' and 'out'
        :raises TypeError: if parameter type is not a string
        :raises ValueError: if parameter value is not in accepted range
        :raises RuntimeError: if worker thread is running
        """
        if not isinstance(value, str):
            raise TypeError('expecting str, got {}'.format(type(value)))
        elif value not in ['in', 'out']:
            raise ValueError('v = {}'.format(value))
        else:
            with self._thread_lock:
                if self._thread is not None and self._thread.is_alive():
                    raise RuntimeError('worker thread running')
                with open(os.path.join(self._path, 'direction'), 'w') as fd:
                    fd.write(value)

    def get_enabled(self) -> bool:
        """Return True if worker thread is running, False otherwise"""
        with self._thread_lock:
            return self._thread is not None and self._thread.is_alive()

    def enable(self):
        """Start worker thread if not already running"""
        with self._thread_lock:
            if self._thread is not None:
                if self._thread.is_alive():
                    return
                self._thread.join()
                self._thread = None
            if self.direction == 'in':
                target = self._input_fun
                name = 'gpio{}-input'.format(self._pin)
            else:
                target = self._output_fun
                name = 'gpio{}-output'.format(self._pin)
            self._thread = threading.Thread(target=target, name=name, daemon=True)
            self._thread.start()

    def disable(self):
        """Stop worker thread"""
        with self._thread_lock:
            if self._thread is None:
                return
            self._thread_cancel.set()
            self._thread.join()
            self._thread = None
            self._thread_cancel.clear()

    def set_enabled(self, value: bool):
        """Start or stop worker thread"""
        if not isinstance(value, bool):
            raise TypeError('expecting bool, got {}'.format(type(value)))
        if value:
            self.enable()
        else:
            self.disable()

    value = property(get_value, set_value)
    invert = property(get_invert, set_invert)
    direction = property(get_direction, set_direction)
    enabled = property(get_enabled, set_enabled)

    def config(self, config=None, **kwargs):
        """Get or set pin configuration

        Accepts configuration as keyword arguments or a dictionary.
        Supported fields are:

        - debounce : floating point value representing debouncing delay;
        - ontime : floating point value indicating how long the output is held in active state, in seconds;
        - offtime : floating point value indicating how long the output is held in inactive state, in seconds;
        - repeat : integer value indicating how many on-off cycles to perform, negative value indicates forever.

        :raises TypeError: if unable to cast passed value as target type
        :raises RuntimeError: if attempting to change configuration and worker thread is running
        """
        if config is None:
            config = kwargs
        if len(config) == 0:
            ret = {}
            for key, value in self._config.items():
                ret[key] = value
            return ret
        with self._thread_lock:
            if self._thread is not None and self._thread.is_alive():
                raise RuntimeError('worker thread running')
            for key in self._config:
                if key in config:
                    if not isinstance(config[key], type(self._config[key])):
                        raise TypeError('invalid type of "%s" field', key)
                    self._config[key] = config[key]
        return

    def _input_fun(self):
        cth = threading.current_thread()
        self._logger.info('%s started', cth.name)
        try:
            try:
                with open(os.path.join(self._path, 'edge'), 'w') as fd:
                    fd.write('both')
                poll = select.poll()
            except FileNotFoundError:
                poll = None

            with open(os.path.join(self._path, 'value'), 'r') as fd:
                stamp = 0
                v = int(fd.read())
                vv = v
                fd.seek(0)

                if poll is not None:
                    poll.register(fd, select.POLLPRI)
                while not self._thread_cancel.is_set():
                    if poll is not None:
                        ret = poll.poll(self._config['debounce'] * 1000)
                        if len(ret) != 0:
                            vv = int(fd.read())
                            fd.seek(0)
                            continue
                    else:
                        if self._thread_cancel.wait((stamp + self._config['debounce']) - time.time()):
                            continue
                        vv = int(fd.read())
                        fd.seek(0)
                        stamp = time.time()
                    if v != vv:
                        v = vv
                        if len(self._input_changed) > 0:
                            self._input_changed(self, v)
                        else:
                            self._logger.info('%s, v=%s, no event handler installed', cth.name, v)
        except Exception:
            self._logger.exception('%s : input processing failed', cth.name)
        finally:
            try:
                with open(os.path.join(self._path, 'edge'), 'w') as fd:
                    fd.write('none')
            except FileNotFoundError:
                pass
            except Exception:
                self._logger.exception('failed to disable interrupts')
        self._logger.info('%s returning', cth.name)
        return

    def _output_fun(self):
        cth = threading.current_thread()
        self._logger.info('%s started', cth.name)
        remcnt = self._config['repeat']
        try:
            with open(os.path.join(self._path, 'value'), 'r+') as fd:
                stamp = 0
                while not self._thread_cancel.is_set() and remcnt != 0:
                    v = int(fd.read())
                    fd.seek(0)
                    if v != 0:
                        dly = self._config['ontime']
                        if remcnt > 0:
                            remcnt -= 1
                    else:
                        dly = self._config['offtime']
                    if dly < 0:
                        self._logger.debug('steady state, exitting')
                        break
                    self._thread_cancel.wait((stamp + dly) - time.time())
                    fd.write('1' if v == 0 else '0')
                    fd.write('\n')
                    fd.seek(0)
                    stamp = time.time()
                self._logger.debug('loop broken')
        except Exception:
            self._logger.exception('%s : input processing failed', cth.name)
            return
        self._logger.info('%s returning', cth.name)
        return
