import functools

from dataclasses import dataclass
from typing import Any

from digi.xbee.devices import RemoteXBeeDevice, XBeeDevice
from digi.xbee.models.message import XBeeMessage

from remote_sensors.exc import RemoteSensorsApiError
from remote_sensors.log import logger
from remote_sensors.models import Request, Response


_callbacks = list()


def bind_to_device():
    """Auto-registration to the device.

    Has to be the most outer decorator!

    Usage:

    @remote_sensors.register_in(xbee.device)
    @someotherdecorator()
    def handle_something():
        pass
    """
    def decorator(fn):
        _callbacks.append(fn)

        @functools.wraps(fn)
        def execute(*args, **kwargs):
            """Simply call the function."""
            return fn(*args, **kwargs)

        return execute
    return decorator


@dataclass
class Device:
    """Context Manager for the Devices."""
    port: str
    baud: int
    device_class: Any
    device: Any = None

    def __enter__(self) -> XBeeDevice:
        if self.device is None:
            self.device = self.device_class(self.port, self.baud)
        self.device.open()
        logger.info(f'Device {self.device} is now opened.')

        return self.device

    def __exit__(self, *exc):
        if self.device is None:
            return

        self.device.close()
        logger.info(f'Device {self.device} was successfully closed.')
        return True


@dataclass(order=True)
class RemoteSensorMessage:
    """Remote Sensor API Message.

        Wraps the XBeeMessage and exposes some relevant
        variables through properties.

    """
    message: XBeeMessage

    @property
    def addresses(self) -> (str, str):
        """Tuple of addresses, (64 bit, 16 bit)."""
        small_address = str(self.source.get_16bit_addr())
        small_address = small_address.replace(' ', '')
        return str(self.source.get_64bit_addr()), small_address

    @property
    def source(self) -> RemoteXBeeDevice:
        return self.message.remote_device

    def as_dict(self):
        return {
            'addresses': self.addresses,
            'timestamp': self.message.timestamp,
        }


@dataclass
class SensorRequest(RemoteSensorMessage):
    """Sensor Request Message.

        Includes the XBeeMessage.

    """
    request: Request = None

    def __post_init__(self):
        if self.request or not self.message:
            return

        try:
            self.request = Request.from_bytearray(self.message.data)
        except RemoteSensorsApiError as e:
            logger.error(f'Failed to marshal request, {self.message}')

    def reply(self, response: Response):
        if not self.source.is_remote():
            return  # ??
        try:
            local_device = self.source.get_local_xbee_device()
            local_device.send_data_async(self.source, response.as_bytearray())
        except Exception as e:
            logger.error(f'Failed to send data, {e}')


@dataclass
class SensorResponse(RemoteSensorMessage):
    """Sensor Response Message.

        Includes the XBeeMessage.
    """
    response: Response = None

    def __post_init__(self):
        if self.response and not self.message:
            return

        try:
            self.response = Response.from_bytearray(self.message.data)
        except RemoteSensorsApiError as e:
            logger.error(f'Failed to marshal response, {self.message}')
