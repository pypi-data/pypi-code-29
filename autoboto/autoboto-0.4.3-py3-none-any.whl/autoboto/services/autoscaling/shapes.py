import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class ActivitiesType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activities",
                "Activities",
                TypeInfo(typing.List[Activity]),
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

    # The scaling activities. Activities are sorted by start time. Activities
    # still in progress are described first.
    activities: typing.List["Activity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ActivitiesType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Activity(ShapeBase):
    """
    Describes scaling activity, which is a long-running process that represents a
    change to your Auto Scaling group, such as changing its size or replacing an
    instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_id",
                "ActivityId",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "cause",
                "Cause",
                TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(typing.Union[str, ScalingActivityStatusCode]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "progress",
                "Progress",
                TypeInfo(int),
            ),
            (
                "details",
                "Details",
                TypeInfo(str),
            ),
        ]

    # The ID of the activity.
    activity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason the activity began.
    cause: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the activity.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the activity.
    status_code: typing.Union[str, "ScalingActivityStatusCode"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # A friendly, more verbose description of the activity.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end time of the activity.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly, more verbose description of the activity status.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value between 0 and 100 that indicates the progress of the activity.
    progress: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The details about the activity.
    details: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActivityType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activity",
                "Activity",
                TypeInfo(Activity),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A scaling activity.
    activity: "Activity" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AdjustmentType(ShapeBase):
    """
    Describes a policy adjustment type.

    For more information, see [Dynamic
    Scaling](http://docs.aws.amazon.com/autoscaling/ec2/DeveloperGuide/as-scale-
    based-on-demand.html) in the _Amazon EC2 Auto Scaling User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adjustment_type",
                "AdjustmentType",
                TypeInfo(str),
            ),
        ]

    # The policy adjustment type. The valid values are `ChangeInCapacity`,
    # `ExactCapacity`, and `PercentChangeInCapacity`.
    adjustment_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Alarm(ShapeBase):
    """
    Describes an alarm.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_name",
                "AlarmName",
                TypeInfo(str),
            ),
            (
                "alarm_arn",
                "AlarmARN",
                TypeInfo(str),
            ),
        ]

    # The name of the alarm.
    alarm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the alarm.
    alarm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsFault(ShapeBase):
    """
    You already have an Auto Scaling group or launch configuration with this name.
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
class AttachInstancesQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the instances. You can specify up to 20 instances.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachLoadBalancerTargetGroupsResultType(OutputShapeBase):
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
class AttachLoadBalancerTargetGroupsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "target_group_arns",
                "TargetGroupARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Names (ARN) of the target groups. You can specify up to
    # 10 target groups.
    target_group_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachLoadBalancersResultType(OutputShapeBase):
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
class AttachLoadBalancersType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the load balancers. You can specify up to 10 load balancers.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingGroup(ShapeBase):
    """
    Describes an Auto Scaling group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
            (
                "default_cooldown",
                "DefaultCooldown",
                TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "health_check_type",
                "HealthCheckType",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "auto_scaling_group_arn",
                "AutoScalingGroupARN",
                TypeInfo(str),
            ),
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "launch_template",
                "LaunchTemplate",
                TypeInfo(LaunchTemplateSpecification),
            ),
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "target_group_arns",
                "TargetGroupARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "health_check_grace_period",
                "HealthCheckGracePeriod",
                TypeInfo(int),
            ),
            (
                "instances",
                "Instances",
                TypeInfo(typing.List[Instance]),
            ),
            (
                "suspended_processes",
                "SuspendedProcesses",
                TypeInfo(typing.List[SuspendedProcess]),
            ),
            (
                "placement_group",
                "PlacementGroup",
                TypeInfo(str),
            ),
            (
                "vpc_zone_identifier",
                "VPCZoneIdentifier",
                TypeInfo(str),
            ),
            (
                "enabled_metrics",
                "EnabledMetrics",
                TypeInfo(typing.List[EnabledMetric]),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[TagDescription]),
            ),
            (
                "termination_policies",
                "TerminationPolicies",
                TypeInfo(typing.List[str]),
            ),
            (
                "new_instances_protected_from_scale_in",
                "NewInstancesProtectedFromScaleIn",
                TypeInfo(bool),
            ),
            (
                "service_linked_role_arn",
                "ServiceLinkedRoleARN",
                TypeInfo(str),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum size of the group.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the group.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired size of the group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scaling activity completes before
    # another scaling activity can start.
    default_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more Availability Zones for the group.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service to use for the health checks. The valid values are `EC2` and
    # `ELB`.
    health_check_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the group was created.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Auto Scaling group.
    auto_scaling_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the associated launch configuration.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch template for the group.
    launch_template: "LaunchTemplateSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more load balancers associated with the group.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Names (ARN) of the target groups for your load
    # balancer.
    target_group_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before
    # checking the health status of an EC2 instance that has come into service.
    health_check_grace_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 instances associated with the group.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The suspended processes associated with the group.
    suspended_processes: typing.List["SuspendedProcess"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the placement group into which you'll launch your instances, if
    # any. For more information, see [Placement
    # Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-
    # groups.html) in the _Amazon Elastic Compute Cloud User Guide_.
    placement_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more subnet IDs, if applicable, separated by commas.

    # If you specify `VPCZoneIdentifier` and `AvailabilityZones`, ensure that the
    # Availability Zones of the subnets match the values for `AvailabilityZones`.
    vpc_zone_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metrics enabled for the group.
    enabled_metrics: typing.List["EnabledMetric"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the group when DeleteAutoScalingGroup is in progress.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags for the group.
    tags: typing.List["TagDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The termination policies for the group.
    termination_policies: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether newly launched instances are protected from termination
    # by Auto Scaling when scaling in.
    new_instances_protected_from_scale_in: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the service-linked role that the Auto
    # Scaling group uses to call other AWS services on your behalf.
    service_linked_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingGroupNamesType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_names",
                "AutoScalingGroupNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The names of the Auto Scaling groups. You can specify up to `MaxRecords`
    # names. If you omit this parameter, all Auto Scaling groups are described.
    auto_scaling_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 50 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutoScalingGroupsType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "auto_scaling_groups",
                "AutoScalingGroups",
                TypeInfo(typing.List[AutoScalingGroup]),
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

    # The groups.
    auto_scaling_groups: typing.List["AutoScalingGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["AutoScalingGroupsType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class AutoScalingInstanceDetails(ShapeBase):
    """
    Describes an EC2 instance associated with an Auto Scaling group.
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
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "lifecycle_state",
                "LifecycleState",
                TypeInfo(str),
            ),
            (
                "health_status",
                "HealthStatus",
                TypeInfo(str),
            ),
            (
                "protected_from_scale_in",
                "ProtectedFromScaleIn",
                TypeInfo(bool),
            ),
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "launch_template",
                "LaunchTemplate",
                TypeInfo(LaunchTemplateSpecification),
            ),
        ]

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group for the instance.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zone for the instance.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The lifecycle state for the instance. For more information, see [Auto
    # Scaling
    # Lifecycle](http://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    lifecycle_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last reported health status of this instance. "Healthy" means that the
    # instance is healthy and should remain in service. "Unhealthy" means that
    # the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and
    # replace it.
    health_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the instance is protected from termination by Amazon EC2
    # Auto Scaling when scaling in.
    protected_from_scale_in: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch configuration used to launch the instance. This value is not
    # available if you attached the instance to the Auto Scaling group.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch template for the instance.
    launch_template: "LaunchTemplateSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingInstancesType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "auto_scaling_instances",
                "AutoScalingInstances",
                TypeInfo(typing.List[AutoScalingInstanceDetails]),
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

    # The instances.
    auto_scaling_instances: typing.List["AutoScalingInstanceDetails"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["AutoScalingInstancesType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class BatchDeleteScheduledActionAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_scheduled_actions",
                "FailedScheduledActions",
                TypeInfo(typing.List[FailedScheduledUpdateGroupActionRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the scheduled actions that could not be deleted, including an
    # error message.
    failed_scheduled_actions: typing.List[
        "FailedScheduledUpdateGroupActionRequest"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class BatchDeleteScheduledActionType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scheduled_action_names",
                "ScheduledActionNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the scheduled actions to delete. The maximum number allowed is
    # 50.
    scheduled_action_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchPutScheduledUpdateGroupActionAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "failed_scheduled_update_group_actions",
                "FailedScheduledUpdateGroupActions",
                TypeInfo(typing.List[FailedScheduledUpdateGroupActionRequest]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the scheduled actions that could not be created or updated,
    # including an error message.
    failed_scheduled_update_group_actions: typing.List[
        "FailedScheduledUpdateGroupActionRequest"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class BatchPutScheduledUpdateGroupActionType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scheduled_update_group_actions",
                "ScheduledUpdateGroupActions",
                TypeInfo(typing.List[ScheduledUpdateGroupActionRequest]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more scheduled actions. The maximum number allowed is 50.
    scheduled_update_group_actions: typing.List[
        "ScheduledUpdateGroupActionRequest"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class BlockDeviceMapping(ShapeBase):
    """
    Describes a block device mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_name",
                "DeviceName",
                TypeInfo(str),
            ),
            (
                "virtual_name",
                "VirtualName",
                TypeInfo(str),
            ),
            (
                "ebs",
                "Ebs",
                TypeInfo(Ebs),
            ),
            (
                "no_device",
                "NoDevice",
                TypeInfo(bool),
            ),
        ]

    # The device name exposed to the EC2 instance (for example, `/dev/sdh` or
    # `xvdh`).
    device_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the virtual device (for example, `ephemeral0`).
    virtual_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The information about the Amazon EBS volume.
    ebs: "Ebs" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Suppresses a device mapping.

    # If this parameter is true for the root device, the instance might fail the
    # EC2 health check. Amazon EC2 Auto Scaling launches a replacement instance
    # if the instance fails the health check.
    no_device: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompleteLifecycleActionAnswer(OutputShapeBase):
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
class CompleteLifecycleActionType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_hook_name",
                "LifecycleHookName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "lifecycle_action_result",
                "LifecycleActionResult",
                TypeInfo(str),
            ),
            (
                "lifecycle_action_token",
                "LifecycleActionToken",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle hook.
    lifecycle_hook_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action for the group to take. This parameter can be either `CONTINUE`
    # or `ABANDON`.
    lifecycle_action_result: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A universally unique identifier (UUID) that identifies a specific lifecycle
    # action associated with an instance. Amazon EC2 Auto Scaling sends this
    # token to the notification target you specified when you created the
    # lifecycle hook.
    lifecycle_action_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAutoScalingGroupType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "launch_template",
                "LaunchTemplate",
                TypeInfo(LaunchTemplateSpecification),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
            (
                "default_cooldown",
                "DefaultCooldown",
                TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "target_group_arns",
                "TargetGroupARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "health_check_type",
                "HealthCheckType",
                TypeInfo(str),
            ),
            (
                "health_check_grace_period",
                "HealthCheckGracePeriod",
                TypeInfo(int),
            ),
            (
                "placement_group",
                "PlacementGroup",
                TypeInfo(str),
            ),
            (
                "vpc_zone_identifier",
                "VPCZoneIdentifier",
                TypeInfo(str),
            ),
            (
                "termination_policies",
                "TerminationPolicies",
                TypeInfo(typing.List[str]),
            ),
            (
                "new_instances_protected_from_scale_in",
                "NewInstancesProtectedFromScaleIn",
                TypeInfo(bool),
            ),
            (
                "lifecycle_hook_specification_list",
                "LifecycleHookSpecificationList",
                TypeInfo(typing.List[LifecycleHookSpecification]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "service_linked_role_arn",
                "ServiceLinkedRoleARN",
                TypeInfo(str),
            ),
        ]

    # The name of the Auto Scaling group. This name must be unique within the
    # scope of your AWS account.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum size of the group.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the group.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the launch configuration. You must specify one of the
    # following: a launch configuration, a launch template, or an EC2 instance.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch template to use to launch instances. You must specify one of the
    # following: a launch template, a launch configuration, or an EC2 instance.
    launch_template: "LaunchTemplateSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the instance used to create a launch configuration for the group.
    # You must specify one of the following: an EC2 instance, a launch
    # configuration, or a launch template.

    # When you specify an ID of an instance, Amazon EC2 Auto Scaling creates a
    # new launch configuration and associates it with the group. This launch
    # configuration derives its attributes from the specified instance, with the
    # exception of the block device mapping.

    # For more information, see [Create an Auto Scaling Group Using an EC2
    # Instance](http://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-
    # from-instance.html) in the _Amazon EC2 Auto Scaling User Guide_.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of EC2 instances that should be running in the group. This
    # number must be greater than or equal to the minimum size of the group and
    # less than or equal to the maximum size of the group. If you do not specify
    # a desired capacity, the default is the minimum size of the group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scaling activity completes before
    # another scaling activity can start. The default is 300.

    # For more information, see [Scaling
    # Cooldowns](http://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    default_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more Availability Zones for the group. This parameter is optional if
    # you specify one or more subnets.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more Classic Load Balancers. To specify an Application Load
    # Balancer, use `TargetGroupARNs` instead.

    # For more information, see [Using a Load Balancer With an Auto Scaling
    # Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-
    # from-instance.html) in the _Amazon EC2 Auto Scaling User Guide_.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Names (ARN) of the target groups.
    target_group_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service to use for the health checks. The valid values are `EC2` and
    # `ELB`.

    # By default, health checks use Amazon EC2 instance status checks to
    # determine the health of an instance. For more information, see [Health
    # Checks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    health_check_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before
    # checking the health status of an EC2 instance that has come into service.
    # During this time, any health check failures for the instance are ignored.
    # The default is 0.

    # This parameter is required if you are adding an `ELB` health check.

    # For more information, see [Health
    # Checks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    health_check_grace_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the placement group into which you'll launch your instances, if
    # any. For more information, see [Placement
    # Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-
    # groups.html) in the _Amazon Elastic Compute Cloud User Guide_.
    placement_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comma-separated list of subnet identifiers for your virtual private cloud
    # (VPC).

    # If you specify subnets and Availability Zones with this call, ensure that
    # the subnets' Availability Zones match the Availability Zones specified.

    # For more information, see [Launching Auto Scaling Instances in a
    # VPC](http://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    vpc_zone_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more termination policies used to select the instance to terminate.
    # These policies are executed in the order that they are listed.

    # For more information, see [Controlling Which Instances Auto Scaling
    # Terminates During Scale
    # In](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-
    # termination.html) in the _Auto Scaling User Guide_.
    termination_policies: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether newly launched instances are protected from termination
    # by Auto Scaling when scaling in.
    new_instances_protected_from_scale_in: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more lifecycle hooks.
    lifecycle_hook_specification_list: typing.List["LifecycleHookSpecification"
                                                  ] = dataclasses.field(
                                                      default=ShapeBase.NOT_SET,
                                                  )

    # One or more tags.

    # For more information, see [Tagging Auto Scaling Groups and
    # Instances](http://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-
    # tagging.html) in the _Amazon EC2 Auto Scaling User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the service-linked role that the Auto
    # Scaling group uses to call other AWS services on your behalf. By default,
    # Amazon EC2 Auto Scaling uses a service-linked role named
    # AWSServiceRoleForAutoScaling, which it creates if it does not exist.
    service_linked_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLaunchConfigurationType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "image_id",
                "ImageId",
                TypeInfo(str),
            ),
            (
                "key_name",
                "KeyName",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "classic_link_vpc_id",
                "ClassicLinkVPCId",
                TypeInfo(str),
            ),
            (
                "classic_link_vpc_security_groups",
                "ClassicLinkVPCSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "user_data",
                "UserData",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "kernel_id",
                "KernelId",
                TypeInfo(str),
            ),
            (
                "ramdisk_id",
                "RamdiskId",
                TypeInfo(str),
            ),
            (
                "block_device_mappings",
                "BlockDeviceMappings",
                TypeInfo(typing.List[BlockDeviceMapping]),
            ),
            (
                "instance_monitoring",
                "InstanceMonitoring",
                TypeInfo(InstanceMonitoring),
            ),
            (
                "spot_price",
                "SpotPrice",
                TypeInfo(str),
            ),
            (
                "iam_instance_profile",
                "IamInstanceProfile",
                TypeInfo(str),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                TypeInfo(bool),
            ),
            (
                "associate_public_ip_address",
                "AssociatePublicIpAddress",
                TypeInfo(bool),
            ),
            (
                "placement_tenancy",
                "PlacementTenancy",
                TypeInfo(str),
            ),
        ]

    # The name of the launch configuration. This name must be unique within the
    # scope of your AWS account.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Amazon Machine Image (AMI) to use to launch your EC2
    # instances.

    # If you do not specify `InstanceId`, you must specify `ImageId`.

    # For more information, see [Finding an
    # AMI](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-
    # ami.html) in the _Amazon Elastic Compute Cloud User Guide_.
    image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the key pair. For more information, see [Amazon EC2 Key
    # Pairs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-
    # pairs.html) in the _Amazon Elastic Compute Cloud User Guide_.
    key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more security groups with which to associate the instances.

    # If your instances are launched in EC2-Classic, you can either specify
    # security group names or the security group IDs. For more information about
    # security groups for EC2-Classic, see [Amazon EC2 Security
    # Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-
    # security.html) in the _Amazon Elastic Compute Cloud User Guide_.

    # If your instances are launched into a VPC, specify security group IDs. For
    # more information, see [Security Groups for Your
    # VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html)
    # in the _Amazon Virtual Private Cloud User Guide_.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.
    # This parameter is supported only if you are launching EC2-Classic
    # instances. For more information, see
    # [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
    # classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
    classic_link_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of one or more security groups for the specified ClassicLink-
    # enabled VPC. This parameter is required if you specify a ClassicLink-
    # enabled VPC, and is not supported otherwise. For more information, see
    # [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
    # classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
    classic_link_vpc_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user data to make available to the launched EC2 instances. For more
    # information, see [Instance Metadata and User
    # Data](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-
    # metadata.html) in the _Amazon Elastic Compute Cloud User Guide_.
    user_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance to use to create the launch configuration. The new
    # launch configuration derives attributes from the instance, with the
    # exception of the block device mapping.

    # If you do not specify `InstanceId`, you must specify both `ImageId` and
    # `InstanceType`.

    # To create a launch configuration with a block device mapping or override
    # any other instance attributes, specify them as part of the same request.

    # For more information, see [Create a Launch Configuration Using an EC2
    # Instance](http://docs.aws.amazon.com/autoscaling/ec2/userguide/create-lc-
    # with-instanceID.html) in the _Amazon EC2 Auto Scaling User Guide_.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type of the EC2 instance.

    # If you do not specify `InstanceId`, you must specify `InstanceType`.

    # For information about available instance types, see [Available Instance
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
    # types.html#AvailableInstanceTypes) in the _Amazon Elastic Compute Cloud
    # User Guide._
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the kernel associated with the AMI.
    kernel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the RAM disk associated with the AMI.
    ramdisk_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more mappings that specify how block devices are exposed to the
    # instance. For more information, see [Block Device
    # Mapping](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-
    # mapping-concepts.html) in the _Amazon Elastic Compute Cloud User Guide_.
    block_device_mappings: typing.List["BlockDeviceMapping"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Enables detailed monitoring (`true`) or basic monitoring (`false`) for the
    # Auto Scaling instances. The default is `true`.
    instance_monitoring: "InstanceMonitoring" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum hourly price to be paid for any Spot Instance launched to
    # fulfill the request. Spot Instances are launched when the price you specify
    # exceeds the current Spot market price. For more information, see [Launching
    # Spot Instances in Your Auto Scaling
    # Group](http://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-
    # spot-instances.html) in the _Amazon EC2 Auto Scaling User Guide_.
    spot_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or the Amazon Resource Name (ARN) of the instance profile
    # associated with the IAM role for the instance.

    # EC2 instances launched with an IAM role will automatically have AWS
    # security credentials available. You can use IAM roles with Amazon EC2 Auto
    # Scaling to automatically enable applications running on your EC2 instances
    # to securely access other AWS resources. For more information, see [Launch
    # Auto Scaling Instances with an IAM
    # Role](http://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-
    # role.html) in the _Amazon EC2 Auto Scaling User Guide_.
    iam_instance_profile: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the instance is optimized for Amazon EBS I/O. By default,
    # the instance is not optimized for EBS I/O. The optimization provides
    # dedicated throughput to Amazon EBS and an optimized configuration stack to
    # provide optimal I/O performance. This optimization is not available with
    # all instance types. Additional usage charges apply. For more information,
    # see [Amazon EBS-Optimized
    # Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html)
    # in the _Amazon Elastic Compute Cloud User Guide_.
    ebs_optimized: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used for groups that launch instances into a virtual private cloud (VPC).
    # Specifies whether to assign a public IP address to each instance. For more
    # information, see [Launching Auto Scaling Instances in a
    # VPC](http://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.

    # If you specify this parameter, be sure to specify at least one subnet when
    # you create your group.

    # Default: If the instance is launched into a default subnet, the default is
    # to assign a public IP address. If the instance is launched into a
    # nondefault subnet, the default is not to assign a public IP address.
    associate_public_ip_address: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tenancy of the instance. An instance with a tenancy of `dedicated` runs
    # on single-tenant hardware and can only be launched into a VPC.

    # You must set the value of this parameter to `dedicated` if want to launch
    # Dedicated Instances into a shared tenancy VPC (VPC with instance placement
    # tenancy attribute set to `default`).

    # If you specify this parameter, be sure to specify at least one subnet when
    # you create your group.

    # For more information, see [Launching Auto Scaling Instances in a
    # VPC](http://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.

    # Valid values: `default` | `dedicated`
    placement_tenancy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateOrUpdateTagsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomizedMetricSpecification(ShapeBase):
    """
    Configures a customized metric for a target tracking policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "statistic",
                "Statistic",
                TypeInfo(typing.Union[str, MetricStatistic]),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[MetricDimension]),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(str),
            ),
        ]

    # The name of the metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the metric.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistic of the metric.
    statistic: typing.Union[str, "MetricStatistic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The dimensions of the metric.
    dimensions: typing.List["MetricDimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unit of the metric.
    unit: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAutoScalingGroupType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "force_delete",
                "ForceDelete",
                TypeInfo(bool),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies that the group will be deleted along with all instances
    # associated with the group, without waiting for all instances to be
    # terminated. This parameter also deletes any lifecycle actions associated
    # with the group.
    force_delete: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLifecycleHookAnswer(OutputShapeBase):
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
class DeleteLifecycleHookType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_hook_name",
                "LifecycleHookName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle hook.
    lifecycle_hook_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteNotificationConfigurationType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicARN",
                TypeInfo(str),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
    # (SNS) topic.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePolicyType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
        ]

    # The name or Amazon Resource Name (ARN) of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteScheduledActionType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scheduled_action_name",
                "ScheduledActionName",
                TypeInfo(str),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the action to delete.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # One or more tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccountLimitsAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "max_number_of_auto_scaling_groups",
                "MaxNumberOfAutoScalingGroups",
                TypeInfo(int),
            ),
            (
                "max_number_of_launch_configurations",
                "MaxNumberOfLaunchConfigurations",
                TypeInfo(int),
            ),
            (
                "number_of_auto_scaling_groups",
                "NumberOfAutoScalingGroups",
                TypeInfo(int),
            ),
            (
                "number_of_launch_configurations",
                "NumberOfLaunchConfigurations",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of groups allowed for your AWS account. The default
    # limit is 20 per region.
    max_number_of_auto_scaling_groups: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of launch configurations allowed for your AWS account.
    # The default limit is 100 per region.
    max_number_of_launch_configurations: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current number of groups for your AWS account.
    number_of_auto_scaling_groups: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current number of launch configurations for your AWS account.
    number_of_launch_configurations: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAdjustmentTypesAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "adjustment_types",
                "AdjustmentTypes",
                TypeInfo(typing.List[AdjustmentType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The policy adjustment types.
    adjustment_types: typing.List["AdjustmentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAutoScalingInstancesType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The IDs of the instances. You can specify up to `MaxRecords` IDs. If you
    # omit this parameter, all Auto Scaling instances are described. If you
    # specify an ID that does not exist, it is ignored with no error.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call. The default value is
    # 50 and the maximum value is 50.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAutoScalingNotificationTypesAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "auto_scaling_notification_types",
                "AutoScalingNotificationTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The notification types.
    auto_scaling_notification_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLifecycleHookTypesAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "lifecycle_hook_types",
                "LifecycleHookTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The lifecycle hook types.
    lifecycle_hook_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLifecycleHooksAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "lifecycle_hooks",
                "LifecycleHooks",
                TypeInfo(typing.List[LifecycleHook]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The lifecycle hooks for the specified group.
    lifecycle_hooks: typing.List["LifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLifecycleHooksType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "lifecycle_hook_names",
                "LifecycleHookNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of one or more lifecycle hooks. If you omit this parameter, all
    # lifecycle hooks are described.
    lifecycle_hook_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoadBalancerTargetGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 100 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoadBalancerTargetGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancer_target_groups",
                "LoadBalancerTargetGroups",
                TypeInfo(typing.List[LoadBalancerTargetGroupState]),
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

    # Information about the target groups.
    load_balancer_target_groups: typing.List["LoadBalancerTargetGroupState"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoadBalancersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 100 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoadBalancersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancers",
                "LoadBalancers",
                TypeInfo(typing.List[LoadBalancerState]),
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

    # The load balancers.
    load_balancers: typing.List["LoadBalancerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMetricCollectionTypesAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.List[MetricCollectionType]),
            ),
            (
                "granularities",
                "Granularities",
                TypeInfo(typing.List[MetricGranularityType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more metrics.
    metrics: typing.List["MetricCollectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The granularities for the metrics.
    granularities: typing.List["MetricGranularityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNotificationConfigurationsAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notification_configurations",
                "NotificationConfigurations",
                TypeInfo(typing.List[NotificationConfiguration]),
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

    # The notification configurations.
    notification_configurations: typing.List["NotificationConfiguration"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator[
        "DescribeNotificationConfigurationsAnswer", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeNotificationConfigurationsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_names",
                "AutoScalingGroupNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 50 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePoliciesType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "policy_types",
                "PolicyTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of one or more policies. If you omit this parameter, all policies
    # are described. If an group name is provided, the results are limited to
    # that group. This list is limited to 50 items. If you specify an unknown
    # policy name, it is ignored with no error.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more policy types. Valid values are `SimpleScaling` and
    # `StepScaling`.
    policy_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be returned with each call. The default
    # value is 50 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingActivitiesType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activity_ids",
                "ActivityIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The activity IDs of the desired scaling activities. You can specify up to
    # 50 IDs. If you omit this parameter, all activities for the past six weeks
    # are described. If unknown activities are requested, they are ignored with
    # no error. If you specify an Auto Scaling group, the results are limited to
    # that group.
    activity_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return with this call. The default value is
    # 100 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScheduledActionsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scheduled_action_names",
                "ScheduledActionNames",
                TypeInfo(typing.List[str]),
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of one or more scheduled actions. You can specify up to 50
    # actions. If you omit this parameter, all scheduled actions are described.
    # If you specify an unknown scheduled action, it is ignored with no error.
    scheduled_action_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The earliest scheduled start time to return. If scheduled action names are
    # provided, this parameter is ignored.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The latest scheduled start time to return. If scheduled action names are
    # provided, this parameter is ignored.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 50 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # A filter used to scope the tags to return.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 50 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTerminationPolicyTypesAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "termination_policy_types",
                "TerminationPolicyTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The termination policies supported by Amazon EC2 Auto Scaling
    # (`OldestInstance`, `OldestLaunchConfiguration`, `NewestInstance`,
    # `ClosestToNextInstanceHour`, and `Default`).
    termination_policy_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachInstancesAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activities",
                "Activities",
                TypeInfo(typing.List[Activity]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The activities related to detaching the instances from the Auto Scaling
    # group.
    activities: typing.List["Activity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachInstancesQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "should_decrement_desired_capacity",
                "ShouldDecrementDesiredCapacity",
                TypeInfo(bool),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the Auto Scaling group decrements the desired capacity
    # value by the number of instances detached.
    should_decrement_desired_capacity: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the instances. You can specify up to 20 instances.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachLoadBalancerTargetGroupsResultType(OutputShapeBase):
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
class DetachLoadBalancerTargetGroupsType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "target_group_arns",
                "TargetGroupARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Names (ARN) of the target groups. You can specify up to
    # 10 target groups.
    target_group_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachLoadBalancersResultType(OutputShapeBase):
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
class DetachLoadBalancersType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "load_balancer_names",
                "LoadBalancerNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the load balancers. You can specify up to 10 load balancers.
    load_balancer_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisableMetricsCollectionQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more of the following metrics. If you omit this parameter, all
    # metrics are disabled.

    #   * `GroupMinSize`

    #   * `GroupMaxSize`

    #   * `GroupDesiredCapacity`

    #   * `GroupInServiceInstances`

    #   * `GroupPendingInstances`

    #   * `GroupStandbyInstances`

    #   * `GroupTerminatingInstances`

    #   * `GroupTotalInstances`
    metrics: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Ebs(ShapeBase):
    """
    Describes an Amazon EBS volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "volume_size",
                "VolumeSize",
                TypeInfo(int),
            ),
            (
                "volume_type",
                "VolumeType",
                TypeInfo(str),
            ),
            (
                "delete_on_termination",
                "DeleteOnTermination",
                TypeInfo(bool),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "encrypted",
                "Encrypted",
                TypeInfo(bool),
            ),
        ]

    # The ID of the snapshot.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The volume size, in GiB. For `standard` volumes, specify a value from 1 to
    # 1,024. For `io1` volumes, specify a value from 4 to 16,384. For `gp2`
    # volumes, specify a value from 1 to 16,384. If you specify a snapshot, the
    # volume size must be equal to or larger than the snapshot size.

    # Default: If you create a volume from a snapshot and you don't specify a
    # volume size, the default is the snapshot size.
    volume_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The volume type. For more information, see [Amazon EBS Volume
    # Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
    # in the _Amazon Elastic Compute Cloud User Guide_.

    # Valid values: `standard` | `io1` | `gp2`
    volume_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the volume is deleted on instance termination. The
    # default is `true`.
    delete_on_termination: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of I/O operations per second (IOPS) to provision for the volume.

    # Constraint: Required when the volume type is `io1`.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the volume should be encrypted. Encrypted EBS volumes
    # must be attached to instances that support Amazon EBS encryption. Volumes
    # that are created from encrypted snapshots are automatically encrypted.
    # There is no way to create an encrypted volume from an unencrypted snapshot
    # or an unencrypted volume from an encrypted snapshot. For more information,
    # see [Amazon EBS
    # Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
    # in the _Amazon Elastic Compute Cloud User Guide_.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableMetricsCollectionQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "granularity",
                "Granularity",
                TypeInfo(str),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The granularity to associate with the metrics to collect. The only valid
    # value is `1Minute`.
    granularity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more of the following metrics. If you omit this parameter, all
    # metrics are enabled.

    #   * `GroupMinSize`

    #   * `GroupMaxSize`

    #   * `GroupDesiredCapacity`

    #   * `GroupInServiceInstances`

    #   * `GroupPendingInstances`

    #   * `GroupStandbyInstances`

    #   * `GroupTerminatingInstances`

    #   * `GroupTotalInstances`
    metrics: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnabledMetric(ShapeBase):
    """
    Describes an enabled metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric",
                "Metric",
                TypeInfo(str),
            ),
            (
                "granularity",
                "Granularity",
                TypeInfo(str),
            ),
        ]

    # One of the following metrics:

    #   * `GroupMinSize`

    #   * `GroupMaxSize`

    #   * `GroupDesiredCapacity`

    #   * `GroupInServiceInstances`

    #   * `GroupPendingInstances`

    #   * `GroupStandbyInstances`

    #   * `GroupTerminatingInstances`

    #   * `GroupTotalInstances`
    metric: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The granularity of the metric. The only valid value is `1Minute`.
    granularity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnterStandbyAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activities",
                "Activities",
                TypeInfo(typing.List[Activity]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The activities related to moving instances into `Standby` mode.
    activities: typing.List["Activity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnterStandbyQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "should_decrement_desired_capacity",
                "ShouldDecrementDesiredCapacity",
                TypeInfo(bool),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether to decrement the desired capacity of the Auto Scaling
    # group by the number of instances moved to `Standby` mode.
    should_decrement_desired_capacity: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the instances. You can specify up to 20 instances.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExecutePolicyType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "honor_cooldown",
                "HonorCooldown",
                TypeInfo(bool),
            ),
            (
                "metric_value",
                "MetricValue",
                TypeInfo(float),
            ),
            (
                "breach_threshold",
                "BreachThreshold",
                TypeInfo(float),
            ),
        ]

    # The name or ARN of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to
    # complete before executing the policy.

    # This parameter is not supported if the policy type is `StepScaling`.

    # For more information, see [Scaling
    # Cooldowns](http://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    honor_cooldown: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metric value to compare to `BreachThreshold`. This enables you to
    # execute a policy of type `StepScaling` and determine which step adjustment
    # to use. For example, if the breach threshold is 50 and you want to use a
    # step adjustment with a lower bound of 0 and an upper bound of 10, you can
    # set the metric value to 59.

    # If you specify a metric value that doesn't correspond to a step adjustment
    # for the policy, the call returns an error.

    # This parameter is required if the policy type is `StepScaling` and not
    # supported otherwise.
    metric_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The breach threshold for the alarm.

    # This parameter is required if the policy type is `StepScaling` and not
    # supported otherwise.
    breach_threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExitStandbyAnswer(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activities",
                "Activities",
                TypeInfo(typing.List[Activity]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The activities related to moving instances out of `Standby` mode.
    activities: typing.List["Activity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExitStandbyQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of the instances. You can specify up to 20 instances.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailedScheduledUpdateGroupActionRequest(ShapeBase):
    """
    Describes a scheduled action that could not be created, updated, or deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_action_name",
                "ScheduledActionName",
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

    # The name of the scheduled action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message accompanying the error code.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Filter(ShapeBase):
    """
    Describes a filter.
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
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the filter. The valid values are: `"auto-scaling-group"`,
    # `"key"`, `"value"`, and `"propagate-at-launch"`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the filter.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Instance(ShapeBase):
    """
    Describes an EC2 instance.
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
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "lifecycle_state",
                "LifecycleState",
                TypeInfo(typing.Union[str, LifecycleState]),
            ),
            (
                "health_status",
                "HealthStatus",
                TypeInfo(str),
            ),
            (
                "protected_from_scale_in",
                "ProtectedFromScaleIn",
                TypeInfo(bool),
            ),
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "launch_template",
                "LaunchTemplate",
                TypeInfo(LaunchTemplateSpecification),
            ),
        ]

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone in which the instance is running.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the current lifecycle state. Note that the `Quarantined`
    # state is not used.
    lifecycle_state: typing.Union[str, "LifecycleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last reported health status of the instance. "Healthy" means that the
    # instance is healthy and should remain in service. "Unhealthy" means that
    # the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and
    # replace it.
    health_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the instance is protected from termination by Amazon EC2
    # Auto Scaling when scaling in.
    protected_from_scale_in: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch configuration associated with the instance.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch template for the instance.
    launch_template: "LaunchTemplateSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceMonitoring(ShapeBase):
    """
    Describes whether detailed monitoring is enabled for the Auto Scaling instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # If `true`, detailed monitoring is enabled. Otherwise, basic monitoring is
    # enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNextToken(ShapeBase):
    """
    The `NextToken` value is not valid.
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
class LaunchConfiguration(ShapeBase):
    """
    Describes a launch configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "image_id",
                "ImageId",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "launch_configuration_arn",
                "LaunchConfigurationARN",
                TypeInfo(str),
            ),
            (
                "key_name",
                "KeyName",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "classic_link_vpc_id",
                "ClassicLinkVPCId",
                TypeInfo(str),
            ),
            (
                "classic_link_vpc_security_groups",
                "ClassicLinkVPCSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "user_data",
                "UserData",
                TypeInfo(str),
            ),
            (
                "kernel_id",
                "KernelId",
                TypeInfo(str),
            ),
            (
                "ramdisk_id",
                "RamdiskId",
                TypeInfo(str),
            ),
            (
                "block_device_mappings",
                "BlockDeviceMappings",
                TypeInfo(typing.List[BlockDeviceMapping]),
            ),
            (
                "instance_monitoring",
                "InstanceMonitoring",
                TypeInfo(InstanceMonitoring),
            ),
            (
                "spot_price",
                "SpotPrice",
                TypeInfo(str),
            ),
            (
                "iam_instance_profile",
                "IamInstanceProfile",
                TypeInfo(str),
            ),
            (
                "ebs_optimized",
                "EbsOptimized",
                TypeInfo(bool),
            ),
            (
                "associate_public_ip_address",
                "AssociatePublicIpAddress",
                TypeInfo(bool),
            ),
            (
                "placement_tenancy",
                "PlacementTenancy",
                TypeInfo(str),
            ),
        ]

    # The name of the launch configuration.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Amazon Machine Image (AMI).
    image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type for the instances.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The creation date and time for the launch configuration.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the launch configuration.
    launch_configuration_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the key pair.
    key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security groups to associate with the instances.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.
    # This parameter can only be used if you are launching EC2-Classic instances.
    # For more information, see
    # [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
    # classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
    classic_link_vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of one or more security groups for the VPC specified in
    # `ClassicLinkVPCId`. This parameter is required if you specify a
    # ClassicLink-enabled VPC, and cannot be used otherwise. For more
    # information, see
    # [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
    # classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
    classic_link_vpc_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user data available to the instances.
    user_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the kernel associated with the AMI.
    kernel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the RAM disk associated with the AMI.
    ramdisk_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A block device mapping, which specifies the block devices for the instance.
    block_device_mappings: typing.List["BlockDeviceMapping"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Controls whether instances in this group are launched with detailed
    # (`true`) or basic (`false`) monitoring.
    instance_monitoring: "InstanceMonitoring" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The price to bid when launching Spot Instances.
    spot_price: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or Amazon Resource Name (ARN) of the instance profile associated
    # with the IAM role for the instance.
    iam_instance_profile: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Controls whether the instance is optimized for EBS I/O (`true`) or not
    # (`false`).
    ebs_optimized: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # [EC2-VPC] Indicates whether to assign a public IP address to each instance.
    associate_public_ip_address: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tenancy of the instance, either `default` or `dedicated`. An instance
    # with `dedicated` tenancy runs in an isolated, single-tenant hardware and
    # can only be launched into a VPC.
    placement_tenancy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LaunchConfigurationNameType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
        ]

    # The name of the launch configuration.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LaunchConfigurationNamesType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "launch_configuration_names",
                "LaunchConfigurationNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
        ]

    # The launch configuration names. If you omit this parameter, all launch
    # configurations are described.
    launch_configuration_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of items to return. (You received this token
    # from a previous call.)
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return with this call. The default value is
    # 50 and the maximum value is 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LaunchConfigurationsType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "launch_configurations",
                "LaunchConfigurations",
                TypeInfo(typing.List[LaunchConfiguration]),
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

    # The launch configurations.
    launch_configurations: typing.List["LaunchConfiguration"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["LaunchConfigurationsType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class LaunchTemplateSpecification(ShapeBase):
    """
    Describes a launch template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "launch_template_id",
                "LaunchTemplateId",
                TypeInfo(str),
            ),
            (
                "launch_template_name",
                "LaunchTemplateName",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    # The ID of the launch template. You must specify either a template ID or a
    # template name.
    launch_template_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the launch template. You must specify either a template name or
    # a template ID.
    launch_template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number, `$Latest`, or `$Default`. If the value is `$Latest`,
    # Amazon EC2 Auto Scaling selects the latest version of the launch template
    # when launching instances. If the value is `$Default`, Amazon EC2 Auto
    # Scaling selects the default version of the launch template when launching
    # instances. The default value is `$Default`.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecycleHook(ShapeBase):
    """
    Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to
    perform an action whenever it launches instances or whenever it terminates
    instances.

    For more information, see [Lifecycle
    Hooks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-
    hooks.html) in the _Amazon EC2 Auto Scaling User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_hook_name",
                "LifecycleHookName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "lifecycle_transition",
                "LifecycleTransition",
                TypeInfo(str),
            ),
            (
                "notification_target_arn",
                "NotificationTargetARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "notification_metadata",
                "NotificationMetadata",
                TypeInfo(str),
            ),
            (
                "heartbeat_timeout",
                "HeartbeatTimeout",
                TypeInfo(int),
            ),
            (
                "global_timeout",
                "GlobalTimeout",
                TypeInfo(int),
            ),
            (
                "default_result",
                "DefaultResult",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle hook.
    lifecycle_hook_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group for the lifecycle hook.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the EC2 instance to which you want to attach the lifecycle
    # hook. The following are possible values:

    #   * autoscaling:EC2_INSTANCE_LAUNCHING

    #   * autoscaling:EC2_INSTANCE_TERMINATING
    lifecycle_transition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the target that Amazon EC2 Auto Scaling sends notifications to
    # when an instance is in the transition state for the lifecycle hook. The
    # notification target can be either an SQS queue or an SNS topic.
    notification_target_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the IAM role that allows the Auto Scaling group to publish to
    # the specified notification target.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information that you want to include any time Amazon EC2 Auto
    # Scaling sends a message to the notification target.
    notification_metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time, in seconds, that can elapse before the lifecycle hook
    # times out. If the lifecycle hook times out, Amazon EC2 Auto Scaling
    # performs the default action. You can prevent the lifecycle hook from timing
    # out by calling RecordLifecycleActionHeartbeat.
    heartbeat_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time, in seconds, that an instance can remain in a
    # `Pending:Wait` or `Terminating:Wait` state. The maximum is 172800 seconds
    # (48 hours) or 100 times `HeartbeatTimeout`, whichever is smaller.
    global_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines the action the Auto Scaling group should take when the lifecycle
    # hook timeout elapses or if an unexpected failure occurs. The valid values
    # are `CONTINUE` and `ABANDON`. The default value is `CONTINUE`.
    default_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecycleHookSpecification(ShapeBase):
    """
    Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to
    perform an action whenever it launches instances or whenever it terminates
    instances.

    For more information, see [Lifecycle
    Hooks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-
    hooks.html) in the _Amazon EC2 Auto Scaling User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_hook_name",
                "LifecycleHookName",
                TypeInfo(str),
            ),
            (
                "lifecycle_transition",
                "LifecycleTransition",
                TypeInfo(str),
            ),
            (
                "notification_metadata",
                "NotificationMetadata",
                TypeInfo(str),
            ),
            (
                "heartbeat_timeout",
                "HeartbeatTimeout",
                TypeInfo(int),
            ),
            (
                "default_result",
                "DefaultResult",
                TypeInfo(str),
            ),
            (
                "notification_target_arn",
                "NotificationTargetARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle hook.
    lifecycle_hook_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the EC2 instance to which you want to attach the lifecycle
    # hook. The possible values are:

    #   * autoscaling:EC2_INSTANCE_LAUNCHING

    #   * autoscaling:EC2_INSTANCE_TERMINATING
    lifecycle_transition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information that you want to include any time Amazon EC2 Auto
    # Scaling sends a message to the notification target.
    notification_metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time, in seconds, that can elapse before the lifecycle hook
    # times out. If the lifecycle hook times out, Amazon EC2 Auto Scaling
    # performs the default action. You can prevent the lifecycle hook from timing
    # out by calling RecordLifecycleActionHeartbeat.
    heartbeat_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines the action the Auto Scaling group should take when the lifecycle
    # hook timeout elapses or if an unexpected failure occurs. The valid values
    # are `CONTINUE` and `ABANDON`.
    default_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the target that Amazon EC2 Auto Scaling sends notifications to
    # when an instance is in the transition state for the lifecycle hook. The
    # notification target can be either an SQS queue or an SNS topic.
    notification_target_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the IAM role that allows the Auto Scaling group to publish to
    # the specified notification target.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LifecycleState(str):
    Pending = "Pending"
    Pending_Wait = "Pending:Wait"
    Pending_Proceed = "Pending:Proceed"
    Quarantined = "Quarantined"
    InService = "InService"
    Terminating = "Terminating"
    Terminating_Wait = "Terminating:Wait"
    Terminating_Proceed = "Terminating:Proceed"
    Terminated = "Terminated"
    Detaching = "Detaching"
    Detached = "Detached"
    EnteringStandby = "EnteringStandby"
    Standby = "Standby"


@dataclasses.dataclass
class LimitExceededFault(ShapeBase):
    """
    You have already reached a limit for your Auto Scaling resources (for example,
    groups, launch configurations, or lifecycle hooks). For more information, see
    DescribeAccountLimits.
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
class LoadBalancerState(ShapeBase):
    """
    Describes the state of a Classic Load Balancer.

    If you specify a load balancer when creating the Auto Scaling group, the state
    of the load balancer is `InService`.

    If you attach a load balancer to an existing Auto Scaling group, the initial
    state is `Adding`. The state transitions to `Added` after all instances in the
    group are registered with the load balancer. If ELB health checks are enabled
    for the load balancer, the state transitions to `InService` after at least one
    instance in the group passes the health check. If EC2 health checks are enabled
    instead, the load balancer remains in the `Added` state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "LoadBalancerName",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the following load balancer states:

    #   * `Adding` \- The instances in the group are being registered with the load balancer.

    #   * `Added` \- All instances in the group are registered with the load balancer.

    #   * `InService` \- At least one instance in the group passed an ELB health check.

    #   * `Removing` \- The instances in the group are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.

    #   * `Removed` \- All instances in the group are deregistered from the load balancer.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoadBalancerTargetGroupState(ShapeBase):
    """
    Describes the state of a target group.

    If you attach a target group to an existing Auto Scaling group, the initial
    state is `Adding`. The state transitions to `Added` after all Auto Scaling
    instances are registered with the target group. If ELB health checks are
    enabled, the state transitions to `InService` after at least one Auto Scaling
    instance passes the health check. If EC2 health checks are enabled instead, the
    target group remains in the `Added` state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_target_group_arn",
                "LoadBalancerTargetGroupARN",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the target group.
    load_balancer_target_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the target group.

    #   * `Adding` \- The Auto Scaling instances are being registered with the target group.

    #   * `Added` \- All Auto Scaling instances are registered with the target group.

    #   * `InService` \- At least one Auto Scaling instance passed an ELB health check.

    #   * `Removing` \- The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.

    #   * `Removed` \- All Auto Scaling instances are deregistered from the target group.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricCollectionType(ShapeBase):
    """
    Describes a metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric",
                "Metric",
                TypeInfo(str),
            ),
        ]

    # One of the following metrics:

    #   * `GroupMinSize`

    #   * `GroupMaxSize`

    #   * `GroupDesiredCapacity`

    #   * `GroupInServiceInstances`

    #   * `GroupPendingInstances`

    #   * `GroupStandbyInstances`

    #   * `GroupTerminatingInstances`

    #   * `GroupTotalInstances`
    metric: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDimension(ShapeBase):
    """
    Describes the dimension of a metric.
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
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The name of the dimension.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the dimension.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricGranularityType(ShapeBase):
    """
    Describes a granularity of a metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "granularity",
                "Granularity",
                TypeInfo(str),
            ),
        ]

    # The granularity. The only valid value is `1Minute`.
    granularity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MetricStatistic(str):
    Average = "Average"
    Minimum = "Minimum"
    Maximum = "Maximum"
    SampleCount = "SampleCount"
    Sum = "Sum"


class MetricType(str):
    ASGAverageCPUUtilization = "ASGAverageCPUUtilization"
    ASGAverageNetworkIn = "ASGAverageNetworkIn"
    ASGAverageNetworkOut = "ASGAverageNetworkOut"
    ALBRequestCountPerTarget = "ALBRequestCountPerTarget"


@dataclasses.dataclass
class NotificationConfiguration(ShapeBase):
    """
    Describes a notification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicARN",
                TypeInfo(str),
            ),
            (
                "notification_type",
                "NotificationType",
                TypeInfo(str),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
    # (SNS) topic.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the following event notification types:

    #   * `autoscaling:EC2_INSTANCE_LAUNCH`

    #   * `autoscaling:EC2_INSTANCE_LAUNCH_ERROR`

    #   * `autoscaling:EC2_INSTANCE_TERMINATE`

    #   * `autoscaling:EC2_INSTANCE_TERMINATE_ERROR`

    #   * `autoscaling:TEST_NOTIFICATION`
    notification_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PoliciesType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scaling_policies",
                "ScalingPolicies",
                TypeInfo(typing.List[ScalingPolicy]),
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

    # The scaling policies.
    scaling_policies: typing.List["ScalingPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["PoliciesType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class PolicyARNType(OutputShapeBase):
    """
    Contains the output of PutScalingPolicy.
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
                "policy_arn",
                "PolicyARN",
                TypeInfo(str),
            ),
            (
                "alarms",
                "Alarms",
                TypeInfo(typing.List[Alarm]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the policy.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CloudWatch alarms created for the target tracking policy.
    alarms: typing.List["Alarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PredefinedMetricSpecification(ShapeBase):
    """
    Configures a predefined metric for a target tracking policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "predefined_metric_type",
                "PredefinedMetricType",
                TypeInfo(typing.Union[str, MetricType]),
            ),
            (
                "resource_label",
                "ResourceLabel",
                TypeInfo(str),
            ),
        ]

    # The metric type.
    predefined_metric_type: typing.Union[str, "MetricType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the resource associated with the metric type. The following
    # predefined metrics are available:

    #   * `ASGAverageCPUUtilization` \- average CPU utilization of the Auto Scaling group

    #   * `ASGAverageNetworkIn` \- average number of bytes received on all network interfaces by the Auto Scaling group

    #   * `ASGAverageNetworkOut` \- average number of bytes sent out on all network interfaces by the Auto Scaling group

    #   * `ALBRequestCountPerTarget` \- number of requests completed per target in an Application Load Balancer target group

    # For predefined metric types `ASGAverageCPUUtilization`,
    # `ASGAverageNetworkIn`, and `ASGAverageNetworkOut`, the parameter must not
    # be specified as the resource associated with the metric type is the Auto
    # Scaling group. For predefined metric type `ALBRequestCountPerTarget`, the
    # parameter must be specified in the format: `app/ _load-balancer-name_ /
    # _load-balancer-id_ /targetgroup/ _target-group-name_ / _target-group-id_ `,
    # where `app/ _load-balancer-name_ / _load-balancer-id_ ` is the final
    # portion of the load balancer ARN, and `targetgroup/ _target-group-name_ /
    # _target-group-id_ ` is the final portion of the target group ARN. The
    # target group must be attached to the Auto Scaling group.
    resource_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProcessType(ShapeBase):
    """
    Describes a process type.

    For more information, see [Scaling
    Processes](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-
    resume-processes.html#process-types) in the _Amazon EC2 Auto Scaling User
    Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "process_name",
                "ProcessName",
                TypeInfo(str),
            ),
        ]

    # One of the following processes:

    #   * `Launch`

    #   * `Terminate`

    #   * `AddToLoadBalancer`

    #   * `AlarmNotification`

    #   * `AZRebalance`

    #   * `HealthCheck`

    #   * `ReplaceUnhealthy`

    #   * `ScheduledActions`
    process_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProcessesType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "processes",
                "Processes",
                TypeInfo(typing.List[ProcessType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the process types.
    processes: typing.List["ProcessType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutLifecycleHookAnswer(OutputShapeBase):
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
class PutLifecycleHookType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_hook_name",
                "LifecycleHookName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "lifecycle_transition",
                "LifecycleTransition",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "notification_target_arn",
                "NotificationTargetARN",
                TypeInfo(str),
            ),
            (
                "notification_metadata",
                "NotificationMetadata",
                TypeInfo(str),
            ),
            (
                "heartbeat_timeout",
                "HeartbeatTimeout",
                TypeInfo(int),
            ),
            (
                "default_result",
                "DefaultResult",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle hook.
    lifecycle_hook_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance state to which you want to attach the lifecycle hook. The
    # possible values are:

    #   * autoscaling:EC2_INSTANCE_LAUNCHING

    #   * autoscaling:EC2_INSTANCE_TERMINATING

    # This parameter is required for new lifecycle hooks, but optional when
    # updating existing hooks.
    lifecycle_transition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role that allows the Auto Scaling group to publish to
    # the specified notification target.

    # This parameter is required for new lifecycle hooks, but optional when
    # updating existing hooks.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the notification target that Amazon EC2 Auto Scaling will use to
    # notify you when an instance is in the transition state for the lifecycle
    # hook. This target can be either an SQS queue or an SNS topic. If you
    # specify an empty string, this overrides the current ARN.

    # This operation uses the JSON format when sending notifications to an Amazon
    # SQS queue, and an email key/value pair format when sending notifications to
    # an Amazon SNS topic.

    # When you specify a notification target, Amazon EC2 Auto Scaling sends it a
    # test message. Test messages contains the following additional key/value
    # pair: `"Event": "autoscaling:TEST_NOTIFICATION"`.
    notification_target_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains additional information that you want to include any time Amazon
    # EC2 Auto Scaling sends a message to the notification target.
    notification_metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum time, in seconds, that can elapse before the lifecycle hook
    # times out. The range is from 30 to 7200 seconds. The default is 3600
    # seconds (1 hour).

    # If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the
    # default action. You can prevent the lifecycle hook from timing out by
    # calling RecordLifecycleActionHeartbeat.
    heartbeat_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines the action the Auto Scaling group should take when the lifecycle
    # hook timeout elapses or if an unexpected failure occurs. This parameter can
    # be either `CONTINUE` or `ABANDON`. The default value is `ABANDON`.
    default_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutNotificationConfigurationType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicARN",
                TypeInfo(str),
            ),
            (
                "notification_types",
                "NotificationTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
    # (SNS) topic.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of event that will cause the notification to be sent. For details
    # about notification types supported by Amazon EC2 Auto Scaling, see
    # DescribeAutoScalingNotificationTypes.
    notification_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutScalingPolicyType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(str),
            ),
            (
                "adjustment_type",
                "AdjustmentType",
                TypeInfo(str),
            ),
            (
                "min_adjustment_step",
                "MinAdjustmentStep",
                TypeInfo(int),
            ),
            (
                "min_adjustment_magnitude",
                "MinAdjustmentMagnitude",
                TypeInfo(int),
            ),
            (
                "scaling_adjustment",
                "ScalingAdjustment",
                TypeInfo(int),
            ),
            (
                "cooldown",
                "Cooldown",
                TypeInfo(int),
            ),
            (
                "metric_aggregation_type",
                "MetricAggregationType",
                TypeInfo(str),
            ),
            (
                "step_adjustments",
                "StepAdjustments",
                TypeInfo(typing.List[StepAdjustment]),
            ),
            (
                "estimated_instance_warmup",
                "EstimatedInstanceWarmup",
                TypeInfo(int),
            ),
            (
                "target_tracking_configuration",
                "TargetTrackingConfiguration",
                TypeInfo(TargetTrackingConfiguration),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy type. The valid values are `SimpleScaling`, `StepScaling`, and
    # `TargetTrackingScaling`. If the policy type is null, the value is treated
    # as `SimpleScaling`.
    policy_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The adjustment type. The valid values are `ChangeInCapacity`,
    # `ExactCapacity`, and `PercentChangeInCapacity`.

    # This parameter is supported if the policy type is `SimpleScaling` or
    # `StepScaling`.

    # For more information, see [Dynamic
    # Scaling](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-
    # based-on-demand.html) in the _Amazon EC2 Auto Scaling User Guide_.
    adjustment_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Available for backward compatibility. Use `MinAdjustmentMagnitude` instead.
    min_adjustment_step: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum number of instances to scale. If the value of `AdjustmentType`
    # is `PercentChangeInCapacity`, the scaling policy changes the
    # `DesiredCapacity` of the Auto Scaling group by at least this many
    # instances. Otherwise, the error is `ValidationError`.

    # This parameter is supported if the policy type is `SimpleScaling` or
    # `StepScaling`.
    min_adjustment_magnitude: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount by which to scale, based on the specified adjustment type. A
    # positive value adds to the current capacity while a negative number removes
    # from the current capacity.

    # This parameter is required if the policy type is `SimpleScaling` and not
    # supported otherwise.
    scaling_adjustment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scaling activity completes and
    # before the next scaling activity can start. If this parameter is not
    # specified, the default cooldown period for the group applies.

    # This parameter is supported if the policy type is `SimpleScaling`.

    # For more information, see [Scaling
    # Cooldowns](http://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The aggregation type for the CloudWatch metrics. The valid values are
    # `Minimum`, `Maximum`, and `Average`. If the aggregation type is null, the
    # value is treated as `Average`.

    # This parameter is supported if the policy type is `StepScaling`.
    metric_aggregation_type: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of adjustments that enable you to scale based on the size of the
    # alarm breach.

    # This parameter is required if the policy type is `StepScaling` and not
    # supported otherwise.
    step_adjustments: typing.List["StepAdjustment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimated time, in seconds, until a newly launched instance can
    # contribute to the CloudWatch metrics. The default is to use the value
    # specified for the default cooldown period for the group.

    # This parameter is supported if the policy type is `StepScaling` or
    # `TargetTrackingScaling`.
    estimated_instance_warmup: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A target tracking policy.

    # This parameter is required if the policy type is `TargetTrackingScaling`
    # and not supported otherwise.
    target_tracking_configuration: "TargetTrackingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutScheduledUpdateGroupActionType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scheduled_action_name",
                "ScheduledActionName",
                TypeInfo(str),
            ),
            (
                "time",
                "Time",
                TypeInfo(datetime.datetime),
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
                "recurrence",
                "Recurrence",
                TypeInfo(str),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of this scaling action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is deprecated.
    time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in
    # UTC/GMT only (for example, `2014-06-01T00:00:00Z`).

    # If you specify `Recurrence` and `StartTime`, Amazon EC2 Auto Scaling
    # performs the action at this time, and then performs the action based on the
    # specified recurrence.

    # If you try to schedule your action in the past, Amazon EC2 Auto Scaling
    # returns an error message.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time for the recurring schedule to end. Amazon EC2 Auto Scaling does
    # not perform the action after this time.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring schedule for this action, in Unix cron syntax format. For
    # more information about this format, see [Crontab](http://crontab.org).
    recurrence: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum size for the Auto Scaling group.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size for the Auto Scaling group.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of EC2 instances that should be running in the group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecordLifecycleActionHeartbeatAnswer(OutputShapeBase):
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
class RecordLifecycleActionHeartbeatType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lifecycle_hook_name",
                "LifecycleHookName",
                TypeInfo(str),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "lifecycle_action_token",
                "LifecycleActionToken",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle hook.
    lifecycle_hook_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token that uniquely identifies a specific lifecycle action associated
    # with an instance. Amazon EC2 Auto Scaling sends this token to the
    # notification target you specified when you created the lifecycle hook.
    lifecycle_action_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceContentionFault(ShapeBase):
    """
    You already have a pending update to an Auto Scaling resource (for example, a
    group, instance, or load balancer).
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
class ResourceInUseFault(ShapeBase):
    """
    The operation can't be performed because the resource is in use.
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
class ScalingActivityInProgressFault(ShapeBase):
    """
    The operation can't be performed because there are scaling activities in
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
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScalingActivityStatusCode(str):
    PendingSpotBidPlacement = "PendingSpotBidPlacement"
    WaitingForSpotInstanceRequestId = "WaitingForSpotInstanceRequestId"
    WaitingForSpotInstanceId = "WaitingForSpotInstanceId"
    WaitingForInstanceId = "WaitingForInstanceId"
    PreInService = "PreInService"
    InProgress = "InProgress"
    WaitingForELBConnectionDraining = "WaitingForELBConnectionDraining"
    MidLifecycleAction = "MidLifecycleAction"
    WaitingForInstanceWarmup = "WaitingForInstanceWarmup"
    Successful = "Successful"
    Failed = "Failed"
    Cancelled = "Cancelled"


@dataclasses.dataclass
class ScalingPolicy(ShapeBase):
    """
    Describes a scaling policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_arn",
                "PolicyARN",
                TypeInfo(str),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(str),
            ),
            (
                "adjustment_type",
                "AdjustmentType",
                TypeInfo(str),
            ),
            (
                "min_adjustment_step",
                "MinAdjustmentStep",
                TypeInfo(int),
            ),
            (
                "min_adjustment_magnitude",
                "MinAdjustmentMagnitude",
                TypeInfo(int),
            ),
            (
                "scaling_adjustment",
                "ScalingAdjustment",
                TypeInfo(int),
            ),
            (
                "cooldown",
                "Cooldown",
                TypeInfo(int),
            ),
            (
                "step_adjustments",
                "StepAdjustments",
                TypeInfo(typing.List[StepAdjustment]),
            ),
            (
                "metric_aggregation_type",
                "MetricAggregationType",
                TypeInfo(str),
            ),
            (
                "estimated_instance_warmup",
                "EstimatedInstanceWarmup",
                TypeInfo(int),
            ),
            (
                "alarms",
                "Alarms",
                TypeInfo(typing.List[Alarm]),
            ),
            (
                "target_tracking_configuration",
                "TargetTrackingConfiguration",
                TypeInfo(TargetTrackingConfiguration),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the policy.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The policy type. Valid values are `SimpleScaling` and `StepScaling`.
    policy_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The adjustment type, which specifies how `ScalingAdjustment` is
    # interpreted. Valid values are `ChangeInCapacity`, `ExactCapacity`, and
    # `PercentChangeInCapacity`.
    adjustment_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Available for backward compatibility. Use `MinAdjustmentMagnitude` instead.
    min_adjustment_step: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum number of instances to scale. If the value of `AdjustmentType`
    # is `PercentChangeInCapacity`, the scaling policy changes the
    # `DesiredCapacity` of the Auto Scaling group by at least this many
    # instances. Otherwise, the error is `ValidationError`.
    min_adjustment_magnitude: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount by which to scale, based on the specified adjustment type. A
    # positive value adds to the current capacity while a negative number removes
    # from the current capacity.
    scaling_adjustment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scaling activity completes before
    # any further dynamic scaling activities can start.
    cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of adjustments that enable you to scale based on the size of the
    # alarm breach.
    step_adjustments: typing.List["StepAdjustment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The aggregation type for the CloudWatch metrics. Valid values are
    # `Minimum`, `Maximum`, and `Average`.
    metric_aggregation_type: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimated time, in seconds, until a newly launched instance can
    # contribute to the CloudWatch metrics.
    estimated_instance_warmup: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatch alarms related to the policy.
    alarms: typing.List["Alarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A target tracking policy.
    target_tracking_configuration: "TargetTrackingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScalingProcessQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scaling_processes",
                "ScalingProcesses",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more of the following processes. If you omit this parameter, all
    # processes are specified.

    #   * `Launch`

    #   * `Terminate`

    #   * `HealthCheck`

    #   * `ReplaceUnhealthy`

    #   * `AZRebalance`

    #   * `AlarmNotification`

    #   * `ScheduledActions`

    #   * `AddToLoadBalancer`
    scaling_processes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduledActionsType(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scheduled_update_group_actions",
                "ScheduledUpdateGroupActions",
                TypeInfo(typing.List[ScheduledUpdateGroupAction]),
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

    # The scheduled actions.
    scheduled_update_group_actions: typing.List["ScheduledUpdateGroupAction"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ScheduledActionsType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ScheduledUpdateGroupAction(ShapeBase):
    """
    Describes a scheduled scaling action. Used in response to
    DescribeScheduledActions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "scheduled_action_name",
                "ScheduledActionName",
                TypeInfo(str),
            ),
            (
                "scheduled_action_arn",
                "ScheduledActionARN",
                TypeInfo(str),
            ),
            (
                "time",
                "Time",
                TypeInfo(datetime.datetime),
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
                "recurrence",
                "Recurrence",
                TypeInfo(str),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the scheduled action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the scheduled action.
    scheduled_action_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is deprecated.
    time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the action is scheduled to begin. This date and time
    # can be up to one month in the future.

    # When `StartTime` and `EndTime` are specified with `Recurrence`, they form
    # the boundaries of when the recurring action will start and stop.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the action is scheduled to end. This date and time
    # can be up to one month in the future.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring schedule for the action.
    recurrence: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum size of the group.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the group.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances you prefer to maintain in the group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScheduledUpdateGroupActionRequest(ShapeBase):
    """
    Describes one or more scheduled scaling action updates for a specified Auto
    Scaling group. Used in combination with BatchPutScheduledUpdateGroupAction.

    When updating a scheduled scaling action, all optional parameters are left
    unchanged if not specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scheduled_action_name",
                "ScheduledActionName",
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
                "recurrence",
                "Recurrence",
                TypeInfo(str),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
        ]

    # The name of the scaling action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time for the action to start, in "YYYY-MM-DDThh:mm:ssZ" format in
    # UTC/GMT only (for example, `2014-06-01T00:00:00Z`).

    # If you specify `Recurrence` and `StartTime`, Amazon EC2 Auto Scaling
    # performs the action at this time, and then performs the action based on the
    # specified recurrence.

    # If you try to schedule the action in the past, Amazon EC2 Auto Scaling
    # returns an error message.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time for the recurring schedule to end. Amazon EC2 Auto Scaling does
    # not perform the action after this time.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring schedule for the action, in Unix cron syntax format. For more
    # information about this format, see [Crontab](http://crontab.org).
    recurrence: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum size of the group.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the group.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of EC2 instances that should be running in the group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceLinkedRoleFailure(ShapeBase):
    """
    The service-linked role is not yet ready for use.
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
class SetDesiredCapacityType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
            (
                "honor_cooldown",
                "HonorCooldown",
                TypeInfo(bool),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of EC2 instances that should be running in the Auto Scaling
    # group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to
    # complete before initiating a scaling activity to set your Auto Scaling
    # group to its new capacity. By default, Amazon EC2 Auto Scaling does not
    # honor the cooldown period during manual scaling activities.
    honor_cooldown: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetInstanceHealthQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "health_status",
                "HealthStatus",
                TypeInfo(str),
            ),
            (
                "should_respect_grace_period",
                "ShouldRespectGracePeriod",
                TypeInfo(bool),
            ),
        ]

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The health status of the instance. Set to `Healthy` if you want the
    # instance to remain in service. Set to `Unhealthy` if you want the instance
    # to be out of service. Amazon EC2 Auto Scaling will terminate and replace
    # the unhealthy instance.
    health_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the Auto Scaling group of the specified instance has a
    # `HealthCheckGracePeriod` specified for the group, by default, this call
    # will respect the grace period. Set this to `False`, if you do not want the
    # call to respect the grace period associated with the group.

    # For more information, see the description of the health check grace period
    # for CreateAutoScalingGroup.
    should_respect_grace_period: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetInstanceProtectionAnswer(OutputShapeBase):
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
class SetInstanceProtectionQuery(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_ids",
                "InstanceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "protected_from_scale_in",
                "ProtectedFromScaleIn",
                TypeInfo(bool),
            ),
        ]

    # One or more instance IDs.
    instance_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the instance is protected from termination by Amazon EC2
    # Auto Scaling when scaling in.
    protected_from_scale_in: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StepAdjustment(ShapeBase):
    """
    Describes an adjustment based on the difference between the value of the
    aggregated CloudWatch metric and the breach threshold that you've defined for
    the alarm.

    For the following examples, suppose that you have an alarm with a breach
    threshold of 50:

      * If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.

      * If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

      * The ranges of your step adjustments can't overlap or have a gap.

      * At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.

      * At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.

      * The upper and lower bound can't be null in the same step adjustment.
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
                "metric_interval_lower_bound",
                "MetricIntervalLowerBound",
                TypeInfo(float),
            ),
            (
                "metric_interval_upper_bound",
                "MetricIntervalUpperBound",
                TypeInfo(float),
            ),
        ]

    # The amount by which to scale, based on the specified adjustment type. A
    # positive value adds to the current capacity while a negative number removes
    # from the current capacity.
    scaling_adjustment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The lower bound for the difference between the alarm threshold and the
    # CloudWatch metric. If the metric value is above the breach threshold, the
    # lower bound is inclusive (the metric must be greater than or equal to the
    # threshold plus the lower bound). Otherwise, it is exclusive (the metric
    # must be greater than the threshold plus the lower bound). A null value
    # indicates negative infinity.
    metric_interval_lower_bound: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upper bound for the difference between the alarm threshold and the
    # CloudWatch metric. If the metric value is above the breach threshold, the
    # upper bound is exclusive (the metric must be less than the threshold plus
    # the upper bound). Otherwise, it is inclusive (the metric must be less than
    # or equal to the threshold plus the upper bound). A null value indicates
    # positive infinity.

    # The upper bound must be greater than the lower bound.
    metric_interval_upper_bound: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SuspendedProcess(ShapeBase):
    """
    Describes an automatic scaling process that has been suspended. For more
    information, see ProcessType.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "process_name",
                "ProcessName",
                TypeInfo(str),
            ),
            (
                "suspension_reason",
                "SuspensionReason",
                TypeInfo(str),
            ),
        ]

    # The name of the suspended process.
    process_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason that the process was suspended.
    suspension_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Describes a tag for an Auto Scaling group.
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
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "propagate_at_launch",
                "PropagateAtLaunch",
                TypeInfo(bool),
            ),
        ]

    # The tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the group.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource. The only supported value is `auto-scaling-group`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines whether the tag is added to new instances as they are launched
    # in the group.
    propagate_at_launch: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagDescription(ShapeBase):
    """
    Describes a tag for an Auto Scaling group.
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
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
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
                "propagate_at_launch",
                "PropagateAtLaunch",
                TypeInfo(bool),
            ),
        ]

    # The name of the group.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource. The only supported value is `auto-scaling-group`.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines whether the tag is added to new instances as they are launched
    # in the group.
    propagate_at_launch: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagsType(OutputShapeBase):
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
                "Tags",
                TypeInfo(typing.List[TagDescription]),
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

    # One or more tags.
    tags: typing.List["TagDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use when requesting the next set of items. If there are no
    # additional items to return, the string is empty.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["TagsType", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class TargetTrackingConfiguration(ShapeBase):
    """
    Represents a target tracking policy configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_value",
                "TargetValue",
                TypeInfo(float),
            ),
            (
                "predefined_metric_specification",
                "PredefinedMetricSpecification",
                TypeInfo(PredefinedMetricSpecification),
            ),
            (
                "customized_metric_specification",
                "CustomizedMetricSpecification",
                TypeInfo(CustomizedMetricSpecification),
            ),
            (
                "disable_scale_in",
                "DisableScaleIn",
                TypeInfo(bool),
            ),
        ]

    # The target value for the metric.
    target_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A predefined metric. You can specify either a predefined metric or a
    # customized metric.
    predefined_metric_specification: "PredefinedMetricSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A customized metric.
    customized_metric_specification: "CustomizedMetricSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether scale in by the target tracking policy is disabled. If
    # scale in is disabled, the target tracking policy won't remove instances
    # from the Auto Scaling group. Otherwise, the target tracking policy can
    # remove instances from the Auto Scaling group. The default is disabled.
    disable_scale_in: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateInstanceInAutoScalingGroupType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "should_decrement_desired_capacity",
                "ShouldDecrementDesiredCapacity",
                TypeInfo(bool),
            ),
        ]

    # The ID of the instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether terminating the instance also decrements the size of the
    # Auto Scaling group.
    should_decrement_desired_capacity: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAutoScalingGroupType(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_scaling_group_name",
                "AutoScalingGroupName",
                TypeInfo(str),
            ),
            (
                "launch_configuration_name",
                "LaunchConfigurationName",
                TypeInfo(str),
            ),
            (
                "launch_template",
                "LaunchTemplate",
                TypeInfo(LaunchTemplateSpecification),
            ),
            (
                "min_size",
                "MinSize",
                TypeInfo(int),
            ),
            (
                "max_size",
                "MaxSize",
                TypeInfo(int),
            ),
            (
                "desired_capacity",
                "DesiredCapacity",
                TypeInfo(int),
            ),
            (
                "default_cooldown",
                "DefaultCooldown",
                TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "health_check_type",
                "HealthCheckType",
                TypeInfo(str),
            ),
            (
                "health_check_grace_period",
                "HealthCheckGracePeriod",
                TypeInfo(int),
            ),
            (
                "placement_group",
                "PlacementGroup",
                TypeInfo(str),
            ),
            (
                "vpc_zone_identifier",
                "VPCZoneIdentifier",
                TypeInfo(str),
            ),
            (
                "termination_policies",
                "TerminationPolicies",
                TypeInfo(typing.List[str]),
            ),
            (
                "new_instances_protected_from_scale_in",
                "NewInstancesProtectedFromScaleIn",
                TypeInfo(bool),
            ),
            (
                "service_linked_role_arn",
                "ServiceLinkedRoleARN",
                TypeInfo(str),
            ),
        ]

    # The name of the Auto Scaling group.
    auto_scaling_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the launch configuration. If you specify a launch
    # configuration, you can't specify a launch template.
    launch_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch template to use to specify the updates. If you specify a launch
    # template, you can't specify a launch configuration.
    launch_template: "LaunchTemplateSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum size of the Auto Scaling group.
    min_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum size of the Auto Scaling group.
    max_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of EC2 instances that should be running in the Auto Scaling
    # group. This number must be greater than or equal to the minimum size of the
    # group and less than or equal to the maximum size of the group.
    desired_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scaling activity completes before
    # another scaling activity can start. The default is 300.

    # For more information, see [Scaling
    # Cooldowns](http://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    default_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more Availability Zones for the group.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service to use for the health checks. The valid values are `EC2` and
    # `ELB`.
    health_check_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before
    # checking the health status of an EC2 instance that has come into service.
    # The default is 0.

    # For more information, see [Health
    # Checks](http://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    health_check_grace_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the placement group into which you'll launch your instances, if
    # any. For more information, see [Placement
    # Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-
    # groups.html) in the _Amazon Elastic Compute Cloud User Guide_.
    placement_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the subnet, if you are launching into a VPC. You can specify
    # several subnets in a comma-separated list.

    # When you specify `VPCZoneIdentifier` with `AvailabilityZones`, ensure that
    # the subnets' Availability Zones match the values you specify for
    # `AvailabilityZones`.

    # For more information, see [Launching Auto Scaling Instances in a
    # VPC](http://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html)
    # in the _Amazon EC2 Auto Scaling User Guide_.
    vpc_zone_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standalone termination policy or a list of termination policies used to
    # select the instance to terminate. The policies are executed in the order
    # that they are listed.

    # For more information, see [Controlling Which Instances Auto Scaling
    # Terminates During Scale
    # In](http://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-
    # termination.html) in the _Auto Scaling User Guide_.
    termination_policies: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether newly launched instances are protected from termination
    # by Auto Scaling when scaling in.
    new_instances_protected_from_scale_in: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the service-linked role that the Auto
    # Scaling group uses to call other AWS services on your behalf.
    service_linked_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
