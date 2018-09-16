import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AssociateKmsKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "kmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    # For more information, see [Amazon Resource Names - AWS Key Management
    # Service (AWS KMS)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html#arn-syntax-kms).
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelExportTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
        ]

    # The ID of the export task.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateExportTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "from_",
                "from",
                TypeInfo(int),
            ),
            (
                "to",
                "to",
                TypeInfo(int),
            ),
            (
                "destination",
                "destination",
                TypeInfo(str),
            ),
            (
                "task_name",
                "taskName",
                TypeInfo(str),
            ),
            (
                "log_stream_name_prefix",
                "logStreamNamePrefix",
                TypeInfo(str),
            ),
            (
                "destination_prefix",
                "destinationPrefix",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the range for the request, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp
    # earlier than this time are not exported.
    from_: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end time of the range for the request, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later
    # than this time are not exported.
    to: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of S3 bucket for the exported log data. The bucket must be in the
    # same AWS region.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the export task.
    task_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Export only log streams that match the provided prefix. If you don't
    # specify a value, no prefix filter is applied.
    log_stream_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix used as the start of the key for every object exported. If you
    # don't specify a value, the default is `exportedlogs`.
    destination_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateExportTaskResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the export task.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLogGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "kmsKeyId",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    # For more information, see [Amazon Resource Names - AWS Key Management
    # Service (AWS KMS)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html#arn-syntax-kms).
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value pairs to use for the tags.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLogStreamRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataAlreadyAcceptedException(ShapeBase):
    """
    The event was already logged.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expected_sequence_token",
                "expectedSequenceToken",
                TypeInfo(str),
            ),
        ]

    expected_sequence_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDestinationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                TypeInfo(str),
            ),
        ]

    # The name of the destination.
    destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLogGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLogStreamRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMetricFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the metric filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourcePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                TypeInfo(str),
            ),
        ]

    # The name of the policy to be revoked. This parameter is required.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRetentionPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSubscriptionFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the subscription filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDestinationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name_prefix",
                "DestinationNamePrefix",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The prefix to match. If you don't specify a value, no prefix filter is
    # applied.
    destination_name_prefix: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDestinationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "destinations",
                "destinations",
                TypeInfo(typing.List[Destination]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destinations.
    destinations: typing.List["Destination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeDestinationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeExportTasksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(typing.Union[str, ExportTaskStatusCode]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The ID of the export task. Specifying a task ID filters the results to zero
    # or one export tasks.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status code of the export task. Specifying a status code filters the
    # results to zero or more export tasks.
    status_code: typing.Union[str, "ExportTaskStatusCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeExportTasksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_tasks",
                "exportTasks",
                TypeInfo(typing.List[ExportTask]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The export tasks.
    export_tasks: typing.List["ExportTask"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name_prefix",
                "logGroupNamePrefix",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The prefix to match.
    log_group_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log_groups",
                "logGroups",
                TypeInfo(typing.List[LogGroup]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log groups.
    log_groups: typing.List["LogGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeLogGroupsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeLogStreamsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_name_prefix",
                "logStreamNamePrefix",
                TypeInfo(str),
            ),
            (
                "order_by",
                "orderBy",
                TypeInfo(typing.Union[str, OrderBy]),
            ),
            (
                "descending",
                "descending",
                TypeInfo(bool),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix to match.

    # If `orderBy` is `LastEventTime`,you cannot specify this parameter.
    log_stream_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the value is `LogStreamName`, the results are ordered by log stream
    # name. If the value is `LastEventTime`, the results are ordered by the event
    # time. The default value is `LogStreamName`.

    # If you order the results by event time, you cannot specify the
    # `logStreamNamePrefix` parameter.

    # lastEventTimestamp represents the time of the most recent log event in the
    # log stream in CloudWatch Logs. This number is expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on
    # an eventual consistency basis. It typically updates in less than an hour
    # from ingestion, but may take longer in some rare situations.
    order_by: typing.Union[str, "OrderBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the value is true, results are returned in descending order. If the
    # value is to false, results are returned in ascending order. The default
    # value is false.
    descending: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLogStreamsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "log_streams",
                "logStreams",
                TypeInfo(typing.List[LogStream]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log streams.
    log_streams: typing.List["LogStream"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeLogStreamsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeMetricFiltersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_name_prefix",
                "filterNamePrefix",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "metric_name",
                "metricName",
                TypeInfo(str),
            ),
            (
                "metric_namespace",
                "metricNamespace",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix to match.
    filter_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters results to include only those with the specified metric name. If
    # you include this parameter in your request, you must also include the
    # `metricNamespace` parameter.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters results to include only those in the specified namespace. If you
    # include this parameter in your request, you must also include the
    # `metricName` parameter.
    metric_namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMetricFiltersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_filters",
                "metricFilters",
                TypeInfo(typing.List[MetricFilter]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metric filters.
    metric_filters: typing.List["MetricFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeMetricFiltersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeResourcePoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of resource policies to be displayed with one call of
    # this API.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResourcePoliciesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_policies",
                "resourcePolicies",
                TypeInfo(typing.List[ResourcePolicy]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource policies that exist in this account.
    resource_policies: typing.List["ResourcePolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSubscriptionFiltersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_name_prefix",
                "filterNamePrefix",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix to match. If you don't specify a value, no prefix filter is
    # applied.
    filter_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items returned. If you don't specify a value, the
    # default is up to 50 items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSubscriptionFiltersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscription_filters",
                "subscriptionFilters",
                TypeInfo(typing.List[SubscriptionFilter]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subscription filters.
    subscription_filters: typing.List["SubscriptionFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. The token expires after 24
    # hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeSubscriptionFiltersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Destination(ShapeBase):
    """
    Represents a cross-account destination that receives subscription log events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                TypeInfo(str),
            ),
            (
                "target_arn",
                "targetArn",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "access_policy",
                "accessPolicy",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(int),
            ),
        ]

    # The name of the destination.
    destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the physical target to where the log
    # events are delivered (for example, a Kinesis stream).
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A role for impersonation, used when delivering log events to the target.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM policy document that governs which AWS accounts can create
    # subscription filters against this destination.
    access_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of this destination.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The creation time of the destination, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateKmsKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Distribution(str):
    """
    The method used to distribute log data to the destination, which can be either
    random or grouped by log stream.
    """
    Random = "Random"
    ByLogStream = "ByLogStream"


@dataclasses.dataclass
class ExportTask(ShapeBase):
    """
    Represents an export task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
            (
                "task_name",
                "taskName",
                TypeInfo(str),
            ),
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "from_",
                "from",
                TypeInfo(int),
            ),
            (
                "to",
                "to",
                TypeInfo(int),
            ),
            (
                "destination",
                "destination",
                TypeInfo(str),
            ),
            (
                "destination_prefix",
                "destinationPrefix",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(ExportTaskStatus),
            ),
            (
                "execution_info",
                "executionInfo",
                TypeInfo(ExportTaskExecutionInfo),
            ),
        ]

    # The ID of the export task.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the export task.
    task_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log group from which logs data was exported.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time, expressed as the number of milliseconds after Jan 1, 1970
    # 00:00:00 UTC. Events with a time stamp before this time are not exported.
    from_: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end time, expressed as the number of milliseconds after Jan 1, 1970
    # 00:00:00 UTC. Events with a time stamp later than this time are not
    # exported.
    to: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of Amazon S3 bucket to which the log data was exported.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix that was used as the start of Amazon S3 key for every object
    # exported.
    destination_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the export task.
    status: "ExportTaskStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Execution info about the export task.
    execution_info: "ExportTaskExecutionInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExportTaskExecutionInfo(ShapeBase):
    """
    Represents the status of an export task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_time",
                "creationTime",
                TypeInfo(int),
            ),
            (
                "completion_time",
                "completionTime",
                TypeInfo(int),
            ),
        ]

    # The creation time of the export task, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The completion time of the export task, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    completion_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportTaskStatus(ShapeBase):
    """
    Represents the status of an export task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(typing.Union[str, ExportTaskStatusCode]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The status code of the export task.
    code: typing.Union[str, "ExportTaskStatusCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status message related to the status code.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExportTaskStatusCode(str):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PENDING_CANCEL = "PENDING_CANCEL"
    RUNNING = "RUNNING"


@dataclasses.dataclass
class FilterLogEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_names",
                "logStreamNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "log_stream_name_prefix",
                "logStreamNamePrefix",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(int),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(int),
            ),
            (
                "filter_pattern",
                "filterPattern",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "interleaved",
                "interleaved",
                TypeInfo(bool),
            ),
        ]

    # The name of the log group to search.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the results to only logs from the log streams in this list.

    # If you specify a value for both `logStreamNamePrefix` and `logStreamNames`,
    # but the value for `logStreamNamePrefix` does not match any log stream names
    # specified in `logStreamNames`, the action returns an
    # `InvalidParameterException` error.
    log_stream_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters the results to include only events from log streams that have names
    # starting with this prefix.

    # If you specify a value for both `logStreamNamePrefix` and `logStreamNames`,
    # but the value for `logStreamNamePrefix` does not match any log stream names
    # specified in `logStreamNames`, the action returns an
    # `InvalidParameterException` error.
    log_stream_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not
    # returned.
    start_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are
    # not returned.
    end_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter pattern to use. For more information, see [Filter and Pattern
    # Syntax](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

    # If not provided, all the events are matched.
    filter_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of events to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of events to return. The default is 10,000 events.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the value is true, the operation makes a best effort to provide
    # responses that contain events from multiple log streams within the log
    # group, interleaved in a single response. If the value is false, all the
    # matched log events in the first log stream are searched first, then those
    # in the next log stream, and so on. The default is false.
    interleaved: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FilterLogEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "events",
                TypeInfo(typing.List[FilteredLogEvent]),
            ),
            (
                "searched_log_streams",
                "searchedLogStreams",
                TypeInfo(typing.List[SearchedLogStream]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The matched events.
    events: typing.List["FilteredLogEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates which log streams have been searched and whether each has been
    # searched completely.
    searched_log_streams: typing.List["SearchedLogStream"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. The token expires
    # after 24 hours.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["FilterLogEventsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class FilteredLogEvent(ShapeBase):
    """
    Represents a matched event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "timestamp",
                TypeInfo(int),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "ingestion_time",
                "ingestionTime",
                TypeInfo(int),
            ),
            (
                "event_id",
                "eventId",
                TypeInfo(str),
            ),
        ]

    # The name of the log stream this event belongs to.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the event occurred, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data contained in the log event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the event was ingested, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    ingestion_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the event.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLogEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(int),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
            (
                "start_from_head",
                "startFromHead",
                TypeInfo(bool),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp equal to this time or
    # later than this time are included. Events with a time stamp earlier than
    # this time are not included.
    start_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end of the time range, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC. Events with a time stamp equal to or later than
    # this time are not included.
    end_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of log events returned. If you don't specify a value,
    # the maximum is as many log events as can fit in a response size of 1 MB, up
    # to 10,000 log events.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the value is true, the earliest log events are returned first. If the
    # value is false, the latest log events are returned first. The default value
    # is false.
    start_from_head: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLogEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "events",
                TypeInfo(typing.List[OutputLogEvent]),
            ),
            (
                "next_forward_token",
                "nextForwardToken",
                TypeInfo(str),
            ),
            (
                "next_backward_token",
                "nextBackwardToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The events.
    events: typing.List["OutputLogEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items in the forward direction. The token
    # expires after 24 hours. If you have reached the end of the stream, it will
    # return the same token you passed in.
    next_forward_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items in the backward direction. The token
    # expires after 24 hours. This token will never be null. If you have reached
    # the end of the stream, it will return the same token you passed in.
    next_backward_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputLogEvent(ShapeBase):
    """
    Represents a log event, which is a record of activity that was recorded by the
    application or resource being monitored.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "timestamp",
                TypeInfo(int),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The time the event occurred, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The raw event message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOperationException(ShapeBase):
    """
    The operation is not valid on the specified resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    A parameter is specified incorrectly.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSequenceTokenException(ShapeBase):
    """
    The sequence token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expected_sequence_token",
                "expectedSequenceToken",
                TypeInfo(str),
            ),
        ]

    expected_sequence_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    You have reached the maximum number of resources that can be created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListTagsLogGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsLogGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags for the log group.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogGroup(ShapeBase):
    """
    Represents a log group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(int),
            ),
            (
                "retention_in_days",
                "retentionInDays",
                TypeInfo(int),
            ),
            (
                "metric_filter_count",
                "metricFilterCount",
                TypeInfo(int),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "stored_bytes",
                "storedBytes",
                TypeInfo(int),
            ),
            (
                "kms_key_id",
                "kmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The creation time of the log group, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days to retain the log events in the specified log group.
    # Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400,
    # 545, 731, 1827, and 3653.
    retention_in_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of metric filters.
    metric_filter_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the log group.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of bytes stored.
    stored_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogStream(ShapeBase):
    """
    Represents a log stream, which is a sequence of log events from a single emitter
    of logs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(int),
            ),
            (
                "first_event_timestamp",
                "firstEventTimestamp",
                TypeInfo(int),
            ),
            (
                "last_event_timestamp",
                "lastEventTimestamp",
                TypeInfo(int),
            ),
            (
                "last_ingestion_time",
                "lastIngestionTime",
                TypeInfo(int),
            ),
            (
                "upload_sequence_token",
                "uploadSequenceToken",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "stored_bytes",
                "storedBytes",
                TypeInfo(int),
            ),
        ]

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The creation time of the stream, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time of the first event, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    first_event_timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # the time of the most recent log event in the log stream in CloudWatch Logs.
    # This number is expressed as the number of milliseconds after Jan 1, 1970
    # 00:00:00 UTC. lastEventTime updates on an eventual consistency basis. It
    # typically updates in less than an hour from ingestion, but may take longer
    # in some rare situations.
    last_event_timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ingestion time, expressed as the number of milliseconds after Jan 1,
    # 1970 00:00:00 UTC.
    last_ingestion_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sequence token.
    upload_sequence_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the log stream.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of bytes stored.
    stored_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricFilter(ShapeBase):
    """
    Metric filters express how CloudWatch Logs would extract metric observations
    from ingested log events and transform them into metric data in a CloudWatch
    metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_name",
                "filterName",
                TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                TypeInfo(str),
            ),
            (
                "metric_transformations",
                "metricTransformations",
                TypeInfo(typing.List[MetricTransformation]),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(int),
            ),
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the metric filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A symbolic description of how CloudWatch Logs should interpret the data in
    # each log event. For example, a log event may contain time stamps, IP
    # addresses, strings, and so on. You use the filter pattern to specify what
    # to look for in the log event message.
    filter_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metric transformations.
    metric_transformations: typing.List["MetricTransformation"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The creation time of the metric filter, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricFilterMatchRecord(ShapeBase):
    """
    Represents a matched event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_number",
                "eventNumber",
                TypeInfo(int),
            ),
            (
                "event_message",
                "eventMessage",
                TypeInfo(str),
            ),
            (
                "extracted_values",
                "extractedValues",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The event number.
    event_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The raw event data.
    event_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The values extracted from the event data by the filter.
    extracted_values: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricTransformation(ShapeBase):
    """
    Indicates how to transform ingested log events in to metric data in a CloudWatch
    metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "metricName",
                TypeInfo(str),
            ),
            (
                "metric_namespace",
                "metricNamespace",
                TypeInfo(str),
            ),
            (
                "metric_value",
                "metricValue",
                TypeInfo(str),
            ),
            (
                "default_value",
                "defaultValue",
                TypeInfo(float),
            ),
        ]

    # The name of the CloudWatch metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the CloudWatch metric.
    metric_namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value to publish to the CloudWatch metric when a filter pattern matches
    # a log event.
    metric_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The value to emit when a filter pattern does not match a log
    # event. This value can be null.
    default_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationAbortedException(ShapeBase):
    """
    Multiple requests to update the same resource were in conflict.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class OrderBy(str):
    LogStreamName = "LogStreamName"
    LastEventTime = "LastEventTime"


@dataclasses.dataclass
class OutputLogEvent(ShapeBase):
    """
    Represents a log event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "timestamp",
                TypeInfo(int),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "ingestion_time",
                "ingestionTime",
                TypeInfo(int),
            ),
        ]

    # The time the event occurred, expressed as the number of milliseconds after
    # Jan 1, 1970 00:00:00 UTC.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data contained in the log event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the event was ingested, expressed as the number of milliseconds
    # after Jan 1, 1970 00:00:00 UTC.
    ingestion_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDestinationPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                TypeInfo(str),
            ),
            (
                "access_policy",
                "accessPolicy",
                TypeInfo(str),
            ),
        ]

    # A name for an existing destination.
    destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM policy document that authorizes cross-account users to deliver their
    # log events to the associated destination.
    access_policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDestinationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_name",
                "destinationName",
                TypeInfo(str),
            ),
            (
                "target_arn",
                "targetArn",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
        ]

    # A name for the destination.
    destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an Amazon Kinesis stream to which to deliver matching log
    # events.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM role that grants CloudWatch Logs permissions to call the
    # Amazon Kinesis PutRecord operation on the destination stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDestinationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "destination",
                "destination",
                TypeInfo(Destination),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination.
    destination: "Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutLogEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
            (
                "log_events",
                "logEvents",
                TypeInfo(typing.List[InputLogEvent]),
            ),
            (
                "sequence_token",
                "sequenceToken",
                TypeInfo(str),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The log events.
    log_events: typing.List["InputLogEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sequence token obtained from the response of the previous
    # `PutLogEvents` call. An upload in a newly created log stream does not
    # require a sequence token. You can also get the sequence token using
    # DescribeLogStreams. If you call `PutLogEvents` twice within a narrow time
    # period using the same value for `sequenceToken`, both calls may be
    # successful, or one may be rejected.
    sequence_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutLogEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_sequence_token",
                "nextSequenceToken",
                TypeInfo(str),
            ),
            (
                "rejected_log_events_info",
                "rejectedLogEventsInfo",
                TypeInfo(RejectedLogEventsInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The next sequence token.
    next_sequence_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rejected events.
    rejected_log_events_info: "RejectedLogEventsInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutMetricFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                TypeInfo(str),
            ),
            (
                "metric_transformations",
                "metricTransformations",
                TypeInfo(typing.List[MetricTransformation]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the metric filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter pattern for extracting metric data out of ingested log events.
    filter_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of information that defines how metric data gets emitted.
    metric_transformations: typing.List["MetricTransformation"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class PutResourcePolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                TypeInfo(str),
            ),
        ]

    # Name of the new policy. This parameter is required.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details of the new policy, including the identity of the principal that is
    # enabled to put logs to this account. This is formatted as a JSON string.

    # The following example creates a resource policy enabling the Route 53
    # service to put DNS query logs in to the specified log group. Replace
    # "logArn" with the ARN of your CloudWatch Logs resource, such as a log group
    # or log stream.

    # `{ "Version": "2012-10-17", "Statement": [ { "Sid":
    # "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service":
    # [ "route53.amazonaws.com" ] }, "Action":"logs:PutLogEvents", "Resource":
    # "logArn" } ] } `
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutResourcePolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_policy",
                "resourcePolicy",
                TypeInfo(ResourcePolicy),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new policy.
    resource_policy: "ResourcePolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRetentionPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "retention_in_days",
                "retentionInDays",
                TypeInfo(int),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days to retain the log events in the specified log group.
    # Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400,
    # 545, 731, 1827, and 3653.
    retention_in_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSubscriptionFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "filterName",
                TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                TypeInfo(str),
            ),
            (
                "destination_arn",
                "destinationArn",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "distribution",
                "distribution",
                TypeInfo(typing.Union[str, Distribution]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the subscription filter. If you are updating an existing filter,
    # you must specify the correct name in `filterName`. Otherwise, the call
    # fails because you cannot associate a second filter with a log group. To
    # find the name of the filter currently associated with a log group, use
    # DescribeSubscriptionFilters.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter pattern for subscribing to a filtered stream of log events.
    filter_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the destination to deliver matching log events to. Currently,
    # the supported destinations are:

    #   * An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.

    #   * A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.

    #   * An Amazon Kinesis Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery.

    #   * An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
    destination_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM role that grants CloudWatch Logs permissions to deliver
    # ingested log events to the destination stream. You don't need to provide
    # the ARN when you are working with a logical destination for cross-account
    # delivery.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The method used to distribute log data to the destination. By default log
    # data is grouped by log stream, but the grouping can be set to random for a
    # more even distribution. This property is only applicable when the
    # destination is an Amazon Kinesis stream.
    distribution: typing.Union[str, "Distribution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RejectedLogEventsInfo(ShapeBase):
    """
    Represents the rejected events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "too_new_log_event_start_index",
                "tooNewLogEventStartIndex",
                TypeInfo(int),
            ),
            (
                "too_old_log_event_end_index",
                "tooOldLogEventEndIndex",
                TypeInfo(int),
            ),
            (
                "expired_log_event_end_index",
                "expiredLogEventEndIndex",
                TypeInfo(int),
            ),
        ]

    # The log events that are too new.
    too_new_log_event_start_index: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log events that are too old.
    too_old_log_event_end_index: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The expired log events.
    expired_log_event_end_index: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    The specified resource already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourcePolicy(ShapeBase):
    """
    A policy enabling one or more entities to put logs to a log group in this
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "policyName",
                TypeInfo(str),
            ),
            (
                "policy_document",
                "policyDocument",
                TypeInfo(str),
            ),
            (
                "last_updated_time",
                "lastUpdatedTime",
                TypeInfo(int),
            ),
        ]

    # The name of the resource policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The details of the policy.
    policy_document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp showing when this policy was last updated, expressed as the
    # number of milliseconds after Jan 1, 1970 00:00:00 UTC.
    last_updated_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchedLogStream(ShapeBase):
    """
    Represents the search status of a log stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
            (
                "searched_completely",
                "searchedCompletely",
                TypeInfo(bool),
            ),
        ]

    # The name of the log stream.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether all the events in this log stream were searched.
    searched_completely: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The service cannot complete the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionFilter(ShapeBase):
    """
    Represents a subscription filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_name",
                "filterName",
                TypeInfo(str),
            ),
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "filter_pattern",
                "filterPattern",
                TypeInfo(str),
            ),
            (
                "destination_arn",
                "destinationArn",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "distribution",
                "distribution",
                TypeInfo(typing.Union[str, Distribution]),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(int),
            ),
        ]

    # The name of the subscription filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A symbolic description of how CloudWatch Logs should interpret the data in
    # each log event. For example, a log event may contain time stamps, IP
    # addresses, strings, and so on. You use the filter pattern to specify what
    # to look for in the log event message.
    filter_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the destination.
    destination_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The method used to distribute log data to the destination, which can be
    # either random or grouped by log stream.
    distribution: typing.Union[str, "Distribution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation time of the subscription filter, expressed as the number of
    # milliseconds after Jan 1, 1970 00:00:00 UTC.
    creation_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagLogGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value pairs to use for the tags.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestMetricFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_pattern",
                "filterPattern",
                TypeInfo(str),
            ),
            (
                "log_event_messages",
                "logEventMessages",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A symbolic description of how CloudWatch Logs should interpret the data in
    # each log event. For example, a log event may contain time stamps, IP
    # addresses, strings, and so on. You use the filter pattern to specify what
    # to look for in the log event message.
    filter_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The log event messages to test.
    log_event_messages: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestMetricFilterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "matches",
                "matches",
                TypeInfo(typing.List[MetricFilterMatchRecord]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The matched events.
    matches: typing.List["MetricFilterMatchRecord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnrecognizedClientException(ShapeBase):
    """
    The most likely cause is an invalid AWS access key ID or secret key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagLogGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_group_name",
                "logGroupName",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the log group.
    log_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag keys. The corresponding tags are removed from the log group.
    tags: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
