# -*- coding: utf-8 -*- äöü vim: sw=4 sts=4 ts=8 scrolloff=3 cul si et
from Products.Five import BrowserView as BaseBrowserView
from zope.interface import implements, Interface
from Products.CMFCore.utils import getToolByName

from .mixin import GetContextMixin

class BrowserView(BaseBrowserView):

    def __call__(self):
        """ """
        context = self.context
        pt = getToolByName(context, 'portal_types')
        fti = pt.getTypeInfo(context.portal_type)
        value = fti.defaultView(context)
        return getattr(context, value)()

BrowserView.getContext = GetContextMixin.getContext
