'''
Python mapping for the MASShortcut framework.

This module does not contain docstrings for the wrapped code, see
<https://github.com/shpakovski/MASShortcut> for documentation.
'''

import objc
import sys
import os
import Foundation

from MASShortcut import _metadata
from MASShortcut._inlines import _inline_list_


sys.modules['MASShortcut'] = mod = objc.ObjCLazyModule(
    "MASShortcut",
    "com.github.shpakovski.MASShortcut",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "MASShortcut.framework"),
    _metadata.__dict__, _inline_list_, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['MASShortcut._metadata']
