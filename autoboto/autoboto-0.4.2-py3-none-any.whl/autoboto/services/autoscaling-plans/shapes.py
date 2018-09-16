import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class ApplicationSource(ShapeBase):
    """
    Represents an application source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_formation_stack_arn",
                "CloudFormationStackARN",
                TypeInfo(str),
            ),
            (
                "tag_filters",
                "TagFilters",
                TypeInfo(typing.List[TagFilter]),
            ),
        ]

    # The Amazon Resource Name (ARN) of a CloudFormation stack.
    cloud_formation_stack_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of tags (up to 50).
    tag_filters: typing.List["TagFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConcurrentUpdateException(ShapeBase):
    """
    Concurrent updates caused an exception, for example, if you request an update to
    a scaling plan that already has a pending update.
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
class CreateScalingPlanRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_name",
                "ScalingPlanName",
                TypeInfo(str),
            ),
            (
                "application_source",
                "ApplicationSource",
                TypeInfo(ApplicationSource),
            ),
            (
                "scaling_instructions",
                "ScalingInstructions",
                TypeInfo(typing.List[ScalingInstruction]),
            ),
        ]

    # The name of the scaling plan. Names cannot contain vertical bars, colons,
    # or forward slashes.
    scaling_plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A CloudFormation stack or set of tags. You can create one scaling plan per
    # application source.
    application_source: "ApplicationSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scaling instructions.
    scaling_instructions: typing.List["ScalingInstruction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateScalingPlanResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the scaling plan. This value is always 1.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomizedScalingMetricSpecification(ShapeBase):
    """
    Represents a customized metric for a target tracking policy.
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
class DeleteScalingPlanRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_name",
                "ScalingPlanName",
                TypeInfo(str),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
            ),
        ]

    # The name of the scaling plan.
    scaling_plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the scaling plan.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteScalingPlanResponse(OutputShapeBase):
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
class DescribeScalingPlanResourcesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_name",
                "ScalingPlanName",
                TypeInfo(str),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
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

    # The name of the scaling plan.
    scaling_plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the scaling plan.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of scalable resources to return. This value can be
    # between 1 and 50. The default value is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingPlanResourcesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scaling_plan_resources",
                "ScalingPlanResources",
                TypeInfo(typing.List[ScalingPlanResource]),
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

    # Information about the scalable resources.
    scaling_plan_resources: typing.List["ScalingPlanResource"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The token required to get the next set of results. This value is `null` if
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingPlansRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_names",
                "ScalingPlanNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
            ),
            (
                "application_sources",
                "ApplicationSources",
                TypeInfo(typing.List[ApplicationSource]),
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

    # The names of the scaling plans (up to 10). If you specify application
    # sources, you cannot specify scaling plan names.
    scaling_plan_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the scaling plan. If you specify a scaling plan version, you
    # must also specify a scaling plan name.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sources for the applications (up to 10). If you specify scaling plan
    # names, you cannot specify application sources.
    application_sources: typing.List["ApplicationSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of scalable resources to return. This value can be
    # between 1 and 50. The default value is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingPlansResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scaling_plans",
                "ScalingPlans",
                TypeInfo(typing.List[ScalingPlan]),
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

    # Information about the scaling plans.
    scaling_plans: typing.List["ScalingPlan"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token required to get the next set of results. This value is `null` if
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceException(ShapeBase):
    """
    The service encountered an internal error.
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
class InvalidNextTokenException(ShapeBase):
    """
    The token provided is not valid.
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
class LimitExceededException(ShapeBase):
    """
    Your account exceeded a limit. This exception is thrown when a per-account
    resource limit is exceeded.
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
class MetricDimension(ShapeBase):
    """
    Represents a dimension for a customized metric.
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


class MetricStatistic(str):
    Average = "Average"
    Minimum = "Minimum"
    Maximum = "Maximum"
    SampleCount = "SampleCount"
    Sum = "Sum"


@dataclasses.dataclass
class ObjectNotFoundException(ShapeBase):
    """
    The specified object could not be found.
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


class PolicyType(str):
    TargetTrackingScaling = "TargetTrackingScaling"


@dataclasses.dataclass
class PredefinedScalingMetricSpecification(ShapeBase):
    """
    Represents a predefined metric for a target tracking policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "predefined_scaling_metric_type",
                "PredefinedScalingMetricType",
                TypeInfo(typing.Union[str, ScalingMetricType]),
            ),
            (
                "resource_label",
                "ResourceLabel",
                TypeInfo(str),
            ),
        ]

    # The metric type. The `ALBRequestCountPerTarget` metric type applies only to
    # Auto Scaling groups, Sport Fleet requests, and ECS services.
    predefined_scaling_metric_type: typing.Union[str, "ScalingMetricType"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    # Identifies the resource associated with the metric type. You can't specify
    # a resource label unless the metric type is `ALBRequestCountPerTarget` and
    # there is a target group for an Application Load Balancer attached to the
    # Auto Scaling group, Spot Fleet request, or ECS service.

    # The format is app/<load-balancer-name>/<load-balancer-
    # id>/targetgroup/<target-group-name>/<target-group-id>, where:

    #   * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN

    #   * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.
    resource_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScalableDimension(str):
    autoscaling_autoScalingGroup_DesiredCapacity = "autoscaling:autoScalingGroup:DesiredCapacity"
    ecs_service_DesiredCount = "ecs:service:DesiredCount"
    ec2_spot_fleet_request_TargetCapacity = "ec2:spot-fleet-request:TargetCapacity"
    rds_cluster_ReadReplicaCount = "rds:cluster:ReadReplicaCount"
    dynamodb_table_ReadCapacityUnits = "dynamodb:table:ReadCapacityUnits"
    dynamodb_table_WriteCapacityUnits = "dynamodb:table:WriteCapacityUnits"
    dynamodb_index_ReadCapacityUnits = "dynamodb:index:ReadCapacityUnits"
    dynamodb_index_WriteCapacityUnits = "dynamodb:index:WriteCapacityUnits"


@dataclasses.dataclass
class ScalingInstruction(ShapeBase):
    """
    Specifies the scaling configuration for a scalable resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "scalable_dimension",
                "ScalableDimension",
                TypeInfo(typing.Union[str, ScalableDimension]),
            ),
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
            (
                "target_tracking_configurations",
                "TargetTrackingConfigurations",
                TypeInfo(typing.List[TargetTrackingConfiguration]),
            ),
        ]

    # The namespace of the AWS service.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The ID of the resource. This string consists of the resource type and
    # unique identifier.

    #   * Auto Scaling group - The resource type is `autoScalingGroup` and the unique identifier is the name of the Auto Scaling group. Example: `autoScalingGroup/my-asg`.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension associated with the resource.

    #   * `autoscaling:autoScalingGroup:DesiredCapacity` \- The desired capacity of an Auto Scaling group.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The minimum value to scale to in response to a scale in event.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value to scale to in response to a scale out event.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target tracking scaling policies (up to 10).
    target_tracking_configurations: typing.List["TargetTrackingConfiguration"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )


class ScalingMetricType(str):
    ASGAverageCPUUtilization = "ASGAverageCPUUtilization"
    ASGAverageNetworkIn = "ASGAverageNetworkIn"
    ASGAverageNetworkOut = "ASGAverageNetworkOut"
    DynamoDBReadCapacityUtilization = "DynamoDBReadCapacityUtilization"
    DynamoDBWriteCapacityUtilization = "DynamoDBWriteCapacityUtilization"
    ECSServiceAverageCPUUtilization = "ECSServiceAverageCPUUtilization"
    ECSServiceAverageMemoryUtilization = "ECSServiceAverageMemoryUtilization"
    ALBRequestCountPerTarget = "ALBRequestCountPerTarget"
    RDSReaderAverageCPUUtilization = "RDSReaderAverageCPUUtilization"
    RDSReaderAverageDatabaseConnections = "RDSReaderAverageDatabaseConnections"
    EC2SpotFleetRequestAverageCPUUtilization = "EC2SpotFleetRequestAverageCPUUtilization"
    EC2SpotFleetRequestAverageNetworkIn = "EC2SpotFleetRequestAverageNetworkIn"
    EC2SpotFleetRequestAverageNetworkOut = "EC2SpotFleetRequestAverageNetworkOut"


@dataclasses.dataclass
class ScalingPlan(ShapeBase):
    """
    Represents a scaling plan.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_name",
                "ScalingPlanName",
                TypeInfo(str),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
            ),
            (
                "application_source",
                "ApplicationSource",
                TypeInfo(ApplicationSource),
            ),
            (
                "scaling_instructions",
                "ScalingInstructions",
                TypeInfo(typing.List[ScalingInstruction]),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(typing.Union[str, ScalingPlanStatusCode]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "status_start_time",
                "StatusStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the scaling plan.
    scaling_plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the scaling plan.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The application source.
    application_source: "ApplicationSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scaling instructions.
    scaling_instructions: typing.List["ScalingInstruction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the scaling plan.

    #   * `Active` \- The scaling plan is active.

    #   * `ActiveWithProblems` \- The scaling plan is active, but the scaling configuration for one or more resources could not be applied.

    #   * `CreationInProgress` \- The scaling plan is being created.

    #   * `CreationFailed` \- The scaling plan could not be created.

    #   * `DeletionInProgress` \- The scaling plan is being deleted.

    #   * `DeletionFailed` \- The scaling plan could not be deleted.
    status_code: typing.Union[str, "ScalingPlanStatusCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A simple message about the current status of the scaling plan.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix timestamp when the scaling plan entered the current status.
    status_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix timestamp when the scaling plan was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScalingPlanResource(ShapeBase):
    """
    Represents a scalable resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_name",
                "ScalingPlanName",
                TypeInfo(str),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
            ),
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "scalable_dimension",
                "ScalableDimension",
                TypeInfo(typing.Union[str, ScalableDimension]),
            ),
            (
                "scaling_status_code",
                "ScalingStatusCode",
                TypeInfo(typing.Union[str, ScalingStatusCode]),
            ),
            (
                "scaling_policies",
                "ScalingPolicies",
                TypeInfo(typing.List[ScalingPolicy]),
            ),
            (
                "scaling_status_message",
                "ScalingStatusMessage",
                TypeInfo(str),
            ),
        ]

    # The name of the scaling plan.
    scaling_plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the scaling plan.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the AWS service.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The ID of the resource. This string consists of the resource type and
    # unique identifier.

    #   * Auto Scaling group - The resource type is `autoScalingGroup` and the unique identifier is the name of the Auto Scaling group. Example: `autoScalingGroup/my-asg`.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension for the resource.

    #   * `autoscaling:autoScalingGroup:DesiredCapacity` \- The desired capacity of an Auto Scaling group.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The scaling status of the resource.

    #   * `Active` \- The scaling configuration is active.

    #   * `Inactive` \- The scaling configuration is not active because the scaling plan is being created or the scaling configuration could not be applied. Check the status message for more information.

    #   * `PartiallyActive` \- The scaling configuration is partially active because the scaling plan is being created or deleted or the scaling configuration could not be fully applied. Check the status message for more information.
    scaling_status_code: typing.Union[str, "ScalingStatusCode"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The scaling policies.
    scaling_policies: typing.List["ScalingPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A simple message about the current scaling status of the resource.
    scaling_status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScalingPlanStatusCode(str):
    Active = "Active"
    ActiveWithProblems = "ActiveWithProblems"
    CreationInProgress = "CreationInProgress"
    CreationFailed = "CreationFailed"
    DeletionInProgress = "DeletionInProgress"
    DeletionFailed = "DeletionFailed"
    UpdateInProgress = "UpdateInProgress"
    UpdateFailed = "UpdateFailed"


@dataclasses.dataclass
class ScalingPolicy(ShapeBase):
    """
    Represents a scaling policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "target_tracking_configuration",
                "TargetTrackingConfiguration",
                TypeInfo(TargetTrackingConfiguration),
            ),
        ]

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of scaling policy.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target tracking scaling policy.
    target_tracking_configuration: "TargetTrackingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ScalingStatusCode(str):
    Inactive = "Inactive"
    PartiallyActive = "PartiallyActive"
    Active = "Active"


class ServiceNamespace(str):
    autoscaling = "autoscaling"
    ecs = "ecs"
    ec2 = "ec2"
    rds = "rds"
    dynamodb = "dynamodb"


@dataclasses.dataclass
class TagFilter(ShapeBase):
    """
    Represents a tag.
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

    # The tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag values (0 to 20).
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetTrackingConfiguration(ShapeBase):
    """
    Represents a target tracking scaling policy.
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
                "predefined_scaling_metric_specification",
                "PredefinedScalingMetricSpecification",
                TypeInfo(PredefinedScalingMetricSpecification),
            ),
            (
                "customized_scaling_metric_specification",
                "CustomizedScalingMetricSpecification",
                TypeInfo(CustomizedScalingMetricSpecification),
            ),
            (
                "disable_scale_in",
                "DisableScaleIn",
                TypeInfo(bool),
            ),
            (
                "scale_out_cooldown",
                "ScaleOutCooldown",
                TypeInfo(int),
            ),
            (
                "scale_in_cooldown",
                "ScaleInCooldown",
                TypeInfo(int),
            ),
            (
                "estimated_instance_warmup",
                "EstimatedInstanceWarmup",
                TypeInfo(int),
            ),
        ]

    # The target value for the metric. The range is 8.515920e-109 to
    # 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
    target_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A predefined metric.
    predefined_scaling_metric_specification: "PredefinedScalingMetricSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A customized metric.
    customized_scaling_metric_specification: "CustomizedScalingMetricSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether scale in by the target tracking policy is disabled. If
    # the value is `true`, scale in is disabled and the target tracking policy
    # won't remove capacity from the scalable resource. Otherwise, scale in is
    # enabled and the target tracking policy can remove capacity from the
    # scalable resource. The default value is `false`.
    disable_scale_in: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale out activity completes before
    # another scale out activity can start. This value is not used if the
    # scalable resource is an Auto Scaling group.

    # While the cooldown period is in effect, the capacity that has been added by
    # the previous scale out event that initiated the cooldown is calculated as
    # part of the desired capacity for the next scale out. The intention is to
    # continuously (but not excessively) scale out.
    scale_out_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale in activity completes before
    # another scale in activity can start. This value is not used if the scalable
    # resource is an Auto Scaling group.

    # The cooldown period is used to block subsequent scale in requests until it
    # has expired. The intention is to scale in conservatively to protect your
    # application's availability. However, if another alarm triggers a scale out
    # policy during the cooldown period after a scale-in, AWS Auto Scaling scales
    # out your scalable target immediately.
    scale_in_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The estimated time, in seconds, until a newly launched instance can
    # contribute to the CloudWatch metrics. This value is used only if the
    # resource is an Auto Scaling group.
    estimated_instance_warmup: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateScalingPlanRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scaling_plan_name",
                "ScalingPlanName",
                TypeInfo(str),
            ),
            (
                "scaling_plan_version",
                "ScalingPlanVersion",
                TypeInfo(int),
            ),
            (
                "application_source",
                "ApplicationSource",
                TypeInfo(ApplicationSource),
            ),
            (
                "scaling_instructions",
                "ScalingInstructions",
                TypeInfo(typing.List[ScalingInstruction]),
            ),
        ]

    # The name of the scaling plan.
    scaling_plan_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number.
    scaling_plan_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A CloudFormation stack or set of tags.
    application_source: "ApplicationSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scaling instructions.
    scaling_instructions: typing.List["ScalingInstruction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateScalingPlanResponse(OutputShapeBase):
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
class ValidationException(ShapeBase):
    """
    An exception was thrown for a validation issue. Review the parameters provided.
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
