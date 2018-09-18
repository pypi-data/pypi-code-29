import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccountLimit(ShapeBase):
    """
    Provides limits of code size and concurrency associated with the current account
    and region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total_code_size",
                "TotalCodeSize",
                TypeInfo(int),
            ),
            (
                "code_size_unzipped",
                "CodeSizeUnzipped",
                TypeInfo(int),
            ),
            (
                "code_size_zipped",
                "CodeSizeZipped",
                TypeInfo(int),
            ),
            (
                "concurrent_executions",
                "ConcurrentExecutions",
                TypeInfo(int),
            ),
            (
                "unreserved_concurrent_executions",
                "UnreservedConcurrentExecutions",
                TypeInfo(int),
            ),
        ]

    # Maximum size, in bytes, of a code package you can upload per region. The
    # default size is 75 GB.
    total_code_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size, in bytes, of code/dependencies that you can zip into a deployment
    # package (uncompressed zip/jar size) for uploading. The default limit is 250
    # MB.
    code_size_unzipped: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size, in bytes, of a single zipped code/dependencies package you can upload
    # for your Lambda function(.zip/.jar file). Try using Amazon S3 for uploading
    # larger files. Default limit is 50 MB.
    code_size_zipped: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of simultaneous executions of your function per region. For more
    # information or to request a limit increase for concurrent executions, see
    # [Lambda Function Concurrent
    # Executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-
    # executions.html). The default limit is 1000.
    concurrent_executions: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of concurrent executions available to functions that do not have
    # concurrency limits set. For more information, see concurrent-executions.
    unreserved_concurrent_executions: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccountUsage(ShapeBase):
    """
    Provides code size usage and function count associated with the current account
    and region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total_code_size",
                "TotalCodeSize",
                TypeInfo(int),
            ),
            (
                "function_count",
                "FunctionCount",
                TypeInfo(int),
            ),
        ]

    # Total size, in bytes, of the account's deployment packages per region.
    total_code_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of your account's existing functions per region.
    function_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddPermissionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "statement_id",
                "StatementId",
                TypeInfo(str),
            ),
            (
                "action",
                "Action",
                TypeInfo(str),
            ),
            (
                "principal",
                "Principal",
                TypeInfo(str),
            ),
            (
                "source_arn",
                "SourceArn",
                TypeInfo(str),
            ),
            (
                "source_account",
                "SourceAccount",
                TypeInfo(str),
            ),
            (
                "event_source_token",
                "EventSourceToken",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    # Name of the Lambda function whose resource policy you are updating by
    # adding a new permission.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique statement identifier.
    statement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Lambda action you want to allow in this statement. Each Lambda
    # action is a string starting with `lambda:` followed by the API name . For
    # example, `lambda:CreateFunction`. You can use wildcard (`lambda:*`) to
    # grant permission for all AWS Lambda actions.
    action: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal who is getting this permission. It can be Amazon S3 service
    # Principal (`s3.amazonaws.com`) if you want Amazon S3 to invoke the
    # function, an AWS account ID if you are granting cross-account permission,
    # or any valid AWS service principal such as `sns.amazonaws.com`. For
    # example, you might want to allow a custom application in another AWS
    # account to push events to AWS Lambda by invoking your function.
    principal: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is optional; however, when granting permission to invoke your
    # function, you should specify this field with the Amazon Resource Name (ARN)
    # as its value. This ensures that only events generated from the specified
    # source can invoke the function.

    # If you add a permission without providing the source ARN, any AWS account
    # that creates a mapping to your function ARN can send events to invoke your
    # Lambda function.
    source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used for S3 and SES. The AWS account ID (without a
    # hyphen) of the source owner. For example, if the `SourceArn` identifies a
    # bucket, then this is the bucket owner's account ID. You can use this
    # additional condition to ensure the bucket you specify is owned by a
    # specific account (it is possible the bucket owner deleted the bucket and
    # some other AWS account created the bucket). You can also use this condition
    # to specify all sources (that is, you don't specify the `SourceArn`) owned
    # by a specific account.
    source_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique token that must be supplied by the principal invoking the
    # function. This is currently only used for Alexa Smart Home functions.
    event_source_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this optional query parameter to describe a qualified ARN using
    # a function version or an alias name. The permission will then apply to the
    # specific qualified ARN. For example, if you specify function version 2 as
    # the qualifier, then permission applies only when request is made using
    # qualified function ARN:

    # `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

    # If you specify an alias name, for example `PROD`, then the permission is
    # valid only for requests made using the alias ARN:

    # `arn:aws:lambda:aws-region:acct-id:function:function-name:PROD`

    # If the qualifier is not specified, the permission is valid only when
    # requests is made using unqualified function ARN.

    # `arn:aws:lambda:aws-region:acct-id:function:function-name`
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional value you can use to ensure you are updating the latest update
    # of the function version or alias. If the `RevisionID` you pass doesn't
    # match the latest `RevisionId` of the function or alias, it will fail with
    # an error message, advising you to retrieve the latest function version or
    # alias `RevisionID` using either or .
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddPermissionResponse(OutputShapeBase):
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
                "statement",
                "Statement",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The permission statement you specified in the request. The response returns
    # the same as a string using a backslash ("\") as an escape character in the
    # JSON.
    statement: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AliasConfiguration(OutputShapeBase):
    """
    Provides configuration information about a Lambda function version alias.
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
                "alias_arn",
                "AliasArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "function_version",
                "FunctionVersion",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "routing_config",
                "RoutingConfig",
                TypeInfo(AliasRoutingConfiguration),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lambda function ARN that is qualified using the alias name as the suffix.
    # For example, if you create an alias called `BETA` that points to a
    # helloworld function version, the ARN is `arn:aws:lambda:aws-regions:acct-
    # id:function:helloworld:BETA`.
    alias_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Alias name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Function version to which the alias points.
    function_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Alias description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies an additional function versions the alias points to, allowing you
    # to dictate what percentage of traffic will invoke each version. For more
    # information, see lambda-traffic-shifting-using-aliases.
    routing_config: "AliasRoutingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the latest updated revision of the function or alias.
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AliasRoutingConfiguration(ShapeBase):
    """
    The parent object that implements what percentage of traffic will invoke each
    function version. For more information, see lambda-traffic-shifting-using-
    aliases.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "additional_version_weights",
                "AdditionalVersionWeights",
                TypeInfo(typing.Dict[str, float]),
            ),
        ]

    # Set this value to dictate what percentage of traffic will invoke the
    # updated function version. If set to an empty string, 100 percent of traffic
    # will invoke `function-version`. For more information, see lambda-traffic-
    # shifting-using-aliases.
    additional_version_weights: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Blob(botocore.response.StreamingBody):
    pass


class BlobStream(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CodeStorageExceededException(ShapeBase):
    """
    You have exceeded your maximum total code size per account.
    [Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Concurrency(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "reserved_concurrent_executions",
                "ReservedConcurrentExecutions",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of concurrent executions reserved for this function. For more
    # information, see concurrent-executions.
    reserved_concurrent_executions: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "function_version",
                "FunctionVersion",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "routing_config",
                "RoutingConfig",
                TypeInfo(AliasRoutingConfiguration),
            ),
        ]

    # Name of the Lambda function for which you want to create an alias. Note
    # that the length constraint applies only to the ARN. If you specify only the
    # function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name for the alias you are creating.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lambda function version for which you are creating the alias.
    function_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies an additional version your alias can point to, allowing you to
    # dictate what percentage of traffic will invoke each version. For more
    # information, see lambda-traffic-shifting-using-aliases.
    routing_config: "AliasRoutingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateEventSourceMappingRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_source_arn",
                "EventSourceArn",
                TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "batch_size",
                "BatchSize",
                TypeInfo(int),
            ),
            (
                "starting_position",
                "StartingPosition",
                TypeInfo(typing.Union[str, EventSourcePosition]),
            ),
            (
                "starting_position_timestamp",
                "StartingPositionTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The Amazon Resource Name (ARN) of the event source. Any record added to
    # this source could cause AWS Lambda to invoke your Lambda function, it
    # depends on the `BatchSize`. AWS Lambda POSTs the event's records to your
    # Lambda function as JSON.
    event_source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Lambda function to invoke when AWS Lambda detects an event on the
    # stream.

    # You can specify the function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`).

    # If you are using versioning, you can also provide a qualified function ARN
    # (ARN that is qualified with function version or alias name as suffix). For
    # more information about versioning, see [AWS Lambda Function Versioning and
    # Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-
    # aliases.html)

    # AWS Lambda also allows you to specify only the function name with the
    # account ID qualifier (for example, `account-id:Thumbnail`).

    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether AWS Lambda should begin polling the event source. By
    # default, `Enabled` is true.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The largest number of records that AWS Lambda will retrieve from your event
    # source at the time of invoking your function. Your function receives an
    # event with all the retrieved records. The default for Amazon Kinesis and
    # Amazon DynamoDB is 100 records. For SQS, the default is 1.
    batch_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The position in the DynamoDB or Kinesis stream where AWS Lambda should
    # start reading. For more information, see
    # [GetShardIterator](http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-
    # GetShardIterator-request-ShardIteratorType) in the _Amazon Kinesis API
    # Reference Guide_ or
    # [GetShardIterator](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html)
    # in the _Amazon DynamoDB API Reference Guide_. The `AT_TIMESTAMP` value is
    # supported only for [Kinesis
    # streams](http://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-
    # streams.html).
    starting_position: typing.Union[str, "EventSourcePosition"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The timestamp of the data record from which to start reading. Used with
    # [shard iterator
    # type](http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-
    # GetShardIterator-request-ShardIteratorType) AT_TIMESTAMP. If a record with
    # this exact timestamp does not exist, the iterator returned is for the next
    # (later) record. If the timestamp is older than the current trim horizon,
    # the iterator returned is for the oldest untrimmed data record
    # (TRIM_HORIZON). Valid only for [Kinesis
    # streams](http://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-
    # streams.html).
    starting_position_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFunctionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "runtime",
                "Runtime",
                TypeInfo(typing.Union[str, Runtime]),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "handler",
                "Handler",
                TypeInfo(str),
            ),
            (
                "code",
                "Code",
                TypeInfo(FunctionCode),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "memory_size",
                "MemorySize",
                TypeInfo(int),
            ),
            (
                "publish",
                "Publish",
                TypeInfo(bool),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "dead_letter_config",
                "DeadLetterConfig",
                TypeInfo(DeadLetterConfig),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(Environment),
            ),
            (
                "kms_key_arn",
                "KMSKeyArn",
                TypeInfo(str),
            ),
            (
                "tracing_config",
                "TracingConfig",
                TypeInfo(TracingConfig),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name you want to assign to the function you are uploading. The function
    # names appear in the console and are returned in the ListFunctions API.
    # Function names are used to specify functions to other AWS Lambda API
    # operations, such as Invoke. Note that the length constraint applies only to
    # the ARN. If you specify only the function name, it is limited to 64
    # characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The runtime environment for the Lambda function you are uploading.

    # To use the Python runtime v3.6, set the value to "python3.6". To use the
    # Python runtime v2.7, set the value to "python2.7". To use the Node.js
    # runtime v6.10, set the value to "nodejs6.10". To use the Node.js runtime
    # v4.3, set the value to "nodejs4.3". To use the .NET Core runtime v1.0, set
    # the value to "dotnetcore1.0". To use the .NET Core runtime v2.0, set the
    # value to "dotnetcore2.0".

    # Node v0.10.42 is currently marked as deprecated. You must migrate existing
    # functions to the newer Node.js runtime versions available on AWS Lambda
    # (nodejs4.3 or nodejs6.10) as soon as possible. Failure to do so will result
    # in an invalid parameter error being returned. Note that you will have to
    # follow this procedure for each region that contains functions written in
    # the Node v0.10.42 runtime.
    runtime: typing.Union[str, "Runtime"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it
    # executes your function to access any other Amazon Web Services (AWS)
    # resources. For more information, see [AWS Lambda: How it
    # Works](http://docs.aws.amazon.com/lambda/latest/dg/lambda-
    # introduction.html).
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function within your code that Lambda calls to begin execution. For
    # Node.js, it is the _module-name_. _export_ value in your function. For
    # Java, it can be `package.class-name::handler` or `package.class-name`. For
    # more information, see [Lambda Function Handler
    # (Java)](http://docs.aws.amazon.com/lambda/latest/dg/java-programming-model-
    # handler-types.html).
    handler: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code for the Lambda function.
    code: "FunctionCode" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short, user-defined function description. Lambda does not use this value.
    # Assign a meaningful description as you see fit.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function execution time at which Lambda should terminate the function.
    # Because the execution time has cost implications, we recommend you set this
    # value based on your expected execution time. The default is 3 seconds.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of memory, in MB, your Lambda function is given. Lambda uses
    # this memory size to infer the amount of CPU and memory allocated to your
    # function. Your function use-case determines your CPU and memory
    # requirements. For example, a database operation might need less memory
    # compared to an image processing function. The default value is 128 MB. The
    # value must be a multiple of 64 MB.
    memory_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This boolean parameter can be used to request AWS Lambda to create the
    # Lambda function and publish a version as an atomic operation.
    publish: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If your Lambda function accesses resources in a VPC, you provide this
    # parameter identifying the list of security group IDs and subnet IDs. These
    # must belong to the same VPC. You must provide at least one security group
    # and one subnet ID.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent object that contains the target ARN (Amazon Resource Name) of an
    # Amazon SQS queue or Amazon SNS topic. For more information, see dlq.
    dead_letter_config: "DeadLetterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parent object that contains your environment's configuration settings.
    environment: "Environment" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the KMS key used to encrypt your
    # function's environment variables. If not provided, AWS Lambda will use a
    # default service key.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent object that contains your function's tracing settings.
    tracing_config: "TracingConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags (key-value pairs) assigned to the new function. For more
    # information, see [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeadLetterConfig(ShapeBase):
    """
    The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic you
    specify as your Dead Letter Queue (DLQ). For more information, see dlq.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_arn",
                "TargetArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic
    # you specify as your Dead Letter Queue (DLQ). dlq. For more information, see
    # dlq.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Lambda function name for which the alias is created. Deleting an alias
    # does not delete the function version to which it is pointing. Note that the
    # length constraint applies only to the ARN. If you specify only the function
    # name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the alias to delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEventSourceMappingRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uuid",
                "UUID",
                TypeInfo(str),
            ),
        ]

    # The event source mapping ID.
    uuid: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFunctionConcurrencyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
        ]

    # The name of the function you are removing concurrent execution limits from.
    # For more information, see concurrent-executions.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFunctionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
        ]

    # The Lambda function to delete.

    # You can specify the function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). If you are using
    # versioning, you can also provide a qualified function ARN (ARN that is
    # qualified with function version or alias name as suffix). AWS Lambda also
    # allows you to specify only the function name with the account ID qualifier
    # (for example, `account-id:Thumbnail`). Note that the length constraint
    # applies only to the ARN. If you specify only the function name, it is
    # limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Using this optional parameter you can specify a function version (but not
    # the `$LATEST` version) to direct AWS Lambda to delete a specific function
    # version. If the function version has one or more aliases pointing to it,
    # you will get an error because you cannot have aliases pointing to it. You
    # can delete any function version but not the `$LATEST`, that is, you cannot
    # specify `$LATEST` as the value of this parameter. The `$LATEST` version can
    # be deleted only when you want to delete all the function versions and
    # aliases.

    # You can only specify a function version, not an alias name, using this
    # parameter. You cannot delete a function version using its alias.

    # If you don't specify this parameter, AWS Lambda will delete the function,
    # including all of its versions and aliases.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2AccessDeniedException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2ThrottledException(ShapeBase):
    """
    AWS Lambda was throttled by Amazon EC2 during Lambda function initialization
    using the execution role provided for the Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2UnexpectedException(ShapeBase):
    """
    AWS Lambda received an unexpected EC2 client exception while setting up for the
    Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "ec2_error_code",
                "EC2ErrorCode",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    ec2_error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ENILimitReachedException(ShapeBase):
    """
    AWS Lambda was not able to create an Elastic Network Interface (ENI) in the VPC,
    specified as part of Lambda function configuration, because the limit for
    network interfaces has been reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Environment(ShapeBase):
    """
    The parent object that contains your environment's configuration settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variables",
                "Variables",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The key-value pairs that represent your environment's configuration
    # settings.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnvironmentError(ShapeBase):
    """
    The parent object that contains error information associated with your
    configuration settings.
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

    # The error code returned by the environment error object.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message returned by the environment error object.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnvironmentResponse(ShapeBase):
    """
    The parent object returned that contains your environment's configuration
    settings or any error information associated with your configuration settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variables",
                "Variables",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "error",
                "Error",
                TypeInfo(EnvironmentError),
            ),
        ]

    # The key-value pairs returned that represent your environment's
    # configuration settings or error information.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parent object that contains error information associated with your
    # configuration settings.
    error: "EnvironmentError" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventSourceMappingConfiguration(OutputShapeBase):
    """
    Describes mapping between an Amazon Kinesis or DynamoDB stream or an Amazon SQS
    queue and a Lambda function.
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
                "uuid",
                "UUID",
                TypeInfo(str),
            ),
            (
                "batch_size",
                "BatchSize",
                TypeInfo(int),
            ),
            (
                "event_source_arn",
                "EventSourceArn",
                TypeInfo(str),
            ),
            (
                "function_arn",
                "FunctionArn",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_processing_result",
                "LastProcessingResult",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "state_transition_reason",
                "StateTransitionReason",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Lambda assigned opaque identifier for the mapping.
    uuid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The largest number of records that AWS Lambda will retrieve from your event
    # source at the time of invoking your function. Your function receives an
    # event with all the retrieved records.
    batch_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon Kinesis or DynamoDB stream or
    # the SQS queue that is the source of events.
    event_source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Lambda function to invoke when AWS Lambda detects an event on the poll-
    # based source.
    function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTC time string indicating the last time the event mapping was updated.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The result of the last AWS Lambda invocation of your Lambda function.
    last_processing_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the event source mapping. It can be `Creating`, `Enabled`,
    # `Disabled`, `Enabling`, `Disabling`, `Updating`, or `Deleting`.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason the event source mapping is in its current state. It is either
    # user-requested or an AWS Lambda-initiated state transition.
    state_transition_reason: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EventSourcePosition(str):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


@dataclasses.dataclass
class FunctionCode(ShapeBase):
    """
    The code for the Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "zip_file",
                "ZipFile",
                TypeInfo(typing.Any),
            ),
            (
                "s3_bucket",
                "S3Bucket",
                TypeInfo(str),
            ),
            (
                "s3_key",
                "S3Key",
                TypeInfo(str),
            ),
            (
                "s3_object_version",
                "S3ObjectVersion",
                TypeInfo(str),
            ),
        ]

    # The contents of your zip file containing your deployment package. If you
    # are using the web API directly, the contents of the zip file must be
    # base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or
    # CLI will do the encoding for you. For more information about creating a
    # .zip file, see [Execution
    # Permissions](http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-
    # model.html#lambda-intro-execution-role.html) in the **AWS Lambda Developer
    # Guide**.
    zip_file: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon S3 bucket name where the .zip file containing your deployment
    # package is stored. This bucket must reside in the same AWS region where you
    # are creating the Lambda function.
    s3_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 object (the deployment package) key name you want to upload.
    s3_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 object (the deployment package) version you want to upload.
    s3_object_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FunctionCodeLocation(ShapeBase):
    """
    The object for the Lambda function location.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "repository_type",
                "RepositoryType",
                TypeInfo(str),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
        ]

    # The repository from which you can download the function.
    repository_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The presigned URL you can use to download the function's .zip file that you
    # previously uploaded. The URL is valid for up to 10 minutes.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FunctionConfiguration(OutputShapeBase):
    """
    A complex type that describes function metadata.
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
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "function_arn",
                "FunctionArn",
                TypeInfo(str),
            ),
            (
                "runtime",
                "Runtime",
                TypeInfo(typing.Union[str, Runtime]),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "handler",
                "Handler",
                TypeInfo(str),
            ),
            (
                "code_size",
                "CodeSize",
                TypeInfo(int),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "memory_size",
                "MemorySize",
                TypeInfo(int),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(str),
            ),
            (
                "code_sha256",
                "CodeSha256",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfigResponse),
            ),
            (
                "dead_letter_config",
                "DeadLetterConfig",
                TypeInfo(DeadLetterConfig),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(EnvironmentResponse),
            ),
            (
                "kms_key_arn",
                "KMSKeyArn",
                TypeInfo(str),
            ),
            (
                "tracing_config",
                "TracingConfig",
                TypeInfo(TracingConfigResponse),
            ),
            (
                "master_arn",
                "MasterArn",
                TypeInfo(str),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the function. Note that the length constraint applies only to
    # the ARN. If you specify only the function name, it is limited to 64
    # characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) assigned to the function.
    function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The runtime environment for the Lambda function.
    runtime: typing.Union[str, "Runtime"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it
    # executes your function to access any other Amazon Web Services (AWS)
    # resources.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function Lambda calls to begin executing your function.
    handler: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size, in bytes, of the function .zip file you uploaded.
    code_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-provided description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function execution time at which Lambda should terminate the function.
    # Because the execution time has cost implications, we recommend you set this
    # value based on your expected execution time. The default is 3 seconds.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The memory size, in MB, you configured for the function. Must be a multiple
    # of 64 MB.
    memory_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp of the last time you updated the function. The time stamp is
    # conveyed as a string complying with ISO-8601 in this way YYYY-MM-
    # DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00). For more information, see
    # [Date and Time Formats](https://www.w3.org/TR/NOTE-datetime).
    last_modified: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # It is the SHA256 hash of your function deployment package.
    code_sha256: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the Lambda function.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # VPC configuration associated with your Lambda function.
    vpc_config: "VpcConfigResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parent object that contains the target ARN (Amazon Resource Name) of an
    # Amazon SQS queue or Amazon SNS topic. For more information, see dlq.
    dead_letter_config: "DeadLetterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parent object that contains your environment's configuration settings.
    environment: "EnvironmentResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the KMS key used to encrypt your
    # function's environment variables. If empty, it means you are using the AWS
    # Lambda default service key.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent object that contains your function's tracing settings.
    tracing_config: "TracingConfigResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns the ARN (Amazon Resource Name) of the master function.
    master_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the latest updated revision of the function or alias.
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FunctionVersion(str):
    ALL = "ALL"


@dataclasses.dataclass
class GetAccountSettingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetAccountSettingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "account_limit",
                "AccountLimit",
                TypeInfo(AccountLimit),
            ),
            (
                "account_usage",
                "AccountUsage",
                TypeInfo(AccountUsage),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides limits of code size and concurrency associated with the current
    # account and region.
    account_limit: "AccountLimit" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides code size usage and function count associated with the current
    # account and region.
    account_usage: "AccountUsage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Function name for which the alias is created. An alias is a subresource
    # that exists only in the context of an existing Lambda function so you must
    # specify the function name. Note that the length constraint applies only to
    # the ARN. If you specify only the function name, it is limited to 64
    # characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the alias for which you want to retrieve information.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEventSourceMappingRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uuid",
                "UUID",
                TypeInfo(str),
            ),
        ]

    # The AWS Lambda assigned ID of the event source mapping.
    uuid: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFunctionConfigurationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
        ]

    # The name of the Lambda function for which you want to retrieve the
    # configuration information.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Using this optional parameter you can specify a function version or an
    # alias name. If you specify function version, the API uses qualified
    # function ARN and returns information about the specific function version.
    # If you specify an alias name, the API uses the alias ARN and returns
    # information about the function version to which the alias points.

    # If you don't specify this parameter, the API uses unqualified function ARN,
    # and returns information about the `$LATEST` function version.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFunctionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
        ]

    # The Lambda function name.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this optional parameter to specify a function version or an alias name.
    # If you specify function version, the API uses qualified function ARN for
    # the request and returns information about the specific Lambda function
    # version. If you specify an alias name, the API uses the alias ARN and
    # returns information about the function version to which the alias points.
    # If you don't provide this parameter, the API uses unqualified function ARN
    # and returns information about the `$LATEST` version of the Lambda function.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFunctionResponse(OutputShapeBase):
    """
    This response contains the object for the Lambda function location (see
    FunctionCodeLocation.
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
                "configuration",
                "Configuration",
                TypeInfo(FunctionConfiguration),
            ),
            (
                "code",
                "Code",
                TypeInfo(FunctionCodeLocation),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "concurrency",
                "Concurrency",
                TypeInfo(Concurrency),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that describes function metadata.
    configuration: "FunctionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The object for the Lambda function location.
    code: "FunctionCodeLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns the list of tags associated with the function. For more
    # information, see [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The concurrent execution limit set for this function. For more information,
    # see concurrent-executions.
    concurrency: "Concurrency" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
        ]

    # Function name whose resource policy you want to retrieve.

    # You can specify the function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). If you are using
    # versioning, you can also provide a qualified function ARN (ARN that is
    # qualified with function version or alias name as suffix). AWS Lambda also
    # allows you to specify only the function name with the account ID qualifier
    # (for example, `account-id:Thumbnail`). Note that the length constraint
    # applies only to the ARN. If you specify only the function name, it is
    # limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can specify this optional query parameter to specify a function version
    # or an alias name in which case this API will return all permissions
    # associated with the specific qualified ARN. If you don't provide this
    # parameter, the API will return permissions that apply to the unqualified
    # function ARN.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPolicyResponse(OutputShapeBase):
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
                "policy",
                "Policy",
                TypeInfo(str),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource policy associated with the specified function. The response
    # returns the same as a string using a backslash ("\") as an escape character
    # in the JSON.
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the latest updated revision of the function or alias.
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterValueException(ShapeBase):
    """
    One of the parameters in the request is invalid. For example, if you provided an
    IAM role for AWS Lambda to assume in the `CreateFunction` or the
    `UpdateFunctionConfiguration` API, that AWS Lambda is unable to assume you will
    get this exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestContentException(ShapeBase):
    """
    The request body could not be parsed as JSON.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRuntimeException(ShapeBase):
    """
    The runtime or runtime version specified is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSecurityGroupIDException(ShapeBase):
    """
    The Security Group ID provided in the Lambda function VPC configuration is
    invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSubnetIDException(ShapeBase):
    """
    The Subnet ID provided in the Lambda function VPC configuration is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidZipFileException(ShapeBase):
    """
    AWS Lambda could not unzip the function zip file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvocationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "invocation_type",
                "InvocationType",
                TypeInfo(typing.Union[str, InvocationType]),
            ),
            (
                "log_type",
                "LogType",
                TypeInfo(typing.Union[str, LogType]),
            ),
            (
                "client_context",
                "ClientContext",
                TypeInfo(str),
            ),
            (
                "payload",
                "Payload",
                TypeInfo(typing.Any),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
        ]

    # The Lambda function name.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # By default, the `Invoke` API assumes `RequestResponse` invocation type. You
    # can optionally request asynchronous execution by specifying `Event` as the
    # `InvocationType`. You can also use this parameter to request AWS Lambda to
    # not execute the function but do some verification, such as if the caller is
    # authorized to invoke the function and if the inputs are valid. You request
    # this by specifying `DryRun` as the `InvocationType`. This is useful in a
    # cross-account scenario when you want to verify access to a function without
    # running it.
    invocation_type: typing.Union[str, "InvocationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can set this optional parameter to `Tail` in the request only if you
    # specify the `InvocationType` parameter with value `RequestResponse`. In
    # this case, AWS Lambda returns the base64-encoded last 4 KB of log data
    # produced by your Lambda function in the `x-amz-log-result` header.
    log_type: typing.Union[str, "LogType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Using the `ClientContext` you can pass client-specific information to the
    # Lambda function you are invoking. You can then process the client
    # information in your Lambda function as you choose through the context
    # variable. For an example of a `ClientContext` JSON, see
    # [PutEvents](http://docs.aws.amazon.com/mobileanalytics/latest/ug/PutEvents.html)
    # in the _Amazon Mobile Analytics API Reference and User Guide_.

    # The ClientContext JSON must be base64-encoded and has a maximum size of
    # 3583 bytes.
    client_context: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JSON that you want to provide to your Lambda function as input.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this optional parameter to specify a Lambda function version or
    # alias name. If you specify a function version, the API uses the qualified
    # function ARN to invoke a specific Lambda function. If you specify an alias
    # name, the API uses the alias ARN to invoke the Lambda function version to
    # which the alias points.

    # If you don't provide this parameter, then the API uses unqualified function
    # ARN which results in invocation of the `$LATEST` version.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvocationResponse(OutputShapeBase):
    """
    Upon success, returns an empty response. Otherwise, throws an exception.
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
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
            (
                "function_error",
                "FunctionError",
                TypeInfo(str),
            ),
            (
                "log_result",
                "LogResult",
                TypeInfo(str),
            ),
            (
                "payload",
                "Payload",
                TypeInfo(typing.Any),
            ),
            (
                "executed_version",
                "ExecutedVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTTP status code will be in the 200 range for successful request. For
    # the `RequestResponse` invocation type this status code will be 200. For the
    # `Event` invocation type this status code will be 202. For the `DryRun`
    # invocation type the status code will be 204.
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether an error occurred while executing the Lambda function. If
    # an error occurred this field will have one of two values; `Handled` or
    # `Unhandled`. `Handled` errors are errors that are reported by the function
    # while the `Unhandled` errors are those detected and reported by AWS Lambda.
    # Unhandled errors include out of memory errors and function timeouts. For
    # information about how to report an `Handled` error, see [Programming
    # Model](http://docs.aws.amazon.com/lambda/latest/dg/programming-model.html).
    function_error: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # It is the base64-encoded logs for the Lambda function invocation. This is
    # present only if the invocation type is `RequestResponse` and the logs were
    # requested.
    log_result: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # It is the JSON representation of the object returned by the Lambda
    # function. This is present only if the invocation type is `RequestResponse`.

    # In the event of a function error this field contains a message describing
    # the error. For the `Handled` errors the Lambda function will report this
    # message. For `Unhandled` errors AWS Lambda reports the message.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function version that has been executed. This value is returned only if
    # the invocation type is `RequestResponse`. For more information, see lambda-
    # traffic-shifting-using-aliases.
    executed_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InvocationType(str):
    Event = "Event"
    RequestResponse = "RequestResponse"
    DryRun = "DryRun"


@dataclasses.dataclass
class InvokeAsyncRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "invoke_args",
                "InvokeArgs",
                TypeInfo(typing.Any),
            ),
        ]

    # The Lambda function name. Note that the length constraint applies only to
    # the ARN. If you specify only the function name, it is limited to 64
    # characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JSON that you want to provide to your Lambda function as input.
    invoke_args: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvokeAsyncResponse(OutputShapeBase):
    """
    Upon success, it returns empty response. Otherwise, throws an exception.
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
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # It will be 202 upon success.
    status: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KMSAccessDeniedException(ShapeBase):
    """
    Lambda was unable to decrypt the environment variables because KMS access was
    denied. Check the Lambda function's KMS permissions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KMSDisabledException(ShapeBase):
    """
    Lambda was unable to decrypt the environment variables because the KMS key used
    is disabled. Check the Lambda function's KMS key settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KMSInvalidStateException(ShapeBase):
    """
    Lambda was unable to decrypt the environment variables because the KMS key used
    is in an invalid state for Decrypt. Check the function's KMS key settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KMSNotFoundException(ShapeBase):
    """
    Lambda was unable to decrypt the environment variables because the KMS key was
    not found. Check the function's KMS key settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAliasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "function_version",
                "FunctionVersion",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # Lambda function name for which the alias is created. Note that the length
    # constraint applies only to the ARN. If you specify only the function name,
    # it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specify this optional parameter, the API returns only the aliases
    # that are pointing to the specific Lambda function version, otherwise the
    # API returns all of the aliases created for the Lambda function.
    function_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional string. An opaque pagination token returned from a previous
    # `ListAliases` operation. If present, indicates where to continue the
    # listing.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional integer. Specifies the maximum number of aliases to return in
    # response. This parameter value must be greater than 0.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAliasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(typing.List[AliasConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string, present if there are more aliases.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of aliases.
    aliases: typing.List["AliasConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ListAliasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListEventSourceMappingsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_source_arn",
                "EventSourceArn",
                TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon Kinesis or DynamoDB stream, or
    # an SQS queue. (This parameter is optional.)
    event_source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Lambda function.

    # You can specify the function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). If you are using
    # versioning, you can also provide a qualified function ARN (ARN that is
    # qualified with function version or alias name as suffix). AWS Lambda also
    # allows you to specify only the function name with the account ID qualifier
    # (for example, `account-id:Thumbnail`). Note that the length constraint
    # applies only to the ARN. If you specify only the function name, it is
    # limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional string. An opaque pagination token returned from a previous
    # `ListEventSourceMappings` operation. If present, specifies to continue the
    # list from where the returning call left off.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional integer. Specifies the maximum number of event sources to return
    # in response. This value must be greater than 0.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEventSourceMappingsResponse(OutputShapeBase):
    """
    Contains a list of event sources (see EventSourceMappingConfiguration)
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
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "event_source_mappings",
                "EventSourceMappings",
                TypeInfo(typing.List[EventSourceMappingConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string, present if there are more event source mappings.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `EventSourceMappingConfiguration` objects.
    event_source_mappings: typing.List["EventSourceMappingConfiguration"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    def paginate(
        self,
    ) -> typing.Generator["ListEventSourceMappingsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFunctionsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "master_region",
                "MasterRegion",
                TypeInfo(str),
            ),
            (
                "function_version",
                "FunctionVersion",
                TypeInfo(typing.Union[str, FunctionVersion]),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # Optional string. If not specified, will return only regular function
    # versions (i.e., non-replicated versions).

    # Valid values are:

    # The region from which the functions are replicated. For example, if you
    # specify `us-east-1`, only functions replicated from that region will be
    # returned.

    # `ALL`: Will return all functions from any region. If specified, you also
    # must specify a valid FunctionVersion parameter.
    master_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional string. If not specified, only the unqualified functions ARNs
    # (Amazon Resource Names) will be returned.

    # Valid value:

    # `ALL`: Will return all versions, including `$LATEST` which will have fully
    # qualified ARNs (Amazon Resource Names).
    function_version: typing.Union[str, "FunctionVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional string. An opaque pagination token returned from a previous
    # `ListFunctions` operation. If present, indicates where to continue the
    # listing.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional integer. Specifies the maximum number of AWS Lambda functions to
    # return in response. This parameter value must be greater than 0.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFunctionsResponse(OutputShapeBase):
    """
    Contains a list of AWS Lambda function configurations (see
    FunctionConfiguration.
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
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "functions",
                "Functions",
                TypeInfo(typing.List[FunctionConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string, present if there are more functions.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Lambda functions.
    functions: typing.List["FunctionConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListFunctionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(str),
            ),
        ]

    # The ARN (Amazon Resource Name) of the function. For more information, see
    # [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(OutputShapeBase):
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
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tags assigned to the function. For more information, see
    # [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVersionsByFunctionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # Function name whose versions to list. You can specify a function name (for
    # example, `Thumbnail`) or you can specify Amazon Resource Name (ARN) of the
    # function (for example, `arn:aws:lambda:us-west-2:account-
    # id:function:ThumbNail`). AWS Lambda also allows you to specify a partial
    # ARN (for example, `account-id:Thumbnail`). Note that the length constraint
    # applies only to the ARN. If you specify only the function name, it is
    # limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional string. An opaque pagination token returned from a previous
    # `ListVersionsByFunction` operation. If present, indicates where to continue
    # the listing.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional integer. Specifies the maximum number of AWS Lambda function
    # versions to return in response. This parameter value must be greater than
    # 0.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVersionsByFunctionResponse(OutputShapeBase):
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
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                TypeInfo(typing.List[FunctionConfiguration]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string, present if there are more function versions.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Lambda function versions.
    versions: typing.List["FunctionConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LogType(str):
    NONE = "None"
    TAIL = "Tail"


@dataclasses.dataclass
class PolicyLengthExceededException(ShapeBase):
    """
    Lambda function access policy is limited to 20 KB.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreconditionFailedException(ShapeBase):
    """
    The RevisionId provided does not match the latest RevisionId for the Lambda
    function or alias. Call the `GetFunction` or the `GetAlias` API to retrieve the
    latest RevisionId for your resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PublishVersionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "code_sha256",
                "CodeSha256",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    # The Lambda function name. You can specify a function name (for example,
    # `Thumbnail`) or you can specify Amazon Resource Name (ARN) of the function
    # (for example, `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`).
    # AWS Lambda also allows you to specify a partial ARN (for example, `account-
    # id:Thumbnail`). Note that the length constraint applies only to the ARN. If
    # you specify only the function name, it is limited to 64 characters in
    # length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SHA256 hash of the deployment package you want to publish. This
    # provides validation on the code you are publishing. If you provide this
    # parameter, the value must match the SHA256 of the $LATEST version for the
    # publication to succeed. You can use the **DryRun** parameter of
    # UpdateFunctionCode to verify the hash value that will be returned before
    # publishing your new version.
    code_sha256: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the version you are publishing. If not provided, AWS
    # Lambda copies the description from the $LATEST version.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional value you can use to ensure you are updating the latest update
    # of the function version or alias. If the `RevisionID` you pass doesn't
    # match the latest `RevisionId` of the function or alias, it will fail with
    # an error message, advising you to retrieve the latest function version or
    # alias `RevisionID` using either or .
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutFunctionConcurrencyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "reserved_concurrent_executions",
                "ReservedConcurrentExecutions",
                TypeInfo(int),
            ),
        ]

    # The name of the function you are setting concurrent execution limits on.
    # For more information, see concurrent-executions.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The concurrent execution limit reserved for this function. For more
    # information, see concurrent-executions.
    reserved_concurrent_executions: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemovePermissionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "statement_id",
                "StatementId",
                TypeInfo(str),
            ),
            (
                "qualifier",
                "Qualifier",
                TypeInfo(str),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    # Lambda function whose resource policy you want to remove a permission from.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Statement ID of the permission to remove.
    statement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can specify this optional parameter to remove permission associated
    # with a specific function version or function alias. If you don't specify
    # this parameter, the API removes permission associated with the unqualified
    # function ARN.
    qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional value you can use to ensure you are updating the latest update
    # of the function version or alias. If the `RevisionID` you pass doesn't
    # match the latest `RevisionId` of the function or alias, it will fail with
    # an error message, advising you to retrieve the latest function version or
    # alias `RevisionID` using either or .
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestTooLargeException(ShapeBase):
    """
    The request payload exceeded the `Invoke` request body JSON input limit. For
    more information, see
    [Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceConflictException(ShapeBase):
    """
    The resource already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The operation conflicts with the resource's availability. For example, you
    attempted to update an EventSoure Mapping in CREATING, or tried to delete a
    EventSoure mapping currently in the UPDATING state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The resource (for example, a Lambda function or access policy statement)
    specified in the request does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Runtime(str):
    nodejs = "nodejs"
    nodejs4_3 = "nodejs4.3"
    nodejs6_10 = "nodejs6.10"
    nodejs8_10 = "nodejs8.10"
    java8 = "java8"
    python2_7 = "python2.7"
    python3_6 = "python3.6"
    dotnetcore1_0 = "dotnetcore1.0"
    dotnetcore2_0 = "dotnetcore2.0"
    dotnetcore2_1 = "dotnetcore2.1"
    nodejs4_3_edge = "nodejs4.3-edge"
    go1_x = "go1.x"


@dataclasses.dataclass
class ServiceException(ShapeBase):
    """
    The AWS Lambda service encountered an internal error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubnetIPAddressLimitReachedException(ShapeBase):
    """
    AWS Lambda was not able to set up VPC access for the Lambda function because one
    or more configured subnets has no available IP addresses.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ARN (Amazon Resource Name) of the Lambda function. For more
    # information, see [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags (key-value pairs) you are assigning to the Lambda
    # function. For more information, see [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ThrottleReason(str):
    ConcurrentInvocationLimitExceeded = "ConcurrentInvocationLimitExceeded"
    FunctionInvocationRateLimitExceeded = "FunctionInvocationRateLimitExceeded"
    ReservedFunctionConcurrentInvocationLimitExceeded = "ReservedFunctionConcurrentInvocationLimitExceeded"
    ReservedFunctionInvocationRateLimitExceeded = "ReservedFunctionInvocationRateLimitExceeded"
    CallerRateLimitExceeded = "CallerRateLimitExceeded"


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "reason",
                "Reason",
                TypeInfo(typing.Union[str, ThrottleReason]),
            ),
        ]

    # The number of seconds the caller should wait before retrying.
    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    reason: typing.Union[str, "ThrottleReason"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TracingConfig(ShapeBase):
    """
    The parent object that contains your function's tracing settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, TracingMode]),
            ),
        ]

    # Can be either PassThrough or Active. If PassThrough, Lambda will only trace
    # the request from an upstream service if it contains a tracing header with
    # "sampled=1". If Active, Lambda will respect any tracing header it receives
    # from an upstream service. If no tracing header is received, Lambda will
    # call X-Ray for a tracing decision.
    mode: typing.Union[str, "TracingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TracingConfigResponse(ShapeBase):
    """
    Parent object of the tracing information associated with your Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, TracingMode]),
            ),
        ]

    # The tracing mode associated with your Lambda function.
    mode: typing.Union[str, "TracingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TracingMode(str):
    Active = "Active"
    PassThrough = "PassThrough"


@dataclasses.dataclass
class UnsupportedMediaTypeException(ShapeBase):
    """
    The content type of the `Invoke` request body is not JSON.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN (Amazon Resource Name) of the function. For more information, see
    # [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tag keys to be deleted from the function. For more information,
    # see [Tagging Lambda
    # Functions](http://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the
    # **AWS Lambda Developer Guide**.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "function_version",
                "FunctionVersion",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "routing_config",
                "RoutingConfig",
                TypeInfo(AliasRoutingConfiguration),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    # The function name for which the alias is created. Note that the length
    # constraint applies only to the ARN. If you specify only the function name,
    # it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Using this parameter you can change the Lambda function version to which
    # the alias points.
    function_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can change the description of the alias using this parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies an additional version your alias can point to, allowing you to
    # dictate what percentage of traffic will invoke each version. For more
    # information, see lambda-traffic-shifting-using-aliases.
    routing_config: "AliasRoutingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional value you can use to ensure you are updating the latest update
    # of the function version or alias. If the `RevisionID` you pass doesn't
    # match the latest `RevisionId` of the function or alias, it will fail with
    # an error message, advising you to retrieve the latest function version or
    # alias `RevisionID` using either or .
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEventSourceMappingRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uuid",
                "UUID",
                TypeInfo(str),
            ),
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "batch_size",
                "BatchSize",
                TypeInfo(int),
            ),
        ]

    # The event source mapping identifier.
    uuid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Lambda function to which you want the stream records sent.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.

    # If you are using versioning, you can also provide a qualified function ARN
    # (ARN that is qualified with function version or alias name as suffix). For
    # more information about versioning, see [AWS Lambda Function Versioning and
    # Aliases](http://docs.aws.amazon.com/lambda/latest/dg/versioning-
    # aliases.html)

    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 character in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether AWS Lambda should actively poll the stream or not. If
    # disabled, AWS Lambda will not poll the stream.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of stream records that can be sent to your Lambda
    # function for a single invocation.
    batch_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFunctionCodeRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "zip_file",
                "ZipFile",
                TypeInfo(typing.Any),
            ),
            (
                "s3_bucket",
                "S3Bucket",
                TypeInfo(str),
            ),
            (
                "s3_key",
                "S3Key",
                TypeInfo(str),
            ),
            (
                "s3_object_version",
                "S3ObjectVersion",
                TypeInfo(str),
            ),
            (
                "publish",
                "Publish",
                TypeInfo(bool),
            ),
            (
                "dry_run",
                "DryRun",
                TypeInfo(bool),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    # The existing Lambda function name whose code you want to replace.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 characters in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The contents of your zip file containing your deployment package. If you
    # are using the web API directly, the contents of the zip file must be
    # base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or
    # CLI will do the encoding for you. For more information about creating a
    # .zip file, see [Execution
    # Permissions](http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-
    # model.html#lambda-intro-execution-role.html).
    zip_file: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon S3 bucket name where the .zip file containing your deployment
    # package is stored. This bucket must reside in the same AWS Region where you
    # are creating the Lambda function.
    s3_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 object (the deployment package) key name you want to upload.
    s3_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 object (the deployment package) version you want to upload.
    s3_object_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This boolean parameter can be used to request AWS Lambda to update the
    # Lambda function and publish a version as an atomic operation.
    publish: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This boolean parameter can be used to test your request to AWS Lambda to
    # update the Lambda function and publish a version as an atomic operation. It
    # will do all necessary computation and validation of your code but will not
    # upload it or a publish a version. Each time this operation is invoked, the
    # `CodeSha256` hash value of the provided code will also be computed and
    # returned in the response.
    dry_run: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional value you can use to ensure you are updating the latest update
    # of the function version or alias. If the `RevisionID` you pass doesn't
    # match the latest `RevisionId` of the function or alias, it will fail with
    # an error message, advising you to retrieve the latest function version or
    # alias `RevisionID` using either or .
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFunctionConfigurationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_name",
                "FunctionName",
                TypeInfo(str),
            ),
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "handler",
                "Handler",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
            (
                "memory_size",
                "MemorySize",
                TypeInfo(int),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(Environment),
            ),
            (
                "runtime",
                "Runtime",
                TypeInfo(typing.Union[str, Runtime]),
            ),
            (
                "dead_letter_config",
                "DeadLetterConfig",
                TypeInfo(DeadLetterConfig),
            ),
            (
                "kms_key_arn",
                "KMSKeyArn",
                TypeInfo(str),
            ),
            (
                "tracing_config",
                "TracingConfig",
                TypeInfo(TracingConfig),
            ),
            (
                "revision_id",
                "RevisionId",
                TypeInfo(str),
            ),
        ]

    # The name of the Lambda function.

    # You can specify a function name (for example, `Thumbnail`) or you can
    # specify Amazon Resource Name (ARN) of the function (for example,
    # `arn:aws:lambda:us-west-2:account-id:function:ThumbNail`). AWS Lambda also
    # allows you to specify a partial ARN (for example, `account-id:Thumbnail`).
    # Note that the length constraint applies only to the ARN. If you specify
    # only the function name, it is limited to 64 character in length.
    function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role that Lambda will assume when
    # it executes your function.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function that Lambda calls to begin executing your function. For
    # Node.js, it is the `module-name.export` value in your function.
    handler: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short user-defined function description. AWS Lambda does not use this
    # value. Assign a meaningful description as you see fit.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The function execution time at which AWS Lambda should terminate the
    # function. Because the execution time has cost implications, we recommend
    # you set this value based on your expected execution time. The default is 3
    # seconds.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of memory, in MB, your Lambda function is given. AWS Lambda uses
    # this memory size to infer the amount of CPU allocated to your function.
    # Your function use-case determines your CPU and memory requirements. For
    # example, a database operation might need less memory compared to an image
    # processing function. The default value is 128 MB. The value must be a
    # multiple of 64 MB.
    memory_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If your Lambda function accesses resources in a VPC, you provide this
    # parameter identifying the list of security group IDs and subnet IDs. These
    # must belong to the same VPC. You must provide at least one security group
    # and one subnet ID.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent object that contains your environment's configuration settings.
    environment: "Environment" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The runtime environment for the Lambda function.

    # To use the Python runtime v3.6, set the value to "python3.6". To use the
    # Python runtime v2.7, set the value to "python2.7". To use the Node.js
    # runtime v6.10, set the value to "nodejs6.10". To use the Node.js runtime
    # v4.3, set the value to "nodejs4.3". To use the .NET Core runtime v1.0, set
    # the value to "dotnetcore1.0". To use the .NET Core runtime v2.0, set the
    # value to "dotnetcore2.0".

    # Node v0.10.42 is currently marked as deprecated. You must migrate existing
    # functions to the newer Node.js runtime versions available on AWS Lambda
    # (nodejs4.3 or nodejs6.10) as soon as possible. Failure to do so will result
    # in an invalid parameter error being returned. Note that you will have to
    # follow this procedure for each region that contains functions written in
    # the Node v0.10.42 runtime.
    runtime: typing.Union[str, "Runtime"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parent object that contains the target ARN (Amazon Resource Name) of an
    # Amazon SQS queue or Amazon SNS topic. For more information, see dlq.
    dead_letter_config: "DeadLetterConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the KMS key used to encrypt your
    # function's environment variables. If you elect to use the AWS Lambda
    # default service key, pass in an empty string ("") for this parameter.
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent object that contains your function's tracing settings.
    tracing_config: "TracingConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional value you can use to ensure you are updating the latest update
    # of the function version or alias. If the `RevisionID` you pass doesn't
    # match the latest `RevisionId` of the function or alias, it will fail with
    # an error message, advising you to retrieve the latest function version or
    # alias `RevisionID` using either or .
    revision_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VpcConfig(ShapeBase):
    """
    If your Lambda function accesses resources in a VPC, you provide this parameter
    identifying the list of security group IDs and subnet IDs. These must belong to
    the same VPC. You must provide at least one security group and one subnet ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of one or more subnet IDs in your VPC.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of one or more security groups IDs in your VPC.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VpcConfigResponse(ShapeBase):
    """
    VPC configuration associated with your Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
        ]

    # A list of subnet IDs associated with the Lambda function.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security group IDs associated with the Lambda function.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC ID associated with you Lambda function.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
