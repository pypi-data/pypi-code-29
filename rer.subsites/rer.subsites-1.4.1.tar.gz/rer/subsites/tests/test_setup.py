# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.browserlayer import utils
from rer.subsites.interfaces import IRERSubsiteLayer  # noqa
from rer.subsites.testing import RER_SUBSITES_INTEGRATION_TESTING  # noqa

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that rer.subsites is properly installed."""

    layer = RER_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """
        Test if rer.subsites is installed
        with portal_quickinstaller.
        """
        self.assertTrue(
            self.installer.isProductInstalled('rer.subsites'))

    def test_browserlayer(self):
        """Test that IRERSubsiteLayer is registered."""
        self.assertIn(
            IRERSubsiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RER_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rer.subsites'])

    def test_product_uninstalled(self):
        """Test if rer.subsites is cleanly uninstalled."""
        self.assertFalse(
            self.installer.isProductInstalled('rer.subsites'))

    def test_browserlayer_removed(self):
        """Test that IRERSubsiteLayer is removed."""
        self.assertNotIn(
            IRERSubsiteLayer, utils.registered_layers())
