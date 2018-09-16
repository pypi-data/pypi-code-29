import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BadRequest(ShapeBase):
    """
    Returned if the request is malformed or contains an error such as an invalid
    parameter value or a missing required parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFileSystemRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_token",
                "CreationToken",
                TypeInfo(str),
            ),
            (
                "performance_mode",
                "PerformanceMode",
                TypeInfo(typing.Union[str, PerformanceMode]),
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
                "throughput_mode",
                "ThroughputMode",
                TypeInfo(typing.Union[str, ThroughputMode]),
            ),
            (
                "provisioned_throughput_in_mibps",
                "ProvisionedThroughputInMibps",
                TypeInfo(float),
            ),
        ]

    # String of up to 64 ASCII characters. Amazon EFS uses this to ensure
    # idempotent creation.
    creation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `PerformanceMode` of the file system. We recommend `generalPurpose`
    # performance mode for most file systems. File systems using the `maxIO`
    # performance mode can scale to higher levels of aggregate throughput and
    # operations per second with a tradeoff of slightly higher latencies for most
    # file operations. This can't be changed after the file system has been
    # created.
    performance_mode: typing.Union[str, "PerformanceMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value that, if true, creates an encrypted file system. When
    # creating an encrypted file system, you have the option of specifying a
    # CreateFileSystemRequest$KmsKeyId for an existing AWS Key Management Service
    # (AWS KMS) customer master key (CMK). If you don't specify a CMK, then the
    # default CMK for Amazon EFS, `/aws/elasticfilesystem`, is used to protect
    # the encrypted file system.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS KMS CMK to be used to protect the encrypted file system.
    # This parameter is only required if you want to use a non-default CMK. If
    # this parameter is not specified, the default CMK for Amazon EFS is used.
    # This ID can be in one of the following formats:

    #   * Key ID - A unique identifier of the key, for example, `1234abcd-12ab-34cd-56ef-1234567890ab`.

    #   * ARN - An Amazon Resource Name (ARN) for the key, for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

    #   * Key alias - A previously created display name for a key. For example, `alias/projectKey1`.

    #   * Key alias ARN - An ARN for a key alias, for example, `arn:aws:kms:us-west-2:444455556666:alias/projectKey1`.

    # If KmsKeyId is specified, the CreateFileSystemRequest$Encrypted parameter
    # must be set to true.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The throughput mode for the file system to be created. There are two
    # throughput modes to choose from for your file system: bursting and
    # provisioned. You can decrease your file system's throughput in Provisioned
    # Throughput mode or change between the throughput modes as long as it’s been
    # more than 24 hours since the last decrease or throughput mode change.
    throughput_mode: typing.Union[str, "ThroughputMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The throughput, measured in MiB/s, that you want to provision for a file
    # system that you're creating. The limit on throughput is 1024 MiB/s. You can
    # get these limits increased by contacting AWS Support. For more information,
    # see [Amazon EFS Limits That You Can
    # Increase](http://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits)
    # in the _Amazon EFS User Guide._
    provisioned_throughput_in_mibps: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMountTargetRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # ID of the file system for which to create the mount target.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the subnet to add the mount target in.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Valid IPv4 address within the address range of the specified subnet.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Up to five VPC security group IDs, of the form `sg-xxxxxxxx`. These must be
    # for the same VPC as subnet specified.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTagsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # ID of the file system whose tags you want to modify (String). This
    # operation modifies the tags only, not the file system.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Array of `Tag` objects to add. Each `Tag` object is a key-value pair.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFileSystemRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
        ]

    # ID of the file system you want to delete.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMountTargetRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mount_target_id",
                "MountTargetId",
                TypeInfo(str),
            ),
        ]

    # ID of the mount target to delete (String).
    mount_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # ID of the file system whose tags you want to delete (String).
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of tag keys to delete.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DependencyTimeout(ShapeBase):
    """
    The service timed out trying to fulfill the request, and the client should try
    the call again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFileSystemsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "creation_token",
                "CreationToken",
                TypeInfo(str),
            ),
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
        ]

    # (Optional) Specifies the maximum number of file systems to return in the
    # response (integer). This parameter value must be greater than 0. The number
    # of items that Amazon EFS returns is the minimum of the `MaxItems` parameter
    # specified in the request and the service's internal maximum number of items
    # per page.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Opaque pagination token returned from a previous
    # `DescribeFileSystems` operation (String). If present, specifies to continue
    # the list from where the returning call had left off.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Restricts the list to the file system with this creation token
    # (String). You specify a creation token when you create an Amazon EFS file
    # system.
    creation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) ID of the file system whose description you want to retrieve
    # (String).
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeFileSystemsResponse(OutputShapeBase):
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
                "file_systems",
                "FileSystems",
                TypeInfo(typing.List[FileSystemDescription]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Present if provided by caller in the request (String).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Array of file system descriptions.
    file_systems: typing.List["FileSystemDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Present if there are more file systems than returned in the response
    # (String). You can use the `NextMarker` in the subsequent request to fetch
    # the descriptions.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeFileSystemsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeMountTargetSecurityGroupsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mount_target_id",
                "MountTargetId",
                TypeInfo(str),
            ),
        ]

    # ID of the mount target whose security groups you want to retrieve.
    mount_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMountTargetSecurityGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Array of security groups.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeMountTargetsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "mount_target_id",
                "MountTargetId",
                TypeInfo(str),
            ),
        ]

    # (Optional) Maximum number of mount targets to return in the response. It
    # must be an integer with a value greater than zero.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Opaque pagination token returned from a previous
    # `DescribeMountTargets` operation (String). If present, it specifies to
    # continue the list from where the previous returning call left off.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) ID of the file system whose mount targets you want to list
    # (String). It must be included in your request if `MountTargetId` is not
    # included.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) ID of the mount target that you want to have described (String).
    # It must be included in your request if `FileSystemId` is not included.
    mount_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeMountTargetsResponse(OutputShapeBase):
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
                "mount_targets",
                "MountTargets",
                TypeInfo(typing.List[MountTargetDescription]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the request included the `Marker`, the response returns that value in
    # this field.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the file system's mount targets as an array of
    # `MountTargetDescription` objects.
    mount_targets: typing.List["MountTargetDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a value is present, there are more mount targets to return. In a
    # subsequent request, you can provide `Marker` in your request with this
    # value to retrieve the next set of mount targets.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeMountTargetsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeTagsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
        ]

    # ID of the file system whose tag set you want to retrieve.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Maximum number of file system tags to return in the response. It
    # must be an integer with a value greater than zero.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Opaque pagination token returned from a previous `DescribeTags`
    # operation (String). If present, it specifies to continue the list from
    # where the previous call left off.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTagsResponse(OutputShapeBase):
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
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns tags associated with the file system as an array of `Tag` objects.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the request included a `Marker`, the response returns that value in this
    # field.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a value is present, there are more tags to return. In a subsequent
    # request, you can provide the value of `NextMarker` as the value of the
    # `Marker` parameter in your next request to retrieve the next set of tags.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeTagsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class FileSystemAlreadyExists(ShapeBase):
    """
    Returned if the file system you are trying to create already exists, with the
    creation token you provided.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FileSystemDescription(OutputShapeBase):
    """
    Description of the file system.
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
                "owner_id",
                "OwnerId",
                TypeInfo(str),
            ),
            (
                "creation_token",
                "CreationToken",
                TypeInfo(str),
            ),
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "life_cycle_state",
                "LifeCycleState",
                TypeInfo(typing.Union[str, LifeCycleState]),
            ),
            (
                "number_of_mount_targets",
                "NumberOfMountTargets",
                TypeInfo(int),
            ),
            (
                "size_in_bytes",
                "SizeInBytes",
                TypeInfo(FileSystemSize),
            ),
            (
                "performance_mode",
                "PerformanceMode",
                TypeInfo(typing.Union[str, PerformanceMode]),
            ),
            (
                "name",
                "Name",
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
                "throughput_mode",
                "ThroughputMode",
                TypeInfo(typing.Union[str, ThroughputMode]),
            ),
            (
                "provisioned_throughput_in_mibps",
                "ProvisionedThroughputInMibps",
                TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS account that created the file system. If the file system was created by
    # an IAM user, the parent account to which the user belongs is the owner.
    owner_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Opaque string specified in the request.
    creation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the file system, assigned by Amazon EFS.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time that the file system was created, in seconds (since
    # 1970-01-01T00:00:00Z).
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lifecycle phase of the file system.
    life_cycle_state: typing.Union[str, "LifeCycleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current number of mount targets that the file system has. For more
    # information, see CreateMountTarget.
    number_of_mount_targets: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Latest known metered size (in bytes) of data stored in the file system, in
    # its `Value` field, and the time at which that size was determined in its
    # `Timestamp` field. The `Timestamp` value is the integer number of seconds
    # since 1970-01-01T00:00:00Z. The `SizeInBytes` value doesn't represent the
    # size of a consistent snapshot of the file system, but it is eventually
    # consistent when there are no writes to the file system. That is,
    # `SizeInBytes` represents actual size only if the file system is not
    # modified for a period longer than a couple of hours. Otherwise, the value
    # is not the exact size that the file system was at any point in time.
    size_in_bytes: "FileSystemSize" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `PerformanceMode` of the file system.
    performance_mode: typing.Union[str, "PerformanceMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can add tags to a file system, including a `Name` tag. For more
    # information, see CreateTags. If the file system has a `Name` tag, Amazon
    # EFS returns the value in this field.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value that, if true, indicates that the file system is encrypted.
    encrypted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK)
    # that was used to protect the encrypted file system.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The throughput mode for a file system. There are two throughput modes to
    # choose from for your file system: bursting and provisioned. You can
    # decrease your file system's throughput in Provisioned Throughput mode or
    # change between the throughput modes as long as it’s been more than 24 hours
    # since the last decrease or throughput mode change.
    throughput_mode: typing.Union[str, "ThroughputMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The throughput, measured in MiB/s, that you want to provision for a file
    # system. The limit on throughput is 1024 MiB/s. You can get these limits
    # increased by contacting AWS Support. For more information, see [Amazon EFS
    # Limits That You Can
    # Increase](http://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits)
    # in the _Amazon EFS User Guide._
    provisioned_throughput_in_mibps: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FileSystemInUse(ShapeBase):
    """
    Returned if a file system has mount targets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FileSystemLimitExceeded(ShapeBase):
    """
    Returned if the AWS account has already created the maximum number of file
    systems allowed per account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FileSystemNotFound(ShapeBase):
    """
    Returned if the specified `FileSystemId` value doesn't exist in the requester's
    AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FileSystemSize(ShapeBase):
    """
    Latest known metered size (in bytes) of data stored in the file system, in its
    `Value` field, and the time at which that size was determined in its `Timestamp`
    field. Note that the value does not represent the size of a consistent snapshot
    of the file system, but it is eventually consistent when there are no writes to
    the file system. That is, the value will represent the actual size only if the
    file system is not modified for a period longer than a couple of hours.
    Otherwise, the value is not necessarily the exact size the file system was at
    any instant in time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(int),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Latest known metered size (in bytes) of data stored in the file system.
    value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time at which the size of data, returned in the `Value` field, was
    # determined. The value is the integer number of seconds since
    # 1970-01-01T00:00:00Z.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IncorrectFileSystemLifeCycleState(ShapeBase):
    """
    Returned if the file system's lifecycle state is not "available".
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IncorrectMountTargetState(ShapeBase):
    """
    Returned if the mount target is not in the correct state for the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InsufficientThroughputCapacity(ShapeBase):
    """
    Returned if there's not enough capacity to provision additional throughput. This
    value might be returned when you try to create a file system in provisioned
    throughput mode, when you attempt to increase the provisioned throughput of an
    existing file system, or when you attempt to change an existing file system from
    bursting to provisioned throughput mode.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    Returned if an error occurred on the server side.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IpAddressInUse(ShapeBase):
    """
    Returned if the request specified an `IpAddress` that is already in use in the
    subnet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LifeCycleState(str):
    creating = "creating"
    available = "available"
    updating = "updating"
    deleting = "deleting"
    deleted = "deleted"


@dataclasses.dataclass
class ModifyMountTargetSecurityGroupsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mount_target_id",
                "MountTargetId",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
        ]

    # ID of the mount target whose security groups you want to modify.
    mount_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Array of up to five VPC security group IDs.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MountTargetConflict(ShapeBase):
    """
    Returned if the mount target would violate one of the specified restrictions
    based on the file system's existing mount targets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MountTargetDescription(OutputShapeBase):
    """
    Provides a description of a mount target.
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
                "mount_target_id",
                "MountTargetId",
                TypeInfo(str),
            ),
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "life_cycle_state",
                "LifeCycleState",
                TypeInfo(typing.Union[str, LifeCycleState]),
            ),
            (
                "owner_id",
                "OwnerId",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "IpAddress",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # System-assigned mount target ID.
    mount_target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the file system for which the mount target is intended.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the mount target's subnet.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lifecycle state of the mount target.
    life_cycle_state: typing.Union[str, "LifeCycleState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS account ID that owns the resource.
    owner_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Address at which the file system may be mounted via the mount target.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the network interface that Amazon EFS created when it created the
    # mount target.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MountTargetNotFound(ShapeBase):
    """
    Returned if there is no mount target with the specified ID found in the caller's
    account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkInterfaceLimitExceeded(ShapeBase):
    """
    The calling account has reached the limit for elastic network interfaces for the
    specific AWS Region. The client should try to delete some elastic network
    interfaces or get the account limit raised. For more information, see [Amazon
    VPC
    Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html)
    in the _Amazon VPC User Guide_ (see the Network interfaces per VPC entry in the
    table).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoFreeAddressesInSubnet(ShapeBase):
    """
    Returned if `IpAddress` was not specified in the request and there are no free
    IP addresses in the subnet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PerformanceMode(str):
    generalPurpose = "generalPurpose"
    maxIO = "maxIO"


@dataclasses.dataclass
class SecurityGroupLimitExceeded(ShapeBase):
    """
    Returned if the size of `SecurityGroups` specified in the request is greater
    than five.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SecurityGroupNotFound(ShapeBase):
    """
    Returned if one of the specified security groups doesn't exist in the subnet's
    VPC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetNotFound(ShapeBase):
    """
    Returned if there is no subnet with ID `SubnetId` provided in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers,
    representable in UTF-8, and the following characters:` + - = . _ : /`
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

    # Tag key (String). The key can't start with `aws:`.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value of the tag key.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ThroughputLimitExceeded(ShapeBase):
    """
    Returned if the throughput mode or amount of provisioned throughput can't be
    changed because the throughput limit of 1024 MiB/s has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ThroughputMode(str):
    bursting = "bursting"
    provisioned = "provisioned"


@dataclasses.dataclass
class TooManyRequests(ShapeBase):
    """
    Returned if you don’t wait at least 24 hours before changing the throughput
    mode, or decreasing the Provisioned Throughput value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnsupportedAvailabilityZone(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFileSystemRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_system_id",
                "FileSystemId",
                TypeInfo(str),
            ),
            (
                "throughput_mode",
                "ThroughputMode",
                TypeInfo(typing.Union[str, ThroughputMode]),
            ),
            (
                "provisioned_throughput_in_mibps",
                "ProvisionedThroughputInMibps",
                TypeInfo(float),
            ),
        ]

    # The ID of the file system that you want to update.
    file_system_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) The throughput mode that you want your file system to use. If
    # you're not updating your throughput mode, you don't need to provide this
    # value in your request.
    throughput_mode: typing.Union[str, "ThroughputMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Optional) The amount of throughput, in MiB/s, that you want to provision
    # for your file system. If you're not updating the amount of provisioned
    # throughput for your file system, you don't need to provide this value in
    # your request.
    provisioned_throughput_in_mibps: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
