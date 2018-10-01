import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf


from ..utils.encode import encode_codex
from ..utils.utils import flatten_nested_dict, filter_dict

from .base import Base

class Encode(Base):


    def encode(self, features:dict, etype):
        return {
            fname: self.encode_feature(fname, fdata, etype)
            for fname, fdata in features.items()
        }

    def encode_feature(self, fname, fdata, etype):
        finfo = self.schema[fname]
        efunc = encode_codex(finfo['encode'], etype)
        return efunc(finfo, fdata)

    def encode_features(self, features:dict, etype:str='example'):
        wrap = tf.train.Features if etype == 'example' else tf.train.FeatureLists
        efeat = self.encode(features, etype)
        feats = flatten_nested_dict(efeat)
        return wrap(feature=feats) if etype == 'example' else wrap(feature_list=feats)

    def _example(self, data):
        feats = data if self.context_features is None else filter_dict(self.context_features, data)
        return tf.train.Example(features=self.encode_features(feats, 'example'))

    def _sequence_example(self, data):
        cfeat, sfeat = self.split_features(data)
        cfeat = self.encode_features(cfeat, 'example')
        sfeat = self.encode_features(sfeat, 'sequence_example')
        return tf.train.SequenceExample(context=cfeat, feature_lists=sfeat)

    def to_example(self, data):
        return self._example(data) if self.etype == 'example' else \
               self._sequence_example(data)
