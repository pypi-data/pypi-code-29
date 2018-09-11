# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualNetworkUsageName(Model):
    """Usage strings container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar localized_value: Localized subnet size and usage string.
    :vartype localized_value: str
    :ivar value: Subnet size and usage string.
    :vartype value: str
    """

    _validation = {
        'localized_value': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkUsageName, self).__init__(**kwargs)
        self.localized_value = None
        self.value = None
