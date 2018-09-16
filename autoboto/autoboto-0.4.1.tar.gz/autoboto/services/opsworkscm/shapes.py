import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccountAttribute(ShapeBase):
    """
    Stores account attributes.
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
                "maximum",
                "Maximum",
                TypeInfo(int),
            ),
            (
                "used",
                "Used",
                TypeInfo(int),
            ),
        ]

    # The attribute name. The following are supported attribute names.

    #   * _ServerLimit:_ The number of current servers/maximum number of servers allowed. By default, you can have a maximum of 10 servers.

    #   * _ManualBackupLimit:_ The number of current manual backups/maximum number of backups allowed. By default, you can have a maximum of 50 manual backups saved.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum allowed value.
    maximum: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current usage, such as the current number of servers that are
    # associated with the account.
    used: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateNodeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "node_name",
                "NodeName",
                TypeInfo(str),
            ),
            (
                "engine_attributes",
                "EngineAttributes",
                TypeInfo(typing.List[EngineAttribute]),
            ),
        ]

    # The name of the server with which to associate the node.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the node.
    node_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Engine attributes used for associating the node.

    # **Attributes accepted in a AssociateNode request for Chef**

    #   * `CHEF_ORGANIZATION`: The Chef organization with which the node is associated. By default only one organization named `default` can exist.

    #   * `CHEF_NODE_PUBLIC_KEY`: A PEM-formatted public key. This key is required for the `chef-client` agent to access the Chef API.

    # **Attributes accepted in a AssociateNode request for Puppet**

    #   * `PUPPET_NODE_CSR`: A PEM-formatted certificate-signing request (CSR) that is created by the node.
    engine_attributes: typing.List["EngineAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateNodeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "node_association_status_token",
                "NodeAssociationStatusToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains a token which can be passed to the `DescribeNodeAssociationStatus`
    # API call to get the status of the association request.
    node_association_status_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Backup(ShapeBase):
    """
    Describes a single backup.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_arn",
                "BackupArn",
                TypeInfo(str),
            ),
            (
                "backup_id",
                "BackupId",
                TypeInfo(str),
            ),
            (
                "backup_type",
                "BackupType",
                TypeInfo(typing.Union[str, BackupType]),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_model",
                "EngineModel",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "instance_profile_arn",
                "InstanceProfileArn",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "key_pair",
                "KeyPair",
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
                "s3_data_size",
                "S3DataSize",
                TypeInfo(int),
            ),
            (
                "s3_data_url",
                "S3DataUrl",
                TypeInfo(str),
            ),
            (
                "s3_log_url",
                "S3LogUrl",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, BackupStatus]),
            ),
            (
                "status_description",
                "StatusDescription",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "tools_version",
                "ToolsVersion",
                TypeInfo(str),
            ),
            (
                "user_arn",
                "UserArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the backup.
    backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The generated ID of the backup. Example: `myServerName-yyyyMMddHHmmssSSS`
    backup_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The backup type. Valid values are `automated` or `manual`.
    backup_type: typing.Union[str, "BackupType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp when the backup was created in the database. Example:
    # `2016-07-29T13:38:47.520Z`
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A user-provided description for a manual backup. This field is empty for
    # automated backups.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine type that is obtained from the server when the backup is
    # created.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine model that is obtained from the server when the backup is
    # created.
    engine_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version that is obtained from the server when the backup is
    # created.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 instance profile ARN that is obtained from the server when the
    # backup is created. Because this value is stored, you are not required to
    # provide the InstanceProfileArn again if you restore a backup.
    instance_profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type that is obtained from the server when the backup is
    # created.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key pair that is obtained from the server when the backup is created.
    key_pair: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The preferred backup period that is obtained from the server when the
    # backup is created.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The preferred maintenance period that is obtained from the server when the
    # backup is created.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is deprecated and is no longer used.
    s3_data_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is deprecated and is no longer used.
    s3_data_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 URL of the backup's log file.
    s3_log_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security group IDs that are obtained from the server when the backup is
    # created.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the server from which the backup was made.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service role ARN that is obtained from the server when the backup is
    # created.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of a backup while in progress.
    status: typing.Union[str, "BackupStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An informational message about backup status.
    status_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subnet IDs that are obtained from the server when the backup is
    # created.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of AWS OpsWorks CM-specific tools that is obtained from the
    # server when the backup is created.
    tools_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM user ARN of the requester for manual backups. This field is empty
    # for automated backups.
    user_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BackupStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    OK = "OK"
    FAILED = "FAILED"
    DELETING = "DELETING"


class BackupType(str):
    AUTOMATED = "AUTOMATED"
    MANUAL = "MANUAL"


@dataclasses.dataclass
class CreateBackupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The name of the server that you want to back up.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-defined description of the backup.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBackupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "backup",
                "Backup",
                TypeInfo(Backup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Backup created by request.
    backup: "Backup" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "instance_profile_arn",
                "InstanceProfileArn",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "associate_public_ip_address",
                "AssociatePublicIpAddress",
                TypeInfo(bool),
            ),
            (
                "disable_automated_backup",
                "DisableAutomatedBackup",
                TypeInfo(bool),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_model",
                "EngineModel",
                TypeInfo(str),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "engine_attributes",
                "EngineAttributes",
                TypeInfo(typing.List[EngineAttribute]),
            ),
            (
                "backup_retention_count",
                "BackupRetentionCount",
                TypeInfo(int),
            ),
            (
                "key_pair",
                "KeyPair",
                TypeInfo(str),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "backup_id",
                "BackupId",
                TypeInfo(str),
            ),
        ]

    # The name of the server. The server name must be unique within your AWS
    # account, within each region. Server names must start with a letter; then
    # letters, numbers, or hyphens (-) are allowed, up to a maximum of 40
    # characters.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the instance profile that your Amazon EC2 instances use.
    # Although the AWS OpsWorks console typically creates the instance profile
    # for you, if you are using API commands instead, run the service-role-
    # creation.yaml AWS CloudFormation template, located at
    # https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-
    # assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation
    # stack that includes the instance profile you need.
    instance_profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 instance type to use. For example, `m4.large`. Recommended
    # instance types include `t2.medium` and greater, `m4.*`, or `c4.xlarge` and
    # greater.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service role that the AWS OpsWorks CM service backend uses to work with
    # your account. Although the AWS OpsWorks management console typically
    # creates the service role for you, if you are using the AWS CLI or API
    # commands, run the service-role-creation.yaml AWS CloudFormation template,
    # located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-
    # assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation
    # stack that includes the service role and instance profile that you need.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Associate a public IP address with a server that you are launching. Valid
    # values are `true` or `false`. The default value is `true`.
    associate_public_ip_address: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable or disable scheduled backups. Valid values are `true` or `false`.
    # The default value is `true`.
    disable_automated_backup: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration management engine to use. Valid values include `Chef` and
    # `Puppet`.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine model of the server. Valid values in this release include
    # `Monolithic` for Puppet and `Single` for Chef.
    engine_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The major release version of the engine that you want to use. For a Chef
    # server, the valid value for EngineVersion is currently `12`. For a Puppet
    # server, the valid value is `2017`.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional engine attributes on a specified server.

    # **Attributes accepted in a Chef createServer request:**

    #   * `CHEF_PIVOTAL_KEY`: A base64-encoded RSA private key that is not stored by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. When no CHEF_PIVOTAL_KEY is set, one is generated and returned in the response.

    #   * `CHEF_DELIVERY_ADMIN_PASSWORD`: The password for the administrative user in the Chef Automate GUI. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_DELIVERY_ADMIN_PASSWORD is set, one is generated and returned in the response.

    # **Attributes accepted in a Puppet createServer request:**

    #   * `PUPPET_ADMIN_PASSWORD`: To work with the Puppet Enterprise console, a password must use ASCII characters.
    engine_attributes: typing.List["EngineAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of automated backups that you want to keep. Whenever a new
    # backup is created, AWS OpsWorks CM deletes the oldest backups if this
    # number is exceeded. The default value is `1`.
    backup_retention_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 key pair to set for the instance. This parameter is
    # optional; if desired, you may specify this parameter to connect to your
    # instances by using SSH.
    key_pair: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time for a one-hour period each week during which AWS OpsWorks CM
    # performs maintenance on the instance. Valid values must be specified in the
    # following format: `DDD:HH:MM`. The specified time is in coordinated
    # universal time (UTC). The default value is a random one-hour period on
    # Tuesday, Wednesday, or Friday. See `TimeWindowDefinition` for more
    # information.

    # **Example:** `Mon:08:00`, which represents a start time of every Monday at
    # 08:00 UTC. (8:00 a.m.)
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start time for a one-hour period during which AWS OpsWorks CM backs up
    # application-level data on your server if automated backups are enabled.
    # Valid values must be specified in one of the following formats:

    #   * `HH:MM` for daily backups

    #   * `DDD:HH:MM` for weekly backups

    # The specified time is in coordinated universal time (UTC). The default
    # value is a random, daily start time.

    # **Example:** `08:00`, which represents a daily start time of 08:00 UTC.

    # **Example:** `Mon:08:00`, which represents a start time of every Monday at
    # 08:00 UTC. (8:00 a.m.)
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security group IDs to attach to the Amazon EC2 instance. If you
    # add this parameter, the specified security groups must be within the VPC
    # that is specified by `SubnetIds`.

    # If you do not specify this parameter, AWS OpsWorks CM creates one new
    # security group that uses TCP ports 22 and 443, open to 0.0.0.0/0
    # (everyone).
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IDs of subnets in which to launch the server EC2 instance.

    # Amazon EC2-Classic customers: This field is required. All servers must run
    # within a VPC. The VPC must have "Auto Assign Public IP" enabled.

    # EC2-VPC customers: This field is optional. If you do not specify subnet
    # IDs, your EC2 instances are created in a default subnet that is selected by
    # Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign
    # Public IP" enabled.

    # For more information about supported Amazon EC2 platforms, see [Supported
    # Platforms](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-
    # platforms.html).
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you specify this field, AWS OpsWorks CM creates the server by using the
    # backup represented by BackupId.
    backup_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server",
                "Server",
                TypeInfo(Server),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The server that is created by the request.
    server: "Server" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBackupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_id",
                "BackupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the backup to delete. Run the DescribeBackups command to get a
    # list of backup IDs. Backup IDs are in the format `ServerName-
    # yyyyMMddHHmmssSSS`.
    backup_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBackupResponse(OutputShapeBase):
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
class DeleteServerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
        ]

    # The ID of the server to delete.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServerResponse(OutputShapeBase):
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
class DescribeAccountAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeAccountAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AccountAttribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes that are currently set for the account.
    attributes: typing.List["AccountAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeBackupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_id",
                "BackupId",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # Describes a single backup.
    backup_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns backups for the server with the specified ServerName.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is not currently implemented for `DescribeBackups` requests.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is not currently implemented for `DescribeBackups` requests.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBackupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "backups",
                "Backups",
                TypeInfo(typing.List[Backup]),
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

    # Contains the response to a `DescribeBackups` request.
    backups: typing.List["Backup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is not currently implemented for `DescribeBackups` requests.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # The name of the server for which you want to view events.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # NextToken is a string that is returned in some command responses. It
    # indicates that not all entries have been returned, and that you must run at
    # least one more request to get remaining items. To get remaining results,
    # call `DescribeEvents` again, and assign the token from the previous results
    # as the value of the `nextToken` parameter. If there are no more results,
    # the response object's `nextToken` parameter value is `null`. Setting a
    # `nextToken` value that was not returned in your previous results causes an
    # `InvalidNextTokenException` to occur.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # To receive a paginated response, use this parameter to specify the maximum
    # number of results to be returned with a single call. If the number of
    # available results exceeds this maximum, the response includes a `NextToken`
    # value that you can assign to the `NextToken` request parameter to get the
    # next set of results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_events",
                "ServerEvents",
                TypeInfo(typing.List[ServerEvent]),
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

    # Contains the response to a `DescribeEvents` request.
    server_events: typing.List["ServerEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # NextToken is a string that is returned in some command responses. It
    # indicates that not all entries have been returned, and that you must run at
    # least one more request to get remaining items. To get remaining results,
    # call `DescribeEvents` again, and assign the token from the previous results
    # as the value of the `nextToken` parameter. If there are no more results,
    # the response object's `nextToken` parameter value is `null`. Setting a
    # `nextToken` value that was not returned in your previous results causes an
    # `InvalidNextTokenException` to occur.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNodeAssociationStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "node_association_status_token",
                "NodeAssociationStatusToken",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
        ]

    # The token returned in either the AssociateNodeResponse or the
    # DisassociateNodeResponse.
    node_association_status_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the server from which to disassociate the node.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNodeAssociationStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "node_association_status",
                "NodeAssociationStatus",
                TypeInfo(typing.Union[str, NodeAssociationStatus]),
            ),
            (
                "engine_attributes",
                "EngineAttributes",
                TypeInfo(typing.List[EngineAttribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the association or disassociation request.

    # **Possible values:**

    #   * `SUCCESS`: The association or disassociation succeeded.

    #   * `FAILED`: The association or disassociation failed.

    #   * `IN_PROGRESS`: The association or disassociation is still in progress.
    node_association_status: typing.Union[str, "NodeAssociationStatus"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Attributes specific to the node association. In Puppet, the attibute
    # PUPPET_NODE_CERT contains the signed certificate (the result of the CSR).
    engine_attributes: typing.List["EngineAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeServersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # Describes the server with the specified ServerName.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is not currently implemented for `DescribeServers` requests.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is not currently implemented for `DescribeServers` requests.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "servers",
                "Servers",
                TypeInfo(typing.List[Server]),
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

    # Contains the response to a `DescribeServers` request.

    # _For Puppet Server:_ `DescribeServersResponse$Servers$EngineAttributes`
    # contains PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is
    # used by the Puppet API over TCP port number 8140. The CA certificate is
    # also used to sign node certificates.
    servers: typing.List["Server"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is not currently implemented for `DescribeServers` requests.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateNodeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "node_name",
                "NodeName",
                TypeInfo(str),
            ),
            (
                "engine_attributes",
                "EngineAttributes",
                TypeInfo(typing.List[EngineAttribute]),
            ),
        ]

    # The name of the server from which to disassociate the node.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the client node.
    node_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Engine attributes that are used for disassociating the node. No attributes
    # are required for Puppet.

    # **Attributes required in a DisassociateNode request for Chef**

    #   * `CHEF_ORGANIZATION`: The Chef organization with which the node was associated. By default only one organization named `default` can exist.
    engine_attributes: typing.List["EngineAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateNodeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "node_association_status_token",
                "NodeAssociationStatusToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains a token which can be passed to the `DescribeNodeAssociationStatus`
    # API call to get the status of the disassociation request.
    node_association_status_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EngineAttribute(ShapeBase):
    """
    A name and value pair that is specific to the engine of the server.
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

    # The name of the engine attribute.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the engine attribute.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    This occurs when the provided nextToken is not valid.
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

    # Error or informational message that can contain more detail about a
    # nextToken failure.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidStateException(ShapeBase):
    """
    The resource is in a state that does not allow you to perform a specified
    action.
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

    # Error or informational message that provides more detail if a resource is
    # in a state that is not valid for performing a specified action.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    The limit of servers or backups has been reached.
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

    # Error or informational message that the maximum allowed number of servers
    # or backups has been exceeded.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MaintenanceStatus(str):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class NodeAssociationStatus(str):
    """
    The status of the association or disassociation request.

    **Possible values:**

      * `SUCCESS`: The association or disassociation succeeded. 

      * `FAILED`: The association or disassociation failed. 

      * `IN_PROGRESS`: The association or disassociation is still in progress.
    """
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    The requested resource cannot be created because it already exists.
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

    # Error or informational message in response to a CreateServer request that a
    # resource cannot be created because it already exists.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The requested resource does not exist, or access was denied.
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

    # Error or informational message that can contain more detail about problems
    # locating or accessing a resource.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreServerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_id",
                "BackupId",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "key_pair",
                "KeyPair",
                TypeInfo(str),
            ),
        ]

    # The ID of the backup that you want to use to restore a server.
    backup_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the server that you want to restore.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the instance to create. Valid values must be specified in the
    # following format: `^([cm][34]|t2).*` For example, `m4.large`. Valid values
    # are `t2.medium`, `m4.large`, and `m4.2xlarge`. If you do not specify this
    # parameter, RestoreServer uses the instance type from the specified backup.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the key pair to set on the new EC2 instance. This can be
    # helpful if the administrator no longer has the SSH key.
    key_pair: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreServerResponse(OutputShapeBase):
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
class Server(ShapeBase):
    """
    Describes a configuration management server.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "associate_public_ip_address",
                "AssociatePublicIpAddress",
                TypeInfo(bool),
            ),
            (
                "backup_retention_count",
                "BackupRetentionCount",
                TypeInfo(int),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "cloud_formation_stack_arn",
                "CloudFormationStackArn",
                TypeInfo(str),
            ),
            (
                "disable_automated_backup",
                "DisableAutomatedBackup",
                TypeInfo(bool),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "engine",
                "Engine",
                TypeInfo(str),
            ),
            (
                "engine_model",
                "EngineModel",
                TypeInfo(str),
            ),
            (
                "engine_attributes",
                "EngineAttributes",
                TypeInfo(typing.List[EngineAttribute]),
            ),
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "instance_profile_arn",
                "InstanceProfileArn",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "key_pair",
                "KeyPair",
                TypeInfo(str),
            ),
            (
                "maintenance_status",
                "MaintenanceStatus",
                TypeInfo(typing.Union[str, MaintenanceStatus]),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "service_role_arn",
                "ServiceRoleArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ServerStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "server_arn",
                "ServerArn",
                TypeInfo(str),
            ),
        ]

    # Associate a public IP address with a server that you are launching.
    associate_public_ip_address: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of automated backups to keep.
    backup_retention_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the server.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time stamp of server creation. Example `2016-07-29T13:38:47.520Z`
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the CloudFormation stack that was used to create the server.
    cloud_formation_stack_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Disables automated backups. The number of stored backups is dependent on
    # the value of PreferredBackupCount.
    disable_automated_backup: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DNS name that can be used to access the engine. Example: `myserver-
    # asdfghjkl.us-east-1.opsworks.io`
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine type of the server. Valid values in this release include `Chef`
    # and `Puppet`.
    engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine model of the server. Valid values in this release include
    # `Monolithic` for Puppet and `Single` for Chef.
    engine_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The response of a createServer() request returns the master credential to
    # access the server in EngineAttributes. These credentials are not stored by
    # AWS OpsWorks CM; they are returned only as part of the result of
    # createServer().

    # **Attributes returned in a createServer response for Chef**

    #   * `CHEF_PIVOTAL_KEY`: A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.

    #   * `CHEF_STARTER_KIT`: A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands.

    # **Attributes returned in a createServer response for Puppet**

    #   * `PUPPET_STARTER_KIT`: A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents.

    #   * `PUPPET_ADMIN_PASSWORD`: An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.
    engine_attributes: typing.List["EngineAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The engine version of the server. For a Chef server, the valid value for
    # EngineVersion is currently `12`. For a Puppet server, the valid value is
    # `2017`.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance profile ARN of the server.
    instance_profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance type for the server, as specified in the CloudFormation stack.
    # This might not be the same instance type that is shown in the EC2 console.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key pair associated with the server.
    key_pair: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the most recent server maintenance run. Shows `SUCCESS` or
    # `FAILED`.
    maintenance_status: typing.Union[str, "MaintenanceStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The preferred maintenance period specified for the server.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The preferred backup period specified for the server.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The security group IDs for the server, as specified in the CloudFormation
    # stack. These might not be the same security groups that are shown in the
    # EC2 console.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service role ARN used to create the server.
    service_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The server's status. This field displays the states of actions in progress,
    # such as creating, running, or backing up the server, as well as the
    # server's health state.
    status: typing.Union[str, "ServerStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Depending on the server status, this field has either a human-readable
    # message (such as a create or backup error), or an escaped block of JSON
    # (used for health check results).
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subnet IDs specified in a CreateServer request.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the server.
    server_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerEvent(ShapeBase):
    """
    An event that is related to the server, such as the start of maintenance or
    backup.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "log_url",
                "LogUrl",
                TypeInfo(str),
            ),
        ]

    # The time when the event occurred.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the server on or for which the event occurred.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A human-readable informational or status message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 URL of the event's log file.
    log_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ServerStatus(str):
    BACKING_UP = "BACKING_UP"
    CONNECTION_LOST = "CONNECTION_LOST"
    CREATING = "CREATING"
    DELETING = "DELETING"
    MODIFYING = "MODIFYING"
    FAILED = "FAILED"
    HEALTHY = "HEALTHY"
    RUNNING = "RUNNING"
    RESTORING = "RESTORING"
    SETUP = "SETUP"
    UNDER_MAINTENANCE = "UNDER_MAINTENANCE"
    UNHEALTHY = "UNHEALTHY"
    TERMINATED = "TERMINATED"


@dataclasses.dataclass
class StartMaintenanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "engine_attributes",
                "EngineAttributes",
                TypeInfo(typing.List[EngineAttribute]),
            ),
        ]

    # The name of the server on which to run maintenance.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Engine attributes that are specific to the server on which you want to run
    # maintenance.
    engine_attributes: typing.List["EngineAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartMaintenanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server",
                "Server",
                TypeInfo(Server),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the response to a `StartMaintenance` request.
    server: "Server" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateServerEngineAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                TypeInfo(str),
            ),
        ]

    # The name of the server to update.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the engine attribute to update.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value to set for the attribute.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateServerEngineAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server",
                "Server",
                TypeInfo(Server),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the response to an `UpdateServerEngineAttributes` request.
    server: "Server" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateServerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "disable_automated_backup",
                "DisableAutomatedBackup",
                TypeInfo(bool),
            ),
            (
                "backup_retention_count",
                "BackupRetentionCount",
                TypeInfo(int),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "preferred_backup_window",
                "PreferredBackupWindow",
                TypeInfo(str),
            ),
        ]

    # The name of the server to update.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Setting DisableAutomatedBackup to `true` disables automated or scheduled
    # backups. Automated backups are enabled by default.
    disable_automated_backup: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the number of automated backups that you want to keep.
    backup_retention_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # `DDD:HH:MM` (weekly start time) or `HH:MM` (daily start time).

    # Time windows always use coordinated universal time (UTC). Valid strings for
    # day of week (`DDD`) are: `Mon`, `Tue`, `Wed`, `Thr`, `Fri`, `Sat`, or
    # `Sun`.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # `DDD:HH:MM` (weekly start time) or `HH:MM` (daily start time).

    # Time windows always use coordinated universal time (UTC). Valid strings for
    # day of week (`DDD`) are: `Mon`, `Tue`, `Wed`, `Thr`, `Fri`, `Sat`, or
    # `Sun`.
    preferred_backup_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateServerResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server",
                "Server",
                TypeInfo(Server),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the response to a `UpdateServer` request.
    server: "Server" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    One or more of the provided request parameters are not valid.
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

    # Error or informational message that can contain more detail about a
    # validation failure.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
