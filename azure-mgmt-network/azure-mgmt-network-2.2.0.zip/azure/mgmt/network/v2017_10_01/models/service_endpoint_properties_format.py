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


class ServiceEndpointPropertiesFormat(Model):
    """The service endpoint properties.

    :param service: The type of the endpoint service.
    :type service: str
    :param locations: A list of locations.
    :type locations: list[str]
    :param provisioning_state: The provisioning state of the resource.
    :type provisioning_state: str
    """

    _attribute_map = {
        'service': {'key': 'service', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceEndpointPropertiesFormat, self).__init__(**kwargs)
        self.service = kwargs.get('service', None)
        self.locations = kwargs.get('locations', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
