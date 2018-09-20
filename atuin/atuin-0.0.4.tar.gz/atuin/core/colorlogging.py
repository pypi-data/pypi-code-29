from logging import StreamHandler, DEBUG, getLogger, Formatter
from colorama import Fore, Back, Style, init


def init_logging(level):
    # colorama initialization for logging
    init()
    getLogger().setLevel(level)


class ColourStreamHandler(StreamHandler):
    """ A colorized output SteamHandler """

    # Some basic colour scheme defaults
    colours = {
        'DEBUG': Fore.CYAN + Style.BRIGHT,
        'INFO': Fore.WHITE + Style.BRIGHT,
        'WARNING': Fore.YELLOW + Style.BRIGHT,
        'ERROR': Fore.RED + Style.BRIGHT,
        'CRITICAL': Back.RED + Fore.WHITE + Style.BRIGHT
    }

    def emit(self, record):
        try:
            message = self.format(record)
            output = self.colours[record.levelname] + message + Style.RESET_ALL
            self.stream.write(output)
            self.stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except (Exception):
            self.handleError(record)


def getColorLogger(name=None, format='%(message)s', level=DEBUG):
    """ Get and initialize a colourised logging instance if the system supports
    it as defined by the log.has_colour
    """
    log = getLogger(name)
    handler = ColourStreamHandler()
    # sets what level this handler can manage
    # root logging level controls output level
    handler.setLevel(level)
    handler.setFormatter(Formatter(format))
    log.addHandler(handler)
    log.propagate = True
    return log


LOG_FORMAT_FULL = '%(name)s [%(levelname)s]: %(msg)s'
LOG_FORMAT_NAME = '%(name)s: %(msg)s'
LOG_FORMAT_LEVEL = '[%(levelname)s]: %(msg)s'
LOG_FORMAT_MSG = '%(msg)s'


def testLogger(logger):
    logger.debug('Test DEBUG')
    logger.info('Test INFO')
    logger.warning('Test WARNING')
    logger.error('Test ERROR')
    logger.critical('Test CRITICAL')
