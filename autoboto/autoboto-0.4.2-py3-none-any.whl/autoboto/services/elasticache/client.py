import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("elasticache", *args, **kwargs)

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceMessage = None,
        *,
        resource_name: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagListMessage:
        """
        Adds up to 50 cost allocation tags to the named resource. A cost allocation tag
        is a key-value pair where the key and value are case-sensitive. You can use cost
        allocation tags to categorize and track your AWS costs.

        When you apply tags to your ElastiCache resources, AWS generates a cost
        allocation report as a comma-separated value (CSV) file with your usage and
        costs aggregated by your tags. You can apply tags that represent business
        categories (such as cost centers, application names, or owners) to organize your
        costs across multiple services. For more information, see [Using Cost Allocation
        Tags in Amazon
        ElastiCache](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Tagging.html)
        in the _ElastiCache User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToResourceMessage(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

        return shapes.TagListMessage.from_boto(response)

    def authorize_cache_security_group_ingress(
        self,
        _request: shapes.AuthorizeCacheSecurityGroupIngressMessage = None,
        *,
        cache_security_group_name: str,
        ec2_security_group_name: str,
        ec2_security_group_owner_id: str,
    ) -> shapes.AuthorizeCacheSecurityGroupIngressResult:
        """
        Allows network ingress to a cache security group. Applications using ElastiCache
        must be running on Amazon EC2, and Amazon EC2 security groups are used as the
        authorization mechanism.

        You cannot authorize ingress from an Amazon EC2 security group in one region to
        an ElastiCache cluster in another region.
        """
        if _request is None:
            _params = {}
            if cache_security_group_name is not ShapeBase.NOT_SET:
                _params['cache_security_group_name'] = cache_security_group_name
            if ec2_security_group_name is not ShapeBase.NOT_SET:
                _params['ec2_security_group_name'] = ec2_security_group_name
            if ec2_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_owner_id'
                       ] = ec2_security_group_owner_id
            _request = shapes.AuthorizeCacheSecurityGroupIngressMessage(
                **_params
            )
        response = self._boto_client.authorize_cache_security_group_ingress(
            **_request.to_boto()
        )

        return shapes.AuthorizeCacheSecurityGroupIngressResult.from_boto(
            response
        )

    def copy_snapshot(
        self,
        _request: shapes.CopySnapshotMessage = None,
        *,
        source_snapshot_name: str,
        target_snapshot_name: str,
        target_bucket: str = ShapeBase.NOT_SET,
    ) -> shapes.CopySnapshotResult:
        """
        Makes a copy of an existing snapshot.

        This operation is valid for Redis only.

        Users or groups that have permissions to use the `CopySnapshot` operation can
        create their own Amazon S3 buckets and copy snapshots to it. To control access
        to your snapshots, use an IAM policy to control who has the ability to use the
        `CopySnapshot` operation. For more information about using IAM to control the
        use of ElastiCache operations, see [Exporting
        Snapshots](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html)
        and [Authentication & Access
        Control](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/IAM.html).

        You could receive the following error messages.

        **Error Messages**

          * **Error Message:** The S3 bucket %s is outside of the region.

        **Solution:** Create an Amazon S3 bucket in the same region as your snapshot.
        For more information, see [Step 1: Create an Amazon S3
        Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.CreateBucket)
        in the ElastiCache User Guide.

          * **Error Message:** The S3 bucket %s does not exist.

        **Solution:** Create an Amazon S3 bucket in the same region as your snapshot.
        For more information, see [Step 1: Create an Amazon S3
        Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.CreateBucket)
        in the ElastiCache User Guide.

          * **Error Message:** The S3 bucket %s is not owned by the authenticated user.

        **Solution:** Create an Amazon S3 bucket in the same region as your snapshot.
        For more information, see [Step 1: Create an Amazon S3
        Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.CreateBucket)
        in the ElastiCache User Guide.

          * **Error Message:** The authenticated user does not have sufficient permissions to perform the desired activity.

        **Solution:** Contact your system administrator to get the needed permissions.

          * **Error Message:** The S3 bucket %s already contains an object with key %s.

        **Solution:** Give the `TargetSnapshotName` a new and unique value. If exporting
        a snapshot, you could alternatively create a new Amazon S3 bucket and use this
        same value for `TargetSnapshotName`.

          * **Error Message:** ElastiCache has not been granted READ permissions %s on the S3 Bucket.

        **Solution:** Add List and Read permissions on the bucket. For more information,
        see [Step 2: Grant ElastiCache Access to Your Amazon S3
        Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess)
        in the ElastiCache User Guide.

          * **Error Message:** ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.

        **Solution:** Add Upload/Delete permissions on the bucket. For more information,
        see [Step 2: Grant ElastiCache Access to Your Amazon S3
        Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess)
        in the ElastiCache User Guide.

          * **Error Message:** ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket.

        **Solution:** Add View Permissions on the bucket. For more information, see
        [Step 2: Grant ElastiCache Access to Your Amazon S3
        Bucket](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess)
        in the ElastiCache User Guide.
        """
        if _request is None:
            _params = {}
            if source_snapshot_name is not ShapeBase.NOT_SET:
                _params['source_snapshot_name'] = source_snapshot_name
            if target_snapshot_name is not ShapeBase.NOT_SET:
                _params['target_snapshot_name'] = target_snapshot_name
            if target_bucket is not ShapeBase.NOT_SET:
                _params['target_bucket'] = target_bucket
            _request = shapes.CopySnapshotMessage(**_params)
        response = self._boto_client.copy_snapshot(**_request.to_boto())

        return shapes.CopySnapshotResult.from_boto(response)

    def create_cache_cluster(
        self,
        _request: shapes.CreateCacheClusterMessage = None,
        *,
        cache_cluster_id: str,
        replication_group_id: str = ShapeBase.NOT_SET,
        az_mode: typing.Union[str, shapes.AZMode] = ShapeBase.NOT_SET,
        preferred_availability_zone: str = ShapeBase.NOT_SET,
        preferred_availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        num_cache_nodes: int = ShapeBase.NOT_SET,
        cache_node_type: str = ShapeBase.NOT_SET,
        engine: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        cache_parameter_group_name: str = ShapeBase.NOT_SET,
        cache_subnet_group_name: str = ShapeBase.NOT_SET,
        cache_security_group_names: typing.List[str] = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        snapshot_arns: typing.List[str] = ShapeBase.NOT_SET,
        snapshot_name: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        notification_topic_arn: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        snapshot_retention_limit: int = ShapeBase.NOT_SET,
        snapshot_window: str = ShapeBase.NOT_SET,
        auth_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCacheClusterResult:
        """
        Creates a cluster. All nodes in the cluster run the same protocol-compliant
        cache engine software, either Memcached or Redis.

        Due to current limitations on Redis (cluster mode disabled), this operation or
        parameter is not supported on Redis (cluster mode enabled) replication groups.
        """
        if _request is None:
            _params = {}
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if az_mode is not ShapeBase.NOT_SET:
                _params['az_mode'] = az_mode
            if preferred_availability_zone is not ShapeBase.NOT_SET:
                _params['preferred_availability_zone'
                       ] = preferred_availability_zone
            if preferred_availability_zones is not ShapeBase.NOT_SET:
                _params['preferred_availability_zones'
                       ] = preferred_availability_zones
            if num_cache_nodes is not ShapeBase.NOT_SET:
                _params['num_cache_nodes'] = num_cache_nodes
            if cache_node_type is not ShapeBase.NOT_SET:
                _params['cache_node_type'] = cache_node_type
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if cache_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_name'] = cache_subnet_group_name
            if cache_security_group_names is not ShapeBase.NOT_SET:
                _params['cache_security_group_names'
                       ] = cache_security_group_names
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if snapshot_arns is not ShapeBase.NOT_SET:
                _params['snapshot_arns'] = snapshot_arns
            if snapshot_name is not ShapeBase.NOT_SET:
                _params['snapshot_name'] = snapshot_name
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if notification_topic_arn is not ShapeBase.NOT_SET:
                _params['notification_topic_arn'] = notification_topic_arn
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if snapshot_retention_limit is not ShapeBase.NOT_SET:
                _params['snapshot_retention_limit'] = snapshot_retention_limit
            if snapshot_window is not ShapeBase.NOT_SET:
                _params['snapshot_window'] = snapshot_window
            if auth_token is not ShapeBase.NOT_SET:
                _params['auth_token'] = auth_token
            _request = shapes.CreateCacheClusterMessage(**_params)
        response = self._boto_client.create_cache_cluster(**_request.to_boto())

        return shapes.CreateCacheClusterResult.from_boto(response)

    def create_cache_parameter_group(
        self,
        _request: shapes.CreateCacheParameterGroupMessage = None,
        *,
        cache_parameter_group_name: str,
        cache_parameter_group_family: str,
        description: str,
    ) -> shapes.CreateCacheParameterGroupResult:
        """
        Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache
        parameter group is a collection of parameters and their values that are applied
        to all of the nodes in any cluster or replication group using the
        CacheParameterGroup.

        A newly created CacheParameterGroup is an exact duplicate of the default
        parameter group for the CacheParameterGroupFamily. To customize the newly
        created CacheParameterGroup you can change the values of specific parameters.
        For more information, see:

          * [ModifyCacheParameterGroup](http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html) in the ElastiCache API Reference.

          * [Parameters and Parameter Groups](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/ParameterGroups.html) in the ElastiCache User Guide.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if cache_parameter_group_family is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_family'
                       ] = cache_parameter_group_family
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateCacheParameterGroupMessage(**_params)
        response = self._boto_client.create_cache_parameter_group(
            **_request.to_boto()
        )

        return shapes.CreateCacheParameterGroupResult.from_boto(response)

    def create_cache_security_group(
        self,
        _request: shapes.CreateCacheSecurityGroupMessage = None,
        *,
        cache_security_group_name: str,
        description: str,
    ) -> shapes.CreateCacheSecurityGroupResult:
        """
        Creates a new cache security group. Use a cache security group to control access
        to one or more clusters.

        Cache security groups are only used when you are creating a cluster outside of
        an Amazon Virtual Private Cloud (Amazon VPC). If you are creating a cluster
        inside of a VPC, use a cache subnet group instead. For more information, see
        [CreateCacheSubnetGroup](http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html).
        """
        if _request is None:
            _params = {}
            if cache_security_group_name is not ShapeBase.NOT_SET:
                _params['cache_security_group_name'] = cache_security_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateCacheSecurityGroupMessage(**_params)
        response = self._boto_client.create_cache_security_group(
            **_request.to_boto()
        )

        return shapes.CreateCacheSecurityGroupResult.from_boto(response)

    def create_cache_subnet_group(
        self,
        _request: shapes.CreateCacheSubnetGroupMessage = None,
        *,
        cache_subnet_group_name: str,
        cache_subnet_group_description: str,
        subnet_ids: typing.List[str],
    ) -> shapes.CreateCacheSubnetGroupResult:
        """
        Creates a new cache subnet group.

        Use this parameter only when you are creating a cluster in an Amazon Virtual
        Private Cloud (Amazon VPC).
        """
        if _request is None:
            _params = {}
            if cache_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_name'] = cache_subnet_group_name
            if cache_subnet_group_description is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_description'
                       ] = cache_subnet_group_description
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            _request = shapes.CreateCacheSubnetGroupMessage(**_params)
        response = self._boto_client.create_cache_subnet_group(
            **_request.to_boto()
        )

        return shapes.CreateCacheSubnetGroupResult.from_boto(response)

    def create_replication_group(
        self,
        _request: shapes.CreateReplicationGroupMessage = None,
        *,
        replication_group_id: str,
        replication_group_description: str,
        primary_cluster_id: str = ShapeBase.NOT_SET,
        automatic_failover_enabled: bool = ShapeBase.NOT_SET,
        num_cache_clusters: int = ShapeBase.NOT_SET,
        preferred_cache_cluster_a_zs: typing.List[str] = ShapeBase.NOT_SET,
        num_node_groups: int = ShapeBase.NOT_SET,
        replicas_per_node_group: int = ShapeBase.NOT_SET,
        node_group_configuration: typing.List[shapes.NodeGroupConfiguration
                                             ] = ShapeBase.NOT_SET,
        cache_node_type: str = ShapeBase.NOT_SET,
        engine: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        cache_parameter_group_name: str = ShapeBase.NOT_SET,
        cache_subnet_group_name: str = ShapeBase.NOT_SET,
        cache_security_group_names: typing.List[str] = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        snapshot_arns: typing.List[str] = ShapeBase.NOT_SET,
        snapshot_name: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        notification_topic_arn: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        snapshot_retention_limit: int = ShapeBase.NOT_SET,
        snapshot_window: str = ShapeBase.NOT_SET,
        auth_token: str = ShapeBase.NOT_SET,
        transit_encryption_enabled: bool = ShapeBase.NOT_SET,
        at_rest_encryption_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateReplicationGroupResult:
        """
        Creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled)
        replication group.

        A Redis (cluster mode disabled) replication group is a collection of clusters,
        where one of the clusters is a read/write primary and the others are read-only
        replicas. Writes to the primary are asynchronously propagated to the replicas.

        A Redis (cluster mode enabled) replication group is a collection of 1 to 15 node
        groups (shards). Each node group (shard) has one read/write primary node and up
        to 5 read-only replica nodes. Writes to the primary are asynchronously
        propagated to the replicas. Redis (cluster mode enabled) replication groups
        partition the data across node groups (shards).

        When a Redis (cluster mode disabled) replication group has been successfully
        created, you can add one or more read replicas to it, up to a total of 5 read
        replicas. You cannot alter a Redis (cluster mode enabled) replication group
        after it has been created. However, if you need to increase or decrease the
        number of node groups (console: shards), you can avail yourself of ElastiCache
        for Redis' enhanced backup and restore. For more information, see [Restoring
        From a Backup with Cluster
        Resizing](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/backups-
        restoring.html) in the _ElastiCache User Guide_.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if replication_group_description is not ShapeBase.NOT_SET:
                _params['replication_group_description'
                       ] = replication_group_description
            if primary_cluster_id is not ShapeBase.NOT_SET:
                _params['primary_cluster_id'] = primary_cluster_id
            if automatic_failover_enabled is not ShapeBase.NOT_SET:
                _params['automatic_failover_enabled'
                       ] = automatic_failover_enabled
            if num_cache_clusters is not ShapeBase.NOT_SET:
                _params['num_cache_clusters'] = num_cache_clusters
            if preferred_cache_cluster_a_zs is not ShapeBase.NOT_SET:
                _params['preferred_cache_cluster_a_zs'
                       ] = preferred_cache_cluster_a_zs
            if num_node_groups is not ShapeBase.NOT_SET:
                _params['num_node_groups'] = num_node_groups
            if replicas_per_node_group is not ShapeBase.NOT_SET:
                _params['replicas_per_node_group'] = replicas_per_node_group
            if node_group_configuration is not ShapeBase.NOT_SET:
                _params['node_group_configuration'] = node_group_configuration
            if cache_node_type is not ShapeBase.NOT_SET:
                _params['cache_node_type'] = cache_node_type
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if cache_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_name'] = cache_subnet_group_name
            if cache_security_group_names is not ShapeBase.NOT_SET:
                _params['cache_security_group_names'
                       ] = cache_security_group_names
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if snapshot_arns is not ShapeBase.NOT_SET:
                _params['snapshot_arns'] = snapshot_arns
            if snapshot_name is not ShapeBase.NOT_SET:
                _params['snapshot_name'] = snapshot_name
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if notification_topic_arn is not ShapeBase.NOT_SET:
                _params['notification_topic_arn'] = notification_topic_arn
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if snapshot_retention_limit is not ShapeBase.NOT_SET:
                _params['snapshot_retention_limit'] = snapshot_retention_limit
            if snapshot_window is not ShapeBase.NOT_SET:
                _params['snapshot_window'] = snapshot_window
            if auth_token is not ShapeBase.NOT_SET:
                _params['auth_token'] = auth_token
            if transit_encryption_enabled is not ShapeBase.NOT_SET:
                _params['transit_encryption_enabled'
                       ] = transit_encryption_enabled
            if at_rest_encryption_enabled is not ShapeBase.NOT_SET:
                _params['at_rest_encryption_enabled'
                       ] = at_rest_encryption_enabled
            _request = shapes.CreateReplicationGroupMessage(**_params)
        response = self._boto_client.create_replication_group(
            **_request.to_boto()
        )

        return shapes.CreateReplicationGroupResult.from_boto(response)

    def create_snapshot(
        self,
        _request: shapes.CreateSnapshotMessage = None,
        *,
        snapshot_name: str,
        replication_group_id: str = ShapeBase.NOT_SET,
        cache_cluster_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSnapshotResult:
        """
        Creates a copy of an entire cluster or replication group at a specific moment in
        time.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if snapshot_name is not ShapeBase.NOT_SET:
                _params['snapshot_name'] = snapshot_name
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            _request = shapes.CreateSnapshotMessage(**_params)
        response = self._boto_client.create_snapshot(**_request.to_boto())

        return shapes.CreateSnapshotResult.from_boto(response)

    def delete_cache_cluster(
        self,
        _request: shapes.DeleteCacheClusterMessage = None,
        *,
        cache_cluster_id: str,
        final_snapshot_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteCacheClusterResult:
        """
        Deletes a previously provisioned cluster. `DeleteCacheCluster` deletes all
        associated cache nodes, node endpoints and the cluster itself. When you receive
        a successful response from this operation, Amazon ElastiCache immediately begins
        deleting the cluster; you cannot cancel or revert this operation.

        This operation cannot be used to delete a cluster that is the last read replica
        of a replication group or node group (shard) that has Multi-AZ mode enabled or a
        cluster from a Redis (cluster mode enabled) replication group.

        Due to current limitations on Redis (cluster mode disabled), this operation or
        parameter is not supported on Redis (cluster mode enabled) replication groups.
        """
        if _request is None:
            _params = {}
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if final_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['final_snapshot_identifier'] = final_snapshot_identifier
            _request = shapes.DeleteCacheClusterMessage(**_params)
        response = self._boto_client.delete_cache_cluster(**_request.to_boto())

        return shapes.DeleteCacheClusterResult.from_boto(response)

    def delete_cache_parameter_group(
        self,
        _request: shapes.DeleteCacheParameterGroupMessage = None,
        *,
        cache_parameter_group_name: str,
    ) -> None:
        """
        Deletes the specified cache parameter group. You cannot delete a cache parameter
        group if it is associated with any cache clusters.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            _request = shapes.DeleteCacheParameterGroupMessage(**_params)
        response = self._boto_client.delete_cache_parameter_group(
            **_request.to_boto()
        )

    def delete_cache_security_group(
        self,
        _request: shapes.DeleteCacheSecurityGroupMessage = None,
        *,
        cache_security_group_name: str,
    ) -> None:
        """
        Deletes a cache security group.

        You cannot delete a cache security group if it is associated with any clusters.
        """
        if _request is None:
            _params = {}
            if cache_security_group_name is not ShapeBase.NOT_SET:
                _params['cache_security_group_name'] = cache_security_group_name
            _request = shapes.DeleteCacheSecurityGroupMessage(**_params)
        response = self._boto_client.delete_cache_security_group(
            **_request.to_boto()
        )

    def delete_cache_subnet_group(
        self,
        _request: shapes.DeleteCacheSubnetGroupMessage = None,
        *,
        cache_subnet_group_name: str,
    ) -> None:
        """
        Deletes a cache subnet group.

        You cannot delete a cache subnet group if it is associated with any clusters.
        """
        if _request is None:
            _params = {}
            if cache_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_name'] = cache_subnet_group_name
            _request = shapes.DeleteCacheSubnetGroupMessage(**_params)
        response = self._boto_client.delete_cache_subnet_group(
            **_request.to_boto()
        )

    def delete_replication_group(
        self,
        _request: shapes.DeleteReplicationGroupMessage = None,
        *,
        replication_group_id: str,
        retain_primary_cluster: bool = ShapeBase.NOT_SET,
        final_snapshot_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteReplicationGroupResult:
        """
        Deletes an existing replication group. By default, this operation deletes the
        entire replication group, including the primary/primaries and all of the read
        replicas. If the replication group has only one primary, you can optionally
        delete only the read replicas, while retaining the primary by setting
        `RetainPrimaryCluster=true`.

        When you receive a successful response from this operation, Amazon ElastiCache
        immediately begins deleting the selected resources; you cannot cancel or revert
        this operation.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if retain_primary_cluster is not ShapeBase.NOT_SET:
                _params['retain_primary_cluster'] = retain_primary_cluster
            if final_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['final_snapshot_identifier'] = final_snapshot_identifier
            _request = shapes.DeleteReplicationGroupMessage(**_params)
        response = self._boto_client.delete_replication_group(
            **_request.to_boto()
        )

        return shapes.DeleteReplicationGroupResult.from_boto(response)

    def delete_snapshot(
        self,
        _request: shapes.DeleteSnapshotMessage = None,
        *,
        snapshot_name: str,
    ) -> shapes.DeleteSnapshotResult:
        """
        Deletes an existing snapshot. When you receive a successful response from this
        operation, ElastiCache immediately begins deleting the snapshot; you cannot
        cancel or revert this operation.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if snapshot_name is not ShapeBase.NOT_SET:
                _params['snapshot_name'] = snapshot_name
            _request = shapes.DeleteSnapshotMessage(**_params)
        response = self._boto_client.delete_snapshot(**_request.to_boto())

        return shapes.DeleteSnapshotResult.from_boto(response)

    def describe_cache_clusters(
        self,
        _request: shapes.DescribeCacheClustersMessage = None,
        *,
        cache_cluster_id: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        show_cache_node_info: bool = ShapeBase.NOT_SET,
        show_cache_clusters_not_in_replication_groups: bool = ShapeBase.NOT_SET,
    ) -> shapes.CacheClusterMessage:
        """
        Returns information about all provisioned clusters if no cluster identifier is
        specified, or about a specific cache cluster if a cluster identifier is
        supplied.

        By default, abbreviated information about the clusters is returned. You can use
        the optional _ShowCacheNodeInfo_ flag to retrieve detailed information about the
        cache nodes associated with the clusters. These details include the DNS address
        and port for the cache node endpoint.

        If the cluster is in the _creating_ state, only cluster-level information is
        displayed until all of the nodes are successfully provisioned.

        If the cluster is in the _deleting_ state, only cluster-level information is
        displayed.

        If cache nodes are currently being added to the cluster, node endpoint
        information and creation time for the additional nodes are not displayed until
        they are completely provisioned. When the cluster state is _available_ , the
        cluster is ready for use.

        If cache nodes are currently being removed from the cluster, no endpoint
        information for the removed nodes is displayed.
        """
        if _request is None:
            _params = {}
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if show_cache_node_info is not ShapeBase.NOT_SET:
                _params['show_cache_node_info'] = show_cache_node_info
            if show_cache_clusters_not_in_replication_groups is not ShapeBase.NOT_SET:
                _params['show_cache_clusters_not_in_replication_groups'
                       ] = show_cache_clusters_not_in_replication_groups
            _request = shapes.DescribeCacheClustersMessage(**_params)
        paginator = self.get_paginator("describe_cache_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.CacheClusterMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.CacheClusterMessage.from_boto(response)

    def describe_cache_engine_versions(
        self,
        _request: shapes.DescribeCacheEngineVersionsMessage = None,
        *,
        engine: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        cache_parameter_group_family: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        default_only: bool = ShapeBase.NOT_SET,
    ) -> shapes.CacheEngineVersionMessage:
        """
        Returns a list of the available cache engines and their versions.
        """
        if _request is None:
            _params = {}
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if cache_parameter_group_family is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_family'
                       ] = cache_parameter_group_family
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if default_only is not ShapeBase.NOT_SET:
                _params['default_only'] = default_only
            _request = shapes.DescribeCacheEngineVersionsMessage(**_params)
        paginator = self.get_paginator("describe_cache_engine_versions"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.CacheEngineVersionMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.CacheEngineVersionMessage.from_boto(response)

    def describe_cache_parameter_groups(
        self,
        _request: shapes.DescribeCacheParameterGroupsMessage = None,
        *,
        cache_parameter_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.CacheParameterGroupsMessage:
        """
        Returns a list of cache parameter group descriptions. If a cache parameter group
        name is specified, the list contains only the descriptions for that group.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCacheParameterGroupsMessage(**_params)
        paginator = self.get_paginator("describe_cache_parameter_groups"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.CacheParameterGroupsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.CacheParameterGroupsMessage.from_boto(response)

    def describe_cache_parameters(
        self,
        _request: shapes.DescribeCacheParametersMessage = None,
        *,
        cache_parameter_group_name: str,
        source: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.CacheParameterGroupDetails:
        """
        Returns the detailed parameter list for a particular cache parameter group.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCacheParametersMessage(**_params)
        paginator = self.get_paginator("describe_cache_parameters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.CacheParameterGroupDetails.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.CacheParameterGroupDetails.from_boto(response)

    def describe_cache_security_groups(
        self,
        _request: shapes.DescribeCacheSecurityGroupsMessage = None,
        *,
        cache_security_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.CacheSecurityGroupMessage:
        """
        Returns a list of cache security group descriptions. If a cache security group
        name is specified, the list contains only the description of that group.
        """
        if _request is None:
            _params = {}
            if cache_security_group_name is not ShapeBase.NOT_SET:
                _params['cache_security_group_name'] = cache_security_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCacheSecurityGroupsMessage(**_params)
        paginator = self.get_paginator("describe_cache_security_groups"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.CacheSecurityGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.CacheSecurityGroupMessage.from_boto(response)

    def describe_cache_subnet_groups(
        self,
        _request: shapes.DescribeCacheSubnetGroupsMessage = None,
        *,
        cache_subnet_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.CacheSubnetGroupMessage:
        """
        Returns a list of cache subnet group descriptions. If a subnet group name is
        specified, the list contains only the description of that group.
        """
        if _request is None:
            _params = {}
            if cache_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_name'] = cache_subnet_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCacheSubnetGroupsMessage(**_params)
        paginator = self.get_paginator("describe_cache_subnet_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.CacheSubnetGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.CacheSubnetGroupMessage.from_boto(response)

    def describe_engine_default_parameters(
        self,
        _request: shapes.DescribeEngineDefaultParametersMessage = None,
        *,
        cache_parameter_group_family: str,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEngineDefaultParametersResult:
        """
        Returns the default engine and system parameter information for the specified
        cache engine.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_family is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_family'
                       ] = cache_parameter_group_family
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEngineDefaultParametersMessage(**_params)
        paginator = self.get_paginator("describe_engine_default_parameters"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEngineDefaultParametersResult.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEngineDefaultParametersResult.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsMessage = None,
        *,
        source_identifier: str = ShapeBase.NOT_SET,
        source_type: typing.Union[str, shapes.SourceType] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        duration: int = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.EventsMessage:
        """
        Returns events related to clusters, cache security groups, and cache parameter
        groups. You can obtain events specific to a particular cluster, cache security
        group, or cache parameter group by providing the name as a parameter.

        By default, only the events occurring within the last hour are returned;
        however, you can retrieve up to 14 days' worth of events if necessary.
        """
        if _request is None:
            _params = {}
            if source_identifier is not ShapeBase.NOT_SET:
                _params['source_identifier'] = source_identifier
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEventsMessage(**_params)
        paginator = self.get_paginator("describe_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.EventsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.EventsMessage.from_boto(response)

    def describe_replication_groups(
        self,
        _request: shapes.DescribeReplicationGroupsMessage = None,
        *,
        replication_group_id: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReplicationGroupMessage:
        """
        Returns information about a particular replication group. If no identifier is
        specified, `DescribeReplicationGroups` returns information about all replication
        groups.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReplicationGroupsMessage(**_params)
        paginator = self.get_paginator("describe_replication_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReplicationGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReplicationGroupMessage.from_boto(response)

    def describe_reserved_cache_nodes(
        self,
        _request: shapes.DescribeReservedCacheNodesMessage = None,
        *,
        reserved_cache_node_id: str = ShapeBase.NOT_SET,
        reserved_cache_nodes_offering_id: str = ShapeBase.NOT_SET,
        cache_node_type: str = ShapeBase.NOT_SET,
        duration: str = ShapeBase.NOT_SET,
        product_description: str = ShapeBase.NOT_SET,
        offering_type: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReservedCacheNodeMessage:
        """
        Returns information about reserved cache nodes for this account, or about a
        specified reserved cache node.
        """
        if _request is None:
            _params = {}
            if reserved_cache_node_id is not ShapeBase.NOT_SET:
                _params['reserved_cache_node_id'] = reserved_cache_node_id
            if reserved_cache_nodes_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_cache_nodes_offering_id'
                       ] = reserved_cache_nodes_offering_id
            if cache_node_type is not ShapeBase.NOT_SET:
                _params['cache_node_type'] = cache_node_type
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if product_description is not ShapeBase.NOT_SET:
                _params['product_description'] = product_description
            if offering_type is not ShapeBase.NOT_SET:
                _params['offering_type'] = offering_type
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReservedCacheNodesMessage(**_params)
        paginator = self.get_paginator("describe_reserved_cache_nodes"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReservedCacheNodeMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReservedCacheNodeMessage.from_boto(response)

    def describe_reserved_cache_nodes_offerings(
        self,
        _request: shapes.DescribeReservedCacheNodesOfferingsMessage = None,
        *,
        reserved_cache_nodes_offering_id: str = ShapeBase.NOT_SET,
        cache_node_type: str = ShapeBase.NOT_SET,
        duration: str = ShapeBase.NOT_SET,
        product_description: str = ShapeBase.NOT_SET,
        offering_type: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReservedCacheNodesOfferingMessage:
        """
        Lists available reserved cache node offerings.
        """
        if _request is None:
            _params = {}
            if reserved_cache_nodes_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_cache_nodes_offering_id'
                       ] = reserved_cache_nodes_offering_id
            if cache_node_type is not ShapeBase.NOT_SET:
                _params['cache_node_type'] = cache_node_type
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if product_description is not ShapeBase.NOT_SET:
                _params['product_description'] = product_description
            if offering_type is not ShapeBase.NOT_SET:
                _params['offering_type'] = offering_type
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReservedCacheNodesOfferingsMessage(
                **_params
            )
        paginator = self.get_paginator(
            "describe_reserved_cache_nodes_offerings"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReservedCacheNodesOfferingMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReservedCacheNodesOfferingMessage.from_boto(response)

    def describe_snapshots(
        self,
        _request: shapes.DescribeSnapshotsMessage = None,
        *,
        replication_group_id: str = ShapeBase.NOT_SET,
        cache_cluster_id: str = ShapeBase.NOT_SET,
        snapshot_name: str = ShapeBase.NOT_SET,
        snapshot_source: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        show_node_group_config: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSnapshotsListMessage:
        """
        Returns information about cluster or replication group snapshots. By default,
        `DescribeSnapshots` lists all of your snapshots; it can optionally describe a
        single snapshot, or just the snapshots associated with a particular cache
        cluster.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if snapshot_name is not ShapeBase.NOT_SET:
                _params['snapshot_name'] = snapshot_name
            if snapshot_source is not ShapeBase.NOT_SET:
                _params['snapshot_source'] = snapshot_source
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if show_node_group_config is not ShapeBase.NOT_SET:
                _params['show_node_group_config'] = show_node_group_config
            _request = shapes.DescribeSnapshotsMessage(**_params)
        paginator = self.get_paginator("describe_snapshots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSnapshotsListMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSnapshotsListMessage.from_boto(response)

    def list_allowed_node_type_modifications(
        self,
        _request: shapes.ListAllowedNodeTypeModificationsMessage = None,
        *,
        cache_cluster_id: str = ShapeBase.NOT_SET,
        replication_group_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AllowedNodeTypeModificationsMessage:
        """
        Lists all available node types that you can scale your Redis cluster's or
        replication group's current node type up to.

        When you use the `ModifyCacheCluster` or `ModifyReplicationGroup` operations to
        scale up your cluster or replication group, the value of the `CacheNodeType`
        parameter must be one of the node types returned by this operation.
        """
        if _request is None:
            _params = {}
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            _request = shapes.ListAllowedNodeTypeModificationsMessage(**_params)
        response = self._boto_client.list_allowed_node_type_modifications(
            **_request.to_boto()
        )

        return shapes.AllowedNodeTypeModificationsMessage.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceMessage = None,
        *,
        resource_name: str,
    ) -> shapes.TagListMessage:
        """
        Lists all cost allocation tags currently on the named resource. A `cost
        allocation tag` is a key-value pair where the key is case-sensitive and the
        value is optional. You can use cost allocation tags to categorize and track your
        AWS costs.

        You can have a maximum of 50 cost allocation tags on an ElastiCache resource.
        For more information, see [Using Cost Allocation Tags in Amazon
        ElastiCache](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html).
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            _request = shapes.ListTagsForResourceMessage(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.TagListMessage.from_boto(response)

    def modify_cache_cluster(
        self,
        _request: shapes.ModifyCacheClusterMessage = None,
        *,
        cache_cluster_id: str,
        num_cache_nodes: int = ShapeBase.NOT_SET,
        cache_node_ids_to_remove: typing.List[str] = ShapeBase.NOT_SET,
        az_mode: typing.Union[str, shapes.AZMode] = ShapeBase.NOT_SET,
        new_availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        cache_security_group_names: typing.List[str] = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        notification_topic_arn: str = ShapeBase.NOT_SET,
        cache_parameter_group_name: str = ShapeBase.NOT_SET,
        notification_topic_status: str = ShapeBase.NOT_SET,
        apply_immediately: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        snapshot_retention_limit: int = ShapeBase.NOT_SET,
        snapshot_window: str = ShapeBase.NOT_SET,
        cache_node_type: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyCacheClusterResult:
        """
        Modifies the settings for a cluster. You can use this operation to change one or
        more cluster configuration parameters by specifying the parameters and the new
        values.
        """
        if _request is None:
            _params = {}
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if num_cache_nodes is not ShapeBase.NOT_SET:
                _params['num_cache_nodes'] = num_cache_nodes
            if cache_node_ids_to_remove is not ShapeBase.NOT_SET:
                _params['cache_node_ids_to_remove'] = cache_node_ids_to_remove
            if az_mode is not ShapeBase.NOT_SET:
                _params['az_mode'] = az_mode
            if new_availability_zones is not ShapeBase.NOT_SET:
                _params['new_availability_zones'] = new_availability_zones
            if cache_security_group_names is not ShapeBase.NOT_SET:
                _params['cache_security_group_names'
                       ] = cache_security_group_names
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if notification_topic_arn is not ShapeBase.NOT_SET:
                _params['notification_topic_arn'] = notification_topic_arn
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if notification_topic_status is not ShapeBase.NOT_SET:
                _params['notification_topic_status'] = notification_topic_status
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if snapshot_retention_limit is not ShapeBase.NOT_SET:
                _params['snapshot_retention_limit'] = snapshot_retention_limit
            if snapshot_window is not ShapeBase.NOT_SET:
                _params['snapshot_window'] = snapshot_window
            if cache_node_type is not ShapeBase.NOT_SET:
                _params['cache_node_type'] = cache_node_type
            _request = shapes.ModifyCacheClusterMessage(**_params)
        response = self._boto_client.modify_cache_cluster(**_request.to_boto())

        return shapes.ModifyCacheClusterResult.from_boto(response)

    def modify_cache_parameter_group(
        self,
        _request: shapes.ModifyCacheParameterGroupMessage = None,
        *,
        cache_parameter_group_name: str,
        parameter_name_values: typing.List[shapes.ParameterNameValue],
    ) -> shapes.CacheParameterGroupNameMessage:
        """
        Modifies the parameters of a cache parameter group. You can modify up to 20
        parameters in a single request by submitting a list parameter name and value
        pairs.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if parameter_name_values is not ShapeBase.NOT_SET:
                _params['parameter_name_values'] = parameter_name_values
            _request = shapes.ModifyCacheParameterGroupMessage(**_params)
        response = self._boto_client.modify_cache_parameter_group(
            **_request.to_boto()
        )

        return shapes.CacheParameterGroupNameMessage.from_boto(response)

    def modify_cache_subnet_group(
        self,
        _request: shapes.ModifyCacheSubnetGroupMessage = None,
        *,
        cache_subnet_group_name: str,
        cache_subnet_group_description: str = ShapeBase.NOT_SET,
        subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyCacheSubnetGroupResult:
        """
        Modifies an existing cache subnet group.
        """
        if _request is None:
            _params = {}
            if cache_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_name'] = cache_subnet_group_name
            if cache_subnet_group_description is not ShapeBase.NOT_SET:
                _params['cache_subnet_group_description'
                       ] = cache_subnet_group_description
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            _request = shapes.ModifyCacheSubnetGroupMessage(**_params)
        response = self._boto_client.modify_cache_subnet_group(
            **_request.to_boto()
        )

        return shapes.ModifyCacheSubnetGroupResult.from_boto(response)

    def modify_replication_group(
        self,
        _request: shapes.ModifyReplicationGroupMessage = None,
        *,
        replication_group_id: str,
        replication_group_description: str = ShapeBase.NOT_SET,
        primary_cluster_id: str = ShapeBase.NOT_SET,
        snapshotting_cluster_id: str = ShapeBase.NOT_SET,
        automatic_failover_enabled: bool = ShapeBase.NOT_SET,
        cache_security_group_names: typing.List[str] = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        notification_topic_arn: str = ShapeBase.NOT_SET,
        cache_parameter_group_name: str = ShapeBase.NOT_SET,
        notification_topic_status: str = ShapeBase.NOT_SET,
        apply_immediately: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        snapshot_retention_limit: int = ShapeBase.NOT_SET,
        snapshot_window: str = ShapeBase.NOT_SET,
        cache_node_type: str = ShapeBase.NOT_SET,
        node_group_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyReplicationGroupResult:
        """
        Modifies the settings for a replication group.

        Due to current limitations on Redis (cluster mode disabled), this operation or
        parameter is not supported on Redis (cluster mode enabled) replication groups.

        This operation is valid for Redis only.
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if replication_group_description is not ShapeBase.NOT_SET:
                _params['replication_group_description'
                       ] = replication_group_description
            if primary_cluster_id is not ShapeBase.NOT_SET:
                _params['primary_cluster_id'] = primary_cluster_id
            if snapshotting_cluster_id is not ShapeBase.NOT_SET:
                _params['snapshotting_cluster_id'] = snapshotting_cluster_id
            if automatic_failover_enabled is not ShapeBase.NOT_SET:
                _params['automatic_failover_enabled'
                       ] = automatic_failover_enabled
            if cache_security_group_names is not ShapeBase.NOT_SET:
                _params['cache_security_group_names'
                       ] = cache_security_group_names
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if notification_topic_arn is not ShapeBase.NOT_SET:
                _params['notification_topic_arn'] = notification_topic_arn
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if notification_topic_status is not ShapeBase.NOT_SET:
                _params['notification_topic_status'] = notification_topic_status
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if snapshot_retention_limit is not ShapeBase.NOT_SET:
                _params['snapshot_retention_limit'] = snapshot_retention_limit
            if snapshot_window is not ShapeBase.NOT_SET:
                _params['snapshot_window'] = snapshot_window
            if cache_node_type is not ShapeBase.NOT_SET:
                _params['cache_node_type'] = cache_node_type
            if node_group_id is not ShapeBase.NOT_SET:
                _params['node_group_id'] = node_group_id
            _request = shapes.ModifyReplicationGroupMessage(**_params)
        response = self._boto_client.modify_replication_group(
            **_request.to_boto()
        )

        return shapes.ModifyReplicationGroupResult.from_boto(response)

    def modify_replication_group_shard_configuration(
        self,
        _request: shapes.ModifyReplicationGroupShardConfigurationMessage = None,
        *,
        replication_group_id: str,
        node_group_count: int,
        apply_immediately: bool,
        resharding_configuration: typing.List[shapes.ReshardingConfiguration
                                             ] = ShapeBase.NOT_SET,
        node_groups_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyReplicationGroupShardConfigurationResult:
        """
        Performs horizontal scaling on a Redis (cluster mode enabled) cluster with no
        downtime. Requires Redis engine version 3.2.10 or newer. For information on
        upgrading your engine to a newer version, see [Upgrading Engine
        Versions](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/VersionManagement.html)
        in the Amazon ElastiCache User Guide.

        For more information on ElastiCache for Redis online horizontal scaling, see
        [ElastiCache for Redis Horizontal
        Scaling](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/redis-
        cluster-resharding-online.html)
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if node_group_count is not ShapeBase.NOT_SET:
                _params['node_group_count'] = node_group_count
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            if resharding_configuration is not ShapeBase.NOT_SET:
                _params['resharding_configuration'] = resharding_configuration
            if node_groups_to_remove is not ShapeBase.NOT_SET:
                _params['node_groups_to_remove'] = node_groups_to_remove
            _request = shapes.ModifyReplicationGroupShardConfigurationMessage(
                **_params
            )
        response = self._boto_client.modify_replication_group_shard_configuration(
            **_request.to_boto()
        )

        return shapes.ModifyReplicationGroupShardConfigurationResult.from_boto(
            response
        )

    def purchase_reserved_cache_nodes_offering(
        self,
        _request: shapes.PurchaseReservedCacheNodesOfferingMessage = None,
        *,
        reserved_cache_nodes_offering_id: str,
        reserved_cache_node_id: str = ShapeBase.NOT_SET,
        cache_node_count: int = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseReservedCacheNodesOfferingResult:
        """
        Allows you to purchase a reserved cache node offering.
        """
        if _request is None:
            _params = {}
            if reserved_cache_nodes_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_cache_nodes_offering_id'
                       ] = reserved_cache_nodes_offering_id
            if reserved_cache_node_id is not ShapeBase.NOT_SET:
                _params['reserved_cache_node_id'] = reserved_cache_node_id
            if cache_node_count is not ShapeBase.NOT_SET:
                _params['cache_node_count'] = cache_node_count
            _request = shapes.PurchaseReservedCacheNodesOfferingMessage(
                **_params
            )
        response = self._boto_client.purchase_reserved_cache_nodes_offering(
            **_request.to_boto()
        )

        return shapes.PurchaseReservedCacheNodesOfferingResult.from_boto(
            response
        )

    def reboot_cache_cluster(
        self,
        _request: shapes.RebootCacheClusterMessage = None,
        *,
        cache_cluster_id: str,
        cache_node_ids_to_reboot: typing.List[str],
    ) -> shapes.RebootCacheClusterResult:
        """
        Reboots some, or all, of the cache nodes within a provisioned cluster. This
        operation applies any modified cache parameter groups to the cluster. The reboot
        operation takes place as soon as possible, and results in a momentary outage to
        the cluster. During the reboot, the cluster status is set to REBOOTING.

        The reboot causes the contents of the cache (for each cache node being rebooted)
        to be lost.

        When the reboot is complete, a cluster event is created.

        Rebooting a cluster is currently supported on Memcached and Redis (cluster mode
        disabled) clusters. Rebooting is not supported on Redis (cluster mode enabled)
        clusters.

        If you make changes to parameters that require a Redis (cluster mode enabled)
        cluster reboot for the changes to be applied, see [Rebooting a
        Cluster](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.htm)
        for an alternate process.
        """
        if _request is None:
            _params = {}
            if cache_cluster_id is not ShapeBase.NOT_SET:
                _params['cache_cluster_id'] = cache_cluster_id
            if cache_node_ids_to_reboot is not ShapeBase.NOT_SET:
                _params['cache_node_ids_to_reboot'] = cache_node_ids_to_reboot
            _request = shapes.RebootCacheClusterMessage(**_params)
        response = self._boto_client.reboot_cache_cluster(**_request.to_boto())

        return shapes.RebootCacheClusterResult.from_boto(response)

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceMessage = None,
        *,
        resource_name: str,
        tag_keys: typing.List[str],
    ) -> shapes.TagListMessage:
        """
        Removes the tags identified by the `TagKeys` list from the named resource.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsFromResourceMessage(**_params)
        response = self._boto_client.remove_tags_from_resource(
            **_request.to_boto()
        )

        return shapes.TagListMessage.from_boto(response)

    def reset_cache_parameter_group(
        self,
        _request: shapes.ResetCacheParameterGroupMessage = None,
        *,
        cache_parameter_group_name: str,
        reset_all_parameters: bool = ShapeBase.NOT_SET,
        parameter_name_values: typing.List[shapes.ParameterNameValue
                                          ] = ShapeBase.NOT_SET,
    ) -> shapes.CacheParameterGroupNameMessage:
        """
        Modifies the parameters of a cache parameter group to the engine or system
        default value. You can reset specific parameters by submitting a list of
        parameter names. To reset the entire cache parameter group, specify the
        `ResetAllParameters` and `CacheParameterGroupName` parameters.
        """
        if _request is None:
            _params = {}
            if cache_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cache_parameter_group_name'
                       ] = cache_parameter_group_name
            if reset_all_parameters is not ShapeBase.NOT_SET:
                _params['reset_all_parameters'] = reset_all_parameters
            if parameter_name_values is not ShapeBase.NOT_SET:
                _params['parameter_name_values'] = parameter_name_values
            _request = shapes.ResetCacheParameterGroupMessage(**_params)
        response = self._boto_client.reset_cache_parameter_group(
            **_request.to_boto()
        )

        return shapes.CacheParameterGroupNameMessage.from_boto(response)

    def revoke_cache_security_group_ingress(
        self,
        _request: shapes.RevokeCacheSecurityGroupIngressMessage = None,
        *,
        cache_security_group_name: str,
        ec2_security_group_name: str,
        ec2_security_group_owner_id: str,
    ) -> shapes.RevokeCacheSecurityGroupIngressResult:
        """
        Revokes ingress from a cache security group. Use this operation to disallow
        access from an Amazon EC2 security group that had been previously authorized.
        """
        if _request is None:
            _params = {}
            if cache_security_group_name is not ShapeBase.NOT_SET:
                _params['cache_security_group_name'] = cache_security_group_name
            if ec2_security_group_name is not ShapeBase.NOT_SET:
                _params['ec2_security_group_name'] = ec2_security_group_name
            if ec2_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_owner_id'
                       ] = ec2_security_group_owner_id
            _request = shapes.RevokeCacheSecurityGroupIngressMessage(**_params)
        response = self._boto_client.revoke_cache_security_group_ingress(
            **_request.to_boto()
        )

        return shapes.RevokeCacheSecurityGroupIngressResult.from_boto(response)

    def test_failover(
        self,
        _request: shapes.TestFailoverMessage = None,
        *,
        replication_group_id: str,
        node_group_id: str,
    ) -> shapes.TestFailoverResult:
        """
        Represents the input of a `TestFailover` operation which test automatic failover
        on a specified node group (called shard in the console) in a replication group
        (called cluster in the console).

        **Note the following**

          * A customer can use this operation to test automatic failover on up to 5 shards (called node groups in the ElastiCache API and AWS CLI) in any rolling 24-hour period.

          * If calling this operation on shards in different clusters (called replication groups in the API and CLI), the calls can be made concurrently.

          * If calling this operation multiple times on different shards in the same Redis (cluster mode enabled) replication group, the first node replacement must complete before a subsequent call can be made.

          * To determine whether the node replacement is complete you can check Events using the Amazon ElastiCache console, the AWS CLI, or the ElastiCache API. Look for the following automatic failover related events, listed here in order of occurrance:

            1. Replication group message: `Test Failover API called for node group <node-group-id>`

            2. Cache cluster message: `Failover from master node <primary-node-id> to replica node <node-id> completed`

            3. Replication group message: `Failover from master node <primary-node-id> to replica node <node-id> completed`

            4. Cache cluster message: `Recovering cache nodes <node-id>`

            5. Cache cluster message: `Finished recovery for cache nodes <node-id>`

        For more information see:

            * [Viewing ElastiCache Events](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/ECEvents.Viewing.html) in the _ElastiCache User Guide_

            * [DescribeEvents](http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEvents.html) in the ElastiCache API Reference

        Also see, [Testing Multi-AZ with Automatic
        Failover](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/AutoFailover.html#auto-
        failover-test) in the _ElastiCache User Guide_.
        """
        if _request is None:
            _params = {}
            if replication_group_id is not ShapeBase.NOT_SET:
                _params['replication_group_id'] = replication_group_id
            if node_group_id is not ShapeBase.NOT_SET:
                _params['node_group_id'] = node_group_id
            _request = shapes.TestFailoverMessage(**_params)
        response = self._boto_client.test_failover(**_request.to_boto())

        return shapes.TestFailoverResult.from_boto(response)
