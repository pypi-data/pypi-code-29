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

from .resource import Resource


class ApplicationGateway(Resource):
    """Application gateway resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: SKU of the application gateway resource.
    :type sku: ~azure.mgmt.network.v2017_06_01.models.ApplicationGatewaySku
    :param ssl_policy: SSL policy of the application gateway resource.
    :type ssl_policy:
     ~azure.mgmt.network.v2017_06_01.models.ApplicationGatewaySslPolicy
    :ivar operational_state: Operational state of the application gateway
     resource. Possible values include: 'Stopped', 'Starting', 'Running',
     'Stopping'
    :vartype operational_state: str or
     ~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayOperationalState
    :param gateway_ip_configurations: Subnets of application the gateway
     resource.
    :type gateway_ip_configurations:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayIPConfiguration]
    :param authentication_certificates: Authentication certificates of the
     application gateway resource.
    :type authentication_certificates:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayAuthenticationCertificate]
    :param ssl_certificates: SSL certificates of the application gateway
     resource.
    :type ssl_certificates:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewaySslCertificate]
    :param frontend_ip_configurations: Frontend IP addresses of the
     application gateway resource.
    :type frontend_ip_configurations:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayFrontendIPConfiguration]
    :param frontend_ports: Frontend ports of the application gateway resource.
    :type frontend_ports:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayFrontendPort]
    :param probes: Probes of the application gateway resource.
    :type probes:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayProbe]
    :param backend_address_pools: Backend address pool of the application
     gateway resource.
    :type backend_address_pools:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayBackendAddressPool]
    :param backend_http_settings_collection: Backend http settings of the
     application gateway resource.
    :type backend_http_settings_collection:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayBackendHttpSettings]
    :param http_listeners: Http listeners of the application gateway resource.
    :type http_listeners:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayHttpListener]
    :param url_path_maps: URL path map of the application gateway resource.
    :type url_path_maps:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayUrlPathMap]
    :param request_routing_rules: Request routing rules of the application
     gateway resource.
    :type request_routing_rules:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayRequestRoutingRule]
    :param redirect_configurations: Redirect configurations of the application
     gateway resource.
    :type redirect_configurations:
     list[~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayRedirectConfiguration]
    :param web_application_firewall_configuration: Web application firewall
     configuration.
    :type web_application_firewall_configuration:
     ~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayWebApplicationFirewallConfiguration
    :param resource_guid: Resource GUID property of the application gateway
     resource.
    :type resource_guid: str
    :param provisioning_state: Provisioning state of the application gateway
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'operational_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'properties.sku', 'type': 'ApplicationGatewaySku'},
        'ssl_policy': {'key': 'properties.sslPolicy', 'type': 'ApplicationGatewaySslPolicy'},
        'operational_state': {'key': 'properties.operationalState', 'type': 'str'},
        'gateway_ip_configurations': {'key': 'properties.gatewayIPConfigurations', 'type': '[ApplicationGatewayIPConfiguration]'},
        'authentication_certificates': {'key': 'properties.authenticationCertificates', 'type': '[ApplicationGatewayAuthenticationCertificate]'},
        'ssl_certificates': {'key': 'properties.sslCertificates', 'type': '[ApplicationGatewaySslCertificate]'},
        'frontend_ip_configurations': {'key': 'properties.frontendIPConfigurations', 'type': '[ApplicationGatewayFrontendIPConfiguration]'},
        'frontend_ports': {'key': 'properties.frontendPorts', 'type': '[ApplicationGatewayFrontendPort]'},
        'probes': {'key': 'properties.probes', 'type': '[ApplicationGatewayProbe]'},
        'backend_address_pools': {'key': 'properties.backendAddressPools', 'type': '[ApplicationGatewayBackendAddressPool]'},
        'backend_http_settings_collection': {'key': 'properties.backendHttpSettingsCollection', 'type': '[ApplicationGatewayBackendHttpSettings]'},
        'http_listeners': {'key': 'properties.httpListeners', 'type': '[ApplicationGatewayHttpListener]'},
        'url_path_maps': {'key': 'properties.urlPathMaps', 'type': '[ApplicationGatewayUrlPathMap]'},
        'request_routing_rules': {'key': 'properties.requestRoutingRules', 'type': '[ApplicationGatewayRequestRoutingRule]'},
        'redirect_configurations': {'key': 'properties.redirectConfigurations', 'type': '[ApplicationGatewayRedirectConfiguration]'},
        'web_application_firewall_configuration': {'key': 'properties.webApplicationFirewallConfiguration', 'type': 'ApplicationGatewayWebApplicationFirewallConfiguration'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGateway, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.ssl_policy = kwargs.get('ssl_policy', None)
        self.operational_state = None
        self.gateway_ip_configurations = kwargs.get('gateway_ip_configurations', None)
        self.authentication_certificates = kwargs.get('authentication_certificates', None)
        self.ssl_certificates = kwargs.get('ssl_certificates', None)
        self.frontend_ip_configurations = kwargs.get('frontend_ip_configurations', None)
        self.frontend_ports = kwargs.get('frontend_ports', None)
        self.probes = kwargs.get('probes', None)
        self.backend_address_pools = kwargs.get('backend_address_pools', None)
        self.backend_http_settings_collection = kwargs.get('backend_http_settings_collection', None)
        self.http_listeners = kwargs.get('http_listeners', None)
        self.url_path_maps = kwargs.get('url_path_maps', None)
        self.request_routing_rules = kwargs.get('request_routing_rules', None)
        self.redirect_configurations = kwargs.get('redirect_configurations', None)
        self.web_application_firewall_configuration = kwargs.get('web_application_firewall_configuration', None)
        self.resource_guid = kwargs.get('resource_guid', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.etag = kwargs.get('etag', None)
