# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WidgetPerformanceComparisonDataPointDto(Model):
    """WidgetPerformanceComparisonDataPointDto.

    :param period_number:
    :type period_number: int
    :param id:
    :type id: int
    :param cy_use:
    :type cy_use: float
    :param py_use:
    :type py_use: float
    """

    _attribute_map = {
        'period_number': {'key': 'periodNumber', 'type': 'int'},
        'id': {'key': 'id', 'type': 'int'},
        'cy_use': {'key': 'cyUse', 'type': 'float'},
        'py_use': {'key': 'pyUse', 'type': 'float'},
    }

    def __init__(self, period_number=None, id=None, cy_use=None, py_use=None):
        super(WidgetPerformanceComparisonDataPointDto, self).__init__()
        self.period_number = period_number
        self.id = id
        self.cy_use = cy_use
        self.py_use = py_use
