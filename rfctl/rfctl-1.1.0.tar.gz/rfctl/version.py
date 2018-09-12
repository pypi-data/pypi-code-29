# -*- coding: utf-8 -*-

import pkgutil

__ns__ = {}
exec(pkgutil.get_data(__package__, 'version.txt').decode('utf-8'), {}, __ns__)

version = __ns__['__version__']
git_commit = __ns__['__git__']

del pkgutil, __ns__
