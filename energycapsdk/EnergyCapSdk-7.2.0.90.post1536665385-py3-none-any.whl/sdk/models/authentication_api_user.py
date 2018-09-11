# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuthenticationApiUser(Model):
    """AuthenticationApiUser.

    :param user_name:
    :type user_name: str
    :param full_name:
    :type full_name: str
    """

    _attribute_map = {
        'user_name': {'key': 'userName', 'type': 'str'},
        'full_name': {'key': 'fullName', 'type': 'str'},
    }

    def __init__(self, user_name=None, full_name=None):
        super(AuthenticationApiUser, self).__init__()
        self.user_name = user_name
        self.full_name = full_name
