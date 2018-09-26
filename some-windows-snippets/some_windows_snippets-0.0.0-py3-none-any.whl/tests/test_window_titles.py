# -*- coding: utf-8 -*-

### imports ###################################################################
import unittest

### imports from ##############################################################
from some_windows_snippets.window_titles import window_titles

###############################################################################
class TestWindowTitles(unittest.TestCase):
    def test_00_window_titles(self):
        titles = window_titles()
        self.assertIn('Program Manager', titles)