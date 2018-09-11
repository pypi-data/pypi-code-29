# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestPlaceDigestGHGMonthlyResponseDTOGHGCommodityDTO(Model):
    """PlaceDigestPlaceDigestGHGMonthlyResponseDTOGHGCommodityDTO.

    :param commodity_id: Commodity Id
    :type commodity_id: int
    :param commodity_code: Commodity Code
    :type commodity_code: str
    :param commodity_info: Commodity info
    :type commodity_info: str
    :param target_comparison: The target monthly info
    :type target_comparison:
     ~energycap.sdk.models.PlaceDigestPlaceDigestGHGMonthlyResponseDTOTargetComparisonDTO
    :param results: An array of monthly data
    :type results:
     list[~energycap.sdk.models.PlaceDigestPlaceDigestGHGMonthlyResponseDTOResultsDTO]
    """

    _attribute_map = {
        'commodity_id': {'key': 'commodityId', 'type': 'int'},
        'commodity_code': {'key': 'commodityCode', 'type': 'str'},
        'commodity_info': {'key': 'commodityInfo', 'type': 'str'},
        'target_comparison': {'key': 'targetComparison', 'type': 'PlaceDigestPlaceDigestGHGMonthlyResponseDTOTargetComparisonDTO'},
        'results': {'key': 'results', 'type': '[PlaceDigestPlaceDigestGHGMonthlyResponseDTOResultsDTO]'},
    }

    def __init__(self, commodity_id=None, commodity_code=None, commodity_info=None, target_comparison=None, results=None):
        super(PlaceDigestPlaceDigestGHGMonthlyResponseDTOGHGCommodityDTO, self).__init__()
        self.commodity_id = commodity_id
        self.commodity_code = commodity_code
        self.commodity_info = commodity_info
        self.target_comparison = target_comparison
        self.results = results
