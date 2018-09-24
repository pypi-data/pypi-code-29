import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .types import list_like_q
from .utils import (channels_iterable, default_channel_names)

def feature_int64(value):
    '''Takes value and wraps into tf.train.Feature(Int64List)'''
    if not list_like_q(value): value = [value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def feature_float(value):
    '''Takes value and wraps into tf.train.Feature(FloatList)'''
    if not list_like_q(value): value = [value]
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def feature_bytes(value):
    '''Takes value and wraps is into tf.train.Feature(BytesList).'''
    if type(value) is np.ndarray: value = value.tostring()
    if type(value) is not bytes:  value = str(value).encode('utf-8')
    if type(value) is not list:   value = [value]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

def feature_function(dtype):
    '''
    Given <dtype> returns the function for wrapping a value into the
    corresponding tf.train.Feature
    '''
    return feature_int64 if dtype == "int64" else \
           feature_float if dtype == "float" else \
           feature_bytes

def feature_list(iterable, dtype:str='float'):
    '''Given an iterable, returns the feature list of corresponding <dtype>.'''
    return tf.train.FeatureList(feature=[feature_function(dtype)(item) for item in iterable])

# the next three for completeness
def feature_list_int64(value):
    return feature_list(value, 'int64')

def feature_list_float(value):
    return feature_list(value, 'float')

def feature_list_bytes(value):
    return feature_list(value, 'bytes')


def feature_list_channels(sequence, dtype:str='float', data_format:str='channels_last'):
    return feature_list(channels_iterable(sequence, data_format), dtype)

def feature_channels(sequence, dtype:str='float', data_format:str='channels_last', channel_names:list=None) -> dict:
    '''
    Given a <sequence> of corresponding <dtype> and <data_format>, with optional <channel_names>
    returns the dictionary of each channel:tf.train.Feature pair.
    '''
    if channel_names is None: channel_names = default_channel_names(sequence, data_format)
    return {c:feature_function(dtype)(f) for c,f in list(zip(channel_names, channels_iterable(sequence, data_format)))}


def record_feature(length, etype):
    return {
        ('fixed', 'example'):             tf.FixedLenFeature,
        ('fixed', 'sequence_example'):    tf.FixedLenSequenceFeature,
        ('variable', 'example'):          tf.VarLenFeature,
        ('variable', 'sequence_example'): tf.VarLenFeature
    }[(length, etype)]


def unwrap_features(features):
    return {
        k: (
            # v[:, 0]
            v[0] if (type(v) is np.ndarray and len(v.shape) > 1) else v[0]
        ) for k, v in features.items()
    }
