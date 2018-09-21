# -*- coding: utf-8 -*-
from plone import api
from plone.app.contenttypes.interfaces import IFolder
from Products.Five.browser import BrowserView
from rer.subsites.interfaces import IRERSubsiteEnabled
from rer.subsites.interfaces import IRERSubsiteUtilsView
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import noLongerProvides


class BaseSubsiteView(BrowserView):
    def get_canonical(self):
        context = self.context.aq_inner
        pcs = context.restrictedTraverse('@@plone_context_state')
        return pcs.canonical_object()


class CheckSubsiteAction(BaseSubsiteView):

    def check_subsite_action_add(self):
        obj = self.get_canonical()
        if not IFolder.providedBy(obj):
            return False
        return not IRERSubsiteEnabled.providedBy(obj)

    def check_subsite_action_remove(self):
        obj = self.get_canonical()
        if not IFolder.providedBy(obj):
            return False
        return IRERSubsiteEnabled.providedBy(obj)


class ToggleMarkSubsite(BaseSubsiteView):

    def add_interface(self):
        obj = self.get_canonical()
        if not IFolder.providedBy(obj):
            api.portal.show_message(
                message=u'Impossibile marcare il contenuto come subsite.',
                type='error',
                request=self.request
            )
            return self.request.response.redirect(obj.absolute_url())
        if not IRERSubsiteEnabled.providedBy(obj):
            alsoProvides(obj, IRERSubsiteEnabled)
            obj.reindexObject(idxs=['object_provides'])
            api.portal.show_message(
                message='Cartella marcata come subsite.',
                type='info',
                request=self.request)
        else:
            api.portal.show_message(
                message=u'Cartella già marcata come subsite.',
                type='warning',
                request=self.request)
        self.request.response.redirect(obj.absolute_url())

    def remove_interface(self):
        obj = self.get_canonical()
        if IRERSubsiteEnabled.providedBy(obj):
            noLongerProvides(obj, IRERSubsiteEnabled)
            obj.subsite_class = ''
            obj.reindexObject(idxs=['object_provides'])
            api.portal.show_message(
                message=u'Cartella non più subsite.',
                type='info',
                request=self.request)
        else:
            api.portal.show_message(
                message=u'La cartella non era già un subsite.',
                request=self.request,
                type='warning')

        self.request.response.redirect(obj.absolute_url())


@implementer(IRERSubsiteUtilsView)
class SubsiteUtilsView(BaseSubsiteView):

    def get_subsite_folder(self):
        """
        Return the parent folder marked as "Subsite", for retrieve some infos
        like a color and the image pin
        """
        context = self.get_canonical()
        for elem in context.aq_inner.aq_chain:
            if IRERSubsiteEnabled.providedBy(elem):
                return elem
        return None

    def get_subsite_attributes(self):
        """
        Retrieve the subsite folder, and get saved css class
        """
        subsite = self.get_subsite_folder()
        if not subsite:
            return {}
        subsite_class = getattr(subsite, "subsite_class", '')
        return {
            'title': subsite.Title(),
            'subsite_class': subsite_class,
            'url': subsite.absolute_url(),
        }
