import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf


def list_like_q(value) -> bool:
    '''
    TensorFlow tf.train.Feature requires a list of feature values.
    Many values used in practice are either python lists or numpy.ndarrays.
    We often have features which consist of a singular value.
    For brevity, we define some light helper functions to wrap a list as a
    tf.train.Feature. This lets us test if we need to wrap the value.
    '''
    # import numpy as np
    return (type(value) is list or type(value) is np.ndarray)


def tf_type_string(tf_type:str) -> str:
  '''
  Convert tf.<dtype> to (str) striping tf. in the process.
  '''
  return str(tf_type).replace("<dtype: \'", '').replace("\'>", '')

def tf_feat_string(tf_type:str) -> str:
  '''
  Convert tf.<dtype> to a corresponding type (str) which can be used with
  tf.Features.
  '''
  t_str = tf_type_string(tf_type)
  if 'string' in t_str: return 'bytes'
  if 'float'  in t_str: return 'float'
  if 'int'    in t_str: return 'int64'




def tf_encoded_type(starting_dtype, encode:str):
    if encode == 'channels': return starting_dtype
    if encode == 'bstrings': return tf.string
    if encode == 'bdstring': return tf.string
