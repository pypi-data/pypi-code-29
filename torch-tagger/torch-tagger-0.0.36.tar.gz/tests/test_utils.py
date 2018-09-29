# -*- coding: utf-8 -*-
"""Test utils class"""

import unittest

from torch_tagger.utils import pad_seq


class TestUtil(unittest.TestCase):
    def test_pad_seq(self):
        r = pad_seq([1, 2, 3], 5)
        self.assertEqual(r, [1, 2, 3, 0, 0])


if __name__ == '__main__':
    unittest.main()
