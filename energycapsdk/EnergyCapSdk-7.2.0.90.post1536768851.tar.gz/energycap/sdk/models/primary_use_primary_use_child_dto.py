# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrimaryUsePrimaryUseChildDTO(Model):
    """PrimaryUsePrimaryUseChildDTO.

    :param primary_use_id:
    :type primary_use_id: int
    :param primary_use_code:
    :type primary_use_code: str
    :param primary_use_info:
    :type primary_use_info: str
    """

    _attribute_map = {
        'primary_use_id': {'key': 'primaryUseId', 'type': 'int'},
        'primary_use_code': {'key': 'primaryUseCode', 'type': 'str'},
        'primary_use_info': {'key': 'primaryUseInfo', 'type': 'str'},
    }

    def __init__(self, primary_use_id=None, primary_use_code=None, primary_use_info=None):
        super(PrimaryUsePrimaryUseChildDTO, self).__init__()
        self.primary_use_id = primary_use_id
        self.primary_use_code = primary_use_code
        self.primary_use_info = primary_use_info
