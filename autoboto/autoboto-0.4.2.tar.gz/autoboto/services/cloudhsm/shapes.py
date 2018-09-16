import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AddTagsToResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more tags.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddTagsToResourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
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

    # The status of the operation.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ClientVersion(str):
    VALUE_OF_5_1 = "5.1"
    VALUE_OF_5_3 = "5.3"


@dataclasses.dataclass
class CloudHsmInternalException(ShapeBase):
    """
    Indicates that an internal error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class CloudHsmObjectState(str):
    READY = "READY"
    UPDATING = "UPDATING"
    DEGRADED = "DEGRADED"


@dataclasses.dataclass
class CloudHsmServiceException(ShapeBase):
    """
    Indicates that an exception occurred in the AWS CloudHSM service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "retryable",
                "retryable",
                TypeInfo(bool),
            ),
        ]

    # Additional information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the action can be retried.
    retryable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHapgRequest(ShapeBase):
    """
    Contains the inputs for the CreateHapgRequest action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
        ]

    # The label of the new high-availability partition group.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHapgResponse(OutputShapeBase):
    """
    Contains the output of the CreateHAPartitionGroup action.
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
                "hapg_arn",
                "HapgArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the high-availability partition group.
    hapg_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHsmRequest(ShapeBase):
    """
    Contains the inputs for the `CreateHsm` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "ssh_key",
                "SshKey",
                TypeInfo(str),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                TypeInfo(str),
            ),
            (
                "subscription_type",
                "SubscriptionType",
                TypeInfo(typing.Union[str, SubscriptionType]),
            ),
            (
                "eni_ip",
                "EniIp",
                TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "syslog_ip",
                "SyslogIp",
                TypeInfo(str),
            ),
        ]

    # The identifier of the subnet in your VPC in which to place the HSM.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSH public key to install on the HSM.
    ssh_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM role to enable the AWS CloudHSM service to allocate an
    # ENI on your behalf.
    iam_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the type of subscription for the HSM.

    #   * **PRODUCTION** \- The HSM is being used in a production environment.

    #   * **TRIAL** \- The HSM is being used in a product trial.
    subscription_type: typing.Union[str, "SubscriptionType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The IP address to assign to the HSM's ENI.

    # If an IP address is not specified, an IP address will be randomly chosen
    # from the CIDR range of the subnet.
    eni_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The external ID from `IamRoleArn`, if present.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-defined token to ensure idempotence. Subsequent calls to this
    # operation with the same token will be ignored.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address for the syslog monitoring server. The AWS CloudHSM service
    # only supports one syslog monitoring server.
    syslog_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHsmResponse(OutputShapeBase):
    """
    Contains the output of the `CreateHsm` operation.
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
                "hsm_arn",
                "HsmArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the HSM.
    hsm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLunaClientRequest(ShapeBase):
    """
    Contains the inputs for the CreateLunaClient action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
        ]

    # The contents of a Base64-Encoded X.509 v3 certificate to be installed on
    # the HSMs used by this client.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The label for the client.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLunaClientResponse(OutputShapeBase):
    """
    Contains the output of the CreateLunaClient action.
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
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteHapgRequest(ShapeBase):
    """
    Contains the inputs for the DeleteHapg action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the high-availability partition group to delete.
    hapg_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteHapgResponse(OutputShapeBase):
    """
    Contains the output of the DeleteHapg action.
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
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the action.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteHsmRequest(ShapeBase):
    """
    Contains the inputs for the DeleteHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the HSM to delete.
    hsm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteHsmResponse(OutputShapeBase):
    """
    Contains the output of the DeleteHsm operation.
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
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the operation.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLunaClientRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the client to delete.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLunaClientResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
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

    # The status of the action.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHapgRequest(ShapeBase):
    """
    Contains the inputs for the DescribeHapg action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the high-availability partition group to describe.
    hapg_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHapgResponse(OutputShapeBase):
    """
    Contains the output of the DescribeHapg action.
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
                "hapg_arn",
                "HapgArn",
                TypeInfo(str),
            ),
            (
                "hapg_serial",
                "HapgSerial",
                TypeInfo(str),
            ),
            (
                "hsms_last_action_failed",
                "HsmsLastActionFailed",
                TypeInfo(typing.List[str]),
            ),
            (
                "hsms_pending_deletion",
                "HsmsPendingDeletion",
                TypeInfo(typing.List[str]),
            ),
            (
                "hsms_pending_registration",
                "HsmsPendingRegistration",
                TypeInfo(typing.List[str]),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "last_modified_timestamp",
                "LastModifiedTimestamp",
                TypeInfo(str),
            ),
            (
                "partition_serial_list",
                "PartitionSerialList",
                TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, CloudHsmObjectState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the high-availability partition group.
    hapg_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number of the high-availability partition group.
    hapg_serial: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    hsms_last_action_failed: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    hsms_pending_deletion: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    hsms_pending_registration: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The label for the high-availability partition group.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the high-availability partition group was last modified.
    last_modified_timestamp: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of partition serial numbers that belong to the high-availability
    # partition group.
    partition_serial_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the high-availability partition group.
    state: typing.Union[str, "CloudHsmObjectState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeHsmRequest(ShapeBase):
    """
    Contains the inputs for the DescribeHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                TypeInfo(str),
            ),
            (
                "hsm_serial_number",
                "HsmSerialNumber",
                TypeInfo(str),
            ),
        ]

    # The ARN of the HSM. Either the `HsmArn` or the `SerialNumber` parameter
    # must be specified.
    hsm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number of the HSM. Either the `HsmArn` or the `HsmSerialNumber`
    # parameter must be specified.
    hsm_serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHsmResponse(OutputShapeBase):
    """
    Contains the output of the DescribeHsm operation.
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
                "hsm_arn",
                "HsmArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, HsmStatus]),
            ),
            (
                "status_details",
                "StatusDetails",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "eni_id",
                "EniId",
                TypeInfo(str),
            ),
            (
                "eni_ip",
                "EniIp",
                TypeInfo(str),
            ),
            (
                "subscription_type",
                "SubscriptionType",
                TypeInfo(typing.Union[str, SubscriptionType]),
            ),
            (
                "subscription_start_date",
                "SubscriptionStartDate",
                TypeInfo(str),
            ),
            (
                "subscription_end_date",
                "SubscriptionEndDate",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "vendor_name",
                "VendorName",
                TypeInfo(str),
            ),
            (
                "hsm_type",
                "HsmType",
                TypeInfo(str),
            ),
            (
                "software_version",
                "SoftwareVersion",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "SshPublicKey",
                TypeInfo(str),
            ),
            (
                "ssh_key_last_updated",
                "SshKeyLastUpdated",
                TypeInfo(str),
            ),
            (
                "server_cert_uri",
                "ServerCertUri",
                TypeInfo(str),
            ),
            (
                "server_cert_last_updated",
                "ServerCertLastUpdated",
                TypeInfo(str),
            ),
            (
                "partitions",
                "Partitions",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the HSM.
    hsm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the HSM.
    status: typing.Union[str, "HsmStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains additional information about the status of the HSM.
    status_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone that the HSM is in.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the elastic network interface (ENI) attached to the HSM.
    eni_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address assigned to the HSM's ENI.
    eni_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the type of subscription for the HSM.

    #   * **PRODUCTION** \- The HSM is being used in a production environment.

    #   * **TRIAL** \- The HSM is being used in a product trial.
    subscription_type: typing.Union[str, "SubscriptionType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The subscription start date.
    subscription_start_date: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subscription end date.
    subscription_end_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the VPC that the HSM is in.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the subnet that the HSM is in.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role assigned to the HSM.
    iam_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The serial number of the HSM.
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the HSM vendor.
    vendor_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HSM model type.
    hsm_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HSM software version.
    software_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public SSH key.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the SSH key was last updated.
    ssh_key_last_updated: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URI of the certificate server.
    server_cert_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the server certificate was last updated.
    server_cert_last_updated: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of partitions on the HSM.
    partitions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLunaClientRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
            (
                "certificate_fingerprint",
                "CertificateFingerprint",
                TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate fingerprint.
    certificate_fingerprint: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeLunaClientResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "certificate_fingerprint",
                "CertificateFingerprint",
                TypeInfo(str),
            ),
            (
                "last_modified_timestamp",
                "LastModifiedTimestamp",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate installed on the HSMs used by this client.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate fingerprint.
    certificate_fingerprint: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time the client was last modified.
    last_modified_timestamp: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The label of the client.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
            (
                "client_version",
                "ClientVersion",
                TypeInfo(typing.Union[str, ClientVersion]),
            ),
            (
                "hapg_list",
                "HapgList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The client version.
    client_version: typing.Union[str, "ClientVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ARNs that identify the high-availability partition groups that
    # are associated with the client.
    hapg_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConfigResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "config_type",
                "ConfigType",
                TypeInfo(str),
            ),
            (
                "config_file",
                "ConfigFile",
                TypeInfo(str),
            ),
            (
                "config_cred",
                "ConfigCred",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of credentials.
    config_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The chrystoki.conf configuration file.
    config_file: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate file containing the server.pem files of the HSMs.
    config_cred: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class HsmStatus(str):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    DEGRADED = "DEGRADED"


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    Indicates that one or more of the request parameters are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAvailableZonesRequest(ShapeBase):
    """
    Contains the inputs for the ListAvailableZones action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListAvailableZonesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "az_list",
                "AZList",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of Availability Zones that have available AWS CloudHSM capacity.
    az_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHapgsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The `NextToken` value from a previous call to `ListHapgs`. Pass null if
    # this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHapgsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hapg_list",
                "HapgList",
                TypeInfo(typing.List[str]),
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

    # The list of high-availability partition groups.
    hapg_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If not null, more results are available. Pass this value to `ListHapgs` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHsmsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The `NextToken` value from a previous call to `ListHsms`. Pass null if this
    # is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListHsmsResponse(OutputShapeBase):
    """
    Contains the output of the `ListHsms` operation.
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
                "hsm_list",
                "HsmList",
                TypeInfo(typing.List[str]),
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

    # The list of ARNs that identify the HSMs.
    hsm_list: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If not null, more results are available. Pass this value to `ListHsms` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLunaClientsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The `NextToken` value from a previous call to `ListLunaClients`. Pass null
    # if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLunaClientsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_list",
                "ClientList",
                TypeInfo(typing.List[str]),
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

    # The list of clients.
    client_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If not null, more results are available. Pass this to `ListLunaClients` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(OutputShapeBase):
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

    # One or more tags.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyHapgRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hapg_arn",
                "HapgArn",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "partition_serial_list",
                "PartitionSerialList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the high-availability partition group to modify.
    hapg_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new label for the high-availability partition group.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of partition serial numbers to make members of the high-
    # availability partition group.
    partition_serial_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ModifyHapgResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hapg_arn",
                "HapgArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the high-availability partition group.
    hapg_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyHsmRequest(ShapeBase):
    """
    Contains the inputs for the ModifyHsm operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hsm_arn",
                "HsmArn",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "eni_ip",
                "EniIp",
                TypeInfo(str),
            ),
            (
                "iam_role_arn",
                "IamRoleArn",
                TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "syslog_ip",
                "SyslogIp",
                TypeInfo(str),
            ),
        ]

    # The ARN of the HSM to modify.
    hsm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new identifier of the subnet that the HSM is in. The new subnet must be
    # in the same Availability Zone as the current subnet.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new IP address for the elastic network interface (ENI) attached to the
    # HSM.

    # If the HSM is moved to a different subnet, and an IP address is not
    # specified, an IP address will be randomly chosen from the CIDR range of the
    # new subnet.
    eni_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new IAM role ARN.
    iam_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new external ID.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new IP address for the syslog monitoring server. The AWS CloudHSM
    # service only supports one syslog monitoring server.
    syslog_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyHsmResponse(OutputShapeBase):
    """
    Contains the output of the ModifyHsm operation.
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
                "hsm_arn",
                "HsmArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the HSM.
    hsm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyLunaClientRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
        ]

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new certificate for the client.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModifyLunaClientResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_arn",
                "ClientArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the client.
    client_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_key_list",
                "TagKeyList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag key or keys to remove.

    # Specify only the tag key to remove (not the value). To overwrite the value
    # for an existing tag, use AddTagsToResource.
    tag_key_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveTagsFromResourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
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

    # The status of the operation.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SubscriptionType(str):
    """
    Specifies the type of subscription for the HSM.

      * **PRODUCTION** \- The HSM is being used in a production environment.

      * **TRIAL** \- The HSM is being used in a product trial.
    """
    PRODUCTION = "PRODUCTION"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A key-value pair that identifies or specifies metadata about an AWS CloudHSM
    resource.
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

    # The key of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )
