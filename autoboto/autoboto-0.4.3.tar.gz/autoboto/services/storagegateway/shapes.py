import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class ActivateGatewayInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * ActivateGatewayInput$ActivationKey

      * ActivateGatewayInput$GatewayName

      * ActivateGatewayInput$GatewayRegion

      * ActivateGatewayInput$GatewayTimezone

      * ActivateGatewayInput$GatewayType

      * ActivateGatewayInput$TapeDriveType

      * ActivateGatewayInput$MediumChangerType
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "activation_key",
                "ActivationKey",
                TypeInfo(str),
            ),
            (
                "gateway_name",
                "GatewayName",
                TypeInfo(str),
            ),
            (
                "gateway_timezone",
                "GatewayTimezone",
                TypeInfo(str),
            ),
            (
                "gateway_region",
                "GatewayRegion",
                TypeInfo(str),
            ),
            (
                "gateway_type",
                "GatewayType",
                TypeInfo(str),
            ),
            (
                "tape_drive_type",
                "TapeDriveType",
                TypeInfo(str),
            ),
            (
                "medium_changer_type",
                "MediumChangerType",
                TypeInfo(str),
            ),
        ]

    # Your gateway activation key. You can obtain the activation key by sending
    # an HTTP GET request with redirects enabled to the gateway IP address (port
    # 80). The redirect URL returned in the response provides you the activation
    # key for your gateway in the query string parameter `activationKey`. It may
    # also include other activation-related parameters, however, these are merely
    # defaults -- the arguments you pass to the `ActivateGateway` API call
    # determine the actual configuration of your gateway.

    # For more information, see
    # https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-
    # key.html in the Storage Gateway User Guide.
    activation_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name you configured for your gateway.
    gateway_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the time zone you want to set for the gateway. The
    # time zone is of the format "GMT-hr:mm" or "GMT+hr:mm". For example,
    # GMT-4:00 indicates the time is 4 hours behind GMT. GMT+2:00 indicates the
    # time is 2 hours ahead of GMT. The time zone is used, for example, for
    # scheduling snapshots and your gateway's maintenance schedule.
    gateway_timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the region where you want to store your data. The
    # gateway region specified must be the same region as the region in your
    # `Host` header in the request. For more information about available regions
    # and endpoints for AWS Storage Gateway, see [Regions and
    # Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#sg_region)
    # in the _Amazon Web Services Glossary_.

    # Valid Values: "us-east-1", "us-east-2", "us-west-1", "us-west-2", "ca-
    # central-1", "eu-west-1", "eu-central-1", "eu-west-2", "eu-west-3", "ap-
    # northeast-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-
    # south-1", "sa-east-1"
    gateway_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that defines the type of gateway to activate. The type specified is
    # critical to all later functions of the gateway and cannot be changed after
    # activation. The default value is `STORED`.

    # Valid Values: "STORED", "CACHED", "VTL", "FILE_S3"
    gateway_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that indicates the type of tape drive to use for tape gateway.
    # This field is optional.

    # Valid Values: "IBM-ULT3580-TD5"
    tape_drive_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that indicates the type of medium changer to use for tape
    # gateway. This field is optional.

    # Valid Values: "STK-L700", "AWS-Gateway-VTL"
    medium_changer_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActivateGatewayOutput(OutputShapeBase):
    """
    AWS Storage Gateway returns the Amazon Resource Name (ARN) of the activated
    gateway. It is a string made of information such as your account, gateway name,
    and region. This ARN is used to reference the gateway in other API operations as
    well as resource-based authorization.

    For gateways activated prior to September 02, 2015, the gateway ARN contains the
    gateway name rather than the gateway ID. Changing the name of the gateway has no
    effect on the gateway ARN.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddCacheInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_ids",
                "DiskIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddCacheOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsToResourceInput(ShapeBase):
    """
    AddTagsToResourceInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource you want to add tags to.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value pair that represents the tag you want to add to the resource.
    # The value can be an empty string.

    # Valid characters for key and value are letters, spaces, and numbers
    # representable in UTF-8 format, and the following special characters: + - =
    # . _ : / @.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsToResourceOutput(OutputShapeBase):
    """
    AddTagsToResourceOutput
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
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the resource you want to add tags to.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddUploadBufferInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_ids",
                "DiskIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddUploadBufferOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddWorkingStorageInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * AddWorkingStorageInput$DiskIds
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_ids",
                "DiskIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings that identify disks that are to be configured as
    # working storage. Each string have a minimum length of 1 and maximum length
    # of 300. You can get the disk IDs from the ListLocalDisks API.
    disk_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddWorkingStorageOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway for which working storage was
    configured.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CachediSCSIVolume(ShapeBase):
    """
    Describes an iSCSI cached volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "volume_id",
                "VolumeId",
                TypeInfo(str),
            ),
            (
                "volume_type",
                "VolumeType",
                TypeInfo(str),
            ),
            (
                "volume_status",
                "VolumeStatus",
                TypeInfo(str),
            ),
            (
                "volume_size_in_bytes",
                "VolumeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "volume_progress",
                "VolumeProgress",
                TypeInfo(float),
            ),
            (
                "source_snapshot_id",
                "SourceSnapshotId",
                TypeInfo(str),
            ),
            (
                "volumei_scsi_attributes",
                "VolumeiSCSIAttributes",
                TypeInfo(VolumeiSCSIAttributes),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "volume_used_in_bytes",
                "VolumeUsedInBytes",
                TypeInfo(int),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the storage volume.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the volume, e.g. vol-AE4B946D.
    volume_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the VolumeType enumeration values that describes the type of the
    # volume.
    volume_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the VolumeStatus values that indicates the state of the storage
    # volume.
    volume_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of the volume capacity.
    volume_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the percentage complete if the volume is restoring or
    # bootstrapping that represents the percent of data transferred. This field
    # does not appear in the response if the cached volume is not restoring or
    # bootstrapping.
    volume_progress: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the cached volume was created from a snapshot, this field contains the
    # snapshot ID used, e.g. snap-78e22663. Otherwise, this field is not
    # included.
    source_snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An VolumeiSCSIAttributes object that represents a collection of iSCSI
    # attributes for one stored volume.
    volumei_scsi_attributes: "VolumeiSCSIAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the volume was created. Volumes created prior to March 28, 2017
    # don’t have this time stamp.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the data stored on the volume in bytes.

    # This value is not available for volumes created prior to May 13, 2015,
    # until you store data on the volume.
    volume_used_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelArchivalInput(ShapeBase):
    """
    CancelArchivalInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the virtual tape you want to cancel
    # archiving for.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelArchivalOutput(OutputShapeBase):
    """
    CancelArchivalOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the virtual tape for which archiving was
    # canceled.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelRetrievalInput(ShapeBase):
    """
    CancelRetrievalInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the virtual tape you want to cancel
    # retrieval for.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelRetrievalOutput(OutputShapeBase):
    """
    CancelRetrievalOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the virtual tape for which retrieval was
    # canceled.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChapInfo(ShapeBase):
    """
    Describes Challenge-Handshake Authentication Protocol (CHAP) information that
    supports authentication between your gateway and iSCSI initiators.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "secret_to_authenticate_initiator",
                "SecretToAuthenticateInitiator",
                TypeInfo(str),
            ),
            (
                "initiator_name",
                "InitiatorName",
                TypeInfo(str),
            ),
            (
                "secret_to_authenticate_target",
                "SecretToAuthenticateTarget",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume.

    # Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and
    # hyphens (-).
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The secret key that the initiator (for example, the Windows client) must
    # provide to participate in mutual CHAP with the target.
    secret_to_authenticate_initiator: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The iSCSI initiator that connects to the target.
    initiator_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The secret key that the target must provide to participate in mutual CHAP
    # with the initiator (e.g. Windows client).
    secret_to_authenticate_target: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCachediSCSIVolumeInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "volume_size_in_bytes",
                "VolumeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "target_name",
                "TargetName",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "source_volume_arn",
                "SourceVolumeARN",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the volume in bytes.
    volume_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the iSCSI target used by initiators to connect to the target
    # and as a suffix for the target ARN. For example, specifying `TargetName` as
    # _myvolume_ results in the target ARN of arn:aws:storagegateway:us-
    # east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume.
    # The target name must be unique across all volumes of a gateway.
    target_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network interface of the gateway on which to expose the iSCSI target.
    # Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a
    # list of the network interfaces available on a gateway.

    # Valid Values: A valid IP address.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that you use to retry a request. If you retry a
    # request, use the same `ClientToken` you specified in the initial request.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the
    # new cached volume. Specify this field if you want to create the iSCSI
    # storage volume from a snapshot otherwise do not include this field. To list
    # snapshots for your account use
    # [DescribeSnapshots](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
    # query-DescribeSnapshots.html) in the _Amazon Elastic Compute Cloud API
    # Reference_.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for an existing volume. Specifying this ARN makes the new volume
    # into an exact copy of the specified existing volume's latest recovery
    # point. The `VolumeSizeInBytes` value for this new volume must be equal to
    # or larger than the size of the existing volume, in bytes.
    source_volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCachediSCSIVolumeOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the configured volume.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # he Amazon Resource Name (ARN) of the volume target that includes the iSCSI
    # name that initiators can use to connect to the target.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateNFSFileShareInput(ShapeBase):
    """
    CreateNFSFileShareInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "location_arn",
                "LocationARN",
                TypeInfo(str),
            ),
            (
                "nfs_file_share_defaults",
                "NFSFileShareDefaults",
                TypeInfo(NFSFileShareDefaults),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
            (
                "default_storage_class",
                "DefaultStorageClass",
                TypeInfo(str),
            ),
            (
                "object_acl",
                "ObjectACL",
                TypeInfo(typing.Union[str, ObjectACL]),
            ),
            (
                "client_list",
                "ClientList",
                TypeInfo(typing.List[str]),
            ),
            (
                "squash",
                "Squash",
                TypeInfo(str),
            ),
            (
                "read_only",
                "ReadOnly",
                TypeInfo(bool),
            ),
            (
                "guess_mime_type_enabled",
                "GuessMIMETypeEnabled",
                TypeInfo(bool),
            ),
            (
                "requester_pays",
                "RequesterPays",
                TypeInfo(bool),
            ),
        ]

    # A unique string value that you supply that is used by file gateway to
    # ensure idempotent file share creation.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the file gateway on which you want to
    # create a file share.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the AWS Identity and Access Management (IAM) role that a file
    # gateway assumes when it accesses the underlying storage.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the backed storage used for storing file data.
    location_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # File share default values. Optional.
    nfs_file_share_defaults: "NFSFileShareDefaults" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) AWS KMS key used for Amazon S3 server side
    # encryption. This value can only be set when KMSEncrypted is true. Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default storage class for objects put into an Amazon S3 bucket by the
    # file gateway. Possible values are `S3_STANDARD`, `S3_STANDARD_IA`, or
    # `S3_ONEZONE_IA`. If this field is not populated, the default value
    # `S3_STANDARD` is used. Optional.
    default_storage_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the access control list permission for objects in the S3
    # bucket that a file gateway puts objects into. The default value is
    # "private".
    object_acl: typing.Union[str, "ObjectACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of clients that are allowed to access the file gateway. The list
    # must contain either valid IP addresses or valid CIDR blocks.
    client_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maps a user to anonymous user. Valid options are the following:

    #   * `RootSquash` \- Only root is mapped to anonymous user.

    #   * `NoSquash` \- No one is mapped to anonymous user

    #   * `AllSquash` \- Everyone is mapped to anonymous user.
    squash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the write status of a file share. This value is true if
    # the write status is read-only, and otherwise false.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that enables guessing of the MIME type for uploaded objects based
    # on file extensions. Set this value to true to enable MIME type guessing,
    # and otherwise to false. The default value is true.
    guess_mime_type_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the access control list permission for objects in the
    # Amazon S3 bucket that a file gateway puts objects into. The default value
    # is `private`.
    requester_pays: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateNFSFileShareOutput(OutputShapeBase):
    """
    CreateNFSFileShareOutput
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
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the newly created file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSMBFileShareInput(ShapeBase):
    """
    CreateSMBFileShareInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "location_arn",
                "LocationARN",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
            (
                "default_storage_class",
                "DefaultStorageClass",
                TypeInfo(str),
            ),
            (
                "object_acl",
                "ObjectACL",
                TypeInfo(typing.Union[str, ObjectACL]),
            ),
            (
                "read_only",
                "ReadOnly",
                TypeInfo(bool),
            ),
            (
                "guess_mime_type_enabled",
                "GuessMIMETypeEnabled",
                TypeInfo(bool),
            ),
            (
                "requester_pays",
                "RequesterPays",
                TypeInfo(bool),
            ),
            (
                "valid_user_list",
                "ValidUserList",
                TypeInfo(typing.List[str]),
            ),
            (
                "invalid_user_list",
                "InvalidUserList",
                TypeInfo(typing.List[str]),
            ),
            (
                "authentication",
                "Authentication",
                TypeInfo(str),
            ),
        ]

    # A unique string value that you supply that is used by file gateway to
    # ensure idempotent file share creation.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the file gateway on which you want to
    # create a file share.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the AWS Identity and Access Management (IAM) role that a file
    # gateway assumes when it accesses the underlying storage.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the backed storage used for storing file data.
    location_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default storage class for objects put into an Amazon S3 bucket by the
    # file gateway. Possible values are `S3_STANDARD`, `S3_STANDARD_IA`, or
    # `S3_ONEZONE_IA`. If this field is not populated, the default value
    # `S3_STANDARD` is used. Optional.
    default_storage_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the access control list permission for objects in the S3
    # bucket that a file gateway puts objects into. The default value is
    # "private".
    object_acl: typing.Union[str, "ObjectACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the write status of a file share. This value is true if
    # the write status is read-only, and otherwise false.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that enables guessing of the MIME type for uploaded objects based
    # on file extensions. Set this value to true to enable MIME type guessing,
    # and otherwise to false. The default value is true.
    guess_mime_type_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the access control list permission for objects in the
    # Amazon S3 bucket that a file gateway puts objects into. The default value
    # is `private`.
    requester_pays: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of users or groups in the Active Directory that are allowed to
    # access the file share. A group must be prefixed with the @ character. For
    # example `@group1`. Can only be set if Authentication is set to
    # `ActiveDirectory`.
    valid_user_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of users or groups in the Active Directory that are not allowed to
    # access the file share. A group must be prefixed with the @ character. For
    # example `@group1`. Can only be set if Authentication is set to
    # `ActiveDirectory`.
    invalid_user_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authentication method that users use to access the file share.

    # Valid values are `ActiveDirectory` or `GuestAccess`. The default is
    # `ActiveDirectory`.
    authentication: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSMBFileShareOutput(OutputShapeBase):
    """
    CreateSMBFileShareOutput
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
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the newly created file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotFromVolumeRecoveryPointInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "snapshot_description",
                "SnapshotDescription",
                TypeInfo(str),
            ),
        ]

    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    snapshot_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotFromVolumeRecoveryPointOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "volume_recovery_point_time",
                "VolumeRecoveryPointTime",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_recovery_point_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSnapshotInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * CreateSnapshotInput$SnapshotDescription

      * CreateSnapshotInput$VolumeARN
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "snapshot_description",
                "SnapshotDescription",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation
    # to return a list of gateway volumes.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Textual description of the snapshot that appears in the Amazon EC2 console,
    # Elastic Block Store snapshots panel in the **Description** field, and in
    # the AWS Storage Gateway snapshot **Details** pane, **Description** field
    snapshot_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the volume of which the snapshot was
    # taken.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot ID that is used to refer to the snapshot in future operations
    # such as describing snapshots (Amazon Elastic Compute Cloud API
    # `DescribeSnapshots`) or creating a volume from a snapshot
    # (CreateStorediSCSIVolume).
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStorediSCSIVolumeInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * CreateStorediSCSIVolumeInput$DiskId

      * CreateStorediSCSIVolumeInput$NetworkInterfaceId

      * CreateStorediSCSIVolumeInput$PreserveExistingData

      * CreateStorediSCSIVolumeInput$SnapshotId

      * CreateStorediSCSIVolumeInput$TargetName
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_id",
                "DiskId",
                TypeInfo(str),
            ),
            (
                "preserve_existing_data",
                "PreserveExistingData",
                TypeInfo(bool),
            ),
            (
                "target_name",
                "TargetName",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the gateway local disk that is configured as a
    # stored volume. Use
    # [ListLocalDisks](http://docs.aws.amazon.com/storagegateway/latest/userguide/API_ListLocalDisks.html)
    # to list disk IDs for a gateway.
    disk_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify this field as true if you want to preserve the data on the local
    # disk. Otherwise, specifying this field as false creates an empty volume.

    # Valid Values: true, false
    preserve_existing_data: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the iSCSI target used by initiators to connect to the target
    # and as a suffix for the target ARN. For example, specifying `TargetName` as
    # _myvolume_ results in the target ARN of arn:aws:storagegateway:us-
    # east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume.
    # The target name must be unique across all volumes of a gateway.
    target_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network interface of the gateway on which to expose the iSCSI target.
    # Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a
    # list of the network interfaces available on a gateway.

    # Valid Values: A valid IP address.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the
    # new stored volume. Specify this field if you want to create the iSCSI
    # storage volume from a snapshot otherwise do not include this field. To list
    # snapshots for your account use
    # [DescribeSnapshots](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
    # query-DescribeSnapshots.html) in the _Amazon Elastic Compute Cloud API
    # Reference_.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStorediSCSIVolumeOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "volume_size_in_bytes",
                "VolumeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the configured volume.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the volume in bytes.
    volume_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # he Amazon Resource Name (ARN) of the volume target that includes the iSCSI
    # name that initiators can use to connect to the target.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTapeWithBarcodeInput(ShapeBase):
    """
    CreateTapeWithBarcodeInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_size_in_bytes",
                "TapeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "tape_barcode",
                "TapeBarcode",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The unique Amazon Resource Name (ARN) that represents the gateway to
    # associate the virtual tape with. Use the ListGateways operation to return a
    # list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of the virtual tape that you want to create.

    # The size must be aligned by gigabyte (1024*1024*1024 byte).
    tape_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The barcode that you want to assign to the tape.

    # Barcodes cannot be reused. This includes barcodes used for tapes that have
    # been deleted.
    tape_barcode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS Key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTapeWithBarcodeOutput(OutputShapeBase):
    """
    CreateTapeOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique Amazon Resource Name (ARN) that represents the virtual tape that
    # was created.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTapesInput(ShapeBase):
    """
    CreateTapesInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_size_in_bytes",
                "TapeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "num_tapes_to_create",
                "NumTapesToCreate",
                TypeInfo(int),
            ),
            (
                "tape_barcode_prefix",
                "TapeBarcodePrefix",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The unique Amazon Resource Name (ARN) that represents the gateway to
    # associate the virtual tapes with. Use the ListGateways operation to return
    # a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of the virtual tapes that you want to create.

    # The size must be aligned by gigabyte (1024*1024*1024 byte).
    tape_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that you use to retry a request. If you retry a
    # request, use the same `ClientToken` you specified in the initial request.

    # Using the same `ClientToken` prevents creating the tape multiple times.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of virtual tapes that you want to create.
    num_tapes_to_create: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A prefix that you append to the barcode of the virtual tape you are
    # creating. This prefix makes the barcode unique.

    # The prefix must be 1 to 4 characters in length and must be one of the
    # uppercase letters from A to Z.
    tape_barcode_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTapesOutput(OutputShapeBase):
    """
    CreateTapeOutput
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
                "tape_arns",
                "TapeARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of unique Amazon Resource Names (ARNs) that represents the virtual
    # tapes that were created.
    tape_arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBandwidthRateLimitInput(ShapeBase):
    """
    A JSON object containing the following fields:

      * DeleteBandwidthRateLimitInput$BandwidthType
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "bandwidth_type",
                "BandwidthType",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the BandwidthType values that indicates the gateway bandwidth rate
    # limit to delete.

    # Valid Values: `Upload`, `Download`, `All`.
    bandwidth_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBandwidthRateLimitOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway whose bandwidth rate information was
    deleted.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChapCredentialsInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * DeleteChapCredentialsInput$InitiatorName

      * DeleteChapCredentialsInput$TargetARN
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "initiator_name",
                "InitiatorName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
    # DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN
    # for specified VolumeARN.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The iSCSI initiator that connects to the target.
    initiator_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChapCredentialsOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "initiator_name",
                "InitiatorName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the target.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The iSCSI initiator that connects to the target.
    initiator_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFileShareInput(ShapeBase):
    """
    DeleteFileShareInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "force_delete",
                "ForceDelete",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the file share to be deleted.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this value is set to true, the operation deletes a file share
    # immediately and aborts all data uploads to AWS. Otherwise, the file share
    # is not deleted until all data is uploaded to AWS. This process aborts the
    # data upload process, and the file share enters the FORCE_DELETING status.
    force_delete: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFileShareOutput(OutputShapeBase):
    """
    DeleteFileShareOutput
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
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the deleted file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGatewayInput(ShapeBase):
    """
    A JSON object containing the ID of the gateway to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGatewayOutput(OutputShapeBase):
    """
    A JSON object containing the ID of the deleted gateway.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSnapshotScheduleInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSnapshotScheduleOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTapeArchiveInput(ShapeBase):
    """
    DeleteTapeArchiveInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the virtual tape to delete from the
    # virtual tape shelf (VTS).
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTapeArchiveOutput(OutputShapeBase):
    """
    DeleteTapeArchiveOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the virtual tape that was deleted from
    # the virtual tape shelf (VTS).
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTapeInput(ShapeBase):
    """
    DeleteTapeInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    # The unique Amazon Resource Name (ARN) of the gateway that the virtual tape
    # to delete is associated with. Use the ListGateways operation to return a
    # list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the virtual tape to delete.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTapeOutput(OutputShapeBase):
    """
    DeleteTapeOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the deleted virtual tape.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVolumeInput(ShapeBase):
    """
    A JSON object containing the DeleteVolumeInput$VolumeARN to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation
    # to return a list of gateway volumes.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVolumeOutput(OutputShapeBase):
    """
    A JSON object containing the of the storage volume that was deleted
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
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the storage volume that was deleted. It
    # is the same ARN you provided in the request.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBandwidthRateLimitInput(ShapeBase):
    """
    A JSON object containing the of the gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBandwidthRateLimitOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "average_upload_rate_limit_in_bits_per_sec",
                "AverageUploadRateLimitInBitsPerSec",
                TypeInfo(int),
            ),
            (
                "average_download_rate_limit_in_bits_per_sec",
                "AverageDownloadRateLimitInBitsPerSec",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The average upload bandwidth rate limit in bits per second. This field does
    # not appear in the response if the upload rate limit is not set.
    average_upload_rate_limit_in_bits_per_sec: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The average download bandwidth rate limit in bits per second. This field
    # does not appear in the response if the download rate limit is not set.
    average_download_rate_limit_in_bits_per_sec: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCacheInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCacheOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_ids",
                "DiskIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "cache_allocated_in_bytes",
                "CacheAllocatedInBytes",
                TypeInfo(int),
            ),
            (
                "cache_used_percentage",
                "CacheUsedPercentage",
                TypeInfo(float),
            ),
            (
                "cache_dirty_percentage",
                "CacheDirtyPercentage",
                TypeInfo(float),
            ),
            (
                "cache_hit_percentage",
                "CacheHitPercentage",
                TypeInfo(float),
            ),
            (
                "cache_miss_percentage",
                "CacheMissPercentage",
                TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
    cache_allocated_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    cache_used_percentage: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    cache_dirty_percentage: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    cache_hit_percentage: float = dataclasses.field(default=ShapeBase.NOT_SET, )
    cache_miss_percentage: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCachediSCSIVolumesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arns",
                "VolumeARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    volume_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCachediSCSIVolumesOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "cachedi_scsi_volumes",
                "CachediSCSIVolumes",
                TypeInfo(typing.List[CachediSCSIVolume]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of objects where each object contains metadata about one cached
    # volume.
    cachedi_scsi_volumes: typing.List["CachediSCSIVolume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeChapCredentialsInput(ShapeBase):
    """
    A JSON object containing the Amazon Resource Name (ARN) of the iSCSI volume
    target.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
    # DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN
    # for specified VolumeARN.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChapCredentialsOutput(OutputShapeBase):
    """
    A JSON object containing a .
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
                "chap_credentials",
                "ChapCredentials",
                TypeInfo(typing.List[ChapInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of ChapInfo objects that represent CHAP credentials. Each object
    # in the array contains CHAP credential information for one target-initiator
    # pair. If no CHAP credentials are set, an empty array is returned. CHAP
    # credential information is provided in a JSON object with the following
    # fields:

    #   * **InitiatorName** : The iSCSI initiator that connects to the target.

    #   * **SecretToAuthenticateInitiator** : The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.

    #   * **SecretToAuthenticateTarget** : The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).

    #   * **TargetARN** : The Amazon Resource Name (ARN) of the storage volume.
    chap_credentials: typing.List["ChapInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeGatewayInformationInput(ShapeBase):
    """
    A JSON object containing the ID of the gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGatewayInformationOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "gateway_id",
                "GatewayId",
                TypeInfo(str),
            ),
            (
                "gateway_name",
                "GatewayName",
                TypeInfo(str),
            ),
            (
                "gateway_timezone",
                "GatewayTimezone",
                TypeInfo(str),
            ),
            (
                "gateway_state",
                "GatewayState",
                TypeInfo(str),
            ),
            (
                "gateway_network_interfaces",
                "GatewayNetworkInterfaces",
                TypeInfo(typing.List[NetworkInterface]),
            ),
            (
                "gateway_type",
                "GatewayType",
                TypeInfo(str),
            ),
            (
                "next_update_availability_date",
                "NextUpdateAvailabilityDate",
                TypeInfo(str),
            ),
            (
                "last_software_update",
                "LastSoftwareUpdate",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier assigned to your gateway during activation. This ID
    # becomes part of the gateway Amazon Resource Name (ARN), which you use as
    # input for other operations.
    gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name you configured for your gateway.
    gateway_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the time zone configured for the gateway.
    gateway_timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that indicates the operating state of the gateway.
    gateway_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A NetworkInterface array that contains descriptions of the gateway network
    # interfaces.
    gateway_network_interfaces: typing.List["NetworkInterface"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # The type of the gateway.
    gateway_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date on which an update to the gateway is available. This date is in
    # the time zone of the gateway. If the gateway is not available for an update
    # this field is not returned in the response.
    next_update_availability_date: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date on which the last software update was applied to the gateway. If
    # the gateway has never been updated, this field does not return a value in
    # the response.
    last_software_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceStartTimeInput(ShapeBase):
    """
    A JSON object containing the of the gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMaintenanceStartTimeOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:

      * DescribeMaintenanceStartTimeOutput$DayOfWeek

      * DescribeMaintenanceStartTimeOutput$HourOfDay

      * DescribeMaintenanceStartTimeOutput$MinuteOfHour

      * DescribeMaintenanceStartTimeOutput$Timezone
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "hour_of_day",
                "HourOfDay",
                TypeInfo(int),
            ),
            (
                "minute_of_hour",
                "MinuteOfHour",
                TypeInfo(int),
            ),
            (
                "day_of_week",
                "DayOfWeek",
                TypeInfo(int),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hour component of the maintenance start time represented as _hh_ ,
    # where _hh_ is the hour (0 to 23). The hour of the day is in the time zone
    # of the gateway.
    hour_of_day: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minute component of the maintenance start time represented as _mm_ ,
    # where _mm_ is the minute (0 to 59). The minute of the hour is in the time
    # zone of the gateway.
    minute_of_hour: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ordinal number between 0 and 6 that represents the day of the week,
    # where 0 represents Sunday and 6 represents Saturday. The day of week is in
    # the time zone of the gateway.
    day_of_week: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNFSFileSharesInput(ShapeBase):
    """
    DescribeNFSFileSharesInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn_list",
                "FileShareARNList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # An array containing the Amazon Resource Name (ARN) of each file share to be
    # described.
    file_share_arn_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNFSFileSharesOutput(OutputShapeBase):
    """
    DescribeNFSFileSharesOutput
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
                "nfs_file_share_info_list",
                "NFSFileShareInfoList",
                TypeInfo(typing.List[NFSFileShareInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array containing a description for each requested file share.
    nfs_file_share_info_list: typing.List["NFSFileShareInfo"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class DescribeSMBFileSharesInput(ShapeBase):
    """
    DescribeSMBFileSharesInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn_list",
                "FileShareARNList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # An array containing the Amazon Resource Name (ARN) of each file share to be
    # described.
    file_share_arn_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSMBFileSharesOutput(OutputShapeBase):
    """
    DescribeSMBFileSharesOutput
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
                "smb_file_share_info_list",
                "SMBFileShareInfoList",
                TypeInfo(typing.List[SMBFileShareInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array containing a description for each requested file share.
    smb_file_share_info_list: typing.List["SMBFileShareInfo"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class DescribeSMBSettingsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSMBSettingsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "smb_guest_password_set",
                "SMBGuestPasswordSet",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the domain that the gateway is joined to.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is true if a password for the guest user “smbguest” is set, and
    # otherwise false.
    smb_guest_password_set: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSnapshotScheduleInput(ShapeBase):
    """
    A JSON object containing the DescribeSnapshotScheduleInput$VolumeARN of the
    volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation
    # to return a list of gateway volumes.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSnapshotScheduleOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "start_at",
                "StartAt",
                TypeInfo(int),
            ),
            (
                "recurrence_in_hours",
                "RecurrenceInHours",
                TypeInfo(int),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    start_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    recurrence_in_hours: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStorediSCSIVolumesInput(ShapeBase):
    """
    A JSON object containing a list of DescribeStorediSCSIVolumesInput$VolumeARNs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arns",
                "VolumeARNs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # An array of strings where each string represents the Amazon Resource Name
    # (ARN) of a stored volume. All of the specified stored volumes must from the
    # same gateway. Use ListVolumes to get volume ARNs for a gateway.
    volume_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStorediSCSIVolumesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "storedi_scsi_volumes",
                "StorediSCSIVolumes",
                TypeInfo(typing.List[StorediSCSIVolume]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    storedi_scsi_volumes: typing.List["StorediSCSIVolume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTapeArchivesInput(ShapeBase):
    """
    DescribeTapeArchivesInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arns",
                "TapeARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # Specifies one or more unique Amazon Resource Names (ARNs) that represent
    # the virtual tapes you want to describe.
    tape_arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An opaque string that indicates the position at which to begin describing
    # virtual tapes.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the number of virtual tapes descried be limited to the
    # specified number.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTapeArchivesOutput(OutputShapeBase):
    """
    DescribeTapeArchivesOutput
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
                "tape_archives",
                "TapeArchives",
                TypeInfo(typing.List[TapeArchive]),
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

    # An array of virtual tape objects in the virtual tape shelf (VTS). The
    # description includes of the Amazon Resource Name (ARN) of the virtual
    # tapes. The information returned includes the Amazon Resource Names (ARNs)
    # of the tapes, size of the tapes, status of the tapes, progress of the
    # description and tape barcode.
    tape_archives: typing.List["TapeArchive"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An opaque string that indicates the position at which the virtual tapes
    # that were fetched for description ended. Use this marker in your next
    # request to fetch the next set of virtual tapes in the virtual tape shelf
    # (VTS). If there are no more virtual tapes to describe, this field does not
    # appear in the response.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeTapeArchivesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeTapeRecoveryPointsInput(ShapeBase):
    """
    DescribeTapeRecoveryPointsInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An opaque string that indicates the position at which to begin describing
    # the virtual tape recovery points.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the number of virtual tape recovery points that are
    # described be limited to the specified number.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTapeRecoveryPointsOutput(OutputShapeBase):
    """
    DescribeTapeRecoveryPointsOutput
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_recovery_point_infos",
                "TapeRecoveryPointInfos",
                TypeInfo(typing.List[TapeRecoveryPointInfo]),
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

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of TapeRecoveryPointInfos that are available for the specified
    # gateway.
    tape_recovery_point_infos: typing.List["TapeRecoveryPointInfo"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # An opaque string that indicates the position at which the virtual tape
    # recovery points that were listed for description ended.

    # Use this marker in your next request to list the next set of virtual tape
    # recovery points in the list. If there are no more recovery points to
    # describe, this field does not appear in the response.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeTapeRecoveryPointsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeTapesInput(ShapeBase):
    """
    DescribeTapesInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "tape_arns",
                "TapeARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies one or more unique Amazon Resource Names (ARNs) that represent
    # the virtual tapes you want to describe. If this parameter is not specified,
    # Tape gateway returns a description of all virtual tapes associated with the
    # specified gateway.
    tape_arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A marker value, obtained in a previous call to `DescribeTapes`. This marker
    # indicates which page of results to retrieve.

    # If not specified, the first page of results is retrieved.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the number of virtual tapes described be limited to the
    # specified number.

    # Amazon Web Services may impose its own limit, if this field is not set.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTapesOutput(OutputShapeBase):
    """
    DescribeTapesOutput
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
                "tapes",
                "Tapes",
                TypeInfo(typing.List[Tape]),
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

    # An array of virtual tape descriptions.
    tapes: typing.List["Tape"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An opaque string which can be used as part of a subsequent DescribeTapes
    # call to retrieve the next page of results.

    # If a response does not contain a marker, then there are no more results to
    # be retrieved.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["DescribeTapesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeUploadBufferInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeUploadBufferOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_ids",
                "DiskIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "upload_buffer_used_in_bytes",
                "UploadBufferUsedInBytes",
                TypeInfo(int),
            ),
            (
                "upload_buffer_allocated_in_bytes",
                "UploadBufferAllocatedInBytes",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
    upload_buffer_used_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    upload_buffer_allocated_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeVTLDevicesInput(ShapeBase):
    """
    DescribeVTLDevicesInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "vtl_device_arns",
                "VTLDeviceARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings, where each string represents the Amazon Resource Name
    # (ARN) of a VTL device.

    # All of the specified VTL devices must be from the same gateway. If no VTL
    # devices are specified, the result will contain all devices on the specified
    # gateway.
    vtl_device_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An opaque string that indicates the position at which to begin describing
    # the VTL devices.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the number of VTL devices described be limited to the
    # specified number.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeVTLDevicesOutput(OutputShapeBase):
    """
    DescribeVTLDevicesOutput
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "vtl_devices",
                "VTLDevices",
                TypeInfo(typing.List[VTLDevice]),
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

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of VTL device objects composed of the Amazon Resource Name(ARN) of
    # the VTL devices.
    vtl_devices: typing.List["VTLDevice"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An opaque string that indicates the position at which the VTL devices that
    # were fetched for description ended. Use the marker in your next request to
    # fetch the next set of VTL devices in the list. If there are no more VTL
    # devices to describe, this field does not appear in the response.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeVTLDevicesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeWorkingStorageInput(ShapeBase):
    """
    A JSON object containing the of the gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeWorkingStorageOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disk_ids",
                "DiskIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "working_storage_used_in_bytes",
                "WorkingStorageUsedInBytes",
                TypeInfo(int),
            ),
            (
                "working_storage_allocated_in_bytes",
                "WorkingStorageAllocatedInBytes",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of the gateway's local disk IDs that are configured as working
    # storage. Each local disk ID is specified as a string (minimum length of 1
    # and maximum length of 300). If no local disks are configured as working
    # storage, then the DiskIds array is empty.
    disk_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total working storage in bytes in use by the gateway. If no working
    # storage is configured for the gateway, this field returns 0.
    working_storage_used_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total working storage in bytes allocated for the gateway. If no working
    # storage is configured for the gateway, this field returns 0.
    working_storage_allocated_in_bytes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeviceiSCSIAttributes(ShapeBase):
    """
    Lists iSCSI information about a VTL device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
            (
                "network_interface_port",
                "NetworkInterfacePort",
                TypeInfo(int),
            ),
            (
                "chap_enabled",
                "ChapEnabled",
                TypeInfo(bool),
            ),
        ]

    # Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI
    # qualified name(iqn) of a tape drive or media changer target.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network interface identifier of the VTL device.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port used to communicate with iSCSI VTL device targets.
    network_interface_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether mutual CHAP is enabled for the iSCSI target.
    chap_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableGatewayInput(ShapeBase):
    """
    DisableGatewayInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableGatewayOutput(OutputShapeBase):
    """
    DisableGatewayOutput
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique Amazon Resource Name (ARN) of the disabled gateway.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Disk(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_id",
                "DiskId",
                TypeInfo(str),
            ),
            (
                "disk_path",
                "DiskPath",
                TypeInfo(str),
            ),
            (
                "disk_node",
                "DiskNode",
                TypeInfo(str),
            ),
            (
                "disk_status",
                "DiskStatus",
                TypeInfo(str),
            ),
            (
                "disk_size_in_bytes",
                "DiskSizeInBytes",
                TypeInfo(int),
            ),
            (
                "disk_allocation_type",
                "DiskAllocationType",
                TypeInfo(str),
            ),
            (
                "disk_allocation_resource",
                "DiskAllocationResource",
                TypeInfo(str),
            ),
        ]

    disk_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_node: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_allocation_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disk_allocation_resource: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ErrorCode(str):
    ActivationKeyExpired = "ActivationKeyExpired"
    ActivationKeyInvalid = "ActivationKeyInvalid"
    ActivationKeyNotFound = "ActivationKeyNotFound"
    GatewayInternalError = "GatewayInternalError"
    GatewayNotConnected = "GatewayNotConnected"
    GatewayNotFound = "GatewayNotFound"
    GatewayProxyNetworkConnectionBusy = "GatewayProxyNetworkConnectionBusy"
    AuthenticationFailure = "AuthenticationFailure"
    BandwidthThrottleScheduleNotFound = "BandwidthThrottleScheduleNotFound"
    Blocked = "Blocked"
    CannotExportSnapshot = "CannotExportSnapshot"
    ChapCredentialNotFound = "ChapCredentialNotFound"
    DiskAlreadyAllocated = "DiskAlreadyAllocated"
    DiskDoesNotExist = "DiskDoesNotExist"
    DiskSizeGreaterThanVolumeMaxSize = "DiskSizeGreaterThanVolumeMaxSize"
    DiskSizeLessThanVolumeSize = "DiskSizeLessThanVolumeSize"
    DiskSizeNotGigAligned = "DiskSizeNotGigAligned"
    DuplicateCertificateInfo = "DuplicateCertificateInfo"
    DuplicateSchedule = "DuplicateSchedule"
    EndpointNotFound = "EndpointNotFound"
    IAMNotSupported = "IAMNotSupported"
    InitiatorInvalid = "InitiatorInvalid"
    InitiatorNotFound = "InitiatorNotFound"
    InternalError = "InternalError"
    InvalidGateway = "InvalidGateway"
    InvalidEndpoint = "InvalidEndpoint"
    InvalidParameters = "InvalidParameters"
    InvalidSchedule = "InvalidSchedule"
    LocalStorageLimitExceeded = "LocalStorageLimitExceeded"
    LunAlreadyAllocated_ = "LunAlreadyAllocated "
    LunInvalid = "LunInvalid"
    MaximumContentLengthExceeded = "MaximumContentLengthExceeded"
    MaximumTapeCartridgeCountExceeded = "MaximumTapeCartridgeCountExceeded"
    MaximumVolumeCountExceeded = "MaximumVolumeCountExceeded"
    NetworkConfigurationChanged = "NetworkConfigurationChanged"
    NoDisksAvailable = "NoDisksAvailable"
    NotImplemented = "NotImplemented"
    NotSupported = "NotSupported"
    OperationAborted = "OperationAborted"
    OutdatedGateway = "OutdatedGateway"
    ParametersNotImplemented = "ParametersNotImplemented"
    RegionInvalid = "RegionInvalid"
    RequestTimeout = "RequestTimeout"
    ServiceUnavailable = "ServiceUnavailable"
    SnapshotDeleted = "SnapshotDeleted"
    SnapshotIdInvalid = "SnapshotIdInvalid"
    SnapshotInProgress = "SnapshotInProgress"
    SnapshotNotFound = "SnapshotNotFound"
    SnapshotScheduleNotFound = "SnapshotScheduleNotFound"
    StagingAreaFull = "StagingAreaFull"
    StorageFailure = "StorageFailure"
    TapeCartridgeNotFound = "TapeCartridgeNotFound"
    TargetAlreadyExists = "TargetAlreadyExists"
    TargetInvalid = "TargetInvalid"
    TargetNotFound = "TargetNotFound"
    UnauthorizedOperation = "UnauthorizedOperation"
    VolumeAlreadyExists = "VolumeAlreadyExists"
    VolumeIdInvalid = "VolumeIdInvalid"
    VolumeInUse = "VolumeInUse"
    VolumeNotFound = "VolumeNotFound"
    VolumeNotReady = "VolumeNotReady"


@dataclasses.dataclass
class FileShareInfo(ShapeBase):
    """
    Describes a file share.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_type",
                "FileShareType",
                TypeInfo(typing.Union[str, FileShareType]),
            ),
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "file_share_id",
                "FileShareId",
                TypeInfo(str),
            ),
            (
                "file_share_status",
                "FileShareStatus",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The type of the file share.
    file_share_type: typing.Union[str, "FileShareType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the file share.
    file_share_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the file share. Possible values are `CREATING`, `UPDATING`,
    # `AVAILABLE` and `DELETING`.
    file_share_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FileShareType(str):
    """
    The type of the file share.
    """
    NFS = "NFS"
    SMB = "SMB"


@dataclasses.dataclass
class GatewayInfo(ShapeBase):
    """
    Describes a gateway object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_id",
                "GatewayId",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "gateway_type",
                "GatewayType",
                TypeInfo(str),
            ),
            (
                "gateway_operational_state",
                "GatewayOperationalState",
                TypeInfo(str),
            ),
            (
                "gateway_name",
                "GatewayName",
                TypeInfo(str),
            ),
        ]

    # The unique identifier assigned to your gateway during activation. This ID
    # becomes part of the gateway Amazon Resource Name (ARN), which you use as
    # input for other operations.
    gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the gateway.
    gateway_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the gateway.

    # Valid Values: DISABLED or ACTIVE
    gateway_operational_state: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the gateway.
    gateway_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    An internal server error has occurred during the request. For more information,
    see the error and message fields.
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
                "error",
                "error",
                TypeInfo(StorageGatewayError),
            ),
        ]

    # A human-readable message describing the error that occurred.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A StorageGatewayError that provides more information about the cause of the
    # error.
    error: "StorageGatewayError" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidGatewayRequestException(ShapeBase):
    """
    An exception occurred because an invalid gateway request was issued to the
    service. For more information, see the error and message fields.
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
                "error",
                "error",
                TypeInfo(StorageGatewayError),
            ),
        ]

    # A human-readable message describing the error that occurred.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A StorageGatewayError that provides more detail about the cause of the
    # error.
    error: "StorageGatewayError" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JoinDomainInput(ShapeBase):
    """
    JoinDomainInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The unique Amazon Resource Name (ARN) of the file gateway you want to add
    # to the Active Directory domain.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the domain that you want the gateway to join.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the user name of user who has permission to add the gateway to the
    # Active Directory domain.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the password of the user who has permission to add the gateway to the
    # Active Directory domain.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JoinDomainOutput(OutputShapeBase):
    """
    JoinDomainOutput
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique Amazon Resource Name (ARN) of the gateway that joined the
    # domain.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFileSharesInput(ShapeBase):
    """
    ListFileShareInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # The Amazon resource Name (ARN) of the gateway whose file shares you want to
    # list. If this field is not present, all file shares under your account are
    # listed.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of file shares to return in the response. The value must
    # be an integer with a value greater than zero. Optional.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Opaque pagination token returned from a previous ListFileShares operation.
    # If present, `Marker` specifies where to continue the list from after a
    # previous call to ListFileShares. Optional.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFileSharesOutput(OutputShapeBase):
    """
    ListFileShareOutput
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
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "file_share_info_list",
                "FileShareInfoList",
                TypeInfo(typing.List[FileShareInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the request includes `Marker`, the response returns that value in this
    # field.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a value is present, there are more file shares to return. In a
    # subsequent request, use `NextMarker` as the value for `Marker` to retrieve
    # the next set of file shares.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of information about the file gateway's file shares.
    file_share_info_list: typing.List["FileShareInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListGatewaysInput(ShapeBase):
    """
    A JSON object containing zero or more of the following fields:

      * ListGatewaysInput$Limit

      * ListGatewaysInput$Marker
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # An opaque string that indicates the position at which to begin the returned
    # list of gateways.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the list of gateways returned be limited to the specified
    # number of items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGatewaysOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateways",
                "Gateways",
                TypeInfo(typing.List[GatewayInfo]),
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
    gateways: typing.List["GatewayInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListGatewaysOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListLocalDisksInput(ShapeBase):
    """
    A JSON object containing the of the gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLocalDisksOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "disks",
                "Disks",
                TypeInfo(typing.List[Disk]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    disks: typing.List["Disk"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceInput(ShapeBase):
    """
    ListTagsForResourceInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource for which you want to list
    # tags.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An opaque string that indicates the position at which to begin returning
    # the list of tags.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the list of tags returned be limited to the specified number
    # of items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceOutput(OutputShapeBase):
    """
    ListTagsForResourceOutput
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
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # he Amazon Resource Name (ARN) of the resource for which you want to list
    # tags.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An opaque string that indicates the position at which to stop returning the
    # list of tags.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array that contains the tags for the specified resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTapesInput(ShapeBase):
    """
    A JSON object that contains one or more of the following fields:

      * ListTapesInput$Limit

      * ListTapesInput$Marker

      * ListTapesInput$TapeARNs
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arns",
                "TapeARNs",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of each of the tapes you want to list. If
    # you don't specify a tape ARN, the response lists all tapes in both your VTL
    # and VTS.
    tape_arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that indicates the position at which to begin the returned list of
    # tapes.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional number limit for the tapes in the list returned by this call.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTapesOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:

      * ListTapesOutput$Marker

      * ListTapesOutput$VolumeInfos
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
                "tape_infos",
                "TapeInfos",
                TypeInfo(typing.List[TapeInfo]),
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

    # An array of TapeInfo objects, where each object describes an a single tape.
    # If there not tapes in the tape library or VTS, then the `TapeInfos` is an
    # empty array.
    tape_infos: typing.List["TapeInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string that indicates the position at which to begin returning the next
    # list of tapes. Use the marker in your next request to continue pagination
    # of tapes. If there are no more tapes to list, this element does not appear
    # in the response body.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVolumeInitiatorsInput(ShapeBase):
    """
    ListVolumeInitiatorsInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation
    # to return a list of gateway volumes for the gateway.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVolumeInitiatorsOutput(OutputShapeBase):
    """
    ListVolumeInitiatorsOutput
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
                "initiators",
                "Initiators",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The host names and port numbers of all iSCSI initiators that are connected
    # to the gateway.
    initiators: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListVolumeRecoveryPointsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVolumeRecoveryPointsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "volume_recovery_point_infos",
                "VolumeRecoveryPointInfos",
                TypeInfo(typing.List[VolumeRecoveryPointInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_recovery_point_infos: typing.List["VolumeRecoveryPointInfo"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class ListVolumesInput(ShapeBase):
    """
    A JSON object that contains one or more of the following fields:

      * ListVolumesInput$Limit

      * ListVolumesInput$Marker
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that indicates the position at which to begin the returned list of
    # volumes. Obtain the marker from the response of a previous List iSCSI
    # Volumes request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that the list of volumes returned be limited to the specified
    # number of items.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVolumesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "volume_infos",
                "VolumeInfos",
                TypeInfo(typing.List[VolumeInfo]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_infos: typing.List["VolumeInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ListVolumesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NFSFileShareDefaults(ShapeBase):
    """
    Describes Network File System (NFS) file share default values. Files and folders
    stored as Amazon S3 objects in S3 buckets don't, by default, have Unix file
    permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway,
    the S3 objects that represent files and folders are assigned these default Unix
    permissions. This operation is only supported for file gateways.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_mode",
                "FileMode",
                TypeInfo(str),
            ),
            (
                "directory_mode",
                "DirectoryMode",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(int),
            ),
            (
                "owner_id",
                "OwnerId",
                TypeInfo(int),
            ),
        ]

    # The Unix file mode in the form "nnnn". For example, "0666" represents the
    # default file mode inside the file share. The default value is 0666.
    file_mode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix directory mode in the form "nnnn". For example, "0666" represents
    # the default access mode for all directories inside the file share. The
    # default value is 0777.
    directory_mode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default group ID for the file share (unless the files have another
    # group ID specified). The default value is nfsnobody.
    group_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default owner ID for files in the file share (unless the files have
    # another owner ID specified). The default value is nfsnobody.
    owner_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NFSFileShareInfo(ShapeBase):
    """
    The Unix file permissions and ownership information assigned, by default, to
    native S3 objects when file gateway discovers them in S3 buckets. This operation
    is only supported in file gateways.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "nfs_file_share_defaults",
                "NFSFileShareDefaults",
                TypeInfo(NFSFileShareDefaults),
            ),
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "file_share_id",
                "FileShareId",
                TypeInfo(str),
            ),
            (
                "file_share_status",
                "FileShareStatus",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "location_arn",
                "LocationARN",
                TypeInfo(str),
            ),
            (
                "default_storage_class",
                "DefaultStorageClass",
                TypeInfo(str),
            ),
            (
                "object_acl",
                "ObjectACL",
                TypeInfo(typing.Union[str, ObjectACL]),
            ),
            (
                "client_list",
                "ClientList",
                TypeInfo(typing.List[str]),
            ),
            (
                "squash",
                "Squash",
                TypeInfo(str),
            ),
            (
                "read_only",
                "ReadOnly",
                TypeInfo(bool),
            ),
            (
                "guess_mime_type_enabled",
                "GuessMIMETypeEnabled",
                TypeInfo(bool),
            ),
            (
                "requester_pays",
                "RequesterPays",
                TypeInfo(bool),
            ),
        ]

    # Describes Network File System (NFS) file share default values. Files and
    # folders stored as Amazon S3 objects in S3 buckets don't, by default, have
    # Unix file permissions assigned to them. Upon discovery in an S3 bucket by
    # Storage Gateway, the S3 objects that represent files and folders are
    # assigned these default Unix permissions. This operation is only supported
    # for file gateways.
    nfs_file_share_defaults: "NFSFileShareDefaults" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the file share.
    file_share_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the file share. Possible values are `CREATING`, `UPDATING`,
    # `AVAILABLE` and `DELETING`.
    file_share_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file share path used by the NFS client to identify the mount point.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role that file gateway assumes when it accesses the
    # underlying storage.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the backend storage used for storing file data.
    location_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default storage class for objects put into an Amazon S3 bucket by the
    # file gateway. Possible values are `S3_STANDARD`, `S3_STANDARD_IA`, or
    # `S3_ONEZONE_IA`. If this field is not populated, the default value
    # `S3_STANDARD` is used. Optional.
    default_storage_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the access control list permission for objects in the S3
    # bucket that a file gateway puts objects into. The default value is
    # "private".
    object_acl: typing.Union[str, "ObjectACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of clients that are allowed to access the file gateway. The list
    # must contain either valid IP addresses or valid CIDR blocks.
    client_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user mapped to anonymous user. Valid options are the following:

    #   * `RootSquash` \- Only root is mapped to anonymous user.

    #   * `NoSquash` \- No one is mapped to anonymous user

    #   * `AllSquash` \- Everyone is mapped to anonymous user.
    squash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the write status of a file share. This value is true if
    # the write status is read-only, and otherwise false.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that enables guessing of the MIME type for uploaded objects based
    # on file extensions. Set this value to true to enable MIME type guessing,
    # and otherwise to false. The default value is true.
    guess_mime_type_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the access control list permission for objects in the
    # Amazon S3 bucket that a file gateway puts objects into. The default value
    # is `private`.
    requester_pays: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkInterface(ShapeBase):
    """
    Describes a gateway's network interface.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ipv4_address",
                "Ipv4Address",
                TypeInfo(str),
            ),
            (
                "mac_address",
                "MacAddress",
                TypeInfo(str),
            ),
            (
                "ipv6_address",
                "Ipv6Address",
                TypeInfo(str),
            ),
        ]

    # The Internet Protocol version 4 (IPv4) address of the interface.
    ipv4_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Media Access Control (MAC) address of the interface.

    # This is currently unsupported and will not be returned in output.
    mac_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Internet Protocol version 6 (IPv6) address of the interface. _Currently
    # not supported_.
    ipv6_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotifyWhenUploadedInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotifyWhenUploadedOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "notification_id",
                "NotificationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The randomly generated ID of the notification that was sent. This ID is in
    # UUID format.
    notification_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ObjectACL(str):
    """
    A value that sets the access control list permission for objects in the S3
    bucket that a file gateway puts objects into. The default value is "private".
    """
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"
    bucket_owner_read = "bucket-owner-read"
    bucket_owner_full_control = "bucket-owner-full-control"
    aws_exec_read = "aws-exec-read"


@dataclasses.dataclass
class RefreshCacheInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RefreshCacheOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceInput(ShapeBase):
    """
    RemoveTagsFromResourceInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource you want to remove the tags
    # from.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The keys of the tags you want to remove from the specified resource. A tag
    # is composed of a key/value pair.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceOutput(OutputShapeBase):
    """
    RemoveTagsFromResourceOutput
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
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the resource that the tags were removed
    # from.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetCacheInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetCacheOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetrieveTapeArchiveInput(ShapeBase):
    """
    RetrieveTapeArchiveInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the virtual tape you want to retrieve
    # from the virtual tape shelf (VTS).
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway you want to retrieve the
    # virtual tape to. Use the ListGateways operation to return a list of
    # gateways for your account and region.

    # You retrieve archived virtual tapes to only one gateway and the gateway
    # must be a tape gateway.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetrieveTapeArchiveOutput(OutputShapeBase):
    """
    RetrieveTapeArchiveOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the retrieved virtual tape.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetrieveTapeRecoveryPointInput(ShapeBase):
    """
    RetrieveTapeRecoveryPointInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the virtual tape for which you want to
    # retrieve the recovery point.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetrieveTapeRecoveryPointOutput(OutputShapeBase):
    """
    RetrieveTapeRecoveryPointOutput
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
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the virtual tape for which the recovery
    # point was retrieved.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SMBFileShareInfo(ShapeBase):
    """
    The Windows file permissions and ownership information assigned, by default, to
    native S3 objects when file gateway discovers them in S3 buckets. This operation
    is only supported for file gateways.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "file_share_id",
                "FileShareId",
                TypeInfo(str),
            ),
            (
                "file_share_status",
                "FileShareStatus",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "location_arn",
                "LocationARN",
                TypeInfo(str),
            ),
            (
                "default_storage_class",
                "DefaultStorageClass",
                TypeInfo(str),
            ),
            (
                "object_acl",
                "ObjectACL",
                TypeInfo(typing.Union[str, ObjectACL]),
            ),
            (
                "read_only",
                "ReadOnly",
                TypeInfo(bool),
            ),
            (
                "guess_mime_type_enabled",
                "GuessMIMETypeEnabled",
                TypeInfo(bool),
            ),
            (
                "requester_pays",
                "RequesterPays",
                TypeInfo(bool),
            ),
            (
                "valid_user_list",
                "ValidUserList",
                TypeInfo(typing.List[str]),
            ),
            (
                "invalid_user_list",
                "InvalidUserList",
                TypeInfo(typing.List[str]),
            ),
            (
                "authentication",
                "Authentication",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the file share.
    file_share_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the file share. Possible values are `CREATING`, `UPDATING`,
    # `AVAILABLE` and `DELETING`.
    file_share_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server-side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file share path used by the SMB client to identify the mount point.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role that file gateway assumes when it accesses the
    # underlying storage.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the backend storage used for storing file data.
    location_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default storage class for objects put into an Amazon S3 bucket by the
    # file gateway. Possible values are `S3_STANDARD`, `S3_STANDARD_IA`, or
    # `S3_ONEZONE_IA`. If this field is not populated, the default value
    # `S3_STANDARD` is used. Optional.
    default_storage_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the access control list permission for objects in the S3
    # bucket that a file gateway puts objects into. The default value is
    # "private".
    object_acl: typing.Union[str, "ObjectACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the write status of a file share. This value is true if
    # the write status is read-only, and otherwise false.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that enables guessing of the MIME type for uploaded objects based
    # on file extensions. Set this value to true to enable MIME type guessing,
    # and otherwise to false. The default value is true.
    guess_mime_type_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the access control list permission for objects in the
    # Amazon S3 bucket that a file gateway puts objects into. The default value
    # is `private`.
    requester_pays: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of users or groups in the Active Directory that are allowed to
    # access the file share. A group must be prefixed with the @ character. For
    # example `@group1`. Can only be set if Authentication is set to
    # `ActiveDirectory`.
    valid_user_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of users or groups in the Active Directory that are not allowed to
    # access the file share. A group must be prefixed with the @ character. For
    # example `@group1`. Can only be set if Authentication is set to
    # `ActiveDirectory`.
    invalid_user_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authentication method of the file share.

    # Valid values are `ActiveDirectory` or `GuestAccess`. The default is
    # `ActiveDirectory`.
    authentication: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceUnavailableError(ShapeBase):
    """
    An internal server error has occurred because the service is unavailable. For
    more information, see the error and message fields.
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
                "error",
                "error",
                TypeInfo(StorageGatewayError),
            ),
        ]

    # A human-readable message describing the error that occurred.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A StorageGatewayError that provides more information about the cause of the
    # error.
    error: "StorageGatewayError" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetLocalConsolePasswordInput(ShapeBase):
    """
    SetLocalConsolePasswordInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "local_console_password",
                "LocalConsolePassword",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password you want to set for your VM local console.
    local_console_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetLocalConsolePasswordOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetSMBGuestPasswordInput(ShapeBase):
    """
    SetSMBGuestPasswordInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the file gateway the SMB file share is
    # associated with.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password that you want to set for your SMB Server.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetSMBGuestPasswordOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ShutdownGatewayInput(ShapeBase):
    """
    A JSON object containing the of the gateway to shut down.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ShutdownGatewayOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway that was shut down.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartGatewayInput(ShapeBase):
    """
    A JSON object containing the of the gateway to start.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartGatewayOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway that was restarted.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StorageGatewayError(ShapeBase):
    """
    Provides additional information about an error that was returned by the service
    as an or. See the `errorCode` and `errorDetails` members for more information
    about the error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "errorCode",
                TypeInfo(typing.Union[str, ErrorCode]),
            ),
            (
                "error_details",
                "errorDetails",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Additional information about the error.
    error_code: typing.Union[str, "ErrorCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human-readable text that provides detail about the error that occurred.
    error_details: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StorediSCSIVolume(ShapeBase):
    """
    Describes an iSCSI stored volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "volume_id",
                "VolumeId",
                TypeInfo(str),
            ),
            (
                "volume_type",
                "VolumeType",
                TypeInfo(str),
            ),
            (
                "volume_status",
                "VolumeStatus",
                TypeInfo(str),
            ),
            (
                "volume_size_in_bytes",
                "VolumeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "volume_progress",
                "VolumeProgress",
                TypeInfo(float),
            ),
            (
                "volume_disk_id",
                "VolumeDiskId",
                TypeInfo(str),
            ),
            (
                "source_snapshot_id",
                "SourceSnapshotId",
                TypeInfo(str),
            ),
            (
                "preserved_existing_data",
                "PreservedExistingData",
                TypeInfo(bool),
            ),
            (
                "volumei_scsi_attributes",
                "VolumeiSCSIAttributes",
                TypeInfo(VolumeiSCSIAttributes),
            ),
            (
                "created_date",
                "CreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "volume_used_in_bytes",
                "VolumeUsedInBytes",
                TypeInfo(int),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the storage volume.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier of the volume, e.g. vol-AE4B946D.
    volume_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the VolumeType enumeration values describing the type of the volume.
    volume_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the VolumeStatus values that indicates the state of the storage
    # volume.
    volume_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the volume in bytes.
    volume_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the percentage complete if the volume is restoring or
    # bootstrapping that represents the percent of data transferred. This field
    # does not appear in the response if the stored volume is not restoring or
    # bootstrapping.
    volume_progress: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the local disk that was specified in the CreateStorediSCSIVolume
    # operation.
    volume_disk_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the stored volume was created from a snapshot, this field contains the
    # snapshot ID used, e.g. snap-78e22663. Otherwise, this field is not
    # included.
    source_snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if when the stored volume was created, existing data on the
    # underlying local disk was preserved.

    # Valid Values: true, false
    preserved_existing_data: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An VolumeiSCSIAttributes object that represents a collection of iSCSI
    # attributes for one stored volume.
    volumei_scsi_attributes: "VolumeiSCSIAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date the volume was created. Volumes created prior to March 28, 2017
    # don’t have this time stamp.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the data stored on the volume in bytes.

    # This value is not available for volumes created prior to May 13, 2015,
    # until you store data on the volume.
    volume_used_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
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

    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tape(ShapeBase):
    """
    Describes a virtual tape object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
            (
                "tape_barcode",
                "TapeBarcode",
                TypeInfo(str),
            ),
            (
                "tape_created_date",
                "TapeCreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "tape_size_in_bytes",
                "TapeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "tape_status",
                "TapeStatus",
                TypeInfo(str),
            ),
            (
                "vtl_device",
                "VTLDevice",
                TypeInfo(str),
            ),
            (
                "progress",
                "Progress",
                TypeInfo(float),
            ),
            (
                "tape_used_in_bytes",
                "TapeUsedInBytes",
                TypeInfo(int),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the virtual tape.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The barcode that identifies a specific virtual tape.
    tape_barcode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the virtual tape was created.
    tape_created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size, in bytes, of the virtual tape capacity.
    tape_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the virtual tape.
    tape_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The virtual tape library (VTL) device that the virtual tape is associated
    # with.
    vtl_device: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For archiving virtual tapes, indicates how much data remains to be uploaded
    # before archiving is complete.

    # Range: 0 (not started) to 100 (complete).
    progress: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of data stored on the virtual tape.

    # This value is not available for tapes created prior to May 13, 2015.
    tape_used_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TapeArchive(ShapeBase):
    """
    Represents a virtual tape that is archived in the virtual tape shelf (VTS).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
            (
                "tape_barcode",
                "TapeBarcode",
                TypeInfo(str),
            ),
            (
                "tape_created_date",
                "TapeCreatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "tape_size_in_bytes",
                "TapeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "completion_time",
                "CompletionTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "retrieved_to",
                "RetrievedTo",
                TypeInfo(str),
            ),
            (
                "tape_status",
                "TapeStatus",
                TypeInfo(str),
            ),
            (
                "tape_used_in_bytes",
                "TapeUsedInBytes",
                TypeInfo(int),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of an archived virtual tape.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The barcode that identifies the archived virtual tape.
    tape_barcode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the virtual tape was created.
    tape_created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size, in bytes, of the archived virtual tape.
    tape_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the archiving of the virtual tape was completed.

    # The default time stamp format is in the ISO8601 extended YYYY-MM-
    # DD'T'HH:MM:SS'Z' format.
    completion_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is
    # being retrieved to.

    # The virtual tape is retrieved from the virtual tape shelf (VTS).
    retrieved_to: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the archived virtual tape.
    tape_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of data stored on the virtual tape.

    # This value is not available for tapes created prior to May 13, 2015.
    tape_used_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TapeInfo(ShapeBase):
    """
    Describes a virtual tape.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
            (
                "tape_barcode",
                "TapeBarcode",
                TypeInfo(str),
            ),
            (
                "tape_size_in_bytes",
                "TapeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "tape_status",
                "TapeStatus",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of a virtual tape.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The barcode that identifies a specific virtual tape.
    tape_barcode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of a virtual tape.
    tape_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the tape.
    tape_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TapeRecoveryPointInfo(ShapeBase):
    """
    Describes a recovery point.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tape_arn",
                "TapeARN",
                TypeInfo(str),
            ),
            (
                "tape_recovery_point_time",
                "TapeRecoveryPointTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "tape_size_in_bytes",
                "TapeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "tape_status",
                "TapeStatus",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the virtual tape.
    tape_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time when the point-in-time view of the virtual tape was replicated for
    # later recovery.

    # The default time stamp format of the tape recovery point time is in the
    # ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.
    tape_recovery_point_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size, in bytes, of the virtual tapes to recover.
    tape_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    tape_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBandwidthRateLimitInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * UpdateBandwidthRateLimitInput$AverageDownloadRateLimitInBitsPerSec

      * UpdateBandwidthRateLimitInput$AverageUploadRateLimitInBitsPerSec
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "average_upload_rate_limit_in_bits_per_sec",
                "AverageUploadRateLimitInBitsPerSec",
                TypeInfo(int),
            ),
            (
                "average_download_rate_limit_in_bits_per_sec",
                "AverageDownloadRateLimitInBitsPerSec",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The average upload bandwidth rate limit in bits per second.
    average_upload_rate_limit_in_bits_per_sec: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The average download bandwidth rate limit in bits per second.
    average_download_rate_limit_in_bits_per_sec: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateBandwidthRateLimitOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway whose throttle information was
    updated.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChapCredentialsInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * UpdateChapCredentialsInput$InitiatorName

      * UpdateChapCredentialsInput$SecretToAuthenticateInitiator

      * UpdateChapCredentialsInput$SecretToAuthenticateTarget

      * UpdateChapCredentialsInput$TargetARN
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "secret_to_authenticate_initiator",
                "SecretToAuthenticateInitiator",
                TypeInfo(str),
            ),
            (
                "initiator_name",
                "InitiatorName",
                TypeInfo(str),
            ),
            (
                "secret_to_authenticate_target",
                "SecretToAuthenticateTarget",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
    # DescribeStorediSCSIVolumes operation to return the TargetARN for specified
    # VolumeARN.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The secret key that the initiator (for example, the Windows client) must
    # provide to participate in mutual CHAP with the target.

    # The secret key must be between 12 and 16 bytes when encoded in UTF-8.
    secret_to_authenticate_initiator: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The iSCSI initiator that connects to the target.
    initiator_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The secret key that the target must provide to participate in mutual CHAP
    # with the initiator (e.g. Windows client).

    # Byte constraints: Minimum bytes of 12. Maximum bytes of 16.

    # The secret key must be between 12 and 16 bytes when encoded in UTF-8.
    secret_to_authenticate_target: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateChapCredentialsOutput(OutputShapeBase):
    """
    A JSON object containing the following fields:
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
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "initiator_name",
                "InitiatorName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the target. This is the same target
    # specified in the request.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The iSCSI initiator that connects to the target. This is the same initiator
    # name specified in the request.
    initiator_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGatewayInformationInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "gateway_name",
                "GatewayName",
                TypeInfo(str),
            ),
            (
                "gateway_timezone",
                "GatewayTimezone",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name you configured for your gateway.
    gateway_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    gateway_timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGatewayInformationOutput(OutputShapeBase):
    """
    A JSON object containing the ARN of the gateway that was updated.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "gateway_name",
                "GatewayName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    gateway_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGatewaySoftwareNowInput(ShapeBase):
    """
    A JSON object containing the of the gateway to update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGatewaySoftwareNowOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway that was updated.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceStartTimeInput(ShapeBase):
    """
    A JSON object containing the following fields:

      * UpdateMaintenanceStartTimeInput$DayOfWeek

      * UpdateMaintenanceStartTimeInput$HourOfDay

      * UpdateMaintenanceStartTimeInput$MinuteOfHour
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "hour_of_day",
                "HourOfDay",
                TypeInfo(int),
            ),
            (
                "minute_of_hour",
                "MinuteOfHour",
                TypeInfo(int),
            ),
            (
                "day_of_week",
                "DayOfWeek",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hour component of the maintenance start time represented as _hh_ ,
    # where _hh_ is the hour (00 to 23). The hour of the day is in the time zone
    # of the gateway.
    hour_of_day: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minute component of the maintenance start time represented as _mm_ ,
    # where _mm_ is the minute (00 to 59). The minute of the hour is in the time
    # zone of the gateway.
    minute_of_hour: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maintenance start time day of the week represented as an ordinal number
    # from 0 to 6, where 0 represents Sunday and 6 Saturday.
    day_of_week: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateMaintenanceStartTimeOutput(OutputShapeBase):
    """
    A JSON object containing the of the gateway whose maintenance start time is
    updated.
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
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNFSFileShareInput(ShapeBase):
    """
    UpdateNFSFileShareInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
            (
                "nfs_file_share_defaults",
                "NFSFileShareDefaults",
                TypeInfo(NFSFileShareDefaults),
            ),
            (
                "default_storage_class",
                "DefaultStorageClass",
                TypeInfo(str),
            ),
            (
                "object_acl",
                "ObjectACL",
                TypeInfo(typing.Union[str, ObjectACL]),
            ),
            (
                "client_list",
                "ClientList",
                TypeInfo(typing.List[str]),
            ),
            (
                "squash",
                "Squash",
                TypeInfo(str),
            ),
            (
                "read_only",
                "ReadOnly",
                TypeInfo(bool),
            ),
            (
                "guess_mime_type_enabled",
                "GuessMIMETypeEnabled",
                TypeInfo(bool),
            ),
            (
                "requester_pays",
                "RequesterPays",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the file share to be updated.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default values for the file share. Optional.
    nfs_file_share_defaults: "NFSFileShareDefaults" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default storage class for objects put into an Amazon S3 bucket by the
    # file gateway. Possible values are `S3_STANDARD`, `S3_STANDARD_IA`, or
    # `S3_ONEZONE_IA`. If this field is not populated, the default value
    # `S3_STANDARD` is used. Optional.
    default_storage_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the access control list permission for objects in the S3
    # bucket that a file gateway puts objects into. The default value is
    # "private".
    object_acl: typing.Union[str, "ObjectACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of clients that are allowed to access the file gateway. The list
    # must contain either valid IP addresses or valid CIDR blocks.
    client_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user mapped to anonymous user. Valid options are the following:

    #   * `RootSquash` \- Only root is mapped to anonymous user.

    #   * `NoSquash` \- No one is mapped to anonymous user

    #   * `AllSquash` \- Everyone is mapped to anonymous user.
    squash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the write status of a file share. This value is true if
    # the write status is read-only, and otherwise false.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that enables guessing of the MIME type for uploaded objects based
    # on file extensions. Set this value to true to enable MIME type guessing,
    # and otherwise to false. The default value is true.
    guess_mime_type_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the access control list permission for objects in the
    # Amazon S3 bucket that a file gateway puts objects into. The default value
    # is `private`.
    requester_pays: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNFSFileShareOutput(OutputShapeBase):
    """
    UpdateNFSFileShareOutput
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
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the updated file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSMBFileShareInput(ShapeBase):
    """
    UpdateSMBFileShareInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
            (
                "kms_encrypted",
                "KMSEncrypted",
                TypeInfo(bool),
            ),
            (
                "kms_key",
                "KMSKey",
                TypeInfo(str),
            ),
            (
                "default_storage_class",
                "DefaultStorageClass",
                TypeInfo(str),
            ),
            (
                "object_acl",
                "ObjectACL",
                TypeInfo(typing.Union[str, ObjectACL]),
            ),
            (
                "read_only",
                "ReadOnly",
                TypeInfo(bool),
            ),
            (
                "guess_mime_type_enabled",
                "GuessMIMETypeEnabled",
                TypeInfo(bool),
            ),
            (
                "requester_pays",
                "RequesterPays",
                TypeInfo(bool),
            ),
            (
                "valid_user_list",
                "ValidUserList",
                TypeInfo(typing.List[str]),
            ),
            (
                "invalid_user_list",
                "InvalidUserList",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the SMB file share that you want to
    # update.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True to use Amazon S3 server side encryption with your own AWS KMS key, or
    # false to use a key managed by Amazon S3. Optional.
    kms_encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server
    # side encryption. This value can only be set when KMSEncrypted is true.
    # Optional.
    kms_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default storage class for objects put into an Amazon S3 bucket by the
    # file gateway. Possible values are `S3_STANDARD`, `S3_STANDARD_IA`, or
    # `S3_ONEZONE_IA`. If this field is not populated, the default value
    # `S3_STANDARD` is used. Optional.
    default_storage_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that sets the access control list permission for objects in the S3
    # bucket that a file gateway puts objects into. The default value is
    # "private".
    object_acl: typing.Union[str, "ObjectACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the write status of a file share. This value is true if
    # the write status is read-only, and otherwise false.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that enables guessing of the MIME type for uploaded objects based
    # on file extensions. Set this value to true to enable MIME type guessing,
    # and otherwise to false. The default value is true.
    guess_mime_type_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that sets the access control list permission for objects in the
    # Amazon S3 bucket that a file gateway puts objects into. The default value
    # is `private`.
    requester_pays: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of users or groups in the Active Directory that are allowed to
    # access the file share. A group must be prefixed with the @ character. For
    # example `@group1`. Can only be set if Authentication is set to
    # `ActiveDirectory`.
    valid_user_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of users or groups in the Active Directory that are not allowed to
    # access the file share. A group must be prefixed with the @ character. For
    # example `@group1`. Can only be set if Authentication is set to
    # `ActiveDirectory`.
    invalid_user_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSMBFileShareOutput(OutputShapeBase):
    """
    UpdateSMBFileShareOutput
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
                "file_share_arn",
                "FileShareARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the updated SMB file share.
    file_share_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSnapshotScheduleInput(ShapeBase):
    """
    A JSON object containing one or more of the following fields:

      * UpdateSnapshotScheduleInput$Description

      * UpdateSnapshotScheduleInput$RecurrenceInHours

      * UpdateSnapshotScheduleInput$StartAt

      * UpdateSnapshotScheduleInput$VolumeARN
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "start_at",
                "StartAt",
                TypeInfo(int),
            ),
            (
                "recurrence_in_hours",
                "RecurrenceInHours",
                TypeInfo(int),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation
    # to return a list of gateway volumes.
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hour of the day at which the snapshot schedule begins represented as
    # _hh_ , where _hh_ is the hour (0 to 23). The hour of the day is in the time
    # zone of the gateway.
    start_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Frequency of snapshots. Specify the number of hours between snapshots.
    recurrence_in_hours: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional description of the snapshot that overwrites the existing
    # description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSnapshotScheduleOutput(OutputShapeBase):
    """
    A JSON object containing the of the updated storage volume.
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
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateVTLDeviceTypeInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vtl_device_arn",
                "VTLDeviceARN",
                TypeInfo(str),
            ),
            (
                "device_type",
                "DeviceType",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the medium changer you want to select.
    vtl_device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of medium changer you want to select.

    # Valid Values: "STK-L700", "AWS-Gateway-VTL"
    device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateVTLDeviceTypeOutput(OutputShapeBase):
    """
    UpdateVTLDeviceTypeOutput
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
                "vtl_device_arn",
                "VTLDeviceARN",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the medium changer you have selected.
    vtl_device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VTLDevice(ShapeBase):
    """
    Represents a device object associated with a tape gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vtl_device_arn",
                "VTLDeviceARN",
                TypeInfo(str),
            ),
            (
                "vtl_device_type",
                "VTLDeviceType",
                TypeInfo(str),
            ),
            (
                "vtl_device_vendor",
                "VTLDeviceVendor",
                TypeInfo(str),
            ),
            (
                "vtl_device_product_identifier",
                "VTLDeviceProductIdentifier",
                TypeInfo(str),
            ),
            (
                "devicei_scsi_attributes",
                "DeviceiSCSIAttributes",
                TypeInfo(DeviceiSCSIAttributes),
            ),
        ]

    # Specifies the unique Amazon Resource Name (ARN) of the device (tape drive
    # or media changer).
    vtl_device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    vtl_device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    vtl_device_vendor: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    vtl_device_product_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of iSCSI information about a VTL device.
    devicei_scsi_attributes: "DeviceiSCSIAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VolumeInfo(ShapeBase):
    """
    Describes a storage volume object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "volume_id",
                "VolumeId",
                TypeInfo(str),
            ),
            (
                "gateway_arn",
                "GatewayARN",
                TypeInfo(str),
            ),
            (
                "gateway_id",
                "GatewayId",
                TypeInfo(str),
            ),
            (
                "volume_type",
                "VolumeType",
                TypeInfo(str),
            ),
            (
                "volume_size_in_bytes",
                "VolumeSizeInBytes",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) for the storage volume. For example, the
    # following is a valid ARN:

    # `arn:aws:storagegateway:us-
    # east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB`

    # Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and
    # hyphens (-).
    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier assigned to the volume. This ID becomes part of the
    # volume Amazon Resource Name (ARN), which you use as input for other
    # operations.

    # Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and
    # hyphens (-).
    volume_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the gateway. Use the ListGateways
    # operation to return a list of gateways for your account and region.
    gateway_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier assigned to your gateway during activation. This ID
    # becomes part of the gateway Amazon Resource Name (ARN), which you use as
    # input for other operations.

    # Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and
    # hyphens (-).
    gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the volume in bytes.

    # Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and
    # hyphens (-).
    volume_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VolumeRecoveryPointInfo(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "volume_arn",
                "VolumeARN",
                TypeInfo(str),
            ),
            (
                "volume_size_in_bytes",
                "VolumeSizeInBytes",
                TypeInfo(int),
            ),
            (
                "volume_usage_in_bytes",
                "VolumeUsageInBytes",
                TypeInfo(int),
            ),
            (
                "volume_recovery_point_time",
                "VolumeRecoveryPointTime",
                TypeInfo(str),
            ),
        ]

    volume_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_size_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_usage_in_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    volume_recovery_point_time: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VolumeiSCSIAttributes(ShapeBase):
    """
    Lists iSCSI information about a volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetARN",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
            (
                "network_interface_port",
                "NetworkInterfacePort",
                TypeInfo(int),
            ),
            (
                "lun_number",
                "LunNumber",
                TypeInfo(int),
            ),
            (
                "chap_enabled",
                "ChapEnabled",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the volume target.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network interface identifier.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port used to communicate with iSCSI targets.
    network_interface_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The logical disk number.
    lun_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether mutual CHAP is enabled for the iSCSI target.
    chap_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
