import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class Activation(ShapeBase):
    """
    An activation registers one or more on-premises servers or virtual machines
    (VMs) with AWS so that you can configure those servers or VMs using Run Command.
    A server or VM that has been registered with AWS is called a managed instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activation_id",
                "ActivationId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "default_instance_name",
                "DefaultInstanceName",
                TypeInfo(str),
            ),
            (
                "iam_role",
                "IamRole",
                TypeInfo(str),
            ),
            (
                "registration_limit",
                "RegistrationLimit",
                TypeInfo(int),
            ),
            (
                "registrations_count",
                "RegistrationsCount",
                TypeInfo(int),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "expired",
                "Expired",
                TypeInfo(bool),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The ID created by Systems Manager when you submitted the activation.
    activation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user defined description of the activation.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the managed instance when it is created.
    default_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Identity and Access Management (IAM) role to assign to the
    # managed instance.
    iam_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of managed instances that can be registered using this
    # activation.
    registration_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of managed instances already registered with this activation.
    registrations_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when this activation can no longer be used to register managed
    # instances.
    expiration_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether or not the activation is expired.
    expired: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the activation was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsToResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, ResourceTypeForTagging]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the type of resource you are tagging.

    # The ManagedInstance type for this API action is for on-premises managed
    # instances. You must specify the the name of the managed instance in the
    # following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_type: typing.Union[str, "ResourceTypeForTagging"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The resource ID you want to tag.

    # Use the ID of the resource. Here are some examples:

    # ManagedInstance: mi-012345abcde

    # MaintenanceWindow: mw-012345abcde

    # PatchBaseline: pb-012345abcde

    # For the Document and Parameter values, use the name of the resource.

    # The ManagedInstance type for this API action is only for on-premises
    # managed instances. You must specify the the name of the managed instance in
    # the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tags. The value parameter is required, but if you don't want
    # the tag to have a value, specify the parameter with no value, and we set
    # the value to an empty string.

    # Do not enter personally identifiable information in this field.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsToResourceResult(OutputShapeBase):
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
class AlreadyExistsException(ShapeBase):
    """
    Error returned if an attempt is made to register a patch group with a patch
    baseline that is already registered with a different patch baseline.
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
class AssociatedInstances(ShapeBase):
    """
    You must disassociate a document from all instances before you can delete it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Association(ShapeBase):
    """
    Describes an association of a Systems Manager document and an instance.
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
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "overview",
                "Overview",
                TypeInfo(AssociationOverview),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID created by the system when you create an association. An association
    # is a binding between a document and a set of targets with a schedule.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association version.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the document used in the association.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instances targeted by the request to create an association.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date on which the association was last run.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the association.
    overview: "AssociationOverview" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A cron expression that specifies a schedule when the association runs.
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association name.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociationAlreadyExists(ShapeBase):
    """
    The specified association already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AssociationDescription(ShapeBase):
    """
    Describes the parameters for a document.
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
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
            (
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_association_date",
                "LastUpdateAssociationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(AssociationStatus),
            ),
            (
                "overview",
                "Overview",
                TypeInfo(AssociationOverview),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_execution_date",
                "LastSuccessfulExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association version.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the association was made.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the association was last updated.
    last_update_association_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The association status.
    status: "AssociationStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the association.
    overview: "AssociationOverview" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameters for a document.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The association ID.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instances targeted by the request.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A cron expression that specifies a schedule when the association runs.
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 bucket where you want to store the output details of the
    # request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date on which the association was last run.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date on which the association was successfully run.
    last_successful_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The association name.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociationDoesNotExist(ShapeBase):
    """
    The specified association does not exist.
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
class AssociationExecution(ShapeBase):
    """
    Includes information about the specified association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_count_by_status",
                "ResourceCountByStatus",
                TypeInfo(str),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association version.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution ID for the association. If the association does not run at
    # intervals or according to a schedule, then the ExecutionID is the same as
    # the AssociationID.
    execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the association execution.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed status information about the execution.
    detailed_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the execution started.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date of the last execution.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An aggregate status of the resources in the execution based on the status
    # type.
    resource_count_by_status: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationExecutionDoesNotExist(ShapeBase):
    """
    The specified execution ID does not exist. Verify the ID number and try again.
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
class AssociationExecutionFilter(ShapeBase):
    """
    Filters used in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, AssociationExecutionFilterKey]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, AssociationFilterOperatorType]),
            ),
        ]

    # The key value used in the request.
    key: typing.Union[str, "AssociationExecutionFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value specified for the key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter type specified in the request.
    type: typing.Union[str, "AssociationFilterOperatorType"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )


class AssociationExecutionFilterKey(str):
    ExecutionId = "ExecutionId"
    Status = "Status"
    CreatedTime = "CreatedTime"


@dataclasses.dataclass
class AssociationExecutionTarget(ShapeBase):
    """
    Includes information about the specified association execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                TypeInfo(str),
            ),
            (
                "last_execution_date",
                "LastExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "output_source",
                "OutputSource",
                TypeInfo(OutputSource),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association version.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution ID. If the association does not run at intervals or according
    # to a schedule, then the ExecutionID is the same as the AssociationID.
    execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource ID, for example, the instance ID where the association ran.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource type, for example, instance.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association execution status.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information about the execution status.
    detailed_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date of the last execution.
    last_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The location where the association details are saved.
    output_source: "OutputSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociationExecutionTargetsFilter(ShapeBase):
    """
    Filters for the association execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(
                    typing.Union[str, AssociationExecutionTargetsFilterKey]
                ),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key value used in the request.
    key: typing.Union[str, "AssociationExecutionTargetsFilterKey"
                     ] = dataclasses.field(
                         default=ShapeBase.NOT_SET,
                     )

    # The value specified for the key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AssociationExecutionTargetsFilterKey(str):
    Status = "Status"
    ResourceId = "ResourceId"
    ResourceType = "ResourceType"


@dataclasses.dataclass
class AssociationFilter(ShapeBase):
    """
    Describes a filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(typing.Union[str, AssociationFilterKey]),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: typing.Union[str, "AssociationFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AssociationFilterKey(str):
    InstanceId = "InstanceId"
    Name = "Name"
    AssociationId = "AssociationId"
    AssociationStatusName = "AssociationStatusName"
    LastExecutedBefore = "LastExecutedBefore"
    LastExecutedAfter = "LastExecutedAfter"
    AssociationName = "AssociationName"


class AssociationFilterOperatorType(str):
    EQUAL = "EQUAL"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


@dataclasses.dataclass
class AssociationLimitExceeded(ShapeBase):
    """
    You can have at most 2,000 active associations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AssociationOverview(ShapeBase):
    """
    Information about the association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                TypeInfo(str),
            ),
            (
                "association_status_aggregated_count",
                "AssociationStatusAggregatedCount",
                TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # The status of the association. Status can be: Pending, Success, or Failed.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A detailed status of the association.
    detailed_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the number of targets for the association status. For example, if
    # you created an association with two instances, and one of them was
    # successful, this would return the count of instances by status.
    association_status_aggregated_count: typing.Dict[
        str, int] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class AssociationStatus(ShapeBase):
    """
    Describes an association status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, AssociationStatusName]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "additional_info",
                "AdditionalInfo",
                TypeInfo(str),
            ),
        ]

    # The date when the status changed.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status.
    name: typing.Union[str, "AssociationStatusName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the status.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-defined string.
    additional_info: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AssociationStatusName(str):
    Pending = "Pending"
    Success = "Success"
    Failed = "Failed"


@dataclasses.dataclass
class AssociationVersionInfo(ShapeBase):
    """
    Information about the association version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
        ]

    # The ID created by the system when the association was created.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association version.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the association version was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name specified when the association was created.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of a Systems Manager document used when the association version
    # was created.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Parameters specified when the association version was created.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The targets specified for the association when the association version was
    # created.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cron or rate schedule specified for the association when the
    # association version was created.
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location in Amazon S3 specified for the association when the
    # association version was created.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name specified for the association version when the association version
    # was created.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociationVersionLimitExceeded(ShapeBase):
    """
    You have reached the maximum number versions allowed for an association. Each
    association has a limit of 1,000 versions.
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
class AutomationDefinitionNotFoundException(ShapeBase):
    """
    An Automation document with the specified name could not be found.
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
class AutomationDefinitionVersionNotFoundException(ShapeBase):
    """
    An Automation document with the specified name and version could not be found.
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
class AutomationExecution(ShapeBase):
    """
    Detailed information about the current state of an individual Automation
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "execution_start_time",
                "ExecutionStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_end_time",
                "ExecutionEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "automation_execution_status",
                "AutomationExecutionStatus",
                TypeInfo(typing.Union[str, AutomationExecutionStatus]),
            ),
            (
                "step_executions",
                "StepExecutions",
                TypeInfo(typing.List[StepExecution]),
            ),
            (
                "step_executions_truncated",
                "StepExecutionsTruncated",
                TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "outputs",
                "Outputs",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "failure_message",
                "FailureMessage",
                TypeInfo(str),
            ),
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, ExecutionMode]),
            ),
            (
                "parent_automation_execution_id",
                "ParentAutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "executed_by",
                "ExecutedBy",
                TypeInfo(str),
            ),
            (
                "current_step_name",
                "CurrentStepName",
                TypeInfo(str),
            ),
            (
                "current_action",
                "CurrentAction",
                TypeInfo(str),
            ),
            (
                "target_parameter_name",
                "TargetParameterName",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "target_maps",
                "TargetMaps",
                TypeInfo(typing.List[typing.Dict[str, typing.List[str]]]),
            ),
            (
                "resolved_targets",
                "ResolvedTargets",
                TypeInfo(ResolvedTargets),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
        ]

    # The execution ID.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Automation document used during the execution.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the document to use during execution.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the execution started.
    execution_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the execution finished.
    execution_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The execution status of the Automation.
    automation_execution_status: typing.Union[str, "AutomationExecutionStatus"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # A list of details about the current state of all steps that comprise an
    # execution. An Automation document contains a list of steps that are
    # executed in order.
    step_executions: typing.List["StepExecution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A boolean value that indicates if the response contains the full list of
    # the Automation step executions. If true, use the
    # DescribeAutomationStepExecutions API action to get the full list of step
    # executions.
    step_executions_truncated: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The key-value map of execution parameters, which were supplied when calling
    # StartAutomationExecution.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of execution outputs as defined in the automation document.
    outputs: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message describing why an execution has failed, if the status is set to
    # Failed.
    failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The automation execution mode.
    mode: typing.Union[str, "ExecutionMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AutomationExecutionId of the parent automation.
    parent_automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the user who executed the automation.
    executed_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the currently executing step.
    current_step_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action of the currently executing step.
    current_action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter name.
    target_parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specified targets.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specified key-value mapping of document parameters to target resources.
    target_maps: typing.List[typing.Dict[str, typing.List[str]]
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A list of resolved targets in the rate control execution.
    resolved_targets: "ResolvedTargets" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The MaxConcurrency value specified by the user when the execution started.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MaxErrors value specified by the user when the execution started.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target of the execution.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationExecutionFilter(ShapeBase):
    """
    A filter used to match specific automation executions. This is used to limit the
    scope of Automation execution information returned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, AutomationExecutionFilterKey]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # One or more keys to limit the results. Valid filter keys include the
    # following: DocumentNamePrefix, ExecutionStatus, ExecutionId,
    # ParentExecutionId, CurrentAction, StartTimeBefore, StartTimeAfter.
    key: typing.Union[str, "AutomationExecutionFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The values used to limit the execution information associated with the
    # filter's key.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class AutomationExecutionFilterKey(str):
    DocumentNamePrefix = "DocumentNamePrefix"
    ExecutionStatus = "ExecutionStatus"
    ExecutionId = "ExecutionId"
    ParentExecutionId = "ParentExecutionId"
    CurrentAction = "CurrentAction"
    StartTimeBefore = "StartTimeBefore"
    StartTimeAfter = "StartTimeAfter"


@dataclasses.dataclass
class AutomationExecutionLimitExceededException(ShapeBase):
    """
    The number of simultaneously running Automation executions exceeded the
    allowable limit.
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
class AutomationExecutionMetadata(ShapeBase):
    """
    Details about a specific Automation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "automation_execution_status",
                "AutomationExecutionStatus",
                TypeInfo(typing.Union[str, AutomationExecutionStatus]),
            ),
            (
                "execution_start_time",
                "ExecutionStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_end_time",
                "ExecutionEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "executed_by",
                "ExecutedBy",
                TypeInfo(str),
            ),
            (
                "log_file",
                "LogFile",
                TypeInfo(str),
            ),
            (
                "outputs",
                "Outputs",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, ExecutionMode]),
            ),
            (
                "parent_automation_execution_id",
                "ParentAutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "current_step_name",
                "CurrentStepName",
                TypeInfo(str),
            ),
            (
                "current_action",
                "CurrentAction",
                TypeInfo(str),
            ),
            (
                "failure_message",
                "FailureMessage",
                TypeInfo(str),
            ),
            (
                "target_parameter_name",
                "TargetParameterName",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "target_maps",
                "TargetMaps",
                TypeInfo(typing.List[typing.Dict[str, typing.List[str]]]),
            ),
            (
                "resolved_targets",
                "ResolvedTargets",
                TypeInfo(ResolvedTargets),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
        ]

    # The execution ID.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Automation document used during execution.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document version used during the execution.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the execution. Valid values include: Running, Succeeded,
    # Failed, Timed out, or Cancelled.
    automation_execution_status: typing.Union[str, "AutomationExecutionStatus"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The time the execution started.>
    execution_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the execution finished. This is not populated if the execution is
    # still in progress.
    execution_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM role ARN of the user who executed the Automation.
    executed_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 bucket where execution information is stored.
    log_file: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of execution outputs as defined in the Automation document.
    outputs: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Automation execution mode.
    mode: typing.Union[str, "ExecutionMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ExecutionId of the parent Automation.
    parent_automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the currently executing step.
    current_step_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action of the currently executing step.
    current_action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of execution outputs as defined in the Automation document.
    failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of execution outputs as defined in the Automation document.
    target_parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets defined by the user when starting the Automation.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specified key-value mapping of document parameters to target resources.
    target_maps: typing.List[typing.Dict[str, typing.List[str]]
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A list of targets that resolved during the execution.
    resolved_targets: "ResolvedTargets" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The MaxConcurrency value specified by the user when starting the
    # Automation.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MaxErrors value specified by the user when starting the Automation.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of execution outputs as defined in the Automation document.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutomationExecutionNotFoundException(ShapeBase):
    """
    There is no automation execution information for the requested automation
    execution ID.
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


class AutomationExecutionStatus(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Waiting = "Waiting"
    Success = "Success"
    TimedOut = "TimedOut"
    Cancelling = "Cancelling"
    Cancelled = "Cancelled"
    Failed = "Failed"


@dataclasses.dataclass
class AutomationStepNotFoundException(ShapeBase):
    """
    The specified step name and execution ID don't exist. Verify the information and
    try again.
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
class CancelCommandRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the command you want to cancel.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) A list of instance IDs on which you want to cancel the command.
    # If not provided, the command is canceled on every instance on which it was
    # requested.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CancelCommandResult(OutputShapeBase):
    """
    Whether or not the command was successfully canceled. There is no guarantee that
    a request can be canceled.
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
class CloudWatchOutputConfig(ShapeBase):
    """
    Configuration options for sending command output to CloudWatch Logs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_watch_log_group_name",
                "CloudWatchLogGroupName",
                TypeInfo(str),
            ),
            (
                "cloud_watch_output_enabled",
                "CloudWatchOutputEnabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the CloudWatch log group where you want to send command output.
    # If you don't specify a group name, Systems Manager automatically creates a
    # log group for you. The log group uses the following naming format: aws/ssm/
    # _SystemsManagerDocumentName_.
    cloud_watch_log_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enables Systems Manager to send command output to CloudWatch Logs.
    cloud_watch_output_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Command(ShapeBase):
    """
    Describes a command request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "expires_after",
                "ExpiresAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "requested_date_time",
                "RequestedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CommandStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
            ),
            (
                "output_s3_region",
                "OutputS3Region",
                TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "target_count",
                "TargetCount",
                TypeInfo(int),
            ),
            (
                "completed_count",
                "CompletedCount",
                TypeInfo(int),
            ),
            (
                "error_count",
                "ErrorCount",
                TypeInfo(int),
            ),
            (
                "delivery_timed_out_count",
                "DeliveryTimedOutCount",
                TypeInfo(int),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "notification_config",
                "NotificationConfig",
                TypeInfo(NotificationConfig),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    # A unique identifier for this command.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the document requested for execution.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSM document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-specified information about the command, such as a brief description
    # of what the command should do.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this time is reached and the command has not already started executing,
    # it will not run. Calculated based on the ExpiresAfter user input provided
    # as part of the SendCommand API.
    expires_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter values to be inserted in the document when executing the
    # command.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance IDs against which this command was requested.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of search criteria that targets instances using a Key,Value
    # combination that you specify. Targets is required if you don't provide one
    # or more instance IDs in the call.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the command was requested.
    requested_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the command.
    status: typing.Union[str, "CommandStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A detailed status of the command execution. StatusDetails includes more
    # information than Status because it includes states resulting from error and
    # concurrency control parameters. StatusDetails can show different results
    # than Status. For more information about these statuses, see [Understanding
    # Command Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to any instances.

    #   * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances.

    #   * Success: The command successfully executed on all invocations. This is a terminal state.

    #   * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state.

    #   * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state.

    #   * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state.

    #   * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 bucket where the responses to the command executions should be
    # stored. This was requested when issuing the command.
    output_s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 directory path inside the bucket where the responses to the command
    # executions should be stored. This was requested when issuing the command.
    output_s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of instances that are allowed to execute the command at
    # the same time. You can specify a number of instances, such as 10, or a
    # percentage of instances, such as 10%. The default value is 50. For more
    # information about how to use MaxConcurrency, see [Executing Commands Using
    # Systems Manager Run Command](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/run-command.html) in the _AWS Systems Manager User
    # Guide_.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of errors allowed before the system stops sending the
    # command to additional targets. You can specify a number of errors, such as
    # 10, or a percentage or errors, such as 10%. The default value is 0. For
    # more information about how to use MaxErrors, see [Executing Commands Using
    # Systems Manager Run Command](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/run-command.html) in the _AWS Systems Manager User
    # Guide_.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of targets for the command.
    target_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of targets for which the command invocation reached a terminal
    # state. Terminal states include the following: Success, Failed, Execution
    # Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.
    completed_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of targets for which the status is Failed or Execution Timed
    # Out.
    error_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of targets for which the status is Delivery Timed Out.
    delivery_timed_out_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM service role that Run Command uses to act on your behalf when
    # sending notifications about command status changes.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configurations for sending notifications about command status changes.
    notification_config: "NotificationConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # CloudWatch Logs information where you want Systems Manager to send the
    # command output.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CommandFilter(ShapeBase):
    """
    Describes a command filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(typing.Union[str, CommandFilterKey]),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: typing.Union[str, "CommandFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filter value. Valid values for each filter key are as follows:

    #   * InvokedAfter: A timestamp to limit your results. For example, specify `2018-07-07T00:00:00Z` to see results occurring July 7, 2018, and later.

    #   * InvokedBefore: A timestamp to limit your results. For example, specify `2018-07-07T00:00:00Z` to see results before July 7, 2018.

    #   * Status: Specify a valid command status to see a list of all command executions with that status. Status values you can specify include:

    #     * Pending

    #     * InProgress

    #     * Success

    #     * Cancelled

    #     * Failed

    #     * TimedOut

    #     * Cancelling

    #   * DocumentName: The name of the SSM document for which you want to see command results.

    # For example, specify `AWS-RunPatchBaseline` to see command executions that
    # used this SSM document to perform security patching operations on
    # instances.

    #   * ExecutionStage: An enum whose value can be either `Executing` or `Complete`.

    #     * Specify `Executing` to see a list of command executions that are currently still running.

    #     * Specify `Complete` to see a list of command exeuctions that have already completed.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CommandFilterKey(str):
    InvokedAfter = "InvokedAfter"
    InvokedBefore = "InvokedBefore"
    Status = "Status"
    ExecutionStage = "ExecutionStage"
    DocumentName = "DocumentName"


@dataclasses.dataclass
class CommandInvocation(ShapeBase):
    """
    An invocation is copy of a command sent to a specific instance. A command can
    apply to one or more instances. A command invocation applies to one instance.
    For example, if a user executes SendCommand against three instances, then a
    command invocation is created for each requested instance ID. A command
    invocation returns status and detail information about a command you executed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "instance_name",
                "InstanceName",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "requested_date_time",
                "RequestedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CommandInvocationStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
            ),
            (
                "trace_output",
                "TraceOutput",
                TypeInfo(str),
            ),
            (
                "standard_output_url",
                "StandardOutputUrl",
                TypeInfo(str),
            ),
            (
                "standard_error_url",
                "StandardErrorUrl",
                TypeInfo(str),
            ),
            (
                "command_plugins",
                "CommandPlugins",
                TypeInfo(typing.List[CommandPlugin]),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "notification_config",
                "NotificationConfig",
                TypeInfo(NotificationConfig),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    # The command against which this invocation was requested.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID in which this invocation was requested.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the invocation target. For Amazon EC2 instances this is the
    # value for the aws:Name tag. For on-premises instances, this is the name of
    # the instance.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-specified information about the command, such as a brief description
    # of what the command should do.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document name that was requested for execution.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSM document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time and date the request was sent to this instance.
    requested_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether or not the invocation succeeded, failed, or is pending.
    status: typing.Union[str, "CommandInvocationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A detailed status of the command execution for each invocation (each
    # instance targeted by the command). StatusDetails includes more information
    # than Status because it includes states resulting from error and concurrency
    # control parameters. StatusDetails can show different results than Status.
    # For more information about these statuses, see [Understanding Command
    # Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to the instance.

    #   * In Progress: The command has been sent to the instance but has not reached a terminal state.

    #   * Success: The execution of the command or plugin was successfully completed. This is a terminal state.

    #   * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Gets the trace output sent by the agent.
    trace_output: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to the plugin's StdOut file in Amazon S3, if the Amazon S3 bucket
    # was defined for the parent command. For an invocation, StandardOutputUrl is
    # populated if there is just one plugin defined for the command, and the
    # Amazon S3 bucket was defined for the command.
    standard_output_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to the plugin's StdErr file in Amazon S3, if the Amazon S3 bucket
    # was defined for the parent command. For an invocation, StandardErrorUrl is
    # populated if there is just one plugin defined for the command, and the
    # Amazon S3 bucket was defined for the command.
    standard_error_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    command_plugins: typing.List["CommandPlugin"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM service role that Run Command uses to act on your behalf when
    # sending notifications about command status changes on a per instance basis.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configurations for sending notifications about command status changes on a
    # per instance basis.
    notification_config: "NotificationConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # CloudWatch Logs information where you want Systems Manager to send the
    # command output.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CommandInvocationStatus(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Delayed = "Delayed"
    Success = "Success"
    Cancelled = "Cancelled"
    TimedOut = "TimedOut"
    Failed = "Failed"
    Cancelling = "Cancelling"


@dataclasses.dataclass
class CommandPlugin(ShapeBase):
    """
    Describes plugin details.
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
                "status",
                "Status",
                TypeInfo(typing.Union[str, CommandPluginStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
            ),
            (
                "response_code",
                "ResponseCode",
                TypeInfo(int),
            ),
            (
                "response_start_date_time",
                "ResponseStartDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "response_finish_date_time",
                "ResponseFinishDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "output",
                "Output",
                TypeInfo(str),
            ),
            (
                "standard_output_url",
                "StandardOutputUrl",
                TypeInfo(str),
            ),
            (
                "standard_error_url",
                "StandardErrorUrl",
                TypeInfo(str),
            ),
            (
                "output_s3_region",
                "OutputS3Region",
                TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                TypeInfo(str),
            ),
        ]

    # The name of the plugin. Must be one of the following: aws:updateAgent,
    # aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule,
    # aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of this plugin. You can execute a document with multiple
    # plugins.
    status: typing.Union[str, "CommandPluginStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A detailed status of the plugin execution. StatusDetails includes more
    # information than Status because it includes states resulting from error and
    # concurrency control parameters. StatusDetails can show different results
    # than Status. For more information about these statuses, see [Understanding
    # Command Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to the instance.

    #   * In Progress: The command has been sent to the instance but has not reached a terminal state.

    #   * Success: The execution of the command or plugin was successfully completed. This is a terminal state.

    #   * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Undeliverable: The command can't be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A numeric response code generated after executing the plugin.
    response_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the plugin started executing.
    response_start_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the plugin stopped executing. Could stop prematurely if, for
    # example, a cancel command was sent.
    response_finish_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Output of the plugin execution.
    output: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL for the complete text written by the plugin to stdout in Amazon S3.
    # If the Amazon S3 bucket for the command was not specified, then this string
    # is empty.
    standard_output_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL for the complete text written by the plugin to stderr. If execution
    # is not yet complete, then this string is empty.
    standard_error_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 bucket where the responses to the command executions should be
    # stored. This was requested when issuing the command. For example, in the
    # following response:

    # test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-
    # Fix/i-1234567876543/awsrunShellScript

    # test_folder is the name of the Amazon S3 bucket;

    # ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

    # i-1234567876543 is the instance ID;

    # awsrunShellScript is the name of the plugin.
    output_s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 directory path inside the bucket where the responses to the command
    # executions should be stored. This was requested when issuing the command.
    # For example, in the following response:

    # test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-
    # Fix/i-1234567876543/awsrunShellScript

    # test_folder is the name of the Amazon S3 bucket;

    # ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;

    # i-1234567876543 is the instance ID;

    # awsrunShellScript is the name of the plugin.
    output_s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CommandPluginStatus(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Success = "Success"
    TimedOut = "TimedOut"
    Cancelled = "Cancelled"
    Failed = "Failed"


class CommandStatus(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Success = "Success"
    Cancelled = "Cancelled"
    Failed = "Failed"
    TimedOut = "TimedOut"
    Cancelling = "Cancelling"


@dataclasses.dataclass
class ComplianceExecutionSummary(ShapeBase):
    """
    A summary of the call execution that includes an execution ID, the type of
    execution (for example, `Command`), and the date/time of the execution using a
    datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "execution_time",
                "ExecutionTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_id",
                "ExecutionId",
                TypeInfo(str),
            ),
            (
                "execution_type",
                "ExecutionType",
                TypeInfo(str),
            ),
        ]

    # The time the execution ran as a datetime object that is saved in the
    # following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    execution_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An ID created by the system when `PutComplianceItems` was called. For
    # example, `CommandID` is a valid execution ID. You can use this ID in
    # subsequent calls.
    execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of execution. For example, `Command` is a valid execution type.
    execution_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComplianceItem(ShapeBase):
    """
    Information about the compliance as defined by the resource type. For example,
    for a patch resource type, `Items` includes information about the PatchSeverity,
    Classification, etc.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ComplianceStatus]),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(typing.Union[str, ComplianceSeverity]),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                TypeInfo(ComplianceExecutionSummary),
            ),
            (
                "details",
                "Details",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The compliance type. For example, Association (for a State Manager
    # association), Patch, or Custom:`string` are all valid compliance types.
    compliance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource. `ManagedInstance` is currently the only supported
    # resource type.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ID for the resource. For a managed instance, this is the instance ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ID for the compliance item. For example, if the compliance item is a
    # Windows patch, the ID could be the number of the KB article; for example:
    # KB4010320.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A title for the compliance item. For example, if the compliance item is a
    # Windows patch, the title could be the title of the KB article for the
    # patch; for example: Security Update for Active Directory Federation
    # Services.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the compliance item. An item is either COMPLIANT or
    # NON_COMPLIANT.
    status: typing.Union[str, "ComplianceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The severity of the compliance status. Severity can be one of the
    # following: Critical, High, Medium, Low, Informational, Unspecified.
    severity: typing.Union[str, "ComplianceSeverity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A summary for the compliance item. The summary includes an execution ID,
    # the execution type (for example, command), and the execution time.
    execution_summary: "ComplianceExecutionSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A "Key": "Value" tag combination for the compliance item.
    details: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceItemEntry(ShapeBase):
    """
    Information about a compliance item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "severity",
                "Severity",
                TypeInfo(typing.Union[str, ComplianceSeverity]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ComplianceStatus]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "details",
                "Details",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The severity of the compliance status. Severity can be one of the
    # following: Critical, High, Medium, Low, Informational, Unspecified.
    severity: typing.Union[str, "ComplianceSeverity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the compliance item. An item is either COMPLIANT or
    # NON_COMPLIANT.
    status: typing.Union[str, "ComplianceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compliance item ID. For example, if the compliance item is a Windows
    # patch, the ID could be the number of the KB article.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The title of the compliance item. For example, if the compliance item is a
    # Windows patch, the title could be the title of the KB article for the
    # patch; for example: Security Update for Active Directory Federation
    # Services.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A "Key": "Value" tag combination for the compliance item.
    details: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ComplianceQueryOperatorType(str):
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    BEGIN_WITH = "BEGIN_WITH"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


class ComplianceSeverity(str):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNSPECIFIED = "UNSPECIFIED"


class ComplianceStatus(str):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"


@dataclasses.dataclass
class ComplianceStringFilter(ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of results.
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
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ComplianceQueryOperatorType]),
            ),
        ]

    # The name of the filter.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for which to search.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of comparison that should be performed for the value: Equal,
    # NotEqual, BeginWith, LessThan, or GreaterThan.
    type: typing.Union[str, "ComplianceQueryOperatorType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceSummaryItem(ShapeBase):
    """
    A summary of compliance information by compliance type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                TypeInfo(str),
            ),
            (
                "compliant_summary",
                "CompliantSummary",
                TypeInfo(CompliantSummary),
            ),
            (
                "non_compliant_summary",
                "NonCompliantSummary",
                TypeInfo(NonCompliantSummary),
            ),
        ]

    # The type of compliance item. For example, the compliance type can be
    # Association, Patch, or Custom:string.
    compliance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of COMPLIANT items for the specified compliance type.
    compliant_summary: "CompliantSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of NON_COMPLIANT items for the specified compliance type.
    non_compliant_summary: "NonCompliantSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ComplianceTypeCountLimitExceededException(ShapeBase):
    """
    You specified too many custom compliance types. You can specify a maximum of 10
    different types.
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
class CompliantSummary(ShapeBase):
    """
    A summary of resources that are compliant. The summary is organized according to
    the resource count for each compliance type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliant_count",
                "CompliantCount",
                TypeInfo(int),
            ),
            (
                "severity_summary",
                "SeveritySummary",
                TypeInfo(SeveritySummary),
            ),
        ]

    # The total number of resources that are compliant.
    compliant_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of the compliance severity by compliance type.
    severity_summary: "SeveritySummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ConnectionStatus(str):
    Connected = "Connected"
    NotConnected = "NotConnected"


@dataclasses.dataclass
class CreateActivationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_role",
                "IamRole",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "default_instance_name",
                "DefaultInstanceName",
                TypeInfo(str),
            ),
            (
                "registration_limit",
                "RegistrationLimit",
                TypeInfo(int),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Identity and Access Management (IAM) role that you want to
    # assign to the managed instance.
    iam_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-defined description of the resource that you want to register with
    # Amazon EC2.

    # Do not enter personally identifiable information in this field.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the registered, managed instance as it will appear in the
    # Amazon EC2 console or when you use the AWS command line tools to list EC2
    # resources.

    # Do not enter personally identifiable information in this field.
    default_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the maximum number of managed instances you want to register. The
    # default value is 1 instance.
    registration_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date by which this activation request should expire. The default value
    # is 24 hours.
    expiration_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateActivationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activation_id",
                "ActivationId",
                TypeInfo(str),
            ),
            (
                "activation_code",
                "ActivationCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID number generated by the system when it processed the activation. The
    # activation ID functions like a user name.
    activation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code the system generates when it processes the activation. The
    # activation code functions like a password to validate the activation ID.
    activation_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssociationBatchRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[CreateAssociationBatchRequestEntry]),
            ),
        ]

    # One or more associations.
    entries: typing.List["CreateAssociationBatchRequestEntry"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


@dataclasses.dataclass
class CreateAssociationBatchRequestEntry(ShapeBase):
    """
    Describes the association of a Systems Manager document and an instance.
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
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameters for a document.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instances targeted by the request.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A cron expression that specifies a schedule when the association runs.
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 bucket where you want to store the results of this request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify a descriptive name for the association.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssociationBatchResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful",
                "Successful",
                TypeInfo(typing.List[AssociationDescription]),
            ),
            (
                "failed",
                "Failed",
                TypeInfo(typing.List[FailedCreateAssociation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the associations that succeeded.
    successful: typing.List["AssociationDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the associations that failed.
    failed: typing.List["FailedCreateAssociation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssociationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document version you want to associate with the target(s). Can be a
    # specific version or the default version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters for the documents runtime configuration.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags) for the association.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A cron expression when the association will be applied to the target(s).
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 bucket where you want to store the output details of the
    # request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify a descriptive name for the association.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssociationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_description: "AssociationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_type",
                "DocumentType",
                TypeInfo(typing.Union[str, DocumentType]),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(str),
            ),
        ]

    # A valid JSON or YAML string.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the Systems Manager document.

    # Do not use the following to begin the names of documents you create. They
    # are reserved by AWS for use as document prefixes:

    #   * `aws`

    #   * `amazon`

    #   * `amzn`
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of document to create. Valid document types include: Policy,
    # Automation, and Command.
    document_type: typing.Union[str, "DocumentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify the document format for the request. The document format can be
    # either JSON or YAML. JSON is the default format.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify a target type to define the kinds of resources the document can run
    # on. For example, to run a document on EC2 instances, specify the following
    # value: /AWS::EC2::Instance. If you specify a value of '/' the document can
    # run on all types of resources. If you don't specify a value, the document
    # can't run on any resources. For a list of valid resource types, see [AWS
    # Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the _AWS CloudFormation User Guide_.
    target_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDocumentResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_description",
                "DocumentDescription",
                TypeInfo(DocumentDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the Systems Manager document.
    document_description: "DocumentDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                TypeInfo(bool),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
        ]

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables a Maintenance Window task to execute on managed instances, even if
    # you have not registered those instances as targets. If enabled, then you
    # must specify the unregistered instances (by instance ID) when you register
    # a task with the Maintenance Window

    # If you don't enable this option, then you must specify previously-
    # registered targets when you register a task with the Maintenance Window.
    allow_unassociated_targets: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional description for the Maintenance Window. We recommend specifying
    # a description to help you organize your Maintenance Windows.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the created Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "global_filters",
                "GlobalFilters",
                TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                TypeInfo(typing.Union[str, PatchComplianceLevel]),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[PatchSource]),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
        ]

    # The name of the patch baseline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines the operating system the patch baseline applies to. The Default
    # value is WINDOWS.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly approved patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    approved_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines the compliance level for approved patches. This means that if an
    # approved patch is reported as missing, this is the severity of the
    # compliance violation. The default value is UNSPECIFIED.
    approved_patches_compliance_level: typing.Union[
        str, "PatchComplianceLevel"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    rejected_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the patch baseline.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the created patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceDataSyncRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                TypeInfo(str),
            ),
            (
                "s3_destination",
                "S3Destination",
                TypeInfo(ResourceDataSyncS3Destination),
            ),
        ]

    # A name for the configuration.
    sync_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon S3 configuration details for the sync.
    s3_destination: "ResourceDataSyncS3Destination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateResourceDataSyncResult(OutputShapeBase):
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
class CustomSchemaCountLimitExceededException(ShapeBase):
    """
    You have exceeded the limit for custom schemas. Delete one or more custom
    schemas and try again.
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
class DeleteActivationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activation_id",
                "ActivationId",
                TypeInfo(str),
            ),
        ]

    # The ID of the activation that you want to delete.
    activation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteActivationResult(OutputShapeBase):
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
class DeleteAssociationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association ID that you want to delete.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAssociationResult(OutputShapeBase):
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
class DeleteDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDocumentResult(OutputShapeBase):
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
class DeleteInventoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "schema_delete_option",
                "SchemaDeleteOption",
                TypeInfo(typing.Union[str, InventorySchemaDeleteOption]),
            ),
            (
                "dry_run",
                "DryRun",
                TypeInfo(bool),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
        ]

    # The name of the custom inventory type for which you want to delete either
    # all previously collected data, or the inventory type itself.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use the `SchemaDeleteOption` to delete a custom inventory type (schema). If
    # you don't choose this option, the system only deletes existing inventory
    # data associated with the custom inventory type. Choose one of the following
    # options:

    # DisableSchema: If you choose this option, the system ignores all inventory
    # data for the specified version, and any earlier versions. To enable this
    # schema again, you must call the `PutInventory` action for a version greater
    # than the disbled version.

    # DeleteSchema: This option deletes the specified custom type from the
    # Inventory service. You can recreate the schema later, if you want.
    schema_delete_option: typing.Union[str, "InventorySchemaDeleteOption"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Use this option to view a summary of the deletion request without deleting
    # any data or the data type. This option is useful when you only want to
    # understand what will be deleted. Once you validate that the data to be
    # deleted is what you intend to delete, you can run the same command without
    # specifying the `DryRun` option.
    dry_run: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInventoryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deletion_id",
                "DeletionId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "deletion_summary",
                "DeletionSummary",
                TypeInfo(InventoryDeletionSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Every `DeleteInventory` action is assigned a unique ID. This option returns
    # a unique ID. You can use this ID to query the status of a delete operation.
    # This option is useful for ensuring that a delete operation has completed
    # before you begin other actions.
    deletion_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the inventory data type specified in the request.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of the delete operation. For more information about this summary,
    # see [Understanding the Delete Inventory
    # Summary](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/sysman-inventory-delete.html#sysman-inventory-
    # delete-summary) in the _AWS Systems Manager User Guide_.
    deletion_summary: "InventoryDeletionSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window to delete.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the deleted Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteParameterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter to delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteParameterResult(OutputShapeBase):
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
class DeleteParametersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the parameters to delete.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteParametersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deleted_parameters",
                "DeletedParameters",
                TypeInfo(typing.List[str]),
            ),
            (
                "invalid_parameters",
                "InvalidParameters",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the deleted parameters.
    deleted_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of parameters that weren't deleted because the parameters are not
    # valid.
    invalid_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletePatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to delete.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the deleted patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceDataSyncRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration to delete.
    sync_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceDataSyncResult(OutputShapeBase):
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
class DeregisterManagedInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The ID assigned to the managed instance when you registered it using the
    # activation process.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterManagedInstanceResult(OutputShapeBase):
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
class DeregisterPatchBaselineForPatchGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to deregister the patch group from.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch group that should be deregistered from the patch
    # baseline.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterPatchBaselineForPatchGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline the patch group was deregistered from.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch group deregistered from the patch baseline.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTargetFromMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
            (
                "safe",
                "Safe",
                TypeInfo(bool),
            ),
        ]

    # The ID of the Maintenance Window the target should be removed from.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the target definition to remove.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The system checks if the target is being referenced by a task. If the
    # target is being referenced, the system returns an error and does not
    # deregister the target from the Maintenance Window.
    safe: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTargetFromMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window the target was removed from.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the removed target definition.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTaskFromMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window the task should be removed from.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the task to remove from the Maintenance Window.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTaskFromMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window the task was removed from.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the task removed from the Maintenance Window.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActivationsFilter(ShapeBase):
    """
    Filter for the DescribeActivation API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_key",
                "FilterKey",
                TypeInfo(typing.Union[str, DescribeActivationsFilterKeys]),
            ),
            (
                "filter_values",
                "FilterValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    filter_key: typing.Union[str, "DescribeActivationsFilterKeys"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # The filter values.
    filter_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DescribeActivationsFilterKeys(str):
    ActivationIds = "ActivationIds"
    DefaultInstanceName = "DefaultInstanceName"
    IamRole = "IamRole"


@dataclasses.dataclass
class DescribeActivationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[DescribeActivationsFilter]),
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

    # A filter to view information about your activations.
    filters: typing.List["DescribeActivationsFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActivationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activation_list",
                "ActivationList",
                TypeInfo(typing.List[Activation]),
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

    # A list of activations for your AWS account.
    activation_list: typing.List["Activation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeActivationsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeAssociationExecutionTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[AssociationExecutionTargetsFilter]),
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

    # The association ID that includes the execution for which you want to view
    # details.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution ID for which you want to view details.
    execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters for the request. You can specify the following filters and values.

    # Status (EQUAL)

    # ResourceId (EQUAL)

    # ResourceType (EQUAL)
    filters: typing.List["AssociationExecutionTargetsFilter"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionTargetsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_execution_targets",
                "AssociationExecutionTargets",
                TypeInfo(typing.List[AssociationExecutionTarget]),
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

    # Information about the execution.
    association_execution_targets: typing.List["AssociationExecutionTarget"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[AssociationExecutionFilter]),
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

    # The association ID for which you want to view execution history details.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters for the request. You can specify the following filters and values.

    # ExecutionId (EQUAL)

    # Status (EQUAL)

    # CreatedTime (EQUAL, GREATER_THAN, LESS_THAN)
    filters: typing.List["AssociationExecutionFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationExecutionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_executions",
                "AssociationExecutions",
                TypeInfo(typing.List[AssociationExecution]),
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

    # A list of the executions for the specified association ID.
    association_executions: typing.List["AssociationExecution"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association ID for which you want information.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the association version to retrieve. To view the latest version,
    # either specify `$LATEST` for this parameter, or omit this parameter. To
    # view a list of all associations for an instance, use
    # ListInstanceAssociations. To get a list of versions for a specific
    # association, use ListAssociationVersions.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAssociationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_description: "AssociationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAutomationExecutionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[AutomationExecutionFilter]),
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

    # Filters used to limit the scope of executions that are requested.
    filters: typing.List["AutomationExecutionFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAutomationExecutionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "automation_execution_metadata_list",
                "AutomationExecutionMetadataList",
                TypeInfo(typing.List[AutomationExecutionMetadata]),
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

    # The list of details about each automation execution which has occurred
    # which matches the filter specification, if any.
    automation_execution_metadata_list: typing.List[
        "AutomationExecutionMetadata"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAutomationStepExecutionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[StepExecutionFilter]),
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
                "reverse_order",
                "ReverseOrder",
                TypeInfo(bool),
            ),
        ]

    # The Automation execution ID for which you want step execution descriptions.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more filters to limit the number of step executions returned by the
    # request.
    filters: typing.List["StepExecutionFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean that indicates whether to list step executions in reverse order
    # by start time. The default value is false.
    reverse_order: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAutomationStepExecutionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "step_executions",
                "StepExecutions",
                TypeInfo(typing.List[StepExecution]),
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

    # A list of details about the current state of all steps that make up an
    # execution.
    step_executions: typing.List["StepExecution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAvailablePatchesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[PatchOrchestratorFilter]),
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

    # Filters used to scope down the returned patches.
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAvailablePatchesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "patches",
                "Patches",
                TypeInfo(typing.List[Patch]),
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

    # An array of patches. Each entry in the array is a patch structure.
    patches: typing.List["Patch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentPermissionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "permission_type",
                "PermissionType",
                TypeInfo(typing.Union[str, DocumentPermissionType]),
            ),
        ]

    # The name of the document for which you are the owner.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The permission type for the document. The permission type can be _Share_.
    permission_type: typing.Union[str, "DocumentPermissionType"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class DescribeDocumentPermissionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The account IDs that have permission to use this document. The ID can be
    # either an AWS account or _All_.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document version for which you want information. Can be a specific
    # version or the default version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDocumentResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document",
                "Document",
                TypeInfo(DocumentDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the Systems Manager document.
    document: "DocumentDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEffectiveInstanceAssociationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
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

    # The instance ID for which you want to view all associations.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEffectiveInstanceAssociationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associations",
                "Associations",
                TypeInfo(typing.List[InstanceAssociation]),
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

    # The associations for the requested instance.
    associations: typing.List["InstanceAssociation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEffectivePatchesForPatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
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

    # The ID of the patch baseline to retrieve the effective patches for.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEffectivePatchesForPatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "effective_patches",
                "EffectivePatches",
                TypeInfo(typing.List[EffectivePatch]),
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

    # An array of patches and patch status.
    effective_patches: typing.List["EffectivePatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceAssociationsStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
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

    # The instance IDs for which you want association status information.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceAssociationsStatusResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_association_status_infos",
                "InstanceAssociationStatusInfos",
                TypeInfo(typing.List[InstanceAssociationStatusInfo]),
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

    # Status information about the association.
    instance_association_status_infos: typing.List[
        "InstanceAssociationStatusInfo"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceInformationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_information_filter_list",
                "InstanceInformationFilterList",
                TypeInfo(typing.List[InstanceInformationFilter]),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[InstanceInformationStringFilter]),
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

    # This is a legacy method. We recommend that you don't use this method.
    # Instead, use the InstanceInformationFilter action. The
    # `InstanceInformationFilter` action enables you to return instance
    # information by using tags that are specified as a key-value mapping.

    # If you do use this method, then you can't use the
    # `InstanceInformationFilter` action. Using this method and the
    # `InstanceInformationFilter` action causes an exception error.
    instance_information_filter_list: typing.List["InstanceInformationFilter"
                                                 ] = dataclasses.field(
                                                     default=ShapeBase.NOT_SET,
                                                 )

    # One or more filters. Use a filter to return a more specific list of
    # instances.
    filters: typing.List["InstanceInformationStringFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstanceInformationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_information_list",
                "InstanceInformationList",
                TypeInfo(typing.List[InstanceInformation]),
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

    # The instance information list.
    instance_information_list: typing.List["InstanceInformation"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeInstanceInformationResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeInstancePatchStatesForPatchGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[InstancePatchStateFilter]),
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

    # The name of the patch group for which the patch state information should be
    # retrieved.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Each entry in the array is a structure containing:

    # Key (string between 1 and 200 characters)

    # Values (array containing a single string)

    # Type (string "Equal", "NotEqual", "LessThan", "GreaterThan")
    filters: typing.List["InstancePatchStateFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesForPatchGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_patch_states",
                "InstancePatchStates",
                TypeInfo(typing.List[InstancePatchState]),
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

    # The high-level patch state for the requested instances.
    instance_patch_states: typing.List["InstancePatchState"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
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

    # The ID of the instance whose patch state information should be retrieved.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of instances to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchStatesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_patch_states",
                "InstancePatchStates",
                TypeInfo(typing.List[InstancePatchState]),
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

    # The high-level patch state for the requested instances.
    instance_patch_states: typing.List["InstancePatchState"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[PatchOrchestratorFilter]),
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

    # The ID of the instance whose patch state information should be retrieved.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Each entry in the array is a structure containing:

    # Key (string, between 1 and 128 characters)

    # Values (array of strings, each string between 1 and 256 characters)
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of patches to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInstancePatchesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "patches",
                "Patches",
                TypeInfo(typing.List[PatchComplianceData]),
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

    # Each entry in the array is a structure containing:

    # Title (string)

    # KBId (string)

    # Classification (string)

    # Severity (string)

    # State (string: "INSTALLED", "INSTALLED OTHER", "MISSING", "NOT APPLICABLE",
    # "FAILED")

    # InstalledTime (DateTime)

    # InstalledBy (string)
    patches: typing.List["PatchComplianceData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInventoryDeletionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_id",
                "DeletionId",
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

    # Specify the delete inventory ID for which you want information. This ID was
    # returned by the `DeleteInventory` action.
    deletion_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInventoryDeletionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "inventory_deletions",
                "InventoryDeletions",
                TypeInfo(typing.List[InventoryDeletionStatusItem]),
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

    # A list of status items for deleted inventory.
    inventory_deletions: typing.List["InventoryDeletionStatusItem"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTaskInvocationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_id",
                "TaskId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[MaintenanceWindowFilter]),
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

    # The ID of the Maintenance Window execution the task is part of.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specific task in the Maintenance Window task that should be
    # retrieved.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional filters used to scope down the returned task invocations. The
    # supported filter key is STATUS with the corresponding values PENDING,
    # IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTaskInvocationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_task_invocation_identities",
                "WindowExecutionTaskInvocationIdentities",
                TypeInfo(
                    typing.
                    List[MaintenanceWindowExecutionTaskInvocationIdentity]
                ),
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

    # Information about the task invocation results per invocation.
    window_execution_task_invocation_identities: typing.List[
        "MaintenanceWindowExecutionTaskInvocationIdentity"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTasksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[MaintenanceWindowFilter]),
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

    # The ID of the Maintenance Window execution whose task executions should be
    # retrieved.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional filters used to scope down the returned tasks. The supported
    # filter key is STATUS with the corresponding values PENDING, IN_PROGRESS,
    # SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionTasksResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_task_identities",
                "WindowExecutionTaskIdentities",
                TypeInfo(typing.List[MaintenanceWindowExecutionTaskIdentity]),
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

    # Information about the task executions.
    window_execution_task_identities: typing.List[
        "MaintenanceWindowExecutionTaskIdentity"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[MaintenanceWindowFilter]),
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

    # The ID of the Maintenance Window whose executions should be retrieved.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Each entry in the array is a structure containing:

    # Key (string, between 1 and 128 characters)

    # Values (array of strings, each string is between 1 and 256 characters)

    # The supported Keys are ExecutedBefore and ExecutedAfter with the value
    # being a date/time string such as 2016-11-04T05:00:00Z.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowExecutionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_executions",
                "WindowExecutions",
                TypeInfo(typing.List[MaintenanceWindowExecution]),
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

    # Information about the Maintenance Windows execution.
    window_executions: typing.List["MaintenanceWindowExecution"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[MaintenanceWindowFilter]),
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

    # The ID of the Maintenance Window whose targets should be retrieved.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional filters that can be used to narrow down the scope of the returned
    # window targets. The supported filter keys are Type, WindowTargetId and
    # OwnerInformation.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTargetsResult(OutputShapeBase):
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
                TypeInfo(typing.List[MaintenanceWindowTarget]),
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

    # Information about the targets in the Maintenance Window.
    targets: typing.List["MaintenanceWindowTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTasksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[MaintenanceWindowFilter]),
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

    # The ID of the Maintenance Window whose tasks should be retrieved.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional filters used to narrow down the scope of the returned tasks. The
    # supported filter keys are WindowTaskId, TaskArn, Priority, and TaskType.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowTasksResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tasks",
                "Tasks",
                TypeInfo(typing.List[MaintenanceWindowTask]),
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

    # Information about the tasks in the Maintenance Window.
    tasks: typing.List["MaintenanceWindowTask"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[MaintenanceWindowFilter]),
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

    # Optional filters used to narrow down the scope of the returned Maintenance
    # Windows. Supported filter keys are Name and Enabled.
    filters: typing.List["MaintenanceWindowFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceWindowsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_identities",
                "WindowIdentities",
                TypeInfo(typing.List[MaintenanceWindowIdentity]),
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

    # Information about the Maintenance Windows.
    window_identities: typing.List["MaintenanceWindowIdentity"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeParametersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[ParametersFilter]),
            ),
            (
                "parameter_filters",
                "ParameterFilters",
                TypeInfo(typing.List[ParameterStringFilter]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["ParametersFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters to limit the request results.
    parameter_filters: typing.List["ParameterStringFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeParametersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[ParameterMetadata]),
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

    # Parameters returned by the request.
    parameters: typing.List["ParameterMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeParametersResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribePatchBaselinesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[PatchOrchestratorFilter]),
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

    # Each element in the array is a structure containing:

    # Key: (string, "NAME_PREFIX" or "OWNER")

    # Value: (array of strings, exactly 1 entry, between 1 and 255 characters)
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of patch baselines to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchBaselinesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_identities",
                "BaselineIdentities",
                TypeInfo(typing.List[PatchBaselineIdentity]),
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

    # An array of PatchBaselineIdentity elements.
    baseline_identities: typing.List["PatchBaselineIdentity"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchGroupStateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
        ]

    # The name of the patch group whose patch snapshot should be retrieved.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchGroupStateResult(OutputShapeBase):
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
                TypeInfo(int),
            ),
            (
                "instances_with_installed_patches",
                "InstancesWithInstalledPatches",
                TypeInfo(int),
            ),
            (
                "instances_with_installed_other_patches",
                "InstancesWithInstalledOtherPatches",
                TypeInfo(int),
            ),
            (
                "instances_with_missing_patches",
                "InstancesWithMissingPatches",
                TypeInfo(int),
            ),
            (
                "instances_with_failed_patches",
                "InstancesWithFailedPatches",
                TypeInfo(int),
            ),
            (
                "instances_with_not_applicable_patches",
                "InstancesWithNotApplicablePatches",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances in the patch group.
    instances: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances with installed patches.
    instances_with_installed_patches: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances with patches installed that aren't defined in the
    # patch baseline.
    instances_with_installed_other_patches: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances with missing patches from the patch baseline.
    instances_with_missing_patches: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances with patches from the patch baseline that failed to
    # install.
    instances_with_failed_patches: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances with patches that aren't applicable.
    instances_with_not_applicable_patches: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribePatchGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[PatchOrchestratorFilter]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of patch groups to return (per page).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["PatchOrchestratorFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePatchGroupsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "mappings",
                "Mappings",
                TypeInfo(typing.List[PatchGroupPatchBaselineMapping]),
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

    # Each entry in the array contains:

    # PatchGroup: string (between 1 and 256 characters, Regex:
    # ^([\p{L}\p{Z}\p{N}_.:/=+\\-@]*)$)

    # PatchBaselineIdentity: A PatchBaselineIdentity element.
    mappings: typing.List["PatchGroupPatchBaselineMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSessionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, SessionState]),
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
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[SessionFilter]),
            ),
        ]

    # The session status to retrieve a list of sessions for. For example,
    # "active".
    state: typing.Union[str, "SessionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more filters to limit the type of sessions returned by the request.
    filters: typing.List["SessionFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSessionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sessions",
                "Sessions",
                TypeInfo(typing.List[Session]),
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

    # A list of sessions meeting the request parameters.
    sessions: typing.List["Session"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentAlreadyExists(ShapeBase):
    """
    The specified document already exists.
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
class DocumentDefaultVersionDescription(ShapeBase):
    """
    A default version of a document.
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
                "default_version",
                "DefaultVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default version of the document.
    default_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentDescription(ShapeBase):
    """
    Describes a Systems Manager document.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sha1",
                "Sha1",
                TypeInfo(str),
            ),
            (
                "hash",
                "Hash",
                TypeInfo(str),
            ),
            (
                "hash_type",
                "HashType",
                TypeInfo(typing.Union[str, DocumentHashType]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, DocumentStatus]),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[DocumentParameter]),
            ),
            (
                "platform_types",
                "PlatformTypes",
                TypeInfo(typing.List[typing.Union[str, PlatformType]]),
            ),
            (
                "document_type",
                "DocumentType",
                TypeInfo(typing.Union[str, DocumentType]),
            ),
            (
                "schema_version",
                "SchemaVersion",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "default_version",
                "DefaultVersion",
                TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The SHA1 hash of the document, which you can use for verification.
    sha1: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Sha256 or Sha1 hash created by the system when the document was
    # created.

    # Sha1 hashes have been deprecated.
    hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sha256 or Sha1.

    # Sha1 hashes have been deprecated.
    hash_type: typing.Union[str, "DocumentHashType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS user account that created the document.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the document was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the Systems Manager document.
    status: typing.Union[str, "DocumentStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the document.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameters for a document.
    parameters: typing.List["DocumentParameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of OS platforms compatible with this Systems Manager document.
    platform_types: typing.List[typing.Union[str, "PlatformType"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The type of document.
    document_type: typing.Union[str, "DocumentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The schema version.
    schema_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the document.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default version.
    default_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document format, either JSON or YAML.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target type which defines the kinds of resources the document can run
    # on. For example, /AWS::EC2::Instance. For a list of valid resource types,
    # see [AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the _AWS CloudFormation User Guide_.
    target_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags, or metadata, that have been applied to the document.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentFilter(ShapeBase):
    """
    Describes a filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(typing.Union[str, DocumentFilterKey]),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: typing.Union[str, "DocumentFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of the filter.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DocumentFilterKey(str):
    Name = "Name"
    Owner = "Owner"
    PlatformTypes = "PlatformTypes"
    DocumentType = "DocumentType"


class DocumentFormat(str):
    YAML = "YAML"
    JSON = "JSON"


class DocumentHashType(str):
    Sha256 = "Sha256"
    Sha1 = "Sha1"


@dataclasses.dataclass
class DocumentIdentifier(ShapeBase):
    """
    Describes the name of a Systems Manager document.
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
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "platform_types",
                "PlatformTypes",
                TypeInfo(typing.List[typing.Union[str, PlatformType]]),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "document_type",
                "DocumentType",
                TypeInfo(typing.Union[str, DocumentType]),
            ),
            (
                "schema_version",
                "SchemaVersion",
                TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS user account that created the document.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system platform.
    platform_types: typing.List[typing.Union[str, "PlatformType"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document type.
    document_type: typing.Union[str, "DocumentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The schema version.
    schema_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document format, either JSON or YAML.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target type which defines the kinds of resources the document can run
    # on. For example, /AWS::EC2::Instance. For a list of valid resource types,
    # see [AWS Resource Types
    # Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
    # template-resource-type-ref.html) in the _AWS CloudFormation User Guide_.
    target_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags, or metadata, that have been applied to the document.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentKeyValuesFilter(ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of documents.

    For keys, you can specify one or more tags that have been applied to a document.

    Other valid values include Owner, Name, PlatformTypes, and DocumentType.

    Note that only one Owner can be specified in a request. For example:
    `Key=Owner,Values=Self`.

    If you use Name as a key, you can use a name prefix to return a list of
    documents. For example, in the AWS CLI, to return a list of all documents that
    begin with `Te`, run the following command:

    `aws ssm list-documents --filters Key=Name,Values=Te`

    If you specify more than two keys, only documents that are identified by all the
    tags are returned in the results. If you specify more than two values for a key,
    documents that are identified by any of the values are returned in the results.

    To specify a custom key and value pair, use the format
    `Key=tag:[tagName],Values=[valueName]`.

    For example, if you created a Key called region and are using the AWS CLI to
    call the `list-documents` command:

    `aws ssm list-documents --filters Key=tag:region,Values=east,west
    Key=Owner,Values=Self`
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

    # The name of the filter key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the filter key.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DocumentLimitExceeded(ShapeBase):
    """
    You can have at most 200 active Systems Manager documents.
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
class DocumentParameter(ShapeBase):
    """
    Parameters specified in a System Manager document that execute on the server
    when the command is run.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, DocumentParameterType]),
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
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of parameter. The type can be either String or StringList.
    type: typing.Union[str, "DocumentParameterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of what the parameter does, how to use it, the default value,
    # and whether or not the parameter is optional.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If specified, the default values for the parameters. Parameters without a
    # default value are required. Parameters with a default value are optional.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DocumentParameterType(str):
    String = "String"
    StringList = "StringList"


@dataclasses.dataclass
class DocumentPermissionLimit(ShapeBase):
    """
    The document cannot be shared with more AWS user accounts. You can share a
    document with a maximum of 20 accounts. You can publicly share up to five
    documents. If you need to increase this limit, contact AWS Support.
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


class DocumentPermissionType(str):
    Share = "Share"


class DocumentStatus(str):
    Creating = "Creating"
    Active = "Active"
    Updating = "Updating"
    Deleting = "Deleting"


class DocumentType(str):
    Command = "Command"
    Policy = "Policy"
    Automation = "Automation"
    Session = "Session"


@dataclasses.dataclass
class DocumentVersionInfo(ShapeBase):
    """
    Version information about the document.
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
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "is_default_version",
                "IsDefaultVersion",
                TypeInfo(bool),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
        ]

    # The document name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the document was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier for the default version of the document.
    is_default_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document format, either JSON or YAML.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DocumentVersionLimitExceeded(ShapeBase):
    """
    The document has too many versions. Delete one or more document versions and try
    again.
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
class DoesNotExistException(ShapeBase):
    """
    Error returned when the ID specified for a resource, such as a Maintenance
    Window or Patch baseline, doesn't exist.

    For information about resource limits in Systems Manager, see [AWS Systems
    Manager
    Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_ssm).
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
class DuplicateDocumentContent(ShapeBase):
    """
    The content of the association document matches another document. Change the
    content of the document and try again.
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
class DuplicateInstanceId(ShapeBase):
    """
    You cannot specify an instance ID in more than one association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EffectivePatch(ShapeBase):
    """
    The EffectivePatch structure defines metadata about a patch along with the
    approval state of the patch in a particular patch baseline. The approval state
    includes information about whether the patch is currently approved, due to be
    approved by a rule, explicitly approved, or explicitly rejected and the date the
    patch was or will be approved.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch",
                "Patch",
                TypeInfo(Patch),
            ),
            (
                "patch_status",
                "PatchStatus",
                TypeInfo(PatchStatus),
            ),
        ]

    # Provides metadata for a patch, including information such as the KB ID,
    # severity, classification and a URL for where more information can be
    # obtained about the patch.
    patch: "Patch" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the patch in a patch baseline. This includes information
    # about whether the patch is currently approved, due to be approved by a
    # rule, explicitly approved, or explicitly rejected and the date the patch
    # was or will be approved.
    patch_status: "PatchStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExecutionMode(str):
    Auto = "Auto"
    Interactive = "Interactive"


@dataclasses.dataclass
class FailedCreateAssociation(ShapeBase):
    """
    Describes a failed association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entry",
                "Entry",
                TypeInfo(CreateAssociationBatchRequestEntry),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "fault",
                "Fault",
                TypeInfo(typing.Union[str, Fault]),
            ),
        ]

    # The association.
    entry: "CreateAssociationBatchRequestEntry" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the failure.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the failure.
    fault: typing.Union[str, "Fault"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailureDetails(ShapeBase):
    """
    Information about an Automation failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failure_stage",
                "FailureStage",
                TypeInfo(str),
            ),
            (
                "failure_type",
                "FailureType",
                TypeInfo(str),
            ),
            (
                "details",
                "Details",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The stage of the Automation execution when the failure occurred. The stages
    # include the following: InputValidation, PreVerification, Invocation,
    # PostVerification.
    failure_stage: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of Automation failure. Failure types include the following:
    # Action, Permission, Throttling, Verification, Internal.
    failure_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information about the Automation step failure.
    details: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Fault(str):
    Client = "Client"
    Server = "Server"
    Unknown = "Unknown"


@dataclasses.dataclass
class FeatureNotAvailableException(ShapeBase):
    """
    You attempted to register a LAMBDA or STEP_FUNCTION task in a region where the
    corresponding service is not available.
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
class GetAutomationExecutionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for an existing automation execution to examine. The
    # execution ID is returned by StartAutomationExecution when the execution of
    # an Automation document is initiated.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAutomationExecutionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "automation_execution",
                "AutomationExecution",
                TypeInfo(AutomationExecution),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information about the current state of an automation execution.
    automation_execution: "AutomationExecution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCommandInvocationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "plugin_name",
                "PluginName",
                TypeInfo(str),
            ),
        ]

    # (Required) The parent command ID of the invocation plugin.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Required) The ID of the managed instance targeted by the command. A
    # managed instance can be an Amazon EC2 instance or an instance in your
    # hybrid environment that is configured for Systems Manager.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The name of the plugin for which you want detailed results. If
    # the document contains only one plugin, the name can be omitted and the
    # details will be returned.
    plugin_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCommandInvocationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "plugin_name",
                "PluginName",
                TypeInfo(str),
            ),
            (
                "response_code",
                "ResponseCode",
                TypeInfo(int),
            ),
            (
                "execution_start_date_time",
                "ExecutionStartDateTime",
                TypeInfo(str),
            ),
            (
                "execution_elapsed_time",
                "ExecutionElapsedTime",
                TypeInfo(str),
            ),
            (
                "execution_end_date_time",
                "ExecutionEndDateTime",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CommandInvocationStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
            ),
            (
                "standard_output_content",
                "StandardOutputContent",
                TypeInfo(str),
            ),
            (
                "standard_output_url",
                "StandardOutputUrl",
                TypeInfo(str),
            ),
            (
                "standard_error_content",
                "StandardErrorContent",
                TypeInfo(str),
            ),
            (
                "standard_error_url",
                "StandardErrorUrl",
                TypeInfo(str),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parent command ID of the invocation plugin.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the managed instance targeted by the command. A managed instance
    # can be an Amazon EC2 instance or an instance in your hybrid environment
    # that is configured for Systems Manager.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The comment text for the command.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the document that was executed. For example, AWS-
    # RunShellScript.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSM document version used in the request.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the plugin for which you want detailed results. For example,
    # aws:RunShellScript is a plugin.
    plugin_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error level response code for the plugin script. If the response code
    # is -1, then the command has not started executing on the instance, or it
    # was not received by the instance.
    response_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the plugin started executing. Date and time are written
    # in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7.
    # The following sample AWS CLI command uses the `InvokedBefore` filter.

    # `aws ssm list-commands --filters
    # key=InvokedBefore,value=2017-06-07T00:00:00Z`

    # If the plugin has not started to execute, the string is empty.
    execution_start_date_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Duration since ExecutionStartDateTime.
    execution_elapsed_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the plugin was finished executing. Date and time are
    # written in ISO 8601 format. For example, June 7, 2017 is represented as
    # 2017-06-7. The following sample AWS CLI command uses the `InvokedAfter`
    # filter.

    # `aws ssm list-commands --filters
    # key=InvokedAfter,value=2017-06-07T00:00:00Z`

    # If the plugin has not started to execute, the string is empty.
    execution_end_date_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of this invocation plugin. This status can be different than
    # StatusDetails.
    status: typing.Union[str, "CommandInvocationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A detailed status of the command execution for an invocation. StatusDetails
    # includes more information than Status because it includes states resulting
    # from error and concurrency control parameters. StatusDetails can show
    # different results than Status. For more information about these statuses,
    # see [Understanding Command Statuses](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/monitor-commands.html) in the _AWS Systems Manager
    # User Guide_. StatusDetails can be one of the following values:

    #   * Pending: The command has not been sent to the instance.

    #   * In Progress: The command has been sent to the instance but has not reached a terminal state.

    #   * Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, the instance was stopped, etc. The system will try to deliver the command again.

    #   * Success: The command or plugin was executed successfully. This is a terminal state.

    #   * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Execution Timed Out: The command started to execute on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Failed: The command wasn't executed successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.

    #   * Canceled: The command was terminated before it was completed. This is a terminal state.

    #   * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.

    #   * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first 24,000 characters written by the plugin to stdout. If the command
    # has not finished executing, if ExecutionStatus is neither Succeeded nor
    # Failed, then this string is empty.
    standard_output_content: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL for the complete text written by the plugin to stdout in Amazon S3.
    # If an Amazon S3 bucket was not specified, then this string is empty.
    standard_output_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first 8,000 characters written by the plugin to stderr. If the command
    # has not finished executing, then this string is empty.
    standard_error_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL for the complete text written by the plugin to stderr. If the
    # command has not finished executing, then this string is empty.
    standard_error_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # CloudWatch Logs information where Systems Manager sent the command output.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetConnectionStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
        ]

    # The ID of the instance.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectionStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ConnectionStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the instance to check connection status.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the connection to the instance. For example, 'Connected' or
    # 'Not Connected'.
    status: typing.Union[str, "ConnectionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDefaultPatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
        ]

    # Returns the default patch baseline for the specified operating system.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDefaultPatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the default patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system for the returned patch baseline.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeployablePatchSnapshotForInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
        ]

    # The ID of the instance for which the appropriate patch snapshot should be
    # retrieved.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined snapshot ID.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeployablePatchSnapshotForInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "snapshot_download_url",
                "SnapshotDownloadUrl",
                TypeInfo(str),
            ),
            (
                "product",
                "Product",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined snapshot ID.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pre-signed Amazon S3 URL that can be used to download the patch snapshot.
    snapshot_download_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the specific operating system (for example Windows Server 2012 or
    # Amazon Linux 2015.09) on the instance for the specified patch snapshot.
    product: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document version for which you want information.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the document in the specified format. The document format can be
    # either JSON or YAML. JSON is the default format.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDocumentResult(OutputShapeBase):
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
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
            (
                "document_type",
                "DocumentType",
                TypeInfo(typing.Union[str, DocumentType]),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the Systems Manager document.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The document type.
    document_type: typing.Union[str, "DocumentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document format, either JSON or YAML.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInventoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[InventoryFilter]),
            ),
            (
                "aggregators",
                "Aggregators",
                TypeInfo(typing.List[InventoryAggregator]),
            ),
            (
                "result_attributes",
                "ResultAttributes",
                TypeInfo(typing.List[ResultAttribute]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["InventoryFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns counts of inventory types based on one or more expressions. For
    # example, if you aggregate by using an expression that uses the
    # `AWS:InstanceInformation.PlatformType` type, you can see a count of how
    # many Windows and Linux instances exist in your inventoried fleet.
    aggregators: typing.List["InventoryAggregator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of inventory item types to return.
    result_attributes: typing.List["ResultAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInventoryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entities",
                "Entities",
                TypeInfo(typing.List[InventoryResultEntity]),
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

    # Collection of inventory entities such as a collection of instance
    # inventory.
    entities: typing.List["InventoryResultEntity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInventorySchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
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
            (
                "aggregator",
                "Aggregator",
                TypeInfo(bool),
            ),
            (
                "sub_type",
                "SubType",
                TypeInfo(bool),
            ),
        ]

    # The type of inventory item to return.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns inventory schemas that support aggregation. For example, this call
    # returns the `AWS:InstanceInformation` type, because it supports aggregation
    # based on the `PlatformName`, `PlatformType`, and `PlatformVersion`
    # attributes.
    aggregator: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the sub-type schema for a specified inventory type.
    sub_type: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInventorySchemaResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schemas",
                "Schemas",
                TypeInfo(typing.List[InventoryItemSchema]),
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

    # Inventory schemas returned by the request.
    schemas: typing.List["InventoryItemSchema"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution that includes the task.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_ids",
                "TaskIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MaintenanceWindowExecutionStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window execution.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the task executions from the Maintenance Window execution.
    task_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the Maintenance Window execution.
    status: typing.Union[str, "MaintenanceWindowExecutionStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The details explaining the Status. Only available for certain status
    # values.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the Maintenance Window started executing.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the Maintenance Window finished executing.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskInvocationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_id",
                "TaskId",
                TypeInfo(str),
            ),
            (
                "invocation_id",
                "InvocationId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution for which the task is a part.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specific task in the Maintenance Window task that should be
    # retrieved.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The invocation ID to retrieve.
    invocation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskInvocationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                TypeInfo(str),
            ),
            (
                "invocation_id",
                "InvocationId",
                TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MaintenanceWindowExecutionStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
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
                "owner_information",
                "OwnerInformation",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Maintenance Window execution ID.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task execution ID.
    task_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The invocation ID.
    invocation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution ID.
    execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Retrieves the task type for a Maintenance Window. Task types include the
    # following: LAMBDA, STEP_FUNCTION, AUTOMATION, RUN_COMMAND.
    task_type: typing.Union[str, "MaintenanceWindowTaskType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The parameters used at the time that the task executed.
    parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task status for an invocation.
    status: typing.Union[str, "MaintenanceWindowExecutionStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The details explaining the status. Details are only available for certain
    # status values.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the task started executing on the target.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time that the task finished executing on the target.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-provided value to be included in any CloudWatch events raised while
    # running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Maintenance Window target ID.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_id",
                "TaskId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution that includes the task.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specific task execution in the Maintenance Window task that
    # should be retrieved.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowExecutionTaskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                TypeInfo(str),
            ),
            (
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
            (
                "task_parameters",
                "TaskParameters",
                TypeInfo(
                    typing.List[typing.Dict[
                        str, MaintenanceWindowTaskParameterValueExpression]]
                ),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MaintenanceWindowExecutionStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window execution that includes the task.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specific task execution in the Maintenance Window task that
    # was retrieved.
    task_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the executed task.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role that was assumed when executing the task.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of task executed.
    type: typing.Union[str, "MaintenanceWindowTaskType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameters passed to the task when it was executed.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # The map has the following format:

    # Key: string, between 1 and 255 characters

    # Value: an array of strings, each string is between 1 and 255 characters
    task_parameters: typing.List[
        typing.Dict[str, "MaintenanceWindowTaskParameterValueExpression"]
    ] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The priority of the task.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The defined maximum number of task executions that could be run in
    # parallel.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The defined maximum number of task execution errors allowed before
    # scheduling of the task execution would have been stopped.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the task.
    status: typing.Union[str, "MaintenanceWindowExecutionStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The details explaining the Status. Only available for certain status
    # values.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the task execution started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the task execution completed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
        ]

    # The ID of the desired Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
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
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                TypeInfo(bool),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_date",
                "ModifiedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the created Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the Maintenance Window.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether targets must be registered with the Maintenance Window before tasks
    # can be defined for those targets.
    allow_unassociated_targets: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the Maintenance Windows is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the Maintenance Window was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the Maintenance Window was last modified.
    modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMaintenanceWindowTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
        ]

    # The Maintenance Window ID that includes the task to retrieve.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Maintenance Window task ID to retrieve.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMaintenanceWindowTaskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
            (
                "task_parameters",
                "TaskParameters",
                TypeInfo(
                    typing.
                    Dict[str, MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "logging_info",
                "LoggingInfo",
                TypeInfo(LoggingInfo),
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retrieved Maintenance Window ID.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The retrieved Maintenance Window task ID.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets where the task should execute.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource that the task used during execution. For RUN_COMMAND and
    # AUTOMATION task types, the TaskArn is the Systems Manager Document
    # name/ARN. For LAMBDA tasks, the value is the function name/ARN. For
    # STEP_FUNCTION tasks, the value is the state machine ARN.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM service role to assume during task execution.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of task to execute.
    task_type: typing.Union[str, "MaintenanceWindowTaskType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The parameters to pass to the task when it executes.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[str,
                                 "MaintenanceWindowTaskParameterValueExpression"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The parameters to pass to the task when it executes.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The priority of the task when it executes. The lower the number, the higher
    # the priority. Tasks that have the same priority are scheduled in parallel.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of targets allowed to run this task in parallel.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of errors allowed before the task stops being scheduled.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location in Amazon S3 where the task results are logged.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The retrieved task name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The retrieved task description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParameterHistoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "with_decryption",
                "WithDecryption",
                TypeInfo(bool),
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

    # The name of a parameter you want to query.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return decrypted values for secure string parameters. This flag is ignored
    # for String and StringList parameter types.
    with_decryption: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParameterHistoryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[ParameterHistory]),
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

    # A list of parameters returned by the request.
    parameters: typing.List["ParameterHistory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetParameterHistoryResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetParameterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "with_decryption",
                "WithDecryption",
                TypeInfo(bool),
            ),
        ]

    # The name of the parameter you want to query.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return decrypted values for secure string parameters. This flag is ignored
    # for String and StringList parameter types.
    with_decryption: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParameterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameter",
                "Parameter",
                TypeInfo(Parameter),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a parameter.
    parameter: "Parameter" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParametersByPathRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "recursive",
                "Recursive",
                TypeInfo(bool),
            ),
            (
                "parameter_filters",
                "ParameterFilters",
                TypeInfo(typing.List[ParameterStringFilter]),
            ),
            (
                "with_decryption",
                "WithDecryption",
                TypeInfo(bool),
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

    # The hierarchy for the parameter. Hierarchies start with a forward slash (/)
    # and end with the parameter name. A parameter name hierarchy can have a
    # maximum of 15 levels. Here is an example of a hierarchy:
    # `/Finance/Prod/IAD/WinServ2016/license33`
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Retrieve all parameters within a hierarchy.

    # If a user has access to a path, then the user can access all levels of that
    # path. For example, if a user has permission to access path /a, then the
    # user can also access /a/b. Even if a user has explicitly been denied access
    # in IAM for parameter /a, they can still call the GetParametersByPath API
    # action recursively and view /a/b.
    recursive: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters to limit the request results.

    # You can't filter using the parameter name.
    parameter_filters: typing.List["ParameterStringFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieve all parameters in a hierarchy with their value decrypted.
    with_decryption: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParametersByPathResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
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

    # A list of parameters found in the specified hierarchy.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetParametersByPathResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetParametersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "with_decryption",
                "WithDecryption",
                TypeInfo(bool),
            ),
        ]

    # Names of the parameters for which you want to query information.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return decrypted secure string value. Return decrypted values for secure
    # string parameters. This flag is ignored for String and StringList parameter
    # types.
    with_decryption: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetParametersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "invalid_parameters",
                "InvalidParameters",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of details for a parameter.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of parameters that are not formatted correctly or do not run when
    # executed.
    invalid_parameters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPatchBaselineForPatchGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
        ]

    # The name of the patch group whose patch baseline should be retrieved.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns he operating system rule specified for patch groups using the patch
    # baseline.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPatchBaselineForPatchGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline that should be used for the patch group.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch group.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system rule specified for patch groups using the patch
    # baseline.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to retrieve.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "global_filters",
                "GlobalFilters",
                TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                TypeInfo(typing.Union[str, PatchComplianceLevel]),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "patch_groups",
                "PatchGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_date",
                "ModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[PatchSource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the retrieved patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the operating system specified for the patch baseline.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly approved patches for the baseline.
    approved_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns the specified compliance severity level for approved patches in the
    # patch baseline.
    approved_patches_compliance_level: typing.Union[
        str, "PatchComplianceLevel"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.
    rejected_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Patch groups included in the patch baseline.
    patch_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the patch baseline was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the patch baseline was last modified.
    modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the patch baseline.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HierarchyLevelLimitExceededException(ShapeBase):
    """
    A hierarchy can have a maximum of 15 levels. For more information, see
    [Requirements and Constraints for Parameter
    Names](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    parameter-name-constraints.html) in the _AWS Systems Manager User Guide_.
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

    # A hierarchy can have a maximum of 15 levels. For more information, see
    # [Requirements and Constraints for Parameter
    # Names](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # parameter-name-constraints.html) in the _AWS Systems Manager User Guide_.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HierarchyTypeMismatchException(ShapeBase):
    """
    Parameter Store does not support changing a parameter type in a hierarchy. For
    example, you can't change a parameter from a String type to a SecureString type.
    You must create a new, unique parameter.
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

    # Parameter Store does not support changing a parameter type in a hierarchy.
    # For example, you can't change a parameter from a String type to a
    # SecureString type. You must create a new, unique parameter.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IdempotentParameterMismatch(ShapeBase):
    """
    Error returned when an idempotent operation is retried and the parameters don't
    match the original call to the API with the same idempotency token.
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
class InstanceAggregatedAssociationOverview(ShapeBase):
    """
    Status information about the aggregated associations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detailed_status",
                "DetailedStatus",
                TypeInfo(str),
            ),
            (
                "instance_association_status_aggregated_count",
                "InstanceAssociationStatusAggregatedCount",
                TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # Detailed status information about the aggregated associations.
    detailed_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of associations for the instance(s).
    instance_association_status_aggregated_count: typing.Dict[
        str, int] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class InstanceAssociation(ShapeBase):
    """
    One or more association documents on the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the association document for the instance(s).
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version information for the association on the instance.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceAssociationOutputLocation(ShapeBase):
    """
    An Amazon S3 bucket where you want to store the results of this request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_location",
                "S3Location",
                TypeInfo(S3OutputLocation),
            ),
        ]

    # An Amazon S3 bucket where you want to store the results of this request.
    s3_location: "S3OutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceAssociationOutputUrl(ShapeBase):
    """
    The URL of Amazon S3 bucket where you want to store the results of this request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_url",
                "S3OutputUrl",
                TypeInfo(S3OutputUrl),
            ),
        ]

    # The URL of Amazon S3 bucket where you want to store the results of this
    # request.
    s3_output_url: "S3OutputUrl" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceAssociationStatusInfo(ShapeBase):
    """
    Status information about the instance association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "execution_date",
                "ExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "detailed_status",
                "DetailedStatus",
                TypeInfo(str),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                TypeInfo(str),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "output_url",
                "OutputUrl",
                TypeInfo(InstanceAssociationOutputUrl),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
        ]

    # The association ID.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the association.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association document verions.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the association applied to the instance.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID where the association was created.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the instance association executed.
    execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Status information about the instance association.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed status information about the instance association.
    detailed_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Summary information about association execution.
    execution_summary: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An error code returned by the request to create the association.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL for an Amazon S3 bucket where you want to store the results of this
    # request.
    output_url: "InstanceAssociationOutputUrl" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the association applied to the instance.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceInformation(ShapeBase):
    """
    Describes a filter for a specific list of instances.
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
                "ping_status",
                "PingStatus",
                TypeInfo(typing.Union[str, PingStatus]),
            ),
            (
                "last_ping_date_time",
                "LastPingDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "agent_version",
                "AgentVersion",
                TypeInfo(str),
            ),
            (
                "is_latest_version",
                "IsLatestVersion",
                TypeInfo(bool),
            ),
            (
                "platform_type",
                "PlatformType",
                TypeInfo(typing.Union[str, PlatformType]),
            ),
            (
                "platform_name",
                "PlatformName",
                TypeInfo(str),
            ),
            (
                "platform_version",
                "PlatformVersion",
                TypeInfo(str),
            ),
            (
                "activation_id",
                "ActivationId",
                TypeInfo(str),
            ),
            (
                "iam_role",
                "IamRole",
                TypeInfo(str),
            ),
            (
                "registration_date",
                "RegistrationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IPAddress",
                TypeInfo(str),
            ),
            (
                "computer_name",
                "ComputerName",
                TypeInfo(str),
            ),
            (
                "association_status",
                "AssociationStatus",
                TypeInfo(str),
            ),
            (
                "last_association_execution_date",
                "LastAssociationExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_association_execution_date",
                "LastSuccessfulAssociationExecutionDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "association_overview",
                "AssociationOverview",
                TypeInfo(InstanceAggregatedAssociationOverview),
            ),
        ]

    # The instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Connection status of SSM Agent.
    ping_status: typing.Union[str, "PingStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when agent last pinged Systems Manager service.
    last_ping_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of SSM Agent running on your Linux instance.
    agent_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether latest version of SSM Agent is running on your instance.
    # Some older versions of Windows Server use the EC2Config service to process
    # SSM requests. For this reason, this field does not indicate whether or not
    # the latest version is installed on Windows managed instances.
    is_latest_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system platform type.
    platform_type: typing.Union[str, "PlatformType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the operating system platform running on your instance.
    platform_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the OS platform running on your instance.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The activation ID created by Systems Manager when the server or VM was
    # registered.
    activation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Identity and Access Management (IAM) role assigned to the on-
    # premises Systems Manager managed instances. This call does not return the
    # IAM role for Amazon EC2 instances.
    iam_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the server or VM was registered with AWS as a managed instance.
    registration_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of instance. Instances are either EC2 instances or managed
    # instances.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the managed instance.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address of the managed instance.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified host name of the managed instance.
    computer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the association.
    association_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the association was last executed.
    last_association_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last date the association was successfully run.
    last_successful_association_execution_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_overview: "InstanceAggregatedAssociationOverview" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceInformationFilter(ShapeBase):
    """
    Describes a filter for a specific list of instances. You can filter instances
    information by using tags. You specify tags by using a key-value mapping.

    Use this action instead of the
    DescribeInstanceInformationRequest$InstanceInformationFilterList method. The
    `InstanceInformationFilterList` method is a legacy method and does not support
    tags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(typing.Union[str, InstanceInformationFilterKey]),
            ),
            (
                "value_set",
                "valueSet",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    key: typing.Union[str, "InstanceInformationFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filter values.
    value_set: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceInformationFilterKey(str):
    InstanceIds = "InstanceIds"
    AgentVersion = "AgentVersion"
    PingStatus = "PingStatus"
    PlatformTypes = "PlatformTypes"
    ActivationIds = "ActivationIds"
    IamRole = "IamRole"
    ResourceType = "ResourceType"
    AssociationStatus = "AssociationStatus"


@dataclasses.dataclass
class InstanceInformationStringFilter(ShapeBase):
    """
    The filters to describe or get information about your managed instances.
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

    # The filter key name to describe your instances. For example:

    # "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"|"ResourceType"|"AssociationStatus"|"Tag
    # Key"
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter values.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstancePatchState(ShapeBase):
    """
    Defines the high-level patch compliance state for a managed instance, providing
    information about the number of installed, missing, not applicable, and failed
    patches along with metadata about the operation when this information was
    gathered for the instance.
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
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "operation_start_time",
                "OperationStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "operation_end_time",
                "OperationEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "operation",
                "Operation",
                TypeInfo(typing.Union[str, PatchOperationType]),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "owner_information",
                "OwnerInformation",
                TypeInfo(str),
            ),
            (
                "installed_count",
                "InstalledCount",
                TypeInfo(int),
            ),
            (
                "installed_other_count",
                "InstalledOtherCount",
                TypeInfo(int),
            ),
            (
                "missing_count",
                "MissingCount",
                TypeInfo(int),
            ),
            (
                "failed_count",
                "FailedCount",
                TypeInfo(int),
            ),
            (
                "not_applicable_count",
                "NotApplicableCount",
                TypeInfo(int),
            ),
        ]

    # The ID of the managed instance the high-level patch compliance information
    # was collected for.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch group the managed instance belongs to.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the patch baseline used to patch the instance.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the most recent patching operation was started on the instance.
    operation_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the most recent patching operation completed on the instance.
    operation_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of patching operation that was performed: SCAN (assess patch
    # compliance state) or INSTALL (install missing patches).
    operation: typing.Union[str, "PatchOperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline snapshot used during the patching operation
    # when this compliance data was collected.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder information. This field will always be empty in the current
    # release of the service.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of patches from the patch baseline that are installed on the
    # instance.
    installed_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of patches not specified in the patch baseline that are
    # installed on the instance.
    installed_other_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of patches from the patch baseline that are applicable for the
    # instance but aren't currently installed.
    missing_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of patches from the patch baseline that were attempted to be
    # installed during the last patching operation, but failed to install.
    failed_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of patches from the patch baseline that aren't applicable for
    # the instance and hence aren't installed on the instance.
    not_applicable_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstancePatchStateFilter(ShapeBase):
    """
    Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope
    down the information returned by the API.
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
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, InstancePatchStateOperatorType]),
            ),
        ]

    # The key for the filter. Supported values are FailedCount, InstalledCount,
    # InstalledOtherCount, MissingCount and NotApplicableCount.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the filter, must be an integer greater than or equal to 0.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of comparison that should be performed for the value: Equal,
    # NotEqual, LessThan or GreaterThan.
    type: typing.Union[str, "InstancePatchStateOperatorType"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )


class InstancePatchStateOperatorType(str):
    Equal = "Equal"
    NotEqual = "NotEqual"
    LessThan = "LessThan"
    GreaterThan = "GreaterThan"


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    An error occurred on the server side.
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
class InvalidActivation(ShapeBase):
    """
    The activation is not valid. The activation might have been deleted, or the
    ActivationId and the ActivationCode do not match.
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
class InvalidActivationId(ShapeBase):
    """
    The activation ID is not valid. Verify the you entered the correct ActivationId
    or ActivationCode and try again.
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
class InvalidAggregatorException(ShapeBase):
    """
    The specified aggregator is not valid for inventory groups. Verify that the
    aggregator uses a valid inventory type such as `AWS:Application` or
    `AWS:InstanceInformation`.
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
class InvalidAllowedPatternException(ShapeBase):
    """
    The request does not meet the regular expression requirement.
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

    # The request does not meet the regular expression requirement.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAssociation(ShapeBase):
    """
    The association is not valid or does not exist.
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
class InvalidAssociationVersion(ShapeBase):
    """
    The version you specified is not valid. Use ListAssociationVersions to view all
    versions of an association according to the association ID. Or, use the
    `$LATEST` parameter to view the latest version of the association.
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
class InvalidAutomationExecutionParametersException(ShapeBase):
    """
    The supplied parameters for invoking the specified Automation document are
    incorrect. For example, they may not match the set of parameters permitted for
    the specified Automation document.
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
class InvalidAutomationSignalException(ShapeBase):
    """
    The signal is not valid for the current Automation execution.
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
class InvalidAutomationStatusUpdateException(ShapeBase):
    """
    The specified update status operation is not valid.
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
class InvalidCommandId(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeleteInventoryParametersException(ShapeBase):
    """
    One or more of the parameters specified for the delete operation is not valid.
    Verify all parameters and try again.
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
class InvalidDeletionIdException(ShapeBase):
    """
    The ID specified for the delete operation does not exist or is not valide.
    Verify the ID and try again.
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
class InvalidDocument(ShapeBase):
    """
    The specified document does not exist.
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

    # The document does not exist or the document is not available to the user.
    # This exception can be issued by CreateAssociation, CreateAssociationBatch,
    # DeleteAssociation, DeleteDocument, DescribeAssociation, DescribeDocument,
    # GetDocument, SendCommand, or UpdateAssociationStatus.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocumentContent(ShapeBase):
    """
    The content for the document is not valid.
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

    # A description of the validation error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDocumentOperation(ShapeBase):
    """
    You attempted to delete a document while it is still shared. You must stop
    sharing the document before you can delete it.
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
class InvalidDocumentSchemaVersion(ShapeBase):
    """
    The version of the document schema is not supported.
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
class InvalidDocumentVersion(ShapeBase):
    """
    The document version is not valid or does not exist.
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
class InvalidFilter(ShapeBase):
    """
    The filter name is not valid. Verify the you entered the correct name and try
    again.
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
class InvalidFilterKey(ShapeBase):
    """
    The specified key is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFilterOption(ShapeBase):
    """
    The specified filter option is not valid. Valid options are Equals and
    BeginsWith. For Path filter, valid options are Recursive and OneLevel.
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

    # The specified filter option is not valid. Valid options are Equals and
    # BeginsWith. For Path filter, valid options are Recursive and OneLevel.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidFilterValue(ShapeBase):
    """
    The filter value is not valid. Verify the value and try again.
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
class InvalidInstanceId(ShapeBase):
    """
    The following problems can cause this exception:

    You do not have permission to access the instance.

    SSM Agent is not running. On managed instances and Linux instances, verify that
    the SSM Agent is running. On EC2 Windows instances, verify that the EC2Config
    service is running.

    SSM Agent or EC2Config service is not registered to the SSM endpoint. Try
    reinstalling SSM Agent or EC2Config service.

    The instance is not in valid state. Valid states are: Running, Pending, Stopped,
    Stopping. Invalid states are: Shutting-down and Terminated.
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
class InvalidInstanceInformationFilterValue(ShapeBase):
    """
    The specified filter value is not valid.
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


@dataclasses.dataclass
class InvalidInventoryGroupException(ShapeBase):
    """
    The specified inventory group is not valid.
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
class InvalidInventoryItemContextException(ShapeBase):
    """
    You specified invalid keys or values in the `Context` attribute for
    `InventoryItem`. Verify the keys and values, and try again.
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
class InvalidInventoryRequestException(ShapeBase):
    """
    The request is not valid.
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
class InvalidItemContentException(ShapeBase):
    """
    One or more content items is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidKeyId(ShapeBase):
    """
    The query key ID is not valid.
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


@dataclasses.dataclass
class InvalidNextToken(ShapeBase):
    """
    The specified token is not valid.
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
class InvalidNotificationConfig(ShapeBase):
    """
    One or more configuration items is not valid. Verify that a valid Amazon
    Resource Name (ARN) was provided for an Amazon SNS topic.
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
class InvalidOptionException(ShapeBase):
    """
    The delete inventory option specified is not valid. Verify the option and try
    again.
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
class InvalidOutputFolder(ShapeBase):
    """
    The S3 bucket does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOutputLocation(ShapeBase):
    """
    The output location is not valid or does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameters(ShapeBase):
    """
    You must specify values for all required parameters in the Systems Manager
    document. You can only supply values to parameters defined in the Systems
    Manager document.
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
class InvalidPermissionType(ShapeBase):
    """
    The permission type is not supported. _Share_ is the only supported permission
    type.
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
class InvalidPluginName(ShapeBase):
    """
    The plugin name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResourceId(ShapeBase):
    """
    The resource ID is not valid. Verify that you entered the correct ID and try
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResourceType(ShapeBase):
    """
    The resource type is not valid. For example, if you are attempting to tag an
    instance, the instance must be a registered, managed instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidResultAttributeException(ShapeBase):
    """
    The specified inventory item result attribute is not valid.
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
class InvalidRole(ShapeBase):
    """
    The role name can't contain invalid characters. Also verify that you specified
    an IAM role for notifications that includes the required trust policy. For
    information about configuring the IAM role for Run Command notifications, see
    [Configuring Amazon SNS Notifications for Run
    Command](http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-
    notifications.html) in the _AWS Systems Manager User Guide_.
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
class InvalidSchedule(ShapeBase):
    """
    The schedule is invalid. Verify your cron or rate expression and try again.
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
class InvalidTarget(ShapeBase):
    """
    The target is not valid or does not exist. It might not be configured for EC2
    Systems Manager or you might not have permission to perform the operation.
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
class InvalidTypeNameException(ShapeBase):
    """
    The parameter type name is not valid.
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
class InvalidUpdate(ShapeBase):
    """
    The update is not valid.
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
class InventoryAggregator(ShapeBase):
    """
    Specifies the inventory type and attribute for the aggregation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "expression",
                "Expression",
                TypeInfo(str),
            ),
            (
                "aggregators",
                "Aggregators",
                TypeInfo(typing.List[InventoryAggregator]),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[InventoryGroup]),
            ),
        ]

    # The inventory type and attribute name for aggregation.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Nested aggregators to further refine aggregation for an inventory type.
    aggregators: typing.List["InventoryAggregator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A user-defined set of one or more filters on which to aggregate inventory
    # data. Groups return a count of resources that match and don't match the
    # specified criteria.
    groups: typing.List["InventoryGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InventoryAttributeDataType(str):
    string = "string"
    number = "number"


class InventoryDeletionStatus(str):
    InProgress = "InProgress"
    Complete = "Complete"


@dataclasses.dataclass
class InventoryDeletionStatusItem(ShapeBase):
    """
    Status information returned by the `DeleteInventory` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deletion_id",
                "DeletionId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "deletion_start_time",
                "DeletionStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_status",
                "LastStatus",
                TypeInfo(typing.Union[str, InventoryDeletionStatus]),
            ),
            (
                "last_status_message",
                "LastStatusMessage",
                TypeInfo(str),
            ),
            (
                "deletion_summary",
                "DeletionSummary",
                TypeInfo(InventoryDeletionSummary),
            ),
            (
                "last_status_update_time",
                "LastStatusUpdateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The deletion ID returned by the `DeleteInventory` action.
    deletion_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the inventory data type.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC timestamp when the delete operation started.
    deletion_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the operation. Possible values are InProgress and Complete.
    last_status: typing.Union[str, "InventoryDeletionStatus"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # Information about the status.
    last_status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the delete operation. For more information about this
    # summary, see [Understanding the Delete Inventory
    # Summary](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/sysman-inventory-delete.html#sysman-inventory-
    # delete-summary) in the _AWS Systems Manager User Guide_.
    deletion_summary: "InventoryDeletionSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The UTC timestamp of when the last status report.
    last_status_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryDeletionSummary(ShapeBase):
    """
    Information about the delete operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
            (
                "remaining_count",
                "RemainingCount",
                TypeInfo(int),
            ),
            (
                "summary_items",
                "SummaryItems",
                TypeInfo(typing.List[InventoryDeletionSummaryItem]),
            ),
        ]

    # The total number of items to delete. This count does not change during the
    # delete operation.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Remaining number of items to delete.
    remaining_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of counts and versions for deleted items.
    summary_items: typing.List["InventoryDeletionSummaryItem"
                              ] = dataclasses.field(
                                  default=ShapeBase.NOT_SET,
                              )


@dataclasses.dataclass
class InventoryDeletionSummaryItem(ShapeBase):
    """
    Either a count, remaining count, or a version number in a delete inventory
    summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "remaining_count",
                "RemainingCount",
                TypeInfo(int),
            ),
        ]

    # The inventory type version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A count of the number of deleted items.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The remaining number of items to delete.
    remaining_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InventoryFilter(ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of results.
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
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, InventoryQueryOperatorType]),
            ),
        ]

    # The name of the filter key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Inventory filter values. Example: inventory filter where instance IDs are
    # specified as values Key=AWS:InstanceInformation.InstanceId,Values=
    # i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of filter. Valid values include the following:
    # "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"
    type: typing.Union[str, "InventoryQueryOperatorType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryGroup(ShapeBase):
    """
    A user-defined set of one or more filters on which to aggregate inventory data.
    Groups return a count of resources that match and don't match the specified
    criteria.
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
                "filters",
                "Filters",
                TypeInfo(typing.List[InventoryFilter]),
            ),
        ]

    # The name of the group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters define the criteria for the group. The `matchingCount` field
    # displays the number of resources that match the criteria. The
    # `notMatchingCount` field displays the number of resources that don't match
    # the criteria.
    filters: typing.List["InventoryFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryItem(ShapeBase):
    """
    Information collected from managed instances based on your inventory policy
    document
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "schema_version",
                "SchemaVersion",
                TypeInfo(str),
            ),
            (
                "capture_time",
                "CaptureTime",
                TypeInfo(str),
            ),
            (
                "content_hash",
                "ContentHash",
                TypeInfo(str),
            ),
            (
                "content",
                "Content",
                TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "context",
                "Context",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the inventory type. Default inventory item type names start
    # with AWS. Custom inventory type names will start with Custom. Default
    # inventory item types include the following: AWS:AWSComponent,
    # AWS:Application, AWS:InstanceInformation, AWS:Network, and
    # AWS:WindowsUpdate.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema version for the inventory item.
    schema_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the inventory information was collected.
    capture_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # MD5 hash of the inventory item type contents. The content hash is used to
    # determine whether to update inventory information. The PutInventory API
    # does not update the inventory item type contents if the MD5 hash has not
    # changed since last update.
    content_hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The inventory data of the inventory type.
    content: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of associated properties for a specified inventory type. For example,
    # with this attribute, you can specify the `ExecutionId`, `ExecutionType`,
    # `ComplianceType` properties of the `AWS:ComplianceItem` type.
    context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryItemAttribute(ShapeBase):
    """
    Attributes are the entries within the inventory item content. It contains name
    and value.
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
                "data_type",
                "DataType",
                TypeInfo(typing.Union[str, InventoryAttributeDataType]),
            ),
        ]

    # Name of the inventory item attribute.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data type of the inventory item attribute.
    data_type: typing.Union[str, "InventoryAttributeDataType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class InventoryItemSchema(ShapeBase):
    """
    The inventory item schema definition. Users can use this to compose inventory
    query filters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[InventoryItemAttribute]),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
        ]

    # The name of the inventory type. Default inventory item type names start
    # with AWS. Custom inventory type names will start with Custom. Default
    # inventory item types include the following: AWS:AWSComponent,
    # AWS:Application, AWS:InstanceInformation, AWS:Network, and
    # AWS:WindowsUpdate.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema attributes for inventory. This contains data type and attribute
    # name.
    attributes: typing.List["InventoryItemAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The schema version for the inventory item.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias name of the inventory type. The alias name is used for display
    # purposes.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InventoryQueryOperatorType(str):
    Equal = "Equal"
    NotEqual = "NotEqual"
    BeginWith = "BeginWith"
    LessThan = "LessThan"
    GreaterThan = "GreaterThan"
    Exists = "Exists"


@dataclasses.dataclass
class InventoryResultEntity(ShapeBase):
    """
    Inventory query results.
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
                "data",
                "Data",
                TypeInfo(typing.Dict[str, InventoryResultItem]),
            ),
        ]

    # ID of the inventory result entity. For example, for managed instance
    # inventory the result will be the managed instance ID. For EC2 instance
    # inventory, the result will be the instance ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data section in the inventory result entity JSON.
    data: typing.Dict[str, "InventoryResultItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryResultItem(ShapeBase):
    """
    The inventory result item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "schema_version",
                "SchemaVersion",
                TypeInfo(str),
            ),
            (
                "content",
                "Content",
                TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "capture_time",
                "CaptureTime",
                TypeInfo(str),
            ),
            (
                "content_hash",
                "ContentHash",
                TypeInfo(str),
            ),
        ]

    # The name of the inventory result item type.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema version for the inventory result item/
    schema_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains all the inventory data of the item type. Results include attribute
    # names and values.
    content: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time inventory item data was captured.
    capture_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # MD5 hash of the inventory item type contents. The content hash is used to
    # determine whether to update inventory information. The PutInventory API
    # does not update the inventory item type contents if the MD5 hash has not
    # changed since last update.
    content_hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InventorySchemaDeleteOption(str):
    DisableSchema = "DisableSchema"
    DeleteSchema = "DeleteSchema"


@dataclasses.dataclass
class InvocationDoesNotExist(ShapeBase):
    """
    The command ID and instance ID you specified did not match any invocations.
    Verify the command ID adn the instance ID and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ItemContentMismatchException(ShapeBase):
    """
    The inventory item has invalid content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ItemSizeLimitExceededException(ShapeBase):
    """
    The inventory item size has exceeded the size limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LabelParameterVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "parameter_version",
                "ParameterVersion",
                TypeInfo(int),
            ),
        ]

    # The parameter name on which you want to attach one or more labels.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more labels to attach to the specified parameter version.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific version of the parameter on which you want to attach one or
    # more labels. If no version is specified, the system attaches the label to
    # the latest version.)
    parameter_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LabelParameterVersionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "invalid_labels",
                "InvalidLabels",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The label does not meet the requirements. For information about parameter
    # label requirements, see [Labeling
    # Parameters](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/sysman-paramstore-labels.html) in the _AWS Systems
    # Manager User Guide_.
    invalid_labels: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LastResourceDataSyncStatus(str):
    Successful = "Successful"
    Failed = "Failed"
    InProgress = "InProgress"


@dataclasses.dataclass
class ListAssociationVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
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

    # The association ID for which you want to view all versions.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociationVersionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_versions",
                "AssociationVersions",
                TypeInfo(typing.List[AssociationVersionInfo]),
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

    # Information about all versions of the association for the specified
    # association ID.
    association_versions: typing.List["AssociationVersionInfo"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_filter_list",
                "AssociationFilterList",
                TypeInfo(typing.List[AssociationFilter]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    association_filter_list: typing.List["AssociationFilter"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssociationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associations",
                "Associations",
                TypeInfo(typing.List[Association]),
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

    # The associations.
    associations: typing.List["Association"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListAssociationsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListCommandInvocationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
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
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[CommandFilter]),
            ),
            (
                "details",
                "Details",
                TypeInfo(bool),
            ),
        ]

    # (Optional) The invocations for a specific command ID.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The command execution details for a specific instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The maximum number of items to return for this call. The call
    # also returns a token that you can specify in a subsequent call to get the
    # next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) One or more filters. Use a filter to return a more specific list
    # of results.
    filters: typing.List["CommandFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) If set this returns the response of the command executions and
    # any command output. By default this is set to False.
    details: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCommandInvocationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "command_invocations",
                "CommandInvocations",
                TypeInfo(typing.List[CommandInvocation]),
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

    # (Optional) A list of all invocations.
    command_invocations: typing.List["CommandInvocation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListCommandInvocationsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListCommandsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command_id",
                "CommandId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
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
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[CommandFilter]),
            ),
        ]

    # (Optional) If provided, lists only the specified command.
    command_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Lists commands issued against this instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The maximum number of items to return for this call. The call
    # also returns a token that you can specify in a subsequent call to get the
    # next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) One or more filters. Use a filter to return a more specific list
    # of results.
    filters: typing.List["CommandFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListCommandsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "commands",
                "Commands",
                TypeInfo(typing.List[Command]),
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

    # (Optional) The list of commands requested by the user.
    commands: typing.List["Command"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) The token for the next set of items to return. (You received
    # this token from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListCommandsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListComplianceItemsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[ComplianceStringFilter]),
            ),
            (
                "resource_ids",
                "ResourceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "resource_types",
                "ResourceTypes",
                TypeInfo(typing.List[str]),
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

    # One or more compliance filters. Use a filter to return a more specific list
    # of results.
    filters: typing.List["ComplianceStringFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID for the resources from which to get compliance information.
    # Currently, you can only specify one resource ID.
    resource_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of resource from which to get compliance information. Currently,
    # the only supported resource type is `ManagedInstance`.
    resource_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceItemsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compliance_items",
                "ComplianceItems",
                TypeInfo(typing.List[ComplianceItem]),
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

    # A list of compliance information for the specified resource ID.
    compliance_items: typing.List["ComplianceItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceSummariesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[ComplianceStringFilter]),
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

    # One or more compliance or inventory filters. Use a filter to return a more
    # specific list of results.
    filters: typing.List["ComplianceStringFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. Currently, you can
    # specify null or 50. The call also returns a token that you can specify in a
    # subsequent call to get the next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListComplianceSummariesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compliance_summary_items",
                "ComplianceSummaryItems",
                TypeInfo(typing.List[ComplianceSummaryItem]),
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

    # A list of compliant and non-compliant summary counts based on compliance
    # types. For example, this call returns State Manager associations, patches,
    # or custom compliance types according to the filter criteria that you
    # specified.
    compliance_summary_items: typing.List["ComplianceSummaryItem"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
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

    # The name of the document about which you want version information.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentVersionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_versions",
                "DocumentVersions",
                TypeInfo(typing.List[DocumentVersionInfo]),
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

    # The document versions.
    document_versions: typing.List["DocumentVersionInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_filter_list",
                "DocumentFilterList",
                TypeInfo(typing.List[DocumentFilter]),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[DocumentKeyValuesFilter]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    document_filter_list: typing.List["DocumentFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["DocumentKeyValuesFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDocumentsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_identifiers",
                "DocumentIdentifiers",
                TypeInfo(typing.List[DocumentIdentifier]),
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

    # The names of the Systems Manager documents.
    document_identifiers: typing.List["DocumentIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListDocumentsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInventoryEntriesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[InventoryFilter]),
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

    # The instance ID for which you want inventory information.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of inventory item for which you want information.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["InventoryFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInventoryEntriesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "schema_version",
                "SchemaVersion",
                TypeInfo(str),
            ),
            (
                "capture_time",
                "CaptureTime",
                TypeInfo(str),
            ),
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[typing.Dict[str, str]]),
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

    # The type of inventory item returned by the request.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID targeted by the request to query inventory information.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The inventory schema version used by the instance(s).
    schema_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that inventory information was collected for the instance(s).
    capture_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of inventory items on the instance(s).
    entries: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceComplianceSummariesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[ComplianceStringFilter]),
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

    # One or more filters. Use a filter to return a more specific list of
    # results.
    filters: typing.List["ComplianceStringFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceComplianceSummariesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_compliance_summary_items",
                "ResourceComplianceSummaryItems",
                TypeInfo(typing.List[ResourceComplianceSummaryItem]),
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

    # A summary count for specified or targeted managed instances. Summary count
    # includes information about compliant and non-compliant State Manager
    # associations, patch status, or custom items according to the filter
    # criteria that you specify.
    resource_compliance_summary_items: typing.List[
        "ResourceComplianceSummaryItem"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDataSyncRequest(ShapeBase):
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

    # A token to start the list. Use this token to get the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return for this call. The call also returns
    # a token that you can specify in a subsequent call to get the next set of
    # results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDataSyncResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_data_sync_items",
                "ResourceDataSyncItems",
                TypeInfo(typing.List[ResourceDataSyncItem]),
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

    # A list of your current Resource Data Sync configurations and their
    # statuses.
    resource_data_sync_items: typing.List["ResourceDataSyncItem"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The token for the next set of items to return. Use this token to get the
    # next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, ResourceTypeForTagging]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # Returns a list of tags for a specific resource type.
    resource_type: typing.Union[str, "ResourceTypeForTagging"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The resource ID for which you want to see a list of tags.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LoggingInfo(ShapeBase):
    """
    Information about an Amazon S3 bucket to write instance-level logs to.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_region",
                "S3Region",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
        ]

    # The name of an Amazon S3 bucket where execution logs are stored .
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region where the Amazon S3 bucket is located.
    s3_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The Amazon S3 bucket subfolder.
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowAutomationParameters(ShapeBase):
    """
    The parameters for an AUTOMATION task type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The version of an Automation document to use during task execution.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters for the AUTOMATION task.

    # For information about specifying and updating task parameters, see
    # RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # For AUTOMATION task types, Systems Manager ignores any values specified for
    # these parameters.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MaintenanceWindowExecution(ShapeBase):
    """
    Describes the information about an execution of a Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MaintenanceWindowExecutionStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
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
        ]

    # The ID of the Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Maintenance Window execution.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the execution.
    status: typing.Union[str, "MaintenanceWindowExecutionStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The details explaining the Status. Only available for certain status
    # values.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the execution started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the execution finished.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


class MaintenanceWindowExecutionStatus(str):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    SKIPPED_OVERLAPPING = "SKIPPED_OVERLAPPING"


@dataclasses.dataclass
class MaintenanceWindowExecutionTaskIdentity(ShapeBase):
    """
    Information about a task execution performed as part of a Maintenance Window
    execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MaintenanceWindowExecutionStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
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
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
        ]

    # The ID of the Maintenance Window execution that ran the task.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specific task execution in the Maintenance Window execution.
    task_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the task execution.
    status: typing.Union[str, "MaintenanceWindowExecutionStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The details explaining the status of the task execution. Only available for
    # certain status values.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the task execution started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the task execution finished.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the executed task.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of executed task.
    task_type: typing.Union[str, "MaintenanceWindowTaskType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class MaintenanceWindowExecutionTaskInvocationIdentity(ShapeBase):
    """
    Describes the information about a task invocation for a particular target as
    part of a task execution performed as part of a Maintenance Window execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_execution_id",
                "WindowExecutionId",
                TypeInfo(str),
            ),
            (
                "task_execution_id",
                "TaskExecutionId",
                TypeInfo(str),
            ),
            (
                "invocation_id",
                "InvocationId",
                TypeInfo(str),
            ),
            (
                "execution_id",
                "ExecutionId",
                TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, MaintenanceWindowExecutionStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
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
                "owner_information",
                "OwnerInformation",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window execution that ran the task.
    window_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the specific task execution in the Maintenance Window execution.
    task_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the task invocation.
    invocation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the action performed in the service that actually handled the
    # task invocation. If the task type is RUN_COMMAND, this value is the command
    # ID.
    execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task type.
    task_type: typing.Union[str, "MaintenanceWindowTaskType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The parameters that were provided for the invocation when it was executed.
    parameters: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the task invocation.
    status: typing.Union[str, "MaintenanceWindowExecutionStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The details explaining the status of the task invocation. Only available
    # for certain Status values.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the invocation started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the invocation finished.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-provided value that was specified when the target was registered with
    # the Maintenance Window. This was also included in any CloudWatch events
    # raised during the task invocation.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the target definition in this Maintenance Window the invocation
    # was performed for.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowFilter(ShapeBase):
    """
    Filter used in the request.
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

    # The name of the filter.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter values.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowIdentity(ShapeBase):
    """
    Information about the Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
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
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                TypeInfo(int),
            ),
        ]

    # The ID of the Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the Maintenance Window.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the Maintenance Window is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowLambdaParameters(ShapeBase):
    """
    The parameters for a LAMBDA task type.

    For information about specifying and updating task parameters, see
    RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    `TaskParameters` has been deprecated. To specify parameters to pass to a task
    when it runs, instead use the `Parameters` option in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    For Lambda tasks, Systems Manager ignores any values specified for
    TaskParameters and LoggingInfo.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_context",
                "ClientContext",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
            (
                "payload",
                "Payload",
                TypeInfo(typing.Any),
            ),
        ]

    # Pass client-specific information to the Lambda function that you are
    # invoking. You can then process the client information in your Lambda
    # function as you choose through the context variable.
    client_context: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specify a Lambda function version or alias name. If you specify
    # a function version, the action uses the qualified function ARN to invoke a
    # specific Lambda function. If you specify an alias name, the action uses the
    # alias ARN to invoke the Lambda function version to which the alias points.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JSON to provide to your Lambda function as input.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


class MaintenanceWindowLambdaPayload(botocore.response.StreamingBody):
    pass


class MaintenanceWindowResourceType(str):
    INSTANCE = "INSTANCE"


@dataclasses.dataclass
class MaintenanceWindowRunCommandParameters(ShapeBase):
    """
    The parameters for a RUN_COMMAND task type.

    For information about specifying and updating task parameters, see
    RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    `TaskParameters` has been deprecated. To specify parameters to pass to a task
    when it runs, instead use the `Parameters` option in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    For Run Command tasks, Systems Manager uses specified values for
    `TaskParameters` and `LoggingInfo` only if no values are specified for
    `TaskInvocationParameters`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "document_hash",
                "DocumentHash",
                TypeInfo(str),
            ),
            (
                "document_hash_type",
                "DocumentHashType",
                TypeInfo(typing.Union[str, DocumentHashType]),
            ),
            (
                "notification_config",
                "NotificationConfig",
                TypeInfo(NotificationConfig),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "timeout_seconds",
                "TimeoutSeconds",
                TypeInfo(int),
            ),
        ]

    # Information about the command(s) to execute.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SHA-256 or SHA-1 hash created by the system when the document was
    # created. SHA-1 hashes have been deprecated.
    document_hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
    document_hash_type: typing.Union[str, "DocumentHashType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Configurations for sending notifications about command status changes on a
    # per-instance basis.
    notification_config: "NotificationConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Amazon S3 bucket.
    output_s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 bucket subfolder.
    output_s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters for the RUN_COMMAND task execution.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM service role to assume during task execution.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this time is reached and the command has not already started executing,
    # it doesn not execute.
    timeout_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowStepFunctionsParameters(ShapeBase):
    """
    The parameters for a STEP_FUNCTION task.

    For information about specifying and updating task parameters, see
    RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask.

    `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    `TaskParameters` has been deprecated. To specify parameters to pass to a task
    when it runs, instead use the `Parameters` option in the
    `TaskInvocationParameters` structure. For information about how Systems Manager
    handles these options for the supported Maintenance Window task types, see
    MaintenanceWindowTaskInvocationParameters.

    For Step Functions tasks, Systems Manager ignores any values specified for
    `TaskParameters` and `LoggingInfo`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The inputs for the STEP_FUNCTION task.
    input: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the STEP_FUNCTION task.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowTarget(ShapeBase):
    """
    The target registered with the Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, MaintenanceWindowResourceType]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
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
        ]

    # The Maintenance Window ID where the target is registered.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the target.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of target.
    resource_type: typing.Union[str, "MaintenanceWindowResourceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The targets (either instances or tags). Instances are specified using
    # Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified
    # using Key=<tag name>,Values=<tag value>.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User-provided value that will be included in any CloudWatch events raised
    # while running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the target.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowTask(ShapeBase):
    """
    Information about a task defined for a Maintenance Window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
            (
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "task_parameters",
                "TaskParameters",
                TypeInfo(
                    typing.
                    Dict[str, MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "logging_info",
                "LoggingInfo",
                TypeInfo(LoggingInfo),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
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
        ]

    # The Maintenance Window ID where the task is registered.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task ID.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource that the task uses during execution. For RUN_COMMAND and
    # AUTOMATION task types, `TaskArn` is the Systems Manager document name or
    # ARN. For LAMBDA tasks, it's the function name or ARN. For STEP_FUNCTION
    # tasks, it's the state machine ARN.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of task. The type can be one of the following: RUN_COMMAND,
    # AUTOMATION, LAMBDA, or STEP_FUNCTION.
    type: typing.Union[str, "MaintenanceWindowTaskType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The targets (either instances or tags). Instances are specified using
    # Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified
    # using Key=<tag name>,Values=<tag value>.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameters that should be passed to the task when it is executed.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[str,
                                 "MaintenanceWindowTaskParameterValueExpression"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The priority of the task in the Maintenance Window. The lower the number,
    # the higher the priority. Tasks that have the same priority are scheduled in
    # parallel.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about an Amazon S3 bucket to write task-level logs to.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role that should be assumed when executing the task
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of targets this task can be run for in parallel.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of errors allowed before this task stops being
    # scheduled.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the task.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceWindowTaskInvocationParameters(ShapeBase):
    """
    The parameters for task execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "run_command",
                "RunCommand",
                TypeInfo(MaintenanceWindowRunCommandParameters),
            ),
            (
                "automation",
                "Automation",
                TypeInfo(MaintenanceWindowAutomationParameters),
            ),
            (
                "step_functions",
                "StepFunctions",
                TypeInfo(MaintenanceWindowStepFunctionsParameters),
            ),
            (
                "lambda_",
                "Lambda",
                TypeInfo(MaintenanceWindowLambdaParameters),
            ),
        ]

    # The parameters for a RUN_COMMAND task type.
    run_command: "MaintenanceWindowRunCommandParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameters for an AUTOMATION task type.
    automation: "MaintenanceWindowAutomationParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameters for a STEP_FUNCTION task type.
    step_functions: "MaintenanceWindowStepFunctionsParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameters for a LAMBDA task type.
    lambda_: "MaintenanceWindowLambdaParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MaintenanceWindowTaskParameterValueExpression(ShapeBase):
    """
    Defines the values for a task parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # This field contains an array of 0 or more strings, each 1 to 255 characters
    # in length.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class MaintenanceWindowTaskType(str):
    RUN_COMMAND = "RUN_COMMAND"
    AUTOMATION = "AUTOMATION"
    STEP_FUNCTIONS = "STEP_FUNCTIONS"
    LAMBDA = "LAMBDA"


@dataclasses.dataclass
class MaxDocumentSizeExceeded(ShapeBase):
    """
    The size limit of a document is 64 KB.
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
class ModifyDocumentPermissionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "permission_type",
                "PermissionType",
                TypeInfo(typing.Union[str, DocumentPermissionType]),
            ),
            (
                "account_ids_to_add",
                "AccountIdsToAdd",
                TypeInfo(typing.List[str]),
            ),
            (
                "account_ids_to_remove",
                "AccountIdsToRemove",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the document that you want to share.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The permission type for the document. The permission type can be _Share_.
    permission_type: typing.Union[str, "DocumentPermissionType"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # The AWS user accounts that should have access to the document. The account
    # IDs can either be a group of account IDs or _All_.
    account_ids_to_add: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS user accounts that should no longer have access to the document.
    # The AWS user account can either be a group of account IDs or _All_. This
    # action has a higher priority than _AccountIdsToAdd_. If you specify an
    # account ID to add and the same ID to remove, the system removes access to
    # the document.
    account_ids_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDocumentPermissionResponse(OutputShapeBase):
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
class NonCompliantSummary(ShapeBase):
    """
    A summary of resources that are not compliant. The summary is organized
    according to resource type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "non_compliant_count",
                "NonCompliantCount",
                TypeInfo(int),
            ),
            (
                "severity_summary",
                "SeveritySummary",
                TypeInfo(SeveritySummary),
            ),
        ]

    # The total number of compliance items that are not compliant.
    non_compliant_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of the non-compliance severity by compliance type
    severity_summary: "SeveritySummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotificationConfig(ShapeBase):
    """
    Configurations for sending notifications.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notification_arn",
                "NotificationArn",
                TypeInfo(str),
            ),
            (
                "notification_events",
                "NotificationEvents",
                TypeInfo(typing.List[typing.Union[str, NotificationEvent]]),
            ),
            (
                "notification_type",
                "NotificationType",
                TypeInfo(typing.Union[str, NotificationType]),
            ),
        ]

    # An Amazon Resource Name (ARN) for a Simple Notification Service (SNS)
    # topic. Run Command pushes notifications about command status changes to
    # this topic.
    notification_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The different events for which you can receive notifications. These events
    # include the following: All (events), InProgress, Success, TimedOut,
    # Cancelled, Failed. To learn more about these events, see [Configuring
    # Amazon SNS Notifications for Run
    # Command](http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-
    # sns-notifications.html) in the _AWS Systems Manager User Guide_.
    notification_events: typing.List[typing.Union[str, "NotificationEvent"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Command: Receive notification when the status of a command changes.
    # Invocation: For commands sent to multiple instances, receive notification
    # on a per-instance basis when the status of a command changes.
    notification_type: typing.Union[str, "NotificationType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


class NotificationEvent(str):
    All = "All"
    InProgress = "InProgress"
    Success = "Success"
    TimedOut = "TimedOut"
    Cancelled = "Cancelled"
    Failed = "Failed"


class NotificationType(str):
    Command = "Command"
    Invocation = "Invocation"


class OperatingSystem(str):
    WINDOWS = "WINDOWS"
    AMAZON_LINUX = "AMAZON_LINUX"
    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    UBUNTU = "UBUNTU"
    REDHAT_ENTERPRISE_LINUX = "REDHAT_ENTERPRISE_LINUX"
    SUSE = "SUSE"
    CENTOS = "CENTOS"


@dataclasses.dataclass
class OutputSource(ShapeBase):
    """
    Information about the source where the association execution details are stored.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_source_id",
                "OutputSourceId",
                TypeInfo(str),
            ),
            (
                "output_source_type",
                "OutputSourceType",
                TypeInfo(str),
            ),
        ]

    # The ID of the output source, for example the URL of an Amazon S3 bucket.
    output_source_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of source where the association execution details are stored, for
    # example, Amazon S3.
    output_source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Parameter(ShapeBase):
    """
    An Amazon EC2 Systems Manager parameter in Parameter Store.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, ParameterType]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "selector",
                "Selector",
                TypeInfo(str),
            ),
            (
                "source_result",
                "SourceResult",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of parameter. Valid values include the following: String, String
    # list, Secure string.
    type: typing.Union[str, "ParameterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter version.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either the version number or the label used to retrieve the parameter
    # value. Specify selectors by using one of the following formats:

    # parameter_name:version

    # parameter_name:label
    selector: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies to parameters that reference information in other AWS services.
    # SourceResult is the raw result or response from the source.
    source_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date the parameter was last changed or updated and the parameter version
    # was created.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the parameter.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterAlreadyExists(ShapeBase):
    """
    The parameter already exists. You can't create duplicate parameters.
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


@dataclasses.dataclass
class ParameterHistory(ShapeBase):
    """
    Information about parameter usage.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, ParameterType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_user",
                "LastModifiedUser",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of parameter used.
    type: typing.Union[str, "ParameterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the query key used for this parameter.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date the parameter was last changed or updated.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
    last_modified_user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Parameter names can include the following letters and symbols.

    # a-zA-Z0-9_.-
    allowed_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter version.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels assigned to the parameter version.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterLimitExceeded(ShapeBase):
    """
    You have exceeded the number of parameters for this AWS account. Delete one or
    more parameters and try again.
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


@dataclasses.dataclass
class ParameterMaxVersionLimitExceeded(ShapeBase):
    """
    The parameter exceeded the maximum number of allowed versions.
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


@dataclasses.dataclass
class ParameterMetadata(ShapeBase):
    """
    Metada includes information like the ARN of the last user and the date/time the
    parameter was last used.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, ParameterType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_user",
                "LastModifiedUser",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The parameter name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of parameter. Valid parameter types include the following: String,
    # String list, Secure string.
    type: typing.Union[str, "ParameterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the query key used for this parameter.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date the parameter was last changed or updated.
    last_modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
    last_modified_user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the parameter actions.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A parameter name can include only the following letters and symbols.

    # a-zA-Z0-9_.-
    allowed_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter version.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterNotFound(ShapeBase):
    """
    The parameter could not be found. Verify the name and try again.
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


@dataclasses.dataclass
class ParameterPatternMismatchException(ShapeBase):
    """
    The parameter name is not valid.
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

    # The parameter name is not valid.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterStringFilter(ShapeBase):
    """
    One or more filters. Use a filter to return a more specific list of results.

    The `Name` field can't be used with the GetParametersByPath API action.
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
                "option",
                "Option",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Valid options are Equals and BeginsWith. For Path filter, valid options are
    # Recursive and OneLevel.
    option: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value you want to search for.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ParameterType(str):
    String = "String"
    StringList = "StringList"
    SecureString = "SecureString"


@dataclasses.dataclass
class ParameterVersionLabelLimitExceeded(ShapeBase):
    """
    A parameter version can have a maximum of ten labels.
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


@dataclasses.dataclass
class ParameterVersionNotFound(ShapeBase):
    """
    The specified parameter version was not found. Verify the parameter name and
    version, and try again.
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


@dataclasses.dataclass
class ParametersFilter(ShapeBase):
    """
    This data type is deprecated. Instead, use ParameterStringFilter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, ParametersFilterKey]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter.
    key: typing.Union[str, "ParametersFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filter values.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ParametersFilterKey(str):
    Name = "Name"
    Type = "Type"
    KeyId = "KeyId"


@dataclasses.dataclass
class Patch(ShapeBase):
    """
    Represents metadata about a patch.
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
                "release_date",
                "ReleaseDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "content_url",
                "ContentUrl",
                TypeInfo(str),
            ),
            (
                "vendor",
                "Vendor",
                TypeInfo(str),
            ),
            (
                "product_family",
                "ProductFamily",
                TypeInfo(str),
            ),
            (
                "product",
                "Product",
                TypeInfo(str),
            ),
            (
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "msrc_severity",
                "MsrcSeverity",
                TypeInfo(str),
            ),
            (
                "kb_number",
                "KbNumber",
                TypeInfo(str),
            ),
            (
                "msrc_number",
                "MsrcNumber",
                TypeInfo(str),
            ),
            (
                "language",
                "Language",
                TypeInfo(str),
            ),
        ]

    # The ID of the patch (this is different than the Microsoft Knowledge Base
    # ID).
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the patch was released.
    release_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The title of the patch.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the patch.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL where more information can be obtained about the patch.
    content_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the vendor providing the patch.
    vendor: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product family the patch is applicable for (for example, Windows).
    product_family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific product the patch is applicable for (for example,
    # WindowsServer2016).
    product: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The classification of the patch (for example, SecurityUpdates, Updates,
    # CriticalUpdates).
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The severity of the patch (for example Critical, Important, Moderate).
    msrc_severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Microsoft Knowledge Base ID of the patch.
    kb_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the MSRC bulletin the patch is related to.
    msrc_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language of the patch if it's language-specific.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchBaselineIdentity(ShapeBase):
    """
    Defines the basic information about a patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "baseline_name",
                "BaselineName",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "baseline_description",
                "BaselineDescription",
                TypeInfo(str),
            ),
            (
                "default_baseline",
                "DefaultBaseline",
                TypeInfo(bool),
            ),
        ]

    # The ID of the patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    baseline_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines the operating system the patch baseline applies to. The Default
    # value is WINDOWS.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the patch baseline.
    baseline_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether this is the default baseline. Note that Systems Manager supports
    # creating multiple default patch baselines. For example, you can create a
    # default patch baseline for each operating system.
    default_baseline: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchComplianceData(ShapeBase):
    """
    Information about the state of a patch on a particular instance as it relates to
    the patch baseline used to patch the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "kb_id",
                "KBId",
                TypeInfo(str),
            ),
            (
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, PatchComplianceDataState]),
            ),
            (
                "installed_time",
                "InstalledTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The title of the patch.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system-specific ID of the patch.
    kb_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The classification of the patch (for example, SecurityUpdates, Updates,
    # CriticalUpdates).
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The severity of the patch (for example, Critical, Important, Moderate).
    severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the patch on the instance (INSTALLED, INSTALLED_OTHER,
    # MISSING, NOT_APPLICABLE or FAILED).
    state: typing.Union[str, "PatchComplianceDataState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date/time the patch was installed on the instance. Note that not all
    # operating systems provide this level of information.
    installed_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PatchComplianceDataState(str):
    INSTALLED = "INSTALLED"
    INSTALLED_OTHER = "INSTALLED_OTHER"
    MISSING = "MISSING"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    FAILED = "FAILED"


class PatchComplianceLevel(str):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNSPECIFIED = "UNSPECIFIED"


class PatchDeploymentStatus(str):
    APPROVED = "APPROVED"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    EXPLICIT_APPROVED = "EXPLICIT_APPROVED"
    EXPLICIT_REJECTED = "EXPLICIT_REJECTED"


@dataclasses.dataclass
class PatchFilter(ShapeBase):
    """
    Defines a patch filter.

    A patch filter consists of key/value pairs, but not all keys are valid for all
    operating system types. For example, the key `PRODUCT` is valid for all
    supported operating system types. The key `MSRC_SEVERITY`, however, is valid
    only for Windows operating systems, and the key `SECTION` is valid only for
    Ubuntu operating systems.

    Refer to the following sections for information about which keys may be used
    with each major operating system, and which values are valid for each key.

    **Windows Operating Systems**

    The supported keys for Windows operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `MSRC_SEVERITY`. See the following lists for valid values
    for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `Windows7`

      * `Windows8`

      * `Windows8.1`

      * `Windows8Embedded`

      * `Windows10`

      * `Windows10LTSB`

      * `WindowsServer2008`

      * `WindowsServer2008R2`

      * `WindowsServer2012`

      * `WindowsServer2012R2`

      * `WindowsServer2016`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `CriticalUpdates`

      * `DefinitionUpdates`

      * `Drivers`

      * `FeaturePacks`

      * `SecurityUpdates`

      * `ServicePacks`

      * `Tools`

      * `UpdateRollups`

      * `Updates`

      * `Upgrades`

    _Supported key:_ `MSRC_SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Moderate`

      * `Low`

      * `Unspecified`

    **Ubuntu Operating Systems**

    The supported keys for Ubuntu operating systems are `PRODUCT`, `PRIORITY`, and
    `SECTION`. See the following lists for valid values for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `Ubuntu14.04`

      * `Ubuntu16.04`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `PRIORITY`

    _Supported values:_

      * `Required`

      * `Important`

      * `Standard`

      * `Optional`

      * `Extra`

    _Supported key:_ `SECTION`

    Only the length of the key value is validated. Minimum length is 1. Maximum
    length is 64.

    **Amazon Linux Operating Systems**

    The supported keys for Amazon Linux operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `SEVERITY`. See the following lists for valid values for
    each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `AmazonLinux2012.03`

      * `AmazonLinux2012.09`

      * `AmazonLinux2013.03`

      * `AmazonLinux2013.09`

      * `AmazonLinux2014.03`

      * `AmazonLinux2014.09`

      * `AmazonLinux2015.03`

      * `AmazonLinux2015.09`

      * `AmazonLinux2016.03`

      * `AmazonLinux2016.09`

      * `AmazonLinux2017.03`

      * `AmazonLinux2017.09`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`

    **Amazon Linux 2 Operating Systems**

    The supported keys for Amazon Linux 2 operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `SEVERITY`. See the following lists for valid values for
    each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `AmazonLinux2`

      * `AmazonLinux2.0`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`

    **RedHat Enterprise Linux (RHEL) Operating Systems**

    The supported keys for RedHat Enterprise Linux operating systems are `PRODUCT`,
    `CLASSIFICATION`, and `SEVERITY`. See the following lists for valid values for
    each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `RedhatEnterpriseLinux6.5`

      * `RedhatEnterpriseLinux6.6`

      * `RedhatEnterpriseLinux6.7`

      * `RedhatEnterpriseLinux6.8`

      * `RedhatEnterpriseLinux6.9`

      * `RedhatEnterpriseLinux7.0`

      * `RedhatEnterpriseLinux7.1`

      * `RedhatEnterpriseLinux7.2`

      * `RedhatEnterpriseLinux7.3`

      * `RedhatEnterpriseLinux7.4`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`

    **SUSE Linux Enterprise Server (SLES) Operating Systems**

    The supported keys for SLES operating systems are `PRODUCT`, `CLASSIFICATION`,
    and `SEVERITY`. See the following lists for valid values for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `Suse12.0`

      * `Suse12.1`

      * `Suse12.2`

      * `Suse12.3`

      * `Suse12.4`

      * `Suse12.5`

      * `Suse12.6`

      * `Suse12.7`

      * `Suse12.8`

      * `Suse12.9`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Recommended`

      * `Optional`

      * `Feature`

      * `Document`

      * `Yast`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Moderate`

      * `Low`

    **CentOS Operating Systems**

    The supported keys for CentOS operating systems are `PRODUCT`, `CLASSIFICATION`,
    and `SEVERITY`. See the following lists for valid values for each of these keys.

    _Supported key:_ `PRODUCT`

    _Supported values:_

      * `CentOS6.5`

      * `CentOS6.6`

      * `CentOS6.7`

      * `CentOS6.8`

      * `CentOS6.9`

      * `CentOS7.0`

      * `CentOS7.1`

      * `CentOS7.2`

      * `CentOS7.3`

      * `CentOS7.4`

      * `*`

    _Use a wildcard character (*) to target all supported operating system
    versions._

    _Supported key:_ `CLASSIFICATION`

    _Supported values:_

      * `Security`

      * `Bugfix`

      * `Enhancement`

      * `Recommended`

      * `Newpackage`

    _Supported key:_ `SEVERITY`

    _Supported values:_

      * `Critical`

      * `Important`

      * `Medium`

      * `Low`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, PatchFilterKey]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The key for the filter.

    # See PatchFilter for lists of valid keys for each operating system type.
    key: typing.Union[str, "PatchFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value for the filter key.

    # See PatchFilter for lists of valid values for each key based on operating
    # system type.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchFilterGroup(ShapeBase):
    """
    A set of patch filters, typically used for approval rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_filters",
                "PatchFilters",
                TypeInfo(typing.List[PatchFilter]),
            ),
        ]

    # The set of patch filters that make up the group.
    patch_filters: typing.List["PatchFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PatchFilterKey(str):
    PRODUCT = "PRODUCT"
    CLASSIFICATION = "CLASSIFICATION"
    MSRC_SEVERITY = "MSRC_SEVERITY"
    PATCH_ID = "PATCH_ID"
    SECTION = "SECTION"
    PRIORITY = "PRIORITY"
    SEVERITY = "SEVERITY"


@dataclasses.dataclass
class PatchGroupPatchBaselineMapping(ShapeBase):
    """
    The mapping between a patch group and the patch baseline the patch group is
    registered with.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
            (
                "baseline_identity",
                "BaselineIdentity",
                TypeInfo(PatchBaselineIdentity),
            ),
        ]

    # The name of the patch group registered with the patch baseline.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The patch baseline the patch group is registered with.
    baseline_identity: "PatchBaselineIdentity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PatchOperationType(str):
    Scan = "Scan"
    Install = "Install"


@dataclasses.dataclass
class PatchOrchestratorFilter(ShapeBase):
    """
    Defines a filter used in Patch Manager APIs.
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

    # The key for the filter.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the filter.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchRule(ShapeBase):
    """
    Defines an approval rule for a patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_filter_group",
                "PatchFilterGroup",
                TypeInfo(PatchFilterGroup),
            ),
            (
                "approve_after_days",
                "ApproveAfterDays",
                TypeInfo(int),
            ),
            (
                "compliance_level",
                "ComplianceLevel",
                TypeInfo(typing.Union[str, PatchComplianceLevel]),
            ),
            (
                "enable_non_security",
                "EnableNonSecurity",
                TypeInfo(bool),
            ),
        ]

    # The patch filter group that defines the criteria for the rule.
    patch_filter_group: "PatchFilterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days after the release date of each patch matched by the rule
    # that the patch is marked as approved in the patch baseline. For example, a
    # value of `7` means that patches are approved seven days after they are
    # released.
    approve_after_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A compliance severity level for all approved patches in a patch baseline.
    # Valid compliance severity levels include the following: Unspecified,
    # Critical, High, Medium, Low, and Informational.
    compliance_level: typing.Union[str, "PatchComplianceLevel"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # For instances identified by the approval rule filters, enables a patch
    # baseline to apply non-security updates available in the specified
    # repository. The default value is 'false'. Applies to Linux instances only.
    enable_non_security: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchRuleGroup(ShapeBase):
    """
    A set of rules defining the approval rules for a patch baseline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "patch_rules",
                "PatchRules",
                TypeInfo(typing.List[PatchRule]),
            ),
        ]

    # The rules that make up the rule group.
    patch_rules: typing.List["PatchRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PatchSource(ShapeBase):
    """
    Information about the patches to use to update the instances, including target
    operating systems and source repository. Applies to Linux instances only.
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
                "products",
                "Products",
                TypeInfo(typing.List[str]),
            ),
            (
                "configuration",
                "Configuration",
                TypeInfo(str),
            ),
        ]

    # The name specified to identify the patch source.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific operating system versions a patch repository applies to, such
    # as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or
    # "Suse12.7". For lists of supported product values, see PatchFilter.
    products: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the yum repo configuration. For example:

    # `cachedir=/var/cache/yum/$basesearch`

    # `$releasever`

    # `keepcache=0`

    # `debuglevel=2`
    configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PatchStatus(ShapeBase):
    """
    Information about the approval status of a patch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_status",
                "DeploymentStatus",
                TypeInfo(typing.Union[str, PatchDeploymentStatus]),
            ),
            (
                "compliance_level",
                "ComplianceLevel",
                TypeInfo(typing.Union[str, PatchComplianceLevel]),
            ),
            (
                "approval_date",
                "ApprovalDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The approval status of a patch (APPROVED, PENDING_APPROVAL,
    # EXPLICIT_APPROVED, EXPLICIT_REJECTED).
    deployment_status: typing.Union[str, "PatchDeploymentStatus"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The compliance severity level for a patch.
    compliance_level: typing.Union[str, "PatchComplianceLevel"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The date the patch was approved (or will be approved if the status is
    # PENDING_APPROVAL).
    approval_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PingStatus(str):
    Online = "Online"
    ConnectionLost = "ConnectionLost"
    Inactive = "Inactive"


class PlatformType(str):
    Windows = "Windows"
    Linux = "Linux"


@dataclasses.dataclass
class PutComplianceItemsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "compliance_type",
                "ComplianceType",
                TypeInfo(str),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                TypeInfo(ComplianceExecutionSummary),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[ComplianceItemEntry]),
            ),
            (
                "item_content_hash",
                "ItemContentHash",
                TypeInfo(str),
            ),
        ]

    # Specify an ID for this resource. For a managed instance, this is the
    # instance ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the type of resource. `ManagedInstance` is currently the only
    # supported resource type.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the compliance type. For example, specify Association (for a State
    # Manager association), Patch, or Custom:`string`.
    compliance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of the call execution that includes an execution ID, the type of
    # execution (for example, `Command`), and the date/time of the execution
    # using a datetime object that is saved in the following format: yyyy-MM-
    # dd'T'HH:mm:ss'Z'.
    execution_summary: "ComplianceExecutionSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the compliance as defined by the resource type. For
    # example, for a patch compliance type, `Items` includes information about
    # the PatchSeverity, Classification, etc.
    items: typing.List["ComplianceItemEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # MD5 or SHA-256 content hash. The content hash is used to determine if
    # existing information should be overwritten or ignored. If the content
    # hashes match, the request to put compliance information is ignored.
    item_content_hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutComplianceItemsResult(OutputShapeBase):
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
class PutInventoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[InventoryItem]),
            ),
        ]

    # One or more instance IDs where you want to add or update inventory items.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The inventory items that you want to add or update on instances.
    items: typing.List["InventoryItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutInventoryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the request.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutParameterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ParameterType]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "overwrite",
                "Overwrite",
                TypeInfo(bool),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                TypeInfo(str),
            ),
        ]

    # The fully qualified name of the parameter that you want to add to the
    # system. The fully qualified name includes the complete hierarchy of the
    # parameter path and name. For example: `/Dev/DBServer/MySQL/db-string13`

    # Naming Constraints:

    #   * Parameter names are case sensitive.

    #   * A parameter name must be unique within an AWS Region

    #   * A parameter name can't be prefixed with "aws" or "ssm" (case-insensitive).

    #   * Parameter names can include only the following symbols and letters: `a-zA-Z0-9_.-/`

    #   * A parameter name can't include spaces.

    #   * Parameter hierarchies are limited to a maximum depth of fifteen levels.

    # For additional information about valid values for parameter names, see
    # [Requirements and Constraints for Parameter
    # Names](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # parameter-name-constraints.html) in the _AWS Systems Manager User Guide_.

    # The maximum length constraint listed below includes capacity for additional
    # system attributes that are not part of the name. The maximum length for the
    # fully qualified parameter name is 1011 characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter value that you want to add to the system.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of parameter that you want to add to the system.

    # Items in a `StringList` must be separated by a comma (,). You can't use
    # other punctuation or special character to escape items in the list. If you
    # have a parameter value that requires a comma, then use the `String` data
    # type.

    # `SecureString` is not currently supported for AWS CloudFormation templates
    # or in the China Regions.
    type: typing.Union[str, "ParameterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the parameter that you want to add to the system.
    # Optional but recommended.

    # Do not enter personally identifiable information in this field.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The KMS Key ID that you want to use to encrypt a parameter. Either the
    # default AWS Key Management Service (AWS KMS) key automatically assigned to
    # your AWS account or a custom key. Required for parameters that use the
    # `SecureString` data type.

    # If you don't specify a key ID, the system uses the default key associated
    # with your AWS account.

    #   * To use your default AWS KMS key, choose the `SecureString` data type, and do _not_ specify the `Key ID` when you create the parameter. The system automatically populates `Key ID` with your default KMS key.

    #   * To use a custom KMS key, choose the `SecureString` data type with the `Key ID` parameter.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Overwrite an existing parameter. If not specified, will default to "false".
    overwrite: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A regular expression used to validate the parameter value. For example, for
    # String types with values restricted to numbers, you can specify the
    # following: AllowedPattern=^\d+$
    allowed_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutParameterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new version number of a parameter. If you edit a parameter value,
    # Parameter Store automatically creates a new version and assigns this new
    # version a unique ID. You can reference a parameter version ID in API
    # actions or in Systems Manager documents (SSM documents). By default, if you
    # don't specify a specific version, the system returns the latest parameter
    # value when a parameter is called.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterDefaultPatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline that should be the default patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterDefaultPatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the default patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterPatchBaselineForPatchGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
        ]

    # The ID of the patch baseline to register the patch group with.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch group that should be registered with the patch
    # baseline.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterPatchBaselineForPatchGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "patch_group",
                "PatchGroup",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the patch baseline the patch group was registered with.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch group registered with the patch baseline.
    patch_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTargetWithMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, MaintenanceWindowResourceType]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
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
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window the target should be registered with.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of target being registered with the Maintenance Window.
    resource_type: typing.Union[str, "MaintenanceWindowResourceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The targets (either instances or tags).

    # Specify instances using the following format:

    # `Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>`

    # Specify tags using either of the following formats:

    # `Key=tag:<tag-key>,Values=<tag-value-1>,<tag-value-2>`

    # `Key=tag-key,Values=<tag-key-1>,<tag-key-2>`
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User-provided value that will be included in any CloudWatch events raised
    # while running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional name for the target.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description for the target.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTargetWithMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the target definition in this Maintenance Window.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTaskWithMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "task_type",
                "TaskType",
                TypeInfo(typing.Union[str, MaintenanceWindowTaskType]),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "task_parameters",
                "TaskParameters",
                TypeInfo(
                    typing.
                    Dict[str, MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "logging_info",
                "LoggingInfo",
                TypeInfo(LoggingInfo),
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
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the Maintenance Window the task should be added to.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets (either instances or Maintenance Window targets).

    # Specify instances using the following format:

    # `Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>`

    # Specify Maintenance Window targets using the following format:

    # `Key=<WindowTargetIds>,Values=<window-target-id-1>,<window-target-id-2>`
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the task to execute
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of task being registered.
    task_type: typing.Union[str, "MaintenanceWindowTaskType"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # The maximum number of targets this task can be run for in parallel.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of errors allowed before this task stops being
    # scheduled.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role to assume when running the Maintenance Window task.

    # If you do not specify a service role ARN, Systems Manager will use your
    # account's service-linked role for Systems Manager by default. If no
    # service-linked role for Systems Manager exists in your account, it will be
    # created when you run `RegisterTaskWithMaintenanceWindow` without specifying
    # a service role ARN.

    # For more information, see [Service-Linked Role Permissions for Systems
    # Manager](http://docs.aws.amazon.com/systems-manager/latest/userguide/using-
    # service-linked-roles.html#slr-permissions) and [Should I Use a Service-
    # Linked Role or a Custom Service Role to Run Maintenance Window Tasks?
    # ](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # maintenance-permissions.html#maintenance-window-tasks-service-role) in the
    # _AWS Systems Manager User Guide_.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters that should be passed to the task when it is executed.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[str,
                                 "MaintenanceWindowTaskParameterValueExpression"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The parameters that the task should use during execution. Populate only the
    # fields that match the task type. All other fields should be empty.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The priority of the task in the Maintenance Window, the lower the number
    # the higher the priority. Tasks in a Maintenance Window are scheduled in
    # priority order with tasks that have the same priority scheduled in
    # parallel.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure containing information about an Amazon S3 bucket to write
    # instance-level logs to.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional name for the task.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description for the task.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-provided idempotency token.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTaskWithMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The id of the task in the Maintenance Window.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, ResourceTypeForTagging]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The type of resource of which you want to remove a tag.

    # The ManagedInstance type for this API action is only for on-premises
    # managed instances. You must specify the the name of the managed instance in
    # the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_type: typing.Union[str, "ResourceTypeForTagging"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The resource ID for which you want to remove tags. Use the ID of the
    # resource. Here are some examples:

    # ManagedInstance: mi-012345abcde

    # MaintenanceWindow: mw-012345abcde

    # PatchBaseline: pb-012345abcde

    # For the Document and Parameter values, use the name of the resource.

    # The ManagedInstance type for this API action is only for on-premises
    # managed instances. You must specify the the name of the managed instance in
    # the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Tag keys that you want to remove from the specified resource.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceResult(OutputShapeBase):
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
class ResolvedTargets(ShapeBase):
    """
    Information about targets that resolved during the Automation execution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_values",
                "ParameterValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "truncated",
                "Truncated",
                TypeInfo(bool),
            ),
        ]

    # A list of parameter values sent to targets that resolved during the
    # Automation execution.
    parameter_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A boolean value indicating whether the resolved target list is truncated.
    truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceComplianceSummaryItem(ShapeBase):
    """
    Compliance summary information for a specific resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compliance_type",
                "ComplianceType",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ComplianceStatus]),
            ),
            (
                "overall_severity",
                "OverallSeverity",
                TypeInfo(typing.Union[str, ComplianceSeverity]),
            ),
            (
                "execution_summary",
                "ExecutionSummary",
                TypeInfo(ComplianceExecutionSummary),
            ),
            (
                "compliant_summary",
                "CompliantSummary",
                TypeInfo(CompliantSummary),
            ),
            (
                "non_compliant_summary",
                "NonCompliantSummary",
                TypeInfo(NonCompliantSummary),
            ),
        ]

    # The compliance type.
    compliance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource type.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource ID.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compliance status for the resource.
    status: typing.Union[str, "ComplianceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The highest severity item found for the resource. The resource is compliant
    # for this item.
    overall_severity: typing.Union[str, "ComplianceSeverity"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Information about the execution.
    execution_summary: "ComplianceExecutionSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of items that are compliant for the resource.
    compliant_summary: "CompliantSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of items that aren't compliant for the resource.
    non_compliant_summary: "NonCompliantSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceDataSyncAlreadyExistsException(ShapeBase):
    """
    A sync configuration with the same name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                TypeInfo(str),
            ),
        ]

    sync_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataSyncCountExceededException(ShapeBase):
    """
    You have exceeded the allowed maximum sync configurations.
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
class ResourceDataSyncInvalidConfigurationException(ShapeBase):
    """
    The specified sync configuration is invalid.
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
class ResourceDataSyncItem(ShapeBase):
    """
    Information about a Resource Data Sync configuration, including its current
    status and last successful sync.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                TypeInfo(str),
            ),
            (
                "s3_destination",
                "S3Destination",
                TypeInfo(ResourceDataSyncS3Destination),
            ),
            (
                "last_sync_time",
                "LastSyncTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_successful_sync_time",
                "LastSuccessfulSyncTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_status",
                "LastStatus",
                TypeInfo(typing.Union[str, LastResourceDataSyncStatus]),
            ),
            (
                "sync_created_time",
                "SyncCreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_sync_status_message",
                "LastSyncStatusMessage",
                TypeInfo(str),
            ),
        ]

    # The name of the Resource Data Sync.
    sync_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configuration information for the target Amazon S3 bucket.
    s3_destination: "ResourceDataSyncS3Destination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the configuration attempted to sync (UTC).
    last_sync_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the sync operations returned a status of `SUCCESSFUL` (UTC).
    last_successful_sync_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status reported by the last sync.
    last_status: typing.Union[str, "LastResourceDataSyncStatus"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The date and time the configuration was created (UTC).
    sync_created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status message details reported by the last sync.
    last_sync_status_message: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceDataSyncNotFoundException(ShapeBase):
    """
    The specified sync name was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sync_name",
                "SyncName",
                TypeInfo(str),
            ),
        ]

    sync_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataSyncS3Destination(ShapeBase):
    """
    Information about the target Amazon S3 bucket for the Resource Data Sync.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "sync_format",
                "SyncFormat",
                TypeInfo(typing.Union[str, ResourceDataSyncS3Format]),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "awskms_key_arn",
                "AWSKMSKeyARN",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon S3 bucket where the aggregated data is stored.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A supported sync format. The following format is currently supported:
    # JsonSerDe
    sync_format: typing.Union[str, "ResourceDataSyncS3Format"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The AWS Region with the Amazon S3 bucket targeted by the Resource Data
    # Sync.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 prefix for the bucket.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an encryption key for a destination in Amazon S3. Must belong to
    # the same region as the destination Amazon S3 bucket.
    awskms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ResourceDataSyncS3Format(str):
    JsonSerDe = "JsonSerDe"


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    Error returned if an attempt is made to delete a patch baseline that is
    registered for a patch group.
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
class ResourceLimitExceededException(ShapeBase):
    """
    Error returned when the caller has exceeded the default resource limits. For
    example, too many Maintenance Windows or Patch baselines have been created.

    For information about resource limits in Systems Manager, see [AWS Systems
    Manager
    Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_ssm).
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


class ResourceType(str):
    ManagedInstance = "ManagedInstance"
    Document = "Document"
    EC2Instance = "EC2Instance"


class ResourceTypeForTagging(str):
    Document = "Document"
    ManagedInstance = "ManagedInstance"
    MaintenanceWindow = "MaintenanceWindow"
    Parameter = "Parameter"
    PatchBaseline = "PatchBaseline"


@dataclasses.dataclass
class ResultAttribute(ShapeBase):
    """
    The inventory item result attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
        ]

    # Name of the inventory item type. Valid value: AWS:InstanceInformation.
    # Default Value: AWS:InstanceInformation.
    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResumeSessionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the disconnected session to resume.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResumeSessionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
            (
                "token_value",
                "TokenValue",
                TypeInfo(str),
            ),
            (
                "stream_url",
                "StreamUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the session.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An encrypted token value containing session and caller information. Used to
    # authenticate the connection to the instance.
    token_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL back to SSM Agent on the instance that the Session Manager client
    # uses to send commands and receive output from the instance. Format:
    # `wss://ssm-messages. **region**.amazonaws.com/v1/data-channel/ **session-
    # id**?stream=(input|output)`.

    # **region** represents the Region identifier for an AWS Region supported by
    # AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For
    # a list of supported **region** values, see the **Region** column in the
    # [AWS Systems Manager table of regions and
    # endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region)
    # in the _AWS General Reference_.

    # **session-id** represents the ID of a Session Manager session, such as
    # `1a2b3c4dEXAMPLE`.
    stream_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3OutputLocation(ShapeBase):
    """
    An Amazon S3 bucket where you want to store the results of this request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_s3_region",
                "OutputS3Region",
                TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                TypeInfo(str),
            ),
        ]

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon S3 bucket.
    output_s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 bucket subfolder.
    output_s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3OutputUrl(ShapeBase):
    """
    A URL for the Amazon S3 bucket where you want to store the results of this
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_url",
                "OutputUrl",
                TypeInfo(str),
            ),
        ]

    # A URL for an Amazon S3 bucket where you want to store the results of this
    # request.
    output_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendAutomationSignalRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "signal_type",
                "SignalType",
                TypeInfo(typing.Union[str, SignalType]),
            ),
            (
                "payload",
                "Payload",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The unique identifier for an existing Automation execution that you want to
    # send the signal to.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of signal. Valid signal types include the following: Approve and
    # Reject
    signal_type: typing.Union[str, "SignalType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data sent with the signal. The data schema depends on the type of
    # signal used in the request.
    payload: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendAutomationSignalResult(OutputShapeBase):
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
class SendCommandRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "document_hash",
                "DocumentHash",
                TypeInfo(str),
            ),
            (
                "document_hash_type",
                "DocumentHashType",
                TypeInfo(typing.Union[str, DocumentHashType]),
            ),
            (
                "timeout_seconds",
                "TimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "output_s3_region",
                "OutputS3Region",
                TypeInfo(str),
            ),
            (
                "output_s3_bucket_name",
                "OutputS3BucketName",
                TypeInfo(str),
            ),
            (
                "output_s3_key_prefix",
                "OutputS3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "notification_config",
                "NotificationConfig",
                TypeInfo(NotificationConfig),
            ),
            (
                "cloud_watch_output_config",
                "CloudWatchOutputConfig",
                TypeInfo(CloudWatchOutputConfig),
            ),
        ]

    # Required. The name of the Systems Manager document to execute. This can be
    # a public document or a custom document.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance IDs where the command should execute. You can specify a
    # maximum of 50 IDs. If you prefer not to list individual instance IDs, you
    # can instead send commands to a fleet of instances using the Targets
    # parameter, which accepts EC2 tags. For more information about how to use
    # Targets, see [Sending Commands to a
    # Fleet](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html) in the _AWS Systems Manager User Guide_.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) An array of search criteria that targets instances using a
    # Key,Value combination that you specify. Targets is required if you don't
    # provide one or more instance IDs in the call. For more information about
    # how to use Targets, see [Sending Commands to a
    # Fleet](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html) in the _AWS Systems Manager User Guide_.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The SSM document version to use in the request. You can specify $DEFAULT,
    # $LATEST, or a specific version number. If you execute commands by using the
    # AWS CLI, then you must escape the first two options by using a backslash.
    # If you specify a version number, then you don't need to use the backslash.
    # For example:

    # \--document-version "\$DEFAULT"

    # \--document-version "\$LATEST"

    # \--document-version "3"
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Sha256 or Sha1 hash created by the system when the document was
    # created.

    # Sha1 hashes have been deprecated.
    document_hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sha256 or Sha1.

    # Sha1 hashes have been deprecated.
    document_hash_type: typing.Union[str, "DocumentHashType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # If this time is reached and the command has not already started executing,
    # it will not run.
    timeout_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-specified information about the command, such as a brief description
    # of what the command should do.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The required and optional parameters specified in the document being
    # executed.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Deprecated) You can no longer specify this parameter. The system ignores
    # it. Instead, Systems Manager automatically determines the Amazon S3 bucket
    # region.
    output_s3_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the S3 bucket where command execution responses should be
    # stored.
    output_s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The directory structure within the S3 bucket where the responses should be
    # stored.
    output_s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The maximum number of instances that are allowed to execute the
    # command at the same time. You can specify a number such as 10 or a
    # percentage such as 10%. The default value is 50. For more information about
    # how to use MaxConcurrency, see [Using Concurrency
    # Controls](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html#send-commands-velocity) in the _AWS Systems Manager
    # User Guide_.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of errors allowed without the command failing. When the
    # command fails one more time beyond the value of MaxErrors, the systems
    # stops sending the command to additional targets. You can specify a number
    # like 10 or a percentage like 10%. The default value is 0. For more
    # information about how to use MaxErrors, see [Using Error
    # Controls](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html#send-commands-maxerrors) in the _AWS Systems Manager
    # User Guide_.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that Systems Manager uses to send notifications.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configurations for sending notifications.
    notification_config: "NotificationConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enables Systems Manager to send Run Command output to Amazon CloudWatch
    # Logs.
    cloud_watch_output_config: "CloudWatchOutputConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendCommandResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "command",
                "Command",
                TypeInfo(Command),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The request as it was received by Systems Manager. Also provides the
    # command ID which can be used future references to this request.
    command: "Command" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Session(ShapeBase):
    """
    Information about a Session Manager connection to an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, SessionStatus]),
            ),
            (
                "start_date",
                "StartDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date",
                "EndDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "details",
                "Details",
                TypeInfo(str),
            ),
            (
                "output_url",
                "OutputUrl",
                TypeInfo(SessionManagerOutputUrl),
            ),
        ]

    # The ID of the session.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance that the Session Manager session connected to.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the session. For example, "Connected" or "Terminated".
    status: typing.Union[str, "SessionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in ISO-8601 Extended format, when the session began.
    start_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time, in ISO-8601 Extended format, when the session was
    # terminated.
    end_date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Session Manager SSM document used to define the parameters
    # and plugin settings for the session. For example, `SSM-
    # SessionManagerRunShell`.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS user account that started the session.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    output_url: "SessionManagerOutputUrl" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SessionFilter(ShapeBase):
    """
    Describes a filter for Session Manager information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(typing.Union[str, SessionFilterKey]),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The name of the filter.
    key: typing.Union[str, "SessionFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filter value. Valid values for each filter key are as follows:

    #   * InvokedAfter: Specify a timestamp to limit your results. For example, specify 2018-08-29T00:00:00Z to see sessions that started August 29, 2018, and later.

    #   * InvokedBefore: Specify a timestamp to limit your results. For example, specify 2018-08-29T00:00:00Z to see sessions that started before August 29, 2018.

    #   * Target: Specify an instance to which session connections have been made.

    #   * Owner: Specify an AWS user account to see a list of sessions started by that user.

    #   * Status: Specify a valid session status to see a list of all sessions with that status. Status values you can specify include:

    #     * Connected

    #     * Connecting

    #     * Disconnected

    #     * Terminated

    #     * Terminating

    #     * Failed
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SessionFilterKey(str):
    InvokedAfter = "InvokedAfter"
    InvokedBefore = "InvokedBefore"
    Target = "Target"
    Owner = "Owner"
    Status = "Status"


@dataclasses.dataclass
class SessionManagerOutputUrl(ShapeBase):
    """
    Reserved for future use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_url",
                "S3OutputUrl",
                TypeInfo(str),
            ),
            (
                "cloud_watch_output_url",
                "CloudWatchOutputUrl",
                TypeInfo(str),
            ),
        ]

    # Reserved for future use.
    s3_output_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    cloud_watch_output_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SessionState(str):
    Active = "Active"
    History = "History"


class SessionStatus(str):
    Connected = "Connected"
    Connecting = "Connecting"
    Disconnected = "Disconnected"
    Terminated = "Terminated"
    Terminating = "Terminating"
    Failed = "Failed"


@dataclasses.dataclass
class SeveritySummary(ShapeBase):
    """
    The number of managed instances found for each patch severity level defined in
    the request filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "critical_count",
                "CriticalCount",
                TypeInfo(int),
            ),
            (
                "high_count",
                "HighCount",
                TypeInfo(int),
            ),
            (
                "medium_count",
                "MediumCount",
                TypeInfo(int),
            ),
            (
                "low_count",
                "LowCount",
                TypeInfo(int),
            ),
            (
                "informational_count",
                "InformationalCount",
                TypeInfo(int),
            ),
            (
                "unspecified_count",
                "UnspecifiedCount",
                TypeInfo(int),
            ),
        ]

    # The total number of resources or compliance items that have a severity
    # level of critical. Critical severity is determined by the organization that
    # published the compliance items.
    critical_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of high. High severity is determined by the organization that
    # published the compliance items.
    high_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of medium. Medium severity is determined by the organization that
    # published the compliance items.
    medium_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of low. Low severity is determined by the organization that published
    # the compliance items.
    low_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of informational. Informational severity is determined by the
    # organization that published the compliance items.
    informational_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of resources or compliance items that have a severity
    # level of unspecified. Unspecified severity is determined by the
    # organization that published the compliance items.
    unspecified_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class SignalType(str):
    Approve = "Approve"
    Reject = "Reject"
    StartStep = "StartStep"
    StopStep = "StopStep"
    Resume = "Resume"


@dataclasses.dataclass
class StartAssociationsOnceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_ids",
                "AssociationIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The association IDs that you want to execute immediately and only one time.
    association_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartAssociationsOnceResult(OutputShapeBase):
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
class StartAutomationExecutionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, ExecutionMode]),
            ),
            (
                "target_parameter_name",
                "TargetParameterName",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "target_maps",
                "TargetMaps",
                TypeInfo(typing.List[typing.Dict[str, typing.List[str]]]),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
        ]

    # The name of the Automation document to use for this execution.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the Automation document to use for this execution.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value map of execution parameters, which match the declared
    # parameters in the Automation document.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User-provided idempotency token. The token must be unique, is case
    # insensitive, enforces the UUID format, and can't be reused.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution mode of the automation. Valid modes include the following:
    # Auto and Interactive. The default mode is Auto.
    mode: typing.Union[str, "ExecutionMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the parameter used as the target resource for the rate-
    # controlled execution. Required if you specify Targets.
    target_parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key-value mapping to target resources. Required if you specify
    # TargetParameterName.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A key-value mapping of document parameters to target resources. Both
    # Targets and TargetMaps cannot be specified together.
    target_maps: typing.List[typing.Dict[str, typing.List[str]]
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # The maximum number of targets allowed to run this task in parallel. You can
    # specify a number, such as 10, or a percentage, such as 10%. The default
    # value is 10.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of errors that are allowed before the system stops running the
    # automation on additional targets. You can specify either an absolute number
    # of errors, for example 10, or a percentage of the target set, for example
    # 10%. If you specify 3, for example, the system stops running the automation
    # when the fourth error is received. If you specify 0, then the system stops
    # running the automation on additional targets after the first error result
    # is returned. If you run an automation on 50 resources and set max-errors to
    # 10%, then the system stops running the automation on additional targets
    # when the sixth error is received.

    # Executions that are already running an automation when max-errors is
    # reached are allowed to complete, but some of these executions may fail as
    # well. If you need to ensure that there won't be more than max-errors failed
    # executions, set max-concurrency to 1 so the executions proceed one at a
    # time.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartAutomationExecutionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of a newly scheduled automation execution.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartSessionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
            (
                "document_name",
                "DocumentName",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The instance to connect to for the session.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SSM document to define the parameters and plugin settings
    # for the session. For example, `SSM-SessionManagerRunShell`. If no document
    # name is provided, a shell to the instance is launched by default.
    document_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartSessionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
            (
                "token_value",
                "TokenValue",
                TypeInfo(str),
            ),
            (
                "stream_url",
                "StreamUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the session.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An encrypted token value containing session and caller information. Used to
    # authenticate the connection to the instance.
    token_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL back to SSM Agent on the instance that the Session Manager client
    # uses to send commands and receive output from the instance. Format:
    # `wss://ssm-messages. **region**.amazonaws.com/v1/data-channel/ **session-
    # id**?stream=(input|output)`

    # **region** represents the Region identifier for an AWS Region supported by
    # AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For
    # a list of supported **region** values, see the **Region** column in the
    # [AWS Systems Manager table of regions and
    # endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region)
    # in the _AWS General Reference_.

    # **session-id** represents the ID of a Session Manager session, such as
    # `1a2b3c4dEXAMPLE`.
    stream_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StatusUnchanged(ShapeBase):
    """
    The updated status is the same as the current status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StepExecution(ShapeBase):
    """
    Detailed information about an the execution state of an Automation step.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "step_name",
                "StepName",
                TypeInfo(str),
            ),
            (
                "action",
                "Action",
                TypeInfo(str),
            ),
            (
                "timeout_seconds",
                "TimeoutSeconds",
                TypeInfo(int),
            ),
            (
                "on_failure",
                "OnFailure",
                TypeInfo(str),
            ),
            (
                "max_attempts",
                "MaxAttempts",
                TypeInfo(int),
            ),
            (
                "execution_start_time",
                "ExecutionStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_end_time",
                "ExecutionEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "step_status",
                "StepStatus",
                TypeInfo(typing.Union[str, AutomationExecutionStatus]),
            ),
            (
                "response_code",
                "ResponseCode",
                TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "outputs",
                "Outputs",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "response",
                "Response",
                TypeInfo(str),
            ),
            (
                "failure_message",
                "FailureMessage",
                TypeInfo(str),
            ),
            (
                "failure_details",
                "FailureDetails",
                TypeInfo(FailureDetails),
            ),
            (
                "step_execution_id",
                "StepExecutionId",
                TypeInfo(str),
            ),
            (
                "overridden_parameters",
                "OverriddenParameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "is_end",
                "IsEnd",
                TypeInfo(bool),
            ),
            (
                "next_step",
                "NextStep",
                TypeInfo(str),
            ),
            (
                "is_critical",
                "IsCritical",
                TypeInfo(bool),
            ),
            (
                "valid_next_steps",
                "ValidNextSteps",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of this execution step.
    step_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action this step performs. The action determines the behavior of the
    # step.
    action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timeout seconds of the step.
    timeout_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action to take if the step fails. The default value is Abort.
    on_failure: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of tries to run the action of the step. The default
    # value is 1.
    max_attempts: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a step has begun execution, this contains the time the step started. If
    # the step is in Pending status, this field is not populated.
    execution_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a step has finished execution, this contains the time the execution
    # ended. If the step has not yet concluded, this field is not populated.
    execution_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The execution status for this step. Valid values include: Pending,
    # InProgress, Success, Cancelled, Failed, and TimedOut.
    step_status: typing.Union[str, "AutomationExecutionStatus"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The response code returned by the execution of the step.
    response_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Fully-resolved values passed into the step before execution.
    inputs: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returned values from the execution of the step.
    outputs: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message associated with the response code for an execution.
    response: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a step failed, this message explains why the execution failed.
    failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the Automation failure.
    failure_details: "FailureDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of a step execution.
    step_execution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-specified list of parameters to override when executing a step.
    overridden_parameters: typing.Dict[str, typing.
                                       List[str]] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The flag which can be used to end automation no matter whether the step
    # succeeds or fails.
    is_end: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The next step after the step succeeds.
    next_step: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The flag which can be used to help decide whether the failure of current
    # step leads to the Automation failure.
    is_critical: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Strategies used when step fails, we support Continue and Abort. Abort will
    # fail the automation when the step fails. Continue will ignore the failure
    # of current step and allow automation to execute the next step. With
    # conditional branching, we add step:stepName to support the automation to go
    # to another specific step.
    valid_next_steps: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StepExecutionFilter(ShapeBase):
    """
    A filter to limit the amount of step execution information returned by the call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, StepExecutionFilterKey]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # One or more keys to limit the results. Valid filter keys include the
    # following: StepName, Action, StepExecutionId, StepExecutionStatus,
    # StartTimeBefore, StartTimeAfter.
    key: typing.Union[str, "StepExecutionFilterKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The values of the filter key.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class StepExecutionFilterKey(str):
    StartTimeBefore = "StartTimeBefore"
    StartTimeAfter = "StartTimeAfter"
    StepExecutionStatus = "StepExecutionStatus"
    StepExecutionId = "StepExecutionId"
    StepName = "StepName"
    Action = "Action"


@dataclasses.dataclass
class StopAutomationExecutionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "automation_execution_id",
                "AutomationExecutionId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, StopType]),
            ),
        ]

    # The execution ID of the Automation to stop.
    automation_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The stop request type. Valid types include the following: Cancel and
    # Complete. The default type is Cancel.
    type: typing.Union[str, "StopType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopAutomationExecutionResult(OutputShapeBase):
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


class StopType(str):
    Complete = "Complete"
    Cancel = "Cancel"


@dataclasses.dataclass
class SubTypeCountLimitExceededException(ShapeBase):
    """
    The sub-type count exceeded the limit for the inventory type.
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
class Tag(ShapeBase):
    """
    Metadata that you assign to your AWS resources. Tags enable you to categorize
    your resources in different ways, for example, by purpose, owner, or
    environment. In Systems Manager, you can apply tags to documents, managed
    instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
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

    # The name of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Target(ShapeBase):
    """
    An array of search criteria that targets instances using a Key,Value combination
    that you specify. `Targets` is required if you don't provide one or more
    instance IDs in the call.
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

    # User-defined criteria for sending commands that target instances that meet
    # the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more
    # information about how to send commands that target instances using
    # Key,Value parameters, see [Targeting Multiple
    # Instances](http://docs.aws.amazon.com/systems-
    # manager/latest/userguide/send-commands-multiple.html#send-commands-
    # targeting) in the _AWS Systems Manager User Guide_.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-defined criteria that maps to Key. For example, if you specified
    # tag:ServerRole, you could specify value:WebServer to execute a command on
    # instances that include Amazon EC2 tags of ServerRole,WebServer. For more
    # information about how to send commands that target instances using
    # Key,Value parameters, see [Sending Commands to a
    # Fleet](http://docs.aws.amazon.com/systems-manager/latest/userguide/send-
    # commands-multiple.html) in the _AWS Systems Manager User Guide_.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetInUseException(ShapeBase):
    """
    You specified the `Safe` option for the DeregisterTargetFromMaintenanceWindow
    operation, but the target is still referenced in a task.
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
class TargetNotConnected(ShapeBase):
    """
    The specified target instance for the session is not fully configured for use
    with Session Manager. For more information, see [Getting Started with Session
    Manager](http://docs.aws.amazon.com/systems-manager/latest/userguide/session-
    manager-getting-started.html) in the _AWS Systems Manager User Guide_.
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
class TerminateSessionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the session to terminate.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateSessionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "session_id",
                "SessionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the session that has been terminated.
    session_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyTagsError(ShapeBase):
    """
    The Targets parameter includes too many tags. Remove one or more tags and try
    the command again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TooManyUpdates(ShapeBase):
    """
    There are concurrent updates for a resource that supports one update at a time.
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
class TotalSizeLimitExceededException(ShapeBase):
    """
    The size of inventory data has exceeded the total size limit for the resource.
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
class UnsupportedInventoryItemContextException(ShapeBase):
    """
    The `Context` attribute that you specified for the `InventoryItem` is not
    allowed for this inventory type. You can only use the `Context` attribute with
    inventory types like `AWS:ComplianceItem`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type_name",
                "TypeName",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedInventorySchemaVersionException(ShapeBase):
    """
    Inventory item type schema version has to match supported versions in the
    service. Check output of GetInventorySchema to see the available schema version
    for each type.
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
class UnsupportedOperatingSystem(ShapeBase):
    """
    The operating systems you specified is not supported, or the operation is not
    supported for the operating system. Valid operating systems include: Windows,
    AmazonLinux, RedhatEnterpriseLinux, and Ubuntu.
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
class UnsupportedParameterType(ShapeBase):
    """
    The parameter type is not supported.
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


@dataclasses.dataclass
class UnsupportedPlatformType(ShapeBase):
    """
    The document does not support the platform type of the given instance ID(s). For
    example, you sent an document for a Windows instance to a Linux instance.
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
class UpdateAssociationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "association_id",
                "AssociationId",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "schedule_expression",
                "ScheduleExpression",
                TypeInfo(str),
            ),
            (
                "output_location",
                "OutputLocation",
                TypeInfo(InstanceAssociationOutputLocation),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "association_name",
                "AssociationName",
                TypeInfo(str),
            ),
            (
                "association_version",
                "AssociationVersion",
                TypeInfo(str),
            ),
        ]

    # The ID of the association you want to update.
    association_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters you want to update for the association. If you create a
    # parameter using Parameter Store, you can reference the parameter using
    # {{ssm:parameter-name}}
    parameters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The document version you want update for the association.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cron expression used to schedule the association that you want to
    # update.
    schedule_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 bucket where you want to store the results of this request.
    output_location: "InstanceAssociationOutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the association document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets of the association.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the association that you want to update.
    association_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is provided for concurrency control purposes. You must
    # specify the latest association version in the service. If you want to
    # ensure that this request succeeds, either specify `$LATEST`, or omit this
    # parameter.
    association_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAssociationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the association that was updated.
    association_description: "AssociationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAssociationStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "association_status",
                "AssociationStatus",
                TypeInfo(AssociationStatus),
            ),
        ]

    # The name of the Systems Manager document.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The association status.
    association_status: "AssociationStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAssociationStatusResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "association_description",
                "AssociationDescription",
                TypeInfo(AssociationDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the association.
    association_description: "AssociationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentDefaultVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
        ]

    # The name of a custom document that you want to set as the default version.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of a custom document that you want to set as the default
    # version.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDocumentDefaultVersionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "description",
                "Description",
                TypeInfo(DocumentDefaultVersionDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of a custom document that you want to set as the default
    # version.
    description: "DocumentDefaultVersionDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDocumentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "document_version",
                "DocumentVersion",
                TypeInfo(str),
            ),
            (
                "document_format",
                "DocumentFormat",
                TypeInfo(typing.Union[str, DocumentFormat]),
            ),
            (
                "target_type",
                "TargetType",
                TypeInfo(str),
            ),
        ]

    # The content in a document that you want to update.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the document that you want to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the document that you want to update.
    document_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the document format for the new document version. Systems Manager
    # supports JSON and YAML documents. JSON is the default format.
    document_format: typing.Union[str, "DocumentFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify a new target type for the document.
    target_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDocumentResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "document_description",
                "DocumentDescription",
                TypeInfo(DocumentDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the document that was updated.
    document_description: "DocumentDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateMaintenanceWindowRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
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
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                TypeInfo(bool),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "replace",
                "Replace",
                TypeInfo(bool),
            ),
        ]

    # The ID of the Maintenance Window to update.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description for the update request.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether targets must be registered with the Maintenance Window before tasks
    # can be defined for those targets.
    allow_unassociated_targets: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the Maintenance Window is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If True, then all fields that are required by the CreateMaintenanceWindow
    # action are also required for this API request. Optional fields that are not
    # specified are set to null.
    replace: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
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
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "cutoff",
                "Cutoff",
                TypeInfo(int),
            ),
            (
                "allow_unassociated_targets",
                "AllowUnassociatedTargets",
                TypeInfo(bool),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the created Maintenance Window.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Maintenance Window.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description of the update.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schedule of the Maintenance Window in the form of a cron or rate
    # expression.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the Maintenance Window in hours.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of hours before the end of the Maintenance Window that Systems
    # Manager stops scheduling new tasks for execution.
    cutoff: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether targets must be registered with the Maintenance Window before tasks
    # can be defined for those targets.
    allow_unassociated_targets: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the Maintenance Window is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTargetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
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
                "replace",
                "Replace",
                TypeInfo(bool),
            ),
        ]

    # The Maintenance Window ID with which to modify the target.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target ID to modify.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets to add or replace.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User-provided value that will be included in any CloudWatch events raised
    # while running tasks for these targets in this Maintenance Window.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description for the update.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If True, then all fields that are required by the
    # RegisterTargetWithMaintenanceWindow action are also required for this API
    # request. Optional fields that are not specified are set to null.
    replace: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTargetResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_target_id",
                "WindowTargetId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "owner_information",
                "OwnerInformation",
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Maintenance Window ID specified in the update request.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target ID specified in the update request.
    window_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated targets.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated owner.
    owner_information: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "task_parameters",
                "TaskParameters",
                TypeInfo(
                    typing.
                    Dict[str, MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "logging_info",
                "LoggingInfo",
                TypeInfo(LoggingInfo),
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
                "replace",
                "Replace",
                TypeInfo(bool),
            ),
        ]

    # The Maintenance Window ID that contains the task to modify.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task ID to modify.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The targets (either instances or tags) to modify. Instances are specified
    # using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified
    # using Key=tag_name,Values=tag_value.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The task ARN to modify.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM service role ARN to modify. The system assumes this role during
    # task execution.

    # If you do not specify a service role ARN, Systems Manager will use your
    # account's service-linked role for Systems Manager by default. If no
    # service-linked role for Systems Manager exists in your account, it will be
    # created when you run `RegisterTaskWithMaintenanceWindow` without specifying
    # a service role ARN.

    # For more information, see [Service-Linked Role Permissions for Systems
    # Manager](http://docs.aws.amazon.com/systems-manager/latest/userguide/using-
    # service-linked-roles.html#slr-permissions) and [Should I Use a Service-
    # Linked Role or a Custom Service Role to Run Maintenance Window Tasks?
    # ](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
    # maintenance-permissions.html#maintenance-window-tasks-service-role) in the
    # _AWS Systems Manager User Guide_.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters to modify.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.

    # The map has the following format:

    # Key: string, between 1 and 255 characters

    # Value: an array of strings, each string is between 1 and 255 characters
    task_parameters: typing.Dict[str,
                                 "MaintenanceWindowTaskParameterValueExpression"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The parameters that the task should use during execution. Populate only the
    # fields that match the task type. All other fields should be empty.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new task priority to specify. The lower the number, the higher the
    # priority. Tasks that have the same priority are scheduled in parallel.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new `MaxConcurrency` value you want to specify. `MaxConcurrency` is the
    # number of targets that are allowed to run this task in parallel.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new `MaxErrors` value to specify. `MaxErrors` is the maximum number of
    # errors that are allowed before the task stops being scheduled.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new logging location in Amazon S3 to specify.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new task name to specify.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new task description to specify.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If True, then all fields that are required by the
    # RegisterTaskWithMaintenanceWndow action are also required for this API
    # request. Optional fields that are not specified are set to null.
    replace: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceWindowTaskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "window_id",
                "WindowId",
                TypeInfo(str),
            ),
            (
                "window_task_id",
                "WindowTaskId",
                TypeInfo(str),
            ),
            (
                "targets",
                "Targets",
                TypeInfo(typing.List[Target]),
            ),
            (
                "task_arn",
                "TaskArn",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "task_parameters",
                "TaskParameters",
                TypeInfo(
                    typing.
                    Dict[str, MaintenanceWindowTaskParameterValueExpression]
                ),
            ),
            (
                "task_invocation_parameters",
                "TaskInvocationParameters",
                TypeInfo(MaintenanceWindowTaskInvocationParameters),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "max_concurrency",
                "MaxConcurrency",
                TypeInfo(str),
            ),
            (
                "max_errors",
                "MaxErrors",
                TypeInfo(str),
            ),
            (
                "logging_info",
                "LoggingInfo",
                TypeInfo(LoggingInfo),
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Maintenance Window that was updated.
    window_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task ID of the Maintenance Window that was updated.
    window_task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated target values.
    targets: typing.List["Target"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated task ARN value.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated service role ARN value.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated parameter values.

    # `TaskParameters` has been deprecated. To specify parameters to pass to a
    # task when it runs, instead use the `Parameters` option in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    task_parameters: typing.Dict[str,
                                 "MaintenanceWindowTaskParameterValueExpression"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The updated parameter values.
    task_invocation_parameters: "MaintenanceWindowTaskInvocationParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated priority value.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated MaxConcurrency value.
    max_concurrency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated MaxErrors value.
    max_errors: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated logging information in Amazon S3.

    # `LoggingInfo` has been deprecated. To specify an S3 bucket to contain logs,
    # instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the
    # `TaskInvocationParameters` structure. For information about how Systems
    # Manager handles these options for the supported Maintenance Window task
    # types, see MaintenanceWindowTaskInvocationParameters.
    logging_info: "LoggingInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated task name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated task description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateManagedInstanceRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "iam_role",
                "IamRole",
                TypeInfo(str),
            ),
        ]

    # The ID of the managed instance where you want to update the role.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role you want to assign or change.
    iam_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateManagedInstanceRoleResult(OutputShapeBase):
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
class UpdatePatchBaselineRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "global_filters",
                "GlobalFilters",
                TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                TypeInfo(typing.Union[str, PatchComplianceLevel]),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[PatchSource]),
            ),
            (
                "replace",
                "Replace",
                TypeInfo(bool),
            ),
        ]

    # The ID of the patch baseline to update.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly approved patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    approved_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Assigns a new compliance severity level to an existing patch baseline.
    approved_patches_compliance_level: typing.Union[
        str, "PatchComplianceLevel"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.

    # For information about accepted formats for lists of approved patches and
    # rejected patches, see [Package Name Formats for Approved and Rejected Patch
    # Lists](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-
    # manager-approved-rejected-package-name-formats.html) in the _AWS Systems
    # Manager User Guide_.
    rejected_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the patch baseline.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If True, then all fields that are required by the CreatePatchBaseline
    # action are also required for this API request. Optional fields that are not
    # specified are set to null.
    replace: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePatchBaselineResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baseline_id",
                "BaselineId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "OperatingSystem",
                TypeInfo(typing.Union[str, OperatingSystem]),
            ),
            (
                "global_filters",
                "GlobalFilters",
                TypeInfo(PatchFilterGroup),
            ),
            (
                "approval_rules",
                "ApprovalRules",
                TypeInfo(PatchRuleGroup),
            ),
            (
                "approved_patches",
                "ApprovedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "approved_patches_compliance_level",
                "ApprovedPatchesComplianceLevel",
                TypeInfo(typing.Union[str, PatchComplianceLevel]),
            ),
            (
                "approved_patches_enable_non_security",
                "ApprovedPatchesEnableNonSecurity",
                TypeInfo(bool),
            ),
            (
                "rejected_patches",
                "RejectedPatches",
                TypeInfo(typing.List[str]),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_date",
                "ModifiedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[PatchSource]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the deleted patch baseline.
    baseline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the patch baseline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system rule used by the updated patch baseline.
    operating_system: typing.Union[str, "OperatingSystem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of global filters used to exclude patches from the baseline.
    global_filters: "PatchFilterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of rules used to include patches in the baseline.
    approval_rules: "PatchRuleGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly approved patches for the baseline.
    approved_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compliance severity level assigned to the patch baseline after the
    # update completed.
    approved_patches_compliance_level: typing.Union[
        str, "PatchComplianceLevel"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Indicates whether the list of approved patches includes non-security
    # updates that should be applied to the instances. The default value is
    # 'false'. Applies to Linux instances only.
    approved_patches_enable_non_security: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of explicitly rejected patches for the baseline.
    rejected_patches: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the patch baseline was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the patch baseline was last modified.
    modified_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the Patch Baseline.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the patches to use to update the instances, including
    # target operating systems and source repositories. Applies to Linux
    # instances only.
    sources: typing.List["PatchSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
