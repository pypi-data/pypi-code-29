from __future__ import print_function
from kpc_connector_utils.common.base_config import BaseConfig
from kpc_connector_utils.common.zip import compress

import re
import json


class PutS3Config(BaseConfig):
    def __init__(self, s3_pusher_env):
        super().__init__(s3_pusher_env)
        self._data_type = ''
        self._s3_prefix_key = ''
        self._s3_file_name = ''
        self._s3_bucket = ''
        self._s3_time_prefix_key = ''
        self._compress_data = ''
        self._raw_data = ''
        self._is_time_flag = True

    def __str__(self):
        value = {
            'StreamingS3Event': {
                'data_type': self._data_type,
                's3_prefix_key': self._s3_prefix_key,
                's3_file_name': self._s3_file_name,
                's3_bucket': self._s3_bucket,
                's3_time_prefix_key': self._s3_time_prefix_key,
                'compress_data': self._compress_data,
                'is_time_flag': True if self._is_time_flag else False
            }
        }

        return json.dumps(value)

    def get_data_type(self):
        return self._data_type

    def set_data_type(self, value):
        if not value.upper() == DataType.CSV and not value.upper() == DataType.JSON:
            raise ValueError('This data type is not support.')

        self._data_type = value

    def get_s3_prefix_key(self):
        return self._s3_prefix_key

    def set_s3_prefix_key(self, value):
        self._s3_prefix_key = value

    def get_s3_file_name(self):
        return self._s3_file_name

    def set_s3_file_name(self, value):
        self._s3_file_name = value

    def get_s3_bucket(self):
        return self._s3_bucket

    def set_s3_bucket(self, value):
        self._s3_bucket = value

    def get_s3_time_prefix_key(self):
        return self._s3_time_prefix_key

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

    def get_data(self):
        return self._compress_data

    def set_data(self, value):
        self._compress_data = compress(value)

    def get_is_time_flag(self):
        return self._is_time_flag

    def set_is_time_flag(self, value):
        self._is_time_flag = value

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


class DataType:
    CSV = 'CSV'
    JSON = 'JSON'
