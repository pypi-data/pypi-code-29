import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AccessDeniedErrorCode(str):
    ACCESS_DENIED_TO_ASSESSMENT_TARGET = "ACCESS_DENIED_TO_ASSESSMENT_TARGET"
    ACCESS_DENIED_TO_ASSESSMENT_TEMPLATE = "ACCESS_DENIED_TO_ASSESSMENT_TEMPLATE"
    ACCESS_DENIED_TO_ASSESSMENT_RUN = "ACCESS_DENIED_TO_ASSESSMENT_RUN"
    ACCESS_DENIED_TO_FINDING = "ACCESS_DENIED_TO_FINDING"
    ACCESS_DENIED_TO_RESOURCE_GROUP = "ACCESS_DENIED_TO_RESOURCE_GROUP"
    ACCESS_DENIED_TO_RULES_PACKAGE = "ACCESS_DENIED_TO_RULES_PACKAGE"
    ACCESS_DENIED_TO_SNS_TOPIC = "ACCESS_DENIED_TO_SNS_TOPIC"
    ACCESS_DENIED_TO_IAM_ROLE = "ACCESS_DENIED_TO_IAM_ROLE"


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    You do not have required permissions to access the requested resource.
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
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, AccessDeniedErrorCode]),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: typing.Union[str, "AccessDeniedErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddAttributesToFindingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_arns",
                "findingArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The ARNs that specify the findings that you want to assign attributes to.
    finding_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The array of attributes that you want to assign to specified findings.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddAttributesToFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attribute details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AgentAlreadyRunningAssessment(ShapeBase):
    """
    Used in the exception error that is thrown if you start an assessment run for an
    assessment target that includes an EC2 instance that is already participating in
    another started assessment run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                TypeInfo(str),
            ),
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
        ]

    # ID of the agent that is running on an EC2 instance that is already
    # participating in another started assessment run.
    agent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the assessment run that has already been started.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AgentFilter(ShapeBase):
    """
    Contains information about an Amazon Inspector agent. This data type is used as
    a request parameter in the ListAssessmentRunAgents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_healths",
                "agentHealths",
                TypeInfo(typing.List[typing.Union[str, AgentHealth]]),
            ),
            (
                "agent_health_codes",
                "agentHealthCodes",
                TypeInfo(typing.List[typing.Union[str, AgentHealthCode]]),
            ),
        ]

    # The current health state of the agent. Values can be set to **HEALTHY** or
    # **UNHEALTHY**.
    agent_healths: typing.List[typing.Union[str, "AgentHealth"]
                              ] = dataclasses.field(
                                  default=ShapeBase.NOT_SET,
                              )

    # The detailed health state of the agent. Values can be set to **IDLE** ,
    # **RUNNING** , **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and
    # **UNKNOWN**.
    agent_health_codes: typing.List[typing.Union[str, "AgentHealthCode"]
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


class AgentHealth(str):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"


class AgentHealthCode(str):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    SHUTDOWN = "SHUTDOWN"
    UNHEALTHY = "UNHEALTHY"
    THROTTLED = "THROTTLED"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class AgentPreview(ShapeBase):
    """
    Used as a response element in the PreviewAgents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group",
                "autoScalingGroup",
                TypeInfo(str),
            ),
            (
                "agent_health",
                "agentHealth",
                TypeInfo(typing.Union[str, AgentHealth]),
            ),
            (
                "agent_version",
                "agentVersion",
                TypeInfo(str),
            ),
            (
                "operating_system",
                "operatingSystem",
                TypeInfo(str),
            ),
            (
                "kernel_version",
                "kernelVersion",
                TypeInfo(str),
            ),
            (
                "ipv4_address",
                "ipv4Address",
                TypeInfo(str),
            ),
        ]

    # The ID of the EC2 instance where the agent is installed.
    agent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hostname of the EC2 instance on which the Amazon Inspector Agent is
    # installed.
    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Auto Scaling group for the EC2 instance where the agent is installed.
    auto_scaling_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The health status of the Amazon Inspector Agent.
    agent_health: typing.Union[str, "AgentHealth"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the Amazon Inspector Agent.
    agent_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system running on the EC2 instance on which the Amazon
    # Inspector Agent is installed.
    operating_system: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The kernel version of the operating system running on the EC2 instance on
    # which the Amazon Inspector Agent is installed.
    kernel_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address of the EC2 instance on which the Amazon Inspector Agent is
    # installed.
    ipv4_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AgentsAlreadyRunningAssessmentException(ShapeBase):
    """
    You started an assessment run, but one of the instances is already participating
    in another assessment run.
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
                "agents",
                "agents",
                TypeInfo(typing.List[AgentAlreadyRunningAssessment]),
            ),
            (
                "agents_truncated",
                "agentsTruncated",
                TypeInfo(bool),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    agents: typing.List["AgentAlreadyRunningAssessment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    agents_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssessmentRun(ShapeBase):
    """
    A snapshot of an Amazon Inspector assessment run that contains the findings of
    the assessment run .

    Used as the response element in the DescribeAssessmentRuns action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, AssessmentRunState]),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                TypeInfo(int),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "user_attributes_for_findings",
                "userAttributesForFindings",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "state_changed_at",
                "stateChangedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "data_collected",
                "dataCollected",
                TypeInfo(bool),
            ),
            (
                "state_changes",
                "stateChanges",
                TypeInfo(typing.List[AssessmentRunStateChange]),
            ),
            (
                "notifications",
                "notifications",
                TypeInfo(typing.List[AssessmentRunNotification]),
            ),
            (
                "finding_counts",
                "findingCounts",
                TypeInfo(typing.Dict[typing.Union[str, Severity], int]),
            ),
            (
                "started_at",
                "startedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "completed_at",
                "completedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the assessment run.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The auto-generated name for the assessment run.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the assessment template that is associated with the assessment
    # run.
    assessment_template_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the assessment run.
    state: typing.Union[str, "AssessmentRunState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration of the assessment run.
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rules packages selected for the assessment run.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-defined attributes that are assigned to every generated finding.
    user_attributes_for_findings: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when StartAssessmentRun was called.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time when the assessment run's state changed.
    state_changed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value (true or false) that specifies whether the process of
    # collecting data from the agents is completed.
    data_collected: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the assessment run state changes.
    state_changes: typing.List["AssessmentRunStateChange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of notifications for the event subscriptions. A notification about a
    # particular generated finding is added to this list only once.
    notifications: typing.List["AssessmentRunNotification"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides a total count of generated findings per severity.
    finding_counts: typing.Dict[typing.Union[str, "Severity"], int
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The time when StartAssessmentRun was called.
    started_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The assessment run completion time that corresponds to the rules packages
    # evaluation completion time or failure.
    completed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentRunAgent(ShapeBase):
    """
    Contains information about an Amazon Inspector agent. This data type is used as
    a response element in the ListAssessmentRunAgents action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_id",
                "agentId",
                TypeInfo(str),
            ),
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
            (
                "agent_health",
                "agentHealth",
                TypeInfo(typing.Union[str, AgentHealth]),
            ),
            (
                "agent_health_code",
                "agentHealthCode",
                TypeInfo(typing.Union[str, AgentHealthCode]),
            ),
            (
                "telemetry_metadata",
                "telemetryMetadata",
                TypeInfo(typing.List[TelemetryMetadata]),
            ),
            (
                "agent_health_details",
                "agentHealthDetails",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group",
                "autoScalingGroup",
                TypeInfo(str),
            ),
        ]

    # The AWS account of the EC2 instance where the agent is installed.
    agent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the assessment run that is associated with the agent.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current health state of the agent.
    agent_health: typing.Union[str, "AgentHealth"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The detailed health state of the agent.
    agent_health_code: typing.Union[str, "AgentHealthCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Inspector application data metrics that are collected by the
    # agent.
    telemetry_metadata: typing.List["TelemetryMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for the agent health code.
    agent_health_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Auto Scaling group of the EC2 instance that is specified by the agent
    # ID.
    auto_scaling_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssessmentRunFilter(ShapeBase):
    """
    Used as the request parameter in the ListAssessmentRuns action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_pattern",
                "namePattern",
                TypeInfo(str),
            ),
            (
                "states",
                "states",
                TypeInfo(typing.List[typing.Union[str, AssessmentRunState]]),
            ),
            (
                "duration_range",
                "durationRange",
                TypeInfo(DurationRange),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "start_time_range",
                "startTimeRange",
                TypeInfo(TimestampRange),
            ),
            (
                "completion_time_range",
                "completionTimeRange",
                TypeInfo(TimestampRange),
            ),
            (
                "state_change_time_range",
                "stateChangeTimeRange",
                TypeInfo(TimestampRange),
            ),
        ]

    # For a record to match a filter, an explicit value or a string containing a
    # wildcard that is specified for this data type property must match the value
    # of the **assessmentRunName** property of the AssessmentRun data type.
    name_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a record to match a filter, one of the values specified for this data
    # type property must be the exact match of the value of the
    # **assessmentRunState** property of the AssessmentRun data type.
    states: typing.List[typing.Union[str, "AssessmentRunState"]
                       ] = dataclasses.field(
                           default=ShapeBase.NOT_SET,
                       )

    # For a record to match a filter, the value that is specified for this data
    # type property must inclusively match any value between the specified
    # minimum and maximum values of the **durationInSeconds** property of the
    # AssessmentRun data type.
    duration_range: "DurationRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must be contained in the list of values of the
    # **rulesPackages** property of the AssessmentRun data type.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must inclusively match any value between the specified
    # minimum and maximum values of the **startTime** property of the
    # AssessmentRun data type.
    start_time_range: "TimestampRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must inclusively match any value between the specified
    # minimum and maximum values of the **completedAt** property of the
    # AssessmentRun data type.
    completion_time_range: "TimestampRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must match the **stateChangedAt** property of the
    # AssessmentRun data type.
    state_change_time_range: "TimestampRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentRunInProgressException(ShapeBase):
    """
    You cannot perform a specified action if an assessment run is currently in
    progress.
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
                "assessment_run_arns",
                "assessmentRunArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "assessment_run_arns_truncated",
                "assessmentRunArnsTruncated",
                TypeInfo(bool),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARNs of the assessment runs that are currently in progress.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Boolean value that indicates whether the ARN list of the assessment runs is
    # truncated.
    assessment_run_arns_truncated: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssessmentRunNotification(ShapeBase):
    """
    Used as one of the elements of the AssessmentRun data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "date",
                TypeInfo(datetime.datetime),
            ),
            (
                "event",
                "event",
                TypeInfo(typing.Union[str, InspectorEvent]),
            ),
            (
                "error",
                "error",
                TypeInfo(bool),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "snsTopicArn",
                TypeInfo(str),
            ),
            (
                "sns_publish_status_code",
                "snsPublishStatusCode",
                TypeInfo(
                    typing.Union[str, AssessmentRunNotificationSnsStatusCode]
                ),
            ),
        ]

    # The date of the notification.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event for which a notification is sent.
    event: typing.Union[str, "InspectorEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Boolean value that specifies whether the notification represents an
    # error.
    error: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message included in the notification.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SNS topic to which the SNS notification is sent.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status code of the SNS notification.
    sns_publish_status_code: typing.Union[
        str, "AssessmentRunNotificationSnsStatusCode"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class AssessmentRunNotificationSnsStatusCode(str):
    SUCCESS = "SUCCESS"
    TOPIC_DOES_NOT_EXIST = "TOPIC_DOES_NOT_EXIST"
    ACCESS_DENIED = "ACCESS_DENIED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class AssessmentRunState(str):
    CREATED = "CREATED"
    START_DATA_COLLECTION_PENDING = "START_DATA_COLLECTION_PENDING"
    START_DATA_COLLECTION_IN_PROGRESS = "START_DATA_COLLECTION_IN_PROGRESS"
    COLLECTING_DATA = "COLLECTING_DATA"
    STOP_DATA_COLLECTION_PENDING = "STOP_DATA_COLLECTION_PENDING"
    DATA_COLLECTED = "DATA_COLLECTED"
    START_EVALUATING_RULES_PENDING = "START_EVALUATING_RULES_PENDING"
    EVALUATING_RULES = "EVALUATING_RULES"
    FAILED = "FAILED"
    ERROR = "ERROR"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"
    CANCELED = "CANCELED"


@dataclasses.dataclass
class AssessmentRunStateChange(ShapeBase):
    """
    Used as one of the elements of the AssessmentRun data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state_changed_at",
                "stateChangedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, AssessmentRunState]),
            ),
        ]

    # The last time the assessment run state changed.
    state_changed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The assessment run state.
    state: typing.Union[str, "AssessmentRunState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTarget(ShapeBase):
    """
    Contains information about an Amazon Inspector application. This data type is
    used as the response element in the DescribeAssessmentTargets action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_at",
                "updatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                TypeInfo(str),
            ),
        ]

    # The ARN that specifies the Amazon Inspector assessment target.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon Inspector assessment target.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the assessment target is created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which UpdateAssessmentTarget is called.
    updated_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that specifies the resource group that is associated with the
    # assessment target.
    resource_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssessmentTargetFilter(ShapeBase):
    """
    Used as the request parameter in the ListAssessmentTargets action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_name_pattern",
                "assessmentTargetNamePattern",
                TypeInfo(str),
            ),
        ]

    # For a record to match a filter, an explicit value or a string that contains
    # a wildcard that is specified for this data type property must match the
    # value of the **assessmentTargetName** property of the AssessmentTarget data
    # type.
    assessment_target_name_pattern: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTemplate(ShapeBase):
    """
    Contains information about an Amazon Inspector assessment template. This data
    type is used as the response element in the DescribeAssessmentTemplates action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                TypeInfo(str),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                TypeInfo(int),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "user_attributes_for_findings",
                "userAttributesForFindings",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "assessment_run_count",
                "assessmentRunCount",
                TypeInfo(int),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_assessment_run_arn",
                "lastAssessmentRunArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the assessment template.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the assessment target that corresponds to this assessment
    # template.
    assessment_target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration in seconds specified for this assessment template. The default
    # value is 3600 seconds (one hour). The maximum value is 86400 seconds (one
    # day).
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rules packages that are specified for this assessment template.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-defined attributes that are assigned to every generated finding
    # from the assessment run that uses this assessment template.
    user_attributes_for_findings: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of existing assessment runs associated with this assessment
    # template. This value can be zero or a positive integer.
    assessment_run_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the assessment template is created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the most recent assessment run associated
    # with this assessment template. This value exists only when the value of
    # assessmentRunCount is greaterpa than zero.
    last_assessment_run_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssessmentTemplateFilter(ShapeBase):
    """
    Used as the request parameter in the ListAssessmentTemplates action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_pattern",
                "namePattern",
                TypeInfo(str),
            ),
            (
                "duration_range",
                "durationRange",
                TypeInfo(DurationRange),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # For a record to match a filter, an explicit value or a string that contains
    # a wildcard that is specified for this data type property must match the
    # value of the **assessmentTemplateName** property of the AssessmentTemplate
    # data type.
    name_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a record to match a filter, the value specified for this data type
    # property must inclusively match any value between the specified minimum and
    # maximum values of the **durationInSeconds** property of the
    # AssessmentTemplate data type.
    duration_range: "DurationRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the values that are specified for this data
    # type property must be contained in the list of values of the
    # **rulesPackageArns** property of the AssessmentTemplate data type.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssetAttributes(ShapeBase):
    """
    A collection of attributes of the host from which the finding is generated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_version",
                "schemaVersion",
                TypeInfo(int),
            ),
            (
                "agent_id",
                "agentId",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group",
                "autoScalingGroup",
                TypeInfo(str),
            ),
            (
                "ami_id",
                "amiId",
                TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                TypeInfo(str),
            ),
            (
                "ipv4_addresses",
                "ipv4Addresses",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The schema version of this data type.
    schema_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the agent that is installed on the EC2 instance where the finding
    # is generated.
    agent_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Auto Scaling group of the EC2 instance where the finding is generated.
    auto_scaling_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the Amazon Machine Image (AMI) that is installed on the EC2
    # instance where the finding is generated.
    ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hostname of the EC2 instance where the finding is generated.
    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of IP v4 addresses of the EC2 instance where the finding is
    # generated.
    ipv4_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AssetType(str):
    ec2_instance = "ec2-instance"


@dataclasses.dataclass
class Attribute(ShapeBase):
    """
    This data type is used as a request parameter in the AddAttributesToFindings and
    CreateAssessmentTemplate actions.
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

    # The attribute key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value assigned to the attribute key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssessmentTargetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_name",
                "assessmentTargetName",
                TypeInfo(str),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                TypeInfo(str),
            ),
        ]

    # The user-defined name that identifies the assessment target that you want
    # to create. The name must be unique within the AWS account.
    assessment_target_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN that specifies the resource group that is used to create the
    # assessment target. If resourceGroupArn is not specified, all EC2 instances
    # in the current AWS account and region are included in the assessment
    # target.
    resource_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssessmentTargetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that specifies the assessment target that is created.
    assessment_target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAssessmentTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                TypeInfo(str),
            ),
            (
                "assessment_template_name",
                "assessmentTemplateName",
                TypeInfo(str),
            ),
            (
                "duration_in_seconds",
                "durationInSeconds",
                TypeInfo(int),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "user_attributes_for_findings",
                "userAttributesForFindings",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The ARN that specifies the assessment target for which you want to create
    # the assessment template.
    assessment_target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined name that identifies the assessment template that you want
    # to create. You can create several assessment templates for an assessment
    # target. The names of the assessment templates that correspond to a
    # particular assessment target must be unique.
    assessment_template_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration of the assessment run in seconds.
    duration_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARNs that specify the rules packages that you want to attach to the
    # assessment template.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-defined attributes that are assigned to every finding that is
    # generated by the assessment run that uses this assessment template. An
    # attribute is a key and value pair (an Attribute object). Within an
    # assessment template, each key must be unique.
    user_attributes_for_findings: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAssessmentTemplateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that specifies the assessment template that is created.
    assessment_template_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExclusionsPreviewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment template for which you want to create
    # an exclusions preview.
    assessment_template_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExclusionsPreviewResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preview_token",
                "previewToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the unique identifier of the requested exclusions preview. You
    # can use the unique identifier to retrieve the exclusions preview when
    # running the GetExclusionsPreview API.
    preview_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_group_tags",
                "resourceGroupTags",
                TypeInfo(typing.List[ResourceGroupTag]),
            ),
        ]

    # A collection of keys and an array of possible values,
    # '[{"key":"key1","values":["Value1","Value2"]},{"key":"Key2","values":["Value3"]}]'.

    # For example,'[{"key":"Name","values":["TestEC2Instance"]}]'.
    resource_group_tags: typing.List["ResourceGroupTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateResourceGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that specifies the resource group that is created.
    resource_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAssessmentRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment run that you want to delete.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAssessmentTargetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment target that you want to delete.
    assessment_target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAssessmentTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment template that you want to delete.
    assessment_template_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentRunsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arns",
                "assessmentRunArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN that specifies the assessment run that you want to describe.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentRunsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_runs",
                "assessmentRuns",
                TypeInfo(typing.List[AssessmentRun]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the assessment run.
    assessment_runs: typing.List["AssessmentRun"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Assessment run details that cannot be described. An error code is provided
    # for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arns",
                "assessmentTargetArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARNs that specifies the assessment targets that you want to describe.
    assessment_target_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentTargetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_targets",
                "assessmentTargets",
                TypeInfo(typing.List[AssessmentTarget]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the assessment targets.
    assessment_targets: typing.List["AssessmentTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Assessment target details that cannot be described. An error code is
    # provided for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentTemplatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arns",
                "assessmentTemplateArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    assessment_template_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAssessmentTemplatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_templates",
                "assessmentTemplates",
                TypeInfo(typing.List[AssessmentTemplate]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the assessment templates.
    assessment_templates: typing.List["AssessmentTemplate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Assessment template details that cannot be described. An error code is
    # provided for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCrossAccountAccessRoleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "valid",
                "valid",
                TypeInfo(bool),
            ),
            (
                "registered_at",
                "registeredAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that specifies the IAM role that Amazon Inspector uses to access
    # your AWS account.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value that specifies whether the IAM role has the necessary
    # policies attached to enable Amazon Inspector to access your AWS account.
    valid: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the cross-account access role was registered.
    registered_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeExclusionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exclusion_arns",
                "exclusionArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
        ]

    # The list of ARNs that specify the exclusions that you want to describe.
    exclusion_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The locale into which you want to translate the exclusion's title,
    # description, and recommendation.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeExclusionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exclusions",
                "exclusions",
                TypeInfo(typing.Dict[str, Exclusion]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the exclusions.
    exclusions: typing.Dict[str, "Exclusion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Exclusion details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeFindingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_arns",
                "findingArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
        ]

    # The ARN that specifies the finding that you want to describe.
    finding_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The locale into which you want to translate a finding description,
    # recommendation, and the short description that identifies the finding.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "findings",
                "findings",
                TypeInfo(typing.List[Finding]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the finding.
    findings: typing.List["Finding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Finding details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeResourceGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_group_arns",
                "resourceGroupArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN that specifies the resource group that you want to describe.
    resource_group_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeResourceGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_groups",
                "resourceGroups",
                TypeInfo(typing.List[ResourceGroup]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a resource group.
    resource_groups: typing.List["ResourceGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Resource group details that cannot be described. An error code is provided
    # for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeRulesPackagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
        ]

    # The ARN that specifies the rules package that you want to describe.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The locale that you want to translate a rules package description into.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeRulesPackagesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules_packages",
                "rulesPackages",
                TypeInfo(typing.List[RulesPackage]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the rules package.
    rules_packages: typing.List["RulesPackage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Rules package details that cannot be described. An error code is provided
    # for each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DurationRange(ShapeBase):
    """
    This data type is used in the AssessmentTemplateFilter data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "min_seconds",
                "minSeconds",
                TypeInfo(int),
            ),
            (
                "max_seconds",
                "maxSeconds",
                TypeInfo(int),
            ),
        ]

    # The minimum value of the duration range. Must be greater than zero.
    min_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value of the duration range. Must be less than or equal to
    # 604800 seconds (1 week).
    max_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSubscription(ShapeBase):
    """
    This data type is used in the Subscription data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event",
                "event",
                TypeInfo(typing.Union[str, InspectorEvent]),
            ),
            (
                "subscribed_at",
                "subscribedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The event for which Amazon Simple Notification Service (SNS) notifications
    # are sent.
    event: typing.Union[str, "InspectorEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which SubscribeToEvent is called.
    subscribed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Exclusion(ShapeBase):
    """
    Contains information about what was excluded from an assessment run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "recommendation",
                "recommendation",
                TypeInfo(str),
            ),
            (
                "scopes",
                "scopes",
                TypeInfo(typing.List[Scope]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The ARN that specifies the exclusion.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the exclusion.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the exclusion.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recommendation for the exclusion.
    recommendation: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS resources for which the exclusion pertains.
    scopes: typing.List["Scope"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The system-defined attributes for the exclusion.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExclusionPreview(ShapeBase):
    """
    Contains information about what is excluded from an assessment run given the
    current state of the assessment template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "recommendation",
                "recommendation",
                TypeInfo(str),
            ),
            (
                "scopes",
                "scopes",
                TypeInfo(typing.List[Scope]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The name of the exclusion preview.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the exclusion preview.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recommendation for the exclusion preview.
    recommendation: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS resources for which the exclusion preview pertains.
    scopes: typing.List["Scope"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The system-defined attributes for the exclusion preview.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailedItemDetails(ShapeBase):
    """
    Includes details about the failed items.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "failure_code",
                "failureCode",
                TypeInfo(typing.Union[str, FailedItemErrorCode]),
            ),
            (
                "retryable",
                "retryable",
                TypeInfo(bool),
            ),
        ]

    # The status code of a failed item.
    failure_code: typing.Union[str, "FailedItemErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether you can immediately retry a request for this item for a
    # specified resource.
    retryable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class FailedItemErrorCode(str):
    INVALID_ARN = "INVALID_ARN"
    DUPLICATE_ARN = "DUPLICATE_ARN"
    ITEM_DOES_NOT_EXIST = "ITEM_DOES_NOT_EXIST"
    ACCESS_DENIED = "ACCESS_DENIED"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


@dataclasses.dataclass
class Finding(ShapeBase):
    """
    Contains information about an Amazon Inspector finding. This data type is used
    as the response element in the DescribeFindings action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "user_attributes",
                "userAttributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_at",
                "updatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "schema_version",
                "schemaVersion",
                TypeInfo(int),
            ),
            (
                "service",
                "service",
                TypeInfo(str),
            ),
            (
                "service_attributes",
                "serviceAttributes",
                TypeInfo(InspectorServiceAttributes),
            ),
            (
                "asset_type",
                "assetType",
                TypeInfo(typing.Union[str, AssetType]),
            ),
            (
                "asset_attributes",
                "assetAttributes",
                TypeInfo(AssetAttributes),
            ),
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "recommendation",
                "recommendation",
                TypeInfo(str),
            ),
            (
                "severity",
                "severity",
                TypeInfo(typing.Union[str, Severity]),
            ),
            (
                "numeric_severity",
                "numericSeverity",
                TypeInfo(float),
            ),
            (
                "confidence",
                "confidence",
                TypeInfo(int),
            ),
            (
                "indicator_of_compromise",
                "indicatorOfCompromise",
                TypeInfo(bool),
            ),
        ]

    # The ARN that specifies the finding.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The system-defined attributes for the finding.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-defined attributes that are assigned to the finding.
    user_attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the finding was generated.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when AddAttributesToFindings is called.
    updated_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The schema version of this data type.
    schema_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data element is set to "Inspector".
    service: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This data type is used in the Finding data type.
    service_attributes: "InspectorServiceAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the host from which the finding is generated.
    asset_type: typing.Union[str, "AssetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of attributes of the host from which the finding is generated.
    asset_attributes: "AssetAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the finding.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the finding.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the finding.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recommendation for the finding.
    recommendation: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The finding severity. Values can be set to High, Medium, Low, and
    # Informational.
    severity: typing.Union[str, "Severity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The numeric value of the finding severity.
    numeric_severity: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This data element is currently not used.
    confidence: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This data element is currently not used.
    indicator_of_compromise: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FindingFilter(ShapeBase):
    """
    This data type is used as a request parameter in the ListFindings action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_ids",
                "agentIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "auto_scaling_groups",
                "autoScalingGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "rule_names",
                "ruleNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "severities",
                "severities",
                TypeInfo(typing.List[typing.Union[str, Severity]]),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "user_attributes",
                "userAttributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "creation_time_range",
                "creationTimeRange",
                TypeInfo(TimestampRange),
            ),
        ]

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **agentId** property of the Finding data type.
    agent_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **autoScalingGroup** property of the Finding data type.
    auto_scaling_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **ruleName** property of the Finding data type.
    rule_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **severity** property of the Finding data type.
    severities: typing.List[typing.Union[str, "Severity"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, one of the values that is specified for
    # this data type property must be the exact match of the value of the
    # **rulesPackageArn** property of the Finding data type.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the list of values that are specified for
    # this data type property must be contained in the list of values of the
    # **attributes** property of the Finding data type.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For a record to match a filter, the value that is specified for this data
    # type property must be contained in the list of values of the
    # **userAttributes** property of the Finding data type.
    user_attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time range during which the finding is generated.
    creation_time_range: "TimestampRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAssessmentReportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
            (
                "report_file_format",
                "reportFileFormat",
                TypeInfo(typing.Union[str, ReportFileFormat]),
            ),
            (
                "report_type",
                "reportType",
                TypeInfo(typing.Union[str, ReportType]),
            ),
        ]

    # The ARN that specifies the assessment run for which you want to generate a
    # report.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the file format (html or pdf) of the assessment report that you
    # want to generate.
    report_file_format: typing.Union[str, "ReportFileFormat"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Specifies the type of the assessment report that you want to generate.
    # There are two types of assessment reports: a finding report and a full
    # report. For more information, see [Assessment
    # Reports](http://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html).
    report_type: typing.Union[str, "ReportType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAssessmentReportResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ReportStatus]),
            ),
            (
                "url",
                "url",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the request to generate an assessment report.
    status: typing.Union[str, "ReportStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the URL where you can find the generated assessment report. This
    # parameter is only returned if the report is successfully generated.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExclusionsPreviewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                TypeInfo(str),
            ),
            (
                "preview_token",
                "previewToken",
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
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
        ]

    # The ARN that specifies the assessment template for which the exclusions
    # preview was requested.
    assessment_template_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier associated of the exclusions preview.
    preview_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the GetExclusionsPreviewRequest
    # action. Subsequent calls to the action fill nextToken in the request with
    # the value of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 100. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locale into which you want to translate the exclusion's title,
    # description, and recommendation.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetExclusionsPreviewResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preview_status",
                "previewStatus",
                TypeInfo(typing.Union[str, PreviewStatus]),
            ),
            (
                "exclusion_previews",
                "exclusionPreviews",
                TypeInfo(typing.List[ExclusionPreview]),
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

    # Specifies the status of the request to generate an exclusions preview.
    preview_status: typing.Union[str, "PreviewStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the exclusions included in the preview.
    exclusion_previews: typing.List["ExclusionPreview"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameters is present in the response and contains the value to use for the
    # nextToken parameter in a subsequent pagination request. If there is no more
    # data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTelemetryMetadataRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
        ]

    # The ARN that specifies the assessment run that has the telemetry data that
    # you want to obtain.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTelemetryMetadataResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "telemetry_metadata",
                "telemetryMetadata",
                TypeInfo(typing.List[TelemetryMetadata]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Telemetry details.
    telemetry_metadata: typing.List["TelemetryMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InspectorEvent(str):
    ASSESSMENT_RUN_STARTED = "ASSESSMENT_RUN_STARTED"
    ASSESSMENT_RUN_COMPLETED = "ASSESSMENT_RUN_COMPLETED"
    ASSESSMENT_RUN_STATE_CHANGED = "ASSESSMENT_RUN_STATE_CHANGED"
    FINDING_REPORTED = "FINDING_REPORTED"
    OTHER = "OTHER"


@dataclasses.dataclass
class InspectorServiceAttributes(ShapeBase):
    """
    This data type is used in the Finding data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_version",
                "schemaVersion",
                TypeInfo(int),
            ),
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
            (
                "rules_package_arn",
                "rulesPackageArn",
                TypeInfo(str),
            ),
        ]

    # The schema version of this data type.
    schema_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the assessment run during which the finding is generated.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the rules package that is used to generate the finding.
    rules_package_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalException(ShapeBase):
    """
    Internal server error.
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
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class InvalidCrossAccountRoleErrorCode(str):
    ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP = "ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP"
    ROLE_DOES_NOT_HAVE_CORRECT_POLICY = "ROLE_DOES_NOT_HAVE_CORRECT_POLICY"


@dataclasses.dataclass
class InvalidCrossAccountRoleException(ShapeBase):
    """
    Amazon Inspector cannot assume the cross-account role that it needs to list your
    EC2 instances during the assessment run.
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
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, InvalidCrossAccountRoleErrorCode]),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: typing.Union[str, "InvalidCrossAccountRoleErrorCode"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class InvalidInputErrorCode(str):
    INVALID_ASSESSMENT_TARGET_ARN = "INVALID_ASSESSMENT_TARGET_ARN"
    INVALID_ASSESSMENT_TEMPLATE_ARN = "INVALID_ASSESSMENT_TEMPLATE_ARN"
    INVALID_ASSESSMENT_RUN_ARN = "INVALID_ASSESSMENT_RUN_ARN"
    INVALID_FINDING_ARN = "INVALID_FINDING_ARN"
    INVALID_RESOURCE_GROUP_ARN = "INVALID_RESOURCE_GROUP_ARN"
    INVALID_RULES_PACKAGE_ARN = "INVALID_RULES_PACKAGE_ARN"
    INVALID_RESOURCE_ARN = "INVALID_RESOURCE_ARN"
    INVALID_SNS_TOPIC_ARN = "INVALID_SNS_TOPIC_ARN"
    INVALID_IAM_ROLE_ARN = "INVALID_IAM_ROLE_ARN"
    INVALID_ASSESSMENT_TARGET_NAME = "INVALID_ASSESSMENT_TARGET_NAME"
    INVALID_ASSESSMENT_TARGET_NAME_PATTERN = "INVALID_ASSESSMENT_TARGET_NAME_PATTERN"
    INVALID_ASSESSMENT_TEMPLATE_NAME = "INVALID_ASSESSMENT_TEMPLATE_NAME"
    INVALID_ASSESSMENT_TEMPLATE_NAME_PATTERN = "INVALID_ASSESSMENT_TEMPLATE_NAME_PATTERN"
    INVALID_ASSESSMENT_TEMPLATE_DURATION = "INVALID_ASSESSMENT_TEMPLATE_DURATION"
    INVALID_ASSESSMENT_TEMPLATE_DURATION_RANGE = "INVALID_ASSESSMENT_TEMPLATE_DURATION_RANGE"
    INVALID_ASSESSMENT_RUN_DURATION_RANGE = "INVALID_ASSESSMENT_RUN_DURATION_RANGE"
    INVALID_ASSESSMENT_RUN_START_TIME_RANGE = "INVALID_ASSESSMENT_RUN_START_TIME_RANGE"
    INVALID_ASSESSMENT_RUN_COMPLETION_TIME_RANGE = "INVALID_ASSESSMENT_RUN_COMPLETION_TIME_RANGE"
    INVALID_ASSESSMENT_RUN_STATE_CHANGE_TIME_RANGE = "INVALID_ASSESSMENT_RUN_STATE_CHANGE_TIME_RANGE"
    INVALID_ASSESSMENT_RUN_STATE = "INVALID_ASSESSMENT_RUN_STATE"
    INVALID_TAG = "INVALID_TAG"
    INVALID_TAG_KEY = "INVALID_TAG_KEY"
    INVALID_TAG_VALUE = "INVALID_TAG_VALUE"
    INVALID_RESOURCE_GROUP_TAG_KEY = "INVALID_RESOURCE_GROUP_TAG_KEY"
    INVALID_RESOURCE_GROUP_TAG_VALUE = "INVALID_RESOURCE_GROUP_TAG_VALUE"
    INVALID_ATTRIBUTE = "INVALID_ATTRIBUTE"
    INVALID_USER_ATTRIBUTE = "INVALID_USER_ATTRIBUTE"
    INVALID_USER_ATTRIBUTE_KEY = "INVALID_USER_ATTRIBUTE_KEY"
    INVALID_USER_ATTRIBUTE_VALUE = "INVALID_USER_ATTRIBUTE_VALUE"
    INVALID_PAGINATION_TOKEN = "INVALID_PAGINATION_TOKEN"
    INVALID_MAX_RESULTS = "INVALID_MAX_RESULTS"
    INVALID_AGENT_ID = "INVALID_AGENT_ID"
    INVALID_AUTO_SCALING_GROUP = "INVALID_AUTO_SCALING_GROUP"
    INVALID_RULE_NAME = "INVALID_RULE_NAME"
    INVALID_SEVERITY = "INVALID_SEVERITY"
    INVALID_LOCALE = "INVALID_LOCALE"
    INVALID_EVENT = "INVALID_EVENT"
    ASSESSMENT_TARGET_NAME_ALREADY_TAKEN = "ASSESSMENT_TARGET_NAME_ALREADY_TAKEN"
    ASSESSMENT_TEMPLATE_NAME_ALREADY_TAKEN = "ASSESSMENT_TEMPLATE_NAME_ALREADY_TAKEN"
    INVALID_NUMBER_OF_ASSESSMENT_TARGET_ARNS = "INVALID_NUMBER_OF_ASSESSMENT_TARGET_ARNS"
    INVALID_NUMBER_OF_ASSESSMENT_TEMPLATE_ARNS = "INVALID_NUMBER_OF_ASSESSMENT_TEMPLATE_ARNS"
    INVALID_NUMBER_OF_ASSESSMENT_RUN_ARNS = "INVALID_NUMBER_OF_ASSESSMENT_RUN_ARNS"
    INVALID_NUMBER_OF_FINDING_ARNS = "INVALID_NUMBER_OF_FINDING_ARNS"
    INVALID_NUMBER_OF_RESOURCE_GROUP_ARNS = "INVALID_NUMBER_OF_RESOURCE_GROUP_ARNS"
    INVALID_NUMBER_OF_RULES_PACKAGE_ARNS = "INVALID_NUMBER_OF_RULES_PACKAGE_ARNS"
    INVALID_NUMBER_OF_ASSESSMENT_RUN_STATES = "INVALID_NUMBER_OF_ASSESSMENT_RUN_STATES"
    INVALID_NUMBER_OF_TAGS = "INVALID_NUMBER_OF_TAGS"
    INVALID_NUMBER_OF_RESOURCE_GROUP_TAGS = "INVALID_NUMBER_OF_RESOURCE_GROUP_TAGS"
    INVALID_NUMBER_OF_ATTRIBUTES = "INVALID_NUMBER_OF_ATTRIBUTES"
    INVALID_NUMBER_OF_USER_ATTRIBUTES = "INVALID_NUMBER_OF_USER_ATTRIBUTES"
    INVALID_NUMBER_OF_AGENT_IDS = "INVALID_NUMBER_OF_AGENT_IDS"
    INVALID_NUMBER_OF_AUTO_SCALING_GROUPS = "INVALID_NUMBER_OF_AUTO_SCALING_GROUPS"
    INVALID_NUMBER_OF_RULE_NAMES = "INVALID_NUMBER_OF_RULE_NAMES"
    INVALID_NUMBER_OF_SEVERITIES = "INVALID_NUMBER_OF_SEVERITIES"


@dataclasses.dataclass
class InvalidInputException(ShapeBase):
    """
    The request was rejected because an invalid or out-of-range value was supplied
    for an input parameter.
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
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, InvalidInputErrorCode]),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: typing.Union[str, "InvalidInputErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class LimitExceededErrorCode(str):
    ASSESSMENT_TARGET_LIMIT_EXCEEDED = "ASSESSMENT_TARGET_LIMIT_EXCEEDED"
    ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED = "ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED"
    ASSESSMENT_RUN_LIMIT_EXCEEDED = "ASSESSMENT_RUN_LIMIT_EXCEEDED"
    RESOURCE_GROUP_LIMIT_EXCEEDED = "RESOURCE_GROUP_LIMIT_EXCEEDED"
    EVENT_SUBSCRIPTION_LIMIT_EXCEEDED = "EVENT_SUBSCRIPTION_LIMIT_EXCEEDED"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The request was rejected because it attempted to create resources beyond the
    current AWS account limits. The error code describes the limit exceeded.
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
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, LimitExceededErrorCode]),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: typing.Union[str, "LimitExceededErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunAgentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
            (
                "filter",
                "filter",
                TypeInfo(AgentFilter),
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

    # The ARN that specifies the assessment run whose agents you want to list.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AgentFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentRunAgents**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunAgentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_run_agents",
                "assessmentRunAgents",
                TypeInfo(typing.List[AssessmentRunAgent]),
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

    # A list of ARNs that specifies the agents returned by the action.
    assessment_run_agents: typing.List["AssessmentRunAgent"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAssessmentRunAgentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAssessmentRunsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arns",
                "assessmentTemplateArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "filter",
                "filter",
                TypeInfo(AssessmentRunFilter),
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

    # The ARNs that specify the assessment templates whose assessment runs you
    # want to list.
    assessment_template_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AssessmentRunFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentRuns** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentRunsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_run_arns",
                "assessmentRunArns",
                TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the assessment runs that are returned by the
    # action.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListAssessmentRunsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAssessmentTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                TypeInfo(AssessmentTargetFilter),
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

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AssessmentTargetFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentTargets**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentTargetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_target_arns",
                "assessmentTargetArns",
                TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the assessment targets that are returned by
    # the action.
    assessment_target_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAssessmentTargetsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAssessmentTemplatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arns",
                "assessmentTargetArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "filter",
                "filter",
                TypeInfo(AssessmentTemplateFilter),
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

    # A list of ARNs that specifies the assessment targets whose assessment
    # templates you want to list.
    assessment_target_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "AssessmentTemplateFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListAssessmentTemplates**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAssessmentTemplatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_template_arns",
                "assessmentTemplateArns",
                TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the assessment templates returned by the
    # action.
    assessment_template_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAssessmentTemplatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListEventSubscriptionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
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

    # The ARN of the assessment template for which you want to list the existing
    # event subscriptions.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListEventSubscriptions**
    # action. Subsequent calls to the action fill **nextToken** in the request
    # with the value of **NextToken** from the previous response to continue
    # listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEventSubscriptionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "subscriptions",
                "subscriptions",
                TypeInfo(typing.List[Subscription]),
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

    # Details of the returned event subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListEventSubscriptionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListExclusionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
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

    # The ARN of the assessment run that generated the exclusions that you want
    # to list.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListExclusionsRequest action.
    # Subsequent calls to the action fill nextToken in the request with the value
    # of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 100. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListExclusionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exclusion_arns",
                "exclusionArns",
                TypeInfo(typing.List[str]),
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

    # A list of exclusions' ARNs returned by the action.
    exclusion_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameters is present in the response and contains the value to use for the
    # nextToken parameter in a subsequent pagination request. If there is no more
    # data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFindingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arns",
                "assessmentRunArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "filter",
                "filter",
                TypeInfo(FindingFilter),
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

    # The ARNs of the assessment runs that generate the findings that you want to
    # list.
    assessment_run_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter to specify a subset of data to be included in
    # the action's response.

    # For a record to match a filter, all specified filter attributes must match.
    # When multiple values are specified for a filter attribute, any of the
    # values can match.
    filter: "FindingFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListFindings** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "finding_arns",
                "findingArns",
                TypeInfo(typing.List[str]),
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

    # A list of ARNs that specifies the findings returned by the action.
    finding_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListFindingsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListRulesPackagesRequest(ShapeBase):
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

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **ListRulesPackages** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRulesPackagesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules_package_arns",
                "rulesPackageArns",
                TypeInfo(typing.List[str]),
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

    # The list of ARNs that specifies the rules packages returned by the action.
    rules_package_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListRulesPackagesResponse", None, None]:
        yield from super()._paginate()


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

    # The ARN that specifies the assessment template whose tags you want to list.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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

    # A collection of key and value pairs.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class Locale(str):
    EN_US = "EN_US"


class NoSuchEntityErrorCode(str):
    ASSESSMENT_TARGET_DOES_NOT_EXIST = "ASSESSMENT_TARGET_DOES_NOT_EXIST"
    ASSESSMENT_TEMPLATE_DOES_NOT_EXIST = "ASSESSMENT_TEMPLATE_DOES_NOT_EXIST"
    ASSESSMENT_RUN_DOES_NOT_EXIST = "ASSESSMENT_RUN_DOES_NOT_EXIST"
    FINDING_DOES_NOT_EXIST = "FINDING_DOES_NOT_EXIST"
    RESOURCE_GROUP_DOES_NOT_EXIST = "RESOURCE_GROUP_DOES_NOT_EXIST"
    RULES_PACKAGE_DOES_NOT_EXIST = "RULES_PACKAGE_DOES_NOT_EXIST"
    SNS_TOPIC_DOES_NOT_EXIST = "SNS_TOPIC_DOES_NOT_EXIST"
    IAM_ROLE_DOES_NOT_EXIST = "IAM_ROLE_DOES_NOT_EXIST"


@dataclasses.dataclass
class NoSuchEntityException(ShapeBase):
    """
    The request was rejected because it referenced an entity that does not exist.
    The error code describes the entity.
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
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, NoSuchEntityErrorCode]),
            ),
            (
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Code that indicates the type of error that is generated.
    error_code: typing.Union[str, "NoSuchEntityErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can immediately retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreviewAgentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "preview_agents_arn",
                "previewAgentsArn",
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

    # The ARN of the assessment target whose agents you want to preview.
    preview_agents_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the **PreviewAgents** action.
    # Subsequent calls to the action fill **nextToken** in the request with the
    # value of **NextToken** from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 10. The maximum value is 500.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreviewAgentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "agent_previews",
                "agentPreviews",
                TypeInfo(typing.List[AgentPreview]),
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

    # The resulting list of agents.
    agent_previews: typing.List["AgentPreview"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When a response is generated, if there is more data to be listed, this
    # parameter is present in the response and contains the value to use for the
    # **nextToken** parameter in a subsequent pagination request. If there is no
    # more data to be listed, this parameter is set to null.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["PreviewAgentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class PreviewGenerationInProgressException(ShapeBase):
    """
    The request is rejected. The specified assessment template is currently
    generating an exclusions preview.
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


class PreviewStatus(str):
    WORK_IN_PROGRESS = "WORK_IN_PROGRESS"
    COMPLETED = "COMPLETED"


@dataclasses.dataclass
class RegisterCrossAccountAccessRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the IAM role that grants Amazon Inspector access to AWS Services
    # needed to perform security assessments.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveAttributesFromFindingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finding_arns",
                "findingArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "attribute_keys",
                "attributeKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARNs that specify the findings that you want to remove attributes from.
    finding_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The array of attribute keys that you want to remove from specified
    # findings.
    attribute_keys: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveAttributesFromFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_items",
                "failedItems",
                TypeInfo(typing.Dict[str, FailedItemDetails]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes details that cannot be described. An error code is provided for
    # each failed item.
    failed_items: typing.Dict[str, "FailedItemDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReportFileFormat(str):
    HTML = "HTML"
    PDF = "PDF"


class ReportStatus(str):
    WORK_IN_PROGRESS = "WORK_IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class ReportType(str):
    FINDING = "FINDING"
    FULL = "FULL"


@dataclasses.dataclass
class ResourceGroup(ShapeBase):
    """
    Contains information about a resource group. The resource group defines a set of
    tags that, when queried, identify the AWS resources that make up the assessment
    target. This data type is used as the response element in the
    DescribeResourceGroups action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[ResourceGroupTag]),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The ARN of the resource group.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags (key and value pairs) of the resource group. This data type
    # property is used in the CreateResourceGroup action.
    tags: typing.List["ResourceGroupTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which resource group is created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceGroupTag(ShapeBase):
    """
    This data type is used as one of the elements of the ResourceGroup data type.
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

    # A tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value assigned to a tag key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RulesPackage(ShapeBase):
    """
    Contains information about an Amazon Inspector rules package. This data type is
    used as the response element in the DescribeRulesPackages action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "provider",
                "provider",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The ARN of the rules package.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the rules package.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the rules package.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The provider of the rules package.
    provider: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the rules package.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Scope(ShapeBase):
    """
    This data type contains key-value pairs that identify various Amazon resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(typing.Union[str, ScopeType]),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The type of the scope.
    key: typing.Union[str, "ScopeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource identifier for the specified scope type.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScopeType(str):
    INSTANCE_ID = "INSTANCE_ID"
    RULES_PACKAGE_ARN = "RULES_PACKAGE_ARN"


@dataclasses.dataclass
class ServiceTemporarilyUnavailableException(ShapeBase):
    """
    The serice is temporary unavailable.
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
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    # Details of the exception error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can wait and then retry your request.
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTagsForResourceRequest(ShapeBase):
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

    # The ARN of the assessment template that you want to set tags to.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of key and value pairs that you want to set to the assessment
    # template.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class Severity(str):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Informational = "Informational"
    Undefined = "Undefined"


@dataclasses.dataclass
class StartAssessmentRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_template_arn",
                "assessmentTemplateArn",
                TypeInfo(str),
            ),
            (
                "assessment_run_name",
                "assessmentRunName",
                TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template of the assessment run that you want to
    # start.
    assessment_template_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can specify the name for the assessment run. The name must be unique
    # for the assessment template whose ARN is used to start the assessment run.
    assessment_run_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartAssessmentRunResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the assessment run that has been started.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StopAction(str):
    START_EVALUATION = "START_EVALUATION"
    SKIP_EVALUATION = "SKIP_EVALUATION"


@dataclasses.dataclass
class StopAssessmentRunRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_run_arn",
                "assessmentRunArn",
                TypeInfo(str),
            ),
            (
                "stop_action",
                "stopAction",
                TypeInfo(typing.Union[str, StopAction]),
            ),
        ]

    # The ARN of the assessment run that you want to stop.
    assessment_run_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An input option that can be set to either START_EVALUATION or
    # SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent
    # from collecting data and begins the results evaluation and the findings
    # generation process. SKIP_EVALUATION cancels the assessment run immediately,
    # after which no findings are generated.
    stop_action: typing.Union[str, "StopAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubscribeToEventRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "event",
                "event",
                TypeInfo(typing.Union[str, InspectorEvent]),
            ),
            (
                "topic_arn",
                "topicArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template that is used during the event for which
    # you want to receive SNS notifications.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event for which you want to receive SNS notifications.
    event: typing.Union[str, "InspectorEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the SNS topic to which the SNS notifications are sent.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Subscription(ShapeBase):
    """
    This data type is used as a response element in the ListEventSubscriptions
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "topicArn",
                TypeInfo(str),
            ),
            (
                "event_subscriptions",
                "eventSubscriptions",
                TypeInfo(typing.List[EventSubscription]),
            ),
        ]

    # The ARN of the assessment template that is used during the event for which
    # the SNS notification is sent.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon Simple Notification Service (SNS) topic to which the
    # SNS notifications are sent.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of existing event subscriptions.
    event_subscriptions: typing.List["EventSubscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A key and value pair. This data type is used as a request parameter in the
    SetTagsForResource action and a response element in the ListTagsForResource
    action.
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

    # A tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value assigned to a tag key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TelemetryMetadata(ShapeBase):
    """
    The metadata about the Amazon Inspector application data metrics collected by
    the agent. This data type is used as the response element in the
    GetTelemetryMetadata action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_type",
                "messageType",
                TypeInfo(str),
            ),
            (
                "count",
                "count",
                TypeInfo(int),
            ),
            (
                "data_size",
                "dataSize",
                TypeInfo(int),
            ),
        ]

    # A specific type of behavioral data that is collected by the agent.
    message_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The count of messages that the agent sends to the Amazon Inspector service.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data size of messages that the agent sends to the Amazon Inspector
    # service.
    data_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimestampRange(ShapeBase):
    """
    This data type is used in the AssessmentRunFilter data type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "begin_date",
                "beginDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date",
                "endDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The minimum value of the timestamp range.
    begin_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum value of the timestamp range.
    end_date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsubscribeFromEventRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "event",
                "event",
                TypeInfo(typing.Union[str, InspectorEvent]),
            ),
            (
                "topic_arn",
                "topicArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the assessment template that is used during the event for which
    # you want to stop receiving SNS notifications.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event for which you want to stop receiving SNS notifications.
    event: typing.Union[str, "InspectorEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the SNS topic to which SNS notifications are sent.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedFeatureException(ShapeBase):
    """
    Used by the GetAssessmentReport API. The request was rejected because you tried
    to generate a report for an assessment run that existed before reporting was
    supported in Amazon Inspector. You can only generate reports for assessment runs
    that took place or will take place after generating reports in Amazon Inspector
    became available.
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
                "can_retry",
                "canRetry",
                TypeInfo(bool),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    can_retry: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAssessmentTargetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "assessment_target_arn",
                "assessmentTargetArn",
                TypeInfo(str),
            ),
            (
                "assessment_target_name",
                "assessmentTargetName",
                TypeInfo(str),
            ),
            (
                "resource_group_arn",
                "resourceGroupArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the assessment target that you want to update.
    assessment_target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the assessment target that you want to update.
    assessment_target_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the resource group that is used to specify the new resource
    # group to associate with the assessment target.
    resource_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
