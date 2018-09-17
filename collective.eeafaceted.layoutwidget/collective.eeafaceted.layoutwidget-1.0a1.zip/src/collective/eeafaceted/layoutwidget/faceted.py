# -*- coding: utf-8 -*-

from eea.facetednavigation.criteria.handler import Criteria
from eea.facetednavigation.interfaces import ICriteria
from eea.facetednavigation.layout.layout import FacetedLayout
from zope.component import queryAdapter
from zope.component import queryUtility
from zope.globalrequest import getRequest
from zope.interface import implementer

from collective.eeafaceted.layoutwidget.interfaces import IAdaptedWidget


class FacetedMultipleLayout(FacetedLayout):

    def __init__(self, *args, **kwargs):
        super(FacetedMultipleLayout, self).__init__(*args, **kwargs)
        self.request = getattr(self.context, 'REQUEST', getRequest())

    @property
    def layout(self):
        cid, criterion = self.get_criterion()
        default = criterion and criterion.default or None
        layout = self.request.form.get('%s[]' % cid, default)
        if not layout:
            return super(FacetedMultipleLayout, self).layout
        return layout

    def get_criterion(self):
        criteria = queryAdapter(self.context, ICriteria)
        criterion = [(cid, c) for cid, c in criteria.items()
                     if c.widget == 'layout']
        return len(criterion) > 0 and criterion[0] or (None, None)


@implementer(ICriteria)
class CriteriaHandler(Criteria):

    def widget(self, *args, **kwargs):
        widget = super(CriteriaHandler, self).widget(*args, **kwargs)
        return self._adapted_widget(widget)

    def _adapted_widget(self, widget):
        def hidden(self):
            utility = queryUtility(
                IAdaptedWidget,
                name=self.data.widget,
            )
            if utility:
                return utility.hidden(self, self.data)
            return self.data.hidden

        widget.hidden = property(hidden)
        return widget
