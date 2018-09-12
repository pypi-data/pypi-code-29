# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewCalculatedBillSubtractRequestDTO(Model):
    """<span class='property-internal'>Only one of SubtractMeterIds,
    SubtractMeterGroupIds is required</span>.

    :param subtract_meter_ids: Meters in this list will have their use or cost
     subtracted during bill calculation
    :type subtract_meter_ids: list[int]
    :param subtract_meter_group_ids: Distinct meters from these meter groups
     will have their use or cost subtracted together during the bill
     calculation
     System auto groups cannot be used
    :type subtract_meter_group_ids: list[int]
    """

    _attribute_map = {
        'subtract_meter_ids': {'key': 'subtractMeterIds', 'type': '[int]'},
        'subtract_meter_group_ids': {'key': 'subtractMeterGroupIds', 'type': '[int]'},
    }

    def __init__(self, subtract_meter_ids=None, subtract_meter_group_ids=None):
        super(ChargebackNewCalculatedBillSubtractRequestDTO, self).__init__()
        self.subtract_meter_ids = subtract_meter_ids
        self.subtract_meter_group_ids = subtract_meter_group_ids
