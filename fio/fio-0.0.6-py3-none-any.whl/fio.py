import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .cls.encode import Encode
from .cls.decode import Decode
from .cls.recon import Recon

class FIO(Encode, Decode, Recon):
    pass
