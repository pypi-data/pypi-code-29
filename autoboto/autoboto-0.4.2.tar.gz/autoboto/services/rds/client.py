import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("rds", *args, **kwargs)

    def add_role_to_db_cluster(
        self,
        _request: shapes.AddRoleToDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
        role_arn: str,
    ) -> None:
        """
        Associates an Identity and Access Management (IAM) role from an Aurora DB
        cluster. For more information, see [Authorizing Amazon Aurora MySQL to Access
        Other AWS Services on Your
        Behalf](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.html)
        in the _Amazon Aurora User Guide_.
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.AddRoleToDBClusterMessage(**_params)
        response = self._boto_client.add_role_to_db_cluster(
            **_request.to_boto()
        )

    def add_source_identifier_to_subscription(
        self,
        _request: shapes.AddSourceIdentifierToSubscriptionMessage = None,
        *,
        subscription_name: str,
        source_identifier: str,
    ) -> shapes.AddSourceIdentifierToSubscriptionResult:
        """
        Adds a source identifier to an existing RDS event notification subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if source_identifier is not ShapeBase.NOT_SET:
                _params['source_identifier'] = source_identifier
            _request = shapes.AddSourceIdentifierToSubscriptionMessage(
                **_params
            )
        response = self._boto_client.add_source_identifier_to_subscription(
            **_request.to_boto()
        )

        return shapes.AddSourceIdentifierToSubscriptionResult.from_boto(
            response
        )

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceMessage = None,
        *,
        resource_name: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Adds metadata tags to an Amazon RDS resource. These tags can also be used with
        cost allocation reporting to track cost associated with Amazon RDS resources, or
        used in a Condition statement in an IAM policy for Amazon RDS.

        For an overview on tagging Amazon RDS resources, see [Tagging Amazon RDS
        Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Tagging.html).
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToResourceMessage(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

    def apply_pending_maintenance_action(
        self,
        _request: shapes.ApplyPendingMaintenanceActionMessage = None,
        *,
        resource_identifier: str,
        apply_action: str,
        opt_in_type: str,
    ) -> shapes.ApplyPendingMaintenanceActionResult:
        """
        Applies a pending maintenance action to a resource (for example, to a DB
        instance).
        """
        if _request is None:
            _params = {}
            if resource_identifier is not ShapeBase.NOT_SET:
                _params['resource_identifier'] = resource_identifier
            if apply_action is not ShapeBase.NOT_SET:
                _params['apply_action'] = apply_action
            if opt_in_type is not ShapeBase.NOT_SET:
                _params['opt_in_type'] = opt_in_type
            _request = shapes.ApplyPendingMaintenanceActionMessage(**_params)
        response = self._boto_client.apply_pending_maintenance_action(
            **_request.to_boto()
        )

        return shapes.ApplyPendingMaintenanceActionResult.from_boto(response)

    def authorize_db_security_group_ingress(
        self,
        _request: shapes.AuthorizeDBSecurityGroupIngressMessage = None,
        *,
        db_security_group_name: str,
        cidrip: str = ShapeBase.NOT_SET,
        ec2_security_group_name: str = ShapeBase.NOT_SET,
        ec2_security_group_id: str = ShapeBase.NOT_SET,
        ec2_security_group_owner_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AuthorizeDBSecurityGroupIngressResult:
        """
        Enables ingress to a DBSecurityGroup using one of two forms of authorization.
        First, EC2 or VPC security groups can be added to the DBSecurityGroup if the
        application using the database is running on EC2 or VPC instances. Second, IP
        ranges are available if the application accessing your database is running on
        the Internet. Required parameters for this API are one of CIDR range,
        EC2SecurityGroupId for VPC, or (EC2SecurityGroupOwnerId and either
        EC2SecurityGroupName or EC2SecurityGroupId for non-VPC).

        You can't authorize ingress from an EC2 security group in one AWS Region to an
        Amazon RDS DB instance in another. You can't authorize ingress from a VPC
        security group in one VPC to an Amazon RDS DB instance in another.

        For an overview of CIDR ranges, go to the [Wikipedia
        Tutorial](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
        """
        if _request is None:
            _params = {}
            if db_security_group_name is not ShapeBase.NOT_SET:
                _params['db_security_group_name'] = db_security_group_name
            if cidrip is not ShapeBase.NOT_SET:
                _params['cidrip'] = cidrip
            if ec2_security_group_name is not ShapeBase.NOT_SET:
                _params['ec2_security_group_name'] = ec2_security_group_name
            if ec2_security_group_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_id'] = ec2_security_group_id
            if ec2_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_owner_id'
                       ] = ec2_security_group_owner_id
            _request = shapes.AuthorizeDBSecurityGroupIngressMessage(**_params)
        response = self._boto_client.authorize_db_security_group_ingress(
            **_request.to_boto()
        )

        return shapes.AuthorizeDBSecurityGroupIngressResult.from_boto(response)

    def backtrack_db_cluster(
        self,
        _request: shapes.BacktrackDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
        backtrack_to: datetime.datetime,
        force: bool = ShapeBase.NOT_SET,
        use_earliest_time_on_point_in_time_unavailable: bool = ShapeBase.
        NOT_SET,
    ) -> shapes.DBClusterBacktrack:
        """
        Backtracks a DB cluster to a specific time, without creating a new DB cluster.

        For more information on backtracking, see [ Backtracking an Aurora DB
        Cluster](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if backtrack_to is not ShapeBase.NOT_SET:
                _params['backtrack_to'] = backtrack_to
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            if use_earliest_time_on_point_in_time_unavailable is not ShapeBase.NOT_SET:
                _params['use_earliest_time_on_point_in_time_unavailable'
                       ] = use_earliest_time_on_point_in_time_unavailable
            _request = shapes.BacktrackDBClusterMessage(**_params)
        response = self._boto_client.backtrack_db_cluster(**_request.to_boto())

        return shapes.DBClusterBacktrack.from_boto(response)

    def copy_db_cluster_parameter_group(
        self,
        _request: shapes.CopyDBClusterParameterGroupMessage = None,
        *,
        source_db_cluster_parameter_group_identifier: str,
        target_db_cluster_parameter_group_identifier: str,
        target_db_cluster_parameter_group_description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CopyDBClusterParameterGroupResult:
        """
        Copies the specified DB cluster parameter group.
        """
        if _request is None:
            _params = {}
            if source_db_cluster_parameter_group_identifier is not ShapeBase.NOT_SET:
                _params['source_db_cluster_parameter_group_identifier'
                       ] = source_db_cluster_parameter_group_identifier
            if target_db_cluster_parameter_group_identifier is not ShapeBase.NOT_SET:
                _params['target_db_cluster_parameter_group_identifier'
                       ] = target_db_cluster_parameter_group_identifier
            if target_db_cluster_parameter_group_description is not ShapeBase.NOT_SET:
                _params['target_db_cluster_parameter_group_description'
                       ] = target_db_cluster_parameter_group_description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CopyDBClusterParameterGroupMessage(**_params)
        response = self._boto_client.copy_db_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.CopyDBClusterParameterGroupResult.from_boto(response)

    def copy_db_cluster_snapshot(
        self,
        _request: shapes.CopyDBClusterSnapshotMessage = None,
        *,
        source_db_cluster_snapshot_identifier: str,
        target_db_cluster_snapshot_identifier: str,
        kms_key_id: str = ShapeBase.NOT_SET,
        pre_signed_url: str = ShapeBase.NOT_SET,
        copy_tags: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        source_region: str = ShapeBase.NOT_SET,
    ) -> shapes.CopyDBClusterSnapshotResult:
        """
        Copies a snapshot of a DB cluster.

        To copy a DB cluster snapshot from a shared manual DB cluster snapshot,
        `SourceDBClusterSnapshotIdentifier` must be the Amazon Resource Name (ARN) of
        the shared DB cluster snapshot.

        You can copy an encrypted DB cluster snapshot from another AWS Region. In that
        case, the AWS Region where you call the `CopyDBClusterSnapshot` action is the
        destination AWS Region for the encrypted DB cluster snapshot to be copied to. To
        copy an encrypted DB cluster snapshot from another AWS Region, you must provide
        the following values:

          * `KmsKeyId` \- The AWS Key Management System (AWS KMS) key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region.

          * `PreSignedUrl` \- A URL that contains a Signature Version 4 signed request for the `CopyDBClusterSnapshot` action to be called in the source AWS Region where the DB cluster snapshot is copied from. The pre-signed URL must be a valid request for the `CopyDBClusterSnapshot` API action that can be executed in the source AWS Region that contains the encrypted DB cluster snapshot to be copied.

        The pre-signed URL request must contain the following parameter values:

            * `KmsKeyId` \- The KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the `CopyDBClusterSnapshot` action that is called in the destination AWS Region, and the action contained in the pre-signed URL.

            * `DestinationRegion` \- The name of the AWS Region that the DB cluster snapshot will be created in.

            * `SourceDBClusterSnapshotIdentifier` \- The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your `SourceDBClusterSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115`.

        To learn how to generate a Signature Version 4 signed request, see [
        Authenticating Requests: Using Query Parameters (AWS Signature Version
        4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html)
        and [ Signature Version 4 Signing
        Process](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

          * `TargetDBClusterSnapshotIdentifier` \- The identifier for the new copy of the DB cluster snapshot in the destination AWS Region.

          * `SourceDBClusterSnapshotIdentifier` \- The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the ARN format for the source AWS Region and is the same value as the `SourceDBClusterSnapshotIdentifier` in the pre-signed URL. 

        To cancel the copy operation once it is in progress, delete the target DB
        cluster snapshot identified by `TargetDBClusterSnapshotIdentifier` while that DB
        cluster snapshot is in "copying" status.

        For more information on copying encrypted DB cluster snapshots from one AWS
        Region to another, see [ Copying a
        Snapshot](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html)
        in the _Amazon Aurora User Guide._

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if source_db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['source_db_cluster_snapshot_identifier'
                       ] = source_db_cluster_snapshot_identifier
            if target_db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['target_db_cluster_snapshot_identifier'
                       ] = target_db_cluster_snapshot_identifier
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if pre_signed_url is not ShapeBase.NOT_SET:
                _params['pre_signed_url'] = pre_signed_url
            if copy_tags is not ShapeBase.NOT_SET:
                _params['copy_tags'] = copy_tags
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            _request = shapes.CopyDBClusterSnapshotMessage(**_params)
        response = self._boto_client.copy_db_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.CopyDBClusterSnapshotResult.from_boto(response)

    def copy_db_parameter_group(
        self,
        _request: shapes.CopyDBParameterGroupMessage = None,
        *,
        source_db_parameter_group_identifier: str,
        target_db_parameter_group_identifier: str,
        target_db_parameter_group_description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CopyDBParameterGroupResult:
        """
        Copies the specified DB parameter group.
        """
        if _request is None:
            _params = {}
            if source_db_parameter_group_identifier is not ShapeBase.NOT_SET:
                _params['source_db_parameter_group_identifier'
                       ] = source_db_parameter_group_identifier
            if target_db_parameter_group_identifier is not ShapeBase.NOT_SET:
                _params['target_db_parameter_group_identifier'
                       ] = target_db_parameter_group_identifier
            if target_db_parameter_group_description is not ShapeBase.NOT_SET:
                _params['target_db_parameter_group_description'
                       ] = target_db_parameter_group_description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CopyDBParameterGroupMessage(**_params)
        response = self._boto_client.copy_db_parameter_group(
            **_request.to_boto()
        )

        return shapes.CopyDBParameterGroupResult.from_boto(response)

    def copy_db_snapshot(
        self,
        _request: shapes.CopyDBSnapshotMessage = None,
        *,
        source_db_snapshot_identifier: str,
        target_db_snapshot_identifier: str,
        kms_key_id: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        copy_tags: bool = ShapeBase.NOT_SET,
        pre_signed_url: str = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        source_region: str = ShapeBase.NOT_SET,
    ) -> shapes.CopyDBSnapshotResult:
        """
        Copies the specified DB snapshot. The source DB snapshot must be in the
        "available" state.

        You can copy a snapshot from one AWS Region to another. In that case, the AWS
        Region where you call the `CopyDBSnapshot` action is the destination AWS Region
        for the DB snapshot copy.

        For more information about copying snapshots, see [Copying a DB
        Snapshot](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopyDBSnapshot.html)
        in the _Amazon RDS User Guide._
        """
        if _request is None:
            _params = {}
            if source_db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['source_db_snapshot_identifier'
                       ] = source_db_snapshot_identifier
            if target_db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['target_db_snapshot_identifier'
                       ] = target_db_snapshot_identifier
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if copy_tags is not ShapeBase.NOT_SET:
                _params['copy_tags'] = copy_tags
            if pre_signed_url is not ShapeBase.NOT_SET:
                _params['pre_signed_url'] = pre_signed_url
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            _request = shapes.CopyDBSnapshotMessage(**_params)
        response = self._boto_client.copy_db_snapshot(**_request.to_boto())

        return shapes.CopyDBSnapshotResult.from_boto(response)

    def copy_option_group(
        self,
        _request: shapes.CopyOptionGroupMessage = None,
        *,
        source_option_group_identifier: str,
        target_option_group_identifier: str,
        target_option_group_description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CopyOptionGroupResult:
        """
        Copies the specified option group.
        """
        if _request is None:
            _params = {}
            if source_option_group_identifier is not ShapeBase.NOT_SET:
                _params['source_option_group_identifier'
                       ] = source_option_group_identifier
            if target_option_group_identifier is not ShapeBase.NOT_SET:
                _params['target_option_group_identifier'
                       ] = target_option_group_identifier
            if target_option_group_description is not ShapeBase.NOT_SET:
                _params['target_option_group_description'
                       ] = target_option_group_description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CopyOptionGroupMessage(**_params)
        response = self._boto_client.copy_option_group(**_request.to_boto())

        return shapes.CopyOptionGroupResult.from_boto(response)

    def create_db_cluster(
        self,
        _request: shapes.CreateDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
        engine: str,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        backup_retention_period: int = ShapeBase.NOT_SET,
        character_set_name: str = ShapeBase.NOT_SET,
        database_name: str = ShapeBase.NOT_SET,
        db_cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        master_username: str = ShapeBase.NOT_SET,
        master_user_password: str = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        replication_source_identifier: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        storage_encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        pre_signed_url: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        backtrack_window: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        engine_mode: str = ShapeBase.NOT_SET,
        scaling_configuration: shapes.ScalingConfiguration = ShapeBase.NOT_SET,
        source_region: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBClusterResult:
        """
        Creates a new Amazon Aurora DB cluster.

        You can use the `ReplicationSourceIdentifier` parameter to create the DB cluster
        as a Read Replica of another DB cluster or Amazon RDS MySQL DB instance. For
        cross-region replication where the DB cluster identified by
        `ReplicationSourceIdentifier` is encrypted, you must also specify the
        `PreSignedUrl` parameter.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if character_set_name is not ShapeBase.NOT_SET:
                _params['character_set_name'] = character_set_name
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if master_username is not ShapeBase.NOT_SET:
                _params['master_username'] = master_username
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if replication_source_identifier is not ShapeBase.NOT_SET:
                _params['replication_source_identifier'
                       ] = replication_source_identifier
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if storage_encrypted is not ShapeBase.NOT_SET:
                _params['storage_encrypted'] = storage_encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if pre_signed_url is not ShapeBase.NOT_SET:
                _params['pre_signed_url'] = pre_signed_url
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if backtrack_window is not ShapeBase.NOT_SET:
                _params['backtrack_window'] = backtrack_window
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if engine_mode is not ShapeBase.NOT_SET:
                _params['engine_mode'] = engine_mode
            if scaling_configuration is not ShapeBase.NOT_SET:
                _params['scaling_configuration'] = scaling_configuration
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            _request = shapes.CreateDBClusterMessage(**_params)
        response = self._boto_client.create_db_cluster(**_request.to_boto())

        return shapes.CreateDBClusterResult.from_boto(response)

    def create_db_cluster_parameter_group(
        self,
        _request: shapes.CreateDBClusterParameterGroupMessage = None,
        *,
        db_cluster_parameter_group_name: str,
        db_parameter_group_family: str,
        description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBClusterParameterGroupResult:
        """
        Creates a new DB cluster parameter group.

        Parameters in a DB cluster parameter group apply to all of the instances in a DB
        cluster.

        A DB cluster parameter group is initially created with the default parameters
        for the database engine used by instances in the DB cluster. To provide custom
        values for any of the parameters, you must modify the group after creating it
        using ModifyDBClusterParameterGroup. Once you've created a DB cluster parameter
        group, you need to associate it with your DB cluster using ModifyDBCluster. When
        you associate a new DB cluster parameter group with a running DB cluster, you
        need to reboot the DB instances in the DB cluster without failover for the new
        DB cluster parameter group and associated settings to take effect.

        After you create a DB cluster parameter group, you should wait at least 5
        minutes before creating your first DB cluster that uses that DB cluster
        parameter group as the default parameter group. This allows Amazon RDS to fully
        complete the create action before the DB cluster parameter group is used as the
        default for a new DB cluster. This is especially important for parameters that
        are critical when creating the default database for a DB cluster, such as the
        character set for the default database defined by the `character_set_database`
        parameter. You can use the _Parameter Groups_ option of the [Amazon RDS
        console](https://console.aws.amazon.com/rds/) or the DescribeDBClusterParameters
        command to verify that your DB cluster parameter group has been created or
        modified.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if db_parameter_group_family is not ShapeBase.NOT_SET:
                _params['db_parameter_group_family'] = db_parameter_group_family
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDBClusterParameterGroupMessage(**_params)
        response = self._boto_client.create_db_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.CreateDBClusterParameterGroupResult.from_boto(response)

    def create_db_cluster_snapshot(
        self,
        _request: shapes.CreateDBClusterSnapshotMessage = None,
        *,
        db_cluster_snapshot_identifier: str,
        db_cluster_identifier: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBClusterSnapshotResult:
        """
        Creates a snapshot of a DB cluster. For more information on Amazon Aurora, see [
        What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_snapshot_identifier'
                       ] = db_cluster_snapshot_identifier
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDBClusterSnapshotMessage(**_params)
        response = self._boto_client.create_db_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.CreateDBClusterSnapshotResult.from_boto(response)

    def create_db_instance(
        self,
        _request: shapes.CreateDBInstanceMessage = None,
        *,
        db_instance_identifier: str,
        db_instance_class: str,
        engine: str,
        db_name: str = ShapeBase.NOT_SET,
        allocated_storage: int = ShapeBase.NOT_SET,
        master_username: str = ShapeBase.NOT_SET,
        master_user_password: str = ShapeBase.NOT_SET,
        db_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        db_parameter_group_name: str = ShapeBase.NOT_SET,
        backup_retention_period: int = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        license_model: str = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        character_set_name: str = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        db_cluster_identifier: str = ShapeBase.NOT_SET,
        storage_type: str = ShapeBase.NOT_SET,
        tde_credential_arn: str = ShapeBase.NOT_SET,
        tde_credential_password: str = ShapeBase.NOT_SET,
        storage_encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        domain: str = ShapeBase.NOT_SET,
        copy_tags_to_snapshot: bool = ShapeBase.NOT_SET,
        monitoring_interval: int = ShapeBase.NOT_SET,
        monitoring_role_arn: str = ShapeBase.NOT_SET,
        domain_iam_role_name: str = ShapeBase.NOT_SET,
        promotion_tier: int = ShapeBase.NOT_SET,
        timezone: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        enable_performance_insights: bool = ShapeBase.NOT_SET,
        performance_insights_kms_key_id: str = ShapeBase.NOT_SET,
        performance_insights_retention_period: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        processor_features: typing.List[shapes.ProcessorFeature
                                       ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBInstanceResult:
        """
        Creates a new DB instance.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if db_name is not ShapeBase.NOT_SET:
                _params['db_name'] = db_name
            if allocated_storage is not ShapeBase.NOT_SET:
                _params['allocated_storage'] = allocated_storage
            if master_username is not ShapeBase.NOT_SET:
                _params['master_username'] = master_username
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if db_security_groups is not ShapeBase.NOT_SET:
                _params['db_security_groups'] = db_security_groups
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if license_model is not ShapeBase.NOT_SET:
                _params['license_model'] = license_model
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if character_set_name is not ShapeBase.NOT_SET:
                _params['character_set_name'] = character_set_name
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if storage_type is not ShapeBase.NOT_SET:
                _params['storage_type'] = storage_type
            if tde_credential_arn is not ShapeBase.NOT_SET:
                _params['tde_credential_arn'] = tde_credential_arn
            if tde_credential_password is not ShapeBase.NOT_SET:
                _params['tde_credential_password'] = tde_credential_password
            if storage_encrypted is not ShapeBase.NOT_SET:
                _params['storage_encrypted'] = storage_encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if copy_tags_to_snapshot is not ShapeBase.NOT_SET:
                _params['copy_tags_to_snapshot'] = copy_tags_to_snapshot
            if monitoring_interval is not ShapeBase.NOT_SET:
                _params['monitoring_interval'] = monitoring_interval
            if monitoring_role_arn is not ShapeBase.NOT_SET:
                _params['monitoring_role_arn'] = monitoring_role_arn
            if domain_iam_role_name is not ShapeBase.NOT_SET:
                _params['domain_iam_role_name'] = domain_iam_role_name
            if promotion_tier is not ShapeBase.NOT_SET:
                _params['promotion_tier'] = promotion_tier
            if timezone is not ShapeBase.NOT_SET:
                _params['timezone'] = timezone
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if enable_performance_insights is not ShapeBase.NOT_SET:
                _params['enable_performance_insights'
                       ] = enable_performance_insights
            if performance_insights_kms_key_id is not ShapeBase.NOT_SET:
                _params['performance_insights_kms_key_id'
                       ] = performance_insights_kms_key_id
            if performance_insights_retention_period is not ShapeBase.NOT_SET:
                _params['performance_insights_retention_period'
                       ] = performance_insights_retention_period
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if processor_features is not ShapeBase.NOT_SET:
                _params['processor_features'] = processor_features
            _request = shapes.CreateDBInstanceMessage(**_params)
        response = self._boto_client.create_db_instance(**_request.to_boto())

        return shapes.CreateDBInstanceResult.from_boto(response)

    def create_db_instance_read_replica(
        self,
        _request: shapes.CreateDBInstanceReadReplicaMessage = None,
        *,
        db_instance_identifier: str,
        source_db_instance_identifier: str,
        db_instance_class: str = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        storage_type: str = ShapeBase.NOT_SET,
        copy_tags_to_snapshot: bool = ShapeBase.NOT_SET,
        monitoring_interval: int = ShapeBase.NOT_SET,
        monitoring_role_arn: str = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        pre_signed_url: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        enable_performance_insights: bool = ShapeBase.NOT_SET,
        performance_insights_kms_key_id: str = ShapeBase.NOT_SET,
        performance_insights_retention_period: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        processor_features: typing.List[shapes.ProcessorFeature
                                       ] = ShapeBase.NOT_SET,
        use_default_processor_features: bool = ShapeBase.NOT_SET,
        source_region: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBInstanceReadReplicaResult:
        """
        Creates a new DB instance that acts as a Read Replica for an existing source DB
        instance. You can create a Read Replica for a DB instance running MySQL,
        MariaDB, or PostgreSQL. For more information, see [Working with PostgreSQL,
        MySQL, and MariaDB Read
        Replicas](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
        in the _Amazon RDS User Guide_.

        Amazon Aurora doesn't support this action. You must call the `CreateDBInstance`
        action to create a DB instance for an Aurora DB cluster.

        All Read Replica DB instances are created with backups disabled. All other DB
        instance attributes (including DB security groups and DB parameter groups) are
        inherited from the source DB instance, except as specified following.

        Your source DB instance must have backup retention enabled.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if source_db_instance_identifier is not ShapeBase.NOT_SET:
                _params['source_db_instance_identifier'
                       ] = source_db_instance_identifier
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if storage_type is not ShapeBase.NOT_SET:
                _params['storage_type'] = storage_type
            if copy_tags_to_snapshot is not ShapeBase.NOT_SET:
                _params['copy_tags_to_snapshot'] = copy_tags_to_snapshot
            if monitoring_interval is not ShapeBase.NOT_SET:
                _params['monitoring_interval'] = monitoring_interval
            if monitoring_role_arn is not ShapeBase.NOT_SET:
                _params['monitoring_role_arn'] = monitoring_role_arn
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if pre_signed_url is not ShapeBase.NOT_SET:
                _params['pre_signed_url'] = pre_signed_url
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if enable_performance_insights is not ShapeBase.NOT_SET:
                _params['enable_performance_insights'
                       ] = enable_performance_insights
            if performance_insights_kms_key_id is not ShapeBase.NOT_SET:
                _params['performance_insights_kms_key_id'
                       ] = performance_insights_kms_key_id
            if performance_insights_retention_period is not ShapeBase.NOT_SET:
                _params['performance_insights_retention_period'
                       ] = performance_insights_retention_period
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if processor_features is not ShapeBase.NOT_SET:
                _params['processor_features'] = processor_features
            if use_default_processor_features is not ShapeBase.NOT_SET:
                _params['use_default_processor_features'
                       ] = use_default_processor_features
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            _request = shapes.CreateDBInstanceReadReplicaMessage(**_params)
        response = self._boto_client.create_db_instance_read_replica(
            **_request.to_boto()
        )

        return shapes.CreateDBInstanceReadReplicaResult.from_boto(response)

    def create_db_parameter_group(
        self,
        _request: shapes.CreateDBParameterGroupMessage = None,
        *,
        db_parameter_group_name: str,
        db_parameter_group_family: str,
        description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBParameterGroupResult:
        """
        Creates a new DB parameter group.

        A DB parameter group is initially created with the default parameters for the
        database engine used by the DB instance. To provide custom values for any of the
        parameters, you must modify the group after creating it using
        _ModifyDBParameterGroup_. Once you've created a DB parameter group, you need to
        associate it with your DB instance using _ModifyDBInstance_. When you associate
        a new DB parameter group with a running DB instance, you need to reboot the DB
        instance without failover for the new DB parameter group and associated settings
        to take effect.

        After you create a DB parameter group, you should wait at least 5 minutes before
        creating your first DB instance that uses that DB parameter group as the default
        parameter group. This allows Amazon RDS to fully complete the create action
        before the parameter group is used as the default for a new DB instance. This is
        especially important for parameters that are critical when creating the default
        database for a DB instance, such as the character set for the default database
        defined by the `character_set_database` parameter. You can use the _Parameter
        Groups_ option of the [Amazon RDS console](https://console.aws.amazon.com/rds/)
        or the _DescribeDBParameters_ command to verify that your DB parameter group has
        been created or modified.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if db_parameter_group_family is not ShapeBase.NOT_SET:
                _params['db_parameter_group_family'] = db_parameter_group_family
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDBParameterGroupMessage(**_params)
        response = self._boto_client.create_db_parameter_group(
            **_request.to_boto()
        )

        return shapes.CreateDBParameterGroupResult.from_boto(response)

    def create_db_security_group(
        self,
        _request: shapes.CreateDBSecurityGroupMessage = None,
        *,
        db_security_group_name: str,
        db_security_group_description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBSecurityGroupResult:
        """
        Creates a new DB security group. DB security groups control access to a DB
        instance.

        A DB security group controls access to EC2-Classic DB instances that are not in
        a VPC.
        """
        if _request is None:
            _params = {}
            if db_security_group_name is not ShapeBase.NOT_SET:
                _params['db_security_group_name'] = db_security_group_name
            if db_security_group_description is not ShapeBase.NOT_SET:
                _params['db_security_group_description'
                       ] = db_security_group_description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDBSecurityGroupMessage(**_params)
        response = self._boto_client.create_db_security_group(
            **_request.to_boto()
        )

        return shapes.CreateDBSecurityGroupResult.from_boto(response)

    def create_db_snapshot(
        self,
        _request: shapes.CreateDBSnapshotMessage = None,
        *,
        db_snapshot_identifier: str,
        db_instance_identifier: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBSnapshotResult:
        """
        Creates a DBSnapshot. The source DBInstance must be in "available" state.
        """
        if _request is None:
            _params = {}
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDBSnapshotMessage(**_params)
        response = self._boto_client.create_db_snapshot(**_request.to_boto())

        return shapes.CreateDBSnapshotResult.from_boto(response)

    def create_db_subnet_group(
        self,
        _request: shapes.CreateDBSubnetGroupMessage = None,
        *,
        db_subnet_group_name: str,
        db_subnet_group_description: str,
        subnet_ids: typing.List[str],
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDBSubnetGroupResult:
        """
        Creates a new DB subnet group. DB subnet groups must contain at least one subnet
        in at least two AZs in the AWS Region.
        """
        if _request is None:
            _params = {}
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if db_subnet_group_description is not ShapeBase.NOT_SET:
                _params['db_subnet_group_description'
                       ] = db_subnet_group_description
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateDBSubnetGroupMessage(**_params)
        response = self._boto_client.create_db_subnet_group(
            **_request.to_boto()
        )

        return shapes.CreateDBSubnetGroupResult.from_boto(response)

    def create_event_subscription(
        self,
        _request: shapes.CreateEventSubscriptionMessage = None,
        *,
        subscription_name: str,
        sns_topic_arn: str,
        source_type: str = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        source_ids: typing.List[str] = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateEventSubscriptionResult:
        """
        Creates an RDS event notification subscription. This action requires a topic ARN
        (Amazon Resource Name) created by either the RDS console, the SNS console, or
        the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS
        and subscribe to the topic. The ARN is displayed in the SNS console.

        You can specify the type of source (SourceType) you want to be notified of,
        provide a list of RDS sources (SourceIds) that triggers the events, and provide
        a list of event categories (EventCategories) for events you want to be notified
        of. For example, you can specify SourceType = db-instance, SourceIds =
        mydbinstance1, mydbinstance2 and EventCategories = Availability, Backup.

        If you specify both the SourceType and SourceIds, such as SourceType = db-
        instance and SourceIdentifier = myDBInstance1, you are notified of all the db-
        instance events for the specified source. If you specify a SourceType but do not
        specify a SourceIdentifier, you receive notice of the events for that source
        type for all your RDS sources. If you do not specify either the SourceType nor
        the SourceIdentifier, you are notified of events generated from all RDS sources
        belonging to your customer account.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if source_ids is not ShapeBase.NOT_SET:
                _params['source_ids'] = source_ids
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateEventSubscriptionMessage(**_params)
        response = self._boto_client.create_event_subscription(
            **_request.to_boto()
        )

        return shapes.CreateEventSubscriptionResult.from_boto(response)

    def create_option_group(
        self,
        _request: shapes.CreateOptionGroupMessage = None,
        *,
        option_group_name: str,
        engine_name: str,
        major_engine_version: str,
        option_group_description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateOptionGroupResult:
        """
        Creates a new option group. You can create up to 20 option groups.
        """
        if _request is None:
            _params = {}
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if engine_name is not ShapeBase.NOT_SET:
                _params['engine_name'] = engine_name
            if major_engine_version is not ShapeBase.NOT_SET:
                _params['major_engine_version'] = major_engine_version
            if option_group_description is not ShapeBase.NOT_SET:
                _params['option_group_description'] = option_group_description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateOptionGroupMessage(**_params)
        response = self._boto_client.create_option_group(**_request.to_boto())

        return shapes.CreateOptionGroupResult.from_boto(response)

    def delete_db_cluster(
        self,
        _request: shapes.DeleteDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
        skip_final_snapshot: bool = ShapeBase.NOT_SET,
        final_db_snapshot_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteDBClusterResult:
        """
        The DeleteDBCluster action deletes a previously provisioned DB cluster. When you
        delete a DB cluster, all automated backups for that DB cluster are deleted and
        can't be recovered. Manual DB cluster snapshots of the specified DB cluster are
        not deleted.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if skip_final_snapshot is not ShapeBase.NOT_SET:
                _params['skip_final_snapshot'] = skip_final_snapshot
            if final_db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['final_db_snapshot_identifier'
                       ] = final_db_snapshot_identifier
            _request = shapes.DeleteDBClusterMessage(**_params)
        response = self._boto_client.delete_db_cluster(**_request.to_boto())

        return shapes.DeleteDBClusterResult.from_boto(response)

    def delete_db_cluster_parameter_group(
        self,
        _request: shapes.DeleteDBClusterParameterGroupMessage = None,
        *,
        db_cluster_parameter_group_name: str,
    ) -> None:
        """
        Deletes a specified DB cluster parameter group. The DB cluster parameter group
        to be deleted can't be associated with any DB clusters.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            _request = shapes.DeleteDBClusterParameterGroupMessage(**_params)
        response = self._boto_client.delete_db_cluster_parameter_group(
            **_request.to_boto()
        )

    def delete_db_cluster_snapshot(
        self,
        _request: shapes.DeleteDBClusterSnapshotMessage = None,
        *,
        db_cluster_snapshot_identifier: str,
    ) -> shapes.DeleteDBClusterSnapshotResult:
        """
        Deletes a DB cluster snapshot. If the snapshot is being copied, the copy
        operation is terminated.

        The DB cluster snapshot must be in the `available` state to be deleted.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_snapshot_identifier'
                       ] = db_cluster_snapshot_identifier
            _request = shapes.DeleteDBClusterSnapshotMessage(**_params)
        response = self._boto_client.delete_db_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.DeleteDBClusterSnapshotResult.from_boto(response)

    def delete_db_instance(
        self,
        _request: shapes.DeleteDBInstanceMessage = None,
        *,
        db_instance_identifier: str,
        skip_final_snapshot: bool = ShapeBase.NOT_SET,
        final_db_snapshot_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteDBInstanceResult:
        """
        The DeleteDBInstance action deletes a previously provisioned DB instance. When
        you delete a DB instance, all automated backups for that instance are deleted
        and can't be recovered. Manual DB snapshots of the DB instance to be deleted by
        `DeleteDBInstance` are not deleted.

        If you request a final DB snapshot the status of the Amazon RDS DB instance is
        `deleting` until the DB snapshot is created. The API action `DescribeDBInstance`
        is used to monitor the status of this operation. The action can't be canceled or
        reverted once submitted.

        Note that when a DB instance is in a failure state and has a status of `failed`,
        `incompatible-restore`, or `incompatible-network`, you can only delete it when
        the `SkipFinalSnapshot` parameter is set to `true`.

        If the specified DB instance is part of an Amazon Aurora DB cluster, you can't
        delete the DB instance if both of the following conditions are true:

          * The DB cluster is a Read Replica of another Amazon Aurora DB cluster.

          * The DB instance is the only instance in the DB cluster.

        To delete a DB instance in this case, first call the PromoteReadReplicaDBCluster
        API action to promote the DB cluster so it's no longer a Read Replica. After the
        promotion completes, then call the `DeleteDBInstance` API action to delete the
        final instance in the DB cluster.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if skip_final_snapshot is not ShapeBase.NOT_SET:
                _params['skip_final_snapshot'] = skip_final_snapshot
            if final_db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['final_db_snapshot_identifier'
                       ] = final_db_snapshot_identifier
            _request = shapes.DeleteDBInstanceMessage(**_params)
        response = self._boto_client.delete_db_instance(**_request.to_boto())

        return shapes.DeleteDBInstanceResult.from_boto(response)

    def delete_db_parameter_group(
        self,
        _request: shapes.DeleteDBParameterGroupMessage = None,
        *,
        db_parameter_group_name: str,
    ) -> None:
        """
        Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can't
        be associated with any DB instances.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            _request = shapes.DeleteDBParameterGroupMessage(**_params)
        response = self._boto_client.delete_db_parameter_group(
            **_request.to_boto()
        )

    def delete_db_security_group(
        self,
        _request: shapes.DeleteDBSecurityGroupMessage = None,
        *,
        db_security_group_name: str,
    ) -> None:
        """
        Deletes a DB security group.

        The specified DB security group must not be associated with any DB instances.
        """
        if _request is None:
            _params = {}
            if db_security_group_name is not ShapeBase.NOT_SET:
                _params['db_security_group_name'] = db_security_group_name
            _request = shapes.DeleteDBSecurityGroupMessage(**_params)
        response = self._boto_client.delete_db_security_group(
            **_request.to_boto()
        )

    def delete_db_snapshot(
        self,
        _request: shapes.DeleteDBSnapshotMessage = None,
        *,
        db_snapshot_identifier: str,
    ) -> shapes.DeleteDBSnapshotResult:
        """
        Deletes a DBSnapshot. If the snapshot is being copied, the copy operation is
        terminated.

        The DBSnapshot must be in the `available` state to be deleted.
        """
        if _request is None:
            _params = {}
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            _request = shapes.DeleteDBSnapshotMessage(**_params)
        response = self._boto_client.delete_db_snapshot(**_request.to_boto())

        return shapes.DeleteDBSnapshotResult.from_boto(response)

    def delete_db_subnet_group(
        self,
        _request: shapes.DeleteDBSubnetGroupMessage = None,
        *,
        db_subnet_group_name: str,
    ) -> None:
        """
        Deletes a DB subnet group.

        The specified database subnet group must not be associated with any DB
        instances.
        """
        if _request is None:
            _params = {}
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            _request = shapes.DeleteDBSubnetGroupMessage(**_params)
        response = self._boto_client.delete_db_subnet_group(
            **_request.to_boto()
        )

    def delete_event_subscription(
        self,
        _request: shapes.DeleteEventSubscriptionMessage = None,
        *,
        subscription_name: str,
    ) -> shapes.DeleteEventSubscriptionResult:
        """
        Deletes an RDS event notification subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            _request = shapes.DeleteEventSubscriptionMessage(**_params)
        response = self._boto_client.delete_event_subscription(
            **_request.to_boto()
        )

        return shapes.DeleteEventSubscriptionResult.from_boto(response)

    def delete_option_group(
        self,
        _request: shapes.DeleteOptionGroupMessage = None,
        *,
        option_group_name: str,
    ) -> None:
        """
        Deletes an existing option group.
        """
        if _request is None:
            _params = {}
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            _request = shapes.DeleteOptionGroupMessage(**_params)
        response = self._boto_client.delete_option_group(**_request.to_boto())

    def describe_account_attributes(
        self,
        _request: shapes.DescribeAccountAttributesMessage = None,
    ) -> shapes.AccountAttributesMessage:
        """
        Lists all of the attributes for a customer account. The attributes include
        Amazon RDS quotas for the account, such as the number of DB instances allowed.
        The description for a quota includes the quota name, current usage toward that
        quota, and the quota's maximum value.

        This command doesn't take any parameters.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeAccountAttributesMessage(**_params)
        response = self._boto_client.describe_account_attributes(
            **_request.to_boto()
        )

        return shapes.AccountAttributesMessage.from_boto(response)

    def describe_certificates(
        self,
        _request: shapes.DescribeCertificatesMessage = None,
        *,
        certificate_identifier: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.CertificateMessage:
        """
        Lists the set of CA certificates provided by Amazon RDS for this AWS account.
        """
        if _request is None:
            _params = {}
            if certificate_identifier is not ShapeBase.NOT_SET:
                _params['certificate_identifier'] = certificate_identifier
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeCertificatesMessage(**_params)
        response = self._boto_client.describe_certificates(**_request.to_boto())

        return shapes.CertificateMessage.from_boto(response)

    def describe_db_cluster_backtracks(
        self,
        _request: shapes.DescribeDBClusterBacktracksMessage = None,
        *,
        db_cluster_identifier: str,
        backtrack_identifier: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterBacktrackMessage:
        """
        Returns information about backtracks for a DB cluster.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if backtrack_identifier is not ShapeBase.NOT_SET:
                _params['backtrack_identifier'] = backtrack_identifier
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBClusterBacktracksMessage(**_params)
        response = self._boto_client.describe_db_cluster_backtracks(
            **_request.to_boto()
        )

        return shapes.DBClusterBacktrackMessage.from_boto(response)

    def describe_db_cluster_parameter_groups(
        self,
        _request: shapes.DescribeDBClusterParameterGroupsMessage = None,
        *,
        db_cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterParameterGroupsMessage:
        """
        Returns a list of `DBClusterParameterGroup` descriptions. If a
        `DBClusterParameterGroupName` parameter is specified, the list will contain only
        the description of the specified DB cluster parameter group.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBClusterParameterGroupsMessage(**_params)
        response = self._boto_client.describe_db_cluster_parameter_groups(
            **_request.to_boto()
        )

        return shapes.DBClusterParameterGroupsMessage.from_boto(response)

    def describe_db_cluster_parameters(
        self,
        _request: shapes.DescribeDBClusterParametersMessage = None,
        *,
        db_cluster_parameter_group_name: str,
        source: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterParameterGroupDetails:
        """
        Returns the detailed parameter list for a particular DB cluster parameter group.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBClusterParametersMessage(**_params)
        response = self._boto_client.describe_db_cluster_parameters(
            **_request.to_boto()
        )

        return shapes.DBClusterParameterGroupDetails.from_boto(response)

    def describe_db_cluster_snapshot_attributes(
        self,
        _request: shapes.DescribeDBClusterSnapshotAttributesMessage = None,
        *,
        db_cluster_snapshot_identifier: str,
    ) -> shapes.DescribeDBClusterSnapshotAttributesResult:
        """
        Returns a list of DB cluster snapshot attribute names and values for a manual DB
        cluster snapshot.

        When sharing snapshots with other AWS accounts,
        `DescribeDBClusterSnapshotAttributes` returns the `restore` attribute and a list
        of IDs for the AWS accounts that are authorized to copy or restore the manual DB
        cluster snapshot. If `all` is included in the list of values for the `restore`
        attribute, then the manual DB cluster snapshot is public and can be copied or
        restored by all AWS accounts.

        To add or remove access for an AWS account to copy or restore a manual DB
        cluster snapshot, or to make the manual DB cluster snapshot public or private,
        use the ModifyDBClusterSnapshotAttribute API action.
        """
        if _request is None:
            _params = {}
            if db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_snapshot_identifier'
                       ] = db_cluster_snapshot_identifier
            _request = shapes.DescribeDBClusterSnapshotAttributesMessage(
                **_params
            )
        response = self._boto_client.describe_db_cluster_snapshot_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeDBClusterSnapshotAttributesResult.from_boto(
            response
        )

    def describe_db_cluster_snapshots(
        self,
        _request: shapes.DescribeDBClusterSnapshotsMessage = None,
        *,
        db_cluster_identifier: str = ShapeBase.NOT_SET,
        db_cluster_snapshot_identifier: str = ShapeBase.NOT_SET,
        snapshot_type: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        include_shared: bool = ShapeBase.NOT_SET,
        include_public: bool = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterSnapshotMessage:
        """
        Returns information about DB cluster snapshots. This API action supports
        pagination.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_snapshot_identifier'
                       ] = db_cluster_snapshot_identifier
            if snapshot_type is not ShapeBase.NOT_SET:
                _params['snapshot_type'] = snapshot_type
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if include_shared is not ShapeBase.NOT_SET:
                _params['include_shared'] = include_shared
            if include_public is not ShapeBase.NOT_SET:
                _params['include_public'] = include_public
            _request = shapes.DescribeDBClusterSnapshotsMessage(**_params)
        paginator = self.get_paginator("describe_db_cluster_snapshots"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBClusterSnapshotMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBClusterSnapshotMessage.from_boto(response)

    def describe_db_clusters(
        self,
        _request: shapes.DescribeDBClustersMessage = None,
        *,
        db_cluster_identifier: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterMessage:
        """
        Returns information about provisioned Aurora DB clusters. This API supports
        pagination.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBClustersMessage(**_params)
        paginator = self.get_paginator("describe_db_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBClusterMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBClusterMessage.from_boto(response)

    def describe_db_engine_versions(
        self,
        _request: shapes.DescribeDBEngineVersionsMessage = None,
        *,
        engine: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        db_parameter_group_family: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        default_only: bool = ShapeBase.NOT_SET,
        list_supported_character_sets: bool = ShapeBase.NOT_SET,
        list_supported_timezones: bool = ShapeBase.NOT_SET,
    ) -> shapes.DBEngineVersionMessage:
        """
        Returns a list of the available DB engines.
        """
        if _request is None:
            _params = {}
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if db_parameter_group_family is not ShapeBase.NOT_SET:
                _params['db_parameter_group_family'] = db_parameter_group_family
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if default_only is not ShapeBase.NOT_SET:
                _params['default_only'] = default_only
            if list_supported_character_sets is not ShapeBase.NOT_SET:
                _params['list_supported_character_sets'
                       ] = list_supported_character_sets
            if list_supported_timezones is not ShapeBase.NOT_SET:
                _params['list_supported_timezones'] = list_supported_timezones
            _request = shapes.DescribeDBEngineVersionsMessage(**_params)
        paginator = self.get_paginator("describe_db_engine_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBEngineVersionMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBEngineVersionMessage.from_boto(response)

    def describe_db_instances(
        self,
        _request: shapes.DescribeDBInstancesMessage = None,
        *,
        db_instance_identifier: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBInstanceMessage:
        """
        Returns information about provisioned RDS instances. This API supports
        pagination.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBInstancesMessage(**_params)
        paginator = self.get_paginator("describe_db_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBInstanceMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBInstanceMessage.from_boto(response)

    def describe_db_log_files(
        self,
        _request: shapes.DescribeDBLogFilesMessage = None,
        *,
        db_instance_identifier: str,
        filename_contains: str = ShapeBase.NOT_SET,
        file_last_written: int = ShapeBase.NOT_SET,
        file_size: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDBLogFilesResponse:
        """
        Returns a list of DB log files for the DB instance.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if filename_contains is not ShapeBase.NOT_SET:
                _params['filename_contains'] = filename_contains
            if file_last_written is not ShapeBase.NOT_SET:
                _params['file_last_written'] = file_last_written
            if file_size is not ShapeBase.NOT_SET:
                _params['file_size'] = file_size
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBLogFilesMessage(**_params)
        paginator = self.get_paginator("describe_db_log_files").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeDBLogFilesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeDBLogFilesResponse.from_boto(response)

    def describe_db_parameter_groups(
        self,
        _request: shapes.DescribeDBParameterGroupsMessage = None,
        *,
        db_parameter_group_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBParameterGroupsMessage:
        """
        Returns a list of `DBParameterGroup` descriptions. If a `DBParameterGroupName`
        is specified, the list will contain only the description of the specified DB
        parameter group.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBParameterGroupsMessage(**_params)
        paginator = self.get_paginator("describe_db_parameter_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBParameterGroupsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBParameterGroupsMessage.from_boto(response)

    def describe_db_parameters(
        self,
        _request: shapes.DescribeDBParametersMessage = None,
        *,
        db_parameter_group_name: str,
        source: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBParameterGroupDetails:
        """
        Returns the detailed parameter list for a particular DB parameter group.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBParametersMessage(**_params)
        paginator = self.get_paginator("describe_db_parameters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBParameterGroupDetails.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBParameterGroupDetails.from_boto(response)

    def describe_db_security_groups(
        self,
        _request: shapes.DescribeDBSecurityGroupsMessage = None,
        *,
        db_security_group_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBSecurityGroupMessage:
        """
        Returns a list of `DBSecurityGroup` descriptions. If a `DBSecurityGroupName` is
        specified, the list will contain only the descriptions of the specified DB
        security group.
        """
        if _request is None:
            _params = {}
            if db_security_group_name is not ShapeBase.NOT_SET:
                _params['db_security_group_name'] = db_security_group_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBSecurityGroupsMessage(**_params)
        paginator = self.get_paginator("describe_db_security_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBSecurityGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBSecurityGroupMessage.from_boto(response)

    def describe_db_snapshot_attributes(
        self,
        _request: shapes.DescribeDBSnapshotAttributesMessage = None,
        *,
        db_snapshot_identifier: str,
    ) -> shapes.DescribeDBSnapshotAttributesResult:
        """
        Returns a list of DB snapshot attribute names and values for a manual DB
        snapshot.

        When sharing snapshots with other AWS accounts, `DescribeDBSnapshotAttributes`
        returns the `restore` attribute and a list of IDs for the AWS accounts that are
        authorized to copy or restore the manual DB snapshot. If `all` is included in
        the list of values for the `restore` attribute, then the manual DB snapshot is
        public and can be copied or restored by all AWS accounts.

        To add or remove access for an AWS account to copy or restore a manual DB
        snapshot, or to make the manual DB snapshot public or private, use the
        ModifyDBSnapshotAttribute API action.
        """
        if _request is None:
            _params = {}
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            _request = shapes.DescribeDBSnapshotAttributesMessage(**_params)
        response = self._boto_client.describe_db_snapshot_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeDBSnapshotAttributesResult.from_boto(response)

    def describe_db_snapshots(
        self,
        _request: shapes.DescribeDBSnapshotsMessage = None,
        *,
        db_instance_identifier: str = ShapeBase.NOT_SET,
        db_snapshot_identifier: str = ShapeBase.NOT_SET,
        snapshot_type: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        include_shared: bool = ShapeBase.NOT_SET,
        include_public: bool = ShapeBase.NOT_SET,
    ) -> shapes.DBSnapshotMessage:
        """
        Returns information about DB snapshots. This API action supports pagination.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            if snapshot_type is not ShapeBase.NOT_SET:
                _params['snapshot_type'] = snapshot_type
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if include_shared is not ShapeBase.NOT_SET:
                _params['include_shared'] = include_shared
            if include_public is not ShapeBase.NOT_SET:
                _params['include_public'] = include_public
            _request = shapes.DescribeDBSnapshotsMessage(**_params)
        paginator = self.get_paginator("describe_db_snapshots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBSnapshotMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBSnapshotMessage.from_boto(response)

    def describe_db_subnet_groups(
        self,
        _request: shapes.DescribeDBSubnetGroupsMessage = None,
        *,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DBSubnetGroupMessage:
        """
        Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is
        specified, the list will contain only the descriptions of the specified
        DBSubnetGroup.

        For an overview of CIDR ranges, go to the [Wikipedia
        Tutorial](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
        """
        if _request is None:
            _params = {}
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDBSubnetGroupsMessage(**_params)
        paginator = self.get_paginator("describe_db_subnet_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DBSubnetGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DBSubnetGroupMessage.from_boto(response)

    def describe_engine_default_cluster_parameters(
        self,
        _request: shapes.DescribeEngineDefaultClusterParametersMessage = None,
        *,
        db_parameter_group_family: str,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEngineDefaultClusterParametersResult:
        """
        Returns the default engine and system parameter information for the cluster
        database engine.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_parameter_group_family is not ShapeBase.NOT_SET:
                _params['db_parameter_group_family'] = db_parameter_group_family
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEngineDefaultClusterParametersMessage(
                **_params
            )
        response = self._boto_client.describe_engine_default_cluster_parameters(
            **_request.to_boto()
        )

        return shapes.DescribeEngineDefaultClusterParametersResult.from_boto(
            response
        )

    def describe_engine_default_parameters(
        self,
        _request: shapes.DescribeEngineDefaultParametersMessage = None,
        *,
        db_parameter_group_family: str,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEngineDefaultParametersResult:
        """
        Returns the default engine and system parameter information for the specified
        database engine.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_family is not ShapeBase.NOT_SET:
                _params['db_parameter_group_family'] = db_parameter_group_family
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
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

    def describe_event_categories(
        self,
        _request: shapes.DescribeEventCategoriesMessage = None,
        *,
        source_type: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.EventCategoriesMessage:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source type. You can see a list of the event categories and source
        types in the [
        Events](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
        topic in the _Amazon RDS User Guide._
        """
        if _request is None:
            _params = {}
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeEventCategoriesMessage(**_params)
        response = self._boto_client.describe_event_categories(
            **_request.to_boto()
        )

        return shapes.EventCategoriesMessage.from_boto(response)

    def describe_event_subscriptions(
        self,
        _request: shapes.DescribeEventSubscriptionsMessage = None,
        *,
        subscription_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.EventSubscriptionsMessage:
        """
        Lists all the subscription descriptions for a customer account. The description
        for a subscription includes SubscriptionName, SNSTopicARN, CustomerID,
        SourceType, SourceID, CreationTime, and Status.

        If you specify a SubscriptionName, lists the description for that subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEventSubscriptionsMessage(**_params)
        paginator = self.get_paginator("describe_event_subscriptions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.EventSubscriptionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.EventSubscriptionsMessage.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsMessage = None,
        *,
        source_identifier: str = ShapeBase.NOT_SET,
        source_type: typing.Union[str, shapes.SourceType] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        duration: int = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.EventsMessage:
        """
        Returns events related to DB instances, DB security groups, DB snapshots, and DB
        parameter groups for the past 14 days. Events specific to a particular DB
        instance, DB security group, database snapshot, or DB parameter group can be
        obtained by providing the name as a parameter. By default, the past hour of
        events are returned.
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
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
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

    def describe_option_group_options(
        self,
        _request: shapes.DescribeOptionGroupOptionsMessage = None,
        *,
        engine_name: str,
        major_engine_version: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.OptionGroupOptionsMessage:
        """
        Describes all available options.
        """
        if _request is None:
            _params = {}
            if engine_name is not ShapeBase.NOT_SET:
                _params['engine_name'] = engine_name
            if major_engine_version is not ShapeBase.NOT_SET:
                _params['major_engine_version'] = major_engine_version
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeOptionGroupOptionsMessage(**_params)
        paginator = self.get_paginator("describe_option_group_options"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.OptionGroupOptionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.OptionGroupOptionsMessage.from_boto(response)

    def describe_option_groups(
        self,
        _request: shapes.DescribeOptionGroupsMessage = None,
        *,
        option_group_name: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        engine_name: str = ShapeBase.NOT_SET,
        major_engine_version: str = ShapeBase.NOT_SET,
    ) -> shapes.OptionGroups:
        """
        Describes the available option groups.
        """
        if _request is None:
            _params = {}
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if engine_name is not ShapeBase.NOT_SET:
                _params['engine_name'] = engine_name
            if major_engine_version is not ShapeBase.NOT_SET:
                _params['major_engine_version'] = major_engine_version
            _request = shapes.DescribeOptionGroupsMessage(**_params)
        paginator = self.get_paginator("describe_option_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.OptionGroups.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.OptionGroups.from_boto(response)

    def describe_orderable_db_instance_options(
        self,
        _request: shapes.DescribeOrderableDBInstanceOptionsMessage = None,
        *,
        engine: str,
        engine_version: str = ShapeBase.NOT_SET,
        db_instance_class: str = ShapeBase.NOT_SET,
        license_model: str = ShapeBase.NOT_SET,
        vpc: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.OrderableDBInstanceOptionsMessage:
        """
        Returns a list of orderable DB instance options for the specified engine.
        """
        if _request is None:
            _params = {}
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if license_model is not ShapeBase.NOT_SET:
                _params['license_model'] = license_model
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeOrderableDBInstanceOptionsMessage(
                **_params
            )
        paginator = self.get_paginator(
            "describe_orderable_db_instance_options"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.OrderableDBInstanceOptionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.OrderableDBInstanceOptionsMessage.from_boto(response)

    def describe_pending_maintenance_actions(
        self,
        _request: shapes.DescribePendingMaintenanceActionsMessage = None,
        *,
        resource_identifier: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
    ) -> shapes.PendingMaintenanceActionsMessage:
        """
        Returns a list of resources (for example, DB instances) that have at least one
        pending maintenance action.
        """
        if _request is None:
            _params = {}
            if resource_identifier is not ShapeBase.NOT_SET:
                _params['resource_identifier'] = resource_identifier
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            _request = shapes.DescribePendingMaintenanceActionsMessage(
                **_params
            )
        response = self._boto_client.describe_pending_maintenance_actions(
            **_request.to_boto()
        )

        return shapes.PendingMaintenanceActionsMessage.from_boto(response)

    def describe_reserved_db_instances(
        self,
        _request: shapes.DescribeReservedDBInstancesMessage = None,
        *,
        reserved_db_instance_id: str = ShapeBase.NOT_SET,
        reserved_db_instances_offering_id: str = ShapeBase.NOT_SET,
        db_instance_class: str = ShapeBase.NOT_SET,
        duration: str = ShapeBase.NOT_SET,
        product_description: str = ShapeBase.NOT_SET,
        offering_type: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReservedDBInstanceMessage:
        """
        Returns information about reserved DB instances for this account, or about a
        specified reserved DB instance.
        """
        if _request is None:
            _params = {}
            if reserved_db_instance_id is not ShapeBase.NOT_SET:
                _params['reserved_db_instance_id'] = reserved_db_instance_id
            if reserved_db_instances_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_db_instances_offering_id'
                       ] = reserved_db_instances_offering_id
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if product_description is not ShapeBase.NOT_SET:
                _params['product_description'] = product_description
            if offering_type is not ShapeBase.NOT_SET:
                _params['offering_type'] = offering_type
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReservedDBInstancesMessage(**_params)
        paginator = self.get_paginator("describe_reserved_db_instances"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReservedDBInstanceMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReservedDBInstanceMessage.from_boto(response)

    def describe_reserved_db_instances_offerings(
        self,
        _request: shapes.DescribeReservedDBInstancesOfferingsMessage = None,
        *,
        reserved_db_instances_offering_id: str = ShapeBase.NOT_SET,
        db_instance_class: str = ShapeBase.NOT_SET,
        duration: str = ShapeBase.NOT_SET,
        product_description: str = ShapeBase.NOT_SET,
        offering_type: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReservedDBInstancesOfferingMessage:
        """
        Lists available reserved DB instance offerings.
        """
        if _request is None:
            _params = {}
            if reserved_db_instances_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_db_instances_offering_id'
                       ] = reserved_db_instances_offering_id
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if product_description is not ShapeBase.NOT_SET:
                _params['product_description'] = product_description
            if offering_type is not ShapeBase.NOT_SET:
                _params['offering_type'] = offering_type
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReservedDBInstancesOfferingsMessage(
                **_params
            )
        paginator = self.get_paginator(
            "describe_reserved_db_instances_offerings"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReservedDBInstancesOfferingMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReservedDBInstancesOfferingMessage.from_boto(response)

    def describe_source_regions(
        self,
        _request: shapes.DescribeSourceRegionsMessage = None,
        *,
        region_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.SourceRegionMessage:
        """
        Returns a list of the source AWS Regions where the current AWS Region can create
        a Read Replica or copy a DB snapshot from. This API action supports pagination.
        """
        if _request is None:
            _params = {}
            if region_name is not ShapeBase.NOT_SET:
                _params['region_name'] = region_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeSourceRegionsMessage(**_params)
        response = self._boto_client.describe_source_regions(
            **_request.to_boto()
        )

        return shapes.SourceRegionMessage.from_boto(response)

    def describe_valid_db_instance_modifications(
        self,
        _request: shapes.DescribeValidDBInstanceModificationsMessage = None,
        *,
        db_instance_identifier: str,
    ) -> shapes.DescribeValidDBInstanceModificationsResult:
        """
        You can call DescribeValidDBInstanceModifications to learn what modifications
        you can make to your DB instance. You can use this information when you call
        ModifyDBInstance.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            _request = shapes.DescribeValidDBInstanceModificationsMessage(
                **_params
            )
        response = self._boto_client.describe_valid_db_instance_modifications(
            **_request.to_boto()
        )

        return shapes.DescribeValidDBInstanceModificationsResult.from_boto(
            response
        )

    def download_db_log_file_portion(
        self,
        _request: shapes.DownloadDBLogFilePortionMessage = None,
        *,
        db_instance_identifier: str,
        log_file_name: str,
        marker: str = ShapeBase.NOT_SET,
        number_of_lines: int = ShapeBase.NOT_SET,
    ) -> shapes.DownloadDBLogFilePortionDetails:
        """
        Downloads all or a portion of the specified log file, up to 1 MB in size.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if log_file_name is not ShapeBase.NOT_SET:
                _params['log_file_name'] = log_file_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if number_of_lines is not ShapeBase.NOT_SET:
                _params['number_of_lines'] = number_of_lines
            _request = shapes.DownloadDBLogFilePortionMessage(**_params)
        paginator = self.get_paginator("download_db_log_file_portion").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DownloadDBLogFilePortionDetails.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DownloadDBLogFilePortionDetails.from_boto(response)

    def failover_db_cluster(
        self,
        _request: shapes.FailoverDBClusterMessage = None,
        *,
        db_cluster_identifier: str = ShapeBase.NOT_SET,
        target_db_instance_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.FailoverDBClusterResult:
        """
        Forces a failover for a DB cluster.

        A failover for a DB cluster promotes one of the Aurora Replicas (read-only
        instances) in the DB cluster to be the primary instance (the cluster writer).

        Amazon Aurora will automatically fail over to an Aurora Replica, if one exists,
        when the primary instance fails. You can force a failover when you want to
        simulate a failure of a primary instance for testing. Because each instance in a
        DB cluster has its own endpoint address, you will need to clean up and re-
        establish any existing connections that use those endpoint addresses when the
        failover is complete.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if target_db_instance_identifier is not ShapeBase.NOT_SET:
                _params['target_db_instance_identifier'
                       ] = target_db_instance_identifier
            _request = shapes.FailoverDBClusterMessage(**_params)
        response = self._boto_client.failover_db_cluster(**_request.to_boto())

        return shapes.FailoverDBClusterResult.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceMessage = None,
        *,
        resource_name: str,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.TagListMessage:
        """
        Lists all tags on an Amazon RDS resource.

        For an overview on tagging an Amazon RDS resource, see [Tagging Amazon RDS
        Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Tagging.html)
        in the _Amazon RDS User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.ListTagsForResourceMessage(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.TagListMessage.from_boto(response)

    def modify_current_db_cluster_capacity(
        self,
        _request: shapes.ModifyCurrentDBClusterCapacityMessage = None,
        *,
        db_cluster_identifier: str,
        capacity: int = ShapeBase.NOT_SET,
        seconds_before_timeout: int = ShapeBase.NOT_SET,
        timeout_action: str = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterCapacityInfo:
        """
        Set the capacity of an Aurora Serverless DB cluster to a specific value.

        Aurora Serverless scales seamlessly based on the workload on the DB cluster. In
        some cases, the capacity might not scale fast enough to meet a sudden change in
        workload, such as a large number of new transactions. Call
        `ModifyCurrentDBClusterCapacity` to set the capacity explicitly.

        After this call sets the DB cluster capacity, Aurora Serverless can
        automatically scale the DB cluster based on the cooldown period for scaling up
        and the cooldown period for scaling down.

        For more information about Aurora Serverless, see [Using Amazon Aurora
        Serverless](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-
        serverless.html) in the _Amazon Aurora User Guide_.

        If you call `ModifyCurrentDBClusterCapacity` with the default `TimeoutAction`,
        connections that prevent Aurora Serverless from finding a scaling point might be
        dropped. For more information about scaling points, see [ Autoscaling for Aurora
        Serverless](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-
        serverless.how-it-works.html#aurora-serverless.how-it-works.auto-scaling) in the
        _Amazon Aurora User Guide_.
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if capacity is not ShapeBase.NOT_SET:
                _params['capacity'] = capacity
            if seconds_before_timeout is not ShapeBase.NOT_SET:
                _params['seconds_before_timeout'] = seconds_before_timeout
            if timeout_action is not ShapeBase.NOT_SET:
                _params['timeout_action'] = timeout_action
            _request = shapes.ModifyCurrentDBClusterCapacityMessage(**_params)
        response = self._boto_client.modify_current_db_cluster_capacity(
            **_request.to_boto()
        )

        return shapes.DBClusterCapacityInfo.from_boto(response)

    def modify_db_cluster(
        self,
        _request: shapes.ModifyDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
        new_db_cluster_identifier: str = ShapeBase.NOT_SET,
        apply_immediately: bool = ShapeBase.NOT_SET,
        backup_retention_period: int = ShapeBase.NOT_SET,
        db_cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        master_user_password: str = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        backtrack_window: int = ShapeBase.NOT_SET,
        cloudwatch_logs_export_configuration: shapes.
        CloudwatchLogsExportConfiguration = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        scaling_configuration: shapes.ScalingConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDBClusterResult:
        """
        Modify a setting for an Amazon Aurora DB cluster. You can change one or more
        database configuration parameters by specifying these parameters and the new
        values in the request. For more information on Amazon Aurora, see [ What Is
        Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if new_db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['new_db_cluster_identifier'] = new_db_cluster_identifier
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if backtrack_window is not ShapeBase.NOT_SET:
                _params['backtrack_window'] = backtrack_window
            if cloudwatch_logs_export_configuration is not ShapeBase.NOT_SET:
                _params['cloudwatch_logs_export_configuration'
                       ] = cloudwatch_logs_export_configuration
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if scaling_configuration is not ShapeBase.NOT_SET:
                _params['scaling_configuration'] = scaling_configuration
            _request = shapes.ModifyDBClusterMessage(**_params)
        response = self._boto_client.modify_db_cluster(**_request.to_boto())

        return shapes.ModifyDBClusterResult.from_boto(response)

    def modify_db_cluster_parameter_group(
        self,
        _request: shapes.ModifyDBClusterParameterGroupMessage = None,
        *,
        db_cluster_parameter_group_name: str,
        parameters: typing.List[shapes.Parameter],
    ) -> shapes.DBClusterParameterGroupNameMessage:
        """
        Modifies the parameters of a DB cluster parameter group. To modify more than one
        parameter, submit a list of the following: `ParameterName`, `ParameterValue`,
        and `ApplyMethod`. A maximum of 20 parameters can be modified in a single
        request.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._

        Changes to dynamic parameters are applied immediately. Changes to static
        parameters require a reboot without failover to the DB cluster associated with
        the parameter group before the change can take effect.

        After you create a DB cluster parameter group, you should wait at least 5
        minutes before creating your first DB cluster that uses that DB cluster
        parameter group as the default parameter group. This allows Amazon RDS to fully
        complete the create action before the parameter group is used as the default for
        a new DB cluster. This is especially important for parameters that are critical
        when creating the default database for a DB cluster, such as the character set
        for the default database defined by the `character_set_database` parameter. You
        can use the _Parameter Groups_ option of the [Amazon RDS
        console](https://console.aws.amazon.com/rds/) or the DescribeDBClusterParameters
        command to verify that your DB cluster parameter group has been created or
        modified.
        """
        if _request is None:
            _params = {}
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ModifyDBClusterParameterGroupMessage(**_params)
        response = self._boto_client.modify_db_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.DBClusterParameterGroupNameMessage.from_boto(response)

    def modify_db_cluster_snapshot_attribute(
        self,
        _request: shapes.ModifyDBClusterSnapshotAttributeMessage = None,
        *,
        db_cluster_snapshot_identifier: str,
        attribute_name: str,
        values_to_add: typing.List[str] = ShapeBase.NOT_SET,
        values_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDBClusterSnapshotAttributeResult:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB cluster snapshot.

        To share a manual DB cluster snapshot with other AWS accounts, specify `restore`
        as the `AttributeName` and use the `ValuesToAdd` parameter to add a list of IDs
        of the AWS accounts that are authorized to restore the manual DB cluster
        snapshot. Use the value `all` to make the manual DB cluster snapshot public,
        which means that it can be copied or restored by all AWS accounts. Do not add
        the `all` value for any manual DB cluster snapshots that contain private
        information that you don't want available to all AWS accounts. If a manual DB
        cluster snapshot is encrypted, it can be shared, but only by specifying a list
        of authorized AWS account IDs for the `ValuesToAdd` parameter. You can't use
        `all` as a value for that parameter in this case.

        To view which AWS accounts have access to copy or restore a manual DB cluster
        snapshot, or whether a manual DB cluster snapshot public or private, use the
        DescribeDBClusterSnapshotAttributes API action.
        """
        if _request is None:
            _params = {}
            if db_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_snapshot_identifier'
                       ] = db_cluster_snapshot_identifier
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if values_to_add is not ShapeBase.NOT_SET:
                _params['values_to_add'] = values_to_add
            if values_to_remove is not ShapeBase.NOT_SET:
                _params['values_to_remove'] = values_to_remove
            _request = shapes.ModifyDBClusterSnapshotAttributeMessage(**_params)
        response = self._boto_client.modify_db_cluster_snapshot_attribute(
            **_request.to_boto()
        )

        return shapes.ModifyDBClusterSnapshotAttributeResult.from_boto(response)

    def modify_db_instance(
        self,
        _request: shapes.ModifyDBInstanceMessage = None,
        *,
        db_instance_identifier: str,
        allocated_storage: int = ShapeBase.NOT_SET,
        db_instance_class: str = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        db_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        apply_immediately: bool = ShapeBase.NOT_SET,
        master_user_password: str = ShapeBase.NOT_SET,
        db_parameter_group_name: str = ShapeBase.NOT_SET,
        backup_retention_period: int = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        allow_major_version_upgrade: bool = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        license_model: str = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        new_db_instance_identifier: str = ShapeBase.NOT_SET,
        storage_type: str = ShapeBase.NOT_SET,
        tde_credential_arn: str = ShapeBase.NOT_SET,
        tde_credential_password: str = ShapeBase.NOT_SET,
        ca_certificate_identifier: str = ShapeBase.NOT_SET,
        domain: str = ShapeBase.NOT_SET,
        copy_tags_to_snapshot: bool = ShapeBase.NOT_SET,
        monitoring_interval: int = ShapeBase.NOT_SET,
        db_port_number: int = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        monitoring_role_arn: str = ShapeBase.NOT_SET,
        domain_iam_role_name: str = ShapeBase.NOT_SET,
        promotion_tier: int = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        enable_performance_insights: bool = ShapeBase.NOT_SET,
        performance_insights_kms_key_id: str = ShapeBase.NOT_SET,
        performance_insights_retention_period: int = ShapeBase.NOT_SET,
        cloudwatch_logs_export_configuration: shapes.
        CloudwatchLogsExportConfiguration = ShapeBase.NOT_SET,
        processor_features: typing.List[shapes.ProcessorFeature
                                       ] = ShapeBase.NOT_SET,
        use_default_processor_features: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDBInstanceResult:
        """
        Modifies settings for a DB instance. You can change one or more database
        configuration parameters by specifying these parameters and the new values in
        the request. To learn what modifications you can make to your DB instance, call
        DescribeValidDBInstanceModifications before you call ModifyDBInstance.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if allocated_storage is not ShapeBase.NOT_SET:
                _params['allocated_storage'] = allocated_storage
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if db_security_groups is not ShapeBase.NOT_SET:
                _params['db_security_groups'] = db_security_groups
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if allow_major_version_upgrade is not ShapeBase.NOT_SET:
                _params['allow_major_version_upgrade'
                       ] = allow_major_version_upgrade
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if license_model is not ShapeBase.NOT_SET:
                _params['license_model'] = license_model
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if new_db_instance_identifier is not ShapeBase.NOT_SET:
                _params['new_db_instance_identifier'
                       ] = new_db_instance_identifier
            if storage_type is not ShapeBase.NOT_SET:
                _params['storage_type'] = storage_type
            if tde_credential_arn is not ShapeBase.NOT_SET:
                _params['tde_credential_arn'] = tde_credential_arn
            if tde_credential_password is not ShapeBase.NOT_SET:
                _params['tde_credential_password'] = tde_credential_password
            if ca_certificate_identifier is not ShapeBase.NOT_SET:
                _params['ca_certificate_identifier'] = ca_certificate_identifier
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if copy_tags_to_snapshot is not ShapeBase.NOT_SET:
                _params['copy_tags_to_snapshot'] = copy_tags_to_snapshot
            if monitoring_interval is not ShapeBase.NOT_SET:
                _params['monitoring_interval'] = monitoring_interval
            if db_port_number is not ShapeBase.NOT_SET:
                _params['db_port_number'] = db_port_number
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if monitoring_role_arn is not ShapeBase.NOT_SET:
                _params['monitoring_role_arn'] = monitoring_role_arn
            if domain_iam_role_name is not ShapeBase.NOT_SET:
                _params['domain_iam_role_name'] = domain_iam_role_name
            if promotion_tier is not ShapeBase.NOT_SET:
                _params['promotion_tier'] = promotion_tier
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if enable_performance_insights is not ShapeBase.NOT_SET:
                _params['enable_performance_insights'
                       ] = enable_performance_insights
            if performance_insights_kms_key_id is not ShapeBase.NOT_SET:
                _params['performance_insights_kms_key_id'
                       ] = performance_insights_kms_key_id
            if performance_insights_retention_period is not ShapeBase.NOT_SET:
                _params['performance_insights_retention_period'
                       ] = performance_insights_retention_period
            if cloudwatch_logs_export_configuration is not ShapeBase.NOT_SET:
                _params['cloudwatch_logs_export_configuration'
                       ] = cloudwatch_logs_export_configuration
            if processor_features is not ShapeBase.NOT_SET:
                _params['processor_features'] = processor_features
            if use_default_processor_features is not ShapeBase.NOT_SET:
                _params['use_default_processor_features'
                       ] = use_default_processor_features
            _request = shapes.ModifyDBInstanceMessage(**_params)
        response = self._boto_client.modify_db_instance(**_request.to_boto())

        return shapes.ModifyDBInstanceResult.from_boto(response)

    def modify_db_parameter_group(
        self,
        _request: shapes.ModifyDBParameterGroupMessage = None,
        *,
        db_parameter_group_name: str,
        parameters: typing.List[shapes.Parameter],
    ) -> shapes.DBParameterGroupNameMessage:
        """
        Modifies the parameters of a DB parameter group. To modify more than one
        parameter, submit a list of the following: `ParameterName`, `ParameterValue`,
        and `ApplyMethod`. A maximum of 20 parameters can be modified in a single
        request.

        Changes to dynamic parameters are applied immediately. Changes to static
        parameters require a reboot without failover to the DB instance associated with
        the parameter group before the change can take effect.

        After you modify a DB parameter group, you should wait at least 5 minutes before
        creating your first DB instance that uses that DB parameter group as the default
        parameter group. This allows Amazon RDS to fully complete the modify action
        before the parameter group is used as the default for a new DB instance. This is
        especially important for parameters that are critical when creating the default
        database for a DB instance, such as the character set for the default database
        defined by the `character_set_database` parameter. You can use the _Parameter
        Groups_ option of the [Amazon RDS console](https://console.aws.amazon.com/rds/)
        or the _DescribeDBParameters_ command to verify that your DB parameter group has
        been created or modified.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ModifyDBParameterGroupMessage(**_params)
        response = self._boto_client.modify_db_parameter_group(
            **_request.to_boto()
        )

        return shapes.DBParameterGroupNameMessage.from_boto(response)

    def modify_db_snapshot(
        self,
        _request: shapes.ModifyDBSnapshotMessage = None,
        *,
        db_snapshot_identifier: str,
        engine_version: str = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDBSnapshotResult:
        """
        Updates a manual DB snapshot, which can be encrypted or not encrypted, with a
        new engine version.

        Amazon RDS supports upgrading DB snapshots for MySQL and Oracle.
        """
        if _request is None:
            _params = {}
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            _request = shapes.ModifyDBSnapshotMessage(**_params)
        response = self._boto_client.modify_db_snapshot(**_request.to_boto())

        return shapes.ModifyDBSnapshotResult.from_boto(response)

    def modify_db_snapshot_attribute(
        self,
        _request: shapes.ModifyDBSnapshotAttributeMessage = None,
        *,
        db_snapshot_identifier: str,
        attribute_name: str,
        values_to_add: typing.List[str] = ShapeBase.NOT_SET,
        values_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDBSnapshotAttributeResult:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB snapshot.

        To share a manual DB snapshot with other AWS accounts, specify `restore` as the
        `AttributeName` and use the `ValuesToAdd` parameter to add a list of IDs of the
        AWS accounts that are authorized to restore the manual DB snapshot. Uses the
        value `all` to make the manual DB snapshot public, which means it can be copied
        or restored by all AWS accounts. Do not add the `all` value for any manual DB
        snapshots that contain private information that you don't want available to all
        AWS accounts. If the manual DB snapshot is encrypted, it can be shared, but only
        by specifying a list of authorized AWS account IDs for the `ValuesToAdd`
        parameter. You can't use `all` as a value for that parameter in this case.

        To view which AWS accounts have access to copy or restore a manual DB snapshot,
        or whether a manual DB snapshot public or private, use the
        DescribeDBSnapshotAttributes API action.
        """
        if _request is None:
            _params = {}
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if values_to_add is not ShapeBase.NOT_SET:
                _params['values_to_add'] = values_to_add
            if values_to_remove is not ShapeBase.NOT_SET:
                _params['values_to_remove'] = values_to_remove
            _request = shapes.ModifyDBSnapshotAttributeMessage(**_params)
        response = self._boto_client.modify_db_snapshot_attribute(
            **_request.to_boto()
        )

        return shapes.ModifyDBSnapshotAttributeResult.from_boto(response)

    def modify_db_subnet_group(
        self,
        _request: shapes.ModifyDBSubnetGroupMessage = None,
        *,
        db_subnet_group_name: str,
        subnet_ids: typing.List[str],
        db_subnet_group_description: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDBSubnetGroupResult:
        """
        Modifies an existing DB subnet group. DB subnet groups must contain at least one
        subnet in at least two AZs in the AWS Region.
        """
        if _request is None:
            _params = {}
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if db_subnet_group_description is not ShapeBase.NOT_SET:
                _params['db_subnet_group_description'
                       ] = db_subnet_group_description
            _request = shapes.ModifyDBSubnetGroupMessage(**_params)
        response = self._boto_client.modify_db_subnet_group(
            **_request.to_boto()
        )

        return shapes.ModifyDBSubnetGroupResult.from_boto(response)

    def modify_event_subscription(
        self,
        _request: shapes.ModifyEventSubscriptionMessage = None,
        *,
        subscription_name: str,
        sns_topic_arn: str = ShapeBase.NOT_SET,
        source_type: str = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyEventSubscriptionResult:
        """
        Modifies an existing RDS event notification subscription. Note that you can't
        modify the source identifiers using this call; to change source identifiers for
        a subscription, use the AddSourceIdentifierToSubscription and
        RemoveSourceIdentifierFromSubscription calls.

        You can see a list of the event categories for a given SourceType in the
        [Events](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
        topic in the _Amazon RDS User Guide_ or by using the **DescribeEventCategories**
        action.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.ModifyEventSubscriptionMessage(**_params)
        response = self._boto_client.modify_event_subscription(
            **_request.to_boto()
        )

        return shapes.ModifyEventSubscriptionResult.from_boto(response)

    def modify_option_group(
        self,
        _request: shapes.ModifyOptionGroupMessage = None,
        *,
        option_group_name: str,
        options_to_include: typing.List[shapes.OptionConfiguration
                                       ] = ShapeBase.NOT_SET,
        options_to_remove: typing.List[str] = ShapeBase.NOT_SET,
        apply_immediately: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyOptionGroupResult:
        """
        Modifies an existing option group.
        """
        if _request is None:
            _params = {}
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if options_to_include is not ShapeBase.NOT_SET:
                _params['options_to_include'] = options_to_include
            if options_to_remove is not ShapeBase.NOT_SET:
                _params['options_to_remove'] = options_to_remove
            if apply_immediately is not ShapeBase.NOT_SET:
                _params['apply_immediately'] = apply_immediately
            _request = shapes.ModifyOptionGroupMessage(**_params)
        response = self._boto_client.modify_option_group(**_request.to_boto())

        return shapes.ModifyOptionGroupResult.from_boto(response)

    def promote_read_replica(
        self,
        _request: shapes.PromoteReadReplicaMessage = None,
        *,
        db_instance_identifier: str,
        backup_retention_period: int = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
    ) -> shapes.PromoteReadReplicaResult:
        """
        Promotes a Read Replica DB instance to a standalone DB instance.

          * Backup duration is a function of the amount of changes to the database since the previous backup. If you plan to promote a Read Replica to a standalone instance, we recommend that you enable backups and complete at least one backup prior to promotion. In addition, a Read Replica cannot be promoted to a standalone instance when it is in the `backing-up` status. If you have enabled backups on your Read Replica, configure the automated backup window so that daily backups do not interfere with Read Replica promotion.

          * This command doesn't apply to Aurora MySQL and Aurora PostgreSQL.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            _request = shapes.PromoteReadReplicaMessage(**_params)
        response = self._boto_client.promote_read_replica(**_request.to_boto())

        return shapes.PromoteReadReplicaResult.from_boto(response)

    def promote_read_replica_db_cluster(
        self,
        _request: shapes.PromoteReadReplicaDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
    ) -> shapes.PromoteReadReplicaDBClusterResult:
        """
        Promotes a Read Replica DB cluster to a standalone DB cluster.
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            _request = shapes.PromoteReadReplicaDBClusterMessage(**_params)
        response = self._boto_client.promote_read_replica_db_cluster(
            **_request.to_boto()
        )

        return shapes.PromoteReadReplicaDBClusterResult.from_boto(response)

    def purchase_reserved_db_instances_offering(
        self,
        _request: shapes.PurchaseReservedDBInstancesOfferingMessage = None,
        *,
        reserved_db_instances_offering_id: str,
        reserved_db_instance_id: str = ShapeBase.NOT_SET,
        db_instance_count: int = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseReservedDBInstancesOfferingResult:
        """
        Purchases a reserved DB instance offering.
        """
        if _request is None:
            _params = {}
            if reserved_db_instances_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_db_instances_offering_id'
                       ] = reserved_db_instances_offering_id
            if reserved_db_instance_id is not ShapeBase.NOT_SET:
                _params['reserved_db_instance_id'] = reserved_db_instance_id
            if db_instance_count is not ShapeBase.NOT_SET:
                _params['db_instance_count'] = db_instance_count
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.PurchaseReservedDBInstancesOfferingMessage(
                **_params
            )
        response = self._boto_client.purchase_reserved_db_instances_offering(
            **_request.to_boto()
        )

        return shapes.PurchaseReservedDBInstancesOfferingResult.from_boto(
            response
        )

    def reboot_db_instance(
        self,
        _request: shapes.RebootDBInstanceMessage = None,
        *,
        db_instance_identifier: str,
        force_failover: bool = ShapeBase.NOT_SET,
    ) -> shapes.RebootDBInstanceResult:
        """
        You might need to reboot your DB instance, usually for maintenance reasons. For
        example, if you make certain modifications, or if you change the DB parameter
        group associated with the DB instance, you must reboot the instance for the
        changes to take effect.

        Rebooting a DB instance restarts the database engine service. Rebooting a DB
        instance results in a momentary outage, during which the DB instance status is
        set to rebooting.

        For more information about rebooting, see [Rebooting a DB
        Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html)
        in the _Amazon RDS User Guide._
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if force_failover is not ShapeBase.NOT_SET:
                _params['force_failover'] = force_failover
            _request = shapes.RebootDBInstanceMessage(**_params)
        response = self._boto_client.reboot_db_instance(**_request.to_boto())

        return shapes.RebootDBInstanceResult.from_boto(response)

    def remove_role_from_db_cluster(
        self,
        _request: shapes.RemoveRoleFromDBClusterMessage = None,
        *,
        db_cluster_identifier: str,
        role_arn: str,
    ) -> None:
        """
        Disassociates an Identity and Access Management (IAM) role from an Aurora DB
        cluster. For more information, see [Authorizing Amazon Aurora MySQL to Access
        Other AWS Services on Your Behalf
        ](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.html)
        in the _Amazon Aurora User Guide_.
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.RemoveRoleFromDBClusterMessage(**_params)
        response = self._boto_client.remove_role_from_db_cluster(
            **_request.to_boto()
        )

    def remove_source_identifier_from_subscription(
        self,
        _request: shapes.RemoveSourceIdentifierFromSubscriptionMessage = None,
        *,
        subscription_name: str,
        source_identifier: str,
    ) -> shapes.RemoveSourceIdentifierFromSubscriptionResult:
        """
        Removes a source identifier from an existing RDS event notification
        subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if source_identifier is not ShapeBase.NOT_SET:
                _params['source_identifier'] = source_identifier
            _request = shapes.RemoveSourceIdentifierFromSubscriptionMessage(
                **_params
            )
        response = self._boto_client.remove_source_identifier_from_subscription(
            **_request.to_boto()
        )

        return shapes.RemoveSourceIdentifierFromSubscriptionResult.from_boto(
            response
        )

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceMessage = None,
        *,
        resource_name: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes metadata tags from an Amazon RDS resource.

        For an overview on tagging an Amazon RDS resource, see [Tagging Amazon RDS
        Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Tagging.html)
        in the _Amazon RDS User Guide._
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

    def reset_db_cluster_parameter_group(
        self,
        _request: shapes.ResetDBClusterParameterGroupMessage = None,
        *,
        db_cluster_parameter_group_name: str,
        reset_all_parameters: bool = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
    ) -> shapes.DBClusterParameterGroupNameMessage:
        """
        Modifies the parameters of a DB cluster parameter group to the default value. To
        reset specific parameters submit a list of the following: `ParameterName` and
        `ApplyMethod`. To reset the entire DB cluster parameter group, specify the
        `DBClusterParameterGroupName` and `ResetAllParameters` parameters.

        When resetting the entire group, dynamic parameters are updated immediately and
        static parameters are set to `pending-reboot` to take effect on the next DB
        instance restart or RebootDBInstance request. You must call RebootDBInstance for
        every DB instance in your DB cluster that you want the updated static parameter
        to apply to.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if reset_all_parameters is not ShapeBase.NOT_SET:
                _params['reset_all_parameters'] = reset_all_parameters
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ResetDBClusterParameterGroupMessage(**_params)
        response = self._boto_client.reset_db_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.DBClusterParameterGroupNameMessage.from_boto(response)

    def reset_db_parameter_group(
        self,
        _request: shapes.ResetDBParameterGroupMessage = None,
        *,
        db_parameter_group_name: str,
        reset_all_parameters: bool = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
    ) -> shapes.DBParameterGroupNameMessage:
        """
        Modifies the parameters of a DB parameter group to the engine/system default
        value. To reset specific parameters, provide a list of the following:
        `ParameterName` and `ApplyMethod`. To reset the entire DB parameter group,
        specify the `DBParameterGroup` name and `ResetAllParameters` parameters. When
        resetting the entire group, dynamic parameters are updated immediately and
        static parameters are set to `pending-reboot` to take effect on the next DB
        instance restart or `RebootDBInstance` request.
        """
        if _request is None:
            _params = {}
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if reset_all_parameters is not ShapeBase.NOT_SET:
                _params['reset_all_parameters'] = reset_all_parameters
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ResetDBParameterGroupMessage(**_params)
        response = self._boto_client.reset_db_parameter_group(
            **_request.to_boto()
        )

        return shapes.DBParameterGroupNameMessage.from_boto(response)

    def restore_db_cluster_from_s3(
        self,
        _request: shapes.RestoreDBClusterFromS3Message = None,
        *,
        db_cluster_identifier: str,
        engine: str,
        master_username: str,
        master_user_password: str,
        source_engine: str,
        source_engine_version: str,
        s3_bucket_name: str,
        s3_ingestion_role_arn: str,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        backup_retention_period: int = ShapeBase.NOT_SET,
        character_set_name: str = ShapeBase.NOT_SET,
        database_name: str = ShapeBase.NOT_SET,
        db_cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        storage_encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        s3_prefix: str = ShapeBase.NOT_SET,
        backtrack_window: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.RestoreDBClusterFromS3Result:
        """
        Creates an Amazon Aurora DB cluster from data stored in an Amazon S3 bucket.
        Amazon RDS must be authorized to access the Amazon S3 bucket and the data must
        be created using the Percona XtraBackup utility as described in [ Migrating Data
        to an Amazon Aurora MySQL DB
        Cluster](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.html)
        in the _Amazon Aurora User Guide_.
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if master_username is not ShapeBase.NOT_SET:
                _params['master_username'] = master_username
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if source_engine is not ShapeBase.NOT_SET:
                _params['source_engine'] = source_engine
            if source_engine_version is not ShapeBase.NOT_SET:
                _params['source_engine_version'] = source_engine_version
            if s3_bucket_name is not ShapeBase.NOT_SET:
                _params['s3_bucket_name'] = s3_bucket_name
            if s3_ingestion_role_arn is not ShapeBase.NOT_SET:
                _params['s3_ingestion_role_arn'] = s3_ingestion_role_arn
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if character_set_name is not ShapeBase.NOT_SET:
                _params['character_set_name'] = character_set_name
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if db_cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_cluster_parameter_group_name'
                       ] = db_cluster_parameter_group_name
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if storage_encrypted is not ShapeBase.NOT_SET:
                _params['storage_encrypted'] = storage_encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if s3_prefix is not ShapeBase.NOT_SET:
                _params['s3_prefix'] = s3_prefix
            if backtrack_window is not ShapeBase.NOT_SET:
                _params['backtrack_window'] = backtrack_window
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            _request = shapes.RestoreDBClusterFromS3Message(**_params)
        response = self._boto_client.restore_db_cluster_from_s3(
            **_request.to_boto()
        )

        return shapes.RestoreDBClusterFromS3Result.from_boto(response)

    def restore_db_cluster_from_snapshot(
        self,
        _request: shapes.RestoreDBClusterFromSnapshotMessage = None,
        *,
        db_cluster_identifier: str,
        snapshot_identifier: str,
        engine: str,
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        database_name: str = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        backtrack_window: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        engine_mode: str = ShapeBase.NOT_SET,
        scaling_configuration: shapes.ScalingConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.RestoreDBClusterFromSnapshotResult:
        """
        Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        If a DB snapshot is specified, the target DB cluster is created from the source
        DB snapshot with a default configuration and default security group.

        If a DB cluster snapshot is specified, the target DB cluster is created from the
        source DB cluster restore point with the same configuration as the original
        source DB cluster, except that the new DB cluster is created with the default
        security group.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if database_name is not ShapeBase.NOT_SET:
                _params['database_name'] = database_name
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if backtrack_window is not ShapeBase.NOT_SET:
                _params['backtrack_window'] = backtrack_window
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if engine_mode is not ShapeBase.NOT_SET:
                _params['engine_mode'] = engine_mode
            if scaling_configuration is not ShapeBase.NOT_SET:
                _params['scaling_configuration'] = scaling_configuration
            _request = shapes.RestoreDBClusterFromSnapshotMessage(**_params)
        response = self._boto_client.restore_db_cluster_from_snapshot(
            **_request.to_boto()
        )

        return shapes.RestoreDBClusterFromSnapshotResult.from_boto(response)

    def restore_db_cluster_to_point_in_time(
        self,
        _request: shapes.RestoreDBClusterToPointInTimeMessage = None,
        *,
        db_cluster_identifier: str,
        source_db_cluster_identifier: str,
        restore_type: str = ShapeBase.NOT_SET,
        restore_to_time: datetime.datetime = ShapeBase.NOT_SET,
        use_latest_restorable_time: bool = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        backtrack_window: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.RestoreDBClusterToPointInTimeResult:
        """
        Restores a DB cluster to an arbitrary point in time. Users can restore to any
        point in time before `LatestRestorableTime` for up to `BackupRetentionPeriod`
        days. The target DB cluster is created from the source DB cluster with the same
        configuration as the original DB cluster, except that the new DB cluster is
        created with the default DB security group.

        This action only restores the DB cluster, not the DB instances for that DB
        cluster. You must invoke the CreateDBInstance action to create DB instances for
        the restored DB cluster, specifying the identifier of the restored DB cluster in
        `DBClusterIdentifier`. You can create DB instances only after the
        `RestoreDBClusterToPointInTime` action has completed and the DB cluster is
        available.

        For more information on Amazon Aurora, see [ What Is Amazon
        Aurora?](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
        in the _Amazon Aurora User Guide._
        """
        if _request is None:
            _params = {}
            if db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['db_cluster_identifier'] = db_cluster_identifier
            if source_db_cluster_identifier is not ShapeBase.NOT_SET:
                _params['source_db_cluster_identifier'
                       ] = source_db_cluster_identifier
            if restore_type is not ShapeBase.NOT_SET:
                _params['restore_type'] = restore_type
            if restore_to_time is not ShapeBase.NOT_SET:
                _params['restore_to_time'] = restore_to_time
            if use_latest_restorable_time is not ShapeBase.NOT_SET:
                _params['use_latest_restorable_time'
                       ] = use_latest_restorable_time
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if backtrack_window is not ShapeBase.NOT_SET:
                _params['backtrack_window'] = backtrack_window
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            _request = shapes.RestoreDBClusterToPointInTimeMessage(**_params)
        response = self._boto_client.restore_db_cluster_to_point_in_time(
            **_request.to_boto()
        )

        return shapes.RestoreDBClusterToPointInTimeResult.from_boto(response)

    def restore_db_instance_from_db_snapshot(
        self,
        _request: shapes.RestoreDBInstanceFromDBSnapshotMessage = None,
        *,
        db_instance_identifier: str,
        db_snapshot_identifier: str,
        db_instance_class: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        license_model: str = ShapeBase.NOT_SET,
        db_name: str = ShapeBase.NOT_SET,
        engine: str = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        storage_type: str = ShapeBase.NOT_SET,
        tde_credential_arn: str = ShapeBase.NOT_SET,
        tde_credential_password: str = ShapeBase.NOT_SET,
        domain: str = ShapeBase.NOT_SET,
        copy_tags_to_snapshot: bool = ShapeBase.NOT_SET,
        domain_iam_role_name: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        processor_features: typing.List[shapes.ProcessorFeature
                                       ] = ShapeBase.NOT_SET,
        use_default_processor_features: bool = ShapeBase.NOT_SET,
    ) -> shapes.RestoreDBInstanceFromDBSnapshotResult:
        """
        Creates a new DB instance from a DB snapshot. The target database is created
        from the source database restore point with the most of original configuration
        with the default security group and the default DB parameter group. By default,
        the new DB instance is created as a single-AZ deployment except when the
        instance is a SQL Server instance that has an option group that is associated
        with mirroring; in this case, the instance becomes a mirrored AZ deployment and
        not a single-AZ deployment.

        If your intent is to replace your original DB instance with the new, restored DB
        instance, then rename your original DB instance before you call the
        RestoreDBInstanceFromDBSnapshot action. RDS doesn't allow two DB instances with
        the same name. Once you have renamed your original DB instance with a different
        identifier, then you can pass the original name of the DB instance as the
        DBInstanceIdentifier in the call to the RestoreDBInstanceFromDBSnapshot action.
        The result is that you will replace the original DB instance with the DB
        instance created from the snapshot.

        If you are restoring from a shared manual DB snapshot, the
        `DBSnapshotIdentifier` must be the ARN of the shared DB snapshot.

        This command doesn't apply to Aurora MySQL and Aurora PostgreSQL. For Aurora,
        use RestoreDBClusterFromSnapshot.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if license_model is not ShapeBase.NOT_SET:
                _params['license_model'] = license_model
            if db_name is not ShapeBase.NOT_SET:
                _params['db_name'] = db_name
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if storage_type is not ShapeBase.NOT_SET:
                _params['storage_type'] = storage_type
            if tde_credential_arn is not ShapeBase.NOT_SET:
                _params['tde_credential_arn'] = tde_credential_arn
            if tde_credential_password is not ShapeBase.NOT_SET:
                _params['tde_credential_password'] = tde_credential_password
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if copy_tags_to_snapshot is not ShapeBase.NOT_SET:
                _params['copy_tags_to_snapshot'] = copy_tags_to_snapshot
            if domain_iam_role_name is not ShapeBase.NOT_SET:
                _params['domain_iam_role_name'] = domain_iam_role_name
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if processor_features is not ShapeBase.NOT_SET:
                _params['processor_features'] = processor_features
            if use_default_processor_features is not ShapeBase.NOT_SET:
                _params['use_default_processor_features'
                       ] = use_default_processor_features
            _request = shapes.RestoreDBInstanceFromDBSnapshotMessage(**_params)
        response = self._boto_client.restore_db_instance_from_db_snapshot(
            **_request.to_boto()
        )

        return shapes.RestoreDBInstanceFromDBSnapshotResult.from_boto(response)

    def restore_db_instance_from_s3(
        self,
        _request: shapes.RestoreDBInstanceFromS3Message = None,
        *,
        db_instance_identifier: str,
        db_instance_class: str,
        engine: str,
        source_engine: str,
        source_engine_version: str,
        s3_bucket_name: str,
        s3_ingestion_role_arn: str,
        db_name: str = ShapeBase.NOT_SET,
        allocated_storage: int = ShapeBase.NOT_SET,
        master_username: str = ShapeBase.NOT_SET,
        master_user_password: str = ShapeBase.NOT_SET,
        db_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        db_parameter_group_name: str = ShapeBase.NOT_SET,
        backup_retention_period: int = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        license_model: str = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        storage_type: str = ShapeBase.NOT_SET,
        storage_encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        copy_tags_to_snapshot: bool = ShapeBase.NOT_SET,
        monitoring_interval: int = ShapeBase.NOT_SET,
        monitoring_role_arn: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        s3_prefix: str = ShapeBase.NOT_SET,
        enable_performance_insights: bool = ShapeBase.NOT_SET,
        performance_insights_kms_key_id: str = ShapeBase.NOT_SET,
        performance_insights_retention_period: int = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        processor_features: typing.List[shapes.ProcessorFeature
                                       ] = ShapeBase.NOT_SET,
        use_default_processor_features: bool = ShapeBase.NOT_SET,
    ) -> shapes.RestoreDBInstanceFromS3Result:
        """
        Amazon Relational Database Service (Amazon RDS) supports importing MySQL
        databases by using backup files. You can create a backup of your on-premises
        database, store it on Amazon Simple Storage Service (Amazon S3), and then
        restore the backup file onto a new Amazon RDS DB instance running MySQL. For
        more information, see [Importing Data into an Amazon RDS MySQL DB
        Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
        in the _Amazon RDS User Guide._
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if source_engine is not ShapeBase.NOT_SET:
                _params['source_engine'] = source_engine
            if source_engine_version is not ShapeBase.NOT_SET:
                _params['source_engine_version'] = source_engine_version
            if s3_bucket_name is not ShapeBase.NOT_SET:
                _params['s3_bucket_name'] = s3_bucket_name
            if s3_ingestion_role_arn is not ShapeBase.NOT_SET:
                _params['s3_ingestion_role_arn'] = s3_ingestion_role_arn
            if db_name is not ShapeBase.NOT_SET:
                _params['db_name'] = db_name
            if allocated_storage is not ShapeBase.NOT_SET:
                _params['allocated_storage'] = allocated_storage
            if master_username is not ShapeBase.NOT_SET:
                _params['master_username'] = master_username
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if db_security_groups is not ShapeBase.NOT_SET:
                _params['db_security_groups'] = db_security_groups
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if db_parameter_group_name is not ShapeBase.NOT_SET:
                _params['db_parameter_group_name'] = db_parameter_group_name
            if backup_retention_period is not ShapeBase.NOT_SET:
                _params['backup_retention_period'] = backup_retention_period
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if license_model is not ShapeBase.NOT_SET:
                _params['license_model'] = license_model
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if storage_type is not ShapeBase.NOT_SET:
                _params['storage_type'] = storage_type
            if storage_encrypted is not ShapeBase.NOT_SET:
                _params['storage_encrypted'] = storage_encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if copy_tags_to_snapshot is not ShapeBase.NOT_SET:
                _params['copy_tags_to_snapshot'] = copy_tags_to_snapshot
            if monitoring_interval is not ShapeBase.NOT_SET:
                _params['monitoring_interval'] = monitoring_interval
            if monitoring_role_arn is not ShapeBase.NOT_SET:
                _params['monitoring_role_arn'] = monitoring_role_arn
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if s3_prefix is not ShapeBase.NOT_SET:
                _params['s3_prefix'] = s3_prefix
            if enable_performance_insights is not ShapeBase.NOT_SET:
                _params['enable_performance_insights'
                       ] = enable_performance_insights
            if performance_insights_kms_key_id is not ShapeBase.NOT_SET:
                _params['performance_insights_kms_key_id'
                       ] = performance_insights_kms_key_id
            if performance_insights_retention_period is not ShapeBase.NOT_SET:
                _params['performance_insights_retention_period'
                       ] = performance_insights_retention_period
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if processor_features is not ShapeBase.NOT_SET:
                _params['processor_features'] = processor_features
            if use_default_processor_features is not ShapeBase.NOT_SET:
                _params['use_default_processor_features'
                       ] = use_default_processor_features
            _request = shapes.RestoreDBInstanceFromS3Message(**_params)
        response = self._boto_client.restore_db_instance_from_s3(
            **_request.to_boto()
        )

        return shapes.RestoreDBInstanceFromS3Result.from_boto(response)

    def restore_db_instance_to_point_in_time(
        self,
        _request: shapes.RestoreDBInstanceToPointInTimeMessage = None,
        *,
        source_db_instance_identifier: str,
        target_db_instance_identifier: str,
        restore_time: datetime.datetime = ShapeBase.NOT_SET,
        use_latest_restorable_time: bool = ShapeBase.NOT_SET,
        db_instance_class: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        db_subnet_group_name: str = ShapeBase.NOT_SET,
        multi_az: bool = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        license_model: str = ShapeBase.NOT_SET,
        db_name: str = ShapeBase.NOT_SET,
        engine: str = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        option_group_name: str = ShapeBase.NOT_SET,
        copy_tags_to_snapshot: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        storage_type: str = ShapeBase.NOT_SET,
        tde_credential_arn: str = ShapeBase.NOT_SET,
        tde_credential_password: str = ShapeBase.NOT_SET,
        domain: str = ShapeBase.NOT_SET,
        domain_iam_role_name: str = ShapeBase.NOT_SET,
        enable_iam_database_authentication: bool = ShapeBase.NOT_SET,
        enable_cloudwatch_logs_exports: typing.List[str] = ShapeBase.NOT_SET,
        processor_features: typing.List[shapes.ProcessorFeature
                                       ] = ShapeBase.NOT_SET,
        use_default_processor_features: bool = ShapeBase.NOT_SET,
    ) -> shapes.RestoreDBInstanceToPointInTimeResult:
        """
        Restores a DB instance to an arbitrary point in time. You can restore to any
        point in time before the time identified by the LatestRestorableTime property.
        You can restore to a point up to the number of days specified by the
        BackupRetentionPeriod property.

        The target database is created with most of the original configuration, but in a
        system-selected Availability Zone, with the default security group, the default
        subnet group, and the default DB parameter group. By default, the new DB
        instance is created as a single-AZ deployment except when the instance is a SQL
        Server instance that has an option group that is associated with mirroring; in
        this case, the instance becomes a mirrored deployment and not a single-AZ
        deployment.

        This command doesn't apply to Aurora MySQL and Aurora PostgreSQL. For Aurora,
        use RestoreDBClusterToPointInTime.
        """
        if _request is None:
            _params = {}
            if source_db_instance_identifier is not ShapeBase.NOT_SET:
                _params['source_db_instance_identifier'
                       ] = source_db_instance_identifier
            if target_db_instance_identifier is not ShapeBase.NOT_SET:
                _params['target_db_instance_identifier'
                       ] = target_db_instance_identifier
            if restore_time is not ShapeBase.NOT_SET:
                _params['restore_time'] = restore_time
            if use_latest_restorable_time is not ShapeBase.NOT_SET:
                _params['use_latest_restorable_time'
                       ] = use_latest_restorable_time
            if db_instance_class is not ShapeBase.NOT_SET:
                _params['db_instance_class'] = db_instance_class
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if db_subnet_group_name is not ShapeBase.NOT_SET:
                _params['db_subnet_group_name'] = db_subnet_group_name
            if multi_az is not ShapeBase.NOT_SET:
                _params['multi_az'] = multi_az
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if license_model is not ShapeBase.NOT_SET:
                _params['license_model'] = license_model
            if db_name is not ShapeBase.NOT_SET:
                _params['db_name'] = db_name
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if option_group_name is not ShapeBase.NOT_SET:
                _params['option_group_name'] = option_group_name
            if copy_tags_to_snapshot is not ShapeBase.NOT_SET:
                _params['copy_tags_to_snapshot'] = copy_tags_to_snapshot
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if storage_type is not ShapeBase.NOT_SET:
                _params['storage_type'] = storage_type
            if tde_credential_arn is not ShapeBase.NOT_SET:
                _params['tde_credential_arn'] = tde_credential_arn
            if tde_credential_password is not ShapeBase.NOT_SET:
                _params['tde_credential_password'] = tde_credential_password
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if domain_iam_role_name is not ShapeBase.NOT_SET:
                _params['domain_iam_role_name'] = domain_iam_role_name
            if enable_iam_database_authentication is not ShapeBase.NOT_SET:
                _params['enable_iam_database_authentication'
                       ] = enable_iam_database_authentication
            if enable_cloudwatch_logs_exports is not ShapeBase.NOT_SET:
                _params['enable_cloudwatch_logs_exports'
                       ] = enable_cloudwatch_logs_exports
            if processor_features is not ShapeBase.NOT_SET:
                _params['processor_features'] = processor_features
            if use_default_processor_features is not ShapeBase.NOT_SET:
                _params['use_default_processor_features'
                       ] = use_default_processor_features
            _request = shapes.RestoreDBInstanceToPointInTimeMessage(**_params)
        response = self._boto_client.restore_db_instance_to_point_in_time(
            **_request.to_boto()
        )

        return shapes.RestoreDBInstanceToPointInTimeResult.from_boto(response)

    def revoke_db_security_group_ingress(
        self,
        _request: shapes.RevokeDBSecurityGroupIngressMessage = None,
        *,
        db_security_group_name: str,
        cidrip: str = ShapeBase.NOT_SET,
        ec2_security_group_name: str = ShapeBase.NOT_SET,
        ec2_security_group_id: str = ShapeBase.NOT_SET,
        ec2_security_group_owner_id: str = ShapeBase.NOT_SET,
    ) -> shapes.RevokeDBSecurityGroupIngressResult:
        """
        Revokes ingress from a DBSecurityGroup for previously authorized IP ranges or
        EC2 or VPC Security Groups. Required parameters for this API are one of CIDRIP,
        EC2SecurityGroupId for VPC, or (EC2SecurityGroupOwnerId and either
        EC2SecurityGroupName or EC2SecurityGroupId).
        """
        if _request is None:
            _params = {}
            if db_security_group_name is not ShapeBase.NOT_SET:
                _params['db_security_group_name'] = db_security_group_name
            if cidrip is not ShapeBase.NOT_SET:
                _params['cidrip'] = cidrip
            if ec2_security_group_name is not ShapeBase.NOT_SET:
                _params['ec2_security_group_name'] = ec2_security_group_name
            if ec2_security_group_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_id'] = ec2_security_group_id
            if ec2_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_owner_id'
                       ] = ec2_security_group_owner_id
            _request = shapes.RevokeDBSecurityGroupIngressMessage(**_params)
        response = self._boto_client.revoke_db_security_group_ingress(
            **_request.to_boto()
        )

        return shapes.RevokeDBSecurityGroupIngressResult.from_boto(response)

    def start_db_instance(
        self,
        _request: shapes.StartDBInstanceMessage = None,
        *,
        db_instance_identifier: str,
    ) -> shapes.StartDBInstanceResult:
        """
        Starts a DB instance that was stopped using the AWS console, the stop-db-
        instance AWS CLI command, or the StopDBInstance action. For more information,
        see Stopping and Starting a DB instance in the AWS RDS user guide.

        This command doesn't apply to Aurora MySQL and Aurora PostgreSQL.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            _request = shapes.StartDBInstanceMessage(**_params)
        response = self._boto_client.start_db_instance(**_request.to_boto())

        return shapes.StartDBInstanceResult.from_boto(response)

    def stop_db_instance(
        self,
        _request: shapes.StopDBInstanceMessage = None,
        *,
        db_instance_identifier: str,
        db_snapshot_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.StopDBInstanceResult:
        """
        Stops a DB instance. When you stop a DB instance, Amazon RDS retains the DB
        instance's metadata, including its endpoint, DB parameter group, and option
        group membership. Amazon RDS also retains the transaction logs so you can do a
        point-in-time restore if necessary. For more information, see Stopping and
        Starting a DB instance in the AWS RDS user guide.

        This command doesn't apply to Aurora MySQL and Aurora PostgreSQL.
        """
        if _request is None:
            _params = {}
            if db_instance_identifier is not ShapeBase.NOT_SET:
                _params['db_instance_identifier'] = db_instance_identifier
            if db_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['db_snapshot_identifier'] = db_snapshot_identifier
            _request = shapes.StopDBInstanceMessage(**_params)
        response = self._boto_client.stop_db_instance(**_request.to_boto())

        return shapes.StopDBInstanceResult.from_boto(response)
