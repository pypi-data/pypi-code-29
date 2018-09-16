import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddTagsRequest(ShapeBase):
    """
    Specifies the tags to add to a trail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tags_list",
                "TagsList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the ARN of the trail to which one or more tags will be added. The
    # format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of CloudTrail tags, up to a limit of 50
    tags_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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


class ByteBuffer(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CloudTrailARNInvalidException(ShapeBase):
    """
    This exception is thrown when an operation is called with an invalid trail ARN.
    The format of a trail ARN is:

    `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CloudWatchLogsDeliveryUnavailableException(ShapeBase):
    """
    Cannot set a CloudWatch Logs delivery for this region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateTrailRequest(ShapeBase):
    """
    Specifies the settings for each trail.
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
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "sns_topic_name",
                "SnsTopicName",
                TypeInfo(str),
            ),
            (
                "include_global_service_events",
                "IncludeGlobalServiceEvents",
                TypeInfo(bool),
            ),
            (
                "is_multi_region_trail",
                "IsMultiRegionTrail",
                TypeInfo(bool),
            ),
            (
                "enable_log_file_validation",
                "EnableLogFileValidation",
                TypeInfo(bool),
            ),
            (
                "cloud_watch_logs_log_group_arn",
                "CloudWatchLogsLogGroupArn",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # Specifies the name of the trail. The name must meet the following
    # requirements:

    #   * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)

    #   * Start with a letter or number, and end with a letter or number

    #   * Be between 3 and 128 characters

    #   * Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are invalid.

    #   * Not be in IP address format (for example, 192.168.5.4)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Amazon S3 bucket designated for publishing log
    # files. See [Amazon S3 Bucket Naming
    # Requirements](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html).
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Amazon S3 key prefix that comes after the name of the bucket
    # you have designated for log file delivery. For more information, see
    # [Finding Your CloudTrail Log
    # Files](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
    # find-log-files.html). The maximum length is 200 characters.
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Amazon SNS topic defined for notification of log
    # file delivery. The maximum length is 256 characters.
    sns_topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the trail is publishing events from global services such
    # as IAM to the log files.
    include_global_service_events: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the trail is created in the current region or in all
    # regions. The default is false.
    is_multi_region_trail: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether log file integrity validation is enabled. The default is
    # false.

    # When you disable log file integrity validation, the chain of digest files
    # is broken after one hour. CloudTrail will not create digest files for log
    # files that were delivered during a period in which log file integrity
    # validation was disabled. For example, if you enable log file integrity
    # validation at noon on January 1, disable it at noon on January 2, and re-
    # enable it at noon on January 10, digest files will not be created for the
    # log files delivered from noon on January 2 to noon on January 10. The same
    # applies whenever you stop CloudTrail logging or delete a trail.
    enable_log_file_validation: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a log group name using an Amazon Resource Name (ARN), a unique
    # identifier that represents the log group to which CloudTrail logs will be
    # delivered. Not required unless you specify CloudWatchLogsRoleArn.
    cloud_watch_logs_log_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the role for the CloudWatch Logs endpoint to assume to write to a
    # user's log group.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the KMS key ID to use to encrypt the logs delivered by
    # CloudTrail. The value can be an alias name prefixed by "alias/", a fully
    # specified ARN to an alias, a fully specified ARN to a key, or a globally
    # unique identifier.

    # Examples:

    #   * alias/MyAliasName

    #   * arn:aws:kms:us-east-1:123456789012:alias/MyAliasName

    #   * arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012

    #   * 12345678-1234-1234-1234-123456789012
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTrailResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "sns_topic_name",
                "SnsTopicName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicARN",
                TypeInfo(str),
            ),
            (
                "include_global_service_events",
                "IncludeGlobalServiceEvents",
                TypeInfo(bool),
            ),
            (
                "is_multi_region_trail",
                "IsMultiRegionTrail",
                TypeInfo(bool),
            ),
            (
                "trail_arn",
                "TrailARN",
                TypeInfo(str),
            ),
            (
                "log_file_validation_enabled",
                "LogFileValidationEnabled",
                TypeInfo(bool),
            ),
            (
                "cloud_watch_logs_log_group_arn",
                "CloudWatchLogsLogGroupArn",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the trail.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Amazon S3 bucket designated for publishing log
    # files.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Amazon S3 key prefix that comes after the name of the bucket
    # you have designated for log file delivery. For more information, see
    # [Finding Your CloudTrail Log
    # Files](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
    # find-log-files.html).
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is deprecated. Use SnsTopicARN.
    sns_topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send
    # notifications when log files are delivered. The format of a topic ARN is:

    # `arn:aws:sns:us-east-1:123456789012:MyTopic`
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the trail is publishing events from global services such
    # as IAM to the log files.
    include_global_service_events: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the trail exists in one region or in all regions.
    is_multi_region_trail: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ARN of the trail that was created. The format of a trail ARN
    # is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    trail_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether log file integrity validation is enabled.
    log_file_validation_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Amazon Resource Name (ARN) of the log group to which
    # CloudTrail logs will be delivered.
    cloud_watch_logs_log_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the role for the CloudWatch Logs endpoint to assume to write to a
    # user's log group.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the KMS key ID that encrypts the logs delivered by CloudTrail.
    # The value is a fully specified ARN to a KMS key in the format:

    # `arn:aws:kms:us-
    # east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataResource(ShapeBase):
    """
    The Amazon S3 objects that you specify in your event selectors for your trail to
    log data events. Data events are object-level API operations that access S3
    objects, such as `GetObject`, `DeleteObject`, and `PutObject`. You can specify
    up to 250 S3 buckets and object prefixes for a trail.

    Example

      1. You create an event selector for a trail and specify an S3 bucket and an empty prefix, such as `arn:aws:s3:::bucket-1/`.

      2. You upload an image file to `bucket-1`.

      3. The `PutObject` API operation occurs on an object in the S3 bucket that you specified in the event selector. The trail processes and logs the event.

      4. You upload another image file to a different S3 bucket named `arn:aws:s3:::bucket-2`.

      5. The event occurs on an object in an S3 bucket that you didn't specify in the event selector. The trail doesn’t log the event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The resource type in which you want to log data events. You can specify
    # only the following value: `AWS::S3::Object`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ARN-like strings for the specified S3 objects.

    # To log data events for all objects in an S3 bucket, specify the bucket and
    # an empty object prefix such as `arn:aws:s3:::bucket-1/`. The trail logs
    # data events for all objects in this S3 bucket.

    # To log data events for specific objects, specify the S3 bucket and object
    # prefix such as `arn:aws:s3:::bucket-1/example-images`. The trail logs data
    # events for objects in this S3 bucket that match the prefix.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTrailRequest(ShapeBase):
    """
    The request that specifies the name of a trail to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Specifies the name or the CloudTrail ARN of the trail to be deleted. The
    # format of a trail ARN is: `arn:aws:cloudtrail:us-
    # east-1:123456789012:trail/MyTrail`
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTrailResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
class DescribeTrailsRequest(ShapeBase):
    """
    Returns information about the trail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trail_name_list",
                "trailNameList",
                TypeInfo(typing.List[str]),
            ),
            (
                "include_shadow_trails",
                "includeShadowTrails",
                TypeInfo(bool),
            ),
        ]

    # Specifies a list of trail names, trail ARNs, or both, of the trails to
    # describe. The format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`

    # If an empty list is specified, information for the trail in the current
    # region is returned.

    #   * If an empty list is specified and `IncludeShadowTrails` is false, then information for all trails in the current region is returned.

    #   * If an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current region and any associated shadow trails in other regions is returned.

    # If one or more trail names are specified, information is returned only if
    # the names match the names of trails belonging only to the current region.
    # To return information about a trail in another region, you must specify its
    # trail ARN.
    trail_name_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether to include shadow trails in the response. A shadow trail
    # is the replication in a region of a trail that was created in a different
    # region. The default is true.
    include_shadow_trails: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrailsResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
                "trail_list",
                "trailList",
                TypeInfo(typing.List[Trail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of trail objects.
    trail_list: typing.List["Trail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Event(ShapeBase):
    """
    Contains information about an event that was returned by a lookup request. The
    result includes a representation of a CloudTrail event.
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
                "event_name",
                "EventName",
                TypeInfo(str),
            ),
            (
                "event_time",
                "EventTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "event_source",
                "EventSource",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[Resource]),
            ),
            (
                "cloud_trail_event",
                "CloudTrailEvent",
                TypeInfo(str),
            ),
        ]

    # The CloudTrail ID of the event returned.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the event returned.
    event_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time of the event returned.
    event_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS service that the request was made to.
    event_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user name or role name of the requester that called the API in the event
    # returned.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of resources referenced by the event returned.
    resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A JSON string that contains a representation of the event returned.
    cloud_trail_event: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSelector(ShapeBase):
    """
    Use event selectors to specify whether you want your trail to log management
    and/or data events. When an event occurs in your account, CloudTrail evaluates
    the event selector for all trails. For each trail, if the event matches any
    event selector, the trail processes and logs the event. If the event doesn't
    match any event selector, the trail doesn't log the event.

    You can configure up to five event selectors for a trail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "read_write_type",
                "ReadWriteType",
                TypeInfo(typing.Union[str, ReadWriteType]),
            ),
            (
                "include_management_events",
                "IncludeManagementEvents",
                TypeInfo(bool),
            ),
            (
                "data_resources",
                "DataResources",
                TypeInfo(typing.List[DataResource]),
            ),
        ]

    # Specify if you want your trail to log read-only events, write-only events,
    # or all. For example, the EC2 `GetConsoleOutput` is a read-only API
    # operation and `RunInstances` is a write-only API operation.

    # By default, the value is `All`.
    read_write_type: typing.Union[str, "ReadWriteType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify if you want your event selector to include management events for
    # your trail.

    # For more information, see [Management
    # Events](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-
    # management-and-data-events-with-cloudtrail.html#logging-management-events)
    # in the _AWS CloudTrail User Guide_.

    # By default, the value is `true`.
    include_management_events: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # CloudTrail supports logging only data events for S3 objects. You can
    # specify up to 250 S3 buckets and object prefixes for a trail.

    # For more information, see [Data
    # Events](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-
    # management-and-data-events-with-cloudtrail.html#logging-data-events) in the
    # _AWS CloudTrail User Guide_.
    data_resources: typing.List["DataResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetEventSelectorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trail_name",
                "TrailName",
                TypeInfo(str),
            ),
        ]

    # Specifies the name of the trail or trail ARN. If you specify a trail name,
    # the string must meet the following requirements:

    #   * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)

    #   * Start with a letter or number, and end with a letter or number

    #   * Be between 3 and 128 characters

    #   * Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are invalid.

    #   * Not be in IP address format (for example, 192.168.5.4)

    # If you specify a trail ARN, it must be in the format:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    trail_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEventSelectorsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "trail_arn",
                "TrailARN",
                TypeInfo(str),
            ),
            (
                "event_selectors",
                "EventSelectors",
                TypeInfo(typing.List[EventSelector]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specified trail ARN that has the event selectors.
    trail_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event selectors that are configured for the trail.
    event_selectors: typing.List["EventSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTrailStatusRequest(ShapeBase):
    """
    The name of a trail about which you want the current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Specifies the name or the CloudTrail ARN of the trail for which you are
    # requesting status. To get the status of a shadow trail (a replication of
    # the trail in another region), you must specify its ARN. The format of a
    # trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTrailStatusResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
                "is_logging",
                "IsLogging",
                TypeInfo(bool),
            ),
            (
                "latest_delivery_error",
                "LatestDeliveryError",
                TypeInfo(str),
            ),
            (
                "latest_notification_error",
                "LatestNotificationError",
                TypeInfo(str),
            ),
            (
                "latest_delivery_time",
                "LatestDeliveryTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "latest_notification_time",
                "LatestNotificationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "start_logging_time",
                "StartLoggingTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stop_logging_time",
                "StopLoggingTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "latest_cloud_watch_logs_delivery_error",
                "LatestCloudWatchLogsDeliveryError",
                TypeInfo(str),
            ),
            (
                "latest_cloud_watch_logs_delivery_time",
                "LatestCloudWatchLogsDeliveryTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "latest_digest_delivery_time",
                "LatestDigestDeliveryTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "latest_digest_delivery_error",
                "LatestDigestDeliveryError",
                TypeInfo(str),
            ),
            (
                "latest_delivery_attempt_time",
                "LatestDeliveryAttemptTime",
                TypeInfo(str),
            ),
            (
                "latest_notification_attempt_time",
                "LatestNotificationAttemptTime",
                TypeInfo(str),
            ),
            (
                "latest_notification_attempt_succeeded",
                "LatestNotificationAttemptSucceeded",
                TypeInfo(str),
            ),
            (
                "latest_delivery_attempt_succeeded",
                "LatestDeliveryAttemptSucceeded",
                TypeInfo(str),
            ),
            (
                "time_logging_started",
                "TimeLoggingStarted",
                TypeInfo(str),
            ),
            (
                "time_logging_stopped",
                "TimeLoggingStopped",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the CloudTrail is currently logging AWS API calls.
    is_logging: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Displays any Amazon S3 error that CloudTrail encountered when attempting to
    # deliver log files to the designated bucket. For more information see the
    # topic [Error
    # Responses](http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html)
    # in the Amazon S3 API Reference.

    # This error occurs only when there is a problem with the destination S3
    # bucket and will not occur for timeouts. To resolve the issue, create a new
    # bucket and call `UpdateTrail` to specify the new bucket, or fix the
    # existing objects so that CloudTrail can again write to the bucket.
    latest_delivery_error: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Displays any Amazon SNS error that CloudTrail encountered when attempting
    # to send a notification. For more information about Amazon SNS errors, see
    # the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/welcome.html).
    latest_notification_error: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the date and time that CloudTrail last delivered log files to an
    # account's Amazon S3 bucket.
    latest_delivery_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the date and time of the most recent Amazon SNS notification that
    # CloudTrail has written a new log file to an account's Amazon S3 bucket.
    latest_notification_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the most recent date and time when CloudTrail started recording
    # API calls for an AWS account.
    start_logging_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the most recent date and time when CloudTrail stopped recording
    # API calls for an AWS account.
    stop_logging_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Displays any CloudWatch Logs error that CloudTrail encountered when
    # attempting to deliver logs to CloudWatch Logs.
    latest_cloud_watch_logs_delivery_error: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Displays the most recent date and time when CloudTrail delivered logs to
    # CloudWatch Logs.
    latest_cloud_watch_logs_delivery_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the date and time that CloudTrail last delivered a digest file to
    # an account's Amazon S3 bucket.
    latest_digest_delivery_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Displays any Amazon S3 error that CloudTrail encountered when attempting to
    # deliver a digest file to the designated bucket. For more information see
    # the topic [Error
    # Responses](http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html)
    # in the Amazon S3 API Reference.

    # This error occurs only when there is a problem with the destination S3
    # bucket and will not occur for timeouts. To resolve the issue, create a new
    # bucket and call `UpdateTrail` to specify the new bucket, or fix the
    # existing objects so that CloudTrail can again write to the bucket.
    latest_digest_delivery_error: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is deprecated.
    latest_delivery_attempt_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is deprecated.
    latest_notification_attempt_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is deprecated.
    latest_notification_attempt_succeeded: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is deprecated.
    latest_delivery_attempt_succeeded: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is deprecated.
    time_logging_started: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is deprecated.
    time_logging_stopped: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InsufficientEncryptionPolicyException(ShapeBase):
    """
    This exception is thrown when the policy on the S3 bucket or KMS key is not
    sufficient.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientS3BucketPolicyException(ShapeBase):
    """
    This exception is thrown when the policy on the S3 bucket is not sufficient.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientSnsTopicPolicyException(ShapeBase):
    """
    This exception is thrown when the policy on the SNS topic is not sufficient.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCloudWatchLogsLogGroupArnException(ShapeBase):
    """
    This exception is thrown when the provided CloudWatch log group is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCloudWatchLogsRoleArnException(ShapeBase):
    """
    This exception is thrown when the provided role is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEventSelectorsException(ShapeBase):
    """
    This exception is thrown when the `PutEventSelectors` operation is called with
    an invalid number of event selectors, data resources, or an invalid value for a
    parameter:

      * Specify a valid number of event selectors (1 to 5) for a trail.

      * Specify a valid number of data resources (1 to 250) for an event selector.

      * Specify a valid value for a parameter. For example, specifying the `ReadWriteType` parameter with a value of `read-only` is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidHomeRegionException(ShapeBase):
    """
    This exception is thrown when an operation is called on a trail from a region
    other than the region in which the trail was created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidKmsKeyIdException(ShapeBase):
    """
    This exception is thrown when the KMS key ARN is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidLookupAttributesException(ShapeBase):
    """
    Occurs when an invalid lookup attribute is specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMaxResultsException(ShapeBase):
    """
    This exception is thrown if the limit specified is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    Invalid token or token that was previously used in a request with different
    parameters. This exception is thrown if the token is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterCombinationException(ShapeBase):
    """
    This exception is thrown when the combination of parameters provided is not
    valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3BucketNameException(ShapeBase):
    """
    This exception is thrown when the provided S3 bucket name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3PrefixException(ShapeBase):
    """
    This exception is thrown when the provided S3 prefix is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSnsTopicNameException(ShapeBase):
    """
    This exception is thrown when the provided SNS topic name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTagParameterException(ShapeBase):
    """
    This exception is thrown when the key or value specified for the tag does not
    match the regular expression `^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTimeRangeException(ShapeBase):
    """
    Occurs if the timestamp values are invalid. Either the start time occurs after
    the end time or the time range is outside the range of possible values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTokenException(ShapeBase):
    """
    Reserved for future use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTrailNameException(ShapeBase):
    """
    This exception is thrown when the provided trail name is not valid. Trail names
    must meet the following requirements:

      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)

      * Start with a letter or number, and end with a letter or number

      * Be between 3 and 128 characters

      * Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are invalid.

      * Not be in IP address format (for example, 192.168.5.4)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KmsException(ShapeBase):
    """
    This exception is thrown when there is an issue with the specified KMS key and
    the trail can’t be updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KmsKeyDisabledException(ShapeBase):
    """
    This exception is deprecated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KmsKeyNotFoundException(ShapeBase):
    """
    This exception is thrown when the KMS key does not exist, or when the S3 bucket
    and the KMS key are not in the same region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListPublicKeysRequest(ShapeBase):
    """
    Requests the public keys for a specified time range.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Optionally specifies, in UTC, the start of the time range to look up public
    # keys for CloudTrail digest files. If not specified, the current time is
    # used, and the current public key is returned.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optionally specifies, in UTC, the end of the time range to look up public
    # keys for CloudTrail digest files. If not specified, the current time is
    # used.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPublicKeysResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
                "public_key_list",
                "PublicKeyList",
                TypeInfo(typing.List[PublicKey]),
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

    # Contains an array of PublicKey objects.

    # The returned public keys may have validity time ranges that overlap.
    public_key_list: typing.List["PublicKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsRequest(ShapeBase):
    """
    Specifies a list of trail tags to return.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id_list",
                "ResourceIdList",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Specifies a list of trail ARNs whose tags will be listed. The list has a
    # limit of 20 ARNs. The format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    resource_id_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
                "resource_tag_list",
                "ResourceTagList",
                TypeInfo(typing.List[ResourceTag]),
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

    # A list of resource tags.
    resource_tag_list: typing.List["ResourceTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupAttribute(ShapeBase):
    """
    Specifies an attribute and value that filter the events returned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_key",
                "AttributeKey",
                TypeInfo(typing.Union[str, LookupAttributeKey]),
            ),
            (
                "attribute_value",
                "AttributeValue",
                TypeInfo(str),
            ),
        ]

    # Specifies an attribute on which to filter the events returned.
    attribute_key: typing.Union[str, "LookupAttributeKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a value for the specified AttributeKey.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LookupAttributeKey(str):
    EventId = "EventId"
    EventName = "EventName"
    Username = "Username"
    ResourceType = "ResourceType"
    ResourceName = "ResourceName"
    EventSource = "EventSource"


@dataclasses.dataclass
class LookupEventsRequest(ShapeBase):
    """
    Contains a request for LookupEvents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lookup_attributes",
                "LookupAttributes",
                TypeInfo(typing.List[LookupAttribute]),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
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

    # Contains a list of lookup attributes. Currently the list can contain only
    # one item.
    lookup_attributes: typing.List["LookupAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies that only events that occur after or at the specified time are
    # returned. If the specified start time is after the specified end time, an
    # error is returned.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies that only events that occur before or at the specified time are
    # returned. If the specified end time is before the specified start time, an
    # error is returned.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of events to return. Possible values are 1 through 50. The
    # default is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to get the next page of results after a previous API call.
    # This token must be passed in with the same parameters that were specified
    # in the the original call. For example, if the original call specified an
    # AttributeKey of 'Username' with a value of 'root', the call with NextToken
    # should include those same parameters.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupEventsResponse(OutputShapeBase):
    """
    Contains a response to a LookupEvents action.
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
                "events",
                "Events",
                TypeInfo(typing.List[Event]),
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

    # A list of events returned based on the lookup attributes specified and the
    # CloudTrail event. The events list is sorted by time. The most recent event
    # is listed first.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use to get the next page of results after a previous API call.
    # If the token does not appear, there are no more results to return. The
    # token must be passed in with the same parameters as the previous call. For
    # example, if the original call specified an AttributeKey of 'Username' with
    # a value of 'root', the call with NextToken should include those same
    # parameters.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["LookupEventsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MaximumNumberOfTrailsExceededException(ShapeBase):
    """
    This exception is thrown when the maximum number of trails is reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OperationNotPermittedException(ShapeBase):
    """
    This exception is thrown when the requested operation is not permitted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PublicKey(ShapeBase):
    """
    Contains information about a returned public key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(typing.Any),
            ),
            (
                "validity_start_time",
                "ValidityStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "validity_end_time",
                "ValidityEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "fingerprint",
                "Fingerprint",
                TypeInfo(str),
            ),
        ]

    # The DER encoded public key value in PKCS#1 format.
    value: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting time of validity of the public key.
    validity_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ending time of validity of the public key.
    validity_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fingerprint of the public key.
    fingerprint: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEventSelectorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trail_name",
                "TrailName",
                TypeInfo(str),
            ),
            (
                "event_selectors",
                "EventSelectors",
                TypeInfo(typing.List[EventSelector]),
            ),
        ]

    # Specifies the name of the trail or trail ARN. If you specify a trail name,
    # the string must meet the following requirements:

    #   * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)

    #   * Start with a letter or number, and end with a letter or number

    #   * Be between 3 and 128 characters

    #   * Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are invalid.

    #   * Not be in IP address format (for example, 192.168.5.4)

    # If you specify a trail ARN, it must be in the format:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    trail_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the settings for your event selectors. You can configure up to
    # five event selectors for a trail.
    event_selectors: typing.List["EventSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutEventSelectorsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "trail_arn",
                "TrailARN",
                TypeInfo(str),
            ),
            (
                "event_selectors",
                "EventSelectors",
                TypeInfo(typing.List[EventSelector]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the ARN of the trail that was updated with event selectors. The
    # format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    trail_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the event selectors configured for your trail.
    event_selectors: typing.List["EventSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReadWriteType(str):
    ReadOnly = "ReadOnly"
    WriteOnly = "WriteOnly"
    All = "All"


@dataclasses.dataclass
class RemoveTagsRequest(ShapeBase):
    """
    Specifies the tags to remove from a trail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tags_list",
                "TagsList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the ARN of the trail from which tags should be removed. The
    # format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a list of tags to be removed.
    tags_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
class Resource(ShapeBase):
    """
    Specifies the type and name of a resource referenced by an event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "resource_name",
                "ResourceName",
                TypeInfo(str),
            ),
        ]

    # The type of a resource referenced by the event returned. When the resource
    # type cannot be determined, null is returned. Some examples of resource
    # types are: **Instance** for EC2, **Trail** for CloudTrail, **DBInstance**
    # for RDS, and **AccessKey** for IAM. For a list of resource types supported
    # for event lookup, see [Resource Types Supported for Event
    # Lookup](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/lookup_supported_resourcetypes.html).
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the resource referenced by the event returned. These are user-
    # created names whose values will depend on the environment. For example, the
    # resource name might be "auto-scaling-test-group" for an Auto Scaling Group
    # or "i-1234567" for an EC2 Instance.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    This exception is thrown when the specified resource is not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceTag(ShapeBase):
    """
    A resource tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tags_list",
                "TagsList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the ARN of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags.
    tags_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceTypeNotSupportedException(ShapeBase):
    """
    This exception is thrown when the specified resource type is not supported by
    CloudTrail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class S3BucketDoesNotExistException(ShapeBase):
    """
    This exception is thrown when the specified S3 bucket does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StartLoggingRequest(ShapeBase):
    """
    The request to CloudTrail to start logging AWS API calls for an account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Specifies the name or the CloudTrail ARN of the trail for which CloudTrail
    # logs AWS API calls. The format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartLoggingResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
class StopLoggingRequest(ShapeBase):
    """
    Passes the request to CloudTrail to stop logging AWS API calls for the specified
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Specifies the name or the CloudTrail ARN of the trail for which CloudTrail
    # will stop logging AWS API calls. The format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopLoggingResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
class Tag(ShapeBase):
    """
    A custom key-value pair associated with a resource such as a CloudTrail trail.
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

    # The key in a key-value pair. The key must be must be no longer than 128
    # Unicode characters. The key must be unique for the resource to which it
    # applies.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value in a key-value pair of a tag. The value must be no longer than
    # 256 Unicode characters.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagsLimitExceededException(ShapeBase):
    """
    The number of tags per trail has exceeded the permitted amount. Currently, the
    limit is 50.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Trail(ShapeBase):
    """
    The settings for a trail.
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
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "sns_topic_name",
                "SnsTopicName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicARN",
                TypeInfo(str),
            ),
            (
                "include_global_service_events",
                "IncludeGlobalServiceEvents",
                TypeInfo(bool),
            ),
            (
                "is_multi_region_trail",
                "IsMultiRegionTrail",
                TypeInfo(bool),
            ),
            (
                "home_region",
                "HomeRegion",
                TypeInfo(str),
            ),
            (
                "trail_arn",
                "TrailARN",
                TypeInfo(str),
            ),
            (
                "log_file_validation_enabled",
                "LogFileValidationEnabled",
                TypeInfo(bool),
            ),
            (
                "cloud_watch_logs_log_group_arn",
                "CloudWatchLogsLogGroupArn",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "has_custom_event_selectors",
                "HasCustomEventSelectors",
                TypeInfo(bool),
            ),
        ]

    # Name of the trail set by calling CreateTrail. The maximum length is 128
    # characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the Amazon S3 bucket into which CloudTrail delivers your trail
    # files. See [Amazon S3 Bucket Naming
    # Requirements](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html).
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Amazon S3 key prefix that comes after the name of the bucket
    # you have designated for log file delivery. For more information, see
    # [Finding Your CloudTrail Log
    # Files](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
    # find-log-files.html).The maximum length is 200 characters.
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is deprecated. Use SnsTopicARN.
    sns_topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send
    # notifications when log files are delivered. The format of a topic ARN is:

    # `arn:aws:sns:us-east-1:123456789012:MyTopic`
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to **True** to include AWS API calls from AWS global services such as
    # IAM. Otherwise, **False**.
    include_global_service_events: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the trail belongs only to one region or exists in all
    # regions.
    is_multi_region_trail: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region in which the trail was created.
    home_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ARN of the trail. The format of a trail ARN is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    trail_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether log file validation is enabled.
    log_file_validation_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies an Amazon Resource Name (ARN), a unique identifier that
    # represents the log group to which CloudTrail logs will be delivered.
    cloud_watch_logs_log_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the role for the CloudWatch Logs endpoint to assume to write to a
    # user's log group.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the KMS key ID that encrypts the logs delivered by CloudTrail.
    # The value is a fully specified ARN to a KMS key in the format:

    # `arn:aws:kms:us-
    # east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies if the trail has custom event selectors.
    has_custom_event_selectors: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrailAlreadyExistsException(ShapeBase):
    """
    This exception is thrown when the specified trail already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TrailNotFoundException(ShapeBase):
    """
    This exception is thrown when the trail with the given name is not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TrailNotProvidedException(ShapeBase):
    """
    This exception is deprecated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedOperationException(ShapeBase):
    """
    This exception is thrown when the requested operation is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateTrailRequest(ShapeBase):
    """
    Specifies settings to update for the trail.
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
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "sns_topic_name",
                "SnsTopicName",
                TypeInfo(str),
            ),
            (
                "include_global_service_events",
                "IncludeGlobalServiceEvents",
                TypeInfo(bool),
            ),
            (
                "is_multi_region_trail",
                "IsMultiRegionTrail",
                TypeInfo(bool),
            ),
            (
                "enable_log_file_validation",
                "EnableLogFileValidation",
                TypeInfo(bool),
            ),
            (
                "cloud_watch_logs_log_group_arn",
                "CloudWatchLogsLogGroupArn",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # Specifies the name of the trail or trail ARN. If `Name` is a trail name,
    # the string must meet the following requirements:

    #   * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)

    #   * Start with a letter or number, and end with a letter or number

    #   * Be between 3 and 128 characters

    #   * Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are invalid.

    #   * Not be in IP address format (for example, 192.168.5.4)

    # If `Name` is a trail ARN, it must be in the format:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Amazon S3 bucket designated for publishing log
    # files. See [Amazon S3 Bucket Naming
    # Requirements](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html).
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Amazon S3 key prefix that comes after the name of the bucket
    # you have designated for log file delivery. For more information, see
    # [Finding Your CloudTrail Log
    # Files](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
    # find-log-files.html). The maximum length is 200 characters.
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Amazon SNS topic defined for notification of log
    # file delivery. The maximum length is 256 characters.
    sns_topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the trail is publishing events from global services such
    # as IAM to the log files.
    include_global_service_events: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the trail applies only to the current region or to all
    # regions. The default is false. If the trail exists only in the current
    # region and this value is set to true, shadow trails (replications of the
    # trail) will be created in the other regions. If the trail exists in all
    # regions and this value is set to false, the trail will remain in the region
    # where it was created, and its shadow trails in other regions will be
    # deleted.
    is_multi_region_trail: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether log file validation is enabled. The default is false.

    # When you disable log file integrity validation, the chain of digest files
    # is broken after one hour. CloudTrail will not create digest files for log
    # files that were delivered during a period in which log file integrity
    # validation was disabled. For example, if you enable log file integrity
    # validation at noon on January 1, disable it at noon on January 2, and re-
    # enable it at noon on January 10, digest files will not be created for the
    # log files delivered from noon on January 2 to noon on January 10. The same
    # applies whenever you stop CloudTrail logging or delete a trail.
    enable_log_file_validation: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a log group name using an Amazon Resource Name (ARN), a unique
    # identifier that represents the log group to which CloudTrail logs will be
    # delivered. Not required unless you specify CloudWatchLogsRoleArn.
    cloud_watch_logs_log_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the role for the CloudWatch Logs endpoint to assume to write to a
    # user's log group.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the KMS key ID to use to encrypt the logs delivered by
    # CloudTrail. The value can be an alias name prefixed by "alias/", a fully
    # specified ARN to an alias, a fully specified ARN to a key, or a globally
    # unique identifier.

    # Examples:

    #   * alias/MyAliasName

    #   * arn:aws:kms:us-east-1:123456789012:alias/MyAliasName

    #   * arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012

    #   * 12345678-1234-1234-1234-123456789012
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTrailResponse(OutputShapeBase):
    """
    Returns the objects or data listed below if successful. Otherwise, returns an
    error.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "sns_topic_name",
                "SnsTopicName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicARN",
                TypeInfo(str),
            ),
            (
                "include_global_service_events",
                "IncludeGlobalServiceEvents",
                TypeInfo(bool),
            ),
            (
                "is_multi_region_trail",
                "IsMultiRegionTrail",
                TypeInfo(bool),
            ),
            (
                "trail_arn",
                "TrailARN",
                TypeInfo(str),
            ),
            (
                "log_file_validation_enabled",
                "LogFileValidationEnabled",
                TypeInfo(bool),
            ),
            (
                "cloud_watch_logs_log_group_arn",
                "CloudWatchLogsLogGroupArn",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logs_role_arn",
                "CloudWatchLogsRoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the trail.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Amazon S3 bucket designated for publishing log
    # files.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Amazon S3 key prefix that comes after the name of the bucket
    # you have designated for log file delivery. For more information, see
    # [Finding Your CloudTrail Log
    # Files](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
    # find-log-files.html).
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is deprecated. Use SnsTopicARN.
    sns_topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send
    # notifications when log files are delivered. The format of a topic ARN is:

    # `arn:aws:sns:us-east-1:123456789012:MyTopic`
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the trail is publishing events from global services such
    # as IAM to the log files.
    include_global_service_events: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the trail exists in one region or in all regions.
    is_multi_region_trail: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ARN of the trail that was updated. The format of a trail ARN
    # is:

    # `arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail`
    trail_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether log file integrity validation is enabled.
    log_file_validation_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Amazon Resource Name (ARN) of the log group to which
    # CloudTrail logs will be delivered.
    cloud_watch_logs_log_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the role for the CloudWatch Logs endpoint to assume to write to a
    # user's log group.
    cloud_watch_logs_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the KMS key ID that encrypts the logs delivered by CloudTrail.
    # The value is a fully specified ARN to a KMS key in the format:

    # `arn:aws:kms:us-
    # east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
