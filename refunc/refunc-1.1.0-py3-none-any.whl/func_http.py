# -*- coding: utf-8 -*-

import base64
import json
import re
import sys
import time
from collections import Iterable

import requests
import six

from .env import current_env
from .errors import ResultError
from .util import remote_logger, sys_logger
from .version import git_commit, version

__all__ = ['FuncHTTP']

__user_agent__ = 'py-refunc v1({},build:{})'.format(version, git_commit)


class FuncHTTP(object):
    """
    FuncHTTP wraps a refunc task using http api
    """

    __json_header = {"Accept": "application/json"}
    __timeout_tuple = (7, 13)  # connect, read timeout
    __min_timeout = 30  # min working timeout 30s
    __max_timeout = 4 * 60 * 60  # max working timeout 4h
    __default_chunk_size = 4 * 1024  # 4K

    def __init__(self, endpoint: str):
        super().__init__()

        self.__endpoint = endpoint.rstrip('/')  # normalize
        self.__http_base = '/'.join([current_env().base_url.rstrip('/'), self.endpoint])

    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @property
    def base(self) -> str:
        return self.__http_base

    @property
    def name(self) -> str:
        n = self.endpoint.split("/")[-1]
        if not n:
            return 'untitled'
        return n

    @property
    def meta(self) -> dict:
        try:
            r = requests.get(self.base + '/_meta')
            if not r.ok:
                sys_logger.warning(
                    '<{}> cannot get meta: {}({})'.format(
                        self.name, self.base, r.status_code
                    )
                )
                return {}
            return r.json()
        except Exception as e:
            sys_logger.error(
                '<{}> failed to request meta, {}: {}'.format(
                    self.name, type(e).__name__, e
                )
            )
            return {}

    def invoke(self, request=None, **kwargs):
        if request and not isinstance(request, dict):
            raise ValueError(
                'request must be a dict, {} got'.format(type(request).__name__)
            )
        if request:
            kwargs.update(request)

        env = current_env()

        # prepare headers
        headers = FuncHTTP.__json_header.copy()

        # forward callers path
        headers.update(
            {
                "User-Agent": __user_agent__,
                "X-Refunc-In-Cluster": "true" if env.in_cluster else "false",
                "X-Refunc-Callers": ','.join(env.callers + [env.name]),
                "X-Refunc-User": env.name,
            }
        )

        params = {}
        if env.pull_logs:
            params['recv_log'] = True

        # build streaming api endpoint
        url = self.base + "/tasks"

        result = None
        exc_info = None
        err_counter = 0
        waitt, maxwait = 0.01, 1
        minto, maxto = FuncHTTP.__min_timeout, FuncHTTP.__max_timeout

        t0 = t = time.time()

        # using session to utilize the connection reuse
        with requests.Session() as session:
            while True:
                dt = t - t0
                if dt > minto and (err_counter > 17 or dt > maxto):
                    # break when:
                    # 1. dt > min working timeout(which is the min timeout)
                    # and number of retry > 17 or dt > max working timeout
                    break

                try:
                    rsp = session.request(
                        'POST',
                        url,
                        stream=True,
                        headers=headers,
                        params=params,
                        json=kwargs,
                        timeout=FuncHTTP.__timeout_tuple,
                    )

                    if not rsp.ok:
                        if (
                            rsp.headers['content-type'].lower().find('appliaction/json')
                            != -1
                        ):
                            err = rsp.json()
                            raise ResultError(self.name, err['code'], err['msg'])

                        raise ResultError(self.name, rsp.status_code, rsp.content)

                    result = self.__readloop(rsp)
                    break

                except ResultError as e:
                    if e.code >= 400:
                        exc_info = sys.exc_info()
                        break
                except (
                    requests.exceptions.Timeout,
                    requests.exceptions.ConnectionError,
                ):
                    time.sleep(waitt)  # have a rest
                    waitt = min(waitt * 2.0, maxwait)
                except Exception:
                    exc_info = sys.exc_info()
                    break

                # update states
                t = time.time()
                err_counter += 1

        if exc_info:
            six.reraise(*exc_info)

        dt = time.time() - t0
        if result or isinstance(result, Iterable):
            if dt > 3:
                sys_logger.warning(
                    'detect slow response from "{}", using {:.3f}s{}'.format(
                        self.name,
                        dt,
                        ' with {} retires'.format(err_counter)
                        if err_counter > 0
                        else '',
                    )
                )
            return result

        raise ResultError(504, self.name, 'retry failed in {:.3f}s'.format(dt))

    def __readloop(self, rsp):
        charset = rsp.headers.get('content-type', default='')
        enc_search = re.search(r'charset=(?P<enc>\S*)', charset)
        if enc_search is not None:
            encoding = enc_search.group('enc')
        else:
            encoding = 'utf-8'

        for line in rsp.iter_lines(chunk_size=FuncHTTP.__default_chunk_size):
            if line.startswith(b'{"a":"_ping"}'):
                continue

            evt = json.loads(line.decode(encoding))

            if 'a' not in evt:
                if 'code' in evt and 'msg' in evt:
                    raise ResultError(self.name, evt['code'], evt['msg'])
                raise ResultError(self.name, 500, line)

            if evt['a'] == 'log':
                remote_logger.debug(evt['p'])
                continue

            if evt['a'] == 'rsp':
                rsp.close()
                return self.__parse_rsp(evt['p'])

            if evt['a'] == 'err':
                msg = evt['p']
                if not isinstance(msg, six.string_types):
                    msg = msg.decode('utf-8')
                raise ResultError(self.name, 500, msg)

        raise ResultError(self.name, 400, 'empty response')

    def __parse_rsp(self, rsp):
        if not isinstance(rsp, str):
            return rsp
        try:
            return base64.decodebytes(rsp.encode('utf-8'))
        except:
            return rsp

    def __call__(self, request=None, **kwargs):
        return self.invoke(request, **kwargs)
