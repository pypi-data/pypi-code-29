# -*- coding: utf-8 -*-

from zope.interface import alsoProvides
from zope.interface import noLongerProvides

from collective.eeafaceted.layoutwidget.interfaces import IMultiLayoutFacetedNavigable
from collective.eeafaceted.layoutwidget.interfaces import IMultiLayoutPossibleFacetedNavigable


def faceted_enabled(obj, event):
    if not IMultiLayoutPossibleFacetedNavigable.providedBy(obj):
        alsoProvides(obj, IMultiLayoutPossibleFacetedNavigable)
    if not IMultiLayoutFacetedNavigable.providedBy(obj):
        alsoProvides(obj, IMultiLayoutFacetedNavigable)


def faceted_disabled(obj, event):
    if IMultiLayoutFacetedNavigable.providedBy(obj):
        noLongerProvides(obj, IMultiLayoutFacetedNavigable)
