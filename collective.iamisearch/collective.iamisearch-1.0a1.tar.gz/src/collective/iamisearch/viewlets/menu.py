# -*- coding: utf-8 -*-

import operator

from collective.iamisearch import _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.taxonomy import PATH_SEPARATOR
from collective.taxonomy.interfaces import ITaxonomy
from plone import api
from plone.app.layout.viewlets import common
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility
from zope.i18n import translate


class MenuViewlet(common.ViewletBase):
    index = ViewPageTemplateFile('menu.pt')

    def generate_menu_value_by_taxonomy_level(self, taxonomy_name, target_level=1, all_path=False, is_fill=True):
        """
        :param target_level:
        :return:
        """
        utility = self.get_taxonomy('collective.taxonomy.' + taxonomy_name)
        if not utility.data:
            return None
        target_language = str(utility.getCurrentLanguage(self.request))
        taxonomy_keys = utility.inverted_data[target_language]
        targets_by_level = {}
        taxonomy_filled = []
        index_filter = "taxonomy_{0}".format(taxonomy_name)
        if is_fill:
            portal_catalog = api.portal.get_tool('portal_catalog')
            taxonomy_filled = portal_catalog.uniqueValuesFor(index_filter)

        for key, value in taxonomy_keys.iteritems():
            item = taxonomy_keys[key]
            targets = item[1:].split(PATH_SEPARATOR)
            if all_path:
                if len(targets) == target_level:
                    if is_fill and key in taxonomy_filled:
                        targets_by_level[key] = targets
                    elif not is_fill:
                        targets_by_level[key] = targets

            else:
                if len(targets) == target_level:
                    if is_fill and key in taxonomy_filled:
                        targets_by_level[key] = targets[-1]
                    elif not is_fill:
                        targets_by_level[key] = targets[-1]

        return targets_by_level

    def get_language(self):
        return api.portal.get_current_language()[:2]

    def taxonomies_links(self, taxonomy_name, taxonomy_title):
        targets_by_level = self.generate_menu_value_by_taxonomy_level(taxonomy_name)
        if not targets_by_level:
            return None
        sorted_targets_by_level = sorted(targets_by_level.items(), key=operator.itemgetter(1))

        current_lang = api.portal.get_current_language()[:2]
        translate_title = translate(_(taxonomy_title), target_language=current_lang)
        normalizer = getUtility(IIDNormalizer)
        folder = normalizer.normalize(translate_title)
        result = {}
        language_tool = api.portal.get_tool('portal_languages')
        langs = language_tool.supported_langs
        for target in sorted_targets_by_level:
            if len(langs) > 1:
                url = "{0}/{1}/{2}#c0={3}".format(api.portal.get().absolute_url(), self.get_language(), folder, target[0])
            else:
                url = "{0}/{1}#c0={2}".format(api.portal.get().absolute_url(), folder, target[0])
            result[target[1]] = url
        return result

    def get_taxonomy(self, name):
        portal = api.portal.get()
        sm = portal.getSiteManager()
        sm.queryUtility(ITaxonomy)
        return sm.queryUtility(ITaxonomy, name=name)
