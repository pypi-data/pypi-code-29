import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
from enum import Enum
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddAttributesActivity(ShapeBase):
    """
    An activity that adds other attributes based on existing attributes in the
    message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'addAttributes' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of 1-50 "AttributeNameMapping" objects that map an existing
    # attribute to a new attribute.

    # The existing attributes remain in the message, so if you want to remove the
    # originals, use "RemoveAttributeActivity".
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["AddAttributesActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class BatchPutMessageErrorEntry(ShapeBase):
    """
    Contains informations about errors.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_id",
                "messageId",
                TypeInfo(str),
            ),
            (
                "error_code",
                "errorCode",
                TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                TypeInfo(str),
            ),
        ]

    # The ID of the message that caused the error. (See the value corresponding
    # to the "messageId" key in the message object.)
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code associated with the error.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message associated with the error.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["BatchPutMessageErrorEntry", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class BatchPutMessageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "messages",
                "messages",
                TypeInfo(typing.List[Message]),
            ),
        ]

    # The name of the channel where the messages are sent.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of messages to be sent. Each message has format: '{ "messageId":
    # "string", "payload": "string"}'.
    messages: typing.List["Message"] = dataclasses.field(default_factory=list, )

    def paginate(self,
                ) -> typing.Generator["BatchPutMessageRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class BatchPutMessageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "batch_put_message_error_entries",
                "batchPutMessageErrorEntries",
                TypeInfo(typing.List[BatchPutMessageErrorEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of any errors encountered when sending the messages to the channel.
    batch_put_message_error_entries: typing.List["BatchPutMessageErrorEntry"
                                                ] = dataclasses.field(
                                                    default_factory=list,
                                                )

    def paginate(self,
                ) -> typing.Generator["BatchPutMessageResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CancelPipelineReprocessingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
            (
                "reprocessing_id",
                "reprocessingId",
                TypeInfo(str),
            ),
        ]

    # The name of pipeline for which data reprocessing is canceled.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the reprocessing task (returned by "StartPipelineReprocessing").
    reprocessing_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["CancelPipelineReprocessingRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CancelPipelineReprocessingResponse(OutputShapeBase):
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

    def paginate(
        self,
    ) -> typing.Generator["CancelPipelineReprocessingResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Channel(ShapeBase):
    """
    A collection of data from an MQTT topic. Channels archive the raw, unprocessed
    messages before publishing the data to a pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(ChannelStatus),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the channel.
    status: "ChannelStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # When the channel was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the channel was last updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["Channel", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ChannelActivity(ShapeBase):
    """
    The activity that determines the source of the messages to be processed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'channel' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the channel from which the messages are processed.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ChannelActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ChannelStatistics(ShapeBase):
    """
    Statistics information about the channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "size",
                TypeInfo(EstimatedResourceSize),
            ),
        ]

    # The estimated size of the channel.
    size: "EstimatedResourceSize" = dataclasses.field(default_factory=dict, )

    def paginate(self, ) -> typing.Generator["ChannelStatistics", None, None]:
        yield from super().paginate()


class ChannelStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class ChannelSummary(ShapeBase):
    """
    A summary of information about a channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(ChannelStatus),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the channel.
    status: "ChannelStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the channel was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the channel was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ChannelSummary", None, None]:
        yield from super().paginate()


class ComputeType(Enum):
    ACU_1 = "ACU_1"
    ACU_2 = "ACU_2"


@dataclasses.dataclass
class ContainerDatasetAction(ShapeBase):
    """
    Information needed to run the "containerAction" to produce data set contents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "image",
                TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "executionRoleArn",
                TypeInfo(str),
            ),
            (
                "resource_configuration",
                "resourceConfiguration",
                TypeInfo(ResourceConfiguration),
            ),
            (
                "variables",
                "variables",
                TypeInfo(typing.List[Variable]),
            ),
        ]

    # The ARN of the Docker container stored in your account. The Docker
    # container contains an application and needed support libraries and is used
    # to generate data set contents.
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role which gives permission to the system to access needed
    # resources in order to run the "containerAction". This includes, at minimum,
    # permission to retrieve the data set contents which are the input to the
    # containerized application.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configuration of the resource which executes the "containerAction".
    resource_configuration: "ResourceConfiguration" = dataclasses.field(
        default_factory=dict,
    )

    # The values of variables used within the context of the execution of the
    # containerized application (basically, parameters passed to the
    # application). Each variable must have a name and a value given by one of
    # "stringValue", "datasetContentVersionValue", or "outputFileUriValue".
    variables: typing.List["Variable"] = dataclasses.field(
        default_factory=list,
    )

    def paginate(self,
                ) -> typing.Generator["ContainerDatasetAction", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata which can be used to manage the channel.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    def paginate(self,
                ) -> typing.Generator["CreateChannelRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "channel_arn",
                "channelArn",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the channel.
    channel_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["CreateChannelResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateDatasetContentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["CreateDatasetContentRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateDatasetContentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version_id",
                "versionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version ID of the data set contents which are being created.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["CreateDatasetContentResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateDatasetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                TypeInfo(typing.List[DatasetAction]),
            ),
            (
                "triggers",
                "triggers",
                TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of actions that create the data set contents.
    actions: typing.List["DatasetAction"] = dataclasses.field(
        default_factory=list,
    )

    # A list of triggers. A trigger causes data set contents to be populated at a
    # specified time interval or when another data set's contents are created.
    # The list of triggers can be empty or contain up to five **DataSetTrigger**
    # objects.
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # [Optional] How long, in days, message data is kept for the data set. If not
    # given or set to null, the latest version of the dataset content plus the
    # latest succeeded version (if they are different) are retained for at most
    # 90 days.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata which can be used to manage the data set.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    def paginate(self,
                ) -> typing.Generator["CreateDatasetRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateDatasetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "dataset_arn",
                "datasetArn",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the data set.
    dataset_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the data set.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["CreateDatasetResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateDatastoreRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the data store.
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # Metadata which can be used to manage the data store.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    def paginate(self,
                ) -> typing.Generator["CreateDatastoreRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreateDatastoreResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
            (
                "datastore_arn",
                "datastoreArn",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the data store.
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the data store.
    datastore_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["CreateDatastoreResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreatePipelineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
            (
                "pipeline_activities",
                "pipelineActivities",
                TypeInfo(typing.List[PipelineActivity]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the pipeline.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of pipeline activities.

    # The list can be 1-25 **PipelineActivity** objects. Activities perform
    # transformations on your messages, such as removing, renaming, or adding
    # message attributes; filtering messages based on attribute values; invoking
    # your Lambda functions on messages for advanced processing; or performing
    # mathematical transformations to normalize device data.
    pipeline_activities: typing.List["PipelineActivity"] = dataclasses.field(
        default_factory=list,
    )

    # Metadata which can be used to manage the pipeline.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    def paginate(self,
                ) -> typing.Generator["CreatePipelineRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class CreatePipelineResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
            (
                "pipeline_arn",
                "pipelineArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the pipeline.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the pipeline.
    pipeline_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["CreatePipelineResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Dataset(ShapeBase):
    """
    Information about a data set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                TypeInfo(typing.List[DatasetAction]),
            ),
            (
                "triggers",
                "triggers",
                TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "status",
                "status",
                TypeInfo(DatasetStatus),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data set.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the data set.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The "DatasetAction" objects that automatically create the data set
    # contents.
    actions: typing.List["DatasetAction"] = dataclasses.field(
        default_factory=list,
    )

    # The "DatasetTrigger" objects that specify when the data set is
    # automatically updated.
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # The status of the data set.
    status: "DatasetStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the data set was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the data set was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # [Optional] How long, in days, message data is kept for the data set.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self, ) -> typing.Generator["Dataset", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatasetAction(ShapeBase):
    """
    A "DatasetAction" object specifying the query that creates the data set content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "actionName",
                TypeInfo(str),
            ),
            (
                "query_action",
                "queryAction",
                TypeInfo(SqlQueryDatasetAction),
            ),
            (
                "container_action",
                "containerAction",
                TypeInfo(ContainerDatasetAction),
            ),
        ]

    # The name of the data set action by which data set contents are
    # automatically created.
    action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An "SqlQueryDatasetAction" object that contains the SQL query to modify the
    # message.
    query_action: "SqlQueryDatasetAction" = dataclasses.field(
        default_factory=dict,
    )

    # Information which allows the system to run a containerized application in
    # order to create the data set contents. The application must be in a Docker
    # container along with any needed support libraries.
    container_action: "ContainerDatasetAction" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self, ) -> typing.Generator["DatasetAction", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatasetActionSummary(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "actionName",
                TypeInfo(str),
            ),
            (
                "action_type",
                "actionType",
                TypeInfo(DatasetActionType),
            ),
        ]

    # The name of the action which automatically creates the data set's contents.
    action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of action by which the data set's contents are automatically
    # created.
    action_type: "DatasetActionType" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DatasetActionSummary", None, None]:
        yield from super().paginate()


class DatasetActionType(Enum):
    QUERY = "QUERY"
    CONTAINER = "CONTAINER"


class DatasetContentState(Enum):
    CREATING = "CREATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class DatasetContentStatus(ShapeBase):
    """
    The state of the data set contents and the reason they are in this state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "state",
                TypeInfo(DatasetContentState),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
        ]

    # The state of the data set contents. Can be one of "READY", "CREATING",
    # "SUCCEEDED" or "FAILED".
    state: "DatasetContentState" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason the data set contents are in this state.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DatasetContentStatus", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatasetContentSummary(ShapeBase):
    """
    Summary information about data set contents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(DatasetContentStatus),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "schedule_time",
                "scheduleTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The version of the data set contents.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the data set contents.
    status: "DatasetContentStatus" = dataclasses.field(default_factory=dict, )

    # The actual time the creation of the data set contents was started.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the creation of the data set contents was scheduled to start.
    schedule_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DatasetContentSummary", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatasetContentVersionValue(ShapeBase):
    """
    The data set whose latest contents will be used as input to the notebook or
    application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
        ]

    # The name of the data set whose latest contents will be used as input to the
    # notebook or application.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DatasetContentVersionValue", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatasetEntry(ShapeBase):
    """
    The reference to a data set entry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entry_name",
                "entryName",
                TypeInfo(str),
            ),
            (
                "data_uri",
                "dataURI",
                TypeInfo(str),
            ),
        ]

    # The name of the data set item.
    entry_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pre-signed URI of the data set item.
    data_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["DatasetEntry", None, None]:
        yield from super().paginate()


class DatasetStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class DatasetSummary(ShapeBase):
    """
    A summary of information about a data set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(DatasetStatus),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "triggers",
                "triggers",
                TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "actions",
                "actions",
                TypeInfo(typing.List[DatasetActionSummary]),
            ),
        ]

    # The name of the data set.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the data set.
    status: "DatasetStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the data set was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the data set was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of triggers. A trigger causes data set content to be populated at a
    # specified time interval or when another data set is populated. The list of
    # triggers can be empty or contain up to five DataSetTrigger objects
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # A list of "DataActionSummary" objects.
    actions: typing.List["DatasetActionSummary"] = dataclasses.field(
        default_factory=list,
    )

    def paginate(self, ) -> typing.Generator["DatasetSummary", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatasetTrigger(ShapeBase):
    """
    The "DatasetTrigger" that specifies when the data set is automatically updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule",
                "schedule",
                TypeInfo(Schedule),
            ),
            (
                "dataset",
                "dataset",
                TypeInfo(TriggeringDataset),
            ),
        ]

    # The "Schedule" when the trigger is initiated.
    schedule: "Schedule" = dataclasses.field(default_factory=dict, )

    # The data set whose content creation will trigger the creation of this data
    # set's contents.
    dataset: "TriggeringDataset" = dataclasses.field(default_factory=dict, )

    def paginate(self, ) -> typing.Generator["DatasetTrigger", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Datastore(ShapeBase):
    """
    Information about a data store.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(DatastoreStatus),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the data store.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the data store.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a data store:

    # CREATING

    # The data store is being created.

    # ACTIVE

    # The data store has been created and can be used.

    # DELETING

    # The data store is being deleted.
    status: "DatastoreStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    # When the data store was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the data store was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["Datastore", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatastoreActivity(ShapeBase):
    """
    The 'datastore' activity that specifies where to store the processed data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
        ]

    # The name of the 'datastore' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the data store where processed messages are stored.
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["DatastoreActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DatastoreStatistics(ShapeBase):
    """
    Statistical information about the data store.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "size",
                TypeInfo(EstimatedResourceSize),
            ),
        ]

    # The estimated size of the data store.
    size: "EstimatedResourceSize" = dataclasses.field(default_factory=dict, )

    def paginate(self, ) -> typing.Generator["DatastoreStatistics", None, None]:
        yield from super().paginate()


class DatastoreStatus(Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclasses.dataclass
class DatastoreSummary(ShapeBase):
    """
    A summary of information about a data store.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(DatastoreStatus),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the data store.
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the data store.
    status: "DatastoreStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the data store was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the data store was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["DatastoreSummary", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeleteChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
        ]

    # The name of the channel to delete.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DeleteChannelRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeleteDatasetContentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "version_id",
                "versionId",
                TypeInfo(str),
            ),
        ]

    # The name of the data set whose content is deleted.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the data set whose content is deleted. You can also use the
    # strings "$LATEST" or "$LATEST_SUCCEEDED" to delete the latest or latest
    # successfully completed data set. If not specified, "$LATEST_SUCCEEDED" is
    # the default.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DeleteDatasetContentRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeleteDatasetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
        ]

    # The name of the data set to delete.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DeleteDatasetRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeleteDatastoreRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
        ]

    # The name of the data store to delete.
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DeleteDatastoreRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeletePipelineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
        ]

    # The name of the pipeline to delete.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DeletePipelineRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeltaTime(ShapeBase):
    """
    When you create data set contents using message data from a specified time
    frame, some message data may still be "in flight" when processing begins, and so
    will not arrive in time to be processed. Use this field to make allowances for
    the "in flight" time of your message data, so that data not processed from the
    previous time frame will be included with the next time frame. Without this,
    missed message data would be excluded from processing during the next time frame
    as well, because its timestamp places it within the previous time frame.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offset_seconds",
                "offsetSeconds",
                TypeInfo(int),
            ),
            (
                "time_expression",
                "timeExpression",
                TypeInfo(str),
            ),
        ]

    # The number of seconds of estimated "in flight" lag time of message data.
    offset_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An expression by which the time of the message data may be determined. This
    # may be the name of a timestamp field, or a SQL expression which is used to
    # derive the time the message data was generated.
    time_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["DeltaTime", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "include_statistics",
                "includeStatistics",
                TypeInfo(bool),
            ),
        ]

    # The name of the channel whose information is retrieved.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, additional statistical information about the channel is included
    # in the response.
    include_statistics: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeChannelRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channel",
                "channel",
                TypeInfo(Channel),
            ),
            (
                "statistics",
                "statistics",
                TypeInfo(ChannelStatistics),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains information about the channel.
    channel: "Channel" = dataclasses.field(default_factory=dict, )

    # Statistics about the channel. Included if the 'includeStatistics' parameter
    # is set to true in the request.
    statistics: "ChannelStatistics" = dataclasses.field(default_factory=dict, )

    def paginate(self,
                ) -> typing.Generator["DescribeChannelResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeDatasetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
        ]

    # The name of the data set whose information is retrieved.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeDatasetRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeDatasetResponse(OutputShapeBase):
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
                "dataset",
                TypeInfo(Dataset),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains information about the data set.
    dataset: "Dataset" = dataclasses.field(default_factory=dict, )

    def paginate(self,
                ) -> typing.Generator["DescribeDatasetResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeDatastoreRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
            (
                "include_statistics",
                "includeStatistics",
                TypeInfo(bool),
            ),
        ]

    # The name of the data store
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, additional statistical information about the datastore is included
    # in the response.
    include_statistics: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeDatastoreRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeDatastoreResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "datastore",
                "datastore",
                TypeInfo(Datastore),
            ),
            (
                "statistics",
                "statistics",
                TypeInfo(DatastoreStatistics),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the data store.
    datastore: "Datastore" = dataclasses.field(default_factory=dict, )

    # Additional statistical information about the data store. Included if the
    # 'includeStatistics' parameter is set to true in the request.
    statistics: "DatastoreStatistics" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["DescribeDatastoreResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeLoggingOptionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []

    def paginate(
        self,
    ) -> typing.Generator["DescribeLoggingOptionsRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribeLoggingOptionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "logging_options",
                "loggingOptions",
                TypeInfo(LoggingOptions),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current settings of the AWS IoT Analytics logging options.
    logging_options: "LoggingOptions" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeLoggingOptionsResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribePipelineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
        ]

    # The name of the pipeline whose information is retrieved.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribePipelineRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DescribePipelineResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline",
                "pipeline",
                TypeInfo(Pipeline),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A "Pipeline" object that contains information about the pipeline.
    pipeline: "Pipeline" = dataclasses.field(default_factory=dict, )

    def paginate(self,
                ) -> typing.Generator["DescribePipelineResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeviceRegistryEnrichActivity(ShapeBase):
    """
    An activity that adds data from the AWS IoT device registry to your message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "attribute",
                "attribute",
                TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'deviceRegistryEnrich' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute that is added to the message.
    attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the IoT device whose registry information is added to the
    # message.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role that allows access to the device's registry
    # information.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DeviceRegistryEnrichActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class DeviceShadowEnrichActivity(ShapeBase):
    """
    An activity that adds information from the AWS IoT Device Shadows service to a
    message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "attribute",
                "attribute",
                TypeInfo(str),
            ),
            (
                "thing_name",
                "thingName",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'deviceShadowEnrich' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute that is added to the message.
    attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the IoT device whose shadow information is added to the
    # message.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role that allows access to the device's shadow.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DeviceShadowEnrichActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class EstimatedResourceSize(ShapeBase):
    """
    The estimated size of the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "estimated_size_in_bytes",
                "estimatedSizeInBytes",
                TypeInfo(float),
            ),
            (
                "estimated_on",
                "estimatedOn",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The estimated size of the resource in bytes.
    estimated_size_in_bytes: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the estimate of the size of the resource was made.
    estimated_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["EstimatedResourceSize", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class FilterActivity(ShapeBase):
    """
    An activity that filters a message based on its attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "filter",
                "filter",
                TypeInfo(str),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'filter' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An expression that looks like a SQL WHERE clause that must return a Boolean
    # value.
    filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["FilterActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class GetDatasetContentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "version_id",
                "versionId",
                TypeInfo(str),
            ),
        ]

    # The name of the data set whose contents are retrieved.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the data set whose contents are retrieved. You can also use
    # the strings "$LATEST" or "$LATEST_SUCCEEDED" to retrieve the contents of
    # the latest or latest successfully completed data set. If not specified,
    # "$LATEST_SUCCEEDED" is the default.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetDatasetContentRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class GetDatasetContentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entries",
                "entries",
                TypeInfo(typing.List[DatasetEntry]),
            ),
            (
                "timestamp",
                "timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(DatasetContentStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of "DatasetEntry" objects.
    entries: typing.List["DatasetEntry"] = dataclasses.field(
        default_factory=list,
    )

    # The time when the request was made.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the data set content.
    status: "DatasetContentStatus" = dataclasses.field(default_factory=dict, )

    def paginate(self,
                ) -> typing.Generator["GetDatasetContentResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    There was an internal failure.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["InternalFailureException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    The request was not valid.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["InvalidRequestException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class LambdaActivity(ShapeBase):
    """
    An activity that runs a Lambda function to modify the message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "lambda_name",
                "lambdaName",
                TypeInfo(str),
            ),
            (
                "batch_size",
                "batchSize",
                TypeInfo(int),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'lambda' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Lambda function that is run on the message.
    lambda_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of messages passed to the Lambda function for processing.

    # The AWS Lambda function must be able to process all of these messages
    # within five minutes, which is the maximum timeout duration for Lambda
    # functions.
    batch_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["LambdaActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The command caused an internal limit to be exceeded.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["LimitExceededException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListChannelsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListChannelsRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListChannelsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channel_summaries",
                "channelSummaries",
                TypeInfo(typing.List[ChannelSummary]),
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

    # A list of "ChannelSummary" objects.
    channel_summaries: typing.List["ChannelSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListChannelsResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListDatasetContentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The name of the data set whose contents information you want to list.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in this request.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDatasetContentsRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListDatasetContentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dataset_content_summaries",
                "datasetContentSummaries",
                TypeInfo(typing.List[DatasetContentSummary]),
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

    # Summary information about data set contents that have been created.
    dataset_content_summaries: typing.List["DatasetContentSummary"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListDatasetContentsResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListDatasetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListDatasetsRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListDatasetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dataset_summaries",
                "datasetSummaries",
                TypeInfo(typing.List[DatasetSummary]),
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

    # A list of "DatasetSummary" objects.
    dataset_summaries: typing.List["DatasetSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDatasetsResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListDatastoresRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDatastoresRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListDatastoresResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "datastore_summaries",
                "datastoreSummaries",
                TypeInfo(typing.List[DatastoreSummary]),
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

    # A list of "DatastoreSummary" objects.
    datastore_summaries: typing.List["DatastoreSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDatastoresResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListPipelinesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return in this request.

    # The default value is 100.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPipelinesRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListPipelinesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_summaries",
                "pipelineSummaries",
                TypeInfo(typing.List[PipelineSummary]),
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

    # A list of "PipelineSummary" objects.
    pipeline_summaries: typing.List["PipelineSummary"] = dataclasses.field(
        default_factory=list,
    )

    # The token to retrieve the next set of results, or `null` if there are no
    # more results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListPipelinesResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the resource whose tags you want to list.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListTagsForResourceRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ListTagsForResourceResponse(OutputShapeBase):
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
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags (metadata) which you have assigned to the resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    def paginate(
        self,
    ) -> typing.Generator["ListTagsForResourceResponse", None, None]:
        yield from super().paginate()


class LoggingLevel(Enum):
    ERROR = "ERROR"


@dataclasses.dataclass
class LoggingOptions(ShapeBase):
    """
    Information about logging options.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "level",
                "level",
                TypeInfo(LoggingLevel),
            ),
            (
                "enabled",
                "enabled",
                TypeInfo(bool),
            ),
        ]

    # The ARN of the role that grants permission to AWS IoT Analytics to perform
    # logging.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The logging level. Currently, only "ERROR" is supported.
    level: "LoggingLevel" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, logging is enabled for AWS IoT Analytics.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["LoggingOptions", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class MathActivity(ShapeBase):
    """
    An activity that computes an arithmetic expression using the message's
    attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "attribute",
                "attribute",
                TypeInfo(str),
            ),
            (
                "math",
                "math",
                TypeInfo(str),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'math' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute that will contain the result of the math
    # operation.
    attribute: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An expression that uses one or more existing attributes and must return an
    # integer value.
    math: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["MathActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Message(ShapeBase):
    """
    Information about a message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_id",
                "messageId",
                TypeInfo(str),
            ),
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
        ]

    # The ID you wish to assign to the message. Each "messageId" must be unique
    # within each batch sent.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The payload of the message. This may be a JSON string or a Base64-encoded
    # string representing binary data (in which case you must decode it by means
    # of a pipeline activity).
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["Message", None, None]:
        yield from super().paginate()


class MessagePayload(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class OutputFileUriValue(ShapeBase):
    """
    The URI of the location where data set contents are stored, usually the URI of a
    file in an S3 bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_name",
                "fileName",
                TypeInfo(str),
            ),
        ]

    # The URI of the location where data set contents are stored, usually the URI
    # of a file in an S3 bucket.
    file_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["OutputFileUriValue", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Pipeline(ShapeBase):
    """
    Contains information about a pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "activities",
                "activities",
                TypeInfo(typing.List[PipelineActivity]),
            ),
            (
                "reprocessing_summaries",
                "reprocessingSummaries",
                TypeInfo(typing.List[ReprocessingSummary]),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the pipeline.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The activities that perform transformations on the messages.
    activities: typing.List["PipelineActivity"] = dataclasses.field(
        default_factory=list,
    )

    # A summary of information about the pipeline reprocessing.
    reprocessing_summaries: typing.List["ReprocessingSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # When the pipeline was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the pipeline was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["Pipeline", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class PipelineActivity(ShapeBase):
    """
    An activity that performs a transformation on a message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "channel",
                TypeInfo(ChannelActivity),
            ),
            (
                "lambda_",
                "lambda",
                TypeInfo(LambdaActivity),
            ),
            (
                "datastore",
                "datastore",
                TypeInfo(DatastoreActivity),
            ),
            (
                "add_attributes",
                "addAttributes",
                TypeInfo(AddAttributesActivity),
            ),
            (
                "remove_attributes",
                "removeAttributes",
                TypeInfo(RemoveAttributesActivity),
            ),
            (
                "select_attributes",
                "selectAttributes",
                TypeInfo(SelectAttributesActivity),
            ),
            (
                "filter",
                "filter",
                TypeInfo(FilterActivity),
            ),
            (
                "math",
                "math",
                TypeInfo(MathActivity),
            ),
            (
                "device_registry_enrich",
                "deviceRegistryEnrich",
                TypeInfo(DeviceRegistryEnrichActivity),
            ),
            (
                "device_shadow_enrich",
                "deviceShadowEnrich",
                TypeInfo(DeviceShadowEnrichActivity),
            ),
        ]

    # Determines the source of the messages to be processed.
    channel: "ChannelActivity" = dataclasses.field(default_factory=dict, )

    # Runs a Lambda function to modify the message.
    lambda_: "LambdaActivity" = dataclasses.field(default_factory=dict, )

    # Specifies where to store the processed message data.
    datastore: "DatastoreActivity" = dataclasses.field(default_factory=dict, )

    # Adds other attributes based on existing attributes in the message.
    add_attributes: "AddAttributesActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Removes attributes from a message.
    remove_attributes: "RemoveAttributesActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Creates a new message using only the specified attributes from the original
    # message.
    select_attributes: "SelectAttributesActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Filters a message based on its attributes.
    filter: "FilterActivity" = dataclasses.field(default_factory=dict, )

    # Computes an arithmetic expression using the message's attributes and adds
    # it to the message.
    math: "MathActivity" = dataclasses.field(default_factory=dict, )

    # Adds data from the AWS IoT device registry to your message.
    device_registry_enrich: "DeviceRegistryEnrichActivity" = dataclasses.field(
        default_factory=dict,
    )

    # Adds information from the AWS IoT Device Shadows service to a message.
    device_shadow_enrich: "DeviceShadowEnrichActivity" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self, ) -> typing.Generator["PipelineActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class PipelineSummary(ShapeBase):
    """
    A summary of information about a pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
            (
                "reprocessing_summaries",
                "reprocessingSummaries",
                TypeInfo(typing.List[ReprocessingSummary]),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_time",
                "lastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of information about the pipeline reprocessing.
    reprocessing_summaries: typing.List["ReprocessingSummary"
                                       ] = dataclasses.field(
                                           default_factory=list,
                                       )

    # When the pipeline was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the pipeline was last updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["PipelineSummary", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class PutLoggingOptionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logging_options",
                "loggingOptions",
                TypeInfo(LoggingOptions),
            ),
        ]

    # The new values of the AWS IoT Analytics logging options.
    logging_options: "LoggingOptions" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["PutLoggingOptionsRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class QueryFilter(ShapeBase):
    """
    Information which is used to filter message data, to segregate it according to
    the time frame in which it arrives.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delta_time",
                "deltaTime",
                TypeInfo(DeltaTime),
            ),
        ]

    # Used to limit data to that which has arrived since the last execution of
    # the action. When you create data set contents using message data from a
    # specified time frame, some message data may still be "in flight" when
    # processing begins, and so will not arrive in time to be processed. Use this
    # field to make allowances for the "in flight" time of you message data, so
    # that data not processed from a previous time frame will be included with
    # the next time frame. Without this, missed message data would be excluded
    # from processing during the next time frame as well, because its timestamp
    # places it within the previous time frame.
    delta_time: "DeltaTime" = dataclasses.field(default_factory=dict, )

    def paginate(self, ) -> typing.Generator["QueryFilter", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class RemoveAttributesActivity(ShapeBase):
    """
    An activity that removes attributes from a message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[str]),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'removeAttributes' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of 1-50 attributes to remove from the message.
    attributes: typing.List[str] = dataclasses.field(default_factory=list, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["RemoveAttributesActivity", None, None]:
        yield from super().paginate()


class ReprocessingStatus(Enum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


@dataclasses.dataclass
class ReprocessingSummary(ShapeBase):
    """
    Information about pipeline reprocessing.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(ReprocessingStatus),
            ),
            (
                "creation_time",
                "creationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The 'reprocessingId' returned by "StartPipelineReprocessing".
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the pipeline reprocessing.
    status: "ReprocessingStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the pipeline reprocessing was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ReprocessingSummary", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    A resource with the same name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ResourceAlreadyExistsException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ResourceConfiguration(ShapeBase):
    """
    The configuration of the resource used to execute the "containerAction".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_type",
                "computeType",
                TypeInfo(ComputeType),
            ),
            (
                "volume_size_in_gb",
                "volumeSizeInGB",
                TypeInfo(int),
            ),
        ]

    # The type of the compute resource used to execute the "containerAction".
    # Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8,
    # memory=32GiB).
    compute_type: "ComputeType" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size (in GB) of the persistent storage available to the resource
    # instance used to execute the "containerAction" (min: 1, max: 50).
    volume_size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ResourceConfiguration", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    A resource with the specified name could not be found.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ResourceNotFoundException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class RetentionPeriod(ShapeBase):
    """
    How long, in days, message data is kept.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "unlimited",
                "unlimited",
                TypeInfo(bool),
            ),
            (
                "number_of_days",
                "numberOfDays",
                TypeInfo(int),
            ),
        ]

    # If true, message data is kept indefinitely.
    unlimited: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days that message data is kept. The "unlimited" parameter
    # must be false.
    number_of_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["RetentionPeriod", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class RunPipelineActivityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_activity",
                "pipelineActivity",
                TypeInfo(PipelineActivity),
            ),
            (
                "payloads",
                "payloads",
                TypeInfo(typing.List[typing.Any]),
            ),
        ]

    # The pipeline activity that is run. This must not be a 'channel' activity or
    # a 'datastore' activity because these activities are used in a pipeline only
    # to load the original message and to store the (possibly) transformed
    # message. If a 'lambda' activity is specified, only short-running Lambda
    # functions (those with a timeout of less than 30 seconds or less) can be
    # used.
    pipeline_activity: "PipelineActivity" = dataclasses.field(
        default_factory=dict,
    )

    # The sample message payloads on which the pipeline activity is run.
    payloads: typing.List[typing.Any] = dataclasses.field(
        default_factory=list,
    )

    def paginate(self,
                ) -> typing.Generator["RunPipelineActivityRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class RunPipelineActivityResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payloads",
                "payloads",
                TypeInfo(typing.List[typing.Any]),
            ),
            (
                "log_result",
                "logResult",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The enriched or transformed sample message payloads as base64-encoded
    # strings. (The results of running the pipeline activity on each input sample
    # message payload, encoded in base64.)
    payloads: typing.List[typing.Any] = dataclasses.field(
        default_factory=list,
    )

    # In case the pipeline activity fails, the log message that is generated.
    log_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["RunPipelineActivityResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class SampleChannelDataRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "max_messages",
                "maxMessages",
                TypeInfo(int),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the channel whose message samples are retrieved.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of sample messages to be retrieved. The limit is 10, the default
    # is also 10.
    max_messages: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start of the time window from which sample messages are retrieved.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time window from which sample messages are retrieved.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SampleChannelDataRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class SampleChannelDataResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payloads",
                "payloads",
                TypeInfo(typing.List[typing.Any]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of message samples. Each sample message is returned as a
    # base64-encoded string.
    payloads: typing.List[typing.Any] = dataclasses.field(
        default_factory=list,
    )

    def paginate(self,
                ) -> typing.Generator["SampleChannelDataResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Schedule(ShapeBase):
    """
    The schedule for when to trigger an update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression",
                "expression",
                TypeInfo(str),
            ),
        ]

    # The expression that defines when to trigger an update. For more
    # information, see [ Schedule Expressions for
    # Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)
    # in the Amazon CloudWatch documentation.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["Schedule", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class SelectAttributesActivity(ShapeBase):
    """
    Creates a new message using only the specified attributes from the original
    message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[str]),
            ),
            (
                "next",
                "next",
                TypeInfo(str),
            ),
        ]

    # The name of the 'selectAttributes' activity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the attributes to select from the message.
    attributes: typing.List[str] = dataclasses.field(default_factory=list, )

    # The next activity in the pipeline.
    next: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["SelectAttributesActivity", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The service is temporarily unavailable.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ServiceUnavailableException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class SqlQueryDatasetAction(ShapeBase):
    """
    The SQL query to modify the message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sql_query",
                "sqlQuery",
                TypeInfo(str),
            ),
            (
                "filters",
                "filters",
                TypeInfo(typing.List[QueryFilter]),
            ),
        ]

    # A SQL query string.
    sql_query: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pre-filters applied to message data.
    filters: typing.List["QueryFilter"] = dataclasses.field(
        default_factory=list,
    )

    def paginate(self,
                ) -> typing.Generator["SqlQueryDatasetAction", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class StartPipelineReprocessingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the pipeline on which to start reprocessing.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time (inclusive) of raw message data that is reprocessed.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time (exclusive) of raw message data that is reprocessed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["StartPipelineReprocessingRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class StartPipelineReprocessingResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "reprocessing_id",
                "reprocessingId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the pipeline reprocessing activity that was started.
    reprocessing_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["StartPipelineReprocessingResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A set of key/value pairs which are used to manage the resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The tag's key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag's value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["Tag", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ARN of the resource whose tags will be modified.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new or modified tags for the resource.
    tags: typing.List["Tag"] = dataclasses.field(default_factory=list, )

    def paginate(self, ) -> typing.Generator["TagResourceRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class TagResourceResponse(OutputShapeBase):
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

    def paginate(self, ) -> typing.Generator["TagResourceResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class ThrottlingException(ShapeBase):
    """
    The request was denied due to request throttling.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ThrottlingException", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class TriggeringDataset(ShapeBase):
    """
    Information about the data set whose content generation will trigger the new
    data set content generation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The name of the data set whose content generation will trigger the new data
    # set content generation.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["TriggeringDataset", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "tagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the resource whose tags will be removed.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The keys of those tags which will be removed.
    tag_keys: typing.List[str] = dataclasses.field(default_factory=list, )

    def paginate(self,
                ) -> typing.Generator["UntagResourceRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class UntagResourceResponse(OutputShapeBase):
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

    def paginate(self,
                ) -> typing.Generator["UntagResourceResponse", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class UpdateChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "channelName",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the channel to be updated.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the channel.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["UpdateChannelRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class UpdateDatasetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dataset_name",
                "datasetName",
                TypeInfo(str),
            ),
            (
                "actions",
                "actions",
                TypeInfo(typing.List[DatasetAction]),
            ),
            (
                "triggers",
                "triggers",
                TypeInfo(typing.List[DatasetTrigger]),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data set to update.
    dataset_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of "DatasetAction" objects.
    actions: typing.List["DatasetAction"] = dataclasses.field(
        default_factory=list,
    )

    # A list of "DatasetTrigger" objects. The list can be empty or can contain up
    # to five **DataSetTrigger** objects.
    triggers: typing.List["DatasetTrigger"] = dataclasses.field(
        default_factory=list,
    )

    # How long, in days, message data is kept for the data set.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["UpdateDatasetRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class UpdateDatastoreRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "datastore_name",
                "datastoreName",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "retentionPeriod",
                TypeInfo(RetentionPeriod),
            ),
        ]

    # The name of the data store to be updated.
    datastore_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long, in days, message data is kept for the data store.
    retention_period: "RetentionPeriod" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self,
                ) -> typing.Generator["UpdateDatastoreRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class UpdatePipelineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_name",
                "pipelineName",
                TypeInfo(str),
            ),
            (
                "pipeline_activities",
                "pipelineActivities",
                TypeInfo(typing.List[PipelineActivity]),
            ),
        ]

    # The name of the pipeline to update.
    pipeline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of "PipelineActivity" objects.

    # The list can be 1-25 **PipelineActivity** objects. Activities perform
    # transformations on your messages, such as removing, renaming or adding
    # message attributes; filtering messages based on attribute values; invoking
    # your Lambda functions on messages for advanced processing; or performing
    # mathematical transformations to normalize device data.
    pipeline_activities: typing.List["PipelineActivity"] = dataclasses.field(
        default_factory=list,
    )

    def paginate(self,
                ) -> typing.Generator["UpdatePipelineRequest", None, None]:
        yield from super().paginate()


@dataclasses.dataclass
class Variable(ShapeBase):
    """
    An instance of a variable to be passed to the "containerAction" execution. Each
    variable must have a name and a value given by one of "stringValue",
    "datasetContentVersionValue", or "outputFileUriValue".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "string_value",
                "stringValue",
                TypeInfo(str),
            ),
            (
                "double_value",
                "doubleValue",
                TypeInfo(float),
            ),
            (
                "dataset_content_version_value",
                "datasetContentVersionValue",
                TypeInfo(DatasetContentVersionValue),
            ),
            (
                "output_file_uri_value",
                "outputFileUriValue",
                TypeInfo(OutputFileUriValue),
            ),
        ]

    # The name of the variable.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the variable as a string.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the variable as a double (numeric).
    double_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the variable as a structure that specifies a data set content
    # version.
    dataset_content_version_value: "DatasetContentVersionValue" = dataclasses.field(
        default_factory=dict,
    )

    # The value of the variable as a structure that specifies an output file URI.
    output_file_uri_value: "OutputFileUriValue" = dataclasses.field(
        default_factory=dict,
    )

    def paginate(self, ) -> typing.Generator["Variable", None, None]:
        yield from super().paginate()
