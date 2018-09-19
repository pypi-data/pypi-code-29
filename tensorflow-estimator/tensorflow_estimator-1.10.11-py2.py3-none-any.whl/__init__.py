from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from tensorflow import _api
import os
__path__ = [os.path.dirname(os.path.dirname(_api.__file__))] + __path__
from tensorflow._api.v1 import *

