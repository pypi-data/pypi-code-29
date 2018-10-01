import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .features import (
    feature_function, feature_channels, feature_list_channels
)
from .types import tf_feat_string




def encode_codex(by, etype):
  return {
      (None,       'example'):          _encode_none_example,
      ('channels', 'example'):          _encode_channels_example,
      ('bstrings', 'example'):          _encode_bstrings_example,
      ('bdstring', 'example'):          _encode_bdstring_example,
      (None,       'sequence_example'): _encode_none_example,
      ('channels', 'sequence_example'): _encode_channels_sequence_example,
      ('bstrings', 'sequence_example'): _encode_bstrings_sequence_example,
      ('bdstring', 'sequence_example'): _encode_bdstring_sequence_example,
  }[(by, etype)]


def _encode_none_example(finfo, data):
    dtype = tf_feat_string(finfo['dtype'])
    return feature_function(dtype)(data)

def _encode_channels_example(finfo, data):
  # finfo['channel_names'] = cn]
  dtype = tf_feat_string(finfo['dtype'])
  return feature_channels(data, dtype,  finfo['data_format'], finfo['channel_names'])

def _encode_bstrings_example(finfo, data):
  return feature_channels(data, 'bytes', finfo['data_format'], finfo['channel_names'])

def _encode_bdstring_example(finfo, data):
  return feature_function('bytes')(data)


def _encode_channels_sequence_example(finfo, data):
  dtype = tf_feat_string(finfo['dtype'])
  return feature_list_channels(data, dtype, finfo['data_format'])

def _encode_bstrings_sequence_example(finfo, data):
  return feature_list_channels(data, 'bytes', finfo['data_format'])


def _encode_bdstring_sequence_example(finfo, data):
  return tf.train.FeatureList(feature=[feature_function('bytes')(data)])
