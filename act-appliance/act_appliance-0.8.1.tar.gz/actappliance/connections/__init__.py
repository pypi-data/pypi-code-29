CALL_TIMEOUT = 6 * 60 * 60

# Hoist classes and functions into connection namespace
from actappliance.connections.rest import ApplianceRest  # NOQA
from actappliance.connections.ssh import ApplianceSsh    # NOQA
from actappliance.connections.aiossh import AIOSsh    # NOQA
from actappliance.connections.aiorest import AIORest  # NOQA

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
