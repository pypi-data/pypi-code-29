import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Alias(ShapeBase):
    """
    An alias for an edge.
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
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The canonical name of the alias.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of names for the alias, including the canonical name.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the alias.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AnnotationValue(ShapeBase):
    """
    Value of a segment annotation. Has one of three value types: Number, Boolean or
    String.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_value",
                "NumberValue",
                TypeInfo(float),
            ),
            (
                "boolean_value",
                "BooleanValue",
                TypeInfo(bool),
            ),
            (
                "string_value",
                "StringValue",
                TypeInfo(str),
            ),
        ]

    # Value for a Number annotation.
    number_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value for a Boolean annotation.
    boolean_value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value for a String annotation.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BackendConnectionErrors(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timeout_count",
                "TimeoutCount",
                TypeInfo(int),
            ),
            (
                "connection_refused_count",
                "ConnectionRefusedCount",
                TypeInfo(int),
            ),
            (
                "http_code4_xx_count",
                "HTTPCode4XXCount",
                TypeInfo(int),
            ),
            (
                "http_code5_xx_count",
                "HTTPCode5XXCount",
                TypeInfo(int),
            ),
            (
                "unknown_host_count",
                "UnknownHostCount",
                TypeInfo(int),
            ),
            (
                "other_count",
                "OtherCount",
                TypeInfo(int),
            ),
        ]

    timeout_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    connection_refused_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    http_code4_xx_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    http_code5_xx_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    unknown_host_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    other_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetTracesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_ids",
                "TraceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Specify the trace IDs of requests for which to retrieve segments.
    trace_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchGetTracesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "traces",
                "Traces",
                TypeInfo(typing.List[Trace]),
            ),
            (
                "unprocessed_trace_ids",
                "UnprocessedTraceIds",
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

    # Full traces for the specified requests.
    traces: typing.List["Trace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Trace IDs of requests that haven't been processed.
    unprocessed_trace_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["BatchGetTracesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class CreateSamplingRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sampling_rule",
                "SamplingRule",
                TypeInfo(SamplingRule),
            ),
        ]

    # The rule definition.
    sampling_rule: "SamplingRule" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSamplingRuleResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sampling_rule_record",
                "SamplingRuleRecord",
                TypeInfo(SamplingRuleRecord),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The saved rule definition and metadata.
    sampling_rule_record: "SamplingRuleRecord" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSamplingRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "rule_arn",
                "RuleARN",
                TypeInfo(str),
            ),
        ]

    # The name of the sampling rule. Specify a rule by either name or ARN, but
    # not both.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the sampling rule. Specify a rule by either name or ARN, but not
    # both.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSamplingRuleResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sampling_rule_record",
                "SamplingRuleRecord",
                TypeInfo(SamplingRuleRecord),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The deleted rule definition and metadata.
    sampling_rule_record: "SamplingRuleRecord" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Edge(ShapeBase):
    """
    Information about a connection between two services.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_id",
                "ReferenceId",
                TypeInfo(int),
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
                "summary_statistics",
                "SummaryStatistics",
                TypeInfo(EdgeStatistics),
            ),
            (
                "response_time_histogram",
                "ResponseTimeHistogram",
                TypeInfo(typing.List[HistogramEntry]),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(typing.List[Alias]),
            ),
        ]

    # Identifier of the edge. Unique within a service map.
    reference_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the first segment on the edge.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time of the last segment on the edge.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Response statistics for segments on the edge.
    summary_statistics: "EdgeStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A histogram that maps the spread of client response times on an edge.
    response_time_histogram: typing.List["HistogramEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Aliases for the edge.
    aliases: typing.List["Alias"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EdgeStatistics(ShapeBase):
    """
    Response statistics for an edge.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ok_count",
                "OkCount",
                TypeInfo(int),
            ),
            (
                "error_statistics",
                "ErrorStatistics",
                TypeInfo(ErrorStatistics),
            ),
            (
                "fault_statistics",
                "FaultStatistics",
                TypeInfo(FaultStatistics),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
            (
                "total_response_time",
                "TotalResponseTime",
                TypeInfo(float),
            ),
        ]

    # The number of requests that completed with a 2xx Success status code.
    ok_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about requests that failed with a 4xx Client Error status code.
    error_statistics: "ErrorStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about requests that failed with a 5xx Server Error status code.
    fault_statistics: "FaultStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of completed requests.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The aggregate response time of completed requests.
    total_response_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionConfig(ShapeBase):
    """
    A configuration document that specifies encryption configuration settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, EncryptionStatus]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
        ]

    # The ID of the customer master key (CMK) used for encryption, if applicable.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encryption status. While the status is `UPDATING`, X-Ray may encrypt
    # data with a combination of the new and old settings.
    status: typing.Union[str, "EncryptionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of encryption. Set to `KMS` for encryption with CMKs. Set to
    # `NONE` for default encryption.
    type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EncryptionStatus(str):
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"


class EncryptionType(str):
    NONE = "NONE"
    KMS = "KMS"


@dataclasses.dataclass
class ErrorStatistics(ShapeBase):
    """
    Information about requests that failed with a 4xx Client Error status code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "throttle_count",
                "ThrottleCount",
                TypeInfo(int),
            ),
            (
                "other_count",
                "OtherCount",
                TypeInfo(int),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    # The number of requests that failed with a 419 throttling status code.
    throttle_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests that failed with untracked 4xx Client Error status
    # codes.
    other_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of requests that failed with a 4xx Client Error status
    # code.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FaultStatistics(ShapeBase):
    """
    Information about requests that failed with a 5xx Server Error status code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "other_count",
                "OtherCount",
                TypeInfo(int),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
        ]

    # The number of requests that failed with untracked 5xx Server Error status
    # codes.
    other_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of requests that failed with a 5xx Server Error status
    # code.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEncryptionConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetEncryptionConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "encryption_config",
                "EncryptionConfig",
                TypeInfo(EncryptionConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encryption configuration document.
    encryption_config: "EncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSamplingRulesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSamplingRulesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sampling_rule_records",
                "SamplingRuleRecords",
                TypeInfo(typing.List[SamplingRuleRecord]),
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

    # Rule definitions and metadata.
    sampling_rule_records: typing.List["SamplingRuleRecord"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSamplingStatisticSummariesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSamplingStatisticSummariesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sampling_statistic_summaries",
                "SamplingStatisticSummaries",
                TypeInfo(typing.List[SamplingStatisticSummary]),
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

    # Information about the number of requests instrumented for each sampling
    # rule.
    sampling_statistic_summaries: typing.List["SamplingStatisticSummary"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSamplingTargetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sampling_statistics_documents",
                "SamplingStatisticsDocuments",
                TypeInfo(typing.List[SamplingStatisticsDocument]),
            ),
        ]

    # Information about rules that the service is using to sample requests.
    sampling_statistics_documents: typing.List["SamplingStatisticsDocument"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class GetSamplingTargetsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sampling_target_documents",
                "SamplingTargetDocuments",
                TypeInfo(typing.List[SamplingTargetDocument]),
            ),
            (
                "last_rule_modification",
                "LastRuleModification",
                TypeInfo(datetime.datetime),
            ),
            (
                "unprocessed_statistics",
                "UnprocessedStatistics",
                TypeInfo(typing.List[UnprocessedStatistics]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Updated rules that the service should use to sample requests.
    sampling_target_documents: typing.List["SamplingTargetDocument"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The last time a user changed the sampling rule configuration. If the
    # sampling rule configuration changed since the service last retrieved it,
    # the service should call GetSamplingRules to get the latest version.
    last_rule_modification: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about SamplingStatisticsDocument that X-Ray could not process.
    unprocessed_statistics: typing.List["UnprocessedStatistics"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class GetServiceGraphRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The start of the time frame for which to generate a graph.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time frame for which to generate a graph.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServiceGraphResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
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
                "services",
                "Services",
                TypeInfo(typing.List[Service]),
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

    # The start of the time frame for which the graph was generated.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time frame for which the graph was generated.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The services that have processed a traced request during the specified time
    # frame.
    services: typing.List["Service"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetServiceGraphResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetTraceGraphRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_ids",
                "TraceIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Trace IDs of requests for which to generate a service graph.
    trace_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTraceGraphResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "services",
                "Services",
                TypeInfo(typing.List[Service]),
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

    # The services that have processed one of the specified requests.
    services: typing.List["Service"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pagination token. Not used.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetTraceGraphResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetTraceSummariesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "sampling",
                "Sampling",
                TypeInfo(bool),
            ),
            (
                "filter_expression",
                "FilterExpression",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The start of the time frame for which to retrieve traces.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end of the time frame for which to retrieve traces.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to `true` to get summaries for only a subset of available traces.
    sampling: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify a filter expression to retrieve trace summaries for services or
    # requests that meet certain requirements.
    filter_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the pagination token returned by a previous request to retrieve the
    # next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTraceSummariesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "trace_summaries",
                "TraceSummaries",
                TypeInfo(typing.List[TraceSummary]),
            ),
            (
                "approximate_time",
                "ApproximateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "traces_processed_count",
                "TracesProcessedCount",
                TypeInfo(int),
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

    # Trace IDs and metadata for traces that were found in the specified time
    # frame.
    trace_summaries: typing.List["TraceSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The start time of this page of results.
    approximate_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of traces processed, including traces that did not match
    # the specified filter expression.
    traces_processed_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the requested time frame contained more than one page of results, you
    # can use this token to retrieve the next page. The first page contains the
    # most most recent results, closest to the end of the time frame.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetTraceSummariesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class HistogramEntry(ShapeBase):
    """
    An entry in a histogram for a statistic. A histogram maps the range of observed
    values on the X axis, and the prevalence of each value on the Y axis.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(float),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
        ]

    # The value of the entry.
    value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prevalence of the entry.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Http(ShapeBase):
    """
    Information about an HTTP request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "http_url",
                "HttpURL",
                TypeInfo(str),
            ),
            (
                "http_status",
                "HttpStatus",
                TypeInfo(int),
            ),
            (
                "http_method",
                "HttpMethod",
                TypeInfo(str),
            ),
            (
                "user_agent",
                "UserAgent",
                TypeInfo(str),
            ),
            (
                "client_ip",
                "ClientIp",
                TypeInfo(str),
            ),
        ]

    # The request URL.
    http_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The response status.
    http_status: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The request method.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The request's user agent string.
    user_agent: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address of the requestor.
    client_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    The request is missing required parameters or has invalid parameters.
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
class PutEncryptionConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, EncryptionType]),
            ),
            (
                "key_id",
                "KeyId",
                TypeInfo(str),
            ),
        ]

    # The type of encryption. Set to `KMS` to use your own key for encryption.
    # Set to `NONE` for default encryption.
    type: typing.Union[str, "EncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An AWS KMS customer master key (CMK) in one of the following formats:

    #   * **Alias** \- The name of the key. For example, `alias/MyKey`.

    #   * **Key ID** \- The KMS key ID of the key. For example, `ae4aa6d49-a4d8-9df9-a475-4ff6d7898456`.

    #   * **ARN** \- The full Amazon Resource Name of the key ID or alias. For example, `arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456`. Use this format to specify a key in a different account.

    # Omit this key if you set `Type` to `NONE`.
    key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEncryptionConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "encryption_config",
                "EncryptionConfig",
                TypeInfo(EncryptionConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new encryption configuration.
    encryption_config: "EncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutTelemetryRecordsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "telemetry_records",
                "TelemetryRecords",
                TypeInfo(typing.List[TelemetryRecord]),
            ),
            (
                "ec2_instance_id",
                "EC2InstanceId",
                TypeInfo(str),
            ),
            (
                "hostname",
                "Hostname",
                TypeInfo(str),
            ),
            (
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
        ]

    telemetry_records: typing.List["TelemetryRecord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    ec2_instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutTelemetryRecordsResult(OutputShapeBase):
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
class PutTraceSegmentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trace_segment_documents",
                "TraceSegmentDocuments",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A string containing a JSON document defining one or more segments or
    # subsegments.
    trace_segment_documents: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutTraceSegmentsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_trace_segments",
                "UnprocessedTraceSegments",
                TypeInfo(typing.List[UnprocessedTraceSegment]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segments that failed processing.
    unprocessed_trace_segments: typing.List["UnprocessedTraceSegment"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class RuleLimitExceededException(ShapeBase):
    """
    You have reached the maximum number of sampling rules.
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
class SamplingRule(ShapeBase):
    """
    A sampling rule that services use to decide whether to instrument a request.
    Rule fields can match properties of the service, or properties of a request. The
    service can ignore rules that don't match its properties.
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
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "fixed_rate",
                "FixedRate",
                TypeInfo(float),
            ),
            (
                "reservoir_size",
                "ReservoirSize",
                TypeInfo(int),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
            (
                "service_type",
                "ServiceType",
                TypeInfo(str),
            ),
            (
                "host",
                "Host",
                TypeInfo(str),
            ),
            (
                "http_method",
                "HTTPMethod",
                TypeInfo(str),
            ),
            (
                "url_path",
                "URLPath",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "rule_arn",
                "RuleARN",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Matches the ARN of the AWS resource on which the service runs.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The priority of the sampling rule.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The percentage of matching requests to instrument, after the reservoir is
    # exhausted.
    fixed_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A fixed number of matching requests to instrument per second, prior to
    # applying the fixed rate. The reservoir is not used directly by services,
    # but applies to all services using the rule collectively.
    reservoir_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the `name` that the service uses to identify itself in segments.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the `origin` that the service uses to identify its type in
    # segments.
    service_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the hostname from a request URL.
    host: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the HTTP method of a request.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the path from a request URL.
    url_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the sampling rule format (`1`).
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the sampling rule. Specify a rule by either name or ARN, but
    # not both.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the sampling rule. Specify a rule by either name or ARN, but not
    # both.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches attributes derived from the request.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SamplingRuleRecord(ShapeBase):
    """
    A SamplingRule and its metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sampling_rule",
                "SamplingRule",
                TypeInfo(SamplingRule),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "modified_at",
                "ModifiedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The sampling rule.
    sampling_rule: "SamplingRule" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the rule was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the rule was last modified.
    modified_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SamplingRuleUpdate(ShapeBase):
    """
    A document specifying changes to a sampling rule's configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "rule_arn",
                "RuleARN",
                TypeInfo(str),
            ),
            (
                "resource_arn",
                "ResourceARN",
                TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(int),
            ),
            (
                "fixed_rate",
                "FixedRate",
                TypeInfo(float),
            ),
            (
                "reservoir_size",
                "ReservoirSize",
                TypeInfo(int),
            ),
            (
                "host",
                "Host",
                TypeInfo(str),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
            (
                "service_type",
                "ServiceType",
                TypeInfo(str),
            ),
            (
                "http_method",
                "HTTPMethod",
                TypeInfo(str),
            ),
            (
                "url_path",
                "URLPath",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the sampling rule. Specify a rule by either name or ARN, but
    # not both.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the sampling rule. Specify a rule by either name or ARN, but not
    # both.
    rule_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the ARN of the AWS resource on which the service runs.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The priority of the sampling rule.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The percentage of matching requests to instrument, after the reservoir is
    # exhausted.
    fixed_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A fixed number of matching requests to instrument per second, prior to
    # applying the fixed rate. The reservoir is not used directly by services,
    # but applies to all services using the rule collectively.
    reservoir_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the hostname from a request URL.
    host: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the `name` that the service uses to identify itself in segments.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the `origin` that the service uses to identify its type in
    # segments.
    service_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the HTTP method of a request.
    http_method: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches the path from a request URL.
    url_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Matches attributes derived from the request.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SamplingStatisticSummary(ShapeBase):
    """
    Aggregated request sampling data for a sampling rule across all services for a
    10 second window.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "request_count",
                "RequestCount",
                TypeInfo(int),
            ),
            (
                "borrow_count",
                "BorrowCount",
                TypeInfo(int),
            ),
            (
                "sampled_count",
                "SampledCount",
                TypeInfo(int),
            ),
        ]

    # The name of the sampling rule.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the reporting window.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of requests that matched the rule.
    request_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests recorded with borrowed reservoir quota.
    borrow_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests recorded.
    sampled_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SamplingStatisticsDocument(ShapeBase):
    """
    Request sampling results for a single rule from a service. Results are for the
    last 10 seconds unless the service has been assigned a longer reporting interval
    after a previous call to GetSamplingTargets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "client_id",
                "ClientID",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "request_count",
                "RequestCount",
                TypeInfo(int),
            ),
            (
                "sampled_count",
                "SampledCount",
                TypeInfo(int),
            ),
            (
                "borrow_count",
                "BorrowCount",
                TypeInfo(int),
            ),
        ]

    # The name of the sampling rule.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the service in hexadecimal.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current time.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of requests that matched the rule.
    request_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests recorded.
    sampled_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests recorded with borrowed reservoir quota.
    borrow_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SamplingTargetDocument(ShapeBase):
    """
    Temporary changes to a sampling rule configuration. To meet the global sampling
    target for a rule, X-Ray calculates a new reservoir for each service based on
    the recent sampling results of all services that called GetSamplingTargets.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "fixed_rate",
                "FixedRate",
                TypeInfo(float),
            ),
            (
                "reservoir_quota",
                "ReservoirQuota",
                TypeInfo(int),
            ),
            (
                "reservoir_quota_ttl",
                "ReservoirQuotaTTL",
                TypeInfo(datetime.datetime),
            ),
            (
                "interval",
                "Interval",
                TypeInfo(int),
            ),
        ]

    # The name of the sampling rule.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The percentage of matching requests to instrument, after the reservoir is
    # exhausted.
    fixed_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of requests per second that X-Ray allocated this service.
    reservoir_quota: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the reservoir quota expires.
    reservoir_quota_ttl: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of seconds for the service to wait before getting sampling
    # targets again.
    interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Segment(ShapeBase):
    """
    A segment from a trace that has been ingested by the X-Ray service. The segment
    can be compiled from documents uploaded with PutTraceSegments, or an `inferred`
    segment for a downstream service, generated from a subsegment sent by the
    service that called it.

    For the full segment document schema, see [AWS X-Ray Segment
    Documents](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-
    segmentdocuments.html) in the _AWS X-Ray Developer Guide_.
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
                "document",
                "Document",
                TypeInfo(str),
            ),
        ]

    # The segment's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The segment document.
    document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Service(ShapeBase):
    """
    Information about an application that processed requests, users that made
    requests, or downstream services, resources and applications that an application
    used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_id",
                "ReferenceId",
                TypeInfo(int),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "root",
                "Root",
                TypeInfo(bool),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
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
                "edges",
                "Edges",
                TypeInfo(typing.List[Edge]),
            ),
            (
                "summary_statistics",
                "SummaryStatistics",
                TypeInfo(ServiceStatistics),
            ),
            (
                "duration_histogram",
                "DurationHistogram",
                TypeInfo(typing.List[HistogramEntry]),
            ),
            (
                "response_time_histogram",
                "ResponseTimeHistogram",
                TypeInfo(typing.List[HistogramEntry]),
            ),
        ]

    # Identifier for the service. Unique within the service map.
    reference_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The canonical name of the service.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of names for the service, including the canonical name.
    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the service was the first service to process a request.
    root: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifier of the AWS account in which the service runs.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of service.

    #   * AWS Resource - The type of an AWS resource. For example, `AWS::EC2::Instance` for a application running on Amazon EC2 or `AWS::DynamoDB::Table` for an Amazon DynamoDB table that the application used.

    #   * AWS Service - The type of an AWS service. For example, `AWS::DynamoDB` for downstream calls to Amazon DynamoDB that didn't target a specific table.

    #   * `client` \- Represents the clients that sent requests to a root service.

    #   * `remote` \- A downstream service of indeterminate type.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service's state.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the first segment that the service generated.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time of the last segment that the service generated.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Connections to downstream services.
    edges: typing.List["Edge"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Aggregated statistics for the service.
    summary_statistics: "ServiceStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A histogram that maps the spread of service durations.
    duration_histogram: typing.List["HistogramEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A histogram that maps the spread of service response times.
    response_time_histogram: typing.List["HistogramEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceId(ShapeBase):
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
                "names",
                "Names",
                TypeInfo(typing.List[str]),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    names: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceStatistics(ShapeBase):
    """
    Response statistics for a service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ok_count",
                "OkCount",
                TypeInfo(int),
            ),
            (
                "error_statistics",
                "ErrorStatistics",
                TypeInfo(ErrorStatistics),
            ),
            (
                "fault_statistics",
                "FaultStatistics",
                TypeInfo(FaultStatistics),
            ),
            (
                "total_count",
                "TotalCount",
                TypeInfo(int),
            ),
            (
                "total_response_time",
                "TotalResponseTime",
                TypeInfo(float),
            ),
        ]

    # The number of requests that completed with a 2xx Success status code.
    ok_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about requests that failed with a 4xx Client Error status code.
    error_statistics: "ErrorStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about requests that failed with a 5xx Server Error status code.
    fault_statistics: "FaultStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of completed requests.
    total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The aggregate response time of completed requests.
    total_response_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TelemetryRecord(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "segments_received_count",
                "SegmentsReceivedCount",
                TypeInfo(int),
            ),
            (
                "segments_sent_count",
                "SegmentsSentCount",
                TypeInfo(int),
            ),
            (
                "segments_spillover_count",
                "SegmentsSpilloverCount",
                TypeInfo(int),
            ),
            (
                "segments_rejected_count",
                "SegmentsRejectedCount",
                TypeInfo(int),
            ),
            (
                "backend_connection_errors",
                "BackendConnectionErrors",
                TypeInfo(BackendConnectionErrors),
            ),
        ]

    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    segments_received_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    segments_sent_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    segments_spillover_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    segments_rejected_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    backend_connection_errors: "BackendConnectionErrors" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ThrottledException(ShapeBase):
    """
    The request exceeds the maximum number of requests per second.
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
class Trace(ShapeBase):
    """
    A collection of segment documents with matching trace IDs.
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
                "duration",
                "Duration",
                TypeInfo(float),
            ),
            (
                "segments",
                "Segments",
                TypeInfo(typing.List[Segment]),
            ),
        ]

    # The unique identifier for the request that generated the trace's segments
    # and subsegments.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time in seconds between the start time of the root segment
    # and the end time of the last segment that completed.
    duration: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Segment documents for the segments and subsegments that comprise the trace.
    segments: typing.List["Segment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TraceSummary(ShapeBase):
    """
    Metadata generated from the segment documents in a trace.
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
                "duration",
                "Duration",
                TypeInfo(float),
            ),
            (
                "response_time",
                "ResponseTime",
                TypeInfo(float),
            ),
            (
                "has_fault",
                "HasFault",
                TypeInfo(bool),
            ),
            (
                "has_error",
                "HasError",
                TypeInfo(bool),
            ),
            (
                "has_throttle",
                "HasThrottle",
                TypeInfo(bool),
            ),
            (
                "is_partial",
                "IsPartial",
                TypeInfo(bool),
            ),
            (
                "http",
                "Http",
                TypeInfo(Http),
            ),
            (
                "annotations",
                "Annotations",
                TypeInfo(typing.Dict[str, typing.List[ValueWithServiceIds]]),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.List[TraceUser]),
            ),
            (
                "service_ids",
                "ServiceIds",
                TypeInfo(typing.List[ServiceId]),
            ),
        ]

    # The unique identifier for the request that generated the trace's segments
    # and subsegments.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time in seconds between the start time of the root segment
    # and the end time of the last segment that completed.
    duration: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time in seconds between the start and end times of the root
    # segment. If the service performs work asynchronously, the response time
    # measures the time before the response is sent to the user, while the
    # duration measures the amount of time before the last traced activity
    # completes.
    response_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more of the segment documents has a 500 series error.
    has_fault: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more of the segment documents has a 400 series error.
    has_error: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more of the segment documents has a 429 throttling error.
    has_throttle: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more of the segment documents is in progress.
    is_partial: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the HTTP request served by the trace.
    http: "Http" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Annotations from the trace's segment documents.
    annotations: typing.Dict[str, typing.
                             List["ValueWithServiceIds"]] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # Users from the trace's segment documents.
    users: typing.List["TraceUser"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Service IDs from the trace's segment documents.
    service_ids: typing.List["ServiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TraceUser(ShapeBase):
    """
    Information about a user recorded in segment documents.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "service_ids",
                "ServiceIds",
                TypeInfo(typing.List[ServiceId]),
            ),
        ]

    # The user's name.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Services that the user's request hit.
    service_ids: typing.List["ServiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnprocessedStatistics(ShapeBase):
    """
    Sampling statistics from a call to GetSamplingTargets that X-Ray could not
    process.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
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

    # The name of the sampling rule.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error code.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnprocessedTraceSegment(ShapeBase):
    """
    Information about a segment that failed processing.
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

    # The segment's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error that caused processing to fail.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSamplingRuleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sampling_rule_update",
                "SamplingRuleUpdate",
                TypeInfo(SamplingRuleUpdate),
            ),
        ]

    # The rule and fields to change.
    sampling_rule_update: "SamplingRuleUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSamplingRuleResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sampling_rule_record",
                "SamplingRuleRecord",
                TypeInfo(SamplingRuleRecord),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated rule definition and metadata.
    sampling_rule_record: "SamplingRuleRecord" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValueWithServiceIds(ShapeBase):
    """
    Information about a segment annotation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "annotation_value",
                "AnnotationValue",
                TypeInfo(AnnotationValue),
            ),
            (
                "service_ids",
                "ServiceIds",
                TypeInfo(typing.List[ServiceId]),
            ),
        ]

    # Values of the annotation.
    annotation_value: "AnnotationValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Services to which the annotation applies.
    service_ids: typing.List["ServiceId"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
