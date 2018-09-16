import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessLog(ShapeBase):
    """
    Information about the `AccessLog` attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "emit_interval",
                "EmitInterval",
                TypeInfo(int),
            ),
            (
                "s3_bucket_prefix",
                "S3BucketPrefix",
                TypeInfo(str),
            ),
        ]

    # Specifies whether access logs are enabled for the load balancer.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon S3 bucket where the access logs are stored.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval for publishing the access logs. You can specify an interval of
    # either 5 minutes or 60 minutes.

    # Default: 60 minutes
    emit_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The logical hierarchy you created for your Amazon S3 bucket, for example
    # `my-bucket-prefix/prod`. If the prefix is not provided, the log is placed
    # at the root level of the bucket.
    s3_bucket_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AccessPointNotFoundException(ShapeBase):
    """
    The specified load balancer does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AddAvailabilityZonesInput(ShapeBase):
    """
    Contains the parameters for EnableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zones. These must be in the same region as the load
    # balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddAvailabilityZonesOutput(OutputShapeBase):
    """
    Contains the output of EnableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated list of Availability Zones for the load balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsInput(ShapeBase):
    """
    Contains the parameters for AddTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the load balancer. You can specify one load balancer only.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsOutput(OutputShapeBase):
    """
    Contains the output of AddTags.
    """

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
class AdditionalAttribute(ShapeBase):
    """
    This data type is reserved.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # This parameter is reserved.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is reserved.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AppCookieStickinessPolicy(ShapeBase):
    """
    Information about a policy for application-controlled session stickiness.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "cookie_name",
                "CookieName",
                TypeInfo(str),
            ),
        ]

    # The mnemonic name for the policy being created. The name must be unique
    # within a set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application cookie used for stickiness.
    cookie_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplySecurityGroupsToLoadBalancerInput(ShapeBase):
    """
    Contains the parameters for ApplySecurityGroupsToLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the security groups to associate with the load balancer. Note
    # that you cannot specify the name of the security group.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApplySecurityGroupsToLoadBalancerOutput(OutputShapeBase):
    """
    Contains the output of ApplySecurityGroupsToLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the security groups associated with the load balancer.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachLoadBalancerToSubnetsInput(ShapeBase):
    """
    Contains the parameters for AttachLoaBalancerToSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the subnets to add. You can add only one subnet per Availability
    # Zone.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachLoadBalancerToSubnetsOutput(OutputShapeBase):
    """
    Contains the output of AttachLoadBalancerToSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the subnets attached to the load balancer.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BackendServerDescription(ShapeBase):
    """
    Information about the configuration of an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_port",
                "InstancePort",
                TypeInfo(int),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The port on which the EC2 instance is listening.
    instance_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the policies enabled for the EC2 instance.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CertificateNotFoundException(ShapeBase):
    """
    The specified ARN does not refer to a valid SSL certificate in AWS Identity and
    Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you
    recently uploaded the certificate to IAM, this error might indicate that the
    certificate is not fully available yet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ConfigureHealthCheckInput(ShapeBase):
    """
    Contains the parameters for ConfigureHealthCheck.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "health_check",
                "HealthCheck",
                TypeInfo(HealthCheck),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration information.
    health_check: "HealthCheck" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfigureHealthCheckOutput(OutputShapeBase):
    """
    Contains the output of ConfigureHealthCheck.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "health_check",
                "HealthCheck",
                TypeInfo(HealthCheck),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated health check.
    health_check: "HealthCheck" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConnectionDraining(ShapeBase):
    """
    Information about the `ConnectionDraining` attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
        ]

    # Specifies whether connection draining is enabled for the load balancer.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time, in seconds, to keep the existing connections open before
    # deregistering the instances.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConnectionSettings(ShapeBase):
    """
    Information about the `ConnectionSettings` attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "idle_timeout",
                "IdleTimeout",
                TypeInfo(int),
            ),
        ]

    # The time, in seconds, that the connection is allowed to be idle (no data
    # has been sent over the connection) before it is closed by the load
    # balancer.
    idle_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAccessPointInput(ShapeBase):
    """
    Contains the parameters for CreateLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "listeners",
                "Listeners",
                TypeInfo(typing.List[Listener]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "scheme",
                "Scheme",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the load balancer.

    # This name must be unique within your set of load balancers for the region,
    # must have a maximum of 32 characters, must contain only alphanumeric
    # characters or hyphens, and cannot begin or end with a hyphen.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The listeners.

    # For more information, see [Listeners for Your Classic Load
    # Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
    # listener-config.html) in the _Classic Load Balancers Guide_.
    listeners: typing.List["Listener"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more Availability Zones from the same region as the load balancer.

    # You must specify at least one Availability Zone.

    # You can add more Availability Zones after you create the load balancer
    # using EnableAvailabilityZonesForLoadBalancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the subnets in your VPC to attach to the load balancer. Specify
    # one subnet per Availability Zone specified in `AvailabilityZones`.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the security groups to assign to the load balancer.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of a load balancer. Valid only for load balancers in a VPC.

    # By default, Elastic Load Balancing creates an Internet-facing load balancer
    # with a DNS name that resolves to public IP addresses. For more information
    # about Internet-facing and Internal load balancers, see [Load Balancer
    # Scheme](http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-
    # elastic-load-balancing-works.html#load-balancer-scheme) in the _Elastic
    # Load Balancing User Guide_.

    # Specify `internal` to create a load balancer with a DNS name that resolves
    # to private IP addresses.
    scheme: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to assign to the load balancer.

    # For more information about tagging your load balancer, see [Tag Your
    # Classic Load
    # Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-
    # remove-tags.html) in the _Classic Load Balancers Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAccessPointOutput(OutputShapeBase):
    """
    Contains the output for CreateLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dns_name",
                "DNSName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DNS name of the load balancer.
    dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAppCookieStickinessPolicyInput(ShapeBase):
    """
    Contains the parameters for CreateAppCookieStickinessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "cookie_name",
                "CookieName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy being created. Policy names must consist of
    # alphanumeric characters and dashes (-). This name must be unique within the
    # set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application cookie used for stickiness.
    cookie_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAppCookieStickinessPolicyOutput(OutputShapeBase):
    """
    Contains the output for CreateAppCookieStickinessPolicy.
    """

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
class CreateLBCookieStickinessPolicyInput(ShapeBase):
    """
    Contains the parameters for CreateLBCookieStickinessPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "cookie_expiration_period",
                "CookieExpirationPeriod",
                TypeInfo(int),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy being created. Policy names must consist of
    # alphanumeric characters and dashes (-). This name must be unique within the
    # set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time period, in seconds, after which the cookie should be considered
    # stale. If you do not specify this parameter, the default value is 0, which
    # indicates that the sticky session should last for the duration of the
    # browser session.
    cookie_expiration_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLBCookieStickinessPolicyOutput(OutputShapeBase):
    """
    Contains the output for CreateLBCookieStickinessPolicy.
    """

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
class CreateLoadBalancerListenerInput(ShapeBase):
    """
    Contains the parameters for CreateLoadBalancerListeners.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "listeners",
                "Listeners",
                TypeInfo(typing.List[Listener]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The listeners.
    listeners: typing.List["Listener"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerListenerOutput(OutputShapeBase):
    """
    Contains the parameters for CreateLoadBalancerListener.
    """

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
class CreateLoadBalancerPolicyInput(ShapeBase):
    """
    Contains the parameters for CreateLoadBalancerPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_type_name",
                "PolicyTypeName",
                TypeInfo(str),
            ),
            (
                "policy_attributes",
                "PolicyAttributes",
                TypeInfo(typing.List[PolicyAttribute]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the load balancer policy to be created. This name must be
    # unique within the set of policies for this load balancer.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the base policy type. To get the list of policy types, use
    # DescribeLoadBalancerPolicyTypes.
    policy_type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy attributes.
    policy_attributes: typing.List["PolicyAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerPolicyOutput(OutputShapeBase):
    """
    Contains the output of CreateLoadBalancerPolicy.
    """

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
class CrossZoneLoadBalancing(ShapeBase):
    """
    Information about the `CrossZoneLoadBalancing` attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # Specifies whether cross-zone load balancing is enabled for the load
    # balancer.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAccessPointInput(ShapeBase):
    """
    Contains the parameters for DeleteLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAccessPointOutput(OutputShapeBase):
    """
    Contains the output of DeleteLoadBalancer.
    """

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
class DeleteLoadBalancerListenerInput(ShapeBase):
    """
    Contains the parameters for DeleteLoadBalancerListeners.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "load_balancer_ports",
                "LoadBalancerPorts",
                TypeInfo(typing.List[int]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The client port numbers of the listeners.
    load_balancer_ports: typing.List[int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLoadBalancerListenerOutput(OutputShapeBase):
    """
    Contains the output of DeleteLoadBalancerListeners.
    """

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
class DeleteLoadBalancerPolicyInput(ShapeBase):
    """
    Contains the parameters for DeleteLoadBalancerPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerPolicyOutput(OutputShapeBase):
    """
    Contains the output of DeleteLoadBalancerPolicy.
    """

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
class DependencyThrottleException(ShapeBase):
    """
    A request made by Elastic Load Balancing to another service exceeds the maximum
    request rate permitted for your account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeregisterEndPointsInput(ShapeBase):
    """
    Contains the parameters for DeregisterInstancesFromLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterEndPointsOutput(OutputShapeBase):
    """
    Contains the output of DeregisterInstancesFromLoadBalancer.
    """

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
                TypeInfo(typing.List[Instance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The remaining instances registered with the load balancer.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAccessPointsInput(ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
        ]

    # The names of the load balancers.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call (a number from 1 to
    # 400). The default is 400.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccessPointsOutput(OutputShapeBase):
    """
    Contains the parameters for DescribeLoadBalancers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancer_descriptions",
                "LoadBalancerDescriptions",
                TypeInfo(typing.List[LoadBalancerDescription]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancers.
    load_balancer_descriptions: typing.List["LoadBalancerDescription"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeAccessPointsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeAccountLimitsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
        ]

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccountLimitsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "limits",
                "Limits",
                TypeInfo(typing.List[Limit]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the limits.
    limits: typing.List["Limit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndPointStateInput(ShapeBase):
    """
    Contains the parameters for DescribeInstanceHealth.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEndPointStateOutput(OutputShapeBase):
    """
    Contains the output for DescribeInstanceHealth.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_states",
                "InstanceStates",
                TypeInfo(typing.List[InstanceState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the health of the instances.
    instance_states: typing.List["InstanceState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerAttributesInput(ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoadBalancerAttributesOutput(OutputShapeBase):
    """
    Contains the output of DescribeLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancer_attributes",
                "LoadBalancerAttributes",
                TypeInfo(LoadBalancerAttributes),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer attributes.
    load_balancer_attributes: "LoadBalancerAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPoliciesInput(ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancerPolicies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the policies.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPoliciesOutput(OutputShapeBase):
    """
    Contains the output of DescribeLoadBalancerPolicies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy_descriptions",
                "PolicyDescriptions",
                TypeInfo(typing.List[PolicyDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the policies.
    policy_descriptions: typing.List["PolicyDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPolicyTypesInput(ShapeBase):
    """
    Contains the parameters for DescribeLoadBalancerPolicyTypes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_type_names",
                "PolicyTypeNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the policy types. If no names are specified, describes all
    # policy types defined by Elastic Load Balancing.
    policy_type_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerPolicyTypesOutput(OutputShapeBase):
    """
    Contains the output of DescribeLoadBalancerPolicyTypes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy_type_descriptions",
                "PolicyTypeDescriptions",
                TypeInfo(typing.List[PolicyTypeDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the policy types.
    policy_type_descriptions: typing.List["PolicyTypeDescription"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class DescribeTagsInput(ShapeBase):
    """
    Contains the parameters for DescribeTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the load balancers.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTagsOutput(OutputShapeBase):
    """
    Contains the output for DescribeTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_descriptions",
                "TagDescriptions",
                TypeInfo(typing.List[TagDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags.
    tag_descriptions: typing.List["TagDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachLoadBalancerFromSubnetsInput(ShapeBase):
    """
    Contains the parameters for DetachLoadBalancerFromSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the subnets.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachLoadBalancerFromSubnetsOutput(OutputShapeBase):
    """
    Contains the output of DetachLoadBalancerFromSubnets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the remaining subnets for the load balancer.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateAccessPointNameException(ShapeBase):
    """
    The specified load balancer name already exists for this account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicateListenerException(ShapeBase):
    """
    A listener already exists for the specified load balancer name and port, but
    with a different instance port, protocol, or SSL certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicatePolicyNameException(ShapeBase):
    """
    A policy with the specified name already exists for this load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicateTagKeysException(ShapeBase):
    """
    A tag key was specified more than once.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HealthCheck(ShapeBase):
    """
    Information about a health check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
            (
                "interval",
                "Interval",
                TypeInfo(int),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "unhealthy_threshold",
                "UnhealthyThreshold",
                TypeInfo(int),
            ),
            (
                "healthy_threshold",
                "HealthyThreshold",
                TypeInfo(int),
            ),
        ]

    # The instance being checked. The protocol is either TCP, HTTP, HTTPS, or
    # SSL. The range of valid ports is one (1) through 65535.

    # TCP is the default, specified as a TCP: port pair, for example "TCP:5000".
    # In this case, a health check simply attempts to open a TCP connection to
    # the instance on the specified port. Failure to connect within the
    # configured timeout is considered unhealthy.

    # SSL is also specified as SSL: port pair, for example, SSL:5000.

    # For HTTP/HTTPS, you must include a ping path in the string. HTTP is
    # specified as a HTTP:port;/;PathToPing; grouping, for example
    # "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued
    # to the instance on the given port and path. Any answer other than "200 OK"
    # within the timeout period is considered unhealthy.

    # The total length of the HTTP ping target must be 1024 16-bit Unicode
    # characters or less.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate interval, in seconds, between health checks of an
    # individual instance.
    interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, during which no response means a failed
    # health check.

    # This value must be less than the `Interval` value.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of consecutive health check failures required before moving the
    # instance to the `Unhealthy` state.
    unhealthy_threshold: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of consecutive health checks successes required before moving
    # the instance to the `Healthy` state.
    healthy_threshold: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Instance(ShapeBase):
    """
    The ID of an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceState(ShapeBase):
    """
    Information about the state of an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "reason_code",
                "ReasonCode",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the instance.

    # Valid values: `InService` | `OutOfService` | `Unknown`
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the cause of `OutOfService` instances. Specifically,
    # whether the cause is Elastic Load Balancing or the instance.

    # Valid values: `ELB` | `Instance` | `N/A`
    reason_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the instance state. This string can contain one or more of
    # the following messages.

    #   * `N/A`

    #   * `A transient error occurred. Please try again later.`

    #   * `Instance has failed at least the UnhealthyThreshold number of health checks consecutively.`

    #   * `Instance has not passed the configured HealthyThreshold number of health checks consecutively.`

    #   * `Instance registration is still in progress.`

    #   * `Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.`

    #   * `Instance is not currently registered with the LoadBalancer.`

    #   * `Instance deregistration currently in progress.`

    #   * `Disable Availability Zone is currently in progress.`

    #   * `Instance is in pending state.`

    #   * `Instance is in stopped state.`

    #   * `Instance is in terminated state.`
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidConfigurationRequestException(ShapeBase):
    """
    The requested configuration change is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEndPointException(ShapeBase):
    """
    The specified endpoint is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSchemeException(ShapeBase):
    """
    The specified value for the schema is not valid. You can only specify a scheme
    for load balancers in a VPC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSecurityGroupException(ShapeBase):
    """
    One or more of the specified security groups do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnetException(ShapeBase):
    """
    The specified VPC has no associated Internet gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LBCookieStickinessPolicy(ShapeBase):
    """
    Information about a policy for duration-based session stickiness.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "cookie_expiration_period",
                "CookieExpirationPeriod",
                TypeInfo(int),
            ),
        ]

    # The name of the policy. This name must be unique within the set of policies
    # for this load balancer.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time period, in seconds, after which the cookie should be considered
    # stale. If this parameter is not specified, the stickiness session lasts for
    # the duration of the browser session.
    cookie_expiration_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Limit(ShapeBase):
    """
    Information about an Elastic Load Balancing resource limit for your AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "max",
                "Max",
                TypeInfo(str),
            ),
        ]

    # The name of the limit. The possible values are:

    #   * classic-listeners

    #   * classic-load-balancers

    #   * classic-registered-instances
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value of the limit.
    max: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Listener(ShapeBase):
    """
    Information about a listener.

    For information about the protocols and the ports supported by Elastic Load
    Balancing, see [Listeners for Your Classic Load
    Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
    listener-config.html) in the _Classic Load Balancers Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "protocol",
                "Protocol",
                TypeInfo(str),
            ),
            (
                "load_balancer_port",
                "LoadBalancerPort",
                TypeInfo(int),
            ),
            (
                "instance_port",
                "InstancePort",
                TypeInfo(int),
            ),
            (
                "instance_protocol",
                "InstanceProtocol",
                TypeInfo(str),
            ),
            (
                "ssl_certificate_id",
                "SSLCertificateId",
                TypeInfo(str),
            ),
        ]

    # The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP,
    # or SSL.
    protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port on which the load balancer is listening. On EC2-VPC, you can
    # specify any port from the range 1-65535. On EC2-Classic, you can specify
    # any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
    load_balancer_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port on which the instance is listening.
    instance_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or
    # SSL.

    # If the front-end protocol is HTTP, HTTPS, TCP, or SSL, `InstanceProtocol`
    # must be at the same protocol.

    # If there is another listener with the same `InstancePort` whose
    # `InstanceProtocol` is secure, (HTTPS or SSL), the listener's
    # `InstanceProtocol` must also be secure.

    # If there is another listener with the same `InstancePort` whose
    # `InstanceProtocol` is HTTP or TCP, the listener's `InstanceProtocol` must
    # be HTTP or TCP.
    instance_protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the server certificate.
    ssl_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListenerDescription(ShapeBase):
    """
    The policies enabled for a listener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener",
                "Listener",
                TypeInfo(Listener),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The listener.
    listener: "Listener" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policies. If there are no policies enabled, the list is empty.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListenerNotFoundException(ShapeBase):
    """
    The load balancer does not have a listener configured at the specified port.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LoadBalancerAttributeNotFoundException(ShapeBase):
    """
    The specified load balancer attribute does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LoadBalancerAttributes(ShapeBase):
    """
    The attributes for a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cross_zone_load_balancing",
                "CrossZoneLoadBalancing",
                TypeInfo(CrossZoneLoadBalancing),
            ),
            (
                "access_log",
                "AccessLog",
                TypeInfo(AccessLog),
            ),
            (
                "connection_draining",
                "ConnectionDraining",
                TypeInfo(ConnectionDraining),
            ),
            (
                "connection_settings",
                "ConnectionSettings",
                TypeInfo(ConnectionSettings),
            ),
            (
                "additional_attributes",
                "AdditionalAttributes",
                TypeInfo(typing.List[AdditionalAttribute]),
            ),
        ]

    # If enabled, the load balancer routes the request traffic evenly across all
    # instances regardless of the Availability Zones.

    # For more information, see [Configure Cross-Zone Load
    # Balancing](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
    # disable-crosszone-lb.html) in the _Classic Load Balancers Guide_.
    cross_zone_load_balancing: "CrossZoneLoadBalancing" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If enabled, the load balancer captures detailed information of all requests
    # and delivers the information to the Amazon S3 bucket that you specify.

    # For more information, see [Enable Access
    # Logs](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
    # access-logs.html) in the _Classic Load Balancers Guide_.
    access_log: "AccessLog" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If enabled, the load balancer allows existing requests to complete before
    # the load balancer shifts traffic away from a deregistered or unhealthy
    # instance.

    # For more information, see [Configure Connection
    # Draining](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-
    # conn-drain.html) in the _Classic Load Balancers Guide_.
    connection_draining: "ConnectionDraining" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If enabled, the load balancer allows the connections to remain idle (no
    # data is sent over the connection) for the specified duration.

    # By default, Elastic Load Balancing maintains a 60-second idle connection
    # timeout for both front-end and back-end connections of your load balancer.
    # For more information, see [Configure Idle Connection
    # Timeout](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-
    # idle-timeout.html) in the _Classic Load Balancers Guide_.
    connection_settings: "ConnectionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is reserved.
    additional_attributes: typing.List["AdditionalAttribute"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class LoadBalancerDescription(ShapeBase):
    """
    Information about a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "dns_name",
                "DNSName",
                TypeInfo(str),
            ),
            (
                "canonical_hosted_zone_name",
                "CanonicalHostedZoneName",
                TypeInfo(str),
            ),
            (
                "canonical_hosted_zone_name_id",
                "CanonicalHostedZoneNameID",
                TypeInfo(str),
            ),
            (
                "listener_descriptions",
                "ListenerDescriptions",
                TypeInfo(typing.List[ListenerDescription]),
            ),
            (
                "policies",
                "Policies",
                TypeInfo(Policies),
            ),
            (
                "backend_server_descriptions",
                "BackendServerDescriptions",
                TypeInfo(typing.List[BackendServerDescription]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_id",
                "VPCId",
                TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
            ),
            (
                "health_check",
                "HealthCheck",
                TypeInfo(HealthCheck),
            ),
            (
                "source_security_group",
                "SourceSecurityGroup",
                TypeInfo(SourceSecurityGroup),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "scheme",
                "Scheme",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS name of the load balancer.
    dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS name of the load balancer.

    # For more information, see [Configure a Custom Domain
    # Name](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-
    # domain-names-with-elb.html) in the _Classic Load Balancers Guide_.
    canonical_hosted_zone_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Amazon Route 53 hosted zone for the load balancer.
    canonical_hosted_zone_name_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The listeners for the load balancer.
    listener_descriptions: typing.List["ListenerDescription"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The policies defined for the load balancer.
    policies: "Policies" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about your EC2 instances.
    backend_server_descriptions: typing.List["BackendServerDescription"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # The Availability Zones for the load balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the subnets for the load balancer.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the VPC for the load balancer.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the instances for the load balancer.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the health checks conducted on the load balancer.
    health_check: "HealthCheck" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security group for the load balancer, which you can use as part of your
    # inbound rules for your registered instances. To only allow traffic from
    # load balancers, add a security group rule that specifies this source
    # security group as the inbound source.
    source_security_group: "SourceSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The security groups for the load balancer. Valid only for load balancers in
    # a VPC.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the load balancer was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of load balancer. Valid only for load balancers in a VPC.

    # If `Scheme` is `internet-facing`, the load balancer has a public DNS name
    # that resolves to a public IP address.

    # If `Scheme` is `internal`, the load balancer has a public DNS name that
    # resolves to a private IP address.
    scheme: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyLoadBalancerAttributesInput(ShapeBase):
    """
    Contains the parameters for ModifyLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "load_balancer_attributes",
                "LoadBalancerAttributes",
                TypeInfo(LoadBalancerAttributes),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes for the load balancer.
    load_balancer_attributes: "LoadBalancerAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyLoadBalancerAttributesOutput(OutputShapeBase):
    """
    Contains the output of ModifyLoadBalancerAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "load_balancer_attributes",
                "LoadBalancerAttributes",
                TypeInfo(LoadBalancerAttributes),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the load balancer attributes.
    load_balancer_attributes: "LoadBalancerAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OperationNotPermittedException(ShapeBase):
    """
    This operation is not allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Policies(ShapeBase):
    """
    The policies for a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_cookie_stickiness_policies",
                "AppCookieStickinessPolicies",
                TypeInfo(typing.List[AppCookieStickinessPolicy]),
            ),
            (
                "lb_cookie_stickiness_policies",
                "LBCookieStickinessPolicies",
                TypeInfo(typing.List[LBCookieStickinessPolicy]),
            ),
            (
                "other_policies",
                "OtherPolicies",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The stickiness policies created using CreateAppCookieStickinessPolicy.
    app_cookie_stickiness_policies: typing.List["AppCookieStickinessPolicy"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # The stickiness policies created using CreateLBCookieStickinessPolicy.
    lb_cookie_stickiness_policies: typing.List["LBCookieStickinessPolicy"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The policies other than the stickiness policies.
    other_policies: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PolicyAttribute(ShapeBase):
    """
    Information about a policy attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyAttributeDescription(ShapeBase):
    """
    Information about a policy attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyAttributeTypeDescription(ShapeBase):
    """
    Information about a policy attribute type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_type",
                "AttributeType",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "cardinality",
                "Cardinality",
                TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the attribute. For example, `Boolean` or `Integer`.
    attribute_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the attribute.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value of the attribute, if applicable.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cardinality of the attribute.

    # Valid values:

    #   * ONE(1) : Single value required

    #   * ZERO_OR_ONE(0..1) : Up to one value is allowed

    #   * ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed

    #   * ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    cardinality: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyDescription(ShapeBase):
    """
    Information about a policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_type_name",
                "PolicyTypeName",
                TypeInfo(str),
            ),
            (
                "policy_attribute_descriptions",
                "PolicyAttributeDescriptions",
                TypeInfo(typing.List[PolicyAttributeDescription]),
            ),
        ]

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy type.
    policy_type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy attributes.
    policy_attribute_descriptions: typing.List["PolicyAttributeDescription"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class PolicyNotFoundException(ShapeBase):
    """
    One or more of the specified policies do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PolicyTypeDescription(ShapeBase):
    """
    Information about a policy type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_type_name",
                "PolicyTypeName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "policy_attribute_type_descriptions",
                "PolicyAttributeTypeDescriptions",
                TypeInfo(typing.List[PolicyAttributeTypeDescription]),
            ),
        ]

    # The name of the policy type.
    policy_type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the policy type.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the policy attributes associated with the policies
    # defined by Elastic Load Balancing.
    policy_attribute_type_descriptions: typing.List[
        "PolicyAttributeTypeDescription"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class PolicyTypeNotFoundException(ShapeBase):
    """
    One or more of the specified policy types do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RegisterEndPointsInput(ShapeBase):
    """
    Contains the parameters for RegisterInstancesWithLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterEndPointsOutput(OutputShapeBase):
    """
    Contains the output of RegisterInstancesWithLoadBalancer.
    """

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
                TypeInfo(typing.List[Instance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated list of instances for the load balancer.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveAvailabilityZonesInput(ShapeBase):
    """
    Contains the parameters for DisableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zones.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveAvailabilityZonesOutput(OutputShapeBase):
    """
    Contains the output for DisableAvailabilityZonesForLoadBalancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The remaining Availability Zones for the load balancer.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsInput(ShapeBase):
    """
    Contains the parameters for RemoveTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[TagKeyOnly]),
            ),
        ]

    # The name of the load balancer. You can specify a maximum of one load
    # balancer name.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tag keys to remove.
    tags: typing.List["TagKeyOnly"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsOutput(OutputShapeBase):
    """
    Contains the output of RemoveTags.
    """

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
class SetLoadBalancerListenerSSLCertificateInput(ShapeBase):
    """
    Contains the parameters for SetLoadBalancerListenerSSLCertificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "load_balancer_port",
                "LoadBalancerPort",
                TypeInfo(int),
            ),
            (
                "ssl_certificate_id",
                "SSLCertificateId",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port that uses the specified SSL certificate.
    load_balancer_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SSL certificate.
    ssl_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetLoadBalancerListenerSSLCertificateOutput(OutputShapeBase):
    """
    Contains the output of SetLoadBalancerListenerSSLCertificate.
    """

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
class SetLoadBalancerPoliciesForBackendServerInput(ShapeBase):
    """
    Contains the parameters for SetLoadBalancerPoliciesForBackendServer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "instance_port",
                "InstancePort",
                TypeInfo(int),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number associated with the EC2 instance.
    instance_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the policies. If the list is empty, then all current polices
    # are removed from the EC2 instance.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetLoadBalancerPoliciesForBackendServerOutput(OutputShapeBase):
    """
    Contains the output of SetLoadBalancerPoliciesForBackendServer.
    """

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
class SetLoadBalancerPoliciesOfListenerInput(ShapeBase):
    """
    Contains the parameters for SetLoadBalancePoliciesOfListener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "load_balancer_port",
                "LoadBalancerPort",
                TypeInfo(int),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The external port of the load balancer.
    load_balancer_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the policies. This list must include all policies to be
    # enabled. If you omit a policy that is currently enabled, it is disabled. If
    # the list is empty, all current policies are disabled.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetLoadBalancerPoliciesOfListenerOutput(OutputShapeBase):
    """
    Contains the output of SetLoadBalancePoliciesOfListener.
    """

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
class SourceSecurityGroup(ShapeBase):
    """
    Information about a source security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner_alias",
                "OwnerAlias",
                TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
        ]

    # The owner of the security group.
    owner_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the security group.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetNotFoundException(ShapeBase):
    """
    One or more of the specified subnets do not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Information about a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagDescription(ShapeBase):
    """
    The tags associated with a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagKeyOnly(ShapeBase):
    """
    The key of a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
        ]

    # The name of the key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyAccessPointsException(ShapeBase):
    """
    The quota for the number of load balancers has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyPoliciesException(ShapeBase):
    """
    The quota for the number of policies for this load balancer has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyTagsException(ShapeBase):
    """
    The quota for the number of tags that can be assigned to a load balancer has
    been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedProtocolException(ShapeBase):
    """
    The specified protocol or signature version is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
