# -*- coding: utf-8 -*-

"""Test functions that get data."""

import os
import unittest

from bio2bel_uniprot import get_mappings_df

HERE = os.path.abspath(os.path.dirname(__file__))
URL = os.path.join(HERE, 'test.tsv')


class TestGet(unittest.TestCase):
    """Test getting data."""

    def test_get_mappings(self):
        """Test getting the full mappings file."""
        df = get_mappings_df(url=URL)
        self.assertEqual(6, len(df.index))
