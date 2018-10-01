import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .utils import default_channel_names
from .types import tf_encoded_type, tf_type_string




def decode_bstring_array(array:list, decode_type:str='ascii') -> list:
    return [bstr.decode(decode_type) for bstr in array]
