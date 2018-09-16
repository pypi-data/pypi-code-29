import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AWSRegion(str):
    """
    Region of customer S3 bucket.
    """
    us_east_1 = "us-east-1"
    us_west_1 = "us-west-1"
    us_west_2 = "us-west-2"
    eu_central_1 = "eu-central-1"
    eu_west_1 = "eu-west-1"
    ap_southeast_1 = "ap-southeast-1"
    ap_southeast_2 = "ap-southeast-2"
    ap_northeast_1 = "ap-northeast-1"


class AdditionalArtifact(str):
    """
    Enable support for Redshift and/or QuickSight.
    """
    REDSHIFT = "REDSHIFT"
    QUICKSIGHT = "QUICKSIGHT"


class CompressionFormat(str):
    """
    Preferred compression format for report.
    """
    ZIP = "ZIP"
    GZIP = "GZIP"


@dataclasses.dataclass
class DeleteReportDefinitionRequest(ShapeBase):
    """
    Request of DeleteReportDefinition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_name",
                "ReportName",
                TypeInfo(str),
            ),
        ]

    # Preferred name for a report, it has to be unique. Must starts with a
    # number/letter, case sensitive. Limited to 256 characters.
    report_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReportDefinitionResponse(OutputShapeBase):
    """
    Response of DeleteReportDefinition
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
                "response_message",
                "ResponseMessage",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message indicates if the deletion is successful.
    response_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReportDefinitionsRequest(ShapeBase):
    """
    Request of DescribeReportDefinitions
    """

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

    # The max number of results returned by the operation.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A generic string.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReportDefinitionsResponse(OutputShapeBase):
    """
    Response of DescribeReportDefinitions
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
                "report_definitions",
                "ReportDefinitions",
                TypeInfo(typing.List[ReportDefinition]),
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

    # A list of report definitions.
    report_definitions: typing.List["ReportDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A generic string.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeReportDefinitionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DuplicateReportNameException(ShapeBase):
    """
    This exception is thrown when putting a report preference with a name that
    already exists.
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

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(ShapeBase):
    """
    This exception is thrown on a known dependency failure.
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

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutReportDefinitionRequest(ShapeBase):
    """
    Request of PutReportDefinition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_definition",
                "ReportDefinition",
                TypeInfo(ReportDefinition),
            ),
        ]

    # The definition of AWS Cost and Usage Report. Customer can specify the
    # report name, time unit, report format, compression format, S3 bucket and
    # additional artifacts and schema elements in the definition.
    report_definition: "ReportDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutReportDefinitionResponse(OutputShapeBase):
    """
    Response of PutReportDefinition
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
class ReportDefinition(ShapeBase):
    """
    The definition of AWS Cost and Usage Report. Customer can specify the report
    name, time unit, report format, compression format, S3 bucket and additional
    artifacts and schema elements in the definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_name",
                "ReportName",
                TypeInfo(str),
            ),
            (
                "time_unit",
                "TimeUnit",
                TypeInfo(typing.Union[str, TimeUnit]),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, ReportFormat]),
            ),
            (
                "compression",
                "Compression",
                TypeInfo(typing.Union[str, CompressionFormat]),
            ),
            (
                "additional_schema_elements",
                "AdditionalSchemaElements",
                TypeInfo(typing.List[typing.Union[str, SchemaElement]]),
            ),
            (
                "s3_bucket",
                "S3Bucket",
                TypeInfo(str),
            ),
            (
                "s3_prefix",
                "S3Prefix",
                TypeInfo(str),
            ),
            (
                "s3_region",
                "S3Region",
                TypeInfo(typing.Union[str, AWSRegion]),
            ),
            (
                "additional_artifacts",
                "AdditionalArtifacts",
                TypeInfo(typing.List[typing.Union[str, AdditionalArtifact]]),
            ),
        ]

    # Preferred name for a report, it has to be unique. Must starts with a
    # number/letter, case sensitive. Limited to 256 characters.
    report_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The frequency on which report data are measured and displayed.
    time_unit: typing.Union[str, "TimeUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Preferred format for report.
    format: typing.Union[str, "ReportFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Preferred compression format for report.
    compression: typing.Union[str, "CompressionFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of schema elements.
    additional_schema_elements: typing.List[typing.Union[str, "SchemaElement"]
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # Name of customer S3 bucket.
    s3_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Preferred report path prefix. Limited to 256 characters.
    s3_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Region of customer S3 bucket.
    s3_region: typing.Union[str, "AWSRegion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of additional artifacts.
    additional_artifacts: typing.List[typing.Union[str, "AdditionalArtifact"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


class ReportFormat(str):
    """
    Preferred format for report.
    """
    textORcsv = "textORcsv"


@dataclasses.dataclass
class ReportLimitReachedException(ShapeBase):
    """
    This exception is thrown when the number of report preference reaches max limit.
    The max number is 5.
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

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SchemaElement(str):
    """
    Preference of including Resource IDs. You can include additional details about
    individual resource IDs in your report.
    """
    RESOURCES = "RESOURCES"


class TimeUnit(str):
    """
    The frequency on which report data are measured and displayed.
    """
    HOURLY = "HOURLY"
    DAILY = "DAILY"


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    This exception is thrown when providing an invalid input. eg. Put a report
    preference with an invalid report name, or Delete a report preference with an
    empty report name.
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

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
