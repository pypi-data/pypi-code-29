##############################################################################
#
# Copyright (c) 2012 Projekt01 GmbH and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
$Id: interfaces.py 4923 2018-10-04 06:52:29Z roger.ineichen $
"""
__docformat__ = "reStructuredText"

from zope.interface.common import sequence
import zope.schema

import z3c.pagelet.interfaces


class IJ01Pager(z3c.pagelet.interfaces.IPagelet):
    """Pager core using j01Pager with special travers

    The J01Pager core class uses a special traverser whcih does not hide
    errors in views.
    """


class IBatch(sequence.IFiniteSequence):
    """A Batch represents a sub-list of the full sequence.

    The Batch constructor takes a list (or any list-like object) of elements,
    a starting index and the size of the batch. From this information all
    other values are calculated.
    """

    sequence = zope.interface.Attribute('Sequence')

    start = zope.schema.Int(
        title=u'Start Index',
        description=(u'The index of the sequence at which the batch starts. '
                     u'If the full sequence is empty, the value is -1.'),
        min=-1,
        default=0,
        required=True)

    end = zope.schema.Int(
        title=u'End Index',
        description=u'The index of the sequence at which the batch ends.',
        min=-1,
        default=0,
        readonly=True,
        required=True)

    size = zope.schema.Int(
        title=u'Batch Size',
        description=u'The maximum size of the batch.',
        min=0,
        default=20,
        required=True)

    total = zope.schema.Int(
        title=u'Total number of items',
        description=u'The total number of sequence items',
        min=1,
        readonly=True,
        required=True)

    sortName = zope.schema.Field(
        title=u'Sort name argument',
        description=u'Python sort attrgetter name, itemgetter int or function',
        default=None,
        required=False)

    sortOrder = zope.schema.Bool(
        title=u'Reverse sort order',
        description=u'True for reverse or False for non reverse order',
        default=False,
        required=False)

    def skip(start):
        """Skip amount of items"""

    def limit(size):
        """Limit result"""

    def sort(sortName, sortOrder):
        """Sort sequence"""

    def __iter__():
        """Creates an iterator for the contents of the batch."""

    def __contains__(item):
        """ `x.__contains__(item)` <==> `item in x` """

    def __eq__(other):
        """`x.__eq__(other)` <==> `x == other`"""

    def __ne__(other):
        """`x.__ne__(other)` <==> `x != other`"""
