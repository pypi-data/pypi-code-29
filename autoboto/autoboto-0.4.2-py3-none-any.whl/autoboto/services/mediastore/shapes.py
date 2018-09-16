import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Container(ShapeBase):
    """
    This section describes operations that you can perform on an AWS Elemental
    MediaStore container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ContainerStatus]),
            ),
        ]

    # The DNS endpoint of the container. Use the endpoint to identify the
    # specific container when sending requests to the data plane. The service
    # assigns this value when the container is created. Once the value has been
    # assigned, it does not change.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unix timestamp.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the container. The ARN has the following
    # format:

    # arn:aws:<region>:<account that owns this container>:container/<name of
    # container>

    # For example: arn:aws:mediastore:us-west-2:111122223333:container/movies
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the container.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of container creation or deletion. The status is one of the
    # following: `CREATING`, `ACTIVE`, or `DELETING`. While the service is
    # creating the container, the status is `CREATING`. When the endpoint is
    # available, the status changes to `ACTIVE`.
    status: typing.Union[str, "ContainerStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContainerInUseException(ShapeBase):
    """
    Resource already exists or is being updated.
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
class ContainerNotFoundException(ShapeBase):
    """
    Could not perform an operation on a container that does not exist.
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


class ContainerStatus(str):
    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"


@dataclasses.dataclass
class CorsPolicyNotFoundException(ShapeBase):
    """
    Could not perform an operation on a policy that does not exist.
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
class CorsRule(ShapeBase):
    """
    A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more
    than one rule applies, the service uses the first applicable rule listed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_origins",
                "AllowedOrigins",
                TypeInfo(typing.List[str]),
            ),
            (
                "allowed_methods",
                "AllowedMethods",
                TypeInfo(typing.List[typing.Union[str, MethodName]]),
            ),
            (
                "allowed_headers",
                "AllowedHeaders",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_age_seconds",
                "MaxAgeSeconds",
                TypeInfo(int),
            ),
            (
                "expose_headers",
                "ExposeHeaders",
                TypeInfo(typing.List[str]),
            ),
        ]

    # One or more response headers that you want users to be able to access from
    # their applications (for example, from a JavaScript `XMLHttpRequest`
    # object).

    # Each CORS rule must have at least one `AllowedOrigin` element. The string
    # value can include only one wildcard character (*), for example,
    # http://*.example.com. Additionally, you can specify only one wildcard
    # character to allow cross-origin access for all origins.
    allowed_origins: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies an HTTP method that the origin that is specified in the rule is
    # allowed to execute.

    # Each CORS rule must contain at least one `AllowedMethod` and one
    # `AllowedOrigin` element.
    allowed_methods: typing.List[typing.Union[str, "MethodName"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Specifies which headers are allowed in a preflight `OPTIONS` request
    # through the `Access-Control-Request-Headers` header. Each header name that
    # is specified in `Access-Control-Request-Headers` must have a corresponding
    # entry in the rule. Only the headers that were requested are sent back.

    # This element can contain only one wildcard character (*).
    allowed_headers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time in seconds that your browser caches the preflight response for the
    # specified resource.

    # A CORS rule can have only one `MaxAgeSeconds` element.
    max_age_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more headers in the response that you want users to be able to
    # access from their applications (for example, from a JavaScript
    # `XMLHttpRequest` object).

    # This element is optional for each rule.
    expose_headers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateContainerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name for the container. The name must be from 1 to 255 characters.
    # Container names must be unique to your AWS account within a specific
    # region. As an example, you could create a container named `movies` in every
    # region, as long as you don’t have an existing container with that name.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateContainerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container",
                "Container",
                TypeInfo(Container),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ContainerARN: The Amazon Resource Name (ARN) of the newly created
    # container. The ARN has the following format: arn:aws:<region>:<account that
    # owns this container>:container/<name of container>. For example:
    # arn:aws:mediastore:us-west-2:111122223333:container/movies

    # ContainerName: The container name as specified in the request.

    # CreationTime: Unix time stamp.

    # Status: The status of container creation or deletion. The status is one of
    # the following: `CREATING`, `ACTIVE`, or `DELETING`. While the service is
    # creating the container, the status is `CREATING`. When an endpoint is
    # available, the status changes to `ACTIVE`.

    # The return value does not include the container's endpoint. To make
    # downstream requests, you must obtain this value by using DescribeContainer
    # or ListContainers.
    container: "Container" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteContainerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name of the container to delete.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteContainerOutput(OutputShapeBase):
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
class DeleteContainerPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name of the container that holds the policy.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteContainerPolicyOutput(OutputShapeBase):
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
class DeleteCorsPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name of the container to remove the policy from.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCorsPolicyOutput(OutputShapeBase):
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
class DescribeContainerInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name of the container to query.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeContainerOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container",
                "Container",
                TypeInfo(Container),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the queried container.
    container: "Container" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetContainerPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name of the container.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetContainerPolicyOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contents of the access policy.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCorsPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
        ]

    # The name of the container that the policy is assigned to.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCorsPolicyOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cors_policy",
                "CorsPolicy",
                TypeInfo(typing.List[CorsRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CORS policy of the container.
    cors_policy: typing.List["CorsRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    The service is temporarily unavailable.
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
class LimitExceededException(ShapeBase):
    """
    A service limit has been exceeded.
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
class ListContainersInput(ShapeBase):
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
        ]

    # Only if you used `MaxResults` in the first command, enter the token (which
    # was included in the previous response) to obtain the next set of
    # containers. This token is included in a response only if there actually are
    # more containers to list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enter the maximum number of containers in the response. Use from 1 to 255
    # characters.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListContainersOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "containers",
                "Containers",
                TypeInfo(typing.List[Container]),
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

    # The names of the containers.
    containers: typing.List["Container"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # `NextToken` is the token to use in the next call to `ListContainers`. This
    # token is returned only if you included the `MaxResults` tag in the original
    # command, and only if there are still containers to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MethodName(str):
    PUT = "PUT"
    GET = "GET"
    DELETE = "DELETE"
    HEAD = "HEAD"


@dataclasses.dataclass
class PolicyNotFoundException(ShapeBase):
    """
    Could not perform an operation on a policy that does not exist.
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
class PutContainerPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
        ]

    # The name of the container.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the policy, which includes the following:

    #   * One `Version` tag

    #   * One `Statement` tag that contains the standard tags for the policy.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutContainerPolicyOutput(OutputShapeBase):
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
class PutCorsPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "ContainerName",
                TypeInfo(str),
            ),
            (
                "cors_policy",
                "CorsPolicy",
                TypeInfo(typing.List[CorsRule]),
            ),
        ]

    # The name of the container that you want to assign the CORS policy to.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CORS policy to apply to the container.
    cors_policy: typing.List["CorsRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutCorsPolicyOutput(OutputShapeBase):
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
