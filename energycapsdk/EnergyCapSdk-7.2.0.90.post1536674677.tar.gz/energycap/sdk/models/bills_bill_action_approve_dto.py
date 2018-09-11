# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillsBillActionApproveDto(Model):
    """BillsBillActionApproveDto.

    :param ids:  <span class='property-internal'>Cannot be Empty</span>
    :type ids: list[int]
    :param approve:
    :type approve: bool
    """

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[int]'},
        'approve': {'key': 'approve', 'type': 'bool'},
    }

    def __init__(self, ids=None, approve=None):
        super(BillsBillActionApproveDto, self).__init__()
        self.ids = ids
        self.approve = approve
