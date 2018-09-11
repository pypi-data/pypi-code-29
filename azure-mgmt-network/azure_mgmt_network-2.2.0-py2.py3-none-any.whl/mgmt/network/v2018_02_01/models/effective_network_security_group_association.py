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


class EffectiveNetworkSecurityGroupAssociation(Model):
    """The effective network security group association.

    :param subnet: The ID of the subnet if assigned.
    :type subnet: ~azure.mgmt.network.v2018_02_01.models.SubResource
    :param network_interface: The ID of the network interface if assigned.
    :type network_interface:
     ~azure.mgmt.network.v2018_02_01.models.SubResource
    """

    _attribute_map = {
        'subnet': {'key': 'subnet', 'type': 'SubResource'},
        'network_interface': {'key': 'networkInterface', 'type': 'SubResource'},
    }

    def __init__(self, **kwargs):
        super(EffectiveNetworkSecurityGroupAssociation, self).__init__(**kwargs)
        self.subnet = kwargs.get('subnet', None)
        self.network_interface = kwargs.get('network_interface', None)
