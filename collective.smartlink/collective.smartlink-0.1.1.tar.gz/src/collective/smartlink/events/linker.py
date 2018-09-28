# -*- coding: utf-8 -*-

from zope import interface
from Products.CMFCore.utils import getToolByName
from plone import api


def set_remote_url(object, event):
    """
    Set remote url for the link
    """
    #import pdb; pdb.set_trace()
    internal_link = getattr(object, 'internal_link', '')
    if internal_link:
        portal = api.portal.get()
        internal_link = '%s/%s' % (portal.absolute_url_path(), internal_link)
        #internal_link = '${navigation_root_url}/%s' % internal_link
        setattr(object, 'remoteUrl', internal_link)
