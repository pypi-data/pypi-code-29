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

from .sub_resource import SubResource


class VirtualNetworkGatewayIPConfiguration(SubResource):
    """IP configuration for virtual network gateway.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param private_ip_allocation_method: The private IP allocation method.
     Possible values are: 'Static' and 'Dynamic'. Possible values include:
     'Static', 'Dynamic'
    :type private_ip_allocation_method: str or
     ~azure.mgmt.network.v2017_03_01.models.IPAllocationMethod
    :param subnet: The reference of the subnet resource.
    :type subnet: ~azure.mgmt.network.v2017_03_01.models.SubResource
    :param public_ip_address: The reference of the public IP resource.
    :type public_ip_address:
     ~azure.mgmt.network.v2017_03_01.models.SubResource
    :ivar provisioning_state: The provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'SubResource'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkGatewayIPConfiguration, self).__init__(**kwargs)
        self.private_ip_allocation_method = kwargs.get('private_ip_allocation_method', None)
        self.subnet = kwargs.get('subnet', None)
        self.public_ip_address = kwargs.get('public_ip_address', None)
        self.provisioning_state = None
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
