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


class VirtualNetworkPeering(SubResource):
    """Peerings in a virtual network resource.

    :param id: Resource ID.
    :type id: str
    :param allow_virtual_network_access: Whether the VMs in the linked virtual
     network space would be able to access all the VMs in local Virtual network
     space.
    :type allow_virtual_network_access: bool
    :param allow_forwarded_traffic: Whether the forwarded traffic from the VMs
     in the remote virtual network will be allowed/disallowed.
    :type allow_forwarded_traffic: bool
    :param allow_gateway_transit: If gateway links can be used in remote
     virtual networking to link to this virtual network.
    :type allow_gateway_transit: bool
    :param use_remote_gateways: If remote gateways can be used on this virtual
     network. If the flag is set to true, and allowGatewayTransit on remote
     peering is also true, virtual network will use gateways of remote virtual
     network for transit. Only one peering can have this flag set to true. This
     flag cannot be set if virtual network already has a gateway.
    :type use_remote_gateways: bool
    :param remote_virtual_network: The reference of the remote virtual
     network. The remote virtual network can be in the same or different region
     (preview). See here to register for the preview and learn more
     (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
    :type remote_virtual_network:
     ~azure.mgmt.network.v2017_09_01.models.SubResource
    :param remote_address_space: The reference of the remote virtual network
     address space.
    :type remote_address_space:
     ~azure.mgmt.network.v2017_09_01.models.AddressSpace
    :param peering_state: The status of the virtual network peering. Possible
     values are 'Initiated', 'Connected', and 'Disconnected'. Possible values
     include: 'Initiated', 'Connected', 'Disconnected'
    :type peering_state: str or
     ~azure.mgmt.network.v2017_09_01.models.VirtualNetworkPeeringState
    :param provisioning_state: The provisioning state of the resource.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'allow_virtual_network_access': {'key': 'properties.allowVirtualNetworkAccess', 'type': 'bool'},
        'allow_forwarded_traffic': {'key': 'properties.allowForwardedTraffic', 'type': 'bool'},
        'allow_gateway_transit': {'key': 'properties.allowGatewayTransit', 'type': 'bool'},
        'use_remote_gateways': {'key': 'properties.useRemoteGateways', 'type': 'bool'},
        'remote_virtual_network': {'key': 'properties.remoteVirtualNetwork', 'type': 'SubResource'},
        'remote_address_space': {'key': 'properties.remoteAddressSpace', 'type': 'AddressSpace'},
        'peering_state': {'key': 'properties.peeringState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkPeering, self).__init__(**kwargs)
        self.allow_virtual_network_access = kwargs.get('allow_virtual_network_access', None)
        self.allow_forwarded_traffic = kwargs.get('allow_forwarded_traffic', None)
        self.allow_gateway_transit = kwargs.get('allow_gateway_transit', None)
        self.use_remote_gateways = kwargs.get('use_remote_gateways', None)
        self.remote_virtual_network = kwargs.get('remote_virtual_network', None)
        self.remote_address_space = kwargs.get('remote_address_space', None)
        self.peering_state = kwargs.get('peering_state', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
