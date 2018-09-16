import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AddTagsToOnPremisesInstancesInput(ShapeBase):
    """
    Represents the input of, and adds tags to, an on-premises instance operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The tag key-value pairs to add to the on-premises instances.

    # Keys and values are both required. Keys cannot be null or empty strings.
    # Value-only tags are not allowed.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the on-premises instances to which to add tags.
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Alarm(ShapeBase):
    """
    Information about an alarm.
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

    # The name of the alarm. Maximum length is 255 characters. Each alarm name
    # can be used only once in a list of alarms.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlarmConfiguration(ShapeBase):
    """
    Information about alarms associated with the deployment group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "enabled",
                TypeInfo(bool),
            ),
            (
                "ignore_poll_alarm_failure",
                "ignorePollAlarmFailure",
                TypeInfo(bool),
            ),
            (
                "alarms",
                "alarms",
                TypeInfo(typing.List[Alarm]),
            ),
        ]

    # Indicates whether the alarm configuration is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a deployment should continue if information about the
    # current state of alarms cannot be retrieved from Amazon CloudWatch. The
    # default value is false.

    #   * true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch.

    #   * false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch.
    ignore_poll_alarm_failure: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of alarms configured for the deployment group. A maximum of 10
    # alarms can be added to a deployment group.
    alarms: typing.List["Alarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AlarmsLimitExceededException(ShapeBase):
    """
    The maximum number of alarms for a deployment group (10) was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ApplicationAlreadyExistsException(ShapeBase):
    """
    An application with the specified name already exists with the applicable IAM
    user or AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ApplicationDoesNotExistException(ShapeBase):
    """
    The application does not exist with the applicable IAM user or AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ApplicationInfo(ShapeBase):
    """
    Information about an application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "applicationId",
                TypeInfo(str),
            ),
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "create_time",
                "createTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "linked_to_git_hub",
                "linkedToGitHub",
                TypeInfo(bool),
            ),
            (
                "git_hub_account_name",
                "gitHubAccountName",
                TypeInfo(str),
            ),
            (
                "compute_platform",
                "computePlatform",
                TypeInfo(typing.Union[str, ComputePlatform]),
            ),
        ]

    # The application ID.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the application was created.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if the user has authenticated with GitHub for the specified
    # application; otherwise, false.
    linked_to_git_hub: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for a connection to a GitHub account.
    git_hub_account_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination platform type for deployment of the application (`Lambda`
    # or `Server`).
    compute_platform: typing.Union[str, "ComputePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApplicationLimitExceededException(ShapeBase):
    """
    More applications were attempted to be created than are allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ApplicationNameRequiredException(ShapeBase):
    """
    The minimum number of required application names was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ApplicationRevisionSortBy(str):
    registerTime = "registerTime"
    firstUsedTime = "firstUsedTime"
    lastUsedTime = "lastUsedTime"


@dataclasses.dataclass
class AutoRollbackConfiguration(ShapeBase):
    """
    Information about a configuration for automatically rolling back to a previous
    version of an application revision when a deployment doesn't complete
    successfully.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "enabled",
                TypeInfo(bool),
            ),
            (
                "events",
                "events",
                TypeInfo(typing.List[typing.Union[str, AutoRollbackEvent]]),
            ),
        ]

    # Indicates whether a defined automatic rollback configuration is currently
    # enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event type or types that trigger a rollback.
    events: typing.List[typing.Union[str, "AutoRollbackEvent"]
                       ] = dataclasses.field(
                           default=ShapeBase.NOT_SET,
                       )


class AutoRollbackEvent(str):
    DEPLOYMENT_FAILURE = "DEPLOYMENT_FAILURE"
    DEPLOYMENT_STOP_ON_ALARM = "DEPLOYMENT_STOP_ON_ALARM"
    DEPLOYMENT_STOP_ON_REQUEST = "DEPLOYMENT_STOP_ON_REQUEST"


@dataclasses.dataclass
class AutoScalingGroup(ShapeBase):
    """
    Information about an Auto Scaling group.
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
                "hook",
                "hook",
                TypeInfo(str),
            ),
        ]

    # The Auto Scaling group name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Auto Scaling lifecycle event hook name.
    hook: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetApplicationRevisionsInput(ShapeBase):
    """
    Represents the input of a BatchGetApplicationRevisions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "revisions",
                "revisions",
                TypeInfo(typing.List[RevisionLocation]),
            ),
        ]

    # The name of an AWS CodeDeploy application about which to get revision
    # information.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information to get about the application revisions, including type and
    # location.
    revisions: typing.List["RevisionLocation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetApplicationRevisionsOutput(OutputShapeBase):
    """
    Represents the output of a BatchGetApplicationRevisions operation.
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
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                TypeInfo(str),
            ),
            (
                "revisions",
                "revisions",
                TypeInfo(typing.List[RevisionInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the application that corresponds to the revisions.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about errors that may have occurred during the API call.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about the revisions, including the type and
    # location.
    revisions: typing.List["RevisionInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetApplicationsInput(ShapeBase):
    """
    Represents the input of a BatchGetApplications operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_names",
                "applicationNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of application names separated by spaces.
    application_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetApplicationsOutput(OutputShapeBase):
    """
    Represents the output of a BatchGetApplications operation.
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
                "applications_info",
                "applicationsInfo",
                TypeInfo(typing.List[ApplicationInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the applications.
    applications_info: typing.List["ApplicationInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetDeploymentGroupsInput(ShapeBase):
    """
    Represents the input of a BatchGetDeploymentGroups operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_names",
                "deploymentGroupNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment groups' names.
    deployment_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetDeploymentGroupsOutput(OutputShapeBase):
    """
    Represents the output of a BatchGetDeploymentGroups operation.
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
                "deployment_groups_info",
                "deploymentGroupsInfo",
                TypeInfo(typing.List[DeploymentGroupInfo]),
            ),
            (
                "error_message",
                "errorMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the deployment groups.
    deployment_groups_info: typing.List["DeploymentGroupInfo"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Information about errors that may have occurred during the API call.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetDeploymentInstancesInput(ShapeBase):
    """
    Represents the input of a BatchGetDeploymentInstances operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "instance_ids",
                "instanceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of a deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique IDs of instances in the deployment group.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetDeploymentInstancesOutput(OutputShapeBase):
    """
    Represents the output of a BatchGetDeploymentInstances operation.
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
                "instances_summary",
                "instancesSummary",
                TypeInfo(typing.List[InstanceSummary]),
            ),
            (
                "error_message",
                "errorMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the instance.
    instances_summary: typing.List["InstanceSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about errors that may have occurred during the API call.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetDeploymentsInput(ShapeBase):
    """
    Represents the input of a BatchGetDeployments operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_ids",
                "deploymentIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of deployment IDs, separated by spaces.
    deployment_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetDeploymentsOutput(OutputShapeBase):
    """
    Represents the output of a BatchGetDeployments operation.
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
                "deployments_info",
                "deploymentsInfo",
                TypeInfo(typing.List[DeploymentInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the deployments.
    deployments_info: typing.List["DeploymentInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetOnPremisesInstancesInput(ShapeBase):
    """
    Represents the input of a BatchGetOnPremisesInstances operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the on-premises instances about which to get information.
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetOnPremisesInstancesOutput(OutputShapeBase):
    """
    Represents the output of a BatchGetOnPremisesInstances operation.
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
                "instance_infos",
                "instanceInfos",
                TypeInfo(typing.List[InstanceInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the on-premises instances.
    instance_infos: typing.List["InstanceInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchLimitExceededException(ShapeBase):
    """
    The maximum number of names or IDs allowed for this request (100) was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BlueGreenDeploymentConfiguration(ShapeBase):
    """
    Information about blue/green deployment options for a deployment group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "terminate_blue_instances_on_deployment_success",
                "terminateBlueInstancesOnDeploymentSuccess",
                TypeInfo(BlueInstanceTerminationOption),
            ),
            (
                "deployment_ready_option",
                "deploymentReadyOption",
                TypeInfo(DeploymentReadyOption),
            ),
            (
                "green_fleet_provisioning_option",
                "greenFleetProvisioningOption",
                TypeInfo(GreenFleetProvisioningOption),
            ),
        ]

    # Information about whether to terminate instances in the original fleet
    # during a blue/green deployment.
    terminate_blue_instances_on_deployment_success: "BlueInstanceTerminationOption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the action to take when newly provisioned instances are
    # ready to receive traffic in a blue/green deployment.
    deployment_ready_option: "DeploymentReadyOption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about how instances are provisioned for a replacement
    # environment in a blue/green deployment.
    green_fleet_provisioning_option: "GreenFleetProvisioningOption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BlueInstanceTerminationOption(ShapeBase):
    """
    Information about whether instances in the original environment are terminated
    when a blue/green deployment is successful.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "action",
                TypeInfo(typing.Union[str, InstanceAction]),
            ),
            (
                "termination_wait_time_in_minutes",
                "terminationWaitTimeInMinutes",
                TypeInfo(int),
            ),
        ]

    # The action to take on instances in the original environment after a
    # successful blue/green deployment.

    #   * TERMINATE: Instances are terminated after a specified wait time.

    #   * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
    action: typing.Union[str, "InstanceAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of minutes to wait after a successful blue/green deployment
    # before terminating instances from the original environment. The maximum
    # setting is 2880 minutes (2 days).
    termination_wait_time_in_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BucketNameFilterRequiredException(ShapeBase):
    """
    A bucket name is required, but was not provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class BundleType(str):
    tar = "tar"
    tgz = "tgz"
    zip = "zip"
    YAML = "YAML"
    JSON = "JSON"


class ComputePlatform(str):
    Server = "Server"
    Lambda = "Lambda"


@dataclasses.dataclass
class ContinueDeploymentInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
        ]

    # The deployment ID of the blue/green deployment for which you want to start
    # rerouting traffic to the replacement environment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationInput(ShapeBase):
    """
    Represents the input of a CreateApplication operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "compute_platform",
                "computePlatform",
                TypeInfo(typing.Union[str, ComputePlatform]),
            ),
        ]

    # The name of the application. This name must be unique with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination platform type for the deployment (`Lambda` or `Server`).
    compute_platform: typing.Union[str, "ComputePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateApplicationOutput(OutputShapeBase):
    """
    Represents the output of a CreateApplication operation.
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
                "application_id",
                "applicationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique application ID.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentConfigInput(ShapeBase):
    """
    Represents the input of a CreateDeploymentConfig operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "minimum_healthy_hosts",
                "minimumHealthyHosts",
                TypeInfo(MinimumHealthyHosts),
            ),
            (
                "traffic_routing_config",
                "trafficRoutingConfig",
                TypeInfo(TrafficRoutingConfig),
            ),
            (
                "compute_platform",
                "computePlatform",
                TypeInfo(typing.Union[str, ComputePlatform]),
            ),
        ]

    # The name of the deployment configuration to create.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum number of healthy instances that should be available at any
    # time during the deployment. There are two parameters expected in the input:
    # type and value.

    # The type parameter takes either of the following values:

    #   * HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.

    #   * FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.

    # The value parameter takes an integer.

    # For example, to set a minimum of 95% healthy instance, specify a type of
    # FLEET_PERCENT and a value of 95.
    minimum_healthy_hosts: "MinimumHealthyHosts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration that specifies how the deployment traffic will be routed.
    traffic_routing_config: "TrafficRoutingConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination platform type for the deployment (`Lambda` or `Server`>).
    compute_platform: typing.Union[str, "ComputePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDeploymentConfigOutput(OutputShapeBase):
    """
    Represents the output of a CreateDeploymentConfig operation.
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
                "deployment_config_id",
                "deploymentConfigId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique deployment configuration ID.
    deployment_config_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentGroupInput(ShapeBase):
    """
    Represents the input of a CreateDeploymentGroup operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                TypeInfo(str),
            ),
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "ec2_tag_filters",
                "ec2TagFilters",
                TypeInfo(typing.List[EC2TagFilter]),
            ),
            (
                "on_premises_instance_tag_filters",
                "onPremisesInstanceTagFilters",
                TypeInfo(typing.List[TagFilter]),
            ),
            (
                "auto_scaling_groups",
                "autoScalingGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "trigger_configurations",
                "triggerConfigurations",
                TypeInfo(typing.List[TriggerConfig]),
            ),
            (
                "alarm_configuration",
                "alarmConfiguration",
                TypeInfo(AlarmConfiguration),
            ),
            (
                "auto_rollback_configuration",
                "autoRollbackConfiguration",
                TypeInfo(AutoRollbackConfiguration),
            ),
            (
                "deployment_style",
                "deploymentStyle",
                TypeInfo(DeploymentStyle),
            ),
            (
                "blue_green_deployment_configuration",
                "blueGreenDeploymentConfiguration",
                TypeInfo(BlueGreenDeploymentConfiguration),
            ),
            (
                "load_balancer_info",
                "loadBalancerInfo",
                TypeInfo(LoadBalancerInfo),
            ),
            (
                "ec2_tag_set",
                "ec2TagSet",
                TypeInfo(EC2TagSet),
            ),
            (
                "on_premises_tag_set",
                "onPremisesTagSet",
                TypeInfo(OnPremisesTagSet),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a new deployment group for the specified application.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A service role ARN that allows AWS CodeDeploy to act on the user's behalf
    # when interacting with AWS services.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If specified, the deployment configuration name can be either one of the
    # predefined configurations provided with AWS CodeDeploy or a custom
    # deployment configuration that you create by calling the create deployment
    # configuration operation.

    # CodeDeployDefault.OneAtATime is the default deployment configuration. It is
    # used if a configuration isn't specified for the deployment or the
    # deployment group.

    # For more information about the predefined deployment configurations in AWS
    # CodeDeploy, see [Working with Deployment Groups in AWS
    # CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-
    # configurations.html) in the AWS CodeDeploy User Guide.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 tags on which to filter. The deployment group will include
    # EC2 instances with any of the specified tags. Cannot be used in the same
    # call as ec2TagSet.
    ec2_tag_filters: typing.List["EC2TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The on-premises instance tags on which to filter. The deployment group will
    # include on-premises instances with any of the specified tags. Cannot be
    # used in the same call as OnPremisesTagSet.
    on_premises_instance_tag_filters: typing.List["TagFilter"
                                                 ] = dataclasses.field(
                                                     default=ShapeBase.NOT_SET,
                                                 )

    # A list of associated Auto Scaling groups.
    auto_scaling_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about triggers to create when the deployment group is created.
    # For examples, see [Create a Trigger for an AWS CodeDeploy
    # Event](http://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-
    # notify-sns.html) in the AWS CodeDeploy User Guide.
    trigger_configurations: typing.List["TriggerConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information to add about Amazon CloudWatch alarms when the deployment group
    # is created.
    alarm_configuration: "AlarmConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Configuration information for an automatic rollback that is added when a
    # deployment group is created.
    auto_rollback_configuration: "AutoRollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the type of deployment, in-place or blue/green, that you
    # want to run and whether to route deployment traffic behind a load balancer.
    deployment_style: "DeploymentStyle" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about blue/green deployment options for a deployment group.
    blue_green_deployment_configuration: "BlueGreenDeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer used in a deployment.
    load_balancer_info: "LoadBalancerInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about groups of tags applied to EC2 instances. The deployment
    # group will include only EC2 instances identified by all the tag groups.
    # Cannot be used in the same call as ec2TagFilters.
    ec2_tag_set: "EC2TagSet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about groups of tags applied to on-premises instances. The
    # deployment group will include only on-premises instances identified by all
    # the tag groups. Cannot be used in the same call as
    # onPremisesInstanceTagFilters.
    on_premises_tag_set: "OnPremisesTagSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDeploymentGroupOutput(OutputShapeBase):
    """
    Represents the output of a CreateDeploymentGroup operation.
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
                "deployment_group_id",
                "deploymentGroupId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique deployment group ID.
    deployment_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentInput(ShapeBase):
    """
    Represents the input of a CreateDeployment operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
            (
                "revision",
                "revision",
                TypeInfo(RevisionLocation),
            ),
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "ignore_application_stop_failures",
                "ignoreApplicationStopFailures",
                TypeInfo(bool),
            ),
            (
                "target_instances",
                "targetInstances",
                TypeInfo(TargetInstances),
            ),
            (
                "auto_rollback_configuration",
                "autoRollbackConfiguration",
                TypeInfo(AutoRollbackConfiguration),
            ),
            (
                "update_outdated_instances_only",
                "updateOutdatedInstancesOnly",
                TypeInfo(bool),
            ),
            (
                "file_exists_behavior",
                "fileExistsBehavior",
                TypeInfo(typing.Union[str, FileExistsBehavior]),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the deployment group.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type and location of the revision to deploy.
    revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a deployment configuration associated with the applicable IAM
    # user or AWS account.

    # If not specified, the value configured in the deployment group will be used
    # as the default. If the deployment group does not have a deployment
    # configuration associated with it, then CodeDeployDefault.OneAtATime will be
    # used by default.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comment about the deployment.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to true, then if the deployment causes the ApplicationStop
    # deployment lifecycle event to an instance to fail, the deployment to that
    # instance will not be considered to have failed at that point and will
    # continue on to the BeforeInstall deployment lifecycle event.

    # If set to false or not specified, then if the deployment causes the
    # ApplicationStop deployment lifecycle event to fail to an instance, the
    # deployment to that instance will stop, and the deployment to that instance
    # will be considered to have failed.
    ignore_application_stop_failures: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the instances that will belong to the replacement
    # environment in a blue/green deployment.
    target_instances: "TargetInstances" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Configuration information for an automatic rollback that is added when a
    # deployment is created.
    auto_rollback_configuration: "AutoRollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether to deploy to all instances or only to instances that are
    # not running the latest application revision.
    update_outdated_instances_only: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about how AWS CodeDeploy handles files that already exist in a
    # deployment target location but weren't part of the previous successful
    # deployment.

    # The fileExistsBehavior parameter takes any of the following values:

    #   * DISALLOW: The deployment fails. This is also the default behavior if no option is specified.

    #   * OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.

    #   * RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.
    file_exists_behavior: typing.Union[str, "FileExistsBehavior"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class CreateDeploymentOutput(OutputShapeBase):
    """
    Represents the output of a CreateDeployment operation.
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
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique deployment ID.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApplicationInput(ShapeBase):
    """
    Represents the input of a DeleteApplication operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeploymentConfigInput(ShapeBase):
    """
    Represents the input of a DeleteDeploymentConfig operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of a deployment configuration associated with the applicable IAM
    # user or AWS account.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeploymentGroupInput(ShapeBase):
    """
    Represents the input of a DeleteDeploymentGroup operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an existing deployment group for the specified application.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeploymentGroupOutput(OutputShapeBase):
    """
    Represents the output of a DeleteDeploymentGroup operation.
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
                "hooks_not_cleaned_up",
                "hooksNotCleanedUp",
                TypeInfo(typing.List[AutoScalingGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output contains no data, and the corresponding deployment group
    # contained at least one Auto Scaling group, AWS CodeDeploy successfully
    # removed all corresponding Auto Scaling lifecycle event hooks from the
    # Amazon EC2 instances in the Auto Scaling group. If the output contains
    # data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event
    # hooks from the Amazon EC2 instances in the Auto Scaling group.
    hooks_not_cleaned_up: typing.List["AutoScalingGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteGitHubAccountTokenInput(ShapeBase):
    """
    Represents the input of a DeleteGitHubAccount operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "token_name",
                "tokenName",
                TypeInfo(str),
            ),
        ]

    # The name of the GitHub account connection to delete.
    token_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGitHubAccountTokenOutput(OutputShapeBase):
    """
    Represents the output of a DeleteGitHubAccountToken operation.
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
                "token_name",
                "tokenName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the GitHub account connection that was deleted.
    token_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeploymentAlreadyCompletedException(ShapeBase):
    """
    The deployment is already complete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentConfigAlreadyExistsException(ShapeBase):
    """
    A deployment configuration with the specified name already exists with the
    applicable IAM user or AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentConfigDoesNotExistException(ShapeBase):
    """
    The deployment configuration does not exist with the applicable IAM user or AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentConfigInUseException(ShapeBase):
    """
    The deployment configuration is still in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentConfigInfo(ShapeBase):
    """
    Information about a deployment configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_config_id",
                "deploymentConfigId",
                TypeInfo(str),
            ),
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "minimum_healthy_hosts",
                "minimumHealthyHosts",
                TypeInfo(MinimumHealthyHosts),
            ),
            (
                "create_time",
                "createTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "compute_platform",
                "computePlatform",
                TypeInfo(typing.Union[str, ComputePlatform]),
            ),
            (
                "traffic_routing_config",
                "trafficRoutingConfig",
                TypeInfo(TrafficRoutingConfig),
            ),
        ]

    # The deployment configuration ID.
    deployment_config_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment configuration name.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the number or percentage of minimum healthy instance.
    minimum_healthy_hosts: "MinimumHealthyHosts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the deployment configuration was created.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination platform type for the deployment (`Lambda` or `Server`).
    compute_platform: typing.Union[str, "ComputePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration specifying how the deployment traffic will be routed.
    # Only deployments with a Lambda compute platform can specify this.
    traffic_routing_config: "TrafficRoutingConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeploymentConfigLimitExceededException(ShapeBase):
    """
    The deployment configurations limit was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentConfigNameRequiredException(ShapeBase):
    """
    The deployment configuration name was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class DeploymentCreator(str):
    user = "user"
    autoscaling = "autoscaling"
    codeDeployRollback = "codeDeployRollback"


@dataclasses.dataclass
class DeploymentDoesNotExistException(ShapeBase):
    """
    The deployment does not exist with the applicable IAM user or AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentGroupAlreadyExistsException(ShapeBase):
    """
    A deployment group with the specified name already exists with the applicable
    IAM user or AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentGroupDoesNotExistException(ShapeBase):
    """
    The named deployment group does not exist with the applicable IAM user or AWS
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentGroupInfo(ShapeBase):
    """
    Information about a deployment group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_id",
                "deploymentGroupId",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "ec2_tag_filters",
                "ec2TagFilters",
                TypeInfo(typing.List[EC2TagFilter]),
            ),
            (
                "on_premises_instance_tag_filters",
                "onPremisesInstanceTagFilters",
                TypeInfo(typing.List[TagFilter]),
            ),
            (
                "auto_scaling_groups",
                "autoScalingGroups",
                TypeInfo(typing.List[AutoScalingGroup]),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                TypeInfo(str),
            ),
            (
                "target_revision",
                "targetRevision",
                TypeInfo(RevisionLocation),
            ),
            (
                "trigger_configurations",
                "triggerConfigurations",
                TypeInfo(typing.List[TriggerConfig]),
            ),
            (
                "alarm_configuration",
                "alarmConfiguration",
                TypeInfo(AlarmConfiguration),
            ),
            (
                "auto_rollback_configuration",
                "autoRollbackConfiguration",
                TypeInfo(AutoRollbackConfiguration),
            ),
            (
                "deployment_style",
                "deploymentStyle",
                TypeInfo(DeploymentStyle),
            ),
            (
                "blue_green_deployment_configuration",
                "blueGreenDeploymentConfiguration",
                TypeInfo(BlueGreenDeploymentConfiguration),
            ),
            (
                "load_balancer_info",
                "loadBalancerInfo",
                TypeInfo(LoadBalancerInfo),
            ),
            (
                "last_successful_deployment",
                "lastSuccessfulDeployment",
                TypeInfo(LastDeploymentInfo),
            ),
            (
                "last_attempted_deployment",
                "lastAttemptedDeployment",
                TypeInfo(LastDeploymentInfo),
            ),
            (
                "ec2_tag_set",
                "ec2TagSet",
                TypeInfo(EC2TagSet),
            ),
            (
                "on_premises_tag_set",
                "onPremisesTagSet",
                TypeInfo(OnPremisesTagSet),
            ),
            (
                "compute_platform",
                "computePlatform",
                TypeInfo(typing.Union[str, ComputePlatform]),
            ),
        ]

    # The application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment group ID.
    deployment_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment group name.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment configuration name.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 tags on which to filter. The deployment group includes EC2
    # instances with any of the specified tags.
    ec2_tag_filters: typing.List["EC2TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The on-premises instance tags on which to filter. The deployment group
    # includes on-premises instances with any of the specified tags.
    on_premises_instance_tag_filters: typing.List["TagFilter"
                                                 ] = dataclasses.field(
                                                     default=ShapeBase.NOT_SET,
                                                 )

    # A list of associated Auto Scaling groups.
    auto_scaling_groups: typing.List["AutoScalingGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A service role ARN.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the deployment group's target revision, including type
    # and location.
    target_revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about triggers associated with the deployment group.
    trigger_configurations: typing.List["TriggerConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of alarms associated with the deployment group.
    alarm_configuration: "AlarmConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the automatic rollback configuration associated with the
    # deployment group.
    auto_rollback_configuration: "AutoRollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the type of deployment, either in-place or blue/green,
    # you want to run and whether to route deployment traffic behind a load
    # balancer.
    deployment_style: "DeploymentStyle" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about blue/green deployment options for a deployment group.
    blue_green_deployment_configuration: "BlueGreenDeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer to use in a deployment.
    load_balancer_info: "LoadBalancerInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the most recent successful deployment to the deployment
    # group.
    last_successful_deployment: "LastDeploymentInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the most recent attempted deployment to the deployment
    # group.
    last_attempted_deployment: "LastDeploymentInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about groups of tags applied to an EC2 instance. The deployment
    # group includes only EC2 instances identified by all the tag groups. Cannot
    # be used in the same call as ec2TagFilters.
    ec2_tag_set: "EC2TagSet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about groups of tags applied to an on-premises instance. The
    # deployment group includes only on-premises instances identified by all the
    # tag groups. Cannot be used in the same call as
    # onPremisesInstanceTagFilters.
    on_premises_tag_set: "OnPremisesTagSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination platform type for the deployment group (`Lambda` or
    # `Server`).
    compute_platform: typing.Union[str, "ComputePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeploymentGroupLimitExceededException(ShapeBase):
    """
    The deployment groups limit was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentGroupNameRequiredException(ShapeBase):
    """
    The deployment group name was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentIdRequiredException(ShapeBase):
    """
    At least one deployment ID must be specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentInfo(ShapeBase):
    """
    Information about a deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "previous_revision",
                "previousRevision",
                TypeInfo(RevisionLocation),
            ),
            (
                "revision",
                "revision",
                TypeInfo(RevisionLocation),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, DeploymentStatus]),
            ),
            (
                "error_information",
                "errorInformation",
                TypeInfo(ErrorInformation),
            ),
            (
                "create_time",
                "createTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "complete_time",
                "completeTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "deployment_overview",
                "deploymentOverview",
                TypeInfo(DeploymentOverview),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "creator",
                "creator",
                TypeInfo(typing.Union[str, DeploymentCreator]),
            ),
            (
                "ignore_application_stop_failures",
                "ignoreApplicationStopFailures",
                TypeInfo(bool),
            ),
            (
                "auto_rollback_configuration",
                "autoRollbackConfiguration",
                TypeInfo(AutoRollbackConfiguration),
            ),
            (
                "update_outdated_instances_only",
                "updateOutdatedInstancesOnly",
                TypeInfo(bool),
            ),
            (
                "rollback_info",
                "rollbackInfo",
                TypeInfo(RollbackInfo),
            ),
            (
                "deployment_style",
                "deploymentStyle",
                TypeInfo(DeploymentStyle),
            ),
            (
                "target_instances",
                "targetInstances",
                TypeInfo(TargetInstances),
            ),
            (
                "instance_termination_wait_time_started",
                "instanceTerminationWaitTimeStarted",
                TypeInfo(bool),
            ),
            (
                "blue_green_deployment_configuration",
                "blueGreenDeploymentConfiguration",
                TypeInfo(BlueGreenDeploymentConfiguration),
            ),
            (
                "load_balancer_info",
                "loadBalancerInfo",
                TypeInfo(LoadBalancerInfo),
            ),
            (
                "additional_deployment_status_info",
                "additionalDeploymentStatusInfo",
                TypeInfo(str),
            ),
            (
                "file_exists_behavior",
                "fileExistsBehavior",
                TypeInfo(typing.Union[str, FileExistsBehavior]),
            ),
            (
                "deployment_status_messages",
                "deploymentStatusMessages",
                TypeInfo(typing.List[str]),
            ),
            (
                "compute_platform",
                "computePlatform",
                TypeInfo(typing.Union[str, ComputePlatform]),
            ),
        ]

    # The application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment group name.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment configuration name.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment ID.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the application revision that was deployed to the
    # deployment group before the most recent successful deployment.
    previous_revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the location of stored application artifacts and the
    # service from which to retrieve them.
    revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the deployment as a whole.
    status: typing.Union[str, "DeploymentStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about any error associated with this deployment.
    error_information: "ErrorInformation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp indicating when the deployment was created.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp indicating when the deployment was deployed to the deployment
    # group.

    # In some cases, the reported value of the start time may be later than the
    # complete time. This is due to differences in the clock settings of back-end
    # servers that participate in the deployment process.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp indicating when the deployment was complete.
    complete_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A summary of the deployment status of the instances in the deployment.
    deployment_overview: "DeploymentOverview" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A comment about the deployment.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The means by which the deployment was created:

    #   * user: A user created the deployment.

    #   * autoscaling: Auto Scaling created the deployment.

    #   * codeDeployRollback: A rollback process created the deployment.
    creator: typing.Union[str, "DeploymentCreator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If true, then if the deployment causes the ApplicationStop deployment
    # lifecycle event to an instance to fail, the deployment to that instance
    # will not be considered to have failed at that point and will continue on to
    # the BeforeInstall deployment lifecycle event.

    # If false or not specified, then if the deployment causes the
    # ApplicationStop deployment lifecycle event to an instance to fail, the
    # deployment to that instance will stop, and the deployment to that instance
    # will be considered to have failed.
    ignore_application_stop_failures: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the automatic rollback configuration associated with the
    # deployment.
    auto_rollback_configuration: "AutoRollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether only instances that are not running the latest
    # application revision are to be deployed to.
    update_outdated_instances_only: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a deployment rollback.
    rollback_info: "RollbackInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the type of deployment, either in-place or blue/green,
    # you want to run and whether to route deployment traffic behind a load
    # balancer.
    deployment_style: "DeploymentStyle" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the instances that belong to the replacement environment
    # in a blue/green deployment.
    target_instances: "TargetInstances" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the wait period set for the termination of instances in
    # the original environment has started. Status is 'false' if the KEEP_ALIVE
    # option is specified; otherwise, 'true' as soon as the termination wait
    # period starts.
    instance_termination_wait_time_started: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about blue/green deployment options for this deployment.
    blue_green_deployment_configuration: "BlueGreenDeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer used in the deployment.
    load_balancer_info: "LoadBalancerInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides information about the results of a deployment, such as whether
    # instances in the original environment in a blue/green deployment were not
    # terminated.
    additional_deployment_status_info: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about how AWS CodeDeploy handles files that already exist in a
    # deployment target location but weren't part of the previous successful
    # deployment.

    #   * DISALLOW: The deployment fails. This is also the default behavior if no option is specified.

    #   * OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.

    #   * RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.
    file_exists_behavior: typing.Union[str, "FileExistsBehavior"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Messages that contain information about the status of a deployment.
    deployment_status_messages: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The destination platform type for the deployment (`Lambda` or `Server`).
    compute_platform: typing.Union[str, "ComputePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeploymentIsNotInReadyStateException(ShapeBase):
    """
    The deployment does not have a status of Ready and can't continue yet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentLimitExceededException(ShapeBase):
    """
    The number of allowed deployments was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeploymentNotStartedException(ShapeBase):
    """
    The specified deployment has not started.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class DeploymentOption(str):
    WITH_TRAFFIC_CONTROL = "WITH_TRAFFIC_CONTROL"
    WITHOUT_TRAFFIC_CONTROL = "WITHOUT_TRAFFIC_CONTROL"


@dataclasses.dataclass
class DeploymentOverview(ShapeBase):
    """
    Information about the deployment status of the instances in the deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pending",
                "Pending",
                TypeInfo(int),
            ),
            (
                "in_progress",
                "InProgress",
                TypeInfo(int),
            ),
            (
                "succeeded",
                "Succeeded",
                TypeInfo(int),
            ),
            (
                "failed",
                "Failed",
                TypeInfo(int),
            ),
            (
                "skipped",
                "Skipped",
                TypeInfo(int),
            ),
            (
                "ready",
                "Ready",
                TypeInfo(int),
            ),
        ]

    # The number of instances in the deployment in a pending state.
    pending: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances in which the deployment is in progress.
    in_progress: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances in the deployment to which revisions have been
    # successfully deployed.
    succeeded: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances in the deployment in a failed state.
    failed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances in the deployment in a skipped state.
    skipped: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances in a replacement environment ready to receive
    # traffic in a blue/green deployment.
    ready: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class DeploymentReadyAction(str):
    CONTINUE_DEPLOYMENT = "CONTINUE_DEPLOYMENT"
    STOP_DEPLOYMENT = "STOP_DEPLOYMENT"


@dataclasses.dataclass
class DeploymentReadyOption(ShapeBase):
    """
    Information about how traffic is rerouted to instances in a replacement
    environment in a blue/green deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_on_timeout",
                "actionOnTimeout",
                TypeInfo(typing.Union[str, DeploymentReadyAction]),
            ),
            (
                "wait_time_in_minutes",
                "waitTimeInMinutes",
                TypeInfo(int),
            ),
        ]

    # Information about when to reroute traffic from an original environment to a
    # replacement environment in a blue/green deployment.

    #   * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.

    #   * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using ContinueDeployment. If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.
    action_on_timeout: typing.Union[str, "DeploymentReadyAction"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The number of minutes to wait before the status of a blue/green deployment
    # changed to Stopped if rerouting is not started manually. Applies only to
    # the STOP_DEPLOYMENT option for actionOnTimeout
    wait_time_in_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class DeploymentStatus(str):
    Created = "Created"
    Queued = "Queued"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Stopped = "Stopped"
    Ready = "Ready"


@dataclasses.dataclass
class DeploymentStyle(ShapeBase):
    """
    Information about the type of deployment, either in-place or blue/green, you
    want to run and whether to route deployment traffic behind a load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_type",
                "deploymentType",
                TypeInfo(typing.Union[str, DeploymentType]),
            ),
            (
                "deployment_option",
                "deploymentOption",
                TypeInfo(typing.Union[str, DeploymentOption]),
            ),
        ]

    # Indicates whether to run an in-place deployment or a blue/green deployment.
    deployment_type: typing.Union[str, "DeploymentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether to route deployment traffic behind a load balancer.
    deployment_option: typing.Union[str, "DeploymentOption"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


class DeploymentType(str):
    IN_PLACE = "IN_PLACE"
    BLUE_GREEN = "BLUE_GREEN"


@dataclasses.dataclass
class DeregisterOnPremisesInstanceInput(ShapeBase):
    """
    Represents the input of a DeregisterOnPremisesInstance operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the on-premises instance to deregister.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescriptionTooLongException(ShapeBase):
    """
    The description is too long.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Diagnostics(ShapeBase):
    """
    Diagnostic information about executable scripts that are part of a deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, LifecycleErrorCode]),
            ),
            (
                "script_name",
                "scriptName",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "log_tail",
                "logTail",
                TypeInfo(str),
            ),
        ]

    # The associated error code:

    #   * Success: The specified script ran.

    #   * ScriptMissing: The specified script was not found in the specified location.

    #   * ScriptNotExecutable: The specified script is not a recognized executable file type.

    #   * ScriptTimedOut: The specified script did not finish running in the specified time period.

    #   * ScriptFailed: The specified script failed to run as expected.

    #   * UnknownError: The specified script did not run for an unknown reason.
    error_code: typing.Union[str, "LifecycleErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the script.
    script_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message associated with the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last portion of the diagnostic log.

    # If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
    # log.
    log_tail: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2TagFilter(ShapeBase):
    """
    Information about an EC2 tag filter.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, EC2TagFilterType]),
            ),
        ]

    # The tag filter key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag filter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag filter type:

    #   * KEY_ONLY: Key only.

    #   * VALUE_ONLY: Value only.

    #   * KEY_AND_VALUE: Key and value.
    type: typing.Union[str, "EC2TagFilterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EC2TagFilterType(str):
    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


@dataclasses.dataclass
class EC2TagSet(ShapeBase):
    """
    Information about groups of EC2 instance tags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ec2_tag_set_list",
                "ec2TagSetList",
                TypeInfo(typing.List[typing.List[EC2TagFilter]]),
            ),
        ]

    # A list containing other lists of EC2 instance tag groups. In order for an
    # instance to be included in the deployment group, it must be identified by
    # all the tag groups in the list.
    ec2_tag_set_list: typing.List[typing.List["EC2TagFilter"]
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class ELBInfo(ShapeBase):
    """
    Information about a load balancer in Elastic Load Balancing to use in a
    deployment. Instances are registered directly with a load balancer, and traffic
    is routed to the load balancer.
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

    # For blue/green deployments, the name of the load balancer that will be used
    # to route traffic from original instances to replacement instances in a
    # blue/green deployment. For in-place deployments, the name of the load
    # balancer that instances are deregistered from so they are not serving
    # traffic during a deployment, and then re-registered with after the
    # deployment completes.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ErrorCode(str):
    DEPLOYMENT_GROUP_MISSING = "DEPLOYMENT_GROUP_MISSING"
    APPLICATION_MISSING = "APPLICATION_MISSING"
    REVISION_MISSING = "REVISION_MISSING"
    IAM_ROLE_MISSING = "IAM_ROLE_MISSING"
    IAM_ROLE_PERMISSIONS = "IAM_ROLE_PERMISSIONS"
    NO_EC2_SUBSCRIPTION = "NO_EC2_SUBSCRIPTION"
    OVER_MAX_INSTANCES = "OVER_MAX_INSTANCES"
    NO_INSTANCES = "NO_INSTANCES"
    TIMEOUT = "TIMEOUT"
    HEALTH_CONSTRAINTS_INVALID = "HEALTH_CONSTRAINTS_INVALID"
    HEALTH_CONSTRAINTS = "HEALTH_CONSTRAINTS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    THROTTLED = "THROTTLED"
    ALARM_ACTIVE = "ALARM_ACTIVE"
    AGENT_ISSUE = "AGENT_ISSUE"
    AUTO_SCALING_IAM_ROLE_PERMISSIONS = "AUTO_SCALING_IAM_ROLE_PERMISSIONS"
    AUTO_SCALING_CONFIGURATION = "AUTO_SCALING_CONFIGURATION"
    MANUAL_STOP = "MANUAL_STOP"
    MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION = "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION"
    MISSING_ELB_INFORMATION = "MISSING_ELB_INFORMATION"
    MISSING_GITHUB_TOKEN = "MISSING_GITHUB_TOKEN"
    ELASTIC_LOAD_BALANCING_INVALID = "ELASTIC_LOAD_BALANCING_INVALID"
    ELB_INVALID_INSTANCE = "ELB_INVALID_INSTANCE"
    INVALID_LAMBDA_CONFIGURATION = "INVALID_LAMBDA_CONFIGURATION"
    INVALID_LAMBDA_FUNCTION = "INVALID_LAMBDA_FUNCTION"
    HOOK_EXECUTION_FAILURE = "HOOK_EXECUTION_FAILURE"


@dataclasses.dataclass
class ErrorInformation(ShapeBase):
    """
    Information about a deployment error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(typing.Union[str, ErrorCode]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # For information about additional error codes, see [Error Codes for AWS
    # CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/error-
    # codes.html) in the [AWS CodeDeploy User
    # Guide](http://docs.aws.amazon.com/codedeploy/latest/userguide).

    # The error code:

    #   * APPLICATION_MISSING: The application was missing. This error code will most likely be raised if the application is deleted after the deployment is created but before it is started.

    #   * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code will most likely be raised if the deployment group is deleted after the deployment is created but before it is started.

    #   * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.

    #   * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.

    #   * IAM_ROLE_MISSING: The service role cannot be accessed.

    #   * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

    #   * INTERNAL_ERROR: There was an internal error.

    #   * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to the Amazon EC2 service.

    #   * NO_INSTANCES: No instance were specified, or no instance can be found.

    #   * OVER_MAX_INSTANCES: The maximum number of instance was exceeded.

    #   * THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services.

    #   * TIMEOUT: The deployment has timed out.

    #   * REVISION_MISSING: The revision ID was missing. This error code will most likely be raised if the revision is deleted after the deployment is created but before it is started.
    code: typing.Union[str, "ErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An accompanying error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FileExistsBehavior(str):
    DISALLOW = "DISALLOW"
    OVERWRITE = "OVERWRITE"
    RETAIN = "RETAIN"


@dataclasses.dataclass
class GenericRevisionInfo(ShapeBase):
    """
    Information about an application revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "deployment_groups",
                "deploymentGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "first_used_time",
                "firstUsedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_used_time",
                "lastUsedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "register_time",
                "registerTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A comment about the revision.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment groups for which this is the current target revision.
    deployment_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the revision was first used by AWS CodeDeploy.
    first_used_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the revision was last used by AWS CodeDeploy.
    last_used_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the revision was registered with AWS CodeDeploy.
    register_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApplicationInput(ShapeBase):
    """
    Represents the input of a GetApplication operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApplicationOutput(OutputShapeBase):
    """
    Represents the output of a GetApplication operation.
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
                "application",
                "application",
                TypeInfo(ApplicationInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the application.
    application: "ApplicationInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApplicationRevisionInput(ShapeBase):
    """
    Represents the input of a GetApplicationRevision operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "revision",
                "revision",
                TypeInfo(RevisionLocation),
            ),
        ]

    # The name of the application that corresponds to the revision.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the application revision to get, including type and
    # location.
    revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApplicationRevisionOutput(OutputShapeBase):
    """
    Represents the output of a GetApplicationRevision operation.
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
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "revision",
                "revision",
                TypeInfo(RevisionLocation),
            ),
            (
                "revision_info",
                "revisionInfo",
                TypeInfo(GenericRevisionInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the application that corresponds to the revision.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about the revision, including type and location.
    revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # General information about the revision.
    revision_info: "GenericRevisionInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeploymentConfigInput(ShapeBase):
    """
    Represents the input of a GetDeploymentConfig operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of a deployment configuration associated with the applicable IAM
    # user or AWS account.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentConfigOutput(OutputShapeBase):
    """
    Represents the output of a GetDeploymentConfig operation.
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
                "deployment_config_info",
                "deploymentConfigInfo",
                TypeInfo(DeploymentConfigInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the deployment configuration.
    deployment_config_info: "DeploymentConfigInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeploymentGroupInput(ShapeBase):
    """
    Represents the input of a GetDeploymentGroup operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an existing deployment group for the specified application.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentGroupOutput(OutputShapeBase):
    """
    Represents the output of a GetDeploymentGroup operation.
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
                "deployment_group_info",
                "deploymentGroupInfo",
                TypeInfo(DeploymentGroupInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the deployment group.
    deployment_group_info: "DeploymentGroupInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeploymentInput(ShapeBase):
    """
    Represents the input of a GetDeployment operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
        ]

    # A deployment ID associated with the applicable IAM user or AWS account.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentInstanceInput(ShapeBase):
    """
    Represents the input of a GetDeploymentInstance operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "instanceId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of a deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of an instance in the deployment group.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentInstanceOutput(OutputShapeBase):
    """
    Represents the output of a GetDeploymentInstance operation.
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
                "instance_summary",
                "instanceSummary",
                TypeInfo(InstanceSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the instance.
    instance_summary: "InstanceSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeploymentOutput(OutputShapeBase):
    """
    Represents the output of a GetDeployment operation.
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
                "deployment_info",
                "deploymentInfo",
                TypeInfo(DeploymentInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the deployment.
    deployment_info: "DeploymentInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOnPremisesInstanceInput(ShapeBase):
    """
    Represents the input of a GetOnPremisesInstance operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the on-premises instance about which to get information.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOnPremisesInstanceOutput(OutputShapeBase):
    """
    Represents the output of a GetOnPremisesInstance operation.
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
                "instance_info",
                "instanceInfo",
                TypeInfo(InstanceInfo),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the on-premises instance.
    instance_info: "InstanceInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GitHubAccountTokenDoesNotExistException(ShapeBase):
    """
    No GitHub account connection exists with the named specified in the call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GitHubAccountTokenNameRequiredException(ShapeBase):
    """
    The call is missing a required GitHub account connection name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GitHubLocation(ShapeBase):
    """
    Information about the location of application artifacts stored in GitHub.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository",
                "repository",
                TypeInfo(str),
            ),
            (
                "commit_id",
                "commitId",
                TypeInfo(str),
            ),
        ]

    # The GitHub account and repository pair that stores a reference to the
    # commit that represents the bundled artifacts for the application revision.

    # Specified as account/repository.
    repository: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SHA1 commit ID of the GitHub commit that represents the bundled
    # artifacts for the application revision.
    commit_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class GreenFleetProvisioningAction(str):
    DISCOVER_EXISTING = "DISCOVER_EXISTING"
    COPY_AUTO_SCALING_GROUP = "COPY_AUTO_SCALING_GROUP"


@dataclasses.dataclass
class GreenFleetProvisioningOption(ShapeBase):
    """
    Information about the instances that belong to the replacement environment in a
    blue/green deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "action",
                TypeInfo(typing.Union[str, GreenFleetProvisioningAction]),
            ),
        ]

    # The method used to add instances to a replacement environment.

    #   * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

    #   * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.
    action: typing.Union[str, "GreenFleetProvisioningAction"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


@dataclasses.dataclass
class IamArnRequiredException(ShapeBase):
    """
    No IAM ARN was included in the request. You must use an IAM session ARN or IAM
    user ARN in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IamSessionArnAlreadyRegisteredException(ShapeBase):
    """
    The request included an IAM session ARN that has already been used to register a
    different instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IamUserArnAlreadyRegisteredException(ShapeBase):
    """
    The specified IAM user ARN is already registered with an on-premises instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IamUserArnRequiredException(ShapeBase):
    """
    An IAM user ARN was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class InstanceAction(str):
    TERMINATE = "TERMINATE"
    KEEP_ALIVE = "KEEP_ALIVE"


@dataclasses.dataclass
class InstanceDoesNotExistException(ShapeBase):
    """
    The specified instance does not exist in the deployment group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InstanceIdRequiredException(ShapeBase):
    """
    The instance ID was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InstanceInfo(ShapeBase):
    """
    Information about an on-premises instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "iam_session_arn",
                "iamSessionArn",
                TypeInfo(str),
            ),
            (
                "iam_user_arn",
                "iamUserArn",
                TypeInfo(str),
            ),
            (
                "instance_arn",
                "instanceArn",
                TypeInfo(str),
            ),
            (
                "register_time",
                "registerTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "deregister_time",
                "deregisterTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the on-premises instance.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM session associated with the on-premises instance.
    iam_session_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM user ARN associated with the on-premises instance.
    iam_user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the on-premises instance.
    instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the on-premises instance was registered.
    register_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the on-premises instance was deregistered, the time at which the on-
    # premises instance was deregistered.
    deregister_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags currently associated with the on-premises instance.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceLimitExceededException(ShapeBase):
    """
    The maximum number of allowed on-premises instances in a single call was
    exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InstanceNameAlreadyRegisteredException(ShapeBase):
    """
    The specified on-premises instance name is already registered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InstanceNameRequiredException(ShapeBase):
    """
    An on-premises instance name was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InstanceNotRegisteredException(ShapeBase):
    """
    The specified on-premises instance is not registered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class InstanceStatus(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"
    Ready = "Ready"


@dataclasses.dataclass
class InstanceSummary(ShapeBase):
    """
    Information about an instance in a deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "instanceId",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, InstanceStatus]),
            ),
            (
                "last_updated_at",
                "lastUpdatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "lifecycle_events",
                "lifecycleEvents",
                TypeInfo(typing.List[LifecycleEvent]),
            ),
            (
                "instance_type",
                "instanceType",
                TypeInfo(typing.Union[str, InstanceType]),
            ),
        ]

    # The deployment ID.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance ID.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment status for this instance:

    #   * Pending: The deployment is pending for this instance.

    #   * In Progress: The deployment is in progress for this instance.

    #   * Succeeded: The deployment has succeeded for this instance.

    #   * Failed: The deployment has failed for this instance.

    #   * Skipped: The deployment has been skipped for this instance.

    #   * Unknown: The deployment status is unknown for this instance.
    status: typing.Union[str, "InstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp indicating when the instance information was last updated.
    last_updated_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of lifecycle events for this instance.
    lifecycle_events: typing.List["LifecycleEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about which environment an instance belongs to in a blue/green
    # deployment.

    #   * BLUE: The instance is part of the original environment.

    #   * GREEN: The instance is part of the replacement environment.
    instance_type: typing.Union[str, "InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceType(str):
    Blue = "Blue"
    Green = "Green"


@dataclasses.dataclass
class InvalidAlarmConfigException(ShapeBase):
    """
    The format of the alarm configuration is invalid. Possible causes include:

      * The alarm list is null.

      * The alarm object is null.

      * The alarm name is empty or null or exceeds the 255 character limit.

      * Two alarms with the same name have been specified.

      * The alarm configuration is enabled but the alarm list is empty.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidApplicationNameException(ShapeBase):
    """
    The application name was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidAutoRollbackConfigException(ShapeBase):
    """
    The automatic rollback configuration was specified in an invalid format. For
    example, automatic rollback is enabled but an invalid triggering event type or
    no event types were listed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidAutoScalingGroupException(ShapeBase):
    """
    The Auto Scaling group was specified in an invalid format or does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBlueGreenDeploymentConfigurationException(ShapeBase):
    """
    The configuration for the blue/green deployment group was provided in an invalid
    format. For information about deployment configuration format, see
    CreateDeploymentConfig.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBucketNameFilterException(ShapeBase):
    """
    The bucket name either doesn't exist or was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidComputePlatformException(ShapeBase):
    """
    The computePlatform is invalid. The computePlatform should be `Lambda` or
    `Server`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeployedStateFilterException(ShapeBase):
    """
    The deployed state filter was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeploymentConfigNameException(ShapeBase):
    """
    The deployment configuration name was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeploymentGroupNameException(ShapeBase):
    """
    The deployment group name was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeploymentIdException(ShapeBase):
    """
    At least one of the deployment IDs was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeploymentInstanceTypeException(ShapeBase):
    """
    An instance type was specified for an in-place deployment. Instance types are
    supported for blue/green deployments only.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeploymentStatusException(ShapeBase):
    """
    The specified deployment status doesn't exist or cannot be determined.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDeploymentStyleException(ShapeBase):
    """
    An invalid deployment style was specified. Valid deployment types include
    "IN_PLACE" and "BLUE_GREEN". Valid deployment options include
    "WITH_TRAFFIC_CONTROL" and "WITHOUT_TRAFFIC_CONTROL".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEC2TagCombinationException(ShapeBase):
    """
    A call was submitted that specified both Ec2TagFilters and Ec2TagSet, but only
    one of these data types can be used in a single call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEC2TagException(ShapeBase):
    """
    The tag was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFileExistsBehaviorException(ShapeBase):
    """
    An invalid fileExistsBehavior option was specified to determine how AWS
    CodeDeploy handles files or directories that already exist in a deployment
    target location but weren't part of the previous successful deployment. Valid
    values include "DISALLOW", "OVERWRITE", and "RETAIN".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidGitHubAccountTokenException(ShapeBase):
    """
    The GitHub token is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidGitHubAccountTokenNameException(ShapeBase):
    """
    The format of the specified GitHub account connection name is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidIamSessionArnException(ShapeBase):
    """
    The IAM session ARN was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidIamUserArnException(ShapeBase):
    """
    The IAM user ARN was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidIgnoreApplicationStopFailuresValueException(ShapeBase):
    """
    The IgnoreApplicationStopFailures value is invalid. For AWS Lambda deployments,
    `false` is expected. For EC2/On-premises deployments, `true` or `false` is
    expected.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidInputException(ShapeBase):
    """
    The specified input was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidInstanceIdException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidInstanceNameException(ShapeBase):
    """
    The specified on-premises instance name was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidInstanceStatusException(ShapeBase):
    """
    The specified instance status does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidInstanceTypeException(ShapeBase):
    """
    An invalid instance type was specified for instances in a blue/green deployment.
    Valid values include "Blue" for an original environment and "Green" for a
    replacement environment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidKeyPrefixFilterException(ShapeBase):
    """
    The specified key prefix filter was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidLifecycleEventHookExecutionIdException(ShapeBase):
    """
    A lifecycle event hook is invalid. Review the `hooks` section in your AppSpec
    file to ensure the lifecycle events and `hooks` functions are valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidLifecycleEventHookExecutionStatusException(ShapeBase):
    """
    The result of a Lambda validation function that verifies a lifecycle event is
    invalid. It should return `Succeeded` or `Failed`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidLoadBalancerInfoException(ShapeBase):
    """
    An invalid load balancer name, or no load balancer name, was specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMinimumHealthyHostValueException(ShapeBase):
    """
    The minimum healthy instance value was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    The next token was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOnPremisesTagCombinationException(ShapeBase):
    """
    A call was submitted that specified both OnPremisesTagFilters and
    OnPremisesTagSet, but only one of these data types can be used in a single call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOperationException(ShapeBase):
    """
    An invalid operation was detected.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRegistrationStatusException(ShapeBase):
    """
    The registration status was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRevisionException(ShapeBase):
    """
    The revision was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRoleException(ShapeBase):
    """
    The service role ARN was specified in an invalid format. Or, if an Auto Scaling
    group was specified, the specified service role does not grant the appropriate
    permissions to Auto Scaling.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSortByException(ShapeBase):
    """
    The column name to sort by is either not present or was specified in an invalid
    format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSortOrderException(ShapeBase):
    """
    The sort order was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTagException(ShapeBase):
    """
    The specified tag was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTagFilterException(ShapeBase):
    """
    The specified tag filter was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTargetInstancesException(ShapeBase):
    """
    The target instance configuration is invalid. Possible causes include:

      * Configuration data for target instances was entered for an in-place deployment.

      * The limit of 10 tags for a tag type was exceeded.

      * The combined length of the tag names exceeded the limit. 

      * A specified tag is not currently applied to any instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTimeRangeException(ShapeBase):
    """
    The specified time range was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTrafficRoutingConfigurationException(ShapeBase):
    """
    The configuration that specifies how traffic is routed during a deployment is
    invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTriggerConfigException(ShapeBase):
    """
    The trigger was specified in an invalid format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidUpdateOutdatedInstancesOnlyValueException(ShapeBase):
    """
    The UpdateOutdatedInstancesOnly value is invalid. For AWS Lambda deployments,
    `false` is expected. For EC2/On-premises deployments, `true` or `false` is
    expected.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LastDeploymentInfo(ShapeBase):
    """
    Information about the most recent attempted or successful deployment to a
    deployment group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, DeploymentStatus]),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "create_time",
                "createTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The deployment ID.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the most recent deployment.
    status: typing.Union[str, "DeploymentStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp indicating when the most recent deployment to the deployment
    # group completed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp indicating when the most recent deployment to the deployment
    # group started.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LifecycleErrorCode(str):
    Success = "Success"
    ScriptMissing = "ScriptMissing"
    ScriptNotExecutable = "ScriptNotExecutable"
    ScriptTimedOut = "ScriptTimedOut"
    ScriptFailed = "ScriptFailed"
    UnknownError = "UnknownError"


@dataclasses.dataclass
class LifecycleEvent(ShapeBase):
    """
    Information about a deployment lifecycle event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_event_name",
                "lifecycleEventName",
                TypeInfo(str),
            ),
            (
                "diagnostics",
                "diagnostics",
                TypeInfo(Diagnostics),
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
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, LifecycleEventStatus]),
            ),
        ]

    # The deployment lifecycle event name, such as ApplicationStop,
    # BeforeInstall, AfterInstall, ApplicationStart, or ValidateService.
    lifecycle_event_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Diagnostic information about the deployment lifecycle event.
    diagnostics: "Diagnostics" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp indicating when the deployment lifecycle event started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp indicating when the deployment lifecycle event ended.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment lifecycle event status:

    #   * Pending: The deployment lifecycle event is pending.

    #   * InProgress: The deployment lifecycle event is in progress.

    #   * Succeeded: The deployment lifecycle event ran successfully.

    #   * Failed: The deployment lifecycle event has failed.

    #   * Skipped: The deployment lifecycle event has been skipped.

    #   * Unknown: The deployment lifecycle event is unknown.
    status: typing.Union[str, "LifecycleEventStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecycleEventAlreadyCompletedException(ShapeBase):
    """
    An attempt to return the status of an already completed lifecycle event
    occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class LifecycleEventStatus(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"


@dataclasses.dataclass
class LifecycleHookLimitExceededException(ShapeBase):
    """
    The limit for lifecycle hooks was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListApplicationRevisionsInput(ShapeBase):
    """
    Represents the input of a ListApplicationRevisions operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "sort_by",
                "sortBy",
                TypeInfo(typing.Union[str, ApplicationRevisionSortBy]),
            ),
            (
                "sort_order",
                "sortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "s3_bucket",
                "s3Bucket",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "s3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "deployed",
                "deployed",
                TypeInfo(typing.Union[str, ListStateFilterAction]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The column name to use to sort the list results:

    #   * registerTime: Sort by the time the revisions were registered with AWS CodeDeploy.

    #   * firstUsedTime: Sort by the time the revisions were first used in a deployment.

    #   * lastUsedTime: Sort by the time the revisions were last used in a deployment.

    # If not specified or set to null, the results will be returned in an
    # arbitrary order.
    sort_by: typing.Union[str, "ApplicationRevisionSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order in which to sort the list results:

    #   * ascending: ascending order.

    #   * descending: descending order.

    # If not specified, the results will be sorted in ascending order.

    # If set to null, the results will be sorted in an arbitrary order.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An Amazon S3 bucket name to limit the search for revisions.

    # If set to null, all of the user's buckets will be searched.
    s3_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A key prefix for the set of Amazon S3 objects to limit the search for
    # revisions.
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to list revisions based on whether the revision is the target
    # revision of an deployment group:

    #   * include: List revisions that are target revisions of a deployment group.

    #   * exclude: Do not list revisions that are target revisions of a deployment group.

    #   * ignore: List all revisions.
    deployed: typing.Union[str, "ListStateFilterAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier returned from the previous list application revisions call.
    # It can be used to return the next set of applications in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListApplicationRevisionsOutput(OutputShapeBase):
    """
    Represents the output of a ListApplicationRevisions operation.
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
                "revisions",
                "revisions",
                TypeInfo(typing.List[RevisionLocation]),
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

    # A list of locations that contain the matching revisions.
    revisions: typing.List["RevisionLocation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier will also be
    # returned. It can be used in a subsequent list application revisions call to
    # return the next set of application revisions in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListApplicationRevisionsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListApplicationsInput(ShapeBase):
    """
    Represents the input of a ListApplications operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier returned from the previous list applications call. It can be
    # used to return the next set of applications in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListApplicationsOutput(OutputShapeBase):
    """
    Represents the output of a ListApplications operation.
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
                "applications",
                "applications",
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

    # A list of application names.
    applications: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent list applications call to return
    # the next set of applications, will also be returned. in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListApplicationsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDeploymentConfigsInput(ShapeBase):
    """
    Represents the input of a ListDeploymentConfigs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier returned from the previous list deployment configurations
    # call. It can be used to return the next set of deployment configurations in
    # the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeploymentConfigsOutput(OutputShapeBase):
    """
    Represents the output of a ListDeploymentConfigs operation.
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
                "deployment_configs_list",
                "deploymentConfigsList",
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

    # A list of deployment configurations, including built-in configurations such
    # as CodeDeployDefault.OneAtATime.
    deployment_configs_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent list deployment configurations
    # call to return the next set of deployment configurations in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListDeploymentConfigsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDeploymentGroupsInput(ShapeBase):
    """
    Represents the input of a ListDeploymentGroups operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier returned from the previous list deployment groups call. It
    # can be used to return the next set of deployment groups in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeploymentGroupsOutput(OutputShapeBase):
    """
    Represents the output of a ListDeploymentGroups operation.
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
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_groups",
                "deploymentGroups",
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

    # The application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of corresponding deployment group names.
    deployment_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent list deployment groups call to
    # return the next set of deployment groups in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDeploymentGroupsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDeploymentInstancesInput(ShapeBase):
    """
    Represents the input of a ListDeploymentInstances operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "instance_status_filter",
                "instanceStatusFilter",
                TypeInfo(typing.List[typing.Union[str, InstanceStatus]]),
            ),
            (
                "instance_type_filter",
                "instanceTypeFilter",
                TypeInfo(typing.List[typing.Union[str, InstanceType]]),
            ),
        ]

    # The unique ID of a deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier returned from the previous list deployment instances call. It
    # can be used to return the next set of deployment instances in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subset of instances to list by status:

    #   * Pending: Include those instance with pending deployments.

    #   * InProgress: Include those instance where deployments are still in progress.

    #   * Succeeded: Include those instances with successful deployments.

    #   * Failed: Include those instance with failed deployments.

    #   * Skipped: Include those instance with skipped deployments.

    #   * Unknown: Include those instance with deployments in an unknown state.
    instance_status_filter: typing.List[typing.Union[str, "InstanceStatus"]
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The set of instances in a blue/green deployment, either those in the
    # original environment ("BLUE") or those in the replacement environment
    # ("GREEN"), for which you want to view instance information.
    instance_type_filter: typing.List[typing.Union[str, "InstanceType"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class ListDeploymentInstancesOutput(OutputShapeBase):
    """
    Represents the output of a ListDeploymentInstances operation.
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
                "instances_list",
                "instancesList",
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

    # A list of instance IDs.
    instances_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent list deployment instances call to
    # return the next set of deployment instances in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListDeploymentInstancesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDeploymentsInput(ShapeBase):
    """
    Represents the input of a ListDeployments operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "deployment_group_name",
                "deploymentGroupName",
                TypeInfo(str),
            ),
            (
                "include_only_statuses",
                "includeOnlyStatuses",
                TypeInfo(typing.List[typing.Union[str, DeploymentStatus]]),
            ),
            (
                "create_time_range",
                "createTimeRange",
                TypeInfo(TimeRange),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an existing deployment group for the specified application.
    deployment_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subset of deployments to list by status:

    #   * Created: Include created deployments in the resulting list.

    #   * Queued: Include queued deployments in the resulting list.

    #   * In Progress: Include in-progress deployments in the resulting list.

    #   * Succeeded: Include successful deployments in the resulting list.

    #   * Failed: Include failed deployments in the resulting list.

    #   * Stopped: Include stopped deployments in the resulting list.
    include_only_statuses: typing.List[typing.Union[str, "DeploymentStatus"]
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A time range (start and end) for returning a subset of the list of
    # deployments.
    create_time_range: "TimeRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier returned from the previous list deployments call. It can be
    # used to return the next set of deployments in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeploymentsOutput(OutputShapeBase):
    """
    Represents the output of a ListDeployments operation.
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
                "deployments",
                "deployments",
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

    # A list of deployment IDs.
    deployments: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent list deployments call to return
    # the next set of deployments in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDeploymentsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGitHubAccountTokenNamesInput(ShapeBase):
    """
    Represents the input of a ListGitHubAccountTokenNames operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier returned from the previous ListGitHubAccountTokenNames call.
    # It can be used to return the next set of names in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGitHubAccountTokenNamesOutput(OutputShapeBase):
    """
    Represents the output of a ListGitHubAccountTokenNames operation.
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
                "token_name_list",
                "tokenNameList",
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

    # A list of names of connections to GitHub accounts.
    token_name_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent ListGitHubAccountTokenNames call
    # to return the next set of names in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOnPremisesInstancesInput(ShapeBase):
    """
    Represents the input of a ListOnPremisesInstances operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registration_status",
                "registrationStatus",
                TypeInfo(typing.Union[str, RegistrationStatus]),
            ),
            (
                "tag_filters",
                "tagFilters",
                TypeInfo(typing.List[TagFilter]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The registration status of the on-premises instances:

    #   * Deregistered: Include deregistered on-premises instances in the resulting list.

    #   * Registered: Include registered on-premises instances in the resulting list.
    registration_status: typing.Union[str, "RegistrationStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The on-premises instance tags that will be used to restrict the
    # corresponding on-premises instance names returned.
    tag_filters: typing.List["TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier returned from the previous list on-premises instances call.
    # It can be used to return the next set of on-premises instances in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOnPremisesInstancesOutput(OutputShapeBase):
    """
    Represents the output of list on-premises instances operation.
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
                "instance_names",
                "instanceNames",
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

    # The list of matching on-premises instance names.
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a large amount of information is returned, an identifier is also
    # returned. It can be used in a subsequent list on-premises instances call to
    # return the next set of on-premises instances in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ListStateFilterAction(str):
    include = "include"
    exclude = "exclude"
    ignore = "ignore"


@dataclasses.dataclass
class LoadBalancerInfo(ShapeBase):
    """
    Information about the Elastic Load Balancing load balancer or target group used
    in a deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elb_info_list",
                "elbInfoList",
                TypeInfo(typing.List[ELBInfo]),
            ),
            (
                "target_group_info_list",
                "targetGroupInfoList",
                TypeInfo(typing.List[TargetGroupInfo]),
            ),
        ]

    # An array containing information about the load balancer to use for load
    # balancing in a deployment. In Elastic Load Balancing, load balancers are
    # used with Classic Load Balancers.

    # Adding more than one load balancer to the array is not supported.
    elb_info_list: typing.List["ELBInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array containing information about the target group to use for load
    # balancing in a deployment. In Elastic Load Balancing, target groups are
    # used with Application Load Balancers.

    # Adding more than one target group to the array is not supported.
    target_group_info_list: typing.List["TargetGroupInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MinimumHealthyHosts(ShapeBase):
    """
    Information about minimum healthy instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "value",
                TypeInfo(int),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, MinimumHealthyHostsType]),
            ),
        ]

    # The minimum healthy instance value.
    value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum healthy instance type:

    #   * HOST_COUNT: The minimum number of healthy instance as an absolute value.

    #   * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment.

    # In an example of nine instance, if a HOST_COUNT of six is specified, deploy
    # to up to three instances at a time. The deployment will be successful if
    # six or more instances are deployed to successfully; otherwise, the
    # deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to
    # five instance at a time. The deployment will be successful if four or more
    # instance are deployed to successfully; otherwise, the deployment fails.

    # In a call to the get deployment configuration operation,
    # CodeDeployDefault.OneAtATime will return a minimum healthy instance type of
    # MOST_CONCURRENCY and a value of 1. This means a deployment to only one
    # instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to
    # HOST_COUNT or FLEET_PERCENT.) In addition, with
    # CodeDeployDefault.OneAtATime, AWS CodeDeploy will try to ensure that all
    # instances but one are kept in a healthy state during the deployment.
    # Although this allows one instance at a time to be taken offline for a new
    # deployment, it also means that if the deployment to the last instance
    # fails, the overall deployment still succeeds.

    # For more information, see [AWS CodeDeploy Instance
    # Health](http://docs.aws.amazon.com/codedeploy/latest/userguide/instances-
    # health.html) in the _AWS CodeDeploy User Guide_.
    type: typing.Union[str, "MinimumHealthyHostsType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class MinimumHealthyHostsType(str):
    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


@dataclasses.dataclass
class MultipleIamArnsProvidedException(ShapeBase):
    """
    Both an IAM user ARN and an IAM session ARN were included in the request. Use
    only one ARN type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OnPremisesTagSet(ShapeBase):
    """
    Information about groups of on-premises instance tags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "on_premises_tag_set_list",
                "onPremisesTagSetList",
                TypeInfo(typing.List[typing.List[TagFilter]]),
            ),
        ]

    # A list containing other lists of on-premises instance tag groups. In order
    # for an instance to be included in the deployment group, it must be
    # identified by all the tag groups in the list.
    on_premises_tag_set_list: typing.List[typing.List["TagFilter"]
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class OperationNotSupportedException(ShapeBase):
    """
    The API used does not support the deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PutLifecycleEventHookExecutionStatusInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "lifecycle_event_hook_execution_id",
                "lifecycleEventHookExecutionId",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, LifecycleEventStatus]),
            ),
        ]

    # The ID of the deployment. Pass this ID to a Lambda function that validates
    # a deployment lifecycle event.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The execution ID of a deployment's lifecycle hook. A deployment lifecycle
    # hook is specified in the `hooks` section of the AppSpec file.
    lifecycle_event_hook_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The result of a Lambda function that validates a deployment lifecycle event
    # (`Succeeded` or `Failed`).
    status: typing.Union[str, "LifecycleEventStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutLifecycleEventHookExecutionStatusOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "lifecycle_event_hook_execution_id",
                "lifecycleEventHookExecutionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The execution ID of the lifecycle event hook. A hook is specified in the
    # `hooks` section of the deployment's AppSpec file.
    lifecycle_event_hook_execution_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RawString(ShapeBase):
    """
    A revision for an AWS Lambda deployment that is a YAML-formatted or JSON-
    formatted string. For AWS Lambda deployments, the revision is the same as the
    AppSpec file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "content",
                TypeInfo(str),
            ),
            (
                "sha256",
                "sha256",
                TypeInfo(str),
            ),
        ]

    # The YAML-formatted or JSON-formatted revision string. It includes
    # information about which Lambda function to update and optional Lambda
    # functions that validate deployment lifecycle events.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SHA256 hash value of the revision that is specified as a RawString.
    sha256: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterApplicationRevisionInput(ShapeBase):
    """
    Represents the input of a RegisterApplicationRevision operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "revision",
                "revision",
                TypeInfo(RevisionLocation),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The name of an AWS CodeDeploy application associated with the applicable
    # IAM user or AWS account.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the application revision to register, including type and
    # location.
    revision: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A comment about the revision.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterOnPremisesInstanceInput(ShapeBase):
    """
    Represents the input of the register on-premises instance operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "iam_session_arn",
                "iamSessionArn",
                TypeInfo(str),
            ),
            (
                "iam_user_arn",
                "iamUserArn",
                TypeInfo(str),
            ),
        ]

    # The name of the on-premises instance to register.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM session to associate with the on-premises instance.
    iam_session_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM user to associate with the on-premises instance.
    iam_user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RegistrationStatus(str):
    Registered = "Registered"
    Deregistered = "Deregistered"


@dataclasses.dataclass
class RemoveTagsFromOnPremisesInstancesInput(ShapeBase):
    """
    Represents the input of a RemoveTagsFromOnPremisesInstances operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The tag key-value pairs to remove from the on-premises instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of the on-premises instances from which to remove tags.
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceValidationException(ShapeBase):
    """
    The specified resource could not be validated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RevisionDoesNotExistException(ShapeBase):
    """
    The named revision does not exist with the applicable IAM user or AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RevisionInfo(ShapeBase):
    """
    Information about an application revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "revision_location",
                "revisionLocation",
                TypeInfo(RevisionLocation),
            ),
            (
                "generic_revision_info",
                "genericRevisionInfo",
                TypeInfo(GenericRevisionInfo),
            ),
        ]

    # Information about the location and type of an application revision.
    revision_location: "RevisionLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about an application revision, including usage details and
    # associated deployment groups.
    generic_revision_info: "GenericRevisionInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevisionLocation(ShapeBase):
    """
    Information about the location of an application revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "revision_type",
                "revisionType",
                TypeInfo(typing.Union[str, RevisionLocationType]),
            ),
            (
                "s3_location",
                "s3Location",
                TypeInfo(S3Location),
            ),
            (
                "git_hub_location",
                "gitHubLocation",
                TypeInfo(GitHubLocation),
            ),
            (
                "string",
                "string",
                TypeInfo(RawString),
            ),
        ]

    # The type of application revision:

    #   * S3: An application revision stored in Amazon S3.

    #   * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only)

    #   * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only)
    revision_type: typing.Union[str, "RevisionLocationType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Information about the location of a revision stored in Amazon S3.
    s3_location: "S3Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the location of application artifacts stored in GitHub.
    git_hub_location: "GitHubLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the location of an AWS Lambda deployment revision stored
    # as a RawString.
    string: "RawString" = dataclasses.field(default=ShapeBase.NOT_SET, )


class RevisionLocationType(str):
    S3 = "S3"
    GitHub = "GitHub"
    String = "String"


@dataclasses.dataclass
class RevisionRequiredException(ShapeBase):
    """
    The revision ID was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RoleRequiredException(ShapeBase):
    """
    The role ID was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RollbackInfo(ShapeBase):
    """
    Information about a deployment rollback.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rollback_deployment_id",
                "rollbackDeploymentId",
                TypeInfo(str),
            ),
            (
                "rollback_triggering_deployment_id",
                "rollbackTriggeringDeploymentId",
                TypeInfo(str),
            ),
            (
                "rollback_message",
                "rollbackMessage",
                TypeInfo(str),
            ),
        ]

    # The ID of the deployment rollback.
    rollback_deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The deployment ID of the deployment that was underway and triggered a
    # rollback deployment because it failed or was stopped.
    rollback_triggering_deployment_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information describing the status of a deployment rollback; for example,
    # whether the deployment can't be rolled back, is in progress, failed, or
    # succeeded.
    rollback_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3Location(ShapeBase):
    """
    Information about the location of application artifacts stored in Amazon S3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "bundle_type",
                "bundleType",
                TypeInfo(typing.Union[str, BundleType]),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "eTag",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon S3 bucket where the application revision is stored.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon S3 object that represents the bundled artifacts for
    # the application revision.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file type of the application revision. Must be one of the following:

    #   * tar: A tar archive file.

    #   * tgz: A compressed tar archive file.

    #   * zip: A zip archive file.
    bundle_type: typing.Union[str, "BundleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A specific version of the Amazon S3 object that represents the bundled
    # artifacts for the application revision.

    # If the version is not specified, the system will use the most recent
    # version by default.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ETag of the Amazon S3 object that represents the bundled artifacts for
    # the application revision.

    # If the ETag is not specified as an input parameter, ETag validation of the
    # object will be skipped.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SkipWaitTimeForInstanceTerminationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
        ]

    # The ID of the blue/green deployment for which you want to skip the instance
    # termination wait time.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SortOrder(str):
    ascending = "ascending"
    descending = "descending"


@dataclasses.dataclass
class StopDeploymentInput(ShapeBase):
    """
    Represents the input of a StopDeployment operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "deploymentId",
                TypeInfo(str),
            ),
            (
                "auto_rollback_enabled",
                "autoRollbackEnabled",
                TypeInfo(bool),
            ),
        ]

    # The unique ID of a deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates, when a deployment is stopped, whether instances that have been
    # updated should be rolled back to the previous version of the application
    # revision.
    auto_rollback_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopDeploymentOutput(OutputShapeBase):
    """
    Represents the output of a StopDeployment operation.
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
                "status",
                "status",
                TypeInfo(typing.Union[str, StopStatus]),
            ),
            (
                "status_message",
                "statusMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the stop deployment operation:

    #   * Pending: The stop operation is pending.

    #   * Succeeded: The stop operation was successful.
    status: typing.Union[str, "StopStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An accompanying status message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StopStatus(str):
    Pending = "Pending"
    Succeeded = "Succeeded"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Information about a tag.
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

    # The tag's key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag's value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagFilter(ShapeBase):
    """
    Information about an on-premises instance tag filter.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, TagFilterType]),
            ),
        ]

    # The on-premises instance tag filter key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The on-premises instance tag filter value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The on-premises instance tag filter type:

    #   * KEY_ONLY: Key only.

    #   * VALUE_ONLY: Value only.

    #   * KEY_AND_VALUE: Key and value.
    type: typing.Union[str, "TagFilterType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TagFilterType(str):
    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


@dataclasses.dataclass
class TagLimitExceededException(ShapeBase):
    """
    The maximum allowed number of tags was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagRequiredException(ShapeBase):
    """
    A tag was not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagSetListLimitExceededException(ShapeBase):
    """
    The number of tag groups included in the tag set list exceeded the maximum
    allowed limit of 3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TargetGroupInfo(ShapeBase):
    """
    Information about a target group in Elastic Load Balancing to use in a
    deployment. Instances are registered as targets in a target group, and traffic
    is routed to the target group.
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

    # For blue/green deployments, the name of the target group that instances in
    # the original environment are deregistered from, and instances in the
    # replacement environment registered with. For in-place deployments, the name
    # of the target group that instances are deregistered from, so they are not
    # serving traffic during a deployment, and then re-registered with after the
    # deployment completes.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetInstances(ShapeBase):
    """
    Information about the instances to be used in the replacement environment in a
    blue/green deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_filters",
                "tagFilters",
                TypeInfo(typing.List[EC2TagFilter]),
            ),
            (
                "auto_scaling_groups",
                "autoScalingGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "ec2_tag_set",
                "ec2TagSet",
                TypeInfo(EC2TagSet),
            ),
        ]

    # The tag filter key, type, and value used to identify Amazon EC2 instances
    # in a replacement environment for a blue/green deployment. Cannot be used in
    # the same call as ec2TagSet.
    tag_filters: typing.List["EC2TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of one or more Auto Scaling groups to identify a replacement
    # environment for a blue/green deployment.
    auto_scaling_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the groups of EC2 instance tags that an instance must be
    # identified by in order for it to be included in the replacement environment
    # for a blue/green deployment. Cannot be used in the same call as tagFilters.
    ec2_tag_set: "EC2TagSet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ThrottlingException(ShapeBase):
    """
    An API function was called too frequently.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TimeBasedCanary(ShapeBase):
    """
    A configuration that shifts traffic from one version of a Lambda function to
    another in two increments. The original and target Lambda function versions are
    specified in the deployment's AppSpec file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "canary_percentage",
                "canaryPercentage",
                TypeInfo(int),
            ),
            (
                "canary_interval",
                "canaryInterval",
                TypeInfo(int),
            ),
        ]

    # The percentage of traffic to shift in the first increment of a
    # `TimeBasedCanary` deployment.
    canary_percentage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes between the first and second traffic shifts of a
    # `TimeBasedCanary` deployment.
    canary_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimeBasedLinear(ShapeBase):
    """
    A configuration that shifts traffic from one version of a Lambda function to
    another in equal increments, with an equal number of minutes between each
    increment. The original and target Lambda function versions are specified in the
    deployment's AppSpec file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "linear_percentage",
                "linearPercentage",
                TypeInfo(int),
            ),
            (
                "linear_interval",
                "linearInterval",
                TypeInfo(int),
            ),
        ]

    # The percentage of traffic that is shifted at the start of each increment of
    # a `TimeBasedLinear` deployment.
    linear_percentage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes between each incremental traffic shift of a
    # `TimeBasedLinear` deployment.
    linear_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimeRange(ShapeBase):
    """
    Information about a time range.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start",
                "start",
                TypeInfo(datetime.datetime),
            ),
            (
                "end",
                "end",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The start time of the time range.

    # Specify null to leave the start time open-ended.
    start: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end time of the time range.

    # Specify null to leave the end time open-ended.
    end: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrafficRoutingConfig(ShapeBase):
    """
    The configuration that specifies how traffic is shifted from one version of a
    Lambda function to another version during an AWS Lambda deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, TrafficRoutingType]),
            ),
            (
                "time_based_canary",
                "timeBasedCanary",
                TypeInfo(TimeBasedCanary),
            ),
            (
                "time_based_linear",
                "timeBasedLinear",
                TypeInfo(TimeBasedLinear),
            ),
        ]

    # The type of traffic shifting (`TimeBasedCanary` or `TimeBasedLinear`) used
    # by a deployment configuration .
    type: typing.Union[str, "TrafficRoutingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A configuration that shifts traffic from one version of a Lambda function
    # to another in two increments. The original and target Lambda function
    # versions are specified in the deployment's AppSpec file.
    time_based_canary: "TimeBasedCanary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A configuration that shifts traffic from one version of a Lambda function
    # to another in equal increments, with an equal number of minutes between
    # each increment. The original and target Lambda function versions are
    # specified in the deployment's AppSpec file.
    time_based_linear: "TimeBasedLinear" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TrafficRoutingType(str):
    TimeBasedCanary = "TimeBasedCanary"
    TimeBasedLinear = "TimeBasedLinear"
    AllAtOnce = "AllAtOnce"


@dataclasses.dataclass
class TriggerConfig(ShapeBase):
    """
    Information about notification triggers for the deployment group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trigger_name",
                "triggerName",
                TypeInfo(str),
            ),
            (
                "trigger_target_arn",
                "triggerTargetArn",
                TypeInfo(str),
            ),
            (
                "trigger_events",
                "triggerEvents",
                TypeInfo(typing.List[typing.Union[str, TriggerEventType]]),
            ),
        ]

    # The name of the notification trigger.
    trigger_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon Simple Notification Service topic through which
    # notifications about deployment or instance events are sent.
    trigger_target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event type or types for which notifications are triggered.
    trigger_events: typing.List[typing.Union[str, "TriggerEventType"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


class TriggerEventType(str):
    DeploymentStart = "DeploymentStart"
    DeploymentSuccess = "DeploymentSuccess"
    DeploymentFailure = "DeploymentFailure"
    DeploymentStop = "DeploymentStop"
    DeploymentRollback = "DeploymentRollback"
    DeploymentReady = "DeploymentReady"
    InstanceStart = "InstanceStart"
    InstanceSuccess = "InstanceSuccess"
    InstanceFailure = "InstanceFailure"
    InstanceReady = "InstanceReady"


@dataclasses.dataclass
class TriggerTargetsLimitExceededException(ShapeBase):
    """
    The maximum allowed number of triggers was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedActionForDeploymentTypeException(ShapeBase):
    """
    A call was submitted that is not supported for the specified deployment type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateApplicationInput(ShapeBase):
    """
    Represents the input of an UpdateApplication operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "new_application_name",
                "newApplicationName",
                TypeInfo(str),
            ),
        ]

    # The current name of the application you want to change.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name to give the application.
    new_application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeploymentGroupInput(ShapeBase):
    """
    Represents the input of an UpdateDeploymentGroup operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "applicationName",
                TypeInfo(str),
            ),
            (
                "current_deployment_group_name",
                "currentDeploymentGroupName",
                TypeInfo(str),
            ),
            (
                "new_deployment_group_name",
                "newDeploymentGroupName",
                TypeInfo(str),
            ),
            (
                "deployment_config_name",
                "deploymentConfigName",
                TypeInfo(str),
            ),
            (
                "ec2_tag_filters",
                "ec2TagFilters",
                TypeInfo(typing.List[EC2TagFilter]),
            ),
            (
                "on_premises_instance_tag_filters",
                "onPremisesInstanceTagFilters",
                TypeInfo(typing.List[TagFilter]),
            ),
            (
                "auto_scaling_groups",
                "autoScalingGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "service_role_arn",
                "serviceRoleArn",
                TypeInfo(str),
            ),
            (
                "trigger_configurations",
                "triggerConfigurations",
                TypeInfo(typing.List[TriggerConfig]),
            ),
            (
                "alarm_configuration",
                "alarmConfiguration",
                TypeInfo(AlarmConfiguration),
            ),
            (
                "auto_rollback_configuration",
                "autoRollbackConfiguration",
                TypeInfo(AutoRollbackConfiguration),
            ),
            (
                "deployment_style",
                "deploymentStyle",
                TypeInfo(DeploymentStyle),
            ),
            (
                "blue_green_deployment_configuration",
                "blueGreenDeploymentConfiguration",
                TypeInfo(BlueGreenDeploymentConfiguration),
            ),
            (
                "load_balancer_info",
                "loadBalancerInfo",
                TypeInfo(LoadBalancerInfo),
            ),
            (
                "ec2_tag_set",
                "ec2TagSet",
                TypeInfo(EC2TagSet),
            ),
            (
                "on_premises_tag_set",
                "onPremisesTagSet",
                TypeInfo(OnPremisesTagSet),
            ),
        ]

    # The application name corresponding to the deployment group to update.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current name of the deployment group.
    current_deployment_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new name of the deployment group, if you want to change it.
    new_deployment_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replacement deployment configuration name to use, if you want to change
    # it.
    deployment_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement set of Amazon EC2 tags on which to filter, if you want to
    # change them. To keep the existing tags, enter their names. To remove tags,
    # do not enter any tag names.
    ec2_tag_filters: typing.List["EC2TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replacement set of on-premises instance tags on which to filter, if you
    # want to change them. To keep the existing tags, enter their names. To
    # remove tags, do not enter any tag names.
    on_premises_instance_tag_filters: typing.List["TagFilter"
                                                 ] = dataclasses.field(
                                                     default=ShapeBase.NOT_SET,
                                                 )

    # The replacement list of Auto Scaling groups to be included in the
    # deployment group, if you want to change them. To keep the Auto Scaling
    # groups, enter their names. To remove Auto Scaling groups, do not enter any
    # Auto Scaling group names.
    auto_scaling_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A replacement ARN for the service role, if you want to change it.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about triggers to change when the deployment group is updated.
    # For examples, see [Modify Triggers in an AWS CodeDeploy Deployment
    # Group](http://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-
    # notify-edit.html) in the AWS CodeDeploy User Guide.
    trigger_configurations: typing.List["TriggerConfig"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information to add or change about Amazon CloudWatch alarms when the
    # deployment group is updated.
    alarm_configuration: "AlarmConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information for an automatic rollback configuration that is added or
    # changed when a deployment group is updated.
    auto_rollback_configuration: "AutoRollbackConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the type of deployment, either in-place or blue/green,
    # you want to run and whether to route deployment traffic behind a load
    # balancer.
    deployment_style: "DeploymentStyle" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about blue/green deployment options for a deployment group.
    blue_green_deployment_configuration: "BlueGreenDeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the load balancer used in a deployment.
    load_balancer_info: "LoadBalancerInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about groups of tags applied to on-premises instances. The
    # deployment group will include only EC2 instances identified by all the tag
    # groups.
    ec2_tag_set: "EC2TagSet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about an on-premises instance tag set. The deployment group
    # will include only on-premises instances identified by all the tag groups.
    on_premises_tag_set: "OnPremisesTagSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDeploymentGroupOutput(OutputShapeBase):
    """
    Represents the output of an UpdateDeploymentGroup operation.
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
                "hooks_not_cleaned_up",
                "hooksNotCleanedUp",
                TypeInfo(typing.List[AutoScalingGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the output contains no data, and the corresponding deployment group
    # contained at least one Auto Scaling group, AWS CodeDeploy successfully
    # removed all corresponding Auto Scaling lifecycle event hooks from the AWS
    # account. If the output contains data, AWS CodeDeploy could not remove some
    # Auto Scaling lifecycle event hooks from the AWS account.
    hooks_not_cleaned_up: typing.List["AutoScalingGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
