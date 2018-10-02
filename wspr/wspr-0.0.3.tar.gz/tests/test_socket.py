#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `wspr` package."""


import unittest

from wspr.containers.address import Address


class SocketCase(unittest.TestCase):
    """Tests for the address used by whisper."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_creation(self):
        """Test a new address."""
        socket = Address("192.168.0.92", 64738)
        self.assertEqual(socket.port, 64738)
        self.assertEqual(socket.host, "192.168.0.92")
