# -*- coding: utf-8 -*-

from eea.facetednavigation.subtypes.interfaces import IPossibleFacetedNavigable
from eea.facetednavigation.subtypes.interfaces import IFacetedNavigable
from zope.interface import Interface


class IMultiLayoutFacetedQuery(Interface):
    pass


class IMultiLayoutFacetedNavigable(IFacetedNavigable):
    """
    Marker interface for multi layout faceted objects
    """


class IMultiLayoutPossibleFacetedNavigable(IPossibleFacetedNavigable):
    """
    Marker interface for all objects that should have the ability to be
    faceted navigable
    """


class IAdaptedWidget(Interface):
    pass
