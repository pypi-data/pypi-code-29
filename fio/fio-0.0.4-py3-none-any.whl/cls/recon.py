import sys
if 'np' not in sys.modules: import numpy as np
if 'tf' not in sys.modules: import tensorflow as tf

from .base import Base
from ..utils.decode import decode_bstring_array
from ..utils.utils import default_channel_names
from ..utils.types import tf_encoded_type, tf_type_string, list_like_q

from ..utils.features import unwrap_features

class Recon(Base):

    def reconstruct(self, features):
        features = features if type(features) is dict else {**features[0], **features[1]}
        features = {
            fname: self.reconstruct_feature(features, fname, finfo)
            for fname, finfo in self.schema.items()
        }
        if self.etype == 'sequence_example':
            return self.split_features(features)
        return features


    # TODO  cleanup logic


    def reconstruct_feature(self, features, fname, finfo):
        finfo = self.schema[fname]
        fdata = features[fname]
        dtype = finfo['dtype']

        etype = self.etype
        if fname in self.context_features: etype = 'example'

        if 'string' in tf_type_string(dtype):
            if list_like_q(features[fname]):
                features[fname] = decode_bstring_array(features[fname])
            elif type(fdata) is bytes:
                features[fname] = features[fname].decode()
            else:
                pass

        if finfo['encode'] is None:
            # sequence_examples encodes channels as unnamed features
            return features[fname]
        if etype == 'sequence_example':
            return [features[fname][0].T]

        return self.reconstruct_channels(features, fname, finfo)

    def reconstruct_channels(self, features, fname, finfo):

        # shorter variable names
        data_format   = finfo['data_format']
        dtype         = finfo['dtype']
        encode        = finfo['encode']
        channel_names = finfo['channel_names']
        if channel_names is None: channel_names = default_channel_names(finfo['shape'], data_format)

        se_dtype = tf_type_string(tf_encoded_type(dtype, encode))
        s_dtype  = tf_type_string(dtype)
        # if encoded as string but specified as not a string, decode
        if ('string' in se_dtype and 'string' not in s_dtype) or 'string' in encode:
            for channel in channel_names:
                features[channel] = tf.decode_raw(features[channel], dtype)

        joined = np.array([features[channel][0] for channel in channel_names], dtype=s_dtype).T
        return np.array([joined])

    def reconstitute(self, features, reconstruct_q=True, unwrap_q=True):
        if reconstruct_q:
            features = self.reconstruct(features)

        if unwrap_q:
            if self.etype == 'example':
                features = unwrap_features(features)
            else:
                features = (unwrap_features(features[0]), unwrap_features(features[1]))


        return features
