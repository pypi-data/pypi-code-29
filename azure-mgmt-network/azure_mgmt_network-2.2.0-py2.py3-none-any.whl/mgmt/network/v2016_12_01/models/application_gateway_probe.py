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


class ApplicationGatewayProbe(SubResource):
    """Probe of the application gateway.

    :param id: Resource ID.
    :type id: str
    :param protocol: Protocol. Possible values are: 'Http' and 'Https'.
     Possible values include: 'Http', 'Https'
    :type protocol: str or
     ~azure.mgmt.network.v2016_12_01.models.ApplicationGatewayProtocol
    :param host: Host name to send the probe to.
    :type host: str
    :param path: Relative path of probe. Valid path starts from '/'. Probe is
     sent to <Protocol>://<host>:<port><path>
    :type path: str
    :param interval: The probing interval in seconds. This is the time
     interval between two consecutive probes. Acceptable values are from 1
     second to 86400 seconds.
    :type interval: int
    :param timeout: the probe timeout in seconds. Probe marked as failed if
     valid response is not received with this timeout period. Acceptable values
     are from 1 second to 86400 seconds.
    :type timeout: int
    :param unhealthy_threshold: The probe retry count. Backend server is
     marked down after consecutive probe failure count reaches
     UnhealthyThreshold. Acceptable values are from 1 second to 20.
    :type unhealthy_threshold: int
    :param provisioning_state: Provisioning state of the backend http settings
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'host': {'key': 'properties.host', 'type': 'str'},
        'path': {'key': 'properties.path', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'int'},
        'timeout': {'key': 'properties.timeout', 'type': 'int'},
        'unhealthy_threshold': {'key': 'properties.unhealthyThreshold', 'type': 'int'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayProbe, self).__init__(**kwargs)
        self.protocol = kwargs.get('protocol', None)
        self.host = kwargs.get('host', None)
        self.path = kwargs.get('path', None)
        self.interval = kwargs.get('interval', None)
        self.timeout = kwargs.get('timeout', None)
        self.unhealthy_threshold = kwargs.get('unhealthy_threshold', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
