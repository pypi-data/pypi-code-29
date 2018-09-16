import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class APICallRateForCustomerExceededFault(ShapeBase):
    """
    The customer has exceeded the allowed rate of API calls.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class AZMode(str):
    single_az = "single-az"
    cross_az = "cross-az"


@dataclasses.dataclass
class AddTagsToResourceMessage(ShapeBase):
    """
    Represents the input of an AddTagsToResource operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource to which the tags are to be
    # added, for example `arn:aws:elasticache:us-
    # west-2:0123456789:cluster:myCluster` or `arn:aws:elasticache:us-
    # west-2:0123456789:snapshot:mySnapshot`. ElastiCache resources are _cluster_
    # and _snapshot_.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cost allocation tags to be added to this resource. A tag is a
    # key-value pair. A tag key must be accompanied by a tag value.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllowedNodeTypeModificationsMessage(OutputShapeBase):
    """
    Represents the allowed node types you can use to modify your cluster or
    replication group.
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
                "scale_up_modifications",
                "ScaleUpModifications",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string list, each element of which specifies a cache node type which you
    # can use to scale your cluster or replication group.

    # When scaling up a Redis cluster or replication group using
    # `ModifyCacheCluster` or `ModifyReplicationGroup`, use a value from this
    # list for the `CacheNodeType` parameter.
    scale_up_modifications: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizationAlreadyExistsFault(ShapeBase):
    """
    The specified Amazon EC2 security group is already authorized for the specified
    cache security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizationNotFoundFault(ShapeBase):
    """
    The specified Amazon EC2 security group is not authorized for the specified
    cache security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizeCacheSecurityGroupIngressMessage(ShapeBase):
    """
    Represents the input of an AuthorizeCacheSecurityGroupIngress operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_name",
                "EC2SecurityGroupName",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_owner_id",
                "EC2SecurityGroupOwnerId",
                TypeInfo(str),
            ),
        ]

    # The cache security group that allows network ingress.
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon EC2 security group to be authorized for ingress to the cache
    # security group.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account number of the Amazon EC2 security group owner. Note that
    # this is not the same thing as an AWS access key ID - you must provide a
    # valid AWS account number for this parameter.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeCacheSecurityGroupIngressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_security_group",
                "CacheSecurityGroup",
                TypeInfo(CacheSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of one of the following operations:

    #   * `AuthorizeCacheSecurityGroupIngress`

    #   * `CreateCacheSecurityGroup`

    #   * `RevokeCacheSecurityGroupIngress`
    cache_security_group: "CacheSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AutomaticFailoverStatus(str):
    enabled = "enabled"
    disabled = "disabled"
    enabling = "enabling"
    disabling = "disabling"


@dataclasses.dataclass
class AvailabilityZone(ShapeBase):
    """
    Describes an Availability Zone in which the cluster is launched.
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

    # The name of the Availability Zone.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CacheCluster(ShapeBase):
    """
    Contains all of the attributes of a specific cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "configuration_endpoint",
                "ConfigurationEndpoint",
                TypeInfo(Endpoint),
            ),
            (
                "client_download_landing_page",
                "ClientDownloadLandingPage",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_cluster_status",
                "CacheClusterStatus",
                TypeInfo(str),
            ),
            (
                "num_cache_nodes",
                "NumCacheNodes",
                TypeInfo(int),
            ),
            (
                "preferred_availability_zone",
                "PreferredAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "cache_cluster_create_time",
                "CacheClusterCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "pending_modified_values",
                "PendingModifiedValues",
                TypeInfo(PendingModifiedValues),
            ),
            (
                "notification_configuration",
                "NotificationConfiguration",
                TypeInfo(NotificationConfiguration),
            ),
            (
                "cache_security_groups",
                "CacheSecurityGroups",
                TypeInfo(typing.List[CacheSecurityGroupMembership]),
            ),
            (
                "cache_parameter_group",
                "CacheParameterGroup",
                TypeInfo(CacheParameterGroupStatus),
            ),
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "cache_nodes",
                "CacheNodes",
                TypeInfo(typing.List[CacheNode]),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[SecurityGroupMembership]),
            ),
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "auth_token_enabled",
                "AuthTokenEnabled",
                TypeInfo(bool),
            ),
            (
                "transit_encryption_enabled",
                "TransitEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "at_rest_encryption_enabled",
                "AtRestEncryptionEnabled",
                TypeInfo(bool),
            ),
        ]

    # The user-supplied identifier of the cluster. This identifier is a unique
    # key that identifies a cluster.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents a Memcached cluster endpoint which, if Automatic Discovery is
    # enabled on the cluster, can be used by an application to connect to any
    # node in the cluster. The configuration endpoint will always have `.cfg` in
    # it.

    # Example: `mem-3.9dvc4r _.cfg_.usw2.cache.amazonaws.com:11211`
    configuration_endpoint: "Endpoint" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the web page where you can download the latest ElastiCache
    # client library.
    client_download_landing_page: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the compute and memory capacity node type for the cluster.

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache engine (`memcached` or `redis`) to be used for this
    # cluster.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the cache engine that is used in this cluster.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of this cluster, one of the following values:
    # `available`, `creating`, `deleted`, `deleting`, `incompatible-network`,
    # `modifying`, `rebooting cluster nodes`, `restore-failed`, or
    # `snapshotting`.
    cache_cluster_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of cache nodes in the cluster.

    # For clusters running Redis, this value must be 1. For clusters running
    # Memcached, this value must be between 1 and 20.
    num_cache_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Availability Zone in which the cluster is located or
    # "Multiple" if the cache nodes are located in different Availability Zones.
    preferred_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the cluster was created.
    cache_cluster_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.

    # Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:23:00-mon:01:30`
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A group of settings that are applied to the cluster in the future, or that
    # are currently being applied.
    pending_modified_values: "PendingModifiedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a notification topic and its status. Notification topics are used
    # for publishing ElastiCache events to subscribers using Amazon Simple
    # Notification Service (SNS).
    notification_configuration: "NotificationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cache security group elements, composed of name and status sub-
    # elements.
    cache_security_groups: typing.List["CacheSecurityGroupMembership"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Status of the cache parameter group.
    cache_parameter_group: "CacheParameterGroupStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cache subnet group associated with the cluster.
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cache nodes that are members of the cluster.
    cache_nodes: typing.List["CacheNode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is currently disabled.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of VPC Security Groups associated with the cluster.
    security_groups: typing.List["SecurityGroupMembership"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication group to which this cluster belongs. If this field is
    # empty, the cluster is not associated with any replication group.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days for which ElastiCache retains automatic cluster
    # snapshots before deleting them. For example, if you set
    # `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained
    # for 5 days before being deleted.

    # If the value of SnapshotRetentionLimit is set to zero (0), backups are
    # turned off.
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range (in UTC) during which ElastiCache begins taking a
    # daily snapshot of your cluster.

    # Example: `05:00-09:00`
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that enables using an `AuthToken` (password) when issuing Redis
    # commands.

    # Default: `false`
    auth_token_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that enables in-transit encryption when set to `true`.

    # You cannot modify the value of `TransitEncryptionEnabled` after the cluster
    # is created. To enable in-transit encryption on a cluster you must set
    # `TransitEncryptionEnabled` to `true` when you create a cluster.

    # Default: `false`
    transit_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that enables encryption at-rest when set to `true`.

    # You cannot modify the value of `AtRestEncryptionEnabled` after the cluster
    # is created. To enable at-rest encryption on a cluster you must set
    # `AtRestEncryptionEnabled` to `true` when you create a cluster.

    # Default: `false`
    at_rest_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheClusterAlreadyExistsFault(ShapeBase):
    """
    You already have a cluster with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheClusterMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeCacheClusters` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "cache_clusters",
                "CacheClusters",
                TypeInfo(typing.List[CacheCluster]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of clusters. Each item in the list contains detailed information
    # about one cluster.
    cache_clusters: typing.List["CacheCluster"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["CacheClusterMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CacheClusterNotFoundFault(ShapeBase):
    """
    The requested cluster ID does not refer to an existing cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheEngineVersion(ShapeBase):
    """
    Provides all of the details about a particular cache engine version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_family",
                "CacheParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "cache_engine_description",
                "CacheEngineDescription",
                TypeInfo(str),
            ),
            (
                "cache_engine_version_description",
                "CacheEngineVersionDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the cache engine.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the cache engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache parameter group family associated with this cache
    # engine.

    # Valid values are: `memcached1.4` | `redis2.6` | `redis2.8` | `redis3.2`
    cache_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the cache engine.
    cache_engine_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the cache engine version.
    cache_engine_version_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheEngineVersionMessage(OutputShapeBase):
    """
    Represents the output of a DescribeCacheEngineVersions operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "cache_engine_versions",
                "CacheEngineVersions",
                TypeInfo(typing.List[CacheEngineVersion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache engine version details. Each element in the list contains
    # detailed information about one cache engine version.
    cache_engine_versions: typing.List["CacheEngineVersion"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    def paginate(self,
                ) -> typing.Generator["CacheEngineVersionMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CacheNode(ShapeBase):
    """
    Represents an individual cache node within a cluster. Each cache node runs its
    own instance of the cluster's protocol-compliant caching software - either
    Memcached or Redis.

    The following node types are supported by ElastiCache. Generally speaking, the
    current generation types provide more memory and computational power at lower
    cost when compared to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation: 

    **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    `cache.m3.2xlarge`

    **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    `cache.m4.4xlarge`, `cache.m4.10xlarge`

        * Previous generation: (not recommended)

    **T1 node types:** `cache.t1.micro`

    **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    `cache.m1.xlarge`

      * Compute optimized:

        * Previous generation: (not recommended)

    **C1 node types:** `cache.c1.xlarge`

      * Memory optimized:

        * Current generation: 

    **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    `cache.r3.4xlarge`, `cache.r3.8xlarge`

        * Previous generation: (not recommended)

    **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`, `cache.m2.4xlarge`

    **Notes:**

      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances. 

      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    For a complete listing of node types and specifications, see [Amazon ElastiCache
    Product Features and Details](http://aws.amazon.com/elasticache/details) and
    either [Cache Node Type-Specific Parameters for
    Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    or [Cache Node Type-Specific Parameters for
    Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_node_id",
                "CacheNodeId",
                TypeInfo(str),
            ),
            (
                "cache_node_status",
                "CacheNodeStatus",
                TypeInfo(str),
            ),
            (
                "cache_node_create_time",
                "CacheNodeCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(Endpoint),
            ),
            (
                "parameter_group_status",
                "ParameterGroupStatus",
                TypeInfo(str),
            ),
            (
                "source_cache_node_id",
                "SourceCacheNodeId",
                TypeInfo(str),
            ),
            (
                "customer_availability_zone",
                "CustomerAvailabilityZone",
                TypeInfo(str),
            ),
        ]

    # The cache node identifier. A node ID is a numeric identifier (0001, 0002,
    # etc.). The combination of cluster ID and node ID uniquely identifies every
    # cache node used in a customer's AWS account.
    cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of this cache node.
    cache_node_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the cache node was created.
    cache_node_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The hostname for connecting to this cache node.
    endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the parameter group applied to this cache node.
    parameter_group_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the primary node to which this read replica node is synchronized.
    # If this field is empty, this node is not associated with a primary cluster.
    source_cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone where this node was created and now resides.
    customer_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheNodeTypeSpecificParameter(ShapeBase):
    """
    A parameter that has a different value for each cache node type it is applied
    to. For example, in a Redis cluster, a `cache.m1.large` cache node type would
    have a larger `maxmemory` value than a `cache.m1.small` type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "data_type",
                "DataType",
                TypeInfo(str),
            ),
            (
                "allowed_values",
                "AllowedValues",
                TypeInfo(str),
            ),
            (
                "is_modifiable",
                "IsModifiable",
                TypeInfo(bool),
            ),
            (
                "minimum_engine_version",
                "MinimumEngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_node_type_specific_values",
                "CacheNodeTypeSpecificValues",
                TypeInfo(typing.List[CacheNodeTypeSpecificValue]),
            ),
            (
                "change_type",
                "ChangeType",
                TypeInfo(typing.Union[str, ChangeType]),
            ),
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the parameter value.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid data type for the parameter.
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid range of values for the parameter.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether (`true`) or not (`false`) the parameter can be modified.
    # Some parameters have security or operational implications that prevent them
    # from being changed.
    is_modifiable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The earliest cache engine version to which the parameter can apply.
    minimum_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache node types and their corresponding values for this
    # parameter.
    cache_node_type_specific_values: typing.List["CacheNodeTypeSpecificValue"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    # Indicates whether a change to the parameter is applied immediately or
    # requires a reboot for the change to be applied. You can force a reboot or
    # wait until the next maintenance window's reboot. For more information, see
    # [Rebooting a
    # Cluster](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html).
    change_type: typing.Union[str, "ChangeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheNodeTypeSpecificValue(ShapeBase):
    """
    A value that applies only to a certain cache node type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The cache node type for which this value applies.
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the cache node type.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CacheParameterGroup(ShapeBase):
    """
    Represents the output of a `CreateCacheParameterGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_family",
                "CacheParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name of the cache parameter group.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cache parameter group family that this cache parameter
    # group is compatible with.

    # Valid values are: `memcached1.4` | `redis2.6` | `redis2.8` | `redis3.2`
    cache_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for this cache parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CacheParameterGroupAlreadyExistsFault(ShapeBase):
    """
    A cache parameter group with the requested name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheParameterGroupDetails(OutputShapeBase):
    """
    Represents the output of a `DescribeCacheParameters` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "cache_node_type_specific_parameters",
                "CacheNodeTypeSpecificParameters",
                TypeInfo(typing.List[CacheNodeTypeSpecificParameter]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Parameter instances.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of parameters specific to a particular cache node type. Each element
    # in the list contains detailed information about one parameter.
    cache_node_type_specific_parameters: typing.List[
        "CacheNodeTypeSpecificParameter"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    def paginate(self,
                ) -> typing.Generator["CacheParameterGroupDetails", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CacheParameterGroupNameMessage(OutputShapeBase):
    """
    Represents the output of one of the following operations:

      * `ModifyCacheParameterGroup`

      * `ResetCacheParameterGroup`
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
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cache parameter group.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheParameterGroupNotFoundFault(ShapeBase):
    """
    The requested cache parameter group name does not refer to an existing cache
    parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheParameterGroupQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the maximum number of
    cache security groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheParameterGroupStatus(ShapeBase):
    """
    Status of the cache parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_apply_status",
                "ParameterApplyStatus",
                TypeInfo(str),
            ),
            (
                "cache_node_ids_to_reboot",
                "CacheNodeIdsToReboot",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the cache parameter group.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of parameter updates.
    parameter_apply_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the cache node IDs which need to be rebooted for parameter
    # changes to be applied. A node ID is a numeric identifier (0001, 0002,
    # etc.).
    cache_node_ids_to_reboot: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheParameterGroupsMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeCacheParameterGroups` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "cache_parameter_groups",
                "CacheParameterGroups",
                TypeInfo(typing.List[CacheParameterGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache parameter groups. Each element in the list contains
    # detailed information about one cache parameter group.
    cache_parameter_groups: typing.List["CacheParameterGroup"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    def paginate(
        self,
    ) -> typing.Generator["CacheParameterGroupsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CacheSecurityGroup(ShapeBase):
    """
    Represents the output of one of the following operations:

      * `AuthorizeCacheSecurityGroupIngress`

      * `CreateCacheSecurityGroup`

      * `RevokeCacheSecurityGroupIngress`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner_id",
                "OwnerId",
                TypeInfo(str),
            ),
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "ec2_security_groups",
                "EC2SecurityGroups",
                TypeInfo(typing.List[EC2SecurityGroup]),
            ),
        ]

    # The AWS account ID of the cache security group owner.
    owner_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache security group.
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the cache security group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Amazon EC2 security groups that are associated with this cache
    # security group.
    ec2_security_groups: typing.List["EC2SecurityGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheSecurityGroupAlreadyExistsFault(ShapeBase):
    """
    A cache security group with the specified name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSecurityGroupMembership(ShapeBase):
    """
    Represents a cluster's status within a particular cache security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The name of the cache security group.
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The membership status in the cache security group. The status changes when
    # a cache security group is modified, or when the cache security groups
    # assigned to a cluster are modified.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CacheSecurityGroupMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeCacheSecurityGroups` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "cache_security_groups",
                "CacheSecurityGroups",
                TypeInfo(typing.List[CacheSecurityGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache security groups. Each element in the list contains detailed
    # information about one group.
    cache_security_groups: typing.List["CacheSecurityGroup"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    def paginate(self,
                ) -> typing.Generator["CacheSecurityGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CacheSecurityGroupNotFoundFault(ShapeBase):
    """
    The requested cache security group name does not refer to an existing cache
    security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSecurityGroupQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    cache security groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSubnetGroup(ShapeBase):
    """
    Represents the output of one of the following operations:

      * `CreateCacheSubnetGroup`

      * `ModifyCacheSubnetGroup`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "cache_subnet_group_description",
                "CacheSubnetGroupDescription",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[Subnet]),
            ),
        ]

    # The name of the cache subnet group.
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the cache subnet group.
    cache_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet
    # group.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of subnets associated with the cache subnet group.
    subnets: typing.List["Subnet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheSubnetGroupAlreadyExistsFault(ShapeBase):
    """
    The requested cache subnet group name is already in use by an existing cache
    subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSubnetGroupInUse(ShapeBase):
    """
    The requested cache subnet group is currently in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSubnetGroupMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeCacheSubnetGroups` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "cache_subnet_groups",
                "CacheSubnetGroups",
                TypeInfo(typing.List[CacheSubnetGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache subnet groups. Each element in the list contains detailed
    # information about one group.
    cache_subnet_groups: typing.List["CacheSubnetGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["CacheSubnetGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CacheSubnetGroupNotFoundFault(ShapeBase):
    """
    The requested cache subnet group name does not refer to an existing cache subnet
    group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSubnetGroupQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    cache subnet groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CacheSubnetQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    subnets in a cache subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ChangeType(str):
    immediate = "immediate"
    requires_reboot = "requires-reboot"


@dataclasses.dataclass
class ClusterQuotaForCustomerExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    clusters per customer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CopySnapshotMessage(ShapeBase):
    """
    Represents the input of a `CopySnapshotMessage` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_snapshot_name",
                "SourceSnapshotName",
                TypeInfo(str),
            ),
            (
                "target_snapshot_name",
                "TargetSnapshotName",
                TypeInfo(str),
            ),
            (
                "target_bucket",
                "TargetBucket",
                TypeInfo(str),
            ),
        ]

    # The name of an existing snapshot from which to make a copy.
    source_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A name for the snapshot copy. ElastiCache does not permit overwriting a
    # snapshot, therefore this name must be unique within its context -
    # ElastiCache or an Amazon S3 bucket if exporting.
    target_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 bucket to which the snapshot is exported. This parameter is
    # used only when exporting a snapshot for external access.

    # When using this parameter to export a snapshot, be sure Amazon ElastiCache
    # has the needed permissions to this S3 bucket. For more information, see
    # [Step 2: Grant ElastiCache Access to Your Amazon S3
    # Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess)
    # in the _Amazon ElastiCache User Guide_.

    # For more information, see [Exporting a
    # Snapshot](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html)
    # in the _Amazon ElastiCache User Guide_.
    target_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopySnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "snapshot",
                "Snapshot",
                TypeInfo(Snapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents a copy of an entire Redis cluster as of the time when the
    # snapshot was taken.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCacheClusterMessage(ShapeBase):
    """
    Represents the input of a CreateCacheCluster operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "az_mode",
                "AZMode",
                TypeInfo(typing.Union[str, AZMode]),
            ),
            (
                "preferred_availability_zone",
                "PreferredAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "preferred_availability_zones",
                "PreferredAvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "num_cache_nodes",
                "NumCacheNodes",
                TypeInfo(int),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "cache_security_group_names",
                "CacheSecurityGroupNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "snapshot_arns",
                "SnapshotArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "snapshot_name",
                "SnapshotName",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "notification_topic_arn",
                "NotificationTopicArn",
                TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "auth_token",
                "AuthToken",
                TypeInfo(str),
            ),
        ]

    # The node group (shard) identifier. This parameter is stored as a lowercase
    # string.

    # **Constraints:**

    #   * A name must contain from 1 to 20 alphanumeric characters or hyphens.

    #   * The first character must be a letter.

    #   * A name cannot end with a hyphen or contain two consecutive hyphens.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Due to current limitations on Redis (cluster mode disabled), this operation
    # or parameter is not supported on Redis (cluster mode enabled) replication
    # groups.

    # The ID of the replication group to which this cluster should belong. If
    # this parameter is specified, the cluster is added to the specified
    # replication group as a read replica; otherwise, the cluster is a standalone
    # primary that is not part of any replication group.

    # If the specified replication group is Multi-AZ enabled and the Availability
    # Zone is not specified, the cluster is created in Availability Zones that
    # provide the best spread of read replicas across Availability Zones.

    # This parameter is only valid if the `Engine` parameter is `redis`.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the nodes in this Memcached cluster are created in a
    # single Availability Zone or created across multiple Availability Zones in
    # the cluster's region.

    # This parameter is only supported for Memcached clusters.

    # If the `AZMode` and `PreferredAvailabilityZones` are not specified,
    # ElastiCache assumes `single-az` mode.
    az_mode: typing.Union[str, "AZMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 Availability Zone in which the cluster is created.

    # All nodes belonging to this Memcached cluster are placed in the preferred
    # Availability Zone. If you want to create your nodes across multiple
    # Availability Zones, use `PreferredAvailabilityZones`.

    # Default: System chosen Availability Zone.
    preferred_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the Availability Zones in which cache nodes are created. The
    # order of the zones in the list is not important.

    # This option is only supported on Memcached.

    # If you are creating your cluster in an Amazon VPC (recommended) you can
    # only locate nodes in Availability Zones that are associated with the
    # subnets in the selected subnet group.

    # The number of Availability Zones listed must equal the value of
    # `NumCacheNodes`.

    # If you want all the nodes in the same Availability Zone, use
    # `PreferredAvailabilityZone` instead, or repeat the Availability Zone
    # multiple times in the list.

    # Default: System chosen Availability Zones.
    preferred_availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The initial number of cache nodes that the cluster has.

    # For clusters running Redis, this value must be 1. For clusters running
    # Memcached, this value must be between 1 and 20.

    # If you need more than 20 nodes for your Memcached cluster, please fill out
    # the ElastiCache Limit Increase Request form at
    # <http://aws.amazon.com/contact-us/elasticache-node-limit-request/>.
    num_cache_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute and memory capacity of the nodes in the node group (shard).

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache engine to be used for this cluster.

    # Valid values for this parameter are: `memcached` | `redis`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the cache engine to be used for this cluster. To view
    # the supported cache engine versions, use the DescribeCacheEngineVersions
    # operation.

    # **Important:** You can upgrade to a newer engine version (see [Selecting a
    # Cache Engine and
    # Version](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement)),
    # but you cannot downgrade to an earlier engine version. If you want to use
    # an earlier engine version, you must delete the existing cluster or
    # replication group and create it anew with the earlier engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the parameter group to associate with this cluster. If this
    # argument is omitted, the default parameter group for the specified engine
    # is used. You cannot use any parameter group which has `cluster-
    # enabled='yes'` when creating a cluster.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the subnet group to be used for the cluster.

    # Use this parameter only when you are creating a cluster in an Amazon
    # Virtual Private Cloud (Amazon VPC).

    # If you're going to launch your cluster in an Amazon VPC, you need to create
    # a subnet group before you start creating a cluster. For more information,
    # see [Subnets and Subnet
    # Groups](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SubnetGroups.html).
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security group names to associate with this cluster.

    # Use this parameter only when you are creating a cluster outside of an
    # Amazon Virtual Private Cloud (Amazon VPC).
    cache_security_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more VPC security groups associated with the cluster.

    # Use this parameter only when you are creating a cluster in an Amazon
    # Virtual Private Cloud (Amazon VPC).
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cost allocation tags to be added to this resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A single-element string list containing an Amazon Resource Name (ARN) that
    # uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The
    # snapshot file is used to populate the node group (shard). The Amazon S3
    # object name in the ARN cannot contain any commas.

    # This parameter is only valid if the `Engine` parameter is `redis`.

    # Example of an Amazon S3 ARN: `arn:aws:s3:::my_bucket/snapshot1.rdb`
    snapshot_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a Redis snapshot from which to restore data into the new node
    # group (shard). The snapshot status changes to `restoring` while the new
    # node group (shard) is being created.

    # This parameter is only valid if the `Engine` parameter is `redis`.
    snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.
    # Valid values for `ddd` are:

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.

    # Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:23:00-mon:01:30`
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which each of the cache nodes accepts connections.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
    # (SNS) topic to which notifications are sent.

    # The Amazon SNS topic owner must be the same as the cluster owner.
    notification_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is currently disabled.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which ElastiCache retains automatic snapshots before
    # deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a
    # snapshot taken today is retained for 5 days before being deleted.

    # This parameter is only valid if the `Engine` parameter is `redis`.

    # Default: 0 (i.e., automatic backups are disabled for this cluster).
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range (in UTC) during which ElastiCache begins taking a
    # daily snapshot of your node group (shard).

    # Example: `05:00-09:00`

    # If you do not specify this parameter, ElastiCache automatically chooses an
    # appropriate time range.

    # This parameter is only valid if the `Engine` parameter is `redis`.
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # **Reserved parameter.** The password used to access a password protected
    # server.

    # This parameter is valid only if:

    #   * The parameter `TransitEncryptionEnabled` was set to `true` when the cluster was created.

    #   * The line `requirepass` was added to the database configuration file.

    # Password constraints:

    #   * Must be only printable ASCII characters.

    #   * Must be at least 16 characters and no more than 128 characters in length.

    #   * Cannot contain any of the following characters: '/', '"', or '@'.

    # For more information, see [AUTH password](http://redis.io/commands/AUTH) at
    # http://redis.io/commands/AUTH.
    auth_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCacheClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_cluster",
                "CacheCluster",
                TypeInfo(CacheCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific cluster.
    cache_cluster: "CacheCluster" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCacheParameterGroupMessage(ShapeBase):
    """
    Represents the input of a `CreateCacheParameterGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_family",
                "CacheParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # A user-specified name for the cache parameter group.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cache parameter group family that the cache parameter group
    # can be used with.

    # Valid values are: `memcached1.4` | `redis2.6` | `redis2.8` | `redis3.2`
    cache_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A user-specified description for the cache parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCacheParameterGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_parameter_group",
                "CacheParameterGroup",
                TypeInfo(CacheParameterGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of a `CreateCacheParameterGroup` operation.
    cache_parameter_group: "CacheParameterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCacheSecurityGroupMessage(ShapeBase):
    """
    Represents the input of a `CreateCacheSecurityGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # A name for the cache security group. This value is stored as a lowercase
    # string.

    # Constraints: Must contain no more than 255 alphanumeric characters. Cannot
    # be the word "Default".

    # Example: `mysecuritygroup`
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the cache security group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCacheSecurityGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_security_group",
                "CacheSecurityGroup",
                TypeInfo(CacheSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of one of the following operations:

    #   * `AuthorizeCacheSecurityGroupIngress`

    #   * `CreateCacheSecurityGroup`

    #   * `RevokeCacheSecurityGroupIngress`
    cache_security_group: "CacheSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCacheSubnetGroupMessage(ShapeBase):
    """
    Represents the input of a `CreateCacheSubnetGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "cache_subnet_group_description",
                "CacheSubnetGroupDescription",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A name for the cache subnet group. This value is stored as a lowercase
    # string.

    # Constraints: Must contain no more than 255 alphanumeric characters or
    # hyphens.

    # Example: `mysubnetgroup`
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the cache subnet group.
    cache_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of VPC subnet IDs for the cache subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCacheSubnetGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_subnet_group",
                "CacheSubnetGroup",
                TypeInfo(CacheSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of one of the following operations:

    #   * `CreateCacheSubnetGroup`

    #   * `ModifyCacheSubnetGroup`
    cache_subnet_group: "CacheSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReplicationGroupMessage(ShapeBase):
    """
    Represents the input of a `CreateReplicationGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "replication_group_description",
                "ReplicationGroupDescription",
                TypeInfo(str),
            ),
            (
                "primary_cluster_id",
                "PrimaryClusterId",
                TypeInfo(str),
            ),
            (
                "automatic_failover_enabled",
                "AutomaticFailoverEnabled",
                TypeInfo(bool),
            ),
            (
                "num_cache_clusters",
                "NumCacheClusters",
                TypeInfo(int),
            ),
            (
                "preferred_cache_cluster_a_zs",
                "PreferredCacheClusterAZs",
                TypeInfo(typing.List[str]),
            ),
            (
                "num_node_groups",
                "NumNodeGroups",
                TypeInfo(int),
            ),
            (
                "replicas_per_node_group",
                "ReplicasPerNodeGroup",
                TypeInfo(int),
            ),
            (
                "node_group_configuration",
                "NodeGroupConfiguration",
                TypeInfo(typing.List[NodeGroupConfiguration]),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "cache_security_group_names",
                "CacheSecurityGroupNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "snapshot_arns",
                "SnapshotArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "snapshot_name",
                "SnapshotName",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "notification_topic_arn",
                "NotificationTopicArn",
                TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "auth_token",
                "AuthToken",
                TypeInfo(str),
            ),
            (
                "transit_encryption_enabled",
                "TransitEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "at_rest_encryption_enabled",
                "AtRestEncryptionEnabled",
                TypeInfo(bool),
            ),
        ]

    # The replication group identifier. This parameter is stored as a lowercase
    # string.

    # Constraints:

    #   * A name must contain from 1 to 20 alphanumeric characters or hyphens.

    #   * The first character must be a letter.

    #   * A name cannot end with a hyphen or contain two consecutive hyphens.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-created description for the replication group.
    replication_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the cluster that serves as the primary for this
    # replication group. This cluster must already exist and have a status of
    # `available`.

    # This parameter is not required if `NumCacheClusters`, `NumNodeGroups`, or
    # `ReplicasPerNodeGroup` is specified.
    primary_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether a read-only replica is automatically promoted to
    # read/write primary if the existing primary fails.

    # If `true`, Multi-AZ is enabled for this replication group. If `false`,
    # Multi-AZ is disabled for this replication group.

    # `AutomaticFailoverEnabled` must be enabled for Redis (cluster mode enabled)
    # replication groups.

    # Default: false

    # Amazon ElastiCache for Redis does not support Multi-AZ with automatic
    # failover on:

    #   * Redis versions earlier than 2.8.6.

    #   * Redis (cluster mode disabled): T1 and T2 cache node types.

    #   * Redis (cluster mode enabled): T1 node types.
    automatic_failover_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of clusters this replication group initially has.

    # This parameter is not used if there is more than one node group (shard).
    # You should use `ReplicasPerNodeGroup` instead.

    # If `AutomaticFailoverEnabled` is `true`, the value of this parameter must
    # be at least 2. If `AutomaticFailoverEnabled` is `false` you can omit this
    # parameter (it will default to 1), or you can explicitly set it to a value
    # between 2 and 6.

    # The maximum permitted value for `NumCacheClusters` is 6 (primary plus 5
    # replicas).
    num_cache_clusters: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of EC2 Availability Zones in which the replication group's clusters
    # are created. The order of the Availability Zones in the list is the order
    # in which clusters are allocated. The primary cluster is created in the
    # first AZ in the list.

    # This parameter is not used if there is more than one node group (shard).
    # You should use `NodeGroupConfiguration` instead.

    # If you are creating your replication group in an Amazon VPC (recommended),
    # you can only locate clusters in Availability Zones associated with the
    # subnets in the selected subnet group.

    # The number of Availability Zones listed must equal the value of
    # `NumCacheClusters`.

    # Default: system chosen Availability Zones.
    preferred_cache_cluster_a_zs: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional parameter that specifies the number of node groups (shards) for
    # this Redis (cluster mode enabled) replication group. For Redis (cluster
    # mode disabled) either omit this parameter or set it to 1.

    # Default: 1
    num_node_groups: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the number of replica nodes in each
    # node group (shard). Valid values are 0 to 5.
    replicas_per_node_group: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of node group (shard) configuration options. Each node group (shard)
    # configuration has the following: Slots, PrimaryAvailabilityZone,
    # ReplicaAvailabilityZones, ReplicaCount.

    # If you're creating a Redis (cluster mode disabled) or a Redis (cluster mode
    # enabled) replication group, you can use this parameter to individually
    # configure each node group (shard), or you can omit this parameter.
    node_group_configuration: typing.List["NodeGroupConfiguration"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The compute and memory capacity of the nodes in the node group (shard).

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache engine to be used for the clusters in this
    # replication group.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the cache engine to be used for the clusters in this
    # replication group. To view the supported cache engine versions, use the
    # `DescribeCacheEngineVersions` operation.

    # **Important:** You can upgrade to a newer engine version (see [Selecting a
    # Cache Engine and
    # Version](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement))
    # in the _ElastiCache User Guide_ , but you cannot downgrade to an earlier
    # engine version. If you want to use an earlier engine version, you must
    # delete the existing cluster or replication group and create it anew with
    # the earlier engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the parameter group to associate with this replication group.
    # If this argument is omitted, the default cache parameter group for the
    # specified engine is used.

    # If you are running Redis version 3.2.4 or later, only one node group
    # (shard), and want to use a default parameter group, we recommend that you
    # specify the parameter group by name.

    #   * To create a Redis (cluster mode disabled) replication group, use `CacheParameterGroupName=default.redis3.2`.

    #   * To create a Redis (cluster mode enabled) replication group, use `CacheParameterGroupName=default.redis3.2.cluster.on`.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cache subnet group to be used for the replication group.

    # If you're going to launch your cluster in an Amazon VPC, you need to create
    # a subnet group before you start creating a cluster. For more information,
    # see [Subnets and Subnet
    # Groups](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SubnetGroups.html).
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cache security group names to associate with this replication
    # group.
    cache_security_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more Amazon VPC security groups associated with this replication
    # group.

    # Use this parameter only when you are creating a replication group in an
    # Amazon Virtual Private Cloud (Amazon VPC).
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cost allocation tags to be added to this resource. A tag is a
    # key-value pair. A tag key does not have to be accompanied by a tag value.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB
    # snapshot files stored in Amazon S3. The snapshot files are used to populate
    # the new replication group. The Amazon S3 object name in the ARN cannot
    # contain any commas. The new replication group will have the number of node
    # groups (console: shards) specified by the parameter _NumNodeGroups_ or the
    # number of node groups configured by _NodeGroupConfiguration_ regardless of
    # the number of ARNs specified here.

    # Example of an Amazon S3 ARN: `arn:aws:s3:::my_bucket/snapshot1.rdb`
    snapshot_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a snapshot from which to restore data into the new replication
    # group. The snapshot status changes to `restoring` while the new replication
    # group is being created.
    snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.
    # Valid values for `ddd` are:

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.

    # Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:23:00-mon:01:30`
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which each member of the replication group accepts
    # connections.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
    # (SNS) topic to which notifications are sent.

    # The Amazon SNS topic owner must be the same as the cluster owner.
    notification_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is currently disabled.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which ElastiCache retains automatic snapshots before
    # deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a
    # snapshot that was taken today is retained for 5 days before being deleted.

    # Default: 0 (i.e., automatic backups are disabled for this cluster).
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range (in UTC) during which ElastiCache begins taking a
    # daily snapshot of your node group (shard).

    # Example: `05:00-09:00`

    # If you do not specify this parameter, ElastiCache automatically chooses an
    # appropriate time range.
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # **Reserved parameter.** The password used to access a password protected
    # server.

    # This parameter is valid only if:

    #   * The parameter `TransitEncryptionEnabled` was set to `true` when the cluster was created.

    #   * The line `requirepass` was added to the database configuration file.

    # Password constraints:

    #   * Must be only printable ASCII characters.

    #   * Must be at least 16 characters and no more than 128 characters in length.

    #   * Cannot contain any of the following characters: '/', '"', or '@'.

    # For more information, see [AUTH password](http://redis.io/commands/AUTH) at
    # http://redis.io/commands/AUTH.
    auth_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that enables in-transit encryption when set to `true`.

    # You cannot modify the value of `TransitEncryptionEnabled` after the cluster
    # is created. To enable in-transit encryption on a cluster you must set
    # `TransitEncryptionEnabled` to `true` when you create a cluster.

    # This parameter is valid only if the `Engine` parameter is `redis`, the
    # `EngineVersion` parameter is `3.2.4` or later, and the cluster is being
    # created in an Amazon VPC.

    # If you enable in-transit encryption, you must also specify a value for
    # `CacheSubnetGroup`.

    # Default: `false`
    transit_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that enables encryption at rest when set to `true`.

    # You cannot modify the value of `AtRestEncryptionEnabled` after the
    # replication group is created. To enable encryption at rest on a replication
    # group you must set `AtRestEncryptionEnabled` to `true` when you create the
    # replication group.

    # This parameter is valid only if the `Engine` parameter is `redis` and the
    # cluster is being created in an Amazon VPC.

    # Default: `false`
    at_rest_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReplicationGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(ReplicationGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific Redis replication group.
    replication_group: "ReplicationGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSnapshotMessage(ShapeBase):
    """
    Represents the input of a `CreateSnapshot` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_name",
                "SnapshotName",
                TypeInfo(str),
            ),
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
        ]

    # A name for the snapshot being created.
    snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of an existing replication group. The snapshot is created
    # from this replication group.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of an existing cluster. The snapshot is created from this
    # cluster.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "snapshot",
                "Snapshot",
                TypeInfo(Snapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents a copy of an entire Redis cluster as of the time when the
    # snapshot was taken.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCacheClusterMessage(ShapeBase):
    """
    Represents the input of a `DeleteCacheCluster` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "final_snapshot_identifier",
                "FinalSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The cluster identifier for the cluster to be deleted. This parameter is not
    # case sensitive.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-supplied name of a final cluster snapshot. This is the unique name
    # that identifies the snapshot. ElastiCache creates the snapshot, and then
    # deletes the cluster immediately afterward.
    final_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCacheClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_cluster",
                "CacheCluster",
                TypeInfo(CacheCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific cluster.
    cache_cluster: "CacheCluster" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCacheParameterGroupMessage(ShapeBase):
    """
    Represents the input of a `DeleteCacheParameterGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the cache parameter group to delete.

    # The specified cache security group must not be associated with any
    # clusters.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCacheSecurityGroupMessage(ShapeBase):
    """
    Represents the input of a `DeleteCacheSecurityGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the cache security group to delete.

    # You cannot delete the default security group.
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCacheSubnetGroupMessage(ShapeBase):
    """
    Represents the input of a `DeleteCacheSubnetGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the cache subnet group to delete.

    # Constraints: Must contain no more than 255 alphanumeric characters or
    # hyphens.
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationGroupMessage(ShapeBase):
    """
    Represents the input of a `DeleteReplicationGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "retain_primary_cluster",
                "RetainPrimaryCluster",
                TypeInfo(bool),
            ),
            (
                "final_snapshot_identifier",
                "FinalSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier for the cluster to be deleted. This parameter is not case
    # sensitive.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to `true`, all of the read replicas are deleted, but the primary
    # node is retained.
    retain_primary_cluster: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a final node group (shard) snapshot. ElastiCache creates the
    # snapshot from the primary node in the cluster, rather than one of the
    # replicas; this is to ensure that it captures the freshest data. After the
    # final snapshot is taken, the replication group is immediately deleted.
    final_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(ReplicationGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific Redis replication group.
    replication_group: "ReplicationGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSnapshotMessage(ShapeBase):
    """
    Represents the input of a `DeleteSnapshot` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_name",
                "SnapshotName",
                TypeInfo(str),
            ),
        ]

    # The name of the snapshot to be deleted.
    snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "snapshot",
                "Snapshot",
                TypeInfo(Snapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents a copy of an entire Redis cluster as of the time when the
    # snapshot was taken.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCacheClustersMessage(ShapeBase):
    """
    Represents the input of a `DescribeCacheClusters` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "show_cache_node_info",
                "ShowCacheNodeInfo",
                TypeInfo(bool),
            ),
            (
                "show_cache_clusters_not_in_replication_groups",
                "ShowCacheClustersNotInReplicationGroups",
                TypeInfo(bool),
            ),
        ]

    # The user-supplied cluster identifier. If this parameter is specified, only
    # information about that specific cluster is returned. This parameter isn't
    # case sensitive.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional flag that can be included in the `DescribeCacheCluster` request
    # to retrieve information about the individual cache nodes.
    show_cache_node_info: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional flag that can be included in the `DescribeCacheCluster` request
    # to show only nodes (API/CLI: clusters) that are not members of a
    # replication group. In practice, this mean Memcached and single node Redis
    # clusters.
    show_cache_clusters_not_in_replication_groups: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCacheEngineVersionsMessage(ShapeBase):
    """
    Represents the input of a `DescribeCacheEngineVersions` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_family",
                "CacheParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "default_only",
                "DefaultOnly",
                TypeInfo(bool),
            ),
        ]

    # The cache engine to return. Valid values: `memcached` | `redis`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cache engine version to return.

    # Example: `1.4.14`
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a specific cache parameter group family to return details for.

    # Valid values are: `memcached1.4` | `redis2.6` | `redis2.8` | `redis3.2`

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    cache_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, specifies that only the default version of the specified engine
    # or engine and major version combination is to be returned.
    default_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCacheParameterGroupsMessage(ShapeBase):
    """
    Represents the input of a `DescribeCacheParameterGroups` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The name of a specific cache parameter group to return details for.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCacheParametersMessage(ShapeBase):
    """
    Represents the input of a `DescribeCacheParameters` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The name of a specific cache parameter group to return details for.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter types to return.

    # Valid values: `user` | `system` | `engine-default`
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCacheSecurityGroupsMessage(ShapeBase):
    """
    Represents the input of a `DescribeCacheSecurityGroups` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The name of the cache security group to return details for.
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCacheSubnetGroupsMessage(ShapeBase):
    """
    Represents the input of a `DescribeCacheSubnetGroups` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The name of the cache subnet group to return details for.
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultParametersMessage(ShapeBase):
    """
    Represents the input of a `DescribeEngineDefaultParameters` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_family",
                "CacheParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The name of the cache parameter group family.

    # Valid values are: `memcached1.4` | `redis2.6` | `redis2.8` | `redis3.2`
    cache_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultParametersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "engine_defaults",
                "EngineDefaults",
                TypeInfo(EngineDefaults),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of a `DescribeEngineDefaultParameters` operation.
    engine_defaults: "EngineDefaults" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeEngineDefaultParametersResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEventsMessage(ShapeBase):
    """
    Represents the input of a `DescribeEvents` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_identifier",
                "SourceIdentifier",
                TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(typing.Union[str, SourceType]),
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
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The identifier of the event source for which events are returned. If not
    # specified, all sources are included in the response.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event source to retrieve events for. If no value is specified, all
    # events are returned.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The beginning of the time interval to retrieve events for, specified in ISO
    # 8601 format.

    # **Example:** 2017-03-30T07:03:49.555Z
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time interval for which to retrieve events, specified in ISO
    # 8601 format.

    # **Example:** 2017-03-30T07:03:49.555Z
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes worth of events to retrieve.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReplicationGroupsMessage(ShapeBase):
    """
    Represents the input of a `DescribeReplicationGroups` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The identifier for the replication group to be described. This parameter is
    # not case sensitive.

    # If you do not specify this parameter, information about all replication
    # groups is returned.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedCacheNodesMessage(ShapeBase):
    """
    Represents the input of a `DescribeReservedCacheNodes` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_cache_node_id",
                "ReservedCacheNodeId",
                TypeInfo(str),
            ),
            (
                "reserved_cache_nodes_offering_id",
                "ReservedCacheNodesOfferingId",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(str),
            ),
            (
                "product_description",
                "ProductDescription",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The reserved cache node identifier filter value. Use this parameter to show
    # only the reservation that matches the specified reservation ID.
    reserved_cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering identifier filter value. Use this parameter to show only
    # purchased reservations matching the specified offering identifier.
    reserved_cache_nodes_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cache node type filter value. Use this parameter to show only those
    # reservations matching the specified cache node type.

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration filter value, specified in years or seconds. Use this
    # parameter to show only reservations for this duration.

    # Valid Values: `1 | 3 | 31536000 | 94608000`
    duration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product description filter value. Use this parameter to show only those
    # reservations matching the specified product description.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type filter value. Use this parameter to show only the
    # available offerings matching the specified offering type.

    # Valid values: `"Light Utilization"|"Medium Utilization"|"Heavy
    # Utilization"`
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedCacheNodesOfferingsMessage(ShapeBase):
    """
    Represents the input of a `DescribeReservedCacheNodesOfferings` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_cache_nodes_offering_id",
                "ReservedCacheNodesOfferingId",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(str),
            ),
            (
                "product_description",
                "ProductDescription",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The offering identifier filter value. Use this parameter to show only the
    # available offering that matches the specified reservation identifier.

    # Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`
    reserved_cache_nodes_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cache node type filter value. Use this parameter to show only the
    # available offerings matching the specified cache node type.

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Duration filter value, specified in years or seconds. Use this parameter to
    # show only reservations for a given duration.

    # Valid Values: `1 | 3 | 31536000 | 94608000`
    duration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product description filter value. Use this parameter to show only the
    # available offerings matching the specified product description.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type filter value. Use this parameter to show only the
    # available offerings matching the specified offering type.

    # Valid Values: `"Light Utilization"|"Medium Utilization"|"Heavy
    # Utilization"`
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 100

    # Constraints: minimum 20; maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSnapshotsListMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeSnapshots` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "snapshots",
                "Snapshots",
                TypeInfo(typing.List[Snapshot]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of snapshots. Each item in the list contains detailed information
    # about one snapshot.
    snapshots: typing.List["Snapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeSnapshotsListMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeSnapshotsMessage(ShapeBase):
    """
    Represents the input of a `DescribeSnapshotsMessage` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "snapshot_name",
                "SnapshotName",
                TypeInfo(str),
            ),
            (
                "snapshot_source",
                "SnapshotSource",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "show_node_group_config",
                "ShowNodeGroupConfig",
                TypeInfo(bool),
            ),
        ]

    # A user-supplied replication group identifier. If this parameter is
    # specified, only snapshots associated with that specific replication group
    # are described.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-supplied cluster identifier. If this parameter is specified, only
    # snapshots associated with that specific cluster are described.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-supplied name of the snapshot. If this parameter is specified, only
    # this snapshot are described.
    snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to `system`, the output shows snapshots that were automatically
    # created by ElastiCache. If set to `user` the output shows snapshots that
    # were manually created. If omitted, the output shows both automatically and
    # manually created snapshots.
    snapshot_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional marker returned from a prior request. Use this marker for
    # pagination of results from this operation. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a marker is included in the
    # response so that the remaining results can be retrieved.

    # Default: 50

    # Constraints: minimum 20; maximum 50.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value which if true, the node group (shard) configuration is
    # included in the snapshot description.
    show_node_group_config: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EC2SecurityGroup(ShapeBase):
    """
    Provides ownership and status information for an Amazon EC2 security group.
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
                "ec2_security_group_name",
                "EC2SecurityGroupName",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_owner_id",
                "EC2SecurityGroupOwnerId",
                TypeInfo(str),
            ),
        ]

    # The status of the Amazon EC2 security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon EC2 security group.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account ID of the Amazon EC2 security group owner.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    """
    Represents the information required for client programs to connect to a cache
    node.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
        ]

    # The DNS hostname of the cache node.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number that the cache engine is listening on.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EngineDefaults(ShapeBase):
    """
    Represents the output of a `DescribeEngineDefaultParameters` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_family",
                "CacheParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
            (
                "cache_node_type_specific_parameters",
                "CacheNodeTypeSpecificParameters",
                TypeInfo(typing.List[CacheNodeTypeSpecificParameter]),
            ),
        ]

    # Specifies the name of the cache parameter group family to which the engine
    # default parameters apply.

    # Valid values are: `memcached1.4` | `redis2.6` | `redis2.8` | `redis3.2`
    cache_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of engine default parameters.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of parameters specific to a particular cache node type. Each element
    # in the list contains detailed information about one parameter.
    cache_node_type_specific_parameters: typing.List[
        "CacheNodeTypeSpecificParameter"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class Event(ShapeBase):
    """
    Represents a single occurrence of something interesting within the system. Some
    examples of events are creating a cluster, adding or removing a cache node, or
    rebooting a node.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_identifier",
                "SourceIdentifier",
                TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(typing.Union[str, SourceType]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier for the source of the event. For example, if the event
    # occurred at the cluster level, the identifier would be the name of the
    # cluster.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the origin of this event - a cluster, a parameter group, a
    # security group, etc.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The text of the event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the event occurred.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventsMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeEvents` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[Event]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of events. Each element in the list contains detailed information
    # about one event.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["EventsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class InsufficientCacheClusterCapacityFault(ShapeBase):
    """
    The requested cache node type is not available in the specified Availability
    Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidARNFault(ShapeBase):
    """
    The requested Amazon Resource Name (ARN) does not refer to an existing resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCacheClusterStateFault(ShapeBase):
    """
    The requested cluster is not in the `available` state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCacheParameterGroupStateFault(ShapeBase):
    """
    The current state of the cache parameter group does not allow the requested
    operation to occur.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidCacheSecurityGroupStateFault(ShapeBase):
    """
    The current state of the cache security group does not allow deletion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterCombinationException(ShapeBase):
    """
    Two or more incompatible parameters were specified.
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

    # Two or more parameters that must not be used together were used together.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterValueException(ShapeBase):
    """
    The value for a parameter is invalid.
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

    # A parameter value is invalid.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidReplicationGroupStateFault(ShapeBase):
    """
    The requested replication group is not in the `available` state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSnapshotStateFault(ShapeBase):
    """
    The current state of the snapshot does not allow the requested operation to
    occur.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnet(ShapeBase):
    """
    An invalid subnet identifier was specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidVPCNetworkStateFault(ShapeBase):
    """
    The VPC network is in an invalid state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAllowedNodeTypeModificationsMessage(ShapeBase):
    """
    The input parameters for the `ListAllowedNodeTypeModifications` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
        ]

    # The name of the cluster you want to scale up to a larger node instanced
    # type. ElastiCache uses the cluster id to identify the current node type of
    # this cluster and from that to create a list of node types you can scale up
    # to.

    # You must provide a value for either the `CacheClusterId` or the
    # `ReplicationGroupId`.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the replication group want to scale up to a larger node type.
    # ElastiCache uses the replication group id to identify the current node type
    # being used by this replication group, and from that to create a list of
    # node types you can scale up to.

    # You must provide a value for either the `CacheClusterId` or the
    # `ReplicationGroupId`.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceMessage(ShapeBase):
    """
    The input parameters for the `ListTagsForResource` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource for which you want the list
    # of tags, for example `arn:aws:elasticache:us-
    # west-2:0123456789:cluster:myCluster` or `arn:aws:elasticache:us-
    # west-2:0123456789:snapshot:mySnapshot`.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyCacheClusterMessage(ShapeBase):
    """
    Represents the input of a `ModifyCacheCluster` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "num_cache_nodes",
                "NumCacheNodes",
                TypeInfo(int),
            ),
            (
                "cache_node_ids_to_remove",
                "CacheNodeIdsToRemove",
                TypeInfo(typing.List[str]),
            ),
            (
                "az_mode",
                "AZMode",
                TypeInfo(typing.Union[str, AZMode]),
            ),
            (
                "new_availability_zones",
                "NewAvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "cache_security_group_names",
                "CacheSecurityGroupNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "notification_topic_arn",
                "NotificationTopicArn",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "notification_topic_status",
                "NotificationTopicStatus",
                TypeInfo(str),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
        ]

    # The cluster identifier. This value is stored as a lowercase string.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of cache nodes that the cluster should have. If the value for
    # `NumCacheNodes` is greater than the sum of the number of current cache
    # nodes and the number of cache nodes pending creation (which may be zero),
    # more nodes are added. If the value is less than the number of existing
    # cache nodes, nodes are removed. If the value is equal to the number of
    # current cache nodes, any pending add or remove requests are canceled.

    # If you are removing cache nodes, you must use the `CacheNodeIdsToRemove`
    # parameter to provide the IDs of the specific cache nodes to remove.

    # For clusters running Redis, this value must be 1. For clusters running
    # Memcached, this value must be between 1 and 20.

    # Adding or removing Memcached cache nodes can be applied immediately or as a
    # pending operation (see `ApplyImmediately`).

    # A pending operation to modify the number of cache nodes in a cluster during
    # its maintenance window, whether by adding or removing nodes in accordance
    # with the scale out architecture, is not queued. The customer's latest
    # request to add or remove nodes to the cluster overrides any previous
    # pending operations to modify the number of cache nodes in the cluster. For
    # example, a request to remove 2 nodes would override a previous pending
    # operation to remove 3 nodes. Similarly, a request to add 2 nodes would
    # override a previous pending operation to remove 3 nodes and vice versa. As
    # Memcached cache nodes may now be provisioned in different Availability
    # Zones with flexible cache node placement, a request to add nodes does not
    # automatically override a previous pending operation to add nodes. The
    # customer can modify the previous pending operation to add more nodes or
    # explicitly cancel the pending request and retry the new request. To cancel
    # pending operations to modify the number of cache nodes in a cluster, use
    # the `ModifyCacheCluster` request and set `NumCacheNodes` equal to the
    # number of cache nodes currently in the cluster.
    num_cache_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache node IDs to be removed. A node ID is a numeric identifier
    # (0001, 0002, etc.). This parameter is only valid when `NumCacheNodes` is
    # less than the existing number of cache nodes. The number of cache node IDs
    # supplied in this parameter must match the difference between the existing
    # number of cache nodes in the cluster or pending cache nodes, whichever is
    # greater, and the value of `NumCacheNodes` in the request.

    # For example: If you have 3 active cache nodes, 7 pending cache nodes, and
    # the number of cache nodes in this `ModifyCacheCluster` call is 5, you must
    # list 2 (7 - 5) cache node IDs to remove.
    cache_node_ids_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the new nodes in this Memcached cluster are all created
    # in a single Availability Zone or created across multiple Availability
    # Zones.

    # Valid values: `single-az` | `cross-az`.

    # This option is only supported for Memcached clusters.

    # You cannot specify `single-az` if the Memcached cluster already has cache
    # nodes in different Availability Zones. If `cross-az` is specified, existing
    # Memcached nodes remain in their current Availability Zone.

    # Only newly created nodes are located in different Availability Zones. For
    # instructions on how to move existing Memcached nodes to different
    # Availability Zones, see the **Availability Zone Considerations** section of
    # [Cache Node Considerations for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheNode.Memcached.html).
    az_mode: typing.Union[str, "AZMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of Availability Zones where the new Memcached cache nodes are
    # created.

    # This parameter is only valid when `NumCacheNodes` in the request is greater
    # than the sum of the number of active cache nodes and the number of cache
    # nodes pending creation (which may be zero). The number of Availability
    # Zones supplied in this list must match the cache nodes being added in this
    # request.

    # This option is only supported on Memcached clusters.

    # Scenarios:

    #   * **Scenario 1:** You have 3 active nodes and wish to add 2 nodes. Specify `NumCacheNodes=5` (3 + 2) and optionally specify two Availability Zones for the two new nodes.

    #   * **Scenario 2:** You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify `NumCacheNodes=6` ((3 + 2) + 1) and optionally specify an Availability Zone for the new node.

    #   * **Scenario 3:** You want to cancel all pending operations. Specify `NumCacheNodes=3` to cancel all pending operations.

    # The Availability Zone placement of nodes pending creation cannot be
    # modified. If you wish to cancel any nodes pending creation, add 0 nodes by
    # setting `NumCacheNodes` to the number of current nodes.

    # If `cross-az` is specified, existing Memcached nodes remain in their
    # current Availability Zone. Only newly created nodes can be located in
    # different Availability Zones. For guidance on how to move existing
    # Memcached nodes to different Availability Zones, see the **Availability
    # Zone Considerations** section of [Cache Node Considerations for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheNode.Memcached.html).

    # **Impact of new add/remove requests upon pending requests**

    #   * Scenario-1

    #     * Pending Action: Delete

    #     * New Request: Delete

    #     * Result: The new delete, pending or immediate, replaces the pending delete.

    #   * Scenario-2

    #     * Pending Action: Delete

    #     * New Request: Create

    #     * Result: The new create, pending or immediate, replaces the pending delete.

    #   * Scenario-3

    #     * Pending Action: Create

    #     * New Request: Delete

    #     * Result: The new delete, pending or immediate, replaces the pending create.

    #   * Scenario-4

    #     * Pending Action: Create

    #     * New Request: Create

    #     * Result: The new create is added to the pending create.

    # **Important:** If the new create request is **Apply Immediately - Yes** ,
    # all creates are performed immediately. If the new create request is **Apply
    # Immediately - No** , all creates are pending.
    new_availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cache security group names to authorize on this cluster. This
    # change is asynchronously applied as soon as possible.

    # You can use this parameter only with clusters that are created outside of
    # an Amazon Virtual Private Cloud (Amazon VPC).

    # Constraints: Must contain no more than 255 alphanumeric characters. Must
    # not be "Default".
    cache_security_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the VPC Security Groups associated with the cluster.

    # This parameter can be used only with clusters that are created in an Amazon
    # Virtual Private Cloud (Amazon VPC).
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.

    # Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:23:00-mon:01:30`
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to which
    # notifications are sent.

    # The Amazon SNS topic owner must be same as the cluster owner.
    notification_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache parameter group to apply to this cluster. This change
    # is asynchronously applied as soon as possible for parameters when the
    # `ApplyImmediately` parameter is specified as `true` for this request.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the Amazon SNS notification topic. Notifications are sent
    # only if the status is `active`.

    # Valid values: `active` | `inactive`
    notification_topic_status: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `true`, this parameter causes the modifications in this request and any
    # pending modifications to be applied, asynchronously and as soon as
    # possible, regardless of the `PreferredMaintenanceWindow` setting for the
    # cluster.

    # If `false`, changes to the cluster are applied on the next maintenance
    # reboot, or the next failure reboot, whichever occurs first.

    # If you perform a `ModifyCacheCluster` before a pending modification is
    # applied, the pending modification is replaced by the newer modification.

    # Valid values: `true` | `false`

    # Default: `false`
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upgraded version of the cache engine to be run on the cache nodes.

    # **Important:** You can upgrade to a newer engine version (see [Selecting a
    # Cache Engine and
    # Version](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement)),
    # but you cannot downgrade to an earlier engine version. If you want to use
    # an earlier engine version, you must delete the existing cluster and create
    # it anew with the earlier engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is currently disabled.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which ElastiCache retains automatic cluster
    # snapshots before deleting them. For example, if you set
    # `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained
    # for 5 days before being deleted.

    # If the value of `SnapshotRetentionLimit` is set to zero (0), backups are
    # turned off.
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range (in UTC) during which ElastiCache begins taking a
    # daily snapshot of your cluster.
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid cache node type that you want to scale this cluster up to.
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyCacheClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_cluster",
                "CacheCluster",
                TypeInfo(CacheCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific cluster.
    cache_cluster: "CacheCluster" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyCacheParameterGroupMessage(ShapeBase):
    """
    Represents the input of a `ModifyCacheParameterGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_name_values",
                "ParameterNameValues",
                TypeInfo(typing.List[ParameterNameValue]),
            ),
        ]

    # The name of the cache parameter group to modify.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of parameter names and values for the parameter update. You must
    # supply at least one parameter name and value; subsequent arguments are
    # optional. A maximum of 20 parameters may be modified per request.
    parameter_name_values: typing.List["ParameterNameValue"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class ModifyCacheSubnetGroupMessage(ShapeBase):
    """
    Represents the input of a `ModifyCacheSubnetGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "cache_subnet_group_description",
                "CacheSubnetGroupDescription",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name for the cache subnet group. This value is stored as a lowercase
    # string.

    # Constraints: Must contain no more than 255 alphanumeric characters or
    # hyphens.

    # Example: `mysubnetgroup`
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the cache subnet group.
    cache_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 subnet IDs for the cache subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyCacheSubnetGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_subnet_group",
                "CacheSubnetGroup",
                TypeInfo(CacheSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of one of the following operations:

    #   * `CreateCacheSubnetGroup`

    #   * `ModifyCacheSubnetGroup`
    cache_subnet_group: "CacheSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationGroupMessage(ShapeBase):
    """
    Represents the input of a `ModifyReplicationGroups` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "replication_group_description",
                "ReplicationGroupDescription",
                TypeInfo(str),
            ),
            (
                "primary_cluster_id",
                "PrimaryClusterId",
                TypeInfo(str),
            ),
            (
                "snapshotting_cluster_id",
                "SnapshottingClusterId",
                TypeInfo(str),
            ),
            (
                "automatic_failover_enabled",
                "AutomaticFailoverEnabled",
                TypeInfo(bool),
            ),
            (
                "cache_security_group_names",
                "CacheSecurityGroupNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "notification_topic_arn",
                "NotificationTopicArn",
                TypeInfo(str),
            ),
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "notification_topic_status",
                "NotificationTopicStatus",
                TypeInfo(str),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "node_group_id",
                "NodeGroupId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the replication group to modify.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description for the replication group. Maximum length is 255 characters.
    replication_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For replication groups with a single primary, if this parameter is
    # specified, ElastiCache promotes the specified cluster in the specified
    # replication group to the primary role. The nodes of all other clusters in
    # the replication group are read replicas.
    primary_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cluster ID that is used as the daily snapshot source for the
    # replication group. This parameter cannot be set for Redis (cluster mode
    # enabled) replication groups.
    snapshotting_cluster_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines whether a read replica is automatically promoted to read/write
    # primary if the existing primary encounters a failure.

    # Valid values: `true` | `false`

    # Amazon ElastiCache for Redis does not support Multi-AZ with automatic
    # failover on:

    #   * Redis versions earlier than 2.8.6.

    #   * Redis (cluster mode disabled): T1 and T2 cache node types.

    #   * Redis (cluster mode enabled): T1 node types.
    automatic_failover_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cache security group names to authorize for the clusters in this
    # replication group. This change is asynchronously applied as soon as
    # possible.

    # This parameter can be used only with replication group containing clusters
    # running outside of an Amazon Virtual Private Cloud (Amazon VPC).

    # Constraints: Must contain no more than 255 alphanumeric characters. Must
    # not be `Default`.
    cache_security_group_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the VPC Security Groups associated with the clusters in the
    # replication group.

    # This parameter can be used only with replication group containing clusters
    # running in an Amazon Virtual Private Cloud (Amazon VPC).
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.

    # Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:23:00-mon:01:30`
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to which
    # notifications are sent.

    # The Amazon SNS topic owner must be same as the replication group owner.
    notification_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache parameter group to apply to all of the clusters in
    # this replication group. This change is asynchronously applied as soon as
    # possible for parameters when the `ApplyImmediately` parameter is specified
    # as `true` for this request.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the Amazon SNS notification topic for the replication group.
    # Notifications are sent only if the status is `active`.

    # Valid values: `active` | `inactive`
    notification_topic_status: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `true`, this parameter causes the modifications in this request and any
    # pending modifications to be applied, asynchronously and as soon as
    # possible, regardless of the `PreferredMaintenanceWindow` setting for the
    # replication group.

    # If `false`, changes to the nodes in the replication group are applied on
    # the next maintenance reboot, or the next failure reboot, whichever occurs
    # first.

    # Valid values: `true` | `false`

    # Default: `false`
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upgraded version of the cache engine to be run on the clusters in the
    # replication group.

    # **Important:** You can upgrade to a newer engine version (see [Selecting a
    # Cache Engine and
    # Version](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement)),
    # but you cannot downgrade to an earlier engine version. If you want to use
    # an earlier engine version, you must delete the existing replication group
    # and create it anew with the earlier engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is currently disabled.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which ElastiCache retains automatic node group
    # (shard) snapshots before deleting them. For example, if you set
    # `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained
    # for 5 days before being deleted.

    # **Important** If the value of SnapshotRetentionLimit is set to zero (0),
    # backups are turned off.
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range (in UTC) during which ElastiCache begins taking a
    # daily snapshot of the node group (shard) specified by
    # `SnapshottingClusterId`.

    # Example: `05:00-09:00`

    # If you do not specify this parameter, ElastiCache automatically chooses an
    # appropriate time range.
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid cache node type that you want to scale this replication group to.
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Node Group (called shard in the console).
    node_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyReplicationGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(ReplicationGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific Redis replication group.
    replication_group: "ReplicationGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationGroupShardConfigurationMessage(ShapeBase):
    """
    Represents the input for a `ModifyReplicationGroupShardConfiguration` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "node_group_count",
                "NodeGroupCount",
                TypeInfo(int),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
            (
                "resharding_configuration",
                "ReshardingConfiguration",
                TypeInfo(typing.List[ReshardingConfiguration]),
            ),
            (
                "node_groups_to_remove",
                "NodeGroupsToRemove",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Redis (cluster mode enabled) cluster (replication group) on
    # which the shards are to be configured.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of node groups (shards) that results from the modification of
    # the shard configuration.
    node_group_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the shard reconfiguration process begins immediately. At
    # present, the only permitted value for this parameter is `true`.

    # Value: true
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the preferred availability zones for each node group in the
    # cluster. If the value of `NodeGroupCount` is greater than the current
    # number of node groups (shards), you can use this parameter to specify the
    # preferred availability zones of the cluster's shards. If you omit this
    # parameter ElastiCache selects availability zones for you.

    # You can specify this parameter only if the value of `NodeGroupCount` is
    # greater than the current number of node groups (shards).
    resharding_configuration: typing.List["ReshardingConfiguration"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # If the value of `NodeGroupCount` is less than the current number of node
    # groups (shards), `NodeGroupsToRemove` is a required list of node group ids
    # to remove from the cluster.
    node_groups_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationGroupShardConfigurationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(ReplicationGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific Redis replication group.
    replication_group: "ReplicationGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NodeGroup(ShapeBase):
    """
    Represents a collection of cache nodes in a replication group. One node in the
    node group is the read/write primary node. All the other nodes are read-only
    Replica nodes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "node_group_id",
                "NodeGroupId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "primary_endpoint",
                "PrimaryEndpoint",
                TypeInfo(Endpoint),
            ),
            (
                "slots",
                "Slots",
                TypeInfo(str),
            ),
            (
                "node_group_members",
                "NodeGroupMembers",
                TypeInfo(typing.List[NodeGroupMember]),
            ),
        ]

    # The identifier for the node group (shard). A Redis (cluster mode disabled)
    # replication group contains only 1 node group; therefore, the node group ID
    # is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15
    # node groups numbered 0001 to 0015.
    node_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of this replication group - `creating`, `available`, etc.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint of the primary node in this node group (shard).
    primary_endpoint: "Endpoint" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The keyspace for this node group (shard).
    slots: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list containing information about individual nodes within the node group
    # (shard).
    node_group_members: typing.List["NodeGroupMember"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NodeGroupConfiguration(ShapeBase):
    """
    Node group (shard) configuration options. Each node group (shard) configuration
    has the following: `Slots`, `PrimaryAvailabilityZone`,
    `ReplicaAvailabilityZones`, `ReplicaCount`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "slots",
                "Slots",
                TypeInfo(str),
            ),
            (
                "replica_count",
                "ReplicaCount",
                TypeInfo(int),
            ),
            (
                "primary_availability_zone",
                "PrimaryAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "replica_availability_zones",
                "ReplicaAvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A string that specifies the keyspace for a particular node group. Keyspaces
    # range from 0 to 16,383. The string is in the format `startkey-endkey`.

    # Example: `"0-3999"`
    slots: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of read replica nodes in this node group (shard).
    replica_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone where the primary node of this node group (shard) is
    # launched.
    primary_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of Availability Zones to be used for the read replicas. The number
    # of Availability Zones in this list must match the value of `ReplicaCount`
    # or `ReplicasPerNodeGroup` if not specified.
    replica_availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NodeGroupMember(ShapeBase):
    """
    Represents a single node within a node group (shard).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "cache_node_id",
                "CacheNodeId",
                TypeInfo(str),
            ),
            (
                "read_endpoint",
                "ReadEndpoint",
                TypeInfo(Endpoint),
            ),
            (
                "preferred_availability_zone",
                "PreferredAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "current_role",
                "CurrentRole",
                TypeInfo(str),
            ),
        ]

    # The ID of the cluster to which the node belongs.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the node within its cluster. A node ID is a numeric identifier
    # (0001, 0002, etc.).
    cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the information required for client programs to connect to a
    # cache node.
    read_endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Availability Zone in which the node is located.
    preferred_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The role that is currently assigned to the node - `primary` or `replica`.
    current_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NodeGroupNotFoundFault(ShapeBase):
    """
    The node group specified by the `NodeGroupId` parameter could not be found.
    Please verify that the node group exists and that you spelled the `NodeGroupId`
    value correctly.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeGroupsPerReplicationGroupQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the maximum allowed
    number of node groups (shards) in a single replication group. The default
    maximum is 15
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeQuotaForClusterExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    cache nodes in a single cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeQuotaForCustomerExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the allowed number of
    cache nodes per customer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NodeSnapshot(ShapeBase):
    """
    Represents an individual cache node in a snapshot of a cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "node_group_id",
                "NodeGroupId",
                TypeInfo(str),
            ),
            (
                "cache_node_id",
                "CacheNodeId",
                TypeInfo(str),
            ),
            (
                "node_group_configuration",
                "NodeGroupConfiguration",
                TypeInfo(NodeGroupConfiguration),
            ),
            (
                "cache_size",
                "CacheSize",
                TypeInfo(str),
            ),
            (
                "cache_node_create_time",
                "CacheNodeCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "snapshot_create_time",
                "SnapshotCreateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A unique identifier for the source cluster.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the source node group (shard).
    node_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cache node identifier for the node in the source cluster.
    cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration for the source node group (shard).
    node_group_configuration: "NodeGroupConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the cache on the source cache node.
    cache_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the cache node was created in the source cluster.
    cache_node_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the source node's metadata and cache data set was
    # obtained for the snapshot.
    snapshot_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotificationConfiguration(ShapeBase):
    """
    Describes a notification topic and its status. Notification topics are used for
    publishing ElastiCache events to subscribers using Amazon Simple Notification
    Service (SNS).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "topic_status",
                "TopicStatus",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the topic.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the topic.
    topic_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Parameter(ShapeBase):
    """
    Describes an individual setting that controls some aspect of ElastiCache
    behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                TypeInfo(str),
            ),
            (
                "parameter_value",
                "ParameterValue",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "data_type",
                "DataType",
                TypeInfo(str),
            ),
            (
                "allowed_values",
                "AllowedValues",
                TypeInfo(str),
            ),
            (
                "is_modifiable",
                "IsModifiable",
                TypeInfo(bool),
            ),
            (
                "minimum_engine_version",
                "MinimumEngineVersion",
                TypeInfo(str),
            ),
            (
                "change_type",
                "ChangeType",
                TypeInfo(typing.Union[str, ChangeType]),
            ),
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the parameter.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the parameter.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid data type for the parameter.
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid range of values for the parameter.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether (`true`) or not (`false`) the parameter can be modified.
    # Some parameters have security or operational implications that prevent them
    # from being changed.
    is_modifiable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The earliest cache engine version to which the parameter can apply.
    minimum_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a change to the parameter is applied immediately or
    # requires a reboot for the change to be applied. You can force a reboot or
    # wait until the next maintenance window's reboot. For more information, see
    # [Rebooting a
    # Cluster](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html).
    change_type: typing.Union[str, "ChangeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ParameterNameValue(ShapeBase):
    """
    Describes a name-value pair that is used to update the value of a parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_name",
                "ParameterName",
                TypeInfo(str),
            ),
            (
                "parameter_value",
                "ParameterValue",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the parameter.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PendingAutomaticFailoverStatus(str):
    enabled = "enabled"
    disabled = "disabled"


@dataclasses.dataclass
class PendingModifiedValues(ShapeBase):
    """
    A group of settings that are applied to the cluster in the future, or that are
    currently being applied.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "num_cache_nodes",
                "NumCacheNodes",
                TypeInfo(int),
            ),
            (
                "cache_node_ids_to_remove",
                "CacheNodeIdsToRemove",
                TypeInfo(typing.List[str]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
        ]

    # The new number of cache nodes for the cluster.

    # For clusters running Redis, this value must be 1. For clusters running
    # Memcached, this value must be between 1 and 20.
    num_cache_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache node IDs that are being removed (or will be removed) from
    # the cluster. A node ID is a numeric identifier (0001, 0002, etc.).
    cache_node_ids_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new cache engine version that the cluster runs.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cache node type that this cluster or replication group is scaled to.
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedCacheNodesOfferingMessage(ShapeBase):
    """
    Represents the input of a `PurchaseReservedCacheNodesOffering` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_cache_nodes_offering_id",
                "ReservedCacheNodesOfferingId",
                TypeInfo(str),
            ),
            (
                "reserved_cache_node_id",
                "ReservedCacheNodeId",
                TypeInfo(str),
            ),
            (
                "cache_node_count",
                "CacheNodeCount",
                TypeInfo(int),
            ),
        ]

    # The ID of the reserved cache node offering to purchase.

    # Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`
    reserved_cache_nodes_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A customer-specified identifier to track this reservation.

    # The Reserved Cache Node ID is an unique customer-specified identifier to
    # track this reservation. If this parameter is not specified, ElastiCache
    # automatically generates an identifier for the reservation.

    # Example: myreservationID
    reserved_cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of cache node instances to reserve.

    # Default: `1`
    cache_node_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedCacheNodesOfferingResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "reserved_cache_node",
                "ReservedCacheNode",
                TypeInfo(ReservedCacheNode),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of a `PurchaseReservedCacheNodesOffering` operation.
    reserved_cache_node: "ReservedCacheNode" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootCacheClusterMessage(ShapeBase):
    """
    Represents the input of a `RebootCacheCluster` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "cache_node_ids_to_reboot",
                "CacheNodeIdsToReboot",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The cluster identifier. This parameter is stored as a lowercase string.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cache node IDs to reboot. A node ID is a numeric identifier
    # (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache
    # node IDs.
    cache_node_ids_to_reboot: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootCacheClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_cluster",
                "CacheCluster",
                TypeInfo(CacheCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific cluster.
    cache_cluster: "CacheCluster" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RecurringCharge(ShapeBase):
    """
    Contains the specific price and frequency of a recurring charges for a reserved
    cache node, or for a reserved cache node offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "recurring_charge_amount",
                "RecurringChargeAmount",
                TypeInfo(float),
            ),
            (
                "recurring_charge_frequency",
                "RecurringChargeFrequency",
                TypeInfo(str),
            ),
        ]

    # The monetary amount of the recurring charge.
    recurring_charge_amount: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The frequency of the recurring charge.
    recurring_charge_frequency: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsFromResourceMessage(ShapeBase):
    """
    Represents the input of a `RemoveTagsFromResource` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "ResourceName",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource from which you want the tags
    # removed, for example `arn:aws:elasticache:us-
    # west-2:0123456789:cluster:myCluster` or `arn:aws:elasticache:us-
    # west-2:0123456789:snapshot:mySnapshot`.

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `TagKeys` identifying the tags you want removed from the named
    # resource.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationGroup(ShapeBase):
    """
    Contains all of the attributes of a specific Redis replication group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "pending_modified_values",
                "PendingModifiedValues",
                TypeInfo(ReplicationGroupPendingModifiedValues),
            ),
            (
                "member_clusters",
                "MemberClusters",
                TypeInfo(typing.List[str]),
            ),
            (
                "node_groups",
                "NodeGroups",
                TypeInfo(typing.List[NodeGroup]),
            ),
            (
                "snapshotting_cluster_id",
                "SnapshottingClusterId",
                TypeInfo(str),
            ),
            (
                "automatic_failover",
                "AutomaticFailover",
                TypeInfo(typing.Union[str, AutomaticFailoverStatus]),
            ),
            (
                "configuration_endpoint",
                "ConfigurationEndpoint",
                TypeInfo(Endpoint),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "cluster_enabled",
                "ClusterEnabled",
                TypeInfo(bool),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "auth_token_enabled",
                "AuthTokenEnabled",
                TypeInfo(bool),
            ),
            (
                "transit_encryption_enabled",
                "TransitEncryptionEnabled",
                TypeInfo(bool),
            ),
            (
                "at_rest_encryption_enabled",
                "AtRestEncryptionEnabled",
                TypeInfo(bool),
            ),
        ]

    # The identifier for the replication group.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user supplied description of the replication group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of this replication group - `creating`, `available`,
    # `modifying`, `deleting`, `create-failed`, `snapshotting`.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A group of settings to be applied to the replication group, either
    # immediately or during the next maintenance window.
    pending_modified_values: "ReplicationGroupPendingModifiedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifiers of all the nodes that are part of this replication group.
    member_clusters: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of node groups in this replication group. For Redis (cluster mode
    # disabled) replication groups, this is a single-element list. For Redis
    # (cluster mode enabled) replication groups, the list contains an entry for
    # each node group (shard).
    node_groups: typing.List["NodeGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cluster ID that is used as the daily snapshot source for the
    # replication group.
    snapshotting_cluster_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the status of Multi-AZ with automatic failover for this Redis
    # replication group.

    # Amazon ElastiCache for Redis does not support Multi-AZ with automatic
    # failover on:

    #   * Redis versions earlier than 2.8.6.

    #   * Redis (cluster mode disabled): T1 and T2 cache node types.

    #   * Redis (cluster mode enabled): T1 node types.
    automatic_failover: typing.Union[str, "AutomaticFailoverStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The configuration endpoint for this replication group. Use the
    # configuration endpoint to connect to this replication group.
    configuration_endpoint: "Endpoint" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which ElastiCache retains automatic cluster
    # snapshots before deleting them. For example, if you set
    # `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained
    # for 5 days before being deleted.

    # If the value of `SnapshotRetentionLimit` is set to zero (0), backups are
    # turned off.
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range (in UTC) during which ElastiCache begins taking a
    # daily snapshot of your node group (shard).

    # Example: `05:00-09:00`

    # If you do not specify this parameter, ElastiCache automatically chooses an
    # appropriate time range.

    # This parameter is only valid if the `Engine` parameter is `redis`.
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag indicating whether or not this replication group is cluster enabled;
    # i.e., whether its data can be partitioned across multiple shards (API/CLI:
    # node groups).

    # Valid values: `true` | `false`
    cluster_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the compute and memory capacity node type for each node in the
    # replication group.
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that enables using an `AuthToken` (password) when issuing Redis
    # commands.

    # Default: `false`
    auth_token_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that enables in-transit encryption when set to `true`.

    # You cannot modify the value of `TransitEncryptionEnabled` after the cluster
    # is created. To enable in-transit encryption on a cluster you must set
    # `TransitEncryptionEnabled` to `true` when you create a cluster.

    # Default: `false`
    transit_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that enables encryption at-rest when set to `true`.

    # You cannot modify the value of `AtRestEncryptionEnabled` after the cluster
    # is created. To enable encryption at-rest on a cluster you must set
    # `AtRestEncryptionEnabled` to `true` when you create a cluster.

    # Default: `false`
    at_rest_encryption_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationGroupAlreadyExistsFault(ShapeBase):
    """
    The specified replication group already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReplicationGroupMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeReplicationGroups` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "replication_groups",
                "ReplicationGroups",
                TypeInfo(typing.List[ReplicationGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of replication groups. Each item in the list contains detailed
    # information about one replication group.
    replication_groups: typing.List["ReplicationGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ReplicationGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ReplicationGroupNotFoundFault(ShapeBase):
    """
    The specified replication group does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReplicationGroupPendingModifiedValues(ShapeBase):
    """
    The settings to be applied to the Redis replication group, either immediately or
    during the next maintenance window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "primary_cluster_id",
                "PrimaryClusterId",
                TypeInfo(str),
            ),
            (
                "automatic_failover_status",
                "AutomaticFailoverStatus",
                TypeInfo(typing.Union[str, PendingAutomaticFailoverStatus]),
            ),
            (
                "resharding",
                "Resharding",
                TypeInfo(ReshardingStatus),
            ),
        ]

    # The primary cluster ID that is applied immediately (if `--apply-
    # immediately` was specified), or during the next maintenance window.
    primary_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the status of Multi-AZ with automatic failover for this Redis
    # replication group.

    # Amazon ElastiCache for Redis does not support Multi-AZ with automatic
    # failover on:

    #   * Redis versions earlier than 2.8.6.

    #   * Redis (cluster mode disabled): T1 and T2 cache node types.

    #   * Redis (cluster mode enabled): T1 node types.
    automatic_failover_status: typing.Union[
        str, "PendingAutomaticFailoverStatus"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The status of an online resharding operation.
    resharding: "ReshardingStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedCacheNode(ShapeBase):
    """
    Represents the output of a `PurchaseReservedCacheNodesOffering` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_cache_node_id",
                "ReservedCacheNodeId",
                TypeInfo(str),
            ),
            (
                "reserved_cache_nodes_offering_id",
                "ReservedCacheNodesOfferingId",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
            (
                "cache_node_count",
                "CacheNodeCount",
                TypeInfo(int),
            ),
            (
                "product_description",
                "ProductDescription",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "recurring_charges",
                "RecurringCharges",
                TypeInfo(typing.List[RecurringCharge]),
            ),
        ]

    # The unique identifier for the reservation.
    reserved_cache_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering identifier.
    reserved_cache_nodes_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cache node type for the reserved cache nodes.

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the reservation started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration of the reservation in seconds.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fixed price charged for this reserved cache node.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hourly price charged for this reserved cache node.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of cache nodes that have been reserved.
    cache_node_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the reserved cache node.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type of this reserved cache node.
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the reserved cache node.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring price charged to run this reserved cache node.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedCacheNodeAlreadyExistsFault(ShapeBase):
    """
    You already have a reservation with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedCacheNodeMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeReservedCacheNodes` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "reserved_cache_nodes",
                "ReservedCacheNodes",
                TypeInfo(typing.List[ReservedCacheNode]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of reserved cache nodes. Each element in the list contains detailed
    # information about one node.
    reserved_cache_nodes: typing.List["ReservedCacheNode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ReservedCacheNodeMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ReservedCacheNodeNotFoundFault(ShapeBase):
    """
    The requested reserved cache node was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedCacheNodeQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the user's cache node
    quota.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedCacheNodesOffering(ShapeBase):
    """
    Describes all of the attributes of a reserved cache node offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_cache_nodes_offering_id",
                "ReservedCacheNodesOfferingId",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
            (
                "product_description",
                "ProductDescription",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(str),
            ),
            (
                "recurring_charges",
                "RecurringCharges",
                TypeInfo(typing.List[RecurringCharge]),
            ),
        ]

    # A unique identifier for the reserved cache node offering.
    reserved_cache_nodes_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cache node type for the reserved cache node.

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the offering. in seconds.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fixed price charged for this offering.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hourly price charged for this offering.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cache engine used by the offering.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type.
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring price charged to run this reserved cache node.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedCacheNodesOfferingMessage(OutputShapeBase):
    """
    Represents the output of a `DescribeReservedCacheNodesOfferings` operation.
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
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "reserved_cache_nodes_offerings",
                "ReservedCacheNodesOfferings",
                TypeInfo(typing.List[ReservedCacheNodesOffering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an identifier to allow retrieval of paginated results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of reserved cache node offerings. Each element in the list contains
    # detailed information about one offering.
    reserved_cache_nodes_offerings: typing.List["ReservedCacheNodesOffering"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    def paginate(
        self,
    ) -> typing.Generator["ReservedCacheNodesOfferingMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ReservedCacheNodesOfferingNotFoundFault(ShapeBase):
    """
    The requested cache node offering does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResetCacheParameterGroupMessage(ShapeBase):
    """
    Represents the input of a `ResetCacheParameterGroup` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "reset_all_parameters",
                "ResetAllParameters",
                TypeInfo(bool),
            ),
            (
                "parameter_name_values",
                "ParameterNameValues",
                TypeInfo(typing.List[ParameterNameValue]),
            ),
        ]

    # The name of the cache parameter group to reset.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `true`, all parameters in the cache parameter group are reset to their
    # default values. If `false`, only the parameters listed by
    # `ParameterNameValues` are reset to their default values.

    # Valid values: `true` | `false`
    reset_all_parameters: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of parameter names to reset to their default values. If
    # `ResetAllParameters` is `true`, do not use `ParameterNameValues`. If
    # `ResetAllParameters` is `false`, you must specify the name of at least one
    # parameter to reset.
    parameter_name_values: typing.List["ParameterNameValue"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class ReshardingConfiguration(ShapeBase):
    """
    A list of `PreferredAvailabilityZones` objects that specifies the configuration
    of a node group in the resharded cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "preferred_availability_zones",
                "PreferredAvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of preferred availability zones for the nodes in this cluster.
    preferred_availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReshardingStatus(ShapeBase):
    """
    The status of an online resharding operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "slot_migration",
                "SlotMigration",
                TypeInfo(SlotMigration),
            ),
        ]

    # Represents the progress of an online resharding operation.
    slot_migration: "SlotMigration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeCacheSecurityGroupIngressMessage(ShapeBase):
    """
    Represents the input of a `RevokeCacheSecurityGroupIngress` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cache_security_group_name",
                "CacheSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_name",
                "EC2SecurityGroupName",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_owner_id",
                "EC2SecurityGroupOwnerId",
                TypeInfo(str),
            ),
        ]

    # The name of the cache security group to revoke ingress from.
    cache_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the Amazon EC2 security group to revoke access from.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account number of the Amazon EC2 security group owner. Note that
    # this is not the same thing as an AWS access key ID - you must provide a
    # valid AWS account number for this parameter.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeCacheSecurityGroupIngressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cache_security_group",
                "CacheSecurityGroup",
                TypeInfo(CacheSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of one of the following operations:

    #   * `AuthorizeCacheSecurityGroupIngress`

    #   * `CreateCacheSecurityGroup`

    #   * `RevokeCacheSecurityGroupIngress`
    cache_security_group: "CacheSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SecurityGroupMembership(ShapeBase):
    """
    Represents a single cache security group and its status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group_id",
                "SecurityGroupId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cache security group.
    security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the cache security group membership. The status changes
    # whenever a cache security group is modified, or when the cache security
    # groups assigned to a cluster are modified.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SlotMigration(ShapeBase):
    """
    Represents the progress of an online resharding operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "progress_percentage",
                "ProgressPercentage",
                TypeInfo(float),
            ),
        ]

    # The percentage of the slot migration that is complete.
    progress_percentage: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Snapshot(ShapeBase):
    """
    Represents a copy of an entire Redis cluster as of the time when the snapshot
    was taken.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_name",
                "SnapshotName",
                TypeInfo(str),
            ),
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "replication_group_description",
                "ReplicationGroupDescription",
                TypeInfo(str),
            ),
            (
                "cache_cluster_id",
                "CacheClusterId",
                TypeInfo(str),
            ),
            (
                "snapshot_status",
                "SnapshotStatus",
                TypeInfo(str),
            ),
            (
                "snapshot_source",
                "SnapshotSource",
                TypeInfo(str),
            ),
            (
                "cache_node_type",
                "CacheNodeType",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "num_cache_nodes",
                "NumCacheNodes",
                TypeInfo(int),
            ),
            (
                "preferred_availability_zone",
                "PreferredAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "cache_cluster_create_time",
                "CacheClusterCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "cache_parameter_group_name",
                "CacheParameterGroupName",
                TypeInfo(str),
            ),
            (
                "cache_subnet_group_name",
                "CacheSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "snapshot_retention_limit",
                "SnapshotRetentionLimit",
                TypeInfo(int),
            ),
            (
                "snapshot_window",
                "SnapshotWindow",
                TypeInfo(str),
            ),
            (
                "num_node_groups",
                "NumNodeGroups",
                TypeInfo(int),
            ),
            (
                "automatic_failover",
                "AutomaticFailover",
                TypeInfo(typing.Union[str, AutomaticFailoverStatus]),
            ),
            (
                "node_snapshots",
                "NodeSnapshots",
                TypeInfo(typing.List[NodeSnapshot]),
            ),
        ]

    # The name of a snapshot. For an automatic snapshot, the name is system-
    # generated. For a manual snapshot, this is the user-provided name.
    snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the source replication group.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the source replication group.
    replication_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user-supplied identifier of the source cluster.
    cache_cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the snapshot. Valid values: `creating` | `available` |
    # `restoring` | `copying` | `deleting`.
    snapshot_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the snapshot is from an automatic backup (`automated`) or
    # was created manually (`manual`).
    snapshot_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the compute and memory capacity node type for the source
    # cluster.

    # The following node types are supported by ElastiCache. Generally speaking,
    # the current generation types provide more memory and computational power at
    # lower cost when compared to their equivalent previous generation
    # counterparts.

    #   * General purpose:

    #     * Current generation:

    # **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`

    # **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`,
    # `cache.m3.2xlarge`

    # **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`,
    # `cache.m4.4xlarge`, `cache.m4.10xlarge`

    #     * Previous generation: (not recommended)

    # **T1 node types:** `cache.t1.micro`

    # **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`,
    # `cache.m1.xlarge`

    #   * Compute optimized:

    #     * Previous generation: (not recommended)

    # **C1 node types:** `cache.c1.xlarge`

    #   * Memory optimized:

    #     * Current generation:

    # **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`,
    # `cache.r3.4xlarge`, `cache.r3.8xlarge`

    #     * Previous generation: (not recommended)

    # **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`,
    # `cache.m2.4xlarge`

    # **Notes:**

    #   * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).

    #   * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.

    #   * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances.

    #   * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.

    # For a complete listing of node types and specifications, see [Amazon
    # ElastiCache Product Features and
    # Details](http://aws.amazon.com/elasticache/details) and either [Cache Node
    # Type-Specific Parameters for
    # Memcached](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific)
    # or [Cache Node Type-Specific Parameters for
    # Redis](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific).
    cache_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cache engine (`memcached` or `redis`) used by the source
    # cluster.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the cache engine version that is used by the source cluster.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of cache nodes in the source cluster.

    # For clusters running Redis, this value must be 1. For clusters running
    # Memcached, this value must be between 1 and 20.
    num_cache_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Availability Zone in which the source cluster is located.
    preferred_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the source cluster was created.
    cache_cluster_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which maintenance on the cluster is
    # performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi
    # (24H Clock UTC). The minimum maintenance window is a 60 minute period.

    # Valid values for `ddd` are:

    #   * `sun`

    #   * `mon`

    #   * `tue`

    #   * `wed`

    #   * `thu`

    #   * `fri`

    #   * `sat`

    # Example: `sun:23:00-mon:01:30`
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the topic used by the source cluster for
    # publishing notifications.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number used by each cache nodes in the source cluster.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cache parameter group that is associated with the source cluster.
    cache_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cache subnet group associated with the source cluster.
    cache_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet
    # group for the source cluster.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is currently disabled.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For an automatic snapshot, the number of days for which ElastiCache retains
    # the snapshot before deleting it.

    # For manual snapshots, this field reflects the `SnapshotRetentionLimit` for
    # the source cluster when the snapshot was created. This field is otherwise
    # ignored: Manual snapshots do not expire, and can only be deleted using the
    # `DeleteSnapshot` operation.

    # **Important** If the value of SnapshotRetentionLimit is set to zero (0),
    # backups are turned off.
    snapshot_retention_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range during which ElastiCache takes daily snapshots of the
    # source cluster.
    snapshot_window: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of node groups (shards) in this snapshot. When restoring from a
    # snapshot, the number of node groups (shards) in the snapshot and in the
    # restored replication group must be the same.
    num_node_groups: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the status of Multi-AZ with automatic failover for the source
    # Redis replication group.

    # Amazon ElastiCache for Redis does not support Multi-AZ with automatic
    # failover on:

    #   * Redis versions earlier than 2.8.6.

    #   * Redis (cluster mode disabled): T1 and T2 cache node types.

    #   * Redis (cluster mode enabled): T1 node types.
    automatic_failover: typing.Union[str, "AutomaticFailoverStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # A list of the cache nodes in the source cluster.
    node_snapshots: typing.List["NodeSnapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SnapshotAlreadyExistsFault(ShapeBase):
    """
    You already have a snapshot with the given name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotFeatureNotSupportedFault(ShapeBase):
    """
    You attempted one of the following operations:

      * Creating a snapshot of a Redis cluster running on a `cache.t1.micro` cache node.

      * Creating a snapshot of a cluster that is running Memcached rather than Redis.

    Neither of these are supported by ElastiCache.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotNotFoundFault(ShapeBase):
    """
    The requested snapshot name does not refer to an existing snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotQuotaExceededFault(ShapeBase):
    """
    The request cannot be processed because it would exceed the maximum number of
    snapshots.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class SourceType(str):
    cache_cluster = "cache-cluster"
    cache_parameter_group = "cache-parameter-group"
    cache_security_group = "cache-security-group"
    cache_subnet_group = "cache-subnet-group"
    replication_group = "replication-group"


@dataclasses.dataclass
class Subnet(ShapeBase):
    """
    Represents the subnet associated with a cluster. This parameter refers to
    subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with
    ElastiCache.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_identifier",
                "SubnetIdentifier",
                TypeInfo(str),
            ),
            (
                "subnet_availability_zone",
                "SubnetAvailabilityZone",
                TypeInfo(AvailabilityZone),
            ),
        ]

    # The unique identifier for the subnet.
    subnet_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone associated with the subnet.
    subnet_availability_zone: "AvailabilityZone" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubnetInUse(ShapeBase):
    """
    The requested subnet is being used by another cache subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A cost allocation Tag that can be added to an ElastiCache cluster or replication
    group. Tags are composed of a Key/Value pair. A tag with a null Value is
    permitted.
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

    # The key for the tag. May not be null.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag's value. May be null.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagListMessage(OutputShapeBase):
    """
    Represents the output from the `AddTagsToResource`, `ListTagsForResource`, and
    `RemoveTagsFromResource` operations.
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
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cost allocation tags as key-value pairs.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TagNotFoundFault(ShapeBase):
    """
    The requested tag was not found on this resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TagQuotaPerResourceExceeded(ShapeBase):
    """
    The request cannot be processed because it would cause the resource to have more
    than the allowed number of tags. The maximum number of tags permitted on a
    resource is 50.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TestFailoverMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group_id",
                "ReplicationGroupId",
                TypeInfo(str),
            ),
            (
                "node_group_id",
                "NodeGroupId",
                TypeInfo(str),
            ),
        ]

    # The name of the replication group (console: cluster) whose automatic
    # failover is being tested by this operation.
    replication_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the node group (called shard in the console) in this
    # replication group on which automatic failover is to be tested. You may test
    # automatic failover on up to 5 node groups in any rolling 24-hour period.
    node_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestFailoverNotAvailableFault(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TestFailoverResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(ReplicationGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains all of the attributes of a specific Redis replication group.
    replication_group: "ReplicationGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
