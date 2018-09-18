import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    You do not have sufficient access to perform this action.
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
class CancelSigningProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
        ]

    # The name of the signing profile to be canceled.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Category(str):
    AWSIoT = "AWSIoT"


@dataclasses.dataclass
class DescribeSigningJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
        ]

    # The ID of the signing job on input.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSigningJobResponse(OutputShapeBase):
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
                "jobId",
                TypeInfo(str),
            ),
            (
                "source",
                "source",
                TypeInfo(Source),
            ),
            (
                "signing_material",
                "signingMaterial",
                TypeInfo(SigningMaterial),
            ),
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
            (
                "overrides",
                "overrides",
                TypeInfo(SigningPlatformOverrides),
            ),
            (
                "signing_parameters",
                "signingParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "completed_at",
                "completedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "requested_by",
                "requestedBy",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, SigningStatus]),
            ),
            (
                "status_reason",
                "statusReason",
                TypeInfo(str),
            ),
            (
                "signed_object",
                "signedObject",
                TypeInfo(SignedObject),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the signing job on output.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The object that contains the name of your S3 bucket or your raw code.
    source: "Source" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name (ARN) of your code signing certificate.
    signing_material: "SigningMaterial" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The microcontroller platform to which your signed code image will be
    # distributed.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the profile that initiated the signing operation.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of any overrides that were applied to the signing operation.
    overrides: "SigningPlatformOverrides" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Map of user-assigned key-value pairs used during signing. These values
    # contain any information that you specified for use in your signing job.
    signing_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date and time that the signing job was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date and time that the signing job was completed.
    completed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IAM principal that requested the signing job.
    requested_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the signing job.
    status: typing.Union[str, "SigningStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # String value that contains the status reason.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the S3 bucket where the signed code image is saved by AWS Signer.
    signed_object: "SignedObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Destination(ShapeBase):
    """
    Points to an `S3Destination` object that contains information about your S3
    bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3",
                "s3",
                TypeInfo(S3Destination),
            ),
        ]

    # The `S3Destination` object.
    s3: "S3Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )


class EncryptionAlgorithm(str):
    RSA = "RSA"
    ECDSA = "ECDSA"


@dataclasses.dataclass
class EncryptionAlgorithmOptions(ShapeBase):
    """
    The encryption algorithm options that are available to an AWS Signer job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_values",
                "allowedValues",
                TypeInfo(typing.List[typing.Union[str, EncryptionAlgorithm]]),
            ),
            (
                "default_value",
                "defaultValue",
                TypeInfo(typing.Union[str, EncryptionAlgorithm]),
            ),
        ]

    # The set of accepted encryption algorithms that are allowed in an AWS Signer
    # job.
    allowed_values: typing.List[typing.Union[str, "EncryptionAlgorithm"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The default encryption algorithm that is used by an AWS Signer job.
    default_value: typing.Union[str, "EncryptionAlgorithm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSigningPlatformRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
        ]

    # The ID of the target signing platform.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSigningPlatformResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "partner",
                "partner",
                TypeInfo(str),
            ),
            (
                "target",
                "target",
                TypeInfo(str),
            ),
            (
                "category",
                "category",
                TypeInfo(typing.Union[str, Category]),
            ),
            (
                "signing_configuration",
                "signingConfiguration",
                TypeInfo(SigningConfiguration),
            ),
            (
                "signing_image_format",
                "signingImageFormat",
                TypeInfo(SigningImageFormat),
            ),
            (
                "max_size_in_mb",
                "maxSizeInMB",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the target signing platform.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name of the target signing platform.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of partner entities that use the target signing platform.
    partner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The validation template that is used by the target signing platform.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category type of the target signing platform.
    category: typing.Union[str, "Category"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of configurations applied to the target platform at signing.
    signing_configuration: "SigningConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the target platform's signing image.
    signing_image_format: "SigningImageFormat" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum size (in MB) of the payload that can be signed by the target
    # platform.
    max_size_in_mb: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSigningProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
        ]

    # The name of the target signing profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSigningProfileResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
            (
                "signing_material",
                "signingMaterial",
                TypeInfo(SigningMaterial),
            ),
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "overrides",
                "overrides",
                TypeInfo(SigningPlatformOverrides),
            ),
            (
                "signing_parameters",
                "signingParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, SigningProfileStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the target signing profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the certificate that the target profile uses for signing
    # operations.
    signing_material: "SigningMaterial" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the platform that is used by the target signing profile.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of overrides applied by the target signing profile for signing
    # operations.
    overrides: "SigningPlatformOverrides" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of key-value pairs for signing operations that is attached to the
    # target signing profile.
    signing_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the target signing profile.
    status: typing.Union[str, "SigningProfileStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HashAlgorithm(str):
    SHA1 = "SHA1"
    SHA256 = "SHA256"


@dataclasses.dataclass
class HashAlgorithmOptions(ShapeBase):
    """
    The hash algorithms that are available to an AWS Signer job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_values",
                "allowedValues",
                TypeInfo(typing.List[typing.Union[str, HashAlgorithm]]),
            ),
            (
                "default_value",
                "defaultValue",
                TypeInfo(typing.Union[str, HashAlgorithm]),
            ),
        ]

    # The set of accepted hash algorithms allowed in an AWS Signer job.
    allowed_values: typing.List[typing.Union[str, "HashAlgorithm"]
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The default hash algorithm that is used in an AWS Signer job.
    default_value: typing.Union[str, "HashAlgorithm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ImageFormat(str):
    JSON = "JSON"


@dataclasses.dataclass
class InternalServiceErrorException(ShapeBase):
    """
    An internal error occurred.
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
class ListSigningJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, SigningStatus]),
            ),
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "requested_by",
                "requestedBy",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # A status value with which to filter your results.
    status: typing.Union[str, "SigningStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of microcontroller platform that you specified for the distribution
    # of your code image.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM principal that requested the signing job.
    requested_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the maximum number of items to return in the response. Use this
    # parameter when paginating results. If additional items exist beyond the
    # number you specify, the `nextToken` element is set in the response. Use the
    # `nextToken` value in a subsequent request to retrieve additional items.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String for specifying the next set of paginated results to return. After
    # you receive a response with truncated results, use this parameter in a
    # subsequent request. Set it to the value of `nextToken` from the response
    # that you just received.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSigningJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "jobs",
                "jobs",
                TypeInfo(typing.List[SigningJob]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of your signing jobs.
    jobs: typing.List["SigningJob"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # String for specifying the next set of paginated results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSigningPlatformsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "category",
                "category",
                TypeInfo(str),
            ),
            (
                "partner",
                "partner",
                TypeInfo(str),
            ),
            (
                "target",
                "target",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The category type of a signing platform.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any partner entities connected to a signing platform.
    partner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The validation template that is used by the target signing platform.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned by this operation.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value for specifying the next set of paginated results to return. After you
    # receive a response with truncated results, use this parameter in a
    # subsequent request. Set it to the value of `nextToken` from the response
    # that you just received.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSigningPlatformsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "platforms",
                "platforms",
                TypeInfo(typing.List[SigningPlatform]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of all platforms that match the request parameters.
    platforms: typing.List["SigningPlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Value for specifying the next set of paginated results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSigningProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_canceled",
                "includeCanceled",
                TypeInfo(bool),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # Designates whether to include profiles with the status of `CANCELED`.
    include_canceled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of profiles to be returned.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value for specifying the next set of paginated results to return. After you
    # receive a response with truncated results, use this parameter in a
    # subsequent request. Set it to the value of `nextToken` from the response
    # that you just received.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSigningProfilesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "profiles",
                "profiles",
                TypeInfo(typing.List[SigningProfile]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of profiles that are available in the AWS account. This includes
    # profiles with the status of `CANCELED` if the `includeCanceled` parameter
    # is set to `true`.
    profiles: typing.List["SigningProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Value for specifying the next set of paginated results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSigningProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
            (
                "signing_material",
                "signingMaterial",
                TypeInfo(SigningMaterial),
            ),
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "overrides",
                "overrides",
                TypeInfo(SigningPlatformOverrides),
            ),
            (
                "signing_parameters",
                "signingParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the signing profile to be created.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Certificate Manager certificate that will be used to sign code with
    # the new signing profile.
    signing_material: "SigningMaterial" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the signing profile to be created.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subfield of `platform`. This specifies any different configuration
    # options that you want to apply to the chosen platform (such as a different
    # `hash-algorithm` or `signing-algorithm`).
    overrides: "SigningPlatformOverrides" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Map of key-value pairs for signing. These can include any information that
    # you want to use during signing.
    signing_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutSigningProfileResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the signing profile created.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    A specified resource could not be found.
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
class S3Destination(ShapeBase):
    """
    The name and prefix of the S3 bucket where AWS Signer saves your signed objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                TypeInfo(str),
            ),
            (
                "prefix",
                "prefix",
                TypeInfo(str),
            ),
        ]

    # Name of the S3 bucket.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An Amazon S3 prefix that you can use to limit responses to those that begin
    # with the specified prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3SignedObject(ShapeBase):
    """
    The S3 bucket name and key where AWS Signer saved your signed code image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                TypeInfo(str),
            ),
            (
                "key",
                "key",
                TypeInfo(str),
            ),
        ]

    # Name of the S3 bucket.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key name that uniquely identifies a signed code image in your bucket.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3Source(ShapeBase):
    """
    Information about the S3 bucket where you saved your unsigned code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "bucketName",
                TypeInfo(str),
            ),
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # Name of the S3 bucket.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key name of the bucket object that contains your unsigned code.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of your source image in your version enabled S3 bucket.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SignedObject(ShapeBase):
    """
    Points to an `S3SignedObject` object that contains information about your signed
    code image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3",
                "s3",
                TypeInfo(S3SignedObject),
            ),
        ]

    # The `S3SignedObject`.
    s3: "S3SignedObject" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SigningConfiguration(ShapeBase):
    """
    The configuration of an AWS Signer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_algorithm_options",
                "encryptionAlgorithmOptions",
                TypeInfo(EncryptionAlgorithmOptions),
            ),
            (
                "hash_algorithm_options",
                "hashAlgorithmOptions",
                TypeInfo(HashAlgorithmOptions),
            ),
        ]

    # The encryption algorithm options that are available for an AWS Signer job.
    encryption_algorithm_options: "EncryptionAlgorithmOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The hash algorithm options that are available for an AWS Signer job.
    hash_algorithm_options: "HashAlgorithmOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SigningConfigurationOverrides(ShapeBase):
    """
    A signing configuration that overrides the default encryption or hash algorithm
    of a signing job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_algorithm",
                "encryptionAlgorithm",
                TypeInfo(typing.Union[str, EncryptionAlgorithm]),
            ),
            (
                "hash_algorithm",
                "hashAlgorithm",
                TypeInfo(typing.Union[str, HashAlgorithm]),
            ),
        ]

    # A specified override of the default encryption algorithm that is used in an
    # AWS Signer job.
    encryption_algorithm: typing.Union[str, "EncryptionAlgorithm"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A specified override of the default hash algorithm that is used in an AWS
    # Signer job.
    hash_algorithm: typing.Union[str, "HashAlgorithm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SigningImageFormat(ShapeBase):
    """
    The image format of an AWS Signer platform or profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "supported_formats",
                "supportedFormats",
                TypeInfo(typing.List[typing.Union[str, ImageFormat]]),
            ),
            (
                "default_format",
                "defaultFormat",
                TypeInfo(typing.Union[str, ImageFormat]),
            ),
        ]

    # The supported formats of an AWS Signer signing image.
    supported_formats: typing.List[typing.Union[str, "ImageFormat"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The default format of an AWS Signer signing image.
    default_format: typing.Union[str, "ImageFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SigningJob(ShapeBase):
    """
    Contains information about a signing job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
            (
                "source",
                "source",
                TypeInfo(Source),
            ),
            (
                "signed_object",
                "signedObject",
                TypeInfo(SignedObject),
            ),
            (
                "signing_material",
                "signingMaterial",
                TypeInfo(SigningMaterial),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, SigningStatus]),
            ),
        ]

    # The ID of the signing job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `Source` that contains information about a signing job's code image
    # source.
    source: "Source" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A `SignedObject` structure that contains information about a signing job's
    # signed code image.
    signed_object: "SignedObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `SigningMaterial` object that contains the Amazon Resource Name (ARN) of
    # the certificate used for the signing job.
    signing_material: "SigningMaterial" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the signing job was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the signing job.
    status: typing.Union[str, "SigningStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SigningMaterial(ShapeBase):
    """
    The ACM certificate that is used to sign your code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "certificateArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the certificates that is used to sign
    # your code.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SigningPlatform(ShapeBase):
    """
    Contains information about the signing configurations and parameters that is
    used to perform an AWS Signer job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "partner",
                "partner",
                TypeInfo(str),
            ),
            (
                "target",
                "target",
                TypeInfo(str),
            ),
            (
                "category",
                "category",
                TypeInfo(typing.Union[str, Category]),
            ),
            (
                "signing_configuration",
                "signingConfiguration",
                TypeInfo(SigningConfiguration),
            ),
            (
                "signing_image_format",
                "signingImageFormat",
                TypeInfo(SigningImageFormat),
            ),
            (
                "max_size_in_mb",
                "maxSizeInMB",
                TypeInfo(int),
            ),
        ]

    # The ID of an AWS Signer platform.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name of an AWS Signer platform.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any partner entities linked to an AWS Signer platform.
    partner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The types of targets that can be signed by an AWS Signer platform.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category of an AWS Signer platform.
    category: typing.Union[str, "Category"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration of an AWS Signer platform. This includes the designated
    # hash algorithm and encryption algorithm of a signing platform.
    signing_configuration: "SigningConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The signing image format that is used by an AWS Signer platform.
    signing_image_format: "SigningImageFormat" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum size (in MB) of code that can be signed by a AWS Signer
    # platform.
    max_size_in_mb: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SigningPlatformOverrides(ShapeBase):
    """
    Any overrides that are applied to the signing configuration of an AWS Signer
    platform.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "signing_configuration",
                "signingConfiguration",
                TypeInfo(SigningConfigurationOverrides),
            ),
        ]

    # A signing configuration that overrides the default encryption or hash
    # algorithm of a signing job.
    signing_configuration: "SigningConfigurationOverrides" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SigningProfile(ShapeBase):
    """
    Contains information about the ACM certificates and AWS Signer configuration
    parameters that can be used by a given AWS Signer user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
            (
                "signing_material",
                "signingMaterial",
                TypeInfo(SigningMaterial),
            ),
            (
                "platform_id",
                "platformId",
                TypeInfo(str),
            ),
            (
                "signing_parameters",
                "signingParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, SigningProfileStatus]),
            ),
        ]

    # The name of the AWS Signer profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ACM certificate that is available for use by a signing profile.
    signing_material: "SigningMaterial" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of a platform that is available for use by a signing profile.
    platform_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parameters that are available for use by an AWS Signer user.
    signing_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of an AWS Signer profile.
    status: typing.Union[str, "SigningProfileStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SigningProfileStatus(str):
    Active = "Active"
    Canceled = "Canceled"


class SigningStatus(str):
    InProgress = "InProgress"
    Failed = "Failed"
    Succeeded = "Succeeded"


@dataclasses.dataclass
class Source(ShapeBase):
    """
    An `S3Source` object that contains information about the S3 bucket where you
    saved your unsigned code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3",
                "s3",
                TypeInfo(S3Source),
            ),
        ]

    # The `S3Source` object.
    s3: "S3Source" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSigningJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "source",
                TypeInfo(Source),
            ),
            (
                "destination",
                "destination",
                TypeInfo(Destination),
            ),
            (
                "client_request_token",
                "clientRequestToken",
                TypeInfo(str),
            ),
            (
                "profile_name",
                "profileName",
                TypeInfo(str),
            ),
        ]

    # The S3 bucket that contains the object to sign or a BLOB that contains your
    # raw code.
    source: "Source" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 bucket in which to save your signed object. The destination contains
    # the name of your bucket and an optional prefix.
    destination: "Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String that identifies the signing request. All calls after the first that
    # use this token return the same response as the first call.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the signing profile.
    profile_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSigningJobResponse(OutputShapeBase):
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
                "jobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of your signing job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ThrottlingException(ShapeBase):
    """
    The signing job has been throttled.
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
class ValidationException(ShapeBase):
    """
    You signing certificate could not be validated.
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
