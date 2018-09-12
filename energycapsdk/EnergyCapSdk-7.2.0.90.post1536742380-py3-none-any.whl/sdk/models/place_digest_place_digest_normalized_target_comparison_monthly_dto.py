# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestPlaceDigestNormalizedTargetComparisonMonthlyDTO(Model):
    """PlaceDigestPlaceDigestNormalizedTargetComparisonMonthlyDTO.

    :param target_year: Target Year
    :type target_year: int
    :param target_label: Target Label
    :type target_label: str
    :param results: Monthly Target Data
    :type results:
     list[~energycap.sdk.models.PlaceDigestPlaceDigestNormalizedTargetComparisonMonthlyDTOResultsDTO]
    """

    _attribute_map = {
        'target_year': {'key': 'targetYear', 'type': 'int'},
        'target_label': {'key': 'targetLabel', 'type': 'str'},
        'results': {'key': 'results', 'type': '[PlaceDigestPlaceDigestNormalizedTargetComparisonMonthlyDTOResultsDTO]'},
    }

    def __init__(self, target_year=None, target_label=None, results=None):
        super(PlaceDigestPlaceDigestNormalizedTargetComparisonMonthlyDTO, self).__init__()
        self.target_year = target_year
        self.target_label = target_label
        self.results = results
