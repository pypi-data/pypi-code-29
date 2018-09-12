# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewCalculatedBillSumRequestDTO(Model):
    """<span class='property-internal'>Only one of SumMeterIds, SumMeterGroupIds
    is required</span>.

    :param sum_meter_ids: Meters in this list will have their use or cost
     added together during the bill calculation
    :type sum_meter_ids: list[int]
    :param sum_meter_group_ids: Distinct meters from these meter groups will
     have their use or cost added together during the bill calculation
     System auto groups cannot be used
    :type sum_meter_group_ids: list[int]
    """

    _attribute_map = {
        'sum_meter_ids': {'key': 'sumMeterIds', 'type': '[int]'},
        'sum_meter_group_ids': {'key': 'sumMeterGroupIds', 'type': '[int]'},
    }

    def __init__(self, sum_meter_ids=None, sum_meter_group_ids=None):
        super(ChargebackNewCalculatedBillSumRequestDTO, self).__init__()
        self.sum_meter_ids = sum_meter_ids
        self.sum_meter_group_ids = sum_meter_group_ids
