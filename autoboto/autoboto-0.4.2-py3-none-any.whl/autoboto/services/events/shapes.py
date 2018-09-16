import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AssignPublicIp(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class AwsVpcConfiguration(ShapeBase):
    """
    This structure specifies the VPC subnets and security groups for the task, and
    whether a public IP address is to be used. This structure is relevant only for
    ECS tasks that use the `awsvpc` network mode.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "assign_public_ip",
                "AssignPublicIp",
                TypeInfo(typing.Union[str, AssignPublicIp]),
            ),
        ]

    # Specifies the subnets associated with the task. These subnets must all be
    # in the same VPC. You can specify as many as 16 subnets.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the security groups associated with the task. These security
    # groups must all be in the same VPC. You can specify as many as five
    # security groups. If you do not specify a security group, the default
    # security group for the VPC is used.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the task's elastic network interface receives a public IP
    # address. You can specify `ENABLED` only when `LaunchType` in
    # `EcsParameters` is set to `FARGATE`.
    assign_public_ip: typing.Union[str, "AssignPublicIp"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchArrayProperties(ShapeBase):
    """
    The array properties for the submitted job, such as the size of the array. The
    array size can be between 2 and 10,000. If you specify array properties for a
    job, it becomes an array job. This parameter is used only if the target is an
    AWS Batch job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
        ]

    # The size of the array, if this is an array batch job. Valid values are
    # integers between 2 and 10,000.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchParameters(ShapeBase):
    """
    The custom parameters to be used when the target is an AWS Batch job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_definition",
                "JobDefinition",
                TypeInfo(str),
            ),
            (
                "job_name",
                "JobName",
                TypeInfo(str),
            ),
            (
                "array_properties",
                "ArrayProperties",
                TypeInfo(BatchArrayProperties),
            ),
            (
                "retry_strategy",
                "RetryStrategy",
                TypeInfo(BatchRetryStrategy),
            ),
        ]

    # The ARN or name of the job definition to use if the event target is an AWS
    # Batch job. This job definition must already exist.
    job_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name to use for this execution of the job, if the target is an AWS
    # Batch job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The array properties for the submitted job, such as the size of the array.
    # The array size can be between 2 and 10,000. If you specify array properties
    # for a job, it becomes an array job. This parameter is used only if the
    # target is an AWS Batch job.
    array_properties: "BatchArrayProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry strategy to use for failed jobs, if the target is an AWS Batch
    # job. The retry strategy is the number of times to retry the failed job
    # execution. Valid values are 1–10. When you specify a retry strategy here,
    # it overrides the retry strategy defined in the job definition.
    retry_strategy: "BatchRetryStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchRetryStrategy(ShapeBase):
    """
    The retry strategy to use for failed jobs, if the target is an AWS Batch job. If
    you specify a retry strategy here, it overrides the retry strategy defined in
    the job definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attempts",
                "Attempts",
                TypeInfo(int),
            ),
        ]

    # The number of times to attempt to retry, if the job fails. Valid values are
    # 1–10.
    attempts: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    There is concurrent modification on a rule or target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventBusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeEventBusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
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

    # The name of the event bus. Currently, this is always `default`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the account permitted to write events to
    # the current account.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy that enables the external account to send events to your
    # account.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRuleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "event_pattern",
                "EventPattern",
                TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, RuleState]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the rule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the rule.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event pattern. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5
    # minutes)".
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the rule is enabled or disabled.
    state: typing.Union[str, "RuleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the rule.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role associated with the rule.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EcsParameters(ShapeBase):
    """
    The custom parameters to be used when the target is an Amazon ECS task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition_arn",
                "TaskDefinitionArn",
                TypeInfo(str),
            ),
            (
                "task_count",
                "TaskCount",
                TypeInfo(int),
            ),
            (
                "launch_type",
                "LaunchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "network_configuration",
                "NetworkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
            (
                "platform_version",
                "PlatformVersion",
                TypeInfo(str),
            ),
            (
                "group",
                "Group",
                TypeInfo(str),
            ),
        ]

    # The ARN of the task definition to use if the event target is an Amazon ECS
    # task.
    task_definition_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks to create based on `TaskDefinition`. The default is 1.
    task_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the launch type on which your task is running. The launch type
    # that you specify here must match one of the launch type (compatibilities)
    # of the target task. The `FARGATE` value is supported only in the Regions
    # where AWS Fargate with Amazon ECS is supported. For more information, see
    # [AWS Fargate on Amazon
    # ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-
    # Fargate.html) in the _Amazon Elastic Container Service Developer Guide_.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this structure if the ECS task uses the `awsvpc` network mode. This
    # structure specifies the VPC subnets and security groups associated with the
    # task, and whether a public IP address is to be used. This structure is
    # required if `LaunchType` is `FARGATE` because the `awsvpc` mode is required
    # for Fargate tasks.

    # If you specify `NetworkConfiguration` when the target ECS task does not use
    # the `awsvpc` network mode, the task fails.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the platform version for the task. Specify only the numeric
    # portion of the platform version, such as `1.1.0`.

    # This structure is used only if `LaunchType` is `FARGATE`. For more
    # information about valid platform versions, see [AWS Fargate Platform
    # Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies an ECS task group for the task. The maximum length is 255
    # characters.
    group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputTransformer(ShapeBase):
    """
    Contains the parameters needed for you to provide custom input to a target based
    on one or more pieces of data extracted from the event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_template",
                "InputTemplate",
                TypeInfo(str),
            ),
            (
                "input_paths_map",
                "InputPathsMap",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Input template where you specify placeholders that will be filled with the
    # values of the keys from `InputPathsMap` to customize the data sent to the
    # target. Enclose each `InputPathsMaps` value in brackets: < _value_ > The
    # InputTemplate must be valid JSON.

    # If `InputTemplate` is a JSON object (surrounded by curly braces), the
    # following restrictions apply:

    #   * The placeholder cannot be used as an object key.

    #   * Object values cannot include quote marks.

    # The following example shows the syntax for using `InputPathsMap` and
    # `InputTemplate`.

    # ` "InputTransformer":`

    # `{`

    # `"InputPathsMap": {"instance": "$.detail.instance","status":
    # "$.detail.status"},`

    # `"InputTemplate": "<instance> is in state <status>"`

    # `}`

    # To have the `InputTemplate` include quote marks within a JSON string,
    # escape each quote marks with a slash, as in the following example:

    # ` "InputTransformer":`

    # `{`

    # `"InputPathsMap": {"instance": "$.detail.instance","status":
    # "$.detail.status"},`

    # `"InputTemplate": "<instance> is in state \"<status>\""`

    # `}`
    input_template: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Map of JSON paths to be extracted from the event. You can then insert these
    # in the template in `InputTemplate` to produce the output you want to be
    # sent to the target.

    # `InputPathsMap` is an array key-value pairs, where each value is a valid
    # JSON path. You can have as many as 10 key-value pairs. You must use JSON
    # dot notation, not bracket notation.

    # The keys cannot start with "AWS."
    input_paths_map: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalException(ShapeBase):
    """
    This exception occurs due to unexpected causes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEventPatternException(ShapeBase):
    """
    The event pattern is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KinesisParameters(ShapeBase):
    """
    This object enables you to specify a JSON path to extract from the event and use
    as the partition key for the Amazon Kinesis data stream, so that you can control
    the shard to which the event goes. If you do not include this parameter, the
    default is to use the `eventId` as the partition key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "partition_key_path",
                "PartitionKeyPath",
                TypeInfo(str),
            ),
        ]

    # The JSON path to be extracted from the event and used as the partition key.
    # For more information, see [Amazon Kinesis Streams Key
    # Concepts](http://docs.aws.amazon.com/streams/latest/dev/key-
    # concepts.html#partition-key) in the _Amazon Kinesis Streams Developer
    # Guide_.
    partition_key_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LaunchType(str):
    EC2 = "EC2"
    FARGATE = "FARGATE"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    You tried to create more rules or add more targets to a rule than is allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListRuleNamesByTargetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetArn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target resource.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned by a previous call to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRuleNamesByTargetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rule_names",
                "RuleNames",
                TypeInfo(typing.List[str]),
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

    # The names of the rules that can invoke the given target.
    rule_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether there are additional results to retrieve. If there are no
    # more results, the value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRulesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_prefix",
                "NamePrefix",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The prefix matching the rule name.
    name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned by a previous call to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRulesResponse(OutputShapeBase):
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rules that match the specified criteria.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether there are additional results to retrieve. If there are no
    # more results, the value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTargetsByRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The name of the rule.
    rule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned by a previous call to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTargetsByRuleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
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

    # The targets assigned to the rule.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether there are additional results to retrieve. If there are no
    # more results, the value is null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkConfiguration(ShapeBase):
    """
    This structure specifies the network configuration for an ECS task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "awsvpc_configuration",
                "awsvpcConfiguration",
                TypeInfo(AwsVpcConfiguration),
            ),
        ]

    # Use this structure to specify the VPC subnets and security groups for the
    # task, and whether a public IP address is to be used. This structure is
    # relevant only for ECS tasks that use the `awsvpc` network mode.
    awsvpc_configuration: "AwsVpcConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PolicyLengthExceededException(ShapeBase):
    """
    The event bus policy is too long. For more information, see the limits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PutEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[PutEventsRequestEntry]),
            ),
        ]

    # The entry that defines an event in your system. You can specify several
    # parameters for the entry such as the source and type of the event,
    # resources associated with the event, and so on.
    entries: typing.List["PutEventsRequestEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutEventsRequestEntry(ShapeBase):
    """
    Represents an event to be submitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time",
                "Time",
                TypeInfo(datetime.datetime),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[str]),
            ),
            (
                "detail_type",
                "DetailType",
                TypeInfo(str),
            ),
            (
                "detail",
                "Detail",
                TypeInfo(str),
            ),
        ]

    # The time stamp of the event, per [RFC3339](https://www.rfc-
    # editor.org/rfc/rfc3339.txt). If no time stamp is provided, the time stamp
    # of the PutEvents call is used.
    time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the event. This field is required.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS resources, identified by Amazon Resource Name (ARN), which the event
    # primarily concerns. Any number, including zero, may be present.
    resources: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Free-form string used to decide what fields to expect in the event detail.
    detail_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid JSON string. There is no other schema imposed. The JSON string may
    # contain fields and nested subobjects.
    detail: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_entry_count",
                "FailedEntryCount",
                TypeInfo(int),
            ),
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[PutEventsResultEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of failed entries.
    failed_entry_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The successfully and unsuccessfully ingested events results. If the
    # ingestion was successful, the entry has the event ID in it. Otherwise, you
    # can use the error code and error message to identify the problem with the
    # entry.
    entries: typing.List["PutEventsResultEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutEventsResultEntry(ShapeBase):
    """
    Represents an event that failed to be submitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_id",
                "EventId",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The ID of the event.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code that indicates why the event submission failed.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message that explains why the event submission failed.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutPermissionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(str),
            ),
            (
                "principal",
                "Principal",
                TypeInfo(str),
            ),
            (
                "statement_id",
                "StatementId",
                TypeInfo(str),
            ),
        ]

    # The action that you are enabling the other account to perform. Currently,
    # this must be `events:PutEvents`.
    action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 12-digit AWS account ID that you are permitting to put events to your
    # default event bus. Specify "*" to permit any account to put events to your
    # default event bus.

    # If you specify "*", avoid creating rules that may match undesirable events.
    # To create more secure rules, make sure that the event pattern for each rule
    # contains an `account` field with a specific account ID from which to
    # receive events. Rules with an account field do not match any events sent
    # from other accounts.
    principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier string for the external account that you are granting
    # permissions to. If you later want to revoke the permission for this
    # external account, specify this `StatementId` when you run RemovePermission.
    statement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "event_pattern",
                "EventPattern",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, RuleState]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The name of the rule that you are creating or updating.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scheduling expression. For example, "cron(0 20 * * ? *)" or "rate(5
    # minutes)".
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event pattern. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the rule is enabled or disabled.
    state: typing.Union[str, "RuleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the rule.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role associated with the rule.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutRuleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rule_arn",
                "RuleArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the rule.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
        ]

    # The name of the rule.
    rule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets to update or add to the rule.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutTargetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_entry_count",
                "FailedEntryCount",
                TypeInfo(int),
            ),
            (
                "failed_entries",
                "FailedEntries",
                TypeInfo(typing.List[PutTargetsResultEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of failed entries.
    failed_entry_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The failed target entries.
    failed_entries: typing.List["PutTargetsResultEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutTargetsResultEntry(ShapeBase):
    """
    Represents a target that failed to be added to a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_id",
                "TargetId",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The ID of the target.
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code that indicates why the target addition failed. If the value
    # is `ConcurrentModificationException`, too many requests were made at the
    # same time.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message that explains why the target addition failed.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemovePermissionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "statement_id",
                "StatementId",
                TypeInfo(str),
            ),
        ]

    # The statement ID corresponding to the account that is no longer allowed to
    # put events to the default event bus.
    statement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule",
                "Rule",
                TypeInfo(str),
            ),
            (
                "ids",
                "Ids",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the rule.
    rule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the targets to remove from the rule.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTargetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_entry_count",
                "FailedEntryCount",
                TypeInfo(int),
            ),
            (
                "failed_entries",
                "FailedEntries",
                TypeInfo(typing.List[RemoveTargetsResultEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of failed entries.
    failed_entry_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The failed target entries.
    failed_entries: typing.List["RemoveTargetsResultEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTargetsResultEntry(ShapeBase):
    """
    Represents a target that failed to be removed from a rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_id",
                "TargetId",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # The ID of the target.
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code that indicates why the target removal failed. If the value
    # is `ConcurrentModificationException`, too many requests were made at the
    # same time.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message that explains why the target removal failed.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    An entity that you specified does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Rule(ShapeBase):
    """
    Contains information about a rule in Amazon CloudWatch Events.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "event_pattern",
                "EventPattern",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, RuleState]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The name of the rule.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the rule.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event pattern of the rule. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the rule.
    state: typing.Union[str, "RuleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the rule.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5
    # minutes)".
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the role that is used for target
    # invocation.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RuleState(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class RunCommandParameters(ShapeBase):
    """
    This parameter contains the criteria (either InstanceIds or a tag) used to
    specify which EC2 instances are to be sent the command.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "run_command_targets",
                "RunCommandTargets",
                TypeInfo(typing.List[RunCommandTarget]),
            ),
        ]

    # Currently, we support including only one RunCommandTarget block, which
    # specifies either an array of InstanceIds or a tag.
    run_command_targets: typing.List["RunCommandTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RunCommandTarget(ShapeBase):
    """
    Information about the EC2 instances that are to be sent the command, specified
    as key-value pairs. Each `RunCommandTarget` block can include only one key, but
    this key may specify multiple values.
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
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Can be either `tag:` _tag-key_ or `InstanceIds`.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `Key` is `tag:` _tag-key_ , `Values` is a list of tag values. If `Key`
    # is `InstanceIds`, `Values` is a list of Amazon EC2 instance IDs.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SqsParameters(ShapeBase):
    """
    This structure includes the custom parameter to be used when the target is an
    SQS FIFO queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_group_id",
                "MessageGroupId",
                TypeInfo(str),
            ),
        ]

    # The FIFO message group ID to use as the target.
    message_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Target(ShapeBase):
    """
    Targets are the resources to be invoked when a rule is triggered. For a complete
    list of services and resources that can be set as a target, see PutTargets.
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
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "input",
                "Input",
                TypeInfo(str),
            ),
            (
                "input_path",
                "InputPath",
                TypeInfo(str),
            ),
            (
                "input_transformer",
                "InputTransformer",
                TypeInfo(InputTransformer),
            ),
            (
                "kinesis_parameters",
                "KinesisParameters",
                TypeInfo(KinesisParameters),
            ),
            (
                "run_command_parameters",
                "RunCommandParameters",
                TypeInfo(RunCommandParameters),
            ),
            (
                "ecs_parameters",
                "EcsParameters",
                TypeInfo(EcsParameters),
            ),
            (
                "batch_parameters",
                "BatchParameters",
                TypeInfo(BatchParameters),
            ),
            (
                "sqs_parameters",
                "SqsParameters",
                TypeInfo(SqsParameters),
            ),
        ]

    # The ID of the target.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the target.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role to be used for this target
    # when the rule is triggered. If one rule triggers multiple targets, you can
    # use a different IAM role for each target.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Valid JSON text passed to the target. In this case, nothing from the event
    # itself is passed to the target. For more information, see [The JavaScript
    # Object Notation (JSON) Data Interchange Format](http://www.rfc-
    # editor.org/rfc/rfc7159.txt).
    input: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the JSONPath that is used for extracting part of the matched
    # event when passing it to the target. You must use JSON dot notation, not
    # bracket notation. For more information about JSON paths, see
    # [JSONPath](http://goessner.net/articles/JsonPath/).
    input_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings to enable you to provide custom input to a target based on certain
    # event data. You can extract one or more key-value pairs from the event and
    # then use that data to send customized input to the target.
    input_transformer: "InputTransformer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The custom parameter you can use to control the shard assignment, when the
    # target is a Kinesis data stream. If you do not include this parameter, the
    # default is to use the `eventId` as the partition key.
    kinesis_parameters: "KinesisParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Parameters used when you are using the rule to invoke Amazon EC2 Run
    # Command.
    run_command_parameters: "RunCommandParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the Amazon ECS task definition and task count to be used, if the
    # event target is an Amazon ECS task. For more information about Amazon ECS
    # tasks, see [Task Definitions
    # ](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html)
    # in the _Amazon EC2 Container Service Developer Guide_.
    ecs_parameters: "EcsParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the event target is an AWS Batch job, this contains the job definition,
    # job name, and other parameters. For more information, see
    # [Jobs](http://docs.aws.amazon.com/batch/latest/userguide/jobs.html) in the
    # _AWS Batch User Guide_.
    batch_parameters: "BatchParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the message group ID to use when the target is a FIFO queue.

    # If you specify an SQS FIFO queue as a target, the queue must have content-
    # based deduplication enabled.
    sqs_parameters: "SqsParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestEventPatternRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_pattern",
                "EventPattern",
                TypeInfo(str),
            ),
            (
                "event",
                "Event",
                TypeInfo(str),
            ),
        ]

    # The event pattern. For more information, see [Events and Event
    # Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html)
    # in the _Amazon CloudWatch Events User Guide_.
    event_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event, in JSON format, to test against the event pattern.
    event: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestEventPatternResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result",
                "Result",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the event matches the event pattern.
    result: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
