###############################################################################
#
# Copyright (c) 2018 Projekt01 GmbH.
# All Rights Reserved.
#
###############################################################################
"""Pagelet traverser

"""
__docformat__ = "reStructuredText"

import zope.interface

import zope.traversing.interfaces


@zope.interface.implementer(zope.traversing.interfaces.ITraversable)
class J01PagerTraverser(object):
    """Traverses J01PagerCore based view"""

    def __init__(self, subject):
        self._subject = subject

    def traverse(self, name, furtherPath):
        """Lookup attribute on views and raise errors on error.

        Don't raise LocationError because LocationError will hide any real
        error and it makes it almost impossible to see what happens.
        """
        return getattr(self._subject, name)
