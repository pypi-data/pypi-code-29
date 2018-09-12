# -*- coding: utf-8 -*-

import asyncio
import base64
import hashlib
import json
import re
import sys
import threading
import time
import traceback
import weakref
from collections import Iterable, defaultdict
from concurrent.futures import CancelledError, Future, TimeoutError
from urllib.parse import urlparse

import six
from nats.aio.client import Client as NATS
from nats.aio.client import (
    AUTHORIZATION_VIOLATION,
    STALE_CONNECTION,
    ErrAuthorization,
    ErrStaleConnection,
    Msg,
    NatsError,
    __version__,
)
from nats.aio.errors import ErrMaxPayload
from nats.aio.utils import INBOX_PREFIX, new_inbox

from .env import current_env
from .errors import ResultError
from .util import (
    add_future_to_cancel_list,
    jsonline_dumps,
    remote_logger,
    start_or_get_running_loop,
    sys_logger,
)
from .version import git_commit, version

__all__ = ['FuncNATS']

DEFAULT_RESPONSE_TIMEOUT = 4 * 60 * 60  # 4hrs


class FuncNATS(object):
    """
    FuncNATS wraps a refunc task using http nats
    """

    def __init__(self, endpoint: str):
        super().__init__()
        self._loop = None
        self.__endpoint = endpoint.rstrip('/')  # normalize
        self.__endpoint_topic = '.'.join(self.endpoint.split("/"))

    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @property
    def endpoint_topic(self) -> str:
        '''
        <router_sink>.<ns>.<name>
        eg: refunc.buildins.cluster-info
        '''
        return f"{current_env().get('router_sink', 'refunc')}.{self.__endpoint_topic}"

    @property
    def name(self) -> str:
        n = self.endpoint.split("/")[-1]
        if not n:
            return 'untitled'
        return n

    @property
    def meta(self) -> dict:
        meta_topic = self.endpoint_topic + "._meta"

        rsp_f = self.__future()
        # add to permission watching list
        _permission_watchlist['pub'][meta_topic].add(rsp_f)

        def read_result(msg: Msg):
            rsp_f.set_result(msg.data)

        # send request
        self.__future(nats_conn().request(meta_topic, b'', cb=read_result))
        try:
            return json.loads(rsp_f.result(1).decode())
        except Exception as e:
            sys_logger.error(
                '<{}> failed to request meta, {}: {}'.format(
                    self.name, type(e).__name__, e
                )
            )
            return {}

    def invoke(self, request=None, **kwargs):
        nc = nats_conn()
        if not nc:
            raise RuntimeError('nats connection is not ready')

        if request and not isinstance(request, dict):
            raise ValueError(
                'request must be a dict, {} got'.format(type(request).__name__)
            )
        if request:
            kwargs.update(request)

        if kwargs is None:
            kwargs = {}

        env = current_env()

        request_msg = {
            'args': kwargs,
            'hash': hashlib.md5(jsonline_dumps(request).encode('utf-8')).hexdigest(),
            'callers': env.callers + [env.name],
            'user': env.name,
            'options': {},
        }

        log_subs_f: asyncio.Future = None
        if env.get('log_endpoint'):
            request_msg['options']['logEndpoint'] = env.get('log_endpoint')
        if not env.in_cluster and env.pull_logs:

            def on_log(msg: Msg):
                try:
                    remote_logger.debug(json.loads(msg.data.decode())['p'])
                except Exception:
                    self.__log_exce(*sys.exc_info())

            log_endpoint = '_refunc.forwardlogs.{}/{}'.format(
                self.endpoint, new_inbox()[len(INBOX_PREFIX) :]
            )
            request_msg['options']['logEndpoint'] = log_endpoint
            log_subs_f = self.__future(nc.subscribe(log_endpoint, cb=on_log))

        t0 = time.time()
        rsp_f = self.__future()
        # add to permission watching list
        _permission_watchlist['pub'][self.endpoint_topic].add(rsp_f)

        def read_result(msg: Msg):
            rsp_f.set_result(msg.data)

        # send request
        subs_f = self.__future(
            nc.request(
                self.endpoint_topic,
                jsonline_dumps(request_msg).encode('utf-8'),
                cb=read_result,
            )
        )
        result = None
        result_err = Exception()
        timeout = env.get('timeout', 0)
        if timeout <= 0:
            timeout = DEFAULT_RESPONSE_TIMEOUT
        try:
            subs_f.result()
            res = rsp_f.result(timeout).decode()
            rsp = json.loads(res)
            if rsp['a'] == 'rsp':
                result = self.__parse_rsp(rsp['p'])
            elif rsp['a'] == 'err':
                if 'Access denied' in rsp['p']:
                    result_err = ResultError(self.name, 401, rsp['p'])
                else:
                    result_err = ResultError(self.name, 500, rsp['p'])
            else:
                result_err = ResultError(
                    self.name, 500, 'Unknown event: {!r}'.format(res)
                )
        except ErrMaxPayload:
            result_err = ResultError(400, self.name, 'Maximum payload exceeded')
        except TimeoutError:
            result_err = ResultError(
                408, self.name, 'Timeout in {:.3f}s'.format(timeout)
            )
        except CancelledError:
            result_err = ResultError(500, self.name, 'Request was cancelled')
        finally:
            if log_subs_f:
                self.__future(nc.unsubscribe(log_subs_f.result()))

        if isinstance(result_err, ResultError):
            raise result_err

        dt = time.time() - t0
        if dt > 3:
            sys_logger.warning(
                'detect slow response from "{}", using {:.3f}s'.format(self.name, dt)
            )
        return result

    @property
    def loop(self):
        if not self._loop:
            self._loop = start_or_get_running_loop(run_in_backgroud=True)
        return self._loop

    def __future(self, f=None):
        return ensure_future(f, self.loop)

    def __log_exce(self, et, e: Exception, tb):
        if tb:
            for entry in traceback.format_exception(et, e, tb):
                for line in entry.split('\n'):
                    if line:
                        sys_logger.error(line)

    def __parse_rsp(self, rsp):
        if not isinstance(rsp, str):
            return rsp
        try:
            return base64.decodebytes(rsp.encode('utf-8'))
        except:
            return rsp

    def __call__(self, request=None, **kwargs):
        return self.invoke(request, **kwargs)


def ensure_future(f=None, loop=None):
    if not loop:
        loop = start_or_get_running_loop(run_in_backgroud=True)
    if f is None:
        fs = Future()
    else:
        fs = asyncio.run_coroutine_threadsafe(f, loop=loop)
    return add_future_to_cancel_list(fs)


_nats_lock = threading.Lock()
_nats_conn: NATS = None
_connect_max_timeout = 5
_permission_watchlist = {
    'pub': defaultdict(weakref.WeakSet),
    'sub': defaultdict(weakref.WeakSet),
}


if __version__ <= '0.7.0':
    PERMISSION_ERR = b'Permissions Violation'

    class _NATS(NATS):
        async def close(self):
            super().close()
            global _nats_conn
            with _nats_lock:
                if _nats_conn:
                    _nats_conn = None
                    sys_logger.debug('nats closed, last err: %s', self.last_error)

        def _process_info(self, info):
            super()._process_info(info)
            env = current_env()
            for i, srv in enumerate(self._server_pool):
                if not srv.discovered:
                    continue
                # modify connect url
                uri = srv.uri
                if uri.username:
                    continue
                url = uri.geturl()[len('nats://') :]
                if env.credentials.token:
                    url = 'nats://{}@{}'.format(env.credentials.token, url)
                elif env.credentials.access_key:
                    url = 'nats://{}:{}@{}'.format(
                        env.credentials.access_key, env.credentials.secret_key, url
                    )
                self._server_pool[i].uri = urlparse(url)

        @asyncio.coroutine
        def _process_err(self, err_msg):
            """
            Processes the raw error message sent by the server
            and close connection with current server.
            """
            if STALE_CONNECTION in err_msg:
                self._process_op_err(ErrStaleConnection)
                return

            if AUTHORIZATION_VIOLATION in err_msg:
                self._err = ErrAuthorization
            else:
                m = b'nats: ' + err_msg[0]
                self._err = NatsError(m.decode())
                if PERMISSION_ERR in err_msg[0]:
                    if self._error_cb is not None:
                        yield from self._error_cb(self._err)
                    return

            do_cbs = False
            if not self.is_connecting:
                do_cbs = True

            self._loop.create_task(self._close(NATS.CLOSED, do_cbs))


else:
    sys_logger.warning('do not know how to patch nats(%s) > 0.7.0', __version__)
    _NATS = NATS


PUB_PERMISSON_ERR = re.compile(r'.*Permissions Violation for Publish to \"(.+)?\"')

SUB_PERMISSON_ERR = re.compile(r'.*Permissions Violation for Subscription to \"(.+)?\"')

UNAUTHORIZED_ERR_BYTES = b'{"a":"err","p":"Access denied"}'
CONNECTIONLOST_ERR_BYTES = b'{"a":"err","p":"Connection lost"}'


def nats_conn(nats_urls: [str] = []) -> NATS:
    '''
    returns global connected nats connection
    '''
    global _nats_conn
    with _nats_lock:
        if _nats_conn and _nats_conn.is_connected:
            return _nats_conn
        # new instance
        _nats_conn = _NATS()

    loop = start_or_get_running_loop(run_in_backgroud=True)

    async def error_cb(e):
        msg = e.args[0] if len(e.args) > 0 else e
        msg = '{}'.format(msg)
        match = PUB_PERMISSON_ERR.match(msg)
        if match:
            topic = match.groups()[0]
            watchset = _permission_watchlist['pub'][topic]
            while len(watchset):
                f = watchset.pop()
                f.set_result(UNAUTHORIZED_ERR_BYTES)
            return

        match = SUB_PERMISSON_ERR.match(msg)
        if match:
            topic = match.groups()[0]
            # ignore log forwarding error
            if topic.startswith('_refunc.forwardlogs.'):
                sys_logger.debug('do not have permissions to pull logs')
                return
            watchset = _permission_watchlist['sub'][topic]
            while len(watchset):
                f = watchset.pop()
                f.set_result(UNAUTHORIZED_ERR_BYTES)
            return

        if 'Connection lost' in msg:

            def set_error():
                for topic in _permission_watchlist['pub']:
                    watchset = _permission_watchlist['pub'][topic]
                    while len(watchset):
                        f = watchset.pop()
                        f.set_result(CONNECTIONLOST_ERR_BYTES)

                for topic in _permission_watchlist['sub']:
                    watchset = _permission_watchlist['sub'][topic]
                    while len(watchset):
                        f = watchset.pop()
                        f.cancel()

            loop.call_later(0.002, set_error)

        sys_logger.error('nats on error, %s', e)

    env = current_env()
    if not nats_urls:
        nats_urls = [env.base_url]

    if env.get('ca_data', ''):
        import ssl

        tls_ctx = ssl.create_default_context(cadata=env.get('ca_data'))
    elif env.get('ca_file', ''):
        import ssl

        tls_ctx = ssl.create_default_context(cafile=env.get('ca_file'))
    else:
        tls_ctx = None

    conn_f = ensure_future(
        _nats_conn.connect(
            name=env.name,
            error_cb=error_cb,
            servers=nats_urls,
            max_reconnect_attempts=3,
            tls=tls_ctx,
        ),
        loop=loop,
    )
    try:
        conn_f.result(_connect_max_timeout)
        _nats_conn.options['max_reconnect_attempts'] = -1
    except (TimeoutError, CancelledError):
        sys_logger.error(
            'connecting to nats failed, last error: {}'.format(_nats_conn.last_error)
        )
        nc = _nats_conn
        loop.create_task(nc.close)
        with _nats_lock:
            _nats_conn = None

    return _nats_conn
