# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.iamisearch.testing import COLLECTIVE_IAMISEARCH_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.iamisearch is properly installed."""

    layer = COLLECTIVE_IAMISEARCH_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.iamisearch is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.iamisearch'))

    def test_browserlayer(self):
        """Test that ICollectiveIamisearchLayer is registered."""
        from collective.iamisearch.interfaces import (
            ICollectiveIamisearchLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveIamisearchLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_IAMISEARCH_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get(userid=TEST_USER_ID).getRoles()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.iamisearch'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.iamisearch is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.iamisearch'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveIamisearchLayer is removed."""
        from collective.iamisearch.interfaces import \
            ICollectiveIamisearchLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveIamisearchLayer,
           utils.registered_layers())
