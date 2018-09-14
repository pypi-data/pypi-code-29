#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test logging filters
--------------------

Test suite for logging_filters.

"""

import unittest

from dataf import LvlFilter


class Record:
    def __init__(self, lvl):
        self.levelno = lvl


class TestLvlFilter(unittest.TestCase):
    """
    Test for LevelFilter class.
    """
    @classmethod
    def setUpClass(cls):
        cls.lvl_filter = LvlFilter(2, 4)

    def test_init(self):
        """
        Test __init__ method.
        """
        self.assertEqual(self.lvl_filter.low, 2)
        self.assertEqual(self.lvl_filter.high, 4)

    def test_fitler_with_lowest_value(self):
        """
        Test filter method with level equal to low value.
        """
        self.assertTrue(self.lvl_filter.filter(Record(2)))

    def test_fitler_with_highest_value(self):
        """
        Test filter method with level equal to high value.
        """
        self.assertTrue(self.lvl_filter.filter(Record(4)))

    def test_fitler_with_inbound_value(self):
        """
        Test filter method with value between low and high.
        """
        self.assertTrue(self.lvl_filter.filter(Record(3)))

    def test_fitler_with_outbound_value(self):
        """
        Test filter method with value greater than high and lower than low.
        """
        self.assertFalse(self.lvl_filter.filter(Record(1)))
        self.assertFalse(self.lvl_filter.filter(Record(5)))
