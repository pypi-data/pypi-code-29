try:
    from .version import version as __version__
except ImportError:
    __version__ = None


try:
    from .version import version as __version__
except ImportError:
    __version__ = None

from .cachelite import (CacheLite, CacheLiteWriteError, CacheLiteReadError, CacheLiteError)
