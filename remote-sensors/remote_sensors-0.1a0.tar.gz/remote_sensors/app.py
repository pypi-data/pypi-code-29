import functools

from digi.xbee.devices import XBeeDevice
from digi.xbee.models.message import XBeeMessage

from remote_sensors.log import logger
from remote_sensors.models import (
    is_request,
    is_response,
    Request,
    Response,
)
from remote_sensors import xbee
from remote_sensors.xbee import SensorRequest, SensorResponse


streams = dict()


def search_stream_request(request: Request):
    for tran, stream in streams.items():
        if request.uri == stream.uri:
            return tran
    return None


def init(device: XBeeDevice):
    """Initialization of device."""
    for cbk in xbee._callbacks:
        device.add_data_received_callback(cbk)


def request(method: str = None, pass_message: bool = False):  # noqa: C901
    """Wrap the XBeeMessage and receive only Remote Sensor Requests.

    Returning a Response object will result in replying to the request.

    This decorator will *not* bind the callback to the device.

    Usage:

    @remote_sensors.request(method='GET')
    def handle_requests(request: remote_sensors.Request) -> remote_sensors.Response:
        return remote_sensors.Response()

    """
    def decorator(fn):
        @functools.wraps(fn)
        def wrap_xbee_message_for_request(xbee_message: XBeeMessage, *args, **kwargs):
            if not is_request(xbee_message):
                logger.debug(f'[Skipping] Message is no request')
                return None
            logger.debug(f'Wrapped request for {xbee_message.data}')
            sensor_message = SensorRequest(message=xbee_message)

            if method and method != sensor_message.request.method:
                logger.debug(f'[Skipped] Request method is filtered, expected: {method}, '
                             f'actual: {sensor_message.request.method}')
                return None

            kwargs['streams'] = streams

            try:
                kwargs['addresses'] = sensor_message.addresses
            except Exception as e:
                kwargs['addresses'] = None
                logger.error(f'Failed to get the message addresses, {e}')

            if pass_message:
                kwargs['sensor_message'] = sensor_message

            _response = None
            try:
                _response = fn(request=sensor_message.request,
                               *args, **kwargs)
            except Exception as e:
                logger.error(f'Error while handling the request - {e}')
            else:
                if _response and isinstance(_response, Response):
                    sensor_message.reply(_response)
            finally:
                return _response
        return wrap_xbee_message_for_request
    return decorator


def response(status: str = None, pass_message: bool = False):  # noqa: C901
    """Remote Sensors API Response handler.

    This decorator does *not* bind the callback with the device.

    As the Remote Sensors API does not define how to reply to a response
    message, the return value is returned by does not reply to the message.

    Usage:

    @remote_sensors.response()
    def handle_response(response: remote_sensors.Response):
        pass
    """
    def decorator(fn):

        @functools.wraps(fn)
        def wrap_xbee_message(xbee_message: XBeeMessage, *args, **kwargs):
            if not is_response(xbee_message):
                logger.debug('[Skipping] Message is not a response.')
                return None

            logger.debug(f'Wrapped response for {xbee_message.data}')
            sensor_message = SensorResponse(message=xbee_message)

            if status and status != sensor_message.response.status:
                logger.debug(f'[Skipped] Response was filtered, expected: {status}, '
                             f'actual: {sensor_message.response.status}')
                return None

            kwargs['streams'] = streams

            try:
                kwargs['addresses'] = sensor_message.addresses
            except Exception as e:
                kwargs['addresses'] = None
                logger.error(f'Failed to get the message addresses, {e}')

            if pass_message:
                kwargs['sensor_message'] = sensor_message

            returned_value = None
            try:
                returned_value = fn(response=sensor_message.response,
                                    *args, **kwargs)
            except Exception as e:
                logger.error(f'Error while handling the response - {e}')
            finally:
                return returned_value

        return wrap_xbee_message
    return decorator
