# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from rer.subsites.interfaces import IRERSubsiteEnabled
from rer.subsites.interfaces import IRERSubsitesSettings
from zope.component import getMultiAdapter


class SubsiteViewletBase(ViewletBase):

    def __init__(self, context, request, view, manager):
        super(SubsiteViewletBase, self).__init__(
            context,
            request,
            view,
            manager
        )
        self.subsite = self.getSubsiteObj()

    def render(self):
        viewlet_enabled = self.is_viewlet_enabled()
        if not viewlet_enabled:
            return ""
        if self.subsite:
            return self.index()
        else:
            return ''

    def getSubsiteObj(self):
        for elem in self.context.aq_inner.aq_chain:
            if IRERSubsiteEnabled.providedBy(elem):
                return elem
        return None

    def is_viewlet_enabled(self):
        """ """
        return api.portal.get_registry_record(
            'viewlets_enabled',
            interface=IRERSubsitesSettings)


class SubsiteTitleViewlet(SubsiteViewletBase):
    """
    viewlet with title
    """
    index = ViewPageTemplateFile('viewlets/rer_subsite_title.pt')

    def get_css_class(self):
        context = self.context.aq_inner
        context_state = getMultiAdapter(
            (context, self.request),
            name=u'plone_context_state'
        )
        real_obj = context_state.canonical_object()

        if real_obj == self.subsite:
            return ''

        return 'subsite-child'


class SubsiteColorViewlet(SubsiteViewletBase):
    """
    A Viewlet that allows to add some dynamic css in the  header
    """

    def render(self):

        viewlet_enabled = self.is_viewlet_enabled()
        if not viewlet_enabled:
            return ""

        if not self.subsite:
            return ''

        return_string = ''
        styles = self.get_default_styles()
        custom_styles = self.get_custom_styles()
        if custom_styles:
            styles += custom_styles
        return_string = '<style type="text/css">{0}</style>'.format(styles)
        return return_string

    def get_default_styles(self):
        color = getattr(self.subsite, 'subsite_color', '')
        image = getattr(self.subsite, 'image', None)
        if not color and not image:
            return ''
        subsite_url = self.subsite.absolute_url()
        styles = []
        css = '#subsite-title {'
        if color:
            styles.append('background-color:{0}'.format(color))
        if image:
            version = getattr(self.subsite, 'styles_last_modified', '')
            styles.append(
                'background-image:url({0}/@@images/image?v={1})'.format(
                    subsite_url,
                    version
                )
            )
        css += ';'.join(styles)
        css += '}'
        styles = []
        css += '#contentCarousel {'
        if color:
            styles.append('background-color:{0}'.format(color))
        css += ';'.join(styles)
        css += '}'
        return css

    def get_custom_styles(self):
        """
        read styles from control panel
        """
        color = getattr(self.subsite, 'subsite_color', '')
        css = api.portal.get_registry_record(
            'subsite_styles',
            interface=IRERSubsitesSettings)
        if not css:
            return ''
        return css.replace('\r\n', ' ').replace('$color$', color)
