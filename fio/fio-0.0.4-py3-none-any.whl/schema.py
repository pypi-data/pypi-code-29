import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

SCHEMA = {
    'Chromosome':     {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Padded Start':   {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Padded Stop':    {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Name':           {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Score':          {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Strand':         {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Original Start': {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Original Stop':  {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Nucleotides':    {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Sequence':       {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'channels',
        'channel_names': ['A', 'C', 'T', 'G'],
        'data_format': 'channels_last'
    },
    'Labels':         {
        'length': 'fixed',
        'dtype': tf.int64,
        'shape': [5, 3],
        'encode': 'channels',
        'channel_names': ['Exon', 'Intron', 'Other'],
        'data_format': 'channels_last'

    },
}

SCHEMA0 = {
    'Sequence':       {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'channels',
        'channel_names': ['A', 'C', 'T', 'G']
    },
    'Labels':         {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'channels',
        'channel_names': ['Exon', 'Intron', 'Other']
    },
}


SCHEMA1 = {
    'Chromosome':     {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Padded Start':   {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Padded Stop':    {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Name':           {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Score':          {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Strand':         {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Original Start': {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Original Stop':  {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Nucleotides':    {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Sequence':       {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'bstrings',
        'channel_names': ['A', 'C', 'T', 'G']
    },
    'Labels':         {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'channels',
        'channel_names': ['Exon', 'Intron', 'Other']
    },
}


SCHEMA2 = {
    'Chromosome':     {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Padded Start':   {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Padded Stop':    {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Name':           {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Score':          {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Strand':         {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Original Start': {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Original Stop':  {'length': 'fixed', 'dtype': tf.int64,   'shape': []},
    'Nucleotides':    {'length': 'fixed', 'dtype': tf.string,  'shape': []},
    'Sequence':       {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'bdstring',
        'channel_names': ['A', 'C', 'T', 'G']
    },
    'Labels':         {
        'length': 'fixed',
        'dtype': tf.float32,
        'shape': [5, 4],
        'encode': 'channels',
        'channel_names': ['Exon', 'Intron', 'Other']
    },
}
