from __future__ import print_function
from kpc_connector_utils.pusher_s3.base import BasePutS3Config
from kpc_connector_utils.common.zip import compress

import json


class PutS3Config(BasePutS3Config):
    def __init__(self, s3_pusher_env):
        super().__init__(s3_pusher_env)
        self._compress_data = None
        self._raw_data = None

    def __str__(self):
        data_dict = self.get_data_dict()
        data_dict['compress_data'] = self._compress_data

        value = {'StreamingS3Event': data_dict}

        return json.dumps(value)

    def set_data(self, value):
        self._compress_data = compress(value)
        return self

    def set_raw_data(self, value):
        self._raw_data = value
        return self

    def set_by_dict(self, config: dict):
        super().set_by_dict(config)

        if config.get('data'):
            self.set_data(config.get('data'))

        if config.get('raw_data'):
            self.set_raw_data(config.get('raw_data'))

        return self
