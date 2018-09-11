# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportsReportCreateDTO(Model):
    """ReportsReportCreateDTO.

    :param report_code: New specific report code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 16 characters</span>
    :type report_code: str
    :param report_info: New specific report name <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 255 characters</span>
    :type report_info: str
    :param report_description: New specific report description <span
     class='property-internal'>Required</span>
    :type report_description: str
    :param report_category: Category for new specific report. <span
     class='property-internal'>Required</span> <span
     class='property-internal'>One of saved, public </span>
    :type report_category: str
    """

    _validation = {
        'report_code': {'required': True, 'max_length': 16, 'min_length': 0},
        'report_info': {'required': True, 'max_length': 255, 'min_length': 0},
        'report_description': {'required': True},
        'report_category': {'required': True},
    }

    _attribute_map = {
        'report_code': {'key': 'reportCode', 'type': 'str'},
        'report_info': {'key': 'reportInfo', 'type': 'str'},
        'report_description': {'key': 'reportDescription', 'type': 'str'},
        'report_category': {'key': 'reportCategory', 'type': 'str'},
    }

    def __init__(self, report_code, report_info, report_description, report_category):
        super(ReportsReportCreateDTO, self).__init__()
        self.report_code = report_code
        self.report_info = report_info
        self.report_description = report_description
        self.report_category = report_category
