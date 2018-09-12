# -*- coding: utf-8 -*-

import abc

from six import with_metaclass

__all__ = ['Context', 'Env', 'Handler', 'Message', 'PayloadCodec', 'Request']


class Message(with_metaclass(abc.ABCMeta)):
    @abc.abstractproperty
    def topic(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def ts(self) -> int:
        """
        timestamp in microseconds
        """
        raise NotImplementedError

    @abc.abstractproperty
    def data(self) -> dict:
        """
        message payload
        """
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Message:
            return all(
                [
                    any(prop in B.__dict__ for B in C.__mro__)
                    for prop in cls.__abstractmethods__
                ]
            )
        return NotImplemented


class Request(with_metaclass(abc.ABCMeta)):
    @abc.abstractproperty
    def args(self) -> dict:
        """
        kv arguments passed func
        """
        raise NotImplementedError

    @abc.abstractproperty
    def hash(self) -> str:
        """
        the hash value of args
        """
        raise NotImplementedError

    @abc.abstractproperty
    def callers(self) -> [str]:
        """
        timestamp in microseconds
        """
        raise NotImplementedError

    @abc.abstractproperty
    def options(self) -> dict:
        """
        other options
        """
        raise NotImplementedError

    @abc.abstractproperty
    def user(self) -> dict:
        """
        user name that issed this request
        """
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Request:
            return all(
                [
                    any(prop in B.__dict__ for B in C.__mro__)
                    for prop in cls.__abstractmethods__
                ]
            )
        return NotImplemented


class Context(with_metaclass(abc.ABCMeta)):
    """Invocation context under current environment"""

    @abc.abstractmethod
    def invoke(self, endpoint: str, request=None, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def put_object(
        self, key: str, bytes_or_filelike, content_type='', expires=60, shared=False
    ):
        """
        Add a new object to the cloud storage server.

        NOTE: Maximum object size supported by this API is 5TiB.

        Examples:
         file_stat = os.stat('hello.txt')
         with open('hello.txt', 'rb') as data:
             minio.put_object('foo', 'bar', data, 'text/plain')

        - For length lesser than 5MB put_object automatically
          does single Put operation.
        - For length larger than 5MB put_object automatically
          does resumable multipart operation.

        :param object_name: Name of new object.
        :param bytes_or_filelike: Contents to upload.
        :param content_type: mime type of object as a string.
        :return: presigned url that can passed to other func within expires
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_object(self, object_name: str):
        """
        Retrieves an object from a bucket.

        Examples:
            with ctx.get_object('foo') as f:
                print(f.read())

        :param object_name: Name of object to read
        :return: :class:`urllib3.response.HTTPResponse` object.

        """
        raise NotImplementedError

    @abc.abstractmethod
    def remove_object(self, object_name: str):
        """
        Remove an object from the bucket.

        :param object_name: Name of object to remove
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def object_exists(self, object_name: str) -> bool:
        """
        Check if objec exists.

        :param object_name: Name of object to remove
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def publish(self, topic: str, payload: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def subscribe(self, topic: str, callback):
        raise NotImplementedError

    @abc.abstractmethod
    def ainvoke(self, endpoint: str, request=None, **kwargs):
        """
        Creates a background new invocation, which can be `wait`
        """
        raise NotImplementedError

    @abc.abstractmethod
    def wait(self, *fs):
        raise NotImplementedError

    @abc.abstractmethod
    def log(self, s: str, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Context:
            return all(
                [
                    any(prop in B.__dict__ for B in C.__mro__)
                    for prop in cls.__abstractmethods__
                ]
            )
        return NotImplemented


class Credentials(with_metaclass(abc.ABCMeta)):
    """
    Interface of func's credential
    """

    @abc.abstractproperty
    def access_key(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def secret_key(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def token(self) -> str:
        raise NotImplementedError


class Env(with_metaclass(abc.ABCMeta)):
    """
    Interface to access different enviroment
    """

    @abc.abstractproperty
    def base_url(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def pull_logs(self) -> bool:
        raise NotImplementedError

    @abc.abstractproperty
    def callers(self) -> [str]:
        raise NotImplementedError

    @abc.abstractproperty
    def in_cluster(self) -> bool:
        raise NotImplementedError

    @abc.abstractproperty
    def context(self) -> Context:
        raise NotImplementedError

    @abc.abstractproperty
    def credentials(self) -> Credentials:
        raise NotImplementedError

    def get(self, key: str, default=None):
        """
        retuns property for key or default
        """
        raise NotImplementedError

    def set(self, key: str, value):
        """
        set extra attributes for current env, this kv can be inherited by `new`
        """
        raise NotImplementedError

    def new(self, **overrides):
        """
        creates new of current env with overrides
        """
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Env:
            return all(
                [
                    any(prop in B.__dict__ for B in C.__mro__)
                    for prop in cls.__abstractmethods__
                ]
            )
        return NotImplemented


class Handler(with_metaclass(abc.ABCMeta)):
    @abc.abstractproperty
    def endpoint(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def dispatch(self, ctx: Context, msg: Message):
        """
        dispatch event on `topic` with `data`
        """
        raise NotImplementedError

    @abc.abstractmethod
    def on_request(self, ctx: Context, payload: Request):
        """
        handle request with payload
        """
        raise NotImplementedError


class PayloadCodec(with_metaclass(abc.ABCMeta)):
    @abc.abstractmethod
    def to_bytes(self, obj) -> bytes:
        raise NotImplementedError

    @abc.abstractmethod
    def from_bytes(self, data: bytes):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, C):
        if cls is PayloadCodec:
            return all(
                [
                    any(prop in B.__dict__ for B in C.__mro__)
                    for prop in PayloadCodec.__abstractmethods__
                ]
            )
        return NotImplemented

