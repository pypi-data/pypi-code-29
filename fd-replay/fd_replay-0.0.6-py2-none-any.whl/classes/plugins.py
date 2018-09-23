# -*- coding: utf-8 -*-
"""fd-replay plugins"""

__author__  = "Adrien DELLE CAVE <adc@doowan.net>"
__license__ = """
    Copyright (C) 2018  fjord-technologies

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA..
"""

import abc
import logging
import Queue
import threading

from fd_replay.classes.target import FdReplayTarget
from fd_replay.classes.exceptions import FdReplayTargetFailed
from dwho.classes.plugins import DWhoPluginBase
from dwho.config import load_credentials

LOG = logging.getLogger('fd-replay.plugins')


class FdReplayPlugins(dict):
    def register(self, plugin):
        if not issubclass(plugin, FdReplayPlugBase):
            raise TypeError("Invalid Plugin class. (class: %r)" % plugin)
        return dict.__setitem__(self, plugin.PLUGIN_NAME, plugin)

PLUGINS   = FdReplayPlugins()


class FdReplayEndpoints(dict):
    def register(self, endpoint):
        if not isinstance(endpoint, FdReplayPlugBase):
            raise TypeError("Invalid Endpoint class. (class: %r)" % endpoint)
        return dict.__setitem__(self, endpoint.name, endpoint)

ENDPOINTS = FdReplayEndpoints()


class FdReplayEPTsSync(dict):
    def register(self, ept_sync):
        if not isinstance(ept_sync, FdReplayEPTSync):
            raise TypeError("Invalid Endpoint Sync class. (class: %r)" % ept_sync)
        return dict.__setitem__(self, ept_sync.name, ept_sync)

EPTS_SYNC = FdReplayEPTsSync()


class FdReplayEPTObject(object):
    def __init__(self, name, uid, endpoint, method, request, callback = None):
        self.name     = name
        self.uid      = uid
        self.endpoint = endpoint
        self.method   = method
        self.request  = request
        self.callback = callback
        self.result   = None
        self.errors   = []

    def get_uid(self):
        return self.uid

    def add_error(self, error):
        self.errors.append(error)
        return self

    def has_error(self):
        return len(self.errors) != 0

    def get_errors(self):
        return self.errors

    def set_result(self, result):
        self.result = result

        return self

    def get_result(self):
        return self.result

    def get_endpoint(self):
        return self.endpoint

    def get_method(self):
        return self.method

    def get_request(self):
        return self.request

    def __call__(self):
        if self.callback:
            return self.callback(self)


class FdReplayEPTSync(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name       = name
        self.queue      = Queue.Queue()
        self.results    = {}

    def qput(self, item):
        return self.queue.put(item)

    def qget(self, block = True, timeout = None):
        return self.queue.get(block, timeout)


class FdReplayPlugBase(threading.Thread, DWhoPluginBase):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        threading.Thread.__init__(self)
        DWhoPluginBase.__init__(self)
        self.daemon      = True
        self.name        = name
        self.credentials = None
        self.target      = None

    def safe_init(self):
        if self.config.get('credentials'):
            self.credentials = load_credentials(self.config['credentials'],
                                                config_dir = self.config['fd-replay']['config_dir'])

        self.target = FdReplayTarget(**{'name':        self.name,
                                        'config':      self.config['config'],
                                        'credentials': self.credentials}) 

        EPTS_SYNC.register(FdReplayEPTSync(self.name))

    def at_start(self):
        if self.name in EPTS_SYNC:
            self.start()

    def run(self):
        while True:
            r = None

            try:
                obj  = EPTS_SYNC[self.name].qget(True)
                func = "do_%s" % obj.get_method()
                if not hasattr(self, func):
                    LOG.warning("unknown method %r for endpoint %r", func, self.name)
                    continue

                r    = getattr(self, func)(obj)
            except Exception, e:
                obj.add_error(str(e))
                LOG.exception("%r", e)
            else:
                obj.set_result(r)
            finally:
                obj()

    def __call__(self):
        self.start()
        return self
