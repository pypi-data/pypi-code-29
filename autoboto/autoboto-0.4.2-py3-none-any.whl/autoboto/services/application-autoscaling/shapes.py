import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AdjustmentType(str):
    ChangeInCapacity = "ChangeInCapacity"
    PercentChangeInCapacity = "PercentChangeInCapacity"
    ExactCapacity = "ExactCapacity"


@dataclasses.dataclass
class Alarm(ShapeBase):
    """
    Represents a CloudWatch alarm associated with a scaling policy.
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
class ConcurrentUpdateException(ShapeBase):
    """
    Concurrent updates caused an exception, for example, if you request an update to
    an Application Auto Scaling resource that already has a pending update.
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
class DeleteScalingPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
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
        ]

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scalable target. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class DeleteScalingPolicyResponse(OutputShapeBase):
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
class DeleteScheduledActionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "scheduled_action_name",
                "ScheduledActionName",
                TypeInfo(str),
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
        ]

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The name of the scheduled action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource associated with the scheduled action. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class DeleteScheduledActionResponse(OutputShapeBase):
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
class DeregisterScalableTargetRequest(ShapeBase):
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
        ]

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scalable target. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension associated with the scalable target. This string
    # consists of the service namespace, resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class DeregisterScalableTargetResponse(OutputShapeBase):
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
class DescribeScalableTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "resource_ids",
                "ResourceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "scalable_dimension",
                "ScalableDimension",
                TypeInfo(typing.Union[str, ScalableDimension]),
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

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scalable target. This
    # string consists of the resource type and unique identifier. If you specify
    # a scalable dimension, you must also specify a resource ID.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scalable dimension associated with the scalable target. This string
    # consists of the service namespace, resource type, and scaling property. If
    # you specify a scalable dimension, you must also specify a resource ID.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The maximum number of scalable targets. This value can be between 1 and 50.
    # The default value is 50.

    # If this parameter is used, the operation returns up to `MaxResults` results
    # at a time, along with a `NextToken` value. To get the next set of results,
    # include the `NextToken` value in a subsequent call. If this parameter is
    # not used, the operation returns up to 50 results and a `NextToken` value,
    # if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalableTargetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scalable_targets",
                "ScalableTargets",
                TypeInfo(typing.List[ScalableTarget]),
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

    # The scalable targets that match the request parameters.
    scalable_targets: typing.List["ScalableTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token required to get the next set of results. This value is `null` if
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeScalableTargetsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeScalingActivitiesRequest(ShapeBase):
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

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scaling activity. This
    # string consists of the resource type and unique identifier. If you specify
    # a scalable dimension, you must also specify a resource ID.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property. If you specify a scalable dimension,
    # you must also specify a resource ID.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The maximum number of scalable targets. This value can be between 1 and 50.
    # The default value is 50.

    # If this parameter is used, the operation returns up to `MaxResults` results
    # at a time, along with a `NextToken` value. To get the next set of results,
    # include the `NextToken` value in a subsequent call. If this parameter is
    # not used, the operation returns up to 50 results and a `NextToken` value,
    # if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingActivitiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scaling_activities",
                "ScalingActivities",
                TypeInfo(typing.List[ScalingActivity]),
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

    # A list of scaling activity objects.
    scaling_activities: typing.List["ScalingActivity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token required to get the next set of results. This value is `null` if
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeScalingActivitiesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeScalingPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
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

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The names of the scaling policies to describe.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the resource associated with the scaling policy. This
    # string consists of the resource type and unique identifier. If you specify
    # a scalable dimension, you must also specify a resource ID.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property. If you specify a scalable dimension,
    # you must also specify a resource ID.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The maximum number of scalable targets. This value can be between 1 and 50.
    # The default value is 50.

    # If this parameter is used, the operation returns up to `MaxResults` results
    # at a time, along with a `NextToken` value. To get the next set of results,
    # include the `NextToken` value in a subsequent call. If this parameter is
    # not used, the operation returns up to 50 results and a `NextToken` value,
    # if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScalingPoliciesResponse(OutputShapeBase):
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

    # Information about the scaling policies.
    scaling_policies: typing.List["ScalingPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token required to get the next set of results. This value is `null` if
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeScalingPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeScheduledActionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "scheduled_action_names",
                "ScheduledActionNames",
                TypeInfo(typing.List[str]),
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

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The names of the scheduled actions to describe.
    scheduled_action_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the resource associated with the scheduled action. This
    # string consists of the resource type and unique identifier. If you specify
    # a scalable dimension, you must also specify a resource ID.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property. If you specify a scalable dimension,
    # you must also specify a resource ID.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The maximum number of scheduled action results. This value can be between 1
    # and 50. The default value is 50.

    # If this parameter is used, the operation returns up to `MaxResults` results
    # at a time, along with a `NextToken` value. To get the next set of results,
    # include the `NextToken` value in a subsequent call. If this parameter is
    # not used, the operation returns up to 50 results and a `NextToken` value,
    # if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScheduledActionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "scheduled_actions",
                "ScheduledActions",
                TypeInfo(typing.List[ScheduledAction]),
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

    # Information about the scheduled actions.
    scheduled_actions: typing.List["ScheduledAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token required to get the next set of results. This value is `null` if
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FailedResourceAccessException(ShapeBase):
    """
    Failed access to resources caused an exception. This exception is thrown when
    Application Auto Scaling is unable to retrieve the alarms associated with a
    scaling policy due to a client error, for example, if the role ARN specified for
    a scalable target does not have permission to call the CloudWatch
    [DescribeAlarms](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html)
    on your behalf.
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
    The next token supplied was invalid.
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
    A per-account resource limit is exceeded. For more information, see [Application
    Auto Scaling
    Limits](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/userguide/application-
    auto-scaling-limits.html).
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


class MetricAggregationType(str):
    Average = "Average"
    Minimum = "Minimum"
    Maximum = "Maximum"


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


class MetricStatistic(str):
    Average = "Average"
    Minimum = "Minimum"
    Maximum = "Maximum"
    SampleCount = "SampleCount"
    Sum = "Sum"


class MetricType(str):
    DynamoDBReadCapacityUtilization = "DynamoDBReadCapacityUtilization"
    DynamoDBWriteCapacityUtilization = "DynamoDBWriteCapacityUtilization"
    ALBRequestCountPerTarget = "ALBRequestCountPerTarget"
    RDSReaderAverageCPUUtilization = "RDSReaderAverageCPUUtilization"
    RDSReaderAverageDatabaseConnections = "RDSReaderAverageDatabaseConnections"
    EC2SpotFleetRequestAverageCPUUtilization = "EC2SpotFleetRequestAverageCPUUtilization"
    EC2SpotFleetRequestAverageNetworkIn = "EC2SpotFleetRequestAverageNetworkIn"
    EC2SpotFleetRequestAverageNetworkOut = "EC2SpotFleetRequestAverageNetworkOut"
    SageMakerVariantInvocationsPerInstance = "SageMakerVariantInvocationsPerInstance"
    ECSServiceAverageCPUUtilization = "ECSServiceAverageCPUUtilization"
    ECSServiceAverageMemoryUtilization = "ECSServiceAverageMemoryUtilization"


@dataclasses.dataclass
class ObjectNotFoundException(ShapeBase):
    """
    The specified object could not be found. For any operation that depends on the
    existence of a scalable target, this exception is thrown if the scalable target
    with the specified service namespace, resource ID, and scalable dimension does
    not exist. For any operation that deletes or deregisters a resource, this
    exception is thrown if the resource cannot be found.
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
    StepScaling = "StepScaling"
    TargetTrackingScaling = "TargetTrackingScaling"


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

    # The metric type. The `ALBRequestCountPerTarget` metric type applies only to
    # Spot fleet requests and ECS services.
    predefined_metric_type: typing.Union[str, "MetricType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the resource associated with the metric type. You can't specify
    # a resource label unless the metric type is `ALBRequestCountPerTarget` and
    # there is a target group attached to the Spot fleet request or ECS service.

    # The format is app/<load-balancer-name>/<load-balancer-
    # id>/targetgroup/<target-group-name>/<target-group-id>, where:

    #   * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN

    #   * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.
    resource_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutScalingPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
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
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "step_scaling_policy_configuration",
                "StepScalingPolicyConfiguration",
                TypeInfo(StepScalingPolicyConfiguration),
            ),
            (
                "target_tracking_scaling_policy_configuration",
                "TargetTrackingScalingPolicyConfiguration",
                TypeInfo(TargetTrackingScalingPolicyConfiguration),
            ),
        ]

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scaling policy. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The policy type. This parameter is required if you are creating a policy.

    # For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS,
    # Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling`
    # are supported. For any other service, only `StepScaling` is supported.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A step scaling policy.

    # This parameter is required if you are creating a policy and the policy type
    # is `StepScaling`.
    step_scaling_policy_configuration: "StepScalingPolicyConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A target tracking policy.

    # This parameter is required if you are creating a policy and the policy type
    # is `TargetTrackingScaling`.
    target_tracking_scaling_policy_configuration: "TargetTrackingScalingPolicyConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutScalingPolicyResponse(OutputShapeBase):
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

    # The Amazon Resource Name (ARN) of the resulting scaling policy.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CloudWatch alarms created for the target tracking policy.
    alarms: typing.List["Alarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutScheduledActionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "scheduled_action_name",
                "ScheduledActionName",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "scalable_dimension",
                "ScalableDimension",
                TypeInfo(typing.Union[str, ScalableDimension]),
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
                "scalable_target_action",
                "ScalableTargetAction",
                TypeInfo(ScalableTargetAction),
            ),
        ]

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The name of the scheduled action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource associated with the scheduled action. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schedule for this action. The following formats are supported:

    #   * At expressions - `at( _yyyy_ - _mm_ - _dd_ T _hh_ : _mm_ : _ss_ )`

    #   * Rate expressions - `rate( _value_ _unit_ )`

    #   * Cron expressions - `cron( _fields_ )`

    # At expressions are useful for one-time schedules. Specify the time, in UTC.

    # For rate expressions, _value_ is a positive integer and _unit_ is `minute`
    # | `minutes` | `hour` | `hours` | `day` | `days`.

    # For more information about cron expressions, see [Cron
    # Expressions](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions)
    # in the _Amazon CloudWatch Events User Guide_.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This parameter is required if you are creating a
    # scheduled action. This string consists of the service namespace, resource
    # type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The date and time for the scheduled action to start.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time for the scheduled action to end.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new minimum and maximum capacity. You can set both values or just one.
    # During the scheduled time, if the current capacity is below the minimum
    # capacity, Application Auto Scaling scales out to the minimum capacity. If
    # the current capacity is above the maximum capacity, Application Auto
    # Scaling scales in to the maximum capacity.
    scalable_target_action: "ScalableTargetAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutScheduledActionResponse(OutputShapeBase):
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
class RegisterScalableTargetRequest(ShapeBase):
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scalable target. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension associated with the scalable target. This string
    # consists of the service namespace, resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The minimum value to scale to in response to a scale in event. This
    # parameter is required if you are registering a scalable target.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value to scale to in response to a scale out event. This
    # parameter is required if you are registering a scalable target.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Application Auto Scaling creates a service-linked role that grants it
    # permissions to modify the scalable target on your behalf. For more
    # information, see [Service-Linked Roles for Application Auto
    # Scaling](http://docs.aws.amazon.com/autoscaling/application/userguide/application-
    # autoscaling-service-linked-roles.html).

    # For resources that are not supported using a service-linked role, this
    # parameter is required and must specify the ARN of an IAM role that allows
    # Application Auto Scaling to modify the scalable target on your behalf.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterScalableTargetResponse(OutputShapeBase):
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


class ScalableDimension(str):
    ecs_service_DesiredCount = "ecs:service:DesiredCount"
    ec2_spot_fleet_request_TargetCapacity = "ec2:spot-fleet-request:TargetCapacity"
    elasticmapreduce_instancegroup_InstanceCount = "elasticmapreduce:instancegroup:InstanceCount"
    appstream_fleet_DesiredCapacity = "appstream:fleet:DesiredCapacity"
    dynamodb_table_ReadCapacityUnits = "dynamodb:table:ReadCapacityUnits"
    dynamodb_table_WriteCapacityUnits = "dynamodb:table:WriteCapacityUnits"
    dynamodb_index_ReadCapacityUnits = "dynamodb:index:ReadCapacityUnits"
    dynamodb_index_WriteCapacityUnits = "dynamodb:index:WriteCapacityUnits"
    rds_cluster_ReadReplicaCount = "rds:cluster:ReadReplicaCount"
    sagemaker_variant_DesiredInstanceCount = "sagemaker:variant:DesiredInstanceCount"
    custom_resource_ResourceType_Property = "custom-resource:ResourceType:Property"


@dataclasses.dataclass
class ScalableTarget(ShapeBase):
    """
    Represents a scalable target.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scalable target. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension associated with the scalable target. This string
    # consists of the service namespace, resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The minimum value to scale to in response to a scale in event.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value to scale to in response to a scale out event.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM role that allows Application Auto Scaling to modify the
    # scalable target on your behalf.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix timestamp for when the scalable target was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScalableTargetAction(ShapeBase):
    """
    Represents the minimum and maximum capacity for a scheduled action.
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

    # The minimum capacity.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum capacity.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScalingActivity(ShapeBase):
    """
    Represents a scaling activity.
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
                "description",
                "Description",
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
                "details",
                "Details",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the scaling activity.
    activity_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scaling activity. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # A simple description of what action the scaling activity intends to
    # accomplish.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A simple description of what caused the scaling activity to happen.
    cause: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix timestamp for when the scaling activity began.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the status of the scaling activity.
    status_code: typing.Union[str, "ScalingActivityStatusCode"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The Unix timestamp for when the scaling activity ended.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A simple message about the current status of the scaling activity.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The details about the scaling activity.
    details: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ScalingActivityStatusCode(str):
    Pending = "Pending"
    InProgress = "InProgress"
    Successful = "Successful"
    Overridden = "Overridden"
    Unfulfilled = "Unfulfilled"
    Failed = "Failed"


@dataclasses.dataclass
class ScalingPolicy(ShapeBase):
    """
    Represents a scaling policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_arn",
                "PolicyARN",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
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
                "policy_type",
                "PolicyType",
                TypeInfo(typing.Union[str, PolicyType]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "step_scaling_policy_configuration",
                "StepScalingPolicyConfiguration",
                TypeInfo(StepScalingPolicyConfiguration),
            ),
            (
                "target_tracking_scaling_policy_configuration",
                "TargetTrackingScalingPolicyConfiguration",
                TypeInfo(TargetTrackingScalingPolicyConfiguration),
            ),
            (
                "alarms",
                "Alarms",
                TypeInfo(typing.List[Alarm]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the scaling policy.
    policy_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The identifier of the resource associated with the scaling policy. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The scaling policy type.
    policy_type: typing.Union[str, "PolicyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix timestamp for when the scaling policy was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A step scaling policy.
    step_scaling_policy_configuration: "StepScalingPolicyConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A target tracking policy.
    target_tracking_scaling_policy_configuration: "TargetTrackingScalingPolicyConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatch alarms associated with the scaling policy.
    alarms: typing.List["Alarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduledAction(ShapeBase):
    """
    Represents a scheduled action.
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
                "scheduled_action_arn",
                "ScheduledActionARN",
                TypeInfo(str),
            ),
            (
                "service_namespace",
                "ServiceNamespace",
                TypeInfo(typing.Union[str, ServiceNamespace]),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "scalable_dimension",
                "ScalableDimension",
                TypeInfo(typing.Union[str, ScalableDimension]),
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
                "scalable_target_action",
                "ScalableTargetAction",
                TypeInfo(ScalableTargetAction),
            ),
        ]

    # The name of the scheduled action.
    scheduled_action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the scheduled action.
    scheduled_action_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the AWS service that provides the resource or `custom-
    # resource` for a resource provided by your own application or service. For
    # more information, see [AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html#genref-aws-service-namespaces) in the _Amazon Web Services
    # General Reference_.
    service_namespace: typing.Union[str, "ServiceNamespace"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The schedule for this action. The following formats are supported:

    #   * At expressions - `at( _yyyy_ - _mm_ - _dd_ T _hh_ : _mm_ : _ss_ )`

    #   * Rate expressions - `rate( _value_ _unit_ )`

    #   * Cron expressions - `cron( _fields_ )`

    # At expressions are useful for one-time schedules. Specify the time, in UTC.

    # For rate expressions, _value_ is a positive integer and _unit_ is `minute`
    # | `minutes` | `hour` | `hours` | `day` | `days`.

    # For more information about cron expressions, see [Cron
    # Expressions](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions)
    # in the _Amazon CloudWatch Events User Guide_.
    schedule: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the resource associated with the scaling policy. This
    # string consists of the resource type and unique identifier.

    #   * ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.

    #   * Spot fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.

    #   * EMR cluster - The resource type is `instancegroup` and the unique identifier is the cluster ID and instance group ID. Example: `instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`.

    #   * AppStream 2.0 fleet - The resource type is `fleet` and the unique identifier is the fleet name. Example: `fleet/sample-fleet`.

    #   * DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.

    #   * DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.

    #   * Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.

    #   * Amazon SageMaker endpoint variants - The resource type is `variant` and the unique identifier is the resource ID. Example: `endpoint/my-end-point/variant/KMeansClustering`.

    #   * Custom resources are not supported with a resource type. This parameter must specify the `OutputValue` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the scheduled action was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scalable dimension. This string consists of the service namespace,
    # resource type, and scaling property.

    #   * `ecs:service:DesiredCount` \- The desired task count of an ECS service.

    #   * `ec2:spot-fleet-request:TargetCapacity` \- The target capacity of a Spot fleet request.

    #   * `elasticmapreduce:instancegroup:InstanceCount` \- The instance count of an EMR Instance Group.

    #   * `appstream:fleet:DesiredCapacity` \- The desired capacity of an AppStream 2.0 fleet.

    #   * `dynamodb:table:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB table.

    #   * `dynamodb:table:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB table.

    #   * `dynamodb:index:ReadCapacityUnits` \- The provisioned read capacity for a DynamoDB global secondary index.

    #   * `dynamodb:index:WriteCapacityUnits` \- The provisioned write capacity for a DynamoDB global secondary index.

    #   * `rds:cluster:ReadReplicaCount` \- The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.

    #   * `sagemaker:variant:DesiredInstanceCount` \- The number of EC2 instances for an Amazon SageMaker model endpoint variant.

    #   * `custom-resource:ResourceType:Property` \- The scalable dimension for a custom resource provided by your own application or service.
    scalable_dimension: typing.Union[str, "ScalableDimension"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The date and time that the action is scheduled to begin.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the action is scheduled to end.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new minimum and maximum capacity. You can set both values or just one.
    # During the scheduled time, if the current capacity is below the minimum
    # capacity, Application Auto Scaling scales out to the minimum capacity. If
    # the current capacity is above the maximum capacity, Application Auto
    # Scaling scales in to the maximum capacity.
    scalable_target_action: "ScalableTargetAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ServiceNamespace(str):
    ecs = "ecs"
    elasticmapreduce = "elasticmapreduce"
    ec2 = "ec2"
    appstream = "appstream"
    dynamodb = "dynamodb"
    rds = "rds"
    sagemaker = "sagemaker"
    custom_resource = "custom-resource"


@dataclasses.dataclass
class StepAdjustment(ShapeBase):
    """
    Represents a step adjustment for a StepScalingPolicyConfiguration. Describes an
    adjustment based on the difference between the value of the aggregated
    CloudWatch metric and the breach threshold that you've defined for the alarm.

    For the following examples, suppose that you have an alarm with a breach
    threshold of 50:

      * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.

      * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

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
    # positive value adds to the current scalable dimension while a negative
    # number removes from the current scalable dimension.
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
class StepScalingPolicyConfiguration(ShapeBase):
    """
    Represents a step scaling policy configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adjustment_type",
                "AdjustmentType",
                TypeInfo(typing.Union[str, AdjustmentType]),
            ),
            (
                "step_adjustments",
                "StepAdjustments",
                TypeInfo(typing.List[StepAdjustment]),
            ),
            (
                "min_adjustment_magnitude",
                "MinAdjustmentMagnitude",
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
                TypeInfo(typing.Union[str, MetricAggregationType]),
            ),
        ]

    # The adjustment type, which specifies how the `ScalingAdjustment` parameter
    # in a StepAdjustment is interpreted.
    adjustment_type: typing.Union[str, "AdjustmentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of adjustments that enable you to scale based on the size of the
    # alarm breach.
    step_adjustments: typing.List["StepAdjustment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum number to adjust your scalable dimension as a result of a
    # scaling activity. If the adjustment type is `PercentChangeInCapacity`, the
    # scaling policy changes the scalable dimension of the scalable target by
    # this amount.
    min_adjustment_magnitude: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, after a scaling activity completes where
    # previous trigger-related scaling activities can influence future scaling
    # events.

    # For scale out policies, while the cooldown period is in effect, the
    # capacity that has been added by the previous scale out event that initiated
    # the cooldown is calculated as part of the desired capacity for the next
    # scale out. The intention is to continuously (but not excessively) scale
    # out. For example, an alarm triggers a step scaling policy to scale out an
    # Amazon ECS service by 2 tasks, the scaling activity completes successfully,
    # and a cooldown period of 5 minutes starts. During the Cooldown period, if
    # the alarm triggers the same policy again but at a more aggressive step
    # adjustment to scale out the service by 3 tasks, the 2 tasks that were added
    # in the previous scale out event are considered part of that capacity and
    # only 1 additional task is added to the desired count.

    # For scale in policies, the cooldown period is used to block subsequent
    # scale in requests until it has expired. The intention is to scale in
    # conservatively to protect your application's availability. However, if
    # another alarm triggers a scale out policy during the cooldown period after
    # a scale-in, Application Auto Scaling scales out your scalable target
    # immediately.
    cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The aggregation type for the CloudWatch metrics. Valid values are
    # `Minimum`, `Maximum`, and `Average`.
    metric_aggregation_type: typing.Union[str, "MetricAggregationType"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class TargetTrackingScalingPolicyConfiguration(ShapeBase):
    """
    Represents a target tracking scaling policy configuration.
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
                "disable_scale_in",
                "DisableScaleIn",
                TypeInfo(bool),
            ),
        ]

    # The target value for the metric. The range is 8.515920e-109 to
    # 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
    target_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A predefined metric.
    predefined_metric_specification: "PredefinedMetricSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A customized metric.
    customized_metric_specification: "CustomizedMetricSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in seconds, after a scale out activity completes before
    # another scale out activity can start.

    # While the cooldown period is in effect, the capacity that has been added by
    # the previous scale out event that initiated the cooldown is calculated as
    # part of the desired capacity for the next scale out. The intention is to
    # continuously (but not excessively) scale out.
    scale_out_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale in activity completes before
    # another scale in activity can start.

    # The cooldown period is used to block subsequent scale in requests until it
    # has expired. The intention is to scale in conservatively to protect your
    # application's availability. However, if another alarm triggers a scale out
    # policy during the cooldown period after a scale-in, Application Auto
    # Scaling scales out your scalable target immediately.
    scale_in_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether scale in by the target tracking policy is disabled. If
    # the value is `true`, scale in is disabled and the target tracking policy
    # won't remove capacity from the scalable resource. Otherwise, scale in is
    # enabled and the target tracking policy can remove capacity from the
    # scalable resource. The default value is `false`.
    disable_scale_in: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    An exception was thrown for a validation issue. Review the available parameters
    for the API request.
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
