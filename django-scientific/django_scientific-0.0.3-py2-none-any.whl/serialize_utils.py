# -*- coding:utf-8 -*-

import numpy as np


def serialize_numpy_array(arr):
    result = {
        "type": "NumpyArray",
        "dtype": arr.dtype.str,
        "shape": list(arr.shape),
        "data": arr.tolist()
    }
    return result


def deserialize_numpy_array(data):
    if isinstance(data, list):
        return np.array(data)
    elif isinstance(data, dict):
        return np.array(data['data'], dtype=data.get('dtype'))
    else:
        raise NotImplementedError(u'Cannot deserialize data type {} into numpy array'.format(type(data)))
