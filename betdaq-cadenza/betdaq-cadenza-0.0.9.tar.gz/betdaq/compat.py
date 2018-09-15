import sys


_ver = sys.version_info


try:
    from builtins import FileNotFoundError
except ImportError:
    raise FileNotFoundError

basestring = (str, bytes)
numeric_types = (int, float)
integer_types = (int,)
