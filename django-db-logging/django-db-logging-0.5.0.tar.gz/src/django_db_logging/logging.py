import logging
import warnings

from .utils import fqn

logger = logging.getLogger('django_db_logging')

for hdlr in logger.handlers[:]:  # remove all old handlers
    if fqn(hdlr).startswith('django_db_logging.'):
        logger.removeHandler(hdlr)
        warnings.warn(UserWarning(
            f"Handler `{hdlr.name}` cannot be used with logger `django_db_logging`. "
            "It has been removed. Please fix your logging configuration."
        ), stacklevel=0)

if logger.propagate:  # pragma: no cover
    if logger.handlers:
        warnings.warn(UserWarning(
            f" `{logger.name}.propagate cannot` be `True`. "
            "It has been disabled. Please fix your logging configuration."
        ), stacklevel=0)
        logger.propagate = False
