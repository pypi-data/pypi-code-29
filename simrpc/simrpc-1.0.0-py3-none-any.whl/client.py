import zmq
import logging
from functools import wraps
from zmq.asyncio import Context
from .message import decode_msg, encode_msg

logger = logging.getLogger(__package__)


class SimRpcClient:
    def __init__(self, server_address="tcp://localhost:5559",
                 is_async=False):
        self.is_async = is_async
        self.server_address = server_address

    def get_socket(self):
        if self.is_async:
            context = Context()
        else:
            context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self.server_address)
        return socket

    def task(self, response_only: bool = False, func=False):

        def decorate(func):

            @wraps(func)
            def wrapper(*args, **kwargs):
                cls = args[0]
                if hasattr(cls, "__module__") and \
                        cls.__class__.__name__ != "function":
                    cls = args[0]
                    args = args[1:]
                else:
                    cls = func
                data = decode_msg(
                    service=cls.__class__.__name__ if cls else "",
                    entry=func.__name__,
                    args=args,
                    kwargs=kwargs
                )
                if hasattr(cls, "socket"):
                    socket = getattr(cls, "socket")
                else:
                    socket = self.get_socket()
                    setattr(cls, "socket", socket)
                socket.send(data)
                res = socket.recv()
                return encode_msg(res, response_only=response_only)

            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                cls = args[0]
                if hasattr(cls, "__module__") and \
                        cls.__class__.__name__ != "function":
                    cls = args[0]
                    args = args[1:]
                else:
                    cls = func
                data = decode_msg(
                    service=cls.__class__.__name__ if cls else "",
                    entry=func.__name__,
                    args=args,
                    kwargs=kwargs
                )
                if hasattr(cls, "socket"):
                    socket = getattr(cls, "socket")
                else:
                    socket = self.get_socket()
                    setattr(cls, "socket", socket)
                await socket.send(data)
                res = await socket.recv()
                return encode_msg(res, response_only=response_only)

            if self.is_async:
                return async_wrapper
            else:
                return wrapper
        return decorate
