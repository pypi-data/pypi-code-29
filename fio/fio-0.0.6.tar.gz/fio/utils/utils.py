import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

def take_all() -> slice: return slice(None, None, None)
def take_channel(sequence, channel:int, data_format:str='channels_last'):
    slices = [take_all(), channel]
    if data_format != 'channels_last': slices.reverse()
    return sequence[tuple(slices)]

def number_of_channels(sequence, data_format:str='channels_last') -> int:
    '''Returns sequence.shape[-1] or [0] depending on data_format.'''
    if data_format is None: data_format =  'channels_last'
    if type(sequence) is list: sequence = np.array(sequence)
    return sequence.shape[-1] if data_format == 'channels_last' else sequence.shape[0]

def default_channel_names(sequence, data_format:str='channels_last') -> list:
    '''Ensures a naming scheme as required for channel based Example'''
    if data_format is None: data_format =  'channels_last'
    return ['Channel '+str(i) for i in range(number_of_channels(sequence, data_format))]

def channels_iterable(sequence, data_format:str='channels_last') -> list:
    num_c = number_of_channels(sequence, data_format)
    if data_format is None: data_format =  'channels_last'
    return [take_channel(sequence, c, data_format) for c in range(num_c)]


def channels_length(sequence_shape, data_format:str='channels_last') -> int:
    '''Returns sequence.shape[-1] or [0] depending on data_format.'''
    if data_format is None: data_format =  'channels_last'

    return (sequence_shape[0],) if data_format == 'channels_last' else (sequence_shape[-1],)



def filter_dict(keys, d):
    return {k: d[k] for k in keys}

def flatten_nested_dict(ndict):
    return {
        _k: _v
        for k, v in ndict.items()
        for _k, _v in (
            v if isinstance(v, dict) else {k: v}
        ).items()
    }

def npify_dict(d:dict) -> dict:
    for key, value in d.items():
        if type(value) is list:
            d[key] = np.array(value)
    return d
