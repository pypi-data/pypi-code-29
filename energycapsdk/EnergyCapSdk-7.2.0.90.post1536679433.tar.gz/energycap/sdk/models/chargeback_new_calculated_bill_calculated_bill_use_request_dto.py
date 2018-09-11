# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewCalculatedBillCalculatedBillUseRequestDTO(Model):
    """Defines how use is calculated for a calculated bill distribution <span
    class='property-internal'>Only one of ReadingsChannelId, FixedAmount,
    CopyUseFromMeter, UseCalculation is required</span>.

    :param readings_channel_id: Use monthly channel data readings to calculate
     bill use
    :type readings_channel_id: int
    :param fixed_amount: Use a fixed amount of a given unit for bill use
    :type fixed_amount:
     ~energycap.sdk.models.ChargebackNewCalculatedBillFixedUseRequestDTO
    :param copy_use_from_meter: Copy aggregated use from another meter
    :type copy_use_from_meter:
     ~energycap.sdk.models.ChargebackNewCalculatedBillCopyMeterRequestDTO
    :param use_calculation: Adding/subtracting calculation involving meters
     and/or meter groups
    :type use_calculation:
     ~energycap.sdk.models.ChargebackNewCalculatedBillCalculationRequestDTO
    """

    _attribute_map = {
        'readings_channel_id': {'key': 'readingsChannelId', 'type': 'int'},
        'fixed_amount': {'key': 'fixedAmount', 'type': 'ChargebackNewCalculatedBillFixedUseRequestDTO'},
        'copy_use_from_meter': {'key': 'copyUseFromMeter', 'type': 'ChargebackNewCalculatedBillCopyMeterRequestDTO'},
        'use_calculation': {'key': 'useCalculation', 'type': 'ChargebackNewCalculatedBillCalculationRequestDTO'},
    }

    def __init__(self, readings_channel_id=None, fixed_amount=None, copy_use_from_meter=None, use_calculation=None):
        super(ChargebackNewCalculatedBillCalculatedBillUseRequestDTO, self).__init__()
        self.readings_channel_id = readings_channel_id
        self.fixed_amount = fixed_amount
        self.copy_use_from_meter = copy_use_from_meter
        self.use_calculation = use_calculation
