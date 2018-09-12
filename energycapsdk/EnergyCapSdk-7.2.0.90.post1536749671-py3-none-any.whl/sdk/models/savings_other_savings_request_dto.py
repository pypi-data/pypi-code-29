# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SavingsOtherSavingsRequestDTO(Model):
    """SavingsOtherSavingsRequestDTO.

    :param frequency: The type of other savings.
     Possible values are: one-time, continuous and recurring <span
     class='property-internal'>Required</span>
    :type frequency: str
    :param other_savings_category_id: The other savings category identifier
     <span class='property-internal'>Required</span>
    :type other_savings_category_id: int
    :param description: The description <span
     class='property-internal'>Required</span>
    :type description: str
    :param start_period: The period the other savings should begin <span
     class='property-internal'>Required</span>
    :type start_period: int
    :param end_period: The period the other savings should end <span
     class='property-internal'>Required when frequency is set to continuous, or
     recurring</span>
    :type end_period: int
    :param annual_cycle_start_month: The month the other savings should begin.
     This should only be set when the other savings type is recurring <span
     class='property-internal'>Required when frequency is set to
     recurring</span>
    :type annual_cycle_start_month: int
    :param annual_cycle_end_month: The month the other savings should end.
     This should only be set when the other savings type is recurring <span
     class='property-internal'>Required when frequency is set to
     recurring</span>
    :type annual_cycle_end_month: int
    :param value: The amount saved <span
     class='property-internal'>Required</span>
    :type value: float
    """

    _validation = {
        'frequency': {'required': True},
        'other_savings_category_id': {'required': True},
        'description': {'required': True},
        'start_period': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'str'},
        'other_savings_category_id': {'key': 'otherSavingsCategoryId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'start_period': {'key': 'startPeriod', 'type': 'int'},
        'end_period': {'key': 'endPeriod', 'type': 'int'},
        'annual_cycle_start_month': {'key': 'annualCycleStartMonth', 'type': 'int'},
        'annual_cycle_end_month': {'key': 'annualCycleEndMonth', 'type': 'int'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, frequency, other_savings_category_id, description, start_period, value, end_period=None, annual_cycle_start_month=None, annual_cycle_end_month=None):
        super(SavingsOtherSavingsRequestDTO, self).__init__()
        self.frequency = frequency
        self.other_savings_category_id = other_savings_category_id
        self.description = description
        self.start_period = start_period
        self.end_period = end_period
        self.annual_cycle_start_month = annual_cycle_start_month
        self.annual_cycle_end_month = annual_cycle_end_month
        self.value = value
