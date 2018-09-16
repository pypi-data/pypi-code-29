import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AbortIncompleteMultipartUpload(ShapeBase):
    """
    Specifies the days since the initiation of an Incomplete Multipart Upload that
    Lifecycle will wait before permanently removing all parts of the upload.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "days_after_initiation",
                "DaysAfterInitiation",
                TypeInfo(int),
            ),
        ]

    # Indicates the number of days that must pass since initiation for Lifecycle
    # to abort an Incomplete Multipart Upload.
    days_after_initiation: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AbortMultipartUploadOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AbortMultipartUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccelerateConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, BucketAccelerateStatus]),
            ),
        ]

    # The accelerate configuration of the bucket.
    status: typing.Union[str, "BucketAccelerateStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessControlPolicy(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grants",
                "Grants",
                TypeInfo(typing.List[Grant]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
        ]

    # A list of grants.
    grants: typing.List["Grant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AccessControlTranslation(ShapeBase):
    """
    Container for information regarding the access control for replicas.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner",
                "Owner",
                TypeInfo(typing.Union[str, OwnerOverride]),
            ),
        ]

    # The override value for the owner of the replica object.
    owner: typing.Union[str, "OwnerOverride"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AnalyticsAndOperator(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The prefix to use when evaluating an AND predicate.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags to use when evaluating an AND predicate.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AnalyticsConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "storage_class_analysis",
                "StorageClassAnalysis",
                TypeInfo(StorageClassAnalysis),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(AnalyticsFilter),
            ),
        ]

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, it indicates that data related to access patterns will be
    # collected and made available to analyze the tradeoffs between different
    # storage classes.
    storage_class_analysis: "StorageClassAnalysis" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filter used to describe a set of objects for analyses. A filter must
    # have exactly one prefix, one tag, or one conjunction
    # (AnalyticsAndOperator). If no filter is provided, all objects will be
    # considered in any analysis.
    filter: "AnalyticsFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AnalyticsExportDestination(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_bucket_destination",
                "S3BucketDestination",
                TypeInfo(AnalyticsS3BucketDestination),
            ),
        ]

    # A destination signifying output to an S3 bucket.
    s3_bucket_destination: "AnalyticsS3BucketDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AnalyticsFilter(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "tag",
                "Tag",
                TypeInfo(Tag),
            ),
            (
                "and_",
                "And",
                TypeInfo(AnalyticsAndOperator),
            ),
        ]

    # The prefix to use when evaluating an analytics filter.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag to use when evaluating an analytics filter.
    tag: "Tag" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A conjunction (logical AND) of predicates, which is used in evaluating an
    # analytics filter. The operator must have at least two predicates.
    and_: "AnalyticsAndOperator" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AnalyticsS3BucketDestination(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, AnalyticsS3ExportFileFormat]),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "bucket_account_id",
                "BucketAccountId",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
        ]

    # The file format used when exporting data to Amazon S3.
    format: typing.Union[str, "AnalyticsS3ExportFileFormat"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The Amazon resource name (ARN) of the bucket to which data is exported.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The account ID that owns the destination bucket. If no account ID is
    # provided, the owner will not be validated prior to exporting data.
    bucket_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix to use when exporting data. The exported data begins with this
    # prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AnalyticsS3ExportFileFormat(str):
    CSV = "CSV"


class Body(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class Bucket(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the bucket.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date the bucket was created.
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BucketAccelerateStatus(str):
    Enabled = "Enabled"
    Suspended = "Suspended"


@dataclasses.dataclass
class BucketAlreadyExists(ShapeBase):
    """
    The requested bucket name is not available. The bucket namespace is shared by
    all users of the system. Please select a different name and try again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BucketAlreadyOwnedByYou(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


class BucketCannedACL(str):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"


@dataclasses.dataclass
class BucketLifecycleConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[LifecycleRule]),
            ),
        ]

    rules: typing.List["LifecycleRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BucketLocationConstraint(str):
    EU = "EU"
    eu_west_1 = "eu-west-1"
    us_west_1 = "us-west-1"
    us_west_2 = "us-west-2"
    ap_south_1 = "ap-south-1"
    ap_southeast_1 = "ap-southeast-1"
    ap_southeast_2 = "ap-southeast-2"
    ap_northeast_1 = "ap-northeast-1"
    sa_east_1 = "sa-east-1"
    cn_north_1 = "cn-north-1"
    eu_central_1 = "eu-central-1"


@dataclasses.dataclass
class BucketLoggingStatus(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logging_enabled",
                "LoggingEnabled",
                TypeInfo(LoggingEnabled),
            ),
        ]

    # Container for logging information. Presence of this element indicates that
    # logging is enabled. Parameters TargetBucket and TargetPrefix are required
    # in this case.
    logging_enabled: "LoggingEnabled" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BucketLogsPermission(str):
    FULL_CONTROL = "FULL_CONTROL"
    READ = "READ"
    WRITE = "WRITE"


class BucketVersioningStatus(str):
    Enabled = "Enabled"
    Suspended = "Suspended"


@dataclasses.dataclass
class CORSConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cors_rules",
                "CORSRules",
                TypeInfo(typing.List[CORSRule]),
            ),
        ]

    cors_rules: typing.List["CORSRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CORSRule(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "allowed_methods",
                "AllowedMethods",
                TypeInfo(typing.List[str]),
            ),
            (
                "allowed_origins",
                "AllowedOrigins",
                TypeInfo(typing.List[str]),
            ),
            (
                "allowed_headers",
                "AllowedHeaders",
                TypeInfo(typing.List[str]),
            ),
            (
                "expose_headers",
                "ExposeHeaders",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_age_seconds",
                "MaxAgeSeconds",
                TypeInfo(int),
            ),
        ]

    # Identifies HTTP methods that the domain/origin specified in the rule is
    # allowed to execute.
    allowed_methods: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more origins you want customers to be able to access the bucket
    # from.
    allowed_origins: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies which headers are allowed in a pre-flight OPTIONS request.
    allowed_headers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more headers in the response that you want customers to be able to
    # access from their applications (for example, from a JavaScript
    # XMLHttpRequest object).
    expose_headers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time in seconds that your browser is to cache the preflight response
    # for the specified resource.
    max_age_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CSVInput(ShapeBase):
    """
    Describes how a CSV-formatted input object is formatted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_header_info",
                "FileHeaderInfo",
                TypeInfo(typing.Union[str, FileHeaderInfo]),
            ),
            (
                "comments",
                "Comments",
                TypeInfo(str),
            ),
            (
                "quote_escape_character",
                "QuoteEscapeCharacter",
                TypeInfo(str),
            ),
            (
                "record_delimiter",
                "RecordDelimiter",
                TypeInfo(str),
            ),
            (
                "field_delimiter",
                "FieldDelimiter",
                TypeInfo(str),
            ),
            (
                "quote_character",
                "QuoteCharacter",
                TypeInfo(str),
            ),
            (
                "allow_quoted_record_delimiter",
                "AllowQuotedRecordDelimiter",
                TypeInfo(bool),
            ),
        ]

    # Describes the first line of input. Valid values: None, Ignore, Use.
    file_header_info: typing.Union[str, "FileHeaderInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Single character used to indicate a row should be ignored when present at
    # the start of a row.
    comments: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Single character used for escaping the quote character inside an already
    # escaped value.
    quote_escape_character: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value used to separate individual records.
    record_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value used to separate individual fields in a record.
    field_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value used for escaping where the field delimiter is part of the value.
    quote_character: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies that CSV field values may contain quoted record delimiters and
    # such records should be allowed. Default value is FALSE. Setting this value
    # to TRUE may lower performance.
    allow_quoted_record_delimiter: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CSVOutput(ShapeBase):
    """
    Describes how CSV-formatted results are formatted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quote_fields",
                "QuoteFields",
                TypeInfo(typing.Union[str, QuoteFields]),
            ),
            (
                "quote_escape_character",
                "QuoteEscapeCharacter",
                TypeInfo(str),
            ),
            (
                "record_delimiter",
                "RecordDelimiter",
                TypeInfo(str),
            ),
            (
                "field_delimiter",
                "FieldDelimiter",
                TypeInfo(str),
            ),
            (
                "quote_character",
                "QuoteCharacter",
                TypeInfo(str),
            ),
        ]

    # Indicates whether or not all output fields should be quoted.
    quote_fields: typing.Union[str, "QuoteFields"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Single character used for escaping the quote character inside an already
    # escaped value.
    quote_escape_character: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value used to separate individual records.
    record_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value used to separate individual fields in a record.
    field_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value used for escaping where the field delimiter is part of the value.
    quote_character: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudFunctionConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "event",
                "Event",
                TypeInfo(typing.Union[str, Event]),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[typing.Union[str, Event]]),
            ),
            (
                "cloud_function",
                "CloudFunction",
                TypeInfo(str),
            ),
            (
                "invocation_role",
                "InvocationRole",
                TypeInfo(str),
            ),
        ]

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bucket event for which to send notifications.
    event: typing.Union[str, "Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    events: typing.List[typing.Union[str, "Event"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    cloud_function: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    invocation_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CommonPrefix(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
        ]

    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompleteMultipartUploadOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the object expiration is configured, this will contain the expiration
    # date (expiry-date) and rule ID (rule-id). The value of rule-id is URL
    # encoded.
    expiration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Entity tag of the object.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CompleteMultipartUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "multipart_upload",
                "MultipartUpload",
                TypeInfo(CompletedMultipartUpload),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    multipart_upload: "CompletedMultipartUpload" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CompletedMultipartUpload(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parts",
                "Parts",
                TypeInfo(typing.List[CompletedPart]),
            ),
        ]

    parts: typing.List["CompletedPart"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CompletedPart(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "part_number",
                "PartNumber",
                TypeInfo(int),
            ),
        ]

    # Entity tag returned when the part was uploaded.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Part number that identifies the part. This is a positive integer between 1
    # and 10,000.
    part_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class CompressionType(str):
    NONE = "NONE"
    GZIP = "GZIP"
    BZIP2 = "BZIP2"


@dataclasses.dataclass
class Condition(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "http_error_code_returned_equals",
                "HttpErrorCodeReturnedEquals",
                TypeInfo(str),
            ),
            (
                "key_prefix_equals",
                "KeyPrefixEquals",
                TypeInfo(str),
            ),
        ]

    # The HTTP error code when the redirect is applied. In the event of an error,
    # if the error code equals this value, then the specified redirect is
    # applied. Required when parent element Condition is specified and sibling
    # KeyPrefixEquals is not specified. If both are specified, then both must be
    # true for the redirect to be applied.
    http_error_code_returned_equals: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The object key name prefix when the redirect is applied. For example, to
    # redirect requests for ExamplePage.html, the key prefix will be
    # ExamplePage.html. To redirect request for all pages with the prefix docs/,
    # the key prefix will be /docs, which identifies all objects in the docs/
    # folder. Required when the parent element Condition is specified and sibling
    # HttpErrorCodeReturnedEquals is not specified. If both conditions are
    # specified, both must be true for the redirect to be applied.
    key_prefix_equals: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContinuationEvent(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CopyObjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_object_result",
                "CopyObjectResult",
                TypeInfo(CopyObjectResult),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(str),
            ),
            (
                "copy_source_version_id",
                "CopySourceVersionId",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    copy_object_result: "CopyObjectResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the object expiration is configured, the response includes this header.
    expiration: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    copy_source_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version ID of the newly created copy.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "copy_source",
                "CopySource",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                TypeInfo(typing.Union[str, ObjectCannedACL]),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "copy_source_if_match",
                "CopySourceIfMatch",
                TypeInfo(str),
            ),
            (
                "copy_source_if_modified_since",
                "CopySourceIfModifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "copy_source_if_none_match",
                "CopySourceIfNoneMatch",
                TypeInfo(str),
            ),
            (
                "copy_source_if_unmodified_since",
                "CopySourceIfUnmodifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata_directive",
                "MetadataDirective",
                TypeInfo(typing.Union[str, MetadataDirective]),
            ),
            (
                "tagging_directive",
                "TaggingDirective",
                TypeInfo(typing.Union[str, TaggingDirective]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_algorithm",
                "CopySourceSSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key",
                "CopySourceSSECustomerKey",
                TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key_md5",
                "CopySourceSSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
            (
                "tagging",
                "Tagging",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source bucket and key name of the source object, separated
    # by a slash (/). Must be URL-encoded.
    copy_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: typing.Union[str, "ObjectCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language the content is in.
    content_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Copies the object if its entity tag (ETag) matches the specified tag.
    copy_source_if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Copies the object if it has been modified since the specified time.
    copy_source_if_modified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Copies the object if its entity tag (ETag) is different than the specified
    # ETag.
    copy_source_if_none_match: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Copies the object if it hasn't been modified since the specified time.
    copy_source_if_unmodified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    grant_full_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the object data and its metadata.
    grant_read: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the object ACL.
    grant_read_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable object.
    grant_write_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the metadata is copied from the source object or replaced
    # with metadata provided in the request.
    metadata_directive: typing.Union[str, "MetadataDirective"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Specifies whether the object tag-set are copied from the source object or
    # replaced with tag-set provided in the request.
    tagging_directive: typing.Union[str, "TaggingDirective"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The type of storage to use for the object. Defaults to 'STANDARD'.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the AWS KMS key ID to use for object encryption. All GET and PUT
    # requests for an object protected by AWS KMS will fail if not made via SSL
    # or using SigV4. Documentation on configuring any of the officially
    # supported AWS SDKs and CLI can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-
    # signature-version
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the algorithm to use when decrypting the source object (e.g.,
    # AES256).
    copy_source_sse_customer_algorithm: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use to
    # decrypt the source object. The encryption key provided in this header must
    # be one that was used when the source object was created.
    copy_source_sse_customer_key: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    copy_source_sse_customer_key_md5: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag-set for the object destination object this value must be used in
    # conjunction with the TaggingDirective. The tag-set must be encoded as URL
    # Query parameters
    tagging: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CopyObjectResult(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
        ]

    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CopyPartResult(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Entity tag of the object.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time at which the object was uploaded.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateBucketConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location_constraint",
                "LocationConstraint",
                TypeInfo(typing.Union[str, BucketLocationConstraint]),
            ),
        ]

    # Specifies the region where the bucket will be created. If you don't specify
    # a region, the bucket will be created in US Standard.
    location_constraint: typing.Union[str, "BucketLocationConstraint"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class CreateBucketOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBucketRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                TypeInfo(typing.Union[str, BucketCannedACL]),
            ),
            (
                "create_bucket_configuration",
                "CreateBucketConfiguration",
                TypeInfo(CreateBucketConfiguration),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                TypeInfo(str),
            ),
            (
                "grant_write",
                "GrantWrite",
                TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the bucket.
    acl: typing.Union[str, "BucketCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    create_bucket_configuration: "CreateBucketConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Allows grantee the read, write, read ACP, and write ACP permissions on the
    # bucket.
    grant_full_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to list the objects in the bucket.
    grant_read: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the bucket ACL.
    grant_read_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to create, overwrite, and delete any object in the bucket.
    grant_write: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable bucket.
    grant_write_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMultipartUploadOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "abort_date",
                "AbortDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "abort_rule_id",
                "AbortRuleId",
                TypeInfo(str),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date when multipart upload will become eligible for abort operation by
    # lifecycle.
    abort_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Id of the lifecycle rule that makes a multipart upload eligible for abort
    # operation.
    abort_rule_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object key for which the multipart upload was initiated.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID for the initiated multipart upload.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMultipartUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                TypeInfo(typing.Union[str, ObjectCannedACL]),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
            (
                "tagging",
                "Tagging",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: typing.Union[str, "ObjectCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language the content is in.
    content_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    grant_full_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the object data and its metadata.
    grant_read: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the object ACL.
    grant_read_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable object.
    grant_write_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The type of storage to use for the object. Defaults to 'STANDARD'.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the AWS KMS key ID to use for object encryption. All GET and PUT
    # requests for an object protected by AWS KMS will fail if not made via SSL
    # or using SigV4. Documentation on configuring any of the officially
    # supported AWS SDKs and CLI can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-
    # signature-version
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag-set for the object. The tag-set must be encoded as URL Query
    # parameters
    tagging: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Delete(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "objects",
                "Objects",
                TypeInfo(typing.List[ObjectIdentifier]),
            ),
            (
                "quiet",
                "Quiet",
                TypeInfo(bool),
            ),
        ]

    objects: typing.List["ObjectIdentifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Element to enable quiet mode for the request. When you add this element,
    # you must set its value to true.
    quiet: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketAnalyticsConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket from which an analytics configuration is deleted.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketCorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketEncryptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the server-side encryption configuration
    # to delete.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketInventoryConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the inventory configuration to delete.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketLifecycleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketMetricsConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the metrics configuration to delete.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketReplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketTaggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBucketWebsiteRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMarkerEntry(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "is_latest",
                "IsLatest",
                TypeInfo(bool),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
        ]

    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The object key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version ID of an object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the object is (true) or is not (false) the latest version
    # of an object.
    is_latest: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                TypeInfo(bool),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the versioned object that was permanently deleted was
    # (true) or was not (false) a delete marker.
    delete_marker: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the version ID of the delete marker created as a result of the
    # DELETE operation.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "mfa",
                "MFA",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The concatenation of the authentication device's serial number, a space,
    # and the value that is displayed on your authentication device.
    mfa: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectTaggingOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The versionId of the object the tag-set was removed from.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteObjectTaggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The versionId of the object that the tag-set will be removed from.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteObjectsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deleted",
                "Deleted",
                TypeInfo(typing.List[DeletedObject]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
            (
                "errors",
                "Errors",
                TypeInfo(typing.List[Error]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    deleted: typing.List["DeletedObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    errors: typing.List["Error"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteObjectsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "delete",
                "Delete",
                TypeInfo(Delete),
            ),
            (
                "mfa",
                "MFA",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    delete: "Delete" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The concatenation of the authentication device's serial number, a space,
    # and the value that is displayed on your authentication device.
    mfa: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeletedObject(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                TypeInfo(bool),
            ),
            (
                "delete_marker_version_id",
                "DeleteMarkerVersionId",
                TypeInfo(str),
            ),
        ]

    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    delete_marker: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    delete_marker_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Destination(ShapeBase):
    """
    Container for replication destination information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "account",
                "Account",
                TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "access_control_translation",
                "AccessControlTranslation",
                TypeInfo(AccessControlTranslation),
            ),
            (
                "encryption_configuration",
                "EncryptionConfiguration",
                TypeInfo(EncryptionConfiguration),
            ),
        ]

    # Amazon resource name (ARN) of the bucket where you want Amazon S3 to store
    # replicas of the object identified by the rule.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Account ID of the destination bucket. Currently this is only being verified
    # if Access Control Translation is enabled
    account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container for information regarding the access control for replicas.
    access_control_translation: "AccessControlTranslation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container for information regarding encryption based configuration for
    # replicas.
    encryption_configuration: "EncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EncodingType(str):
    """
    Requests Amazon S3 to encode the object keys in the response and specifies the
    encoding method to use. An object key may contain any Unicode character;
    however, XML 1.0 parser cannot parse some characters, such as characters with an
    ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you
    can add this parameter to request that Amazon S3 encode the keys in the
    response.
    """
    url = "url"


@dataclasses.dataclass
class Encryption(ShapeBase):
    """
    Describes the server-side encryption that will be applied to the restore
    results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "kms_key_id",
                "KMSKeyId",
                TypeInfo(str),
            ),
            (
                "kms_context",
                "KMSContext",
                TypeInfo(str),
            ),
        ]

    # The server-side encryption algorithm used when storing job results in
    # Amazon S3 (e.g., AES256, aws:kms).
    encryption_type: typing.Union[str, "ServerSideEncryption"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # If the encryption type is aws:kms, this optional value specifies the AWS
    # KMS key ID to use for encryption of job results.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the encryption type is aws:kms, this optional value can be used to
    # specify the encryption context for the restore results.
    kms_context: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionConfiguration(ShapeBase):
    """
    Container for information regarding encryption based configuration for replicas.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replica_kms_key_id",
                "ReplicaKmsKeyID",
                TypeInfo(str),
            ),
        ]

    # The id of the KMS key used to encrypt the replica object.
    replica_kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndEvent(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Error(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ErrorDocument(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
        ]

    # The object key name to use when a 4XX class error occurs.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Event(str):
    """
    Bucket event for which to send notifications.
    """
    s3_ReducedRedundancyLostObject = "s3:ReducedRedundancyLostObject"
    s3_ObjectCreated_Wildcard = "s3:ObjectCreated:*"
    s3_ObjectCreated_Put = "s3:ObjectCreated:Put"
    s3_ObjectCreated_Post = "s3:ObjectCreated:Post"
    s3_ObjectCreated_Copy = "s3:ObjectCreated:Copy"
    s3_ObjectCreated_CompleteMultipartUpload = "s3:ObjectCreated:CompleteMultipartUpload"
    s3_ObjectRemoved_Wildcard = "s3:ObjectRemoved:*"
    s3_ObjectRemoved_Delete = "s3:ObjectRemoved:Delete"
    s3_ObjectRemoved_DeleteMarkerCreated = "s3:ObjectRemoved:DeleteMarkerCreated"


class ExpirationStatus(str):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ExpressionType(str):
    SQL = "SQL"


class FileHeaderInfo(str):
    USE = "USE"
    IGNORE = "IGNORE"
    NONE = "NONE"


@dataclasses.dataclass
class FilterRule(ShapeBase):
    """
    Container for key value pair that defines the criteria for the filter rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, FilterRuleName]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # Object key name prefix or suffix identifying one or more objects to which
    # the filtering rule applies. Maximum prefix length can be up to 1,024
    # characters. Overlapping prefixes and suffixes are not supported. For more
    # information, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    name: typing.Union[str, "FilterRuleName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FilterRuleName(str):
    prefix = "prefix"
    suffix = "suffix"


@dataclasses.dataclass
class GetBucketAccelerateConfigurationOutput(OutputShapeBase):
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
                TypeInfo(typing.Union[str, BucketAccelerateStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The accelerate configuration of the bucket.
    status: typing.Union[str, "BucketAccelerateStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketAccelerateConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    # Name of the bucket for which the accelerate configuration is retrieved.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketAclOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
            (
                "grants",
                "Grants",
                TypeInfo(typing.List[Grant]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of grants.
    grants: typing.List["Grant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketAclRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketAnalyticsConfigurationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                TypeInfo(AnalyticsConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration and any analyses for the analytics filter.
    analytics_configuration: "AnalyticsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketAnalyticsConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket from which an analytics configuration is retrieved.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketCorsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cors_rules",
                "CORSRules",
                TypeInfo(typing.List[CORSRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    cors_rules: typing.List["CORSRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketCorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketEncryptionOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption_configuration",
                "ServerSideEncryptionConfiguration",
                TypeInfo(ServerSideEncryptionConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container for server-side encryption configuration rules. Currently S3
    # supports one rule only.
    server_side_encryption_configuration: "ServerSideEncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketEncryptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket from which the server-side encryption configuration
    # is retrieved.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketInventoryConfigurationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "inventory_configuration",
                "InventoryConfiguration",
                TypeInfo(InventoryConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the inventory configuration.
    inventory_configuration: "InventoryConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketInventoryConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the inventory configuration to retrieve.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLifecycleConfigurationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[LifecycleRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    rules: typing.List["LifecycleRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketLifecycleConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLifecycleOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLifecycleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLocationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location_constraint",
                "LocationConstraint",
                TypeInfo(typing.Union[str, BucketLocationConstraint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    location_constraint: typing.Union[str, "BucketLocationConstraint"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class GetBucketLocationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketLoggingOutput(OutputShapeBase):
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
                TypeInfo(LoggingEnabled),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container for logging information. Presence of this element indicates that
    # logging is enabled. Parameters TargetBucket and TargetPrefix are required
    # in this case.
    logging_enabled: "LoggingEnabled" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketLoggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketMetricsConfigurationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metrics_configuration",
                "MetricsConfiguration",
                TypeInfo(MetricsConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the metrics configuration.
    metrics_configuration: "MetricsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketMetricsConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the metrics configuration to retrieve.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketNotificationConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    # Name of the bucket to get the notification configuration for.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketPolicyOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The bucket policy as a JSON document.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketReplicationOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "replication_configuration",
                "ReplicationConfiguration",
                TypeInfo(ReplicationConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container for replication rules. You can add as many as 1,000 rules. Total
    # replication configuration size can be up to 2 MB.
    replication_configuration: "ReplicationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketReplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketRequestPaymentOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payer",
                "Payer",
                TypeInfo(typing.Union[str, Payer]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies who pays for the download and request fees.
    payer: typing.Union[str, "Payer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketRequestPaymentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketTaggingOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_set",
                "TagSet",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    tag_set: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketTaggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketVersioningOutput(OutputShapeBase):
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
                TypeInfo(typing.Union[str, BucketVersioningStatus]),
            ),
            (
                "mfa_delete",
                "MFADelete",
                TypeInfo(typing.Union[str, MFADeleteStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The versioning state of the bucket.
    status: typing.Union[str, "BucketVersioningStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether MFA delete is enabled in the bucket versioning
    # configuration. This element is only returned if the bucket has been
    # configured with MFA delete. If the bucket has never been so configured,
    # this element is not returned.
    mfa_delete: typing.Union[str, "MFADeleteStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketVersioningRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBucketWebsiteOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "redirect_all_requests_to",
                "RedirectAllRequestsTo",
                TypeInfo(RedirectAllRequestsTo),
            ),
            (
                "index_document",
                "IndexDocument",
                TypeInfo(IndexDocument),
            ),
            (
                "error_document",
                "ErrorDocument",
                TypeInfo(ErrorDocument),
            ),
            (
                "routing_rules",
                "RoutingRules",
                TypeInfo(typing.List[RoutingRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    redirect_all_requests_to: "RedirectAllRequestsTo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    index_document: "IndexDocument" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    error_document: "ErrorDocument" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    routing_rules: typing.List["RoutingRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBucketWebsiteRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectAclOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
            (
                "grants",
                "Grants",
                TypeInfo(typing.List[Grant]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of grants.
    grants: typing.List["Grant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectAclRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "body",
                "Body",
                TypeInfo(typing.Any),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                TypeInfo(bool),
            ),
            (
                "accept_ranges",
                "AcceptRanges",
                TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(str),
            ),
            (
                "restore",
                "Restore",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "missing_meta",
                "MissingMeta",
                TypeInfo(int),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                TypeInfo(str),
            ),
            (
                "content_range",
                "ContentRange",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
            (
                "replication_status",
                "ReplicationStatus",
                TypeInfo(typing.Union[str, ReplicationStatus]),
            ),
            (
                "parts_count",
                "PartsCount",
                TypeInfo(int),
            ),
            (
                "tag_count",
                "TagCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object data.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the object retrieved was (true) or was not (false) a
    # Delete Marker. If false, this response header does not appear in the
    # response.
    delete_marker: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    accept_ranges: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the object expiration is configured (see PUT Bucket lifecycle), the
    # response includes this header. It includes the expiry-date and rule-id key
    # value pairs providing object expiration information. The value of the rule-
    # id is URL encoded.
    expiration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides information about object restoration operation and expiration time
    # of the restored object copy.
    restore: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last modified date of the object
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of the body in bytes.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ETag is an opaque identifier assigned by a web server to a specific
    # version of a resource found at a URL
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is set to the number of metadata entries not returned in x-amz-meta
    # headers. This can happen if you create metadata using an API like SOAP that
    # supports more flexible metadata than the REST API. For example, using SOAP,
    # you can create metadata whose values are not legal HTTP headers.
    missing_meta: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language the content is in.
    content_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The portion of the object returned in the response.
    content_range: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    replication_status: typing.Union[str, "ReplicationStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The count of parts this object has.
    parts_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tags, if any, on the object.
    tag_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
            (
                "if_modified_since",
                "IfModifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "if_none_match",
                "IfNoneMatch",
                TypeInfo(str),
            ),
            (
                "if_unmodified_since",
                "IfUnmodifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "range",
                "Range",
                TypeInfo(str),
            ),
            (
                "response_cache_control",
                "ResponseCacheControl",
                TypeInfo(str),
            ),
            (
                "response_content_disposition",
                "ResponseContentDisposition",
                TypeInfo(str),
            ),
            (
                "response_content_encoding",
                "ResponseContentEncoding",
                TypeInfo(str),
            ),
            (
                "response_content_language",
                "ResponseContentLanguage",
                TypeInfo(str),
            ),
            (
                "response_content_type",
                "ResponseContentType",
                TypeInfo(str),
            ),
            (
                "response_expires",
                "ResponseExpires",
                TypeInfo(datetime.datetime),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
            (
                "part_number",
                "PartNumber",
                TypeInfo(int),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return the object only if its entity tag (ETag) is the same as the one
    # specified, otherwise return a 412 (precondition failed).
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return the object only if it has been modified since the specified time,
    # otherwise return a 304 (not modified).
    if_modified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the object only if its entity tag (ETag) is different from the one
    # specified, otherwise return a 304 (not modified).
    if_none_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return the object only if it has not been modified since the specified
    # time, otherwise return a 412 (precondition failed).
    if_unmodified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Downloads the specified range bytes of an object. For more information
    # about the HTTP Range header, go to
    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
    range: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the Cache-Control header of the response.
    response_cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the Content-Disposition header of the response
    response_content_disposition: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the Content-Encoding header of the response.
    response_content_encoding: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the Content-Language header of the response.
    response_content_language: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the Content-Type header of the response.
    response_content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the Expires header of the response.
    response_expires: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Part number of the object being read. This is a positive integer between 1
    # and 10,000. Effectively performs a 'ranged' GET request for the part
    # specified. Useful for downloading just a part of an object.
    part_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectTaggingOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tag_set",
                "TagSet",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    tag_set: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectTaggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectTorrentOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "body",
                "Body",
                TypeInfo(typing.Any),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectTorrentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlacierJobParameters(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tier",
                "Tier",
                TypeInfo(typing.Union[str, Tier]),
            ),
        ]

    # Glacier retrieval tier at which the restore will be processed.
    tier: typing.Union[str, "Tier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Grant(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grantee",
                "Grantee",
                TypeInfo(Grantee),
            ),
            (
                "permission",
                "Permission",
                TypeInfo(typing.Union[str, Permission]),
            ),
        ]

    grantee: "Grantee" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the permission given to the grantee.
    permission: typing.Union[str, "Permission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Grantee(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, Type]),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
            (
                "id",
                "ID",
                TypeInfo(str),
            ),
            (
                "uri",
                "URI",
                TypeInfo(str),
            ),
        ]

    # Type of grantee
    type: typing.Union[str, "Type"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Screen name of the grantee.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Email address of the grantee.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canonical user ID of the grantee.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # URI of the grantee group.
    uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HeadBucketRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HeadObjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "delete_marker",
                "DeleteMarker",
                TypeInfo(bool),
            ),
            (
                "accept_ranges",
                "AcceptRanges",
                TypeInfo(str),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(str),
            ),
            (
                "restore",
                "Restore",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "missing_meta",
                "MissingMeta",
                TypeInfo(int),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
            (
                "replication_status",
                "ReplicationStatus",
                TypeInfo(typing.Union[str, ReplicationStatus]),
            ),
            (
                "parts_count",
                "PartsCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the object retrieved was (true) or was not (false) a
    # Delete Marker. If false, this response header does not appear in the
    # response.
    delete_marker: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    accept_ranges: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the object expiration is configured (see PUT Bucket lifecycle), the
    # response includes this header. It includes the expiry-date and rule-id key
    # value pairs providing object expiration information. The value of the rule-
    # id is URL encoded.
    expiration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides information about object restoration operation and expiration time
    # of the restored object copy.
    restore: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last modified date of the object
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of the body in bytes.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ETag is an opaque identifier assigned by a web server to a specific
    # version of a resource found at a URL
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is set to the number of metadata entries not returned in x-amz-meta
    # headers. This can happen if you create metadata using an API like SOAP that
    # supports more flexible metadata than the REST API. For example, using SOAP,
    # you can create metadata whose values are not legal HTTP headers.
    missing_meta: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language the content is in.
    content_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    replication_status: typing.Union[str, "ReplicationStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The count of parts this object has.
    parts_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HeadObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
            (
                "if_modified_since",
                "IfModifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "if_none_match",
                "IfNoneMatch",
                TypeInfo(str),
            ),
            (
                "if_unmodified_since",
                "IfUnmodifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "range",
                "Range",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
            (
                "part_number",
                "PartNumber",
                TypeInfo(int),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return the object only if its entity tag (ETag) is the same as the one
    # specified, otherwise return a 412 (precondition failed).
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return the object only if it has been modified since the specified time,
    # otherwise return a 304 (not modified).
    if_modified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the object only if its entity tag (ETag) is different from the one
    # specified, otherwise return a 304 (not modified).
    if_none_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Return the object only if it has not been modified since the specified
    # time, otherwise return a 412 (precondition failed).
    if_unmodified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Downloads the specified range bytes of an object. For more information
    # about the HTTP Range header, go to
    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
    range: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Part number of the object being read. This is a positive integer between 1
    # and 10,000. Effectively performs a 'ranged' HEAD request for the part
    # specified. Useful querying about the size of the part and the number of
    # parts in this object.
    part_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IndexDocument(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "suffix",
                "Suffix",
                TypeInfo(str),
            ),
        ]

    # A suffix that is appended to a request that is for a directory on the
    # website endpoint (e.g. if the suffix is index.html and you make a request
    # to samplebucket/images/ the data that is returned will be for the object
    # with the key name images/index.html) The suffix must not be empty and must
    # not include a slash character.
    suffix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Initiator(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "ID",
                TypeInfo(str),
            ),
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
        ]

    # If the principal is an AWS account, it provides the Canonical User ID. If
    # the principal is an IAM User, it provides a user ARN value.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the Principal.
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputSerialization(ShapeBase):
    """
    Describes the serialization format of the object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "csv",
                "CSV",
                TypeInfo(CSVInput),
            ),
            (
                "compression_type",
                "CompressionType",
                TypeInfo(typing.Union[str, CompressionType]),
            ),
            (
                "json",
                "JSON",
                TypeInfo(JSONInput),
            ),
            (
                "parquet",
                "Parquet",
                TypeInfo(ParquetInput),
            ),
        ]

    # Describes the serialization of a CSV-encoded object.
    csv: "CSVInput" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies object's compression format. Valid values: NONE, GZIP, BZIP2.
    # Default Value: NONE.
    compression_type: typing.Union[str, "CompressionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies JSON as object's input serialization format.
    json: "JSONInput" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies Parquet as object's input serialization format.
    parquet: "ParquetInput" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InventoryConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(InventoryDestination),
            ),
            (
                "is_enabled",
                "IsEnabled",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "included_object_versions",
                "IncludedObjectVersions",
                TypeInfo(typing.Union[str, InventoryIncludedObjectVersions]),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(InventorySchedule),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(InventoryFilter),
            ),
            (
                "optional_fields",
                "OptionalFields",
                TypeInfo(
                    typing.List[typing.Union[str, InventoryOptionalField]]
                ),
            ),
        ]

    # Contains information about where to publish the inventory results.
    destination: "InventoryDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the inventory is enabled or disabled.
    is_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies which object version(s) to included in the inventory results.
    included_object_versions: typing.Union[
        str, "InventoryIncludedObjectVersions"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Specifies the schedule for generating inventory results.
    schedule: "InventorySchedule" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies an inventory filter. The inventory only includes objects that
    # meet the filter's criteria.
    filter: "InventoryFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the optional fields that are included in the inventory results.
    optional_fields: typing.List[typing.Union[str, "InventoryOptionalField"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class InventoryDestination(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_bucket_destination",
                "S3BucketDestination",
                TypeInfo(InventoryS3BucketDestination),
            ),
        ]

    # Contains the bucket name, file format, bucket owner (optional), and prefix
    # (optional) where inventory results are published.
    s3_bucket_destination: "InventoryS3BucketDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventoryEncryption(ShapeBase):
    """
    Contains the type of server-side encryption used to encrypt the inventory
    results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sses3",
                "SSES3",
                TypeInfo(SSES3),
            ),
            (
                "ssekms",
                "SSEKMS",
                TypeInfo(SSEKMS),
            ),
        ]

    # Specifies the use of SSE-S3 to encrypt delievered Inventory reports.
    sses3: "SSES3" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the use of SSE-KMS to encrypt delievered Inventory reports.
    ssekms: "SSEKMS" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InventoryFilter(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
        ]

    # The prefix that an object must have to be included in the inventory
    # results.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InventoryFormat(str):
    CSV = "CSV"
    ORC = "ORC"


class InventoryFrequency(str):
    Daily = "Daily"
    Weekly = "Weekly"


class InventoryIncludedObjectVersions(str):
    All = "All"
    Current = "Current"


class InventoryOptionalField(str):
    Size = "Size"
    LastModifiedDate = "LastModifiedDate"
    StorageClass = "StorageClass"
    ETag = "ETag"
    IsMultipartUploaded = "IsMultipartUploaded"
    ReplicationStatus = "ReplicationStatus"
    EncryptionStatus = "EncryptionStatus"


@dataclasses.dataclass
class InventoryS3BucketDestination(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, InventoryFormat]),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(InventoryEncryption),
            ),
        ]

    # The Amazon resource name (ARN) of the bucket where inventory results will
    # be published.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the output format of the inventory results.
    format: typing.Union[str, "InventoryFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the account that owns the destination bucket.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix that is prepended to all inventory results.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains the type of server-side encryption used to encrypt the inventory
    # results.
    encryption: "InventoryEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InventorySchedule(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "frequency",
                "Frequency",
                TypeInfo(typing.Union[str, InventoryFrequency]),
            ),
        ]

    # Specifies how frequently inventory results are produced.
    frequency: typing.Union[str, "InventoryFrequency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JSONInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, JSONType]),
            ),
        ]

    # The type of JSON. Valid values: Document, Lines.
    type: typing.Union[str, "JSONType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JSONOutput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_delimiter",
                "RecordDelimiter",
                TypeInfo(str),
            ),
        ]

    # The value used to separate individual records in the output.
    record_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class JSONType(str):
    DOCUMENT = "DOCUMENT"
    LINES = "LINES"


@dataclasses.dataclass
class LambdaFunctionConfiguration(ShapeBase):
    """
    Container for specifying the AWS Lambda notification configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_arn",
                "LambdaFunctionArn",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[typing.Union[str, Event]]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(NotificationConfigurationFilter),
            ),
        ]

    # Lambda cloud function ARN that Amazon S3 can invoke when it detects events
    # of the specified type.
    lambda_function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    events: typing.List[typing.Union[str, "Event"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for object key name filtering rules. For information about key
    # name filtering, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    filter: "NotificationConfigurationFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecycleConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecycleExpiration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
            (
                "days",
                "Days",
                TypeInfo(int),
            ),
            (
                "expired_object_delete_marker",
                "ExpiredObjectDeleteMarker",
                TypeInfo(bool),
            ),
        ]

    # Indicates at what date the object is to be moved or deleted. Should be in
    # GMT ISO 8601 Format.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the lifetime, in days, of the objects that are subject to the
    # rule. The value must be a non-zero positive integer.
    days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether Amazon S3 will remove a delete marker with no noncurrent
    # versions. If set to true, the delete marker will be expired; if set to
    # false the policy takes no action. This cannot be specified with Days or
    # Date in a Lifecycle Expiration Policy.
    expired_object_delete_marker: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecycleRule(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ExpirationStatus]),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(LifecycleExpiration),
            ),
            (
                "id",
                "ID",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(LifecycleRuleFilter),
            ),
            (
                "transitions",
                "Transitions",
                TypeInfo(typing.List[Transition]),
            ),
            (
                "noncurrent_version_transitions",
                "NoncurrentVersionTransitions",
                TypeInfo(typing.List[NoncurrentVersionTransition]),
            ),
            (
                "noncurrent_version_expiration",
                "NoncurrentVersionExpiration",
                TypeInfo(NoncurrentVersionExpiration),
            ),
            (
                "abort_incomplete_multipart_upload",
                "AbortIncompleteMultipartUpload",
                TypeInfo(AbortIncompleteMultipartUpload),
            ),
        ]

    # If 'Enabled', the rule is currently being applied. If 'Disabled', the rule
    # is not currently being applied.
    status: typing.Union[str, "ExpirationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    expiration: "LifecycleExpiration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for the rule. The value cannot be longer than 255
    # characters.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Prefix identifying one or more objects to which the rule applies. This is
    # deprecated; use Filter instead.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Filter is used to identify objects that a Lifecycle Rule applies to. A
    # Filter must have exactly one of Prefix, Tag, or And specified.
    filter: "LifecycleRuleFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    transitions: typing.List["Transition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    noncurrent_version_transitions: typing.List["NoncurrentVersionTransition"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # Specifies when noncurrent object versions expire. Upon expiration, Amazon
    # S3 permanently deletes the noncurrent object versions. You set this
    # lifecycle configuration action on a bucket that has versioning enabled (or
    # suspended) to request that Amazon S3 delete noncurrent object versions at a
    # specific period in the object's lifetime.
    noncurrent_version_expiration: "NoncurrentVersionExpiration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the days since the initiation of an Incomplete Multipart Upload
    # that Lifecycle will wait before permanently removing all parts of the
    # upload.
    abort_incomplete_multipart_upload: "AbortIncompleteMultipartUpload" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LifecycleRuleAndOperator(ShapeBase):
    """
    This is used in a Lifecycle Rule Filter to apply a logical AND to two or more
    predicates. The Lifecycle Rule will apply to any object matching all of the
    predicates configured inside the And operator.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # All of these tags must exist in the object's tag set in order for the rule
    # to apply.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LifecycleRuleFilter(ShapeBase):
    """
    The Filter is used to identify objects that a Lifecycle Rule applies to. A
    Filter must have exactly one of Prefix, Tag, or And specified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "tag",
                "Tag",
                TypeInfo(Tag),
            ),
            (
                "and_",
                "And",
                TypeInfo(LifecycleRuleAndOperator),
            ),
        ]

    # Prefix identifying one or more objects to which the rule applies.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This tag must exist in the object's tag set in order for the rule to apply.
    tag: "Tag" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is used in a Lifecycle Rule Filter to apply a logical AND to two or
    # more predicates. The Lifecycle Rule will apply to any object matching all
    # of the predicates configured inside the And operator.
    and_: "LifecycleRuleAndOperator" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBucketAnalyticsConfigurationsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                TypeInfo(str),
            ),
            (
                "analytics_configuration_list",
                "AnalyticsConfigurationList",
                TypeInfo(typing.List[AnalyticsConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the returned list of analytics configurations is
    # complete. A value of true indicates that the list is not complete and the
    # NextContinuationToken will be provided for a subsequent request.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ContinuationToken that represents where this request began.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # NextContinuationToken is sent when isTruncated is true, which indicates
    # that there are more analytics configurations to list. The next request must
    # include this NextContinuationToken. The token is obfuscated and is not a
    # usable value.
    next_continuation_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of analytics configurations for a bucket.
    analytics_configuration_list: typing.List["AnalyticsConfiguration"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class ListBucketAnalyticsConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket from which analytics configurations are retrieved.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ContinuationToken that represents a placeholder from where this request
    # should begin.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBucketInventoryConfigurationsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
            (
                "inventory_configuration_list",
                "InventoryConfigurationList",
                TypeInfo(typing.List[InventoryConfiguration]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If sent in the request, the marker that is used as a starting point for
    # this inventory configuration list response.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of inventory configurations for a bucket.
    inventory_configuration_list: typing.List["InventoryConfiguration"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # Indicates whether the returned list of inventory configurations is
    # truncated in this response. A value of true indicates that the list is
    # truncated.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker used to continue this inventory configuration listing. Use the
    # NextContinuationToken from this response to continue the listing in a
    # subsequent request. The continuation token is an opaque value that Amazon
    # S3 understands.
    next_continuation_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBucketInventoryConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the inventory configurations to retrieve.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker used to continue an inventory configuration listing that has
    # been truncated. Use the NextContinuationToken from a previously truncated
    # list response to continue the listing. The continuation token is an opaque
    # value that Amazon S3 understands.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBucketMetricsConfigurationsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                TypeInfo(str),
            ),
            (
                "metrics_configuration_list",
                "MetricsConfigurationList",
                TypeInfo(typing.List[MetricsConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the returned list of metrics configurations is complete.
    # A value of true indicates that the list is not complete and the
    # NextContinuationToken will be provided for a subsequent request.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker that is used as a starting point for this metrics configuration
    # list response. This value is present if it was sent in the request.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker used to continue a metrics configuration listing that has been
    # truncated. Use the NextContinuationToken from a previously truncated list
    # response to continue the listing. The continuation token is an opaque value
    # that Amazon S3 understands.
    next_continuation_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of metrics configurations for a bucket.
    metrics_configuration_list: typing.List["MetricsConfiguration"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class ListBucketMetricsConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket containing the metrics configurations to retrieve.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The marker that is used to continue a metrics configuration listing that
    # has been truncated. Use the NextContinuationToken from a previously
    # truncated list response to continue the listing. The continuation token is
    # an opaque value that Amazon S3 understands.
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBucketsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "buckets",
                "Buckets",
                TypeInfo(typing.List[Bucket]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    buckets: typing.List["Bucket"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMultipartUploadsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key_marker",
                "KeyMarker",
                TypeInfo(str),
            ),
            (
                "upload_id_marker",
                "UploadIdMarker",
                TypeInfo(str),
            ),
            (
                "next_key_marker",
                "NextKeyMarker",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "next_upload_id_marker",
                "NextUploadIdMarker",
                TypeInfo(str),
            ),
            (
                "max_uploads",
                "MaxUploads",
                TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "uploads",
                "Uploads",
                TypeInfo(typing.List[MultipartUpload]),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key at or after which the listing began.
    key_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Upload ID after which listing began.
    upload_id_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When a list is truncated, this element specifies the value that should be
    # used for the key-marker request parameter in a subsequent request.
    next_key_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When a prefix is provided in the request, this field contains the specified
    # prefix. The result contains only keys starting with the specified prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When a list is truncated, this element specifies the value that should be
    # used for the upload-id-marker request parameter in a subsequent request.
    next_upload_id_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of multipart uploads that could have been included in the
    # response.
    max_uploads: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the returned list of multipart uploads is truncated. A
    # value of true indicates that the list was truncated. The list can be
    # truncated if the number of multipart uploads exceeds the limit allowed or
    # specified by max uploads.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    uploads: typing.List["MultipartUpload"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListMultipartUploadsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListMultipartUploadsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
            (
                "key_marker",
                "KeyMarker",
                TypeInfo(str),
            ),
            (
                "max_uploads",
                "MaxUploads",
                TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "upload_id_marker",
                "UploadIdMarker",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Character you use to group keys.
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Requests Amazon S3 to encode the object keys in the response and specifies
    # the encoding method to use. An object key may contain any Unicode
    # character; however, XML 1.0 parser cannot parse some characters, such as
    # characters with an ASCII value from 0 to 10. For characters that are not
    # supported in XML 1.0, you can add this parameter to request that Amazon S3
    # encode the keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Together with upload-id-marker, this parameter specifies the multipart
    # upload after which listing should begin.
    key_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the maximum number of multipart uploads, from 1 to 1,000, to return in
    # the response body. 1,000 is the maximum number of uploads that can be
    # returned in a response.
    max_uploads: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lists in-progress uploads only for those keys that begin with the specified
    # prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Together with key-marker, specifies the multipart upload after which
    # listing should begin. If key-marker is not specified, the upload-id-marker
    # parameter is ignored.
    upload_id_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectVersionsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "key_marker",
                "KeyMarker",
                TypeInfo(str),
            ),
            (
                "version_id_marker",
                "VersionIdMarker",
                TypeInfo(str),
            ),
            (
                "next_key_marker",
                "NextKeyMarker",
                TypeInfo(str),
            ),
            (
                "next_version_id_marker",
                "NextVersionIdMarker",
                TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                TypeInfo(typing.List[ObjectVersion]),
            ),
            (
                "delete_markers",
                "DeleteMarkers",
                TypeInfo(typing.List[DeleteMarkerEntry]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                TypeInfo(int),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether or not Amazon S3 returned all of the results
    # that satisfied the search criteria. If your results were truncated, you can
    # make a follow-up paginated request using the NextKeyMarker and
    # NextVersionIdMarker response parameters as a starting place in another
    # request to return the rest of the results.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Marks the last Key returned in a truncated response.
    key_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this value for the key marker request parameter in a subsequent
    # request.
    next_key_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this value for the next version id marker parameter in a subsequent
    # request.
    next_version_id_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    versions: typing.List["ObjectVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    delete_markers: typing.List["DeleteMarkerEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    max_keys: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListObjectVersionsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListObjectVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
            (
                "key_marker",
                "KeyMarker",
                TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "version_id_marker",
                "VersionIdMarker",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Requests Amazon S3 to encode the object keys in the response and specifies
    # the encoding method to use. An object key may contain any Unicode
    # character; however, XML 1.0 parser cannot parse some characters, such as
    # characters with an ASCII value from 0 to 10. For characters that are not
    # supported in XML 1.0, you can add this parameter to request that Amazon S3
    # encode the keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the key to start with when listing objects in a bucket.
    key_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the object version you want to start listing from.
    version_id_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
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
                "contents",
                "Contents",
                TypeInfo(typing.List[Object]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                TypeInfo(int),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether or not Amazon S3 returned all of the results
    # that satisfied the search criteria.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When response is truncated (the IsTruncated element value in the response
    # is true), you can use the key name in this field as marker in the
    # subsequent request to get next set of objects. Amazon S3 lists objects in
    # alphabetical order Note: This element is returned only if you have
    # delimiter request parameter specified. If response does not include the
    # NextMaker and it is truncated, you can use the value of the last Key in the
    # response as the marker in the subsequent request to get the next set of
    # object keys.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    contents: typing.List["Object"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    max_keys: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ListObjectsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListObjectsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Requests Amazon S3 to encode the object keys in the response and specifies
    # the encoding method to use. An object key may contain any Unicode
    # character; however, XML 1.0 parser cannot parse some characters, such as
    # characters with an ASCII value from 0 to 10. For characters that are not
    # supported in XML 1.0, you can add this parameter to request that Amazon S3
    # encode the keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the key to start with when listing objects in a bucket.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # list objects request. Bucket owners need not specify this parameter in
    # their requests.
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListObjectsV2Output(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "contents",
                "Contents",
                TypeInfo(typing.List[Object]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "max_keys",
                "MaxKeys",
                TypeInfo(int),
            ),
            (
                "common_prefixes",
                "CommonPrefixes",
                TypeInfo(typing.List[CommonPrefix]),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
            (
                "key_count",
                "KeyCount",
                TypeInfo(int),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
            (
                "next_continuation_token",
                "NextContinuationToken",
                TypeInfo(str),
            ),
            (
                "start_after",
                "StartAfter",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that indicates whether or not Amazon S3 returned all of the results
    # that satisfied the search criteria.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Metadata about each object returned.
    contents: typing.List["Object"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the bucket to list.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # CommonPrefixes contains all (if there are any) keys between Prefix and the
    # next occurrence of the string specified by delimiter
    common_prefixes: typing.List["CommonPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # KeyCount is the number of keys returned with this request. KeyCount will
    # always be less than equals to MaxKeys field. Say you ask for 50 keys, your
    # result will include less than equals 50 keys
    key_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ContinuationToken indicates Amazon S3 that the list is being continued on
    # this bucket with a token. ContinuationToken is obfuscated and is not a real
    # key
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # NextContinuationToken is sent when isTruncated is true which means there
    # are more keys in the bucket that can be listed. The next list requests to
    # Amazon S3 can be continued with this NextContinuationToken.
    # NextContinuationToken is obfuscated and is not a real key
    next_continuation_token: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # StartAfter is where you want Amazon S3 to start listing from. Amazon S3
    # starts listing after this specified key. StartAfter can be any key in the
    # bucket
    start_after: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListObjectsV2Output", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListObjectsV2Request(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "delimiter",
                "Delimiter",
                TypeInfo(str),
            ),
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
            (
                "max_keys",
                "MaxKeys",
                TypeInfo(int),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "continuation_token",
                "ContinuationToken",
                TypeInfo(str),
            ),
            (
                "fetch_owner",
                "FetchOwner",
                TypeInfo(bool),
            ),
            (
                "start_after",
                "StartAfter",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    # Name of the bucket to list.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A delimiter is a character you use to group keys.
    delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Encoding type used by Amazon S3 to encode object keys in the response.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the maximum number of keys returned in the response. The response
    # might contain fewer keys but will never contain more.
    max_keys: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Limits the response to keys that begin with the specified prefix.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ContinuationToken indicates Amazon S3 that the list is being continued on
    # this bucket with a token. ContinuationToken is obfuscated and is not a real
    # key
    continuation_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner field is not present in listV2 by default, if you want to return
    # owner field with each key in the result then set the fetch owner field to
    # true
    fetch_owner: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # StartAfter is where you want Amazon S3 to start listing from. Amazon S3
    # starts listing after this specified key. StartAfter can be any key in the
    # bucket
    start_after: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # list objects request in V2 style. Bucket owners need not specify this
    # parameter in their requests.
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPartsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "abort_date",
                "AbortDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "abort_rule_id",
                "AbortRuleId",
                TypeInfo(str),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "part_number_marker",
                "PartNumberMarker",
                TypeInfo(int),
            ),
            (
                "next_part_number_marker",
                "NextPartNumberMarker",
                TypeInfo(int),
            ),
            (
                "max_parts",
                "MaxParts",
                TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "parts",
                "Parts",
                TypeInfo(typing.List[Part]),
            ),
            (
                "initiator",
                "Initiator",
                TypeInfo(Initiator),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date when multipart upload will become eligible for abort operation by
    # lifecycle.
    abort_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Id of the lifecycle rule that makes a multipart upload eligible for abort
    # operation.
    abort_rule_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object key for which the multipart upload was initiated.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose parts are being listed.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Part number after which listing begins.
    part_number_marker: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When a list is truncated, this element specifies the last part in the list,
    # as well as the value to use for the part-number-marker request parameter in
    # a subsequent request.
    next_part_number_marker: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum number of parts that were allowed in the response.
    max_parts: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the returned list of parts is truncated.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    parts: typing.List["Part"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies who initiated the multipart upload.
    initiator: "Initiator" = dataclasses.field(default=ShapeBase.NOT_SET, )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ListPartsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPartsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "max_parts",
                "MaxParts",
                TypeInfo(int),
            ),
            (
                "part_number_marker",
                "PartNumberMarker",
                TypeInfo(int),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose parts are being listed.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the maximum number of parts to return.
    max_parts: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the part after which listing should begin. Only parts with higher
    # part numbers will be listed.
    part_number_marker: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LoggingEnabled(ShapeBase):
    """
    Container for logging information. Presence of this element indicates that
    logging is enabled. Parameters TargetBucket and TargetPrefix are required in
    this case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_bucket",
                "TargetBucket",
                TypeInfo(str),
            ),
            (
                "target_prefix",
                "TargetPrefix",
                TypeInfo(str),
            ),
            (
                "target_grants",
                "TargetGrants",
                TypeInfo(typing.List[TargetGrant]),
            ),
        ]

    # Specifies the bucket where you want Amazon S3 to store server access logs.
    # You can have your logs delivered to any bucket that you own, including the
    # same bucket that is being logged. You can also configure multiple buckets
    # to deliver their logs to the same target bucket. In this case you should
    # choose a different TargetPrefix for each source bucket so that the
    # delivered log files can be distinguished by key.
    target_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This element lets you specify a prefix for the keys that the log files will
    # be stored under.
    target_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    target_grants: typing.List["TargetGrant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class MFADelete(str):
    Enabled = "Enabled"
    Disabled = "Disabled"


class MFADeleteStatus(str):
    Enabled = "Enabled"
    Disabled = "Disabled"


class MetadataDirective(str):
    COPY = "COPY"
    REPLACE = "REPLACE"


@dataclasses.dataclass
class MetadataEntry(ShapeBase):
    """
    A metadata key-value pair to store with an object.
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

    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricsAndOperator(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The prefix used when evaluating an AND predicate.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags used when evaluating an AND predicate.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricsConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(MetricsFilter),
            ),
        ]

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a metrics configuration filter. The metrics configuration will
    # only include objects that meet the filter's criteria. A filter must be a
    # prefix, a tag, or a conjunction (MetricsAndOperator).
    filter: "MetricsFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricsFilter(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "tag",
                "Tag",
                TypeInfo(Tag),
            ),
            (
                "and_",
                "And",
                TypeInfo(MetricsAndOperator),
            ),
        ]

    # The prefix used when evaluating a metrics filter.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag used when evaluating a metrics filter.
    tag: "Tag" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A conjunction (logical AND) of predicates, which is used in evaluating a
    # metrics filter. The operator must have at least two predicates, and an
    # object must match all of the predicates in order for the filter to apply.
    and_: "MetricsAndOperator" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MultipartUpload(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "initiated",
                "Initiated",
                TypeInfo(datetime.datetime),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
            (
                "initiator",
                "Initiator",
                TypeInfo(Initiator),
            ),
        ]

    # Upload ID that identifies the multipart upload.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key of the object for which the multipart upload was initiated.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time at which the multipart upload was initiated.
    initiated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies who initiated the multipart upload.
    initiator: "Initiator" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchBucket(ShapeBase):
    """
    The specified bucket does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchKey(ShapeBase):
    """
    The specified key does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoSuchUpload(ShapeBase):
    """
    The specified multipart upload does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class NoncurrentVersionExpiration(ShapeBase):
    """
    Specifies when noncurrent object versions expire. Upon expiration, Amazon S3
    permanently deletes the noncurrent object versions. You set this lifecycle
    configuration action on a bucket that has versioning enabled (or suspended) to
    request that Amazon S3 delete noncurrent object versions at a specific period in
    the object's lifetime.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "noncurrent_days",
                "NoncurrentDays",
                TypeInfo(int),
            ),
        ]

    # Specifies the number of days an object is noncurrent before Amazon S3 can
    # perform the associated action. For information about the noncurrent days
    # calculations, see [How Amazon S3 Calculates When an Object Became
    # Noncurrent](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-
    # control.html) in the Amazon Simple Storage Service Developer Guide.
    noncurrent_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoncurrentVersionTransition(ShapeBase):
    """
    Container for the transition rule that describes when noncurrent objects
    transition to the STANDARD_IA, ONEZONE_IA or GLACIER storage class. If your
    bucket is versioning-enabled (or versioning is suspended), you can set this
    action to request that Amazon S3 transition noncurrent object versions to the
    STANDARD_IA, ONEZONE_IA or GLACIER storage class at a specific period in the
    object's lifetime.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "noncurrent_days",
                "NoncurrentDays",
                TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, TransitionStorageClass]),
            ),
        ]

    # Specifies the number of days an object is noncurrent before Amazon S3 can
    # perform the associated action. For information about the noncurrent days
    # calculations, see [How Amazon S3 Calculates When an Object Became
    # Noncurrent](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-
    # control.html) in the Amazon Simple Storage Service Developer Guide.
    noncurrent_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "TransitionStorageClass"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


@dataclasses.dataclass
class NotificationConfiguration(OutputShapeBase):
    """
    Container for specifying the notification configuration of the bucket. If this
    element is empty, notifications are turned off on the bucket.
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
                "topic_configurations",
                "TopicConfigurations",
                TypeInfo(typing.List[TopicConfiguration]),
            ),
            (
                "queue_configurations",
                "QueueConfigurations",
                TypeInfo(typing.List[QueueConfiguration]),
            ),
            (
                "lambda_function_configurations",
                "LambdaFunctionConfigurations",
                TypeInfo(typing.List[LambdaFunctionConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    topic_configurations: typing.List["TopicConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    queue_configurations: typing.List["QueueConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    lambda_function_configurations: typing.List["LambdaFunctionConfiguration"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )


@dataclasses.dataclass
class NotificationConfigurationDeprecated(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "topic_configuration",
                "TopicConfiguration",
                TypeInfo(TopicConfigurationDeprecated),
            ),
            (
                "queue_configuration",
                "QueueConfiguration",
                TypeInfo(QueueConfigurationDeprecated),
            ),
            (
                "cloud_function_configuration",
                "CloudFunctionConfiguration",
                TypeInfo(CloudFunctionConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    topic_configuration: "TopicConfigurationDeprecated" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    queue_configuration: "QueueConfigurationDeprecated" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    cloud_function_configuration: "CloudFunctionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotificationConfigurationFilter(ShapeBase):
    """
    Container for object key name filtering rules. For information about key name
    filtering, go to [Configuring Event
    Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    in the Amazon Simple Storage Service Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(S3KeyFilter),
            ),
        ]

    # Container for object key name prefix and suffix filtering rules.
    key: "S3KeyFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Object(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, ObjectStorageClass]),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
        ]

    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "ObjectStorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ObjectAlreadyInActiveTierError(ShapeBase):
    """
    This operation is not allowed against this storage tier
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ObjectCannedACL(str):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"
    aws_exec_read = "aws-exec-read"
    bucket_owner_read = "bucket-owner-read"
    bucket_owner_full_control = "bucket-owner-full-control"


@dataclasses.dataclass
class ObjectIdentifier(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    # Key name of the object to delete.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VersionId for the specific version of the object to delete.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ObjectNotInActiveTierError(ShapeBase):
    """
    The source object of the COPY operation is not in the active tier and is only
    stored in Amazon Glacier.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ObjectStorageClass(str):
    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    GLACIER = "GLACIER"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"


@dataclasses.dataclass
class ObjectVersion(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, ObjectVersionStorageClass]),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "is_latest",
                "IsLatest",
                TypeInfo(bool),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(Owner),
            ),
        ]

    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size in bytes of the object.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "ObjectVersionStorageClass"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The object key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version ID of an object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the object is (true) or is not (false) the latest version
    # of an object.
    is_latest: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    owner: "Owner" = dataclasses.field(default=ShapeBase.NOT_SET, )


class ObjectVersionStorageClass(str):
    STANDARD = "STANDARD"


@dataclasses.dataclass
class OutputLocation(ShapeBase):
    """
    Describes the location where the restore job's output is stored.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3",
                "S3",
                TypeInfo(S3Location),
            ),
        ]

    # Describes an S3 location that will receive the results of the restore
    # request.
    s3: "S3Location" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputSerialization(ShapeBase):
    """
    Describes how results of the Select job are serialized.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "csv",
                "CSV",
                TypeInfo(CSVOutput),
            ),
            (
                "json",
                "JSON",
                TypeInfo(JSONOutput),
            ),
        ]

    # Describes the serialization of CSV-encoded Select results.
    csv: "CSVOutput" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies JSON as request's output serialization format.
    json: "JSONOutput" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Owner(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "display_name",
                "DisplayName",
                TypeInfo(str),
            ),
            (
                "id",
                "ID",
                TypeInfo(str),
            ),
        ]

    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OwnerOverride(str):
    Destination = "Destination"


@dataclasses.dataclass
class ParquetInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Part(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "part_number",
                "PartNumber",
                TypeInfo(int),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
        ]

    # Part number identifying the part. This is a positive integer between 1 and
    # 10,000.
    part_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time at which the part was uploaded.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Entity tag returned when the part was uploaded.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size of the uploaded part data.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Payer(str):
    Requester = "Requester"
    BucketOwner = "BucketOwner"


class Permission(str):
    FULL_CONTROL = "FULL_CONTROL"
    WRITE = "WRITE"
    WRITE_ACP = "WRITE_ACP"
    READ = "READ"
    READ_ACP = "READ_ACP"


@dataclasses.dataclass
class Progress(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bytes_scanned",
                "BytesScanned",
                TypeInfo(int),
            ),
            (
                "bytes_processed",
                "BytesProcessed",
                TypeInfo(int),
            ),
            (
                "bytes_returned",
                "BytesReturned",
                TypeInfo(int),
            ),
        ]

    # Current number of object bytes scanned.
    bytes_scanned: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current number of uncompressed object bytes processed.
    bytes_processed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current number of bytes of records payload data returned.
    bytes_returned: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProgressEvent(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "Details",
                TypeInfo(Progress),
            ),
        ]

    # The Progress event details.
    details: "Progress" = dataclasses.field(default=ShapeBase.NOT_SET, )


class Protocol(str):
    http = "http"
    https = "https"


@dataclasses.dataclass
class PutBucketAccelerateConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "accelerate_configuration",
                "AccelerateConfiguration",
                TypeInfo(AccelerateConfiguration),
            ),
        ]

    # Name of the bucket for which the accelerate configuration is set.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the Accelerate Configuration you want to set for the bucket.
    accelerate_configuration: "AccelerateConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketAclRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                TypeInfo(typing.Union[str, BucketCannedACL]),
            ),
            (
                "access_control_policy",
                "AccessControlPolicy",
                TypeInfo(AccessControlPolicy),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                TypeInfo(str),
            ),
            (
                "grant_write",
                "GrantWrite",
                TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the bucket.
    acl: typing.Union[str, "BucketCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    access_control_policy: "AccessControlPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee the read, write, read ACP, and write ACP permissions on the
    # bucket.
    grant_full_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to list the objects in the bucket.
    grant_read: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the bucket ACL.
    grant_read_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to create, overwrite, and delete any object in the bucket.
    grant_write: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable bucket.
    grant_write_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketAnalyticsConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "analytics_configuration",
                "AnalyticsConfiguration",
                TypeInfo(AnalyticsConfiguration),
            ),
        ]

    # The name of the bucket to which an analytics configuration is stored.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier used to represent an analytics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration and any analyses for the analytics filter.
    analytics_configuration: "AnalyticsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketCorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "cors_configuration",
                "CORSConfiguration",
                TypeInfo(CORSConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    cors_configuration: "CORSConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketEncryptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "server_side_encryption_configuration",
                "ServerSideEncryptionConfiguration",
                TypeInfo(ServerSideEncryptionConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    # The name of the bucket for which the server-side encryption configuration
    # is set.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for server-side encryption configuration rules. Currently S3
    # supports one rule only.
    server_side_encryption_configuration: "ServerSideEncryptionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The base64-encoded 128-bit MD5 digest of the server-side encryption
    # configuration.
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketInventoryConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "inventory_configuration",
                "InventoryConfiguration",
                TypeInfo(InventoryConfiguration),
            ),
        ]

    # The name of the bucket where the inventory configuration will be stored.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the inventory configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the inventory configuration.
    inventory_configuration: "InventoryConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketLifecycleConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "lifecycle_configuration",
                "LifecycleConfiguration",
                TypeInfo(BucketLifecycleConfiguration),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    lifecycle_configuration: "BucketLifecycleConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketLifecycleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "lifecycle_configuration",
                "LifecycleConfiguration",
                TypeInfo(LifecycleConfiguration),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    lifecycle_configuration: "LifecycleConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketLoggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "bucket_logging_status",
                "BucketLoggingStatus",
                TypeInfo(BucketLoggingStatus),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    bucket_logging_status: "BucketLoggingStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketMetricsConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "metrics_configuration",
                "MetricsConfiguration",
                TypeInfo(MetricsConfiguration),
            ),
        ]

    # The name of the bucket for which the metrics configuration is set.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID used to identify the metrics configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the metrics configuration.
    metrics_configuration: "MetricsConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketNotificationConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "notification_configuration",
                "NotificationConfiguration",
                TypeInfo(NotificationConfiguration),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for specifying the notification configuration of the bucket. If
    # this element is empty, notifications are turned off on the bucket.
    notification_configuration: "NotificationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketNotificationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "notification_configuration",
                "NotificationConfiguration",
                TypeInfo(NotificationConfigurationDeprecated),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    notification_configuration: "NotificationConfigurationDeprecated" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "confirm_remove_self_bucket_access",
                "ConfirmRemoveSelfBucketAccess",
                TypeInfo(bool),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bucket policy as a JSON document.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set this parameter to true to confirm that you want to remove your
    # permissions to change this bucket policy in the future.
    confirm_remove_self_bucket_access: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutBucketReplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "replication_configuration",
                "ReplicationConfiguration",
                TypeInfo(ReplicationConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for replication rules. You can add as many as 1,000 rules. Total
    # replication configuration size can be up to 2 MB.
    replication_configuration: "ReplicationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketRequestPaymentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "request_payment_configuration",
                "RequestPaymentConfiguration",
                TypeInfo(RequestPaymentConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    request_payment_configuration: "RequestPaymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketTaggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "tagging",
                "Tagging",
                TypeInfo(Tagging),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tagging: "Tagging" = dataclasses.field(default=ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketVersioningRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "versioning_configuration",
                "VersioningConfiguration",
                TypeInfo(VersioningConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "mfa",
                "MFA",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    versioning_configuration: "VersioningConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The concatenation of the authentication device's serial number, a space,
    # and the value that is displayed on your authentication device.
    mfa: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBucketWebsiteRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "website_configuration",
                "WebsiteConfiguration",
                TypeInfo(WebsiteConfiguration),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    website_configuration: "WebsiteConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectAclOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutObjectAclRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                TypeInfo(typing.Union[str, ObjectCannedACL]),
            ),
            (
                "access_control_policy",
                "AccessControlPolicy",
                TypeInfo(AccessControlPolicy),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                TypeInfo(str),
            ),
            (
                "grant_write",
                "GrantWrite",
                TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: typing.Union[str, "ObjectCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    access_control_policy: "AccessControlPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee the read, write, read ACP, and write ACP permissions on the
    # bucket.
    grant_full_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to list the objects in the bucket.
    grant_read: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the bucket ACL.
    grant_read_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to create, overwrite, and delete any object in the bucket.
    grant_write: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable bucket.
    grant_write_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # VersionId used to reference a specific version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the object expiration is configured, this will contain the expiration
    # date (expiry-date) and rule ID (rule-id). The value of rule-id is URL
    # encoded.
    expiration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Entity tag for the uploaded object.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Version of the object.
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "acl",
                "ACL",
                TypeInfo(typing.Union[str, ObjectCannedACL]),
            ),
            (
                "body",
                "Body",
                TypeInfo(typing.Any),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "content_disposition",
                "ContentDisposition",
                TypeInfo(str),
            ),
            (
                "content_encoding",
                "ContentEncoding",
                TypeInfo(str),
            ),
            (
                "content_language",
                "ContentLanguage",
                TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "expires",
                "Expires",
                TypeInfo(datetime.datetime),
            ),
            (
                "grant_full_control",
                "GrantFullControl",
                TypeInfo(str),
            ),
            (
                "grant_read",
                "GrantRead",
                TypeInfo(str),
            ),
            (
                "grant_read_acp",
                "GrantReadACP",
                TypeInfo(str),
            ),
            (
                "grant_write_acp",
                "GrantWriteACP",
                TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
            (
                "website_redirect_location",
                "WebsiteRedirectLocation",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
            (
                "tagging",
                "Tagging",
                TypeInfo(str),
            ),
        ]

    # Name of the bucket to which the PUT operation was initiated.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object key for which the PUT operation was initiated.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the object.
    acl: typing.Union[str, "ObjectCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Object data.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies caching behavior along the request/reply chain.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies presentational information for the object.
    content_disposition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies what content encodings have been applied to the object and thus
    # what decoding mechanisms must be applied to obtain the media-type
    # referenced by the Content-Type header field.
    content_encoding: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The language the content is in.
    content_language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size of the body in bytes. This parameter is useful when the size of the
    # body cannot be determined automatically.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base64-encoded 128-bit MD5 digest of the part data.
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard MIME type describing the format of the object data.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time at which the object is no longer cacheable.
    expires: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    grant_full_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the object data and its metadata.
    grant_read: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to read the object ACL.
    grant_read_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows grantee to write the ACL for the applicable object.
    grant_write_acp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of metadata to store with the object in S3.
    metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The type of storage to use for the object. Defaults to 'STANDARD'.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the bucket is configured as a website, redirects requests for this
    # object to another object in the same bucket or to an external URL. Amazon
    # S3 stores the value of this header in the object metadata.
    website_redirect_location: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the AWS KMS key ID to use for object encryption. All GET and PUT
    # requests for an object protected by AWS KMS will fail if not made via SSL
    # or using SigV4. Documentation on configuring any of the officially
    # supported AWS SDKs and CLI can be found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-
    # signature-version
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag-set for the object. The tag-set must be encoded as URL Query
    # parameters
    tagging: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectTaggingOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutObjectTaggingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "tagging",
                "Tagging",
                TypeInfo(Tagging),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tagging: "Tagging" = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueueConfiguration(ShapeBase):
    """
    Container for specifying an configuration when you want Amazon S3 to publish
    events to an Amazon Simple Queue Service (Amazon SQS) queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_arn",
                "QueueArn",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[typing.Union[str, Event]]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(NotificationConfigurationFilter),
            ),
        ]

    # Amazon SQS queue ARN to which Amazon S3 will publish a message when it
    # detects events of specified type.
    queue_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    events: typing.List[typing.Union[str, "Event"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for object key name filtering rules. For information about key
    # name filtering, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    filter: "NotificationConfigurationFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QueueConfigurationDeprecated(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "event",
                "Event",
                TypeInfo(typing.Union[str, Event]),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[typing.Union[str, Event]]),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
        ]

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bucket event for which to send notifications.
    event: typing.Union[str, "Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    events: typing.List[typing.Union[str, "Event"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class QuoteFields(str):
    ALWAYS = "ALWAYS"
    ASNEEDED = "ASNEEDED"


@dataclasses.dataclass
class RecordsEvent(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payload",
                "Payload",
                TypeInfo(typing.Any),
            ),
        ]

    # The byte array of partial, one or more result records.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Redirect(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_name",
                "HostName",
                TypeInfo(str),
            ),
            (
                "http_redirect_code",
                "HttpRedirectCode",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, Protocol]),
            ),
            (
                "replace_key_prefix_with",
                "ReplaceKeyPrefixWith",
                TypeInfo(str),
            ),
            (
                "replace_key_with",
                "ReplaceKeyWith",
                TypeInfo(str),
            ),
        ]

    # The host name to use in the redirect request.
    host_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP redirect code to use on the response. Not required if one of the
    # siblings is present.
    http_redirect_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Protocol to use (http, https) when redirecting requests. The default is the
    # protocol that is used in the original request.
    protocol: typing.Union[str, "Protocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The object key prefix to use in the redirect request. For example, to
    # redirect requests for all pages with prefix docs/ (objects in the docs/
    # folder) to documents/, you can set a condition block with KeyPrefixEquals
    # set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents.
    # Not required if one of the siblings is present. Can be present only if
    # ReplaceKeyWith is not provided.
    replace_key_prefix_with: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specific object key to use in the redirect request. For example,
    # redirect request to error.html. Not required if one of the sibling is
    # present. Can be present only if ReplaceKeyPrefixWith is not provided.
    replace_key_with: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RedirectAllRequestsTo(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_name",
                "HostName",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(typing.Union[str, Protocol]),
            ),
        ]

    # Name of the host where requests will be redirected.
    host_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Protocol to use (http, https) when redirecting requests. The default is the
    # protocol that is used in the original request.
    protocol: typing.Union[str, "Protocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationConfiguration(ShapeBase):
    """
    Container for replication rules. You can add as many as 1,000 rules. Total
    replication configuration size can be up to 2 MB.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[ReplicationRule]),
            ),
        ]

    # Amazon Resource Name (ARN) of an IAM role for Amazon S3 to assume when
    # replicating the objects.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for information about a particular replication rule. Replication
    # configuration must have at least one rule and can contain up to 1,000
    # rules.
    rules: typing.List["ReplicationRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicationRule(ShapeBase):
    """
    Container for information about a particular replication rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ReplicationRuleStatus]),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(Destination),
            ),
            (
                "id",
                "ID",
                TypeInfo(str),
            ),
            (
                "source_selection_criteria",
                "SourceSelectionCriteria",
                TypeInfo(SourceSelectionCriteria),
            ),
        ]

    # Object keyname prefix identifying one or more objects to which the rule
    # applies. Maximum prefix length can be up to 1,024 characters. Overlapping
    # prefixes are not supported.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The rule is ignored if status is not Enabled.
    status: typing.Union[str, "ReplicationRuleStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container for replication destination information.
    destination: "Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the rule. The value cannot be longer than 255
    # characters.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for filters that define which source objects should be
    # replicated.
    source_selection_criteria: "SourceSelectionCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReplicationRuleStatus(str):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ReplicationStatus(str):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    FAILED = "FAILED"
    REPLICA = "REPLICA"


class RequestCharged(str):
    """
    If present, indicates that the requester was successfully charged for the
    request.
    """
    requester = "requester"


class RequestPayer(str):
    """
    Confirms that the requester knows that she or he will be charged for the
    request. Bucket owners need not specify this parameter in their requests.
    Documentation on downloading objects from requester pays buckets can be found at
    http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    """
    requester = "requester"


@dataclasses.dataclass
class RequestPaymentConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payer",
                "Payer",
                TypeInfo(typing.Union[str, Payer]),
            ),
        ]

    # Specifies who pays for the download and request fees.
    payer: typing.Union[str, "Payer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RequestProgress(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # Specifies whether periodic QueryProgress frames should be sent. Valid
    # values: TRUE, FALSE. Default value: FALSE.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreObjectOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
            (
                "restore_output_path",
                "RestoreOutputPath",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the path in the provided S3 output location where Select results
    # will be restored to.
    restore_output_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "version_id",
                "VersionId",
                TypeInfo(str),
            ),
            (
                "restore_request",
                "RestoreRequest",
                TypeInfo(RestoreRequest),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for restore job parameters.
    restore_request: "RestoreRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreRequest(ShapeBase):
    """
    Container for restore job parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "days",
                "Days",
                TypeInfo(int),
            ),
            (
                "glacier_job_parameters",
                "GlacierJobParameters",
                TypeInfo(GlacierJobParameters),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, RestoreRequestType]),
            ),
            (
                "tier",
                "Tier",
                TypeInfo(typing.Union[str, Tier]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "select_parameters",
                "SelectParameters",
                TypeInfo(SelectParameters),
            ),
            (
                "output_location",
                "OutputLocation",
                TypeInfo(OutputLocation),
            ),
        ]

    # Lifetime of the active copy in days. Do not use with restores that specify
    # OutputLocation.
    days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Glacier related parameters pertaining to this job. Do not use with restores
    # that specify OutputLocation.
    glacier_job_parameters: "GlacierJobParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of restore request.
    type: typing.Union[str, "RestoreRequestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Glacier retrieval tier at which the restore will be processed.
    tier: typing.Union[str, "Tier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The optional description for the job.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the parameters for Select job types.
    select_parameters: "SelectParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the location where the restore job's output is stored.
    output_location: "OutputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RestoreRequestType(str):
    SELECT = "SELECT"


@dataclasses.dataclass
class RoutingRule(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "redirect",
                "Redirect",
                TypeInfo(Redirect),
            ),
            (
                "condition",
                "Condition",
                TypeInfo(Condition),
            ),
        ]

    # Container for redirect information. You can redirect requests to another
    # host, to another page, or with another protocol. In the event of an error,
    # you can can specify a different error code to return.
    redirect: "Redirect" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A container for describing a condition that must be met for the specified
    # redirect to apply. For example, 1. If request is for pages in the /docs
    # folder, redirect to the /documents folder. 2. If request results in HTTP
    # error 4xx, redirect request to another host where you might process the
    # error.
    condition: "Condition" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Rule(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ExpirationStatus]),
            ),
            (
                "expiration",
                "Expiration",
                TypeInfo(LifecycleExpiration),
            ),
            (
                "id",
                "ID",
                TypeInfo(str),
            ),
            (
                "transition",
                "Transition",
                TypeInfo(Transition),
            ),
            (
                "noncurrent_version_transition",
                "NoncurrentVersionTransition",
                TypeInfo(NoncurrentVersionTransition),
            ),
            (
                "noncurrent_version_expiration",
                "NoncurrentVersionExpiration",
                TypeInfo(NoncurrentVersionExpiration),
            ),
            (
                "abort_incomplete_multipart_upload",
                "AbortIncompleteMultipartUpload",
                TypeInfo(AbortIncompleteMultipartUpload),
            ),
        ]

    # Prefix identifying one or more objects to which the rule applies.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If 'Enabled', the rule is currently being applied. If 'Disabled', the rule
    # is not currently being applied.
    status: typing.Union[str, "ExpirationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    expiration: "LifecycleExpiration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier for the rule. The value cannot be longer than 255
    # characters.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    transition: "Transition" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for the transition rule that describes when noncurrent objects
    # transition to the STANDARD_IA, ONEZONE_IA or GLACIER storage class. If your
    # bucket is versioning-enabled (or versioning is suspended), you can set this
    # action to request that Amazon S3 transition noncurrent object versions to
    # the STANDARD_IA, ONEZONE_IA or GLACIER storage class at a specific period
    # in the object's lifetime.
    noncurrent_version_transition: "NoncurrentVersionTransition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies when noncurrent object versions expire. Upon expiration, Amazon
    # S3 permanently deletes the noncurrent object versions. You set this
    # lifecycle configuration action on a bucket that has versioning enabled (or
    # suspended) to request that Amazon S3 delete noncurrent object versions at a
    # specific period in the object's lifetime.
    noncurrent_version_expiration: "NoncurrentVersionExpiration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the days since the initiation of an Incomplete Multipart Upload
    # that Lifecycle will wait before permanently removing all parts of the
    # upload.
    abort_incomplete_multipart_upload: "AbortIncompleteMultipartUpload" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3KeyFilter(ShapeBase):
    """
    Container for object key name prefix and suffix filtering rules.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_rules",
                "FilterRules",
                TypeInfo(typing.List[FilterRule]),
            ),
        ]

    # A list of containers for key value pair that defines the criteria for the
    # filter rule.
    filter_rules: typing.List["FilterRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3Location(ShapeBase):
    """
    Describes an S3 location that will receive the results of the restore request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(Encryption),
            ),
            (
                "canned_acl",
                "CannedACL",
                TypeInfo(typing.Union[str, ObjectCannedACL]),
            ),
            (
                "access_control_list",
                "AccessControlList",
                TypeInfo(typing.List[Grant]),
            ),
            (
                "tagging",
                "Tagging",
                TypeInfo(Tagging),
            ),
            (
                "user_metadata",
                "UserMetadata",
                TypeInfo(typing.List[MetadataEntry]),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
        ]

    # The name of the bucket where the restore results will be placed.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prefix that is prepended to the restore results for this request.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the server-side encryption that will be applied to the restore
    # results.
    encryption: "Encryption" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canned ACL to apply to the restore results.
    canned_acl: typing.Union[str, "ObjectCannedACL"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of grants that control access to the staged results.
    access_control_list: typing.List["Grant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag-set that is applied to the restore results.
    tagging: "Tagging" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of metadata to store with the restore results in S3.
    user_metadata: typing.List["MetadataEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The class of storage used to store the restore results.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SSEKMS(ShapeBase):
    """
    Specifies the use of SSE-KMS to encrypt delievered Inventory reports.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # Specifies the ID of the AWS Key Management Service (KMS) master encryption
    # key to use for encrypting Inventory reports.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SSES3(ShapeBase):
    """
    Specifies the use of SSE-S3 to encrypt delievered Inventory reports.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class SelectObjectContentEventStream(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "records",
                "Records",
                TypeInfo(RecordsEvent),
            ),
            (
                "stats",
                "Stats",
                TypeInfo(StatsEvent),
            ),
            (
                "progress",
                "Progress",
                TypeInfo(ProgressEvent),
            ),
            (
                "cont",
                "Cont",
                TypeInfo(ContinuationEvent),
            ),
            (
                "end",
                "End",
                TypeInfo(EndEvent),
            ),
        ]

    # The Records Event.
    records: "RecordsEvent" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Stats Event.
    stats: "StatsEvent" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Progress Event.
    progress: "ProgressEvent" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Continuation Event.
    cont: "ContinuationEvent" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The End Event.
    end: "EndEvent" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SelectObjectContentOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "payload",
                "Payload",
                TypeInfo(SelectObjectContentEventStream),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    payload: "SelectObjectContentEventStream" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SelectObjectContentRequest(ShapeBase):
    """
    Request to filter the contents of an Amazon S3 object based on a simple
    Structured Query Language (SQL) statement. In the request, along with the SQL
    expression, you must also specify a data serialization format (JSON or CSV) of
    the object. Amazon S3 uses this to parse object data into records, and returns
    only records that match the specified SQL expression. You must also specify the
    data serialization format for the response. For more information, go to
    [S3Select API
    Documentation](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectSELECTContent.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "expression",
                "Expression",
                TypeInfo(str),
            ),
            (
                "expression_type",
                "ExpressionType",
                TypeInfo(typing.Union[str, ExpressionType]),
            ),
            (
                "input_serialization",
                "InputSerialization",
                TypeInfo(InputSerialization),
            ),
            (
                "output_serialization",
                "OutputSerialization",
                TypeInfo(OutputSerialization),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "request_progress",
                "RequestProgress",
                TypeInfo(RequestProgress),
            ),
        ]

    # The S3 Bucket.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Object Key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The expression that is used to query the object.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the provided expression (e.g., SQL).
    expression_type: typing.Union[str, "ExpressionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the format of the data in the object that is being queried.
    input_serialization: "InputSerialization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the format of the data that you want Amazon S3 to return in
    # response.
    output_serialization: "OutputSerialization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The SSE Algorithm used to encrypt the object. For more information, go to [
    # Server-Side Encryption (Using Customer-Provided Encryption
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSE Customer Key. For more information, go to [ Server-Side Encryption
    # (Using Customer-Provided Encryption
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html).
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSE Customer Key MD5. For more information, go to [ Server-Side
    # Encryption (Using Customer-Provided Encryption
    # Keys](http://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html).
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies if periodic request progress information should be enabled.
    request_progress: "RequestProgress" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SelectParameters(ShapeBase):
    """
    Describes the parameters for Select job types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_serialization",
                "InputSerialization",
                TypeInfo(InputSerialization),
            ),
            (
                "expression_type",
                "ExpressionType",
                TypeInfo(typing.Union[str, ExpressionType]),
            ),
            (
                "expression",
                "Expression",
                TypeInfo(str),
            ),
            (
                "output_serialization",
                "OutputSerialization",
                TypeInfo(OutputSerialization),
            ),
        ]

    # Describes the serialization format of the object.
    input_serialization: "InputSerialization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the provided expression (e.g., SQL).
    expression_type: typing.Union[str, "ExpressionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The expression that is used to query the object.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes how the results of the Select job are serialized.
    output_serialization: "OutputSerialization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ServerSideEncryption(str):
    AES256 = "AES256"
    aws_kms = "aws:kms"


@dataclasses.dataclass
class ServerSideEncryptionByDefault(ShapeBase):
    """
    Describes the default server-side encryption to apply to new objects in the
    bucket. If Put Object request does not specify any server-side encryption, this
    default encryption will be applied.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sse_algorithm",
                "SSEAlgorithm",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "kms_master_key_id",
                "KMSMasterKeyID",
                TypeInfo(str),
            ),
        ]

    # Server-side encryption algorithm to use for the default encryption.
    sse_algorithm: typing.Union[str, "ServerSideEncryption"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # KMS master key ID to use for the default encryption. This parameter is
    # allowed if SSEAlgorithm is aws:kms.
    kms_master_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServerSideEncryptionConfiguration(ShapeBase):
    """
    Container for server-side encryption configuration rules. Currently S3 supports
    one rule only.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[ServerSideEncryptionRule]),
            ),
        ]

    # Container for information about a particular server-side encryption
    # configuration rule.
    rules: typing.List["ServerSideEncryptionRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServerSideEncryptionRule(ShapeBase):
    """
    Container for information about a particular server-side encryption
    configuration rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apply_server_side_encryption_by_default",
                "ApplyServerSideEncryptionByDefault",
                TypeInfo(ServerSideEncryptionByDefault),
            ),
        ]

    # Describes the default server-side encryption to apply to new objects in the
    # bucket. If Put Object request does not specify any server-side encryption,
    # this default encryption will be applied.
    apply_server_side_encryption_by_default: "ServerSideEncryptionByDefault" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SourceSelectionCriteria(ShapeBase):
    """
    Container for filters that define which source objects should be replicated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sse_kms_encrypted_objects",
                "SseKmsEncryptedObjects",
                TypeInfo(SseKmsEncryptedObjects),
            ),
        ]

    # Container for filter information of selection of KMS Encrypted S3 objects.
    sse_kms_encrypted_objects: "SseKmsEncryptedObjects" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SseKmsEncryptedObjects(ShapeBase):
    """
    Container for filter information of selection of KMS Encrypted S3 objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, SseKmsEncryptedObjectsStatus]),
            ),
        ]

    # The replication for KMS encrypted S3 objects is disabled if status is not
    # Enabled.
    status: typing.Union[str, "SseKmsEncryptedObjectsStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


class SseKmsEncryptedObjectsStatus(str):
    Enabled = "Enabled"
    Disabled = "Disabled"


@dataclasses.dataclass
class Stats(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bytes_scanned",
                "BytesScanned",
                TypeInfo(int),
            ),
            (
                "bytes_processed",
                "BytesProcessed",
                TypeInfo(int),
            ),
            (
                "bytes_returned",
                "BytesReturned",
                TypeInfo(int),
            ),
        ]

    # Total number of object bytes scanned.
    bytes_scanned: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total number of uncompressed object bytes processed.
    bytes_processed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total number of bytes of records payload data returned.
    bytes_returned: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StatsEvent(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "details",
                "Details",
                TypeInfo(Stats),
            ),
        ]

    # The Stats event details.
    details: "Stats" = dataclasses.field(default=ShapeBase.NOT_SET, )


class StorageClass(str):
    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"


@dataclasses.dataclass
class StorageClassAnalysis(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_export",
                "DataExport",
                TypeInfo(StorageClassAnalysisDataExport),
            ),
        ]

    # A container used to describe how data related to the storage class analysis
    # should be exported.
    data_export: "StorageClassAnalysisDataExport" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StorageClassAnalysisDataExport(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_schema_version",
                "OutputSchemaVersion",
                TypeInfo(typing.Union[str, StorageClassAnalysisSchemaVersion]),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(AnalyticsExportDestination),
            ),
        ]

    # The version of the output schema to use when exporting data. Must be V_1.
    output_schema_version: typing.Union[str, "StorageClassAnalysisSchemaVersion"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The place to store the data for an analysis.
    destination: "AnalyticsExportDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StorageClassAnalysisSchemaVersion(str):
    V_1 = "V_1"


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

    # Name of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tagging(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tag_set",
                "TagSet",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    tag_set: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class TaggingDirective(str):
    COPY = "COPY"
    REPLACE = "REPLACE"


@dataclasses.dataclass
class TargetGrant(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "grantee",
                "Grantee",
                TypeInfo(Grantee),
            ),
            (
                "permission",
                "Permission",
                TypeInfo(typing.Union[str, BucketLogsPermission]),
            ),
        ]

    grantee: "Grantee" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Logging permissions assigned to the Grantee for the bucket.
    permission: typing.Union[str, "BucketLogsPermission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Tier(str):
    Standard = "Standard"
    Bulk = "Bulk"
    Expedited = "Expedited"


@dataclasses.dataclass
class TopicConfiguration(ShapeBase):
    """
    Container for specifying the configuration when you want Amazon S3 to publish
    events to an Amazon Simple Notification Service (Amazon SNS) topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[typing.Union[str, Event]]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(NotificationConfigurationFilter),
            ),
        ]

    # Amazon SNS topic ARN to which Amazon S3 will publish a message when it
    # detects events of specified type.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    events: typing.List[typing.Union[str, "Event"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Container for object key name filtering rules. For information about key
    # name filtering, go to [Configuring Event
    # Notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
    # in the Amazon Simple Storage Service Developer Guide.
    filter: "NotificationConfigurationFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TopicConfigurationDeprecated(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.List[typing.Union[str, Event]]),
            ),
            (
                "event",
                "Event",
                TypeInfo(typing.Union[str, Event]),
            ),
            (
                "topic",
                "Topic",
                TypeInfo(str),
            ),
        ]

    # Optional unique identifier for configurations in a notification
    # configuration. If you don't provide one, Amazon S3 will assign an ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    events: typing.List[typing.Union[str, "Event"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Bucket event for which to send notifications.
    event: typing.Union[str, "Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon SNS topic to which Amazon S3 will publish a message to report the
    # specified events for the bucket.
    topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Transition(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "date",
                "Date",
                TypeInfo(datetime.datetime),
            ),
            (
                "days",
                "Days",
                TypeInfo(int),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, TransitionStorageClass]),
            ),
        ]

    # Indicates at what date the object is to be moved or deleted. Should be in
    # GMT ISO 8601 Format.
    date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the lifetime, in days, of the objects that are subject to the
    # rule. The value must be a non-zero positive integer.
    days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The class of storage used to store the object.
    storage_class: typing.Union[str, "TransitionStorageClass"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


class TransitionStorageClass(str):
    GLACIER = "GLACIER"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"


class Type(str):
    CanonicalUser = "CanonicalUser"
    AmazonCustomerByEmail = "AmazonCustomerByEmail"
    Group = "Group"


@dataclasses.dataclass
class UploadPartCopyOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "copy_source_version_id",
                "CopySourceVersionId",
                TypeInfo(str),
            ),
            (
                "copy_part_result",
                "CopyPartResult",
                TypeInfo(CopyPartResult),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the source object that was copied, if you have enabled
    # versioning on the source bucket.
    copy_source_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    copy_part_result: "CopyPartResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadPartCopyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "copy_source",
                "CopySource",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "part_number",
                "PartNumber",
                TypeInfo(int),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "copy_source_if_match",
                "CopySourceIfMatch",
                TypeInfo(str),
            ),
            (
                "copy_source_if_modified_since",
                "CopySourceIfModifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "copy_source_if_none_match",
                "CopySourceIfNoneMatch",
                TypeInfo(str),
            ),
            (
                "copy_source_if_unmodified_since",
                "CopySourceIfUnmodifiedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "copy_source_range",
                "CopySourceRange",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_algorithm",
                "CopySourceSSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key",
                "CopySourceSSECustomerKey",
                TypeInfo(str),
            ),
            (
                "copy_source_sse_customer_key_md5",
                "CopySourceSSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the source bucket and key name of the source object, separated
    # by a slash (/). Must be URL-encoded.
    copy_source: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Part number of part being copied. This is a positive integer between 1 and
    # 10,000.
    part_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose part is being copied.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Copies the object if its entity tag (ETag) matches the specified tag.
    copy_source_if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Copies the object if it has been modified since the specified time.
    copy_source_if_modified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Copies the object if its entity tag (ETag) is different than the specified
    # ETag.
    copy_source_if_none_match: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Copies the object if it hasn't been modified since the specified time.
    copy_source_if_unmodified_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The range of bytes to copy from the source object. The range value must use
    # the form bytes=first-last, where the first and last are the zero-based byte
    # offsets to copy. For example, bytes=0-9 indicates that you want to copy the
    # first ten bytes of the source. You can copy a range only if the source
    # object is greater than 5 GB.
    copy_source_range: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header. This must be the same
    # encryption key specified in the initiate multipart upload request.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the algorithm to use when decrypting the source object (e.g.,
    # AES256).
    copy_source_sse_customer_algorithm: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the customer-provided encryption key for Amazon S3 to use to
    # decrypt the source object. The encryption key provided in this header must
    # be one that was used when the source object was created.
    copy_source_sse_customer_key: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    copy_source_sse_customer_key_md5: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadPartOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "server_side_encryption",
                "ServerSideEncryption",
                TypeInfo(typing.Union[str, ServerSideEncryption]),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "ssekms_key_id",
                "SSEKMSKeyId",
                TypeInfo(str),
            ),
            (
                "request_charged",
                "RequestCharged",
                TypeInfo(typing.Union[str, RequestCharged]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Server-side encryption algorithm used when storing this object in S3
    # (e.g., AES256, aws:kms).
    server_side_encryption: typing.Union[str, "ServerSideEncryption"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Entity tag for the uploaded object.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header confirming the encryption
    # algorithm used.
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If server-side encryption with a customer-provided encryption key was
    # requested, the response will include this header to provide round trip
    # message integrity verification of the customer-provided encryption key.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, specifies the ID of the AWS Key Management Service (KMS) master
    # encryption key that was used for the object.
    ssekms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If present, indicates that the requester was successfully charged for the
    # request.
    request_charged: typing.Union[str, "RequestCharged"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UploadPartRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "part_number",
                "PartNumber",
                TypeInfo(int),
            ),
            (
                "upload_id",
                "UploadId",
                TypeInfo(str),
            ),
            (
                "body",
                "Body",
                TypeInfo(typing.Any),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
            (
                "content_md5",
                "ContentMD5",
                TypeInfo(str),
            ),
            (
                "sse_customer_algorithm",
                "SSECustomerAlgorithm",
                TypeInfo(str),
            ),
            (
                "sse_customer_key",
                "SSECustomerKey",
                TypeInfo(str),
            ),
            (
                "sse_customer_key_md5",
                "SSECustomerKeyMD5",
                TypeInfo(str),
            ),
            (
                "request_payer",
                "RequestPayer",
                TypeInfo(typing.Union[str, RequestPayer]),
            ),
        ]

    # Name of the bucket to which the multipart upload was initiated.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object key for which the multipart upload was initiated.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Part number of part being uploaded. This is a positive integer between 1
    # and 10,000.
    part_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Upload ID identifying the multipart upload whose part is being uploaded.
    upload_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object data.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size of the body in bytes. This parameter is useful when the size of the
    # body cannot be determined automatically.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base64-encoded 128-bit MD5 digest of the part data.
    content_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the algorithm to use to when encrypting the object (e.g.,
    # AES256).
    sse_customer_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the customer-provided encryption key for Amazon S3 to use in
    # encrypting data. This value is used to store the object and then it is
    # discarded; Amazon does not store the encryption key. The key must be
    # appropriate for use with the algorithm specified in the x-amz-server-
    # side​-encryption​-customer-algorithm header. This must be the same
    # encryption key specified in the initiate multipart upload request.
    sse_customer_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the 128-bit MD5 digest of the encryption key according to RFC
    # 1321. Amazon S3 uses this header for a message integrity check to ensure
    # the encryption key was transmitted without error.
    sse_customer_key_md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confirms that the requester knows that she or he will be charged for the
    # request. Bucket owners need not specify this parameter in their requests.
    # Documentation on downloading objects from requester pays buckets can be
    # found at
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
    request_payer: typing.Union[str, "RequestPayer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VersioningConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mfa_delete",
                "MFADelete",
                TypeInfo(typing.Union[str, MFADelete]),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, BucketVersioningStatus]),
            ),
        ]

    # Specifies whether MFA delete is enabled in the bucket versioning
    # configuration. This element is only returned if the bucket has been
    # configured with MFA delete. If the bucket has never been so configured,
    # this element is not returned.
    mfa_delete: typing.Union[str, "MFADelete"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The versioning state of the bucket.
    status: typing.Union[str, "BucketVersioningStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WebsiteConfiguration(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_document",
                "ErrorDocument",
                TypeInfo(ErrorDocument),
            ),
            (
                "index_document",
                "IndexDocument",
                TypeInfo(IndexDocument),
            ),
            (
                "redirect_all_requests_to",
                "RedirectAllRequestsTo",
                TypeInfo(RedirectAllRequestsTo),
            ),
            (
                "routing_rules",
                "RoutingRules",
                TypeInfo(typing.List[RoutingRule]),
            ),
        ]

    error_document: "ErrorDocument" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    index_document: "IndexDocument" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    redirect_all_requests_to: "RedirectAllRequestsTo" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    routing_rules: typing.List["RoutingRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
