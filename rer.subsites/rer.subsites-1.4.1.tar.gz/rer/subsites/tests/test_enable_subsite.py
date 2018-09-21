# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rer.subsites.interfaces import IRERSubsiteEnabled
from rer.subsites.testing import RER_SUBSITES_INTEGRATION_TESTING  # noqa
from zope.interface import alsoProvides

import unittest2 as unittest


class TestStylesForm(unittest.TestCase):
    """Test view for subsite styles"""

    layer = RER_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        self.folder = api.content.create(
            type='Folder',
            title='Test folder',
            container=self.portal)

    def test_no_subsite_cant_access_subsite_styles_form(self):
        """
        """
        view = self.folder.restrictedTraverse('subsite_styles_form', None)
        self.assertIsNone(view)

    def test_subsite_can_access_subsite_styles_form(self):
        """
        """
        alsoProvides(self.folder, IRERSubsiteEnabled)
        view = self.folder.restrictedTraverse('subsite_styles_form', None)
        self.assertIsNotNone(view)


class TestMarkSubsite(unittest.TestCase):
    """Test views that marks a subsite"""

    layer = RER_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        self.folder = api.content.create(
            type='Folder',
            title='Test folder',
            container=self.portal)

    def test_mark_folder_as_subsite(self):
        """
        """
        self.assertFalse(IRERSubsiteEnabled.providedBy(self.folder))
        view = self.folder.restrictedTraverse('mark_subsite', None)
        view()
        self.assertTrue(IRERSubsiteEnabled.providedBy(self.folder))

    def test_unmark_subsite(self):
        """
        """
        mark_view = self.folder.restrictedTraverse('mark_subsite', None)
        unmark_view = self.folder.restrictedTraverse('unmark_subsite', None)
        mark_view()
        self.assertTrue(IRERSubsiteEnabled.providedBy(self.folder))
        unmark_view()
        self.assertFalse(IRERSubsiteEnabled.providedBy(self.folder))
