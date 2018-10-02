#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `wspr` package."""


import unittest

from wspr.containers.credentials import Credentials


class CredentialsCase(unittest.TestCase):
    """Tests for the credentials used in whisper."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_creation(self):
        """Test new credentials."""
        cred = Credentials("Whisp", "ogurek")
        self.assertEqual(cred.name, "Whisp")
        self.assertEqual(cred.password, "ogurek")


