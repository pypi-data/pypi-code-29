# -*- coding: utf-8 -*- äöü vim: sw=4 sts=4 ts=8 scrolloff=3 cul si et
from Products.CMFCore.utils import getToolByName

class GetContextMixin(object):
    """
    Mixin-Klasse für getContext-Methode
    """

    def getContext(self):
        """
        TODO: Warum wird das benötigt?
        """
        context = self.context
        if hasattr(context, 'UID'):
            rc = getToolByName(context, 'reference_catalog')
            return rc.lookupObject(context.UID())
        else:
            return context
