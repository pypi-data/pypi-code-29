# /usr/bin/env python
# coding=utf-8

import os
import unittest
from tests import context

test_dir = os.path.join(os.path.dirname(__file__), "..")
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
