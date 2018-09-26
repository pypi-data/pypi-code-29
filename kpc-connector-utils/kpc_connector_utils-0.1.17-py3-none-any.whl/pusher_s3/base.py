from __future__ import print_function
from kpc_connector_utils.common.base_config import BaseConfig
from kpc_connector_utils.pusher_s3.data_type import DataType

import re


class BasePutS3Config(BaseConfig):
    def __init__(self, func_env_name):
        super().__init__(func_env_name)
        self._data_type = None
        self._s3_prefix_key = None
        self._s3_file_name = None
        self._s3_bucket = None
        self._s3_time_prefix_key = None
        self._is_time_flag = True

    def set_data_type(self, value):
        if not value.upper() == DataType.CSV and not value.upper() == DataType.JSON:
            raise ValueError('This data type is not support.')

        self._data_type = value
        return self

    def set_s3_prefix_key(self, value):
        self._s3_prefix_key = value
        return self

    def set_s3_file_name(self, value):
        self._s3_file_name = value
        return self

    def set_s3_bucket(self, value):
        self._s3_bucket = value
        return self

    def set_s3_time_prefix_key(self, value):
        if not value:
            return

        checks = value.split('%')
        if len(checks) == 1:
            raise ValueError('Time directive should be include at least 1')

        pattern = '^[a,A,b,B,c,d,H,I,j,m,M,p,S,U,w,W,x,X,y,Y,Z].*$'
        p = re.compile(pattern)

        for x in checks:
            res = True if p.match(x) else False
            if not res:
                raise ValueError('Time directive is not in correct format: "{}"'.format(x))

        self._s3_time_prefix_key = value
        return self

    def set_is_time_flag(self, value):
        self._is_time_flag = value
        return self

    def set_by_dict(self, config: dict):
        if config.get('data_type'):
            self.set_data_type(config.get('data_type'))

        if config.get('s3_prefix_key'):
            self.set_s3_prefix_key(config.get('s3_prefix_key'))

        if config.get('s3_file_name'):
            self.set_s3_file_name(config.get('s3_file_name'))

        if config.get('s3_bucket'):
            self.set_s3_bucket(config.get('s3_bucket'))

        if config.get('s3_time_prefix_key'):
            self.set_s3_time_prefix_key(config.get('s3_time_prefix_key'))

        if config.get('is_time_flag'):
            self.set_is_time_flag(config.get('is_time_flag'))

        return self

    def get_data_dict(self):
        return {
            'data_type': self._data_type,
            's3_prefix_key': self._s3_prefix_key,
            's3_file_name': self._s3_file_name,
            's3_bucket': self._s3_bucket,
            's3_time_prefix_key': self._s3_time_prefix_key,
            'is_time_flag': True if self._is_time_flag else False
        }
