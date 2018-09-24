import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .base import Base
from ..utils.features import unwrap_features, record_feature
from ..utils.utils import flatten_nested_dict, default_channel_names
from ..utils.types import tf_encoded_type

class Decode(Base):

    def decode(self, features:dict, etype):
        return {
            fname: self.decode_feature(fname, finfo, etype)
            for fname, finfo in features.items()
        }


    def decode_feature(self, fname, finfo, etype):
        if finfo['encode'] is not None:
            return self.decode_channels(finfo, etype)
        else:
            wrap = record_feature(finfo['length'], etype)
            return wrap(finfo['shape'], dtype=finfo['dtype'])


    def decode_channels(self, finfo, etype):
        wrap = record_feature(finfo['length'], etype)

        encode = finfo['encode']
        dtype = tf_encoded_type(finfo['dtype'], encode)
        shape = [] if encode in ['bstrings', 'bdstring'] else finfo['shape'][0]
        channel_names = finfo['channel_names'] if finfo['channel_names'] is not None else default_channel_names(finfo['shape'], finfo['data_format'])

        if self.etype == 'example':
            return {channel: wrap(shape, dtype=dtype) for channel in channel_names}
        return wrap(shape, dtype=dtype)


    def decode_features(self, features, etype):
        dfeat = self.decode(features, etype)
        feats = flatten_nested_dict(dfeat)
        return feats

    def decode_schema(self):
        if self.etype == 'sequence_example':
            cfeat, sfeat = self.split_features(self.schema)
            cfeat = self.decode_features(cfeat, 'example')
            sfeat = self.decode_features(sfeat, 'sequence_example')
            return cfeat, sfeat
        else:
            feats = self.decode_features(self.schema, 'example')
            return feats


    def _example_record(self, serialized_record):
        feats = self.decode_schema()
        return tf.parse_single_example(serialized_record, feats)

    def _sequence_example_record(self, serialized_record):
        cfeat, sfeat = self.decode_schema()
        # cfeat = {}
        return tf.parse_single_sequence_example(serialized_record, context_features=cfeat, sequence_features=sfeat)

    def from_record(self, serialized_record):
        return self._example_record(serialized_record) if self.etype == 'example' else \
               self._sequence_example_record(serialized_record)
