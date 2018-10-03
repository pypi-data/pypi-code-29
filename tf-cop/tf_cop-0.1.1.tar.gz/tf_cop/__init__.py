from .api import TfCop
from .cli import cli

try:
    from .version import __version__
except ImportError:
    __version__ = 'master'
