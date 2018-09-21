# -*- coding=utf-8 -*-
from .. import subsitesMessageFactory as _
from datetime import datetime
from plone import api
from plone.directives.form import SchemaForm
from rer.subsites.interfaces import IRERSubsiteEnabled
from z3c.form import button
from z3c.form import field
from z3c.form.interfaces import WidgetActionExecutionError
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Invalid

import re


@implementer(IRERSubsiteEnabled)
@adapter(IRERSubsiteEnabled)
class SubsiteStylesFormAdapter(object):
    """
    """

    def __init__(self, context):
        """ To basic stuff
        """
        self.context = context
        self.subsite_color = getattr(context, 'subsite_color', '')
        self.image = getattr(context, 'image', '')
        self.subsite_class = getattr(context, 'subsite_class', '')


class SubsiteStylesForm(SchemaForm):

    """ Dinamically built form
    """
    schema = IRERSubsiteEnabled
    ignoreContext = False

    fields = field.Fields(IRERSubsiteEnabled)
    # ignoreContext = True

    def show_message(self, msg, msg_type):
        """ Facade for the show message api function
        """
        show_message = api.portal.show_message
        return show_message(msg, request=self.request, type=msg_type)

    def redirect(self, target=None, msg='', msg_type='error'):
        """ Redirects the user to the target, optionally with a portal message
        """
        if target is None:
            target = self.context.absolute_url()
        if msg:
            self.show_message(msg, msg_type)
        return self.request.response.redirect(target)

    def store_data(self, data):
        """ Store the data before returning
        """
        self.context.subsite_color = data.get('subsite_color')
        self.context.image = data.get('image')
        self.context.subsite_class = data.get('subsite_class')
        # update last modified date
        self.context.styles_last_modified = datetime.now().strftime('%Y%m%d%H%M%S')  # noqa

    def additional_validation(self, data):
        if not data.get('subsite_color', ''):
            return
        m = re.search('^#?\w+;?$', data.get('subsite_color'))
        if not m:
            raise WidgetActionExecutionError(
                'subsite_color',
                Invalid(
                    _(
                        'error_invalid_css_color',
                        default='Not a valid color'),
                )
            )

    @button.buttonAndHandler(u'Salva', name='save')
    def handleSubmit(self, action):
        data, errors = self.extractData()
        self.additional_validation(data)
        if not errors:
            self.store_data(data)
            return self.redirect()

    @button.buttonAndHandler(u'Annulla', name='cancel')
    def handleCancel(self, action):
        """
        """
        return self.redirect()
