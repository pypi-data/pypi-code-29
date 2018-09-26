from kpc_connector_utils.common.pusher import Pusher
from kpc_connector_utils.common.types import EventType

import os


class BaseConfig:
    def __init__(self, env_name=''):
        func_name = os.getenv('{}'.format(env_name))
        if not func_name:
            raise ValueError('No env defined in system env for env_name: {}'.format(env_name))

        self._func_name = func_name
        self._event_type = EventType.Event

    def set_event_type(self, value):
        self._event_type = value
        return self

    def set_func_name(self, value):
        self._func_name = value
        return self

    def build(self):
        return Pusher(self)
