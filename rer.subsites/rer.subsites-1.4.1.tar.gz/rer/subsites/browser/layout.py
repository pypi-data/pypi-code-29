# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.globals.layout import LayoutPolicy as BaseView


class LayoutPolicy(BaseView):
    """A view that gives access to various layout related functions.
    """

    def bodyClass(self, template, view):
        """
        Returns the CSS class to be used on the body tag.

        Included body classes
        - template name: template-{}
        - portal type: portaltype-{}
        - navigation root: site-{}
        - section: section-{}
            - only the first section
        - section structure
            - a class for every container in the tree
        - hide icons: icons-on
        - markspeciallinks: pat-markspeciallinks
        - userrole-{} for each role the user has in this context
        - min-view-role: role required to view context
        - default-view: if view is the default view
        """
        body_classes = super(LayoutPolicy, self).bodyClass(template, view)
        view = api.content.get_view(
            name='subsite_utils_view',
            context=self.context,
            request=self.request,
        )
        subsite = view.get_subsite_folder()

        if not subsite:
            return body_classes

        canonical = api.content.get_view(
            name='plone_context_state',
            context=self.context,
            request=self.request,
        ).canonical_object()

        if canonical == subsite:
            body_classes += ' subsite-root'
        else:
            body_classes += ' subsite-child'

        if getattr(self.context, 'subsite_class', ''):
            subsite_class_name = ' subsite-{}'.format(
                getattr(self.context, 'subsite_class'),
            )
            body_classes += subsite_class_name

        return body_classes
