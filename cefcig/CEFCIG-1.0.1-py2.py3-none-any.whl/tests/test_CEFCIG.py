#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_CEFCIG
----------------------------------

Tests for `CEFCIG` module.
"""

import unittest

import CEFCIG


class TestCefcig(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(CEFCIG.__version__)

    def tearDown(self):
        pass
