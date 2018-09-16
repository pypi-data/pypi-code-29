import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AddApplicationCloudWatchLoggingOptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "cloud_watch_logging_option",
                "CloudWatchLoggingOption",
                TypeInfo(CloudWatchLoggingOption),
            ),
        ]

    # The Kinesis Analytics application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the Kinesis Analytics application.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM
    # role ARN. Note: To write application messages to CloudWatch, the IAM role
    # that is used must have the `PutLogEvents` policy action enabled.
    cloud_watch_logging_option: "CloudWatchLoggingOption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddApplicationCloudWatchLoggingOptionResponse(OutputShapeBase):
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
class AddApplicationInputProcessingConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
            (
                "input_processing_configuration",
                "InputProcessingConfiguration",
                TypeInfo(InputProcessingConfiguration),
            ),
        ]

    # Name of the application to which you want to add the input processing
    # configuration.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the application to which you want to add the input processing
    # configuration. You can use the DescribeApplication operation to get the
    # current application version. If the version specified is not the current
    # version, the `ConcurrentModificationException` is returned.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the input configuration to add the input processing configuration
    # to. You can get a list of the input IDs for an application using the
    # DescribeApplication operation.
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The InputProcessingConfiguration to add to the application.
    input_processing_configuration: "InputProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddApplicationInputProcessingConfigurationResponse(OutputShapeBase):
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
class AddApplicationInputRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "input",
                "Input",
                TypeInfo(Input),
            ),
        ]

    # Name of your existing Amazon Kinesis Analytics application to which you
    # want to add the streaming source.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current version of your Amazon Kinesis Analytics application. You can use
    # the DescribeApplication operation to find the current application version.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Input to add.
    input: "Input" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddApplicationInputResponse(OutputShapeBase):
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
class AddApplicationOutputRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "output",
                "Output",
                TypeInfo(Output),
            ),
        ]

    # Name of the application to which you want to add the output configuration.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the application to which you want to add the output
    # configuration. You can use the DescribeApplication operation to get the
    # current application version. If the version specified is not the current
    # version, the `ConcurrentModificationException` is returned.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of objects, each describing one output configuration. In the
    # output configuration, you specify the name of an in-application stream, a
    # destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose
    # delivery stream, or an Amazon Lambda function), and record the formation to
    # use when writing to the destination.
    output: "Output" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddApplicationOutputResponse(OutputShapeBase):
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
class AddApplicationReferenceDataSourceRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "reference_data_source",
                "ReferenceDataSource",
                TypeInfo(ReferenceDataSource),
            ),
        ]

    # Name of an existing application.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the application for which you are adding the reference data
    # source. You can use the DescribeApplication operation to get the current
    # application version. If the version specified is not the current version,
    # the `ConcurrentModificationException` is returned.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reference data source can be an object in your Amazon S3 bucket. Amazon
    # Kinesis Analytics reads the object and copies the data into the in-
    # application table that is created. You provide an S3 bucket, object key
    # name, and the resulting in-application table that is created. You must also
    # provide an IAM role with the necessary permissions that Amazon Kinesis
    # Analytics can assume to read the object from your S3 bucket on your behalf.
    reference_data_source: "ReferenceDataSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddApplicationReferenceDataSourceResponse(OutputShapeBase):
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
class ApplicationDetail(ShapeBase):
    """
    Provides a description of the application, including the application Amazon
    Resource Name (ARN), status, latest version, and input and output configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "application_arn",
                "ApplicationARN",
                TypeInfo(str),
            ),
            (
                "application_status",
                "ApplicationStatus",
                TypeInfo(typing.Union[str, ApplicationStatus]),
            ),
            (
                "application_version_id",
                "ApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "application_description",
                "ApplicationDescription",
                TypeInfo(str),
            ),
            (
                "create_timestamp",
                "CreateTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_timestamp",
                "LastUpdateTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "input_descriptions",
                "InputDescriptions",
                TypeInfo(typing.List[InputDescription]),
            ),
            (
                "output_descriptions",
                "OutputDescriptions",
                TypeInfo(typing.List[OutputDescription]),
            ),
            (
                "reference_data_source_descriptions",
                "ReferenceDataSourceDescriptions",
                TypeInfo(typing.List[ReferenceDataSourceDescription]),
            ),
            (
                "cloud_watch_logging_option_descriptions",
                "CloudWatchLoggingOptionDescriptions",
                TypeInfo(typing.List[CloudWatchLoggingOptionDescription]),
            ),
            (
                "application_code",
                "ApplicationCode",
                TypeInfo(str),
            ),
        ]

    # Name of the application.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the application.
    application_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the application.
    application_status: typing.Union[str, "ApplicationStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Provides the current application version.
    application_version_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the application.
    application_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp when the application version was created.
    create_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time stamp when the application was last updated.
    last_update_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the application input configuration. For more information, see
    # [Configuring Application
    # Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    # input.html).
    input_descriptions: typing.List["InputDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the application output configuration. For more information, see
    # [Configuring Application
    # Output](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-
    # works-output.html).
    output_descriptions: typing.List["OutputDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes reference data sources configured for the application. For more
    # information, see [Configuring Application
    # Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    # input.html).
    reference_data_source_descriptions: typing.List[
        "ReferenceDataSourceDescription"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Describes the CloudWatch log streams that are configured to receive
    # application messages. For more information about using CloudWatch log
    # streams with Amazon Kinesis Analytics applications, see [Working with
    # Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-
    # logs.html).
    cloud_watch_logging_option_descriptions: typing.List[
        "CloudWatchLoggingOptionDescription"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Returns the application code that you provided to perform data analysis on
    # any of the in-application streams in your application.
    application_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ApplicationStatus(str):
    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    READY = "READY"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"


@dataclasses.dataclass
class ApplicationSummary(ShapeBase):
    """
    Provides application summary information, including the application Amazon
    Resource Name (ARN), name, and status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "application_arn",
                "ApplicationARN",
                TypeInfo(str),
            ),
            (
                "application_status",
                "ApplicationStatus",
                TypeInfo(typing.Union[str, ApplicationStatus]),
            ),
        ]

    # Name of the application.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the application.
    application_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of the application.
    application_status: typing.Union[str, "ApplicationStatus"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class ApplicationUpdate(ShapeBase):
    """
    Describes updates to apply to an existing Amazon Kinesis Analytics application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_updates",
                "InputUpdates",
                TypeInfo(typing.List[InputUpdate]),
            ),
            (
                "application_code_update",
                "ApplicationCodeUpdate",
                TypeInfo(str),
            ),
            (
                "output_updates",
                "OutputUpdates",
                TypeInfo(typing.List[OutputUpdate]),
            ),
            (
                "reference_data_source_updates",
                "ReferenceDataSourceUpdates",
                TypeInfo(typing.List[ReferenceDataSourceUpdate]),
            ),
            (
                "cloud_watch_logging_option_updates",
                "CloudWatchLoggingOptionUpdates",
                TypeInfo(typing.List[CloudWatchLoggingOptionUpdate]),
            ),
        ]

    # Describes application input configuration updates.
    input_updates: typing.List["InputUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes application code updates.
    application_code_update: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes application output configuration updates.
    output_updates: typing.List["OutputUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes application reference data source updates.
    reference_data_source_updates: typing.List["ReferenceDataSourceUpdate"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # Describes application CloudWatch logging option updates.
    cloud_watch_logging_option_updates: typing.List[
        "CloudWatchLoggingOptionUpdate"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class CSVMappingParameters(ShapeBase):
    """
    Provides additional mapping information when the record format uses delimiters,
    such as CSV. For example, the following sample records use CSV format, where the
    records use the _'\n'_ as the row delimiter and a comma (",") as the column
    delimiter:

    `"name1", "address1" `

    `"name2, "address2"`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_row_delimiter",
                "RecordRowDelimiter",
                TypeInfo(str),
            ),
            (
                "record_column_delimiter",
                "RecordColumnDelimiter",
                TypeInfo(str),
            ),
        ]

    # Row delimiter. For example, in a CSV format, _'\n'_ is the typical row
    # delimiter.
    record_row_delimiter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Column delimiter. For example, in a CSV format, a comma (",") is the
    # typical column delimiter.
    record_column_delimiter: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudWatchLoggingOption(ShapeBase):
    """
    Provides a description of CloudWatch logging options, including the log stream
    Amazon Resource Name (ARN) and the role ARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_arn",
                "LogStreamARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # ARN of the CloudWatch log to receive application messages.
    log_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IAM ARN of the role to use to send application messages. Note: To write
    # application messages to CloudWatch, the IAM role that is used must have the
    # `PutLogEvents` policy action enabled.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudWatchLoggingOptionDescription(ShapeBase):
    """
    Description of the CloudWatch logging option.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_stream_arn",
                "LogStreamARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "cloud_watch_logging_option_id",
                "CloudWatchLoggingOptionId",
                TypeInfo(str),
            ),
        ]

    # ARN of the CloudWatch log to receive application messages.
    log_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IAM ARN of the role to use to send application messages. Note: To write
    # application messages to CloudWatch, the IAM role used must have the
    # `PutLogEvents` policy action enabled.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the CloudWatch logging option description.
    cloud_watch_logging_option_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudWatchLoggingOptionUpdate(ShapeBase):
    """
    Describes CloudWatch logging option updates.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_watch_logging_option_id",
                "CloudWatchLoggingOptionId",
                TypeInfo(str),
            ),
            (
                "log_stream_arn_update",
                "LogStreamARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # ID of the CloudWatch logging option to update
    cloud_watch_logging_option_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ARN of the CloudWatch log to receive application messages.
    log_stream_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IAM ARN of the role to use to send application messages. Note: To write
    # application messages to CloudWatch, the IAM role used must have the
    # `PutLogEvents` policy action enabled.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CodeValidationException(ShapeBase):
    """
    User-provided application code (query) is invalid. This can be a simple syntax
    error.
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

    # Test
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    Exception thrown as a result of concurrent modification to an application. For
    example, two individuals attempting to edit the same application at the same
    time.
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
class CreateApplicationRequest(ShapeBase):
    """
    TBD
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "application_description",
                "ApplicationDescription",
                TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.List[Input]),
            ),
            (
                "outputs",
                "Outputs",
                TypeInfo(typing.List[Output]),
            ),
            (
                "cloud_watch_logging_options",
                "CloudWatchLoggingOptions",
                TypeInfo(typing.List[CloudWatchLoggingOption]),
            ),
            (
                "application_code",
                "ApplicationCode",
                TypeInfo(str),
            ),
        ]

    # Name of your Amazon Kinesis Analytics application (for example, `sample-
    # app`).
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Summary description of the application.
    application_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this parameter to configure the application input.

    # You can configure your application to receive input from a single streaming
    # source. In this configuration, you map this streaming source to an in-
    # application stream that is created. Your application code can then query
    # the in-application stream like a table (you can think of it as a constantly
    # updating table).

    # For the streaming source, you provide its Amazon Resource Name (ARN) and
    # format of data on the stream (for example, JSON, CSV, etc.). You also must
    # provide an IAM role that Amazon Kinesis Analytics can assume to read this
    # stream on your behalf.

    # To create the in-application stream, you need to specify a schema to
    # transform your data into a schematized version used in SQL. In the schema,
    # you provide the necessary mapping of the data elements in the streaming
    # source to record columns in the in-app stream.
    inputs: typing.List["Input"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can configure application output to write data from any of the in-
    # application streams to up to three destinations.

    # These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose
    # delivery streams, Amazon Lambda destinations, or any combination of the
    # three.

    # In the configuration, you specify the in-application stream name, the
    # destination stream or Lambda function Amazon Resource Name (ARN), and the
    # format to use when writing data. You must also provide an IAM role that
    # Amazon Kinesis Analytics can assume to write to the destination stream or
    # Lambda function on your behalf.

    # In the output configuration, you also provide the output stream or Lambda
    # function ARN. For stream destinations, you provide the format of data in
    # the stream (for example, JSON, CSV). You also must provide an IAM role that
    # Amazon Kinesis Analytics can assume to write to the stream or Lambda
    # function on your behalf.
    outputs: typing.List["Output"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this parameter to configure a CloudWatch log stream to monitor
    # application configuration errors. For more information, see [Working with
    # Amazon CloudWatch
    # Logs](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-
    # logs.html).
    cloud_watch_logging_options: typing.List["CloudWatchLoggingOption"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # One or more SQL statements that read input data, transform it, and generate
    # output. For example, you can write a SQL statement that reads data from one
    # in-application stream, generates a running average of the number of
    # advertisement clicks by vendor, and insert resulting rows in another in-
    # application stream using pumps. For more information about the typical
    # pattern, see [Application
    # Code](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    # app-code.html).

    # You can provide such series of SQL statements, where output of one
    # statement can be used as the input for the next statement. You store
    # intermediate results by creating in-application streams and pumps.

    # Note that the application code must create the streams with names specified
    # in the `Outputs`. For example, if your `Outputs` defines output streams
    # named `ExampleOutputStream1` and `ExampleOutputStream2`, then your
    # application code must create these streams.
    application_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationResponse(OutputShapeBase):
    """
    TBD
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
                "application_summary",
                "ApplicationSummary",
                TypeInfo(ApplicationSummary),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # In response to your `CreateApplication` request, Amazon Kinesis Analytics
    # returns a response with a summary of the application it created, including
    # the application Amazon Resource Name (ARN), name, and status.
    application_summary: "ApplicationSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApplicationCloudWatchLoggingOptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "cloud_watch_logging_option_id",
                "CloudWatchLoggingOptionId",
                TypeInfo(str),
            ),
        ]

    # The Kinesis Analytics application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the Kinesis Analytics application.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `CloudWatchLoggingOptionId` of the CloudWatch logging option to delete.
    # You can get the `CloudWatchLoggingOptionId` by using the
    # DescribeApplication operation.
    cloud_watch_logging_option_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApplicationCloudWatchLoggingOptionResponse(OutputShapeBase):
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
class DeleteApplicationInputProcessingConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
        ]

    # The Kinesis Analytics application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version ID of the Kinesis Analytics application.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the input configuration from which to delete the input processing
    # configuration. You can get a list of the input IDs for an application by
    # using the DescribeApplication operation.
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApplicationInputProcessingConfigurationResponse(OutputShapeBase):
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
class DeleteApplicationOutputRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "output_id",
                "OutputId",
                TypeInfo(str),
            ),
        ]

    # Amazon Kinesis Analytics application name.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Kinesis Analytics application version. You can use the
    # DescribeApplication operation to get the current application version. If
    # the version specified is not the current version, the
    # `ConcurrentModificationException` is returned.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the configuration to delete. Each output configuration that is
    # added to the application, either when the application is created or later
    # using the AddApplicationOutput operation, has a unique ID. You need to
    # provide the ID to uniquely identify the output configuration that you want
    # to delete from the application configuration. You can use the
    # DescribeApplication operation to get the specific `OutputId`.
    output_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApplicationOutputResponse(OutputShapeBase):
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
class DeleteApplicationReferenceDataSourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "reference_id",
                "ReferenceId",
                TypeInfo(str),
            ),
        ]

    # Name of an existing application.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of the application. You can use the DescribeApplication operation
    # to get the current application version. If the version specified is not the
    # current version, the `ConcurrentModificationException` is returned.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ID of the reference data source. When you add a reference data source to
    # your application using the AddApplicationReferenceDataSource, Amazon
    # Kinesis Analytics assigns an ID. You can use the DescribeApplication
    # operation to get the reference ID.
    reference_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApplicationReferenceDataSourceResponse(OutputShapeBase):
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
class DeleteApplicationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "create_timestamp",
                "CreateTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Name of the Amazon Kinesis Analytics application to delete.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use the `DescribeApplication` operation to get this value.
    create_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApplicationResponse(OutputShapeBase):
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
class DescribeApplicationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
        ]

    # Name of the application.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeApplicationResponse(OutputShapeBase):
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
                "application_detail",
                "ApplicationDetail",
                TypeInfo(ApplicationDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides a description of the application, such as the application Amazon
    # Resource Name (ARN), status, latest version, and input and output
    # configuration details.
    application_detail: "ApplicationDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DestinationSchema(ShapeBase):
    """
    Describes the data format when records are written to the destination. For more
    information, see [Configuring Application
    Output](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    output.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_format_type",
                "RecordFormatType",
                TypeInfo(typing.Union[str, RecordFormatType]),
            ),
        ]

    # Specifies the format of the records on the output stream.
    record_format_type: typing.Union[str, "RecordFormatType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class DiscoverInputSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "input_starting_position_configuration",
                "InputStartingPositionConfiguration",
                TypeInfo(InputStartingPositionConfiguration),
            ),
            (
                "s3_configuration",
                "S3Configuration",
                TypeInfo(S3Configuration),
            ),
            (
                "input_processing_configuration",
                "InputProcessingConfiguration",
                TypeInfo(InputProcessingConfiguration),
            ),
        ]

    # Amazon Resource Name (ARN) of the streaming source.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Point at which you want Amazon Kinesis Analytics to start reading records
    # from the specified streaming source discovery purposes.
    input_starting_position_configuration: "InputStartingPositionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify this parameter to discover a schema from data in an S3 object.
    s3_configuration: "S3Configuration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The InputProcessingConfiguration to use to preprocess the records before
    # discovering the schema of the records.
    input_processing_configuration: "InputProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DiscoverInputSchemaResponse(OutputShapeBase):
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
                "input_schema",
                "InputSchema",
                TypeInfo(SourceSchema),
            ),
            (
                "parsed_input_records",
                "ParsedInputRecords",
                TypeInfo(typing.List[typing.List[str]]),
            ),
            (
                "processed_input_records",
                "ProcessedInputRecords",
                TypeInfo(typing.List[str]),
            ),
            (
                "raw_input_records",
                "RawInputRecords",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Schema inferred from the streaming source. It identifies the format of the
    # data in the streaming source and how each data element maps to
    # corresponding columns in the in-application stream that you can create.
    input_schema: "SourceSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of elements, where each element corresponds to a row in a stream
    # record (a stream record can have more than one row).
    parsed_input_records: typing.List[typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Stream data that was modified by the processor specified in the
    # `InputProcessingConfiguration` parameter.
    processed_input_records: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Raw stream data that was sampled to infer the schema.
    raw_input_records: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Input(ShapeBase):
    """
    When you configure the application input, you specify the streaming source, the
    in-application stream name that is created, and the mapping between the two. For
    more information, see [Configuring Application
    Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    input.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_prefix",
                "NamePrefix",
                TypeInfo(str),
            ),
            (
                "input_schema",
                "InputSchema",
                TypeInfo(SourceSchema),
            ),
            (
                "input_processing_configuration",
                "InputProcessingConfiguration",
                TypeInfo(InputProcessingConfiguration),
            ),
            (
                "kinesis_streams_input",
                "KinesisStreamsInput",
                TypeInfo(KinesisStreamsInput),
            ),
            (
                "kinesis_firehose_input",
                "KinesisFirehoseInput",
                TypeInfo(KinesisFirehoseInput),
            ),
            (
                "input_parallelism",
                "InputParallelism",
                TypeInfo(InputParallelism),
            ),
        ]

    # Name prefix to use when creating an in-application stream. Suppose that you
    # specify a prefix "MyInApplicationStream." Amazon Kinesis Analytics then
    # creates one or more (as per the `InputParallelism` count you specified) in-
    # application streams with names "MyInApplicationStream_001,"
    # "MyInApplicationStream_002," and so on.
    name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the format of the data in the streaming source, and how each data
    # element maps to corresponding columns in the in-application stream that is
    # being created.

    # Also used to describe the format of the reference data source.
    input_schema: "SourceSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The InputProcessingConfiguration for the input. An input processor
    # transforms records as they are received from the stream, before the
    # application's SQL code executes. Currently, the only input processing
    # configuration available is InputLambdaProcessor.
    input_processing_configuration: "InputProcessingConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the streaming source is an Amazon Kinesis stream, identifies the
    # stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon
    # Kinesis Analytics to access the stream on your behalf.

    # Note: Either `KinesisStreamsInput` or `KinesisFirehoseInput` is required.
    kinesis_streams_input: "KinesisStreamsInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the streaming source is an Amazon Kinesis Firehose delivery stream,
    # identifies the delivery stream's ARN and an IAM role that enables Amazon
    # Kinesis Analytics to access the stream on your behalf.

    # Note: Either `KinesisStreamsInput` or `KinesisFirehoseInput` is required.
    kinesis_firehose_input: "KinesisFirehoseInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the number of in-application streams to create.

    # Data from your source is routed to these in-application input streams.

    # (see [Configuring Application
    # Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    # input.html).
    input_parallelism: "InputParallelism" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputConfiguration(ShapeBase):
    """
    When you start your application, you provide this configuration, which
    identifies the input source and the point in the input source at which you want
    the application to start processing records.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_starting_position_configuration",
                "InputStartingPositionConfiguration",
                TypeInfo(InputStartingPositionConfiguration),
            ),
        ]

    # Input source ID. You can get this ID by calling the DescribeApplication
    # operation.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Point at which you want the application to start processing records from
    # the streaming source.
    input_starting_position_configuration: "InputStartingPositionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputDescription(ShapeBase):
    """
    Describes the application input configuration. For more information, see
    [Configuring Application
    Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    input.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
            (
                "name_prefix",
                "NamePrefix",
                TypeInfo(str),
            ),
            (
                "in_app_stream_names",
                "InAppStreamNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "input_processing_configuration_description",
                "InputProcessingConfigurationDescription",
                TypeInfo(InputProcessingConfigurationDescription),
            ),
            (
                "kinesis_streams_input_description",
                "KinesisStreamsInputDescription",
                TypeInfo(KinesisStreamsInputDescription),
            ),
            (
                "kinesis_firehose_input_description",
                "KinesisFirehoseInputDescription",
                TypeInfo(KinesisFirehoseInputDescription),
            ),
            (
                "input_schema",
                "InputSchema",
                TypeInfo(SourceSchema),
            ),
            (
                "input_parallelism",
                "InputParallelism",
                TypeInfo(InputParallelism),
            ),
            (
                "input_starting_position_configuration",
                "InputStartingPositionConfiguration",
                TypeInfo(InputStartingPositionConfiguration),
            ),
        ]

    # Input ID associated with the application input. This is the ID that Amazon
    # Kinesis Analytics assigns to each input configuration you add to your
    # application.
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In-application name prefix.
    name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the in-application stream names that are mapped to the stream
    # source.
    in_app_stream_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the preprocessor that executes on records in this input
    # before the application's code is run.
    input_processing_configuration_description: "InputProcessingConfigurationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If an Amazon Kinesis stream is configured as streaming source, provides
    # Amazon Kinesis stream's Amazon Resource Name (ARN) and an IAM role that
    # enables Amazon Kinesis Analytics to access the stream on your behalf.
    kinesis_streams_input_description: "KinesisStreamsInputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If an Amazon Kinesis Firehose delivery stream is configured as a streaming
    # source, provides the delivery stream's ARN and an IAM role that enables
    # Amazon Kinesis Analytics to access the stream on your behalf.
    kinesis_firehose_input_description: "KinesisFirehoseInputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the format of the data in the streaming source, and how each data
    # element maps to corresponding columns in the in-application stream that is
    # being created.
    input_schema: "SourceSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the configured parallelism (number of in-application streams
    # mapped to the streaming source).
    input_parallelism: "InputParallelism" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Point at which the application is configured to read from the input stream.
    input_starting_position_configuration: "InputStartingPositionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputLambdaProcessor(ShapeBase):
    """
    An object that contains the Amazon Resource Name (ARN) of the [AWS
    Lambda](https://aws.amazon.com/documentation/lambda/) function that is used to
    preprocess records in the stream, and the ARN of the IAM role that is used to
    access the AWS Lambda function.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the [AWS Lambda](https://aws.amazon.com/documentation/lambda/)
    # function that operates on records in the stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role that is used to access the AWS Lambda function.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputLambdaProcessorDescription(ShapeBase):
    """
    An object that contains the Amazon Resource Name (ARN) of the [AWS
    Lambda](https://aws.amazon.com/documentation/lambda/) function that is used to
    preprocess records in the stream, and the ARN of the IAM role that is used to
    access the AWS Lambda expression.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the [AWS Lambda](https://aws.amazon.com/documentation/lambda/)
    # function that is used to preprocess the records in the stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role that is used to access the AWS Lambda function.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputLambdaProcessorUpdate(ShapeBase):
    """
    Represents an update to the InputLambdaProcessor that is used to preprocess the
    records in the stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_update",
                "ResourceARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the new [AWS
    # Lambda](https://aws.amazon.com/documentation/lambda/) function that is used
    # to preprocess the records in the stream.
    resource_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the new IAM role that is used to access the AWS Lambda function.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputParallelism(ShapeBase):
    """
    Describes the number of in-application streams to create for a given streaming
    source. For information about parallelism, see [Configuring Application
    Input](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-
    input.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
        ]

    # Number of in-application streams to create. For more information, see
    # [Limits](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html).
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputParallelismUpdate(ShapeBase):
    """
    Provides updates to the parallelism count.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count_update",
                "CountUpdate",
                TypeInfo(int),
            ),
        ]

    # Number of in-application streams to create for the specified streaming
    # source.
    count_update: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputProcessingConfiguration(ShapeBase):
    """
    Provides a description of a processor that is used to preprocess the records in
    the stream before being processed by your application code. Currently, the only
    input processor available is [AWS
    Lambda](https://aws.amazon.com/documentation/lambda/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_lambda_processor",
                "InputLambdaProcessor",
                TypeInfo(InputLambdaProcessor),
            ),
        ]

    # The InputLambdaProcessor that is used to preprocess the records in the
    # stream before being processed by your application code.
    input_lambda_processor: "InputLambdaProcessor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputProcessingConfigurationDescription(ShapeBase):
    """
    Provides configuration information about an input processor. Currently, the only
    input processor available is [AWS
    Lambda](https://aws.amazon.com/documentation/lambda/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_lambda_processor_description",
                "InputLambdaProcessorDescription",
                TypeInfo(InputLambdaProcessorDescription),
            ),
        ]

    # Provides configuration information about the associated
    # InputLambdaProcessorDescription.
    input_lambda_processor_description: "InputLambdaProcessorDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputProcessingConfigurationUpdate(ShapeBase):
    """
    Describes updates to an InputProcessingConfiguration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_lambda_processor_update",
                "InputLambdaProcessorUpdate",
                TypeInfo(InputLambdaProcessorUpdate),
            ),
        ]

    # Provides update information for an InputLambdaProcessor.
    input_lambda_processor_update: "InputLambdaProcessorUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputSchemaUpdate(ShapeBase):
    """
    Describes updates for the application's input schema.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_format_update",
                "RecordFormatUpdate",
                TypeInfo(RecordFormat),
            ),
            (
                "record_encoding_update",
                "RecordEncodingUpdate",
                TypeInfo(str),
            ),
            (
                "record_column_updates",
                "RecordColumnUpdates",
                TypeInfo(typing.List[RecordColumn]),
            ),
        ]

    # Specifies the format of the records on the streaming source.
    record_format_update: "RecordFormat" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the encoding of the records in the streaming source. For example,
    # UTF-8.
    record_encoding_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `RecordColumn` objects. Each object describes the mapping of the
    # streaming source element to the corresponding column in the in-application
    # stream.
    record_column_updates: typing.List["RecordColumn"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InputStartingPosition(str):
    NOW = "NOW"
    TRIM_HORIZON = "TRIM_HORIZON"
    LAST_STOPPED_POINT = "LAST_STOPPED_POINT"


@dataclasses.dataclass
class InputStartingPositionConfiguration(ShapeBase):
    """
    Describes the point at which the application reads from the streaming source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_starting_position",
                "InputStartingPosition",
                TypeInfo(typing.Union[str, InputStartingPosition]),
            ),
        ]

    # The starting position on the stream.

    #   * `NOW` \- Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.

    #   * `TRIM_HORIZON` \- Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.

    #   * `LAST_STOPPED_POINT` \- Resume reading from where the application last stopped reading.
    input_starting_position: typing.Union[str, "InputStartingPosition"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class InputUpdate(ShapeBase):
    """
    Describes updates to a specific input configuration (identified by the `InputId`
    of an application).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
            (
                "name_prefix_update",
                "NamePrefixUpdate",
                TypeInfo(str),
            ),
            (
                "input_processing_configuration_update",
                "InputProcessingConfigurationUpdate",
                TypeInfo(InputProcessingConfigurationUpdate),
            ),
            (
                "kinesis_streams_input_update",
                "KinesisStreamsInputUpdate",
                TypeInfo(KinesisStreamsInputUpdate),
            ),
            (
                "kinesis_firehose_input_update",
                "KinesisFirehoseInputUpdate",
                TypeInfo(KinesisFirehoseInputUpdate),
            ),
            (
                "input_schema_update",
                "InputSchemaUpdate",
                TypeInfo(InputSchemaUpdate),
            ),
            (
                "input_parallelism_update",
                "InputParallelismUpdate",
                TypeInfo(InputParallelismUpdate),
            ),
        ]

    # Input ID of the application input to be updated.
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name prefix for in-application streams that Amazon Kinesis Analytics
    # creates for the specific streaming source.
    name_prefix_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes updates for an input processing configuration.
    input_processing_configuration_update: "InputProcessingConfigurationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If an Amazon Kinesis stream is the streaming source to be updated, provides
    # an updated stream Amazon Resource Name (ARN) and IAM role ARN.
    kinesis_streams_input_update: "KinesisStreamsInputUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If an Amazon Kinesis Firehose delivery stream is the streaming source to be
    # updated, provides an updated stream ARN and IAM role ARN.
    kinesis_firehose_input_update: "KinesisFirehoseInputUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the data format on the streaming source, and how record elements
    # on the streaming source map to columns of the in-application stream that is
    # created.
    input_schema_update: "InputSchemaUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the parallelism updates (the number in-application streams Amazon
    # Kinesis Analytics creates for the specific streaming source).
    input_parallelism_update: "InputParallelismUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidApplicationConfigurationException(ShapeBase):
    """
    User-provided application configuration is not valid.
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

    # test
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidArgumentException(ShapeBase):
    """
    Specified input parameter value is invalid.
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
class JSONMappingParameters(ShapeBase):
    """
    Provides additional mapping information when JSON is the record format on the
    streaming source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_row_path",
                "RecordRowPath",
                TypeInfo(str),
            ),
        ]

    # Path to the top-level parent that contains the records.
    record_row_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisFirehoseInput(ShapeBase):
    """
    Identifies an Amazon Kinesis Firehose delivery stream as the streaming source.
    You provide the delivery stream's Amazon Resource Name (ARN) and an IAM role ARN
    that enables Amazon Kinesis Analytics to access the stream on your behalf.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # ARN of the input delivery stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf. You need to make sure the role has necessary
    # permissions to access the stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisFirehoseInputDescription(ShapeBase):
    """
    Describes the Amazon Kinesis Firehose delivery stream that is configured as the
    streaming source in the application input configuration.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics assumes to access the
    # stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisFirehoseInputUpdate(ShapeBase):
    """
    When updating application input configuration, provides information about an
    Amazon Kinesis Firehose delivery stream as the streaming source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_update",
                "ResourceARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the input Amazon Kinesis Firehose delivery
    # stream to read.
    resource_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf. You need to grant necessary permissions to this
    # role.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisFirehoseOutput(ShapeBase):
    """
    When configuring application output, identifies an Amazon Kinesis Firehose
    delivery stream as the destination. You provide the stream Amazon Resource Name
    (ARN) and an IAM role that enables Amazon Kinesis Analytics to write to the
    stream on your behalf.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # ARN of the destination Amazon Kinesis Firehose delivery stream to write to.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to write to
    # the destination stream on your behalf. You need to grant the necessary
    # permissions to this role.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisFirehoseOutputDescription(ShapeBase):
    """
    For an application output, describes the Amazon Kinesis Firehose delivery stream
    configured as its destination.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisFirehoseOutputUpdate(ShapeBase):
    """
    When updating an output configuration using the UpdateApplication operation,
    provides information about an Amazon Kinesis Firehose delivery stream configured
    as the destination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_update",
                "ResourceARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream
    # to write to.
    resource_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf. You need to grant necessary permissions to this
    # role.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamsInput(ShapeBase):
    """
    Identifies an Amazon Kinesis stream as the streaming source. You provide the
    stream's Amazon Resource Name (ARN) and an IAM role ARN that enables Amazon
    Kinesis Analytics to access the stream on your behalf.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # ARN of the input Amazon Kinesis stream to read.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf. You need to grant the necessary permissions to this
    # role.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamsInputDescription(ShapeBase):
    """
    Describes the Amazon Kinesis stream that is configured as the streaming source
    in the application input configuration.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the Amazon Kinesis stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamsInputUpdate(ShapeBase):
    """
    When updating application input configuration, provides information about an
    Amazon Kinesis stream as the streaming source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_update",
                "ResourceARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.
    resource_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf. You need to grant the necessary permissions to this
    # role.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamsOutput(ShapeBase):
    """
    When configuring application output, identifies an Amazon Kinesis stream as the
    destination. You provide the stream Amazon Resource Name (ARN) and also an IAM
    role ARN that Amazon Kinesis Analytics can use to write to the stream on your
    behalf.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # ARN of the destination Amazon Kinesis stream to write to.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to write to
    # the destination stream on your behalf. You need to grant the necessary
    # permissions to this role.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamsOutputDescription(ShapeBase):
    """
    For an application output, describes the Amazon Kinesis stream configured as its
    destination.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the Amazon Kinesis stream.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisStreamsOutputUpdate(ShapeBase):
    """
    When updating an output configuration using the UpdateApplication operation,
    provides information about an Amazon Kinesis stream configured as the
    destination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_update",
                "ResourceARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to
    # write the output.
    resource_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
    # stream on your behalf. You need to grant the necessary permissions to this
    # role.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaOutput(ShapeBase):
    """
    When configuring application output, identifies an AWS Lambda function as the
    destination. You provide the function Amazon Resource Name (ARN) and also an IAM
    role ARN that Amazon Kinesis Analytics can use to write to the function on your
    behalf.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the destination Lambda function to write to.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to write to
    # the destination function on your behalf. You need to grant the necessary
    # permissions to this role.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaOutputDescription(ShapeBase):
    """
    For an application output, describes the AWS Lambda function configured as its
    destination.
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
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the destination Lambda function.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to write to
    # the destination function.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaOutputUpdate(ShapeBase):
    """
    When updating an output configuration using the UpdateApplication operation,
    provides information about an AWS Lambda function configured as the destination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn_update",
                "ResourceARNUpdate",
                TypeInfo(str),
            ),
            (
                "role_arn_update",
                "RoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the destination Lambda function.
    resource_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to write to
    # the destination function on your behalf. You need to grant the necessary
    # permissions to this role.
    role_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    Exceeded the number of applications allowed.
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
class ListApplicationsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "exclusive_start_application_name",
                "ExclusiveStartApplicationName",
                TypeInfo(str),
            ),
        ]

    # Maximum number of applications to list.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the application to start the list with. When using pagination to
    # retrieve the list, you don't need to specify this parameter in the first
    # request. However, in subsequent requests, you add the last application name
    # from the previous response to get the next page of applications.
    exclusive_start_application_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListApplicationsResponse(OutputShapeBase):
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
                "application_summaries",
                "ApplicationSummaries",
                TypeInfo(typing.List[ApplicationSummary]),
            ),
            (
                "has_more_applications",
                "HasMoreApplications",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of `ApplicationSummary` objects.
    application_summaries: typing.List["ApplicationSummary"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Returns true if there are more applications to retrieve.
    has_more_applications: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MappingParameters(ShapeBase):
    """
    When configuring application input at the time of creating or updating an
    application, provides additional mapping information specific to the record
    format (such as JSON, CSV, or record fields delimited by some delimiter) on the
    streaming source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "json_mapping_parameters",
                "JSONMappingParameters",
                TypeInfo(JSONMappingParameters),
            ),
            (
                "csv_mapping_parameters",
                "CSVMappingParameters",
                TypeInfo(CSVMappingParameters),
            ),
        ]

    # Provides additional mapping information when JSON is the record format on
    # the streaming source.
    json_mapping_parameters: "JSONMappingParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides additional mapping information when the record format uses
    # delimiters (for example, CSV).
    csv_mapping_parameters: "CSVMappingParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Output(ShapeBase):
    """
    Describes application output configuration in which you identify an in-
    application stream and a destination where you want the in-application stream
    data to be written. The destination can be an Amazon Kinesis stream or an Amazon
    Kinesis Firehose delivery stream.

    For limits on how many destinations an application can write and other
    limitations, see
    [Limits](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html).
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
                "destination_schema",
                "DestinationSchema",
                TypeInfo(DestinationSchema),
            ),
            (
                "kinesis_streams_output",
                "KinesisStreamsOutput",
                TypeInfo(KinesisStreamsOutput),
            ),
            (
                "kinesis_firehose_output",
                "KinesisFirehoseOutput",
                TypeInfo(KinesisFirehoseOutput),
            ),
            (
                "lambda_output",
                "LambdaOutput",
                TypeInfo(LambdaOutput),
            ),
        ]

    # Name of the in-application stream.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the data format when records are written to the destination. For
    # more information, see [Configuring Application
    # Output](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-
    # works-output.html).
    destination_schema: "DestinationSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies an Amazon Kinesis stream as the destination.
    kinesis_streams_output: "KinesisStreamsOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies an Amazon Kinesis Firehose delivery stream as the destination.
    kinesis_firehose_output: "KinesisFirehoseOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies an AWS Lambda function as the destination.
    lambda_output: "LambdaOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputDescription(ShapeBase):
    """
    Describes the application output configuration, which includes the in-
    application stream name and the destination where the stream data is written.
    The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose
    delivery stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_id",
                "OutputId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "kinesis_streams_output_description",
                "KinesisStreamsOutputDescription",
                TypeInfo(KinesisStreamsOutputDescription),
            ),
            (
                "kinesis_firehose_output_description",
                "KinesisFirehoseOutputDescription",
                TypeInfo(KinesisFirehoseOutputDescription),
            ),
            (
                "lambda_output_description",
                "LambdaOutputDescription",
                TypeInfo(LambdaOutputDescription),
            ),
            (
                "destination_schema",
                "DestinationSchema",
                TypeInfo(DestinationSchema),
            ),
        ]

    # A unique identifier for the output configuration.
    output_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the in-application stream configured as output.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes Amazon Kinesis stream configured as the destination where output
    # is written.
    kinesis_streams_output_description: "KinesisStreamsOutputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the Amazon Kinesis Firehose delivery stream configured as the
    # destination where output is written.
    kinesis_firehose_output_description: "KinesisFirehoseOutputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the AWS Lambda function configured as the destination where
    # output is written.
    lambda_output_description: "LambdaOutputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Data format used for writing data to the destination.
    destination_schema: "DestinationSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputUpdate(ShapeBase):
    """
    Describes updates to the output configuration identified by the `OutputId`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_id",
                "OutputId",
                TypeInfo(str),
            ),
            (
                "name_update",
                "NameUpdate",
                TypeInfo(str),
            ),
            (
                "kinesis_streams_output_update",
                "KinesisStreamsOutputUpdate",
                TypeInfo(KinesisStreamsOutputUpdate),
            ),
            (
                "kinesis_firehose_output_update",
                "KinesisFirehoseOutputUpdate",
                TypeInfo(KinesisFirehoseOutputUpdate),
            ),
            (
                "lambda_output_update",
                "LambdaOutputUpdate",
                TypeInfo(LambdaOutputUpdate),
            ),
            (
                "destination_schema_update",
                "DestinationSchemaUpdate",
                TypeInfo(DestinationSchema),
            ),
        ]

    # Identifies the specific output configuration that you want to update.
    output_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you want to specify a different in-application stream for this output
    # configuration, use this field to specify the new in-application stream
    # name.
    name_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes an Amazon Kinesis stream as the destination for the output.
    kinesis_streams_output_update: "KinesisStreamsOutputUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes an Amazon Kinesis Firehose delivery stream as the destination for
    # the output.
    kinesis_firehose_output_update: "KinesisFirehoseOutputUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes an AWS Lambda function as the destination for the output.
    lambda_output_update: "LambdaOutputUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the data format when records are written to the destination. For
    # more information, see [Configuring Application
    # Output](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-
    # works-output.html).
    destination_schema_update: "DestinationSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RecordColumn(ShapeBase):
    """
    Describes the mapping of each data element in the streaming source to the
    corresponding column in the in-application stream.

    Also used to describe the format of the reference data source.
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
                "sql_type",
                "SqlType",
                TypeInfo(str),
            ),
            (
                "mapping",
                "Mapping",
                TypeInfo(str),
            ),
        ]

    # Name of the column created in the in-application input stream or reference
    # table.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of column created in the in-application input stream or reference
    # table.
    sql_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reference to the data element in the streaming input of the reference data
    # source.
    mapping: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecordFormat(ShapeBase):
    """
    Describes the record format and relevant mapping information that should be
    applied to schematize the records on the stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_format_type",
                "RecordFormatType",
                TypeInfo(typing.Union[str, RecordFormatType]),
            ),
            (
                "mapping_parameters",
                "MappingParameters",
                TypeInfo(MappingParameters),
            ),
        ]

    # The type of record format.
    record_format_type: typing.Union[str, "RecordFormatType"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # When configuring application input at the time of creating or updating an
    # application, provides additional mapping information specific to the record
    # format (such as JSON, CSV, or record fields delimited by some delimiter) on
    # the streaming source.
    mapping_parameters: "MappingParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RecordFormatType(str):
    JSON = "JSON"
    CSV = "CSV"


@dataclasses.dataclass
class ReferenceDataSource(ShapeBase):
    """
    Describes the reference data source by providing the source information (S3
    bucket name and object key name), the resulting in-application table name that
    is created, and the necessary schema to map the data elements in the Amazon S3
    object to the in-application table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "reference_schema",
                "ReferenceSchema",
                TypeInfo(SourceSchema),
            ),
            (
                "s3_reference_data_source",
                "S3ReferenceDataSource",
                TypeInfo(S3ReferenceDataSource),
            ),
        ]

    # Name of the in-application table to create.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the format of the data in the streaming source, and how each data
    # element maps to corresponding columns created in the in-application stream.
    reference_schema: "SourceSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the S3 bucket and object that contains the reference data. Also
    # identifies the IAM role Amazon Kinesis Analytics can assume to read this
    # object on your behalf. An Amazon Kinesis Analytics application loads
    # reference data only once. If the data changes, you call the
    # UpdateApplication operation to trigger reloading of data into your
    # application.
    s3_reference_data_source: "S3ReferenceDataSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReferenceDataSourceDescription(ShapeBase):
    """
    Describes the reference data source configured for an application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_id",
                "ReferenceId",
                TypeInfo(str),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "s3_reference_data_source_description",
                "S3ReferenceDataSourceDescription",
                TypeInfo(S3ReferenceDataSourceDescription),
            ),
            (
                "reference_schema",
                "ReferenceSchema",
                TypeInfo(SourceSchema),
            ),
        ]

    # ID of the reference data source. This is the ID that Amazon Kinesis
    # Analytics assigns when you add the reference data source to your
    # application using the AddApplicationReferenceDataSource operation.
    reference_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The in-application table name created by the specific reference data source
    # configuration.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides the S3 bucket name, the object key name that contains the
    # reference data. It also provides the Amazon Resource Name (ARN) of the IAM
    # role that Amazon Kinesis Analytics can assume to read the Amazon S3 object
    # and populate the in-application reference table.
    s3_reference_data_source_description: "S3ReferenceDataSourceDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the format of the data in the streaming source, and how each data
    # element maps to corresponding columns created in the in-application stream.
    reference_schema: "SourceSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReferenceDataSourceUpdate(ShapeBase):
    """
    When you update a reference data source configuration for an application, this
    object provides all the updated values (such as the source bucket name and
    object key name), the in-application table name that is created, and updated
    mapping information that maps the data in the Amazon S3 object to the in-
    application reference table that is created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_id",
                "ReferenceId",
                TypeInfo(str),
            ),
            (
                "table_name_update",
                "TableNameUpdate",
                TypeInfo(str),
            ),
            (
                "s3_reference_data_source_update",
                "S3ReferenceDataSourceUpdate",
                TypeInfo(S3ReferenceDataSourceUpdate),
            ),
            (
                "reference_schema_update",
                "ReferenceSchemaUpdate",
                TypeInfo(SourceSchema),
            ),
        ]

    # ID of the reference data source being updated. You can use the
    # DescribeApplication operation to get this value.
    reference_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # In-application table name that is created by this update.
    table_name_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the S3 bucket name, object key name, and IAM role that Amazon
    # Kinesis Analytics can assume to read the Amazon S3 object on your behalf
    # and populate the in-application reference table.
    s3_reference_data_source_update: "S3ReferenceDataSourceUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the format of the data in the streaming source, and how each data
    # element maps to corresponding columns created in the in-application stream.
    reference_schema_update: "SourceSchema" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    Application is not available for this operation.
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
class ResourceNotFoundException(ShapeBase):
    """
    Specified application can't be found.
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
class ResourceProvisionedThroughputExceededException(ShapeBase):
    """
    Discovery failed to get a record from the streaming source because of the Amazon
    Kinesis Streams ProvisionedThroughputExceededException. For more information,
    see
    [GetRecords](http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html)
    in the Amazon Kinesis Streams API Reference.
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
class S3Configuration(ShapeBase):
    """
    Provides a description of an Amazon S3 data source, including the Amazon
    Resource Name (ARN) of the S3 bucket, the ARN of the IAM role that is used to
    access the bucket, and the name of the S3 object that contains the data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleARN",
                TypeInfo(str),
            ),
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "file_key",
                "FileKey",
                TypeInfo(str),
            ),
        ]

    # IAM ARN of the role used to access the data.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the S3 bucket that contains the data.
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the object that contains the data.
    file_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3ReferenceDataSource(ShapeBase):
    """
    Identifies the S3 bucket and object that contains the reference data. Also
    identifies the IAM role Amazon Kinesis Analytics can assume to read this object
    on your behalf.

    An Amazon Kinesis Analytics application loads reference data only once. If the
    data changes, you call the UpdateApplication operation to trigger reloading of
    data into your application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "file_key",
                "FileKey",
                TypeInfo(str),
            ),
            (
                "reference_role_arn",
                "ReferenceRoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the S3 bucket.
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object key name containing reference data.
    file_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that the service can assume to read data on your
    # behalf. This role must have permission for the `s3:GetObject` action on the
    # object and trust policy that allows Amazon Kinesis Analytics service
    # principal to assume this role.
    reference_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3ReferenceDataSourceDescription(ShapeBase):
    """
    Provides the bucket name and object key name that stores the reference data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_arn",
                "BucketARN",
                TypeInfo(str),
            ),
            (
                "file_key",
                "FileKey",
                TypeInfo(str),
            ),
            (
                "reference_role_arn",
                "ReferenceRoleARN",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the S3 bucket.
    bucket_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon S3 object key name.
    file_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to read the
    # Amazon S3 object on your behalf to populate the in-application reference
    # table.
    reference_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3ReferenceDataSourceUpdate(ShapeBase):
    """
    Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis
    Analytics can assume to read the Amazon S3 object on your behalf and populate
    the in-application reference table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_arn_update",
                "BucketARNUpdate",
                TypeInfo(str),
            ),
            (
                "file_key_update",
                "FileKeyUpdate",
                TypeInfo(str),
            ),
            (
                "reference_role_arn_update",
                "ReferenceRoleARNUpdate",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the S3 bucket.
    bucket_arn_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Object key name.
    file_key_update: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the IAM role that Amazon Kinesis Analytics can assume to read the
    # Amazon S3 object and populate the in-application.
    reference_role_arn_update: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceUnavailableException(ShapeBase):
    """
    The service is unavailable, back off and retry the operation.
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
class SourceSchema(ShapeBase):
    """
    Describes the format of the data in the streaming source, and how each data
    element maps to corresponding columns created in the in-application stream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "record_format",
                "RecordFormat",
                TypeInfo(RecordFormat),
            ),
            (
                "record_columns",
                "RecordColumns",
                TypeInfo(typing.List[RecordColumn]),
            ),
            (
                "record_encoding",
                "RecordEncoding",
                TypeInfo(str),
            ),
        ]

    # Specifies the format of the records on the streaming source.
    record_format: "RecordFormat" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `RecordColumn` objects.
    record_columns: typing.List["RecordColumn"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the encoding of the records in the streaming source. For example,
    # UTF-8.
    record_encoding: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartApplicationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "input_configurations",
                "InputConfigurations",
                TypeInfo(typing.List[InputConfiguration]),
            ),
        ]

    # Name of the application.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies the specific input, by ID, that the application starts
    # consuming. Amazon Kinesis Analytics starts reading the streaming source
    # associated with the input. You can also specify where in the streaming
    # source you want Amazon Kinesis Analytics to start reading.
    input_configurations: typing.List["InputConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartApplicationResponse(OutputShapeBase):
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
class StopApplicationRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
        ]

    # Name of the running application to stop.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopApplicationResponse(OutputShapeBase):
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
class UnableToDetectSchemaException(ShapeBase):
    """
    Data format is not valid, Amazon Kinesis Analytics is not able to detect schema
    for the given streaming source.
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
                "raw_input_records",
                "RawInputRecords",
                TypeInfo(typing.List[str]),
            ),
            (
                "processed_input_records",
                "ProcessedInputRecords",
                TypeInfo(typing.List[str]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    raw_input_records: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    processed_input_records: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_name",
                "ApplicationName",
                TypeInfo(str),
            ),
            (
                "current_application_version_id",
                "CurrentApplicationVersionId",
                TypeInfo(int),
            ),
            (
                "application_update",
                "ApplicationUpdate",
                TypeInfo(ApplicationUpdate),
            ),
        ]

    # Name of the Amazon Kinesis Analytics application to update.
    application_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current application version ID. You can use the DescribeApplication
    # operation to get this value.
    current_application_version_id: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes application updates.
    application_update: "ApplicationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApplicationResponse(OutputShapeBase):
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
