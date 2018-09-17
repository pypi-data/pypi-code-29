# -*- coding: utf-8 -*-

from eea.facetednavigation.browser.app.query import FacetedQueryHandler
from zope.component import queryUtility

from collective.eeafaceted.layoutwidget.faceted import FacetedMultipleLayout
from collective.eeafaceted.layoutwidget.interfaces import IMultiLayoutFacetedQuery


class QueryHandler(FacetedQueryHandler):

    @property
    def layout(self):
        return FacetedMultipleLayout(self.context).layout

    def criteria(self, *args, **kwargs):
        query = super(QueryHandler, self).criteria(*args, **kwargs)
        utility = queryUtility(IMultiLayoutFacetedQuery, name=self.layout)
        if utility is not None and hasattr(utility, 'apply_filters'):
            query = utility.apply_filters(query)
        return query

    def query(self, *args, **kwargs):
        utility = queryUtility(IMultiLayoutFacetedQuery, name=self.layout)
        if utility is not None and hasattr(utility, 'custom_query_filters'):
            args, kwargs = utility.custom_query_filters(*args, **kwargs)
        return super(QueryHandler, self).query(*args, **kwargs)
