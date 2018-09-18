import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccountAttributesMessage(OutputShapeBase):
    """
    Data returned by the **DescribeAccountAttributes** action.
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
                "account_quotas",
                "AccountQuotas",
                TypeInfo(typing.List[AccountQuota]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of AccountQuota objects. Within this list, each quota has a name, a
    # count of usage toward the quota maximum, and a maximum value for the quota.
    account_quotas: typing.List["AccountQuota"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccountQuota(ShapeBase):
    """
    Describes a quota for an AWS account, for example, the number of DB instances
    allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_quota_name",
                "AccountQuotaName",
                TypeInfo(str),
            ),
            (
                "used",
                "Used",
                TypeInfo(int),
            ),
            (
                "max",
                "Max",
                TypeInfo(int),
            ),
        ]

    # The name of the Amazon RDS quota for this AWS account.
    account_quota_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount currently used toward the quota maximum.
    used: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum allowed value for the quota.
    max: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddRoleToDBClusterMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The name of the DB cluster to associate the IAM role with.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora
    # DB cluster, for example `arn:aws:iam::123456789012:role/AuroraAccessRole`.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddSourceIdentifierToSubscriptionMessage(ShapeBase):
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
                "source_identifier",
                "SourceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The name of the RDS event notification subscription you want to add a
    # source identifier to.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the event source to be added.

    # Constraints:

    #   * If the source type is a DB instance, then a `DBInstanceIdentifier` must be supplied.

    #   * If the source type is a DB security group, a `DBSecurityGroupName` must be supplied.

    #   * If the source type is a DB parameter group, a `DBParameterGroupName` must be supplied.

    #   * If the source type is a DB snapshot, a `DBSnapshotIdentifier` must be supplied.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddSourceIdentifierToSubscriptionResult(OutputShapeBase):
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

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsToResourceMessage(ShapeBase):
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
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon RDS resource that the tags are added to. This value is an Amazon
    # Resource Name (ARN). For information about creating an ARN, see [
    # Constructing an RDS Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing).
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to be assigned to the Amazon RDS resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ApplyMethod(str):
    immediate = "immediate"
    pending_reboot = "pending-reboot"


@dataclasses.dataclass
class ApplyPendingMaintenanceActionMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_identifier",
                "ResourceIdentifier",
                TypeInfo(str),
            ),
            (
                "apply_action",
                "ApplyAction",
                TypeInfo(str),
            ),
            (
                "opt_in_type",
                "OptInType",
                TypeInfo(str),
            ),
        ]

    # The RDS Amazon Resource Name (ARN) of the resource that the pending
    # maintenance action applies to. For information about creating an ARN, see [
    # Constructing an RDS Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing).
    resource_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pending maintenance action to apply to this resource.

    # Valid values: `system-update`, `db-upgrade`
    apply_action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that specifies the type of opt-in request, or undoes an opt-in
    # request. An opt-in request of type `immediate` can't be undone.

    # Valid values:

    #   * `immediate` \- Apply the maintenance action immediately.

    #   * `next-maintenance` \- Apply the maintenance action during the next maintenance window for the resource.

    #   * `undo-opt-in` \- Cancel any existing `next-maintenance` opt-in requests.
    opt_in_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplyPendingMaintenanceActionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_pending_maintenance_actions",
                "ResourcePendingMaintenanceActions",
                TypeInfo(ResourcePendingMaintenanceActions),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the pending maintenance actions for a resource.
    resource_pending_maintenance_actions: "ResourcePendingMaintenanceActions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizationAlreadyExistsFault(ShapeBase):
    """
    The specified CIDRIP or Amazon EC2 security group is already authorized for the
    specified DB security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizationNotFoundFault(ShapeBase):
    """
    The specified CIDRIP or Amazon EC2 security group isn't authorized for the
    specified DB security group.

    RDS also may not be authorized by using IAM to perform necessary actions on your
    behalf.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizationQuotaExceededFault(ShapeBase):
    """
    The DB security group authorization quota has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AuthorizeDBSecurityGroupIngressMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
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
                "ec2_security_group_id",
                "EC2SecurityGroupId",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_owner_id",
                "EC2SecurityGroupOwnerId",
                TypeInfo(str),
            ),
        ]

    # The name of the DB security group to add authorization to.
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP range to authorize.
    cidrip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the EC2 security group to authorize. For VPC DB security groups,
    # `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId`
    # and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Id of the EC2 security group to authorize. For VPC DB security groups,
    # `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId`
    # and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
    ec2_security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS account number of the owner of the EC2 security group specified in the
    # `EC2SecurityGroupName` parameter. The AWS Access Key ID is not an
    # acceptable value. For VPC DB security groups, `EC2SecurityGroupId` must be
    # provided. Otherwise, `EC2SecurityGroupOwnerId` and either
    # `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizeDBSecurityGroupIngressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_security_group",
                "DBSecurityGroup",
                TypeInfo(DBSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details for an Amazon RDS DB security group.

    # This data type is used as a response element in the
    # DescribeDBSecurityGroups action.
    db_security_group: "DBSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AvailabilityZone(ShapeBase):
    """
    Contains Availability Zone information.

    This data type is used as an element in the following data type:

      * OrderableDBInstanceOption
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
class AvailableProcessorFeature(ShapeBase):
    """
    Contains the available processor feature information for the DB instance class
    of a DB instance.

    For more information, see [Configuring the Processor of the DB Instance
    Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor)
    in the _Amazon RDS User Guide._
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
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "allowed_values",
                "AllowedValues",
                TypeInfo(str),
            ),
        ]

    # The name of the processor feature. Valid names are `coreCount` and
    # `threadsPerCore`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value for the processor feature of the DB instance class.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allowed values for the processor feature of the DB instance class.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BacktrackDBClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "backtrack_to",
                "BacktrackTo",
                TypeInfo(datetime.datetime),
            ),
            (
                "force",
                "Force",
                TypeInfo(bool),
            ),
            (
                "use_earliest_time_on_point_in_time_unavailable",
                "UseEarliestTimeOnPointInTimeUnavailable",
                TypeInfo(bool),
            ),
        ]

    # The DB cluster identifier of the DB cluster to be backtracked. This
    # parameter is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp of the time to backtrack the DB cluster to, specified in ISO
    # 8601 format. For more information about ISO 8601, see the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # If the specified time is not a consistent time for the DB cluster, Aurora
    # automatically chooses the nearest possible consistent time for the DB
    # cluster.

    # Constraints:

    #   * Must contain a valid ISO 8601 timestamp.

    #   * Cannot contain a timestamp set in the future.

    # Example: `2017-07-08T18:00Z`
    backtrack_to: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that, if specified, forces the DB cluster to backtrack when binary
    # logging is enabled. Otherwise, an error occurs when binary logging is
    # enabled.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If _BacktrackTo_ is set to a timestamp earlier than the earliest backtrack
    # time, this value backtracks the DB cluster to the earliest possible
    # backtrack time. Otherwise, an error occurs.
    use_earliest_time_on_point_in_time_unavailable: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BackupPolicyNotFoundFault(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Certificate(ShapeBase):
    """
    A CA certificate for an AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_identifier",
                "CertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "certificate_type",
                "CertificateType",
                TypeInfo(str),
            ),
            (
                "thumbprint",
                "Thumbprint",
                TypeInfo(str),
            ),
            (
                "valid_from",
                "ValidFrom",
                TypeInfo(datetime.datetime),
            ),
            (
                "valid_till",
                "ValidTill",
                TypeInfo(datetime.datetime),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # The unique key that identifies a certificate.
    certificate_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the certificate.
    certificate_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The thumbprint of the certificate.
    thumbprint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting date from which the certificate is valid.
    valid_from: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The final date that the certificate continues to be valid.
    valid_till: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the certificate.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CertificateMessage(OutputShapeBase):
    """
    Data returned by the **DescribeCertificates** action.
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
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
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

    # The list of Certificate objects for the AWS account.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous DescribeCertificates
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CertificateNotFoundFault(ShapeBase):
    """
    _CertificateIdentifier_ doesn't refer to an existing certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CharacterSet(ShapeBase):
    """
    This data type is used as a response element in the action
    DescribeDBEngineVersions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "character_set_name",
                "CharacterSetName",
                TypeInfo(str),
            ),
            (
                "character_set_description",
                "CharacterSetDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the character set.
    character_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the character set.
    character_set_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudwatchLogsExportConfiguration(ShapeBase):
    """
    The configuration setting for the log types to be enabled for export to
    CloudWatch Logs for a specific DB instance or DB cluster.

    The `EnableLogTypes` and `DisableLogTypes` arrays determine which logs will be
    exported (or not exported) to CloudWatch Logs. The values within these arrays
    depend on the DB engine being used. For more information, see [Publishing
    Database Logs to Amazon CloudWatch Logs
    ](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    in the _Amazon RDS User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable_log_types",
                "EnableLogTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "disable_log_types",
                "DisableLogTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The list of log types to enable.
    enable_log_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of log types to disable.
    disable_log_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyDBClusterParameterGroupMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_cluster_parameter_group_identifier",
                "SourceDBClusterParameterGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_cluster_parameter_group_identifier",
                "TargetDBClusterParameterGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_cluster_parameter_group_description",
                "TargetDBClusterParameterGroupDescription",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier or Amazon Resource Name (ARN) for the source DB cluster
    # parameter group. For information about creating an ARN, see [ Constructing
    # an ARN for Amazon
    # RDS](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing)
    # in the _Amazon Aurora User Guide_.

    # Constraints:

    #   * Must specify a valid DB cluster parameter group.

    #   * If the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier, for example `my-db-cluster-param-group`, or a valid ARN.

    #   * If the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN, for example `arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1`.
    source_db_cluster_parameter_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the copied DB cluster parameter group.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-cluster-param-group1`
    target_db_cluster_parameter_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the copied DB cluster parameter group.
    target_db_cluster_parameter_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyDBClusterParameterGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_parameter_group",
                "DBClusterParameterGroup",
                TypeInfo(DBClusterParameterGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster parameter group.

    # This data type is used as a response element in the
    # DescribeDBClusterParameterGroups action.
    db_cluster_parameter_group: "DBClusterParameterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyDBClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_cluster_snapshot_identifier",
                "SourceDBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_cluster_snapshot_identifier",
                "TargetDBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                TypeInfo(str),
            ),
            (
                "copy_tags",
                "CopyTags",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "source_region",
                "SourceRegion",
                TypeInfo(str),
            ),
        ]

    # The identifier of the DB cluster snapshot to copy. This parameter is not
    # case-sensitive.

    # You can't copy an encrypted, shared DB cluster snapshot from one AWS Region
    # to another.

    # Constraints:

    #   * Must specify a valid system snapshot in the "available" state.

    #   * If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier.

    #   * If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN. For more information, go to [ Copying Snapshots Across AWS Regions](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html#USER_CopySnapshot.AcrossRegions) in the _Amazon Aurora User Guide._

    # Example: `my-cluster-snapshot1`
    source_db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the new DB cluster snapshot to create from the source DB
    # cluster snapshot. This parameter is not case-sensitive.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster-snapshot2`
    target_db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS AWS KMS key ID for an encrypted DB cluster snapshot. The KMS key ID
    # is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias
    # for the KMS encryption key.

    # If you copy an encrypted DB cluster snapshot from your AWS account, you can
    # specify a value for `KmsKeyId` to encrypt the copy with a new KMS
    # encryption key. If you don't specify a value for `KmsKeyId`, then the copy
    # of the DB cluster snapshot is encrypted with the same KMS key as the source
    # DB cluster snapshot.

    # If you copy an encrypted DB cluster snapshot that is shared from another
    # AWS account, then you must specify a value for `KmsKeyId`.

    # To copy an encrypted DB cluster snapshot to another AWS Region, you must
    # set `KmsKeyId` to the KMS key ID you want to use to encrypt the copy of the
    # DB cluster snapshot in the destination AWS Region. KMS encryption keys are
    # specific to the AWS Region that they are created in, and you can't use
    # encryption keys from one AWS Region in another AWS Region.

    # If you copy an unencrypted DB cluster snapshot and specify a value for the
    # `KmsKeyId` parameter, an error is returned.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that contains a Signature Version 4 signed request for the
    # `CopyDBClusterSnapshot` API action in the AWS Region that contains the
    # source DB cluster snapshot to copy. The `PreSignedUrl` parameter must be
    # used when copying an encrypted DB cluster snapshot from another AWS Region.

    # The pre-signed URL must be a valid request for the `CopyDBSClusterSnapshot`
    # API action that can be executed in the source AWS Region that contains the
    # encrypted DB cluster snapshot to be copied. The pre-signed URL request must
    # contain the following parameter values:

    #   * `KmsKeyId` \- The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the `CopyDBClusterSnapshot` action that is called in the destination AWS Region, and the action contained in the pre-signed URL.

    #   * `DestinationRegion` \- The name of the AWS Region that the DB cluster snapshot will be created in.

    #   * `SourceDBClusterSnapshotIdentifier` \- The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your `SourceDBClusterSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115`.

    # To learn how to generate a Signature Version 4 signed request, see [
    # Authenticating Requests: Using Query Parameters (AWS Signature Version
    # 4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-
    # auth.html) and [ Signature Version 4 Signing
    # Process](http://docs.aws.amazon.com/general/latest/gr/signature-
    # version-4.html).
    pre_signed_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the source DB cluster snapshot to the target DB
    # cluster snapshot, and otherwise false. The default is false.
    copy_tags: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the region that contains the snapshot to be copied.
    source_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyDBClusterSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_snapshot",
                "DBClusterSnapshot",
                TypeInfo(DBClusterSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details for an Amazon RDS DB cluster snapshot

    # This data type is used as a response element in the
    # DescribeDBClusterSnapshots action.
    db_cluster_snapshot: "DBClusterSnapshot" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyDBParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_parameter_group_identifier",
                "SourceDBParameterGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_parameter_group_identifier",
                "TargetDBParameterGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_parameter_group_description",
                "TargetDBParameterGroupDescription",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier or ARN for the source DB parameter group. For information
    # about creating an ARN, see [ Constructing an ARN for Amazon
    # RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing)
    # in the _Amazon RDS User Guide_.

    # Constraints:

    #   * Must specify a valid DB parameter group.

    #   * Must specify a valid DB parameter group identifier, for example `my-db-param-group`, or a valid ARN.
    source_db_parameter_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the copied DB parameter group.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-db-parameter-group`
    target_db_parameter_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description for the copied DB parameter group.
    target_db_parameter_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyDBParameterGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_parameter_group",
                "DBParameterGroup",
                TypeInfo(DBParameterGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB parameter group.

    # This data type is used as a response element in the
    # DescribeDBParameterGroups action.
    db_parameter_group: "DBParameterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyDBSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_snapshot_identifier",
                "SourceDBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_snapshot_identifier",
                "TargetDBSnapshotIdentifier",
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
            (
                "copy_tags",
                "CopyTags",
                TypeInfo(bool),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "source_region",
                "SourceRegion",
                TypeInfo(str),
            ),
        ]

    # The identifier for the source DB snapshot.

    # If the source snapshot is in the same AWS Region as the copy, specify a
    # valid DB snapshot identifier. For example, you might specify `rds:mysql-
    # instance1-snapshot-20130805`.

    # If the source snapshot is in a different AWS Region than the copy, specify
    # a valid DB snapshot ARN. For example, you might specify `arn:aws:rds:us-
    # west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805`.

    # If you are copying from a shared manual DB snapshot, this parameter must be
    # the Amazon Resource Name (ARN) of the shared DB snapshot.

    # If you are copying an encrypted snapshot this parameter must be in the ARN
    # format for the source AWS Region, and must match the
    # `SourceDBSnapshotIdentifier` in the `PreSignedUrl` parameter.

    # Constraints:

    #   * Must specify a valid system snapshot in the "available" state.

    # Example: `rds:mydb-2012-04-02-00-01`

    # Example: `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-
    # instance1-snapshot-20130805`
    source_db_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the copy of the snapshot.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-db-snapshot`
    target_db_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS KMS key ID for an encrypted DB snapshot. The KMS key ID is the
    # Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for
    # the KMS encryption key.

    # If you copy an encrypted DB snapshot from your AWS account, you can specify
    # a value for this parameter to encrypt the copy with a new KMS encryption
    # key. If you don't specify a value for this parameter, then the copy of the
    # DB snapshot is encrypted with the same KMS key as the source DB snapshot.

    # If you copy an encrypted DB snapshot that is shared from another AWS
    # account, then you must specify a value for this parameter.

    # If you specify this parameter when you copy an unencrypted snapshot, the
    # copy is encrypted.

    # If you copy an encrypted snapshot to a different AWS Region, then you must
    # specify a KMS key for the destination AWS Region. KMS encryption keys are
    # specific to the AWS Region that they are created in, and you can't use
    # encryption keys from one AWS Region in another AWS Region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the source DB snapshot to the target DB
    # snapshot, and otherwise false. The default is false.
    copy_tags: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that contains a Signature Version 4 signed request for the
    # `CopyDBSnapshot` API action in the source AWS Region that contains the
    # source DB snapshot to copy.

    # You must specify this parameter when you copy an encrypted DB snapshot from
    # another AWS Region by using the Amazon RDS API. You can specify the
    # `--source-region` option instead of this parameter when you copy an
    # encrypted DB snapshot from another AWS Region by using the AWS CLI.

    # The presigned URL must be a valid request for the `CopyDBSnapshot` API
    # action that can be executed in the source AWS Region that contains the
    # encrypted DB snapshot to be copied. The presigned URL request must contain
    # the following parameter values:

    #   * `DestinationRegion` \- The AWS Region that the encrypted DB snapshot is copied to. This AWS Region is the same one where the `CopyDBSnapshot` action is called that contains this presigned URL.

    # For example, if you copy an encrypted DB snapshot from the us-west-2 AWS
    # Region to the us-east-1 AWS Region, then you call the `CopyDBSnapshot`
    # action in the us-east-1 AWS Region and provide a presigned URL that
    # contains a call to the `CopyDBSnapshot` action in the us-west-2 AWS Region.
    # For this example, the `DestinationRegion` in the presigned URL must be set
    # to the us-east-1 AWS Region.

    #   * `KmsKeyId` \- The AWS KMS key identifier for the key to use to encrypt the copy of the DB snapshot in the destination AWS Region. This is the same identifier for both the `CopyDBSnapshot` action that is called in the destination AWS Region, and the action contained in the presigned URL.

    #   * `SourceDBSnapshotIdentifier` \- The DB snapshot identifier for the encrypted snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB snapshot from the us-west-2 AWS Region, then your `SourceDBSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20161115`.

    # To learn how to generate a Signature Version 4 signed request, see
    # [Authenticating Requests: Using Query Parameters (AWS Signature Version
    # 4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-
    # auth.html) and [Signature Version 4 Signing
    # Process](http://docs.aws.amazon.com/general/latest/gr/signature-
    # version-4.html).
    pre_signed_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an option group to associate with the copy of the snapshot.

    # Specify this option if you are copying a snapshot from one AWS Region to
    # another, and your DB instance uses a nondefault option group. If your
    # source DB instance uses Transparent Data Encryption for Oracle or Microsoft
    # SQL Server, you must specify this option when copying across AWS Regions.
    # For more information, see [Option Group
    # Considerations](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopySnapshot.Options)
    # in the _Amazon RDS User Guide._
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the region that contains the snapshot to be copied.
    source_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyDBSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_snapshot",
                "DBSnapshot",
                TypeInfo(DBSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB snapshot.

    # This data type is used as a response element in the DescribeDBSnapshots
    # action.
    db_snapshot: "DBSnapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyOptionGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_option_group_identifier",
                "SourceOptionGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "target_option_group_identifier",
                "TargetOptionGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "target_option_group_description",
                "TargetOptionGroupDescription",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier or ARN for the source option group. For information about
    # creating an ARN, see [ Constructing an ARN for Amazon
    # RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing)
    # in the _Amazon RDS User Guide_.

    # Constraints:

    #   * Must specify a valid option group.

    #   * If the source option group is in the same AWS Region as the copy, specify a valid option group identifier, for example `my-option-group`, or a valid ARN.

    #   * If the source option group is in a different AWS Region than the copy, specify a valid option group ARN, for example `arn:aws:rds:us-west-2:123456789012:og:special-options`.
    source_option_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the copied option group.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-option-group`
    target_option_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for the copied option group.
    target_option_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyOptionGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "option_group",
                "OptionGroup",
                TypeInfo(OptionGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    option_group: "OptionGroup" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
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
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "replication_source_identifier",
                "ReplicationSourceIdentifier",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "backtrack_window",
                "BacktrackWindow",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "engine_mode",
                "EngineMode",
                TypeInfo(str),
            ),
            (
                "scaling_configuration",
                "ScalingConfiguration",
                TypeInfo(ScalingConfiguration),
            ),
            (
                "source_region",
                "SourceRegion",
                TypeInfo(str),
            ),
        ]

    # The DB cluster identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database engine to be used for this DB cluster.

    # Valid Values: `aurora` (for MySQL 5.6-compatible Aurora), `aurora-mysql`
    # (for MySQL 5.7-compatible Aurora), and `aurora-postgresql`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of EC2 Availability Zones that instances in the DB cluster can be
    # created in. For information on AWS Regions and Availability Zones, see
    # [Choosing the Regions and Availability
    # Zones](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html)
    # in the _Amazon Aurora User Guide_.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which automated backups are retained. You must
    # specify a minimum value of 1.

    # Default: 1

    # Constraints:

    #   * Must be a value from 1 to 35
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates that the DB cluster should be associated with the
    # specified CharacterSet.
    character_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for your database of up to 64 alpha-numeric characters. If you do
    # not provide a name, Amazon RDS will not create a database in the DB cluster
    # you are creating.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the DB cluster parameter group to associate with this DB
    # cluster. If this argument is omitted, `default.aurora5.6` is used.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of EC2 VPC security groups to associate with this DB cluster.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DB subnet group to associate with this DB cluster.

    # Constraints: Must match the name of an existing DBSubnetGroup. Must not be
    # default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the database engine to use.

    # **Aurora MySQL**

    # Example: `5.6.10a`, `5.7.12`

    # **Aurora PostgreSQL**

    # Example: `9.6.3`
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on which the instances in the DB cluster accept
    # connections.

    # Default: `3306` if engine is set as aurora or `5432` if set to aurora-
    # postgresql.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the master user for the DB cluster.

    # Constraints:

    #   * Must be 1 to 16 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the master database user. This password can contain any
    # printable ASCII character except "/", """, or "@".

    # Constraints: Must contain from 8 to 41 characters.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates that the DB cluster should be associated with the
    # specified option group.

    # Permanent options can't be removed from an option group. The option group
    # can't be removed from a DB cluster once it is associated with a DB cluster.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The daily time range during which automated backups are created if
    # automated backups are enabled using the `BackupRetentionPeriod` parameter.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region. To see the time blocks available, see [
    # Adjusting the Preferred DB Cluster Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora)
    # in the _Amazon Aurora User Guide._

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week. To see
    # the time blocks available, see [ Adjusting the Preferred DB Cluster
    # Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora)
    # in the _Amazon Aurora User Guide._

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the source DB instance or DB cluster if
    # this DB cluster is created as a Read Replica.
    replication_source_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB cluster is encrypted.
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key identifier for an encrypted DB cluster.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are creating a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KMS encryption
    # key.

    # If an encryption key is not specified in `KmsKeyId`:

    #   * If `ReplicationSourceIdentifier` identifies an encrypted source, then Amazon RDS will use the encryption key used to encrypt the source. Otherwise, Amazon RDS will use your default encryption key.

    #   * If the `StorageEncrypted` parameter is true and `ReplicationSourceIdentifier` is not specified, then Amazon RDS will use your default encryption key.

    # AWS KMS creates the default encryption key for your AWS account. Your AWS
    # account has a different default encryption key for each AWS Region.

    # If you create a Read Replica of an encrypted DB cluster in another AWS
    # Region, you must set `KmsKeyId` to a KMS key ID that is valid in the
    # destination AWS Region. This key is used to encrypt the Read Replica in
    # that AWS Region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL that contains a Signature Version 4 signed request for the
    # `CreateDBCluster` action to be called in the source AWS Region where the DB
    # cluster is replicated from. You only need to specify `PreSignedUrl` when
    # you are performing cross-region replication from an encrypted DB cluster.

    # The pre-signed URL must be a valid request for the `CreateDBCluster` API
    # action that can be executed in the source AWS Region that contains the
    # encrypted DB cluster to be copied.

    # The pre-signed URL request must contain the following parameter values:

    #   * `KmsKeyId` \- The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster in the destination AWS Region. This should refer to the same KMS key for both the `CreateDBCluster` action that is called in the destination AWS Region, and the action contained in the pre-signed URL.

    #   * `DestinationRegion` \- The name of the AWS Region that Aurora Read Replica will be created in.

    #   * `ReplicationSourceIdentifier` \- The DB cluster identifier for the encrypted DB cluster to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster from the us-west-2 AWS Region, then your `ReplicationSourceIdentifier` would look like Example: `arn:aws:rds:us-west-2:123456789012:cluster:aurora-cluster1`.

    # To learn how to generate a Signature Version 4 signed request, see [
    # Authenticating Requests: Using Query Parameters (AWS Signature Version
    # 4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-
    # auth.html) and [ Signature Version 4 Signing
    # Process](http://docs.aws.amazon.com/general/latest/gr/signature-
    # version-4.html).
    pre_signed_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target backtrack window, in seconds. To disable backtracking, set this
    # value to 0.

    # Default: 0

    # Constraints:

    #   * If specified, this value must be set to a number from 0 to 259,200 (72 hours).
    backtrack_window: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of log types that need to be enabled for exporting to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon Aurora User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB engine mode of the DB cluster, either `provisioned` or `serverless`.
    engine_mode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For DB clusters in `serverless` DB engine mode, the scaling properties of
    # the DB cluster.
    scaling_configuration: "ScalingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the region that contains the source for the db cluster.
    source_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
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

    # The name of the DB cluster parameter group.

    # Constraints:

    #   * Must match the name of an existing DBClusterParameterGroup.

    # This value is stored as a lowercase string.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB cluster parameter group family name. A DB cluster parameter group
    # can be associated with one and only one DB cluster parameter group family,
    # and can be applied only to a DB cluster running a database engine and
    # engine version compatible with that DB cluster parameter group family.

    # **Aurora MySQL**

    # Example: `aurora5.6`, `aurora-mysql5.7`

    # **Aurora PostgreSQL**

    # Example: `aurora-postgresql9.6`
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for the DB cluster parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBClusterParameterGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_parameter_group",
                "DBClusterParameterGroup",
                TypeInfo(DBClusterParameterGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster parameter group.

    # This data type is used as a response element in the
    # DescribeDBClusterParameterGroups action.
    db_cluster_parameter_group: "DBClusterParameterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDBClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier of the DB cluster snapshot. This parameter is stored as a
    # lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1-snapshot1`
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the DB cluster to create a snapshot for. This parameter
    # is not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to be assigned to the DB cluster snapshot.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBClusterSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_snapshot",
                "DBClusterSnapshot",
                TypeInfo(DBClusterSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details for an Amazon RDS DB cluster snapshot

    # This data type is used as a response element in the
    # DescribeDBClusterSnapshots action.
    db_cluster_snapshot: "DBClusterSnapshot" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDBInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
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
                "db_security_groups",
                "DBSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "multi_az",
                "MultiAZ",
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
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                TypeInfo(str),
            ),
            (
                "tde_credential_password",
                "TdeCredentialPassword",
                TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                TypeInfo(int),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                TypeInfo(str),
            ),
            (
                "domain_iam_role_name",
                "DomainIAMRoleName",
                TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                TypeInfo(int),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "enable_performance_insights",
                "EnablePerformanceInsights",
                TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                TypeInfo(str),
            ),
            (
                "performance_insights_retention_period",
                "PerformanceInsightsRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
        ]

    # The DB instance identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `mydbinstance`
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute and memory capacity of the DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions, or for all database engines. For the full list of DB instance
    # classes, and availability for your engine, see [DB Instance
    # Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
    # in the _Amazon RDS User Guide._
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database engine to be used for this instance.

    # Not every database engine is available for every AWS Region.

    # Valid Values:

    #   * `aurora` (for MySQL 5.6-compatible Aurora)

    #   * `aurora-mysql` (for MySQL 5.7-compatible Aurora)

    #   * `aurora-postgresql`

    #   * `mariadb`

    #   * `mysql`

    #   * `oracle-ee`

    #   * `oracle-se2`

    #   * `oracle-se1`

    #   * `oracle-se`

    #   * `postgres`

    #   * `sqlserver-ee`

    #   * `sqlserver-se`

    #   * `sqlserver-ex`

    #   * `sqlserver-web`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The meaning of this parameter differs according to the database engine you
    # use.

    # Type: String

    # **MySQL**

    # The name of the database to create when the DB instance is created. If this
    # parameter is not specified, no database is created in the DB instance.

    # Constraints:

    #   * Must contain 1 to 64 letters or numbers.

    #   * Cannot be a word reserved by the specified database engine

    # **MariaDB**

    # The name of the database to create when the DB instance is created. If this
    # parameter is not specified, no database is created in the DB instance.

    # Constraints:

    #   * Must contain 1 to 64 letters or numbers.

    #   * Cannot be a word reserved by the specified database engine

    # **PostgreSQL**

    # The name of the database to create when the DB instance is created. If this
    # parameter is not specified, the default "postgres" database is created in
    # the DB instance.

    # Constraints:

    #   * Must contain 1 to 63 letters, numbers, or underscores.

    #   * Must begin with a letter or an underscore. Subsequent characters can be letters, underscores, or digits (0-9).

    #   * Cannot be a word reserved by the specified database engine

    # **Oracle**

    # The Oracle System ID (SID) of the created DB instance. If you specify
    # `null`, the default value `ORCL` is used. You can't specify the string
    # NULL, or any other reserved word, for `DBName`.

    # Default: `ORCL`

    # Constraints:

    #   * Cannot be longer than 8 characters

    # **SQL Server**

    # Not applicable. Must be null.

    # **Amazon Aurora**

    # The name of the database to create when the primary instance of the DB
    # cluster is created. If this parameter is not specified, no database is
    # created in the DB instance.

    # Constraints:

    #   * Must contain 1 to 64 letters or numbers.

    #   * Cannot be a word reserved by the specified database engine
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of storage (in gibibytes) to allocate for the DB instance.

    # Type: Integer

    # **Amazon Aurora**

    # Not applicable. Aurora cluster volumes automatically grow as the amount of
    # data in your database increases, though you are only charged for the space
    # that you use in an Aurora cluster volume.

    # **MySQL**

    # Constraints to the amount of storage for each storage type are the
    # following:

    #   * General Purpose (SSD) storage (gp2): Must be an integer from 20 to 16384.

    #   * Provisioned IOPS storage (io1): Must be an integer from 100 to 16384.

    #   * Magnetic storage (standard): Must be an integer from 5 to 3072.

    # **MariaDB**

    # Constraints to the amount of storage for each storage type are the
    # following:

    #   * General Purpose (SSD) storage (gp2): Must be an integer from 20 to 16384.

    #   * Provisioned IOPS storage (io1): Must be an integer from 100 to 16384.

    #   * Magnetic storage (standard): Must be an integer from 5 to 3072.

    # **PostgreSQL**

    # Constraints to the amount of storage for each storage type are the
    # following:

    #   * General Purpose (SSD) storage (gp2): Must be an integer from 20 to 16384.

    #   * Provisioned IOPS storage (io1): Must be an integer from 100 to 16384.

    #   * Magnetic storage (standard): Must be an integer from 5 to 3072.

    # **Oracle**

    # Constraints to the amount of storage for each storage type are the
    # following:

    #   * General Purpose (SSD) storage (gp2): Must be an integer from 20 to 16384.

    #   * Provisioned IOPS storage (io1): Must be an integer from 100 to 16384.

    #   * Magnetic storage (standard): Must be an integer from 10 to 3072.

    # **SQL Server**

    # Constraints to the amount of storage for each storage type are the
    # following:

    #   * General Purpose (SSD) storage (gp2):

    #     * Enterprise and Standard editions: Must be an integer from 200 to 16384.

    #     * Web and Express editions: Must be an integer from 20 to 16384.

    #   * Provisioned IOPS storage (io1):

    #     * Enterprise and Standard editions: Must be an integer from 200 to 16384.

    #     * Web and Express editions: Must be an integer from 100 to 16384.

    #   * Magnetic storage (standard):

    #     * Enterprise and Standard editions: Must be an integer from 200 to 1024.

    #     * Web and Express editions: Must be an integer from 20 to 1024.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the master user.

    # **Amazon Aurora**

    # Not applicable. The name for the master user is managed by the DB cluster.
    # For more information, see CreateDBCluster.

    # **MariaDB**

    # Constraints:

    #   * Required for MariaDB.

    #   * Must be 1 to 16 letters or numbers.

    #   * Cannot be a reserved word for the chosen database engine.

    # **Microsoft SQL Server**

    # Constraints:

    #   * Required for SQL Server.

    #   * Must be 1 to 128 letters or numbers.

    #   * The first character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.

    # **MySQL**

    # Constraints:

    #   * Required for MySQL.

    #   * Must be 1 to 16 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.

    # **Oracle**

    # Constraints:

    #   * Required for Oracle.

    #   * Must be 1 to 30 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.

    # **PostgreSQL**

    # Constraints:

    #   * Required for PostgreSQL.

    #   * Must be 1 to 63 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the master user. The password can include any printable
    # ASCII character except "/", """, or "@".

    # **Amazon Aurora**

    # Not applicable. The password for the master user is managed by the DB
    # cluster. For more information, see CreateDBCluster.

    # **MariaDB**

    # Constraints: Must contain from 8 to 41 characters.

    # **Microsoft SQL Server**

    # Constraints: Must contain from 8 to 128 characters.

    # **MySQL**

    # Constraints: Must contain from 8 to 41 characters.

    # **Oracle**

    # Constraints: Must contain from 8 to 30 characters.

    # **PostgreSQL**

    # Constraints: Must contain from 8 to 128 characters.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DB security groups to associate with this DB instance.

    # Default: The default DB security group for the database engine.
    db_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of EC2 VPC security groups to associate with this DB instance.

    # **Amazon Aurora**

    # Not applicable. The associated list of EC2 VPC security groups is managed
    # by the DB cluster. For more information, see CreateDBCluster.

    # Default: The default EC2 VPC security group for the DB subnet group's VPC.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 Availability Zone that the DB instance is created in. For
    # information on AWS Regions and Availability Zones, see [Regions and
    # Availability
    # Zones](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).

    # Default: A random, system-chosen Availability Zone in the endpoint's AWS
    # Region.

    # Example: `us-east-1d`

    # Constraint: The AvailabilityZone parameter can't be specified if the
    # MultiAZ parameter is set to `true`. The specified Availability Zone must be
    # in the same AWS Region as the current endpoint.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A DB subnet group to associate with this DB instance.

    # If there is no DB subnet group, then it is a non-VPC DB instance.
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time range each week during which system maintenance can occur, in
    # Universal Coordinated Time (UTC). For more information, see [Amazon RDS
    # Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week.

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the DB parameter group to associate with this DB instance. If
    # this argument is omitted, the default DBParameterGroup for the specified
    # engine is used.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which automated backups are retained. Setting this
    # parameter to a positive number enables backups. Setting this parameter to 0
    # disables automated backups.

    # **Amazon Aurora**

    # Not applicable. The retention period for automated backups is managed by
    # the DB cluster. For more information, see CreateDBCluster.

    # Default: 1

    # Constraints:

    #   * Must be a value from 0 to 35

    #   * Cannot be set to 0 if the DB instance is a source to Read Replicas
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created if
    # automated backups are enabled, using the `BackupRetentionPeriod` parameter.
    # For more information, see [The Backup
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow)
    # in the _Amazon RDS User Guide_.

    # **Amazon Aurora**

    # Not applicable. The daily time range for creating automated backups is
    # managed by the DB cluster. For more information, see CreateDBCluster.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region. To see the time blocks available, see [
    # Adjusting the Preferred DB Instance Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow)
    # in the _Amazon RDS User Guide_.

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which the database accepts connections.

    # **MySQL**

    # Default: `3306`

    # Valid Values: `1150-65535`

    # Type: Integer

    # **MariaDB**

    # Default: `3306`

    # Valid Values: `1150-65535`

    # Type: Integer

    # **PostgreSQL**

    # Default: `5432`

    # Valid Values: `1150-65535`

    # Type: Integer

    # **Oracle**

    # Default: `1521`

    # Valid Values: `1150-65535`

    # **SQL Server**

    # Default: `1433`

    # Valid Values: `1150-65535` except for `1434`, `3389`, `47001`, `49152`, and
    # `49152` through `49156`.

    # **Amazon Aurora**

    # Default: `3306`

    # Valid Values: `1150-65535`

    # Type: Integer
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies if the DB instance is a Multi-AZ deployment. You can't set the
    # AvailabilityZone parameter if the MultiAZ parameter is set to true.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the database engine to use.

    # For a list of valid engine versions, call DescribeDBEngineVersions.

    # The following are the database engines and links to information about the
    # major and minor versions that are available with Amazon RDS. Not every
    # database engine is available for every AWS Region.

    # **Amazon Aurora**

    # Not applicable. The version number of the database engine to be used by the
    # DB instance is managed by the DB cluster. For more information, see
    # CreateDBCluster.

    # **MariaDB**

    # See [MariaDB on Amazon RDS
    # Versions](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt)
    # in the _Amazon RDS User Guide._

    # **Microsoft SQL Server**

    # See [Version and Feature Support on Amazon
    # RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport)
    # in the _Amazon RDS User Guide._

    # **MySQL**

    # See [MySQL on Amazon RDS
    # Versions](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt)
    # in the _Amazon RDS User Guide._

    # **Oracle**

    # See [Oracle Database Engine Release
    # Notes](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.PatchComposition.html)
    # in the _Amazon RDS User Guide._

    # **PostgreSQL**

    # See [Supported PostgreSQL Database
    # Versions](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.DBVersions)
    # in the _Amazon RDS User Guide._
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that minor engine upgrades are applied automatically to the DB
    # instance during the maintenance window.

    # Default: `true`
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # License model information for this DB instance.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of Provisioned IOPS (input/output operations per second) to be
    # initially allocated for the DB instance. For information about valid Iops
    # values, see see [Amazon RDS Provisioned IOPS Storage to Improve
    # Performance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS)
    # in the _Amazon RDS User Guide_.

    # Constraints: Must be a multiple between 1 and 50 of the storage amount for
    # the DB instance. Must also be an integer multiple of 1000. For example, if
    # the size of your DB instance is 500 GiB, then your `Iops` value can be
    # 2000, 3000, 4000, or 5000.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the DB instance should be associated with the specified
    # option group.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For supported engines, indicates that the DB instance should be associated
    # with the specified CharacterSet.

    # **Amazon Aurora**

    # Not applicable. The character set is managed by the DB cluster. For more
    # information, see CreateDBCluster.
    character_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the accessibility options for the DB instance. A value of true
    # specifies an Internet-facing instance with a publicly resolvable DNS name,
    # which resolves to a public IP address. A value of false specifies an
    # internal instance with a DNS name that resolves to a private IP address.

    # Default: The default behavior varies depending on whether
    # `DBSubnetGroupName` is specified.

    # If `DBSubnetGroupName` is not specified, and `PubliclyAccessible` is not
    # specified, the following applies:

    #   * If the default VPC in the target region doesn’t have an Internet gateway attached to it, the DB instance is private.

    #   * If the default VPC in the target region has an Internet gateway attached to it, the DB instance is public.

    # If `DBSubnetGroupName` is specified, and `PubliclyAccessible` is not
    # specified, the following applies:

    #   * If the subnets are part of a VPC that doesn’t have an Internet gateway attached to it, the DB instance is private.

    #   * If the subnets are part of a VPC that has an Internet gateway attached to it, the DB instance is public.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the DB cluster that the instance will belong to.

    # For information on creating a DB cluster, see CreateDBCluster.

    # Type: String
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the storage type to be associated with the DB instance.

    # Valid values: `standard | gp2 | io1`

    # If you specify `io1`, you must also include a value for the `Iops`
    # parameter.

    # Default: `io1` if the `Iops` parameter is specified, otherwise `standard`
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the given ARN from the key store in order to access the
    # device.
    tde_credential_password: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the DB instance is encrypted.

    # **Amazon Aurora**

    # Not applicable. The encryption for DB instances is managed by the DB
    # cluster. For more information, see CreateDBCluster.

    # Default: false
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key identifier for an encrypted DB instance.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are creating a DB instance with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB instance, then
    # you can use the KMS key alias instead of the ARN for the KM encryption key.

    # **Amazon Aurora**

    # Not applicable. The KMS key identifier is managed by the DB cluster. For
    # more information, see CreateDBCluster.

    # If the `StorageEncrypted` parameter is true, and you do not specify a value
    # for the `KmsKeyId` parameter, then Amazon RDS will use your default
    # encryption key. AWS KMS creates the default encryption key for your AWS
    # account. Your AWS account has a different default encryption key for each
    # AWS Region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the Active Directory Domain to create the instance in.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the DB instance to snapshots of the DB instance,
    # and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance. To disable collecting Enhanced
    # Monitoring metrics, specify 0. The default is 0.

    # If `MonitoringRoleArn` is specified, then you must also set
    # `MonitoringInterval` to a value other than 0.

    # Valid Values: `0, 1, 5, 10, 15, 30, 60`
    monitoring_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the IAM role that permits RDS to send enhanced monitoring
    # metrics to Amazon CloudWatch Logs. For example,
    # `arn:aws:iam:123456789012:role/emaccess`. For information on creating a
    # monitoring role, go to [Setting Up and Enabling Enhanced
    # Monitoring](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling)
    # in the _Amazon RDS User Guide_.

    # If `MonitoringInterval` is set to a value other than 0, then you must
    # supply a `MonitoringRoleArn` value.
    monitoring_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the name of the IAM role to be used when making API calls to the
    # Directory Service.
    domain_iam_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that specifies the order in which an Aurora Replica is promoted to
    # the primary instance after a failure of the existing primary instance. For
    # more information, see [ Fault Tolerance for an Aurora DB
    # Cluster](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance)
    # in the _Amazon Aurora User Guide_.

    # Default: 1

    # Valid Values: 0 - 15
    promotion_tier: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone of the DB instance. The time zone parameter is currently
    # supported only by [Microsoft SQL
    # Server](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone).
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # You can enable IAM database authentication for the following database
    # engines:

    # **Amazon Aurora**

    # Not applicable. Mapping AWS IAM accounts to database accounts is managed by
    # the DB cluster. For more information, see CreateDBCluster.

    # **MySQL**

    #   * For MySQL 5.6, minor version 5.6.34 or higher

    #   * For MySQL 5.7, minor version 5.7.16 or higher

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True to enable Performance Insights for the DB instance, and otherwise
    # false.

    # For more information, see [Using Amazon Performance
    # Insights](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
    # in the _Amazon Relational Database Service User Guide_.
    enable_performance_insights: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in days, to retain Performance Insights data. Valid
    # values are 7 or 731 (2 years).
    performance_insights_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of log types that need to be enabled for exporting to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch Logs
    # ](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon Relational Database Service User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDBInstanceReadReplicaMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "source_db_instance_identifier",
                "SourceDBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                TypeInfo(int),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "pre_signed_url",
                "PreSignedUrl",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "enable_performance_insights",
                "EnablePerformanceInsights",
                TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                TypeInfo(str),
            ),
            (
                "performance_insights_retention_period",
                "PerformanceInsightsRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
            (
                "use_default_processor_features",
                "UseDefaultProcessorFeatures",
                TypeInfo(bool),
            ),
            (
                "source_region",
                "SourceRegion",
                TypeInfo(str),
            ),
        ]

    # The DB instance identifier of the Read Replica. This identifier is the
    # unique key that identifies a DB instance. This parameter is stored as a
    # lowercase string.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the DB instance that will act as the source for the Read
    # Replica. Each DB instance can have up to five Read Replicas.

    # Constraints:

    #   * Must be the identifier of an existing MySQL, MariaDB, or PostgreSQL DB instance.

    #   * Can specify a DB instance that is a MySQL Read Replica only if the source is running MySQL 5.6.

    #   * Can specify a DB instance that is a PostgreSQL DB instance only if the source is running PostgreSQL 9.3.5 or later (9.4.7 and higher for cross-region replication).

    #   * The specified DB instance must have automatic backups enabled, its backup retention period must be greater than 0.

    #   * If the source DB instance is in the same AWS Region as the Read Replica, specify a valid DB instance identifier.

    #   * If the source DB instance is in a different AWS Region than the Read Replica, specify a valid DB instance ARN. For more information, go to [ Constructing an ARN for Amazon RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing) in the _Amazon RDS User Guide_.
    source_db_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compute and memory capacity of the Read Replica, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions, or for all database engines. For the full list of DB instance
    # classes, and availability for your engine, see [DB Instance
    # Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
    # in the _Amazon RDS User Guide._

    # Default: Inherits from the source DB instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 Availability Zone that the Read Replica is created in.

    # Default: A random, system-chosen Availability Zone in the endpoint's AWS
    # Region.

    # Example: `us-east-1d`
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number that the DB instance uses for connections.

    # Default: Inherits from the source DB instance

    # Valid Values: `1150-65535`
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the Read Replica is in a Multi-AZ deployment.

    # You can create a Read Replica as a Multi-AZ DB instance. RDS creates a
    # standby of your replica in another Availability Zone for failover support
    # for the replica. Creating your Read Replica as a Multi-AZ DB instance is
    # independent of whether the source database is a Multi-AZ DB instance.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that minor engine upgrades are applied automatically to the Read
    # Replica during the maintenance window.

    # Default: Inherits from the source DB instance
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of Provisioned IOPS (input/output operations per second) to be
    # initially allocated for the DB instance.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The option group the DB instance is associated with. If omitted, the
    # default option group for the engine specified is used.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the accessibility options for the DB instance. A value of true
    # specifies an Internet-facing instance with a publicly resolvable DNS name,
    # which resolves to a public IP address. A value of false specifies an
    # internal instance with a DNS name that resolves to a private IP address.
    # For more information, see CreateDBInstance.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a DB subnet group for the DB instance. The new DB instance is
    # created in the VPC associated with the DB subnet group. If no DB subnet
    # group is specified, then the new DB instance is not created in a VPC.

    # Constraints:

    #   * Can only be specified if the source DB instance identifier specifies a DB instance in another AWS Region.

    #   * If supplied, must match the name of an existing DBSubnetGroup.

    #   * The specified DB subnet group must be in the same AWS Region in which the operation is running.

    #   * All Read Replicas in one AWS Region that are created from the same source DB instance must either:>

    #     * Specify DB subnet groups from the same VPC. All these Read Replicas are created in the same VPC.

    #     * Not specify a DB subnet group. All these Read Replicas are created outside of any VPC.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the storage type to be associated with the Read Replica.

    # Valid values: `standard | gp2 | io1`

    # If you specify `io1`, you must also include a value for the `Iops`
    # parameter.

    # Default: `io1` if the `Iops` parameter is specified, otherwise `standard`
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the Read Replica to snapshots of the Read
    # Replica, and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the Read Replica. To disable collecting Enhanced
    # Monitoring metrics, specify 0. The default is 0.

    # If `MonitoringRoleArn` is specified, then you must also set
    # `MonitoringInterval` to a value other than 0.

    # Valid Values: `0, 1, 5, 10, 15, 30, 60`
    monitoring_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the IAM role that permits RDS to send enhanced monitoring
    # metrics to Amazon CloudWatch Logs. For example,
    # `arn:aws:iam:123456789012:role/emaccess`. For information on creating a
    # monitoring role, go to [To create an IAM role for Amazon RDS Enhanced
    # Monitoring](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole)
    # in the _Amazon RDS User Guide_.

    # If `MonitoringInterval` is set to a value other than 0, then you must
    # supply a `MonitoringRoleArn` value.
    monitoring_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key ID for an encrypted Read Replica. The KMS key ID is the
    # Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for
    # the KMS encryption key.

    # If you specify this parameter when you create a Read Replica from an
    # unencrypted DB instance, the Read Replica is encrypted.

    # If you create an encrypted Read Replica in the same AWS Region as the
    # source DB instance, then you do not have to specify a value for this
    # parameter. The Read Replica is encrypted with the same KMS key as the
    # source DB instance.

    # If you create an encrypted Read Replica in a different AWS Region, then you
    # must specify a KMS key for the destination AWS Region. KMS encryption keys
    # are specific to the AWS Region that they are created in, and you can't use
    # encryption keys from one AWS Region in another AWS Region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that contains a Signature Version 4 signed request for the
    # `CreateDBInstanceReadReplica` API action in the source AWS Region that
    # contains the source DB instance.

    # You must specify this parameter when you create an encrypted Read Replica
    # from another AWS Region by using the Amazon RDS API. You can specify the
    # `--source-region` option instead of this parameter when you create an
    # encrypted Read Replica from another AWS Region by using the AWS CLI.

    # The presigned URL must be a valid request for the
    # `CreateDBInstanceReadReplica` API action that can be executed in the source
    # AWS Region that contains the encrypted source DB instance. The presigned
    # URL request must contain the following parameter values:

    #   * `DestinationRegion` \- The AWS Region that the encrypted Read Replica is created in. This AWS Region is the same one where the `CreateDBInstanceReadReplica` action is called that contains this presigned URL.

    # For example, if you create an encrypted DB instance in the us-west-1 AWS
    # Region, from a source DB instance in the us-east-2 AWS Region, then you
    # call the `CreateDBInstanceReadReplica` action in the us-east-1 AWS Region
    # and provide a presigned URL that contains a call to the
    # `CreateDBInstanceReadReplica` action in the us-west-2 AWS Region. For this
    # example, the `DestinationRegion` in the presigned URL must be set to the
    # us-east-1 AWS Region.

    #   * `KmsKeyId` \- The AWS KMS key identifier for the key to use to encrypt the Read Replica in the destination AWS Region. This is the same identifier for both the `CreateDBInstanceReadReplica` action that is called in the destination AWS Region, and the action contained in the presigned URL.

    #   * `SourceDBInstanceIdentifier` \- The DB instance identifier for the encrypted DB instance to be replicated. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are creating an encrypted Read Replica from a DB instance in the us-west-2 AWS Region, then your `SourceDBInstanceIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:instance:mysql-instance1-20161115`.

    # To learn how to generate a Signature Version 4 signed request, see
    # [Authenticating Requests: Using Query Parameters (AWS Signature Version
    # 4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-
    # auth.html) and [Signature Version 4 Signing
    # Process](http://docs.aws.amazon.com/general/latest/gr/signature-
    # version-4.html).
    pre_signed_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # You can enable IAM database authentication for the following database
    # engines

    #   * For MySQL 5.6, minor version 5.6.34 or higher

    #   * For MySQL 5.7, minor version 5.7.16 or higher

    #   * Aurora 5.6 or higher.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True to enable Performance Insights for the read replica, and otherwise
    # false.

    # For more information, see [Using Amazon Performance
    # Insights](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
    # in the _Amazon RDS User Guide_.
    enable_performance_insights: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in days, to retain Performance Insights data. Valid
    # values are 7 or 731 (2 years).
    performance_insights_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of logs that the new DB instance is to export to CloudWatch Logs.
    # The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch Logs
    # ](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon RDS User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies that the DB instance class of the DB instance uses
    # its default processor features.
    use_default_processor_features: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the region that contains the source for the read replica.
    source_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBInstanceReadReplicaResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
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

    # The name of the DB parameter group.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # This value is stored as a lowercase string.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB parameter group family name. A DB parameter group can be associated
    # with one and only one DB parameter group family, and can be applied only to
    # a DB instance running a database engine and engine version compatible with
    # that DB parameter group family.

    # To list all of the available parameter group families, use the following
    # command:

    # `aws rds describe-db-engine-versions --query
    # "DBEngineVersions[].DBParameterGroupFamily"`

    # The output contains duplicates.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for the DB parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBParameterGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_parameter_group",
                "DBParameterGroup",
                TypeInfo(DBParameterGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB parameter group.

    # This data type is used as a response element in the
    # DescribeDBParameterGroups action.
    db_parameter_group: "DBParameterGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDBSecurityGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "db_security_group_description",
                "DBSecurityGroupDescription",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the DB security group. This value is stored as a lowercase
    # string.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    #   * Must not be "Default"

    # Example: `mysecuritygroup`
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the DB security group.
    db_security_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBSecurityGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_security_group",
                "DBSecurityGroup",
                TypeInfo(DBSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details for an Amazon RDS DB security group.

    # This data type is used as a response element in the
    # DescribeDBSecurityGroups action.
    db_security_group: "DBSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDBSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The identifier for the DB snapshot.

    # Constraints:

    #   * Cannot be null, empty, or blank

    #   * Must contain from 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-snapshot-id`
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the DB instance that you want to create the snapshot of.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_snapshot",
                "DBSnapshot",
                TypeInfo(DBSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB snapshot.

    # This data type is used as a response element in the DescribeDBSnapshots
    # action.
    db_snapshot: "DBSnapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "db_subnet_group_description",
                "DBSubnetGroupDescription",
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

    # The name for the DB subnet group. This value is stored as a lowercase
    # string.

    # Constraints: Must contain no more than 255 letters, numbers, periods,
    # underscores, spaces, or hyphens. Must not be default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the DB subnet group.
    db_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 Subnet IDs for the DB subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDBSubnetGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_subnet_group",
                "DBSubnetGroup",
                TypeInfo(DBSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB subnet group.

    # This data type is used as a response element in the DescribeDBSubnetGroups
    # action.
    db_subnet_group: "DBSubnetGroup" = dataclasses.field(
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
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "source_ids",
                "SourceIds",
                TypeInfo(typing.List[str]),
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

    # The name of the subscription.

    # Constraints: The name must be less than 255 characters.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SNS topic created for event
    # notification. The ARN is created by Amazon SNS when you create a topic and
    # subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of source that is generating the events. For example, if you want
    # to be notified of events generated by a DB instance, you would set this
    # parameter to db-instance. if this value is not specified, all events are
    # returned.

    # Valid values: `db-instance` | `db-cluster` | `db-parameter-group` | `db-
    # security-group` | `db-snapshot` | `db-cluster-snapshot`
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories for a SourceType that you want to subscribe to.
    # You can see a list of the categories for a given SourceType in the
    # [Events](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
    # topic in the _Amazon RDS User Guide_ or by using the
    # **DescribeEventCategories** action.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of identifiers of the event sources for which events are returned.
    # If not specified, then all sources are included in the response. An
    # identifier must begin with a letter and must contain only ASCII letters,
    # digits, and hyphens; it can't end with a hyphen or contain two consecutive
    # hyphens.

    # Constraints:

    #   * If SourceIds are supplied, SourceType must also be provided.

    #   * If the source type is a DB instance, then a `DBInstanceIdentifier` must be supplied.

    #   * If the source type is a DB security group, a `DBSecurityGroupName` must be supplied.

    #   * If the source type is a DB parameter group, a `DBParameterGroupName` must be supplied.

    #   * If the source type is a DB snapshot, a `DBSnapshotIdentifier` must be supplied.
    source_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value; set to **true** to activate the subscription, set to
    # **false** to create the subscription but not active it.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
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

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateOptionGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "major_engine_version",
                "MajorEngineVersion",
                TypeInfo(str),
            ),
            (
                "option_group_description",
                "OptionGroupDescription",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Specifies the name of the option group to be created.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `myoptiongroup`
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the engine that this option group should be
    # associated with.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the major version of the engine that this option group should be
    # associated with.
    major_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the option group.
    option_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateOptionGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "option_group",
                "OptionGroup",
                TypeInfo(OptionGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    option_group: "OptionGroup" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBCluster(ShapeBase):
    """
    Contains the details of an Amazon RDS DB cluster.

    This data type is used as a response element in the DescribeDBClusters action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group",
                "DBClusterParameterGroup",
                TypeInfo(str),
            ),
            (
                "db_subnet_group",
                "DBSubnetGroup",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "percent_progress",
                "PercentProgress",
                TypeInfo(str),
            ),
            (
                "earliest_restorable_time",
                "EarliestRestorableTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "reader_endpoint",
                "ReaderEndpoint",
                TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
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
                "latest_restorable_time",
                "LatestRestorableTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "master_username",
                "MasterUsername",
                TypeInfo(str),
            ),
            (
                "db_cluster_option_group_memberships",
                "DBClusterOptionGroupMemberships",
                TypeInfo(typing.List[DBClusterOptionGroupStatus]),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "replication_source_identifier",
                "ReplicationSourceIdentifier",
                TypeInfo(str),
            ),
            (
                "read_replica_identifiers",
                "ReadReplicaIdentifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "db_cluster_members",
                "DBClusterMembers",
                TypeInfo(typing.List[DBClusterMember]),
            ),
            (
                "vpc_security_groups",
                "VpcSecurityGroups",
                TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
            (
                "hosted_zone_id",
                "HostedZoneId",
                TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "db_cluster_resource_id",
                "DbClusterResourceId",
                TypeInfo(str),
            ),
            (
                "db_cluster_arn",
                "DBClusterArn",
                TypeInfo(str),
            ),
            (
                "associated_roles",
                "AssociatedRoles",
                TypeInfo(typing.List[DBClusterRole]),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                TypeInfo(bool),
            ),
            (
                "clone_group_id",
                "CloneGroupId",
                TypeInfo(str),
            ),
            (
                "cluster_create_time",
                "ClusterCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "earliest_backtrack_time",
                "EarliestBacktrackTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "backtrack_window",
                "BacktrackWindow",
                TypeInfo(int),
            ),
            (
                "backtrack_consumed_change_records",
                "BacktrackConsumedChangeRecords",
                TypeInfo(int),
            ),
            (
                "enabled_cloudwatch_logs_exports",
                "EnabledCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "capacity",
                "Capacity",
                TypeInfo(int),
            ),
            (
                "engine_mode",
                "EngineMode",
                TypeInfo(str),
            ),
            (
                "scaling_configuration_info",
                "ScalingConfigurationInfo",
                TypeInfo(ScalingConfigurationInfo),
            ),
        ]

    # For all database engines except Amazon Aurora, `AllocatedStorage` specifies
    # the allocated storage size in gibibytes (GiB). For Aurora,
    # `AllocatedStorage` always returns 1, because Aurora DB cluster storage size
    # is not fixed, but instead automatically adjusts as needed.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the list of EC2 Availability Zones that instances in the DB
    # cluster can be created in.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the number of days for which automatic DB snapshots are retained.
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, specifies the name of the character set that this cluster is
    # associated with.
    character_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the name of the initial database of this DB cluster that was
    # provided at create time, if one was specified when the DB cluster was
    # created. This same name is returned for the life of the DB cluster.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a user-supplied DB cluster identifier. This identifier is the
    # unique key that identifies a DB cluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the DB cluster parameter group for the DB cluster.
    db_cluster_parameter_group: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies information on the subnet group associated with the DB cluster,
    # including the name, description, and subnets in the subnet group.
    db_subnet_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the current state of this DB cluster.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the progress of the operation as a percentage.
    percent_progress: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The earliest time to which a database can be restored with point-in-time
    # restore.
    earliest_restorable_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the connection endpoint for the primary instance of the DB
    # cluster.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reader endpoint for the DB cluster. The reader endpoint for a DB
    # cluster load-balances connections across the Aurora Replicas that are
    # available in a DB cluster. As clients request new connections to the reader
    # endpoint, Aurora distributes the connection requests among the Aurora
    # Replicas in the DB cluster. This functionality can help balance your read
    # workload across multiple Aurora Replicas in your DB cluster.

    # If a failover occurs, and the Aurora Replica that you are connected to is
    # promoted to be the primary instance, your connection is dropped. To
    # continue sending your read workload to other Aurora Replicas in the
    # cluster, you can then reconnect to the reader endpoint.
    reader_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB cluster has instances in multiple Availability
    # Zones.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the name of the database engine to be used for this DB cluster.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the database engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the latest time to which a database can be restored with point-
    # in-time restore.
    latest_restorable_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the port that the database engine is listening on.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the master username for the DB cluster.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the list of option group memberships for this DB cluster.
    db_cluster_option_group_memberships: typing.List[
        "DBClusterOptionGroupStatus"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Specifies the daily time range during which automated backups are created
    # if automated backups are enabled, as determined by the
    # `BackupRetentionPeriod`.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which system maintenance can occur,
    # in Universal Coordinated Time (UTC).
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the identifier of the source DB cluster if this DB cluster is a
    # Read Replica.
    replication_source_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains one or more identifiers of the Read Replicas associated with this
    # DB cluster.
    read_replica_identifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the list of instances that make up the DB cluster.
    db_cluster_members: typing.List["DBClusterMember"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides a list of VPC security groups that the DB cluster belongs to.
    vpc_security_groups: typing.List["VpcSecurityGroupMembership"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Specifies the ID that Amazon Route 53 assigns when you create a hosted
    # zone.
    hosted_zone_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB cluster is encrypted.
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted
    # DB cluster.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region-unique, immutable identifier for the DB cluster. This
    # identifier is found in AWS CloudTrail log entries whenever the AWS KMS key
    # for the DB cluster is accessed.
    db_cluster_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB cluster.
    db_cluster_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides a list of the AWS Identity and Access Management (IAM) roles that
    # are associated with the DB cluster. IAM roles that are associated with a DB
    # cluster grant permission for the DB cluster to access other AWS services on
    # your behalf.
    associated_roles: typing.List["DBClusterRole"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if mapping of AWS Identity and Access Management (IAM) accounts to
    # database accounts is enabled, and otherwise false.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the clone group to which the DB cluster is associated.
    clone_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the time when the DB cluster was created, in Universal
    # Coordinated Time (UTC).
    cluster_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The earliest time to which a DB cluster can be backtracked.
    earliest_backtrack_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target backtrack window, in seconds. If this value is set to 0,
    # backtracking is disabled for the DB cluster. Otherwise, backtracking is
    # enabled.
    backtrack_window: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of change records stored for Backtrack.
    backtrack_consumed_change_records: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of log types that this DB cluster is configured to export to
    # CloudWatch Logs.

    # Log types vary by DB engine. For information about the log types for each
    # DB engine, see [Amazon RDS Database Log
    # Files](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html)
    # in the _Amazon Aurora User Guide._
    enabled_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB engine mode of the DB cluster, either `provisioned` or `serverless`.
    engine_mode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Shows the scaling configuration for an Aurora DB cluster in `serverless` DB
    # engine mode.

    # For more information, see [Using Amazon Aurora
    # Serverless](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-
    # serverless.html) in the _Amazon Aurora User Guide_.
    scaling_configuration_info: "ScalingConfigurationInfo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterAlreadyExistsFault(ShapeBase):
    """
    The user already has a DB cluster with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterBacktrack(OutputShapeBase):
    """
    This data type is used as a response element in the DescribeDBClusterBacktracks
    action.
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
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "backtrack_identifier",
                "BacktrackIdentifier",
                TypeInfo(str),
            ),
            (
                "backtrack_to",
                "BacktrackTo",
                TypeInfo(datetime.datetime),
            ),
            (
                "backtracked_from",
                "BacktrackedFrom",
                TypeInfo(datetime.datetime),
            ),
            (
                "backtrack_request_creation_time",
                "BacktrackRequestCreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains a user-supplied DB cluster identifier. This identifier is the
    # unique key that identifies a DB cluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the backtrack identifier.
    backtrack_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp of the time to which the DB cluster was backtracked.
    backtrack_to: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp of the time from which the DB cluster was backtracked.
    backtracked_from: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp of the time at which the backtrack was requested.
    backtrack_request_creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the backtrack. This property returns one of the following
    # values:

    #   * `applying` \- The backtrack is currently being applied to or rolled back from the DB cluster.

    #   * `completed` \- The backtrack has successfully been applied to or rolled back from the DB cluster.

    #   * `failed` \- An error occurred while the backtrack was applied to or rolled back from the DB cluster.

    #   * `pending` \- The backtrack is currently pending application to or rollback from the DB cluster.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterBacktrackMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeDBClusterBacktracks action.
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
                "db_cluster_backtracks",
                "DBClusterBacktracks",
                TypeInfo(typing.List[DBClusterBacktrack]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token that can be used in a subsequent
    # DescribeDBClusterBacktracks request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of backtracks for the user.
    db_cluster_backtracks: typing.List["DBClusterBacktrack"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class DBClusterBacktrackNotFoundFault(ShapeBase):
    """
    _BacktrackIdentifier_ doesn't refer to an existing backtrack.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterCapacityInfo(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "pending_capacity",
                "PendingCapacity",
                TypeInfo(int),
            ),
            (
                "current_capacity",
                "CurrentCapacity",
                TypeInfo(int),
            ),
            (
                "seconds_before_timeout",
                "SecondsBeforeTimeout",
                TypeInfo(int),
            ),
            (
                "timeout_action",
                "TimeoutAction",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A user-supplied DB cluster identifier. This identifier is the unique key
    # that identifies a DB cluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that specifies the capacity that the DB cluster scales to next.
    pending_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current capacity of the DB cluster.
    current_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of seconds before a call to `ModifyCurrentDBClusterCapacity`
    # times out.
    seconds_before_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timeout action of a call to `ModifyCurrentDBClusterCapacity`, either
    # `ForceApplyCapacityChange` or `RollbackCapacityChange`.
    timeout_action: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterMember(ShapeBase):
    """
    Contains information about an instance that is part of a DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "is_cluster_writer",
                "IsClusterWriter",
                TypeInfo(bool),
            ),
            (
                "db_cluster_parameter_group_status",
                "DBClusterParameterGroupStatus",
                TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                TypeInfo(int),
            ),
        ]

    # Specifies the instance identifier for this member of the DB cluster.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value that is `true` if the cluster member is the primary instance for the
    # DB cluster and `false` otherwise.
    is_cluster_writer: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of the DB cluster parameter group for this member of
    # the DB cluster.
    db_cluster_parameter_group_status: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies the order in which an Aurora Replica is promoted to
    # the primary instance after a failure of the existing primary instance. For
    # more information, see [ Fault Tolerance for an Aurora DB
    # Cluster](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance)
    # in the _Amazon Aurora User Guide_.
    promotion_tier: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBClusters action.
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
                "db_clusters",
                "DBClusters",
                TypeInfo(typing.List[DBCluster]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token that can be used in a subsequent DescribeDBClusters
    # request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of DB clusters for the user.
    db_clusters: typing.List["DBCluster"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["DBClusterMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBClusterNotFoundFault(ShapeBase):
    """
    _DBClusterIdentifier_ doesn't refer to an existing DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterOptionGroupStatus(ShapeBase):
    """
    Contains status information for a DB cluster option group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_option_group_name",
                "DBClusterOptionGroupName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # Specifies the name of the DB cluster option group.
    db_cluster_option_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the DB cluster option group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterParameterGroup(ShapeBase):
    """
    Contains the details of an Amazon RDS DB cluster parameter group.

    This data type is used as a response element in the
    DescribeDBClusterParameterGroups action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group_arn",
                "DBClusterParameterGroupArn",
                TypeInfo(str),
            ),
        ]

    # Provides the name of the DB cluster parameter group.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the name of the DB parameter group family that this DB cluster
    # parameter group is compatible with.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the customer-specified description for this DB cluster parameter
    # group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB cluster parameter group.
    db_cluster_parameter_group_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterParameterGroupDetails(OutputShapeBase):
    """
    Provides details about a DB cluster parameter group including the parameters in
    the DB cluster parameter group.
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

    # Provides a list of parameters for the DB cluster parameter group.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous
    # DescribeDBClusterParameters request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterParameterGroupNameMessage(OutputShapeBase):
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
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the DB cluster parameter group.

    # Constraints:

    #   * Must be 1 to 255 letters or numbers.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # This value is stored as a lowercase string.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterParameterGroupNotFoundFault(ShapeBase):
    """
    _DBClusterParameterGroupName_ doesn't refer to an existing DB cluster parameter
    group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterParameterGroupsMessage(OutputShapeBase):
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
                "db_cluster_parameter_groups",
                "DBClusterParameterGroups",
                TypeInfo(typing.List[DBClusterParameterGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterParameterGroups` request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DB cluster parameter groups.
    db_cluster_parameter_groups: typing.List["DBClusterParameterGroup"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class DBClusterQuotaExceededFault(ShapeBase):
    """
    The user attempted to create a new DB cluster and the user has already reached
    the maximum allowed DB cluster quota.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterRole(ShapeBase):
    """
    Describes an AWS Identity and Access Management (IAM) role that is associated
    with a DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "feature_name",
                "FeatureName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the IAM role that is associated with the
    # DB cluster.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the state of association between the IAM role and the DB cluster.
    # The Status property returns one of the following values:

    #   * `ACTIVE` \- the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.

    #   * `PENDING` \- the IAM role ARN is being associated with the DB cluster.

    #   * `INVALID` \- the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    feature_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBClusterRoleAlreadyExistsFault(ShapeBase):
    """
    The specified IAM role Amazon Resource Name (ARN) is already associated with the
    specified DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterRoleNotFoundFault(ShapeBase):
    """
    The specified IAM role Amazon Resource Name (ARN) isn't associated with the
    specified DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterRoleQuotaExceededFault(ShapeBase):
    """
    You have exceeded the maximum number of IAM roles that can be associated with
    the specified DB cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterSnapshot(ShapeBase):
    """
    Contains the details for an Amazon RDS DB cluster snapshot

    This data type is used as a response element in the DescribeDBClusterSnapshots
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_create_time",
                "SnapshotCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
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
                "vpc_id",
                "VpcId",
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
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                TypeInfo(str),
            ),
            (
                "percent_progress",
                "PercentProgress",
                TypeInfo(int),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "db_cluster_snapshot_arn",
                "DBClusterSnapshotArn",
                TypeInfo(str),
            ),
            (
                "source_db_cluster_snapshot_arn",
                "SourceDBClusterSnapshotArn",
                TypeInfo(str),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                TypeInfo(bool),
            ),
        ]

    # Provides the list of EC2 Availability Zones that instances in the DB
    # cluster snapshot can be restored in.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the identifier for the DB cluster snapshot.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the DB cluster identifier of the DB cluster that this DB cluster
    # snapshot was created from.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the time when the snapshot was taken, in Universal Coordinated
    # Time (UTC).
    snapshot_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the database engine.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the allocated storage size in gibibytes (GiB).
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of this DB cluster snapshot.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the port that the DB cluster was listening on at the time of the
    # snapshot.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the VPC ID associated with the DB cluster snapshot.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the time when the DB cluster was created, in Universal
    # Coordinated Time (UTC).
    cluster_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the master username for the DB cluster snapshot.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the version of the database engine for this DB cluster snapshot.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the license model information for this DB cluster snapshot.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the type of the DB cluster snapshot.
    snapshot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the percentage of the estimated data that has been transferred.
    percent_progress: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB cluster snapshot is encrypted.
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted
    # DB cluster snapshot.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB cluster snapshot.
    db_cluster_snapshot_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the DB cluster snapshot was copied from a source DB cluster snapshot,
    # the Amazon Resource Name (ARN) for the source DB cluster snapshot,
    # otherwise, a null value.
    source_db_cluster_snapshot_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if mapping of AWS Identity and Access Management (IAM) accounts to
    # database accounts is enabled, and otherwise false.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterSnapshotAlreadyExistsFault(ShapeBase):
    """
    The user already has a DB cluster snapshot with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBClusterSnapshotAttribute(ShapeBase):
    """
    Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts
    to restore a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_values",
                "AttributeValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the manual DB cluster snapshot attribute.

    # The attribute named `restore` refers to the list of AWS accounts that have
    # permission to copy or restore the manual DB cluster snapshot. For more
    # information, see the ModifyDBClusterSnapshotAttribute API action.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value(s) for the manual DB cluster snapshot attribute.

    # If the `AttributeName` field is set to `restore`, then this element returns
    # a list of IDs of the AWS accounts that are authorized to copy or restore
    # the manual DB cluster snapshot. If a value of `all` is in the list, then
    # the manual DB cluster snapshot is public and available for any AWS account
    # to copy or restore.
    attribute_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBClusterSnapshotAttributesResult(ShapeBase):
    """
    Contains the results of a successful call to the
    DescribeDBClusterSnapshotAttributes API action.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts
    to copy or restore a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_cluster_snapshot_attributes",
                "DBClusterSnapshotAttributes",
                TypeInfo(typing.List[DBClusterSnapshotAttribute]),
            ),
        ]

    # The identifier of the manual DB cluster snapshot that the attributes apply
    # to.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of attributes and values for the manual DB cluster snapshot.
    db_cluster_snapshot_attributes: typing.List["DBClusterSnapshotAttribute"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )


@dataclasses.dataclass
class DBClusterSnapshotMessage(OutputShapeBase):
    """
    Provides a list of DB cluster snapshots for the user as the result of a call to
    the DescribeDBClusterSnapshots action.
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
                "db_cluster_snapshots",
                "DBClusterSnapshots",
                TypeInfo(typing.List[DBClusterSnapshot]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous
    # DescribeDBClusterSnapshots request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides a list of DB cluster snapshots for the user.
    db_cluster_snapshots: typing.List["DBClusterSnapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DBClusterSnapshotMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBClusterSnapshotNotFoundFault(ShapeBase):
    """
    _DBClusterSnapshotIdentifier_ doesn't refer to an existing DB cluster snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBEngineVersion(ShapeBase):
    """
    This data type is used as a response element in the action
    DescribeDBEngineVersions.
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
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "db_engine_description",
                "DBEngineDescription",
                TypeInfo(str),
            ),
            (
                "db_engine_version_description",
                "DBEngineVersionDescription",
                TypeInfo(str),
            ),
            (
                "default_character_set",
                "DefaultCharacterSet",
                TypeInfo(CharacterSet),
            ),
            (
                "supported_character_sets",
                "SupportedCharacterSets",
                TypeInfo(typing.List[CharacterSet]),
            ),
            (
                "valid_upgrade_target",
                "ValidUpgradeTarget",
                TypeInfo(typing.List[UpgradeTarget]),
            ),
            (
                "supported_timezones",
                "SupportedTimezones",
                TypeInfo(typing.List[Timezone]),
            ),
            (
                "exportable_log_types",
                "ExportableLogTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "supports_log_exports_to_cloudwatch_logs",
                "SupportsLogExportsToCloudwatchLogs",
                TypeInfo(bool),
            ),
            (
                "supports_read_replica",
                "SupportsReadReplica",
                TypeInfo(bool),
            ),
            (
                "supported_engine_modes",
                "SupportedEngineModes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the database engine.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the database engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the DB parameter group family for the database engine.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the database engine.
    db_engine_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the database engine version.
    db_engine_version_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default character set for new instances of this engine version, if the
    # `CharacterSetName` parameter of the CreateDBInstance API is not specified.
    default_character_set: "CharacterSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the character sets supported by this engine for the
    # `CharacterSetName` parameter of the `CreateDBInstance` action.
    supported_character_sets: typing.List["CharacterSet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of engine versions that this database engine version can be upgraded
    # to.
    valid_upgrade_target: typing.List["UpgradeTarget"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the time zones supported by this engine for the `Timezone`
    # parameter of the `CreateDBInstance` action.
    supported_timezones: typing.List["Timezone"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The types of logs that the database engine has available for export to
    # CloudWatch Logs.
    exportable_log_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates whether the engine version supports exporting the
    # log types specified by ExportableLogTypes to CloudWatch Logs.
    supports_log_exports_to_cloudwatch_logs: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the database engine version supports read replicas.
    supports_read_replica: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the supported DB engine modes.
    supported_engine_modes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBEngineVersionMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBEngineVersions
    action.
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
                "db_engine_versions",
                "DBEngineVersions",
                TypeInfo(typing.List[DBEngineVersion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `DBEngineVersion` elements.
    db_engine_versions: typing.List["DBEngineVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DBEngineVersionMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBInstance(ShapeBase):
    """
    Contains the details of an Amazon RDS DB instance.

    This data type is used as a response element in the DescribeDBInstances action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "db_instance_status",
                "DBInstanceStatus",
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
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
            ),
            (
                "instance_create_time",
                "InstanceCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "db_security_groups",
                "DBSecurityGroups",
                TypeInfo(typing.List[DBSecurityGroupMembership]),
            ),
            (
                "vpc_security_groups",
                "VpcSecurityGroups",
                TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
            (
                "db_parameter_groups",
                "DBParameterGroups",
                TypeInfo(typing.List[DBParameterGroupStatus]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "db_subnet_group",
                "DBSubnetGroup",
                TypeInfo(DBSubnetGroup),
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
                "latest_restorable_time",
                "LatestRestorableTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "multi_az",
                "MultiAZ",
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
                "read_replica_source_db_instance_identifier",
                "ReadReplicaSourceDBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "read_replica_db_instance_identifiers",
                "ReadReplicaDBInstanceIdentifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "read_replica_db_cluster_identifiers",
                "ReadReplicaDBClusterIdentifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_memberships",
                "OptionGroupMemberships",
                TypeInfo(typing.List[OptionGroupMembership]),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                TypeInfo(str),
            ),
            (
                "secondary_availability_zone",
                "SecondaryAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "status_infos",
                "StatusInfos",
                TypeInfo(typing.List[DBInstanceStatusInfo]),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                TypeInfo(str),
            ),
            (
                "db_instance_port",
                "DbInstancePort",
                TypeInfo(int),
            ),
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "dbi_resource_id",
                "DbiResourceId",
                TypeInfo(str),
            ),
            (
                "ca_certificate_identifier",
                "CACertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "domain_memberships",
                "DomainMemberships",
                TypeInfo(typing.List[DomainMembership]),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                TypeInfo(int),
            ),
            (
                "enhanced_monitoring_resource_arn",
                "EnhancedMonitoringResourceArn",
                TypeInfo(str),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                TypeInfo(int),
            ),
            (
                "db_instance_arn",
                "DBInstanceArn",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                TypeInfo(bool),
            ),
            (
                "performance_insights_enabled",
                "PerformanceInsightsEnabled",
                TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                TypeInfo(str),
            ),
            (
                "performance_insights_retention_period",
                "PerformanceInsightsRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "enabled_cloudwatch_logs_exports",
                "EnabledCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
        ]

    # Contains a user-supplied database identifier. This identifier is the unique
    # key that identifies a DB instance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the name of the compute and memory capacity class of the DB
    # instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the name of the database engine to be used for this DB instance.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the current state of this database.
    db_instance_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the master username for the DB instance.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The meaning of this parameter differs according to the database engine you
    # use. For example, this value returns MySQL, MariaDB, or PostgreSQL
    # information when returning values from CreateDBInstanceReadReplica since
    # Read Replicas are only supported for these engines.

    # **MySQL, MariaDB, SQL Server, PostgreSQL**

    # Contains the name of the initial database of this instance that was
    # provided at create time, if one was specified when the DB instance was
    # created. This same name is returned for the life of the DB instance.

    # Type: String

    # **Oracle**

    # Contains the Oracle System ID (SID) of the created DB instance. Not shown
    # when the returned parameters do not apply to an Oracle DB instance.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the connection endpoint.
    endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the allocated storage size specified in gibibytes.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the date and time the DB instance was created.
    instance_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the daily time range during which automated backups are created
    # if automated backups are enabled, as determined by the
    # `BackupRetentionPeriod`.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the number of days for which automatic DB snapshots are retained.
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides List of DB security group elements containing only
    # `DBSecurityGroup.Name` and `DBSecurityGroup.Status` subelements.
    db_security_groups: typing.List["DBSecurityGroupMembership"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Provides a list of VPC security group elements that the DB instance belongs
    # to.
    vpc_security_groups: typing.List["VpcSecurityGroupMembership"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Provides the list of DB parameter groups applied to this DB instance.
    db_parameter_groups: typing.List["DBParameterGroupStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Specifies the name of the Availability Zone the DB instance is located in.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies information on the subnet group associated with the DB instance,
    # including the name, description, and subnets in the subnet group.
    db_subnet_group: "DBSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the weekly time range during which system maintenance can occur,
    # in Universal Coordinated Time (UTC).
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies that changes to the DB instance are pending. This element is only
    # included when changes are pending. Specific changes are identified by
    # subelements.
    pending_modified_values: "PendingModifiedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the latest time to which a database can be restored with point-
    # in-time restore.
    latest_restorable_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies if the DB instance is a Multi-AZ deployment.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the database engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that minor version patches are applied automatically.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the identifier of the source DB instance if this DB instance is a
    # Read Replica.
    read_replica_source_db_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains one or more identifiers of the Read Replicas associated with this
    # DB instance.
    read_replica_db_instance_identifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains one or more identifiers of Aurora DB clusters to which the RDS DB
    # instance is replicated as a Read Replica. For example, when you create an
    # Aurora Read Replica of an RDS MySQL DB instance, the Aurora MySQL DB
    # cluster for the Aurora Read Replica is shown. This output does not contain
    # information about cross region Aurora Read Replicas.
    read_replica_db_cluster_identifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # License model information for this DB instance.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Provisioned IOPS (I/O operations per second) value.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the list of option group memberships for this DB instance.
    option_group_memberships: typing.List["OptionGroupMembership"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # If present, specifies the name of the character set that this instance is
    # associated with.
    character_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the name of the secondary Availability Zone for a DB
    # instance with multi-AZ support.
    secondary_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the accessibility options for the DB instance. A value of true
    # specifies an Internet-facing instance with a publicly resolvable DNS name,
    # which resolves to a public IP address. A value of false specifies an
    # internal instance with a DNS name that resolves to a private IP address.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a Read Replica. If the instance is not a Read Replica, this
    # is blank.
    status_infos: typing.List["DBInstanceStatusInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the storage type associated with DB instance.
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN from the key store with which the instance is associated for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the port that the DB instance listens on. If the DB instance is
    # part of a DB cluster, this can be a different port than the DB cluster
    # port.
    db_instance_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the DB instance is a member of a DB cluster, contains the name of the DB
    # cluster that the DB instance is a member of.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB instance is encrypted.
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted
    # DB instance.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region-unique, immutable identifier for the DB instance. This
    # identifier is found in AWS CloudTrail log entries whenever the AWS KMS key
    # for the DB instance is accessed.
    dbi_resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the CA certificate for this DB instance.
    ca_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Active Directory Domain membership records associated with the DB
    # instance.
    domain_memberships: typing.List["DomainMembership"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether tags are copied from the DB instance to snapshots of the
    # DB instance.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance.
    monitoring_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
    # that receives the Enhanced Monitoring metrics data for the DB instance.
    enhanced_monitoring_resource_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN for the IAM role that permits RDS to send Enhanced Monitoring
    # metrics to Amazon CloudWatch Logs.
    monitoring_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that specifies the order in which an Aurora Replica is promoted to
    # the primary instance after a failure of the existing primary instance. For
    # more information, see [ Fault Tolerance for an Aurora DB
    # Cluster](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance)
    # in the _Amazon Aurora User Guide_.
    promotion_tier: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB instance.
    db_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone of the DB instance. In most cases, the `Timezone` element is
    # empty. `Timezone` content appears only for Microsoft SQL Server DB
    # instances that were created with a time zone specified.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if mapping of AWS Identity and Access Management (IAM) accounts to
    # database accounts is enabled, and otherwise false.

    # IAM database authentication can be enabled for the following database
    # engines

    #   * For MySQL 5.6, minor version 5.6.34 or higher

    #   * For MySQL 5.7, minor version 5.7.16 or higher

    #   * Aurora 5.6 or higher. To enable IAM database authentication for Aurora, see DBCluster Type.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if Performance Insights is enabled for the DB instance, and otherwise
    # false.
    performance_insights_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in days, to retain Performance Insights data. Valid
    # values are 7 or 731 (2 years).
    performance_insights_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of log types that this DB instance is configured to export to
    # CloudWatch Logs.

    # Log types vary by DB engine. For information about the log types for each
    # DB engine, see [Amazon RDS Database Log
    # Files](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html)
    # in the _Amazon RDS User Guide._
    enabled_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBInstanceAlreadyExistsFault(ShapeBase):
    """
    The user already has a DB instance with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBInstanceMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBInstances
    action.
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
                "db_instances",
                "DBInstances",
                TypeInfo(typing.List[DBInstance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DBInstance instances.
    db_instances: typing.List["DBInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["DBInstanceMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBInstanceNotFoundFault(ShapeBase):
    """
    _DBInstanceIdentifier_ doesn't refer to an existing DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBInstanceStatusInfo(ShapeBase):
    """
    Provides a list of status information for a DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_type",
                "StatusType",
                TypeInfo(str),
            ),
            (
                "normal",
                "Normal",
                TypeInfo(bool),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # This value is currently "read replication."
    status_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Boolean value that is true if the instance is operating normally, or false
    # if the instance is in an error state.
    normal: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the DB instance. For a StatusType of read replica, the values can
    # be replicating, replication stop point set, replication stop point reached,
    # error, stopped, or terminated.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details of the error if there is an error for the instance. If the instance
    # is not in an error state, this value is blank.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBLogFileNotFoundFault(ShapeBase):
    """
    _LogFileName_ doesn't refer to an existing DB log file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroup(ShapeBase):
    """
    Contains the details of an Amazon RDS DB parameter group.

    This data type is used as a response element in the DescribeDBParameterGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_arn",
                "DBParameterGroupArn",
                TypeInfo(str),
            ),
        ]

    # Provides the name of the DB parameter group.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the name of the DB parameter group family that this DB parameter
    # group is compatible with.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the customer-specified description for this DB parameter group.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB parameter group.
    db_parameter_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBParameterGroupAlreadyExistsFault(ShapeBase):
    """
    A DB parameter group with the same name exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroupDetails(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBParameters
    action.
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

    # A list of Parameter values.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DBParameterGroupDetails", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBParameterGroupNameMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the ModifyDBParameterGroup or
    ResetDBParameterGroup action.
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
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the name of the DB parameter group.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBParameterGroupNotFoundFault(ShapeBase):
    """
    _DBParameterGroupName_ doesn't refer to an existing DB parameter group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroupQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of DB
    parameter groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBParameterGroupStatus(ShapeBase):
    """
    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

      * CreateDBInstance

      * CreateDBInstanceReadReplica

      * DeleteDBInstance

      * ModifyDBInstance

      * RebootDBInstance

      * RestoreDBInstanceFromDBSnapshot
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameter_apply_status",
                "ParameterApplyStatus",
                TypeInfo(str),
            ),
        ]

    # The name of the DP parameter group.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of parameter updates.
    parameter_apply_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBParameterGroupsMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBParameterGroups
    action.
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
                "db_parameter_groups",
                "DBParameterGroups",
                TypeInfo(typing.List[DBParameterGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DBParameterGroup instances.
    db_parameter_groups: typing.List["DBParameterGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DBParameterGroupsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBSecurityGroup(ShapeBase):
    """
    Contains the details for an Amazon RDS DB security group.

    This data type is used as a response element in the DescribeDBSecurityGroups
    action.
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
                "db_security_group_name",
                "DBSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "db_security_group_description",
                "DBSecurityGroupDescription",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
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
                "db_security_group_arn",
                "DBSecurityGroupArn",
                TypeInfo(str),
            ),
        ]

    # Provides the AWS ID of the owner of a specific DB security group.
    owner_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the DB security group.
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the description of the DB security group.
    db_security_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the VpcId of the DB security group.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of EC2SecurityGroup elements.
    ec2_security_groups: typing.List["EC2SecurityGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains a list of IPRange elements.
    ip_ranges: typing.List["IPRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the DB security group.
    db_security_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBSecurityGroupAlreadyExistsFault(ShapeBase):
    """
    A DB security group with the name specified in _DBSecurityGroupName_ already
    exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSecurityGroupMembership(ShapeBase):
    """
    This data type is used as a response element in the following actions:

      * ModifyDBInstance

      * RebootDBInstance

      * RestoreDBInstanceFromDBSnapshot

      * RestoreDBInstanceToPointInTime
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The name of the DB security group.
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the DB security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBSecurityGroupMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBSecurityGroups
    action.
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
                "db_security_groups",
                "DBSecurityGroups",
                TypeInfo(typing.List[DBSecurityGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DBSecurityGroup instances.
    db_security_groups: typing.List["DBSecurityGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DBSecurityGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBSecurityGroupNotFoundFault(ShapeBase):
    """
    _DBSecurityGroupName_ doesn't refer to an existing DB security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSecurityGroupNotSupportedFault(ShapeBase):
    """
    A DB security group isn't allowed for this action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSecurityGroupQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of DB security
    groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSnapshot(ShapeBase):
    """
    Contains the details of an Amazon RDS DB snapshot.

    This data type is used as a response element in the DescribeDBSnapshots action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_create_time",
                "SnapshotCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
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
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "instance_create_time",
                "InstanceCreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "master_username",
                "MasterUsername",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "percent_progress",
                "PercentProgress",
                TypeInfo(int),
            ),
            (
                "source_region",
                "SourceRegion",
                TypeInfo(str),
            ),
            (
                "source_db_snapshot_identifier",
                "SourceDBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
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
                "db_snapshot_arn",
                "DBSnapshotArn",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "iam_database_authentication_enabled",
                "IAMDatabaseAuthenticationEnabled",
                TypeInfo(bool),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
        ]

    # Specifies the identifier for the DB snapshot.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the DB instance identifier of the DB instance this DB snapshot
    # was created from.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the time when the snapshot was taken, in Universal Coordinated
    # Time (UTC).
    snapshot_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the name of the database engine.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the allocated storage size in gibibytes (GiB).
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the status of this DB snapshot.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the port that the database engine was listening on at the time of
    # the snapshot.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the Availability Zone the DB instance was located in
    # at the time of the DB snapshot.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the VPC ID associated with the DB snapshot.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the time when the snapshot was taken, in Universal Coordinated
    # Time (UTC).
    instance_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the master username for the DB snapshot.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the database engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # License model information for the restored DB instance.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the type of the DB snapshot.
    snapshot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Provisioned IOPS (I/O operations per second) value of the DB
    # instance at the time of the snapshot.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the option group name for the DB snapshot.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The percentage of the estimated data that has been transferred.
    percent_progress: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region that the DB snapshot was created in or copied from.
    source_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB snapshot Amazon Resource Name (ARN) that the DB snapshot was copied
    # from. It only has value in case of cross-customer or cross-region copy.
    source_db_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the storage type associated with DB snapshot.
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB snapshot is encrypted.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `Encrypted` is true, the AWS KMS key identifier for the encrypted DB
    # snapshot.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the DB snapshot.
    db_snapshot_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone of the DB snapshot. In most cases, the `Timezone` element is
    # empty. `Timezone` content appears only for snapshots taken from Microsoft
    # SQL Server DB instances that were created with a time zone specified.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if mapping of AWS Identity and Access Management (IAM) accounts to
    # database accounts is enabled, and otherwise false.
    iam_database_authentication_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance when the DB snapshot was created.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBSnapshotAlreadyExistsFault(ShapeBase):
    """
    _DBSnapshotIdentifier_ is already used by an existing snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSnapshotAttribute(ShapeBase):
    """
    Contains the name and values of a manual DB snapshot attribute

    Manual DB snapshot attributes are used to authorize other AWS accounts to
    restore a manual DB snapshot. For more information, see the
    ModifyDBSnapshotAttribute API.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_values",
                "AttributeValues",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the manual DB snapshot attribute.

    # The attribute named `restore` refers to the list of AWS accounts that have
    # permission to copy or restore the manual DB cluster snapshot. For more
    # information, see the ModifyDBSnapshotAttribute API action.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value or values for the manual DB snapshot attribute.

    # If the `AttributeName` field is set to `restore`, then this element returns
    # a list of IDs of the AWS accounts that are authorized to copy or restore
    # the manual DB snapshot. If a value of `all` is in the list, then the manual
    # DB snapshot is public and available for any AWS account to copy or restore.
    attribute_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DBSnapshotAttributesResult(ShapeBase):
    """
    Contains the results of a successful call to the DescribeDBSnapshotAttributes
    API action.

    Manual DB snapshot attributes are used to authorize other AWS accounts to copy
    or restore a manual DB snapshot. For more information, see the
    ModifyDBSnapshotAttribute API action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_snapshot_attributes",
                "DBSnapshotAttributes",
                TypeInfo(typing.List[DBSnapshotAttribute]),
            ),
        ]

    # The identifier of the manual DB snapshot that the attributes apply to.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of attributes and values for the manual DB snapshot.
    db_snapshot_attributes: typing.List["DBSnapshotAttribute"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class DBSnapshotMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBSnapshots
    action.
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
                "db_snapshots",
                "DBSnapshots",
                TypeInfo(typing.List[DBSnapshot]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DBSnapshot instances.
    db_snapshots: typing.List["DBSnapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["DBSnapshotMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBSnapshotNotFoundFault(ShapeBase):
    """
    _DBSnapshotIdentifier_ doesn't refer to an existing DB snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroup(ShapeBase):
    """
    Contains the details of an Amazon RDS DB subnet group.

    This data type is used as a response element in the DescribeDBSubnetGroups
    action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "db_subnet_group_description",
                "DBSubnetGroupDescription",
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
                "db_subnet_group_arn",
                "DBSubnetGroupArn",
                TypeInfo(str),
            ),
        ]

    # The name of the DB subnet group.
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the description of the DB subnet group.
    db_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the VpcId of the DB subnet group.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the status of the DB subnet group.
    subnet_group_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of Subnet elements.
    subnets: typing.List["Subnet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the DB subnet group.
    db_subnet_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DBSubnetGroupAlreadyExistsFault(ShapeBase):
    """
    _DBSubnetGroupName_ is already used by an existing DB subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupDoesNotCoverEnoughAZs(ShapeBase):
    """
    Subnets in the DB subnet group should cover at least two Availability Zones
    unless there is only one Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeDBSubnetGroups
    action.
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
                "db_subnet_groups",
                "DBSubnetGroups",
                TypeInfo(typing.List[DBSubnetGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DBSubnetGroup instances.
    db_subnet_groups: typing.List["DBSubnetGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DBSubnetGroupMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DBSubnetGroupNotAllowedFault(ShapeBase):
    """
    The DBSubnetGroup shouldn't be specified while creating read replicas that lie
    in the same region as the source instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupNotFoundFault(ShapeBase):
    """
    _DBSubnetGroupName_ doesn't refer to an existing DB subnet group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetGroupQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of DB subnet
    groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBSubnetQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of subnets in
    a DB subnet groups.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DBUpgradeDependencyFailureFault(ShapeBase):
    """
    The DB upgrade failed because a resource the DB depends on can't be modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteDBClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "skip_final_snapshot",
                "SkipFinalSnapshot",
                TypeInfo(bool),
            ),
            (
                "final_db_snapshot_identifier",
                "FinalDBSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The DB cluster identifier for the DB cluster to be deleted. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * Must match an existing DBClusterIdentifier.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines whether a final DB cluster snapshot is created before the DB
    # cluster is deleted. If `true` is specified, no DB cluster snapshot is
    # created. If `false` is specified, a DB cluster snapshot is created before
    # the DB cluster is deleted.

    # You must specify a `FinalDBSnapshotIdentifier` parameter if
    # `SkipFinalSnapshot` is `false`.

    # Default: `false`
    skip_final_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB cluster snapshot identifier of the new DB cluster snapshot created
    # when `SkipFinalSnapshot` is set to `false`.

    # Specifying this parameter and also setting the `SkipFinalShapshot`
    # parameter to true results in an error.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    final_db_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the DB cluster parameter group.

    # Constraints:

    #   * Must be the name of an existing DB cluster parameter group.

    #   * You can't delete a default DB cluster parameter group.

    #   * Cannot be associated with any DB clusters.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDBClusterSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the DB cluster snapshot to delete.

    # Constraints: Must be the name of an existing DB cluster snapshot in the
    # `available` state.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBClusterSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_snapshot",
                "DBClusterSnapshot",
                TypeInfo(DBClusterSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details for an Amazon RDS DB cluster snapshot

    # This data type is used as a response element in the
    # DescribeDBClusterSnapshots action.
    db_cluster_snapshot: "DBClusterSnapshot" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "skip_final_snapshot",
                "SkipFinalSnapshot",
                TypeInfo(bool),
            ),
            (
                "final_db_snapshot_identifier",
                "FinalDBSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The DB instance identifier for the DB instance to be deleted. This
    # parameter isn't case-sensitive.

    # Constraints:

    #   * Must match the name of an existing DB instance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines whether a final DB snapshot is created before the DB instance is
    # deleted. If `true` is specified, no DBSnapshot is created. If `false` is
    # specified, a DB snapshot is created before the DB instance is deleted.

    # Note that when a DB instance is in a failure state and has a status of
    # 'failed', 'incompatible-restore', or 'incompatible-network', it can only be
    # deleted when the SkipFinalSnapshot parameter is set to "true".

    # Specify `true` when deleting a Read Replica.

    # The FinalDBSnapshotIdentifier parameter must be specified if
    # SkipFinalSnapshot is `false`.

    # Default: `false`
    skip_final_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DBSnapshotIdentifier of the new DBSnapshot created when
    # SkipFinalSnapshot is set to `false`.

    # Specifying this parameter and also setting the SkipFinalShapshot parameter
    # to true results in an error.

    # Constraints:

    #   * Must be 1 to 255 letters or numbers.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    #   * Cannot be specified when deleting a Read Replica.
    final_db_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDBParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the DB parameter group.

    # Constraints:

    #   * Must be the name of an existing DB parameter group

    #   * You can't delete a default DB parameter group

    #   * Cannot be associated with any DB instances
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDBSecurityGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the DB security group to delete.

    # You can't delete the default DB security group.

    # Constraints:

    #   * Must be 1 to 255 letters, numbers, or hyphens.

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    #   * Must not be "Default"
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDBSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The DBSnapshot identifier.

    # Constraints: Must be the name of an existing DB snapshot in the `available`
    # state.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDBSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_snapshot",
                "DBSnapshot",
                TypeInfo(DBSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB snapshot.

    # This data type is used as a response element in the DescribeDBSnapshots
    # action.
    db_snapshot: "DBSnapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDBSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the database subnet group to delete.

    # You can't delete the default subnet group.

    # Constraints:

    # Constraints: Must match the name of an existing DBSubnetGroup. Must not be
    # default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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

    # The name of the RDS event notification subscription you want to delete.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEventSubscriptionResult(OutputShapeBase):
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

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteOptionGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
        ]

    # The name of the option group to be deleted.

    # You can't delete default option groups.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAccountAttributesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeCertificatesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_identifier",
                "CertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The user-supplied certificate identifier. If this parameter is specified,
    # information for only the identified certificate is returned. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * Must match an existing CertificateIdentifier.
    certificate_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeCertificates
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClusterBacktracksMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "backtrack_identifier",
                "BacktrackIdentifier",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The DB cluster identifier of the DB cluster to be described. This parameter
    # is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If specified, this value is the backtrack identifier of the backtrack to be
    # described.

    # Constraints:

    #   * Must contain a valid universally unique identifier (UUID). For more information about UUIDs, see [A Universally Unique Identifier (UUID) URN Namespace](http://www.ietf.org/rfc/rfc4122.txt).

    # Example: `123e4567-e89b-12d3-a456-426655440000`
    backtrack_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that specifies one or more DB clusters to describe. Supported
    # filters include the following:

    #   * `db-cluster-backtrack-id` \- Accepts backtrack identifiers. The results list includes information about only the backtracks identified by these identifiers.

    #   * `db-cluster-backtrack-status` \- Accepts any of the following backtrack status values:

    #     * `applying`

    #     * `completed`

    #     * `failed`

    #     * `pending`

    # The results list includes information about only the backtracks identified
    # by these values. For more information about backtrack status values, see
    # DBClusterBacktrack.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # DescribeDBClusterBacktracks request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClusterParameterGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of a specific DB cluster parameter group to return details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterParameterGroups` request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClusterParametersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of a specific DB cluster parameter group to return parameter
    # details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates to return only parameters for a specific source.
    # Parameter sources can be `engine`, `service`, or `customer`.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterParameters` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClusterSnapshotAttributesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier for the DB cluster snapshot to describe the attributes for.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBClusterSnapshotAttributesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_snapshot_attributes_result",
                "DBClusterSnapshotAttributesResult",
                TypeInfo(DBClusterSnapshotAttributesResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the results of a successful call to the
    # DescribeDBClusterSnapshotAttributes API action.

    # Manual DB cluster snapshot attributes are used to authorize other AWS
    # accounts to copy or restore a manual DB cluster snapshot. For more
    # information, see the ModifyDBClusterSnapshotAttribute API action.
    db_cluster_snapshot_attributes_result: "DBClusterSnapshotAttributesResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBClusterSnapshotsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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
                "include_shared",
                "IncludeShared",
                TypeInfo(bool),
            ),
            (
                "include_public",
                "IncludePublic",
                TypeInfo(bool),
            ),
        ]

    # The ID of the DB cluster to retrieve the list of DB cluster snapshots for.
    # This parameter can't be used in conjunction with the
    # `DBClusterSnapshotIdentifier` parameter. This parameter is not case-
    # sensitive.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBCluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A specific DB cluster snapshot identifier to describe. This parameter can't
    # be used in conjunction with the `DBClusterIdentifier` parameter. This value
    # is stored as a lowercase string.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBClusterSnapshot.

    #   * If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of DB cluster snapshots to be returned. You can specify one of the
    # following values:

    #   * `automated` \- Return all DB cluster snapshots that have been automatically taken by Amazon RDS for my AWS account.

    #   * `manual` \- Return all DB cluster snapshots that have been taken by my AWS account.

    #   * `shared` \- Return all manual DB cluster snapshots that have been shared to my AWS account.

    #   * `public` \- Return all DB cluster snapshots that have been marked as public.

    # If you don't specify a `SnapshotType` value, then both automated and manual
    # DB cluster snapshots are returned. You can include shared DB cluster
    # snapshots with these results by setting the `IncludeShared` parameter to
    # `true`. You can include public DB cluster snapshots with these results by
    # setting the `IncludePublic` parameter to `true`.

    # The `IncludeShared` and `IncludePublic` parameters don't apply for
    # `SnapshotType` values of `manual` or `automated`. The `IncludePublic`
    # parameter doesn't apply when `SnapshotType` is set to `shared`. The
    # `IncludeShared` parameter doesn't apply when `SnapshotType` is set to
    # `public`.
    snapshot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBClusterSnapshots` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to include shared manual DB cluster snapshots from other AWS accounts
    # that this AWS account has been given permission to copy or restore, and
    # otherwise false. The default is `false`.

    # You can give an AWS account permission to restore a manual DB cluster
    # snapshot from another AWS account by the ModifyDBClusterSnapshotAttribute
    # API action.
    include_shared: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to include manual DB cluster snapshots that are public and can be
    # copied or restored by any AWS account, and otherwise false. The default is
    # `false`. The default is false.

    # You can share a manual DB cluster snapshot as public by using the
    # ModifyDBClusterSnapshotAttribute API action.
    include_public: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBClustersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The user-supplied DB cluster identifier. If this parameter is specified,
    # information from only the specific DB cluster is returned. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * If supplied, must match an existing DBClusterIdentifier.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that specifies one or more DB clusters to describe.

    # Supported filters:

    #   * `db-cluster-id` \- Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeDBClusters
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBEngineVersionsMessage(ShapeBase):
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
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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
            (
                "list_supported_character_sets",
                "ListSupportedCharacterSets",
                TypeInfo(bool),
            ),
            (
                "list_supported_timezones",
                "ListSupportedTimezones",
                TypeInfo(bool),
            ),
        ]

    # The database engine to return.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database engine version to return.

    # Example: `5.1.49`
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a specific DB parameter group family to return details for.

    # Constraints:

    #   * If supplied, must match an existing DBParameterGroupFamily.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more than the
    # `MaxRecords` value is available, a pagination token called a marker is
    # included in the response so that the following results can be retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that only the default version of the specified engine or engine
    # and major version combination is returned.
    default_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this parameter is specified and the requested engine supports the
    # `CharacterSetName` parameter for `CreateDBInstance`, the response includes
    # a list of supported character sets for each engine version.
    list_supported_character_sets: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If this parameter is specified and the requested engine supports the
    # `TimeZone` parameter for `CreateDBInstance`, the response includes a list
    # of supported time zones for each engine version.
    list_supported_timezones: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBInstancesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The user-supplied instance identifier. If this parameter is specified,
    # information from only the specific DB instance is returned. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that specifies one or more DB instances to describe.

    # Supported filters:

    #   * `db-cluster-id` \- Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.

    #   * `db-instance-id` \- Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include information about the DB instances identified by these ARNs.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous `DescribeDBInstances`
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBLogFilesDetails(ShapeBase):
    """
    This data type is used as a response element to DescribeDBLogFiles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_file_name",
                "LogFileName",
                TypeInfo(str),
            ),
            (
                "last_written",
                "LastWritten",
                TypeInfo(int),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
        ]

    # The name of the log file for the specified DB instance.
    log_file_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A POSIX timestamp when the last log entry was written.
    last_written: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of the log file for the specified DB instance.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBLogFilesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "filename_contains",
                "FilenameContains",
                TypeInfo(str),
            ),
            (
                "file_last_written",
                "FileLastWritten",
                TypeInfo(int),
            ),
            (
                "file_size",
                "FileSize",
                TypeInfo(int),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The customer-assigned name of the DB instance that contains the log files
    # you want to list.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the available log files for log file names that contain the
    # specified string.
    filename_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the available log files for files written since the specified date,
    # in POSIX timestamp format with milliseconds.
    file_last_written: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the available log files for files larger than the specified size.
    file_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified MaxRecords value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token provided in the previous request. If this parameter is
    # specified the response includes only records beyond the marker, up to
    # MaxRecords.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBLogFilesResponse(OutputShapeBase):
    """
    The response from a call to DescribeDBLogFiles.
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
                "describe_db_log_files",
                "DescribeDBLogFiles",
                TypeInfo(typing.List[DescribeDBLogFilesDetails]),
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

    # The DB log files returned.
    describe_db_log_files: typing.List["DescribeDBLogFilesDetails"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A pagination token that can be used in a subsequent DescribeDBLogFiles
    # request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeDBLogFilesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeDBParameterGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of a specific DB parameter group to return details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBParameterGroups` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBParametersMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of a specific DB parameter group to return details for.

    # Constraints:

    #   * If supplied, must match the name of an existing DBParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter types to return.

    # Default: All parameter types returned

    # Valid Values: `user | system | engine-default`
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous `DescribeDBParameters`
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBSecurityGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of the DB security group to return details for.
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeDBSecurityGroups` request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBSnapshotAttributesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier for the DB snapshot to describe the attributes for.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBSnapshotAttributesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_snapshot_attributes_result",
                "DBSnapshotAttributesResult",
                TypeInfo(DBSnapshotAttributesResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the results of a successful call to the
    # DescribeDBSnapshotAttributes API action.

    # Manual DB snapshot attributes are used to authorize other AWS accounts to
    # copy or restore a manual DB snapshot. For more information, see the
    # ModifyDBSnapshotAttribute API action.
    db_snapshot_attributes_result: "DBSnapshotAttributesResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeDBSnapshotsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_type",
                "SnapshotType",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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
                "include_shared",
                "IncludeShared",
                TypeInfo(bool),
            ),
            (
                "include_public",
                "IncludePublic",
                TypeInfo(bool),
            ),
        ]

    # The ID of the DB instance to retrieve the list of DB snapshots for. This
    # parameter can't be used in conjunction with `DBSnapshotIdentifier`. This
    # parameter is not case-sensitive.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A specific DB snapshot identifier to describe. This parameter can't be used
    # in conjunction with `DBInstanceIdentifier`. This value is stored as a
    # lowercase string.

    # Constraints:

    #   * If supplied, must match the identifier of an existing DBSnapshot.

    #   * If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of snapshots to be returned. You can specify one of the following
    # values:

    #   * `automated` \- Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account.

    #   * `manual` \- Return all DB snapshots that have been taken by my AWS account.

    #   * `shared` \- Return all manual DB snapshots that have been shared to my AWS account.

    #   * `public` \- Return all DB snapshots that have been marked as public.

    # If you don't specify a `SnapshotType` value, then both automated and manual
    # snapshots are returned. Shared and public DB snapshots are not included in
    # the returned results by default. You can include shared snapshots with
    # these results by setting the `IncludeShared` parameter to `true`. You can
    # include public snapshots with these results by setting the `IncludePublic`
    # parameter to `true`.

    # The `IncludeShared` and `IncludePublic` parameters don't apply for
    # `SnapshotType` values of `manual` or `automated`. The `IncludePublic`
    # parameter doesn't apply when `SnapshotType` is set to `shared`. The
    # `IncludeShared` parameter doesn't apply when `SnapshotType` is set to
    # `public`.
    snapshot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous `DescribeDBSnapshots`
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to include shared manual DB snapshots from other AWS accounts that
    # this AWS account has been given permission to copy or restore, and
    # otherwise false. The default is `false`.

    # You can give an AWS account permission to restore a manual DB snapshot from
    # another AWS account by using the ModifyDBSnapshotAttribute API action.
    include_shared: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to include manual DB snapshots that are public and can be copied or
    # restored by any AWS account, and otherwise false. The default is false.

    # You can share a manual DB snapshot as public by using the
    # ModifyDBSnapshotAttribute API.
    include_public: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDBSubnetGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of the DB subnet group to return details for.
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeDBSubnetGroups
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultClusterParametersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of the DB cluster parameter group family to return engine
    # parameter information for.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeEngineDefaultClusterParameters` request. If this parameter is
    # specified, the response includes only records beyond the marker, up to the
    # value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEngineDefaultClusterParametersResult(OutputShapeBase):
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

    # Contains the result of a successful invocation of the
    # DescribeEngineDefaultParameters action.
    engine_defaults: "EngineDefaults" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEngineDefaultParametersMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of the DB parameter group family.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # `DescribeEngineDefaultParameters` request. If this parameter is specified,
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

    # Contains the result of a successful invocation of the
    # DescribeEngineDefaultParameters action.
    engine_defaults: "EngineDefaults" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeEngineDefaultParametersResult", None, None]:
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
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
        ]

    # The type of source that is generating the events.

    # Valid values: db-instance | db-parameter-group | db-security-group | db-
    # snapshot
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of the RDS event notification subscription you want to describe.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # DescribeOrderableDBInstanceOptions request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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
    # specified, then all sources are included in the response.

    # Constraints:

    #   * If SourceIdentifier is supplied, SourceType must also be provided.

    #   * If the source type is `DBInstance`, then a `DBInstanceIdentifier` must be supplied.

    #   * If the source type is `DBSecurityGroup`, a `DBSecurityGroupName` must be supplied.

    #   * If the source type is `DBParameterGroup`, a `DBParameterGroupName` must be supplied.

    #   * If the source type is `DBSnapshot`, a `DBSnapshotIdentifier` must be supplied.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event source to retrieve events for. If no value is specified, all
    # events are returned.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The beginning of the time interval to retrieve events for, specified in ISO
    # 8601 format. For more information about ISO 8601, go to the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: 2009-07-08T18:00Z
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time interval for which to retrieve events, specified in ISO
    # 8601 format. For more information about ISO 8601, go to the [ISO8601
    # Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

    # Example: 2009-07-08T18:00Z
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes to retrieve events for.

    # Default: 60
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories that trigger notifications for a event
    # notification subscription.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeEvents request.
    # If this parameter is specified, the response includes only records beyond
    # the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOptionGroupOptionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "major_engine_version",
                "MajorEngineVersion",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # A required parameter. Options available for the given engine name are
    # described.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If specified, filters the results to include only options for the specified
    # major engine version.
    major_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOptionGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "major_engine_version",
                "MajorEngineVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the option group to describe. Cannot be supplied together with
    # EngineName or MajorEngineVersion.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous DescribeOptionGroups
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of option groups to only include groups associated with a
    # specific database engine.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the list of option groups to only include groups associated with a
    # specific database engine version. If specified, then EngineName must also
    # be specified.
    major_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOrderableDBInstanceOptionsMessage(ShapeBase):
    """

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
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "vpc",
                "Vpc",
                TypeInfo(bool),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The name of the engine to retrieve DB instance options for.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version filter value. Specify this parameter to show only the
    # available offerings matching the specified engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB instance class filter value. Specify this parameter to show only the
    # available offerings matching the specified DB instance class.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The license model filter value. Specify this parameter to show only the
    # available offerings matching the specified license model.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC filter value. Specify this parameter to show only the available VPC
    # or non-VPC offerings.
    vpc: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous
    # DescribeOrderableDBInstanceOptions request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePendingMaintenanceActionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_identifier",
                "ResourceIdentifier",
                TypeInfo(str),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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
        ]

    # The ARN of a resource to return pending maintenance actions for.
    resource_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that specifies one or more resources to return pending maintenance
    # actions for.

    # Supported filters:

    #   * `db-cluster-id` \- Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.

    #   * `db-instance-id` \- Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous
    # `DescribePendingMaintenanceActions` request. If this parameter is
    # specified, the response includes only records beyond the marker, up to a
    # number of records specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedDBInstancesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_db_instance_id",
                "ReservedDBInstanceId",
                TypeInfo(str),
            ),
            (
                "reserved_db_instances_offering_id",
                "ReservedDBInstancesOfferingId",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
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
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The reserved DB instance identifier filter value. Specify this parameter to
    # show only the reservation that matches the specified reservation ID.
    reserved_db_instance_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The offering identifier filter value. Specify this parameter to show only
    # purchased reservations matching the specified offering identifier.
    reserved_db_instances_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB instance class filter value. Specify this parameter to show only
    # those reservations matching the specified DB instances class.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration filter value, specified in years or seconds. Specify this
    # parameter to show only reservations for this duration.

    # Valid Values: `1 | 3 | 31536000 | 94608000`
    duration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product description filter value. Specify this parameter to show only
    # those reservations matching the specified product description.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type filter value. Specify this parameter to show only the
    # available offerings matching the specified offering type.

    # Valid Values: `"Partial Upfront" | "All Upfront" | "No Upfront" `
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Multi-AZ filter value. Specify this parameter to show only those
    # reservations matching the specified Multi-AZ parameter.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more than the
    # `MaxRecords` value is available, a pagination token called a marker is
    # included in the response so that the following results can be retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservedDBInstancesOfferingsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_db_instances_offering_id",
                "ReservedDBInstancesOfferingId",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
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
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
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

    # The offering identifier filter value. Specify this parameter to show only
    # the available offering that matches the specified reservation identifier.

    # Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`
    reserved_db_instances_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB instance class filter value. Specify this parameter to show only the
    # available offerings matching the specified DB instance class.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Duration filter value, specified in years or seconds. Specify this
    # parameter to show only reservations for this duration.

    # Valid Values: `1 | 3 | 31536000 | 94608000`
    duration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Product description filter value. Specify this parameter to show only the
    # available offerings that contain the specified product description.

    # The results show offerings that partially match the filter value.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type filter value. Specify this parameter to show only the
    # available offerings matching the specified offering type.

    # Valid Values: `"Partial Upfront" | "All Upfront" | "No Upfront" `
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Multi-AZ filter value. Specify this parameter to show only the
    # available offerings matching the specified Multi-AZ parameter.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more than the
    # `MaxRecords` value is available, a pagination token called a marker is
    # included in the response so that the following results can be retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSourceRegionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
        ]

    # The source AWS Region name. For example, `us-east-1`.

    # Constraints:

    #   * Must specify a valid AWS Region name.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 100.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous DescribeSourceRegions
    # request. If this parameter is specified, the response includes only records
    # beyond the marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeValidDBInstanceModificationsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The customer identifier or the ARN of your DB instance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeValidDBInstanceModificationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "valid_db_instance_modifications_message",
                "ValidDBInstanceModificationsMessage",
                TypeInfo(ValidDBInstanceModificationsMessage),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about valid modifications that you can make to your DB
    # instance. Contains the result of a successful call to the
    # DescribeValidDBInstanceModifications action. You can use this information
    # when you call ModifyDBInstance.
    valid_db_instance_modifications_message: "ValidDBInstanceModificationsMessage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DomainMembership(ShapeBase):
    """
    An Active Directory Domain membership record associated with the DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "fqdn",
                "FQDN",
                TypeInfo(str),
            ),
            (
                "iam_role_name",
                "IAMRoleName",
                TypeInfo(str),
            ),
        ]

    # The identifier of the Active Directory Domain.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the DB instance's Active Directory Domain membership, such as
    # joined, pending-join, failed etc).
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain name of the Active Directory Domain.
    fqdn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the IAM role to be used when making API calls to the Directory
    # Service.
    iam_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainNotFoundFault(ShapeBase):
    """
    _Domain_ doesn't refer to an existing Active Directory domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DoubleRange(ShapeBase):
    """
    A range of double values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_",
                "From",
                TypeInfo(float),
            ),
            (
                "to",
                "To",
                TypeInfo(float),
            ),
        ]

    # The minimum value in the range.
    from_: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value in the range.
    to: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DownloadDBLogFilePortionDetails(OutputShapeBase):
    """
    This data type is used as a response element to DownloadDBLogFilePortion.
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
                "log_file_data",
                "LogFileData",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "additional_data_pending",
                "AdditionalDataPending",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Entries from the specified log file.
    log_file_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token that can be used in a subsequent
    # DownloadDBLogFilePortion request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Boolean value that if true, indicates there is more data to be downloaded.
    additional_data_pending: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DownloadDBLogFilePortionDetails", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DownloadDBLogFilePortionMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "log_file_name",
                "LogFileName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "number_of_lines",
                "NumberOfLines",
                TypeInfo(int),
            ),
        ]

    # The customer-assigned name of the DB instance that contains the log files
    # you want to list.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the log file to be downloaded.
    log_file_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token provided in the previous request or "0". If the Marker
    # parameter is specified the response includes only records beyond the marker
    # until the end of the file or up to NumberOfLines.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of lines to download. If the number of lines specified results
    # in a file over 1 MB in size, the file is truncated at 1 MB in size.

    # If the NumberOfLines parameter is specified, then the block of lines
    # returned can be from the beginning or the end of the log file, depending on
    # the value of the Marker parameter.

    #   * If neither Marker or NumberOfLines are specified, the entire log file is returned up to a maximum of 10000 lines, starting with the most recent log entries first.

    #   * If NumberOfLines is specified and Marker is not specified, then the most recent lines from the end of the log file are returned.

    #   * If Marker is specified as "0", then the specified number of lines from the beginning of the log file are returned.

    #   * You can download the log file in blocks of lines by specifying the size of the block using the NumberOfLines parameter, and by specifying a value of "0" for the Marker parameter in your first request. Include the Marker value returned in the response as the Marker value for the next request, continuing until the AdditionalDataPending response element returns false.
    number_of_lines: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2SecurityGroup(ShapeBase):
    """
    This data type is used as a response element in the following actions:

      * AuthorizeDBSecurityGroupIngress

      * DescribeDBSecurityGroups

      * RevokeDBSecurityGroupIngress
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
                "ec2_security_group_id",
                "EC2SecurityGroupId",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_owner_id",
                "EC2SecurityGroupOwnerId",
                TypeInfo(str),
            ),
        ]

    # Provides the status of the EC2 security group. Status can be "authorizing",
    # "authorized", "revoking", and "revoked".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the EC2 security group.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the id of the EC2 security group.
    ec2_security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the AWS ID of the owner of the EC2 security group specified in
    # the `EC2SecurityGroupName` field.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    """
    This data type is used as a response element in the following actions:

      * CreateDBInstance

      * DescribeDBInstances

      * DeleteDBInstance
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
            (
                "hosted_zone_id",
                "HostedZoneId",
                TypeInfo(str),
            ),
        ]

    # Specifies the DNS address of the DB instance.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the port that the database engine is listening on.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the ID that Amazon Route 53 assigns when you create a hosted
    # zone.
    hosted_zone_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EngineDefaults(ShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeEngineDefaultParameters action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_family",
                "DBParameterGroupFamily",
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

    # Specifies the name of the DB parameter group family that the engine default
    # parameters apply to.
    db_parameter_group_family: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous EngineDefaults request.
    # If this parameter is specified, the response includes only records beyond
    # the marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a list of engine default parameters.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Event(ShapeBase):
    """
    This data type is used as a response element in the DescribeEvents action.
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
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
            (
                "source_arn",
                "SourceArn",
                TypeInfo(str),
            ),
        ]

    # Provides the identifier for the source of the event.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the source type for this event.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the text of this event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the category for the event.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the date and time of the event.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the event.
    source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventCategoriesMap(ShapeBase):
    """
    Contains the results of a successful invocation of the DescribeEventCategories
    action.
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
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The source type that the returned categories belong to
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event categories for the specified source type
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventCategoriesMessage(OutputShapeBase):
    """
    Data returned from the **DescribeEventCategories** action.
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

    # A list of EventCategoriesMap data types.
    event_categories_map_list: typing.List["EventCategoriesMap"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class EventSubscription(ShapeBase):
    """
    Contains the results of a successful invocation of the
    DescribeEventSubscriptions action.
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
                TypeInfo(str),
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
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "event_subscription_arn",
                "EventSubscriptionArn",
                TypeInfo(str),
            ),
        ]

    # The AWS customer account associated with the RDS event notification
    # subscription.
    customer_aws_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The RDS event notification subscription Id.
    cust_subscription_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The topic ARN of the RDS event notification subscription.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the RDS event notification subscription.

    # Constraints:

    # Can be one of the following: creating | modifying | deleting | active | no-
    # permission | topic-not-exist

    # The status "no-permission" indicates that RDS no longer has permission to
    # post to the SNS topic. The status "topic-not-exist" indicates that the
    # topic was deleted after the subscription was created.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the RDS event notification subscription was created.
    subscription_creation_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source type for the RDS event notification subscription.
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source IDs for the RDS event notification subscription.
    source_ids_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event categories for the RDS event notification subscription.
    event_categories_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value indicating if the subscription is enabled. True indicates
    # the subscription is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the event subscription.
    event_subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSubscriptionQuotaExceededFault(ShapeBase):
    """
    You have reached the maximum number of event subscriptions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EventSubscriptionsMessage(OutputShapeBase):
    """
    Data returned by the **DescribeEventSubscriptions** action.
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

    # An optional pagination token provided by a previous
    # DescribeOrderableDBInstanceOptions request. If this parameter is specified,
    # the response includes only records beyond the marker, up to the value
    # specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of EventSubscriptions data types.
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
    Contains the result of a successful invocation of the DescribeEvents action.
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

    # An optional pagination token provided by a previous Events request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Event instances.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["EventsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class FailoverDBClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_instance_identifier",
                "TargetDBInstanceIdentifier",
                TypeInfo(str),
            ),
        ]

    # A DB cluster identifier to force a failover for. This parameter is not
    # case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the instance to promote to the primary instance.

    # You must specify the instance identifier for an Aurora Replica in the DB
    # cluster. For example, `mydbcluster-replica1`.
    target_db_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FailoverDBClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Filter(ShapeBase):
    """
    A filter name and value pair that is used to return a more specific list of
    results from a describe operation. Filters can be used to match a set of
    resources by specific criteria, such as IDs. The filters supported by a describe
    operation are documented with the describe operation.

    Currently, wildcards are not supported in filters.

    The following actions can be filtered:

      * DescribeDBClusterBacktracks

      * DescribeDBClusters

      * DescribeDBInstances

      * DescribePendingMaintenanceActions
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

    # The name of the filter. Filter names are case-sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more filter values. Filter values are case-sensitive.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IPRange(ShapeBase):
    """
    This data type is used as a response element in the DescribeDBSecurityGroups
    action.
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
        ]

    # Specifies the status of the IP range. Status can be "authorizing",
    # "authorized", "revoking", and "revoked".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the IP range.
    cidrip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of DB
    instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientDBClusterCapacityFault(ShapeBase):
    """
    The DB cluster doesn't have enough capacity for the current operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientDBInstanceCapacityFault(ShapeBase):
    """
    The specified DB instance class isn't available in the specified Availability
    Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InsufficientStorageClusterCapacityFault(ShapeBase):
    """
    There is insufficient storage available for the current action. You might be
    able to resolve this error by updating your subnet group to use different
    Availability Zones that have more storage available.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBClusterCapacityFault(ShapeBase):
    """
    _Capacity_ isn't a valid Aurora Serverless DB cluster capacity. Valid capacity
    values are `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBClusterSnapshotStateFault(ShapeBase):
    """
    The supplied value isn't a valid DB cluster snapshot state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBClusterStateFault(ShapeBase):
    """
    The DB cluster isn't in a valid state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBInstanceStateFault(ShapeBase):
    """
    The specified DB instance isn't in the _available_ state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBParameterGroupStateFault(ShapeBase):
    """
    The DB parameter group is in use or is in an invalid state. If you are
    attempting to delete the parameter group, you can't delete it when the parameter
    group is in this state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSecurityGroupStateFault(ShapeBase):
    """
    The state of the DB security group doesn't allow deletion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSnapshotStateFault(ShapeBase):
    """
    The state of the DB snapshot doesn't allow deletion.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSubnetGroupFault(ShapeBase):
    """
    The DBSubnetGroup doesn't belong to the same VPC as that of an existing cross-
    region read replica of the same source instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSubnetGroupStateFault(ShapeBase):
    """
    The DB subnet group cannot be deleted because it's in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidDBSubnetStateFault(ShapeBase):
    """
    The DB subnet isn't in the _available_ state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidEventSubscriptionStateFault(ShapeBase):
    """
    This error can occur if someone else is modifying a subscription. You should
    retry the action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidOptionGroupStateFault(ShapeBase):
    """
    The option group isn't in the _available_ state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRestoreFault(ShapeBase):
    """
    Cannot restore from VPC backup to non-VPC DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3BucketFault(ShapeBase):
    """
    The specified Amazon S3 bucket name can't be found or Amazon RDS isn't
    authorized to access the specified Amazon S3 bucket. Verify the
    **SourceS3BucketName** and **S3IngestionRoleArn** values and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidSubnet(ShapeBase):
    """
    The requested subnet is invalid, or multiple subnets were requested that are not
    all in a common VPC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidVPCNetworkStateFault(ShapeBase):
    """
    The DB subnet group doesn't cover all Availability Zones after it's created
    because of users' change.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KMSKeyNotAccessibleFault(ShapeBase):
    """
    An error occurred accessing an AWS KMS key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListTagsForResourceMessage(ShapeBase):
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
                "filters",
                "Filters",
                TypeInfo(typing.List[Filter]),
            ),
        ]

    # The Amazon RDS resource with tags to be listed. This value is an Amazon
    # Resource Name (ARN). For information about creating an ARN, see [
    # Constructing an ARN for Amazon
    # RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing)
    # in the _Amazon RDS User Guide_.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is not currently supported.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyCurrentDBClusterCapacityMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "capacity",
                "Capacity",
                TypeInfo(int),
            ),
            (
                "seconds_before_timeout",
                "SecondsBeforeTimeout",
                TypeInfo(int),
            ),
            (
                "timeout_action",
                "TimeoutAction",
                TypeInfo(str),
            ),
        ]

    # The DB cluster identifier for the cluster being modified. This parameter is
    # not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DB cluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB cluster capacity.

    # Constraints:

    #   * Value must be `2`, `4`, `8`, `16`, `32`, `64`, `128`, or `256`.
    capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, that Aurora Serverless tries to find a
    # scaling point to perform seamless scaling before enforcing the timeout
    # action. The default is 300.

    #   * Value must be from 10 through 600.
    seconds_before_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action to take when the timeout is reached, either
    # `ForceApplyCapacityChange` or `RollbackCapacityChange`.

    # `ForceApplyCapacityChange`, the default, sets the capacity to the specified
    # value as soon as possible.

    # `RollbackCapacityChange` ignores the capacity change if a scaling point is
    # not found in the timeout period.
    timeout_action: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyDBClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "new_db_cluster_identifier",
                "NewDBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "backtrack_window",
                "BacktrackWindow",
                TypeInfo(int),
            ),
            (
                "cloudwatch_logs_export_configuration",
                "CloudwatchLogsExportConfiguration",
                TypeInfo(CloudwatchLogsExportConfiguration),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "scaling_configuration",
                "ScalingConfiguration",
                TypeInfo(ScalingConfiguration),
            ),
        ]

    # The DB cluster identifier for the cluster being modified. This parameter is
    # not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new DB cluster identifier for the DB cluster when renaming a DB
    # cluster. This value is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * The first character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-cluster2`
    new_db_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies whether the modifications in this request and any
    # pending modifications are asynchronously applied as soon as possible,
    # regardless of the `PreferredMaintenanceWindow` setting for the DB cluster.
    # If this parameter is set to `false`, changes to the DB cluster are applied
    # during the next maintenance window.

    # The `ApplyImmediately` parameter only affects the
    # `EnableIAMDatabaseAuthentication`, `MasterUserPassword`, and
    # `NewDBClusterIdentifier` values. If you set the `ApplyImmediately`
    # parameter value to false, then changes to the
    # `EnableIAMDatabaseAuthentication`, `MasterUserPassword`, and
    # `NewDBClusterIdentifier` values are applied during the next maintenance
    # window. All other changes are applied immediately, regardless of the value
    # of the `ApplyImmediately` parameter.

    # Default: `false`
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days for which automated backups are retained. You must
    # specify a minimum value of 1.

    # Default: 1

    # Constraints:

    #   * Must be a value from 1 to 35
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the DB cluster parameter group to use for the DB cluster.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of VPC security groups that the DB cluster will belong to.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which the DB cluster accepts connections.

    # Constraints: Value must be `1150-65535`

    # Default: The same port as the original DB cluster.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password for the master database user. This password can contain
    # any printable ASCII character except "/", """, or "@".

    # Constraints: Must contain from 8 to 41 characters.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates that the DB cluster should be associated with the
    # specified option group. Changing this parameter doesn't result in an outage
    # except in the following case, and the change is applied during the next
    # maintenance window unless the `ApplyImmediately` parameter is set to `true`
    # for this request. If the parameter change results in an option group that
    # enables OEM, this change can cause a brief (sub-second) period during which
    # new connections are rejected but existing connections are not interrupted.

    # Permanent options can't be removed from an option group. The option group
    # can't be removed from a DB cluster once it is associated with a DB cluster.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The daily time range during which automated backups are created if
    # automated backups are enabled, using the `BackupRetentionPeriod` parameter.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region. To see the time blocks available, see [
    # Adjusting the Preferred DB Cluster Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora)
    # in the _Amazon Aurora User Guide._

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week. To see
    # the time blocks available, see [ Adjusting the Preferred DB Cluster
    # Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora)
    # in the _Amazon Aurora User Guide._

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target backtrack window, in seconds. To disable backtracking, set this
    # value to 0.

    # Default: 0

    # Constraints:

    #   * If specified, this value must be set to a number from 0 to 259,200 (72 hours).
    backtrack_window: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration setting for the log types to be enabled for export to
    # CloudWatch Logs for a specific DB cluster.
    cloudwatch_logs_export_configuration: "CloudwatchLogsExportConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version number of the database engine to which you want to upgrade.
    # Changing this parameter results in an outage. The change is applied during
    # the next maintenance window unless the ApplyImmediately parameter is set to
    # true.

    # For a list of valid engine versions, see CreateDBCluster, or call
    # DescribeDBEngineVersions.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scaling properties of the DB cluster. You can only modify scaling
    # properties for DB clusters in `serverless` DB engine mode.
    scaling_configuration: "ScalingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the DB cluster parameter group to modify.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of parameters in the DB cluster parameter group to modify.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyDBClusterSnapshotAttributeMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_snapshot_identifier",
                "DBClusterSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "values_to_add",
                "ValuesToAdd",
                TypeInfo(typing.List[str]),
            ),
            (
                "values_to_remove",
                "ValuesToRemove",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier for the DB cluster snapshot to modify the attributes for.
    db_cluster_snapshot_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the DB cluster snapshot attribute to modify.

    # To manage authorization for other AWS accounts to copy or restore a manual
    # DB cluster snapshot, set this value to `restore`.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DB cluster snapshot attributes to add to the attribute specified
    # by `AttributeName`.

    # To authorize other AWS accounts to copy or restore a manual DB cluster
    # snapshot, set this list to include one or more AWS account IDs, or `all` to
    # make the manual DB cluster snapshot restorable by any AWS account. Do not
    # add the `all` value for any manual DB cluster snapshots that contain
    # private information that you don't want available to all AWS accounts.
    values_to_add: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of DB cluster snapshot attributes to remove from the attribute
    # specified by `AttributeName`.

    # To remove authorization for other AWS accounts to copy or restore a manual
    # DB cluster snapshot, set this list to include one or more AWS account
    # identifiers, or `all` to remove authorization for any AWS account to copy
    # or restore the DB cluster snapshot. If you specify `all`, an AWS account
    # whose account ID is explicitly added to the `restore` attribute can still
    # copy or restore a manual DB cluster snapshot.
    values_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBClusterSnapshotAttributeResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster_snapshot_attributes_result",
                "DBClusterSnapshotAttributesResult",
                TypeInfo(DBClusterSnapshotAttributesResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the results of a successful call to the
    # DescribeDBClusterSnapshotAttributes API action.

    # Manual DB cluster snapshot attributes are used to authorize other AWS
    # accounts to copy or restore a manual DB cluster snapshot. For more
    # information, see the ModifyDBClusterSnapshotAttribute API action.
    db_cluster_snapshot_attributes_result: "DBClusterSnapshotAttributesResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "db_security_groups",
                "DBSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "allow_major_version_upgrade",
                "AllowMajorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "new_db_instance_identifier",
                "NewDBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                TypeInfo(str),
            ),
            (
                "tde_credential_password",
                "TdeCredentialPassword",
                TypeInfo(str),
            ),
            (
                "ca_certificate_identifier",
                "CACertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                TypeInfo(int),
            ),
            (
                "db_port_number",
                "DBPortNumber",
                TypeInfo(int),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                TypeInfo(str),
            ),
            (
                "domain_iam_role_name",
                "DomainIAMRoleName",
                TypeInfo(str),
            ),
            (
                "promotion_tier",
                "PromotionTier",
                TypeInfo(int),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "enable_performance_insights",
                "EnablePerformanceInsights",
                TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                TypeInfo(str),
            ),
            (
                "performance_insights_retention_period",
                "PerformanceInsightsRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "cloudwatch_logs_export_configuration",
                "CloudwatchLogsExportConfiguration",
                TypeInfo(CloudwatchLogsExportConfiguration),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
            (
                "use_default_processor_features",
                "UseDefaultProcessorFeatures",
                TypeInfo(bool),
            ),
        ]

    # The DB instance identifier. This value is stored as a lowercase string.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new amount of storage (in gibibytes) to allocate for the DB instance.

    # For MariaDB, MySQL, Oracle, and PostgreSQL, the value supplied must be at
    # least 10% greater than the current value. Values that are not at least 10%
    # greater than the existing value are rounded up so that they are 10% greater
    # than the current value.

    # For the valid values for allocated storage for each engine, see
    # CreateDBInstance.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new compute and memory capacity of the DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions, or for all database engines. For the full list of DB instance
    # classes, and availability for your engine, see [DB Instance
    # Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
    # in the _Amazon RDS User Guide._

    # If you modify the DB instance class, an outage occurs during the change.
    # The change is applied during the next maintenance window, unless
    # `ApplyImmediately` is specified as `true` for this request.

    # Default: Uses existing setting
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new DB subnet group for the DB instance. You can use this parameter to
    # move your DB instance to a different VPC. If your DB instance is not in a
    # VPC, you can also use this parameter to move your DB instance into a VPC.
    # For more information, see [Updating the VPC for a DB
    # Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Non-
    # VPC2VPC) in the _Amazon RDS User Guide._

    # Changing the subnet group causes an outage during the change. The change is
    # applied during the next maintenance window, unless you specify `true` for
    # the `ApplyImmediately` parameter.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetGroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DB security groups to authorize on this DB instance. Changing
    # this setting doesn't result in an outage and the change is asynchronously
    # applied as soon as possible.

    # Constraints:

    #   * If supplied, must match existing DBSecurityGroups.
    db_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of EC2 VPC security groups to authorize on this DB instance. This
    # change is asynchronously applied as soon as possible.

    # **Amazon Aurora**

    # Not applicable. The associated list of EC2 VPC security groups is managed
    # by the DB cluster. For more information, see ModifyDBCluster.

    # Constraints:

    #   * If supplied, must match existing VpcSecurityGroupIds.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the modifications in this request and any pending
    # modifications are asynchronously applied as soon as possible, regardless of
    # the `PreferredMaintenanceWindow` setting for the DB instance.

    # If this parameter is set to `false`, changes to the DB instance are applied
    # during the next maintenance window. Some parameter changes can cause an
    # outage and are applied on the next call to RebootDBInstance, or the next
    # failure reboot. Review the table of parameters in [Modifying a DB Instance
    # and Using the Apply Immediately
    # Parameter](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
    # in the _Amazon RDS User Guide._ to see the impact that setting
    # `ApplyImmediately` to `true` or `false` has for each modified parameter and
    # to determine when the changes are applied.

    # Default: `false`
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password for the master user. The password can include any
    # printable ASCII character except "/", """, or "@".

    # Changing this parameter doesn't result in an outage and the change is
    # asynchronously applied as soon as possible. Between the time of the request
    # and the completion of the request, the `MasterUserPassword` element exists
    # in the `PendingModifiedValues` element of the operation response.

    # **Amazon Aurora**

    # Not applicable. The password for the master user is managed by the DB
    # cluster. For more information, see ModifyDBCluster.

    # Default: Uses existing setting

    # **MariaDB**

    # Constraints: Must contain from 8 to 41 characters.

    # **Microsoft SQL Server**

    # Constraints: Must contain from 8 to 128 characters.

    # **MySQL**

    # Constraints: Must contain from 8 to 41 characters.

    # **Oracle**

    # Constraints: Must contain from 8 to 30 characters.

    # **PostgreSQL**

    # Constraints: Must contain from 8 to 128 characters.

    # Amazon RDS API actions never return the password, so this action provides a
    # way to regain access to a primary instance user if the password is lost.
    # This includes restoring privileges that might have been accidentally
    # revoked.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the DB parameter group to apply to the DB instance. Changing
    # this setting doesn't result in an outage. The parameter group name itself
    # is changed immediately, but the actual parameter changes are not applied
    # until you reboot the instance without failover. The db instance will NOT be
    # rebooted automatically and the parameter changes will NOT be applied during
    # the next maintenance window.

    # Default: Uses existing setting

    # Constraints: The DB parameter group must be in the same DB parameter group
    # family as this DB instance.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days to retain automated backups. Setting this parameter to a
    # positive number enables backups. Setting this parameter to 0 disables
    # automated backups.

    # Changing this parameter can result in an outage if you change from 0 to a
    # non-zero value or from a non-zero value to 0. These changes are applied
    # during the next maintenance window unless the `ApplyImmediately` parameter
    # is set to `true` for this request. If you change the parameter from one
    # non-zero value to another non-zero value, the change is asynchronously
    # applied as soon as possible.

    # **Amazon Aurora**

    # Not applicable. The retention period for automated backups is managed by
    # the DB cluster. For more information, see ModifyDBCluster.

    # Default: Uses existing setting

    # Constraints:

    #   * Must be a value from 0 to 35

    #   * Can be specified for a MySQL Read Replica only if the source is running MySQL 5.6

    #   * Can be specified for a PostgreSQL Read Replica only if the source is running PostgreSQL 9.3.5

    #   * Cannot be set to 0 if the DB instance is a source to Read Replicas
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created if
    # automated backups are enabled, as determined by the `BackupRetentionPeriod`
    # parameter. Changing this parameter doesn't result in an outage and the
    # change is asynchronously applied as soon as possible.

    # **Amazon Aurora**

    # Not applicable. The daily time range for creating automated backups is
    # managed by the DB cluster. For more information, see ModifyDBCluster.

    # Constraints:

    #   * Must be in the format hh24:mi-hh24:mi

    #   * Must be in Universal Time Coordinated (UTC)

    #   * Must not conflict with the preferred maintenance window

    #   * Must be at least 30 minutes
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range (in UTC) during which system maintenance can occur,
    # which might result in an outage. Changing this parameter doesn't result in
    # an outage, except in the following situation, and the change is
    # asynchronously applied as soon as possible. If there are pending actions
    # that cause a reboot, and the maintenance window is changed to include the
    # current time, then changing this parameter will cause a reboot of the DB
    # instance. If moving this window to the current time, there must be at least
    # 30 minutes between the current time and end of the window to ensure pending
    # changes are applied.

    # Default: Uses existing setting

    # Format: ddd:hh24:mi-ddd:hh24:mi

    # Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

    # Constraints: Must be at least 30 minutes
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies if the DB instance is a Multi-AZ deployment. Changing this
    # parameter doesn't result in an outage and the change is applied during the
    # next maintenance window unless the `ApplyImmediately` parameter is set to
    # `true` for this request.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the database engine to upgrade to. Changing this
    # parameter results in an outage and the change is applied during the next
    # maintenance window unless the `ApplyImmediately` parameter is set to `true`
    # for this request.

    # For major version upgrades, if a nondefault DB parameter group is currently
    # in use, a new DB parameter group in the DB parameter group family for the
    # new engine version must be specified. The new DB parameter group can be the
    # default for that DB parameter group family.

    # For information about valid engine versions, see CreateDBInstance, or call
    # DescribeDBEngineVersions.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that major version upgrades are allowed. Changing this parameter
    # doesn't result in an outage and the change is asynchronously applied as
    # soon as possible.

    # Constraints: This parameter must be set to true when specifying a value for
    # the EngineVersion parameter that is a different major version than the DB
    # instance's current version.
    allow_major_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates that minor version upgrades are applied automatically to the DB
    # instance during the maintenance window. Changing this parameter doesn't
    # result in an outage except in the following case and the change is
    # asynchronously applied as soon as possible. An outage will result if this
    # parameter is set to `true` during the maintenance window, and a newer minor
    # version is available, and RDS has enabled auto patching for that engine
    # version.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The license model for the DB instance.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new Provisioned IOPS (I/O operations per second) value for the RDS
    # instance.

    # Changing this setting doesn't result in an outage and the change is applied
    # during the next maintenance window unless the `ApplyImmediately` parameter
    # is set to `true` for this request. If you are migrating from Provisioned
    # IOPS to standard storage, set this value to 0. The DB instance will require
    # a reboot for the change in storage type to take effect.

    # If you choose to migrate your DB instance from using standard storage to
    # using Provisioned IOPS, or from using Provisioned IOPS to using standard
    # storage, the process can take time. The duration of the migration depends
    # on several factors such as database load, storage size, storage type
    # (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and
    # the number of prior scale storage operations. Typical migration times are
    # under 24 hours, but the process can take up to several days in some cases.
    # During the migration, the DB instance is available for use, but might
    # experience performance degradation. While the migration takes place,
    # nightly backups for the instance are suspended. No other Amazon RDS
    # operations can take place for the instance, including modifying the
    # instance, rebooting the instance, deleting the instance, creating a Read
    # Replica for the instance, and creating a DB snapshot of the instance.

    # Constraints: For MariaDB, MySQL, Oracle, and PostgreSQL, the value supplied
    # must be at least 10% greater than the current value. Values that are not at
    # least 10% greater than the existing value are rounded up so that they are
    # 10% greater than the current value.

    # Default: Uses existing setting
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the DB instance should be associated with the specified
    # option group. Changing this parameter doesn't result in an outage except in
    # the following case and the change is applied during the next maintenance
    # window unless the `ApplyImmediately` parameter is set to `true` for this
    # request. If the parameter change results in an option group that enables
    # OEM, this change can cause a brief (sub-second) period during which new
    # connections are rejected but existing connections are not interrupted.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new DB instance identifier for the DB instance when renaming a DB
    # instance. When you change the DB instance identifier, an instance reboot
    # will occur immediately if you set `Apply Immediately` to true, or will
    # occur during the next maintenance window if `Apply Immediately` to false.
    # This value is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * The first character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `mydbinstance`
    new_db_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the storage type to be associated with the DB instance.

    # If you specify Provisioned IOPS (`io1`), you must also include a value for
    # the `Iops` parameter.

    # If you choose to migrate your DB instance from using standard storage to
    # using Provisioned IOPS, or from using Provisioned IOPS to using standard
    # storage, the process can take time. The duration of the migration depends
    # on several factors such as database load, storage size, storage type
    # (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and
    # the number of prior scale storage operations. Typical migration times are
    # under 24 hours, but the process can take up to several days in some cases.
    # During the migration, the DB instance is available for use, but might
    # experience performance degradation. While the migration takes place,
    # nightly backups for the instance are suspended. No other Amazon RDS
    # operations can take place for the instance, including modifying the
    # instance, rebooting the instance, deleting the instance, creating a Read
    # Replica for the instance, and creating a DB snapshot of the instance.

    # Valid values: `standard | gp2 | io1`

    # Default: `io1` if the `Iops` parameter is specified, otherwise `standard`
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the given ARN from the key store in order to access the
    # device.
    tde_credential_password: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the certificate that needs to be associated with the instance.
    ca_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Active Directory Domain to move the instance to. Specify `none` to
    # remove the instance from its current domain. The domain must be created
    # prior to this operation. Currently only a Microsoft SQL Server instance can
    # be created in a Active Directory Domain.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the DB instance to snapshots of the DB instance,
    # and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance. To disable collecting Enhanced
    # Monitoring metrics, specify 0. The default is 0.

    # If `MonitoringRoleArn` is specified, then you must also set
    # `MonitoringInterval` to a value other than 0.

    # Valid Values: `0, 1, 5, 10, 15, 30, 60`
    monitoring_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on which the database accepts connections.

    # The value of the `DBPortNumber` parameter must not match any of the port
    # values specified for options in the option group for the DB instance.

    # Your database will restart when you change the `DBPortNumber` value
    # regardless of the value of the `ApplyImmediately` parameter.

    # **MySQL**

    # Default: `3306`

    # Valid Values: `1150-65535`

    # **MariaDB**

    # Default: `3306`

    # Valid Values: `1150-65535`

    # **PostgreSQL**

    # Default: `5432`

    # Valid Values: `1150-65535`

    # Type: Integer

    # **Oracle**

    # Default: `1521`

    # Valid Values: `1150-65535`

    # **SQL Server**

    # Default: `1433`

    # Valid Values: `1150-65535` except for `1434`, `3389`, `47001`, `49152`, and
    # `49152` through `49156`.

    # **Amazon Aurora**

    # Default: `3306`

    # Valid Values: `1150-65535`
    db_port_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Boolean value that indicates if the DB instance has a publicly resolvable
    # DNS name. Set to `True` to make the DB instance Internet-facing with a
    # publicly resolvable DNS name, which resolves to a public IP address. Set to
    # `False` to make the DB instance internal with a DNS name that resolves to a
    # private IP address.

    # `PubliclyAccessible` only applies to DB instances in a VPC. The DB instance
    # must be part of a public subnet and `PubliclyAccessible` must be true in
    # order for it to be publicly accessible.

    # Changes to the `PubliclyAccessible` parameter are applied immediately
    # regardless of the value of the `ApplyImmediately` parameter.

    # Default: false
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the IAM role that permits RDS to send enhanced monitoring
    # metrics to Amazon CloudWatch Logs. For example,
    # `arn:aws:iam:123456789012:role/emaccess`. For information on creating a
    # monitoring role, go to [To create an IAM role for Amazon RDS Enhanced
    # Monitoring](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole)
    # in the _Amazon RDS User Guide._

    # If `MonitoringInterval` is set to a value other than 0, then you must
    # supply a `MonitoringRoleArn` value.
    monitoring_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the IAM role to use when making API calls to the Directory
    # Service.
    domain_iam_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that specifies the order in which an Aurora Replica is promoted to
    # the primary instance after a failure of the existing primary instance. For
    # more information, see [ Fault Tolerance for an Aurora DB
    # Cluster](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance)
    # in the _Amazon Aurora User Guide_.

    # Default: 1

    # Valid Values: 0 - 15
    promotion_tier: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # You can enable IAM database authentication for the following database
    # engines

    # **Amazon Aurora**

    # Not applicable. Mapping AWS IAM accounts to database accounts is managed by
    # the DB cluster. For more information, see ModifyDBCluster.

    # **MySQL**

    #   * For MySQL 5.6, minor version 5.6.34 or higher

    #   * For MySQL 5.7, minor version 5.7.16 or higher

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True to enable Performance Insights for the DB instance, and otherwise
    # false.

    # For more information, see [Using Amazon Performance
    # Insights](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
    # in the _Amazon Relational Database Service User Guide_.
    enable_performance_insights: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the
    # KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in days, to retain Performance Insights data. Valid
    # values are 7 or 731 (2 years).
    performance_insights_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration setting for the log types to be enabled for export to
    # CloudWatch Logs for a specific DB instance.
    cloudwatch_logs_export_configuration: "CloudwatchLogsExportConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies that the DB instance class of the DB instance uses
    # its default processor features.
    use_default_processor_features: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyDBParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.List[Parameter]),
            ),
        ]

    # The name of the DB parameter group.

    # Constraints:

    #   * If supplied, must match the name of an existing DBParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of parameter names, values, and the apply method for the parameter
    # update. At least one parameter name, value, and apply method must be
    # supplied; subsequent arguments are optional. A maximum of 20 parameters can
    # be modified in a single request.

    # Valid Values (for the application method): `immediate | pending-reboot`

    # You can use the immediate value with dynamic parameters only. You can use
    # the pending-reboot value for both dynamic and static parameters, and
    # changes are applied when you reboot the DB instance without failover.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBSnapshotAttributeMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "values_to_add",
                "ValuesToAdd",
                TypeInfo(typing.List[str]),
            ),
            (
                "values_to_remove",
                "ValuesToRemove",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier for the DB snapshot to modify the attributes for.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the DB snapshot attribute to modify.

    # To manage authorization for other AWS accounts to copy or restore a manual
    # DB snapshot, set this value to `restore`.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DB snapshot attributes to add to the attribute specified by
    # `AttributeName`.

    # To authorize other AWS accounts to copy or restore a manual snapshot, set
    # this list to include one or more AWS account IDs, or `all` to make the
    # manual DB snapshot restorable by any AWS account. Do not add the `all`
    # value for any manual DB snapshots that contain private information that you
    # don't want available to all AWS accounts.
    values_to_add: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of DB snapshot attributes to remove from the attribute specified by
    # `AttributeName`.

    # To remove authorization for other AWS accounts to copy or restore a manual
    # snapshot, set this list to include one or more AWS account identifiers, or
    # `all` to remove authorization for any AWS account to copy or restore the DB
    # snapshot. If you specify `all`, an AWS account whose account ID is
    # explicitly added to the `restore` attribute can still copy or restore the
    # manual DB snapshot.
    values_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBSnapshotAttributeResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_snapshot_attributes_result",
                "DBSnapshotAttributesResult",
                TypeInfo(DBSnapshotAttributesResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the results of a successful call to the
    # DescribeDBSnapshotAttributes API action.

    # Manual DB snapshot attributes are used to authorize other AWS accounts to
    # copy or restore a manual DB snapshot. For more information, see the
    # ModifyDBSnapshotAttribute API action.
    db_snapshot_attributes_result: "DBSnapshotAttributesResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBSnapshotMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
        ]

    # The identifier of the DB snapshot to modify.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version to upgrade the DB snapshot to.

    # The following are the database engines and engine versions that are
    # available when you upgrade a DB snapshot.

    # **MySQL**

    #   * `5.5.46` (supported for 5.1 DB snapshots)

    # **Oracle**

    #   * `12.1.0.2.v8` (supported for 12.1.0.1 DB snapshots)

    #   * `11.2.0.4.v12` (supported for 11.2.0.2 DB snapshots)

    #   * `11.2.0.4.v11` (supported for 11.2.0.3 DB snapshots)
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The option group to identify with the upgraded DB snapshot.

    # You can specify this parameter when you upgrade an Oracle DB snapshot. The
    # same option group considerations apply when upgrading a DB snapshot as when
    # upgrading a DB instance. For more information, see [Option Group
    # Considerations](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.html#USER_UpgradeDBInstance.Oracle.OGPG.OG)
    # in the _Amazon RDS User Guide._
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyDBSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_snapshot",
                "DBSnapshot",
                TypeInfo(DBSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB snapshot.

    # This data type is used as a response element in the DescribeDBSnapshots
    # action.
    db_snapshot: "DBSnapshot" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyDBSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "db_subnet_group_description",
                "DBSubnetGroupDescription",
                TypeInfo(str),
            ),
        ]

    # The name for the DB subnet group. This value is stored as a lowercase
    # string. You can't modify the default subnet group.

    # Constraints: Must match the name of an existing DBSubnetGroup. Must not be
    # default.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 subnet IDs for the DB subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for the DB subnet group.
    db_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyDBSubnetGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_subnet_group",
                "DBSubnetGroup",
                TypeInfo(DBSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB subnet group.

    # This data type is used as a response element in the DescribeDBSubnetGroups
    # action.
    db_subnet_group: "DBSubnetGroup" = dataclasses.field(
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
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the RDS event notification subscription.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SNS topic created for event
    # notification. The ARN is created by Amazon SNS when you create a topic and
    # subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of source that is generating the events. For example, if you want
    # to be notified of events generated by a DB instance, you would set this
    # parameter to db-instance. if this value is not specified, all events are
    # returned.

    # Valid values: db-instance | db-parameter-group | db-security-group | db-
    # snapshot
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories for a SourceType that you want to subscribe to.
    # You can see a list of the categories for a given SourceType in the
    # [Events](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
    # topic in the _Amazon RDS User Guide_ or by using the
    # **DescribeEventCategories** action.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value; set to **true** to activate the subscription.
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

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyOptionGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "options_to_include",
                "OptionsToInclude",
                TypeInfo(typing.List[OptionConfiguration]),
            ),
            (
                "options_to_remove",
                "OptionsToRemove",
                TypeInfo(typing.List[str]),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
        ]

    # The name of the option group to be modified.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Options in this list are added to the option group or, if already present,
    # the specified configuration is used to update the existing configuration.
    options_to_include: typing.List["OptionConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Options in this list are removed from the option group.
    options_to_remove: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the changes should be applied immediately, or during the
    # next maintenance window for each instance associated with the option group.
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyOptionGroupResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "option_group",
                "OptionGroup",
                TypeInfo(OptionGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    option_group: "OptionGroup" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Option(ShapeBase):
    """
    Option details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_name",
                "OptionName",
                TypeInfo(str),
            ),
            (
                "option_description",
                "OptionDescription",
                TypeInfo(str),
            ),
            (
                "persistent",
                "Persistent",
                TypeInfo(bool),
            ),
            (
                "permanent",
                "Permanent",
                TypeInfo(bool),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "option_version",
                "OptionVersion",
                TypeInfo(str),
            ),
            (
                "option_settings",
                "OptionSettings",
                TypeInfo(typing.List[OptionSetting]),
            ),
            (
                "db_security_group_memberships",
                "DBSecurityGroupMemberships",
                TypeInfo(typing.List[DBSecurityGroupMembership]),
            ),
            (
                "vpc_security_group_memberships",
                "VpcSecurityGroupMemberships",
                TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
        ]

    # The name of the option.
    option_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the option.
    option_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicate if this option is persistent.
    persistent: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicate if this option is permanent.
    permanent: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If required, the port configured for this option to use.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the option.
    option_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The option settings for this option.
    option_settings: typing.List["OptionSetting"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the option requires access to a port, then this DB security group allows
    # access to the port.
    db_security_group_memberships: typing.List["DBSecurityGroupMembership"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # If the option requires access to a port, then this VPC security group
    # allows access to the port.
    vpc_security_group_memberships: typing.List["VpcSecurityGroupMembership"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )


@dataclasses.dataclass
class OptionConfiguration(ShapeBase):
    """
    A list of all available options
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_name",
                "OptionName",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "option_version",
                "OptionVersion",
                TypeInfo(str),
            ),
            (
                "db_security_group_memberships",
                "DBSecurityGroupMemberships",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_memberships",
                "VpcSecurityGroupMemberships",
                TypeInfo(typing.List[str]),
            ),
            (
                "option_settings",
                "OptionSettings",
                TypeInfo(typing.List[OptionSetting]),
            ),
        ]

    # The configuration of options to include in a group.
    option_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The optional port for the option.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version for the option.
    option_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DBSecurityGroupMemebrship name strings used for this option.
    db_security_group_memberships: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of VpcSecurityGroupMemebrship name strings used for this option.
    vpc_security_group_memberships: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The option settings to include in an option group.
    option_settings: typing.List["OptionSetting"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OptionGroup(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "option_group_description",
                "OptionGroupDescription",
                TypeInfo(str),
            ),
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "major_engine_version",
                "MajorEngineVersion",
                TypeInfo(str),
            ),
            (
                "options",
                "Options",
                TypeInfo(typing.List[Option]),
            ),
            (
                "allows_vpc_and_non_vpc_instance_memberships",
                "AllowsVpcAndNonVpcInstanceMemberships",
                TypeInfo(bool),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "option_group_arn",
                "OptionGroupArn",
                TypeInfo(str),
            ),
        ]

    # Specifies the name of the option group.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides a description of the option group.
    option_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the name of the engine that this option group can be applied to.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the major engine version associated with this option group.
    major_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates what options are available in the option group.
    options: typing.List["Option"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether this option group can be applied to both VPC and non-VPC
    # instances. The value `true` indicates the option group can be applied to
    # both VPC and non-VPC instances.
    allows_vpc_and_non_vpc_instance_memberships: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If **AllowsVpcAndNonVpcInstanceMemberships** is `false`, this field is
    # blank. If **AllowsVpcAndNonVpcInstanceMemberships** is `true` and this
    # field is blank, then this option group can be applied to both VPC and non-
    # VPC instances. If this field contains a value, then this option group can
    # only be applied to instances that are in the VPC indicated by this field.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the option group.
    option_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OptionGroupAlreadyExistsFault(ShapeBase):
    """
    The option group you are trying to create already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OptionGroupMembership(ShapeBase):
    """
    Provides information on the option groups the DB instance is a member of.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The name of the option group that the instance belongs to.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the DB instance's option group membership. Valid values are:
    # `in-sync`, `pending-apply`, `pending-removal`, `pending-maintenance-apply`,
    # `pending-maintenance-removal`, `applying`, `removing`, and `failed`.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OptionGroupNotFoundFault(ShapeBase):
    """
    The specified option group could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OptionGroupOption(ShapeBase):
    """
    Available option.
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
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "major_engine_version",
                "MajorEngineVersion",
                TypeInfo(str),
            ),
            (
                "minimum_required_minor_engine_version",
                "MinimumRequiredMinorEngineVersion",
                TypeInfo(str),
            ),
            (
                "port_required",
                "PortRequired",
                TypeInfo(bool),
            ),
            (
                "default_port",
                "DefaultPort",
                TypeInfo(int),
            ),
            (
                "options_depended_on",
                "OptionsDependedOn",
                TypeInfo(typing.List[str]),
            ),
            (
                "options_conflicts_with",
                "OptionsConflictsWith",
                TypeInfo(typing.List[str]),
            ),
            (
                "persistent",
                "Persistent",
                TypeInfo(bool),
            ),
            (
                "permanent",
                "Permanent",
                TypeInfo(bool),
            ),
            (
                "requires_auto_minor_engine_version_upgrade",
                "RequiresAutoMinorEngineVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "vpc_only",
                "VpcOnly",
                TypeInfo(bool),
            ),
            (
                "supports_option_version_downgrade",
                "SupportsOptionVersionDowngrade",
                TypeInfo(bool),
            ),
            (
                "option_group_option_settings",
                "OptionGroupOptionSettings",
                TypeInfo(typing.List[OptionGroupOptionSetting]),
            ),
            (
                "option_group_option_versions",
                "OptionGroupOptionVersions",
                TypeInfo(typing.List[OptionVersion]),
            ),
        ]

    # The name of the option.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the option.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the engine that this option can be applied to.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the major engine version that the option is available for.
    major_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum required engine version for the option to be applied.
    minimum_required_minor_engine_version: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the option requires a port.
    port_required: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the option requires a port, specifies the default port for the option.
    default_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The options that are prerequisites for this option.
    options_depended_on: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The options that conflict with this option.
    options_conflicts_with: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Persistent options can't be removed from an option group while DB instances
    # are associated with the option group. If you disassociate all DB instances
    # from the option group, your can remove the persistent option from the
    # option group.
    persistent: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Permanent options can never be removed from an option group. An option
    # group containing a permanent option can't be removed from a DB instance.
    permanent: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, you must enable the Auto Minor Version Upgrade setting for your DB
    # instance before you can use this option. You can enable Auto Minor Version
    # Upgrade when you first create your DB instance, or by modifying your DB
    # instance later.
    requires_auto_minor_engine_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If true, you can only use this option with a DB instance that is in a VPC.
    vpc_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, you can change the option to an earlier version of the option.
    # This only applies to options that have different versions available.
    supports_option_version_downgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The option settings that are available (and the default value) for each
    # option in an option group.
    option_group_option_settings: typing.List["OptionGroupOptionSetting"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The versions that are available for the option.
    option_group_option_versions: typing.List["OptionVersion"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class OptionGroupOptionSetting(ShapeBase):
    """
    Option group option settings are used to display settings available for each
    option with their default values and other information. These values are used
    with the DescribeOptionGroupOptions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "setting_name",
                "SettingName",
                TypeInfo(str),
            ),
            (
                "setting_description",
                "SettingDescription",
                TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "apply_type",
                "ApplyType",
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
        ]

    # The name of the option group option.
    setting_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the option group option.
    setting_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value for the option group option.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB engine specific parameter type for the option group option.
    apply_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the acceptable values for the option group option.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Boolean value where true indicates that this option group option can be
    # changed from the default value.
    is_modifiable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OptionGroupOptionsMessage(OutputShapeBase):
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
                "option_group_options",
                "OptionGroupOptions",
                TypeInfo(typing.List[OptionGroupOption]),
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

    # List of available option group options.
    option_group_options: typing.List["OptionGroupOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["OptionGroupOptionsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class OptionGroupQuotaExceededFault(ShapeBase):
    """
    The quota of 20 option groups was exceeded for this AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class OptionGroups(OutputShapeBase):
    """
    List of option groups.
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
                "option_groups_list",
                "OptionGroupsList",
                TypeInfo(typing.List[OptionGroup]),
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

    # List of option groups.
    option_groups_list: typing.List["OptionGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["OptionGroups", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class OptionSetting(ShapeBase):
    """
    Option settings are the actual settings being applied or configured for that
    option. It is used when you modify an option group or describe option groups.
    For example, the NATIVE_NETWORK_ENCRYPTION option has a setting called
    SQLNET.ENCRYPTION_SERVER that can have several different values.
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
            (
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "apply_type",
                "ApplyType",
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
                "is_collection",
                "IsCollection",
                TypeInfo(bool),
            ),
        ]

    # The name of the option that has settings that you can set.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current value of the option setting.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default value of the option setting.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the option setting.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB engine specific parameter type.
    apply_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data type of the option setting.
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allowed values of the option setting.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value that, when true, indicates the option setting can be
    # modified from the default.
    is_modifiable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the option setting is part of a collection.
    is_collection: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OptionVersion(ShapeBase):
    """
    The version for an option. Option group option versions are returned by the
    DescribeOptionGroupOptions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "is_default",
                "IsDefault",
                TypeInfo(bool),
            ),
        ]

    # The version of the option.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if the version is the default version of the option, and otherwise
    # false.
    is_default: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OrderableDBInstanceOption(ShapeBase):
    """
    Contains a list of available options for a DB instance.

    This data type is used as a response element in the
    DescribeOrderableDBInstanceOptions action.
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
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[AvailabilityZone]),
            ),
            (
                "multi_az_capable",
                "MultiAZCapable",
                TypeInfo(bool),
            ),
            (
                "read_replica_capable",
                "ReadReplicaCapable",
                TypeInfo(bool),
            ),
            (
                "vpc",
                "Vpc",
                TypeInfo(bool),
            ),
            (
                "supports_storage_encryption",
                "SupportsStorageEncryption",
                TypeInfo(bool),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "supports_iops",
                "SupportsIops",
                TypeInfo(bool),
            ),
            (
                "supports_enhanced_monitoring",
                "SupportsEnhancedMonitoring",
                TypeInfo(bool),
            ),
            (
                "supports_iam_database_authentication",
                "SupportsIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "supports_performance_insights",
                "SupportsPerformanceInsights",
                TypeInfo(bool),
            ),
            (
                "min_storage_size",
                "MinStorageSize",
                TypeInfo(int),
            ),
            (
                "max_storage_size",
                "MaxStorageSize",
                TypeInfo(int),
            ),
            (
                "min_iops_per_db_instance",
                "MinIopsPerDbInstance",
                TypeInfo(int),
            ),
            (
                "max_iops_per_db_instance",
                "MaxIopsPerDbInstance",
                TypeInfo(int),
            ),
            (
                "min_iops_per_gib",
                "MinIopsPerGib",
                TypeInfo(float),
            ),
            (
                "max_iops_per_gib",
                "MaxIopsPerGib",
                TypeInfo(float),
            ),
            (
                "available_processor_features",
                "AvailableProcessorFeatures",
                TypeInfo(typing.List[AvailableProcessorFeature]),
            ),
            (
                "supported_engine_modes",
                "SupportedEngineModes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The engine type of a DB instance.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version of a DB instance.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB instance class for a DB instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The license model for a DB instance.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Availability Zones for a DB instance.
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether a DB instance is Multi-AZ capable.
    multi_az_capable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a DB instance can have a Read Replica.
    read_replica_capable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a DB instance is in a VPC.
    vpc: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a DB instance supports encrypted storage.
    supports_storage_encryption: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the storage type for a DB instance.
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a DB instance supports provisioned IOPS.
    supports_iops: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a DB instance supports Enhanced Monitoring at intervals
    # from 1 to 60 seconds.
    supports_enhanced_monitoring: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether a DB instance supports IAM database authentication.
    supports_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if a DB instance supports Performance Insights, otherwise false.
    supports_performance_insights: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Minimum storage size for a DB instance.
    min_storage_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum storage size for a DB instance.
    max_storage_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Minimum total provisioned IOPS for a DB instance.
    min_iops_per_db_instance: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum total provisioned IOPS for a DB instance.
    max_iops_per_db_instance: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Minimum provisioned IOPS per GiB for a DB instance.
    min_iops_per_gib: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum provisioned IOPS per GiB for a DB instance.
    max_iops_per_gib: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the available processor features for the DB instance class of a
    # DB instance.
    available_processor_features: typing.List["AvailableProcessorFeature"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # A list of the supported DB engine modes.
    supported_engine_modes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OrderableDBInstanceOptionsMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeOrderableDBInstanceOptions action.
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
                "orderable_db_instance_options",
                "OrderableDBInstanceOptions",
                TypeInfo(typing.List[OrderableDBInstanceOption]),
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

    # An OrderableDBInstanceOption structure containing information about
    # orderable options for the DB instance.
    orderable_db_instance_options: typing.List["OrderableDBInstanceOption"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # An optional pagination token provided by a previous
    # OrderableDBInstanceOptions request. If this parameter is specified, the
    # response includes only records beyond the marker, up to the value specified
    # by `MaxRecords` .
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["OrderableDBInstanceOptionsMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Parameter(ShapeBase):
    """
    This data type is used as a request parameter in the ModifyDBParameterGroup and
    ResetDBParameterGroup actions.

    This data type is used as a response element in the
    DescribeEngineDefaultParameters and DescribeDBParameters actions.
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
                "apply_type",
                "ApplyType",
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
                "apply_method",
                "ApplyMethod",
                TypeInfo(typing.Union[str, ApplyMethod]),
            ),
            (
                "supported_engine_modes",
                "SupportedEngineModes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Specifies the name of the parameter.
    parameter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the value of the parameter.
    parameter_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides a description of the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the source of the parameter value.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the engine specific parameters type.
    apply_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the valid data type for the parameter.
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the valid range of values for the parameter.
    allowed_values: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether (`true`) or not (`false`) the parameter can be modified.
    # Some parameters have security or operational implications that prevent them
    # from being changed.
    is_modifiable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The earliest engine version to which the parameter can apply.
    minimum_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates when to apply parameter updates.
    apply_method: typing.Union[str, "ApplyMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The valid DB engine modes.
    supported_engine_modes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PendingCloudwatchLogsExports(ShapeBase):
    """
    A list of the log types whose configuration is still pending. In other words,
    these log types are in the process of being activated or deactivated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_types_to_enable",
                "LogTypesToEnable",
                TypeInfo(typing.List[str]),
            ),
            (
                "log_types_to_disable",
                "LogTypesToDisable",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Log types that are in the process of being deactivated. After they are
    # deactivated, these log types aren't exported to CloudWatch Logs.
    log_types_to_enable: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Log types that are in the process of being enabled. After they are enabled,
    # these log types are exported to CloudWatch Logs.
    log_types_to_disable: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PendingMaintenanceAction(ShapeBase):
    """
    Provides information about a pending maintenance action for a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(str),
            ),
            (
                "auto_applied_after_date",
                "AutoAppliedAfterDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "forced_apply_date",
                "ForcedApplyDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "opt_in_status",
                "OptInStatus",
                TypeInfo(str),
            ),
            (
                "current_apply_date",
                "CurrentApplyDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The type of pending maintenance action that is available for the resource.
    action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date of the maintenance window when the action is applied. The
    # maintenance action is applied to the resource during its first maintenance
    # window after this date. If this date is specified, any `next-maintenance`
    # opt-in requests are ignored.
    auto_applied_after_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the maintenance action is automatically applied. The
    # maintenance action is applied to the resource on this date regardless of
    # the maintenance window for the resource. If this date is specified, any
    # `immediate` opt-in requests are ignored.
    forced_apply_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the type of opt-in request that has been received for the
    # resource.
    opt_in_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The effective date when the pending maintenance action is applied to the
    # resource. This date takes into account opt-in requests received from the
    # ApplyPendingMaintenanceAction API, the `AutoAppliedAfterDate`, and the
    # `ForcedApplyDate`. This value is blank if an opt-in request has not been
    # received and nothing has been specified as `AutoAppliedAfterDate` or
    # `ForcedApplyDate`.
    current_apply_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description providing more detail about the maintenance action.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PendingMaintenanceActionsMessage(OutputShapeBase):
    """
    Data returned from the **DescribePendingMaintenanceActions** action.
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
                "pending_maintenance_actions",
                "PendingMaintenanceActions",
                TypeInfo(typing.List[ResourcePendingMaintenanceActions]),
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

    # A list of the pending maintenance actions for the resource.
    pending_maintenance_actions: typing.List["ResourcePendingMaintenanceActions"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # An optional pagination token provided by a previous
    # `DescribePendingMaintenanceActions` request. If this parameter is
    # specified, the response includes only records beyond the marker, up to a
    # number of records specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PendingModifiedValues(ShapeBase):
    """
    This data type is used as a response element in the ModifyDBInstance action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
            ),
            (
                "master_user_password",
                "MasterUserPassword",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "ca_certificate_identifier",
                "CACertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "pending_cloudwatch_logs_exports",
                "PendingCloudwatchLogsExports",
                TypeInfo(PendingCloudwatchLogsExports),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
        ]

    # Contains the new `DBInstanceClass` for the DB instance that will be applied
    # or is currently being applied.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the new `AllocatedStorage` size for the DB instance that will be
    # applied or is currently being applied.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the pending or currently-in-progress change of the master
    # credentials for the DB instance.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the pending port for the DB instance.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the pending number of days for which automated backups are
    # retained.
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates that the Single-AZ DB instance is to change to a Multi-AZ
    # deployment.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the database engine version.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The license model for the DB instance.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the new Provisioned IOPS value for the DB instance that will be
    # applied or is currently being applied.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the new `DBInstanceIdentifier` for the DB instance that will be
    # applied or is currently being applied.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the storage type to be associated with the DB instance.
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the identifier of the CA certificate for the DB instance.
    ca_certificate_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new DB subnet group for the DB instance.
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the log types whose configuration is still pending. In other
    # words, these log types are in the process of being activated or
    # deactivated.
    pending_cloudwatch_logs_exports: "PendingCloudwatchLogsExports" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PointInTimeRestoreNotEnabledFault(ShapeBase):
    """
    _SourceDBInstanceIdentifier_ refers to a DB instance with
    _BackupRetentionPeriod_ equal to 0.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ProcessorFeature(ShapeBase):
    """
    Contains the processor features of a DB instance class.

    To specify the number of CPU cores, use the `coreCount` feature name for the
    `Name` parameter. To specify the number of threads per core, use the
    `threadsPerCore` feature name for the `Name` parameter.

    You can set the processor features of the DB instance class for a DB instance
    when you call one of the following actions:

      * CreateDBInstance

      * ModifyDBInstance

      * RestoreDBInstanceFromDBSnapshot

      * RestoreDBInstanceFromS3

      * RestoreDBInstanceToPointInTime

    You can view the valid processor values for a particular instance class by
    calling the DescribeOrderableDBInstanceOptions action and specifying the
    instance class for the `DBInstanceClass` parameter.

    In addition, you can use the following actions for DB instance class processor
    information:

      * DescribeDBInstances

      * DescribeDBSnapshots

      * DescribeValidDBInstanceModifications

    For more information, see [Configuring the Processor of the DB Instance
    Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor)
    in the _Amazon RDS User Guide._
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

    # The name of the processor feature. Valid names are `coreCount` and
    # `threadsPerCore`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of a processor feature name.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PromoteReadReplicaDBClusterMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
        ]

    # The identifier of the DB cluster Read Replica to promote. This parameter is
    # not case-sensitive.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster Read Replica.

    # Example: `my-cluster-replica1`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PromoteReadReplicaDBClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PromoteReadReplicaMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
        ]

    # The DB instance identifier. This value is stored as a lowercase string.

    # Constraints:

    #   * Must match the identifier of an existing Read Replica DB instance.

    # Example: `mydbinstance`
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of days to retain automated backups. Setting this parameter to a
    # positive number enables backups. Setting this parameter to 0 disables
    # automated backups.

    # Default: 1

    # Constraints:

    #   * Must be a value from 0 to 8
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The daily time range during which automated backups are created if
    # automated backups are enabled, using the `BackupRetentionPeriod` parameter.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region. To see the time blocks available, see [
    # Adjusting the Preferred Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html)
    # in the _Amazon RDS User Guide._

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PromoteReadReplicaResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionedIopsNotAvailableInAZFault(ShapeBase):
    """
    Provisioned IOPS not available in the specified Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PurchaseReservedDBInstancesOfferingMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_db_instances_offering_id",
                "ReservedDBInstancesOfferingId",
                TypeInfo(str),
            ),
            (
                "reserved_db_instance_id",
                "ReservedDBInstanceId",
                TypeInfo(str),
            ),
            (
                "db_instance_count",
                "DBInstanceCount",
                TypeInfo(int),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ID of the Reserved DB instance offering to purchase.

    # Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
    reserved_db_instances_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Customer-specified identifier to track this reservation.

    # Example: myreservationID
    reserved_db_instance_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances to reserve.

    # Default: `1`
    db_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseReservedDBInstancesOfferingResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "reserved_db_instance",
                "ReservedDBInstance",
                TypeInfo(ReservedDBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This data type is used as a response element in the
    # DescribeReservedDBInstances and PurchaseReservedDBInstancesOffering
    # actions.
    reserved_db_instance: "ReservedDBInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Range(ShapeBase):
    """
    A range of integer values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_",
                "From",
                TypeInfo(int),
            ),
            (
                "to",
                "To",
                TypeInfo(int),
            ),
            (
                "step",
                "Step",
                TypeInfo(int),
            ),
        ]

    # The minimum value in the range.
    from_: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value in the range.
    to: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The step value for the range. For example, if you have a range of 5,000 to
    # 10,000, with a step value of 1,000, the valid values start at 5,000 and
    # step up by 1,000. Even though 7,500 is within the range, it isn't a valid
    # value for the range. The valid values are 5,000, 6,000, 7,000, 8,000...
    step: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootDBInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "force_failover",
                "ForceFailover",
                TypeInfo(bool),
            ),
        ]

    # The DB instance identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must match the identifier of an existing DBInstance.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `true`, the reboot is conducted through a MultiAZ failover.

    # Constraint: You can't specify `true` if the instance is not configured for
    # MultiAZ.
    force_failover: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootDBInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecurringCharge(ShapeBase):
    """
    This data type is used as a response element in the DescribeReservedDBInstances
    and DescribeReservedDBInstancesOfferings actions.
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

    # The amount of the recurring charge.
    recurring_charge_amount: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The frequency of the recurring charge.
    recurring_charge_frequency: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveRoleFromDBClusterMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The name of the DB cluster to disassociate the IAM role from.
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role to disassociate from the
    # Aurora DB cluster, for example
    # `arn:aws:iam::123456789012:role/AuroraAccessRole`.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveSourceIdentifierFromSubscriptionMessage(ShapeBase):
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
                "source_identifier",
                "SourceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The name of the RDS event notification subscription you want to remove a
    # source identifier from.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source identifier to be removed from the subscription, such as the **DB
    # instance identifier** for a DB instance or the name of a security group.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveSourceIdentifierFromSubscriptionResult(OutputShapeBase):
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

    # Contains the results of a successful invocation of the
    # DescribeEventSubscriptions action.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsFromResourceMessage(ShapeBase):
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
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon RDS resource that the tags are removed from. This value is an
    # Amazon Resource Name (ARN). For information about creating an ARN, see [
    # Constructing an ARN for Amazon
    # RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing)
    # in the _Amazon RDS User Guide._
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag key (name) of the tag to be removed.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReservedDBInstance(ShapeBase):
    """
    This data type is used as a response element in the DescribeReservedDBInstances
    and PurchaseReservedDBInstancesOffering actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_db_instance_id",
                "ReservedDBInstanceId",
                TypeInfo(str),
            ),
            (
                "reserved_db_instances_offering_id",
                "ReservedDBInstancesOfferingId",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
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
                "db_instance_count",
                "DBInstanceCount",
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
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
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
            (
                "reserved_db_instance_arn",
                "ReservedDBInstanceArn",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the reservation.
    reserved_db_instance_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The offering identifier.
    reserved_db_instances_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB instance class for the reserved DB instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the reservation started.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The duration of the reservation in seconds.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fixed price charged for this reserved DB instance.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hourly price charged for this reserved DB instance.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code for the reserved DB instance.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of reserved DB instances.
    db_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the reserved DB instance.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type of this reserved DB instance.
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the reservation applies to Multi-AZ deployments.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the reserved DB instance.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring price charged to run this reserved DB instance.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the reserved DB instance.
    reserved_db_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedDBInstanceAlreadyExistsFault(ShapeBase):
    """
    User already has a reservation with the given identifier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedDBInstanceMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeReservedDBInstances action.
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
                "reserved_db_instances",
                "ReservedDBInstances",
                TypeInfo(typing.List[ReservedDBInstance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of reserved DB instances.
    reserved_db_instances: typing.List["ReservedDBInstance"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    def paginate(self,
                ) -> typing.Generator["ReservedDBInstanceMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ReservedDBInstanceNotFoundFault(ShapeBase):
    """
    The specified reserved DB Instance not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedDBInstanceQuotaExceededFault(ShapeBase):
    """
    Request would exceed the user's DB Instance quota.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReservedDBInstancesOffering(ShapeBase):
    """
    This data type is used as a response element in the
    DescribeReservedDBInstancesOfferings action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reserved_db_instances_offering_id",
                "ReservedDBInstancesOfferingId",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
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
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "recurring_charges",
                "RecurringCharges",
                TypeInfo(typing.List[RecurringCharge]),
            ),
        ]

    # The offering identifier.
    reserved_db_instances_offering_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB instance class for the reserved DB instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the offering in seconds.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fixed price charged for this offering.
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hourly price charged for this offering.
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code for the reserved DB instance offering.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database engine used by the offering.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The offering type.
    offering_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the offering applies to Multi-AZ deployments.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The recurring price charged to run this reserved DB instance.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservedDBInstancesOfferingMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the
    DescribeReservedDBInstancesOfferings action.
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
                "reserved_db_instances_offerings",
                "ReservedDBInstancesOfferings",
                TypeInfo(typing.List[ReservedDBInstancesOffering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of reserved DB instance offerings.
    reserved_db_instances_offerings: typing.List["ReservedDBInstancesOffering"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    def paginate(
        self,
    ) -> typing.Generator["ReservedDBInstancesOfferingMessage", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ReservedDBInstancesOfferingNotFoundFault(ShapeBase):
    """
    Specified offering does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResetDBClusterParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
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

    # The name of the DB cluster parameter group to reset.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that is set to `true` to reset all parameters in the DB cluster
    # parameter group to their default values, and `false` otherwise. You can't
    # use this parameter if there is a list of parameter names specified for the
    # `Parameters` parameter.
    reset_all_parameters: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of parameter names in the DB cluster parameter group to reset to the
    # default values. You can't use this parameter if the `ResetAllParameters`
    # parameter is set to `true`.
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResetDBParameterGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
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

    # The name of the DB parameter group.

    # Constraints:

    #   * Must match the name of an existing DBParameterGroup.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether (`true`) or not (`false`) to reset all parameters in the
    # DB parameter group to default values.

    # Default: `true`
    reset_all_parameters: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To reset the entire DB parameter group, specify the `DBParameterGroup` name
    # and `ResetAllParameters` parameters. To reset specific parameters, provide
    # a list of the following: `ParameterName` and `ApplyMethod`. A maximum of 20
    # parameters can be modified in a single request.

    # **MySQL**

    # Valid Values (for Apply method): `immediate` | `pending-reboot`

    # You can use the immediate value with dynamic parameters only. You can use
    # the `pending-reboot` value for both dynamic and static parameters, and
    # changes are applied when DB instance reboots.

    # **MariaDB**

    # Valid Values (for Apply method): `immediate` | `pending-reboot`

    # You can use the immediate value with dynamic parameters only. You can use
    # the `pending-reboot` value for both dynamic and static parameters, and
    # changes are applied when DB instance reboots.

    # **Oracle**

    # Valid Values (for Apply method): `pending-reboot`
    parameters: typing.List["Parameter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFoundFault(ShapeBase):
    """
    The specified resource ID was not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourcePendingMaintenanceActions(ShapeBase):
    """
    Describes the pending maintenance actions for a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_identifier",
                "ResourceIdentifier",
                TypeInfo(str),
            ),
            (
                "pending_maintenance_action_details",
                "PendingMaintenanceActionDetails",
                TypeInfo(typing.List[PendingMaintenanceAction]),
            ),
        ]

    # The ARN of the resource that has pending maintenance actions.
    resource_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list that provides details about the pending maintenance actions for the
    # resource.
    pending_maintenance_action_details: typing.List[
        "PendingMaintenanceAction"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class RestoreDBClusterFromS3Message(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
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
                "source_engine",
                "SourceEngine",
                TypeInfo(str),
            ),
            (
                "source_engine_version",
                "SourceEngineVersion",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_ingestion_role_arn",
                "S3IngestionRoleArn",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "character_set_name",
                "CharacterSetName",
                TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "db_cluster_parameter_group_name",
                "DBClusterParameterGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "s3_prefix",
                "S3Prefix",
                TypeInfo(str),
            ),
            (
                "backtrack_window",
                "BacktrackWindow",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the DB cluster to create from the source data in the Amazon S3
    # bucket. This parameter is isn't case-sensitive.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `my-cluster1`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database engine to be used for the restored DB cluster.

    # Valid Values: `aurora`, `aurora-postgresql`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the master user for the restored DB cluster.

    # Constraints:

    #   * Must be 1 to 16 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the master database user. This password can contain any
    # printable ASCII character except "/", """, or "@".

    # Constraints: Must contain from 8 to 41 characters.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the database engine that was backed up to create the
    # files stored in the Amazon S3 bucket.

    # Valid values: `mysql`
    source_engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the database that the backup files were created from.

    # MySQL version 5.5 and 5.6 are supported.

    # Example: `5.6.22`
    source_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon S3 bucket that contains the data used to create the
    # Amazon Aurora DB cluster.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS Identity and Access Management
    # (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on
    # your behalf.
    s3_ingestion_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of EC2 Availability Zones that instances in the restored DB cluster
    # can be created in.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which automated backups of the restored DB cluster
    # are retained. You must specify a minimum value of 1.

    # Default: 1

    # Constraints:

    #   * Must be a value from 1 to 35
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates that the restored DB cluster should be associated
    # with the specified CharacterSet.
    character_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database name for the restored DB cluster.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the DB cluster parameter group to associate with the restored
    # DB cluster. If this argument is omitted, `default.aurora5.6` is used.

    # Constraints:

    #   * If supplied, must match the name of an existing DBClusterParameterGroup.
    db_cluster_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of EC2 VPC security groups to associate with the restored DB
    # cluster.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DB subnet group to associate with the restored DB cluster.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the database engine to use.

    # **Aurora MySQL**

    # Example: `5.6.10a`

    # **Aurora PostgreSQL**

    # Example: `9.6.3`
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on which the instances in the restored DB cluster accept
    # connections.

    # Default: `3306`
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates that the restored DB cluster should be associated
    # with the specified option group.

    # Permanent options can't be removed from an option group. An option group
    # can't be removed from a DB cluster once it is associated with a DB cluster.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The daily time range during which automated backups are created if
    # automated backups are enabled using the `BackupRetentionPeriod` parameter.

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region. To see the time blocks available, see [
    # Adjusting the Preferred Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora)
    # in the _Amazon Aurora User Guide._

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # The default is a 30-minute window selected at random from an 8-hour block
    # of time for each AWS Region, occurring on a random day of the week. To see
    # the time blocks available, see [ Adjusting the Preferred Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora)
    # in the _Amazon Aurora User Guide._

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the restored DB cluster is encrypted.
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key identifier for an encrypted DB cluster.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are creating a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KM encryption key.

    # If the `StorageEncrypted` parameter is true, and you do not specify a value
    # for the `KmsKeyId` parameter, then Amazon RDS will use your default
    # encryption key. AWS KMS creates the default encryption key for your AWS
    # account. Your AWS account has a different default encryption key for each
    # AWS Region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The prefix for all of the file names that contain the data used to create
    # the Amazon Aurora DB cluster. If you do not specify a **SourceS3Prefix**
    # value, then the Amazon Aurora DB cluster is created by using all of the
    # files in the Amazon S3 bucket.
    s3_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target backtrack window, in seconds. To disable backtracking, set this
    # value to 0.

    # Default: 0

    # Constraints:

    #   * If specified, this value must be set to a number from 0 to 259,200 (72 hours).
    backtrack_window: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of logs that the restored DB cluster is to export to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon Aurora User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBClusterFromS3Result(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreDBClusterFromSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "snapshot_identifier",
                "SnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
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
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "backtrack_window",
                "BacktrackWindow",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "engine_mode",
                "EngineMode",
                TypeInfo(str),
            ),
            (
                "scaling_configuration",
                "ScalingConfiguration",
                TypeInfo(ScalingConfiguration),
            ),
        ]

    # The name of the DB cluster to create from the DB snapshot or DB cluster
    # snapshot. This parameter isn't case-sensitive.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-snapshot-id`
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the DB snapshot or DB cluster snapshot to restore from.

    # You can use either the name or the Amazon Resource Name (ARN) to specify a
    # DB cluster snapshot. However, you can use only the ARN to specify a DB
    # snapshot.

    # Constraints:

    #   * Must match the identifier of an existing Snapshot.
    snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database engine to use for the new DB cluster.

    # Default: The same as source

    # Constraint: Must be compatible with the engine of the source
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the list of EC2 Availability Zones that instances in the restored
    # DB cluster can be created in.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the database engine to use for the new DB cluster.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on which the new DB cluster accepts connections.

    # Constraints: Value must be `1150-65535`

    # Default: The same port as the original DB cluster.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the DB subnet group to use for the new DB cluster.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database name for the restored DB cluster.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the option group to use for the restored DB cluster.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of VPC security groups that the new DB cluster will belong to.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags to be assigned to the restored DB cluster.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key identifier to use when restoring an encrypted DB cluster
    # from a DB snapshot or DB cluster snapshot.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are restoring a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KMS encryption
    # key.

    # If you do not specify a value for the `KmsKeyId` parameter, then the
    # following will occur:

    #   * If the DB snapshot or DB cluster snapshot in `SnapshotIdentifier` is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.

    #   * If the DB snapshot or DB cluster snapshot in `SnapshotIdentifier` is not encrypted, then the restored DB cluster is not encrypted.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target backtrack window, in seconds. To disable backtracking, set this
    # value to 0.

    # Default: 0

    # Constraints:

    #   * If specified, this value must be set to a number from 0 to 259,200 (72 hours).
    backtrack_window: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of logs that the restored DB cluster is to export to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch Logs
    # ](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon Aurora User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DB engine mode of the DB cluster, either `provisioned` or `serverless`.
    engine_mode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For DB clusters in `serverless` DB engine mode, the scaling properties of
    # the DB cluster.
    scaling_configuration: "ScalingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBClusterFromSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreDBClusterToPointInTimeMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_cluster_identifier",
                "DBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "source_db_cluster_identifier",
                "SourceDBClusterIdentifier",
                TypeInfo(str),
            ),
            (
                "restore_type",
                "RestoreType",
                TypeInfo(str),
            ),
            (
                "restore_to_time",
                "RestoreToTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "use_latest_restorable_time",
                "UseLatestRestorableTime",
                TypeInfo(bool),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
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
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "backtrack_window",
                "BacktrackWindow",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the new DB cluster to be created.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    db_cluster_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the source DB cluster from which to restore.

    # Constraints:

    #   * Must match the identifier of an existing DBCluster.
    source_db_cluster_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of restore to be performed. You can specify one of the following
    # values:

    #   * `full-copy` \- The new DB cluster is restored as a full copy of the source DB cluster.

    #   * `copy-on-write` \- The new DB cluster is restored as a clone of the source DB cluster.

    # Constraints: You can't specify `copy-on-write` if the engine version of the
    # source DB cluster is earlier than 1.11.

    # If you don't specify a `RestoreType` value, then the new DB cluster is
    # restored as a full copy of the source DB cluster.
    restore_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time to restore the DB cluster to.

    # Valid Values: Value must be a time in Universal Coordinated Time (UTC)
    # format

    # Constraints:

    #   * Must be before the latest restorable time for the DB instance

    #   * Must be specified if `UseLatestRestorableTime` parameter is not provided

    #   * Cannot be specified if `UseLatestRestorableTime` parameter is true

    #   * Cannot be specified if `RestoreType` parameter is `copy-on-write`

    # Example: `2015-03-07T23:45:00Z`
    restore_to_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that is set to `true` to restore the DB cluster to the latest
    # restorable backup time, and `false` otherwise.

    # Default: `false`

    # Constraints: Cannot be specified if `RestoreToTime` parameter is provided.
    use_latest_restorable_time: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which the new DB cluster accepts connections.

    # Constraints: A value from `1150-65535`.

    # Default: The default port for the engine.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB subnet group name to use for the new DB cluster.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the option group for the new DB cluster.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of VPC security groups that the new DB cluster belongs to.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key identifier to use when restoring an encrypted DB cluster
    # from an encrypted DB cluster.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are restoring a DB cluster with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB cluster, then
    # you can use the KMS key alias instead of the ARN for the KMS encryption
    # key.

    # You can restore to a new DB cluster and encrypt the new DB cluster with a
    # KMS key that is different than the KMS key used to encrypt the source DB
    # cluster. The new DB cluster is encrypted with the KMS key identified by the
    # `KmsKeyId` parameter.

    # If you do not specify a value for the `KmsKeyId` parameter, then the
    # following will occur:

    #   * If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.

    #   * If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.

    # If `DBClusterIdentifier` refers to a DB cluster that is not encrypted, then
    # the restore request is rejected.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The target backtrack window, in seconds. To disable backtracking, set this
    # value to 0.

    # Default: 0

    # Constraints:

    #   * If specified, this value must be set to a number from 0 to 259,200 (72 hours).
    backtrack_window: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of logs that the restored DB cluster is to export to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon Aurora User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBClusterToPointInTimeResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_cluster",
                "DBCluster",
                TypeInfo(DBCluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB cluster.

    # This data type is used as a response element in the DescribeDBClusters
    # action.
    db_cluster: "DBCluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreDBInstanceFromDBSnapshotMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
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
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                TypeInfo(str),
            ),
            (
                "tde_credential_password",
                "TdeCredentialPassword",
                TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "domain_iam_role_name",
                "DomainIAMRoleName",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
            (
                "use_default_processor_features",
                "UseDefaultProcessorFeatures",
                TypeInfo(bool),
            ),
        ]

    # Name of the DB instance to create from the DB snapshot. This parameter
    # isn't case-sensitive.

    # Constraints:

    #   * Must contain from 1 to 63 numbers, letters, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens

    # Example: `my-snapshot-id`
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the DB snapshot to restore from.

    # Constraints:

    #   * Must match the identifier of an existing DBSnapshot.

    #   * If you are restoring from a shared manual DB snapshot, the `DBSnapshotIdentifier` must be the ARN of the shared DB snapshot.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute and memory capacity of the Amazon RDS DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions, or for all database engines. For the full list of DB instance
    # classes, and availability for your engine, see [DB Instance
    # Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
    # in the _Amazon RDS User Guide._

    # Default: The same DBInstanceClass as the original DB instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on which the database accepts connections.

    # Default: The same port as the original DB instance

    # Constraints: Value must be `1150-65535`
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 Availability Zone that the DB instance is created in.

    # Default: A random, system-chosen Availability Zone.

    # Constraint: You can't specify the AvailabilityZone parameter if the MultiAZ
    # parameter is set to `true`.

    # Example: `us-east-1a`
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB subnet group name to use for the new instance.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies if the DB instance is a Multi-AZ deployment.

    # Constraint: You can't specify the AvailabilityZone parameter if the MultiAZ
    # parameter is set to `true`.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the accessibility options for the DB instance. A value of true
    # specifies an Internet-facing instance with a publicly resolvable DNS name,
    # which resolves to a public IP address. A value of false specifies an
    # internal instance with a DNS name that resolves to a private IP address.
    # For more information, see CreateDBInstance.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that minor version upgrades are applied automatically to the DB
    # instance during the maintenance window.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # License model information for the restored DB instance.

    # Default: Same as source.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database name for the restored DB instance.

    # This parameter doesn't apply to the MySQL, PostgreSQL, or MariaDB engines.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database engine to use for the new instance.

    # Default: The same as source

    # Constraint: Must be compatible with the engine of the source. For example,
    # you can restore a MariaDB 10.1 DB instance from a MySQL 5.6 snapshot.

    # Valid Values:

    #   * `mariadb`

    #   * `mysql`

    #   * `oracle-ee`

    #   * `oracle-se2`

    #   * `oracle-se1`

    #   * `oracle-se`

    #   * `postgres`

    #   * `sqlserver-ee`

    #   * `sqlserver-se`

    #   * `sqlserver-ex`

    #   * `sqlserver-web`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the amount of provisioned IOPS for the DB instance, expressed in
    # I/O operations per second. If this parameter is not specified, the IOPS
    # value is taken from the backup. If this parameter is set to 0, the new
    # instance is converted to a non-PIOPS instance. The conversion takes
    # additional time, though your DB instance is available for connections
    # before the conversion starts.

    # The provisioned IOPS value must follow the requirements for your database
    # engine. For more information, see [Amazon RDS Provisioned IOPS Storage to
    # Improve
    # Performance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS)
    # in the _Amazon RDS User Guide._

    # Constraints: Must be an integer greater than 1000.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the option group to be used for the restored DB instance.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the storage type to be associated with the DB instance.

    # Valid values: `standard | gp2 | io1`

    # If you specify `io1`, you must also include a value for the `Iops`
    # parameter.

    # Default: `io1` if the `Iops` parameter is specified, otherwise `standard`
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the given ARN from the key store in order to access the
    # device.
    tde_credential_password: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify the Active Directory Domain to restore the instance in.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the restored DB instance to snapshots of the DB
    # instance, and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the name of the IAM role to be used when making API calls to the
    # Directory Service.
    domain_iam_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # You can enable IAM database authentication for the following database
    # engines

    #   * For MySQL 5.6, minor version 5.6.34 or higher

    #   * For MySQL 5.7, minor version 5.7.16 or higher

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of logs that the restored DB instance is to export to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon Aurora User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies that the DB instance class of the DB instance uses
    # its default processor features.
    use_default_processor_features: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBInstanceFromDBSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreDBInstanceFromS3Message(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "source_engine",
                "SourceEngine",
                TypeInfo(str),
            ),
            (
                "source_engine_version",
                "SourceEngineVersion",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_ingestion_role_arn",
                "S3IngestionRoleArn",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
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
                "db_security_groups",
                "DBSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_security_group_ids",
                "VpcSecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "db_parameter_group_name",
                "DBParameterGroupName",
                TypeInfo(str),
            ),
            (
                "backup_retention_period",
                "BackupRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "multi_az",
                "MultiAZ",
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
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "storage_encrypted",
                "StorageEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "monitoring_interval",
                "MonitoringInterval",
                TypeInfo(int),
            ),
            (
                "monitoring_role_arn",
                "MonitoringRoleArn",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "s3_prefix",
                "S3Prefix",
                TypeInfo(str),
            ),
            (
                "enable_performance_insights",
                "EnablePerformanceInsights",
                TypeInfo(bool),
            ),
            (
                "performance_insights_kms_key_id",
                "PerformanceInsightsKMSKeyId",
                TypeInfo(str),
            ),
            (
                "performance_insights_retention_period",
                "PerformanceInsightsRetentionPeriod",
                TypeInfo(int),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
            (
                "use_default_processor_features",
                "UseDefaultProcessorFeatures",
                TypeInfo(bool),
            ),
        ]

    # The DB instance identifier. This parameter is stored as a lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `mydbinstance`
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute and memory capacity of the DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions, or for all database engines. For the full list of DB instance
    # classes, and availability for your engine, see [DB Instance
    # Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
    # in the _Amazon RDS User Guide._

    # Importing from Amazon S3 is not supported on the db.t2.micro DB instance
    # class.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database engine to be used for this instance.

    # Valid Values: `mysql`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the engine of your source database.

    # Valid Values: `mysql`
    source_engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version of your source database.

    # Valid Values: `5.6`
    source_engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of your Amazon S3 bucket that contains your database backup file.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An AWS Identity and Access Management (IAM) role to allow Amazon RDS to
    # access your Amazon S3 bucket.
    s3_ingestion_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database to create when the DB instance is created. Follow
    # the naming rules specified in CreateDBInstance.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of storage (in gigabytes) to allocate initially for the DB
    # instance. Follow the allocation rules specified in CreateDBInstance.

    # Be sure to allocate enough memory for your new DB instance so that the
    # restore operation can succeed. You can also allocate additional memory for
    # future growth.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the master user.

    # Constraints:

    #   * Must be 1 to 16 letters or numbers.

    #   * First character must be a letter.

    #   * Cannot be a reserved word for the chosen database engine.
    master_username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the master user. The password can include any printable
    # ASCII character except "/", """, or "@".

    # Constraints: Must contain from 8 to 41 characters.
    master_user_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of DB security groups to associate with this DB instance.

    # Default: The default DB security group for the database engine.
    db_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of VPC security groups to associate with this DB instance.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zone that the DB instance is created in. For information
    # about AWS Regions and Availability Zones, see [Regions and Availability
    # Zones](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)
    # in the _Amazon RDS User Guide._

    # Default: A random, system-chosen Availability Zone in the endpoint's AWS
    # Region.

    # Example: `us-east-1d`

    # Constraint: The AvailabilityZone parameter can't be specified if the
    # MultiAZ parameter is set to `true`. The specified Availability Zone must be
    # in the same AWS Region as the current endpoint.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A DB subnet group to associate with this DB instance.
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time range each week during which system maintenance can occur, in
    # Universal Coordinated Time (UTC). For more information, see [Amazon RDS
    # Maintenance
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance)
    # in the _Amazon RDS User Guide._

    # Constraints:

    #   * Must be in the format `ddd:hh24:mi-ddd:hh24:mi`.

    #   * Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred backup window.

    #   * Must be at least 30 minutes.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the DB parameter group to associate with this DB instance. If
    # this argument is omitted, the default parameter group for the specified
    # engine is used.
    db_parameter_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days for which automated backups are retained. Setting this
    # parameter to a positive number enables backups. For more information, see
    # CreateDBInstance.
    backup_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time range each day during which automated backups are created if
    # automated backups are enabled. For more information, see [The Backup
    # Window](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow)
    # in the _Amazon RDS User Guide._

    # Constraints:

    #   * Must be in the format `hh24:mi-hh24:mi`.

    #   * Must be in Universal Coordinated Time (UTC).

    #   * Must not conflict with the preferred maintenance window.

    #   * Must be at least 30 minutes.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port number on which the database accepts connections.

    # Type: Integer

    # Valid Values: `1150`-`65535`

    # Default: `3306`
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the DB instance is a Multi-AZ deployment. If MultiAZ is
    # set to `true`, you can't set the AvailabilityZone parameter.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the database engine to use. Choose the latest minor
    # version of your database engine. For information about engine versions, see
    # CreateDBInstance, or call DescribeDBEngineVersions.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to indicate that minor engine upgrades are applied automatically to
    # the DB instance during the maintenance window, and otherwise false.

    # Default: `true`
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The license model for this DB instance. Use `general-public-license`.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of Provisioned IOPS (input/output operations per second) to
    # allocate initially for the DB instance. For information about valid Iops
    # values, see see [Amazon RDS Provisioned IOPS Storage to Improve
    # Performance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS)
    # in the _Amazon RDS User Guide._
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the option group to associate with this DB instance. If this
    # argument is omitted, the default option group for the specified engine is
    # used.
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the accessibility options for the DB instance. A value of true
    # specifies an Internet-facing instance with a publicly resolvable DNS name,
    # which resolves to a public IP address. A value of false specifies an
    # internal instance with a DNS name that resolves to a private IP address.
    # For more information, see CreateDBInstance.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to associate with this DB instance. For more information,
    # see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the storage type to be associated with the DB instance.

    # Valid values: `standard` | `gp2` | `io1`

    # If you specify `io1`, you must also include a value for the `Iops`
    # parameter.

    # Default: `io1` if the `Iops` parameter is specified; otherwise `standard`
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the new DB instance is encrypted or not.
    storage_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS KMS key identifier for an encrypted DB instance.

    # The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
    # encryption key. If you are creating a DB instance with the same AWS account
    # that owns the KMS encryption key used to encrypt the new DB instance, then
    # you can use the KMS key alias instead of the ARN for the KM encryption key.

    # If the `StorageEncrypted` parameter is true, and you do not specify a value
    # for the `KmsKeyId` parameter, then Amazon RDS will use your default
    # encryption key. AWS KMS creates the default encryption key for your AWS
    # account. Your AWS account has a different default encryption key for each
    # AWS Region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the DB instance to snapshots of the DB instance,
    # and otherwise false.

    # Default: false.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interval, in seconds, between points when Enhanced Monitoring metrics
    # are collected for the DB instance. To disable collecting Enhanced
    # Monitoring metrics, specify 0.

    # If `MonitoringRoleArn` is specified, then you must also set
    # `MonitoringInterval` to a value other than 0.

    # Valid Values: 0, 1, 5, 10, 15, 30, 60

    # Default: `0`
    monitoring_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the IAM role that permits RDS to send enhanced monitoring
    # metrics to Amazon CloudWatch Logs. For example,
    # `arn:aws:iam:123456789012:role/emaccess`. For information on creating a
    # monitoring role, see [Setting Up and Enabling Enhanced
    # Monitoring](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling)
    # in the _Amazon RDS User Guide._

    # If `MonitoringInterval` is set to a value other than 0, then you must
    # supply a `MonitoringRoleArn` value.
    monitoring_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The prefix of your Amazon S3 bucket.
    s3_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable Performance Insights for the DB instance, and otherwise
    # false.

    # For more information, see [Using Amazon Performance
    # Insights](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
    # in the _Amazon Relational Database Service User Guide_.
    enable_performance_insights: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS KMS key identifier for encryption of Performance Insights data. The
    # KMS key ID is the Amazon Resource Name (ARN), the KMS key identifier, or
    # the KMS key alias for the KMS encryption key.
    performance_insights_kms_key_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time, in days, to retain Performance Insights data. Valid
    # values are 7 or 731 (2 years).
    performance_insights_retention_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of logs that the restored DB instance is to export to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon RDS User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies that the DB instance class of the DB instance uses
    # its default processor features.
    use_default_processor_features: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBInstanceFromS3Result(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreDBInstanceToPointInTimeMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_db_instance_identifier",
                "SourceDBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "target_db_instance_identifier",
                "TargetDBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "restore_time",
                "RestoreTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "use_latest_restorable_time",
                "UseLatestRestorableTime",
                TypeInfo(bool),
            ),
            (
                "db_instance_class",
                "DBInstanceClass",
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
                "db_subnet_group_name",
                "DBSubnetGroupName",
                TypeInfo(str),
            ),
            (
                "multi_az",
                "MultiAZ",
                TypeInfo(bool),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "db_name",
                "DBName",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "iops",
                "Iops",
                TypeInfo(int),
            ),
            (
                "option_group_name",
                "OptionGroupName",
                TypeInfo(str),
            ),
            (
                "copy_tags_to_snapshot",
                "CopyTagsToSnapshot",
                TypeInfo(bool),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "tde_credential_arn",
                "TdeCredentialArn",
                TypeInfo(str),
            ),
            (
                "tde_credential_password",
                "TdeCredentialPassword",
                TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
            (
                "domain_iam_role_name",
                "DomainIAMRoleName",
                TypeInfo(str),
            ),
            (
                "enable_iam_database_authentication",
                "EnableIAMDatabaseAuthentication",
                TypeInfo(bool),
            ),
            (
                "enable_cloudwatch_logs_exports",
                "EnableCloudwatchLogsExports",
                TypeInfo(typing.List[str]),
            ),
            (
                "processor_features",
                "ProcessorFeatures",
                TypeInfo(typing.List[ProcessorFeature]),
            ),
            (
                "use_default_processor_features",
                "UseDefaultProcessorFeatures",
                TypeInfo(bool),
            ),
        ]

    # The identifier of the source DB instance from which to restore.

    # Constraints:

    #   * Must match the identifier of an existing DB instance.
    source_db_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the new DB instance to be created.

    # Constraints:

    #   * Must contain from 1 to 63 letters, numbers, or hyphens

    #   * First character must be a letter

    #   * Cannot end with a hyphen or contain two consecutive hyphens
    target_db_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time to restore from.

    # Valid Values: Value must be a time in Universal Coordinated Time (UTC)
    # format

    # Constraints:

    #   * Must be before the latest restorable time for the DB instance

    #   * Cannot be specified if UseLatestRestorableTime parameter is true

    # Example: `2009-09-07T23:45:00Z`
    restore_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether (`true`) or not (`false`) the DB instance is restored
    # from the latest backup time.

    # Default: `false`

    # Constraints: Cannot be specified if RestoreTime parameter is provided.
    use_latest_restorable_time: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compute and memory capacity of the Amazon RDS DB instance, for example,
    # `db.m4.large`. Not all DB instance classes are available in all AWS
    # Regions, or for all database engines. For the full list of DB instance
    # classes, and availability for your engine, see [DB Instance
    # Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
    # in the _Amazon RDS User Guide._

    # Default: The same DBInstanceClass as the original DB instance.
    db_instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on which the database accepts connections.

    # Constraints: Value must be `1150-65535`

    # Default: The same port as the original DB instance.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 Availability Zone that the DB instance is created in.

    # Default: A random, system-chosen Availability Zone.

    # Constraint: You can't specify the AvailabilityZone parameter if the MultiAZ
    # parameter is set to true.

    # Example: `us-east-1a`
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DB subnet group name to use for the new instance.

    # Constraints: If supplied, must match the name of an existing DBSubnetGroup.

    # Example: `mySubnetgroup`
    db_subnet_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies if the DB instance is a Multi-AZ deployment.

    # Constraint: You can't specify the AvailabilityZone parameter if the MultiAZ
    # parameter is set to `true`.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the accessibility options for the DB instance. A value of true
    # specifies an Internet-facing instance with a publicly resolvable DNS name,
    # which resolves to a public IP address. A value of false specifies an
    # internal instance with a DNS name that resolves to a private IP address.
    # For more information, see CreateDBInstance.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that minor version upgrades are applied automatically to the DB
    # instance during the maintenance window.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # License model information for the restored DB instance.

    # Default: Same as source.

    # Valid values: `license-included` | `bring-your-own-license` | `general-
    # public-license`
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database name for the restored DB instance.

    # This parameter is not used for the MySQL or MariaDB engines.
    db_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database engine to use for the new instance.

    # Default: The same as source

    # Constraint: Must be compatible with the engine of the source

    # Valid Values:

    #   * `mariadb`

    #   * `mysql`

    #   * `oracle-ee`

    #   * `oracle-se2`

    #   * `oracle-se1`

    #   * `oracle-se`

    #   * `postgres`

    #   * `sqlserver-ee`

    #   * `sqlserver-se`

    #   * `sqlserver-ex`

    #   * `sqlserver-web`
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of Provisioned IOPS (input/output operations per second) to be
    # initially allocated for the DB instance.

    # Constraints: Must be an integer greater than 1000.

    # **SQL Server**

    # Setting the IOPS value for the SQL Server database engine is not supported.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the option group to be used for the restored DB instance.

    # Permanent options, such as the TDE option for Oracle Advanced Security TDE,
    # can't be removed from an option group, and that option group can't be
    # removed from a DB instance once it is associated with a DB instance
    option_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to copy all tags from the restored DB instance to snapshots of the DB
    # instance, and otherwise false. The default is false.
    copy_tags_to_snapshot: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags. For more information, see [Tagging Amazon RDS
    # Resources](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)
    # in the _Amazon RDS User Guide._
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the storage type to be associated with the DB instance.

    # Valid values: `standard | gp2 | io1`

    # If you specify `io1`, you must also include a value for the `Iops`
    # parameter.

    # Default: `io1` if the `Iops` parameter is specified, otherwise `standard`
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN from the key store with which to associate the instance for TDE
    # encryption.
    tde_credential_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the given ARN from the key store in order to access the
    # device.
    tde_credential_password: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify the Active Directory Domain to restore the instance in.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the name of the IAM role to be used when making API calls to the
    # Directory Service.
    domain_iam_role_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to enable mapping of AWS Identity and Access Management (IAM) accounts
    # to database accounts, and otherwise false.

    # You can enable IAM database authentication for the following database
    # engines

    #   * For MySQL 5.6, minor version 5.6.34 or higher

    #   * For MySQL 5.7, minor version 5.7.16 or higher

    # Default: `false`
    enable_iam_database_authentication: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of logs that the restored DB instance is to export to CloudWatch
    # Logs. The values in the list depend on the DB engine being used. For more
    # information, see [Publishing Database Logs to Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch)
    # in the _Amazon RDS User Guide_.
    enable_cloudwatch_logs_exports: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of CPU cores and the number of threads per core for the DB
    # instance class of the DB instance.
    processor_features: typing.List["ProcessorFeature"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that specifies that the DB instance class of the DB instance uses
    # its default processor features.
    use_default_processor_features: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreDBInstanceToPointInTimeResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RevokeDBSecurityGroupIngressMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_security_group_name",
                "DBSecurityGroupName",
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
                "ec2_security_group_id",
                "EC2SecurityGroupId",
                TypeInfo(str),
            ),
            (
                "ec2_security_group_owner_id",
                "EC2SecurityGroupOwnerId",
                TypeInfo(str),
            ),
        ]

    # The name of the DB security group to revoke ingress from.
    db_security_group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP range to revoke access from. Must be a valid CIDR range. If `CIDRIP`
    # is specified, `EC2SecurityGroupName`, `EC2SecurityGroupId` and
    # `EC2SecurityGroupOwnerId` can't be provided.
    cidrip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the EC2 security group to revoke access from. For VPC DB
    # security groups, `EC2SecurityGroupId` must be provided. Otherwise,
    # EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or
    # `EC2SecurityGroupId` must be provided.
    ec2_security_group_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The id of the EC2 security group to revoke access from. For VPC DB security
    # groups, `EC2SecurityGroupId` must be provided. Otherwise,
    # EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or
    # `EC2SecurityGroupId` must be provided.
    ec2_security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Account Number of the owner of the EC2 security group specified in
    # the `EC2SecurityGroupName` parameter. The AWS Access Key ID is not an
    # acceptable value. For VPC DB security groups, `EC2SecurityGroupId` must be
    # provided. Otherwise, EC2SecurityGroupOwnerId and either
    # `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.
    ec2_security_group_owner_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevokeDBSecurityGroupIngressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_security_group",
                "DBSecurityGroup",
                TypeInfo(DBSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details for an Amazon RDS DB security group.

    # This data type is used as a response element in the
    # DescribeDBSecurityGroups action.
    db_security_group: "DBSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SNSInvalidTopicFault(ShapeBase):
    """
    SNS has responded that there is a problem with the SND topic specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SNSNoAuthorizationFault(ShapeBase):
    """
    You do not have permission to publish to the SNS topic ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SNSTopicArnNotFoundFault(ShapeBase):
    """
    The SNS topic ARN does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ScalingConfiguration(ShapeBase):
    """
    Contains the scaling configuration of an Aurora Serverless DB cluster.

    For more information, see [Using Amazon Aurora
    Serverless](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-
    serverless.html) in the _Amazon Aurora User Guide_.
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
            (
                "auto_pause",
                "AutoPause",
                TypeInfo(bool),
            ),
            (
                "seconds_until_auto_pause",
                "SecondsUntilAutoPause",
                TypeInfo(int),
            ),
        ]

    # The minimum capacity for an Aurora DB cluster in `serverless` DB engine
    # mode.

    # Valid capacity values are `2`, `4`, `8`, `16`, `32`, `64`, `128`, and
    # `256`.

    # The minimum capacity must be less than or equal to the maximum capacity.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum capacity for an Aurora DB cluster in `serverless` DB engine
    # mode.

    # Valid capacity values are `2`, `4`, `8`, `16`, `32`, `64`, `128`, and
    # `256`.

    # The maximum capacity must be greater than or equal to the minimum capacity.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that specifies whether to allow or disallow automatic pause for an
    # Aurora DB cluster in `serverless` DB engine mode. A DB cluster can be
    # paused only when it's idle (it has no connections).

    # If a DB cluster is paused for more than seven days, the DB cluster might be
    # backed up with a snapshot. In this case, the DB cluster is restored when
    # there is a request to connect to it.
    auto_pause: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in seconds, before an Aurora DB cluster in `serverless` mode is
    # paused.
    seconds_until_auto_pause: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScalingConfigurationInfo(ShapeBase):
    """
    Shows the scaling configuration for an Aurora DB cluster in `serverless` DB
    engine mode.

    For more information, see [Using Amazon Aurora
    Serverless](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-
    serverless.html) in the _Amazon Aurora User Guide_.
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
            (
                "auto_pause",
                "AutoPause",
                TypeInfo(bool),
            ),
            (
                "seconds_until_auto_pause",
                "SecondsUntilAutoPause",
                TypeInfo(int),
            ),
        ]

    # The maximum capacity for the Aurora DB cluster in `serverless` DB engine
    # mode.
    min_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum capacity for an Aurora DB cluster in `serverless` DB engine
    # mode.
    max_capacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates whether automatic pause is allowed for the Aurora DB
    # cluster in `serverless` DB engine mode.
    auto_pause: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The remaining amount of time, in seconds, before the Aurora DB cluster in
    # `serverless` mode is paused. A DB cluster can be paused only when it's idle
    # (it has no connections).
    seconds_until_auto_pause: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SharedSnapshotQuotaExceededFault(ShapeBase):
    """
    You have exceeded the maximum number of accounts that you can share a manual DB
    snapshot with.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SnapshotQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed number of DB
    snapshots.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SourceNotFoundFault(ShapeBase):
    """
    The requested source could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SourceRegion(ShapeBase):
    """
    Contains an AWS Region name as the result of a successful call to the
    DescribeSourceRegions action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The name of the source AWS Region.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint for the source AWS Region endpoint.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the source AWS Region.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SourceRegionMessage(OutputShapeBase):
    """
    Contains the result of a successful invocation of the DescribeSourceRegions
    action.
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
                "source_regions",
                "SourceRegions",
                TypeInfo(typing.List[SourceRegion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of SourceRegion instances that contains each source AWS Region that
    # the current AWS Region can get a Read Replica or a DB snapshot from.
    source_regions: typing.List["SourceRegion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SourceType(str):
    db_instance = "db-instance"
    db_parameter_group = "db-parameter-group"
    db_security_group = "db-security-group"
    db_snapshot = "db-snapshot"
    db_cluster = "db-cluster"
    db_cluster_snapshot = "db-cluster-snapshot"


@dataclasses.dataclass
class StartDBInstanceMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The user-supplied instance identifier.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartDBInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopDBInstanceMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "db_instance_identifier",
                "DBInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "db_snapshot_identifier",
                "DBSnapshotIdentifier",
                TypeInfo(str),
            ),
        ]

    # The user-supplied instance identifier.
    db_instance_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-supplied instance identifier of the DB Snapshot created
    # immediately before the DB instance is stopped.
    db_snapshot_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopDBInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "db_instance",
                "DBInstance",
                TypeInfo(DBInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of an Amazon RDS DB instance.

    # This data type is used as a response element in the DescribeDBInstances
    # action.
    db_instance: "DBInstance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StorageQuotaExceededFault(ShapeBase):
    """
    The request would result in the user exceeding the allowed amount of storage
    available across all DB instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StorageTypeNotSupportedFault(ShapeBase):
    """
    Storage of the _StorageType_ specified can't be associated with the DB instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Subnet(ShapeBase):
    """
    This data type is used as a response element in the DescribeDBSubnetGroups
    action.
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

    # Specifies the identifier of the subnet.
    subnet_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains Availability Zone information.

    # This data type is used as an element in the following data type:

    #   * OrderableDBInstanceOption
    subnet_availability_zone: "AvailabilityZone" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the status of the subnet.
    subnet_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetAlreadyInUse(ShapeBase):
    """
    The DB subnet is already in use in the Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionAlreadyExistFault(ShapeBase):
    """
    The supplied subscription name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionCategoryNotFoundFault(ShapeBase):
    """
    The supplied category does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SubscriptionNotFoundFault(ShapeBase):
    """
    The subscription name does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
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

    # A key is the required name of the tag. The string value can be from 1 to
    # 128 Unicode characters in length and can't be prefixed with "aws:" or
    # "rds:". The string can only contain only the set of Unicode letters,
    # digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value is the optional value of the tag. The string value can be from 1 to
    # 256 Unicode characters in length and can't be prefixed with "aws:" or
    # "rds:". The string can only contain only the set of Unicode letters,
    # digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagListMessage(OutputShapeBase):
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
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of tags returned by the ListTagsForResource operation.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Timezone(ShapeBase):
    """
    A time zone associated with a DBInstance or a DBSnapshot. This data type is an
    element in the response to the DescribeDBInstances, the DescribeDBSnapshots, and
    the DescribeDBEngineVersions actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timezone_name",
                "TimezoneName",
                TypeInfo(str),
            ),
        ]

    # The name of the time zone.
    timezone_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradeTarget(ShapeBase):
    """
    The version of the database engine that a DB instance can be upgraded to.
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
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "auto_upgrade",
                "AutoUpgrade",
                TypeInfo(bool),
            ),
            (
                "is_major_version_upgrade",
                "IsMajorVersionUpgrade",
                TypeInfo(bool),
            ),
        ]

    # The name of the upgrade target database engine.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the upgrade target database engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the database engine that a DB instance can be upgraded to.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates whether the target version is applied to any source
    # DB instances that have AutoMinorVersionUpgrade set to true.
    auto_upgrade: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates whether a database engine is upgraded to a major
    # version.
    is_major_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidDBInstanceModificationsMessage(ShapeBase):
    """
    Information about valid modifications that you can make to your DB instance.
    Contains the result of a successful call to the
    DescribeValidDBInstanceModifications action. You can use this information when
    you call ModifyDBInstance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage",
                "Storage",
                TypeInfo(typing.List[ValidStorageOptions]),
            ),
            (
                "valid_processor_features",
                "ValidProcessorFeatures",
                TypeInfo(typing.List[AvailableProcessorFeature]),
            ),
        ]

    # Valid storage options for your DB instance.
    storage: typing.List["ValidStorageOptions"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Valid processor features for your DB instance.
    valid_processor_features: typing.List["AvailableProcessorFeature"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class ValidStorageOptions(ShapeBase):
    """
    Information about valid modifications that you can make to your DB instance.
    Contains the result of a successful call to the
    DescribeValidDBInstanceModifications action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "storage_size",
                "StorageSize",
                TypeInfo(typing.List[Range]),
            ),
            (
                "provisioned_iops",
                "ProvisionedIops",
                TypeInfo(typing.List[Range]),
            ),
            (
                "iops_to_storage_ratio",
                "IopsToStorageRatio",
                TypeInfo(typing.List[DoubleRange]),
            ),
        ]

    # The valid storage types for your DB instance. For example, gp2, io1.
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid range of storage in gibibytes. For example, 100 to 16384.
    storage_size: typing.List["Range"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The valid range of provisioned IOPS. For example, 1000-20000.
    provisioned_iops: typing.List["Range"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The valid range of Provisioned IOPS to gibibytes of storage multiplier. For
    # example, 3-10, which means that provisioned IOPS can be between 3 and 10
    # times storage.
    iops_to_storage_ratio: typing.List["DoubleRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VpcSecurityGroupMembership(ShapeBase):
    """
    This data type is used as a response element for queries on VPC security group
    membership.
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

    # The name of the VPC security group.
    vpc_security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the VPC security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )
