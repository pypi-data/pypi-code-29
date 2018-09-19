# encoding: utf-8
import os

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets.common import GlobalSectionsViewlet


class IconifiedNavigationViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile('iconifiednavigation-sections.pt')

    def relative_path(self, url):
        portal_url = api.portal.get_navigation_root(self.context).absolute_url()
        relative_path = url.replace(portal_url, '')
        if not relative_path:
            return ''
        if relative_path.startswith('/'):
            relative_path = relative_path[1:]
        return relative_path

    def get_image(self, url):
        icon_path = self.relative_path(url)
        if not icon_path:
            return None

        obj = api.portal.get_navigation_root(self.context).unrestrictedTraverse(icon_path)
        if obj.navigation_icon:
            img_details = {}
            name, ext = os.path.splitext(obj.navigation_icon.filename)
            img_details["path"] = url + '/@@images/navigation_icon'
            img_details["ext"] = ext
            img_details["data"] = obj.navigation_icon.data
            return img_details
        return None
