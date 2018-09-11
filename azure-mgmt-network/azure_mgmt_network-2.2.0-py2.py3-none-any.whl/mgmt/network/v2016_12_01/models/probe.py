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


class Probe(SubResource):
    """A load balancer probe.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :ivar load_balancing_rules: The load balancer rules that use this probe.
    :vartype load_balancing_rules:
     list[~azure.mgmt.network.v2016_12_01.models.SubResource]
    :param protocol: Required. The protocol of the end point. Possible values
     are: 'Http' or 'Tcp'. If 'Tcp' is specified, a received ACK is required
     for the probe to be successful. If 'Http' is specified, a 200 OK response
     from the specifies URI is required for the probe to be successful.
     Possible values include: 'Http', 'Tcp'
    :type protocol: str or
     ~azure.mgmt.network.v2016_12_01.models.ProbeProtocol
    :param port: Required. The port for communicating the probe. Possible
     values range from 1 to 65535, inclusive.
    :type port: int
    :param interval_in_seconds: The interval, in seconds, for how frequently
     to probe the endpoint for health status. Typically, the interval is
     slightly less than half the allocated timeout period (in seconds) which
     allows two full probes before taking the instance out of rotation. The
     default value is 15, the minimum value is 5.
    :type interval_in_seconds: int
    :param number_of_probes: The number of probes where if no response, will
     result in stopping further traffic from being delivered to the endpoint.
     This values allows endpoints to be taken out of rotation faster or slower
     than the typical times used in Azure.
    :type number_of_probes: int
    :param request_path: The URI used for requesting health status from the
     VM. Path is required if a protocol is set to http. Otherwise, it is not
     allowed. There is no default value.
    :type request_path: str
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'load_balancing_rules': {'readonly': True},
        'protocol': {'required': True},
        'port': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'load_balancing_rules': {'key': 'properties.loadBalancingRules', 'type': '[SubResource]'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'interval_in_seconds': {'key': 'properties.intervalInSeconds', 'type': 'int'},
        'number_of_probes': {'key': 'properties.numberOfProbes', 'type': 'int'},
        'request_path': {'key': 'properties.requestPath', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Probe, self).__init__(**kwargs)
        self.load_balancing_rules = None
        self.protocol = kwargs.get('protocol', None)
        self.port = kwargs.get('port', None)
        self.interval_in_seconds = kwargs.get('interval_in_seconds', None)
        self.number_of_probes = kwargs.get('number_of_probes', None)
        self.request_path = kwargs.get('request_path', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
