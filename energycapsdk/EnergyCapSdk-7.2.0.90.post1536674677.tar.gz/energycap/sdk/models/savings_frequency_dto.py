# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SavingsFrequencyDTO(Model):
    """SavingsFrequencyDTO.

    :param frequency: The frequency
    :type frequency: str
    :param start_date: The start date
    :type start_date: datetime
    :param end_date: The end date
    :type end_date: datetime
    :param annual_cycle_start_mmdd: The frequency start period
    :type annual_cycle_start_mmdd: int
    :param annual_cycle_end_mmdd: The frequency end period
    :type annual_cycle_end_mmdd: int
    :param annual_cycle_start_info: The precision on value
    :type annual_cycle_start_info: str
    :param annual_cycle_end_info: The frequency cycle end of recurrsion
    :type annual_cycle_end_info: str
    """

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'annual_cycle_start_mmdd': {'key': 'annualCycleStartMMDD', 'type': 'int'},
        'annual_cycle_end_mmdd': {'key': 'annualCycleEndMMDD', 'type': 'int'},
        'annual_cycle_start_info': {'key': 'annualCycleStartInfo', 'type': 'str'},
        'annual_cycle_end_info': {'key': 'annualCycleEndInfo', 'type': 'str'},
    }

    def __init__(self, frequency=None, start_date=None, end_date=None, annual_cycle_start_mmdd=None, annual_cycle_end_mmdd=None, annual_cycle_start_info=None, annual_cycle_end_info=None):
        super(SavingsFrequencyDTO, self).__init__()
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date
        self.annual_cycle_start_mmdd = annual_cycle_start_mmdd
        self.annual_cycle_end_mmdd = annual_cycle_end_mmdd
        self.annual_cycle_start_info = annual_cycle_start_info
        self.annual_cycle_end_info = annual_cycle_end_info
