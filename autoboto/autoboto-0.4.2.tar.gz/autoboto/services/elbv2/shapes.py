import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Action(ShapeBase):
    """
    Information about an action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ActionTypeEnum]),
            ),
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "authenticate_oidc_config",
                "AuthenticateOidcConfig",
                TypeInfo(AuthenticateOidcActionConfig),
            ),
            (
                "authenticate_cognito_config",
                "AuthenticateCognitoConfig",
                TypeInfo(AuthenticateCognitoActionConfig),
            ),
            (
                "order",
                "Order",
                TypeInfo(int),
            ),
            (
                "redirect_config",
                "RedirectConfig",
                TypeInfo(RedirectActionConfig),
            ),
            (
                "fixed_response_config",
                "FixedResponseConfig",
                TypeInfo(FixedResponseActionConfig),
            ),
        ]

    # The type of action. Each rule must include exactly one of the following
    # types of actions: `forward`, `fixed-response`, or `redirect`.
    type: typing.Union[str, "ActionTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the target group. Specify only when
    # `Type` is `forward`.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [HTTPS listener] Information about an identity provider that is compliant
    # with OpenID Connect (OIDC). Specify only when `Type` is `authenticate-
    # oidc`.
    authenticate_oidc_config: "AuthenticateOidcActionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [HTTPS listener] Information for using Amazon Cognito to authenticate
    # users. Specify only when `Type` is `authenticate-cognito`.
    authenticate_cognito_config: "AuthenticateCognitoActionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order for the action. This value is required for rules with multiple
    # actions. The action with the lowest value for order is performed first. The
    # final action to be performed must be a `forward` or a `fixed-response`
    # action.
    order: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Application Load Balancer] Information for creating a redirect action.
    # Specify only when `Type` is `redirect`.
    redirect_config: "RedirectActionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Application Load Balancer] Information for creating an action that returns
    # a custom HTTP response. Specify only when `Type` is `fixed-response`.
    fixed_response_config: "FixedResponseActionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ActionTypeEnum(str):
    forward = "forward"
    authenticate_oidc = "authenticate-oidc"
    authenticate_cognito = "authenticate-cognito"
    redirect = "redirect"
    fixed_response = "fixed-response"


@dataclasses.dataclass
class AddListenerCertificatesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate to add. You can specify one certificate per call.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddListenerCertificatesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the certificates.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arns",
                "ResourceArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags. Each resource can have a maximum of 10 tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsOutput(OutputShapeBase):
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
class AllocationIdNotFoundException(ShapeBase):
    """
    The specified allocation ID does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class AuthenticateCognitoActionConditionalBehaviorEnum(str):
    deny = "deny"
    allow = "allow"
    authenticate = "authenticate"


@dataclasses.dataclass
class AuthenticateCognitoActionConfig(ShapeBase):
    """
    Request parameters to use when integrating with Amazon Cognito to authenticate
    users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_pool_arn",
                "UserPoolArn",
                TypeInfo(str),
            ),
            (
                "user_pool_client_id",
                "UserPoolClientId",
                TypeInfo(str),
            ),
            (
                "user_pool_domain",
                "UserPoolDomain",
                TypeInfo(str),
            ),
            (
                "session_cookie_name",
                "SessionCookieName",
                TypeInfo(str),
            ),
            (
                "scope",
                "Scope",
                TypeInfo(str),
            ),
            (
                "session_timeout",
                "SessionTimeout",
                TypeInfo(int),
            ),
            (
                "authentication_request_extra_params",
                "AuthenticationRequestExtraParams",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "on_unauthenticated_request",
                "OnUnauthenticatedRequest",
                TypeInfo(
                    typing.
                    Union[str, AuthenticateCognitoActionConditionalBehaviorEnum]
                ),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
    user_pool_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Amazon Cognito user pool client.
    user_pool_client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain prefix or fully-qualified domain name of the Amazon Cognito user
    # pool.
    user_pool_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cookie used to maintain session information. The default is
    # AWSELBAuthSessionCookie.
    session_cookie_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The set of user claims to be requested from the IdP. The default is
    # `openid`.

    # To verify which scope values your IdP supports and how to separate multiple
    # values, see the documentation for your IdP.
    scope: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum duration of the authentication session, in seconds. The default
    # is 604800 seconds (7 days).
    session_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The query parameters (up to 10) to include in the redirect request to the
    # authorization endpoint.
    authentication_request_extra_params: typing.Dict[
        str, str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The behavior if the user is not authenticated. The following are possible
    # values:

    #   * deny`` \- Return an HTTP 401 Unauthorized error.

    #   * allow`` \- Allow the request to be forwarded to the target.

    #   * authenticate`` \- Redirect the request to the IdP authorization endpoint. This is the default value.
    on_unauthenticated_request: typing.Union[
        str, "AuthenticateCognitoActionConditionalBehaviorEnum"
    ] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AuthenticateOidcActionConditionalBehaviorEnum(str):
    deny = "deny"
    allow = "allow"
    authenticate = "authenticate"


@dataclasses.dataclass
class AuthenticateOidcActionConfig(ShapeBase):
    """
    Request parameters when using an identity provider (IdP) that is compliant with
    OpenID Connect (OIDC) to authenticate users.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "issuer",
                "Issuer",
                TypeInfo(str),
            ),
            (
                "authorization_endpoint",
                "AuthorizationEndpoint",
                TypeInfo(str),
            ),
            (
                "token_endpoint",
                "TokenEndpoint",
                TypeInfo(str),
            ),
            (
                "user_info_endpoint",
                "UserInfoEndpoint",
                TypeInfo(str),
            ),
            (
                "client_id",
                "ClientId",
                TypeInfo(str),
            ),
            (
                "client_secret",
                "ClientSecret",
                TypeInfo(str),
            ),
            (
                "session_cookie_name",
                "SessionCookieName",
                TypeInfo(str),
            ),
            (
                "scope",
                "Scope",
                TypeInfo(str),
            ),
            (
                "session_timeout",
                "SessionTimeout",
                TypeInfo(int),
            ),
            (
                "authentication_request_extra_params",
                "AuthenticationRequestExtraParams",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "on_unauthenticated_request",
                "OnUnauthenticatedRequest",
                TypeInfo(
                    typing.
                    Union[str, AuthenticateOidcActionConditionalBehaviorEnum]
                ),
            ),
        ]

    # The OIDC issuer identifier of the IdP. This must be a full URL, including
    # the HTTPS protocol, the domain, and the path.
    issuer: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authorization endpoint of the IdP. This must be a full URL, including
    # the HTTPS protocol, the domain, and the path.
    authorization_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token endpoint of the IdP. This must be a full URL, including the HTTPS
    # protocol, the domain, and the path.
    token_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user info endpoint of the IdP. This must be a full URL, including the
    # HTTPS protocol, the domain, and the path.
    user_info_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The OAuth 2.0 client identifier.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The OAuth 2.0 client secret.
    client_secret: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cookie used to maintain session information. The default is
    # AWSELBAuthSessionCookie.
    session_cookie_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The set of user claims to be requested from the IdP. The default is
    # `openid`.

    # To verify which scope values your IdP supports and how to separate multiple
    # values, see the documentation for your IdP.
    scope: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum duration of the authentication session, in seconds. The default
    # is 604800 seconds (7 days).
    session_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The query parameters (up to 10) to include in the redirect request to the
    # authorization endpoint.
    authentication_request_extra_params: typing.Dict[
        str, str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The behavior if the user is not authenticated. The following are possible
    # values:

    #   * deny`` \- Return an HTTP 401 Unauthorized error.

    #   * allow`` \- Allow the request to be forwarded to the target.

    #   * authenticate`` \- Redirect the request to the IdP authorization endpoint. This is the default value.
    on_unauthenticated_request: typing.Union[
        str, "AuthenticateOidcActionConditionalBehaviorEnum"
    ] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AvailabilityZone(ShapeBase):
    """
    Information about an Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "zone_name",
                "ZoneName",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "load_balancer_addresses",
                "LoadBalancerAddresses",
                TypeInfo(typing.List[LoadBalancerAddress]),
            ),
        ]

    # The name of the Availability Zone.
    zone_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the subnet.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Network Load Balancers] The static IP address.
    load_balancer_addresses: typing.List["LoadBalancerAddress"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class AvailabilityZoneNotSupportedException(ShapeBase):
    """
    The specified Availability Zone is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Certificate(ShapeBase):
    """
    Information about an SSL server certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "is_default",
                "IsDefault",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the certificate.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the certificate is the default certificate.
    is_default: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CertificateNotFoundException(ShapeBase):
    """
    The specified certificate does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Cipher(ShapeBase):
    """
    Information about a cipher used in a policy.
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
                "priority",
                "Priority",
                TypeInfo(int),
            ),
        ]

    # The name of the cipher.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The priority of the cipher.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateListenerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "default_actions",
                "DefaultActions",
                TypeInfo(typing.List[Action]),
            ),
            (
                "ssl_policy",
                "SslPolicy",
                TypeInfo(str),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol for connections from clients to the load balancer. For
    # Application Load Balancers, the supported protocols are HTTP and HTTPS. For
    # Network Load Balancers, the supported protocol is TCP.
    protocol: typing.Union[str, "ProtocolEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port on which the load balancer is listening.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions for the default rule. The rule must include one forward action
    # or one or more fixed-response actions.

    # If the action type is `forward`, you can specify a single target group. The
    # protocol of the target group must be HTTP or HTTPS for an Application Load
    # Balancer or TCP for a Network Load Balancer.

    # [HTTPS listener] If the action type is `authenticate-oidc`, you can use an
    # identity provider that is OpenID Connect (OIDC) compliant to authenticate
    # users as they access your application.

    # [HTTPS listener] If the action type is `authenticate-cognito`, you can use
    # Amazon Cognito to authenticate users as they access your application.

    # [Application Load Balancer] If the action type is `redirect`, you can
    # redirect HTTP and HTTPS requests.

    # [Application Load Balancer] If the action type is `fixed-response`, you can
    # return a custom HTTP response.
    default_actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [HTTPS listeners] The security policy that defines which ciphers and
    # protocols are supported. The default is the current predefined security
    # policy.
    ssl_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [HTTPS listeners] The default SSL server certificate. You must provide
    # exactly one default certificate. To create a certificate list, use
    # AddListenerCertificates.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateListenerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "listeners",
                "Listeners",
                TypeInfo(typing.List[Listener]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the listener.
    listeners: typing.List["Listener"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_mappings",
                "SubnetMappings",
                TypeInfo(typing.List[SubnetMapping]),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "scheme",
                "Scheme",
                TypeInfo(typing.Union[str, LoadBalancerSchemeEnum]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, LoadBalancerTypeEnum]),
            ),
            (
                "ip_address_type",
                "IpAddressType",
                TypeInfo(typing.Union[str, IpAddressType]),
            ),
        ]

    # The name of the load balancer.

    # This name must be unique per region per account, can have a maximum of 32
    # characters, must contain only alphanumeric characters or hyphens, must not
    # begin or end with a hyphen, and must not begin with "internal-".
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the public subnets. You can specify only one subnet per
    # Availability Zone. You must specify either subnets or subnet mappings.

    # [Application Load Balancers] You must specify subnets from at least two
    # Availability Zones.

    # [Network Load Balancers] You can specify subnets from one or more
    # Availability Zones.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the public subnets. You can specify only one subnet per
    # Availability Zone. You must specify either subnets or subnet mappings.

    # [Application Load Balancers] You must specify subnets from at least two
    # Availability Zones. You cannot specify Elastic IP addresses for your
    # subnets.

    # [Network Load Balancers] You can specify subnets from one or more
    # Availability Zones. You can specify one Elastic IP address per subnet.
    subnet_mappings: typing.List["SubnetMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Application Load Balancers] The IDs of the security groups for the load
    # balancer.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The nodes of an Internet-facing load balancer have public IP addresses. The
    # DNS name of an Internet-facing load balancer is publicly resolvable to the
    # public IP addresses of the nodes. Therefore, Internet-facing load balancers
    # can route requests from clients over the internet.

    # The nodes of an internal load balancer have only private IP addresses. The
    # DNS name of an internal load balancer is publicly resolvable to the private
    # IP addresses of the nodes. Therefore, internal load balancers can only
    # route requests from clients with access to the VPC for the load balancer.

    # The default is an Internet-facing load balancer.
    scheme: typing.Union[str, "LoadBalancerSchemeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more tags to assign to the load balancer.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of load balancer. The default is `application`.
    type: typing.Union[str, "LoadBalancerTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Application Load Balancers] The type of IP addresses used by the subnets
    # for your load balancer. The possible values are `ipv4` (for IPv4 addresses)
    # and `dualstack` (for IPv4 and IPv6 addresses). Internal load balancers must
    # use `ipv4`.
    ip_address_type: typing.Union[str, "IpAddressType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancers",
                "LoadBalancers",
                TypeInfo(typing.List[LoadBalancer]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer.
    load_balancers: typing.List["LoadBalancer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateRuleInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
            (
                "conditions",
                "Conditions",
                TypeInfo(typing.List[RuleCondition]),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[Action]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The conditions. Each condition specifies a field name and a single value.

    # If the field name is `host-header`, you can specify a single host name (for
    # example, my.example.com). A host name is case insensitive, can be up to 128
    # characters in length, and can contain any of the following characters. You
    # can include up to three wildcard characters.

    #   * A-Z, a-z, 0-9

    #   * \- .

    #   * * (matches 0 or more characters)

    #   * ? (matches exactly 1 character)

    # If the field name is `path-pattern`, you can specify a single path pattern.
    # A path pattern is case-sensitive, can be up to 128 characters in length,
    # and can contain any of the following characters. You can include up to
    # three wildcard characters.

    #   * A-Z, a-z, 0-9

    #   * _ - . $ / ~ " ' @ : +

    #   * & (using &amp;)

    #   * * (matches 0 or more characters)

    #   * ? (matches exactly 1 character)
    conditions: typing.List["RuleCondition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rule priority. A listener can't have multiple rules with the same
    # priority.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions. Each rule must include exactly one of the following types of
    # actions: `forward`, `fixed-response`, or `redirect`.

    # If the action type is `forward`, you can specify a single target group.

    # [HTTPS listener] If the action type is `authenticate-oidc`, you can use an
    # identity provider that is OpenID Connect (OIDC) compliant to authenticate
    # users as they access your application.

    # [HTTPS listener] If the action type is `authenticate-cognito`, you can use
    # Amazon Cognito to authenticate users as they access your application.

    # [Application Load Balancer] If the action type is `redirect`, you can
    # redirect HTTP and HTTPS requests.

    # [Application Load Balancer] If the action type is `fixed-response`, you can
    # return a custom HTTP response.
    actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateRuleOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the rule.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTargetGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "health_check_protocol",
                "HealthCheckProtocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "health_check_port",
                "HealthCheckPort",
                TypeInfo(str),
            ),
            (
                "health_check_path",
                "HealthCheckPath",
                TypeInfo(str),
            ),
            (
                "health_check_interval_seconds",
                "HealthCheckIntervalSeconds",
                TypeInfo(int),
            ),
            (
                "health_check_timeout_seconds",
                "HealthCheckTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "healthy_threshold_count",
                "HealthyThresholdCount",
                TypeInfo(int),
            ),
            (
                "unhealthy_threshold_count",
                "UnhealthyThresholdCount",
                TypeInfo(int),
            ),
            (
                "matcher",
                "Matcher",
                TypeInfo(Matcher),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(typing.Union[str, TargetTypeEnum]),
            ),
        ]

    # The name of the target group.

    # This name must be unique per region per account, can have a maximum of 32
    # characters, must contain only alphanumeric characters or hyphens, and must
    # not begin or end with a hyphen.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol to use for routing traffic to the targets. For Application
    # Load Balancers, the supported protocols are HTTP and HTTPS. For Network
    # Load Balancers, the supported protocol is TCP.
    protocol: typing.Union[str, "ProtocolEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port on which the targets receive traffic. This port is used unless you
    # specify a port override when registering the target.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the virtual private cloud (VPC).
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol the load balancer uses when performing health checks on
    # targets. The TCP protocol is supported only if the protocol of the target
    # group is TCP. For Application Load Balancers, the default is HTTP. For
    # Network Load Balancers, the default is TCP.
    health_check_protocol: typing.Union[str, "ProtocolEnum"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The port the load balancer uses when performing health checks on targets.
    # The default is `traffic-port`, which is the port on which each target
    # receives traffic from the load balancer.
    health_check_port: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [HTTP/HTTPS health checks] The ping path that is the destination on the
    # targets for health checks. The default is /.
    health_check_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate amount of time, in seconds, between health checks of an
    # individual target. For Application Load Balancers, the range is 5–300
    # seconds. For Network Load Balancers, the supported values are 10 or 30
    # seconds. The default is 30 seconds.
    health_check_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, during which no response from a target
    # means a failed health check. For Application Load Balancers, the range is
    # 2–60 seconds and the default is 5 seconds. For Network Load Balancers, this
    # is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health
    # checks.
    health_check_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of consecutive health checks successes required before
    # considering an unhealthy target healthy. For Application Load Balancers,
    # the default is 5. For Network Load Balancers, the default is 3.
    healthy_threshold_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of consecutive health check failures required before considering
    # a target unhealthy. For Application Load Balancers, the default is 2. For
    # Network Load Balancers, this value must be the same as the healthy
    # threshold count.
    unhealthy_threshold_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [HTTP/HTTPS health checks] The HTTP codes to use when checking for a
    # successful response from a target.
    matcher: "Matcher" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of target that you must specify when registering targets with this
    # target group. The possible values are `instance` (targets are specified by
    # instance ID) or `ip` (targets are specified by IP address). The default is
    # `instance`. You can't specify targets for a target group using both
    # instance IDs and IP addresses.

    # If the target type is `ip`, specify IP addresses from the subnets of the
    # virtual private cloud (VPC) for the target group, the RFC 1918 range
    # (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range
    # (100.64.0.0/10). You can't specify publicly routable IP addresses.
    target_type: typing.Union[str, "TargetTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTargetGroupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "target_groups",
                "TargetGroups",
                TypeInfo(typing.List[TargetGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the target group.
    target_groups: typing.List["TargetGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteListenerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteListenerOutput(OutputShapeBase):
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
class DeleteLoadBalancerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerOutput(OutputShapeBase):
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
class DeleteRuleInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "RuleArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the rule.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRuleOutput(OutputShapeBase):
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
class DeleteTargetGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTargetGroupOutput(OutputShapeBase):
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
class DeregisterTargetsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[TargetDescription]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets. If you specified a port override when you registered a target,
    # you must specify both the target ID and the port when you deregister it.
    targets: typing.List["TargetDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterTargetsOutput(OutputShapeBase):
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
class DescribeListenerCertificatesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
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

    # The Amazon Resource Names (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeListenerCertificatesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
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

    # Information about the certificates.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeListenersInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "listener_arns",
                "ListenerArns",
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

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Names (ARN) of the listeners.
    listener_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeListenersOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "listeners",
                "Listeners",
                TypeInfo(typing.List[Listener]),
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

    # Information about the listeners.
    listeners: typing.List["Listener"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeListenersOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeLoadBalancerAttributesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoadBalancerAttributesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[LoadBalancerAttribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer attributes.
    attributes: typing.List["LoadBalancerAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancersInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arns",
                "LoadBalancerArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "names",
                "Names",
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

    # The Amazon Resource Names (ARN) of the load balancers. You can specify up
    # to 20 load balancers in a single call.
    load_balancer_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the load balancers.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoadBalancersOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancers",
                "LoadBalancers",
                TypeInfo(typing.List[LoadBalancer]),
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
    load_balancers: typing.List["LoadBalancer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeLoadBalancersOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeRulesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
            (
                "rule_arns",
                "RuleArns",
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

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Names (ARN) of the rules.
    rule_arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRulesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[Rule]),
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

    # Information about the rules.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSSLPoliciesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
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

    # The names of the policies.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSSLPoliciesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ssl_policies",
                "SslPolicies",
                TypeInfo(typing.List[SslPolicy]),
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

    # Information about the policies.
    ssl_policies: typing.List["SslPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arns",
                "ResourceArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Names (ARN) of the resources.
    resource_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTagsOutput(OutputShapeBase):
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
class DescribeTargetGroupAttributesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTargetGroupAttributesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[TargetGroupAttribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the target group attributes
    attributes: typing.List["TargetGroupAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTargetGroupsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "target_group_arns",
                "TargetGroupArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "names",
                "Names",
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

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Names (ARN) of the target groups.
    target_group_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the target groups.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker for the next set of results. (You received this marker from a
    # previous call.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return with this call.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTargetGroupsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "target_groups",
                "TargetGroups",
                TypeInfo(typing.List[TargetGroup]),
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

    # Information about the target groups.
    target_groups: typing.List["TargetGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The marker to use when requesting the next set of results. If there are no
    # additional results, the string is empty.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeTargetGroupsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeTargetHealthInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[TargetDescription]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets.
    targets: typing.List["TargetDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTargetHealthOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "target_health_descriptions",
                "TargetHealthDescriptions",
                TypeInfo(typing.List[TargetHealthDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the health of the targets.
    target_health_descriptions: typing.List["TargetHealthDescription"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class DuplicateListenerException(ShapeBase):
    """
    A listener with the specified port already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DuplicateLoadBalancerNameException(ShapeBase):
    """
    A load balancer with the specified name already exists.
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
class DuplicateTargetGroupNameException(ShapeBase):
    """
    A target group with the specified name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class FixedResponseActionConfig(ShapeBase):
    """
    Information about an action that returns a custom HTTP response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_code",
                "StatusCode",
                TypeInfo(str),
            ),
            (
                "message_body",
                "MessageBody",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
        ]

    # The HTTP response code (2XX, 4XX, or 5XX).
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message.
    message_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content type.

    # Valid Values: text/plain | text/css | text/html | application/javascript |
    # application/json
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HealthUnavailableException(ShapeBase):
    """
    The health of the specified targets could not be retrieved due to an internal
    error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IncompatibleProtocolsException(ShapeBase):
    """
    The specified configuration is not valid with this protocol.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidConfigurationRequestException(ShapeBase):
    """
    The requested configuration is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidLoadBalancerActionException(ShapeBase):
    """
    The requested action is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSchemeException(ShapeBase):
    """
    The requested scheme is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSecurityGroupException(ShapeBase):
    """
    The specified security group does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnetException(ShapeBase):
    """
    The specified subnet is out of available addresses.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTargetException(ShapeBase):
    """
    The specified target does not exist, is not in the same VPC as the target group,
    or has an unsupported instance type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class IpAddressType(str):
    ipv4 = "ipv4"
    dualstack = "dualstack"


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

    #   * application-load-balancers

    #   * listeners-per-application-load-balancer

    #   * listeners-per-network-load-balancer

    #   * network-load-balancers

    #   * rules-per-application-load-balancer

    #   * target-groups

    #   * targets-per-application-load-balancer

    #   * targets-per-availability-zone-per-network-load-balancer

    #   * targets-per-network-load-balancer
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value of the limit.
    max: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Listener(ShapeBase):
    """
    Information about a listener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
            (
                "ssl_policy",
                "SslPolicy",
                TypeInfo(str),
            ),
            (
                "default_actions",
                "DefaultActions",
                TypeInfo(typing.List[Action]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port on which the load balancer is listening.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol for connections from clients to the load balancer.
    protocol: typing.Union[str, "ProtocolEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The SSL server certificate. You must provide a certificate if the protocol
    # is HTTPS.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The security policy that defines which ciphers and protocols are supported.
    # The default is the current predefined security policy.
    ssl_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default actions for the listener.
    default_actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListenerNotFoundException(ShapeBase):
    """
    The specified listener does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LoadBalancer(ShapeBase):
    """
    Information about a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "dns_name",
                "DNSName",
                TypeInfo(str),
            ),
            (
                "canonical_hosted_zone_id",
                "CanonicalHostedZoneId",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "scheme",
                "Scheme",
                TypeInfo(typing.Union[str, LoadBalancerSchemeEnum]),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(LoadBalancerState),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, LoadBalancerTypeEnum]),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[AvailabilityZone]),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "ip_address_type",
                "IpAddressType",
                TypeInfo(typing.Union[str, IpAddressType]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public DNS name of the load balancer.
    dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Amazon Route 53 hosted zone associated with the load
    # balancer.
    canonical_hosted_zone_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the load balancer was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The nodes of an Internet-facing load balancer have public IP addresses. The
    # DNS name of an Internet-facing load balancer is publicly resolvable to the
    # public IP addresses of the nodes. Therefore, Internet-facing load balancers
    # can route requests from clients over the internet.

    # The nodes of an internal load balancer have only private IP addresses. The
    # DNS name of an internal load balancer is publicly resolvable to the private
    # IP addresses of the nodes. Therefore, internal load balancers can only
    # route requests from clients with access to the VPC for the load balancer.
    scheme: typing.Union[str, "LoadBalancerSchemeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the VPC for the load balancer.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the load balancer.
    state: "LoadBalancerState" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of load balancer.
    type: typing.Union[str, "LoadBalancerTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zones for the load balancer.
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the security groups for the load balancer.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of IP addresses used by the subnets for your load balancer. The
    # possible values are `ipv4` (for IPv4 addresses) and `dualstack` (for IPv4
    # and IPv6 addresses).
    ip_address_type: typing.Union[str, "IpAddressType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LoadBalancerAddress(ShapeBase):
    """
    Information about a static IP address for a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "allocation_id",
                "AllocationId",
                TypeInfo(str),
            ),
        ]

    # The static IP address.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Network Load Balancers] The allocation ID of the Elastic IP address.
    allocation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoadBalancerAttribute(ShapeBase):
    """
    Information about a load balancer attribute.
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

    # The name of the attribute.

    # The following attributes are supported by both Application Load Balancers
    # and Network Load Balancers:

    #   * `deletion_protection.enabled` \- Indicates whether deletion protection is enabled. The value is `true` or `false`. The default is `false`.

    # The following attributes are supported by only Application Load Balancers:

    #   * `access_logs.s3.enabled` \- Indicates whether access logs are enabled. The value is `true` or `false`. The default is `false`.

    #   * `access_logs.s3.bucket` \- The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.

    #   * `access_logs.s3.prefix` \- The prefix for the location in the S3 bucket for the access logs.

    #   * `idle_timeout.timeout_seconds` \- The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds.

    #   * `routing.http2.enabled` \- Indicates whether HTTP/2 is enabled. The value is `true` or `false`. The default is `true`.

    # The following attributes are supported by only Network Load Balancers:

    #   * `load_balancing.cross_zone.enabled` \- Indicates whether cross-zone load balancing is enabled. The value is `true` or `false`. The default is `false`.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoadBalancerNotFoundException(ShapeBase):
    """
    The specified load balancer does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class LoadBalancerSchemeEnum(str):
    internet_facing = "internet-facing"
    internal = "internal"


@dataclasses.dataclass
class LoadBalancerState(ShapeBase):
    """
    Information about the state of the load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, LoadBalancerStateEnum]),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(str),
            ),
        ]

    # The state code. The initial state of the load balancer is `provisioning`.
    # After the load balancer is fully set up and ready to route traffic, its
    # state is `active`. If the load balancer could not be set up, its state is
    # `failed`.
    code: typing.Union[str, "LoadBalancerStateEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the state.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LoadBalancerStateEnum(str):
    active = "active"
    provisioning = "provisioning"
    active_impaired = "active_impaired"
    failed = "failed"


class LoadBalancerTypeEnum(str):
    application = "application"
    network = "network"


@dataclasses.dataclass
class Matcher(ShapeBase):
    """
    Information to use when checking for a successful response from a target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "http_code",
                "HttpCode",
                TypeInfo(str),
            ),
        ]

    # The HTTP codes.

    # For Application Load Balancers, you can specify values between 200 and 499,
    # and the default value is 200. You can specify multiple values (for example,
    # "200,202") or a range of values (for example, "200-299").

    # For Network Load Balancers, this is 200–399.
    http_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyListenerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "ssl_policy",
                "SslPolicy",
                TypeInfo(str),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
            (
                "default_actions",
                "DefaultActions",
                TypeInfo(typing.List[Action]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port for connections from clients to the load balancer.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol for connections from clients to the load balancer. Application
    # Load Balancers support HTTP and HTTPS and Network Load Balancers support
    # TCP.
    protocol: typing.Union[str, "ProtocolEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [HTTPS listeners] The security policy that defines which protocols and
    # ciphers are supported. For more information, see [Security
    # Policies](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-
    # https-listener.html#describe-ssl-policies) in the _Application Load
    # Balancers Guide_.
    ssl_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [HTTPS listeners] The default SSL server certificate. You must provide
    # exactly one default certificate. To create a certificate list, use
    # AddListenerCertificates.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions for the default rule. The rule must include one forward action
    # or one or more fixed-response actions.

    # If the action type is `forward`, you can specify a single target group. The
    # protocol of the target group must be HTTP or HTTPS for an Application Load
    # Balancer or TCP for a Network Load Balancer.

    # [HTTPS listener] If the action type is `authenticate-oidc`, you can use an
    # identity provider that is OpenID Connect (OIDC) compliant to authenticate
    # users as they access your application.

    # [HTTPS listener] If the action type is `authenticate-cognito`, you can use
    # Amazon Cognito to authenticate users as they access your application.

    # [Application Load Balancer] If the action type is `redirect`, you can
    # redirect HTTP and HTTPS requests.

    # [Application Load Balancer] If the action type is `fixed-response`, you can
    # return a custom HTTP response.
    default_actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyListenerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "listeners",
                "Listeners",
                TypeInfo(typing.List[Listener]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the modified listener.
    listeners: typing.List["Listener"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyLoadBalancerAttributesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[LoadBalancerAttribute]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The load balancer attributes.
    attributes: typing.List["LoadBalancerAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyLoadBalancerAttributesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[LoadBalancerAttribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer attributes.
    attributes: typing.List["LoadBalancerAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyRuleInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "RuleArn",
                TypeInfo(str),
            ),
            (
                "conditions",
                "Conditions",
                TypeInfo(typing.List[RuleCondition]),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[Action]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the rule.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The conditions. Each condition specifies a field name and a single value.

    # If the field name is `host-header`, you can specify a single host name (for
    # example, my.example.com). A host name is case insensitive, can be up to 128
    # characters in length, and can contain any of the following characters. You
    # can include up to three wildcard characters.

    #   * A-Z, a-z, 0-9

    #   * \- .

    #   * * (matches 0 or more characters)

    #   * ? (matches exactly 1 character)

    # If the field name is `path-pattern`, you can specify a single path pattern.
    # A path pattern is case-sensitive, can be up to 128 characters in length,
    # and can contain any of the following characters. You can include up to
    # three wildcard characters.

    #   * A-Z, a-z, 0-9

    #   * _ - . $ / ~ " ' @ : +

    #   * & (using &amp;)

    #   * * (matches 0 or more characters)

    #   * ? (matches exactly 1 character)
    conditions: typing.List["RuleCondition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions.

    # If the action type is `forward`, you can specify a single target group.

    # If the action type is `authenticate-oidc`, you can use an identity provider
    # that is OpenID Connect (OIDC) compliant to authenticate users as they
    # access your application.

    # If the action type is `authenticate-cognito`, you can use Amazon Cognito to
    # authenticate users as they access your application.
    actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyRuleOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the modified rule.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyTargetGroupAttributesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[TargetGroupAttribute]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes.
    attributes: typing.List["TargetGroupAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyTargetGroupAttributesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[TargetGroupAttribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the attributes.
    attributes: typing.List["TargetGroupAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyTargetGroupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "health_check_protocol",
                "HealthCheckProtocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "health_check_port",
                "HealthCheckPort",
                TypeInfo(str),
            ),
            (
                "health_check_path",
                "HealthCheckPath",
                TypeInfo(str),
            ),
            (
                "health_check_interval_seconds",
                "HealthCheckIntervalSeconds",
                TypeInfo(int),
            ),
            (
                "health_check_timeout_seconds",
                "HealthCheckTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "healthy_threshold_count",
                "HealthyThresholdCount",
                TypeInfo(int),
            ),
            (
                "unhealthy_threshold_count",
                "UnhealthyThresholdCount",
                TypeInfo(int),
            ),
            (
                "matcher",
                "Matcher",
                TypeInfo(Matcher),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol the load balancer uses when performing health checks on
    # targets. The TCP protocol is supported only if the protocol of the target
    # group is TCP.
    health_check_protocol: typing.Union[str, "ProtocolEnum"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The port the load balancer uses when performing health checks on targets.
    health_check_port: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [HTTP/HTTPS health checks] The ping path that is the destination for the
    # health check request.
    health_check_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate amount of time, in seconds, between health checks of an
    # individual target. For Application Load Balancers, the range is 5–300
    # seconds. For Network Load Balancers, the supported values are 10 or 30
    # seconds.
    health_check_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [HTTP/HTTPS health checks] The amount of time, in seconds, during which no
    # response means a failed health check.
    health_check_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of consecutive health checks successes required before
    # considering an unhealthy target healthy.
    healthy_threshold_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of consecutive health check failures required before considering
    # the target unhealthy. For Network Load Balancers, this value must be the
    # same as the healthy threshold count.
    unhealthy_threshold_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [HTTP/HTTPS health checks] The HTTP codes to use when checking for a
    # successful response from a target.
    matcher: "Matcher" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyTargetGroupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "target_groups",
                "TargetGroups",
                TypeInfo(typing.List[TargetGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the modified target group.
    target_groups: typing.List["TargetGroup"] = dataclasses.field(
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
class PriorityInUseException(ShapeBase):
    """
    The specified priority is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ProtocolEnum(str):
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"


@dataclasses.dataclass
class RedirectActionConfig(ShapeBase):
    """
    Information about a redirect action.

    A URI consists of the following components: protocol://hostname:port/path?query.
    You must modify at least one of the following components to avoid a redirect
    loop: protocol, hostname, port, or path. Any components that you do not modify
    retain their original values.

    You can reuse URI components using the following reserved keywords:

      * #{protocol}

      * #{host}

      * #{port}

      * #{path} (the leading "/" is removed)

      * #{query}

    For example, you can change the path to "/new/#{path}", the hostname to
    "example.#{host}", or the query to "#{query}&value=xyz".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_code",
                "StatusCode",
                TypeInfo(typing.Union[str, RedirectActionStatusCodeEnum]),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(str),
            ),
            (
                "host",
                "Host",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "query",
                "Query",
                TypeInfo(str),
            ),
        ]

    # The HTTP redirect code. The redirect is either permanent (HTTP 301) or
    # temporary (HTTP 302).
    status_code: typing.Union[str, "RedirectActionStatusCodeEnum"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect
    # HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS
    # to HTTP.
    protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port. You can specify a value from 1 to 65535 or #{port}.
    port: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hostname. This component is not percent-encoded. The hostname can
    # contain #{host}.
    host: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The absolute path, starting with the leading "/". This component is not
    # percent-encoded. The path can contain #{host}, #{path}, and #{port}.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The query parameters, URL-encoded when necessary, but not percent-encoded.
    # Do not include the leading "?", as it is automatically added. You can
    # specify any of the reserved keywords.
    query: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RedirectActionStatusCodeEnum(str):
    HTTP_301 = "HTTP_301"
    HTTP_302 = "HTTP_302"


@dataclasses.dataclass
class RegisterTargetsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[TargetDescription]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets.
    targets: typing.List["TargetDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterTargetsOutput(OutputShapeBase):
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
class RemoveListenerCertificatesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "listener_arn",
                "ListenerArn",
                TypeInfo(str),
            ),
            (
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the listener.
    listener_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate to remove. You can specify one certificate per call.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveListenerCertificatesOutput(OutputShapeBase):
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
class RemoveTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arns",
                "ResourceArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag keys for the tags to remove.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsOutput(OutputShapeBase):
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
class ResourceInUseException(ShapeBase):
    """
    A specified resource is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Rule(ShapeBase):
    """
    Information about a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "RuleArn",
                TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(str),
            ),
            (
                "conditions",
                "Conditions",
                TypeInfo(typing.List[RuleCondition]),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[Action]),
            ),
            (
                "is_default",
                "IsDefault",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the rule.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The priority.
    priority: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The conditions.
    conditions: typing.List["RuleCondition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions.
    actions: typing.List["Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether this is the default rule.
    is_default: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RuleCondition(ShapeBase):
    """
    Information about a condition for a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field",
                "Field",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the field. The possible values are `host-header` and `path-
    # pattern`.
    field: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The condition value.

    # If the field name is `host-header`, you can specify a single host name (for
    # example, my.example.com). A host name is case insensitive, can be up to 128
    # characters in length, and can contain any of the following characters. You
    # can include up to three wildcard characters.

    #   * A-Z, a-z, 0-9

    #   * \- .

    #   * * (matches 0 or more characters)

    #   * ? (matches exactly 1 character)

    # If the field name is `path-pattern`, you can specify a single path pattern
    # (for example, /img/*). A path pattern is case-sensitive, can be up to 128
    # characters in length, and can contain any of the following characters. You
    # can include up to three wildcard characters.

    #   * A-Z, a-z, 0-9

    #   * _ - . $ / ~ " ' @ : +

    #   * & (using &amp;)

    #   * * (matches 0 or more characters)

    #   * ? (matches exactly 1 character)
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RuleNotFoundException(ShapeBase):
    """
    The specified rule does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RulePriorityPair(ShapeBase):
    """
    Information about the priorities for the rules for a listener.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_arn",
                "RuleArn",
                TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the rule.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rule priority.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SSLPolicyNotFoundException(ShapeBase):
    """
    The specified SSL policy does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SetIpAddressTypeInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "ip_address_type",
                "IpAddressType",
                TypeInfo(typing.Union[str, IpAddressType]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address type. The possible values are `ipv4` (for IPv4 addresses)
    # and `dualstack` (for IPv4 and IPv6 addresses). Internal load balancers must
    # use `ipv4`.
    ip_address_type: typing.Union[str, "IpAddressType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetIpAddressTypeOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ip_address_type",
                "IpAddressType",
                TypeInfo(typing.Union[str, IpAddressType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IP address type.
    ip_address_type: typing.Union[str, "IpAddressType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetRulePrioritiesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_priorities",
                "RulePriorities",
                TypeInfo(typing.List[RulePriorityPair]),
            ),
        ]

    # The rule priorities.
    rule_priorities: typing.List["RulePriorityPair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetRulePrioritiesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the rules.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetSecurityGroupsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the security groups.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetSecurityGroupsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the security groups associated with the load balancer.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetSubnetsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_arn",
                "LoadBalancerArn",
                TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_mappings",
                "SubnetMappings",
                TypeInfo(typing.List[SubnetMapping]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the load balancer.
    load_balancer_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the public subnets. You must specify subnets from at least two
    # Availability Zones. You can specify only one subnet per Availability Zone.
    # You must specify either subnets or subnet mappings.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the public subnets. You must specify subnets from at least two
    # Availability Zones. You can specify only one subnet per Availability Zone.
    # You must specify either subnets or subnet mappings.

    # You cannot specify Elastic IP addresses for your subnets.
    subnet_mappings: typing.List["SubnetMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetSubnetsOutput(OutputShapeBase):
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
                TypeInfo(typing.List[AvailabilityZone]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the subnet and Availability Zone.
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SslPolicy(ShapeBase):
    """
    Information about a policy used for SSL negotiation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ssl_protocols",
                "SslProtocols",
                TypeInfo(typing.List[str]),
            ),
            (
                "ciphers",
                "Ciphers",
                TypeInfo(typing.List[Cipher]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The protocols.
    ssl_protocols: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ciphers.
    ciphers: typing.List["Cipher"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the policy.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetMapping(ShapeBase):
    """
    Information about a subnet mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "allocation_id",
                "AllocationId",
                TypeInfo(str),
            ),
        ]

    # The ID of the subnet.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [Network Load Balancers] The allocation ID of the Elastic IP address.
    allocation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetNotFoundException(ShapeBase):
    """
    The specified subnet does not exist.
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
    The tags associated with a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetDescription(ShapeBase):
    """
    Information about a target.
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
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
        ]

    # The ID of the target. If the target type of the target group is `instance`,
    # specify an instance ID. If the target type is `ip`, specify an IP address.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port on which the target is listening.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Availability Zone or `all`. This determines whether the target receives
    # traffic from the load balancer nodes in the specified Availability Zone or
    # from all enabled Availability Zones for the load balancer.

    # This parameter is not supported if the target type of the target group is
    # `instance`. If the IP address is in a subnet of the VPC for the target
    # group, the Availability Zone is automatically detected and this parameter
    # is optional. If the IP address is outside the VPC, this parameter is
    # required.

    # With an Application Load Balancer, if the IP address is outside the VPC for
    # the target group, the only supported value is `all`.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetGroup(ShapeBase):
    """
    Information about a target group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "TargetGroupArn",
                TypeInfo(str),
            ),
            (
                "target_group_name",
                "TargetGroupName",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "health_check_protocol",
                "HealthCheckProtocol",
                TypeInfo(typing.Union[str, ProtocolEnum]),
            ),
            (
                "health_check_port",
                "HealthCheckPort",
                TypeInfo(str),
            ),
            (
                "health_check_interval_seconds",
                "HealthCheckIntervalSeconds",
                TypeInfo(int),
            ),
            (
                "health_check_timeout_seconds",
                "HealthCheckTimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "healthy_threshold_count",
                "HealthyThresholdCount",
                TypeInfo(int),
            ),
            (
                "unhealthy_threshold_count",
                "UnhealthyThresholdCount",
                TypeInfo(int),
            ),
            (
                "health_check_path",
                "HealthCheckPath",
                TypeInfo(str),
            ),
            (
                "matcher",
                "Matcher",
                TypeInfo(Matcher),
            ),
            (
                "load_balancer_arns",
                "LoadBalancerArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(typing.Union[str, TargetTypeEnum]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the target group.
    target_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol to use for routing traffic to the targets.
    protocol: typing.Union[str, "ProtocolEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port on which the targets are listening.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the VPC for the targets.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol to use to connect with the target.
    health_check_protocol: typing.Union[str, "ProtocolEnum"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The port to use to connect with the target.
    health_check_port: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The approximate amount of time, in seconds, between health checks of an
    # individual target.
    health_check_interval_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, during which no response means a failed
    # health check.
    health_check_timeout_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of consecutive health checks successes required before
    # considering an unhealthy target healthy.
    healthy_threshold_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of consecutive health check failures required before considering
    # the target unhealthy.
    unhealthy_threshold_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination for the health check request.
    health_check_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP codes to use when checking for a successful response from a
    # target.
    matcher: "Matcher" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Names (ARN) of the load balancers that route traffic to
    # this target group.
    load_balancer_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of target that you must specify when registering targets with this
    # target group. The possible values are `instance` (targets are specified by
    # instance ID) or `ip` (targets are specified by IP address).
    target_type: typing.Union[str, "TargetTypeEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TargetGroupAssociationLimitException(ShapeBase):
    """
    You've reached the limit on the number of load balancers per target group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TargetGroupAttribute(ShapeBase):
    """
    Information about a target group attribute.
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

    # The name of the attribute.

    # The following attributes are supported by both Application Load Balancers
    # and Network Load Balancers:

    #   * `deregistration_delay.timeout_seconds` \- The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from `draining` to `unused`. The range is 0-3600 seconds. The default value is 300 seconds.

    # The following attributes are supported by only Application Load Balancers:

    #   * `slow_start.duration_seconds` \- The time period, in seconds, during which a newly registered target receives a linearly increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.

    #   * `stickiness.enabled` \- Indicates whether sticky sessions are enabled. The value is `true` or `false`. The default is `false`.

    #   * `stickiness.type` \- The type of sticky sessions. The possible value is `lb_cookie`.

    #   * `stickiness.lb_cookie.duration_seconds` \- The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).

    # The following attributes are supported by only Network Load Balancers:

    #   * `proxy_protocol_v2.enabled` \- Indicates whether Proxy Protocol version 2 is enabled. The value is `true` or `false`. The default is `false`.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetGroupNotFoundException(ShapeBase):
    """
    The specified target group does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TargetHealth(ShapeBase):
    """
    Information about the current health of a target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, TargetHealthStateEnum]),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(typing.Union[str, TargetHealthReasonEnum]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The state of the target.
    state: typing.Union[str, "TargetHealthStateEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason code. If the target state is `healthy`, a reason code is not
    # provided.

    # If the target state is `initial`, the reason code can be one of the
    # following values:

    #   * `Elb.RegistrationInProgress` \- The target is in the process of being registered with the load balancer.

    #   * `Elb.InitialHealthChecking` \- The load balancer is still sending the target the minimum number of health checks required to determine its health status.

    # If the target state is `unhealthy`, the reason code can be one of the
    # following values:

    #   * `Target.ResponseCodeMismatch` \- The health checks did not return an expected HTTP code.

    #   * `Target.Timeout` \- The health check requests timed out.

    #   * `Target.FailedHealthChecks` \- The health checks failed because the connection to the target timed out, the target response was malformed, or the target failed the health check for an unknown reason.

    #   * `Elb.InternalError` \- The health checks failed due to an internal error.

    # If the target state is `unused`, the reason code can be one of the
    # following values:

    #   * `Target.NotRegistered` \- The target is not registered with the target group.

    #   * `Target.NotInUse` \- The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer.

    #   * `Target.IpUnusable` \- The target IP address is reserved for use by a load balancer.

    #   * `Target.InvalidState` \- The target is in the stopped or terminated state.

    # If the target state is `draining`, the reason code can be the following
    # value:

    #   * `Target.DeregistrationInProgress` \- The target is in the process of being deregistered and the deregistration delay period has not expired.
    reason: typing.Union[str, "TargetHealthReasonEnum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the target health that provides additional details. If the
    # state is `healthy`, a description is not provided.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetHealthDescription(ShapeBase):
    """
    Information about the health of a target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(TargetDescription),
            ),
            (
                "health_check_port",
                "HealthCheckPort",
                TypeInfo(str),
            ),
            (
                "target_health",
                "TargetHealth",
                TypeInfo(TargetHealth),
            ),
        ]

    # The description of the target.
    target: "TargetDescription" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port to use to connect with the target.
    health_check_port: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The health information for the target.
    target_health: "TargetHealth" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TargetHealthReasonEnum(str):
    Elb_RegistrationInProgress = "Elb.RegistrationInProgress"
    Elb_InitialHealthChecking = "Elb.InitialHealthChecking"
    Target_ResponseCodeMismatch = "Target.ResponseCodeMismatch"
    Target_Timeout = "Target.Timeout"
    Target_FailedHealthChecks = "Target.FailedHealthChecks"
    Target_NotRegistered = "Target.NotRegistered"
    Target_NotInUse = "Target.NotInUse"
    Target_DeregistrationInProgress = "Target.DeregistrationInProgress"
    Target_InvalidState = "Target.InvalidState"
    Target_IpUnusable = "Target.IpUnusable"
    Elb_InternalError = "Elb.InternalError"


class TargetHealthStateEnum(str):
    initial = "initial"
    healthy = "healthy"
    unhealthy = "unhealthy"
    unused = "unused"
    draining = "draining"
    unavailable = "unavailable"


class TargetTypeEnum(str):
    instance = "instance"
    ip = "ip"


@dataclasses.dataclass
class TooManyActionsException(ShapeBase):
    """
    You've reached the limit on the number of actions per rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyCertificatesException(ShapeBase):
    """
    You've reached the limit on the number of certificates per load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyListenersException(ShapeBase):
    """
    You've reached the limit on the number of listeners per load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyLoadBalancersException(ShapeBase):
    """
    You've reached the limit on the number of load balancers for your AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyRegistrationsForTargetIdException(ShapeBase):
    """
    You've reached the limit on the number of times a target can be registered with
    a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyRulesException(ShapeBase):
    """
    You've reached the limit on the number of rules per load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyTagsException(ShapeBase):
    """
    You've reached the limit on the number of tags per load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyTargetGroupsException(ShapeBase):
    """
    You've reached the limit on the number of target groups for your AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyTargetsException(ShapeBase):
    """
    You've reached the limit on the number of targets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedProtocolException(ShapeBase):
    """
    The specified protocol is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
