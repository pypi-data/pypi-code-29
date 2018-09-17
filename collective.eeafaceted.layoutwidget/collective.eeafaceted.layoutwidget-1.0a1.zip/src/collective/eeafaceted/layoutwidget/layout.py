# -*- coding: utf-8 -*-

from eea.facetednavigation.widgets.interfaces import ISchema
from eea.facetednavigation.widgets import ViewPageTemplateFile
from eea.facetednavigation.widgets.widget import Widget as AbstractWidget
from eea.facetednavigation.widgets.interfaces import DefaultSchemata as DS
from eea.facetednavigation.widgets.interfaces import LayoutSchemata
from z3c.form import field
from zope import schema
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility

import logging

from collective.eeafaceted.layoutwidget import _


logger = logging.getLogger('eea.facetednavigation.widgets.portlet')


class ILayoutSchema(ISchema):

    values = schema.List(
        title=_(u'values'),
        required=False,
        value_type=schema.Choice(
            title=u'values',
            vocabulary='collective.eeafaceted.layoutwidget.Layouts',
        ),
    )


class DefaultSchemata(DS):

    fields = field.Fields(ILayoutSchema).select(
        u'title',
        u'values',
        u'default',
    )


class Widget(AbstractWidget):
    """ Widget
    """
    # Widget properties
    widget_type = 'layout'
    widget_label = _('Layout selection')

    groups = (
        DefaultSchemata,
        LayoutSchemata,
    )

    index = ViewPageTemplateFile('layout.pt')

    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        self.data.widget_context = self.context

    def vocabulary(self, **kwargs):
        voc_factory = getUtility(
            IVocabularyFactory,
            name='collective.eeafaceted.layoutwidget.Layouts',
        )
        return [(t.value, t.title) for t in voc_factory(self.context)
                if t.value in self.data.values]
