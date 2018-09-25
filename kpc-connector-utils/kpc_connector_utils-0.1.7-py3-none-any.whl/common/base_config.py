from kpc_connector_utils.common.pusher import Pusher
from kpc_connector_utils.common.types import EventType

import os


class BaseConfig:
    def __init__(self, env_name):
        func_name = os.getenv('{}'.format(env_name))
        if not func_name:
            raise ValueError('No env defined in system env for env_name: {}'.format(env_name))

        self._func_name = func_name
        self._event_type = EventType.Event

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    @property
    def func_name(self):
        return self._func_name

    @func_name.setter
    def func_name(self, value):
        self._func_name = value

    def build(self):
        return Pusher(self)
