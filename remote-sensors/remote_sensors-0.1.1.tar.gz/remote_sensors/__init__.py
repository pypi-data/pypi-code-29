"""Remote Sensors API index."""
from remote_sensors.models import Request, Response, URI
from remote_sensors import xbee
from remote_sensors.xbee import Device, bind_to_device
from remote_sensors import app
from remote_sensors.app import request, response
from remote_sensors.registration import is_registration


__all__ = [
    'Request', 'URI', 'Response', 'Device',
    'request', 'response',
    'app', 'xbee', 'is_registration', 'bind_to_device',
]
