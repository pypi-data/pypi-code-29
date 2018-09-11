# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestPlaceDigestSavingsYearlyResponseDTO(Model):
    """PlaceDigestPlaceDigestSavingsYearlyResponseDTO.

    :param place_code: The place code
    :type place_code: str
    :param place_info: The place info
    :type place_info: str
    :param place_id: The place identifier
    :type place_id: int
    :param all_time_batcc_global_use: Program to Date BATCC (Baseline Adjusted
     to Current Conditions) Global Use
    :type all_time_batcc_global_use: float
    :param all_time_global_use: Program to Date Global Use
    :type all_time_global_use: float
    :param all_time_savings_global_use: Program to Date Savings Global Use =
     allTimeBATCCGlobalUse - allTimeGlobalUse
    :type all_time_savings_global_use: float
    :param all_time_batcc_total_cost: Program to Date BATCC (Baseline Adjusted
     to Current Conditions) Total Cost
    :type all_time_batcc_total_cost: float
    :param all_time_total_cost: Program to Date Savings Total Cost
    :type all_time_total_cost: float
    :param all_time_savings_total_cost: Program to Date Savings Total Cost =
     allTimeBATCCTotalCost - allTimeTotalCost
    :type all_time_savings_total_cost: float
    :param results: An array of savings yearly data
    :type results:
     list[~energycap.sdk.models.PlaceDigestPlaceDigestSavingsYearlyResponseDTOResultsDTO]
    :param updated: The date and time the data was updated
    :type updated: datetime
    :param global_use_unit: The use global unit of measure
    :type global_use_unit: ~energycap.sdk.models.UnitUnitChildDTO
    :param cost_unit: The cost unit of measure
    :type cost_unit: ~energycap.sdk.models.UnitUnitChildDTO
    :param commodities: An array of savings yearly data per commodity
    :type commodities:
     list[~energycap.sdk.models.PlaceDigestPlaceDigestSavingsYearlyResponseDTOCommodityDataDTO]
    """

    _attribute_map = {
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
        'place_id': {'key': 'placeId', 'type': 'int'},
        'all_time_batcc_global_use': {'key': 'allTimeBATCCGlobalUse', 'type': 'float'},
        'all_time_global_use': {'key': 'allTimeGlobalUse', 'type': 'float'},
        'all_time_savings_global_use': {'key': 'allTimeSavingsGlobalUse', 'type': 'float'},
        'all_time_batcc_total_cost': {'key': 'allTimeBATCCTotalCost', 'type': 'float'},
        'all_time_total_cost': {'key': 'allTimeTotalCost', 'type': 'float'},
        'all_time_savings_total_cost': {'key': 'allTimeSavingsTotalCost', 'type': 'float'},
        'results': {'key': 'results', 'type': '[PlaceDigestPlaceDigestSavingsYearlyResponseDTOResultsDTO]'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'global_use_unit': {'key': 'globalUseUnit', 'type': 'UnitUnitChildDTO'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitUnitChildDTO'},
        'commodities': {'key': 'commodities', 'type': '[PlaceDigestPlaceDigestSavingsYearlyResponseDTOCommodityDataDTO]'},
    }

    def __init__(self, place_code=None, place_info=None, place_id=None, all_time_batcc_global_use=None, all_time_global_use=None, all_time_savings_global_use=None, all_time_batcc_total_cost=None, all_time_total_cost=None, all_time_savings_total_cost=None, results=None, updated=None, global_use_unit=None, cost_unit=None, commodities=None):
        super(PlaceDigestPlaceDigestSavingsYearlyResponseDTO, self).__init__()
        self.place_code = place_code
        self.place_info = place_info
        self.place_id = place_id
        self.all_time_batcc_global_use = all_time_batcc_global_use
        self.all_time_global_use = all_time_global_use
        self.all_time_savings_global_use = all_time_savings_global_use
        self.all_time_batcc_total_cost = all_time_batcc_total_cost
        self.all_time_total_cost = all_time_total_cost
        self.all_time_savings_total_cost = all_time_savings_total_cost
        self.results = results
        self.updated = updated
        self.global_use_unit = global_use_unit
        self.cost_unit = cost_unit
        self.commodities = commodities
