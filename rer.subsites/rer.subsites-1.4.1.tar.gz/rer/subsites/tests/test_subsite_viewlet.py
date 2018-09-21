# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rer.subsites.interfaces import IRERSubsiteEnabled
from rer.subsites.testing import RER_SUBSITES_INTEGRATION_TESTING  # noqa
from zope.interface import alsoProvides

import unittest2 as unittest


class TestSubsiteViewlet(unittest.TestCase):
    """Test the viewlets"""

    layer = RER_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.subsite_color = '#123456'
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        self.subsite = api.content.create(
            type='Folder',
            title='Super Subsite',
            container=self.portal)
        self.document = api.content.create(
            type='Document',
            title='Foo',
            container=self.subsite
        )
        alsoProvides(self.subsite, IRERSubsiteEnabled)
        self.subsite.subsite_color = self.subsite_color

        self.unmark_view = self.subsite.restrictedTraverse(
            'unmark_subsite', None)
        self.mark_view = self.subsite.restrictedTraverse(
            'mark_subsite', None)

    def test_show_title_viewlet_in_subsite(self):
        """
        """
        view = self.subsite.restrictedTraverse('view')()
        self.assertTrue('id="subsite-title"' in view)

    def test_show_title_viewlet_in_subsite_children(self):
        """
        """
        view = self.document.restrictedTraverse('view')()
        subsite_title = '<h2>{0}</h2>'.format(self.subsite.Title())
        self.assertTrue('id="subsite-title"' in view)
        self.assertTrue(subsite_title in view)

    def test_show_styles_viewlet_in_subsite(self):
        """
        """
        view = self.subsite.restrictedTraverse('view')()
        self.assertTrue(self.subsite_color in view)

    def test_show_styles_viewlet_in_subsite_children(self):
        """
        """
        view = self.document.restrictedTraverse('view')()
        self.assertTrue(self.subsite_color in view)

    def test_not_show_viewlets_in_disabled_subsite(self):
        """
        """
        self.unmark_view()
        view = self.subsite.restrictedTraverse('view')()
        self.assertFalse(self.subsite_color in view)
        self.assertFalse('id="subsite-title"' in view)
        self.mark_view()

    def test_not_show_viewlets_in_disabled_subsite_children(self):
        """
        """
        self.unmark_view()
        view = self.document.restrictedTraverse('view')()
        subsite_title = '<h2>{0}</h2>'.format(self.subsite.Title())
        self.assertFalse(self.subsite_color in view)
        self.assertFalse('id="subsite-title"' in view)
        self.assertFalse(subsite_title in view)
        self.mark_view()
