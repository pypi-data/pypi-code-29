# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from rer.subsites.interfaces import IRERSubsiteEnabled


class View(BrowserView):
    """If the object is in a subsite, the css is loaded
    """
    def __call__(self):
        for elem in self.context.aq_chain:
            if IRERSubsiteEnabled.providedBy(elem):
                return True
        return False
