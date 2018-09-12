# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommonFilterEditDTO(Model):
    """CommonFilterEditDTO.

    :param field_id:  <span class='property-internal'>Required</span>
    :type field_id: int
    :param operator:  <span class='property-internal'>Required</span>
    :type operator: str
    :param value:
    :type value: str
    """

    _validation = {
        'field_id': {'required': True},
        'operator': {'required': True},
    }

    _attribute_map = {
        'field_id': {'key': 'fieldId', 'type': 'int'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, field_id, operator, value=None):
        super(CommonFilterEditDTO, self).__init__()
        self.field_id = field_id
        self.operator = operator
        self.value = value
