import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccessDeniedFault(ShapeBase):
    """
    AWS DMS was denied access to the endpoint.
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
class AccountQuota(ShapeBase):
    """
    Describes a quota for an AWS account, for example, the number of replication
    instances allowed.
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

    # The name of the AWS DMS quota for this AWS account.
    account_quota_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount currently used toward the quota maximum.
    used: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum allowed value for the quota.
    max: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsToResourceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be
    # added to. AWS DMS resources include a replication instance, endpoint, and a
    # replication task.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag to be assigned to the DMS resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsToResourceResponse(OutputShapeBase):
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AuthMechanismValue(str):
    default = "default"
    mongodb_cr = "mongodb_cr"
    scram_sha_1 = "scram_sha_1"


class AuthTypeValue(str):
    no = "no"
    password = "password"


@dataclasses.dataclass
class AvailabilityZone(ShapeBase):
    """

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

    # The name of the availability zone.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Certificate(ShapeBase):
    """
    The SSL certificate that can be used to encrypt connections between the
    endpoints and the replication instance.
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
                "certificate_creation_date",
                "CertificateCreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "certificate_pem",
                "CertificatePem",
                TypeInfo(str),
            ),
            (
                "certificate_wallet",
                "CertificateWallet",
                TypeInfo(typing.Any),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "certificate_owner",
                "CertificateOwner",
                TypeInfo(str),
            ),
            (
                "valid_from_date",
                "ValidFromDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "valid_to_date",
                "ValidToDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "signing_algorithm",
                "SigningAlgorithm",
                TypeInfo(str),
            ),
            (
                "key_length",
                "KeyLength",
                TypeInfo(int),
            ),
        ]

    # The customer-assigned name of the certificate. Valid characters are A-z and
    # 0-9.
    certificate_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the certificate was created.
    certificate_creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The contents of the .pem X.509 certificate file for the certificate.
    certificate_pem: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the imported Oracle Wallet certificate for use with SSL.
    certificate_wallet: typing.Any = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the certificate.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the certificate.
    certificate_owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The beginning date that the certificate is valid.
    valid_from_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The final date that the certificate is valid.
    valid_to_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The signing algorithm for the certificate.
    signing_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key length of the cryptographic algorithm being used.
    key_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class CertificateWallet(botocore.response.StreamingBody):
    pass


class CompressionTypeValue(str):
    none = "none"
    gzip = "gzip"


@dataclasses.dataclass
class Connection(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "last_failure_message",
                "LastFailureMessage",
                TypeInfo(str),
            ),
            (
                "endpoint_identifier",
                "EndpointIdentifier",
                TypeInfo(str),
            ),
            (
                "replication_instance_identifier",
                "ReplicationInstanceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The connection status.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message when the connection last failed.
    last_failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the endpoint. Identifiers must begin with a letter; must
    # contain only ASCII letters, digits, and hyphens; and must not end with a
    # hyphen or contain two consecutive hyphens.
    endpoint_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replication instance identifier. This parameter is stored as a
    # lowercase string.
    replication_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateEndpointMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_identifier",
                "EndpointIdentifier",
                TypeInfo(str),
            ),
            (
                "endpoint_type",
                "EndpointType",
                TypeInfo(typing.Union[str, ReplicationEndpointTypeValue]),
            ),
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "extra_connection_attributes",
                "ExtraConnectionAttributes",
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
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "ssl_mode",
                "SslMode",
                TypeInfo(typing.Union[str, DmsSslModeValue]),
            ),
            (
                "service_access_role_arn",
                "ServiceAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "external_table_definition",
                "ExternalTableDefinition",
                TypeInfo(str),
            ),
            (
                "dynamo_db_settings",
                "DynamoDbSettings",
                TypeInfo(DynamoDbSettings),
            ),
            (
                "s3_settings",
                "S3Settings",
                TypeInfo(S3Settings),
            ),
            (
                "dms_transfer_settings",
                "DmsTransferSettings",
                TypeInfo(DmsTransferSettings),
            ),
            (
                "mongo_db_settings",
                "MongoDbSettings",
                TypeInfo(MongoDbSettings),
            ),
        ]

    # The database endpoint identifier. Identifiers must begin with a letter;
    # must contain only ASCII letters, digits, and hyphens; and must not end with
    # a hyphen or contain two consecutive hyphens.
    endpoint_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of endpoint.
    endpoint_type: typing.Union[str, "ReplicationEndpointTypeValue"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The type of engine for the endpoint. Valid values, depending on the
    # EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-
    # postgresql, redshift, s3, db2, azuredb, sybase, dynamodb, mongodb, and
    # sqlserver.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name to be used to login to the endpoint database.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password to be used to login to the endpoint database.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the server where the endpoint database resides.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port used by the endpoint database.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the endpoint database.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional attributes associated with the connection.
    extra_connection_attributes: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The KMS key identifier that will be used to encrypt the connection
    # parameters. If you do not specify a value for the KmsKeyId parameter, then
    # AWS DMS will use your default encryption key. AWS KMS creates the default
    # encryption key for your AWS account. Your AWS account has a different
    # default encryption key for each AWS region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Tags to be added to the endpoint.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the certificate.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSL mode to use for the SSL connection.

    # SSL mode can be one of four values: none, require, verify-ca, verify-full.

    # The default value is none.
    ssl_mode: typing.Union[str, "DmsSslModeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the service access role you want to use
    # to create the endpoint.
    service_access_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The external table definition.
    external_table_definition: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings in JSON format for the target Amazon DynamoDB endpoint. For more
    # information about the available settings, see the **Using Object Mapping to
    # Migrate Data to DynamoDB** section at [ Using an Amazon DynamoDB Database
    # as a Target for AWS Database Migration
    # Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html).
    dynamo_db_settings: "DynamoDbSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings in JSON format for the target Amazon S3 endpoint. For more
    # information about the available settings, see the **Extra Connection
    # Attributes** section at [ Using Amazon S3 as a Target for AWS Database
    # Migration
    # Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html).
    s3_settings: "S3Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The settings in JSON format for the DMS Transfer type source endpoint.

    # Attributes include:

    #   * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.

    #   * bucketName - The name of the S3 bucket to use.

    #   * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed.

    # Shorthand syntax: ServiceAccessRoleArn=string
    # ,BucketName=string,CompressionType=string

    # JSON syntax:

    # { "ServiceAccessRoleArn": "string", "BucketName": "string",
    # "CompressionType": "none"|"gzip" }
    dms_transfer_settings: "DmsTransferSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings in JSON format for the source MongoDB endpoint. For more
    # information about the available settings, see the **Configuration
    # Properties When Using MongoDB as a Source for AWS Database Migration
    # Service** section at [ Using MongoDB as a Target for AWS Database Migration
    # Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html).
    mongo_db_settings: "MongoDbSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateEndpointResponse(OutputShapeBase):
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
                "endpoint",
                "Endpoint",
                TypeInfo(Endpoint),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint that was created.
    endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )


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

    # The name of the AWS DMS event notification subscription.

    # Constraints: The name must be less than 255 characters.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic created for event
    # notification. The ARN is created by Amazon SNS when you create a topic and
    # subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS DMS resource that generates the events. For example, if you
    # want to be notified of events generated by a replication instance, you set
    # this parameter to `replication-instance`. If this value is not specified,
    # all events are returned.

    # Valid values: replication-instance | migration-task
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories for a source type that you want to subscribe to.
    # You can see a list of the categories for a given source type by calling the
    # **DescribeEventCategories** action or in the topic [ Working with Events
    # and
    # Notifications](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)
    # in the AWS Database Migration Service User Guide.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of identifiers of the event sources for which events will be
    # returned. If not specified, then all sources are included in the response.
    # An identifier must begin with a letter and must contain only ASCII letters,
    # digits, and hyphens; it cannot end with a hyphen or contain two consecutive
    # hyphens.
    source_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value; set to **true** to activate the subscription, or set to
    # **false** to create the subscription but not activate it.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A tag to be attached to the event subscription.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEventSubscriptionResponse(OutputShapeBase):
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
                "event_subscription",
                "EventSubscription",
                TypeInfo(EventSubscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The event subscription that was created.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReplicationInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_identifier",
                "ReplicationInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "replication_instance_class",
                "ReplicationInstanceClass",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
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
                "replication_subnet_group_identifier",
                "ReplicationSubnetGroupIdentifier",
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
                "auto_minor_version_upgrade",
                "AutoMinorVersionUpgrade",
                TypeInfo(bool),
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
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
        ]

    # The replication instance identifier. This parameter is stored as a
    # lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `myrepinstance`
    replication_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compute and memory capacity of the replication instance as specified by
    # the replication instance class.

    # Valid Values: `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
    # dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge `
    replication_instance_class: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of storage (in gigabytes) to be initially allocated for the
    # replication instance.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the VPC security group to be used with the replication instance.
    # The VPC security group must work with the VPC containing the replication
    # instance.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 Availability Zone that the replication instance will be created in.

    # Default: A random, system-chosen Availability Zone in the endpoint's
    # region.

    # Example: `us-east-1d`
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subnet group to associate with the replication instance.
    replication_subnet_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range during which system maintenance can occur, in
    # Universal Coordinated Time (UTC).

    # Format: `ddd:hh24:mi-ddd:hh24:mi`

    # Default: A 30-minute window selected at random from an 8-hour block of time
    # per region, occurring on a random day of the week.

    # Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

    # Constraints: Minimum 30-minute window.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies if the replication instance is a Multi-AZ deployment. You cannot
    # set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to
    # `true`.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version number of the replication instance.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that minor engine upgrades will be applied automatically to the
    # replication instance during the maintenance window.

    # Default: `true`
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Tags to be associated with the replication instance.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The KMS key identifier that will be used to encrypt the content on the
    # replication instance. If you do not specify a value for the KmsKeyId
    # parameter, then AWS DMS will use your default encryption key. AWS KMS
    # creates the default encryption key for your AWS account. Your AWS account
    # has a different default encryption key for each AWS region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the accessibility options for the replication instance. A value
    # of `true` represents an instance with a public IP address. A value of
    # `false` represents an instance with a private IP address. The default value
    # is `true`.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReplicationInstanceResponse(OutputShapeBase):
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
                "replication_instance",
                "ReplicationInstance",
                TypeInfo(ReplicationInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication instance that was created.
    replication_instance: "ReplicationInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReplicationSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_subnet_group_identifier",
                "ReplicationSubnetGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "replication_subnet_group_description",
                "ReplicationSubnetGroupDescription",
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

    # The name for the replication subnet group. This value is stored as a
    # lowercase string.

    # Constraints: Must contain no more than 255 alphanumeric characters,
    # periods, spaces, underscores, or hyphens. Must not be "default".

    # Example: `mySubnetgroup`
    replication_subnet_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description for the subnet group.
    replication_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The EC2 subnet IDs for the subnet group.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag to be assigned to the subnet group.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReplicationSubnetGroupResponse(OutputShapeBase):
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
                "replication_subnet_group",
                "ReplicationSubnetGroup",
                TypeInfo(ReplicationSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication subnet group that was created.
    replication_subnet_group: "ReplicationSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReplicationTaskMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_identifier",
                "ReplicationTaskIdentifier",
                TypeInfo(str),
            ),
            (
                "source_endpoint_arn",
                "SourceEndpointArn",
                TypeInfo(str),
            ),
            (
                "target_endpoint_arn",
                "TargetEndpointArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "migration_type",
                "MigrationType",
                TypeInfo(typing.Union[str, MigrationTypeValue]),
            ),
            (
                "table_mappings",
                "TableMappings",
                TypeInfo(str),
            ),
            (
                "replication_task_settings",
                "ReplicationTaskSettings",
                TypeInfo(str),
            ),
            (
                "cdc_start_time",
                "CdcStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "cdc_start_position",
                "CdcStartPosition",
                TypeInfo(str),
            ),
            (
                "cdc_stop_position",
                "CdcStopPosition",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The replication task identifier.

    # Constraints:

    #   * Must contain from 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    replication_task_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    source_endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    target_endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The migration type.
    migration_type: typing.Union[str, "MigrationTypeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When using the AWS CLI or boto3, provide the path of the JSON file that
    # contains the table mappings. Precede the path with "file://". When working
    # with the DMS API, provide the JSON as the parameter value.

    # For example, --table-mappings file://mappingfile.json
    table_mappings: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for the task, such as target metadata settings. For a complete
    # list of task settings, see [Task Settings for AWS Database Migration
    # Service
    # Tasks](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).
    replication_task_settings: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the start time for a change data capture (CDC) operation. Use
    # either CdcStartTime or CdcStartPosition to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
    cdc_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when you want a change data capture (CDC) operation to start. Use
    # either CdcStartPosition or CdcStartTime to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # The value can be in date, checkpoint, or LSN/SCN format.

    # Date Example: --cdc-start-position “2018-03-08T12:12:12”

    # Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-
    # changelog.157832:1975:-1:2002:677883278264080:mysql-bin-
    # changelog.157832:1876#0#0#*#0#93"

    # LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
    cdc_start_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates when you want a change data capture (CDC) operation to stop. The
    # value can be either server time or commit time.

    # Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

    # Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12
    # “
    cdc_stop_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Tags to be added to the replication instance.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReplicationTaskResponse(OutputShapeBase):
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
                "replication_task",
                "ReplicationTask",
                TypeInfo(ReplicationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication task that was created.
    replication_task: "ReplicationTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCertificateMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the deleted certificate.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCertificateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(Certificate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Secure Sockets Layer (SSL) certificate.
    certificate: "Certificate" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEndpointMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEndpointResponse(OutputShapeBase):
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
                "endpoint",
                "Endpoint",
                TypeInfo(Endpoint),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint that was deleted.
    endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )


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

    # The name of the DMS event notification subscription to be deleted.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEventSubscriptionResponse(OutputShapeBase):
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
                "event_subscription",
                "EventSubscription",
                TypeInfo(EventSubscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The event subscription that was deleted.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication instance to be deleted.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationInstanceResponse(OutputShapeBase):
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
                "replication_instance",
                "ReplicationInstance",
                TypeInfo(ReplicationInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication instance that was deleted.
    replication_instance: "ReplicationInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_subnet_group_identifier",
                "ReplicationSubnetGroupIdentifier",
                TypeInfo(str),
            ),
        ]

    # The subnet group name of the replication instance.
    replication_subnet_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationSubnetGroupResponse(OutputShapeBase):
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicationTaskMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication task to be deleted.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReplicationTaskResponse(OutputShapeBase):
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
                "replication_task",
                "ReplicationTask",
                TypeInfo(ReplicationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The deleted replication task.
    replication_task: "ReplicationTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAccountAttributesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeAccountAttributesResponse(OutputShapeBase):
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
                "account_quotas",
                "AccountQuotas",
                TypeInfo(typing.List[AccountQuota]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Account quota information.
    account_quotas: typing.List["AccountQuota"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCertificatesMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Filters applied to the certificate described in the form of key-value
    # pairs.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 10
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCertificatesResponse(OutputShapeBase):
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
                "certificates",
                "Certificates",
                TypeInfo(typing.List[Certificate]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Secure Sockets Layer (SSL) certificates associated with the replication
    # instance.
    certificates: typing.List["Certificate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeCertificatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeConnectionsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # The filters applied to the connection.

    # Valid filter names: endpoint-arn | replication-instance-arn
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
class DescribeConnectionsResponse(OutputShapeBase):
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
                "connections",
                "Connections",
                TypeInfo(typing.List[Connection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the connections.
    connections: typing.List["Connection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeConnectionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEndpointTypesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Filters applied to the describe action.

    # Valid filter names: engine-name | endpoint-type
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
class DescribeEndpointTypesResponse(OutputShapeBase):
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
                "supported_endpoint_types",
                "SupportedEndpointTypes",
                TypeInfo(typing.List[SupportedEndpointType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of endpoints that are supported.
    supported_endpoint_types: typing.List["SupportedEndpointType"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    def paginate(
        self,
    ) -> typing.Generator["DescribeEndpointTypesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEndpointsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Filters applied to the describe action.

    # Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-
    # name
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
class DescribeEndpointsResponse(OutputShapeBase):
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
                "endpoints",
                "Endpoints",
                TypeInfo(typing.List[Endpoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Endpoint description.
    endpoints: typing.List["Endpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DescribeEndpointsResponse", None, None]:
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

    # The type of AWS DMS resource that generates events.

    # Valid values: replication-instance | migration-task
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters applied to the action.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEventCategoriesResponse(OutputShapeBase):
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
                "event_category_group_list",
                "EventCategoryGroupList",
                TypeInfo(typing.List[EventCategoryGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event categories.
    event_category_group_list: typing.List["EventCategoryGroup"
                                          ] = dataclasses.field(
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

    # The name of the AWS DMS event subscription to be described.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters applied to the action.
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
class DescribeEventSubscriptionsResponse(OutputShapeBase):
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

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event subscriptions.
    event_subscriptions_list: typing.List["EventSubscription"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    def paginate(
        self,
    ) -> typing.Generator["DescribeEventSubscriptionsResponse", None, None]:
        yield from super()._paginate()


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

    # The identifier of the event source. An identifier must begin with a letter
    # and must contain only ASCII letters, digits, and hyphens. It cannot end
    # with a hyphen or contain two consecutive hyphens.
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS DMS resource that generates events.

    # Valid values: replication-instance | migration-task
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start time for the events to be listed.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time for the events to be listed.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the events to be listed.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories for a source type that you want to subscribe to.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters applied to the action.
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
class DescribeEventsResponse(OutputShapeBase):
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

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The events described.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DescribeEventsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeOrderableReplicationInstancesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
class DescribeOrderableReplicationInstancesResponse(OutputShapeBase):
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
                "orderable_replication_instances",
                "OrderableReplicationInstances",
                TypeInfo(typing.List[OrderableReplicationInstance]),
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

    # The order-able replication instances available.
    orderable_replication_instances: typing.List["OrderableReplicationInstance"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator[
        "DescribeOrderableReplicationInstancesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeRefreshSchemasStatusMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeRefreshSchemasStatusResponse(OutputShapeBase):
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
                "refresh_schemas_status",
                "RefreshSchemasStatus",
                TypeInfo(RefreshSchemasStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the schema.
    refresh_schemas_status: "RefreshSchemasStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeReplicationInstanceTaskLogsMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
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

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
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
class DescribeReplicationInstanceTaskLogsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_task_logs",
                "ReplicationInstanceTaskLogs",
                TypeInfo(typing.List[ReplicationInstanceTaskLog]),
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

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of replication task log metadata. Each member of the array
    # contains the replication task name, ARN, and task log size (in bytes).
    replication_instance_task_logs: typing.List["ReplicationInstanceTaskLog"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReplicationInstancesMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Filters applied to the describe action.

    # Valid filter names: replication-instance-arn | replication-instance-id |
    # replication-instance-class | engine-version
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
class DescribeReplicationInstancesResponse(OutputShapeBase):
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
                "replication_instances",
                "ReplicationInstances",
                TypeInfo(typing.List[ReplicationInstance]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replication instances described.
    replication_instances: typing.List["ReplicationInstance"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    def paginate(
        self,
    ) -> typing.Generator["DescribeReplicationInstancesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeReplicationSubnetGroupsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Filters applied to the describe action.
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
class DescribeReplicationSubnetGroupsResponse(OutputShapeBase):
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
                "replication_subnet_groups",
                "ReplicationSubnetGroups",
                TypeInfo(typing.List[ReplicationSubnetGroup]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the replication subnet groups.
    replication_subnet_groups: typing.List["ReplicationSubnetGroup"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    def paginate(self, ) -> typing.Generator[
        "DescribeReplicationSubnetGroupsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeReplicationTaskAssessmentResultsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
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

    # \- The Amazon Resource Name (ARN) string that uniquely identifies the task.
    # When this input parameter is specified the API will return only one result
    # and ignore the values of the max-records and marker parameters.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

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
class DescribeReplicationTaskAssessmentResultsResponse(OutputShapeBase):
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
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "replication_task_assessment_results",
                "ReplicationTaskAssessmentResults",
                TypeInfo(typing.List[ReplicationTaskAssessmentResult]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # \- The Amazon S3 bucket where the task assessment report is located.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task assessment report.
    replication_task_assessment_results: typing.List[
        "ReplicationTaskAssessmentResult"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    def paginate(self, ) -> typing.Generator[
        "DescribeReplicationTaskAssessmentResultsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeReplicationTasksMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # Filters applied to the describe action.

    # Valid filter names: replication-task-arn | replication-task-id | migration-
    # type | endpoint-arn | replication-instance-arn
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
class DescribeReplicationTasksResponse(OutputShapeBase):
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
                "replication_tasks",
                "ReplicationTasks",
                TypeInfo(typing.List[ReplicationTask]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the replication tasks.
    replication_tasks: typing.List["ReplicationTask"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["DescribeReplicationTasksResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeSchemasMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
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

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

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
class DescribeSchemasResponse(OutputShapeBase):
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
                "schemas",
                "Schemas",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The described schema.
    schemas: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeSchemasResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeTableStatisticsMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
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

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of records to include in the response. If more records
    # exist than the specified `MaxRecords` value, a pagination token called a
    # marker is included in the response so that the remaining results can be
    # retrieved.

    # Default: 100

    # Constraints: Minimum 20, maximum 500.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters applied to the describe table statistics action.

    # Valid filter names: schema-name | table-name | table-state

    # A combination of filters creates an AND condition where each record matches
    # all specified filters.
    filters: typing.List["Filter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTableStatisticsResponse(OutputShapeBase):
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
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "table_statistics",
                "TableStatistics",
                TypeInfo(typing.List[TableStatistics]),
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

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The table statistics.
    table_statistics: typing.List["TableStatistics"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # marker, up to the value specified by `MaxRecords`.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeTableStatisticsResponse", None, None]:
        yield from super()._paginate()


class DmsSslModeValue(str):
    none = "none"
    require = "require"
    verify_ca = "verify-ca"
    verify_full = "verify-full"


@dataclasses.dataclass
class DmsTransferSettings(ShapeBase):
    """
    The settings in JSON format for the DMS Transfer type source endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_access_role_arn",
                "ServiceAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
        ]

    # The IAM role that has permission to access the Amazon S3 bucket.
    service_access_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the S3 bucket to use.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DynamoDbSettings(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_access_role_arn",
                "ServiceAccessRoleArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) used by the service access IAM role.
    service_access_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_identifier",
                "EndpointIdentifier",
                TypeInfo(str),
            ),
            (
                "endpoint_type",
                "EndpointType",
                TypeInfo(typing.Union[str, ReplicationEndpointTypeValue]),
            ),
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "engine_display_name",
                "EngineDisplayName",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "extra_connection_attributes",
                "ExtraConnectionAttributes",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "ssl_mode",
                "SslMode",
                TypeInfo(typing.Union[str, DmsSslModeValue]),
            ),
            (
                "service_access_role_arn",
                "ServiceAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "external_table_definition",
                "ExternalTableDefinition",
                TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "dynamo_db_settings",
                "DynamoDbSettings",
                TypeInfo(DynamoDbSettings),
            ),
            (
                "s3_settings",
                "S3Settings",
                TypeInfo(S3Settings),
            ),
            (
                "dms_transfer_settings",
                "DmsTransferSettings",
                TypeInfo(DmsTransferSettings),
            ),
            (
                "mongo_db_settings",
                "MongoDbSettings",
                TypeInfo(MongoDbSettings),
            ),
        ]

    # The database endpoint identifier. Identifiers must begin with a letter;
    # must contain only ASCII letters, digits, and hyphens; and must not end with
    # a hyphen or contain two consecutive hyphens.
    endpoint_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of endpoint.
    endpoint_type: typing.Union[str, "ReplicationEndpointTypeValue"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The database engine name. Valid values, depending on the EndPointType,
    # include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql,
    # redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb, and
    # sqlserver.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The expanded name for the engine name. For example, if the `EngineName`
    # parameter is "aurora," this value would be "Amazon Aurora MySQL."
    engine_display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name used to connect to the endpoint.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the server at the endpoint.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port value used to access the endpoint.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the database at the endpoint.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional connection attributes used to connect to the endpoint.
    extra_connection_attributes: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the endpoint.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The KMS key identifier that will be used to encrypt the connection
    # parameters. If you do not specify a value for the KmsKeyId parameter, then
    # AWS DMS will use your default encryption key. AWS KMS creates the default
    # encryption key for your AWS account. Your AWS account has a different
    # default encryption key for each AWS region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) used for SSL connection to the endpoint.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSL mode used to connect to the endpoint.

    # SSL mode can be one of four values: none, require, verify-ca, verify-full.

    # The default value is none.
    ssl_mode: typing.Union[str, "DmsSslModeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) used by the service access IAM role.
    service_access_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The external table definition.
    external_table_definition: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Value returned by a call to CreateEndpoint that can be used for cross-
    # account validation. Use it on a subsequent call to CreateEndpoint to create
    # the endpoint with a cross-account.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The settings for the target DynamoDB database. For more information, see
    # the `DynamoDBSettings` structure.
    dynamo_db_settings: "DynamoDbSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The settings for the S3 target endpoint. For more information, see the
    # `S3Settings` structure.
    s3_settings: "S3Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The settings in JSON format for the DMS Transfer type source endpoint.

    # Attributes include:

    #   * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.

    #   * bucketName - The name of the S3 bucket to use.

    #   * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed.

    # Shorthand syntax: ServiceAccessRoleArn=string
    # ,BucketName=string,CompressionType=string

    # JSON syntax:

    # { "ServiceAccessRoleArn": "string", "BucketName": "string",
    # "CompressionType": "none"|"gzip" }
    dms_transfer_settings: "DmsTransferSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The settings for the MongoDB source endpoint. For more information, see the
    # `MongoDbSettings` structure.
    mongo_db_settings: "MongoDbSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Event(ShapeBase):
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
        ]

    # The identifier of the event source. An identifier must begin with a letter
    # and must contain only ASCII letters, digits, and hyphens; it cannot end
    # with a hyphen or contain two consecutive hyphens.

    # Constraints:replication instance, endpoint, migration task
    source_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS DMS resource that generates events.

    # Valid values: replication-instance | endpoint | migration-task
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The event message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event categories available for the specified source type.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date of the event.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventCategoryGroup(ShapeBase):
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
                "event_categories",
                "EventCategories",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The type of AWS DMS resource that generates events.

    # Valid values: replication-instance | replication-server | security-group |
    # migration-task
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories for a `SourceType` that you want to subscribe
    # to.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventSubscription(ShapeBase):
    """

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
        ]

    # The AWS customer account associated with the AWS DMS event notification
    # subscription.
    customer_aws_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS DMS event notification subscription Id.
    cust_subscription_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The topic ARN of the AWS DMS event notification subscription.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the AWS DMS event notification subscription.

    # Constraints:

    # Can be one of the following: creating | modifying | deleting | active | no-
    # permission | topic-not-exist

    # The status "no-permission" indicates that AWS DMS no longer has permission
    # to post to the SNS topic. The status "topic-not-exist" indicates that the
    # topic was deleted after the subscription was created.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the RDS event notification subscription was created.
    subscription_creation_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of AWS DMS resource that generates events.

    # Valid values: replication-instance | replication-server | security-group |
    # migration-task
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of source Ids for the event subscription.
    source_ids_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A lists of event categories.
    event_categories_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Boolean value that indicates if the event subscription is enabled.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Filter(ShapeBase):
    """

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

    # The name of the filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The filter value.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportCertificateMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_identifier",
                "CertificateIdentifier",
                TypeInfo(str),
            ),
            (
                "certificate_pem",
                "CertificatePem",
                TypeInfo(str),
            ),
            (
                "certificate_wallet",
                "CertificateWallet",
                TypeInfo(typing.Any),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The customer-assigned name of the certificate. Valid characters are A-z and
    # 0-9.
    certificate_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of the .pem X.509 certificate file for the certificate.
    certificate_pem: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the imported Oracle Wallet certificate for use with SSL.
    certificate_wallet: typing.Any = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags associated with the certificate.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportCertificateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(Certificate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The certificate to be uploaded.
    certificate: "Certificate" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InsufficientResourceCapacityFault(ShapeBase):
    """
    There are not enough resources allocated to the database migration.
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
class InvalidCertificateFault(ShapeBase):
    """
    The certificate was not valid.
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
class InvalidResourceStateFault(ShapeBase):
    """
    The resource is in a state that prevents it from being used for database
    migration.
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
class InvalidSubnet(ShapeBase):
    """
    The subnet provided is invalid.
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
class KMSKeyNotAccessibleFault(ShapeBase):
    """
    AWS DMS cannot access the KMS key.
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
class ListTagsForResourceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) string that uniquely identifies the AWS DMS
    # resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(OutputShapeBase):
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

    # A list of tags for the resource.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class MigrationTypeValue(str):
    full_load = "full-load"
    cdc = "cdc"
    full_load_and_cdc = "full-load-and-cdc"


@dataclasses.dataclass
class ModifyEndpointMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "endpoint_identifier",
                "EndpointIdentifier",
                TypeInfo(str),
            ),
            (
                "endpoint_type",
                "EndpointType",
                TypeInfo(typing.Union[str, ReplicationEndpointTypeValue]),
            ),
            (
                "engine_name",
                "EngineName",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "extra_connection_attributes",
                "ExtraConnectionAttributes",
                TypeInfo(str),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "ssl_mode",
                "SslMode",
                TypeInfo(typing.Union[str, DmsSslModeValue]),
            ),
            (
                "service_access_role_arn",
                "ServiceAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "external_table_definition",
                "ExternalTableDefinition",
                TypeInfo(str),
            ),
            (
                "dynamo_db_settings",
                "DynamoDbSettings",
                TypeInfo(DynamoDbSettings),
            ),
            (
                "s3_settings",
                "S3Settings",
                TypeInfo(S3Settings),
            ),
            (
                "dms_transfer_settings",
                "DmsTransferSettings",
                TypeInfo(DmsTransferSettings),
            ),
            (
                "mongo_db_settings",
                "MongoDbSettings",
                TypeInfo(MongoDbSettings),
            ),
        ]

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database endpoint identifier. Identifiers must begin with a letter;
    # must contain only ASCII letters, digits, and hyphens; and must not end with
    # a hyphen or contain two consecutive hyphens.
    endpoint_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of endpoint.
    endpoint_type: typing.Union[str, "ReplicationEndpointTypeValue"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The type of engine for the endpoint. Valid values, depending on the
    # EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-
    # postgresql, redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb,
    # and sqlserver.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name to be used to login to the endpoint database.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password to be used to login to the endpoint database.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the server where the endpoint database resides.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port used by the endpoint database.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the endpoint database.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional attributes associated with the connection. To reset this
    # parameter, pass the empty string ("") as an argument.
    extra_connection_attributes: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the certificate used for SSL connection.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSL mode to be used.

    # SSL mode can be one of four values: none, require, verify-ca, verify-full.

    # The default value is none.
    ssl_mode: typing.Union[str, "DmsSslModeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) for the service access role you want to use
    # to modify the endpoint.
    service_access_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The external table definition.
    external_table_definition: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings in JSON format for the target Amazon DynamoDB endpoint. For more
    # information about the available settings, see the **Using Object Mapping to
    # Migrate Data to DynamoDB** section at [ Using an Amazon DynamoDB Database
    # as a Target for AWS Database Migration
    # Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html).
    dynamo_db_settings: "DynamoDbSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings in JSON format for the target S3 endpoint. For more information
    # about the available settings, see the **Extra Connection Attributes**
    # section at [ Using Amazon S3 as a Target for AWS Database Migration
    # Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html).
    s3_settings: "S3Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The settings in JSON format for the DMS Transfer type source endpoint.

    # Attributes include:

    #   * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.

    #   * BucketName - The name of the S3 bucket to use.

    #   * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed.

    # Shorthand syntax: ServiceAccessRoleArn=string
    # ,BucketName=string,CompressionType=string

    # JSON syntax:

    # { "ServiceAccessRoleArn": "string", "BucketName": "string",
    # "CompressionType": "none"|"gzip" }
    dms_transfer_settings: "DmsTransferSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings in JSON format for the source MongoDB endpoint. For more
    # information about the available settings, see the **Configuration
    # Properties When Using MongoDB as a Source for AWS Database Migration
    # Service** section at [ Using Amazon S3 as a Target for AWS Database
    # Migration
    # Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html).
    mongo_db_settings: "MongoDbSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyEndpointResponse(OutputShapeBase):
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
                "endpoint",
                "Endpoint",
                TypeInfo(Endpoint),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The modified endpoint.
    endpoint: "Endpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )


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

    # The name of the AWS DMS event notification subscription to be modified.
    subscription_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic created for event
    # notification. The ARN is created by Amazon SNS when you create a topic and
    # subscribe to it.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS DMS resource that generates the events you want to
    # subscribe to.

    # Valid values: replication-instance | migration-task
    source_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event categories for a source type that you want to subscribe to.
    # Use the `DescribeEventCategories` action to see a list of event categories.
    event_categories: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value; set to **true** to activate the subscription.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyEventSubscriptionResponse(OutputShapeBase):
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
                "event_subscription",
                "EventSubscription",
                TypeInfo(EventSubscription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The modified event subscription.
    event_subscription: "EventSubscription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationInstanceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
                TypeInfo(int),
            ),
            (
                "apply_immediately",
                "ApplyImmediately",
                TypeInfo(bool),
            ),
            (
                "replication_instance_class",
                "ReplicationInstanceClass",
                TypeInfo(str),
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
                "replication_instance_identifier",
                "ReplicationInstanceIdentifier",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of storage (in gigabytes) to be allocated for the replication
    # instance.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the changes should be applied immediately or during the
    # next maintenance window.
    apply_immediately: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute and memory capacity of the replication instance.

    # Valid Values: `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
    # dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge `
    replication_instance_class: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the VPC security group to be used with the replication instance.
    # The VPC security group must work with the VPC containing the replication
    # instance.
    vpc_security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weekly time range (in UTC) during which system maintenance can occur,
    # which might result in an outage. Changing this parameter does not result in
    # an outage, except in the following situation, and the change is
    # asynchronously applied as soon as possible. If moving this window to the
    # current time, there must be at least 30 minutes between the current time
    # and end of the window to ensure pending changes are applied.

    # Default: Uses existing setting

    # Format: ddd:hh24:mi-ddd:hh24:mi

    # Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

    # Constraints: Must be at least 30 minutes
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies if the replication instance is a Multi-AZ deployment. You cannot
    # set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to
    # `true`.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version number of the replication instance.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that major version upgrades are allowed. Changing this parameter
    # does not result in an outage and the change is asynchronously applied as
    # soon as possible.

    # Constraints: This parameter must be set to true when specifying a value for
    # the `EngineVersion` parameter that is a different major version than the
    # replication instance's current version.
    allow_major_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates that minor version upgrades will be applied automatically to the
    # replication instance during the maintenance window. Changing this parameter
    # does not result in an outage except in the following case and the change is
    # asynchronously applied as soon as possible. An outage will result if this
    # parameter is set to `true` during the maintenance window, and a newer minor
    # version is available, and AWS DMS has enabled auto patching for that engine
    # version.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication instance identifier. This parameter is stored as a
    # lowercase string.
    replication_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationInstanceResponse(OutputShapeBase):
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
                "replication_instance",
                "ReplicationInstance",
                TypeInfo(ReplicationInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The modified replication instance.
    replication_instance: "ReplicationInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationSubnetGroupMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_subnet_group_identifier",
                "ReplicationSubnetGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "replication_subnet_group_description",
                "ReplicationSubnetGroupDescription",
                TypeInfo(str),
            ),
        ]

    # The name of the replication instance subnet group.
    replication_subnet_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of subnet IDs.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the replication instance subnet group.
    replication_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationSubnetGroupResponse(OutputShapeBase):
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
                "replication_subnet_group",
                "ReplicationSubnetGroup",
                TypeInfo(ReplicationSubnetGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The modified replication subnet group.
    replication_subnet_group: "ReplicationSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyReplicationTaskMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "replication_task_identifier",
                "ReplicationTaskIdentifier",
                TypeInfo(str),
            ),
            (
                "migration_type",
                "MigrationType",
                TypeInfo(typing.Union[str, MigrationTypeValue]),
            ),
            (
                "table_mappings",
                "TableMappings",
                TypeInfo(str),
            ),
            (
                "replication_task_settings",
                "ReplicationTaskSettings",
                TypeInfo(str),
            ),
            (
                "cdc_start_time",
                "CdcStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "cdc_start_position",
                "CdcStartPosition",
                TypeInfo(str),
            ),
            (
                "cdc_stop_position",
                "CdcStopPosition",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replication task identifier.

    # Constraints:

    #   * Must contain from 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    replication_task_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The migration type.

    # Valid values: full-load | cdc | full-load-and-cdc
    migration_type: typing.Union[str, "MigrationTypeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When using the AWS CLI or boto3, provide the path of the JSON file that
    # contains the table mappings. Precede the path with "file://". When working
    # with the DMS API, provide the JSON as the parameter value.

    # For example, --table-mappings file://mappingfile.json
    table_mappings: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JSON file that contains settings for the task, such as target metadata
    # settings.
    replication_task_settings: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the start time for a change data capture (CDC) operation. Use
    # either CdcStartTime or CdcStartPosition to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
    cdc_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when you want a change data capture (CDC) operation to start. Use
    # either CdcStartPosition or CdcStartTime to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # The value can be in date, checkpoint, or LSN/SCN format.

    # Date Example: --cdc-start-position “2018-03-08T12:12:12”

    # Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-
    # changelog.157832:1975:-1:2002:677883278264080:mysql-bin-
    # changelog.157832:1876#0#0#*#0#93"

    # LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
    cdc_start_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates when you want a change data capture (CDC) operation to stop. The
    # value can be either server time or commit time.

    # Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

    # Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12
    # “
    cdc_stop_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyReplicationTaskResponse(OutputShapeBase):
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
                "replication_task",
                "ReplicationTask",
                TypeInfo(ReplicationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication task that was modified.
    replication_task: "ReplicationTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MongoDbSettings(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "server_name",
                "ServerName",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "database_name",
                "DatabaseName",
                TypeInfo(str),
            ),
            (
                "auth_type",
                "AuthType",
                TypeInfo(typing.Union[str, AuthTypeValue]),
            ),
            (
                "auth_mechanism",
                "AuthMechanism",
                TypeInfo(typing.Union[str, AuthMechanismValue]),
            ),
            (
                "nesting_level",
                "NestingLevel",
                TypeInfo(typing.Union[str, NestingLevelValue]),
            ),
            (
                "extract_doc_id",
                "ExtractDocId",
                TypeInfo(str),
            ),
            (
                "docs_to_investigate",
                "DocsToInvestigate",
                TypeInfo(str),
            ),
            (
                "auth_source",
                "AuthSource",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The user name you use to access the MongoDB source endpoint.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the user account you use to access the MongoDB source
    # endpoint.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the server on the MongoDB source endpoint.
    server_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port value for the MongoDB source endpoint.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database name on the MongoDB source endpoint.
    database_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication type you use to access the MongoDB source endpoint.

    # Valid values: NO, PASSWORD

    # When NO is selected, user name and password parameters are not used and can
    # be empty.
    auth_type: typing.Union[str, "AuthTypeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authentication mechanism you use to access the MongoDB source endpoint.

    # Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

    # DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x,
    # use SCRAM_SHA_1. This attribute is not used when authType=No.
    auth_mechanism: typing.Union[str, "AuthMechanismValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies either document or table mode.

    # Valid values: NONE, ONE

    # Default value is NONE. Specify NONE to use document mode. Specify ONE to
    # use table mode.
    nesting_level: typing.Union[str, "NestingLevelValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the document ID. Use this attribute when `NestingLevel` is set to
    # NONE.

    # Default value is false.
    extract_doc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the number of documents to preview to determine the document
    # organization. Use this attribute when `NestingLevel` is set to ONE.

    # Must be a positive value greater than 0. Default value is 1000.
    docs_to_investigate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MongoDB database name. This attribute is not used when `authType=NO`.

    # The default is admin.
    auth_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The KMS key identifier that will be used to encrypt the connection
    # parameters. If you do not specify a value for the KmsKeyId parameter, then
    # AWS DMS will use your default encryption key. AWS KMS creates the default
    # encryption key for your AWS account. Your AWS account has a different
    # default encryption key for each AWS region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class NestingLevelValue(str):
    none = "none"
    one = "one"


@dataclasses.dataclass
class OrderableReplicationInstance(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "engine_version",
                "EngineVersion",
                TypeInfo(str),
            ),
            (
                "replication_instance_class",
                "ReplicationInstanceClass",
                TypeInfo(str),
            ),
            (
                "storage_type",
                "StorageType",
                TypeInfo(str),
            ),
            (
                "min_allocated_storage",
                "MinAllocatedStorage",
                TypeInfo(int),
            ),
            (
                "max_allocated_storage",
                "MaxAllocatedStorage",
                TypeInfo(int),
            ),
            (
                "default_allocated_storage",
                "DefaultAllocatedStorage",
                TypeInfo(int),
            ),
            (
                "included_allocated_storage",
                "IncludedAllocatedStorage",
                TypeInfo(int),
            ),
        ]

    # The version of the replication engine.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute and memory capacity of the replication instance.

    # Valid Values: `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
    # dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge `
    replication_instance_class: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of storage used by the replication instance.
    storage_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum amount of storage (in gigabytes) that can be allocated for the
    # replication instance.
    min_allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum amount of storage (in gigabytes) that can be allocated for the
    # replication instance.
    max_allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default amount of storage (in gigabytes) that is allocated for the
    # replication instance.
    default_allocated_storage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of storage (in gigabytes) that is allocated for the replication
    # instance.
    included_allocated_storage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RebootReplicationInstanceMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "force_failover",
                "ForceFailover",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If this parameter is `true`, the reboot is conducted through a Multi-AZ
    # failover. (If the instance isn't configured for Multi-AZ, then you can't
    # specify `true`.)
    force_failover: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootReplicationInstanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_instance",
                "ReplicationInstance",
                TypeInfo(ReplicationInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication instance that is being rebooted.
    replication_instance: "ReplicationInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RefreshSchemasMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RefreshSchemasResponse(OutputShapeBase):
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
                "refresh_schemas_status",
                "RefreshSchemasStatus",
                TypeInfo(RefreshSchemasStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the refreshed schema.
    refresh_schemas_status: "RefreshSchemasStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RefreshSchemasStatus(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, RefreshSchemasStatusTypeValue]),
            ),
            (
                "last_refresh_date",
                "LastRefreshDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_failure_message",
                "LastFailureMessage",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the schema.
    status: typing.Union[str, "RefreshSchemasStatusTypeValue"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The date the schema was last refreshed.
    last_refresh_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last failure message for the schema.
    last_failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RefreshSchemasStatusTypeValue(str):
    successful = "successful"
    failed = "failed"
    refreshing = "refreshing"


class ReloadOptionValue(str):
    data_reload = "data-reload"
    validate_only = "validate-only"


@dataclasses.dataclass
class ReloadTablesMessage(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "tables_to_reload",
                "TablesToReload",
                TypeInfo(typing.List[TableToReload]),
            ),
            (
                "reload_option",
                "ReloadOption",
                TypeInfo(typing.Union[str, ReloadOptionValue]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name and schema of the table to be reloaded.
    tables_to_reload: typing.List["TableToReload"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Options for reload. Specify `data-reload` to reload the data and re-
    # validate it if validation is enabled. Specify `validate-only` to re-
    # validate the table. This option applies only when validation is enabled for
    # the task.

    # Valid values: data-reload, validate-only

    # Default value is data-reload.
    reload_option: typing.Union[str, "ReloadOptionValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReloadTablesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # >The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be
    # removed from.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag key (name) of the tag to be removed.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceResponse(OutputShapeBase):
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReplicationEndpointTypeValue(str):
    source = "source"
    target = "target"


@dataclasses.dataclass
class ReplicationInstance(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_identifier",
                "ReplicationInstanceIdentifier",
                TypeInfo(str),
            ),
            (
                "replication_instance_class",
                "ReplicationInstanceClass",
                TypeInfo(str),
            ),
            (
                "replication_instance_status",
                "ReplicationInstanceStatus",
                TypeInfo(str),
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
                "vpc_security_groups",
                "VpcSecurityGroups",
                TypeInfo(typing.List[VpcSecurityGroupMembership]),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "replication_subnet_group",
                "ReplicationSubnetGroup",
                TypeInfo(ReplicationSubnetGroup),
            ),
            (
                "preferred_maintenance_window",
                "PreferredMaintenanceWindow",
                TypeInfo(str),
            ),
            (
                "pending_modified_values",
                "PendingModifiedValues",
                TypeInfo(ReplicationPendingModifiedValues),
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
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_public_ip_address",
                "ReplicationInstancePublicIpAddress",
                TypeInfo(str),
            ),
            (
                "replication_instance_private_ip_address",
                "ReplicationInstancePrivateIpAddress",
                TypeInfo(str),
            ),
            (
                "replication_instance_public_ip_addresses",
                "ReplicationInstancePublicIpAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "replication_instance_private_ip_addresses",
                "ReplicationInstancePrivateIpAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "publicly_accessible",
                "PubliclyAccessible",
                TypeInfo(bool),
            ),
            (
                "secondary_availability_zone",
                "SecondaryAvailabilityZone",
                TypeInfo(str),
            ),
            (
                "free_until",
                "FreeUntil",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The replication instance identifier. This parameter is stored as a
    # lowercase string.

    # Constraints:

    #   * Must contain from 1 to 63 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.

    # Example: `myrepinstance`
    replication_instance_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The compute and memory capacity of the replication instance.

    # Valid Values: `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
    # dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge `
    replication_instance_class: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the replication instance.
    replication_instance_status: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of storage (in gigabytes) that is allocated for the replication
    # instance.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the replication instance was created.
    instance_create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC security group for the instance.
    vpc_security_groups: typing.List["VpcSecurityGroupMembership"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The Availability Zone for the instance.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subnet group for the replication instance.
    replication_subnet_group: "ReplicationSubnetGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maintenance window times for the replication instance.
    preferred_maintenance_window: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pending modification values.
    pending_modified_values: "ReplicationPendingModifiedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies if the replication instance is a Multi-AZ deployment. You cannot
    # set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to
    # `true`.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version number of the replication instance.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Boolean value indicating if minor version upgrades will be automatically
    # applied to the instance.
    auto_minor_version_upgrade: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The KMS key identifier that is used to encrypt the content on the
    # replication instance. If you do not specify a value for the KmsKeyId
    # parameter, then AWS DMS will use your default encryption key. AWS KMS
    # creates the default encryption key for your AWS account. Your AWS account
    # has a different default encryption key for each AWS region.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public IP address of the replication instance.
    replication_instance_public_ip_address: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The private IP address of the replication instance.
    replication_instance_private_ip_address: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public IP address of the replication instance.
    replication_instance_public_ip_addresses: typing.List[
        str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The private IP address of the replication instance.
    replication_instance_private_ip_addresses: typing.List[
        str] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Specifies the accessibility options for the replication instance. A value
    # of `true` represents an instance with a public IP address. A value of
    # `false` represents an instance with a private IP address. The default value
    # is `true`.
    publicly_accessible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The availability zone of the standby replication instance in a Multi-AZ
    # deployment.
    secondary_availability_zone: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The expiration date of the free replication instance that is part of the
    # Free DMS program.
    free_until: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationInstanceTaskLog(ShapeBase):
    """
    Contains metadata for a replication instance task log.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_name",
                "ReplicationTaskName",
                TypeInfo(str),
            ),
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_task_log_size",
                "ReplicationInstanceTaskLogSize",
                TypeInfo(int),
            ),
        ]

    # The name of the replication task.
    replication_task_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of the replication task log.
    replication_instance_task_log_size: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationPendingModifiedValues(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_class",
                "ReplicationInstanceClass",
                TypeInfo(str),
            ),
            (
                "allocated_storage",
                "AllocatedStorage",
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
        ]

    # The compute and memory capacity of the replication instance.

    # Valid Values: `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
    # dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge `
    replication_instance_class: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of storage (in gigabytes) that is allocated for the replication
    # instance.
    allocated_storage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies if the replication instance is a Multi-AZ deployment. You cannot
    # set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to
    # `true`.
    multi_az: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The engine version number of the replication instance.
    engine_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationSubnetGroup(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_subnet_group_identifier",
                "ReplicationSubnetGroupIdentifier",
                TypeInfo(str),
            ),
            (
                "replication_subnet_group_description",
                "ReplicationSubnetGroupDescription",
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
        ]

    # The identifier of the replication instance subnet group.
    replication_subnet_group_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the replication subnet group.
    replication_subnet_group_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the VPC.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the subnet group.
    subnet_group_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subnets that are in the subnet group.
    subnets: typing.List["Subnet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationSubnetGroupDoesNotCoverEnoughAZs(ShapeBase):
    """
    The replication subnet group does not cover enough Availability Zones (AZs).
    Edit the replication subnet group and add more AZs.
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
class ReplicationTask(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_identifier",
                "ReplicationTaskIdentifier",
                TypeInfo(str),
            ),
            (
                "source_endpoint_arn",
                "SourceEndpointArn",
                TypeInfo(str),
            ),
            (
                "target_endpoint_arn",
                "TargetEndpointArn",
                TypeInfo(str),
            ),
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "migration_type",
                "MigrationType",
                TypeInfo(typing.Union[str, MigrationTypeValue]),
            ),
            (
                "table_mappings",
                "TableMappings",
                TypeInfo(str),
            ),
            (
                "replication_task_settings",
                "ReplicationTaskSettings",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "last_failure_message",
                "LastFailureMessage",
                TypeInfo(str),
            ),
            (
                "stop_reason",
                "StopReason",
                TypeInfo(str),
            ),
            (
                "replication_task_creation_date",
                "ReplicationTaskCreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "replication_task_start_date",
                "ReplicationTaskStartDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "cdc_start_position",
                "CdcStartPosition",
                TypeInfo(str),
            ),
            (
                "cdc_stop_position",
                "CdcStopPosition",
                TypeInfo(str),
            ),
            (
                "recovery_checkpoint",
                "RecoveryCheckpoint",
                TypeInfo(str),
            ),
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "replication_task_stats",
                "ReplicationTaskStats",
                TypeInfo(ReplicationTaskStats),
            ),
        ]

    # The user-assigned replication task identifier or name.

    # Constraints:

    #   * Must contain from 1 to 255 alphanumeric characters or hyphens.

    #   * First character must be a letter.

    #   * Cannot end with a hyphen or contain two consecutive hyphens.
    replication_task_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    source_endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    target_endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of migration.
    migration_type: typing.Union[str, "MigrationTypeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Table mappings specified in the task.
    table_mappings: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The settings for the replication task.
    replication_task_settings: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the replication task.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last error (failure) message generated for the replication instance.
    last_failure_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason the replication task was stopped.
    stop_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the replication task was created.
    replication_task_creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the replication task is scheduled to start.
    replication_task_start_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when you want a change data capture (CDC) operation to start. Use
    # either CdcStartPosition or CdcStartTime to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # The value can be in date, checkpoint, or LSN/SCN format.

    # Date Example: --cdc-start-position “2018-03-08T12:12:12”

    # Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-
    # changelog.157832:1975:-1:2002:677883278264080:mysql-bin-
    # changelog.157832:1876#0#0#*#0#93"

    # LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
    cdc_start_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates when you want a change data capture (CDC) operation to stop. The
    # value can be either server time or commit time.

    # Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

    # Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12
    # “
    cdc_stop_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the last checkpoint that occurred during a change data capture
    # (CDC) operation. You can provide this value to the `CdcStartPosition`
    # parameter to start a CDC operation that begins at that checkpoint.
    recovery_checkpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistics for the task, including elapsed time, tables loaded, and
    # table errors.
    replication_task_stats: "ReplicationTaskStats" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationTaskAssessmentResult(ShapeBase):
    """
    The task assessment report in JSON format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_identifier",
                "ReplicationTaskIdentifier",
                TypeInfo(str),
            ),
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "replication_task_last_assessment_date",
                "ReplicationTaskLastAssessmentDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "assessment_status",
                "AssessmentStatus",
                TypeInfo(str),
            ),
            (
                "assessment_results_file",
                "AssessmentResultsFile",
                TypeInfo(str),
            ),
            (
                "assessment_results",
                "AssessmentResults",
                TypeInfo(str),
            ),
            (
                "s3_object_url",
                "S3ObjectUrl",
                TypeInfo(str),
            ),
        ]

    # The replication task identifier of the task on which the task assessment
    # was run.
    replication_task_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the task assessment was completed.
    replication_task_last_assessment_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the task assessment.
    assessment_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file containing the results of the task assessment.
    assessment_results_file: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The task assessment results in JSON format.
    assessment_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the S3 object containing the task assessment results.
    s3_object_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicationTaskStats(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "full_load_progress_percent",
                "FullLoadProgressPercent",
                TypeInfo(int),
            ),
            (
                "elapsed_time_millis",
                "ElapsedTimeMillis",
                TypeInfo(int),
            ),
            (
                "tables_loaded",
                "TablesLoaded",
                TypeInfo(int),
            ),
            (
                "tables_loading",
                "TablesLoading",
                TypeInfo(int),
            ),
            (
                "tables_queued",
                "TablesQueued",
                TypeInfo(int),
            ),
            (
                "tables_errored",
                "TablesErrored",
                TypeInfo(int),
            ),
        ]

    # The percent complete for the full load migration task.
    full_load_progress_percent: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The elapsed time of the task, in milliseconds.
    elapsed_time_millis: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tables loaded for this task.
    tables_loaded: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tables currently loading for this task.
    tables_loading: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tables queued for this task.
    tables_queued: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of errors that have occurred during this task.
    tables_errored: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceAlreadyExistsFault(ShapeBase):
    """
    The resource you are attempting to create already exists.
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
class ResourceNotFoundFault(ShapeBase):
    """
    The resource could not be found.
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
class ResourceQuotaExceededFault(ShapeBase):
    """
    The quota for this resource quota has been exceeded.
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
class S3Settings(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_access_role_arn",
                "ServiceAccessRoleArn",
                TypeInfo(str),
            ),
            (
                "external_table_definition",
                "ExternalTableDefinition",
                TypeInfo(str),
            ),
            (
                "csv_row_delimiter",
                "CsvRowDelimiter",
                TypeInfo(str),
            ),
            (
                "csv_delimiter",
                "CsvDelimiter",
                TypeInfo(str),
            ),
            (
                "bucket_folder",
                "BucketFolder",
                TypeInfo(str),
            ),
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "compression_type",
                "CompressionType",
                TypeInfo(typing.Union[str, CompressionTypeValue]),
            ),
        ]

    # The Amazon Resource Name (ARN) used by the service access IAM role.
    service_access_role_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The external table definition.
    external_table_definition: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The delimiter used to separate rows in the source files. The default is a
    # carriage return (\n).
    csv_row_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The delimiter used to separate columns in the source files. The default is
    # a comma.
    csv_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter to set a folder name in the S3 bucket. If provided,
    # tables are created in the path <bucketFolder>/<schema_name>/<table_name>/.
    # If this parameter is not specified, then the path used is
    # <schema_name>/<table_name>/.
    bucket_folder: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the S3 bucket.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional parameter to use GZIP to compress the target files. Set to GZIP
    # to compress the target files. Set to NONE (the default) or do not use to
    # leave the files uncompressed.
    compression_type: typing.Union[str, "CompressionTypeValue"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class SNSInvalidTopicFault(ShapeBase):
    """
    The SNS topic is invalid.
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
class SNSNoAuthorizationFault(ShapeBase):
    """
    You are not authorized for the SNS subscription.
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


class SourceType(str):
    replication_instance = "replication-instance"


@dataclasses.dataclass
class StartReplicationTaskAssessmentMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication task.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartReplicationTaskAssessmentResponse(OutputShapeBase):
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
                "replication_task",
                "ReplicationTask",
                TypeInfo(ReplicationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The assessed replication task.
    replication_task: "ReplicationTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartReplicationTaskMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
            (
                "start_replication_task_type",
                "StartReplicationTaskType",
                TypeInfo(typing.Union[str, StartReplicationTaskTypeValue]),
            ),
            (
                "cdc_start_time",
                "CdcStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "cdc_start_position",
                "CdcStartPosition",
                TypeInfo(str),
            ),
            (
                "cdc_stop_position",
                "CdcStopPosition",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication task to be started.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of replication task.
    start_replication_task_type: typing.Union[
        str, "StartReplicationTaskTypeValue"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Indicates the start time for a change data capture (CDC) operation. Use
    # either CdcStartTime or CdcStartPosition to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
    cdc_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when you want a change data capture (CDC) operation to start. Use
    # either CdcStartPosition or CdcStartTime to specify when you want a CDC
    # operation to start. Specifying both values results in an error.

    # The value can be in date, checkpoint, or LSN/SCN format.

    # Date Example: --cdc-start-position “2018-03-08T12:12:12”

    # Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-
    # changelog.157832:1975:-1:2002:677883278264080:mysql-bin-
    # changelog.157832:1876#0#0#*#0#93"

    # LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
    cdc_start_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates when you want a change data capture (CDC) operation to stop. The
    # value can be either server time or commit time.

    # Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

    # Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12
    # “
    cdc_stop_position: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartReplicationTaskResponse(OutputShapeBase):
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
                "replication_task",
                "ReplicationTask",
                TypeInfo(ReplicationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication task started.
    replication_task: "ReplicationTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StartReplicationTaskTypeValue(str):
    start_replication = "start-replication"
    resume_processing = "resume-processing"
    reload_target = "reload-target"


@dataclasses.dataclass
class StopReplicationTaskMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_task_arn",
                "ReplicationTaskArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name(ARN) of the replication task to be stopped.
    replication_task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopReplicationTaskResponse(OutputShapeBase):
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
                "replication_task",
                "ReplicationTask",
                TypeInfo(ReplicationTask),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication task stopped.
    replication_task: "ReplicationTask" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StorageQuotaExceededFault(ShapeBase):
    """
    The storage quota has been exceeded.
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
class Subnet(ShapeBase):
    """

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

    # The subnet identifier.
    subnet_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone of the subnet.
    subnet_availability_zone: "AvailabilityZone" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the subnet.
    subnet_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetAlreadyInUse(ShapeBase):
    """
    The specified subnet is already in use.
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
class SupportedEndpointType(ShapeBase):
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
                "supports_cdc",
                "SupportsCDC",
                TypeInfo(bool),
            ),
            (
                "endpoint_type",
                "EndpointType",
                TypeInfo(typing.Union[str, ReplicationEndpointTypeValue]),
            ),
            (
                "engine_display_name",
                "EngineDisplayName",
                TypeInfo(str),
            ),
        ]

    # The database engine name. Valid values, depending on the EndPointType,
    # include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql,
    # redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb, and
    # sqlserver.
    engine_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if Change Data Capture (CDC) is supported.
    supports_cdc: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of endpoint.
    endpoint_type: typing.Union[str, "ReplicationEndpointTypeValue"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The expanded name for the engine name. For example, if the `EngineName`
    # parameter is "aurora," this value would be "Amazon Aurora MySQL."
    engine_display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableStatistics(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_name",
                "SchemaName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "inserts",
                "Inserts",
                TypeInfo(int),
            ),
            (
                "deletes",
                "Deletes",
                TypeInfo(int),
            ),
            (
                "updates",
                "Updates",
                TypeInfo(int),
            ),
            (
                "ddls",
                "Ddls",
                TypeInfo(int),
            ),
            (
                "full_load_rows",
                "FullLoadRows",
                TypeInfo(int),
            ),
            (
                "full_load_condtnl_chk_failed_rows",
                "FullLoadCondtnlChkFailedRows",
                TypeInfo(int),
            ),
            (
                "full_load_error_rows",
                "FullLoadErrorRows",
                TypeInfo(int),
            ),
            (
                "last_update_time",
                "LastUpdateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "table_state",
                "TableState",
                TypeInfo(str),
            ),
            (
                "validation_pending_records",
                "ValidationPendingRecords",
                TypeInfo(int),
            ),
            (
                "validation_failed_records",
                "ValidationFailedRecords",
                TypeInfo(int),
            ),
            (
                "validation_suspended_records",
                "ValidationSuspendedRecords",
                TypeInfo(int),
            ),
            (
                "validation_state",
                "ValidationState",
                TypeInfo(str),
            ),
            (
                "validation_state_details",
                "ValidationStateDetails",
                TypeInfo(str),
            ),
        ]

    # The schema name.
    schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of insert actions performed on a table.
    inserts: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of delete actions performed on a table.
    deletes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of update actions performed on a table.
    updates: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Data Definition Language (DDL) used to build and modify the structure
    # of your tables.
    ddls: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of rows added during the Full Load operation.
    full_load_rows: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of rows that failed conditional checks during the Full Load
    # operation (valid only for DynamoDB as a target migrations).
    full_load_condtnl_chk_failed_rows: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of rows that failed to load during the Full Load operation
    # (valid only for DynamoDB as a target migrations).
    full_load_error_rows: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last time the table was updated.
    last_update_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the tables described.

    # Valid states: Table does not exist | Before load | Full load | Table
    # completed | Table cancelled | Table error | Table all | Table updates |
    # Table is being reloaded
    table_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of records that have yet to be validated.
    validation_pending_records: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of records that failed validation.
    validation_failed_records: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of records that could not be validated.
    validation_suspended_records: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The validation state of the table.

    # The parameter can have the following values

    #   * Not enabled—Validation is not enabled for the table in the migration task.

    #   * Pending records—Some records in the table are waiting for validation.

    #   * Mismatched records—Some records in the table do not match between the source and target.

    #   * Suspended records—Some records in the table could not be validated.

    #   * No primary key—The table could not be validated because it had no primary key.

    #   * Table error—The table was not validated because it was in an error state and some data was not migrated.

    #   * Validated—All rows in the table were validated. If the table is updated, the status can change from Validated.

    #   * Error—The table could not be validated because of an unexpected error.
    validation_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional details about the state of validation.
    validation_state_details: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TableToReload(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_name",
                "SchemaName",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
        ]

    # The schema name of the table to be reloaded.
    schema_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The table name of the table to be reloaded.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """

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
    # 128 Unicode characters in length and cannot be prefixed with "aws:" or
    # "dms:". The string can only contain only the set of Unicode letters,
    # digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value is the optional value of the tag. The string value can be from 1 to
    # 256 Unicode characters in length and cannot be prefixed with "aws:" or
    # "dms:". The string can only contain only the set of Unicode letters,
    # digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestConnectionMessage(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_instance_arn",
                "ReplicationInstanceArn",
                TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the replication instance.
    replication_instance_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) string that uniquely identifies the
    # endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestConnectionResponse(OutputShapeBase):
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
                "connection",
                "Connection",
                TypeInfo(Connection),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The connection tested.
    connection: "Connection" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradeDependencyFailureFault(ShapeBase):
    """
    An upgrade dependency is preventing the database migration.
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
class VpcSecurityGroupMembership(ShapeBase):
    """

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

    # The VPC security group Id.
    vpc_security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the VPC security group.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )
