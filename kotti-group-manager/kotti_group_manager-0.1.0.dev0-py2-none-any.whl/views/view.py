# -*- coding: utf-8 -*-

"""
Created on 2018-09-19
:author: Oshane Bailey (b4.oshany@gmail.com)
"""
from kotti_toolkit.security import (
    find_group    
)
from pyramid import httpexceptions as httpexc
from pyramid.view import view_config
from pyramid.view import view_defaults


from kotti_group_manager import _
from kotti_group_manager.fanstatic import css_and_js
from kotti_group_manager.views import BaseView
from kotti_group_manager.resources import GroupPage


@view_defaults(permission='view')
class GroupViews(BaseView):
    """ Views for :class:`kotti_group_manager.resources.GroupPage` """
    
    def get_group(self):
        group_name = self.request.matchdict.get('group')
        if not group_name:
            raise httpexc.HTTPNotFound(location=self.context.path)
        group = find_group(group_name)
        if not group:
            raise httpexc.HTTPNotFound(location=self.context.path)
        return group

    @view_config(route_name='find-group',
                 renderer='kotti_group_manager:templates/group.pt')
    def default_view(self):
        group = self.get_group()
        return dict(
            group=group    
        )


@view_defaults(context=GroupPage, permission='view')
class GroupPageViews(BaseView):
    """ Views for :class:`kotti_group_manager.resources.GroupPage` """

    @view_config(name='view', permission='view',
                 renderer='kotti_group_manager:templates/group.page.pt')
    def default_view(self):
        """ Default view for :class:`kotti_group_manager.resources.GroupPage`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {}