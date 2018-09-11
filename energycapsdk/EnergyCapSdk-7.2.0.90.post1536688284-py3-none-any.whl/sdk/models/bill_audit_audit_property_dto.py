# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillAuditAuditPropertyDTO(Model):
    """BillAuditAuditPropertyDTO.

    :param property_id:
    :type property_id: int
    :param property_code:
    :type property_code: str
    :param description:
    :type description: str
    :param data_type:
    :type data_type: ~energycap.sdk.models.UnitDataTypeResponseDTO
    :param operator:
    :type operator: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'property_id': {'key': 'propertyId', 'type': 'int'},
        'property_code': {'key': 'propertyCode', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'UnitDataTypeResponseDTO'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, property_id=None, property_code=None, description=None, data_type=None, operator=None, value=None):
        super(BillAuditAuditPropertyDTO, self).__init__()
        self.property_id = property_id
        self.property_code = property_code
        self.description = description
        self.data_type = data_type
        self.operator = operator
        self.value = value
