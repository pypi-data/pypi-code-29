from __future__ import print_function, division, absolute_import

from .main import TestRunner

import sys
t = TestRunner()
t.run(*sys.argv[1:])
sys.exit(0)