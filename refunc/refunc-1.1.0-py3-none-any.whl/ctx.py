# -*- coding: utf-8 -*-

import asyncio
import json
import os
import time
from collections import namedtuple
from datetime import timedelta
from io import BytesIO

import six
from minio import Minio
from minio.error import NoSuchKey
from minio.api import get_target_url, presign_v4

from .codec import get_codec
from .env import current_env, new_env
from .func import Func
from .interface import Context, Env, Handler, Request
from .util import (
    _get_data_size,
    content_type_by_name,
    get_default_threadpool,
    jsonline_dumps,
    sys_logger,
    to_bytes,
)


class BaseContext(Context):
    """First level of accessing context"""

    def __init__(self, parent: Context = None):
        self._parent = parent if parent else current_env().context
        self.__loop = None
        self.__mc = None

    def invoke(self, endpoint: str, request=None, **kwargs):
        result = self._do(endpoint, request, kwargs)
        if isinstance(result, bytes):
            return get_codec(endpoint).from_bytes(result)
        return result

    def put_object(
        self,
        object_name: str,
        bytes_or_filelike,
        content_type='',
        expires=60,
        shared=False,
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
        key = self.to_object_name(object_name)
        data = to_bytes(bytes_or_filelike)
        if not callable(getattr(data, 'read', None)):
            data = BytesIO(data)
        size = _get_data_size(data)
        if not content_type:
            content_type = content_type_by_name(key)
        self.s3_client.put_object(self.s3_bucket, key, data, size, content_type)
        if not shared:
            return self.s3_client.presigned_get_object(
                self.s3_bucket, key, timedelta(seconds=expires)
            )

        return self._new_mc(
            current_env().get('storage').public_endpoint
        ).presigned_get_object(self.s3_bucket, key, timedelta(seconds=expires))

    def get_object(self, object_name: str):
        """
        Retrieves an object from a bucket.

        Examples:
            with ctx.get_object('foo') as f:
                print(f.read())

        :param object_name: Name of object to read
        :return: :class:`urllib3.response.HTTPResponse` object.

        """
        return self.s3_client.get_object(
            self.s3_bucket, self.to_object_name(object_name)
        )

    def remove_object(self, object_name: str):
        """
        Remove an object from the bucket.

        :param object_name: Name of object to remove
        :return: None
        """
        return self.s3_client.remove_object(
            self.s3_bucket, self.to_object_name(object_name)
        )

    def object_exists(self, object_name: str) -> bool:
        """
        Check if objec exists.

        :param object_name: Name of object to remove
        :return: None
        """
        try:
            self.s3_client.stat_object(self.s3_bucket, self.to_object_name(object_name))
            return True
        except NoSuchKey:
            return False

    @property
    def s3_client(self):
        if self.__mc:
            return self.__mc
        # creates
        self.__mc = self._new_mc(current_env().get('storage').endpoint)
        return self.__mc

    def _new_mc(self, endpoint: str) -> Minio:
        # creates
        env = current_env()
        cred = env.credentials
        if endpoint.startswith("https://"):
            endpoint, secure = endpoint[len("https://") :], True
        elif endpoint.startswith("http://"):
            endpoint, secure = endpoint[len("http://") :], False
        else:
            secure = False
        return Minio(endpoint, cred.access_key, cred.secret_key, secure)

    @property
    def s3_bucket(self):
        return current_env().get('storage').bucket

    def to_object_name(self, key: str) -> str:
        path = os.path.normpath(
            os.path.join(self._s3_prefix(), os.path.normpath(key).lstrip('/'))
        )
        if path.endswith('/'):
            raise ValueError('access object ends with slash is not allowed')
        if not path.startswith(self._s3_prefix()):
            raise ValueError(f'access to {path} is not allowed')
        return path

    def _s3_prefix(self):
        # default behavior is to invoke parent's _s3_prefix
        if self._parent and isinstance(self._parent, BaseContext):
            return self._parent._s3_prefix()
        return current_env().get('storage').scope

    def publish(self, topic: str, payload: dict):
        raise NotImplementedError

    def subscribe(self, topic: str, callback):
        raise NotImplementedError

    @property
    def loop(self):
        """
        local event loop
        """
        if self.__loop is None:
            self.__loop = asyncio.new_event_loop()
        return self.__loop

    def ainvoke(self, endpoint: str, request=None, **kwargs):
        # save env in current thread
        env = current_env().new()
        if endpoint not in BaseContext.__known_funcs:
            self.ensure_func(endpoint)

        def invoke_future():
            with new_env(env):
                return self.invoke(endpoint, request, **kwargs)

        return self.loop.run_in_executor(get_default_threadpool(), invoke_future)

    def wait(self, *fs):
        if len(fs) == 0:
            return
        fut = asyncio.gather(*fs, loop=self.loop, return_exceptions=True)
        try:
            if asyncio.get_event_loop().is_running():
                # current thread has a running loop,
                # execute in a seperate thread instead
                get_default_threadpool().submit(
                    lambda: self.loop.run_until_complete(fut)
                ).result()
            else:
                self.loop.run_until_complete(fut)
        except RuntimeError:
            self.loop.run_until_complete(fut)
        return fut.result()

    def log(self, s: str, *args, **kwargs):
        sys_logger.info(s, *args, **kwargs)

    def _do(self, endpoint: str, request: dict, kwargs: dict):
        # default behavior is to invoke parent's _do
        if self._parent and isinstance(self._parent, BaseContext):
            return self._parent._do(endpoint, request, kwargs)
        return self.ensure_func(endpoint)(request, **kwargs)

    __known_funcs = {}

    def ensure_func(self, endpoint: str):
        endpoint = endpoint.rstrip('/')
        if endpoint not in BaseContext.__known_funcs:
            BaseContext.__known_funcs[endpoint] = Func(endpoint)

        return BaseContext.__known_funcs[endpoint]

    def __getattr__(self, item):
        "proxy to parent context"
        if self._parent:
            return getattr(self._parent, item)
        raise NotImplementedError


assert issubclass(BaseContext, Context)


class LocalContextBase(BaseContext):
    def __init__(self, endpoint, parent: Context = None):
        super().__init__(parent=parent)
        self.endpoint = endpoint

    def _s3_prefix(self):
        return os.path.join(current_env().get('storage').scope, self.endpoint)


class LocalHandlerContext(LocalContextBase):
    """
    Context with a handler mount at endpoint.

    This is intend to use in local dev mode
    """

    ReqTuple = namedtuple("LocalReqTuple", tuple(Request.__abstractmethods__))

    def __init__(self, handler: Handler, parent: Context = None):
        super().__init__(handler.endpoint, parent=parent)
        if not handler:
            raise ValueError('handler must be set')
        assert isinstance(handler, Handler)
        self.handler = handler

    def _do(self, endpoint: str, request: dict, kwargs: dict):
        if endpoint != self.handler.endpoint:
            return super()._do(endpoint, request, kwargs)

        env = current_env()
        req = LocalHandlerContext.ReqTuple(
            args=kwargs,
            callers=[env.name] if not env.callers else env.callers,
            hash='',
            options={},
            user=env.name,
        )
        if env.pull_logs:
            self.log('received request: {}'.format(req))
        return self.handler.on_request(self, req)


assert issubclass(LocalHandlerContext, Context)


class LocalExecContext(LocalContextBase):
    """
    Context with exec func in globals mount at endpoint
    """

    def __init__(self, endpoint: str, scope: dict = {}, parent: Context = None):
        super().__init__(endpoint, parent=parent)
        self.scope = scope
        self.mock_dict = {}

    def set_mock_endpoint(self, endpoint: str):
        '''
        set endpoint for current context to be mocked
        '''
        if not endpoint:
            return

        if self.endpoint:
            raise ValueError(
                'mock_endpoint() can only be invoked when current endpoint is empty, '
                'while "{}" got'.format(endpoint)
            )
        self.endpoint = endpoint
        self.log('current env is mocking "{}"'.format(endpoint))

    def add_mock_func(self, endpoint: str, func):
        '''
        add a mock function at "endpoint"
        '''
        if not hasattr(func, '__call__'):
            raise ValueError('func must be a callable')
        if endpoint:
            self.mock_dict[endpoint] = func
            self.log('starting mocking "{}"'.format(endpoint))

    def _do(self, endpoint: str, request: dict, kwargs: dict):
        if not endpoint:
            raise ValueError('endpoint must not be empty')

        if endpoint != self.endpoint:
            if endpoint in self.mock_dict:
                return self.mock_dict[endpoint](self, kwargs)

            return super()._do(endpoint, request, kwargs)

        on_request = self.scope.get('on_request', None)
        if not on_request or not hasattr(on_request, '__call__'):
            return super()._do(endpoint, request, kwargs)

        return get_codec(self.endpoint).to_bytes(on_request(self, kwargs))


assert issubclass(LocalExecContext, Context)
