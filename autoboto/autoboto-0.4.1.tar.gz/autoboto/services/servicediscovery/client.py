import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("servicediscovery", *args, **kwargs)

    def create_private_dns_namespace(
        self,
        _request: shapes.CreatePrivateDnsNamespaceRequest = None,
        *,
        name: str,
        vpc: str,
        creator_request_id: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePrivateDnsNamespaceResponse:
        """
        Creates a private namespace based on DNS, which will be visible only inside a
        specified Amazon VPC. The namespace defines your service naming scheme. For
        example, if you name your namespace `example.com` and name your service
        `backend`, the resulting DNS name for the service will be `backend.example.com`.
        For the current limit on the number of namespaces that you can create using the
        same AWS account, see [Limits on Auto
        Naming](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-
        api-entities-autonaming) in the _Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            if creator_request_id is not ShapeBase.NOT_SET:
                _params['creator_request_id'] = creator_request_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreatePrivateDnsNamespaceRequest(**_params)
        response = self._boto_client.create_private_dns_namespace(
            **_request.to_boto()
        )

        return shapes.CreatePrivateDnsNamespaceResponse.from_boto(response)

    def create_public_dns_namespace(
        self,
        _request: shapes.CreatePublicDnsNamespaceRequest = None,
        *,
        name: str,
        creator_request_id: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePublicDnsNamespaceResponse:
        """
        Creates a public namespace based on DNS, which will be visible on the internet.
        The namespace defines your service naming scheme. For example, if you name your
        namespace `example.com` and name your service `backend`, the resulting DNS name
        for the service will be `backend.example.com`. For the current limit on the
        number of namespaces that you can create using the same AWS account, see [Limits
        on Auto
        Naming](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-
        api-entities-autonaming) in the _Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if creator_request_id is not ShapeBase.NOT_SET:
                _params['creator_request_id'] = creator_request_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreatePublicDnsNamespaceRequest(**_params)
        response = self._boto_client.create_public_dns_namespace(
            **_request.to_boto()
        )

        return shapes.CreatePublicDnsNamespaceResponse.from_boto(response)

    def create_service(
        self,
        _request: shapes.CreateServiceRequest = None,
        *,
        name: str,
        dns_config: shapes.DnsConfig,
        creator_request_id: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        health_check_config: shapes.HealthCheckConfig = ShapeBase.NOT_SET,
        health_check_custom_config: shapes.HealthCheckCustomConfig = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateServiceResponse:
        """
        Creates a service, which defines the configuration for the following entities:

          * Up to three records (A, AAAA, and SRV) or one CNAME record

          * Optionally, a health check

        After you create the service, you can submit a RegisterInstance request, and
        Amazon Route 53 uses the values in the configuration to create the specified
        entities.

        For the current limit on the number of instances that you can register using the
        same namespace and using the same service, see [Limits on Auto
        Naming](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-
        api-entities-autonaming) in the _Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if dns_config is not ShapeBase.NOT_SET:
                _params['dns_config'] = dns_config
            if creator_request_id is not ShapeBase.NOT_SET:
                _params['creator_request_id'] = creator_request_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if health_check_config is not ShapeBase.NOT_SET:
                _params['health_check_config'] = health_check_config
            if health_check_custom_config is not ShapeBase.NOT_SET:
                _params['health_check_custom_config'
                       ] = health_check_custom_config
            _request = shapes.CreateServiceRequest(**_params)
        response = self._boto_client.create_service(**_request.to_boto())

        return shapes.CreateServiceResponse.from_boto(response)

    def delete_namespace(
        self,
        _request: shapes.DeleteNamespaceRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteNamespaceResponse:
        """
        Deletes a namespace from the current account. If the namespace still contains
        one or more services, the request fails.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteNamespaceRequest(**_params)
        response = self._boto_client.delete_namespace(**_request.to_boto())

        return shapes.DeleteNamespaceResponse.from_boto(response)

    def delete_service(
        self,
        _request: shapes.DeleteServiceRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteServiceResponse:
        """
        Deletes a specified service. If the service still contains one or more
        registered instances, the request fails.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteServiceRequest(**_params)
        response = self._boto_client.delete_service(**_request.to_boto())

        return shapes.DeleteServiceResponse.from_boto(response)

    def deregister_instance(
        self,
        _request: shapes.DeregisterInstanceRequest = None,
        *,
        service_id: str,
        instance_id: str,
    ) -> shapes.DeregisterInstanceResponse:
        """
        Deletes the records and the health check, if any, that Amazon Route 53 created
        for the specified instance.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.DeregisterInstanceRequest(**_params)
        response = self._boto_client.deregister_instance(**_request.to_boto())

        return shapes.DeregisterInstanceResponse.from_boto(response)

    def get_instance(
        self,
        _request: shapes.GetInstanceRequest = None,
        *,
        service_id: str,
        instance_id: str,
    ) -> shapes.GetInstanceResponse:
        """
        Gets information about a specified instance.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.GetInstanceRequest(**_params)
        response = self._boto_client.get_instance(**_request.to_boto())

        return shapes.GetInstanceResponse.from_boto(response)

    def get_instances_health_status(
        self,
        _request: shapes.GetInstancesHealthStatusRequest = None,
        *,
        service_id: str,
        instances: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetInstancesHealthStatusResponse:
        """
        Gets the current health status (`Healthy`, `Unhealthy`, or `Unknown`) of one or
        more instances that are associated with a specified service.

        There is a brief delay between when you register an instance and when the health
        status for the instance is available.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if instances is not ShapeBase.NOT_SET:
                _params['instances'] = instances
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetInstancesHealthStatusRequest(**_params)
        response = self._boto_client.get_instances_health_status(
            **_request.to_boto()
        )

        return shapes.GetInstancesHealthStatusResponse.from_boto(response)

    def get_namespace(
        self,
        _request: shapes.GetNamespaceRequest = None,
        *,
        id: str,
    ) -> shapes.GetNamespaceResponse:
        """
        Gets information about a namespace.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetNamespaceRequest(**_params)
        response = self._boto_client.get_namespace(**_request.to_boto())

        return shapes.GetNamespaceResponse.from_boto(response)

    def get_operation(
        self,
        _request: shapes.GetOperationRequest = None,
        *,
        operation_id: str,
    ) -> shapes.GetOperationResponse:
        """
        Gets information about any operation that returns an operation ID in the
        response, such as a `CreateService` request.

        To get a list of operations that match specified criteria, see ListOperations.
        """
        if _request is None:
            _params = {}
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.GetOperationRequest(**_params)
        response = self._boto_client.get_operation(**_request.to_boto())

        return shapes.GetOperationResponse.from_boto(response)

    def get_service(
        self,
        _request: shapes.GetServiceRequest = None,
        *,
        id: str,
    ) -> shapes.GetServiceResponse:
        """
        Gets the settings for a specified service.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetServiceRequest(**_params)
        response = self._boto_client.get_service(**_request.to_boto())

        return shapes.GetServiceResponse.from_boto(response)

    def list_instances(
        self,
        _request: shapes.ListInstancesRequest = None,
        *,
        service_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListInstancesResponse:
        """
        Lists summary information about the instances that you registered by using a
        specified service.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListInstancesRequest(**_params)
        paginator = self.get_paginator("list_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInstancesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInstancesResponse.from_boto(response)

    def list_namespaces(
        self,
        _request: shapes.ListNamespacesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.NamespaceFilter] = ShapeBase.NOT_SET,
    ) -> shapes.ListNamespacesResponse:
        """
        Lists summary information about the namespaces that were created by the current
        AWS account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.ListNamespacesRequest(**_params)
        paginator = self.get_paginator("list_namespaces").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListNamespacesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListNamespacesResponse.from_boto(response)

    def list_operations(
        self,
        _request: shapes.ListOperationsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.OperationFilter] = ShapeBase.NOT_SET,
    ) -> shapes.ListOperationsResponse:
        """
        Lists operations that match the criteria that you specify.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.ListOperationsRequest(**_params)
        paginator = self.get_paginator("list_operations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOperationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOperationsResponse.from_boto(response)

    def list_services(
        self,
        _request: shapes.ListServicesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.ServiceFilter] = ShapeBase.NOT_SET,
    ) -> shapes.ListServicesResponse:
        """
        Lists summary information for all the services that are associated with one or
        more specified namespaces.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.ListServicesRequest(**_params)
        paginator = self.get_paginator("list_services").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListServicesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListServicesResponse.from_boto(response)

    def register_instance(
        self,
        _request: shapes.RegisterInstanceRequest = None,
        *,
        service_id: str,
        instance_id: str,
        attributes: typing.Dict[str, str],
        creator_request_id: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterInstanceResponse:
        """
        Creates or updates one or more records and optionally a health check based on
        the settings in a specified service. When you submit a `RegisterInstance`
        request, Amazon Route 53 does the following:

          * For each DNS record that you define in the service specified by `ServiceId`, creates or updates a record in the hosted zone that is associated with the corresponding namespace

          * If the service includes `HealthCheckConfig`, creates or updates a health check based on the settings in the health check configuration

          * Associates the health check, if any, with each of the records

        One `RegisterInstance` request must complete before you can submit another
        request and specify the same service ID and instance ID.

        For more information, see CreateService.

        When Route 53 receives a DNS query for the specified DNS name, it returns the
        applicable value:

          * **If the health check is healthy** : returns all the records

          * **If the health check is unhealthy** : returns the applicable value for the last healthy instance

          * **If you didn't specify a health check configuration** : returns all the records

        For the current limit on the number of instances that you can register using the
        same namespace and using the same service, see [Limits on Auto
        Naming](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-
        api-entities-autonaming) in the _Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if creator_request_id is not ShapeBase.NOT_SET:
                _params['creator_request_id'] = creator_request_id
            _request = shapes.RegisterInstanceRequest(**_params)
        response = self._boto_client.register_instance(**_request.to_boto())

        return shapes.RegisterInstanceResponse.from_boto(response)

    def update_instance_custom_health_status(
        self,
        _request: shapes.UpdateInstanceCustomHealthStatusRequest = None,
        *,
        service_id: str,
        instance_id: str,
        status: typing.Union[str, shapes.CustomHealthStatus],
    ) -> None:
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.UpdateInstanceCustomHealthStatusRequest(**_params)
        response = self._boto_client.update_instance_custom_health_status(
            **_request.to_boto()
        )

    def update_service(
        self,
        _request: shapes.UpdateServiceRequest = None,
        *,
        id: str,
        service: shapes.ServiceChange,
    ) -> shapes.UpdateServiceResponse:
        """
        Submits a request to perform the following operations:

          * Add or delete `DnsRecords` configurations

          * Update the TTL setting for existing `DnsRecords` configurations

          * Add, update, or delete `HealthCheckConfig` for a specified service

        You must specify all `DnsRecords` configurations (and, optionally,
        `HealthCheckConfig`) that you want to appear in the updated service. Any current
        configurations that don't appear in an `UpdateService` request are deleted.

        When you update the TTL setting for a service, Amazon Route 53 also updates the
        corresponding settings in all the records and health checks that were created by
        using the specified service.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if service is not ShapeBase.NOT_SET:
                _params['service'] = service
            _request = shapes.UpdateServiceRequest(**_params)
        response = self._boto_client.update_service(**_request.to_boto())

        return shapes.UpdateServiceResponse.from_boto(response)
