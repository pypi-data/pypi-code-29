#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from kazoo.client import KazooClient

name = "weichigong"


class zconfig:

    def __init__(self, zkHosts, app, env):
        self.app = app
        self.env = env
        self.client = KazooClient(hosts=zkHosts)
        self.client.start()

    def getPath(self, path):
        return os.path.join('/', self.app, self.env, path)

    def set(self, path, value):
        fullPath = self.getPath(path)
        self.client.ensure_path(fullPath)
        self.client.set(fullPath, value)
