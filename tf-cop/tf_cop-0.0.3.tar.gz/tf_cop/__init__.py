from .api import TfCop

try:
    from .version import __version__
except ImportError:
    __version__ = 'master'
