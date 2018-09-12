# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UDFUDFSelectValueEntityResponseDTO(Model):
    """UDFUDFSelectValueEntityResponseDTO.

    :param udf_select_value_id:
    :type udf_select_value_id: int
    :param value:
    :type value: str
    :param display_order:
    :type display_order: int
    """

    _attribute_map = {
        'udf_select_value_id': {'key': 'udfSelectValueId', 'type': 'int'},
        'value': {'key': 'value', 'type': 'str'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
    }

    def __init__(self, udf_select_value_id=None, value=None, display_order=None):
        super(UDFUDFSelectValueEntityResponseDTO, self).__init__()
        self.udf_select_value_id = udf_select_value_id
        self.value = value
        self.display_order = display_order
