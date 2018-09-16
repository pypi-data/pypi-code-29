import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Address(ShapeBase):
    """
    The address that you want the Snowball or Snowballs associated with a specific
    job to be shipped to. Addresses are validated at the time of creation. The
    address you provide must be located within the serviceable area of your region.
    Although no individual elements of the `Address` are required, if the address is
    invalid or unsupported, then an exception is thrown.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "company",
                "Company",
                TypeInfo(str),
            ),
            (
                "street1",
                "Street1",
                TypeInfo(str),
            ),
            (
                "street2",
                "Street2",
                TypeInfo(str),
            ),
            (
                "street3",
                "Street3",
                TypeInfo(str),
            ),
            (
                "city",
                "City",
                TypeInfo(str),
            ),
            (
                "state_or_province",
                "StateOrProvince",
                TypeInfo(str),
            ),
            (
                "prefecture_or_district",
                "PrefectureOrDistrict",
                TypeInfo(str),
            ),
            (
                "landmark",
                "Landmark",
                TypeInfo(str),
            ),
            (
                "country",
                "Country",
                TypeInfo(str),
            ),
            (
                "postal_code",
                "PostalCode",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
            (
                "is_restricted",
                "IsRestricted",
                TypeInfo(bool),
            ),
        ]

    # The unique ID for an address.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a person to receive a Snowball at an address.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the company to receive a Snowball at an address.
    company: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first line in a street address that a Snowball is to be delivered to.
    street1: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The second line in a street address that a Snowball is to be delivered to.
    street2: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The third line in a street address that a Snowball is to be delivered to.
    street3: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The city in an address that a Snowball is to be delivered to.
    city: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state or province in an address that a Snowball is to be delivered to.
    state_or_province: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is no longer used and the value is ignored.
    prefecture_or_district: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field is no longer used and the value is ignored.
    landmark: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The country in an address that a Snowball is to be delivered to.
    country: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The postal code in an address that a Snowball is to be delivered to.
    postal_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number associated with an address that a Snowball is to be
    # delivered to.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the address you are creating is a primary address, then set this option
    # to true. This field is not supported in most regions.
    is_restricted: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelClusterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
        ]

    # The 39-character ID for the cluster that you want to cancel, for example
    # `CID123e4567-e89b-12d3-a456-426655440000`.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelClusterResult(OutputShapeBase):
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
class CancelJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The 39-character job ID for the job that you want to cancel, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelJobResult(OutputShapeBase):
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
class ClusterLimitExceededException(ShapeBase):
    """
    Job creation failed. Currently, clusters support five nodes. If you have less
    than five nodes for your cluster and you have more nodes to create for this
    cluster, try again and create jobs until your cluster has exactly five notes.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterListEntry(ShapeBase):
    """
    Contains a cluster's state, a cluster's ID, and other important information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "cluster_state",
                "ClusterState",
                TypeInfo(typing.Union[str, ClusterState]),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The 39-character ID for the cluster that you want to list, for example
    # `CID123e4567-e89b-12d3-a456-426655440000`.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of this cluster. For information about the state of a
    # specific node, see JobListEntry$JobState.
    cluster_state: typing.Union[str, "ClusterState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date for this cluster.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines an optional description of the cluster, for example `Environmental
    # Data Cluster-01`.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ClusterMetadata(ShapeBase):
    """
    Contains metadata about a specific cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "kms_key_arn",
                "KmsKeyARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "cluster_state",
                "ClusterState",
                TypeInfo(typing.Union[str, ClusterState]),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "snowball_type",
                "SnowballType",
                TypeInfo(typing.Union[str, SnowballType]),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(JobResource),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "shipping_option",
                "ShippingOption",
                TypeInfo(typing.Union[str, ShippingOption]),
            ),
            (
                "notification",
                "Notification",
                TypeInfo(Notification),
            ),
            (
                "forwarding_address_id",
                "ForwardingAddressId",
                TypeInfo(str),
            ),
        ]

    # The automatically generated ID for a cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The optional description of the cluster.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `KmsKeyARN` Amazon Resource Name (ARN) associated with this cluster.
    # This ARN was created using the
    # [CreateKey](http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html)
    # API action in AWS Key Management Service (AWS KMS).
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role ARN associated with this cluster. This ARN was created using the
    # [CreateRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)
    # API action in AWS Identity and Access Management (IAM).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the cluster.
    cluster_state: typing.Union[str, "ClusterState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of job for this cluster. Currently, the only job type supported
    # for clusters is `LOCAL_USE`.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of AWS Snowball device to use for this cluster. Currently, the
    # only supported device type for cluster jobs is `EDGE`.
    snowball_type: typing.Union[str, "SnowballType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date for this cluster.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The arrays of JobResource objects that can include updated S3Resource
    # objects or LambdaResource objects.
    resources: "JobResource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The automatically generated ID for a specific address.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shipping speed for each node in this cluster. This speed doesn't
    # dictate how soon you'll get each Snowball Edge device, rather it represents
    # how quickly each device moves to its destination while in transit. Regional
    # shipping speeds are as follows:

    #   * In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.

    #   * In the European Union (EU), you have access to express shipping. Typically, Snowball Edges shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.

    #   * In India, Snowball Edges are delivered in one to seven days.

    #   * In the US, you have access to one-day shipping and two-day shipping.
    shipping_option: typing.Union[str, "ShippingOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Simple Notification Service (Amazon SNS) notification settings
    # for this cluster.
    notification: "Notification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the address that you want a cluster shipped to, after it will be
    # shipped to its primary address. This field is not supported in most
    # regions.
    forwarding_address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ClusterState(str):
    AwaitingQuorum = "AwaitingQuorum"
    Pending = "Pending"
    InUse = "InUse"
    Complete = "Complete"
    Cancelled = "Cancelled"


@dataclasses.dataclass
class CompatibleImage(ShapeBase):
    """
    A JSON-formatted object that describes a compatible Amazon Machine Image (AMI),
    including the ID and name for a Snowball Edge AMI. This AMI is compatible with
    the device's physical hardware requirements, and it should be able to be run in
    an SBE1 instance on the device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ami_id",
                "AmiId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for an individual Snowball Edge AMI.
    ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The optional name of a compatible image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAddressRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(Address),
            ),
        ]

    # The address that you want the Snowball shipped to.
    address: "Address" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAddressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The automatically generated ID for a specific address. You'll use this ID
    # when you create a job to specify which address you want the Snowball for
    # that job shipped to.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(JobResource),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "shipping_option",
                "ShippingOption",
                TypeInfo(typing.Union[str, ShippingOption]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "kms_key_arn",
                "KmsKeyARN",
                TypeInfo(str),
            ),
            (
                "snowball_type",
                "SnowballType",
                TypeInfo(typing.Union[str, SnowballType]),
            ),
            (
                "notification",
                "Notification",
                TypeInfo(Notification),
            ),
            (
                "forwarding_address_id",
                "ForwardingAddressId",
                TypeInfo(str),
            ),
        ]

    # The type of job for this cluster. Currently, the only job type supported
    # for clusters is `LOCAL_USE`.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resources associated with the cluster job. These resources include
    # Amazon S3 buckets and optional AWS Lambda functions written in the Python
    # language.
    resources: "JobResource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the address that you want the cluster shipped to.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `RoleARN` that you want to associate with this cluster. `RoleArn`
    # values are created by using the
    # [CreateRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)
    # API action in AWS Identity and Access Management (IAM).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shipping speed for each node in this cluster. This speed doesn't
    # dictate how soon you'll get each Snowball Edge device, rather it represents
    # how quickly each device moves to its destination while in transit. Regional
    # shipping speeds are as follows:

    #   * In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.

    #   * In the European Union (EU), you have access to express shipping. Typically, Snowball Edges shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.

    #   * In India, Snowball Edges are delivered in one to seven days.

    #   * In the US, you have access to one-day shipping and two-day shipping.
    shipping_option: typing.Union[str, "ShippingOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional description of this specific cluster, for example
    # `Environmental Data Cluster-01`.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `KmsKeyARN` value that you want to associate with this cluster.
    # `KmsKeyARN` values are created by using the
    # [CreateKey](http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html)
    # API action in AWS Key Management Service (AWS KMS).
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS Snowball device to use for this cluster. Currently, the
    # only supported device type for cluster jobs is `EDGE`.
    snowball_type: typing.Union[str, "SnowballType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Simple Notification Service (Amazon SNS) notification settings
    # for this cluster.
    notification: "Notification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The forwarding address ID for a cluster. This field is not supported in
    # most regions.
    forwarding_address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The automatically generated ID for a cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(JobResource),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "kms_key_arn",
                "KmsKeyARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "snowball_capacity_preference",
                "SnowballCapacityPreference",
                TypeInfo(typing.Union[str, SnowballCapacity]),
            ),
            (
                "shipping_option",
                "ShippingOption",
                TypeInfo(typing.Union[str, ShippingOption]),
            ),
            (
                "notification",
                "Notification",
                TypeInfo(Notification),
            ),
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "snowball_type",
                "SnowballType",
                TypeInfo(typing.Union[str, SnowballType]),
            ),
            (
                "forwarding_address_id",
                "ForwardingAddressId",
                TypeInfo(str),
            ),
        ]

    # Defines the type of job that you're creating.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines the Amazon S3 buckets associated with this job.

    # With `IMPORT` jobs, you specify the bucket or buckets that your transferred
    # data will be imported into.

    # With `EXPORT` jobs, you specify the bucket or buckets that your transferred
    # data will be exported from. Optionally, you can also specify a `KeyRange`
    # value. If you choose to export a range, you define the length of the range
    # by providing either an inclusive `BeginMarker` value, an inclusive
    # `EndMarker` value, or both. Ranges are UTF-8 binary sorted.
    resources: "JobResource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines an optional description of this specific job, for example
    # `Important Photos 2016-08-11`.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the address that you want the Snowball shipped to.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `KmsKeyARN` that you want to associate with this job. `KmsKeyARN`s are
    # created using the
    # [CreateKey](http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html)
    # AWS Key Management Service (KMS) API action.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `RoleARN` that you want to associate with this job. `RoleArn`s are
    # created using the
    # [CreateRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)
    # AWS Identity and Access Management (IAM) API action.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If your job is being created in one of the US regions, you have the option
    # of specifying what size Snowball you'd like for this job. In all other
    # regions, Snowballs come with 80 TB in storage capacity.
    snowball_capacity_preference: typing.Union[str, "SnowballCapacity"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The shipping speed for this job. This speed doesn't dictate how soon you'll
    # get the Snowball, rather it represents how quickly the Snowball moves to
    # its destination while in transit. Regional shipping speeds are as follows:

    #   * In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.

    #   * In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.

    #   * In India, Snowballs are delivered in one to seven days.

    #   * In the US, you have access to one-day shipping and two-day shipping.
    shipping_option: typing.Union[str, "ShippingOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Defines the Amazon Simple Notification Service (Amazon SNS) notification
    # settings for this job.
    notification: "Notification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of a cluster. If you're creating a job for a node in a cluster, you
    # need to provide only this `clusterId` value. The other job attributes are
    # inherited from the cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of AWS Snowball device to use for this job. Currently, the only
    # supported device type for cluster jobs is `EDGE`.
    snowball_type: typing.Union[str, "SnowballType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The forwarding address ID for a job. This field is not supported in most
    # regions.
    forwarding_address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The automatically generated ID for a job, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataTransfer(ShapeBase):
    """
    Defines the real-time status of a Snowball's data transfer while the device is
    at AWS. This data is only available while a job has a `JobState` value of
    `InProgress`, for both import and export jobs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bytes_transferred",
                "BytesTransferred",
                TypeInfo(int),
            ),
            (
                "objects_transferred",
                "ObjectsTransferred",
                TypeInfo(int),
            ),
            (
                "total_bytes",
                "TotalBytes",
                TypeInfo(int),
            ),
            (
                "total_objects",
                "TotalObjects",
                TypeInfo(int),
            ),
        ]

    # The number of bytes transferred between a Snowball and Amazon S3.
    bytes_transferred: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of objects transferred between a Snowball and Amazon S3.
    objects_transferred: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total bytes of data for a transfer between a Snowball and Amazon S3.
    # This value is set to 0 (zero) until all the keys that will be transferred
    # have been listed.
    total_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of objects for a transfer between a Snowball and Amazon
    # S3. This value is set to 0 (zero) until all the keys that will be
    # transferred have been listed.
    total_objects: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAddressRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
        ]

    # The automatically generated ID for a specific address.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAddressResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "address",
                "Address",
                TypeInfo(Address),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The address that you want the Snowball or Snowballs associated with a
    # specific job to be shipped to.
    address: "Address" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAddressesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The number of `ADDRESS` objects to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HTTP requests are stateless. To identify what object comes "next" in the
    # list of `ADDRESS` objects, you have the option of specifying a value for
    # `NextToken` as the starting point for your list of returned addresses.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAddressesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "addresses",
                "Addresses",
                TypeInfo(typing.List[Address]),
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

    # The Snowball shipping addresses that were created for this account.
    addresses: typing.List["Address"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # HTTP requests are stateless. If you use the automatically generated
    # `NextToken` value in your next `DescribeAddresses` call, your list of
    # returned addresses will start from this point in the array.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeAddressesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeClusterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
        ]

    # The automatically generated ID for a cluster.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeClusterResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_metadata",
                "ClusterMetadata",
                TypeInfo(ClusterMetadata),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a specific cluster, including shipping information,
    # cluster status, and other important metadata.
    cluster_metadata: "ClusterMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The automatically generated ID for a job, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_metadata",
                "JobMetadata",
                TypeInfo(JobMetadata),
            ),
            (
                "sub_job_metadata",
                "SubJobMetadata",
                TypeInfo(typing.List[JobMetadata]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about a specific job, including shipping information, job
    # status, and other important metadata.
    job_metadata: "JobMetadata" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a specific job part (in the case of an export job),
    # including shipping information, job status, and other important metadata.
    sub_job_metadata: typing.List["JobMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Ec2AmiResource(ShapeBase):
    """
    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI),
    including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these
    two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ami_id",
                "AmiId",
                TypeInfo(str),
            ),
            (
                "snowball_ami_id",
                "SnowballAmiId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AMI in Amazon EC2.
    ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AMI on the Snowball Edge device.
    snowball_ami_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Ec2RequestFailedException(ShapeBase):
    """
    Your IAM user lacks the necessary Amazon EC2 permissions to perform the
    attempted action.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventTriggerDefinition(ShapeBase):
    """
    The container for the EventTriggerDefinition$EventResourceARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_resource_arn",
                "EventResourceARN",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an
    # AWS Lambda function's event trigger associated with this job.
    event_resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobManifestRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The ID for a job that you want to get the manifest file for, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobManifestResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "manifest_uri",
                "ManifestURI",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon S3 presigned URL for the manifest file associated with the
    # specified `JobId` value.
    manifest_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobUnlockCodeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The ID for the job that you want to get the `UnlockCode` value for, for
    # example `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobUnlockCodeResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unlock_code",
                "UnlockCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `UnlockCode` value for the specified job. The `UnlockCode` value can be
    # accessed for up to 90 days after the job has been created.
    unlock_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSnowballUsageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetSnowballUsageResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "snowball_limit",
                "SnowballLimit",
                TypeInfo(int),
            ),
            (
                "snowballs_in_use",
                "SnowballsInUse",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service limit for number of Snowballs this account can have at once.
    # The default service limit is 1 (one).
    snowball_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of Snowballs that this account is currently using.
    snowballs_in_use: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAddressException(ShapeBase):
    """
    The address provided was invalid. Check the address with your region's carrier,
    and try again.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInputCombinationException(ShapeBase):
    """
    Job or cluster creation failed. One ore more inputs were invalid. Confirm that
    the CreateClusterRequest$SnowballType value supports your
    CreateJobRequest$JobType, and try again.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidJobStateException(ShapeBase):
    """
    The action can't be performed because the job's current state doesn't allow that
    action to be performed.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    The `NextToken` string was altered unexpectedly, and the operation has stopped.
    Run the operation without changing the `NextToken` string, and try again.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidResourceException(ShapeBase):
    """
    The specified resource can't be found. Check the information you provided in
    your last request, and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The provided resource value is invalid.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobListEntry(ShapeBase):
    """
    Each `JobListEntry` object contains a job's state, a job's ID, and a value that
    indicates whether the job is a job part, in the case of an export job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_state",
                "JobState",
                TypeInfo(typing.Union[str, JobState]),
            ),
            (
                "is_master",
                "IsMaster",
                TypeInfo(bool),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "snowball_type",
                "SnowballType",
                TypeInfo(typing.Union[str, SnowballType]),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The automatically generated ID for a job, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of this job.
    job_state: typing.Union[str, "JobState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that indicates that this job is a master job. A master job
    # represents a successful request to create an export job. Master jobs aren't
    # associated with any Snowballs. Instead, each master job will have at least
    # one job part, and each job part is associated with a Snowball. It might
    # take some time before the job parts associated with a particular master job
    # are listed, because they are created after the master job is created.
    is_master: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of device used with this job.
    snowball_type: typing.Union[str, "SnowballType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date for this job.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The optional description of this specific job, for example `Important
    # Photos 2016-08-11`.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobLogs(ShapeBase):
    """
    Contains job logs. Whenever Snowball is used to import data into or export data
    out of Amazon S3, you'll have the option of downloading a PDF job report. Job
    logs are returned as a part of the response syntax of the `DescribeJob` action
    in the `JobMetadata` data type. The job logs can be accessed for up to 60
    minutes after this request has been made. To access any of the job logs after 60
    minutes have passed, you'll have to make another call to the `DescribeJob`
    action.

    For import jobs, the PDF job report becomes available at the end of the import
    process. For export jobs, your job report typically becomes available while the
    Snowball for your job part is being delivered to you.

    The job report provides you insight into the state of your Amazon S3 data
    transfer. The report includes details about your job or job part for your
    records.

    For deeper visibility into the status of your transferred objects, you can look
    at the two associated logs: a success log and a failure log. The logs are saved
    in comma-separated value (CSV) format, and the name of each log includes the ID
    of the job or job part that the log describes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_completion_report_uri",
                "JobCompletionReportURI",
                TypeInfo(str),
            ),
            (
                "job_success_log_uri",
                "JobSuccessLogURI",
                TypeInfo(str),
            ),
            (
                "job_failure_log_uri",
                "JobFailureLogURI",
                TypeInfo(str),
            ),
        ]

    # A link to an Amazon S3 presigned URL where the job completion report is
    # located.
    job_completion_report_uri: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A link to an Amazon S3 presigned URL where the job success log is located.
    job_success_log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to an Amazon S3 presigned URL where the job failure log is located.
    job_failure_log_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobMetadata(ShapeBase):
    """
    Contains information about a specific job including shipping information, job
    status, and other important metadata. This information is returned as a part of
    the response syntax of the `DescribeJob` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_state",
                "JobState",
                TypeInfo(typing.Union[str, JobState]),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "snowball_type",
                "SnowballType",
                TypeInfo(typing.Union[str, SnowballType]),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(JobResource),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "kms_key_arn",
                "KmsKeyARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "shipping_details",
                "ShippingDetails",
                TypeInfo(ShippingDetails),
            ),
            (
                "snowball_capacity_preference",
                "SnowballCapacityPreference",
                TypeInfo(typing.Union[str, SnowballCapacity]),
            ),
            (
                "notification",
                "Notification",
                TypeInfo(Notification),
            ),
            (
                "data_transfer_progress",
                "DataTransferProgress",
                TypeInfo(DataTransfer),
            ),
            (
                "job_log_info",
                "JobLogInfo",
                TypeInfo(JobLogs),
            ),
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "forwarding_address_id",
                "ForwardingAddressId",
                TypeInfo(str),
            ),
        ]

    # The automatically generated ID for a job, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the jobs.
    job_state: typing.Union[str, "JobState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of device used with this job.
    snowball_type: typing.Union[str, "SnowballType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The creation date for this job.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `S3Resource` objects. Each `S3Resource` object represents an
    # Amazon S3 bucket that your transferred data will be exported from or
    # imported into.
    resources: "JobResource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the job, provided at job creation.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS)
    # key associated with this job. This ARN was created using the
    # [CreateKey](http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html)
    # API action in AWS KMS.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role ARN associated with this job. This ARN was created using the
    # [CreateRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)
    # API action in AWS Identity and Access Management (IAM).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the address that you want the Snowball shipped to.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A job's shipping information, including inbound and outbound tracking
    # numbers and shipping speed options.
    shipping_details: "ShippingDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Snowball capacity preference for this job, specified at job creation.
    # In US regions, you can choose between 50 TB and 80 TB Snowballs. All other
    # regions use 80 TB capacity Snowballs.
    snowball_capacity_preference: typing.Union[str, "SnowballCapacity"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The Amazon Simple Notification Service (Amazon SNS) notification settings
    # associated with a specific job. The `Notification` object is returned as a
    # part of the response syntax of the `DescribeJob` action in the
    # `JobMetadata` data type.
    notification: "Notification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value that defines the real-time status of a Snowball's data transfer
    # while the device is at AWS. This data is only available while a job has a
    # `JobState` value of `InProgress`, for both import and export jobs.
    data_transfer_progress: "DataTransfer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Links to Amazon S3 presigned URLs for the job report and logs. For import
    # jobs, the PDF job report becomes available at the end of the import
    # process. For export jobs, your job report typically becomes available while
    # the Snowball for your job part is being delivered to you.
    job_log_info: "JobLogs" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 39-character ID for the cluster, for example
    # `CID123e4567-e89b-12d3-a456-426655440000`.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the address that you want a job shipped to, after it will be
    # shipped to its primary address. This field is not supported in most
    # regions.
    forwarding_address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobResource(ShapeBase):
    """
    Contains an array of AWS resource objects. Each object represents an Amazon S3
    bucket, an AWS Lambda function, or an Amazon Machine Image (AMI) based on Amazon
    EC2 that is associated with a particular job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_resources",
                "S3Resources",
                TypeInfo(typing.List[S3Resource]),
            ),
            (
                "lambda_resources",
                "LambdaResources",
                TypeInfo(typing.List[LambdaResource]),
            ),
            (
                "ec2_ami_resources",
                "Ec2AmiResources",
                TypeInfo(typing.List[Ec2AmiResource]),
            ),
        ]

    # An array of `S3Resource` objects.
    s3_resources: typing.List["S3Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Python-language Lambda functions for this job.
    lambda_resources: typing.List["LambdaResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Machine Images (AMIs) associated with this job.
    ec2_ami_resources: typing.List["Ec2AmiResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class JobState(str):
    New = "New"
    PreparingAppliance = "PreparingAppliance"
    PreparingShipment = "PreparingShipment"
    InTransitToCustomer = "InTransitToCustomer"
    WithCustomer = "WithCustomer"
    InTransitToAWS = "InTransitToAWS"
    WithAWSSortingFacility = "WithAWSSortingFacility"
    WithAWS = "WithAWS"
    InProgress = "InProgress"
    Complete = "Complete"
    Cancelled = "Cancelled"
    Listing = "Listing"
    Pending = "Pending"


class JobType(str):
    IMPORT = "IMPORT"
    EXPORT = "EXPORT"
    LOCAL_USE = "LOCAL_USE"


@dataclasses.dataclass
class KMSRequestFailedException(ShapeBase):
    """
    The provided AWS Key Management Service key lacks the permissions to perform the
    specified CreateJob or UpdateJob action.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyRange(ShapeBase):
    """
    Contains a key range. For export jobs, a `S3Resource` object can have an
    optional `KeyRange` value. The length of the range is defined at job creation,
    and has either an inclusive `BeginMarker`, an inclusive `EndMarker`, or both.
    Ranges are UTF-8 binary sorted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "begin_marker",
                "BeginMarker",
                TypeInfo(str),
            ),
            (
                "end_marker",
                "EndMarker",
                TypeInfo(str),
            ),
        ]

    # The key that starts an optional key range for an export job. Ranges are
    # inclusive and UTF-8 binary sorted.
    begin_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key that ends an optional key range for an export job. Ranges are
    # inclusive and UTF-8 binary sorted.
    end_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaResource(ShapeBase):
    """
    Identifies
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_arn",
                "LambdaArn",
                TypeInfo(str),
            ),
            (
                "event_triggers",
                "EventTriggers",
                TypeInfo(typing.List[EventTriggerDefinition]),
            ),
        ]

    # An Amazon Resource Name (ARN) that represents an AWS Lambda function to be
    # triggered by PUT object actions on the associated local Amazon S3 resource.
    lambda_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The array of ARNs for S3Resource objects to trigger the LambdaResource
    # objects associated with this job.
    event_triggers: typing.List["EventTriggerDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListClusterJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The 39-character ID for the cluster that you want to list, for example
    # `CID123e4567-e89b-12d3-a456-426655440000`.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of `JobListEntry` objects to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HTTP requests are stateless. To identify what object comes "next" in the
    # list of `JobListEntry` objects, you have the option of specifying
    # `NextToken` as the starting point for your returned list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClusterJobsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_list_entries",
                "JobListEntries",
                TypeInfo(typing.List[JobListEntry]),
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

    # Each `JobListEntry` object contains a job's state, a job's ID, and a value
    # that indicates whether the job is a job part, in the case of export jobs.
    job_list_entries: typing.List["JobListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # HTTP requests are stateless. If you use the automatically generated
    # `NextToken` value in your next `ListClusterJobsResult` call, your list of
    # returned jobs will start from this point in the array.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The number of `ClusterListEntry` objects to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HTTP requests are stateless. To identify what object comes "next" in the
    # list of `ClusterListEntry` objects, you have the option of specifying
    # `NextToken` as the starting point for your returned list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_list_entries",
                "ClusterListEntries",
                TypeInfo(typing.List[ClusterListEntry]),
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

    # Each `ClusterListEntry` object contains a cluster's state, a cluster's ID,
    # and other important status information.
    cluster_list_entries: typing.List["ClusterListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # HTTP requests are stateless. If you use the automatically generated
    # `NextToken` value in your next `ClusterListEntry` call, your list of
    # returned clusters will start from this point in the array.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCompatibleImagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results for the list of compatible images. Currently,
    # a Snowball Edge device can store 10 AMIs.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HTTP requests are stateless. To identify what object comes "next" in the
    # list of compatible images, you can specify a value for `NextToken` as the
    # starting point for your list of returned images.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCompatibleImagesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compatible_images",
                "CompatibleImages",
                TypeInfo(typing.List[CompatibleImage]),
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

    # A JSON-formatted object that describes a compatible AMI, including the ID
    # and name for a Snowball Edge AMI.
    compatible_images: typing.List["CompatibleImage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Because HTTP requests are stateless, this is the starting point for your
    # next list of returned images.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The number of `JobListEntry` objects to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HTTP requests are stateless. To identify what object comes "next" in the
    # list of `JobListEntry` objects, you have the option of specifying
    # `NextToken` as the starting point for your returned list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_list_entries",
                "JobListEntries",
                TypeInfo(typing.List[JobListEntry]),
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

    # Each `JobListEntry` object contains a job's state, a job's ID, and a value
    # that indicates whether the job is a job part, in the case of export jobs.
    job_list_entries: typing.List["JobListEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # HTTP requests are stateless. If you use this automatically generated
    # `NextToken` value in your next `ListJobs` call, your returned
    # `JobListEntry` objects will start from this point in the array.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListJobsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Notification(ShapeBase):
    """
    The Amazon Simple Notification Service (Amazon SNS) notification settings
    associated with a specific job. The `Notification` object is returned as a part
    of the response syntax of the `DescribeJob` action in the `JobMetadata` data
    type.

    When the notification settings are defined during job creation, you can choose
    to notify based on a specific set of job states using the `JobStatesToNotify`
    array of strings, or you can specify that you want to have Amazon SNS
    notifications sent out for all job states with `NotifyAll` set to true.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sns_topic_arn",
                "SnsTopicARN",
                TypeInfo(str),
            ),
            (
                "job_states_to_notify",
                "JobStatesToNotify",
                TypeInfo(typing.List[typing.Union[str, JobState]]),
            ),
            (
                "notify_all",
                "NotifyAll",
                TypeInfo(bool),
            ),
        ]

    # The new SNS `TopicArn` that you want to associate with this job. You can
    # create Amazon Resource Names (ARNs) for topics by using the
    # [CreateTopic](http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html)
    # Amazon SNS API action.

    # You can subscribe email addresses to an Amazon SNS topic through the AWS
    # Management Console, or by using the
    # [Subscribe](http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)
    # AWS Simple Notification Service (SNS) API action.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of job states that will trigger a notification for this job.
    job_states_to_notify: typing.List[typing.Union[str, "JobState"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Any change in job state will trigger a notification for this job.
    notify_all: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3Resource(ShapeBase):
    """
    Each `S3Resource` object represents an Amazon S3 bucket that your transferred
    data will be exported from or imported into. For export jobs, this object can
    have an optional `KeyRange` value. The length of the range is defined at job
    creation, and has either an inclusive `BeginMarker`, an inclusive `EndMarker`,
    or both. Ranges are UTF-8 binary sorted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_arn",
                "BucketArn",
                TypeInfo(str),
            ),
            (
                "key_range",
                "KeyRange",
                TypeInfo(KeyRange),
            ),
        ]

    # The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For export jobs, you can provide an optional `KeyRange` within a specific
    # Amazon S3 bucket. The length of the range is defined at job creation, and
    # has either an inclusive `BeginMarker`, an inclusive `EndMarker`, or both.
    # Ranges are UTF-8 binary sorted.
    key_range: "KeyRange" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Shipment(ShapeBase):
    """
    The `Status` and `TrackingNumber` information for an inbound or outbound
    shipment.
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
                "tracking_number",
                "TrackingNumber",
                TypeInfo(str),
            ),
        ]

    # Status information for a shipment.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tracking number for this job. Using this tracking number with your
    # region's carrier's website, you can track a Snowball as the carrier
    # transports it.

    # For India, the carrier is Amazon Logistics. For all other regions, UPS is
    # the carrier.
    tracking_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ShippingDetails(ShapeBase):
    """
    A job's shipping information, including inbound and outbound tracking numbers
    and shipping speed options.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "shipping_option",
                "ShippingOption",
                TypeInfo(typing.Union[str, ShippingOption]),
            ),
            (
                "inbound_shipment",
                "InboundShipment",
                TypeInfo(Shipment),
            ),
            (
                "outbound_shipment",
                "OutboundShipment",
                TypeInfo(Shipment),
            ),
        ]

    # The shipping speed for a particular job. This speed doesn't dictate how
    # soon you'll get the Snowball from the job's creation date. This speed
    # represents how quickly it moves to its destination while in transit.
    # Regional shipping speeds are as follows:

    #   * In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.

    #   * In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.

    #   * In India, Snowballs are delivered in one to seven days.

    #   * In the United States of America (US), you have access to one-day shipping and two-day shipping.
    shipping_option: typing.Union[str, "ShippingOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Status` and `TrackingNumber` values for a Snowball being returned to
    # AWS for a particular job.
    inbound_shipment: "Shipment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `Status` and `TrackingNumber` values for a Snowball being delivered to
    # the address that you specified for a particular job.
    outbound_shipment: "Shipment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ShippingOption(str):
    SECOND_DAY = "SECOND_DAY"
    NEXT_DAY = "NEXT_DAY"
    EXPRESS = "EXPRESS"
    STANDARD = "STANDARD"


class SnowballCapacity(str):
    T50 = "T50"
    T80 = "T80"
    T100 = "T100"
    NoPreference = "NoPreference"


class SnowballType(str):
    STANDARD = "STANDARD"
    EDGE = "EDGE"


@dataclasses.dataclass
class UnsupportedAddressException(ShapeBase):
    """
    The address is either outside the serviceable area for your region, or an error
    occurred. Check the address with your region's carrier and try again. If the
    issue persists, contact AWS Support.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateClusterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_id",
                "ClusterId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(JobResource),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "shipping_option",
                "ShippingOption",
                TypeInfo(typing.Union[str, ShippingOption]),
            ),
            (
                "notification",
                "Notification",
                TypeInfo(Notification),
            ),
            (
                "forwarding_address_id",
                "ForwardingAddressId",
                TypeInfo(str),
            ),
        ]

    # The cluster ID of the cluster that you want to update, for example
    # `CID123e4567-e89b-12d3-a456-426655440000`.
    cluster_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new role Amazon Resource Name (ARN) that you want to associate with
    # this cluster. To create a role ARN, use the
    # [CreateRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)
    # API action in AWS Identity and Access Management (IAM).
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description of this cluster.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated arrays of JobResource objects that can include updated
    # S3Resource objects or LambdaResource objects.
    resources: "JobResource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the updated Address object.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated shipping option value of this cluster's ShippingDetails object.
    shipping_option: typing.Union[str, "ShippingOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new or updated Notification object.
    notification: "Notification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated ID for the forwarding address for a cluster. This field is not
    # supported in most regions.
    forwarding_address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateClusterResult(OutputShapeBase):
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
class UpdateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                TypeInfo(Notification),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(JobResource),
            ),
            (
                "address_id",
                "AddressId",
                TypeInfo(str),
            ),
            (
                "shipping_option",
                "ShippingOption",
                TypeInfo(typing.Union[str, ShippingOption]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "snowball_capacity_preference",
                "SnowballCapacityPreference",
                TypeInfo(typing.Union[str, SnowballCapacity]),
            ),
            (
                "forwarding_address_id",
                "ForwardingAddressId",
                TypeInfo(str),
            ),
        ]

    # The job ID of the job that you want to update, for example
    # `JID123e4567-e89b-12d3-a456-426655440000`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new role Amazon Resource Name (ARN) that you want to associate with
    # this job. To create a role ARN, use the
    # [CreateRole](http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)AWS
    # Identity and Access Management (IAM) API action.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new or updated Notification object.
    notification: "Notification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated `JobResource` object, or the updated JobResource object.
    resources: "JobResource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the updated Address object.
    address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated shipping option value of this job's ShippingDetails object.
    shipping_option: typing.Union[str, "ShippingOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated description of this job's JobMetadata object.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated `SnowballCapacityPreference` of this job's JobMetadata object.
    # The 50 TB Snowballs are only available in the US regions.
    snowball_capacity_preference: typing.Union[str, "SnowballCapacity"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The updated ID for the forwarding address for a job. This field is not
    # supported in most regions.
    forwarding_address_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJobResult(OutputShapeBase):
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
