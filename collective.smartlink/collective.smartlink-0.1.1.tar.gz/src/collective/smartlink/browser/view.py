# -*- coding: utf-8 -*-
from plone.app.contenttypes.browser.link_redirect_view import LinkRedirectView as Base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone import api
from .. import _


class LinkRedirectView(Base):
    index = ViewPageTemplateFile('templates/link.pt')

    def _url_uses_scheme(self, schemes, url=None):
        url = url or self.context.remoteUrl
        if not url:
            return False
        for scheme in schemes:
            if url.startswith(scheme):
                return True
        return False

    def absolute_target_url(self):
        """Compute the absolute target URL."""
        context = self.context
        mtool = getToolByName(context, 'portal_membership')
        can_edit = mtool.checkPermission('Modify portal content', context)

        if self.context.internal_link:
            if not self.context.internal_link.to_object:
                if not can_edit:
		    api.portal.show_message(
				    message=_("link_not_found"),
				    request=self.request,
				    type='warning')
                    return self.request.response.redirect(api.portal.get().absolute_url())
                else:
                    return
            return self.context.internal_link.to_object.absolute_url()
        else:
            return super(LinkRedirectView, self).absolute_target_url()
