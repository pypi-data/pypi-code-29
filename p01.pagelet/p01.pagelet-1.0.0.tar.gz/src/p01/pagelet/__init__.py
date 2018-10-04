###############################################################################
#
# Copyright (c) 2010 Projekt01 GmbH.
# All Rights Reserved.
#
###############################################################################
"""
$Id:$
"""
__docformat__ = "reStructuredText"

import zope.interface
from zope.traversing.browser import absoluteURL

from z3c.template.template import getPageTemplate
from z3c.template.template import getLayoutTemplate

import z3c.pagelet.browser

from p01.pagelet import interfaces


class LayoutMixin(object):
    """Layout helper mixin class

    The following attributes can get used for render css class and id for html
    and body elements. This allows you to control css rendering or javascript
    includes.

    You can simply implement your own logik for apply the right ids or css
    classes in your pages within this methods. All you have to do is to use
    them in your layout with something like:

        <!DOCTYPE html>
        <html i18n:domain="demo" lang="de"
              tal:attributes="lang request/lang|nothing;
                              id view/cssHTMLId;
                              class view/cssHTMLClass">
        <head>...</head>
        <body tal:attributes="id view/cssBodyId;
                              class view/cssBodyClass">
        ...
        </body>
        </html>

    and apply the classes and ids like:

        cssBodyId = 'body'
        cssBodyClass = 'option1 feature2'
        cssHTMLId = 'layout2'
        cssHTMLClass = 'more another'

    """

    cssBodyId = None
    cssBodyClass = None
    cssHTMLId = None
    cssHTMLClass = None


@zope.interface.implementer(interfaces.IBrowserPagelet)
class BrowserPagelet(LayoutMixin, z3c.pagelet.browser.BrowserPagelet):
    """Pagelet with layout and template lookup and url support.

    Get rid of template and layout multi adapter call in render method from
    original pagelet implementation. Just use our template and layout lookup
    methods

    """

    _contextURL = None
    _pageURL = None
    nextURL = None

    layout = getLayoutTemplate()
    template = getPageTemplate()

    @property
    def contextURL(self):
        """Setup and cache context URL"""
        if self._contextURL is None:
            self._contextURL = absoluteURL(self.context, self.request)
        return self._contextURL

    @property
    def pageURL(self):
        """Setup and cache context URL"""
        if self._pageURL is None:
            self._pageURL = '%s/%s' % (absoluteURL(self.context, self.request),
                self.__name__)
        return self._pageURL

    def render(self):
        if self.nextURL is not None:
            return None
        return self.template()

    def __call__(self):
        self.update()
        if self.nextURL is not None:
            self.request.response.redirect(self.nextURL)
            return u''
        return self.layout()
