# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountMeterFormTemplateRequestDTO(Model):
    """AccountMeterFormTemplateRequestDTO.

    :param template_id: The identifier for the template being assigned <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Required</span>
    :type template_id: int
    :param begin_date: The begin date of the template assignment <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Required</span>
    :type begin_date: datetime
    """

    _validation = {
        'template_id': {'required': True},
        'begin_date': {'required': True},
    }

    _attribute_map = {
        'template_id': {'key': 'templateId', 'type': 'int'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
    }

    def __init__(self, template_id, begin_date):
        super(AccountMeterFormTemplateRequestDTO, self).__init__()
        self.template_id = template_id
        self.begin_date = begin_date
