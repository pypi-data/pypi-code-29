"""Aries agent for python wsgi application server
Jennifer version 5 agent for python
"""

import os
from . import config
from . import wrap


__version__ = '5.3.0.11'
__author__ = 'Luavis'


def wsgi_app(app):
    if os.environ.get('JENNIFER_MASTER_ADDRESS') is not None:
        return wrap.wsgi.wrap_wsgi_app(app)
    return app
