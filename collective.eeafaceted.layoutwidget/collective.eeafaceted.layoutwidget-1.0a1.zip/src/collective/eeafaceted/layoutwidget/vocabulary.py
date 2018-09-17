# -*- coding: utf-8 -*-

from eea.facetednavigation.interfaces import IViewsInfo
from zope.i18n import translate
from zope.schema.vocabulary import SimpleVocabulary
from zope.globalrequest import getRequest
from zope.component import getUtility

from collective.eeafaceted.layoutwidget import _


class FacetedLayoutVocabulary(object):

    def __call__(self, context):
        utility = getUtility(IViewsInfo)
        request = getattr(context, 'REQUEST', getRequest())
        terms = [
            SimpleVocabulary.createTerm(
                key,
                key,
                translate(_(name), context=request),
            ) for key, name in utility.views.items()]
        return SimpleVocabulary(terms)
