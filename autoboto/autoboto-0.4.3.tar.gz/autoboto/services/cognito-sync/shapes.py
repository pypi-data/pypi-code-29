import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AlreadyStreamedException(ShapeBase):
    """
    An exception thrown when a bulk publish operation is requested less than 24
    hours after a previous bulk publish operation completed successfully.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The message associated with the AlreadyStreamedException exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BulkPublishRequest(ShapeBase):
    """
    The input for the BulkPublish operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BulkPublishResponse(OutputShapeBase):
    """
    The output for the BulkPublish operation.
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BulkPublishStatus(str):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


@dataclasses.dataclass
class CognitoStreams(ShapeBase):
    """
    Configuration options for configure Cognito streams.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "streaming_status",
                "StreamingStatus",
                TypeInfo(typing.Union[str, StreamingStatus]),
            ),
        ]

    # The name of the Cognito stream to receive updates. This stream must be in
    # the developers account and in the same region as the identity pool.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role Amazon Cognito can assume in order to publish to the
    # stream. This role must grant access to Amazon Cognito (cognito-sync) to
    # invoke PutRecord on your Cognito stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the Cognito streams. Valid values are:

    # ENABLED - Streaming of updates to identity pool is enabled.

    # DISABLED - Streaming of updates to identity pool is disabled. Bulk publish
    # will also fail if StreamingStatus is DISABLED.
    streaming_status: typing.Union[str, "StreamingStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Thrown if there are parallel requests to modify a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The message returned by a ConcurrentModicationException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Dataset(ShapeBase):
    """
    A collection of data for an identity pool. An identity pool can have multiple
    datasets. A dataset is per identity and can be general or associated with a
    particular entity in an application (like a saved game). Datasets are
    automatically created if they don't exist. Data is synced by dataset, and a
    dataset can hold up to 1MB of key-value pairs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "data_storage",
                "DataStorage",
                TypeInfo(int),
            ),
            (
                "num_records",
                "NumRecords",
                TypeInfo(int),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_'
    # (underscore), '-' (dash), and '.' (dot).
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date on which the dataset was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date when the dataset was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device that made the last change to this dataset.
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total size in bytes of the records in this dataset.
    data_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of records in this dataset.
    num_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDatasetRequest(ShapeBase):
    """
    A request to delete the specific dataset.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_'
    # (underscore), '-' (dash), and '.' (dot).
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDatasetResponse(OutputShapeBase):
    """
    Response to a successful DeleteDataset request.
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
                "dataset",
                "Dataset",
                TypeInfo(Dataset),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of data for an identity pool. An identity pool can have
    # multiple datasets. A dataset is per identity and can be general or
    # associated with a particular entity in an application (like a saved game).
    # Datasets are automatically created if they don't exist. Data is synced by
    # dataset, and a dataset can hold up to 1MB of key-value pairs.
    dataset: "Dataset" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDatasetRequest(ShapeBase):
    """
    A request for meta data about a dataset (creation date, number of records, size)
    by owner and dataset name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_'
    # (underscore), '-' (dash), and '.' (dot).
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDatasetResponse(OutputShapeBase):
    """
    Response to a successful DescribeDataset request.
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
                "dataset",
                "Dataset",
                TypeInfo(Dataset),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Meta data for a collection of data for an identity. An identity can have
    # multiple datasets. A dataset can be general or associated with a particular
    # entity in an application (like a saved game). Datasets are automatically
    # created if they don't exist. Data is synced by dataset, and a dataset can
    # hold up to 1MB of key-value pairs.
    dataset: "Dataset" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIdentityPoolUsageRequest(ShapeBase):
    """
    A request for usage information about the identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIdentityPoolUsageResponse(OutputShapeBase):
    """
    Response to a successful DescribeIdentityPoolUsage request.
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
                "identity_pool_usage",
                "IdentityPoolUsage",
                TypeInfo(IdentityPoolUsage),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the usage of the identity pool.
    identity_pool_usage: "IdentityPoolUsage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeIdentityUsageRequest(ShapeBase):
    """
    A request for information about the usage of an identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeIdentityUsageResponse(OutputShapeBase):
    """
    The response to a successful DescribeIdentityUsage request.
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
                "identity_usage",
                "IdentityUsage",
                TypeInfo(IdentityUsage),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Usage information for the identity.
    identity_usage: "IdentityUsage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DuplicateRequestException(ShapeBase):
    """
    An exception thrown when there is an IN_PROGRESS bulk publish operation for the
    given identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The message associated with the DuplicateRequestException exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBulkPublishDetailsRequest(ShapeBase):
    """
    The input for the GetBulkPublishDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBulkPublishDetailsResponse(OutputShapeBase):
    """
    The output for the GetBulkPublishDetails operation.
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "bulk_publish_start_time",
                "BulkPublishStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "bulk_publish_complete_time",
                "BulkPublishCompleteTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "bulk_publish_status",
                "BulkPublishStatus",
                TypeInfo(typing.Union[str, BulkPublishStatus]),
            ),
            (
                "failure_message",
                "FailureMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date/time at which the last bulk publish was initiated.
    bulk_publish_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If BulkPublishStatus is SUCCEEDED, the time the last bulk publish operation
    # completed.
    bulk_publish_complete_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Status of the last bulk publish operation, valid values are:

    # NOT_STARTED - No bulk publish has been requested for this identity pool

    # IN_PROGRESS - Data is being published to the configured stream

    # SUCCEEDED - All data for the identity pool has been published to the
    # configured stream

    # FAILED - Some portion of the data has failed to publish, check
    # FailureMessage for the cause.
    bulk_publish_status: typing.Union[str, "BulkPublishStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # If BulkPublishStatus is FAILED this field will contain the error message
    # that caused the bulk publish to fail.
    failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCognitoEventsRequest(ShapeBase):
    """
    A request for a list of the configured Cognito Events
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # The Cognito Identity Pool ID for the request
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCognitoEventsResponse(OutputShapeBase):
    """
    The response from the GetCognitoEvents request
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
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Cognito Events returned from the GetCognitoEvents request
    events: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityPoolConfigurationRequest(ShapeBase):
    """
    The input for the GetIdentityPoolConfiguration operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # This is the ID of the pool for which to return a configuration.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIdentityPoolConfigurationResponse(OutputShapeBase):
    """
    The output for the GetIdentityPoolConfiguration operation.
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "push_sync",
                "PushSync",
                TypeInfo(PushSync),
            ),
            (
                "cognito_streams",
                "CognitoStreams",
                TypeInfo(CognitoStreams),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to apply to this identity pool for push synchronization.
    push_sync: "PushSync" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to apply to this identity pool for Amazon Cognito streams.
    cognito_streams: "CognitoStreams" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdentityPoolUsage(ShapeBase):
    """
    Usage information for the identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "sync_sessions_count",
                "SyncSessionsCount",
                TypeInfo(int),
            ),
            (
                "data_storage",
                "DataStorage",
                TypeInfo(int),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of sync sessions for the identity pool.
    sync_sessions_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Data storage information for the identity pool.
    data_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date on which the identity pool was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdentityUsage(ShapeBase):
    """
    Usage information for the identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "dataset_count",
                "DatasetCount",
                TypeInfo(int),
            ),
            (
                "data_storage",
                "DataStorage",
                TypeInfo(int),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date on which the identity was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of datasets for the identity.
    dataset_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total data storage for this identity.
    data_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(ShapeBase):
    """
    Indicates an internal service error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Message returned by InternalErrorException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidConfigurationException(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Message returned by InvalidConfigurationException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLambdaFunctionOutputException(ShapeBase):
    """
    The AWS Lambda function returned invalid output or an exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # A message returned when an InvalidLambdaFunctionOutputException occurs
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    Thrown when a request parameter does not comply with the associated constraints.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Message returned by InvalidParameterException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaThrottledException(ShapeBase):
    """
    AWS Lambda throttled your account, please contact AWS Support
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # A message returned when an LambdaThrottledException is thrown
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    Thrown when the limit on the number of objects or operations has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Message returned by LimitExceededException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDatasetsRequest(ShapeBase):
    """
    Request for a list of datasets for an identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
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

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for obtaining the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDatasetsResponse(OutputShapeBase):
    """
    Returned for a successful ListDatasets request.
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
                "datasets",
                "Datasets",
                TypeInfo(typing.List[Dataset]),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
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

    # A set of datasets.
    datasets: typing.List["Dataset"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of datasets returned.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for obtaining the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoolUsageRequest(ShapeBase):
    """
    A request for usage information on an identity pool.
    """

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

    # A pagination token for obtaining the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoolUsageResponse(OutputShapeBase):
    """
    Returned for a successful ListIdentityPoolUsage request.
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
                "identity_pool_usages",
                "IdentityPoolUsages",
                TypeInfo(typing.List[IdentityPoolUsage]),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
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

    # Usage information for the identity pools.
    identity_pool_usages: typing.List["IdentityPoolUsage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of results to be returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total number of identities for the identity pool.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for obtaining the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRecordsRequest(ShapeBase):
    """
    A request for a list of records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
            (
                "last_sync_count",
                "LastSyncCount",
                TypeInfo(int),
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
            (
                "sync_session_token",
                "SyncSessionToken",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_'
    # (underscore), '-' (dash), and '.' (dot).
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last server sync count for this record.
    last_sync_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for obtaining the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token containing a session ID, identity ID, and expiration.
    sync_session_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRecordsResponse(OutputShapeBase):
    """
    Returned for a successful ListRecordsRequest.
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
                "records",
                "Records",
                TypeInfo(typing.List[Record]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "dataset_sync_count",
                "DatasetSyncCount",
                TypeInfo(int),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "merged_dataset_names",
                "MergedDatasetNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "dataset_exists",
                "DatasetExists",
                TypeInfo(bool),
            ),
            (
                "dataset_deleted_after_requested_sync_count",
                "DatasetDeletedAfterRequestedSyncCount",
                TypeInfo(bool),
            ),
            (
                "sync_session_token",
                "SyncSessionToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of all records.
    records: typing.List["Record"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token for obtaining the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total number of records.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Server sync count for this dataset.
    dataset_sync_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user/device that made the last change to this record.
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Names of merged datasets.
    merged_dataset_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the dataset exists.
    dataset_exists: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value specifying whether to delete the dataset locally.
    dataset_deleted_after_requested_sync_count: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token containing a session ID, identity ID, and expiration.
    sync_session_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotAuthorizedException(ShapeBase):
    """
    Thrown when a user is not authorized to access the requested resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The message returned by a NotAuthorizedException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Operation(str):
    replace = "replace"
    remove = "remove"


class Platform(str):
    APNS = "APNS"
    APNS_SANDBOX = "APNS_SANDBOX"
    GCM = "GCM"
    ADM = "ADM"


@dataclasses.dataclass
class PushSync(ShapeBase):
    """
    Configuration options to be applied to the identity pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_arns",
                "ApplicationArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # List of SNS platform application ARNs that could be used by clients.
    application_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A role configured to allow Cognito to call SNS on behalf of the developer.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Record(ShapeBase):
    """
    The basic data structure of a dataset.
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
            (
                "sync_count",
                "SyncCount",
                TypeInfo(int),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "device_last_modified_date",
                "DeviceLastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The key for the record.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the record.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The server sync count for this record.
    sync_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date on which the record was last modified.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user/device that made the last change to this record.
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last modified date of the client device.
    device_last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RecordPatch(ShapeBase):
    """
    An update operation for a record.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "op",
                "Op",
                TypeInfo(typing.Union[str, Operation]),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "sync_count",
                "SyncCount",
                TypeInfo(int),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "device_last_modified_date",
                "DeviceLastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # An operation, either replace or remove.
    op: typing.Union[str, "Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The key associated with the record patch.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last known server sync count for this record. Set to 0 if unknown.
    sync_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value associated with the record patch.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last modified date of the client device.
    device_last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterDeviceRequest(ShapeBase):
    """
    A request to RegisterDevice.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(typing.Union[str, Platform]),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # Here, the ID of the pool that the identity belongs to.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID for this identity.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).
    platform: typing.Union[str, "Platform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The push token.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterDeviceResponse(OutputShapeBase):
    """
    Response to a RegisterDevice request.
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
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID generated for this device by Cognito.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceConflictException(ShapeBase):
    """
    Thrown if an update can't be applied because the resource was changed by another
    call and this would result in a conflict.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The message returned by a ResourceConflictException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    Thrown if the resource doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Message returned by a ResourceNotFoundException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetCognitoEventsRequest(ShapeBase):
    """
    A request to configure Cognito Events"

    "
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Cognito Identity Pool to use when configuring Cognito Events
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The events to configure
    events: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetIdentityPoolConfigurationRequest(ShapeBase):
    """
    The input for the SetIdentityPoolConfiguration operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "push_sync",
                "PushSync",
                TypeInfo(PushSync),
            ),
            (
                "cognito_streams",
                "CognitoStreams",
                TypeInfo(CognitoStreams),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # This is the ID of the pool to modify.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to apply to this identity pool for push synchronization.
    push_sync: "PushSync" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to apply to this identity pool for Amazon Cognito streams.
    cognito_streams: "CognitoStreams" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetIdentityPoolConfigurationResponse(OutputShapeBase):
    """
    The output for the SetIdentityPoolConfiguration operation
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
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "push_sync",
                "PushSync",
                TypeInfo(PushSync),
            ),
            (
                "cognito_streams",
                "CognitoStreams",
                TypeInfo(CognitoStreams),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to apply to this identity pool for push synchronization.
    push_sync: "PushSync" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options to apply to this identity pool for Amazon Cognito streams.
    cognito_streams: "CognitoStreams" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StreamingStatus(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class SubscribeToDatasetRequest(ShapeBase):
    """
    A request to SubscribeToDatasetRequest.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The
    # ID of the pool to which the identity belongs.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique ID for this identity.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the dataset to subcribe to.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID generated for this device by Cognito.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubscribeToDatasetResponse(OutputShapeBase):
    """
    Response to a SubscribeToDataset request.
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
class TooManyRequestsException(ShapeBase):
    """
    Thrown if the request is throttled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Message returned by a TooManyRequestsException.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsubscribeFromDatasetRequest(ShapeBase):
    """
    A request to UnsubscribeFromDataset.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The
    # ID of the pool to which this identity belongs.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique ID for this identity.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the dataset from which to unsubcribe.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID generated for this device by Cognito.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsubscribeFromDatasetResponse(OutputShapeBase):
    """
    Response to an UnsubscribeFromDataset request.
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
class UpdateRecordsRequest(ShapeBase):
    """
    A request to post updates to records or add and delete records for a dataset and
    user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_pool_id",
                "IdentityPoolId",
                TypeInfo(str),
            ),
            (
                "identity_id",
                "IdentityId",
                TypeInfo(str),
            ),
            (
                "dataset_name",
                "DatasetName",
                TypeInfo(str),
            ),
            (
                "sync_session_token",
                "SyncSessionToken",
                TypeInfo(str),
            ),
            (
                "device_id",
                "DeviceId",
                TypeInfo(str),
            ),
            (
                "record_patches",
                "RecordPatches",
                TypeInfo(typing.List[RecordPatch]),
            ),
            (
                "client_context",
                "ClientContext",
                TypeInfo(str),
            ),
        ]

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_pool_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name-spaced GUID (for example, us-
    # east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
    # GUID generation is unique within a region.
    identity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_'
    # (underscore), '-' (dash), and '.' (dot).
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SyncSessionToken returned by a previous call to ListRecords for this
    # dataset and identity.
    sync_session_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID generated for this device by Cognito.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of patch operations.
    record_patches: typing.List["RecordPatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Intended to supply a device ID that will populate the lastModifiedBy field
    # referenced in other methods. The ClientContext field is not yet
    # implemented.
    client_context: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateRecordsResponse(OutputShapeBase):
    """
    Returned for a successful UpdateRecordsRequest.
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
                "records",
                "Records",
                TypeInfo(typing.List[Record]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of records that have been updated.
    records: typing.List["Record"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
