import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class CreatePrivateDnsNamespaceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "vpc",
                "Vpc",
                TypeInfo(str),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name that you want to assign to this namespace. When you create a
    # namespace, Amazon Route 53 automatically creates a hosted zone that has the
    # same name as the namespace.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Amazon VPC that you want to associate the namespace with.
    vpc: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique string that identifies the request and that allows failed
    # `CreatePrivateDnsNamespace` requests to be retried without the risk of
    # executing the operation twice. `CreatorRequestId` can be any unique string,
    # for example, a date/time stamp.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description for the namespace.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePrivateDnsNamespaceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that you can use to determine whether the request completed
    # successfully. To get the status of the operation, see GetOperation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePublicDnsNamespaceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name that you want to assign to this namespace.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique string that identifies the request and that allows failed
    # `CreatePublicDnsNamespace` requests to be retried without the risk of
    # executing the operation twice. `CreatorRequestId` can be any unique string,
    # for example, a date/time stamp.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description for the namespace.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePublicDnsNamespaceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that you can use to determine whether the request completed
    # successfully. To get the status of the operation, see GetOperation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "dns_config",
                "DnsConfig",
                TypeInfo(DnsConfig),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "health_check_config",
                "HealthCheckConfig",
                TypeInfo(HealthCheckConfig),
            ),
            (
                "health_check_custom_config",
                "HealthCheckCustomConfig",
                TypeInfo(HealthCheckCustomConfig),
            ),
        ]

    # The name that you want to assign to the service.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about the records that you want
    # Route 53 to create when you register an instance.
    dns_config: "DnsConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique string that identifies the request and that allows failed
    # `CreateService` requests to be retried without the risk of executing the
    # operation twice. `CreatorRequestId` can be any unique string, for example,
    # a date/time stamp.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description for the service.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # _Public DNS namespaces only._ A complex type that contains settings for an
    # optional health check. If you specify settings for a health check, Route 53
    # associates the health check with all the records that you specify in
    # `DnsConfig`.

    # For information about the charges for health checks, see [Route 53
    # Pricing](http://aws.amazon.com/route53/pricing).
    health_check_config: "HealthCheckConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    health_check_custom_config: "HealthCheckCustomConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service",
                "Service",
                TypeInfo(Service),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about the new service.
    service: "Service" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomHealthNotFound(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CustomHealthStatus(str):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


@dataclasses.dataclass
class DeleteNamespaceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the namespace that you want to delete.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNamespaceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that you can use to determine whether the request completed
    # successfully. To get the status of the operation, see GetOperation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the service that you want to delete.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the service that the instance is associated with.
    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that you specified for `Id` in the RegisterInstance request.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterInstanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that you can use to determine whether the request completed
    # successfully. For more information, see GetOperation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DnsConfig(ShapeBase):
    """
    A complex type that contains information about the records that you want Amazon
    Route 53 to create when you register an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "namespace_id",
                "NamespaceId",
                TypeInfo(str),
            ),
            (
                "dns_records",
                "DnsRecords",
                TypeInfo(typing.List[DnsRecord]),
            ),
            (
                "routing_policy",
                "RoutingPolicy",
                TypeInfo(typing.Union[str, RoutingPolicy]),
            ),
        ]

    # The ID of the namespace to use for DNS configuration.
    namespace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array that contains one `DnsRecord` object for each record that you want
    # Route 53 to create when you register an instance.
    dns_records: typing.List["DnsRecord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The routing policy that you want to apply to all records that Route 53
    # creates when you register an instance and specify this service.

    # If you want to use this service to register instances that create alias
    # records, specify `WEIGHTED` for the routing policy.

    # You can specify the following values:

    # **MULTIVALUE**

    # If you define a health check for the service and the health check is
    # healthy, Route 53 returns the applicable value for up to eight instances.

    # For example, suppose the service includes configurations for one A record
    # and a health check, and you use the service to register 10 instances. Route
    # 53 responds to DNS queries with IP addresses for up to eight healthy
    # instances. If fewer than eight instances are healthy, Route 53 responds to
    # every DNS query with the IP addresses for all of the healthy instances.

    # If you don't define a health check for the service, Route 53 assumes that
    # all instances are healthy and returns the values for up to eight instances.

    # For more information about the multivalue routing policy, see [Multivalue
    # Answer
    # Routing](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-
    # policy.html#routing-policy-multivalue) in the _Route 53 Developer Guide_.

    # **WEIGHTED**

    # Route 53 returns the applicable value from one randomly selected instance
    # from among the instances that you registered using the same service.
    # Currently, all records have the same weight, so you can't route more or
    # less traffic to any instances.

    # For example, suppose the service includes configurations for one A record
    # and a health check, and you use the service to register 10 instances. Route
    # 53 responds to DNS queries with the IP address for one randomly selected
    # instance from among the healthy instances. If no instances are healthy,
    # Route 53 responds to DNS queries as if all of the instances were healthy.

    # If you don't define a health check for the service, Route 53 assumes that
    # all instances are healthy and returns the applicable value for one randomly
    # selected instance.

    # For more information about the weighted routing policy, see [Weighted
    # Routing](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-
    # policy.html#routing-policy-weighted) in the _Route 53 Developer Guide_.
    routing_policy: typing.Union[str, "RoutingPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DnsConfigChange(ShapeBase):
    """
    A complex type that contains information about changes to the records that Route
    53 creates when you register an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dns_records",
                "DnsRecords",
                TypeInfo(typing.List[DnsRecord]),
            ),
        ]

    # An array that contains one `DnsRecord` object for each record that you want
    # Route 53 to create when you register an instance.
    dns_records: typing.List["DnsRecord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DnsProperties(ShapeBase):
    """
    A complex type that contains the ID for the hosted zone that Route 53 creates
    when you create a namespace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hosted_zone_id",
                "HostedZoneId",
                TypeInfo(str),
            ),
        ]

    # The ID for the hosted zone that Route 53 creates when you create a
    # namespace.
    hosted_zone_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DnsRecord(ShapeBase):
    """
    A complex type that contains information about the records that you want Route
    53 to create when you register an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, RecordType]),
            ),
            (
                "ttl",
                "TTL",
                TypeInfo(int),
            ),
        ]

    # The type of the resource, which indicates the type of value that Route 53
    # returns in response to DNS queries.

    # Note the following:

    #   * **A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.**

    #   * **CNAME records:** If you specify `CNAME` for `Type`, you can't define any other records. This is a limitation of DNS—you can't create a CNAME record and any other type of record that has the same name as a CNAME record.

    #   * **Alias records:** If you want Route 53 to create an alias record when you register an instance, specify `A` or `AAAA` for `Type`.

    #   * **All records:** You specify settings other than `TTL` and `Type` when you register an instance.

    # The following values are supported:

    # **A**

    # Route 53 returns the IP address of the resource in IPv4 format, such as
    # 192.0.2.44.

    # **AAAA**

    # Route 53 returns the IP address of the resource in IPv6 format, such as
    # 2001:0db8:85a3:0000:0000:abcd:0001:2345.

    # **CNAME**

    # Route 53 returns the domain name of the resource, such as www.example.com.
    # Note the following:

    #   * You specify the domain name that you want to route traffic to when you register an instance. For more information, see RegisterInstanceRequest$Attributes.

    #   * You must specify `WEIGHTED` for the value of `RoutingPolicy`.

    #   * You can't specify both `CNAME` for `Type` and settings for `HealthCheckConfig`. If you do, the request will fail with an `InvalidInput` error.

    # **SRV**

    # Route 53 returns the value for an SRV record. The value for an SRV record
    # uses the following values:

    # `priority weight port service-hostname`

    # Note the following about the values:

    #   * The values of `priority` and `weight` are both set to `1` and can't be changed.

    #   * The value of `port` comes from the value that you specify for the `AWS_INSTANCE_PORT` attribute when you submit a RegisterInstance request.

    #   * The value of `service-hostname` is a concatenation of the following values:

    #     * The value that you specify for `InstanceId` when you register an instance.

    #     * The name of the service.

    #     * The name of the namespace.

    # For example, if the value of `InstanceId` is `test`, the name of the
    # service is `backend`, and the name of the namespace is `example.com`, the
    # value of `service-hostname` is:

    # `test.backend.example.com`

    # If you specify settings for an SRV record and if you specify values for
    # `AWS_INSTANCE_IPV4`, `AWS_INSTANCE_IPV6`, or both in the `RegisterInstance`
    # request, Route 53 automatically creates `A` and/or `AAAA` records that have
    # the same name as the value of `service-hostname` in the SRV record. You can
    # ignore these records.
    type: typing.Union[str, "RecordType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, that you want DNS resolvers to cache the
    # settings for this record.

    # Alias records don't include a TTL because Route 53 uses the TTL for the AWS
    # resource that an alias record routes traffic to. If you include the
    # `AWS_ALIAS_DNS_NAME` attribute when you submit a RegisterInstance request,
    # the `TTL` value is ignored. Always specify a TTL for the service; you can
    # use a service to register instances that create either alias or non-alias
    # records.
    ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateRequest(ShapeBase):
    """
    The operation is already in progress.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FilterCondition(str):
    EQ = "EQ"
    IN = "IN"
    BETWEEN = "BETWEEN"


@dataclasses.dataclass
class GetInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the service that the instance is associated with.
    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance that you want to get information about.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance",
                "Instance",
                TypeInfo(Instance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about a specified instance.
    instance: "Instance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancesHealthStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the service that the instance is associated with.
    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array that contains the IDs of all the instances that you want to get
    # the health status for.

    # If you omit `Instances`, Amazon Route 53 returns the health status for all
    # the instances that are associated with the specified service.

    # To get the IDs for the instances that you've registered by using a
    # specified service, submit a ListInstances request.
    instances: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of instances that you want Route 53 to return in the
    # response to a `GetInstancesHealthStatus` request. If you don't specify a
    # value for `MaxResults`, Route 53 returns up to 100 instances.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For the first `GetInstancesHealthStatus` request, omit this value.

    # If more than `MaxResults` instances match the specified criteria, you can
    # submit another `GetInstancesHealthStatus` request to get the next group of
    # results. Specify the value of `NextToken` from the previous response in the
    # next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancesHealthStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Dict[str, typing.Union[str, HealthStatus]]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains the IDs and the health status of the instances
    # that you specified in the `GetInstancesHealthStatus` request.
    status: typing.Dict[str, typing.
                        Union[str, "HealthStatus"]] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # If more than `MaxResults` instances match the specified criteria, you can
    # submit another `GetInstancesHealthStatus` request to get the next group of
    # results. Specify the value of `NextToken` from the previous response in the
    # next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetNamespaceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the namespace that you want to get information about.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetNamespaceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "namespace",
                "Namespace",
                TypeInfo(Namespace),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about the specified namespace.
    namespace: "Namespace" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The ID of the operation that you want to get more information about.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "Operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about the operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID of the service that you want to get settings for.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service",
                "Service",
                TypeInfo(Service),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about the service.
    service: "Service" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HealthCheckConfig(ShapeBase):
    """
    _Public DNS namespaces only._ A complex type that contains settings for an
    optional health check. If you specify settings for a health check, Amazon Route
    53 associates the health check with all the records that you specify in
    `DnsConfig`.

    **A and AAAA records**

    If `DnsConfig` includes configurations for both A and AAAA records, Route 53
    creates a health check that uses the IPv4 address to check the health of the
    resource. If the endpoint that is specified by the IPv4 address is unhealthy,
    Route 53 considers both the A and AAAA records to be unhealthy.

    **CNAME records**

    You can't specify settings for `HealthCheckConfig` when the `DNSConfig` includes
    `CNAME` for the value of `Type`. If you do, the `CreateService` request will
    fail with an `InvalidInput` error.

    **Request interval**

    The health check uses 30 seconds as the request interval. This is the number of
    seconds between the time that each Route 53 health checker gets a response from
    your endpoint and the time that it sends the next health check request. A health
    checker in each data center around the world sends your endpoint a health check
    request every 30 seconds. On average, your endpoint receives a health check
    request about every two seconds. Health checkers in different data centers don't
    coordinate with one another, so you'll sometimes see several requests per second
    followed by a few seconds with no health checks at all.

    **Health checking regions**

    Health checkers perform checks from all Route 53 health-checking regions. For a
    list of the current regions, see
    [Regions](http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-
    HealthCheckConfig-Regions).

    **Alias records**

    When you register an instance, if you include the `AWS_ALIAS_DNS_NAME`
    attribute, Route 53 creates an alias record. Note the following:

      * Route 53 automatically sets `EvaluateTargetHealth` to true for alias records. When `EvaluateTargetHealth` is true, the alias record inherits the health of the referenced AWS resource. such as an ELB load balancer. For more information, see [EvaluateTargetHealth](http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth).

      * If you include `HealthCheckConfig` and then use the service to register an instance that creates an alias record, Route 53 doesn't create the health check.

    For information about the charges for health checks, see [Route 53
    Pricing](http://aws.amazon.com/route53/pricing).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, HealthCheckType]),
            ),
            (
                "resource_path",
                "ResourcePath",
                TypeInfo(str),
            ),
            (
                "failure_threshold",
                "FailureThreshold",
                TypeInfo(int),
            ),
        ]

    # The type of health check that you want to create, which indicates how Route
    # 53 determines whether an endpoint is healthy.

    # You can't change the value of `Type` after you create a health check.

    # You can create the following types of health checks:

    #   * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.

    #   * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

    # If you specify HTTPS for the value of `Type`, the endpoint must support TLS
    # v1.0 or later.

    #   * **TCP** : Route 53 tries to establish a TCP connection.

    # For more information, see [How Route 53 Determines Whether an Endpoint Is
    # Healthy](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-
    # failover-determining-health-of-endpoints.html) in the _Route 53 Developer
    # Guide_.
    type: typing.Union[str, "HealthCheckType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path that you want Route 53 to request when performing health checks.
    # The path can be any value for which your endpoint will return an HTTP
    # status code of 2xx or 3xx when the endpoint is healthy, such as the file
    # `/docs/route53-health-check.html`. Route 53 automatically adds the DNS name
    # for the service and a leading forward slash (`/`) character.
    resource_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of consecutive health checks that an endpoint must pass or fail
    # for Route 53 to change the current status of the endpoint from unhealthy to
    # healthy or vice versa. For more information, see [How Route 53 Determines
    # Whether an Endpoint Is
    # Healthy](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-
    # failover-determining-health-of-endpoints.html) in the _Route 53 Developer
    # Guide_.
    failure_threshold: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HealthCheckCustomConfig(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failure_threshold",
                "FailureThreshold",
                TypeInfo(int),
            ),
        ]

    failure_threshold: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class HealthCheckType(str):
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"


class HealthStatus(str):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class Instance(ShapeBase):
    """
    A complex type that contains information about an instance that Amazon Route 53
    creates when you submit a `RegisterInstance` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # An identifier that you want to associate with the instance. Note the
    # following:

    #   * If the service that is specified by `ServiceId` includes settings for an SRV record, the value of `InstanceId` is automatically included as part of the value for the SRV record. For more information, see DnsRecord$Type.

    #   * You can use this value to update an existing instance.

    #   * To register a new instance, you must specify a value that is unique among instances that you register by using the same service.

    #   * If you specify an existing `InstanceId` and `ServiceId`, Route 53 updates the existing records. If there's also an existing health check, Route 53 deletes the old health check and creates a new one.

    # The health check isn't deleted immediately, so it will still appear for a
    # while if you submit a `ListHealthChecks` request, for example.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique string that identifies the request and that allows failed
    # `RegisterInstance` requests to be retried without the risk of executing the
    # operation twice. You must use a unique `CreatorRequestId` string every time
    # you submit a `RegisterInstance` request if you're registering additional
    # instances for the same namespace and service. `CreatorRequestId` can be any
    # unique string, for example, a date/time stamp.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string map that contains the following information for the service that
    # you specify in `ServiceId`:

    #   * The attributes that apply to the records that are defined in the service.

    #   * For each attribute, the applicable value.

    # Supported attribute keys include the following:

    # **AWS_ALIAS_DNS_NAME**

    # ****

    # If you want Route 53 to create an alias record that routes traffic to an
    # Elastic Load Balancing load balancer, specify the DNS name that is
    # associated with the load balancer. For information about how to get the DNS
    # name, see "DNSName" in the topic
    # [AliasTarget](http://docs.aws.amazon.com/http:/docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html).

    # Note the following:

    #   * The configuration for the service that is specified by `ServiceId` must include settings for an A record, an AAAA record, or both.

    #   * In the service that is specified by `ServiceId`, the value of `RoutingPolicy` must be `WEIGHTED`.

    #   * If the service that is specified by `ServiceId` includes `HealthCheckConfig` settings, Route 53 will create the health check, but it won't associate the health check with the alias record.

    #   * Auto naming currently doesn't support creating alias records that route traffic to AWS resources other than ELB load balancers.

    #   * If you specify a value for `AWS_ALIAS_DNS_NAME`, don't specify values for any of the `AWS_INSTANCE` attributes.

    # **AWS_INSTANCE_CNAME**

    # If the service configuration includes a CNAME record, the domain name that
    # you want Route 53 to return in response to DNS queries, for example,
    # `example.com`.

    # This value is required if the service specified by `ServiceId` includes
    # settings for an CNAME record.

    # **AWS_INSTANCE_IPV4**

    # If the service configuration includes an A record, the IPv4 address that
    # you want Route 53 to return in response to DNS queries, for example,
    # `192.0.2.44`.

    # This value is required if the service specified by `ServiceId` includes
    # settings for an A record. If the service includes settings for an SRV
    # record, you must specify a value for `AWS_INSTANCE_IPV4`,
    # `AWS_INSTANCE_IPV6`, or both.

    # **AWS_INSTANCE_IPV6**

    # If the service configuration includes an AAAA record, the IPv6 address that
    # you want Route 53 to return in response to DNS queries, for example,
    # `2001:0db8:85a3:0000:0000:abcd:0001:2345`.

    # This value is required if the service specified by `ServiceId` includes
    # settings for an AAAA record. If the service includes settings for an SRV
    # record, you must specify a value for `AWS_INSTANCE_IPV4`,
    # `AWS_INSTANCE_IPV6`, or both.

    # **AWS_INSTANCE_PORT**

    # If the service includes an SRV record, the value that you want Route 53 to
    # return for the port.

    # If the service includes `HealthCheckConfig`, the port on the endpoint that
    # you want Route 53 to send requests to.

    # This value is required if you specified settings for an SRV record when you
    # created the service.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceNotFound(ShapeBase):
    """
    No instance exists with the specified ID, or the instance was recently
    registered, and information about the instance hasn't propagated yet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceSummary(ShapeBase):
    """
    A complex type that contains information about the instances that you registered
    by using a specified service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID for an instance that you created by using a specified service.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string map that contains the following information:

    #   * The attributes that are associate with the instance.

    #   * For each attribute, the applicable value.

    # Supported attribute keys include the following:

    #   * `AWS_ALIAS_DNS_NAME`: For an alias record that routes traffic to an Elastic Load Balancing load balancer, the DNS name that is associated with the load balancer.

    #   * `AWS_INSTANCE_CNAME`: For a CNAME record, the domain name that Route 53 returns in response to DNS queries, for example, `example.com`.

    #   * `AWS_INSTANCE_IPV4`: For an A record, the IPv4 address that Route 53 returns in response to DNS queries, for example, `192.0.2.44`.

    #   * `AWS_INSTANCE_IPV6`: For an AAAA record, the IPv6 address that Route 53 returns in response to DNS queries, for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345`.

    #   * `AWS_INSTANCE_PORT`: For an SRV record, the value that Route 53 returns for the port. In addition, if the service includes `HealthCheckConfig`, the port on the endpoint that Route 53 sends requests to.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidInput(ShapeBase):
    """
    One or more specified values aren't valid. For example, when you're creating a
    namespace, the value of `Name` might not be a valid DNS name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # The ID of the service that you want to list instances for.
    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For the first `ListInstances` request, omit this value.

    # If more than `MaxResults` instances match the specified criteria, you can
    # submit another `ListInstances` request to get the next group of results.
    # Specify the value of `NextToken` from the previous response in the next
    # request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of instances that you want Amazon Route 53 to return in
    # the response to a `ListInstances` request. If you don't specify a value for
    # `MaxResults`, Route 53 returns up to 100 instances.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstancesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[InstanceSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information about the instances that are associated with the
    # specified service.
    instances: typing.List["InstanceSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If more than `MaxResults` instances match the specified criteria, you can
    # submit another `ListInstances` request to get the next group of results.
    # Specify the value of `NextToken` from the previous response in the next
    # request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListInstancesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListNamespacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[NamespaceFilter]),
            ),
        ]

    # For the first `ListNamespaces` request, omit this value.

    # If the response contains `NextToken`, submit another `ListNamespaces`
    # request to get the next group of results. Specify the value of `NextToken`
    # from the previous response in the next request.

    # Route 53 gets `MaxResults` namespaces and then filters them based on the
    # specified criteria. It's possible that no namespaces in the first
    # `MaxResults` namespaces matched the specified criteria but that subsequent
    # groups of `MaxResults` namespaces do contain namespaces that match the
    # criteria.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of namespaces that you want Amazon Route 53 to return in
    # the response to a `ListNamespaces` request. If you don't specify a value
    # for `MaxResults`, Route 53 returns up to 100 namespaces.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains specifications for the namespaces that you
    # want to list.

    # If you specify more than one filter, a namespace must match all filters to
    # be returned by `ListNamespaces`.
    filters: typing.List["NamespaceFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListNamespacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "namespaces",
                "Namespaces",
                TypeInfo(typing.List[NamespaceSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array that contains one `NamespaceSummary` object for each namespace
    # that matches the specified filter criteria.
    namespaces: typing.List["NamespaceSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response contains `NextToken`, submit another `ListNamespaces`
    # request to get the next group of results. Specify the value of `NextToken`
    # from the previous response in the next request.

    # Route 53 gets `MaxResults` namespaces and then filters them based on the
    # specified criteria. It's possible that no namespaces in the first
    # `MaxResults` namespaces matched the specified criteria but that subsequent
    # groups of `MaxResults` namespaces do contain namespaces that match the
    # criteria.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListNamespacesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOperationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[OperationFilter]),
            ),
        ]

    # For the first `ListOperations` request, omit this value.

    # If the response contains `NextToken`, submit another `ListOperations`
    # request to get the next group of results. Specify the value of `NextToken`
    # from the previous response in the next request.

    # Route 53 gets `MaxResults` operations and then filters them based on the
    # specified criteria. It's possible that no operations in the first
    # `MaxResults` operations matched the specified criteria but that subsequent
    # groups of `MaxResults` operations do contain operations that match the
    # criteria.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items that you want Amazon Route 53 to return in the
    # response to a `ListOperations` request. If you don't specify a value for
    # `MaxResults`, Route 53 returns up to 100 operations.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains specifications for the operations that you
    # want to list, for example, operations that you started between a specified
    # start date and end date.

    # If you specify more than one filter, an operation must match all filters to
    # be returned by `ListOperations`.
    filters: typing.List["OperationFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListOperationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "Operations",
                TypeInfo(typing.List[OperationSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information about the operations that match the specified criteria.
    operations: typing.List["OperationSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response contains `NextToken`, submit another `ListOperations`
    # request to get the next group of results. Specify the value of `NextToken`
    # from the previous response in the next request.

    # Route 53 gets `MaxResults` operations and then filters them based on the
    # specified criteria. It's possible that no operations in the first
    # `MaxResults` operations matched the specified criteria but that subsequent
    # groups of `MaxResults` operations do contain operations that match the
    # criteria.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListOperationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListServicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[ServiceFilter]),
            ),
        ]

    # For the first `ListServices` request, omit this value.

    # If the response contains `NextToken`, submit another `ListServices` request
    # to get the next group of results. Specify the value of `NextToken` from the
    # previous response in the next request.

    # Route 53 gets `MaxResults` services and then filters them based on the
    # specified criteria. It's possible that no services in the first
    # `MaxResults` services matched the specified criteria but that subsequent
    # groups of `MaxResults` services do contain services that match the
    # criteria.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of services that you want Amazon Route 53 to return in
    # the response to a `ListServices` request. If you don't specify a value for
    # `MaxResults`, Route 53 returns up to 100 services.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains specifications for the namespaces that you
    # want to list services for.

    # If you specify more than one filter, an operation must match all filters to
    # be returned by `ListServices`.
    filters: typing.List["ServiceFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListServicesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "services",
                "Services",
                TypeInfo(typing.List[ServiceSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array that contains one `ServiceSummary` object for each service that
    # matches the specified filter criteria.
    services: typing.List["ServiceSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response contains `NextToken`, submit another `ListServices` request
    # to get the next group of results. Specify the value of `NextToken` from the
    # previous response in the next request.

    # Route 53 gets `MaxResults` services and then filters them based on the
    # specified criteria. It's possible that no services in the first
    # `MaxResults` services matched the specified criteria but that subsequent
    # groups of `MaxResults` services do contain services that match the
    # criteria.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListServicesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Namespace(ShapeBase):
    """
    A complex type that contains information about a specified namespace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, NamespaceType]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "service_count",
                "ServiceCount",
                TypeInfo(int),
            ),
            (
                "properties",
                "Properties",
                TypeInfo(NamespaceProperties),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
        ]

    # The ID of a namespace.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that Route 53 assigns to the namespace when
    # you create it.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the namespace, such as `example.com`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the namespace. Valid values are `DNS_PUBLIC` and `DNS_PRIVATE`.
    type: typing.Union[str, "NamespaceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description that you specify for the namespace when you create it.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of services that are associated with the namespace.
    service_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information that's specific to the type of the
    # namespace.
    properties: "NamespaceProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the namespace was created, in Unix date/time format and
    # Coordinated Universal Time (UTC). The value of `CreateDate` is accurate to
    # milliseconds. For example, the value `1516925490.087` represents Friday,
    # January 26, 2018 12:11:30.087 AM.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique string that identifies the request and that allows failed requests
    # to be retried without the risk of executing an operation twice.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NamespaceAlreadyExists(ShapeBase):
    """
    The namespace that you're trying to create already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "namespace_id",
                "NamespaceId",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `CreatorRequestId` that was used to create the namespace.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the existing namespace.
    namespace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NamespaceFilter(ShapeBase):
    """
    A complex type that identifies the namespaces that you want to list. You can
    choose to list public or private namespaces.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, NamespaceFilterName]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "Condition",
                TypeInfo(typing.Union[str, FilterCondition]),
            ),
        ]

    # Specify `TYPE`.
    name: typing.Union[str, "NamespaceFilterName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you specify `EQ` for `Condition`, specify either `DNS_PUBLIC` or
    # `DNS_PRIVATE`.

    # If you specify `IN` for `Condition`, you can specify `DNS_PUBLIC`,
    # `DNS_PRIVATE`, or both.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operator that you want to use to determine whether `ListNamespaces`
    # returns a namespace. Valid values for `condition` include:

    #   * `EQ`: When you specify `EQ` for the condition, you can choose to list only public namespaces or private namespaces, but not both. `EQ` is the default condition and can be omitted.

    #   * `IN`: When you specify `IN` for the condition, you can choose to list public namespaces, private namespaces, or both.

    #   * `BETWEEN`: Not applicable
    condition: typing.Union[str, "FilterCondition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class NamespaceFilterName(str):
    TYPE = "TYPE"


@dataclasses.dataclass
class NamespaceNotFound(ShapeBase):
    """
    No namespace exists with the specified ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NamespaceProperties(ShapeBase):
    """
    A complex type that contains information that is specific to the namespace type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dns_properties",
                "DnsProperties",
                TypeInfo(DnsProperties),
            ),
        ]

    # A complex type that contains the ID for the hosted zone that Route 53
    # creates when you create a namespace.
    dns_properties: "DnsProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NamespaceSummary(ShapeBase):
    """
    A complex type that contains information about a namespace.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, NamespaceType]),
            ),
        ]

    # The ID of the namespace.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that Route 53 assigns to the namespace when
    # you create it.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the namespace. When you create a namespace, Route 53
    # automatically creates a hosted zone that has the same name as the
    # namespace.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the namespace, either public or private.
    type: typing.Union[str, "NamespaceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class NamespaceType(str):
    DNS_PUBLIC = "DNS_PUBLIC"
    DNS_PRIVATE = "DNS_PRIVATE"


@dataclasses.dataclass
class Operation(ShapeBase):
    """
    A complex type that contains information about a specified operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, OperationType]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, OperationStatus]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "update_date",
                "UpdateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(
                    typing.Dict[typing.Union[str, OperationTargetType], str]
                ),
            ),
        ]

    # The ID of the operation that you want to get information about.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the operation that is associated with the specified ID.
    type: typing.Union[str, "OperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the operation. Values include the following:

    #   * **SUBMITTED** : This is the initial state immediately after you submit a request.

    #   * **PENDING** : Route 53 is performing the operation.

    #   * **SUCCESS** : The operation succeeded.

    #   * **FAIL** : The operation failed. For the failure reason, see `ErrorMessage`.
    status: typing.Union[str, "OperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the value of `Status` is `FAIL`, the reason that the operation failed.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code associated with `ErrorMessage`. Values for `ErrorCode` include the
    # following:

    #   * `ACCESS_DENIED`

    #   * `CANNOT_CREATE_HOSTED_ZONE`

    #   * `EXPIRED_TOKEN`

    #   * `HOSTED_ZONE_NOT_FOUND`

    #   * `INTERNAL_FAILURE`

    #   * `INVALID_CHANGE_BATCH`

    #   * `THROTTLED_REQUEST`
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the request was submitted, in Unix date/time format
    # and Coordinated Universal Time (UTC). The value of `CreateDate` is accurate
    # to milliseconds. For example, the value `1516925490.087` represents Friday,
    # January 26, 2018 12:11:30.087 AM.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the value of `Status` changed to the current value,
    # in Unix date/time format and Coordinated Universal Time (UTC). The value of
    # `UpdateDate` is accurate to milliseconds. For example, the value
    # `1516925490.087` represents Friday, January 26, 2018 12:11:30.087 AM.
    update_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the target entity that is associated with the operation:

    #   * **NAMESPACE** : The namespace ID is returned in the `ResourceId` property.

    #   * **SERVICE** : The service ID is returned in the `ResourceId` property.

    #   * **INSTANCE** : The instance ID is returned in the `ResourceId` property.
    targets: typing.Dict[typing.Union[str, "OperationTargetType"], str
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


@dataclasses.dataclass
class OperationFilter(ShapeBase):
    """
    A complex type that lets you select the operations that you want to list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, OperationFilterName]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "Condition",
                TypeInfo(typing.Union[str, FilterCondition]),
            ),
        ]

    # Specify the operations that you want to get:

    #   * **NAMESPACE_ID** : Gets operations related to specified namespaces.

    #   * **SERVICE_ID** : Gets operations related to specified services.

    #   * **STATUS** : Gets operations based on the status of the operations: `SUBMITTED`, `PENDING`, `SUCCEED`, or `FAIL`.

    #   * **TYPE** : Gets specified types of operation.

    #   * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.
    name: typing.Union[str, "OperationFilterName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify values that are applicable to the value that you specify for
    # `Name`:

    #   * **NAMESPACE_ID** : Specify one namespace ID.

    #   * **SERVICE_ID** : Specify one service ID.

    #   * **STATUS** : Specify one or more statuses: `SUBMITTED`, `PENDING`, `SUCCEED`, or `FAIL`.

    #   * **TYPE** : Specify one or more of the following types: `CREATE_NAMESPACE`, `DELETE_NAMESPACE`, `UPDATE_SERVICE`, `REGISTER_INSTANCE`, or `DEREGISTER_INSTANCE`.

    #   * **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operator that you want to use to determine whether an operation matches
    # the specified value. Valid values for condition include:

    #   * `EQ`: When you specify `EQ` for the condition, you can specify only one value. `EQ` is supported for `NAMESPACE_ID`, `SERVICE_ID`, `STATUS`, and `TYPE`. `EQ` is the default condition and can be omitted.

    #   * `IN`: When you specify `IN` for the condition, you can specify a list of one or more values. `IN` is supported for `STATUS` and `TYPE`. An operation must match one of the specified values to be returned in the response.

    #   * `BETWEEN`: Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. `BETWEEN` is supported for `UPDATE_DATE`.
    condition: typing.Union[str, "FilterCondition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class OperationFilterName(str):
    NAMESPACE_ID = "NAMESPACE_ID"
    SERVICE_ID = "SERVICE_ID"
    STATUS = "STATUS"
    TYPE = "TYPE"
    UPDATE_DATE = "UPDATE_DATE"


@dataclasses.dataclass
class OperationNotFound(ShapeBase):
    """
    No operation exists with the specified ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OperationStatus(str):
    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


@dataclasses.dataclass
class OperationSummary(ShapeBase):
    """
    A complex type that contains information about an operation that matches the
    criteria that you specified in a ListOperations request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, OperationStatus]),
            ),
        ]

    # The ID for an operation.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the operation. Values include the following:

    #   * **SUBMITTED** : This is the initial state immediately after you submit a request.

    #   * **PENDING** : Route 53 is performing the operation.

    #   * **SUCCESS** : The operation succeeded.

    #   * **FAIL** : The operation failed. For the failure reason, see `ErrorMessage`.
    status: typing.Union[str, "OperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class OperationTargetType(str):
    NAMESPACE = "NAMESPACE"
    SERVICE = "SERVICE"
    INSTANCE = "INSTANCE"


class OperationType(str):
    CREATE_NAMESPACE = "CREATE_NAMESPACE"
    DELETE_NAMESPACE = "DELETE_NAMESPACE"
    UPDATE_SERVICE = "UPDATE_SERVICE"
    REGISTER_INSTANCE = "REGISTER_INSTANCE"
    DEREGISTER_INSTANCE = "DEREGISTER_INSTANCE"


class RecordType(str):
    SRV = "SRV"
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"


@dataclasses.dataclass
class RegisterInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
        ]

    # The ID of the service that you want to use for settings for the records and
    # health check that Route 53 will create.
    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that you want to associate with the instance. Note the
    # following:

    #   * If the service that is specified by `ServiceId` includes settings for an SRV record, the value of `InstanceId` is automatically included as part of the value for the SRV record. For more information, see DnsRecord$Type.

    #   * You can use this value to update an existing instance.

    #   * To register a new instance, you must specify a value that is unique among instances that you register by using the same service.

    #   * If you specify an existing `InstanceId` and `ServiceId`, Route 53 updates the existing records. If there's also an existing health check, Route 53 deletes the old health check and creates a new one.

    # The health check isn't deleted immediately, so it will still appear for a
    # while if you submit a `ListHealthChecks` request, for example.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string map that contains the following information for the service that
    # you specify in `ServiceId`:

    #   * The attributes that apply to the records that are defined in the service.

    #   * For each attribute, the applicable value.

    # Supported attribute keys include the following:

    # **AWS_ALIAS_DNS_NAME**

    # ****

    # If you want Route 53 to create an alias record that routes traffic to an
    # Elastic Load Balancing load balancer, specify the DNS name that is
    # associated with the load balancer. For information about how to get the DNS
    # name, see "DNSName" in the topic
    # [AliasTarget](http://docs.aws.amazon.com/http:/docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html).

    # Note the following:

    #   * The configuration for the service that is specified by `ServiceId` must include settings for an A record, an AAAA record, or both.

    #   * In the service that is specified by `ServiceId`, the value of `RoutingPolicy` must be `WEIGHTED`.

    #   * If the service that is specified by `ServiceId` includes `HealthCheckConfig` settings, Route 53 will create the health check, but it won't associate the health check with the alias record.

    #   * Auto naming currently doesn't support creating alias records that route traffic to AWS resources other than ELB load balancers.

    #   * If you specify a value for `AWS_ALIAS_DNS_NAME`, don't specify values for any of the `AWS_INSTANCE` attributes.

    # **AWS_INSTANCE_CNAME**

    # If the service configuration includes a CNAME record, the domain name that
    # you want Route 53 to return in response to DNS queries, for example,
    # `example.com`.

    # This value is required if the service specified by `ServiceId` includes
    # settings for an CNAME record.

    # **AWS_INSTANCE_IPV4**

    # If the service configuration includes an A record, the IPv4 address that
    # you want Route 53 to return in response to DNS queries, for example,
    # `192.0.2.44`.

    # This value is required if the service specified by `ServiceId` includes
    # settings for an A record. If the service includes settings for an SRV
    # record, you must specify a value for `AWS_INSTANCE_IPV4`,
    # `AWS_INSTANCE_IPV6`, or both.

    # **AWS_INSTANCE_IPV6**

    # If the service configuration includes an AAAA record, the IPv6 address that
    # you want Route 53 to return in response to DNS queries, for example,
    # `2001:0db8:85a3:0000:0000:abcd:0001:2345`.

    # This value is required if the service specified by `ServiceId` includes
    # settings for an AAAA record. If the service includes settings for an SRV
    # record, you must specify a value for `AWS_INSTANCE_IPV4`,
    # `AWS_INSTANCE_IPV6`, or both.

    # **AWS_INSTANCE_PORT**

    # If the service includes an SRV record, the value that you want Route 53 to
    # return for the port.

    # If the service includes `HealthCheckConfig`, the port on the endpoint that
    # you want Route 53 to send requests to.

    # This value is required if you specified settings for an SRV record when you
    # created the service.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique string that identifies the request and that allows failed
    # `RegisterInstance` requests to be retried without the risk of executing the
    # operation twice. You must use a unique `CreatorRequestId` string every time
    # you submit a `RegisterInstance` request if you're registering additional
    # instances for the same namespace and service. `CreatorRequestId` can be any
    # unique string, for example, a date/time stamp.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterInstanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that you can use to determine whether the request completed
    # successfully. To get the status of the operation, see GetOperation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceInUse(ShapeBase):
    """
    The specified resource can't be deleted because it contains other resources. For
    example, you can't delete a service that contains any instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceLimitExceeded(ShapeBase):
    """
    The resource can't be created because you've reached the limit on the number of
    resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RoutingPolicy(str):
    MULTIVALUE = "MULTIVALUE"
    WEIGHTED = "WEIGHTED"


@dataclasses.dataclass
class Service(ShapeBase):
    """
    A complex type that contains information about the specified service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "dns_config",
                "DnsConfig",
                TypeInfo(DnsConfig),
            ),
            (
                "health_check_config",
                "HealthCheckConfig",
                TypeInfo(HealthCheckConfig),
            ),
            (
                "health_check_custom_config",
                "HealthCheckCustomConfig",
                TypeInfo(HealthCheckCustomConfig),
            ),
            (
                "create_date",
                "CreateDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
        ]

    # The ID that Route 53 assigned to the service when you created it.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that Route 53 assigns to the service when
    # you create it.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the service.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the service.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances that are currently associated with the service.
    # Instances that were previously associated with the service but that have
    # been deleted are not included in the count.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about the records that you want
    # Route 53 to create when you register an instance.
    dns_config: "DnsConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # _Public DNS namespaces only._ A complex type that contains settings for an
    # optional health check. If you specify settings for a health check, Route 53
    # associates the health check with all the records that you specify in
    # `DnsConfig`.

    # For information about the charges for health checks, see [Route 53
    # Pricing](http://aws.amazon.com/route53/pricing).
    health_check_config: "HealthCheckConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    health_check_custom_config: "HealthCheckCustomConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the service was created, in Unix format and
    # Coordinated Universal Time (UTC). The value of `CreateDate` is accurate to
    # milliseconds. For example, the value `1516925490.087` represents Friday,
    # January 26, 2018 12:11:30.087 AM.
    create_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique string that identifies the request and that allows failed requests
    # to be retried without the risk of executing the operation twice.
    # `CreatorRequestId` can be any unique string, for example, a date/time
    # stamp.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceAlreadyExists(ShapeBase):
    """
    The service can't be created because a service with the same name already
    exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "creator_request_id",
                "CreatorRequestId",
                TypeInfo(str),
            ),
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `CreatorRequestId` that was used to create the service.
    creator_request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the existing service.
    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceChange(ShapeBase):
    """
    A complex type that contains changes to an existing service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dns_config",
                "DnsConfig",
                TypeInfo(DnsConfigChange),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "health_check_config",
                "HealthCheckConfig",
                TypeInfo(HealthCheckConfig),
            ),
        ]

    # A complex type that contains information about the records that you want
    # Route 53 to create when you register an instance.
    dns_config: "DnsConfigChange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the service.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # _Public DNS namespaces only._ A complex type that contains settings for an
    # optional health check. If you specify settings for a health check, Amazon
    # Route 53 associates the health check with all the records that you specify
    # in `DnsConfig`.

    # **A and AAAA records**

    # If `DnsConfig` includes configurations for both A and AAAA records, Route
    # 53 creates a health check that uses the IPv4 address to check the health of
    # the resource. If the endpoint that is specified by the IPv4 address is
    # unhealthy, Route 53 considers both the A and AAAA records to be unhealthy.

    # **CNAME records**

    # You can't specify settings for `HealthCheckConfig` when the `DNSConfig`
    # includes `CNAME` for the value of `Type`. If you do, the `CreateService`
    # request will fail with an `InvalidInput` error.

    # **Request interval**

    # The health check uses 30 seconds as the request interval. This is the
    # number of seconds between the time that each Route 53 health checker gets a
    # response from your endpoint and the time that it sends the next health
    # check request. A health checker in each data center around the world sends
    # your endpoint a health check request every 30 seconds. On average, your
    # endpoint receives a health check request about every two seconds. Health
    # checkers in different data centers don't coordinate with one another, so
    # you'll sometimes see several requests per second followed by a few seconds
    # with no health checks at all.

    # **Health checking regions**

    # Health checkers perform checks from all Route 53 health-checking regions.
    # For a list of the current regions, see
    # [Regions](http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-
    # HealthCheckConfig-Regions).

    # **Alias records**

    # When you register an instance, if you include the `AWS_ALIAS_DNS_NAME`
    # attribute, Route 53 creates an alias record. Note the following:

    #   * Route 53 automatically sets `EvaluateTargetHealth` to true for alias records. When `EvaluateTargetHealth` is true, the alias record inherits the health of the referenced AWS resource. such as an ELB load balancer. For more information, see [EvaluateTargetHealth](http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth).

    #   * If you include `HealthCheckConfig` and then use the service to register an instance that creates an alias record, Route 53 doesn't create the health check.

    # For information about the charges for health checks, see [Route 53
    # Pricing](http://aws.amazon.com/route53/pricing).
    health_check_config: "HealthCheckConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceFilter(ShapeBase):
    """
    A complex type that lets you specify the namespaces that you want to list
    services for.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, ServiceFilterName]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
            (
                "condition",
                "Condition",
                TypeInfo(typing.Union[str, FilterCondition]),
            ),
        ]

    # Specify `NAMESPACE_ID`.
    name: typing.Union[str, "ServiceFilterName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The values that are applicable to the value that you specify for
    # `Condition` to filter the list of services.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operator that you want to use to determine whether a service is
    # returned by `ListServices`. Valid values for `Condition` include the
    # following:

    #   * `EQ`: When you specify `EQ`, specify one namespace ID for `Values`. `EQ` is the default condition and can be omitted.

    #   * `IN`: When you specify `IN`, specify a list of the IDs for the namespaces that you want `ListServices` to return a list of services for.

    #   * `BETWEEN`: Not applicable.
    condition: typing.Union[str, "FilterCondition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ServiceFilterName(str):
    NAMESPACE_ID = "NAMESPACE_ID"


@dataclasses.dataclass
class ServiceNotFound(ShapeBase):
    """
    No service exists with the specified ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceSummary(ShapeBase):
    """
    A complex type that contains information about a specified service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
        ]

    # The ID that Route 53 assigned to the service when you created it.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that Route 53 assigns to the service when
    # you create it.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the service.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description that you specify when you create the service.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances that are currently associated with the service.
    # Instances that were previously associated with the service but that have
    # been deleted are not included in the count.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInstanceCustomHealthStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_id",
                "ServiceId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CustomHealthStatus]),
            ),
        ]

    service_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    status: typing.Union[str, "CustomHealthStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "service",
                "Service",
                TypeInfo(ServiceChange),
            ),
        ]

    # The ID of the service that you want to update.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains the new settings for the service.
    service: "ServiceChange" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that you can use to determine whether the request completed
    # successfully. To get the status of the operation, see GetOperation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
