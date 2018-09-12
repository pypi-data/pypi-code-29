# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestPlaceDigestSavingsMonthlyResponseDTOResultsDTO(Model):
    """PlaceDigestPlaceDigestSavingsMonthlyResponseDTOResultsDTO.

    :param period_name: Calendar Period Name
    :type period_name: str
    :param calendar_period: Calendar Period
    :type calendar_period: int
    :param calendar_year: Calendar Year
    :type calendar_year: int
    :param fiscal_period: Fiscal Period
    :type fiscal_period: int
    :param fiscal_year: Fiscal Year
    :type fiscal_year: int
    :param savings_total_cost: Savings Total Cost
    :type savings_total_cost: float
    :param savings_global_use: Savings Global Use
    :type savings_global_use: float
    """

    _attribute_map = {
        'period_name': {'key': 'periodName', 'type': 'str'},
        'calendar_period': {'key': 'calendarPeriod', 'type': 'int'},
        'calendar_year': {'key': 'calendarYear', 'type': 'int'},
        'fiscal_period': {'key': 'fiscalPeriod', 'type': 'int'},
        'fiscal_year': {'key': 'fiscalYear', 'type': 'int'},
        'savings_total_cost': {'key': 'savingsTotalCost', 'type': 'float'},
        'savings_global_use': {'key': 'savingsGlobalUse', 'type': 'float'},
    }

    def __init__(self, period_name=None, calendar_period=None, calendar_year=None, fiscal_period=None, fiscal_year=None, savings_total_cost=None, savings_global_use=None):
        super(PlaceDigestPlaceDigestSavingsMonthlyResponseDTOResultsDTO, self).__init__()
        self.period_name = period_name
        self.calendar_period = calendar_period
        self.calendar_year = calendar_year
        self.fiscal_period = fiscal_period
        self.fiscal_year = fiscal_year
        self.savings_total_cost = savings_total_cost
        self.savings_global_use = savings_global_use
