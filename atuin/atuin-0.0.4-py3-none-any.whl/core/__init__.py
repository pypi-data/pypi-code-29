from atuin.core.colorlogging import init_logging
from atuin.core.colorlogging import getColorLogger
# from atuin.core.colorlogging import testLogger
from atuin.core.colorlogging import LOG_FORMAT_MSG
import logging


init_logging(logging.DEBUG)
CORE_LOGGER = getColorLogger(__name__, LOG_FORMAT_MSG)
# colorlogging.testLogger(CORE_LOGGER)
