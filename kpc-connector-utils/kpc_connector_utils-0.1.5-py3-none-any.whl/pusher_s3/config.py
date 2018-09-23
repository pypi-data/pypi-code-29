from __future__ import print_function
from kpc_connector_utils.base.base_config import BaseConfig

import re
import zlib
import json
import base64


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
                'data_type': self.data_type,
                's3_prefix_key': self.s3_prefix_key,
                's3_file_name': self.s3_file_name,
                's3_bucket': self.s3_bucket,
                's3_time_prefix_key': self.s3_time_prefix_key,
                'compress_data': self.data,
                'is_time_flag': True if self.is_time_flag else False
            }
        }

        return json.dumps(value)

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        if not value == DataType.CSV or not value == DataType.JSON:
            raise ValueError('This data type is not support.')

        self._data_type = value

    @property
    def s3_prefix_key(self):
        return self._s3_prefix_key

    @s3_prefix_key.setter
    def s3_prefix_key(self, value):
        self._s3_prefix_key = value

    @property
    def s3_file_name(self):
        return self._s3_file_name

    @s3_file_name.setter
    def s3_file_name(self, value):
        self._s3_file_name = value

    @property
    def s3_bucket(self):
        return self._s3_bucket

    @s3_bucket.setter
    def s3_bucket(self, value):
        self._s3_bucket = value

    @property
    def s3_time_prefix_key(self):
        return self._s3_time_prefix_key

    @s3_time_prefix_key.setter
    def s3_time_prefix_key(self, value):
        if not value:
            return

        checks = value.split('%')
        pattern = '^%[a,A,b,B,c,d,H,I,j,m,M,p,S,U,w,W,x,X,y,Y,Z].*$'
        p = re.compile(pattern)

        for x in checks:
            res = True if p.match(x) else False
            if not res:
                raise ValueError('Time directive is not in correct format: "{}"'.format(x))

        self._s3_time_prefix_key = value

    @property
    def data(self):
        return self._compress_data

    @data.setter
    def data(self, value):
        self._compress_data = base64.b64encode(zlib.compress(value.encode('utf-8'))).decode()

    @property
    def is_time_flag(self):
        return self._is_time_flag

    @is_time_flag.setter
    def is_time_flag(self, value):
        self._is_time_flag = value


class DataType:
    CSV = 'CSV'
    JSON = 'JSON'
