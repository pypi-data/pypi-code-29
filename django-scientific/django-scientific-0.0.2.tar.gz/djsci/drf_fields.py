# -*- coding:utf-8 -*-
# Django RestFramework (DRF) serializer fields

from rest_framework.fields import Field as DRFField
import numpy as np
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
from .serialize_utils import *


class DRFDataField(DRFField):
    def to_representation(self, value):
        if isinstance(value, np.ndarray):
            return serialize_numpy_array(value)
        else:
            raise NotImplementedError(u'Data type {} is not supported by DRFDataField.'.format(type(value)))

    def to_internal_value(self, data):
        if isinstance(data, dict):
            data_type = data.get('type')
            if data_type == 'NumpyArray':
                return deserialize_numpy_array(data)
            else:
                raise NotImplementedError(u'Not supported: {}'.format(data_type))

        raise NotImplementedError(u'Not supported: {}'.format(type(data)))


class DRFNumpyArrayField(DRFField):
    def to_representation(self, value):
        return serialize_numpy_array(value)

    def to_internal_value(self, data):
        return deserialize_numpy_array(data)


class DRFPandasDataFrameField(DRFField):
    def to_representation(self, value):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")

    def to_internal_value(self, data):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")


class DRFPandasSeriesField(DRFField):
    def to_representation(self, value):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")

    def to_internal_value(self, data):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")

