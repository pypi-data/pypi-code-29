# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewCalculatedBillGenericBodylineResponseDTO(Model):
    """Representation of a generic "empty" bodyline which is not associated with a
    specific bill or template.

    :param observation_type: The observation type
    :type observation_type:
     ~energycap.sdk.models.LogicalDeviceObservationTypeChildDTO
    :param caption: The caption
    :type caption: str
    :param calculation_type: The calculation type for the line item.  Either
     "Fixed", "Percentage", or "Subtotal"
    :type calculation_type: str
    :param value: The bodyline's value
    :type value: float
    """

    _attribute_map = {
        'observation_type': {'key': 'observationType', 'type': 'LogicalDeviceObservationTypeChildDTO'},
        'caption': {'key': 'caption', 'type': 'str'},
        'calculation_type': {'key': 'calculationType', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, observation_type=None, caption=None, calculation_type=None, value=None):
        super(ChargebackNewCalculatedBillGenericBodylineResponseDTO, self).__init__()
        self.observation_type = observation_type
        self.caption = caption
        self.calculation_type = calculation_type
        self.value = value
