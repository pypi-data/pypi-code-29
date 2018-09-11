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


class TopologyResource(Model):
    """The network resource topology information for the given resource group.

    :param name: Name of the resource.
    :type name: str
    :param id: ID of the resource.
    :type id: str
    :param location: Resource location.
    :type location: str
    :param associations: Holds the associations the resource has with other
     resources in the resource group.
    :type associations:
     list[~azure.mgmt.network.v2017_08_01.models.TopologyAssociation]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'associations': {'key': 'associations', 'type': '[TopologyAssociation]'},
    }

    def __init__(self, *, name: str=None, id: str=None, location: str=None, associations=None, **kwargs) -> None:
        super(TopologyResource, self).__init__(**kwargs)
        self.name = name
        self.id = id
        self.location = location
        self.associations = associations
