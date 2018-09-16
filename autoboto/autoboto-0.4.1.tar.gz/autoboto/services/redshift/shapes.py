import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AcceptReservedNodeExchangeInputMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_id",
                "ReservedNodeId",
                TypeInfo(str),
            ),
            (
                "target_reserved_node_offering_id",
                "TargetReservedNodeOfferingId",
                TypeInfo(str),
            ),
        ]

    # A string representing the node identifier of the DC1 Reserved Node to be
    # exchanged.
    reserved_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the DC2 Reserved Node offering to be used for the
    # exchange. You can obtain the value for the parameter by calling
    # GetReservedNodeExchangeOfferings
    target_reserved_node_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AcceptReservedNodeExchangeOutputMessage(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "exchanged_reserved_node",
                "ExchangedReservedNode",
                TypeInfo(ReservedNode),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a reserved node. You can call the DescribeReservedNodeOfferings
    # API to obtain the available reserved node offerings.
    exchanged_reserved_node: "ReservedNode" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessToSnapshotDeniedFault(ShapeBase):
    """
    The owner of the specified snapshot has not authorized your account to access
    the snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AccountWithRestoreAccess(ShapeBase):
    """
    Describes an AWS customer account authorized to restore a snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "account_alias",
                "AccountAlias",
                TypeInfo(str),
            ),
        ]

    # The identifier of an AWS customer account authorized to restore a snapshot.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of an AWS support account authorized to restore a snapshot.
    # For AWS support, the identifier is `amazon-redshift-support`.
    account_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AuthorizationAlreadyExistsFault(ShapeBase):
    """
    The specified CIDR block or EC2 security group is already authorized for the
    specified cluster security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizationNotFoundFault(ShapeBase):
    """
    The specified CIDR IP range or EC2 security group is not authorized for the
    specified cluster security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizationQuotaExceededFault(ShapeBase):
    """
    The authorization quota for the cluster security group has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizeClusterSecurityGroupIngressMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "cidrip",
                "CIDRIP",
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

    # The name of the security group to which the ingress rule is added.
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IP range to be added the Amazon Redshift security group.
    cidrip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 security group to be added the Amazon Redshift security group.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account number of the owner of the security group specified by the
    # _EC2SecurityGroupName_ parameter. The AWS Access Key ID is not an
    # acceptable value.

    # Example: `111122223333`
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeClusterSecurityGroupIngressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_security_group",
                "ClusterSecurityGroup",
                TypeInfo(ClusterSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a security group.
    cluster_security_group: "ClusterSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeSnapshotAccessMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "account_with_restore_access",
                "AccountWithRestoreAccess",
                TypeInfo(str),
            ),
            (
                "snapshot_cluster_identifier",
                "SnapshotClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the snapshot the account is authorized to restore.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the AWS customer account authorized to restore the
    # specified snapshot.

    # To share a snapshot with AWS support, specify amazon-redshift-support.
    account_with_restore_access: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the cluster the snapshot was created from. This parameter
    # is required if your IAM user has a policy containing a snapshot resource
    # element that specifies anything other than * for the cluster name.
    snapshot_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeSnapshotAccessResult(OutputShapeBase):
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

    # Describes a snapshot.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AvailabilityZone(ShapeBase):
    """
    Describes an availability zone.
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
                "supported_platforms",
                "SupportedPlatforms",
                TypeInfo(typing.List[SupportedPlatform]),
            ),
        ]

    # The name of the availability zone.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    supported_platforms: typing.List["SupportedPlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BucketNotFoundFault(ShapeBase):
    """
    Could not find the specified S3 bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Cluster(ShapeBase):
    """
    Describes a cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "cluster_status",
                "ClusterStatus",
                TypeInfo(str),
            ),
            (
                "modify_status",
                "ModifyStatus",
                TypeInfo(str),
            ),
            (
                "master_username",
                "MasterUsername",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(Endpoint),
            ),
            (
                "cluster_create_time",
                "ClusterCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "automated_snapshot_retention_period",
                "AutomatedSnapshotRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "cluster_security_groups",
                "ClusterSecurityGroups",
                TypeInfo(typing.List[ClusterSecurityGroupMembership]),
            ),
            (
                "vpc_security_groups",
                "VpcSecurityGroups",
                TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
            (
                "cluster_parameter_groups",
                "ClusterParameterGroups",
                TypeInfo(typing.List[ClusterParameterGroupStatus]),
            ),
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
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
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "allow_version_upgrade",
                "AllowVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "encrypted",
                "Encrypted",
                TypeInfo(bool),
            ),
            (
                "restore_status",
                "RestoreStatus",
                TypeInfo(RestoreStatus),
            ),
            (
                "hsm_status",
                "HsmStatus",
                TypeInfo(HsmStatus),
            ),
            (
                "cluster_snapshot_copy_status",
                "ClusterSnapshotCopyStatus",
                TypeInfo(ClusterSnapshotCopyStatus),
            ),
            (
                "cluster_public_key",
                "ClusterPublicKey",
                TypeInfo(str),
            ),
            (
                "cluster_nodes",
                "ClusterNodes",
                TypeInfo(typing.List[ClusterNode]),
            ),
            (
                "elastic_ip_status",
                "ElasticIpStatus",
                TypeInfo(ElasticIpStatus),
            ),
            (
                "cluster_revision_number",
                "ClusterRevisionNumber",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "enhanced_vpc_routing",
                "EnhancedVpcRouting",
                TypeInfo(bool),
            ),
            (
                "iam_roles",
                "IamRoles",
                TypeInfo(typing.List[ClusterIamRole]),
            ),
            (
                "pending_actions",
                "PendingActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
            (
                "elastic_resize_number_of_node_options",
                "ElasticResizeNumberOfNodeOptions",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the cluster.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type for the nodes in the cluster.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the cluster. Possible values are the following:

    #   * `available`

    #   * `creating`

    #   * `deleting`

    #   * `final-snapshot`

    #   * `hardware-failure`

    #   * `incompatible-hsm`

    #   * `incompatible-network`

    #   * `incompatible-parameters`

    #   * `incompatible-restore`

    #   * `modifying`

    #   * `rebooting`

    #   * `renaming`

    #   * `resizing`

    #   * `rotating-keys`

    #   * `storage-full`

    #   * `updating-hsm`
    cluster_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a modify operation, if any, initiated for the cluster.
    modify_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The master user name for the cluster. This name is used to connect to the
    # database that is specified in the **DBName** parameter.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the initial database that was created when the cluster was
    # created. This same name is returned for the life of the cluster. If an
    # initial database was not specified, a database named `dev`dev was created
    # by default.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The connection endpoint.
    endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the cluster was created.
    cluster_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days that automatic cluster snapshots are retained.
    automated_snapshot_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of cluster security group that are associated with the cluster. Each
    # security group is represented by an element that contains
    # `ClusterSecurityGroup.Name` and `ClusterSecurityGroup.Status` subelements.

    # Cluster security groups are used when the cluster is not created in an
    # Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use
    # VPC security groups, which are listed by the **VpcSecurityGroups**
    # parameter.
    cluster_security_groups: typing.List["ClusterSecurityGroupMembership"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that
    # are associated with the cluster. This parameter is returned only if the
    # cluster is in a VPC.
    vpc_security_groups: typing.List["VpcSecurityGroupMembership"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The list of cluster parameter groups that are associated with this cluster.
    # Each parameter group in the list is returned with its status.
    cluster_parameter_groups: typing.List["ClusterParameterGroupStatus"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The name of the subnet group that is associated with the cluster. This
    # parameter is valid only when the cluster is in a VPC.
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the VPC the cluster is in, if the cluster is in a VPC.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Availability Zone in which the cluster is located.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The weekly time range, in Universal Coordinated Time (UTC), during which
    # system maintenance can occur.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that, if present, indicates that changes to the cluster are
    # pending. Specific pending changes are identified by subelements.
    pending_modified_values: "PendingModifiedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version ID of the Amazon Redshift engine that is running on the
    # cluster.
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value that, if `true`, indicates that major version upgrades will
    # be applied automatically to the cluster during the maintenance window.
    allow_version_upgrade: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of compute nodes in the cluster.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value that, if `true`, indicates that the cluster can be accessed
    # from a public network.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value that, if `true`, indicates that data in the cluster is
    # encrypted at rest.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that describes the status of a cluster restore action. This
    # parameter returns null if the cluster was not created by restoring a
    # snapshot.
    restore_status: "RestoreStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that reports whether the Amazon Redshift cluster has finished
    # applying any hardware security module (HSM) settings changes specified in a
    # modify cluster command.

    # Values: active, applying
    hsm_status: "HsmStatus" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that returns the destination region and retention period that are
    # configured for cross-region snapshot copy.
    cluster_snapshot_copy_status: "ClusterSnapshotCopyStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public key for the cluster.
    cluster_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The nodes in the cluster.
    cluster_nodes: typing.List["ClusterNode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the elastic IP (EIP) address.
    elastic_ip_status: "ElasticIpStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specific revision number of the database in the cluster.
    cluster_revision_number: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags for the cluster.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (AWS KMS) key ID of the encryption key used
    # to encrypt data in the cluster.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An option that specifies whether to create the cluster with enhanced VPC
    # routing enabled. To create a cluster that uses enhanced VPC routing, the
    # cluster must be in a VPC. For more information, see [Enhanced VPC
    # Routing](http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-
    # routing.html) in the Amazon Redshift Cluster Management Guide.

    # If this option is `true`, enhanced VPC routing is enabled.

    # Default: false
    enhanced_vpc_routing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of AWS Identity and Access Management (IAM) roles that can be used
    # by the cluster to access other AWS services.
    iam_roles: typing.List["ClusterIamRole"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Cluster operations that are waiting to be started.
    pending_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the maintenance track for the cluster.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the number of nodes the cluster can be resized to with the
    # elastic resize method.
    elastic_resize_number_of_node_options: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterAlreadyExistsFault(ShapeBase):
    """
    The account already has a cluster with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterCredentials(OutputShapeBase):
    """
    Temporary credentials with authorization to log on to an Amazon Redshift
    database.
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
                "db_user",
                "DbUser",
                TypeInfo(str),
            ),
            (
                "db_password",
                "DbPassword",
                TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A database user name that is authorized to log on to the database `DbName`
    # using the password `DbPassword`. If the specified DbUser exists in the
    # database, the new user name has the same database privileges as the the
    # user named in DbUser. By default, the user is added to PUBLIC. If the
    # `DbGroups` parameter is specifed, `DbUser` is added to the listed groups
    # for any sessions created using these credentials.
    db_user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A temporary password that authorizes the user name returned by `DbUser` to
    # log on to the database `DbName`.
    db_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the password in `DbPassword` expires.
    expiration: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterDbRevision(ShapeBase):
    """
    Describes a `ClusterDbRevision`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "current_database_revision",
                "CurrentDatabaseRevision",
                TypeInfo(str),
            ),
            (
                "database_revision_release_date",
                "DatabaseRevisionReleaseDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "revision_targets",
                "RevisionTargets",
                TypeInfo(typing.List[RevisionTarget]),
            ),
        ]

    # The unique identifier of the cluster.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string representing the current cluster version.
    current_database_revision: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date on which the database revision was released.
    database_revision_release_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `RevisionTarget` objects, where each object describes the
    # database revision that a cluster can be updated to.
    revision_targets: typing.List["RevisionTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterDbRevisionsMessage(OutputShapeBase):
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
                "cluster_db_revisions",
                "ClusterDbRevisions",
                TypeInfo(typing.List[ClusterDbRevision]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string representing the starting point for the next set of revisions. If
    # a value is returned in a response, you can retrieve the next set of
    # revisions by providing the value in the `marker` parameter and retrying the
    # command. If the `marker` field is empty, all revisions have already been
    # returned.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of revisions.
    cluster_db_revisions: typing.List["ClusterDbRevision"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterIamRole(ShapeBase):
    """
    An AWS Identity and Access Management (IAM) role that can be used by the
    associated Amazon Redshift cluster to access other AWS services.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_role_arn",
                "IamRoleArn",
                TypeInfo(str),
            ),
            (
                "apply_status",
                "ApplyStatus",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role, for example,
    # `arn:aws:iam::123456789012:role/RedshiftCopyUnload`.
    iam_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that describes the status of the IAM role's association with an
    # Amazon Redshift cluster.

    # The following are possible statuses and descriptions.

    #   * `in-sync`: The role is available for use by the cluster.

    #   * `adding`: The role is in the process of being associated with the cluster.

    #   * `removing`: The role is in the process of being disassociated with the cluster.
    apply_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterNode(ShapeBase):
    """
    The identifier of a node in a cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "node_role",
                "NodeRole",
                TypeInfo(str),
            ),
            (
                "private_ip_address",
                "PrivateIPAddress",
                TypeInfo(str),
            ),
            (
                "public_ip_address",
                "PublicIPAddress",
                TypeInfo(str),
            ),
        ]

    # Whether the node is a leader node or a compute node.
    node_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private IP address of a node within a cluster.
    private_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public IP address of a node within a cluster.
    public_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterNotFoundFault(ShapeBase):
    """
    The `ClusterIdentifier` parameter does not refer to an existing cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterOnLatestRevisionFault(ShapeBase):
    """
    Cluster is already on the latest database revision.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterParameterGroup(ShapeBase):
    """
    Describes a parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_group_family",
                "ParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the cluster parameter group.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster parameter group family that this cluster parameter
    # group is compatible with.
    parameter_group_family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags for the cluster parameter group.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterParameterGroupAlreadyExistsFault(ShapeBase):
    """
    A cluster parameter group with the same name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterParameterGroupDetails(OutputShapeBase):
    """
    Contains the output from the DescribeClusterParameters action.
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
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
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

    # A list of Parameter instances. Each instance lists the parameters of one
    # cluster parameter group.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ClusterParameterGroupDetails", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ClusterParameterGroupNameMessage(OutputShapeBase):
    """

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
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_group_status",
                "ParameterGroupStatus",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the cluster parameter group.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the parameter group. For example, if you made a change to a
    # parameter group name-value pair, then the change could be pending a reboot
    # of an associated cluster.
    parameter_group_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterParameterGroupNotFoundFault(ShapeBase):
    """
    The parameter group name does not refer to an existing parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterParameterGroupQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of cluster
    parameter groups. For information about increasing your quota, go to [Limits in
    Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-
    redshift-limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterParameterGroupStatus(ShapeBase):
    """
    Describes the status of a parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_apply_status",
                "ParameterApplyStatus",
                TypeInfo(str),
            ),
            (
                "cluster_parameter_status_list",
                "ClusterParameterStatusList",
                TypeInfo(typing.List[ClusterParameterStatus]),
            ),
        ]

    # The name of the cluster parameter group.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of parameter updates.
    parameter_apply_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of parameter statuses.

    # For more information about parameters and parameter groups, go to [Amazon
    # Redshift Parameter
    # Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # parameter-groups.html) in the _Amazon Redshift Cluster Management Guide_.
    cluster_parameter_status_list: typing.List["ClusterParameterStatus"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class ClusterParameterGroupsMessage(OutputShapeBase):
    """
    Contains the output from the DescribeClusterParameterGroups action.
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
                "parameter_groups",
                "ParameterGroups",
                TypeInfo(typing.List[ClusterParameterGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ClusterParameterGroup instances. Each instance describes one
    # cluster parameter group.
    parameter_groups: typing.List["ClusterParameterGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["ClusterParameterGroupsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ClusterParameterStatus(ShapeBase):
    """
    Describes the status of a parameter group.
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
                "parameter_apply_status",
                "ParameterApplyStatus",
                TypeInfo(str),
            ),
            (
                "parameter_apply_error_description",
                "ParameterApplyErrorDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the parameter that indicates whether the parameter is in sync
    # with the database, waiting for a cluster reboot, or encountered an error
    # when being applied.

    # The following are possible statuses and descriptions.

    #   * `in-sync`: The parameter value is in sync with the database.

    #   * `pending-reboot`: The parameter value will be applied after the cluster reboots.

    #   * `applying`: The parameter value is being applied to the database.

    #   * `invalid-parameter`: Cannot apply the parameter value because it has an invalid value or syntax.

    #   * `apply-deferred`: The parameter contains static property changes. The changes are deferred until the cluster reboots.

    #   * `apply-error`: Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.

    #   * `unknown-error`: Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
    parameter_apply_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error that prevented the parameter from being applied to the database.
    parameter_apply_error_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterQuotaExceededFault(ShapeBase):
    """
    The request would exceed the allowed number of cluster instances for this
    account. For information about increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSecurityGroup(ShapeBase):
    """
    Describes a security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
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
            (
                "ip_ranges",
                "IPRanges",
                TypeInfo(typing.List[IPRange]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the cluster security group to which the operation was applied.
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the security group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of EC2 security groups that are permitted to access clusters
    # associated with this cluster security group.
    ec2_security_groups: typing.List["EC2SecurityGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IP ranges (CIDR blocks) that are permitted to access clusters
    # associated with this cluster security group.
    ip_ranges: typing.List["IPRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags for the cluster security group.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterSecurityGroupAlreadyExistsFault(ShapeBase):
    """
    A cluster security group with the same name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSecurityGroupMembership(ShapeBase):
    """
    Describes a cluster security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The name of the cluster security group.
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the cluster security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterSecurityGroupMessage(OutputShapeBase):
    """

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
                "cluster_security_groups",
                "ClusterSecurityGroups",
                TypeInfo(typing.List[ClusterSecurityGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ClusterSecurityGroup instances.
    cluster_security_groups: typing.List["ClusterSecurityGroup"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    def paginate(
        self,
    ) -> typing.Generator["ClusterSecurityGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ClusterSecurityGroupNotFoundFault(ShapeBase):
    """
    The cluster security group name does not refer to an existing cluster security
    group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSecurityGroupQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of cluster
    security groups. For information about increasing your quota, go to [Limits in
    Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-
    redshift-limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSnapshotAlreadyExistsFault(ShapeBase):
    """
    The value specified as a snapshot identifier is already used by an existing
    snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSnapshotCopyStatus(ShapeBase):
    """
    Returns the destination region and retention period that are configured for
    cross-region snapshot copy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_region",
                "DestinationRegion",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "RetentionPeriod",
                TypeInfo(int),
            ),
            (
                "snapshot_copy_grant_name",
                "SnapshotCopyGrantName",
                TypeInfo(str),
            ),
        ]

    # The destination region that snapshots are automatically copied to when
    # cross-region snapshot copy is enabled.
    destination_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days that automated snapshots are retained in the destination
    # region after they are copied from a source region.
    retention_period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the snapshot copy grant.
    snapshot_copy_grant_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterSnapshotNotFoundFault(ShapeBase):
    """
    The snapshot identifier does not refer to an existing cluster snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSnapshotQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of cluster
    snapshots.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSubnetGroup(ShapeBase):
    """
    Describes a subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_group_status",
                "SubnetGroupStatus",
                TypeInfo(str),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[Subnet]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the cluster subnet group.
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the cluster subnet group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC ID of the cluster subnet group.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the cluster subnet group. Possible values are `Complete`,
    # `Incomplete` and `Invalid`.
    subnet_group_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the VPC Subnet elements.
    subnets: typing.List["Subnet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags for the cluster subnet group.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterSubnetGroupAlreadyExistsFault(ShapeBase):
    """
    A _ClusterSubnetGroupName_ is already used by an existing cluster subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSubnetGroupMessage(OutputShapeBase):
    """
    Contains the output from the DescribeClusterSubnetGroups action.
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
                "cluster_subnet_groups",
                "ClusterSubnetGroups",
                TypeInfo(typing.List[ClusterSubnetGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ClusterSubnetGroup instances.
    cluster_subnet_groups: typing.List["ClusterSubnetGroup"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    def paginate(self,
                ) -> typing.Generator["ClusterSubnetGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ClusterSubnetGroupNotFoundFault(ShapeBase):
    """
    The cluster subnet group name does not refer to an existing cluster subnet
    group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSubnetGroupQuotaExceededFault(ShapeBase):
    """
    The request would result in user exceeding the allowed number of cluster subnet
    groups. For information about increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterSubnetQuotaExceededFault(ShapeBase):
    """
    The request would result in user exceeding the allowed number of subnets in a
    cluster subnet groups. For information about increasing your quota, go to
    [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterVersion(ShapeBase):
    """
    Describes a cluster version, including the parameter group family and
    description of the version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "cluster_parameter_group_family",
                "ClusterParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The version number used by the cluster.
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster parameter group family for the cluster.
    cluster_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the cluster version.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterVersionsMessage(OutputShapeBase):
    """
    Contains the output from the DescribeClusterVersions action.
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
                "cluster_versions",
                "ClusterVersions",
                TypeInfo(typing.List[ClusterVersion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Version` elements.
    cluster_versions: typing.List["ClusterVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ClusterVersionsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ClustersMessage(OutputShapeBase):
    """
    Contains the output from the DescribeClusters action.
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
                "clusters",
                "Clusters",
                TypeInfo(typing.List[Cluster]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Cluster` objects, where each object describes one cluster.
    clusters: typing.List["Cluster"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ClustersMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CopyClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_snapshot_identifier",
                "SourceSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "target_snapshot_identifier",
                "TargetSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "source_snapshot_cluster_identifier",
                "SourceSnapshotClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier for the source snapshot.

    # Constraints:

    #   * Must be the identifier for a valid automated snapshot whose state is `available`.
    source_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier given to the new manual snapshot.

    # Constraints:

    #   * Cannot be null, empty, or blank.

    #   * Must contain from 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    #   * Must be unique for the AWS account that is making the request.
    target_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the cluster the source snapshot was created from. This
    # parameter is required if your IAM user has a policy containing a snapshot
    # resource element that specifies anything other than * for the cluster name.

    # Constraints:

    #   * Must be the identifier for a valid cluster.
    source_snapshot_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyClusterSnapshotResult(OutputShapeBase):
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

    # Describes a snapshot.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyToRegionDisabledFault(ShapeBase):
    """
    Cross-region snapshot copy was temporarily disabled. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "master_username",
                "MasterUsername",
                TypeInfo(str),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "cluster_type",
                "ClusterType",
                TypeInfo(str),
            ),
            (
                "cluster_security_groups",
                "ClusterSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "cluster_parameter_group_name",
                "ClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "automated_snapshot_retention_period",
                "AutomatedSnapshotRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "allow_version_upgrade",
                "AllowVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "encrypted",
                "Encrypted",
                TypeInfo(bool),
            ),
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
            (
                "elastic_ip",
                "ElasticIp",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "enhanced_vpc_routing",
                "EnhancedVpcRouting",
                TypeInfo(bool),
            ),
            (
                "additional_info",
                "AdditionalInfo",
                TypeInfo(str),
            ),
            (
                "iam_roles",
                "IamRoles",
                TypeInfo(typing.List[str]),
            ),
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
        ]

    # A unique identifier for the cluster. You use this identifier to refer to
    # the cluster for any subsequent cluster operations such as deleting or
    # modifying. The identifier also appears in the Amazon Redshift console.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * Alphabetic characters must be lowercase.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    #   * Must be unique for all clusters within an AWS account.

    # Example: `myexamplecluster`
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type to be provisioned for the cluster. For information about node
    # types, go to [ Working with
    # Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # clusters.html#how-many-nodes) in the _Amazon Redshift Cluster Management
    # Guide_.

    # Valid Values: `ds2.xlarge` | `ds2.8xlarge` | `ds2.xlarge` | `ds2.8xlarge` |
    # `dc1.large` | `dc1.8xlarge` | `dc2.large` | `dc2.8xlarge`
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name associated with the master user account for the cluster that
    # is being created.

    # Constraints:

    #   * Must be 1 - 128 alphanumeric characters. The user name can't be `PUBLIC`.

    #   * First character must be a letter.

    #   * Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password associated with the master user account for the cluster that
    # is being created.

    # Constraints:

    #   * Must be between 8 and 64 characters in length.

    #   * Must contain at least one uppercase letter.

    #   * Must contain at least one lowercase letter.

    #   * Must contain one number.

    #   * Can be any printable ASCII character (ASCII code 33 to 126) except ' (single quote), " (double quote), \, /, @, or space.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the first database to be created when the cluster is created.

    # To create additional databases after the cluster is created, connect to the
    # cluster with a SQL client and use SQL commands to create a database. For
    # more information, go to [Create a
    # Database](http://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html)
    # in the Amazon Redshift Database Developer Guide.

    # Default: `dev`

    # Constraints:

    #   * Must contain 1 to 64 alphanumeric characters.

    #   * Must contain only lowercase letters.

    #   * Cannot be a word that is reserved by the service. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the cluster. When cluster type is specified as

    #   * `single-node`, the **NumberOfNodes** parameter is not required.

    #   * `multi-node`, the **NumberOfNodes** parameter is required.

    # Valid Values: `multi-node` | `single-node`

    # Default: `multi-node`
    cluster_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of security groups to be associated with this cluster.

    # Default: The default cluster security group for Amazon Redshift.
    cluster_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of Virtual Private Cloud (VPC) security groups to be associated with
    # the cluster.

    # Default: The default VPC security group is associated with the cluster.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a cluster subnet group to be associated with this cluster.

    # If this parameter is not provided the resulting cluster will be deployed
    # outside virtual private cloud (VPC).
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 Availability Zone (AZ) in which you want Amazon Redshift to
    # provision the cluster. For example, if you have several EC2 instances
    # running in a specific Availability Zone, then you might want the cluster to
    # be provisioned in the same zone in order to decrease network latency.

    # Default: A random, system-chosen Availability Zone in the region that is
    # specified by the endpoint.

    # Example: `us-east-1d`

    # Constraint: The specified Availability Zone must be in the same region as
    # the current endpoint.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The weekly time range (in UTC) during which automated cluster maintenance
    # can occur.

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # Default: A 30-minute window selected at random from an 8-hour block of time
    # per region, occurring on a random day of the week. For more information
    # about the time blocks for each region, see [Maintenance
    # Windows](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # clusters.html#rs-maintenance-windows) in Amazon Redshift Cluster Management
    # Guide.

    # Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the parameter group to be associated with this cluster.

    # Default: The default Amazon Redshift cluster parameter group. For
    # information about the default parameter group, go to [Working with Amazon
    # Redshift Parameter
    # Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # parameter-groups.html)

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days that automated snapshots are retained. If the value is
    # 0, automated snapshots are disabled. Even if automated snapshots are
    # disabled, you can still create manual snapshots when you want with
    # CreateClusterSnapshot.

    # Default: `1`

    # Constraints: Must be a value from 0 to 35.
    automated_snapshot_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which the cluster accepts incoming connections.

    # The cluster is accessible only via the JDBC and ODBC connection strings.
    # Part of the connection string requires the port on which the cluster will
    # listen for incoming connections.

    # Default: `5439`

    # Valid Values: `1150-65535`
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the Amazon Redshift engine software that you want to deploy
    # on the cluster.

    # The version selected runs on all the nodes in the cluster.

    # Constraints: Only version 1.0 is currently available.

    # Example: `1.0`
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, major version upgrades can be applied during the maintenance
    # window to the Amazon Redshift engine that is running on the cluster.

    # When a new major version of the Amazon Redshift engine is released, you can
    # request that the service automatically apply upgrades during the
    # maintenance window to the Amazon Redshift engine that is running on your
    # cluster.

    # Default: `true`
    allow_version_upgrade: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of compute nodes in the cluster. This parameter is required when
    # the **ClusterType** parameter is specified as `multi-node`.

    # For information about determining how many nodes you need, go to [ Working
    # with Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-
    # with-clusters.html#how-many-nodes) in the _Amazon Redshift Cluster
    # Management Guide_.

    # If you don't specify this parameter, you get a single-node cluster. When
    # requesting a multi-node cluster, you must specify the number of nodes that
    # you want in the cluster.

    # Default: `1`

    # Constraints: Value must be at least 1 and no more than 100.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, the cluster can be accessed from a public network.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, the data in the cluster is encrypted at rest.

    # Default: false
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the HSM client certificate the Amazon Redshift
    # cluster uses to retrieve the data encryption keys stored in an HSM.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the HSM configuration that contains the information
    # the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Elastic IP (EIP) address for the cluster.

    # Constraints: The cluster must be provisioned in EC2-VPC and publicly-
    # accessible through an Internet gateway. For more information about
    # provisioning clusters in EC2-VPC, go to [Supported Platforms to Launch Your
    # Cluster](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # clusters.html#cluster-platforms) in the Amazon Redshift Cluster Management
    # Guide.
    elastic_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (KMS) key ID of the encryption key that you
    # want to use to encrypt data in the cluster.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An option that specifies whether to create the cluster with enhanced VPC
    # routing enabled. To create a cluster that uses enhanced VPC routing, the
    # cluster must be in a VPC. For more information, see [Enhanced VPC
    # Routing](http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-
    # routing.html) in the Amazon Redshift Cluster Management Guide.

    # If this option is `true`, enhanced VPC routing is enabled.

    # Default: false
    enhanced_vpc_routing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved.
    additional_info: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of AWS Identity and Access Management (IAM) roles that can be used
    # by the cluster to access other AWS services. You must supply the IAM roles
    # in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM
    # roles in a single request.

    # A cluster can have up to 10 IAM roles associated with it at any time.
    iam_roles: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter for the name of the maintenance track for the
    # cluster. If you don't provide a maintenance track name, the cluster is
    # assigned to the `current` track.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_group_family",
                "ParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the cluster parameter group.

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters or hyphens

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    #   * Must be unique withing your AWS account.

    # This value is stored as a lower-case string.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Redshift engine version to which the cluster parameter group
    # applies. The cluster engine version determines the set of parameters.

    # To get a list of valid parameter group family names, you can call
    # DescribeClusterParameterGroups. By default, Amazon Redshift returns a list
    # of all the parameter groups that are owned by your AWS account, including
    # the default parameter groups for each Amazon Redshift engine version. The
    # parameter group family names associated with the default parameter groups
    # provide you the valid values. For example, a valid family name is
    # "redshift-1.0".
    parameter_group_family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterParameterGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_parameter_group",
                "ClusterParameterGroup",
                TypeInfo(ClusterParameterGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a parameter group.
    cluster_parameter_group: "ClusterParameterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateClusterResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterSecurityGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the security group. Amazon Redshift stores the value as a
    # lowercase string.

    # Constraints:

    #   * Must contain no more than 255 alphanumeric characters or hyphens.

    #   * Must not be "Default".

    #   * Must be unique for all security groups that are created by your AWS account.

    # Example: `examplesecuritygroup`
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the security group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterSecurityGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_security_group",
                "ClusterSecurityGroup",
                TypeInfo(ClusterSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a security group.
    cluster_security_group: "ClusterSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # A unique identifier for the snapshot that you are requesting. This
    # identifier must be unique for all snapshots within the AWS account.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 alphanumeric characters or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-snapshot-id`
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cluster identifier for which you want a snapshot.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterSnapshotResult(OutputShapeBase):
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

    # Describes a snapshot.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the subnet group. Amazon Redshift stores the value as a
    # lowercase string.

    # Constraints:

    #   * Must contain no more than 255 alphanumeric characters or hyphens.

    #   * Must not be "Default".

    #   * Must be unique for all subnet groups that are created by your AWS account.

    # Example: `examplesubnetgroup`
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the subnet group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a
    # single request.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterSubnetGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_subnet_group",
                "ClusterSubnetGroup",
                TypeInfo(ClusterSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a subnet group.
    cluster_subnet_group: "ClusterSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateEventSubscriptionMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(str),
            ),
            (
                "source_ids",
                "SourceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the event subscription to be created.

    # Constraints:

    #   * Cannot be null, empty, or blank.

    #   * Must contain from 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the
    # event notifications. The ARN is created by Amazon SNS when you create a
    # topic and subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of source that will be generating the events. For example, if you
    # want to be notified of events generated by a cluster, you would set this
    # parameter to cluster. If this value is not specified, events are returned
    # for all Amazon Redshift objects in your AWS account. You must specify a
    # source type in order to specify source IDs.

    # Valid values: cluster, cluster-parameter-group, cluster-security-group, and
    # cluster-snapshot.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of one or more identifiers of Amazon Redshift source objects. All of
    # the objects must be of the same type as was specified in the source type
    # parameter. The event subscription will return only events generated by the
    # specified objects. If not specified, then events are returned for all
    # objects within the source type specified.

    # Example: my-cluster-1, my-cluster-2

    # Example: my-snapshot-20131010
    source_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Amazon Redshift event categories to be published by the event
    # notification subscription.

    # Values: Configuration, Management, Monitoring, Security
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Amazon Redshift event severity to be published by the event
    # notification subscription.

    # Values: ERROR, INFO
    severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value; set to `true` to activate the subscription, set to `false`
    # to create the subscription but not active it.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEventSubscriptionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_subscription",
                "EventSubscription",
                TypeInfo(EventSubscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes event subscriptions.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateHsmClientCertificateMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier to be assigned to the new HSM client certificate that the
    # cluster will use to connect to the HSM to use the database encryption keys.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHsmClientCertificateResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hsm_client_certificate",
                "HsmClientCertificate",
                TypeInfo(HsmClientCertificate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns information about an HSM client certificate. The certificate is
    # stored in a secure Hardware Storage Module (HSM), and used by the Amazon
    # Redshift cluster to encrypt data files.
    hsm_client_certificate: "HsmClientCertificate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateHsmConfigurationMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hsm_ip_address",
                "HsmIpAddress",
                TypeInfo(str),
            ),
            (
                "hsm_partition_name",
                "HsmPartitionName",
                TypeInfo(str),
            ),
            (
                "hsm_partition_password",
                "HsmPartitionPassword",
                TypeInfo(str),
            ),
            (
                "hsm_server_public_certificate",
                "HsmServerPublicCertificate",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier to be assigned to the new Amazon Redshift HSM configuration.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A text description of the HSM configuration to be created.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address that the Amazon Redshift cluster must use to access the HSM.
    hsm_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the partition in the HSM where the Amazon Redshift clusters
    # will store their database encryption keys.
    hsm_partition_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password required to access the HSM partition.
    hsm_partition_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HSMs public certificate file. When using Cloud HSM, the file name is
    # server.pem.
    hsm_server_public_certificate: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHsmConfigurationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hsm_configuration",
                "HsmConfiguration",
                TypeInfo(HsmConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns information about an HSM configuration, which is an object that
    # describes to Amazon Redshift clusters the information they require to
    # connect to an HSM where they can store database encryption keys.
    hsm_configuration: "HsmConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSnapshotCopyGrantMessage(ShapeBase):
    """
    The result of the `CreateSnapshotCopyGrant` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_copy_grant_name",
                "SnapshotCopyGrantName",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the snapshot copy grant. This name must be unique in the region
    # for the AWS account.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * Alphabetic characters must be lowercase.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    #   * Must be unique for all clusters within an AWS account.
    snapshot_copy_grant_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the customer master key (CMK) to which to grant
    # Amazon Redshift permission. If no key is specified, the default key is
    # used.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotCopyGrantResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "snapshot_copy_grant",
                "SnapshotCopyGrant",
                TypeInfo(SnapshotCopyGrant),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The snapshot copy grant that grants Amazon Redshift permission to encrypt
    # copied snapshots with the specified customer master key (CMK) from AWS KMS
    # in the destination region.

    # For more information about managing snapshot copy grants, go to [Amazon
    # Redshift Database
    # Encryption](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # db-encryption.html) in the _Amazon Redshift Cluster Management Guide_.
    snapshot_copy_grant: "SnapshotCopyGrant" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTagsMessage(ShapeBase):
    """
    Contains the output from the `CreateTags` action.
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

    # The Amazon Resource Name (ARN) to which you want to add the tag or tags.
    # For example, `arn:aws:redshift:us-east-1:123456789:cluster:t1`.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more name/value pairs to add as tags to the specified resource. Each
    # tag name is passed in with the parameter `Key` and the corresponding value
    # is passed in with the parameter `Value`. The `Key` and `Value` parameters
    # are separated by a comma (,). Separate multiple tags with a space. For
    # example, `--tags "Key"="owner","Value"="admin"
    # "Key"="environment","Value"="test" "Key"="version","Value"="1.0"`.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DefaultClusterParameters(ShapeBase):
    """
    Describes the default cluster parameters for a parameter group family.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_family",
                "ParameterGroupFamily",
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
        ]

    # The name of the cluster parameter group family to which the engine default
    # parameters apply.
    parameter_group_family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of cluster default parameters.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "skip_final_cluster_snapshot",
                "SkipFinalClusterSnapshot",
                TypeInfo(bool),
            ),
            (
                "final_cluster_snapshot_identifier",
                "FinalClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster to be deleted.

    # Constraints:

    #   * Must contain lowercase characters.

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines whether a final snapshot of the cluster is created before Amazon
    # Redshift deletes the cluster. If `true`, a final cluster snapshot is not
    # created. If `false`, a final cluster snapshot is created before the cluster
    # is deleted.

    # The _FinalClusterSnapshotIdentifier_ parameter must be specified if
    # _SkipFinalClusterSnapshot_ is `false`.

    # Default: `false`
    skip_final_cluster_snapshot: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the final snapshot that is to be created immediately
    # before deleting the cluster. If this parameter is provided,
    # _SkipFinalClusterSnapshot_ must be `false`.

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    final_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter group to be deleted.

    # Constraints:

    #   * Must be the name of an existing cluster parameter group.

    #   * Cannot delete a default cluster parameter group.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClusterResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClusterSecurityGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the cluster security group to be deleted.
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_cluster_identifier",
                "SnapshotClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the manual snapshot to be deleted.

    # Constraints: Must be the name of an existing snapshot that is in the
    # `available` state.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the cluster the snapshot was created from. This
    # parameter is required if your IAM user has a policy containing a snapshot
    # resource element that specifies anything other than * for the cluster name.

    # Constraints: Must be the name of valid cluster.
    snapshot_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteClusterSnapshotResult(OutputShapeBase):
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

    # Describes a snapshot.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClusterSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the cluster subnet group name to be deleted.
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEventSubscriptionMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon Redshift event notification subscription to be
    # deleted.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteHsmClientCertificateMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the HSM client certificate to be deleted.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteHsmConfigurationMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the Amazon Redshift HSM configuration to be deleted.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSnapshotCopyGrantMessage(ShapeBase):
    """
    The result of the `DeleteSnapshotCopyGrant` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_copy_grant_name",
                "SnapshotCopyGrantName",
                TypeInfo(str),
            ),
        ]

    # The name of the snapshot copy grant to delete.
    snapshot_copy_grant_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagsMessage(ShapeBase):
    """
    Contains the output from the `DeleteTags` action.
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

    # The Amazon Resource Name (ARN) from which you want to remove the tag or
    # tags. For example, `arn:aws:redshift:us-east-1:123456789:cluster:t1`.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag key that you want to delete.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DependentServiceRequestThrottlingFault(ShapeBase):
    """
    The request cannot be completed because a dependent service is throttling
    requests made by Amazon Redshift on your behalf. Wait and retry the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DependentServiceUnavailableFault(ShapeBase):
    """
    Your request cannot be completed because a dependent internal service is
    temporarily unavailable. Wait 30 to 60 seconds and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeClusterDbRevisionsMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
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

    # A unique identifier for a cluster whose `ClusterDbRevisions` you are
    # requesting. This parameter is case sensitive. All clusters defined for an
    # account are returned by default.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified MaxRecords
    # value, a value is returned in the `marker` field of the response. You can
    # retrieve the next set of response records by providing the returned
    # `marker` value in the `marker` parameter and retrying the request.

    # Default: 100

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point for returning a set
    # of response records. When the results of a `DescribeClusterDbRevisions`
    # request exceed the value specified in `MaxRecords`, Amazon Redshift returns
    # a value in the `marker` field of the response. You can retrieve the next
    # set of response records by providing the returned `marker` value in the
    # `marker` parameter and retrying the request.

    # Constraints: You can specify either the `ClusterIdentifier` parameter, or
    # the `marker` parameter, but not both.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterParameterGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of a specific parameter group for which to return details. By
    # default, details about all parameter groups and the default parameter group
    # are returned.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusterParameterGroups
    # request exceed the value specified in `MaxRecords`, AWS returns a value in
    # the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching cluster
    # parameter groups that are associated with the specified key or keys. For
    # example, suppose that you have parameter groups that are tagged with keys
    # called `owner` and `environment`. If you specify both of these tag keys in
    # the request, Amazon Redshift returns a response with the parameter groups
    # that have either or both of these tag keys associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching cluster
    # parameter groups that are associated with the specified tag value or
    # values. For example, suppose that you have parameter groups that are tagged
    # with values called `admin` and `test`. If you specify both of these tag
    # values in the request, Amazon Redshift returns a response with the
    # parameter groups that have either or both of these tag values associated
    # with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeClusterParametersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
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

    # The name of a cluster parameter group for which to return details.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameter types to return. Specify `user` to show parameters that are
    # different form the default. Similarly, specify `engine-default` to show
    # parameters that are the same as the default parameter group.

    # Default: All parameter types returned.

    # Valid Values: `user` | `engine-default`
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusterParameters request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterSecurityGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of a cluster security group for which you are requesting details.
    # You can specify either the **Marker** parameter or a
    # **ClusterSecurityGroupName** parameter, but not both.

    # Example: `securitygroup1`
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusterSecurityGroups
    # request exceed the value specified in `MaxRecords`, AWS returns a value in
    # the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.

    # Constraints: You can specify either the **ClusterSecurityGroupName**
    # parameter or the **Marker** parameter, but not both.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching cluster
    # security groups that are associated with the specified key or keys. For
    # example, suppose that you have security groups that are tagged with keys
    # called `owner` and `environment`. If you specify both of these tag keys in
    # the request, Amazon Redshift returns a response with the security groups
    # that have either or both of these tag keys associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching cluster
    # security groups that are associated with the specified tag value or values.
    # For example, suppose that you have security groups that are tagged with
    # values called `admin` and `test`. If you specify both of these tag values
    # in the request, Amazon Redshift returns a response with the security groups
    # that have either or both of these tag values associated with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeClusterSnapshotsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
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
                "owner_account",
                "OwnerAccount",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "cluster_exists",
                "ClusterExists",
                TypeInfo(bool),
            ),
        ]

    # The identifier of the cluster for which information about snapshots is
    # requested.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot identifier of the snapshot about which to return information.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of snapshots for which you are requesting information. By default,
    # snapshots of all types are returned.

    # Valid Values: `automated` | `manual`
    snapshot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that requests only snapshots created at or after the specified
    # time. The time value is specified in ISO 8601 format. For more information
    # about ISO 8601, go to the [ISO8601 Wikipedia
    # page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: `2012-07-16T18:00:00Z`
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A time value that requests only snapshots created at or before the
    # specified time. The time value is specified in ISO 8601 format. For more
    # information about ISO 8601, go to the [ISO8601 Wikipedia
    # page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: `2012-07-16T18:00:00Z`
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusterSnapshots request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS customer account used to create or copy the snapshot. Use this
    # field to filter the results to snapshots owned by a particular account. To
    # describe snapshots you own, either specify your AWS customer account, or do
    # not specify the parameter.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching cluster
    # snapshots that are associated with the specified key or keys. For example,
    # suppose that you have snapshots that are tagged with keys called `owner`
    # and `environment`. If you specify both of these tag keys in the request,
    # Amazon Redshift returns a response with the snapshots that have either or
    # both of these tag keys associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching cluster
    # snapshots that are associated with the specified tag value or values. For
    # example, suppose that you have snapshots that are tagged with values called
    # `admin` and `test`. If you specify both of these tag values in the request,
    # Amazon Redshift returns a response with the snapshots that have either or
    # both of these tag values associated with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates whether to return snapshots only for an existing
    # cluster. Table-level restore can be performed only using a snapshot of an
    # existing cluster, that is, a cluster that has not been deleted. If
    # `ClusterExists` is set to `true`, `ClusterIdentifier` is required.
    cluster_exists: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterSubnetGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the cluster subnet group for which information is requested.
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusterSubnetGroups request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching cluster subnet
    # groups that are associated with the specified key or keys. For example,
    # suppose that you have subnet groups that are tagged with keys called
    # `owner` and `environment`. If you specify both of these tag keys in the
    # request, Amazon Redshift returns a response with the subnet groups that
    # have either or both of these tag keys associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching cluster
    # subnet groups that are associated with the specified tag value or values.
    # For example, suppose that you have subnet groups that are tagged with
    # values called `admin` and `test`. If you specify both of these tag values
    # in the request, Amazon Redshift returns a response with the subnet groups
    # that have either or both of these tag values associated with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeClusterTracksMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
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

    # The name of the maintenance track.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An integer value for the maximum number of maintenance tracks to return.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a `DescribeClusterTracks` request
    # exceed the value specified in `MaxRecords`, Amazon Redshift returns a value
    # in the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterVersionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "cluster_parameter_group_family",
                "ClusterParameterGroupFamily",
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

    # The specific cluster version to return.

    # Example: `1.0`
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a specific cluster parameter group family to return details
    # for.

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    cluster_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusterVersions request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClustersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique identifier of a cluster whose properties you are requesting.
    # This parameter is case sensitive.

    # The default is that all clusters defined for an account are returned.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeClusters request exceed the
    # value specified in `MaxRecords`, AWS returns a value in the `Marker` field
    # of the response. You can retrieve the next set of response records by
    # providing the returned marker value in the `Marker` parameter and retrying
    # the request.

    # Constraints: You can specify either the **ClusterIdentifier** parameter or
    # the **Marker** parameter, but not both.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching clusters that
    # are associated with the specified key or keys. For example, suppose that
    # you have clusters that are tagged with keys called `owner` and
    # `environment`. If you specify both of these tag keys in the request, Amazon
    # Redshift returns a response with the clusters that have either or both of
    # these tag keys associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching clusters
    # that are associated with the specified tag value or values. For example,
    # suppose that you have clusters that are tagged with values called `admin`
    # and `test`. If you specify both of these tag values in the request, Amazon
    # Redshift returns a response with the clusters that have either or both of
    # these tag values associated with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDefaultClusterParametersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_family",
                "ParameterGroupFamily",
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

    # The name of the cluster parameter group family.
    parameter_group_family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeDefaultClusterParameters
    # request exceed the value specified in `MaxRecords`, AWS returns a value in
    # the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDefaultClusterParametersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "default_cluster_parameters",
                "DefaultClusterParameters",
                TypeInfo(DefaultClusterParameters),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the default cluster parameters for a parameter group family.
    default_cluster_parameters: "DefaultClusterParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeDefaultClusterParametersResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEventCategoriesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_type",
                "SourceType",
                TypeInfo(str),
            ),
        ]

    # The source type, such as cluster or parameter group, to which the described
    # event categories apply.

    # Valid values: cluster, cluster-snapshot, cluster-parameter-group, and
    # cluster-security-group.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventSubscriptionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Amazon Redshift event notification subscription to be
    # described.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeEventSubscriptions request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching event
    # notification subscriptions that are associated with the specified key or
    # keys. For example, suppose that you have subscriptions that are tagged with
    # keys called `owner` and `environment`. If you specify both of these tag
    # keys in the request, Amazon Redshift returns a response with the
    # subscriptions that have either or both of these tag keys associated with
    # them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching event
    # notification subscriptions that are associated with the specified tag value
    # or values. For example, suppose that you have subscriptions that are tagged
    # with values called `admin` and `test`. If you specify both of these tag
    # values in the request, Amazon Redshift returns a response with the
    # subscriptions that have either or both of these tag values associated with
    # them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEventsMessage(ShapeBase):
    """

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

    # The identifier of the event source for which events will be returned. If
    # this parameter is not specified, then all sources are included in the
    # response.

    # Constraints:

    # If _SourceIdentifier_ is supplied, _SourceType_ must also be provided.

    #   * Specify a cluster identifier when _SourceType_ is `cluster`.

    #   * Specify a cluster security group name when _SourceType_ is `cluster-security-group`.

    #   * Specify a cluster parameter group name when _SourceType_ is `cluster-parameter-group`.

    #   * Specify a cluster snapshot identifier when _SourceType_ is `cluster-snapshot`.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event source to retrieve events for. If no value is specified, all
    # events are returned.

    # Constraints:

    # If _SourceType_ is supplied, _SourceIdentifier_ must also be provided.

    #   * Specify `cluster` when _SourceIdentifier_ is a cluster identifier.

    #   * Specify `cluster-security-group` when _SourceIdentifier_ is a cluster security group name.

    #   * Specify `cluster-parameter-group` when _SourceIdentifier_ is a cluster parameter group name.

    #   * Specify `cluster-snapshot` when _SourceIdentifier_ is a cluster snapshot identifier.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The beginning of the time interval to retrieve events for, specified in ISO
    # 8601 format. For more information about ISO 8601, go to the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: `2009-07-08T18:00Z`
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time interval for which to retrieve events, specified in ISO
    # 8601 format. For more information about ISO 8601, go to the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: `2009-07-08T18:00Z`
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes prior to the time of the request for which to
    # retrieve events. For example, if the request is sent at 18:00 and you
    # specify a duration of 60, then only events which have occurred after 17:00
    # will be returned.

    # Default: `60`
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeEvents request exceed the
    # value specified in `MaxRecords`, AWS returns a value in the `Marker` field
    # of the response. You can retrieve the next set of response records by
    # providing the returned marker value in the `Marker` parameter and retrying
    # the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHsmClientCertificatesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of a specific HSM client certificate for which you want
    # information. If no identifier is specified, information is returned for all
    # HSM client certificates owned by your AWS customer account.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeHsmClientCertificates
    # request exceed the value specified in `MaxRecords`, AWS returns a value in
    # the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching HSM client
    # certificates that are associated with the specified key or keys. For
    # example, suppose that you have HSM client certificates that are tagged with
    # keys called `owner` and `environment`. If you specify both of these tag
    # keys in the request, Amazon Redshift returns a response with the HSM client
    # certificates that have either or both of these tag keys associated with
    # them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching HSM client
    # certificates that are associated with the specified tag value or values.
    # For example, suppose that you have HSM client certificates that are tagged
    # with values called `admin` and `test`. If you specify both of these tag
    # values in the request, Amazon Redshift returns a response with the HSM
    # client certificates that have either or both of these tag values associated
    # with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeHsmConfigurationsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of a specific Amazon Redshift HSM configuration to be
    # described. If no identifier is specified, information is returned for all
    # HSM configurations owned by your AWS customer account.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeHsmConfigurations request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching HSM
    # configurations that are associated with the specified key or keys. For
    # example, suppose that you have HSM configurations that are tagged with keys
    # called `owner` and `environment`. If you specify both of these tag keys in
    # the request, Amazon Redshift returns a response with the HSM configurations
    # that have either or both of these tag keys associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching HSM
    # configurations that are associated with the specified tag value or values.
    # For example, suppose that you have HSM configurations that are tagged with
    # values called `admin` and `test`. If you specify both of these tag values
    # in the request, Amazon Redshift returns a response with the HSM
    # configurations that have either or both of these tag values associated with
    # them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLoggingStatusMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster from which to get the logging status.

    # Example: `examplecluster`
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOrderableClusterOptionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
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

    # The version filter value. Specify this parameter to show only the available
    # offerings matching the specified version.

    # Default: All versions.

    # Constraints: Must be one of the version returned from
    # DescribeClusterVersions.
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type filter value. Specify this parameter to show only the
    # available offerings matching the specified node type.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeOrderableClusterOptions
    # request exceed the value specified in `MaxRecords`, AWS returns a value in
    # the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedNodeOfferingsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_offering_id",
                "ReservedNodeOfferingId",
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

    # The unique identifier for the offering.
    reserved_node_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeReservedNodeOfferings
    # request exceed the value specified in `MaxRecords`, AWS returns a value in
    # the `Marker` field of the response. You can retrieve the next set of
    # response records by providing the returned marker value in the `Marker`
    # parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedNodesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_id",
                "ReservedNodeId",
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

    # Identifier for the node reservation.
    reserved_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a DescribeReservedNodes request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeResizeMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of a cluster whose resize progress you are
    # requesting. This parameter is case-sensitive.

    # By default, resize operations for all clusters defined for an AWS account
    # are returned.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSnapshotCopyGrantsMessage(ShapeBase):
    """
    The result of the `DescribeSnapshotCopyGrants` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_copy_grant_name",
                "SnapshotCopyGrantName",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the snapshot copy grant.
    snapshot_copy_grant_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # marker value.

    # Default: `100`

    # Constraints: minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a `DescribeSnapshotCopyGrant` request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.

    # Constraints: You can specify either the **SnapshotCopyGrantName** parameter
    # or the **Marker** parameter, but not both.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching resources that
    # are associated with the specified key or keys. For example, suppose that
    # you have resources tagged with keys called `owner` and `environment`. If
    # you specify both of these tag keys in the request, Amazon Redshift returns
    # a response with all resources that have either or both of these tag keys
    # associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching resources
    # that are associated with the specified value or values. For example,
    # suppose that you have resources tagged with values called `admin` and
    # `test`. If you specify both of these tag values in the request, Amazon
    # Redshift returns a response with all resources that have either or both of
    # these tag values associated with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTableRestoreStatusMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "table_restore_request_id",
                "TableRestoreRequestId",
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

    # The Amazon Redshift cluster that the table is being restored to.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the table restore request to return status for. If you
    # don't specify a `TableRestoreRequestId` value, then
    # `DescribeTableRestoreStatus` returns the status of all in-progress table
    # restore requests.
    table_restore_request_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeTableRestoreStatus` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by the `MaxRecords` parameter.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsMessage(ShapeBase):
    """

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
                "resource_type",
                "ResourceType",
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
            (
                "tag_values",
                "TagValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) for which you want to describe the tag or
    # tags. For example, `arn:aws:redshift:us-east-1:123456789:cluster:t1`.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource with which you want to view tags. Valid resource types
    # are:

    #   * Cluster

    #   * CIDR/IP

    #   * EC2 security group

    #   * Snapshot

    #   * Cluster security group

    #   * Subnet group

    #   * HSM connection

    #   * HSM certificate

    #   * Parameter group

    #   * Snapshot copy grant

    # For more information about Amazon Redshift resource types and constructing
    # ARNs, go to [Specifying Policy Elements: Actions, Effects, Resources, and
    # Principals](http://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-
    # access-control-overview.html#redshift-iam-access-control-specify-actions)
    # in the Amazon Redshift Cluster Management Guide.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number or response records to return in each call. If the
    # number of remaining response records exceeds the specified `MaxRecords`
    # value, a value is returned in a `marker` field of the response. You can
    # retrieve the next set of records by retrying the command with the returned
    # `marker` value.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `marker` parameter and retrying the command. If the `marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag key or keys for which you want to return all matching resources that
    # are associated with the specified key or keys. For example, suppose that
    # you have resources tagged with keys called `owner` and `environment`. If
    # you specify both of these tag keys in the request, Amazon Redshift returns
    # a response with all resources that have either or both of these tag keys
    # associated with them.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag value or values for which you want to return all matching resources
    # that are associated with the specified value or values. For example,
    # suppose that you have resources tagged with values called `admin` and
    # `test`. If you specify both of these tag values in the request, Amazon
    # Redshift returns a response with all resources that have either or both of
    # these tag values associated with them.
    tag_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisableLoggingMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster on which logging is to be stopped.

    # Example: `examplecluster`
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableSnapshotCopyMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the source cluster that you want to disable
    # copying of snapshots to a destination region.

    # Constraints: Must be the valid name of an existing cluster that has cross-
    # region snapshot copy enabled.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableSnapshotCopyResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2SecurityGroup(ShapeBase):
    """
    Describes an Amazon EC2 security group.
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
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The status of the EC2 security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the EC2 Security Group.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS ID of the owner of the EC2 security group specified in the
    # `EC2SecurityGroupName` field.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags for the EC2 security group.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElasticIpStatus(ShapeBase):
    """
    Describes the status of the elastic IP (EIP) address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "elastic_ip",
                "ElasticIp",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The elastic IP (EIP) address for the cluster.
    elastic_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the elastic IP (EIP) address.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableLoggingMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster on which logging is to be started.

    # Example: `examplecluster`
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an existing S3 bucket where the log files are to be stored.

    # Constraints:

    #   * Must be in the same region as the cluster

    #   * The cluster must have read bucket and put object permissions
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix applied to the log file names.

    # Constraints:

    #   * Cannot exceed 512 characters

    #   * Cannot contain spaces( ), double quotes ("), single quotes ('), a backslash (\\), or control characters. The hexadecimal codes for invalid characters are:

    #     * x00 to x20

    #     * x22

    #     * x27

    #     * x5c

    #     * x7f or larger
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableSnapshotCopyMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "destination_region",
                "DestinationRegion",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "RetentionPeriod",
                TypeInfo(int),
            ),
            (
                "snapshot_copy_grant_name",
                "SnapshotCopyGrantName",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the source cluster to copy snapshots from.

    # Constraints: Must be the valid name of an existing cluster that does not
    # already have cross-region snapshot copy enabled.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination region that you want to copy snapshots to.

    # Constraints: Must be the name of a valid region. For more information, see
    # [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region)
    # in the Amazon Web Services General Reference.
    destination_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days to retain automated snapshots in the destination region
    # after they are copied from the source region.

    # Default: 7.

    # Constraints: Must be at least 1 and no more than 35.
    retention_period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the snapshot copy grant to use when snapshots of an AWS KMS-
    # encrypted cluster are copied to the destination region.
    snapshot_copy_grant_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnableSnapshotCopyResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    """
    Describes a connection endpoint.
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

    # The DNS address of the Cluster.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port that the database engine is listening on.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Event(ShapeBase):
    """
    Describes an event.
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
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(str),
            ),
            (
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
            (
                "event_id",
                "EventId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the source of the event.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source type for this event.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The text of this event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the event categories.

    # Values: Configuration, Management, Monitoring, Security
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The severity of the event.

    # Values: ERROR, INFO
    severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time of the event.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the event.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventCategoriesMap(ShapeBase):
    """
    Describes event categories.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_type",
                "SourceType",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[EventInfoMap]),
            ),
        ]

    # The source type, such as cluster or cluster-snapshot, that the returned
    # categories belong to.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The events in the event category.
    events: typing.List["EventInfoMap"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventCategoriesMessage(OutputShapeBase):
    """

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
                "event_categories_map_list",
                "EventCategoriesMapList",
                TypeInfo(typing.List[EventCategoriesMap]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event categories descriptions.
    event_categories_map_list: typing.List["EventCategoriesMap"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class EventInfoMap(ShapeBase):
    """
    Describes event information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_id",
                "EventId",
                TypeInfo(str),
            ),
            (
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_description",
                "EventDescription",
                TypeInfo(str),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(str),
            ),
        ]

    # The identifier of an Amazon Redshift event.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category of an Amazon Redshift event.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of an Amazon Redshift event.
    event_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The severity of the event.

    # Values: ERROR, INFO
    severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSubscription(ShapeBase):
    """
    Describes event subscriptions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "customer_aws_id",
                "CustomerAwsId",
                TypeInfo(str),
            ),
            (
                "cust_subscription_id",
                "CustSubscriptionId",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "subscription_creation_time",
                "SubscriptionCreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(str),
            ),
            (
                "source_ids_list",
                "SourceIdsList",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_categories_list",
                "EventCategoriesList",
                TypeInfo(typing.List[str]),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The AWS customer account associated with the Amazon Redshift event
    # notification subscription.
    customer_aws_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon Redshift event notification subscription.
    cust_subscription_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event
    # notification subscription.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the Amazon Redshift event notification subscription.

    # Constraints:

    #   * Can be one of the following: active | no-permission | topic-not-exist

    #   * The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the Amazon Redshift event notification subscription was
    # created.
    subscription_creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source type of the events returned the Amazon Redshift event
    # notification, such as cluster, or cluster-snapshot.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the sources that publish events to the Amazon Redshift event
    # notification subscription.
    source_ids_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of Amazon Redshift event categories specified in the event
    # notification subscription.

    # Values: Configuration, Management, Monitoring, Security
    event_categories_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The event severity specified in the Amazon Redshift event notification
    # subscription.

    # Values: ERROR, INFO
    severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the subscription is enabled. `true`
    # indicates the subscription is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags for the event subscription.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSubscriptionQuotaExceededFault(ShapeBase):
    """
    The request would exceed the allowed number of event subscriptions for this
    account. For information about increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EventSubscriptionsMessage(OutputShapeBase):
    """

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
                "event_subscriptions_list",
                "EventSubscriptionsList",
                TypeInfo(typing.List[EventSubscription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event subscriptions.
    event_subscriptions_list: typing.List["EventSubscription"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    def paginate(self,
                ) -> typing.Generator["EventSubscriptionsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class EventsMessage(OutputShapeBase):
    """

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

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `Event` instances.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["EventsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetClusterCredentialsMessage(ShapeBase):
    """
    The request parameters to get cluster credentials.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_user",
                "DbUser",
                TypeInfo(str),
            ),
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DbName",
                TypeInfo(str),
            ),
            (
                "duration_seconds",
                "DurationSeconds",
                TypeInfo(int),
            ),
            (
                "auto_create",
                "AutoCreate",
                TypeInfo(bool),
            ),
            (
                "db_groups",
                "DbGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of a database user. If a user name matching `DbUser` exists in the
    # database, the temporary user credentials have the same permissions as the
    # existing user. If `DbUser` doesn't exist in the database and `Autocreate`
    # is `True`, a new user is created using the value for `DbUser` with PUBLIC
    # permissions. If a database user matching the value for `DbUser` doesn't
    # exist and `Autocreate` is `False`, then the command succeeds but the
    # connection attempt will fail because the user doesn't exist in the
    # database.

    # For more information, see [CREATE
    # USER](http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html) in
    # the Amazon Redshift Database Developer Guide.

    # Constraints:

    #   * Must be 1 to 64 alphanumeric characters or hyphens. The user name can't be `PUBLIC`.

    #   * Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.

    #   * First character must be a letter.

    #   * Must not contain a colon ( : ) or slash ( / ).

    #   * Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
    db_user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the cluster that contains the database for which
    # your are requesting credentials. This parameter is case sensitive.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a database that `DbUser` is authorized to log on to. If
    # `DbName` is not specified, `DbUser` can log on to any existing database.

    # Constraints:

    #   * Must be 1 to 64 alphanumeric characters or hyphens

    #   * Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.

    #   * First character must be a letter.

    #   * Must not contain a colon ( : ) or slash ( / ).

    #   * Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of seconds until the returned temporary password expires.

    # Constraint: minimum 900, maximum 3600.

    # Default: 900
    duration_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Create a database user with the name specified for the user named in
    # `DbUser` if one does not exist.
    auto_create: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the names of existing database groups that the user named in
    # `DbUser` will join for the current session, in addition to any group
    # memberships for an existing user. If not specified, a new user is added
    # only to PUBLIC.

    # Database group name constraints

    #   * Must be 1 to 64 alphanumeric characters or hyphens

    #   * Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.

    #   * First character must be a letter.

    #   * Must not contain a colon ( : ) or slash ( / ).

    #   * Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
    db_groups: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservedNodeExchangeOfferingsInputMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_id",
                "ReservedNodeId",
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

    # A string representing the node identifier for the DC1 Reserved Node to be
    # exchanged.
    reserved_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An integer setting the maximum number of ReservedNodeOfferings to retrieve.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the starting point for the next set of
    # ReservedNodeOfferings.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservedNodeExchangeOfferingsOutputMessage(OutputShapeBase):
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
                "reserved_node_offerings",
                "ReservedNodeOfferings",
                TypeInfo(typing.List[ReservedNodeOffering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional parameter that specifies the starting point for returning a set
    # of response records. When the results of a
    # `GetReservedNodeExchangeOfferings` request exceed the value specified in
    # MaxRecords, Amazon Redshift returns a value in the marker field of the
    # response. You can retrieve the next set of response records by providing
    # the returned marker value in the marker parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns an array of ReservedNodeOffering objects.
    reserved_node_offerings: typing.List["ReservedNodeOffering"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class HsmClientCertificate(ShapeBase):
    """
    Returns information about an HSM client certificate. The certificate is stored
    in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift
    cluster to encrypt data files.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "hsm_client_certificate_public_key",
                "HsmClientCertificatePublicKey",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier of the HSM client certificate.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public key that the Amazon Redshift cluster will use to connect to the
    # HSM. You must register the public key in the HSM.
    hsm_client_certificate_public_key: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags for the HSM client certificate.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HsmClientCertificateAlreadyExistsFault(ShapeBase):
    """
    There is already an existing Amazon Redshift HSM client certificate with the
    specified identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HsmClientCertificateMessage(OutputShapeBase):
    """

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
                "hsm_client_certificates",
                "HsmClientCertificates",
                TypeInfo(typing.List[HsmClientCertificate]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the identifiers for one or more HSM client certificates used by
    # Amazon Redshift clusters to store and retrieve database encryption keys in
    # an HSM.
    hsm_client_certificates: typing.List["HsmClientCertificate"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    def paginate(
        self,
    ) -> typing.Generator["HsmClientCertificateMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class HsmClientCertificateNotFoundFault(ShapeBase):
    """
    There is no Amazon Redshift HSM client certificate with the specified
    identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HsmClientCertificateQuotaExceededFault(ShapeBase):
    """
    The quota for HSM client certificates has been reached. For information about
    increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HsmConfiguration(ShapeBase):
    """
    Returns information about an HSM configuration, which is an object that
    describes to Amazon Redshift clusters the information they require to connect to
    an HSM where they can store database encryption keys.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "hsm_ip_address",
                "HsmIpAddress",
                TypeInfo(str),
            ),
            (
                "hsm_partition_name",
                "HsmPartitionName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the Amazon Redshift HSM configuration.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A text description of the HSM configuration.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address that the Amazon Redshift cluster must use to access the HSM.
    hsm_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the partition in the HSM where the Amazon Redshift clusters
    # will store their database encryption keys.
    hsm_partition_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags for the HSM configuration.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HsmConfigurationAlreadyExistsFault(ShapeBase):
    """
    There is already an existing Amazon Redshift HSM configuration with the
    specified identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HsmConfigurationMessage(OutputShapeBase):
    """

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
                "hsm_configurations",
                "HsmConfigurations",
                TypeInfo(typing.List[HsmConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `HsmConfiguration` objects.
    hsm_configurations: typing.List["HsmConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["HsmConfigurationMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class HsmConfigurationNotFoundFault(ShapeBase):
    """
    There is no Amazon Redshift HSM configuration with the specified identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HsmConfigurationQuotaExceededFault(ShapeBase):
    """
    The quota for HSM configurations has been reached. For information about
    increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class HsmStatus(ShapeBase):
    """
    Describes the status of changes to HSM settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # Specifies the name of the HSM client certificate the Amazon Redshift
    # cluster uses to retrieve the data encryption keys stored in an HSM.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the HSM configuration that contains the information
    # the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reports whether the Amazon Redshift cluster has finished applying any HSM
    # settings changes specified in a modify cluster command.

    # Values: active, applying
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IPRange(ShapeBase):
    """
    Describes an IP range used in a security group.
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
                "cidrip",
                "CIDRIP",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The status of the IP range, for example, "authorized".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP range in Classless Inter-Domain Routing (CIDR) notation.
    cidrip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags for the IP range.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InProgressTableRestoreQuotaExceededFault(ShapeBase):
    """
    You have exceeded the allowed number of table restore requests. Wait for your
    current table restore requests to complete before making a new request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IncompatibleOrderableOptions(ShapeBase):
    """
    The specified options are incompatible.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientClusterCapacityFault(ShapeBase):
    """
    The number of nodes specified exceeds the allotted capacity of the cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientS3BucketPolicyFault(ShapeBase):
    """
    The cluster does not have read bucket or put object permissions on the S3 bucket
    specified when enabling logging.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterParameterGroupStateFault(ShapeBase):
    """
    The cluster parameter group action can not be completed because another task is
    in progress that involves the parameter group. Wait a few moments and try the
    operation again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterSecurityGroupStateFault(ShapeBase):
    """
    The state of the cluster security group is not `available`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterSnapshotStateFault(ShapeBase):
    """
    The specified cluster snapshot is not in the `available` state, or other
    accounts are authorized to access the snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterStateFault(ShapeBase):
    """
    The specified cluster is not in the `available` state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterSubnetGroupStateFault(ShapeBase):
    """
    The cluster subnet group cannot be deleted because it is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterSubnetStateFault(ShapeBase):
    """
    The state of the subnet is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidClusterTrackFault(ShapeBase):
    """
    The provided cluster track name is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidElasticIpFault(ShapeBase):
    """
    The Elastic IP (EIP) is invalid or cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidHsmClientCertificateStateFault(ShapeBase):
    """
    The specified HSM client certificate is not in the `available` state, or it is
    still in use by one or more Amazon Redshift clusters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidHsmConfigurationStateFault(ShapeBase):
    """
    The specified HSM configuration is not in the `available` state, or it is still
    in use by one or more Amazon Redshift clusters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidReservedNodeStateFault(ShapeBase):
    """
    Indicates that the Reserved Node being exchanged is not in an active state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRestoreFault(ShapeBase):
    """
    The restore is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3BucketNameFault(ShapeBase):
    """
    The S3 bucket name is invalid. For more information about naming rules, go to
    [Bucket Restrictions and
    Limitations](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html)
    in the Amazon Simple Storage Service (S3) Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3KeyPrefixFault(ShapeBase):
    """
    The string specified for the logging S3 key prefix does not comply with the
    documented constraints.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSnapshotCopyGrantStateFault(ShapeBase):
    """
    The snapshot copy grant can't be deleted because it is used by one or more
    clusters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnet(ShapeBase):
    """
    The requested subnet is not valid, or not all of the subnets are in the same
    VPC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubscriptionStateFault(ShapeBase):
    """
    The subscription request is invalid because it is a duplicate request. This
    subscription request is already in progress.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTableRestoreArgumentFault(ShapeBase):
    """
    The value specified for the `sourceDatabaseName`, `sourceSchemaName`, or
    `sourceTableName` parameter, or a combination of these, doesn't exist in the
    snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidTagFault(ShapeBase):
    """
    The tag is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidVPCNetworkStateFault(ShapeBase):
    """
    The cluster subnet group does not cover all Availability Zones.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LimitExceededFault(ShapeBase):
    """
    The encryption key has exceeded its grant limit in AWS KMS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class LoggingStatus(OutputShapeBase):
    """
    Describes the status of logging for a cluster.
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
                "logging_enabled",
                "LoggingEnabled",
                TypeInfo(bool),
            ),
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key_prefix",
                "S3KeyPrefix",
                TypeInfo(str),
            ),
            (
                "last_successful_delivery_time",
                "LastSuccessfulDeliveryTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_failure_time",
                "LastFailureTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_failure_message",
                "LastFailureMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # `true` if logging is on, `false` if logging is off.
    logging_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the S3 bucket where the log files are stored.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix applied to the log file names.
    s3_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last time that logs were delivered.
    last_successful_delivery_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time when logs failed to be delivered.
    last_failure_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message indicating that logs failed to be delivered.
    last_failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MaintenanceTrack(ShapeBase):
    """
    Defines a maintenance track that determines which Amazon Redshift version to
    apply during a maintenance window. If the value for `MaintenanceTrack` is
    `current`, the cluster is updated to the most recently certified maintenance
    release. If the value is `trailing`, the cluster is updated to the previously
    certified maintenance release.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
            (
                "database_version",
                "DatabaseVersion",
                TypeInfo(str),
            ),
            (
                "update_targets",
                "UpdateTargets",
                TypeInfo(typing.List[UpdateTarget]),
            ),
        ]

    # The name of the maintenance track. Possible values are `current` and
    # `trailing`.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number for the cluster release.
    database_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of UpdateTarget objects to update with the maintenance track.
    update_targets: typing.List["UpdateTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyClusterDbRevisionMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "revision_target",
                "RevisionTarget",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of a cluster whose database revision you want to
    # modify.

    # Example: `examplecluster`
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the database revision. You can retrieve this value from
    # the response to the DescribeClusterDbRevisions request.
    revision_target: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyClusterDbRevisionResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyClusterIamRolesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "add_iam_roles",
                "AddIamRoles",
                TypeInfo(typing.List[str]),
            ),
            (
                "remove_iam_roles",
                "RemoveIamRoles",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique identifier of the cluster for which you want to associate or
    # disassociate IAM roles.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Zero or more IAM roles to associate with the cluster. The roles must be in
    # their Amazon Resource Name (ARN) format. You can associate up to 10 IAM
    # roles with a single cluster in a single request.
    add_iam_roles: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Zero or more IAM roles in ARN format to disassociate from the cluster. You
    # can disassociate up to 10 IAM roles from a single cluster in a single
    # request.
    remove_iam_roles: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyClusterIamRolesResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "cluster_type",
                "ClusterType",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "cluster_security_groups",
                "ClusterSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                TypeInfo(str),
            ),
            (
                "cluster_parameter_group_name",
                "ClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "automated_snapshot_retention_period",
                "AutomatedSnapshotRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "allow_version_upgrade",
                "AllowVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
            (
                "new_cluster_identifier",
                "NewClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "elastic_ip",
                "ElasticIp",
                TypeInfo(str),
            ),
            (
                "enhanced_vpc_routing",
                "EnhancedVpcRouting",
                TypeInfo(bool),
            ),
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
            (
                "encrypted",
                "Encrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the cluster to be modified.

    # Example: `examplecluster`
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new cluster type.

    # When you submit your cluster resize request, your existing cluster goes
    # into a read-only mode. After Amazon Redshift provisions a new cluster based
    # on your resize requirements, there will be outage for a period while the
    # old cluster is deleted and your connection is switched to the new cluster.
    # You can use DescribeResize to track the progress of the resize request.

    # Valid Values: ` multi-node | single-node `
    cluster_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new node type of the cluster. If you specify a new node type, you must
    # also specify the number of nodes parameter.

    # When you submit your request to resize a cluster, Amazon Redshift sets
    # access permissions for the cluster to read-only. After Amazon Redshift
    # provisions a new cluster according to your resize requirements, there will
    # be a temporary outage while the old cluster is deleted and your connection
    # is switched to the new cluster. When the new connection is complete, the
    # original access permissions for the cluster are restored. You can use
    # DescribeResize to track the progress of the resize request.

    # Valid Values: `ds2.xlarge` | `ds2.8xlarge` | `dc1.large` | `dc1.8xlarge` |
    # `dc2.large` | `dc2.8xlarge`
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new number of nodes of the cluster. If you specify a new number of
    # nodes, you must also specify the node type parameter.

    # When you submit your request to resize a cluster, Amazon Redshift sets
    # access permissions for the cluster to read-only. After Amazon Redshift
    # provisions a new cluster according to your resize requirements, there will
    # be a temporary outage while the old cluster is deleted and your connection
    # is switched to the new cluster. When the new connection is complete, the
    # original access permissions for the cluster are restored. You can use
    # DescribeResize to track the progress of the resize request.

    # Valid Values: Integer greater than `0`.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cluster security groups to be authorized on this cluster. This
    # change is asynchronously applied as soon as possible.

    # Security groups currently associated with the cluster, and not in the list
    # of groups to apply, will be revoked from the cluster.

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    cluster_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of virtual private cloud (VPC) security groups to be associated with
    # the cluster. This change is asynchronously applied as soon as possible.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new password for the cluster master user. This change is asynchronously
    # applied as soon as possible. Between the time of the request and the
    # completion of the request, the `MasterUserPassword` element exists in the
    # `PendingModifiedValues` element of the operation response.

    # Operations never return the password, so this operation provides a way to
    # regain access to the master user account for a cluster if the password is
    # lost.

    # Default: Uses existing setting.

    # Constraints:

    #   * Must be between 8 and 64 characters in length.

    #   * Must contain at least one uppercase letter.

    #   * Must contain at least one lowercase letter.

    #   * Must contain one number.

    #   * Can be any printable ASCII character (ASCII code 33 to 126) except ' (single quote), " (double quote), \, /, @, or space.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster parameter group to apply to this cluster. This
    # change is applied only after the cluster is rebooted. To reboot a cluster
    # use RebootCluster.

    # Default: Uses existing setting.

    # Constraints: The cluster parameter group must be in the same parameter
    # group family that matches the cluster version.
    cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days that automated snapshots are retained. If the value is
    # 0, automated snapshots are disabled. Even if automated snapshots are
    # disabled, you can still create manual snapshots when you want with
    # CreateClusterSnapshot.

    # If you decrease the automated snapshot retention period from its current
    # value, existing automated snapshots that fall outside of the new retention
    # period will be immediately deleted.

    # Default: Uses existing setting.

    # Constraints: Must be a value from 0 to 35.
    automated_snapshot_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range (in UTC) during which system maintenance can occur,
    # if necessary. If system maintenance is necessary during the window, it may
    # result in an outage.

    # This maintenance window change is made immediately. If the new maintenance
    # window indicates the current time, there must be at least 120 minutes
    # between the current time and end of the window in order to ensure that
    # pending changes are applied.

    # Default: Uses existing setting.

    # Format: ddd:hh24:mi-ddd:hh24:mi, for example `wed:07:30-wed:08:00`.

    # Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

    # Constraints: Must be at least 30 minutes.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new version number of the Amazon Redshift engine to upgrade to.

    # For major version upgrades, if a non-default cluster parameter group is
    # currently in use, a new cluster parameter group in the cluster parameter
    # group family for the new version must be specified. The new cluster
    # parameter group can be the default for that cluster parameter group family.
    # For more information about parameters and parameter groups, go to [Amazon
    # Redshift Parameter
    # Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # parameter-groups.html) in the _Amazon Redshift Cluster Management Guide_.

    # Example: `1.0`
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, major version upgrades will be applied automatically to the
    # cluster during the maintenance window.

    # Default: `false`
    allow_version_upgrade: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the HSM client certificate the Amazon Redshift
    # cluster uses to retrieve the data encryption keys stored in an HSM.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the HSM configuration that contains the information
    # the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new identifier for the cluster.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * Alphabetic characters must be lowercase.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    #   * Must be unique for all clusters within an AWS account.

    # Example: `examplecluster`
    new_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, the cluster can be accessed from a public network. Only clusters
    # in VPCs can be set to be publicly available.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Elastic IP (EIP) address for the cluster.

    # Constraints: The cluster must be provisioned in EC2-VPC and publicly-
    # accessible through an Internet gateway. For more information about
    # provisioning clusters in EC2-VPC, go to [Supported Platforms to Launch Your
    # Cluster](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # clusters.html#cluster-platforms) in the Amazon Redshift Cluster Management
    # Guide.
    elastic_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An option that specifies whether to create the cluster with enhanced VPC
    # routing enabled. To create a cluster that uses enhanced VPC routing, the
    # cluster must be in a VPC. For more information, see [Enhanced VPC
    # Routing](http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-
    # routing.html) in the Amazon Redshift Cluster Management Guide.

    # If this option is `true`, enhanced VPC routing is enabled.

    # Default: false
    enhanced_vpc_routing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the maintenance track that you want to assign for the cluster.
    # This name change is asynchronous. The new track name stays in the
    # `PendingModifiedValues` for the cluster until the next maintenance window.
    # When the maintenance track changes, the cluster is switched to the latest
    # cluster release available for the maintenance track. At this point, the
    # maintenance track name is applied.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the cluster is encrypted. If the cluster is encrypted and
    # you provide a value for the `KmsKeyId` parameter, we will encrypt the
    # cluster with the provided `KmsKeyId`. If you don't provide a `KmsKeyId`, we
    # will encrypt with the default key. In the China region we will use legacy
    # encryption if you specify that the cluster is encrypted.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (KMS) key ID of the encryption key that you
    # want to use to encrypt data in the cluster.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the parameter group to be modified.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of parameters to be modified. A maximum of 20 parameters can be
    # modified in a single request.

    # For each parameter to be modified, you must supply at least the parameter
    # name and parameter value; other name-value pairs of the parameter are
    # optional.

    # For the workload management (WLM) configuration, you must supply all the
    # name-value pairs in the wlm_json_configuration parameter.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyClusterResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyClusterSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name of the subnet group to be modified.
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a
    # single request.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A text description of the subnet group to be modified.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyClusterSubnetGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_subnet_group",
                "ClusterSubnetGroup",
                TypeInfo(ClusterSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a subnet group.
    cluster_subnet_group: "ClusterSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyEventSubscriptionMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_name",
                "SubscriptionName",
                TypeInfo(str),
            ),
            (
                "sns_topic_arn",
                "SnsTopicArn",
                TypeInfo(str),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(str),
            ),
            (
                "source_ids",
                "SourceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the modified Amazon Redshift event notification subscription.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SNS topic to be used by the event
    # notification subscription.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of source that will be generating the events. For example, if you
    # want to be notified of events generated by a cluster, you would set this
    # parameter to cluster. If this value is not specified, events are returned
    # for all Amazon Redshift objects in your AWS account. You must specify a
    # source type in order to specify source IDs.

    # Valid values: cluster, cluster-parameter-group, cluster-security-group, and
    # cluster-snapshot.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of one or more identifiers of Amazon Redshift source objects. All of
    # the objects must be of the same type as was specified in the source type
    # parameter. The event subscription will return only events generated by the
    # specified objects. If not specified, then events are returned for all
    # objects within the source type specified.

    # Example: my-cluster-1, my-cluster-2

    # Example: my-snapshot-20131010
    source_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Amazon Redshift event categories to be published by the event
    # notification subscription.

    # Values: Configuration, Management, Monitoring, Security
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the Amazon Redshift event severity to be published by the event
    # notification subscription.

    # Values: ERROR, INFO
    severity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating if the subscription is enabled. `true` indicates
    # the subscription is enabled
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyEventSubscriptionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_subscription",
                "EventSubscription",
                TypeInfo(EventSubscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes event subscriptions.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifySnapshotCopyRetentionPeriodMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "retention_period",
                "RetentionPeriod",
                TypeInfo(int),
            ),
        ]

    # The unique identifier of the cluster for which you want to change the
    # retention period for automated snapshots that are copied to a destination
    # region.

    # Constraints: Must be the valid name of an existing cluster that has cross-
    # region snapshot copy enabled.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days to retain automated snapshots in the destination region
    # after they are copied from the source region.

    # If you decrease the retention period for automated snapshots that are
    # copied to a destination region, Amazon Redshift will delete any existing
    # automated snapshots that were copied to the destination region and that
    # fall outside of the new retention period.

    # Constraints: Must be at least 1 and no more than 35.
    retention_period: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifySnapshotCopyRetentionPeriodResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberOfNodesPerClusterLimitExceededFault(ShapeBase):
    """
    The operation would exceed the number of nodes allowed for a cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NumberOfNodesQuotaExceededFault(ShapeBase):
    """
    The operation would exceed the number of nodes allotted to the account. For
    information about increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OrderableClusterOption(ShapeBase):
    """
    Describes an orderable cluster option.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "cluster_type",
                "ClusterType",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[AvailabilityZone]),
            ),
        ]

    # The version of the orderable cluster.
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cluster type, for example `multi-node`.
    cluster_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type for the orderable cluster.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of availability zones for the orderable cluster.
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OrderableClusterOptionsMessage(OutputShapeBase):
    """
    Contains the output from the DescribeOrderableClusterOptions action.
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
                "orderable_cluster_options",
                "OrderableClusterOptions",
                TypeInfo(typing.List[OrderableClusterOption]),
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

    # An `OrderableClusterOption` structure containing information about
    # orderable options for the cluster.
    orderable_cluster_options: typing.List["OrderableClusterOption"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["OrderableClusterOptionsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Parameter(ShapeBase):
    """
    Describes a parameter in a cluster parameter group.
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
                "apply_type",
                "ApplyType",
                TypeInfo(typing.Union[str, ParameterApplyType]),
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
        ]

    # The name of the parameter.
    parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the parameter.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the parameter value, such as "engine-default" or "user".
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data type of the parameter.
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid range of values for the parameter.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies how to apply the WLM configuration parameter. Some properties can
    # be applied dynamically, while other properties require that any associated
    # clusters be rebooted for the configuration changes to be applied. For more
    # information about parameters and parameter groups, go to [Amazon Redshift
    # Parameter Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-
    # with-parameter-groups.html) in the _Amazon Redshift Cluster Management
    # Guide_.
    apply_type: typing.Union[str, "ParameterApplyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `true`, the parameter can be modified. Some parameters have security or
    # operational implications that prevent them from being changed.
    is_modifiable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The earliest engine version to which the parameter can apply.
    minimum_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ParameterApplyType(str):
    static = "static"
    dynamic = "dynamic"


@dataclasses.dataclass
class PendingModifiedValues(ShapeBase):
    """
    Describes cluster attributes that are in a pending state. A change to one or
    more the attributes was requested and is in progress or will be applied.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "master_user_password",
                "MasterUserPassword",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "cluster_type",
                "ClusterType",
                TypeInfo(str),
            ),
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "automated_snapshot_retention_period",
                "AutomatedSnapshotRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "enhanced_vpc_routing",
                "EnhancedVpcRouting",
                TypeInfo(bool),
            ),
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(str),
            ),
        ]

    # The pending or in-progress change of the master user password for the
    # cluster.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending or in-progress change of the cluster's node type.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending or in-progress change of the number of nodes in the cluster.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending or in-progress change of the cluster type.
    cluster_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending or in-progress change of the service version.
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending or in-progress change of the automated snapshot retention
    # period.
    automated_snapshot_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pending or in-progress change of the new identifier for the cluster.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending or in-progress change of the ability to connect to the cluster
    # from the public network.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An option that specifies whether to create the cluster with enhanced VPC
    # routing enabled. To create a cluster that uses enhanced VPC routing, the
    # cluster must be in a VPC. For more information, see [Enhanced VPC
    # Routing](http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-
    # routing.html) in the Amazon Redshift Cluster Management Guide.

    # If this option is `true`, enhanced VPC routing is enabled.

    # Default: false
    enhanced_vpc_routing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the maintenance track that the cluster will change to during
    # the next maintenance window.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption type for a cluster. Possible values are: KMS and None. For
    # the China region the possible values are None, and Legacy.
    encryption_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedNodeOfferingMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_offering_id",
                "ReservedNodeOfferingId",
                TypeInfo(str),
            ),
            (
                "node_count",
                "NodeCount",
                TypeInfo(int),
            ),
        ]

    # The unique identifier of the reserved node offering you want to purchase.
    reserved_node_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of reserved nodes that you want to purchase.

    # Default: `1`
    node_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedNodeOfferingResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "reserved_node",
                "ReservedNode",
                TypeInfo(ReservedNode),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a reserved node. You can call the DescribeReservedNodeOfferings
    # API to obtain the available reserved node offerings.
    reserved_node: "ReservedNode" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The cluster identifier.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootClusterResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecurringCharge(ShapeBase):
    """
    Describes a recurring charge.
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

    # The amount charged per the period of time specified by the recurring charge
    # frequency.
    recurring_charge_amount: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The frequency at which the recurring charge amount is applied.
    recurring_charge_frequency: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedNode(ShapeBase):
    """
    Describes a reserved node. You can call the DescribeReservedNodeOfferings API to
    obtain the available reserved node offerings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_id",
                "ReservedNodeId",
                TypeInfo(str),
            ),
            (
                "reserved_node_offering_id",
                "ReservedNodeOfferingId",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
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
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "node_count",
                "NodeCount",
                TypeInfo(int),
            ),
            (
                "state",
                "State",
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
            (
                "reserved_node_offering_type",
                "ReservedNodeOfferingType",
                TypeInfo(typing.Union[str, ReservedNodeOfferingType]),
            ),
        ]

    # The unique identifier for the reservation.
    reserved_node_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the reserved node offering.
    reserved_node_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The node type of the reserved node.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the reservation started. You purchase a reserved node offering for
    # a duration. This is the start time of that duration.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration of the node reservation in seconds.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fixed cost Amazon Redshift charges you for this reserved node.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hourly rate Amazon Redshift charges you for this reserved node.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code for the reserved cluster.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of reserved compute nodes.
    node_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the reserved compute node.

    # Possible Values:

    #   * pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.

    #   * active-This reserved node is owned by the caller and is available for use.

    #   * payment-failed-Payment failed for the purchase attempt.

    #   * retired-The reserved node is no longer available.

    #   * exchanging-The owner is exchanging the reserved node for another reserved node.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The anticipated utilization of the reserved node, as defined in the
    # reserved node offering.
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring charges for the reserved node.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    reserved_node_offering_type: typing.Union[str, "ReservedNodeOfferingType"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class ReservedNodeAlreadyExistsFault(ShapeBase):
    """
    User already has a reservation with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedNodeAlreadyMigratedFault(ShapeBase):
    """
    Indicates that the reserved node has already been exchanged.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedNodeNotFoundFault(ShapeBase):
    """
    The specified reserved compute node not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedNodeOffering(ShapeBase):
    """
    Describes a reserved node offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_node_offering_id",
                "ReservedNodeOfferingId",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
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
                "currency_code",
                "CurrencyCode",
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
            (
                "reserved_node_offering_type",
                "ReservedNodeOfferingType",
                TypeInfo(typing.Union[str, ReservedNodeOfferingType]),
            ),
        ]

    # The offering identifier.
    reserved_node_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The node type offered by the reserved node offering.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration, in seconds, for which the offering will reserve the node.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upfront fixed charge you will pay to purchase the specific reserved
    # node offering.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rate you are charged for each hour the cluster that is using the
    # offering is running.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code for the compute nodes offering.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The anticipated utilization of the reserved node, as defined in the
    # reserved node offering.
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The charge to your account regardless of whether you are creating any
    # clusters using the node offering. Recurring charges are only in effect for
    # heavy-utilization reserved nodes.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    reserved_node_offering_type: typing.Union[str, "ReservedNodeOfferingType"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class ReservedNodeOfferingNotFoundFault(ShapeBase):
    """
    Specified offering does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ReservedNodeOfferingType(str):
    Regular = "Regular"
    Upgradable = "Upgradable"


@dataclasses.dataclass
class ReservedNodeOfferingsMessage(OutputShapeBase):
    """

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
                "reserved_node_offerings",
                "ReservedNodeOfferings",
                TypeInfo(typing.List[ReservedNodeOffering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `ReservedNodeOffering` objects.
    reserved_node_offerings: typing.List["ReservedNodeOffering"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    def paginate(
        self,
    ) -> typing.Generator["ReservedNodeOfferingsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ReservedNodeQuotaExceededFault(ShapeBase):
    """
    Request would exceed the user's compute node quota. For information about
    increasing your quota, go to [Limits in Amazon
    Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-
    limits.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedNodesMessage(OutputShapeBase):
    """

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
                "reserved_nodes",
                "ReservedNodes",
                TypeInfo(typing.List[ReservedNode]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of `ReservedNode` objects.
    reserved_nodes: typing.List["ReservedNode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ReservedNodesMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ResetClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parameter_group_name",
                "ParameterGroupName",
                TypeInfo(str),
            ),
            (
                "reset_all_parameters",
                "ResetAllParameters",
                TypeInfo(bool),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the cluster parameter group to be reset.
    parameter_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, all parameters in the specified parameter group will be reset to
    # their default values.

    # Default: `true`
    reset_all_parameters: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of names of parameters to be reset. If _ResetAllParameters_ option
    # is not used, then at least one parameter name must be supplied.

    # Constraints: A maximum of 20 parameters can be reset in a single request.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResizeClusterMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "cluster_type",
                "ClusterType",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "classic",
                "Classic",
                TypeInfo(bool),
            ),
        ]

    # The unique identifier for the cluster to resize.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new number of nodes for the cluster.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new cluster type for the specified cluster.
    cluster_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new node type for the nodes you are adding.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value indicating whether the resize operation is using the
    # classic resize process. If you don't provide this parameter or set the
    # value to `false` the resize type is elastic.
    classic: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResizeClusterResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResizeNotFoundFault(ShapeBase):
    """
    A resize operation for the specified cluster is not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResizeProgressMessage(OutputShapeBase):
    """
    Describes the result of a cluster resize operation.
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
                "target_node_type",
                "TargetNodeType",
                TypeInfo(str),
            ),
            (
                "target_number_of_nodes",
                "TargetNumberOfNodes",
                TypeInfo(int),
            ),
            (
                "target_cluster_type",
                "TargetClusterType",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "import_tables_completed",
                "ImportTablesCompleted",
                TypeInfo(typing.List[str]),
            ),
            (
                "import_tables_in_progress",
                "ImportTablesInProgress",
                TypeInfo(typing.List[str]),
            ),
            (
                "import_tables_not_started",
                "ImportTablesNotStarted",
                TypeInfo(typing.List[str]),
            ),
            (
                "avg_resize_rate_in_mega_bytes_per_second",
                "AvgResizeRateInMegaBytesPerSecond",
                TypeInfo(float),
            ),
            (
                "total_resize_data_in_mega_bytes",
                "TotalResizeDataInMegaBytes",
                TypeInfo(int),
            ),
            (
                "progress_in_mega_bytes",
                "ProgressInMegaBytes",
                TypeInfo(int),
            ),
            (
                "elapsed_time_in_seconds",
                "ElapsedTimeInSeconds",
                TypeInfo(int),
            ),
            (
                "estimated_time_to_completion_in_seconds",
                "EstimatedTimeToCompletionInSeconds",
                TypeInfo(int),
            ),
            (
                "resize_type",
                "ResizeType",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "target_encryption_type",
                "TargetEncryptionType",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The node type that the cluster will have after the resize operation is
    # complete.
    target_node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of nodes that the cluster will have after the resize operation
    # is complete.
    target_number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cluster type after the resize operation is complete.

    # Valid Values: `multi-node` | `single-node`
    target_cluster_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the resize operation.

    # Valid Values: `NONE` | `IN_PROGRESS` | `FAILED` | `SUCCEEDED`
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The names of tables that have been completely imported .

    # Valid Values: List of table names.
    import_tables_completed: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of tables that are being currently imported.

    # Valid Values: List of table names.
    import_tables_in_progress: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of tables that have not been yet imported.

    # Valid Values: List of table names
    import_tables_not_started: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The average rate of the resize operation over the last few minutes,
    # measured in megabytes per second. After the resize operation completes,
    # this value shows the average rate of the entire resize operation.
    avg_resize_rate_in_mega_bytes_per_second: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimated total amount of data, in megabytes, on the cluster before the
    # resize operation began.
    total_resize_data_in_mega_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # While the resize operation is in progress, this value shows the current
    # amount of data, in megabytes, that has been processed so far. When the
    # resize operation is complete, this value shows the total amount of data, in
    # megabytes, on the cluster, which may be more or less than
    # TotalResizeDataInMegaBytes (the estimated total amount of data before
    # resize).
    progress_in_mega_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of seconds that have elapsed since the resize operation began.
    # After the resize operation completes, this value shows the total actual
    # time, in seconds, for the resize operation.
    elapsed_time_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimated time remaining, in seconds, until the resize operation is
    # complete. This value is calculated based on the average resize rate and the
    # estimated amount of data remaining to be processed. Once the resize
    # operation is complete, this value will be 0.
    estimated_time_to_completion_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An enum with possible values of ClassicResize and ElasticResize. These
    # values describe the type of resize operation being performed.
    resize_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional string to provide additional details about the resize action.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of encryption for the cluster after the resize is complete.

    # Possible values are `KMS` and `None`. In the China region possible values
    # are: `Legacy` and `None`.
    target_encryption_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundFault(ShapeBase):
    """
    The resource could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RestoreFromClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_cluster_identifier",
                "SnapshotClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "allow_version_upgrade",
                "AllowVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "cluster_subnet_group_name",
                "ClusterSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "owner_account",
                "OwnerAccount",
                TypeInfo(str),
            ),
            (
                "hsm_client_certificate_identifier",
                "HsmClientCertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "hsm_configuration_identifier",
                "HsmConfigurationIdentifier",
                TypeInfo(str),
            ),
            (
                "elastic_ip",
                "ElasticIp",
                TypeInfo(str),
            ),
            (
                "cluster_parameter_group_name",
                "ClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "cluster_security_groups",
                "ClusterSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "automated_snapshot_retention_period",
                "AutomatedSnapshotRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "enhanced_vpc_routing",
                "EnhancedVpcRouting",
                TypeInfo(bool),
            ),
            (
                "additional_info",
                "AdditionalInfo",
                TypeInfo(str),
            ),
            (
                "iam_roles",
                "IamRoles",
                TypeInfo(typing.List[str]),
            ),
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
        ]

    # The identifier of the cluster that will be created from restoring the
    # snapshot.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * Alphabetic characters must be lowercase.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    #   * Must be unique for all clusters within an AWS account.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the snapshot from which to create the new cluster. This
    # parameter isn't case sensitive.

    # Example: `my-snapshot-id`
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the cluster the source snapshot was created from. This
    # parameter is required if your IAM user has a policy containing a snapshot
    # resource element that specifies anything other than * for the cluster name.
    snapshot_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which the cluster accepts connections.

    # Default: The same port as the original cluster.

    # Constraints: Must be between `1115` and `65535`.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 Availability Zone in which to restore the cluster.

    # Default: A random, system-chosen Availability Zone.

    # Example: `us-east-1a`
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, major version upgrades can be applied during the maintenance
    # window to the Amazon Redshift engine that is running on the cluster.

    # Default: `true`
    allow_version_upgrade: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the subnet group where you want to cluster restored.

    # A snapshot of cluster in VPC can be restored only in VPC. Therefore, you
    # must provide subnet group name where you want the cluster restored.
    cluster_subnet_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `true`, the cluster can be accessed from a public network.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS customer account used to create or copy the snapshot. Required if
    # you are restoring a snapshot you do not own, optional if you own the
    # snapshot.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the HSM client certificate the Amazon Redshift
    # cluster uses to retrieve the data encryption keys stored in an HSM.
    hsm_client_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the HSM configuration that contains the information
    # the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    hsm_configuration_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The elastic IP (EIP) address for the cluster.
    elastic_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the parameter group to be associated with this cluster.

    # Default: The default Amazon Redshift cluster parameter group. For
    # information about the default parameter group, go to [Working with Amazon
    # Redshift Parameter
    # Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # parameter-groups.html).

    # Constraints:

    #   * Must be 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security groups to be associated with this cluster.

    # Default: The default cluster security group for Amazon Redshift.

    # Cluster security groups only apply to clusters outside of VPCs.
    cluster_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of Virtual Private Cloud (VPC) security groups to be associated with
    # the cluster.

    # Default: The default VPC security group is associated with the cluster.

    # VPC security groups only apply to clusters in VPCs.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range (in UTC) during which automated cluster maintenance
    # can occur.

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # Default: The value selected for the cluster from which the snapshot was
    # taken. For more information about the time blocks for each region, see
    # [Maintenance
    # Windows](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # clusters.html#rs-maintenance-windows) in Amazon Redshift Cluster Management
    # Guide.

    # Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days that automated snapshots are retained. If the value is
    # 0, automated snapshots are disabled. Even if automated snapshots are
    # disabled, you can still create manual snapshots when you want with
    # CreateClusterSnapshot.

    # Default: The value selected for the cluster from which the snapshot was
    # taken.

    # Constraints: Must be a value from 0 to 35.
    automated_snapshot_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Key Management Service (KMS) key ID of the encryption key that you
    # want to use to encrypt data in the cluster that you restore from a shared
    # snapshot.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type that the restored cluster will be provisioned with.

    # Default: The node type of the cluster from which the snapshot was taken.
    # You can modify this if you are using any DS node type. In that case, you
    # can choose to restore into another DS node type of the same size. For
    # example, you can restore ds1.8xlarge into ds2.8xlarge, or ds1.xlarge into
    # ds2.xlarge. If you have a DC instance type, you must restore into that same
    # instance type and size. In other words, you can only restore a dc1.large
    # instance type into another dc1.large instance type or dc2.large instance
    # type. You can't restore dc1.8xlarge to dc2.8xlarge. First restore to a
    # dc1.8xlareg cluster, then resize to a dc2.8large cluster. For more
    # information about node types, see [ About Clusters and
    # Nodes](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
    # clusters.html#rs-about-clusters-and-nodes) in the _Amazon Redshift Cluster
    # Management Guide_.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An option that specifies whether to create the cluster with enhanced VPC
    # routing enabled. To create a cluster that uses enhanced VPC routing, the
    # cluster must be in a VPC. For more information, see [Enhanced VPC
    # Routing](http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-
    # routing.html) in the Amazon Redshift Cluster Management Guide.

    # If this option is `true`, enhanced VPC routing is enabled.

    # Default: false
    enhanced_vpc_routing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved.
    additional_info: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of AWS Identity and Access Management (IAM) roles that can be used
    # by the cluster to access other AWS services. You must supply the IAM roles
    # in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM
    # roles in a single request.

    # A cluster can have up to 10 IAM roles associated at any time.
    iam_roles: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the maintenance track for the restored cluster. When you take a
    # snapshot, the snapshot inherits the `MaintenanceTrack` value from the
    # cluster. The snapshot might be on a different track than the cluster that
    # was the source for the snapshot. For example, suppose that you take a
    # snapshot of a cluster that is on the current track and then change the
    # cluster to be on the trailing track. In this case, the snapshot and the
    # source cluster are on different tracks.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreFromClusterSnapshotResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreStatus(ShapeBase):
    """
    Describes the status of a cluster restore action. Returns null if the cluster
    was not created by restoring a snapshot.
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
                "current_restore_rate_in_mega_bytes_per_second",
                "CurrentRestoreRateInMegaBytesPerSecond",
                TypeInfo(float),
            ),
            (
                "snapshot_size_in_mega_bytes",
                "SnapshotSizeInMegaBytes",
                TypeInfo(int),
            ),
            (
                "progress_in_mega_bytes",
                "ProgressInMegaBytes",
                TypeInfo(int),
            ),
            (
                "elapsed_time_in_seconds",
                "ElapsedTimeInSeconds",
                TypeInfo(int),
            ),
            (
                "estimated_time_to_completion_in_seconds",
                "EstimatedTimeToCompletionInSeconds",
                TypeInfo(int),
            ),
        ]

    # The status of the restore action. Returns starting, restoring, completed,
    # or failed.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of megabytes per second being transferred from the backup
    # storage. Returns the average rate for a completed backup.
    current_restore_rate_in_mega_bytes_per_second: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the set of snapshot data used to restore the cluster.
    snapshot_size_in_mega_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of megabytes that have been transferred from snapshot storage.
    progress_in_mega_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time an in-progress restore has been running, or the amount
    # of time it took a completed restore to finish.
    elapsed_time_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimate of the time remaining before the restore will complete.
    # Returns 0 for a completed restore.
    estimated_time_to_completion_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreTableFromClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "source_database_name",
                "SourceDatabaseName",
                TypeInfo(str),
            ),
            (
                "source_table_name",
                "SourceTableName",
                TypeInfo(str),
            ),
            (
                "new_table_name",
                "NewTableName",
                TypeInfo(str),
            ),
            (
                "source_schema_name",
                "SourceSchemaName",
                TypeInfo(str),
            ),
            (
                "target_database_name",
                "TargetDatabaseName",
                TypeInfo(str),
            ),
            (
                "target_schema_name",
                "TargetSchemaName",
                TypeInfo(str),
            ),
        ]

    # The identifier of the Amazon Redshift cluster to restore the table to.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the snapshot to restore the table from. This snapshot
    # must have been created from the Amazon Redshift cluster specified by the
    # `ClusterIdentifier` parameter.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source database that contains the table to restore from.
    source_database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source table to restore from.
    source_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table to create as a result of the current request.
    new_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source schema that contains the table to restore from. If
    # you do not specify a `SourceSchemaName` value, the default is `public`.
    source_schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database to restore the table to.
    target_database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the schema to restore the table to.
    target_schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreTableFromClusterSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table_restore_status",
                "TableRestoreStatus",
                TypeInfo(TableRestoreStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the status of a RestoreTableFromClusterSnapshot operation.
    table_restore_status: "TableRestoreStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevisionTarget(ShapeBase):
    """
    Describes a `RevisionTarget`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "database_revision",
                "DatabaseRevision",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "database_revision_release_date",
                "DatabaseRevisionReleaseDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A unique string that identifies the version to update the cluster to. You
    # can use this value in ModifyClusterDbRevision.
    database_revision: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that describes the changes and features that will be applied to
    # the cluster when it is updated to the corresponding ClusterDbRevision.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date on which the database revision was released.
    database_revision_release_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeClusterSecurityGroupIngressMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_security_group_name",
                "ClusterSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "cidrip",
                "CIDRIP",
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

    # The name of the security Group from which to revoke the ingress rule.
    cluster_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IP range for which to revoke access. This range must be a valid
    # Classless Inter-Domain Routing (CIDR) block of IP addresses. If `CIDRIP` is
    # specified, `EC2SecurityGroupName` and `EC2SecurityGroupOwnerId` cannot be
    # provided.
    cidrip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the EC2 Security Group whose access is to be revoked. If
    # `EC2SecurityGroupName` is specified, `EC2SecurityGroupOwnerId` must also be
    # provided and `CIDRIP` cannot be provided.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account number of the owner of the security group specified in the
    # `EC2SecurityGroupName` parameter. The AWS access key ID is not an
    # acceptable value. If `EC2SecurityGroupOwnerId` is specified,
    # `EC2SecurityGroupName` must also be provided. and `CIDRIP` cannot be
    # provided.

    # Example: `111122223333`
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeClusterSecurityGroupIngressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_security_group",
                "ClusterSecurityGroup",
                TypeInfo(ClusterSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes a security group.
    cluster_security_group: "ClusterSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeSnapshotAccessMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "account_with_restore_access",
                "AccountWithRestoreAccess",
                TypeInfo(str),
            ),
            (
                "snapshot_cluster_identifier",
                "SnapshotClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the snapshot that the account can no longer access.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the AWS customer account that can no longer restore the
    # specified snapshot.
    account_with_restore_access: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the cluster the snapshot was created from. This parameter
    # is required if your IAM user has a policy containing a snapshot resource
    # element that specifies anything other than * for the cluster name.
    snapshot_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeSnapshotAccessResult(OutputShapeBase):
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

    # Describes a snapshot.
    snapshot: "Snapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateEncryptionKeyMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The unique identifier of the cluster that you want to rotate the encryption
    # keys for.

    # Constraints: Must be the name of valid cluster that has encryption enabled.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RotateEncryptionKeyResult(OutputShapeBase):
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

    # Describes a cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SNSInvalidTopicFault(ShapeBase):
    """
    Amazon SNS has responded that there is a problem with the specified Amazon SNS
    topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SNSNoAuthorizationFault(ShapeBase):
    """
    You do not have permission to publish to the specified Amazon SNS topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SNSTopicArnNotFoundFault(ShapeBase):
    """
    An Amazon SNS topic with the specified Amazon Resource Name (ARN) does not
    exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Snapshot(ShapeBase):
    """
    Describes a snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_create_time",
                "SnapshotCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "cluster_create_time",
                "ClusterCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "master_username",
                "MasterUsername",
                TypeInfo(str),
            ),
            (
                "cluster_version",
                "ClusterVersion",
                TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "number_of_nodes",
                "NumberOfNodes",
                TypeInfo(int),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "encrypted",
                "Encrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "encrypted_with_hsm",
                "EncryptedWithHSM",
                TypeInfo(bool),
            ),
            (
                "accounts_with_restore_access",
                "AccountsWithRestoreAccess",
                TypeInfo(typing.List[AccountWithRestoreAccess]),
            ),
            (
                "owner_account",
                "OwnerAccount",
                TypeInfo(str),
            ),
            (
                "total_backup_size_in_mega_bytes",
                "TotalBackupSizeInMegaBytes",
                TypeInfo(float),
            ),
            (
                "actual_incremental_backup_size_in_mega_bytes",
                "ActualIncrementalBackupSizeInMegaBytes",
                TypeInfo(float),
            ),
            (
                "backup_progress_in_mega_bytes",
                "BackupProgressInMegaBytes",
                TypeInfo(float),
            ),
            (
                "current_backup_rate_in_mega_bytes_per_second",
                "CurrentBackupRateInMegaBytesPerSecond",
                TypeInfo(float),
            ),
            (
                "estimated_seconds_to_completion",
                "EstimatedSecondsToCompletion",
                TypeInfo(int),
            ),
            (
                "elapsed_time_in_seconds",
                "ElapsedTimeInSeconds",
                TypeInfo(int),
            ),
            (
                "source_region",
                "SourceRegion",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "restorable_node_types",
                "RestorableNodeTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "enhanced_vpc_routing",
                "EnhancedVpcRouting",
                TypeInfo(bool),
            ),
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
        ]

    # The snapshot identifier that is provided in the request.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the cluster for which the snapshot was taken.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains
    # a copy of the cluster data as of this exact time.
    snapshot_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The snapshot status. The value of the status depends on the API operation
    # used.

    #   * CreateClusterSnapshot and CopyClusterSnapshot returns status as "creating".

    #   * DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".

    #   * DeleteClusterSnapshot returns status as "deleted".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port that the cluster is listening on.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone in which the cluster was created.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time (UTC) when the cluster was originally created.
    cluster_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The master user name for the cluster.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the Amazon Redshift engine that is running on the
    # cluster.
    cluster_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot type. Snapshots created using CreateClusterSnapshot and
    # CopyClusterSnapshot will be of type "manual".
    snapshot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The node type of the nodes in the cluster.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of nodes in the cluster.
    number_of_nodes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database that was created when the cluster was created.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC identifier of the cluster if the snapshot is from a cluster in a
    # VPC. Otherwise, this field is not in the output.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, the data in the snapshot is encrypted at rest.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (KMS) key ID of the encryption key that was
    # used to encrypt data in the cluster from which the snapshot was taken.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean that indicates whether the snapshot data is encrypted using the
    # HSM keys of the source cluster. `true` indicates that the data is encrypted
    # using HSM keys.
    encrypted_with_hsm: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the AWS customer accounts authorized to restore the snapshot.
    # Returns `null` if no accounts are authorized. Visible only to the snapshot
    # owner.
    accounts_with_restore_access: typing.List["AccountWithRestoreAccess"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # For manual snapshots, the AWS customer account used to create or copy the
    # snapshot. For automatic snapshots, the owner of the cluster. The owner can
    # perform all snapshot actions, such as sharing a manual snapshot.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the complete set of backup data that would be used to restore
    # the cluster.
    total_backup_size_in_mega_bytes: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the incremental backup.
    actual_incremental_backup_size_in_mega_bytes: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of megabytes that have been transferred to the snapshot backup.
    backup_progress_in_mega_bytes: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of megabytes per second being transferred to the snapshot
    # backup. Returns `0` for a completed backup.
    current_backup_rate_in_mega_bytes_per_second: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimate of the time remaining before the snapshot backup will
    # complete. Returns `0` for a completed backup.
    estimated_seconds_to_completion: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time an in-progress snapshot backup has been running, or the
    # amount of time it took a completed backup to finish.
    elapsed_time_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source region from which the snapshot was copied.
    source_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags for the cluster snapshot.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of node types that this cluster snapshot is able to restore into.
    restorable_node_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An option that specifies whether to create the cluster with enhanced VPC
    # routing enabled. To create a cluster that uses enhanced VPC routing, the
    # cluster must be in a VPC. For more information, see [Enhanced VPC
    # Routing](http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-
    # routing.html) in the Amazon Redshift Cluster Management Guide.

    # If this option is `true`, enhanced VPC routing is enabled.

    # Default: false
    enhanced_vpc_routing: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the maintenance track for the snapshot.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SnapshotCopyAlreadyDisabledFault(ShapeBase):
    """
    The cluster already has cross-region snapshot copy disabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotCopyAlreadyEnabledFault(ShapeBase):
    """
    The cluster already has cross-region snapshot copy enabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotCopyDisabledFault(ShapeBase):
    """
    Cross-region snapshot copy was temporarily disabled. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotCopyGrant(ShapeBase):
    """
    The snapshot copy grant that grants Amazon Redshift permission to encrypt copied
    snapshots with the specified customer master key (CMK) from AWS KMS in the
    destination region.

    For more information about managing snapshot copy grants, go to [Amazon Redshift
    Database Encryption](http://docs.aws.amazon.com/redshift/latest/mgmt/working-
    with-db-encryption.html) in the _Amazon Redshift Cluster Management Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_copy_grant_name",
                "SnapshotCopyGrantName",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the snapshot copy grant.
    snapshot_copy_grant_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the customer master key (CMK) in AWS KMS to which
    # Amazon Redshift is granted permission.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag instances.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SnapshotCopyGrantAlreadyExistsFault(ShapeBase):
    """
    The snapshot copy grant can't be created because a grant with the same name
    already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotCopyGrantMessage(OutputShapeBase):
    """

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
                "snapshot_copy_grants",
                "SnapshotCopyGrants",
                TypeInfo(typing.List[SnapshotCopyGrant]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional parameter that specifies the starting point to return a set of
    # response records. When the results of a `DescribeSnapshotCopyGrant` request
    # exceed the value specified in `MaxRecords`, AWS returns a value in the
    # `Marker` field of the response. You can retrieve the next set of response
    # records by providing the returned marker value in the `Marker` parameter
    # and retrying the request.

    # Constraints: You can specify either the **SnapshotCopyGrantName** parameter
    # or the **Marker** parameter, but not both.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of `SnapshotCopyGrant` objects.
    snapshot_copy_grants: typing.List["SnapshotCopyGrant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SnapshotCopyGrantNotFoundFault(ShapeBase):
    """
    The specified snapshot copy grant can't be found. Make sure that the name is
    typed correctly and that the grant exists in the destination region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotCopyGrantQuotaExceededFault(ShapeBase):
    """
    The AWS account has exceeded the maximum number of snapshot copy grants in this
    region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotMessage(OutputShapeBase):
    """
    Contains the output from the DescribeClusterSnapshots action.
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

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Snapshot instances.
    snapshots: typing.List["Snapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["SnapshotMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class SourceNotFoundFault(ShapeBase):
    """
    The specified Amazon Redshift event source could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class SourceType(str):
    cluster = "cluster"
    cluster_parameter_group = "cluster-parameter-group"
    cluster_security_group = "cluster-security-group"
    cluster_snapshot = "cluster-snapshot"


@dataclasses.dataclass
class Subnet(ShapeBase):
    """
    Describes a subnet.
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
            (
                "subnet_status",
                "SubnetStatus",
                TypeInfo(str),
            ),
        ]

    # The identifier of the subnet.
    subnet_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes an availability zone.
    subnet_availability_zone: "AvailabilityZone" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the subnet.
    subnet_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetAlreadyInUse(ShapeBase):
    """
    A specified subnet is already in use by another cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionAlreadyExistFault(ShapeBase):
    """
    There is already an existing event notification subscription with the specified
    name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionCategoryNotFoundFault(ShapeBase):
    """
    The value specified for the event category was not one of the allowed values, or
    it specified a category that does not apply to the specified source type. The
    allowed values are Configuration, Management, Monitoring, and Security.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionEventIdNotFoundFault(ShapeBase):
    """
    An Amazon Redshift event with the specified event ID does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionNotFoundFault(ShapeBase):
    """
    An Amazon Redshift event notification subscription with the specified name does
    not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionSeverityNotFoundFault(ShapeBase):
    """
    The value specified for the event severity was not one of the allowed values, or
    it specified a severity that does not apply to the specified source type. The
    allowed values are ERROR and INFO.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SupportedPlatform(ShapeBase):
    """
    A list of supported platforms for orderable clusters.
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

    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableLimitExceededFault(ShapeBase):
    """
    The number of tables in the cluster exceeds the limit for the requested new
    cluster node type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TableRestoreNotFoundFault(ShapeBase):
    """
    The specified `TableRestoreRequestId` value was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TableRestoreStatus(ShapeBase):
    """
    Describes the status of a RestoreTableFromClusterSnapshot operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_restore_request_id",
                "TableRestoreRequestId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, TableRestoreStatusType]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_time",
                "RequestTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "progress_in_mega_bytes",
                "ProgressInMegaBytes",
                TypeInfo(int),
            ),
            (
                "total_data_in_mega_bytes",
                "TotalDataInMegaBytes",
                TypeInfo(int),
            ),
            (
                "cluster_identifier",
                "ClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "source_database_name",
                "SourceDatabaseName",
                TypeInfo(str),
            ),
            (
                "source_schema_name",
                "SourceSchemaName",
                TypeInfo(str),
            ),
            (
                "source_table_name",
                "SourceTableName",
                TypeInfo(str),
            ),
            (
                "target_database_name",
                "TargetDatabaseName",
                TypeInfo(str),
            ),
            (
                "target_schema_name",
                "TargetSchemaName",
                TypeInfo(str),
            ),
            (
                "new_table_name",
                "NewTableName",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the table restore request.
    table_restore_request_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that describes the current state of the table restore request.

    # Valid Values: `SUCCEEDED`, `FAILED`, `CANCELED`, `PENDING`, `IN_PROGRESS`
    status: typing.Union[str, "TableRestoreStatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the status of the table restore request. Status values
    # include `SUCCEEDED`, `FAILED`, `CANCELED`, `PENDING`, `IN_PROGRESS`.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the table restore request was made, in Universal Coordinated
    # Time (UTC).
    request_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of data restored to the new table so far, in megabytes (MB).
    progress_in_mega_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total amount of data to restore to the new table, in megabytes (MB).
    total_data_in_mega_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the Amazon Redshift cluster that the table is being
    # restored to.
    cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the snapshot that the table is being restored from.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source database that contains the table being restored.
    source_database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source schema that contains the table being restored.
    source_schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source table being restored.
    source_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database to restore the table to.
    target_database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the schema to restore the table to.
    target_schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table to create as a result of the table restore request.
    new_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableRestoreStatusMessage(OutputShapeBase):
    """

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
                "table_restore_status_details",
                "TableRestoreStatusDetails",
                TypeInfo(typing.List[TableRestoreStatus]),
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

    # A list of status details for one or more table restore requests.
    table_restore_status_details: typing.List["TableRestoreStatus"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # A pagination token that can be used in a subsequent
    # DescribeTableRestoreStatus request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TableRestoreStatusType(str):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A tag consisting of a name/value pair for a resource.
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

    # The key, or name, for the resource tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the resource tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagLimitExceededFault(ShapeBase):
    """
    The number of tables in your source cluster exceeds the limit for the target
    cluster. Resize to a larger cluster node type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TaggedResource(ShapeBase):
    """
    A tag and its associated resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag",
                "Tag",
                TypeInfo(Tag),
            ),
            (
                "resource_name",
                "ResourceName",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
        ]

    # The tag for the resource.
    tag: "Tag" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) with which the tag is associated. For
    # example, `arn:aws:redshift:us-east-1:123456789:cluster:t1`.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource with which the tag is associated. Valid resource types
    # are:

    #   * Cluster

    #   * CIDR/IP

    #   * EC2 security group

    #   * Snapshot

    #   * Cluster security group

    #   * Subnet group

    #   * HSM connection

    #   * HSM certificate

    #   * Parameter group

    # For more information about Amazon Redshift resource types and constructing
    # ARNs, go to [Constructing an Amazon Redshift Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-
    # control-overview.html#redshift-iam-access-control-specify-actions) in the
    # Amazon Redshift Cluster Management Guide.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TaggedResourceListMessage(OutputShapeBase):
    """

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
                "tagged_resources",
                "TaggedResources",
                TypeInfo(typing.List[TaggedResource]),
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

    # A list of tags with their associated resources.
    tagged_resources: typing.List["TaggedResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates the starting point for the next set of response
    # records in a subsequent request. If a value is returned in a response, you
    # can retrieve the next set of records by providing this returned marker
    # value in the `Marker` parameter and retrying the command. If the `Marker`
    # field is empty, all response records have been retrieved for the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrackListMessage(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "maintenance_tracks",
                "MaintenanceTracks",
                TypeInfo(typing.List[MaintenanceTrack]),
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

    # A list of maintenance tracks output by the `DescribeClusterTracks`
    # operation.
    maintenance_tracks: typing.List["MaintenanceTrack"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The starting point to return a set of response tracklist records. You can
    # retrieve the next set of response records by providing the returned marker
    # value in the `Marker` parameter and retrying the request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnauthorizedOperation(ShapeBase):
    """
    Your account is not authorized to perform the requested operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnknownSnapshotCopyRegionFault(ShapeBase):
    """
    The specified region is incorrect or does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedOperationFault(ShapeBase):
    """
    The requested operation isn't supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedOptionFault(ShapeBase):
    """
    A request option was specified that is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateTarget(ShapeBase):
    """
    A maintenance track that you can switch the current track to.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maintenance_track_name",
                "MaintenanceTrackName",
                TypeInfo(str),
            ),
            (
                "database_version",
                "DatabaseVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the new maintenance track.
    maintenance_track_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cluster version for the new maintenance track.
    database_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VpcSecurityGroupMembership(ShapeBase):
    """
    Describes the members of a VPC security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_security_group_id",
                "VpcSecurityGroupId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The identifier of the VPC security group.
    vpc_security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the VPC security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )
