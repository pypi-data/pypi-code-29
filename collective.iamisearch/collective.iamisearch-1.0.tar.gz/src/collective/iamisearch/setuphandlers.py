# -*- coding: utf-8 -*-
import os

from Products.CMFCore.utils import getToolByName
from collective.iamisearch import _
from plone.dexterity.interfaces import IDexterityFTI

from Products.CMFPlone.interfaces import INonInstallable
from collective.taxonomy.factory import registerTaxonomy
from collective.taxonomy.interfaces import ITaxonomy
from plone import api
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation
from plone.app.multilingual import api as api_lng
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility, queryUtility
from zope.i18n.interfaces import ITranslationDomain
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.i18n import translate


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.iamisearch:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # creation of taxonomies

    language_tool = api.portal.get_tool('portal_languages')
    langs = language_tool.supported_langs
    current_lang = api.portal.get_current_language()[:2]

    taxonomies_collection = ['I am', 'I search']
    data_iam = {
        'taxonomy': 'iam',
        'field_title': translate(_('I am'), target_language=current_lang),
        'field_description': '',
        'default_language': 'fr',
    }

    data_isearch = {
        'taxonomy': 'isearch',
        'field_title': translate(_('I search'), target_language=current_lang),
        'field_description': '',
        'default_language': 'fr',
    }

    faced_config = {
        'I am': '/faceted/config/iam_folder.xml',
        'I search': '/faceted/config/isearch_folder.xml',
    }

    # install taxonomy
    portal = api.portal.get()
    sm = portal.getSiteManager()
    iam_item = 'collective.taxonomy.iam'
    isearch_item = 'collective.taxonomy.isearch'
    utility_iam = sm.queryUtility(ITaxonomy, name=iam_item)
    utility_isearch = sm.queryUtility(ITaxonomy, name=isearch_item)

    # stop installation if already
    if utility_iam and utility_isearch:
        enable_taxonomies_content_type()
        return

    create_taxonomy_object(data_iam)
    create_taxonomy_object(data_isearch)

     # remove taxonomy test
    item = 'collective.taxonomy.test'
    utility = sm.queryUtility(ITaxonomy, name=item)
    if utility:
        utility.unregisterBehavior()
        sm.unregisterUtility(utility, ITaxonomy, name=item)
        sm.unregisterUtility(utility, IVocabularyFactory, name=item)
        sm.unregisterUtility(utility, ITranslationDomain, name=item)


    enable_taxonomies_content_type()
    # creation of two collections by language

    container = api.portal.get().get(current_lang)
    if container is None:
        container = api.portal.get()
    for taxonomy_collection in taxonomies_collection:
        title = taxonomy_collection
        translate_title = translate(_(title), target_language=current_lang)
        normalizer = getUtility(IIDNormalizer)
        new_id = normalizer.normalize(translate_title)
        if normalizer.normalize(title) not in container:
            new_obj = api.content.create(
                type='Folder',
                title=translate_title,
                container=container)
            if new_obj.id != new_id:
                api.content.rename(new_obj, new_id=new_id)
            try:
                nav = IExcludeFromNavigation(new_obj)
            except:
                pass
            if nav:
                nav.exclude_from_nav = True
            new_obj.reindexObject()
            _activate_dashboard_navigation(new_obj, faced_config[taxonomy_collection])
            for lang in langs:
                if lang != current_lang:
                    translated_obj = translation_folderish(new_obj, lang, title)
                    _activate_dashboard_navigation(translated_obj, faced_config[taxonomy_collection])

def create_taxonomy_object(data):
    taxonomy = registerTaxonomy(
        api.portal.get(),
        name=data['taxonomy'],
        title=data['field_title'],
        description=data['field_description'],
        default_language=data['default_language']
    )

    del data['taxonomy']
    taxonomy.registerBehavior(**data)


def translation_folderish(obj, lang, title):
    translated_obj = api_lng.translate(obj, lang)
    translate_title = translate(_(title), target_language=lang)
    normalizer = getUtility(IIDNormalizer)
    new_id = normalizer.normalize(translate_title)
    translated_obj.title = translate_title
    if translated_obj.id != new_id:
        api.content.rename(translated_obj, new_id=new_id)
    try:
        nav = IExcludeFromNavigation(translated_obj)
    except:
        pass
    if nav:
        nav.exclude_from_nav = True
    translated_obj.reindexObject()
    return translated_obj


def _activate_dashboard_navigation(context, config_path=''):
    subtyper = context.restrictedTraverse('@@faceted_subtyper')
    if subtyper.is_faceted:
        return
    subtyper.enable()
    context.unrestrictedTraverse('@@faceted_exportimport').import_xml(
        import_file=open(os.path.dirname(__file__) + config_path)
    )

def enable_taxonomies_content_type():
    portal_types = getToolByName(api.portal.get(), "portal_types")
    types = portal_types.listContentTypes()
    for type in types:
        add_behavior(type, 'collective.taxonomy.generated.iam')
        add_behavior(type, 'collective.taxonomy.generated.isearch')


def add_behavior(type_name, behavior_name):
    """Add a behavior to a type"""
    fti = queryUtility(IDexterityFTI, name=type_name)
    if not fti:
        return
    behaviors = list(fti.behaviors)
    if behavior_name not in behaviors:
        behaviors.append(behavior_name)
        fti._updateProperty('behaviors', tuple(behaviors))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
