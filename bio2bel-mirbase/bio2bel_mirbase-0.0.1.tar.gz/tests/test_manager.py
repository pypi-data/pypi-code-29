# -*- coding: utf-8 -*-

"""Tests for Bio2BEL miRBase."""

import unittest

from bio2bel_mirbase import get_version
from tests.constants import TemporaryCacheClass


class TestMeta(unittest.TestCase):
    """Test metadata from Bio2BEL miRBase."""

    def test_get_version(self):
        """Test the get_version function."""
        self.assertIsInstance(get_version(), str)


class TestPopulate(TemporaryCacheClass):
    """Test the populated database."""

    def test_count(self):
        """Test the counts in the database."""
        self.assertEqual(2, self.manager.count_sequences())
