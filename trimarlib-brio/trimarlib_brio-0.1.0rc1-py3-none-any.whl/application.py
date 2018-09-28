import signal
import logging
import threading
from .server import Server


class Application(object):
    def __init__(self, *, configuration: str = None, endpoint: tuple = None, hostname: str = None, port: int = None,
                 logger=None):
        if logger is None or isinstance(logger, str):
            self._logger = logging.getLogger(logger or 'brio.Application')
        elif isinstance(logger, logging.Logger):
            self._logger = logger
        else:
            raise TypeError('logger must be a Logger or a string')
        self._cancel = threading.Event()
        self._server = Server()
        if configuration is not None:
            self._logger.info('applying server configuration from file: %s', configuration)
            self._server.configure(configuration)
        else:
            self._server.configure()
        if endpoint is not None:
            self._logger.info('overriding server endpoint with: %s', endpoint)
            self._server.endpoint = endpoint
        else:
            if hostname is not None:
                self._logger.info('overriding server hostname with: %s', hostname)
                self._server.hostname = hostname
            if port is not None:
                self._logger.info('overriding sever port with: %d', port)
                self._server.port = port

    def _signal_handler(self, signum, frame):
        self._logger.info('signal caught: %s, frame=%s', signum, frame)
        self._cancel.set()

    def run(self):
        self._logger.debug('installing signal handlers')
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)

        self._logger.debug('starting server')
        self._server.start()

        self._logger.debug('waiting for termination signal')
        try:
            self._cancel.wait()
            self._logger.debug('cancellation requested via signal')
        except KeyboardInterrupt:
            self._logger.debug('cancellation requested via keyboard interrupt')
        finally:
            self._logger.debug('stopping server')
            self._server.stop()

        self._logger.debug('restoring default signal handlers')
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        self._logger.debug('terminating application')
        return
