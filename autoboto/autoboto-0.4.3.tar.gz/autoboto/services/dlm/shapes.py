import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class CreateLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, SettablePolicyStateValues]),
            ),
            (
                "policy_details",
                "PolicyDetails",
                TypeInfo(PolicyDetails),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role used to run the operations
    # specified by the lifecycle policy.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are
    # supported.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired activation state of the lifecycle policy after creation.
    state: typing.Union[str, "SettablePolicyStateValues"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration details of the lifecycle policy.

    # Target tags cannot be re-used across lifecycle policies.
    policy_details: "PolicyDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLifecyclePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRule(ShapeBase):
    """
    Specifies when to create snapshots of EBS volumes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interval",
                "Interval",
                TypeInfo(int),
            ),
            (
                "interval_unit",
                "IntervalUnit",
                TypeInfo(typing.Union[str, IntervalUnitValues]),
            ),
            (
                "times",
                "Times",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The interval. The supported values are 12 and 24.
    interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval unit.
    interval_unit: typing.Union[str, "IntervalUnitValues"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time, in UTC, to start the operation.

    # The operation occurs within a one-hour window following the specified time.
    times: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecyclePolicyResponse(OutputShapeBase):
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
class GetLifecyclePoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_ids",
                "PolicyIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, GettablePolicyStateValues]),
            ),
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[typing.Union[str, ResourceTypeValues]]),
            ),
            (
                "target_tags",
                "TargetTags",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags_to_add",
                "TagsToAdd",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifiers of the data lifecycle policies.
    policy_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The activation state.
    state: typing.Union[str, "GettablePolicyStateValues"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type.
    resource_types: typing.List[typing.Union[str, "ResourceTypeValues"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The target tag for a policy.

    # Tags are strings in the format `key=value`.
    target_tags: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags to add to objects created by the policy.

    # Tags are strings in the format `key=value`.

    # These user-defined tags are added in addition to the AWS-added lifecycle
    # tags.
    tags_to_add: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLifecyclePoliciesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policies",
                "Policies",
                TypeInfo(typing.List[LifecyclePolicySummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information about the lifecycle policies.
    policies: typing.List["LifecyclePolicySummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLifecyclePolicyResponse(OutputShapeBase):
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
                TypeInfo(LifecyclePolicy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about the lifecycle policy.
    policy: "LifecyclePolicy" = dataclasses.field(default=ShapeBase.NOT_SET, )


class GettablePolicyStateValues(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ERROR = "ERROR"


@dataclasses.dataclass
class InternalServerException(ShapeBase):
    """
    The service failed in an unexpected way.
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
                "code",
                "Code",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class IntervalUnitValues(str):
    HOURS = "HOURS"


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    Bad request. The request is missing required parameters or has invalid
    parameters.
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
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "required_parameters",
                "RequiredParameters",
                TypeInfo(typing.List[str]),
            ),
            (
                "mutually_exclusive_parameters",
                "MutuallyExclusiveParameters",
                TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The request omitted one or more required parameters.
    required_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request included parameters that cannot be provided together.
    mutually_exclusive_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecyclePolicy(ShapeBase):
    """
    Detailed information about a lifecycle policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, GettablePolicyStateValues]),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                TypeInfo(str),
            ),
            (
                "date_created",
                "DateCreated",
                TypeInfo(datetime.datetime),
            ),
            (
                "date_modified",
                "DateModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "policy_details",
                "PolicyDetails",
                TypeInfo(PolicyDetails),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the lifecycle policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The activation state of the lifecycle policy.
    state: typing.Union[str, "GettablePolicyStateValues"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role used to run the operations
    # specified by the lifecycle policy.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The local date and time when the lifecycle policy was created.
    date_created: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The local date and time when the lifecycle policy was last modified.
    date_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration of the lifecycle policy
    policy_details: "PolicyDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecyclePolicySummary(ShapeBase):
    """
    Summary information about a lifecycle policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, GettablePolicyStateValues]),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the lifecycle policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The activation state of the lifecycle policy.
    state: typing.Union[str, "GettablePolicyStateValues"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The request failed because a limit was exceeded.
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
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value is the type of resource for which a limit was exceeded.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyDetails(ShapeBase):
    """
    Specifies the configuration of a lifecycle policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[typing.Union[str, ResourceTypeValues]]),
            ),
            (
                "target_tags",
                "TargetTags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "schedules",
                "Schedules",
                TypeInfo(typing.List[Schedule]),
            ),
        ]

    # The resource type.
    resource_types: typing.List[typing.Union[str, "ResourceTypeValues"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The single tag that identifies targeted resources for this policy.
    target_tags: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The schedule of policy-defined actions.
    schedules: typing.List["Schedule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    A requested resource was not found.
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
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "resource_ids",
                "ResourceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value is the type of resource that was not found.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value is a list of resource IDs that were not found.
    resource_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ResourceTypeValues(str):
    VOLUME = "VOLUME"


@dataclasses.dataclass
class RetainRule(ShapeBase):
    """
    Specifies the number of snapshots to keep for each EBS volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
        ]

    # The number of snapshots to keep for each volume, up to a maximum of 1000.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Schedule(ShapeBase):
    """
    Specifies a schedule.
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
                "tags_to_add",
                "TagsToAdd",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "create_rule",
                "CreateRule",
                TypeInfo(CreateRule),
            ),
            (
                "retain_rule",
                "RetainRule",
                TypeInfo(RetainRule),
            ),
        ]

    # The name of the schedule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to apply to policy-created resources. These user-defined tags are
    # in addition to the AWS-added lifecycle tags.
    tags_to_add: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The create rule.
    create_rule: "CreateRule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The retain rule.
    retain_rule: "RetainRule" = dataclasses.field(default=ShapeBase.NOT_SET, )


class SettablePolicyStateValues(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Specifies a tag for a resource.
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

    # The tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateLifecyclePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, SettablePolicyStateValues]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "policy_details",
                "PolicyDetails",
                TypeInfo(PolicyDetails),
            ),
        ]

    # The identifier of the lifecycle policy.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role used to run the operations
    # specified by the lifecycle policy.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired activation state of the lifecycle policy after creation.
    state: typing.Union[str, "SettablePolicyStateValues"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the lifecycle policy.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration of the lifecycle policy.

    # Target tags cannot be re-used across policies.
    policy_details: "PolicyDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateLifecyclePolicyResponse(OutputShapeBase):
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
