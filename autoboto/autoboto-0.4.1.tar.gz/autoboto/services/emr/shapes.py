import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class ActionOnFailure(str):
    TERMINATE_JOB_FLOW = "TERMINATE_JOB_FLOW"
    TERMINATE_CLUSTER = "TERMINATE_CLUSTER"
    CANCEL_AND_WAIT = "CANCEL_AND_WAIT"
    CONTINUE = "CONTINUE"


@dataclasses.dataclass
class AddInstanceFleetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_fleet",
                "InstanceFleet",
                TypeInfo(InstanceFleetConfig),
            ),
        ]

    # The unique identifier of the cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the configuration of the instance fleet.
    instance_fleet: "InstanceFleetConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddInstanceFleetOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_fleet_id",
                "InstanceFleetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the instance fleet.
    instance_fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddInstanceGroupsInput(ShapeBase):
    """
    Input to an AddInstanceGroups call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_groups",
                "InstanceGroups",
                TypeInfo(typing.List[InstanceGroupConfig]),
            ),
            (
                "job_flow_id",
                "JobFlowId",
                TypeInfo(str),
            ),
        ]

    # Instance groups to add.
    instance_groups: typing.List["InstanceGroupConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Job flow in which to add the instance groups.
    job_flow_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddInstanceGroupsOutput(OutputShapeBase):
    """
    Output from an AddInstanceGroups call.
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
                "job_flow_id",
                "JobFlowId",
                TypeInfo(str),
            ),
            (
                "instance_group_ids",
                "InstanceGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The job flow ID in which the instance groups are added.
    job_flow_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Instance group IDs of the newly created instance groups.
    instance_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddJobFlowStepsInput(ShapeBase):
    """
    The input argument to the AddJobFlowSteps operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_flow_id",
                "JobFlowId",
                TypeInfo(str),
            ),
            (
                "steps",
                "Steps",
                TypeInfo(typing.List[StepConfig]),
            ),
        ]

    # A string that uniquely identifies the job flow. This identifier is returned
    # by RunJobFlow and can also be obtained from ListClusters.
    job_flow_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of StepConfig to be executed by the job flow.
    steps: typing.List["StepConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddJobFlowStepsOutput(OutputShapeBase):
    """
    The output for the AddJobFlowSteps operation.
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
                "step_ids",
                "StepIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifiers of the list of steps added to the job flow.
    step_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsInput(ShapeBase):
    """
    This input identifies a cluster and a list of tags to attach.
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
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon EMR resource identifier to which tags will be added. This value
    # must be a cluster identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to associate with a cluster and propagate to EC2 instances.
    # Tags are user-defined key/value pairs that consist of a required key string
    # with a maximum of 128 characters, and an optional value string with a
    # maximum of 256 characters.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsOutput(OutputShapeBase):
    """
    This output indicates the result of adding tags to a resource.
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


class AdjustmentType(str):
    CHANGE_IN_CAPACITY = "CHANGE_IN_CAPACITY"
    PERCENT_CHANGE_IN_CAPACITY = "PERCENT_CHANGE_IN_CAPACITY"
    EXACT_CAPACITY = "EXACT_CAPACITY"


@dataclasses.dataclass
class Application(ShapeBase):
    """
    An application is any Amazon or third-party software that you can add to the
    cluster. This structure contains a list of strings that indicates the software
    to use with the cluster and accepts a user argument list. Amazon EMR accepts and
    forwards the argument list to the corresponding installation script as bootstrap
    action argument. For more information, see [Using the MapR Distribution for
    Hadoop](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-mapr.html).
    Currently supported values are:

      * "mapr-m3" - launch the cluster using MapR M3 Edition.

      * "mapr-m5" - launch the cluster using MapR M5 Edition.

      * "mapr" with the user arguments specifying "--edition,m3" or "--edition,m5" - launch the cluster using MapR M3 or M5 Edition, respectively.

    In Amazon EMR releases 4.x and later, the only accepted parameter is the
    application name. To pass arguments to applications, you supply a configuration
    for each application.
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
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "args",
                "Args",
                TypeInfo(typing.List[str]),
            ),
            (
                "additional_info",
                "AdditionalInfo",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the application.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the application.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Arguments for Amazon EMR to pass to the application.
    args: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This option is for advanced users only. This is meta information about
    # third-party applications that third-party vendors use for testing purposes.
    additional_info: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingPolicy(ShapeBase):
    """
    An automatic scaling policy for a core instance group or task instance group in
    an Amazon EMR cluster. An automatic scaling policy defines how an instance group
    dynamically adds and terminates EC2 instances in response to the value of a
    CloudWatch metric. See PutAutoScalingPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "constraints",
                "Constraints",
                TypeInfo(ScalingConstraints),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[ScalingRule]),
            ),
        ]

    # The upper and lower EC2 instance limits for an automatic scaling policy.
    # Automatic scaling activity will not cause an instance group to grow above
    # or below these limits.
    constraints: "ScalingConstraints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scale-in and scale-out rules that comprise the automatic scaling
    # policy.
    rules: typing.List["ScalingRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingPolicyDescription(ShapeBase):
    """
    An automatic scaling policy for a core instance group or task instance group in
    an Amazon EMR cluster. The automatic scaling policy defines how an instance
    group dynamically adds and terminates EC2 instances in response to the value of
    a CloudWatch metric. See PutAutoScalingPolicy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(AutoScalingPolicyStatus),
            ),
            (
                "constraints",
                "Constraints",
                TypeInfo(ScalingConstraints),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[ScalingRule]),
            ),
        ]

    # The status of an automatic scaling policy.
    status: "AutoScalingPolicyStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upper and lower EC2 instance limits for an automatic scaling policy.
    # Automatic scaling activity will not cause an instance group to grow above
    # or below these limits.
    constraints: "ScalingConstraints" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scale-in and scale-out rules that comprise the automatic scaling
    # policy.
    rules: typing.List["ScalingRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AutoScalingPolicyState(str):
    PENDING = "PENDING"
    ATTACHING = "ATTACHING"
    ATTACHED = "ATTACHED"
    DETACHING = "DETACHING"
    DETACHED = "DETACHED"
    FAILED = "FAILED"


@dataclasses.dataclass
class AutoScalingPolicyStateChangeReason(ShapeBase):
    """
    The reason for an AutoScalingPolicyStatus change.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(
                    typing.Union[str, AutoScalingPolicyStateChangeReasonCode]
                ),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The code indicating the reason for the change in status.`USER_REQUEST`
    # indicates that the scaling policy status was changed by a user.
    # `PROVISION_FAILURE` indicates that the status change was because the policy
    # failed to provision. `CLEANUP_FAILURE` indicates an error.
    code: typing.Union[str, "AutoScalingPolicyStateChangeReasonCode"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # A friendly, more verbose message that accompanies an automatic scaling
    # policy state change.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AutoScalingPolicyStateChangeReasonCode(str):
    USER_REQUEST = "USER_REQUEST"
    PROVISION_FAILURE = "PROVISION_FAILURE"
    CLEANUP_FAILURE = "CLEANUP_FAILURE"


@dataclasses.dataclass
class AutoScalingPolicyStatus(ShapeBase):
    """
    The status of an automatic scaling policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, AutoScalingPolicyState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(AutoScalingPolicyStateChangeReason),
            ),
        ]

    # Indicates the status of the automatic scaling policy.
    state: typing.Union[str, "AutoScalingPolicyState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for a change in status.
    state_change_reason: "AutoScalingPolicyStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BootstrapActionConfig(ShapeBase):
    """
    Configuration of a bootstrap action.
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
                "script_bootstrap_action",
                "ScriptBootstrapAction",
                TypeInfo(ScriptBootstrapActionConfig),
            ),
        ]

    # The name of the bootstrap action.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The script run by the bootstrap action.
    script_bootstrap_action: "ScriptBootstrapActionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BootstrapActionDetail(ShapeBase):
    """
    Reports the configuration of a bootstrap action in a cluster (job flow).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bootstrap_action_config",
                "BootstrapActionConfig",
                TypeInfo(BootstrapActionConfig),
            ),
        ]

    # A description of the bootstrap action.
    bootstrap_action_config: "BootstrapActionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CancelStepsInfo(ShapeBase):
    """
    Specification of the status of a CancelSteps request. Available only in Amazon
    EMR version 4.8.0 and later, excluding version 5.0.0.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "step_id",
                "StepId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CancelStepsRequestStatus]),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(str),
            ),
        ]

    # The encrypted StepId of a step.
    step_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a CancelSteps Request. The value may be SUBMITTED or FAILED.
    status: typing.Union[str, "CancelStepsRequestStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the failure if the CancelSteps request fails.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelStepsInput(ShapeBase):
    """
    The input argument to the CancelSteps operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "step_ids",
                "StepIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The `ClusterID` for which specified steps will be canceled. Use RunJobFlow
    # and ListClusters to get ClusterIDs.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of `StepIDs` to cancel. Use ListSteps to get steps and their
    # states for the specified cluster.
    step_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelStepsOutput(OutputShapeBase):
    """
    The output for the CancelSteps operation.
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
                "cancel_steps_info_list",
                "CancelStepsInfoList",
                TypeInfo(typing.List[CancelStepsInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of CancelStepsInfo, which shows the status of specified cancel
    # requests for each `StepID` specified.
    cancel_steps_info_list: typing.List["CancelStepsInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CancelStepsRequestStatus(str):
    SUBMITTED = "SUBMITTED"
    FAILED = "FAILED"


@dataclasses.dataclass
class CloudWatchAlarmDefinition(ShapeBase):
    """
    The definition of a CloudWatch metric alarm, which determines when an automatic
    scaling activity is triggered. When the defined alarm conditions are satisfied,
    scaling activity begins.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperator]),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "period",
                "Period",
                TypeInfo(int),
            ),
            (
                "threshold",
                "Threshold",
                TypeInfo(float),
            ),
            (
                "evaluation_periods",
                "EvaluationPeriods",
                TypeInfo(int),
            ),
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "statistic",
                "Statistic",
                TypeInfo(typing.Union[str, Statistic]),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, Unit]),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[MetricDimension]),
            ),
        ]

    # Determines how the metric specified by `MetricName` is compared to the
    # value specified by `Threshold`.
    comparison_operator: typing.Union[str, "ComparisonOperator"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The name of the CloudWatch metric that is watched to determine an alarm
    # condition.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The period, in seconds, over which the statistic is applied. EMR CloudWatch
    # metrics are emitted every five minutes (300 seconds), so if an EMR
    # CloudWatch metric is specified, specify `300`.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value against which the specified statistic is compared.
    threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of periods, expressed in seconds using `Period`, during which
    # the alarm condition must exist before the alarm triggers automatic scaling
    # activity. The default value is `1`.
    evaluation_periods: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace for the CloudWatch metric. The default is
    # `AWS/ElasticMapReduce`.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistic to apply to the metric associated with the alarm. The default
    # is `AVERAGE`.
    statistic: typing.Union[str, "Statistic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unit of measure associated with the CloudWatch metric being watched.
    # The value specified for `Unit` must correspond to the units specified in
    # the CloudWatch metric.
    unit: typing.Union[str, "Unit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A CloudWatch metric dimension.
    dimensions: typing.List["MetricDimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Cluster(ShapeBase):
    """
    The detailed description of the cluster.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(ClusterStatus),
            ),
            (
                "ec2_instance_attributes",
                "Ec2InstanceAttributes",
                TypeInfo(Ec2InstanceAttributes),
            ),
            (
                "instance_collection_type",
                "InstanceCollectionType",
                TypeInfo(typing.Union[str, InstanceCollectionType]),
            ),
            (
                "log_uri",
                "LogUri",
                TypeInfo(str),
            ),
            (
                "requested_ami_version",
                "RequestedAmiVersion",
                TypeInfo(str),
            ),
            (
                "running_ami_version",
                "RunningAmiVersion",
                TypeInfo(str),
            ),
            (
                "release_label",
                "ReleaseLabel",
                TypeInfo(str),
            ),
            (
                "auto_terminate",
                "AutoTerminate",
                TypeInfo(bool),
            ),
            (
                "termination_protected",
                "TerminationProtected",
                TypeInfo(bool),
            ),
            (
                "visible_to_all_users",
                "VisibleToAllUsers",
                TypeInfo(bool),
            ),
            (
                "applications",
                "Applications",
                TypeInfo(typing.List[Application]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "normalized_instance_hours",
                "NormalizedInstanceHours",
                TypeInfo(int),
            ),
            (
                "master_public_dns_name",
                "MasterPublicDnsName",
                TypeInfo(str),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
            (
                "auto_scaling_role",
                "AutoScalingRole",
                TypeInfo(str),
            ),
            (
                "scale_down_behavior",
                "ScaleDownBehavior",
                TypeInfo(typing.Union[str, ScaleDownBehavior]),
            ),
            (
                "custom_ami_id",
                "CustomAmiId",
                TypeInfo(str),
            ),
            (
                "ebs_root_volume_size",
                "EbsRootVolumeSize",
                TypeInfo(int),
            ),
            (
                "repo_upgrade_on_boot",
                "RepoUpgradeOnBoot",
                TypeInfo(typing.Union[str, RepoUpgradeOnBoot]),
            ),
            (
                "kerberos_attributes",
                "KerberosAttributes",
                TypeInfo(KerberosAttributes),
            ),
        ]

    # The unique identifier for the cluster.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status details about the cluster.
    status: "ClusterStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides information about the EC2 instances in a cluster grouped by
    # category. For example, key name, subnet ID, IAM instance profile, and so
    # on.
    ec2_instance_attributes: "Ec2InstanceAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance fleet configuration is available only in Amazon EMR versions
    # 4.8.0 and later, excluding 5.0.x versions.

    # The instance group configuration of the cluster. A value of
    # `INSTANCE_GROUP` indicates a uniform instance group configuration. A value
    # of `INSTANCE_FLEET` indicates an instance fleets configuration.
    instance_collection_type: typing.Union[str, "InstanceCollectionType"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The path to the Amazon S3 location where logs for this cluster are stored.
    log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AMI version requested for this cluster.
    requested_ami_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AMI version running on this cluster.
    running_ami_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EMR release label, which determines the version of open-source
    # application packages installed on the cluster. Release labels are in the
    # form `emr-x.x.x`, where x.x.x is an Amazon EMR release version, for
    # example, `emr-5.14.0`. For more information about Amazon EMR release
    # versions and included application versions and features, see
    # <http://docs.aws.amazon.com/emr/latest/ReleaseGuide/>. The release label
    # applies only to Amazon EMR releases versions 4.x and later. Earlier
    # versions use `AmiVersion`.
    release_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the cluster should terminate after completing all steps.
    auto_terminate: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether Amazon EMR will lock the cluster to prevent the EC2
    # instances from being terminated by an API call or user intervention, or in
    # the event of a cluster error.
    termination_protected: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the cluster is visible to all IAM users of the AWS
    # account associated with the cluster. If this value is set to `true`, all
    # IAM users of that AWS account can view and manage the cluster if they have
    # the proper policy permissions set. If this value is `false`, only the IAM
    # user that created the cluster can view and manage it. This value can be
    # changed using the SetVisibleToAllUsers action.
    visible_to_all_users: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The applications installed on this cluster.
    applications: typing.List["Application"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags associated with a cluster.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that will be assumed by the Amazon EMR service to access AWS
    # resources on your behalf.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An approximation of the cost of the cluster, represented in m1.small/hours.
    # This value is incremented one time for every hour an m1.small instance
    # runs. Larger instances are weighted more, so an EC2 instance that is
    # roughly four times more expensive would result in the normalized instance
    # hours being incremented by four. This result is only an approximation and
    # does not reflect the actual billing rate.
    normalized_instance_hours: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DNS name of the master node. If the cluster is on a private subnet,
    # this is the private DNS name. On a public subnet, this is the public DNS
    # name.
    master_public_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only to Amazon EMR releases 4.x and later. The list of
    # Configurations supplied to the EMR cluster.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the security configuration applied to the cluster.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM role for automatic scaling policies. The default role is
    # `EMR_AutoScaling_DefaultRole`. The IAM role provides permissions that the
    # automatic scaling feature requires to launch and terminate EC2 instances in
    # an instance group.
    auto_scaling_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The way that individual Amazon EC2 instances terminate when an automatic
    # scale-in activity occurs or an instance group is resized.
    # `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at
    # the instance-hour boundary, regardless of when the request to terminate the
    # instance was submitted. This option is only available with Amazon EMR 5.1.0
    # and later and is the default for clusters created using that version.
    # `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR blacklists and
    # drains tasks from nodes before terminating the Amazon EC2 instances,
    # regardless of the instance-hour boundary. With either behavior, Amazon EMR
    # removes the least active nodes first and blocks instance termination if it
    # could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` is available
    # only in Amazon EMR version 4.1.0 and later, and is the default for versions
    # of Amazon EMR earlier than 5.1.0.
    scale_down_behavior: typing.Union[str, "ScaleDownBehavior"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Available only in Amazon EMR version 5.7.0 and later. The ID of a custom
    # Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.
    custom_ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in GiB, of the EBS root device volume of the Linux AMI that is
    # used for each EC2 instance. Available in Amazon EMR version 4.x and later.
    ebs_root_volume_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only when `CustomAmiID` is used. Specifies the type of updates that
    # are applied from the Amazon Linux AMI package repositories when an instance
    # boots using the AMI.
    repo_upgrade_on_boot: typing.Union[str, "RepoUpgradeOnBoot"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Attributes for Kerberos configuration when Kerberos authentication is
    # enabled using a security configuration. For more information see [Use
    # Kerberos
    # Authentication](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-
    # kerberos.html) in the _EMR Management Guide_.
    kerberos_attributes: "KerberosAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ClusterState(str):
    STARTING = "STARTING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    TERMINATED_WITH_ERRORS = "TERMINATED_WITH_ERRORS"


@dataclasses.dataclass
class ClusterStateChangeReason(ShapeBase):
    """
    The reason that the cluster changed to its current state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, ClusterStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The programmatic code for the state change reason.
    code: typing.Union[str, "ClusterStateChangeReasonCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The descriptive message for the state change reason.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ClusterStateChangeReasonCode(str):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    INSTANCE_FLEET_TIMEOUT = "INSTANCE_FLEET_TIMEOUT"
    BOOTSTRAP_FAILURE = "BOOTSTRAP_FAILURE"
    USER_REQUEST = "USER_REQUEST"
    STEP_FAILURE = "STEP_FAILURE"
    ALL_STEPS_COMPLETED = "ALL_STEPS_COMPLETED"


@dataclasses.dataclass
class ClusterStatus(ShapeBase):
    """
    The detailed status of the cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ClusterState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(ClusterStateChangeReason),
            ),
            (
                "timeline",
                "Timeline",
                TypeInfo(ClusterTimeline),
            ),
        ]

    # The current state of the cluster.
    state: typing.Union[str, "ClusterState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the cluster status change.
    state_change_reason: "ClusterStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timeline that represents the status of a cluster over the lifetime of the
    # cluster.
    timeline: "ClusterTimeline" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterSummary(ShapeBase):
    """
    The summary description of the cluster.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(ClusterStatus),
            ),
            (
                "normalized_instance_hours",
                "NormalizedInstanceHours",
                TypeInfo(int),
            ),
        ]

    # The unique identifier for the cluster.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The details about the current status of the cluster.
    status: "ClusterStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An approximation of the cost of the cluster, represented in m1.small/hours.
    # This value is incremented one time for every hour an m1.small instance
    # runs. Larger instances are weighted more, so an EC2 instance that is
    # roughly four times more expensive would result in the normalized instance
    # hours being incremented by four. This result is only an approximation and
    # does not reflect the actual billing rate.
    normalized_instance_hours: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterTimeline(ShapeBase):
    """
    Represents the timeline of the cluster's lifecycle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ready_date_time",
                "ReadyDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The creation date and time of the cluster.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the cluster was ready to execute steps.
    ready_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the cluster was terminated.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Command(ShapeBase):
    """
    An entity describing an executable that runs on a cluster.
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
                "script_path",
                "ScriptPath",
                TypeInfo(str),
            ),
            (
                "args",
                "Args",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the command.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 location of the command script.
    script_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Arguments for Amazon EMR to pass to the command for execution.
    args: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ComparisonOperator(str):
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"


@dataclasses.dataclass
class Configuration(ShapeBase):
    """
    Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster
    instances, which can include configurations for applications and software
    bundled with Amazon EMR. A configuration consists of a classification,
    properties, and optional nested configurations. A classification refers to an
    application-specific configuration file. Properties are the settings you want to
    change in that file. For more information, see [Configuring
    Applications](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-
    apps.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "classification",
                "Classification",
                TypeInfo(str),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
            (
                "properties",
                "Properties",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The classification within a configuration.
    classification: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of additional configurations to apply within a configuration object.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of properties specified within a configuration classification.
    properties: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSecurityConfigurationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
        ]

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security configuration details in JSON format. For JSON parameters and
    # examples, see [Use Security Configurations to Set Up Cluster
    # Security](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-
    # security-configurations.html) in the _Amazon EMR Management Guide_.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSecurityConfigurationOutput(OutputShapeBase):
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
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the security configuration was created.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSecurityConfigurationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSecurityConfigurationOutput(OutputShapeBase):
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
class DescribeClusterInput(ShapeBase):
    """
    This input determines which cluster to describe.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster to describe.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterOutput(OutputShapeBase):
    """
    This output contains the description of the cluster.
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
                "cluster",
                "Cluster",
                TypeInfo(Cluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This output contains the details for the requested cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobFlowsInput(ShapeBase):
    """
    The input for the DescribeJobFlows operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_after",
                "CreatedAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_before",
                "CreatedBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "job_flow_ids",
                "JobFlowIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "job_flow_states",
                "JobFlowStates",
                TypeInfo(typing.List[typing.Union[str, JobFlowExecutionState]]),
            ),
        ]

    # Return only job flows created after this date and time.
    created_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return only job flows created before this date and time.
    created_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return only job flows whose job flow ID is contained in this list.
    job_flow_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return only job flows whose state is contained in this list.
    job_flow_states: typing.List[typing.Union[str, "JobFlowExecutionState"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class DescribeJobFlowsOutput(OutputShapeBase):
    """
    The output for the DescribeJobFlows operation.
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
                "job_flows",
                "JobFlows",
                TypeInfo(typing.List[JobFlowDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of job flows matching the parameters supplied.
    job_flows: typing.List["JobFlowDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSecurityConfigurationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSecurityConfigurationOutput(OutputShapeBase):
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
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security configuration details in JSON format.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the security configuration was created
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStepInput(ShapeBase):
    """
    This input determines which step to describe.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "step_id",
                "StepId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster with steps to describe.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the step to describe.
    step_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStepOutput(OutputShapeBase):
    """
    This output contains the description of the cluster step.
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
                "step",
                "Step",
                TypeInfo(Step),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The step details for the requested step identifier.
    step: "Step" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EbsBlockDevice(ShapeBase):
    """
    Configuration of requested EBS block device associated with the instance group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_specification",
                "VolumeSpecification",
                TypeInfo(VolumeSpecification),
            ),
            (
                "device",
                "Device",
                TypeInfo(str),
            ),
        ]

    # EBS volume specifications such as volume type, IOPS, and size (GiB) that
    # will be requested for the EBS volume attached to an EC2 instance in the
    # cluster.
    volume_specification: "VolumeSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device name that is exposed to the instance, such as /dev/sdh.
    device: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EbsBlockDeviceConfig(ShapeBase):
    """
    Configuration of requested EBS block device associated with the instance group
    with count of volumes that will be associated to every instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_specification",
                "VolumeSpecification",
                TypeInfo(VolumeSpecification),
            ),
            (
                "volumes_per_instance",
                "VolumesPerInstance",
                TypeInfo(int),
            ),
        ]

    # EBS volume specifications such as volume type, IOPS, and size (GiB) that
    # will be requested for the EBS volume attached to an EC2 instance in the
    # cluster.
    volume_specification: "VolumeSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of EBS volumes with a specific volume configuration that will be
    # associated with every instance in the instance group
    volumes_per_instance: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EbsConfiguration(ShapeBase):
    """
    The Amazon EBS configuration of a cluster instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ebs_block_device_configs",
                "EbsBlockDeviceConfigs",
                TypeInfo(typing.List[EbsBlockDeviceConfig]),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                TypeInfo(bool),
            ),
        ]

    # An array of Amazon EBS volume specifications attached to a cluster
    # instance.
    ebs_block_device_configs: typing.List["EbsBlockDeviceConfig"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Indicates whether an Amazon EBS volume is EBS-optimized.
    ebs_optimized: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EbsVolume(ShapeBase):
    """
    EBS block device that's attached to an EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device",
                "Device",
                TypeInfo(str),
            ),
            (
                "volume_id",
                "VolumeId",
                TypeInfo(str),
            ),
        ]

    # The device name that is exposed to the instance, such as /dev/sdh.
    device: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The volume identifier of the EBS volume.
    volume_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Ec2InstanceAttributes(ShapeBase):
    """
    Provides information about the EC2 instances in a cluster grouped by category.
    For example, key name, subnet ID, IAM instance profile, and so on.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ec2_key_name",
                "Ec2KeyName",
                TypeInfo(str),
            ),
            (
                "ec2_subnet_id",
                "Ec2SubnetId",
                TypeInfo(str),
            ),
            (
                "requested_ec2_subnet_ids",
                "RequestedEc2SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "ec2_availability_zone",
                "Ec2AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "requested_ec2_availability_zones",
                "RequestedEc2AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "iam_instance_profile",
                "IamInstanceProfile",
                TypeInfo(str),
            ),
            (
                "emr_managed_master_security_group",
                "EmrManagedMasterSecurityGroup",
                TypeInfo(str),
            ),
            (
                "emr_managed_slave_security_group",
                "EmrManagedSlaveSecurityGroup",
                TypeInfo(str),
            ),
            (
                "service_access_security_group",
                "ServiceAccessSecurityGroup",
                TypeInfo(str),
            ),
            (
                "additional_master_security_groups",
                "AdditionalMasterSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "additional_slave_security_groups",
                "AdditionalSlaveSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Amazon EC2 key pair to use when connecting with SSH into
    # the master node as a user named "hadoop".
    ec2_key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To launch the cluster in Amazon VPC, set this parameter to the identifier
    # of the Amazon VPC subnet where you want the cluster to launch. If you do
    # not specify this value, the cluster is launched in the normal AWS cloud,
    # outside of a VPC.

    # Amazon VPC currently does not support cluster compute quadruple extra large
    # (cc1.4xlarge) instances. Thus, you cannot specify the cc1.4xlarge instance
    # type for nodes of a cluster launched in a VPC.
    ec2_subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies to clusters configured with the instance fleets option. Specifies
    # the unique identifier of one or more Amazon EC2 subnets in which to launch
    # EC2 cluster instances. Subnets must exist within the same VPC. Amazon EMR
    # chooses the EC2 subnet with the best fit from among the list of
    # `RequestedEc2SubnetIds`, and then launches all cluster instances within
    # that Subnet. If this value is not specified, and the account and region
    # support EC2-Classic networks, the cluster launches instances in the
    # EC2-Classic network and uses `RequestedEc2AvailabilityZones` instead of
    # this setting. If EC2-Classic is not supported, and no Subnet is specified,
    # Amazon EMR chooses the subnet for you. `RequestedEc2SubnetIDs` and
    # `RequestedEc2AvailabilityZones` cannot be specified together.
    requested_ec2_subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zone in which the cluster will run.
    ec2_availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies to clusters configured with the instance fleets option. Specifies
    # one or more Availability Zones in which to launch EC2 cluster instances
    # when the EC2-Classic network configuration is supported. Amazon EMR chooses
    # the Availability Zone with the best fit from among the list of
    # `RequestedEc2AvailabilityZones`, and then launches all cluster instances
    # within that Availability Zone. If you do not specify this value, Amazon EMR
    # chooses the Availability Zone for you. `RequestedEc2SubnetIDs` and
    # `RequestedEc2AvailabilityZones` cannot be specified together.
    requested_ec2_availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM role that was specified when the cluster was launched. The EC2
    # instances of the cluster assume this role.
    iam_instance_profile: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the Amazon EC2 security group for the master node.
    emr_managed_master_security_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Amazon EC2 security group for the slave nodes.
    emr_managed_slave_security_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Amazon EC2 security group for the Amazon EMR service
    # to access clusters in VPC private subnets.
    service_access_security_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of additional Amazon EC2 security group IDs for the master node.
    additional_master_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of additional Amazon EC2 security group IDs for the slave nodes.
    additional_slave_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailureDetails(ShapeBase):
    """
    The details of the step failure. The service attempts to detect the root cause
    for many common failures.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reason",
                "Reason",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "log_file",
                "LogFile",
                TypeInfo(str),
            ),
        ]

    # The reason for the step failure. In the case where the service cannot
    # successfully determine the root cause of the failure, it returns "Unknown
    # Error" as a reason.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The descriptive message including the error the EMR service has identified
    # as the cause of step failure. This is text from an error log that describes
    # the root cause of the failure.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the log file where the step failure root cause was originally
    # recorded.
    log_file: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HadoopJarStepConfig(ShapeBase):
    """
    A job flow step consisting of a JAR file whose main function will be executed.
    The main function submits a job for Hadoop to execute and waits for the job to
    finish or fail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jar",
                "Jar",
                TypeInfo(str),
            ),
            (
                "properties",
                "Properties",
                TypeInfo(typing.List[KeyValue]),
            ),
            (
                "main_class",
                "MainClass",
                TypeInfo(str),
            ),
            (
                "args",
                "Args",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A path to a JAR file run during the step.
    jar: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Java properties that are set when the step runs. You can use
    # these properties to pass key value pairs to your main function.
    properties: typing.List["KeyValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the main class in the specified Java file. If not specified,
    # the JAR file should specify a Main-Class in its manifest file.
    main_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of command line arguments passed to the JAR file's main function
    # when executed.
    args: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HadoopStepConfig(ShapeBase):
    """
    A cluster step consisting of a JAR file whose main function will be executed.
    The main function submits a job for Hadoop to execute and waits for the job to
    finish or fail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jar",
                "Jar",
                TypeInfo(str),
            ),
            (
                "properties",
                "Properties",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "main_class",
                "MainClass",
                TypeInfo(str),
            ),
            (
                "args",
                "Args",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The path to the JAR file that runs during the step.
    jar: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of Java properties that are set when the step runs. You can use
    # these properties to pass key value pairs to your main function.
    properties: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the main class in the specified Java file. If not specified,
    # the JAR file should specify a main class in its manifest file.
    main_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of command line arguments to pass to the JAR file's main function
    # for execution.
    args: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Instance(ShapeBase):
    """
    Represents an EC2 instance provisioned as part of cluster.
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
                "ec2_instance_id",
                "Ec2InstanceId",
                TypeInfo(str),
            ),
            (
                "public_dns_name",
                "PublicDnsName",
                TypeInfo(str),
            ),
            (
                "public_ip_address",
                "PublicIpAddress",
                TypeInfo(str),
            ),
            (
                "private_dns_name",
                "PrivateDnsName",
                TypeInfo(str),
            ),
            (
                "private_ip_address",
                "PrivateIpAddress",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(InstanceStatus),
            ),
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
            (
                "instance_fleet_id",
                "InstanceFleetId",
                TypeInfo(str),
            ),
            (
                "market",
                "Market",
                TypeInfo(typing.Union[str, MarketType]),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "ebs_volumes",
                "EbsVolumes",
                TypeInfo(typing.List[EbsVolume]),
            ),
        ]

    # The unique identifier for the instance in Amazon EMR.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the instance in Amazon EC2.
    ec2_instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public DNS name of the instance.
    public_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public IP address of the instance.
    public_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private DNS name of the instance.
    private_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private IP address of the instance.
    private_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the instance.
    status: "InstanceStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the instance group to which this instance belongs.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the instance fleet to which an EC2 instance
    # belongs.
    instance_fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance purchasing option. Valid values are `ON_DEMAND` or `SPOT`.
    market: typing.Union[str, "MarketType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 instance type, for example `m3.xlarge`.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of EBS volumes that are attached to this instance.
    ebs_volumes: typing.List["EbsVolume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceCollectionType(str):
    INSTANCE_FLEET = "INSTANCE_FLEET"
    INSTANCE_GROUP = "INSTANCE_GROUP"


@dataclasses.dataclass
class InstanceFleet(ShapeBase):
    """
    Describes an instance fleet, which is a group of EC2 instances that host a
    particular node type (master, core, or task) in an Amazon EMR cluster. Instance
    fleets can consist of a mix of instance types and On-Demand and Spot instances,
    which are provisioned to meet a defined target capacity.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(InstanceFleetStatus),
            ),
            (
                "instance_fleet_type",
                "InstanceFleetType",
                TypeInfo(typing.Union[str, InstanceFleetType]),
            ),
            (
                "target_on_demand_capacity",
                "TargetOnDemandCapacity",
                TypeInfo(int),
            ),
            (
                "target_spot_capacity",
                "TargetSpotCapacity",
                TypeInfo(int),
            ),
            (
                "provisioned_on_demand_capacity",
                "ProvisionedOnDemandCapacity",
                TypeInfo(int),
            ),
            (
                "provisioned_spot_capacity",
                "ProvisionedSpotCapacity",
                TypeInfo(int),
            ),
            (
                "instance_type_specifications",
                "InstanceTypeSpecifications",
                TypeInfo(typing.List[InstanceTypeSpecification]),
            ),
            (
                "launch_specifications",
                "LaunchSpecifications",
                TypeInfo(InstanceFleetProvisioningSpecifications),
            ),
        ]

    # The unique identifier of the instance fleet.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly name for the instance fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the instance fleet.
    status: "InstanceFleetStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The node type that the instance fleet hosts. Valid values are MASTER, CORE,
    # or TASK.
    instance_fleet_type: typing.Union[str, "InstanceFleetType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The target capacity of On-Demand units for the instance fleet, which
    # determines how many On-Demand instances to provision. When the instance
    # fleet launches, Amazon EMR tries to provision On-Demand instances as
    # specified by InstanceTypeConfig. Each instance configuration has a
    # specified `WeightedCapacity`. When an On-Demand instance is provisioned,
    # the `WeightedCapacity` units count toward the target capacity. Amazon EMR
    # provisions instances until the target capacity is totally fulfilled, even
    # if this results in an overage. For example, if there are 2 units remaining
    # to fulfill capacity, and Amazon EMR can only provision an instance with a
    # `WeightedCapacity` of 5 units, the instance is provisioned, and the target
    # capacity is exceeded by 3 units. You can use
    # InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity
    # units that have been provisioned for the instance fleet.

    # If not specified or set to 0, only Spot instances are provisioned for the
    # instance fleet using `TargetSpotCapacity`. At least one of
    # `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0.
    # For a master instance fleet, only one of `TargetSpotCapacity` and
    # `TargetOnDemandCapacity` can be specified, and its value must be 1.
    target_on_demand_capacity: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target capacity of Spot units for the instance fleet, which determines
    # how many Spot instances to provision. When the instance fleet launches,
    # Amazon EMR tries to provision Spot instances as specified by
    # InstanceTypeConfig. Each instance configuration has a specified
    # `WeightedCapacity`. When a Spot instance is provisioned, the
    # `WeightedCapacity` units count toward the target capacity. Amazon EMR
    # provisions instances until the target capacity is totally fulfilled, even
    # if this results in an overage. For example, if there are 2 units remaining
    # to fulfill capacity, and Amazon EMR can only provision an instance with a
    # `WeightedCapacity` of 5 units, the instance is provisioned, and the target
    # capacity is exceeded by 3 units. You can use
    # InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units
    # that have been provisioned for the instance fleet.

    # If not specified or set to 0, only On-Demand instances are provisioned for
    # the instance fleet. At least one of `TargetSpotCapacity` and
    # `TargetOnDemandCapacity` should be greater than 0. For a master instance
    # fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be
    # specified, and its value must be 1.
    target_spot_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of On-Demand units that have been provisioned for the instance
    # fleet to fulfill `TargetOnDemandCapacity`. This provisioned capacity might
    # be less than or greater than `TargetOnDemandCapacity`.
    provisioned_on_demand_capacity: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of Spot units that have been provisioned for this instance fleet
    # to fulfill `TargetSpotCapacity`. This provisioned capacity might be less
    # than or greater than `TargetSpotCapacity`.
    provisioned_spot_capacity: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specification for the instance types that comprise an instance fleet.
    # Up to five unique instance specifications may be defined for each instance
    # fleet.
    instance_type_specifications: typing.List["InstanceTypeSpecification"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # Describes the launch specification for an instance fleet.
    launch_specifications: "InstanceFleetProvisioningSpecifications" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceFleetConfig(ShapeBase):
    """
    The configuration that defines an instance fleet.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_fleet_type",
                "InstanceFleetType",
                TypeInfo(typing.Union[str, InstanceFleetType]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "target_on_demand_capacity",
                "TargetOnDemandCapacity",
                TypeInfo(int),
            ),
            (
                "target_spot_capacity",
                "TargetSpotCapacity",
                TypeInfo(int),
            ),
            (
                "instance_type_configs",
                "InstanceTypeConfigs",
                TypeInfo(typing.List[InstanceTypeConfig]),
            ),
            (
                "launch_specifications",
                "LaunchSpecifications",
                TypeInfo(InstanceFleetProvisioningSpecifications),
            ),
        ]

    # The node type that the instance fleet hosts. Valid values are
    # MASTER,CORE,and TASK.
    instance_fleet_type: typing.Union[str, "InstanceFleetType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The friendly name of the instance fleet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target capacity of On-Demand units for the instance fleet, which
    # determines how many On-Demand instances to provision. When the instance
    # fleet launches, Amazon EMR tries to provision On-Demand instances as
    # specified by InstanceTypeConfig. Each instance configuration has a
    # specified `WeightedCapacity`. When an On-Demand instance is provisioned,
    # the `WeightedCapacity` units count toward the target capacity. Amazon EMR
    # provisions instances until the target capacity is totally fulfilled, even
    # if this results in an overage. For example, if there are 2 units remaining
    # to fulfill capacity, and Amazon EMR can only provision an instance with a
    # `WeightedCapacity` of 5 units, the instance is provisioned, and the target
    # capacity is exceeded by 3 units.

    # If not specified or set to 0, only Spot instances are provisioned for the
    # instance fleet using `TargetSpotCapacity`. At least one of
    # `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0.
    # For a master instance fleet, only one of `TargetSpotCapacity` and
    # `TargetOnDemandCapacity` can be specified, and its value must be 1.
    target_on_demand_capacity: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target capacity of Spot units for the instance fleet, which determines
    # how many Spot instances to provision. When the instance fleet launches,
    # Amazon EMR tries to provision Spot instances as specified by
    # InstanceTypeConfig. Each instance configuration has a specified
    # `WeightedCapacity`. When a Spot instance is provisioned, the
    # `WeightedCapacity` units count toward the target capacity. Amazon EMR
    # provisions instances until the target capacity is totally fulfilled, even
    # if this results in an overage. For example, if there are 2 units remaining
    # to fulfill capacity, and Amazon EMR can only provision an instance with a
    # `WeightedCapacity` of 5 units, the instance is provisioned, and the target
    # capacity is exceeded by 3 units.

    # If not specified or set to 0, only On-Demand instances are provisioned for
    # the instance fleet. At least one of `TargetSpotCapacity` and
    # `TargetOnDemandCapacity` should be greater than 0. For a master instance
    # fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be
    # specified, and its value must be 1.
    target_spot_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type configurations that define the EC2 instances in the
    # instance fleet.
    instance_type_configs: typing.List["InstanceTypeConfig"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The launch specification for the instance fleet.
    launch_specifications: "InstanceFleetProvisioningSpecifications" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceFleetModifyConfig(ShapeBase):
    """
    Configuration parameters for an instance fleet modification request.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_fleet_id",
                "InstanceFleetId",
                TypeInfo(str),
            ),
            (
                "target_on_demand_capacity",
                "TargetOnDemandCapacity",
                TypeInfo(int),
            ),
            (
                "target_spot_capacity",
                "TargetSpotCapacity",
                TypeInfo(int),
            ),
        ]

    # A unique identifier for the instance fleet.
    instance_fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target capacity of On-Demand units for the instance fleet. For more
    # information see InstanceFleetConfig$TargetOnDemandCapacity.
    target_on_demand_capacity: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target capacity of Spot units for the instance fleet. For more
    # information, see InstanceFleetConfig$TargetSpotCapacity.
    target_spot_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceFleetProvisioningSpecifications(ShapeBase):
    """
    The launch specification for Spot instances in the fleet, which determines the
    defined duration and provisioning timeout behavior.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "spot_specification",
                "SpotSpecification",
                TypeInfo(SpotProvisioningSpecification),
            ),
        ]

    # The launch specification for Spot instances in the fleet, which determines
    # the defined duration and provisioning timeout behavior.
    spot_specification: "SpotProvisioningSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceFleetState(str):
    PROVISIONING = "PROVISIONING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    RESIZING = "RESIZING"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"


@dataclasses.dataclass
class InstanceFleetStateChangeReason(ShapeBase):
    """
    Provides status change reason details for the instance fleet.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, InstanceFleetStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # A code corresponding to the reason the state change occurred.
    code: typing.Union[str, "InstanceFleetStateChangeReasonCode"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # An explanatory message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceFleetStateChangeReasonCode(str):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    CLUSTER_TERMINATED = "CLUSTER_TERMINATED"


@dataclasses.dataclass
class InstanceFleetStatus(ShapeBase):
    """
    The status of the instance fleet.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InstanceFleetState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(InstanceFleetStateChangeReason),
            ),
            (
                "timeline",
                "Timeline",
                TypeInfo(InstanceFleetTimeline),
            ),
        ]

    # A code representing the instance fleet status.

    #   * `PROVISIONING`—The instance fleet is provisioning EC2 resources and is not yet ready to run jobs.

    #   * `BOOTSTRAPPING`—EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway.

    #   * `RUNNING`—EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs.

    #   * `RESIZING`—A resize operation is underway. EC2 instances are either being added or removed.

    #   * `SUSPENDED`—A resize operation could not complete. Existing EC2 instances are running, but instances can't be added or removed.

    #   * `TERMINATING`—The instance fleet is terminating EC2 instances.

    #   * `TERMINATED`—The instance fleet is no longer active, and all EC2 instances have been terminated.
    state: typing.Union[str, "InstanceFleetState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides status change reason details for the instance fleet.
    state_change_reason: "InstanceFleetStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides historical timestamps for the instance fleet, including the time
    # of creation, the time it became ready to run jobs, and the time of
    # termination.
    timeline: "InstanceFleetTimeline" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceFleetTimeline(ShapeBase):
    """
    Provides historical timestamps for the instance fleet, including the time of
    creation, the time it became ready to run jobs, and the time of termination.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ready_date_time",
                "ReadyDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The time and date the instance fleet was created.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time and date the instance fleet was ready to run jobs.
    ready_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time and date the instance fleet terminated.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceFleetType(str):
    MASTER = "MASTER"
    CORE = "CORE"
    TASK = "TASK"


@dataclasses.dataclass
class InstanceGroup(ShapeBase):
    """
    This entity represents an instance group, which is a group of instances that
    have common purpose. For example, CORE instance group is used for HDFS.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "market",
                "Market",
                TypeInfo(typing.Union[str, MarketType]),
            ),
            (
                "instance_group_type",
                "InstanceGroupType",
                TypeInfo(typing.Union[str, InstanceGroupType]),
            ),
            (
                "bid_price",
                "BidPrice",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "requested_instance_count",
                "RequestedInstanceCount",
                TypeInfo(int),
            ),
            (
                "running_instance_count",
                "RunningInstanceCount",
                TypeInfo(int),
            ),
            (
                "status",
                "Status",
                TypeInfo(InstanceGroupStatus),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
            (
                "ebs_block_devices",
                "EbsBlockDevices",
                TypeInfo(typing.List[EbsBlockDevice]),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                TypeInfo(bool),
            ),
            (
                "shrink_policy",
                "ShrinkPolicy",
                TypeInfo(ShrinkPolicy),
            ),
            (
                "auto_scaling_policy",
                "AutoScalingPolicy",
                TypeInfo(AutoScalingPolicyDescription),
            ),
        ]

    # The identifier of the instance group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the instance group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marketplace to provision instances for this group. Valid values are
    # ON_DEMAND or SPOT.
    market: typing.Union[str, "MarketType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the instance group. Valid values are MASTER, CORE or TASK.
    instance_group_type: typing.Union[str, "InstanceGroupType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The maximum Spot price your are willing to pay for EC2 instances.

    # An optional, nullable field that applies if the `MarketType` for the
    # instance group is specified as `SPOT`. Specify the maximum spot price in
    # USD. If the value is NULL and `SPOT` is specified, the maximum Spot price
    # is set equal to the On-Demand price.
    bid_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 instance type for all instances in the instance group.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target number of instances for the instance group.
    requested_instance_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances currently running in this instance group.
    running_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the instance group.
    status: "InstanceGroupStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon EMR releases 4.x or later.

    # The list of configurations supplied for an EMR cluster instance group. You
    # can specify a separate configuration for each instance group (master, core,
    # and task).
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EBS block devices that are mapped to this instance group.
    ebs_block_devices: typing.List["EbsBlockDevice"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the instance group is EBS-optimized. An Amazon EBS-optimized instance
    # uses an optimized configuration stack and provides additional, dedicated
    # capacity for Amazon EBS I/O.
    ebs_optimized: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Policy for customizing shrink operations.
    shrink_policy: "ShrinkPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An automatic scaling policy for a core instance group or task instance
    # group in an Amazon EMR cluster. The automatic scaling policy defines how an
    # instance group dynamically adds and terminates EC2 instances in response to
    # the value of a CloudWatch metric. See PutAutoScalingPolicy.
    auto_scaling_policy: "AutoScalingPolicyDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceGroupConfig(ShapeBase):
    """
    Configuration defining a new instance group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_role",
                "InstanceRole",
                TypeInfo(typing.Union[str, InstanceRoleType]),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "market",
                "Market",
                TypeInfo(typing.Union[str, MarketType]),
            ),
            (
                "bid_price",
                "BidPrice",
                TypeInfo(str),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
            (
                "ebs_configuration",
                "EbsConfiguration",
                TypeInfo(EbsConfiguration),
            ),
            (
                "auto_scaling_policy",
                "AutoScalingPolicy",
                TypeInfo(AutoScalingPolicy),
            ),
        ]

    # The role of the instance group in the cluster.
    instance_role: typing.Union[str, "InstanceRoleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 instance type for all instances in the instance group.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Target number of instances for the instance group.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Friendly name given to the instance group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Market type of the EC2 instances used to create a cluster node.
    market: typing.Union[str, "MarketType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum Spot price your are willing to pay for EC2 instances.

    # An optional, nullable field that applies if the `MarketType` for the
    # instance group is specified as `SPOT`. Specify the maximum spot price in
    # USD. If the value is NULL and `SPOT` is specified, the maximum Spot price
    # is set equal to the On-Demand price.
    bid_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon EMR releases 4.x or later.

    # The list of configurations supplied for an EMR cluster instance group. You
    # can specify a separate configuration for each instance group (master, core,
    # and task).
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # EBS configurations that will be attached to each EC2 instance in the
    # instance group.
    ebs_configuration: "EbsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An automatic scaling policy for a core instance group or task instance
    # group in an Amazon EMR cluster. The automatic scaling policy defines how an
    # instance group dynamically adds and terminates EC2 instances in response to
    # the value of a CloudWatch metric. See PutAutoScalingPolicy.
    auto_scaling_policy: "AutoScalingPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceGroupDetail(ShapeBase):
    """
    Detailed information about an instance group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "market",
                "Market",
                TypeInfo(typing.Union[str, MarketType]),
            ),
            (
                "instance_role",
                "InstanceRole",
                TypeInfo(typing.Union[str, InstanceRoleType]),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "instance_request_count",
                "InstanceRequestCount",
                TypeInfo(int),
            ),
            (
                "instance_running_count",
                "InstanceRunningCount",
                TypeInfo(int),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InstanceGroupState]),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "bid_price",
                "BidPrice",
                TypeInfo(str),
            ),
            (
                "last_state_change_reason",
                "LastStateChangeReason",
                TypeInfo(str),
            ),
            (
                "start_date_time",
                "StartDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ready_date_time",
                "ReadyDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Market type of the EC2 instances used to create a cluster node.
    market: typing.Union[str, "MarketType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Instance group role in the cluster
    instance_role: typing.Union[str, "InstanceRoleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # EC2 instance type.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Target number of instances to run in the instance group.
    instance_request_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Actual count of running instances.
    instance_running_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # State of instance group. The following values are deprecated: STARTING,
    # TERMINATED, and FAILED.
    state: typing.Union[str, "InstanceGroupState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date/time the instance group was created.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for the instance group.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Friendly name for the instance group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum Spot price your are willing to pay for EC2 instances.

    # An optional, nullable field that applies if the `MarketType` for the
    # instance group is specified as `SPOT`. Specified in USD. If the value is
    # NULL and `SPOT` is specified, the maximum Spot price is set equal to the
    # On-Demand price.
    bid_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details regarding the state of the instance group.
    last_state_change_reason: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date/time the instance group was started.
    start_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date/time the instance group was available to the cluster.
    ready_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date/time the instance group was terminated.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceGroupModifyConfig(ShapeBase):
    """
    Modify an instance group size.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "ec2_instance_ids_to_terminate",
                "EC2InstanceIdsToTerminate",
                TypeInfo(typing.List[str]),
            ),
            (
                "shrink_policy",
                "ShrinkPolicy",
                TypeInfo(ShrinkPolicy),
            ),
        ]

    # Unique ID of the instance group to expand or shrink.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Target size for the instance group.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 InstanceIds to terminate. After you terminate the instances, the
    # instance group will not return to its original requested size.
    ec2_instance_ids_to_terminate: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Policy for customizing shrink operations.
    shrink_policy: "ShrinkPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceGroupState(str):
    PROVISIONING = "PROVISIONING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    RESIZING = "RESIZING"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    ARRESTED = "ARRESTED"
    SHUTTING_DOWN = "SHUTTING_DOWN"
    ENDED = "ENDED"


@dataclasses.dataclass
class InstanceGroupStateChangeReason(ShapeBase):
    """
    The status change reason details for the instance group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, InstanceGroupStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The programmable code for the state change reason.
    code: typing.Union[str, "InstanceGroupStateChangeReasonCode"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # The status change reason description.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceGroupStateChangeReasonCode(str):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    CLUSTER_TERMINATED = "CLUSTER_TERMINATED"


@dataclasses.dataclass
class InstanceGroupStatus(ShapeBase):
    """
    The details of the instance group status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InstanceGroupState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(InstanceGroupStateChangeReason),
            ),
            (
                "timeline",
                "Timeline",
                TypeInfo(InstanceGroupTimeline),
            ),
        ]

    # The current state of the instance group.
    state: typing.Union[str, "InstanceGroupState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status change reason details for the instance group.
    state_change_reason: "InstanceGroupStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeline of the instance group status over time.
    timeline: "InstanceGroupTimeline" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceGroupTimeline(ShapeBase):
    """
    The timeline of the instance group lifecycle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ready_date_time",
                "ReadyDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The creation date and time of the instance group.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the instance group became ready to perform tasks.
    ready_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the instance group terminated.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceGroupType(str):
    MASTER = "MASTER"
    CORE = "CORE"
    TASK = "TASK"


@dataclasses.dataclass
class InstanceResizePolicy(ShapeBase):
    """
    Custom policy for requesting termination protection or termination of specific
    instances when shrinking an instance group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instances_to_terminate",
                "InstancesToTerminate",
                TypeInfo(typing.List[str]),
            ),
            (
                "instances_to_protect",
                "InstancesToProtect",
                TypeInfo(typing.List[str]),
            ),
            (
                "instance_termination_timeout",
                "InstanceTerminationTimeout",
                TypeInfo(int),
            ),
        ]

    # Specific list of instances to be terminated when shrinking an instance
    # group.
    instances_to_terminate: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specific list of instances to be protected when shrinking an instance
    # group.
    instances_to_protect: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Decommissioning timeout override for the specific list of instances to be
    # terminated.
    instance_termination_timeout: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceRoleType(str):
    MASTER = "MASTER"
    CORE = "CORE"
    TASK = "TASK"


class InstanceState(str):
    AWAITING_FULFILLMENT = "AWAITING_FULFILLMENT"
    PROVISIONING = "PROVISIONING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    TERMINATED = "TERMINATED"


@dataclasses.dataclass
class InstanceStateChangeReason(ShapeBase):
    """
    The details of the status change reason for the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, InstanceStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The programmable code for the state change reason.
    code: typing.Union[str, "InstanceStateChangeReasonCode"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # The status change reason description.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceStateChangeReasonCode(str):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    BOOTSTRAP_FAILURE = "BOOTSTRAP_FAILURE"
    CLUSTER_TERMINATED = "CLUSTER_TERMINATED"


@dataclasses.dataclass
class InstanceStatus(ShapeBase):
    """
    The instance status details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InstanceState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(InstanceStateChangeReason),
            ),
            (
                "timeline",
                "Timeline",
                TypeInfo(InstanceTimeline),
            ),
        ]

    # The current state of the instance.
    state: typing.Union[str, "InstanceState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the status change reason for the instance.
    state_change_reason: "InstanceStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeline of the instance status over time.
    timeline: "InstanceTimeline" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceTimeline(ShapeBase):
    """
    The timeline of the instance lifecycle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ready_date_time",
                "ReadyDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The creation date and time of the instance.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the instance was ready to perform tasks.
    ready_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the instance was terminated.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceTypeConfig(ShapeBase):
    """
    An instance type configuration for each instance type in an instance fleet,
    which determines the EC2 instances Amazon EMR attempts to provision to fulfill
    On-Demand and Spot target capacities. There can be a maximum of 5 instance type
    configurations in a fleet.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "weighted_capacity",
                "WeightedCapacity",
                TypeInfo(int),
            ),
            (
                "bid_price",
                "BidPrice",
                TypeInfo(str),
            ),
            (
                "bid_price_as_percentage_of_on_demand_price",
                "BidPriceAsPercentageOfOnDemandPrice",
                TypeInfo(float),
            ),
            (
                "ebs_configuration",
                "EbsConfiguration",
                TypeInfo(EbsConfiguration),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
        ]

    # An EC2 instance type, such as `m3.xlarge`.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of units that a provisioned instance of this type provides
    # toward fulfilling the target capacities defined in InstanceFleetConfig.
    # This value is 1 for a master instance fleet, and must be 1 or greater for
    # core and task instance fleets. Defaults to 1 if not specified.
    weighted_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bid price for each EC2 Spot instance type as defined by `InstanceType`.
    # Expressed in USD. If neither `BidPrice` nor
    # `BidPriceAsPercentageOfOnDemandPrice` is provided,
    # `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.
    bid_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bid price, as a percentage of On-Demand price, for each EC2 Spot
    # instance as defined by `InstanceType`. Expressed as a number (for example,
    # 20 specifies 20%). If neither `BidPrice` nor
    # `BidPriceAsPercentageOfOnDemandPrice` is provided,
    # `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.
    bid_price_as_percentage_of_on_demand_price: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration of Amazon Elastic Block Storage (EBS) attached to each
    # instance as defined by `InstanceType`.
    ebs_configuration: "EbsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A configuration classification that applies when provisioning cluster
    # instances, which can include configurations for applications and software
    # that run on the cluster.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceTypeSpecification(ShapeBase):
    """
    The configuration specification for each instance type in an instance fleet.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "weighted_capacity",
                "WeightedCapacity",
                TypeInfo(int),
            ),
            (
                "bid_price",
                "BidPrice",
                TypeInfo(str),
            ),
            (
                "bid_price_as_percentage_of_on_demand_price",
                "BidPriceAsPercentageOfOnDemandPrice",
                TypeInfo(float),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
            (
                "ebs_block_devices",
                "EbsBlockDevices",
                TypeInfo(typing.List[EbsBlockDevice]),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                TypeInfo(bool),
            ),
        ]

    # The EC2 instance type, for example `m3.xlarge`.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of units that a provisioned instance of this type provides
    # toward fulfilling the target capacities defined in InstanceFleetConfig.
    # Capacity values represent performance characteristics such as vCPUs,
    # memory, or I/O. If not specified, the default value is 1.
    weighted_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bid price for each EC2 Spot instance type as defined by `InstanceType`.
    # Expressed in USD.
    bid_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bid price, as a percentage of On-Demand price, for each EC2 Spot
    # instance as defined by `InstanceType`. Expressed as a number (for example,
    # 20 specifies 20%).
    bid_price_as_percentage_of_on_demand_price: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A configuration classification that applies when provisioning cluster
    # instances, which can include configurations for applications and software
    # bundled with Amazon EMR.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration of Amazon Elastic Block Storage (EBS) attached to each
    # instance as defined by `InstanceType`.
    ebs_block_devices: typing.List["EbsBlockDevice"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Evaluates to `TRUE` when the specified `InstanceType` is EBS-optimized.
    ebs_optimized: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    Indicates that an error occurred while processing the request and that the
    request was not completed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InternalServerException(ShapeBase):
    """
    This exception occurs when there is an internal failure in the EMR service.
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

    # The message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    This exception occurs when there is something wrong with user input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The error code associated with the exception.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message associated with the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobFlowDetail(ShapeBase):
    """
    A description of a cluster (job flow).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_flow_id",
                "JobFlowId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "execution_status_detail",
                "ExecutionStatusDetail",
                TypeInfo(JobFlowExecutionStatusDetail),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(JobFlowInstancesDetail),
            ),
            (
                "log_uri",
                "LogUri",
                TypeInfo(str),
            ),
            (
                "ami_version",
                "AmiVersion",
                TypeInfo(str),
            ),
            (
                "steps",
                "Steps",
                TypeInfo(typing.List[StepDetail]),
            ),
            (
                "bootstrap_actions",
                "BootstrapActions",
                TypeInfo(typing.List[BootstrapActionDetail]),
            ),
            (
                "supported_products",
                "SupportedProducts",
                TypeInfo(typing.List[str]),
            ),
            (
                "visible_to_all_users",
                "VisibleToAllUsers",
                TypeInfo(bool),
            ),
            (
                "job_flow_role",
                "JobFlowRole",
                TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "auto_scaling_role",
                "AutoScalingRole",
                TypeInfo(str),
            ),
            (
                "scale_down_behavior",
                "ScaleDownBehavior",
                TypeInfo(typing.Union[str, ScaleDownBehavior]),
            ),
        ]

    # The job flow identifier.
    job_flow_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the job flow.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the execution status of the job flow.
    execution_status_detail: "JobFlowExecutionStatusDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the Amazon EC2 instances of the job flow.
    instances: "JobFlowInstancesDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The location in Amazon S3 where log files for the job are stored.
    log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR
    # releases 4.0 and later, `ReleaseLabel` is used. To specify a custom AMI,
    # use `CustomAmiID`.
    ami_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of steps run by the job flow.
    steps: typing.List["StepDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the bootstrap actions run by the job flow.
    bootstrap_actions: typing.List["BootstrapActionDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of strings set by third party software when the job flow is
    # launched. If you are not using third party software to manage the job flow
    # this value is empty.
    supported_products: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the cluster is visible to all IAM users of the AWS
    # account associated with the cluster. If this value is set to `true`, all
    # IAM users of that AWS account can view and (if they have the proper policy
    # permissions set) manage the cluster. If it is set to `false`, only the IAM
    # user that created the cluster can view and manage it. This value can be
    # changed using the SetVisibleToAllUsers action.
    visible_to_all_users: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that was specified when the job flow was launched. The EC2
    # instances of the job flow assume this role.
    job_flow_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that will be assumed by the Amazon EMR service to access AWS
    # resources on your behalf.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM role for automatic scaling policies. The default role is
    # `EMR_AutoScaling_DefaultRole`. The IAM role provides a way for the
    # automatic scaling feature to get the required permissions it needs to
    # launch and terminate EC2 instances in an instance group.
    auto_scaling_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The way that individual Amazon EC2 instances terminate when an automatic
    # scale-in activity occurs or an instance group is resized.
    # `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at
    # the instance-hour boundary, regardless of when the request to terminate the
    # instance was submitted. This option is only available with Amazon EMR 5.1.0
    # and later and is the default for clusters created using that version.
    # `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR blacklists and
    # drains tasks from nodes before terminating the Amazon EC2 instances,
    # regardless of the instance-hour boundary. With either behavior, Amazon EMR
    # removes the least active nodes first and blocks instance termination if it
    # could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` available
    # only in Amazon EMR version 4.1.0 and later, and is the default for versions
    # of Amazon EMR earlier than 5.1.0.
    scale_down_behavior: typing.Union[str, "ScaleDownBehavior"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


class JobFlowExecutionState(str):
    """
    The type of instance.
    """
    STARTING = "STARTING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    SHUTTING_DOWN = "SHUTTING_DOWN"
    TERMINATED = "TERMINATED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclasses.dataclass
class JobFlowExecutionStatusDetail(ShapeBase):
    """
    Describes the status of the cluster (job flow).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, JobFlowExecutionState]),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "start_date_time",
                "StartDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ready_date_time",
                "ReadyDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_state_change_reason",
                "LastStateChangeReason",
                TypeInfo(str),
            ),
        ]

    # The state of the job flow.
    state: typing.Union[str, "JobFlowExecutionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date and time of the job flow.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start date and time of the job flow.
    start_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the job flow was ready to start running bootstrap
    # actions.
    ready_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The completion date and time of the job flow.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Description of the job flow last changed state.
    last_state_change_reason: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JobFlowInstancesConfig(ShapeBase):
    """
    A description of the Amazon EC2 instance on which the cluster (job flow) runs. A
    valid JobFlowInstancesConfig must contain either InstanceGroups or
    InstanceFleets, which is the recommended configuration. They cannot be used
    together. You may also have MasterInstanceType, SlaveInstanceType, and
    InstanceCount (all three must be present), but we don't recommend this
    configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "master_instance_type",
                "MasterInstanceType",
                TypeInfo(str),
            ),
            (
                "slave_instance_type",
                "SlaveInstanceType",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "instance_groups",
                "InstanceGroups",
                TypeInfo(typing.List[InstanceGroupConfig]),
            ),
            (
                "instance_fleets",
                "InstanceFleets",
                TypeInfo(typing.List[InstanceFleetConfig]),
            ),
            (
                "ec2_key_name",
                "Ec2KeyName",
                TypeInfo(str),
            ),
            (
                "placement",
                "Placement",
                TypeInfo(PlacementType),
            ),
            (
                "keep_job_flow_alive_when_no_steps",
                "KeepJobFlowAliveWhenNoSteps",
                TypeInfo(bool),
            ),
            (
                "termination_protected",
                "TerminationProtected",
                TypeInfo(bool),
            ),
            (
                "hadoop_version",
                "HadoopVersion",
                TypeInfo(str),
            ),
            (
                "ec2_subnet_id",
                "Ec2SubnetId",
                TypeInfo(str),
            ),
            (
                "ec2_subnet_ids",
                "Ec2SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "emr_managed_master_security_group",
                "EmrManagedMasterSecurityGroup",
                TypeInfo(str),
            ),
            (
                "emr_managed_slave_security_group",
                "EmrManagedSlaveSecurityGroup",
                TypeInfo(str),
            ),
            (
                "service_access_security_group",
                "ServiceAccessSecurityGroup",
                TypeInfo(str),
            ),
            (
                "additional_master_security_groups",
                "AdditionalMasterSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "additional_slave_security_groups",
                "AdditionalSlaveSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The EC2 instance type of the master node.
    master_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 instance type of the slave nodes.
    slave_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of EC2 instances in the cluster.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Configuration for the instance groups in a cluster.
    instance_groups: typing.List["InstanceGroupConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance fleet configuration is available only in Amazon EMR versions
    # 4.8.0 and later, excluding 5.0.x versions.

    # Describes the EC2 instances and instance configurations for clusters that
    # use the instance fleet configuration.
    instance_fleets: typing.List["InstanceFleetConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the EC2 key pair that can be used to ssh to the master node as
    # the user called "hadoop."
    ec2_key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone in which the cluster runs.
    placement: "PlacementType" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the cluster should remain available after completing all
    # steps.
    keep_job_flow_alive_when_no_steps: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether to lock the cluster to prevent the Amazon EC2 instances
    # from being terminated by API call, user intervention, or in the event of a
    # job-flow error.
    termination_protected: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop
    # version for the cluster. Valid inputs are "0.18" (deprecated), "0.20"
    # (deprecated), "0.20.205" (deprecated), "1.0.3", "2.2.0", or "2.4.0". If you
    # do not set this value, the default of 0.18 is used, unless the `AmiVersion`
    # parameter is set in the RunJobFlow call, in which case the default version
    # of Hadoop for that AMI version is used.
    hadoop_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies to clusters that use the uniform instance group configuration. To
    # launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this
    # parameter to the identifier of the Amazon VPC subnet where you want the
    # cluster to launch. If you do not specify this value, the cluster launches
    # in the normal Amazon Web Services cloud, outside of an Amazon VPC, if the
    # account launching the cluster supports EC2 Classic networks in the region
    # where the cluster launches.

    # Amazon VPC currently does not support cluster compute quadruple extra large
    # (cc1.4xlarge) instances. Thus you cannot specify the cc1.4xlarge instance
    # type for clusters launched in an Amazon VPC.
    ec2_subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies to clusters that use the instance fleet configuration. When
    # multiple EC2 subnet IDs are specified, Amazon EMR evaluates them and
    # launches instances in the optimal subnet.

    # The instance fleet configuration is available only in Amazon EMR versions
    # 4.8.0 and later, excluding 5.0.x versions.
    ec2_subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Amazon EC2 security group for the master node.
    emr_managed_master_security_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Amazon EC2 security group for the slave nodes.
    emr_managed_slave_security_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Amazon EC2 security group for the Amazon EMR service
    # to access clusters in VPC private subnets.
    service_access_security_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of additional Amazon EC2 security group IDs for the master node.
    additional_master_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of additional Amazon EC2 security group IDs for the slave nodes.
    additional_slave_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JobFlowInstancesDetail(ShapeBase):
    """
    Specify the type of Amazon EC2 instances that the cluster (job flow) runs on.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "master_instance_type",
                "MasterInstanceType",
                TypeInfo(str),
            ),
            (
                "slave_instance_type",
                "SlaveInstanceType",
                TypeInfo(str),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "master_public_dns_name",
                "MasterPublicDnsName",
                TypeInfo(str),
            ),
            (
                "master_instance_id",
                "MasterInstanceId",
                TypeInfo(str),
            ),
            (
                "instance_groups",
                "InstanceGroups",
                TypeInfo(typing.List[InstanceGroupDetail]),
            ),
            (
                "normalized_instance_hours",
                "NormalizedInstanceHours",
                TypeInfo(int),
            ),
            (
                "ec2_key_name",
                "Ec2KeyName",
                TypeInfo(str),
            ),
            (
                "ec2_subnet_id",
                "Ec2SubnetId",
                TypeInfo(str),
            ),
            (
                "placement",
                "Placement",
                TypeInfo(PlacementType),
            ),
            (
                "keep_job_flow_alive_when_no_steps",
                "KeepJobFlowAliveWhenNoSteps",
                TypeInfo(bool),
            ),
            (
                "termination_protected",
                "TerminationProtected",
                TypeInfo(bool),
            ),
            (
                "hadoop_version",
                "HadoopVersion",
                TypeInfo(str),
            ),
        ]

    # The Amazon EC2 master node instance type.
    master_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 slave node instance type.
    slave_instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of Amazon EC2 instances in the cluster. If the value is 1, the
    # same instance serves as both the master and slave node. If the value is
    # greater than 1, one instance is the master node and all others are slave
    # nodes.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS name of the master node. If the cluster is on a private subnet,
    # this is the private DNS name. On a public subnet, this is the public DNS
    # name.
    master_public_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 instance identifier of the master node.
    master_instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about the instance groups in a cluster.
    instance_groups: typing.List["InstanceGroupDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An approximation of the cost of the cluster, represented in m1.small/hours.
    # This value is incremented one time for every hour that an m1.small runs.
    # Larger instances are weighted more, so an Amazon EC2 instance that is
    # roughly four times more expensive would result in the normalized instance
    # hours being incremented by four. This result is only an approximation and
    # does not reflect the actual billing rate.
    normalized_instance_hours: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of an Amazon EC2 key pair that can be used to ssh to the master
    # node.
    ec2_key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For clusters launched within Amazon Virtual Private Cloud, this is the
    # identifier of the subnet where the cluster was launched.
    ec2_subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 Availability Zone for the cluster.
    placement: "PlacementType" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the cluster should remain available after completing all
    # steps.
    keep_job_flow_alive_when_no_steps: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the Amazon EC2 instances in the cluster are protected
    # from termination by API calls, user intervention, or in the event of a job-
    # flow error.
    termination_protected: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Hadoop version for the cluster.
    hadoop_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KerberosAttributes(ShapeBase):
    """
    Attributes for Kerberos configuration when Kerberos authentication is enabled
    using a security configuration. For more information see [Use Kerberos
    Authentication](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-
    kerberos.html) in the _EMR Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "realm",
                "Realm",
                TypeInfo(str),
            ),
            (
                "kdc_admin_password",
                "KdcAdminPassword",
                TypeInfo(str),
            ),
            (
                "cross_realm_trust_principal_password",
                "CrossRealmTrustPrincipalPassword",
                TypeInfo(str),
            ),
            (
                "ad_domain_join_user",
                "ADDomainJoinUser",
                TypeInfo(str),
            ),
            (
                "ad_domain_join_password",
                "ADDomainJoinPassword",
                TypeInfo(str),
            ),
        ]

    # The name of the Kerberos realm to which all nodes in a cluster belong. For
    # example, `EC2.INTERNAL`.
    realm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password used within the cluster for the kadmin service on the cluster-
    # dedicated KDC, which maintains Kerberos principals, password policies, and
    # keytabs for the cluster.
    kdc_admin_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required only when establishing a cross-realm trust with a KDC in a
    # different realm. The cross-realm principal password, which must be
    # identical across realms.
    cross_realm_trust_principal_password: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required only when establishing a cross-realm trust with an Active
    # Directory domain. A user with sufficient privileges to join resources to
    # the domain.
    ad_domain_join_user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Active Directory password for `ADDomainJoinUser`.
    ad_domain_join_password: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class KeyValue(ShapeBase):
    """
    A key value pair.
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

    # The unique identifier of a key value pair.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value part of the identified key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBootstrapActionsInput(ShapeBase):
    """
    This input determines which bootstrap actions to retrieve.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The cluster identifier for the bootstrap actions to list.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBootstrapActionsOutput(OutputShapeBase):
    """
    This output contains the bootstrap actions detail.
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
                "bootstrap_actions",
                "BootstrapActions",
                TypeInfo(typing.List[Command]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The bootstrap actions associated with the cluster.
    bootstrap_actions: typing.List["Command"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListBootstrapActionsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListClustersInput(ShapeBase):
    """
    This input determines how the ListClusters action filters the list of clusters
    that it returns.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_after",
                "CreatedAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_before",
                "CreatedBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "cluster_states",
                "ClusterStates",
                TypeInfo(typing.List[typing.Union[str, ClusterState]]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The creation date and time beginning value filter for listing clusters.
    created_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date and time end value filter for listing clusters.
    created_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cluster state filters to apply when listing clusters.
    cluster_states: typing.List[typing.Union[str, "ClusterState"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersOutput(OutputShapeBase):
    """
    This contains a ClusterSummaryList with the cluster details; for example, the
    cluster IDs, names, and status.
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
                "clusters",
                "Clusters",
                TypeInfo(typing.List[ClusterSummary]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of clusters for the account based on the given filters.
    clusters: typing.List["ClusterSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListClustersOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInstanceFleetsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstanceFleetsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_fleets",
                "InstanceFleets",
                TypeInfo(typing.List[InstanceFleet]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of instance fleets for the cluster and given filters.
    instance_fleets: typing.List["InstanceFleet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListInstanceFleetsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInstanceGroupsInput(ShapeBase):
    """
    This input determines which instance groups to retrieve.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster for which to list the instance groups.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstanceGroupsOutput(OutputShapeBase):
    """
    This input determines which instance groups to retrieve.
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
                "instance_groups",
                "InstanceGroups",
                TypeInfo(typing.List[InstanceGroup]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of instance groups for the cluster and given filters.
    instance_groups: typing.List["InstanceGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListInstanceGroupsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInstancesInput(ShapeBase):
    """
    This input determines which instances to list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
            (
                "instance_group_types",
                "InstanceGroupTypes",
                TypeInfo(typing.List[typing.Union[str, InstanceGroupType]]),
            ),
            (
                "instance_fleet_id",
                "InstanceFleetId",
                TypeInfo(str),
            ),
            (
                "instance_fleet_type",
                "InstanceFleetType",
                TypeInfo(typing.Union[str, InstanceFleetType]),
            ),
            (
                "instance_states",
                "InstanceStates",
                TypeInfo(typing.List[typing.Union[str, InstanceState]]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster for which to list the instances.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the instance group for which to list the instances.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of instance group for which to list the instances.
    instance_group_types: typing.List[typing.Union[str, "InstanceGroupType"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The unique identifier of the instance fleet.
    instance_fleet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type of the instance fleet. For example MASTER, CORE, or TASK.
    instance_fleet_type: typing.Union[str, "InstanceFleetType"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # A list of instance states that will filter the instances returned with this
    # request.
    instance_states: typing.List[typing.Union[str, "InstanceState"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstancesOutput(OutputShapeBase):
    """
    This output contains the list of instances.
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
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of instances for the cluster and given filters.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListInstancesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListSecurityConfigurationsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The pagination token that indicates the set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSecurityConfigurationsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_configurations",
                "SecurityConfigurations",
                TypeInfo(typing.List[SecurityConfigurationSummary]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date and time, and name, of each security configuration.
    security_configurations: typing.List["SecurityConfigurationSummary"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # A pagination token that indicates the next set of results to retrieve.
    # Include the marker in the next ListSecurityConfiguration call to retrieve
    # the next page of results, if required.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStepsInput(ShapeBase):
    """
    This input determines which steps to list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "step_states",
                "StepStates",
                TypeInfo(typing.List[typing.Union[str, StepState]]),
            ),
            (
                "step_ids",
                "StepIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster for which to list the steps.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter to limit the step list based on certain states.
    step_states: typing.List[typing.Union[str, "StepState"]
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # The filter to limit the step list based on the identifier of the steps.
    step_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStepsOutput(OutputShapeBase):
    """
    This output contains the list of steps returned in reverse order. This means
    that the last step is the first element in the list.
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
                "steps",
                "Steps",
                TypeInfo(typing.List[StepSummary]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filtered list of steps for the cluster.
    steps: typing.List["StepSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token that indicates the next set of results to retrieve.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListStepsOutput", None, None]:
        yield from super()._paginate()


class MarketType(str):
    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"


@dataclasses.dataclass
class MetricDimension(ShapeBase):
    """
    A CloudWatch dimension, which is specified using a `Key` (known as a `Name` in
    CloudWatch), `Value` pair. By default, Amazon EMR uses one dimension whose `Key`
    is `JobFlowID` and `Value` is a variable representing the cluster ID, which is
    `${emr.clusterId}`. This enables the rule to bootstrap when the cluster ID
    becomes available.
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

    # The dimension name.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimension value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyInstanceFleetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_fleet",
                "InstanceFleet",
                TypeInfo(InstanceFleetModifyConfig),
            ),
        ]

    # The unique identifier of the cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the instance fleet.
    instance_fleet: "InstanceFleetModifyConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyInstanceGroupsInput(ShapeBase):
    """
    Change the size of some instance groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_groups",
                "InstanceGroups",
                TypeInfo(typing.List[InstanceGroupModifyConfig]),
            ),
        ]

    # The ID of the cluster to which the instance group belongs.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Instance groups to change.
    instance_groups: typing.List["InstanceGroupModifyConfig"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class PlacementType(ShapeBase):
    """
    The Amazon EC2 Availability Zone configuration of the cluster (job flow).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon EC2 Availability Zone for the cluster. `AvailabilityZone` is
    # used for uniform instance groups, while `AvailabilityZones` (plural) is
    # used for instance fleets.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When multiple Availability Zones are specified, Amazon EMR evaluates them
    # and launches instances in the optimal Availability Zone.
    # `AvailabilityZones` is used for instance fleets, while `AvailabilityZone`
    # (singular) is used for uniform instance groups.

    # The instance fleet configuration is available only in Amazon EMR versions
    # 4.8.0 and later, excluding 5.0.x versions.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutAutoScalingPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
            (
                "auto_scaling_policy",
                "AutoScalingPolicy",
                TypeInfo(AutoScalingPolicy),
            ),
        ]

    # Specifies the ID of a cluster. The instance group to which the automatic
    # scaling policy is applied is within this cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ID of the instance group to which the automatic scaling
    # policy is applied.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the definition of the automatic scaling policy.
    auto_scaling_policy: "AutoScalingPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutAutoScalingPolicyOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
            (
                "auto_scaling_policy",
                "AutoScalingPolicy",
                TypeInfo(AutoScalingPolicyDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the ID of a cluster. The instance group to which the automatic
    # scaling policy is applied is within this cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ID of the instance group to which the scaling policy is
    # applied.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The automatic scaling policy definition.
    auto_scaling_policy: "AutoScalingPolicyDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveAutoScalingPolicyInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "instance_group_id",
                "InstanceGroupId",
                TypeInfo(str),
            ),
        ]

    # Specifies the ID of a cluster. The instance group to which the automatic
    # scaling policy is applied is within this cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ID of the instance group to which the scaling policy is
    # applied.
    instance_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveAutoScalingPolicyOutput(OutputShapeBase):
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
    """
    This input identifies a cluster and a list of tags to remove.
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon EMR resource identifier from which tags will be removed. This
    # value must be a cluster identifier.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag keys to remove from a resource.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsOutput(OutputShapeBase):
    """
    This output indicates the result of removing tags from a resource.
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


class RepoUpgradeOnBoot(str):
    SECURITY = "SECURITY"
    NONE = "NONE"


@dataclasses.dataclass
class RunJobFlowInput(ShapeBase):
    """
    Input to the RunJobFlow operation.
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
                "instances",
                "Instances",
                TypeInfo(JobFlowInstancesConfig),
            ),
            (
                "log_uri",
                "LogUri",
                TypeInfo(str),
            ),
            (
                "additional_info",
                "AdditionalInfo",
                TypeInfo(str),
            ),
            (
                "ami_version",
                "AmiVersion",
                TypeInfo(str),
            ),
            (
                "release_label",
                "ReleaseLabel",
                TypeInfo(str),
            ),
            (
                "steps",
                "Steps",
                TypeInfo(typing.List[StepConfig]),
            ),
            (
                "bootstrap_actions",
                "BootstrapActions",
                TypeInfo(typing.List[BootstrapActionConfig]),
            ),
            (
                "supported_products",
                "SupportedProducts",
                TypeInfo(typing.List[str]),
            ),
            (
                "new_supported_products",
                "NewSupportedProducts",
                TypeInfo(typing.List[SupportedProductConfig]),
            ),
            (
                "applications",
                "Applications",
                TypeInfo(typing.List[Application]),
            ),
            (
                "configurations",
                "Configurations",
                TypeInfo(typing.List[Configuration]),
            ),
            (
                "visible_to_all_users",
                "VisibleToAllUsers",
                TypeInfo(bool),
            ),
            (
                "job_flow_role",
                "JobFlowRole",
                TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "security_configuration",
                "SecurityConfiguration",
                TypeInfo(str),
            ),
            (
                "auto_scaling_role",
                "AutoScalingRole",
                TypeInfo(str),
            ),
            (
                "scale_down_behavior",
                "ScaleDownBehavior",
                TypeInfo(typing.Union[str, ScaleDownBehavior]),
            ),
            (
                "custom_ami_id",
                "CustomAmiId",
                TypeInfo(str),
            ),
            (
                "ebs_root_volume_size",
                "EbsRootVolumeSize",
                TypeInfo(int),
            ),
            (
                "repo_upgrade_on_boot",
                "RepoUpgradeOnBoot",
                TypeInfo(typing.Union[str, RepoUpgradeOnBoot]),
            ),
            (
                "kerberos_attributes",
                "KerberosAttributes",
                TypeInfo(KerberosAttributes),
            ),
        ]

    # The name of the job flow.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A specification of the number and type of Amazon EC2 instances.
    instances: "JobFlowInstancesConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The location in Amazon S3 to write the log files of the job flow. If a
    # value is not provided, logs are not created.
    log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A JSON string for selecting additional features.
    additional_info: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR
    # releases 4.0 and later, `ReleaseLabel` is used. To specify a custom AMI,
    # use `CustomAmiID`.
    ami_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EMR release label, which determines the version of open-source
    # application packages installed on the cluster. Release labels are in the
    # form `emr-x.x.x`, where x.x.x is an Amazon EMR release version, for
    # example, `emr-5.14.0`. For more information about Amazon EMR release
    # versions and included application versions and features, see
    # <http://docs.aws.amazon.com/emr/latest/ReleaseGuide/>. The release label
    # applies only to Amazon EMR releases versions 4.x and later. Earlier
    # versions use `AmiVersion`.
    release_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of steps to run.
    steps: typing.List["StepConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of bootstrap actions to run before Hadoop starts on the cluster
    # nodes.
    bootstrap_actions: typing.List["BootstrapActionConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later,
    # use Applications.

    # A list of strings that indicates third-party software to use. For more
    # information, see the [Amazon EMR Developer
    # Guide](http://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf).
    # Currently supported values are:

    #   * "mapr-m3" - launch the job flow using MapR M3 Edition.

    #   * "mapr-m5" - launch the job flow using MapR M5 Edition.
    supported_products: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later,
    # use Applications.

    # A list of strings that indicates third-party software to use with the job
    # flow that accepts a user argument list. EMR accepts and forwards the
    # argument list to the corresponding installation script as bootstrap action
    # arguments. For more information, see "Launch a Job Flow on the MapR
    # Distribution for Hadoop" in the [Amazon EMR Developer
    # Guide](http://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf).
    # Supported values are:

    #   * "mapr-m3" - launch the cluster using MapR M3 Edition.

    #   * "mapr-m5" - launch the cluster using MapR M5 Edition.

    #   * "mapr" with the user arguments specifying "--edition,m3" or "--edition,m5" - launch the job flow using MapR M3 or M5 Edition respectively.

    #   * "mapr-m7" - launch the cluster using MapR M7 Edition.

    #   * "hunk" - launch the cluster with the Hunk Big Data Analtics Platform.

    #   * "hue"- launch the cluster with Hue installed.

    #   * "spark" - launch the cluster with Apache Spark installed.

    #   * "ganglia" - launch the cluster with the Ganglia Monitoring System installed.
    new_supported_products: typing.List["SupportedProductConfig"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # For Amazon EMR releases 4.0 and later. A list of applications for the
    # cluster. Valid values are: "Hadoop", "Hive", "Mahout", "Pig", and "Spark."
    # They are case insensitive.
    applications: typing.List["Application"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For Amazon EMR releases 4.0 and later. The list of configurations supplied
    # for the EMR cluster you are creating.
    configurations: typing.List["Configuration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the cluster is visible to all IAM users of the AWS account
    # associated with the cluster. If this value is set to `true`, all IAM users
    # of that AWS account can view and (if they have the proper policy
    # permissions set) manage the cluster. If it is set to `false`, only the IAM
    # user that created the cluster can view and manage it.
    visible_to_all_users: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Also called instance profile and EC2 role. An IAM role for an EMR cluster.
    # The EC2 instances of the cluster assume this role. The default role is
    # `EMR_EC2_DefaultRole`. In order to use the default role, you must have
    # already created it using the CLI or console.
    job_flow_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that will be assumed by the Amazon EMR service to access AWS
    # resources on your behalf.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to associate with a cluster and propagate to Amazon EC2
    # instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a security configuration to apply to the cluster.
    security_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An IAM role for automatic scaling policies. The default role is
    # `EMR_AutoScaling_DefaultRole`. The IAM role provides permissions that the
    # automatic scaling feature requires to launch and terminate EC2 instances in
    # an instance group.
    auto_scaling_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the way that individual Amazon EC2 instances terminate when an
    # automatic scale-in activity occurs or an instance group is resized.
    # `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at
    # the instance-hour boundary, regardless of when the request to terminate the
    # instance was submitted. This option is only available with Amazon EMR 5.1.0
    # and later and is the default for clusters created using that version.
    # `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR blacklists and
    # drains tasks from nodes before terminating the Amazon EC2 instances,
    # regardless of the instance-hour boundary. With either behavior, Amazon EMR
    # removes the least active nodes first and blocks instance termination if it
    # could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` available
    # only in Amazon EMR version 4.1.0 and later, and is the default for versions
    # of Amazon EMR earlier than 5.1.0.
    scale_down_behavior: typing.Union[str, "ScaleDownBehavior"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Available only in Amazon EMR version 5.7.0 and later. The ID of a custom
    # Amazon EBS-backed Linux AMI. If specified, Amazon EMR uses this AMI when it
    # launches cluster EC2 instances. For more information about custom AMIs in
    # Amazon EMR, see [Using a Custom
    # AMI](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-
    # ami.html) in the _Amazon EMR Management Guide_. If omitted, the cluster
    # uses the base Linux AMI for the `ReleaseLabel` specified. For Amazon EMR
    # versions 2.x and 3.x, use `AmiVersion` instead.

    # For information about creating a custom AMI, see [Creating an Amazon EBS-
    # Backed Linux
    # AMI](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-
    # ebs.html) in the _Amazon Elastic Compute Cloud User Guide for Linux
    # Instances_. For information about finding an AMI ID, see [Finding a Linux
    # AMI](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-
    # ami.html).
    custom_ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in GiB, of the EBS root device volume of the Linux AMI that is
    # used for each EC2 instance. Available in Amazon EMR version 4.x and later.
    ebs_root_volume_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only when `CustomAmiID` is used. Specifies which updates from the
    # Amazon Linux AMI package repositories to apply automatically when the
    # instance boots using the AMI. If omitted, the default is `SECURITY`, which
    # indicates that only security updates are applied. If `NONE` is specified,
    # no updates are applied, and all updates must be applied manually.
    repo_upgrade_on_boot: typing.Union[str, "RepoUpgradeOnBoot"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Attributes for Kerberos configuration when Kerberos authentication is
    # enabled using a security configuration. For more information see [Use
    # Kerberos
    # Authentication](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-
    # kerberos.html) in the _EMR Management Guide_.
    kerberos_attributes: "KerberosAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RunJobFlowOutput(OutputShapeBase):
    """
    The result of the RunJobFlow operation.
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
                "job_flow_id",
                "JobFlowId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An unique identifier for the job flow.
    job_flow_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScaleDownBehavior(str):
    TERMINATE_AT_INSTANCE_HOUR = "TERMINATE_AT_INSTANCE_HOUR"
    TERMINATE_AT_TASK_COMPLETION = "TERMINATE_AT_TASK_COMPLETION"


@dataclasses.dataclass
class ScalingAction(ShapeBase):
    """
    The type of adjustment the automatic scaling activity makes when triggered, and
    the periodicity of the adjustment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "simple_scaling_policy_configuration",
                "SimpleScalingPolicyConfiguration",
                TypeInfo(SimpleScalingPolicyConfiguration),
            ),
            (
                "market",
                "Market",
                TypeInfo(typing.Union[str, MarketType]),
            ),
        ]

    # The type of adjustment the automatic scaling activity makes when triggered,
    # and the periodicity of the adjustment.
    simple_scaling_policy_configuration: "SimpleScalingPolicyConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Not available for instance groups. Instance groups use the market type
    # specified for the group.
    market: typing.Union[str, "MarketType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScalingConstraints(ShapeBase):
    """
    The upper and lower EC2 instance limits for an automatic scaling policy.
    Automatic scaling activities triggered by automatic scaling rules will not cause
    an instance group to grow above or below these limits.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "min_capacity",
                "MinCapacity",
                TypeInfo(int),
            ),
            (
                "max_capacity",
                "MaxCapacity",
                TypeInfo(int),
            ),
        ]

    # The lower boundary of EC2 instances in an instance group below which
    # scaling activities are not allowed to shrink. Scale-in activities will not
    # terminate instances below this boundary.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upper boundary of EC2 instances in an instance group beyond which
    # scaling activities are not allowed to grow. Scale-out activities will not
    # add instances beyond this boundary.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScalingRule(ShapeBase):
    """
    A scale-in or scale-out rule that defines scaling activity, including the
    CloudWatch metric alarm that triggers activity, how EC2 instances are added or
    removed, and the periodicity of adjustments. The automatic scaling policy for an
    instance group can comprise one or more automatic scaling rules.
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
                "action",
                "Action",
                TypeInfo(ScalingAction),
            ),
            (
                "trigger",
                "Trigger",
                TypeInfo(ScalingTrigger),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name used to identify an automatic scaling rule. Rule names must be
    # unique within a scaling policy.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The conditions that trigger an automatic scaling activity.
    action: "ScalingAction" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CloudWatch alarm definition that determines when automatic scaling
    # activity is triggered.
    trigger: "ScalingTrigger" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly, more verbose description of the automatic scaling rule.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScalingTrigger(ShapeBase):
    """
    The conditions that trigger an automatic scaling activity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_watch_alarm_definition",
                "CloudWatchAlarmDefinition",
                TypeInfo(CloudWatchAlarmDefinition),
            ),
        ]

    # The definition of a CloudWatch metric alarm. When the defined alarm
    # conditions are met along with other trigger parameters, scaling activity
    # begins.
    cloud_watch_alarm_definition: "CloudWatchAlarmDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScriptBootstrapActionConfig(ShapeBase):
    """
    Configuration of the script to run during a bootstrap action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "args",
                "Args",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Location of the script to run during a bootstrap action. Can be either a
    # location in Amazon S3 or on a local file system.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of command line arguments to pass to the bootstrap action script.
    args: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SecurityConfigurationSummary(ShapeBase):
    """
    The creation date and time, and name, of a security configuration.
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
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the security configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the security configuration was created.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetTerminationProtectionInput(ShapeBase):
    """
    The input argument to the TerminationProtection operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_flow_ids",
                "JobFlowIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "termination_protected",
                "TerminationProtected",
                TypeInfo(bool),
            ),
        ]

    # A list of strings that uniquely identify the clusters to protect. This
    # identifier is returned by RunJobFlow and can also be obtained from
    # DescribeJobFlows .
    job_flow_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean that indicates whether to protect the cluster and prevent the
    # Amazon EC2 instances in the cluster from shutting down due to API calls,
    # user intervention, or job-flow error.
    termination_protected: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetVisibleToAllUsersInput(ShapeBase):
    """
    The input to the SetVisibleToAllUsers action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_flow_ids",
                "JobFlowIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "visible_to_all_users",
                "VisibleToAllUsers",
                TypeInfo(bool),
            ),
        ]

    # Identifiers of the job flows to receive the new visibility setting.
    job_flow_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the specified clusters are visible to all IAM users of the AWS
    # account associated with the cluster. If this value is set to True, all IAM
    # users of that AWS account can view and, if they have the proper IAM policy
    # permissions set, manage the clusters. If it is set to False, only the IAM
    # user that created a cluster can view and manage it.
    visible_to_all_users: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ShrinkPolicy(ShapeBase):
    """
    Policy for customizing shrink operations. Allows configuration of
    decommissioning timeout and targeted instance shrinking.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "decommission_timeout",
                "DecommissionTimeout",
                TypeInfo(int),
            ),
            (
                "instance_resize_policy",
                "InstanceResizePolicy",
                TypeInfo(InstanceResizePolicy),
            ),
        ]

    # The desired timeout for decommissioning an instance. Overrides the default
    # YARN decommissioning timeout.
    decommission_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom policy for requesting termination protection or termination of
    # specific instances when shrinking an instance group.
    instance_resize_policy: "InstanceResizePolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SimpleScalingPolicyConfiguration(ShapeBase):
    """
    An automatic scaling configuration, which describes how the policy adds or
    removes instances, the cooldown period, and the number of EC2 instances that
    will be added each time the CloudWatch metric alarm condition is satisfied.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_adjustment",
                "ScalingAdjustment",
                TypeInfo(int),
            ),
            (
                "adjustment_type",
                "AdjustmentType",
                TypeInfo(typing.Union[str, AdjustmentType]),
            ),
            (
                "cool_down",
                "CoolDown",
                TypeInfo(int),
            ),
        ]

    # The amount by which to scale in or scale out, based on the specified
    # `AdjustmentType`. A positive value adds to the instance group's EC2
    # instance count while a negative number removes instances. If
    # `AdjustmentType` is set to `EXACT_CAPACITY`, the number should only be a
    # positive integer. If `AdjustmentType` is set to
    # `PERCENT_CHANGE_IN_CAPACITY`, the value should express the percentage as an
    # integer. For example, -20 indicates a decrease in 20% increments of cluster
    # capacity.
    scaling_adjustment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The way in which EC2 instances are added (if `ScalingAdjustment` is a
    # positive number) or terminated (if `ScalingAdjustment` is a negative
    # number) each time the scaling activity is triggered. `CHANGE_IN_CAPACITY`
    # is the default. `CHANGE_IN_CAPACITY` indicates that the EC2 instance count
    # increments or decrements by `ScalingAdjustment`, which should be expressed
    # as an integer. `PERCENT_CHANGE_IN_CAPACITY` indicates the instance count
    # increments or decrements by the percentage specified by
    # `ScalingAdjustment`, which should be expressed as an integer. For example,
    # 20 indicates an increase in 20% increments of cluster capacity.
    # `EXACT_CAPACITY` indicates the scaling activity results in an instance
    # group with the number of EC2 instances specified by `ScalingAdjustment`,
    # which should be expressed as a positive integer.
    adjustment_type: typing.Union[str, "AdjustmentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, after a scaling activity completes before
    # any further trigger-related scaling activities can start. The default value
    # is 0.
    cool_down: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SpotProvisioningSpecification(ShapeBase):
    """
    The launch specification for Spot instances in the instance fleet, which
    determines the defined duration and provisioning timeout behavior.

    The instance fleet configuration is available only in Amazon EMR versions 4.8.0
    and later, excluding 5.0.x versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timeout_duration_minutes",
                "TimeoutDurationMinutes",
                TypeInfo(int),
            ),
            (
                "timeout_action",
                "TimeoutAction",
                TypeInfo(typing.Union[str, SpotProvisioningTimeoutAction]),
            ),
            (
                "block_duration_minutes",
                "BlockDurationMinutes",
                TypeInfo(int),
            ),
        ]

    # The spot provisioning timeout period in minutes. If Spot instances are not
    # provisioned within this time period, the `TimeOutAction` is taken. Minimum
    # value is 5 and maximum value is 1440. The timeout applies only during
    # initial provisioning, when the cluster is first created.
    timeout_duration_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action to take when `TargetSpotCapacity` has not been fulfilled when
    # the `TimeoutDurationMinutes` has expired. Spot instances are not
    # uprovisioned within the Spot provisioining timeout. Valid values are
    # `TERMINATE_CLUSTER` and `SWITCH_TO_ON_DEMAND`. SWITCH_TO_ON_DEMAND
    # specifies that if no Spot instances are available, On-Demand Instances
    # should be provisioned to fulfill any remaining Spot capacity.
    timeout_action: typing.Union[str, "SpotProvisioningTimeoutAction"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The defined duration for Spot instances (also known as Spot blocks) in
    # minutes. When specified, the Spot instance does not terminate before the
    # defined duration expires, and defined duration pricing for Spot instances
    # applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration
    # period starts as soon as a Spot instance receives its instance ID. At the
    # end of the duration, Amazon EC2 marks the Spot instance for termination and
    # provides a Spot instance termination notice, which gives the instance a
    # two-minute warning before it terminates.
    block_duration_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class SpotProvisioningTimeoutAction(str):
    SWITCH_TO_ON_DEMAND = "SWITCH_TO_ON_DEMAND"
    TERMINATE_CLUSTER = "TERMINATE_CLUSTER"


class Statistic(str):
    SAMPLE_COUNT = "SAMPLE_COUNT"
    AVERAGE = "AVERAGE"
    SUM = "SUM"
    MINIMUM = "MINIMUM"
    MAXIMUM = "MAXIMUM"


@dataclasses.dataclass
class Step(ShapeBase):
    """
    This represents a step in a cluster.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "config",
                "Config",
                TypeInfo(HadoopStepConfig),
            ),
            (
                "action_on_failure",
                "ActionOnFailure",
                TypeInfo(typing.Union[str, ActionOnFailure]),
            ),
            (
                "status",
                "Status",
                TypeInfo(StepStatus),
            ),
        ]

    # The identifier of the cluster step.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster step.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Hadoop job configuration of the cluster step.
    config: "HadoopStepConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This specifies what action to take when the cluster step fails. Possible
    # values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE.
    action_on_failure: typing.Union[str, "ActionOnFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current execution status details of the cluster step.
    status: "StepStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StepConfig(ShapeBase):
    """
    Specification of a cluster (job flow) step.
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
                "hadoop_jar_step",
                "HadoopJarStep",
                TypeInfo(HadoopJarStepConfig),
            ),
            (
                "action_on_failure",
                "ActionOnFailure",
                TypeInfo(typing.Union[str, ActionOnFailure]),
            ),
        ]

    # The name of the step.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JAR file used for the step.
    hadoop_jar_step: "HadoopJarStepConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action to take if the step fails.
    action_on_failure: typing.Union[str, "ActionOnFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StepDetail(ShapeBase):
    """
    Combines the execution state and configuration of a step.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "step_config",
                "StepConfig",
                TypeInfo(StepConfig),
            ),
            (
                "execution_status_detail",
                "ExecutionStatusDetail",
                TypeInfo(StepExecutionStatusDetail),
            ),
        ]

    # The step configuration.
    step_config: "StepConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the step status.
    execution_status_detail: "StepExecutionStatusDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StepExecutionState(str):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    CONTINUE = "CONTINUE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    INTERRUPTED = "INTERRUPTED"


@dataclasses.dataclass
class StepExecutionStatusDetail(ShapeBase):
    """
    The execution state of a step.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, StepExecutionState]),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "start_date_time",
                "StartDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_state_change_reason",
                "LastStateChangeReason",
                TypeInfo(str),
            ),
        ]

    # The state of the step.
    state: typing.Union[str, "StepExecutionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date and time of the step.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start date and time of the step.
    start_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The completion date and time of the step.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the step's current state.
    last_state_change_reason: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StepState(str):
    PENDING = "PENDING"
    CANCEL_PENDING = "CANCEL_PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    INTERRUPTED = "INTERRUPTED"


@dataclasses.dataclass
class StepStateChangeReason(ShapeBase):
    """
    The details of the step state change reason.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(typing.Union[str, StepStateChangeReasonCode]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The programmable code for the state change reason. Note: Currently, the
    # service provides no code for the state change.
    code: typing.Union[str, "StepStateChangeReasonCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The descriptive message for the state change reason.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StepStateChangeReasonCode(str):
    NONE = "NONE"


@dataclasses.dataclass
class StepStatus(ShapeBase):
    """
    The execution status details of the cluster step.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, StepState]),
            ),
            (
                "state_change_reason",
                "StateChangeReason",
                TypeInfo(StepStateChangeReason),
            ),
            (
                "failure_details",
                "FailureDetails",
                TypeInfo(FailureDetails),
            ),
            (
                "timeline",
                "Timeline",
                TypeInfo(StepTimeline),
            ),
        ]

    # The execution state of the cluster step.
    state: typing.Union[str, "StepState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the step execution status change.
    state_change_reason: "StepStateChangeReason" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details for the step failure including reason, message, and log file
    # path where the root cause was identified.
    failure_details: "FailureDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeline of the cluster step status over time.
    timeline: "StepTimeline" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StepSummary(ShapeBase):
    """
    The summary of the cluster step.
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
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "config",
                "Config",
                TypeInfo(HadoopStepConfig),
            ),
            (
                "action_on_failure",
                "ActionOnFailure",
                TypeInfo(typing.Union[str, ActionOnFailure]),
            ),
            (
                "status",
                "Status",
                TypeInfo(StepStatus),
            ),
        ]

    # The identifier of the cluster step.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster step.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Hadoop job configuration of the cluster step.
    config: "HadoopStepConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This specifies what action to take when the cluster step fails. Possible
    # values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE.
    action_on_failure: typing.Union[str, "ActionOnFailure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current execution status details of the cluster step.
    status: "StepStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StepTimeline(ShapeBase):
    """
    The timeline of the cluster step lifecycle.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "start_date_time",
                "StartDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The date and time when the cluster step was created.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the cluster step execution started.
    start_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the cluster step execution completed or failed.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SupportedProductConfig(ShapeBase):
    """
    The list of supported product configurations which allow user-supplied
    arguments. EMR accepts these arguments and forwards them to the corresponding
    installation script as bootstrap action arguments.
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
                "args",
                "Args",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the product configuration.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of user-supplied arguments.
    args: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A key/value pair containing user-defined metadata that you can associate with an
    Amazon EMR resource. Tags make it easier to associate clusters in various ways,
    such as grouping clusters to track your Amazon EMR resource allocation costs.
    For more information, see [Tag
    Clusters](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-
    tags.html).
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

    # A user-defined key, which is the minimum required information for a valid
    # tag. For more information, see [Tag
    # ](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-
    # tags.html).
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-defined value, which is optional in a tag. For more information, see
    # [Tag Clusters](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-
    # plan-tags.html).
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateJobFlowsInput(ShapeBase):
    """
    Input to the TerminateJobFlows operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_flow_ids",
                "JobFlowIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of job flows to be shutdown.
    job_flow_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Unit(str):
    NONE = "NONE"
    SECONDS = "SECONDS"
    MICRO_SECONDS = "MICRO_SECONDS"
    MILLI_SECONDS = "MILLI_SECONDS"
    BYTES = "BYTES"
    KILO_BYTES = "KILO_BYTES"
    MEGA_BYTES = "MEGA_BYTES"
    GIGA_BYTES = "GIGA_BYTES"
    TERA_BYTES = "TERA_BYTES"
    BITS = "BITS"
    KILO_BITS = "KILO_BITS"
    MEGA_BITS = "MEGA_BITS"
    GIGA_BITS = "GIGA_BITS"
    TERA_BITS = "TERA_BITS"
    PERCENT = "PERCENT"
    COUNT = "COUNT"
    BYTES_PER_SECOND = "BYTES_PER_SECOND"
    KILO_BYTES_PER_SECOND = "KILO_BYTES_PER_SECOND"
    MEGA_BYTES_PER_SECOND = "MEGA_BYTES_PER_SECOND"
    GIGA_BYTES_PER_SECOND = "GIGA_BYTES_PER_SECOND"
    TERA_BYTES_PER_SECOND = "TERA_BYTES_PER_SECOND"
    BITS_PER_SECOND = "BITS_PER_SECOND"
    KILO_BITS_PER_SECOND = "KILO_BITS_PER_SECOND"
    MEGA_BITS_PER_SECOND = "MEGA_BITS_PER_SECOND"
    GIGA_BITS_PER_SECOND = "GIGA_BITS_PER_SECOND"
    TERA_BITS_PER_SECOND = "TERA_BITS_PER_SECOND"
    COUNT_PER_SECOND = "COUNT_PER_SECOND"


@dataclasses.dataclass
class VolumeSpecification(ShapeBase):
    """
    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_type",
                "VolumeType",
                TypeInfo(str),
            ),
            (
                "size_in_gb",
                "SizeInGB",
                TypeInfo(int),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
        ]

    # The volume type. Volume types supported are gp2, io1, standard.
    volume_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If
    # the volume type is EBS-optimized, the minimum value is 10.
    size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of I/O operations per second (IOPS) that the volume supports.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )
