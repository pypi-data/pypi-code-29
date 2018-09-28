# -*- coding: utf-8 -*-
from .. import _
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from plone.dexterity.events import AddCancelledEvent
from plone.dexterity.events import EditCancelledEvent
from plone.dexterity.events import EditFinishedEvent
from plone.dexterity.i18n import MessageFactory as dmf
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form.interfaces import WidgetActionExecutionError
from zope.event import notify
from zope.interface import Invalid


class BaseForm(object):

    def additional_validation(self, data):
        # Some additional validation
        if (not data.get('remoteUrl') and not data.get('ISmartLinkExtension.internal_link')) or \
            bool(data.get('remoteUrl')) and bool(data.get('ISmartLinkExtension.internal_link')):
            raise WidgetActionExecutionError('remoteUrl',
                Invalid(_('error_internallink_externallink_doubled', default="You must select an internal link or enter an external link. You cannot have both."),))


class EditForm(BaseForm, DefaultEditForm):
    """
    """

    def updateWidgets(self):
        super(EditForm, self).updateWidgets()
        self.widgets['remoteUrl'].required = False
        self.fields['remoteUrl'].field.required = False

    @button.buttonAndHandler(dmf(u'Save'), name='save')
    def handleApply(self, action):
        data, errors = self.extractData()
        self.additional_validation(data)
        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(
            dmf(u"Changes saved"), "info")
        self.request.response.redirect(self.nextURL())
        notify(EditFinishedEvent(self.context))

    @button.buttonAndHandler(dmf(u'Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(
            dmf(u"Edit cancelled"), "info")
        self.request.response.redirect(self.nextURL())
        notify(EditCancelledEvent(self.context))


class AddForm(BaseForm, DefaultAddForm):
    """
    """

    def updateWidgets(self):
        super(AddForm, self).updateWidgets()
        self.widgets['remoteUrl'].required = False
        self.fields['remoteUrl'].field.required = False

    @button.buttonAndHandler(dmf('Save'), name='save')
    def handleAdd(self, action):
        data, errors = self.extractData()
        self.additional_validation(data)
        if errors:
            self.status = self.formErrorsMessage
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            IStatusMessage(self.request).addStatusMessage(
                dmf(u"Item created"), "info")

    @button.buttonAndHandler(dmf(u'Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(
            dmf(u"Add New Item operation cancelled"), "info")
        self.request.response.redirect(self.nextURL())
        notify(AddCancelledEvent(self.context))


class AddView(DefaultAddView):
    form = AddForm


class EditView(DefaultEditView):
    form = EditForm
