import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from ..utils.utils import filter_dict, flatten_nested_dict
from ..utils.types import (tf_type_string)

class Base:
    '''
    Here we treat context_features of sequenece_example the same as features
    for example
    '''
    _valid_etypes = {'example', 'sequence_example'}

    def __init__(self,
        schema:dict, etype:str='example',
        context_features:list=None,
        sequence_features:list=None,
    ):
        self.schema = schema
        self.etype = etype

        if context_features is None and etype == 'example':
            context_features = list(schema.keys())

        if sequence_features is not None and context_features is None:
            context_features = [k for k in list(schema.keys()) if k not in sequence_features]

        self.context_features = context_features
        self.sequence_features = sequence_features



    @property
    def etype(self):
        return self._etype

    @etype.setter
    def etype(self, value):
        if value not in self._valid_etypes:
            print('{} is not in {}. Defaulting to "example".'.format(
                value, self._valid_etypes
            ))
            value = 'example'
        self._etype = value

    @etype.deleter
    def etype(self):
        del self._etype


    @property
    def schema(self):
        return self._schema
    @schema.setter
    def schema(self, value:dict):
        if type(value) is not dict:
            raise(ValueError('schema expected to be type dict.'))

        for fname, finfo in value.items():
            if 'data_format' not in finfo:
                finfo['data_format'] = 'channels_last' if 'encode' in finfo else None
            if 'channel_names' not in finfo:
                finfo['channel_names'] = None
            if 'encode' not in finfo:
                finfo['encode'] = None

        self._schema = value
    @schema.deleter
    def schema(self):
        del self._schema

    @property
    def context_features(self):
        return self._context
    @context_features.setter
    def context_features(self, value:list):
        if value is not None:
            value = [v for v in self.schema.keys() if v in value]
        self._context = value
    @context_features.deleter
    def context_features(self):
        del self._context


    @property
    def sequence_features(self):
        return self._sequence
    @sequence_features.setter
    def sequence_features(self, value:list):
        if value is not None:
            value = [v for v in self.schema.keys() if v in value]
        self._sequence = value
    @sequence_features.deleter
    def sequence_features(self):
        del self._sequence



    def split_features(self, features):
        cf = {} if self.context_features is None else filter_dict(self.context_features, features)
        sf = {} if self.sequence_features is None else filter_dict(self.sequence_features, features)
        return (cf, sf)
