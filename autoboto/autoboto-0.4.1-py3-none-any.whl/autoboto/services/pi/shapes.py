import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class DataPoint(ShapeBase):
    """
    A timestamp, and a single numerical value, which together represent a
    measurement at a particular point in time.
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
                "value",
                "Value",
                TypeInfo(float),
            ),
        ]

    # The time, in epoch format, associated with a particular `Value`.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actual value associated with a particular `Timestamp`.
    value: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDimensionKeysRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_type",
                "ServiceType",
                TypeInfo(typing.Union[str, ServiceType]),
            ),
            (
                "identifier",
                "Identifier",
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
                "metric",
                "Metric",
                TypeInfo(str),
            ),
            (
                "group_by",
                "GroupBy",
                TypeInfo(DimensionGroup),
            ),
            (
                "period_in_seconds",
                "PeriodInSeconds",
                TypeInfo(int),
            ),
            (
                "partition_by",
                "PartitionBy",
                TypeInfo(DimensionGroup),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(typing.Dict[str, str]),
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

    # The AWS service for which Performance Insights will return metrics. The
    # only valid value for _ServiceType_ is: `RDS`
    service_type: typing.Union[str, "ServiceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An immutable, AWS Region-unique identifier for a data source. Performance
    # Insights gathers metrics from this data source.

    # To use an Amazon RDS instance as a data source, you specify its
    # `DbiResourceId` value - for example: `db-FAIHNTYBKTGAUSUZQYPDS2GW4A`
    identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time specifying the beginning of the requested time series
    # data. You can't specify a `StartTime` that's earlier than 7 days ago. The
    # value specified is _inclusive_ \- data points equal to or greater than
    # `StartTime` will be returned.

    # The value for `StartTime` must be earlier than the value for `EndTime`.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time specifying the end of the requested time series data. The
    # value specified is _exclusive_ \- data points less than (but not equal to)
    # `EndTime` will be returned.

    # The value for `EndTime` must be later than the value for `StartTime`.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a Performance Insights metric to be measured.

    # Valid values for `Metric` are:

    #   * `db.load.avg` \- a scaled representation of the number of active sessions for the database engine.

    #   * `db.sampledload.avg` \- the raw number of active sessions for the database engine.
    metric: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A specification for how to aggregate the data points from a query result.
    # You must specify a valid dimension group. Performance Insights will return
    # all of the dimensions within that group, unless you provide the names of
    # specific dimensions within that group. You can also request that
    # Performance Insights return a limited number of values for a dimension.
    group_by: "DimensionGroup" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The granularity, in seconds, of the data points returned from Performance
    # Insights. A period can be as short as one second, or as long as one day
    # (86400 seconds). Valid values are:

    #   * `1` (one second)

    #   * `60` (one minute)

    #   * `300` (five minutes)

    #   * `3600` (one hour)

    #   * `86400` (twenty-four hours)

    # If you don't specify `PeriodInSeconds`, then Performance Insights will
    # choose a value for you, with a goal of returning roughly 100-200 data
    # points in the response.
    period_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For each dimension specified in `GroupBy`, specify a secondary dimension to
    # further subdivide the partition keys in the response.
    partition_by: "DimensionGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more filters to apply in the request. Restrictions:

    #   * Any number of filters by the same dimension, as specified in the `GroupBy` or `Partition` parameters.

    #   * A single filter for any other dimension in this dimension group.
    filter: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to return in the response. If more items exist
    # than the specified `MaxRecords` value, a pagination token is included in
    # the response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # token, up to the value specified by `MaxRecords`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDimensionKeysResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "aligned_start_time",
                "AlignedStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "aligned_end_time",
                "AlignedEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "partition_keys",
                "PartitionKeys",
                TypeInfo(typing.List[ResponsePartitionKey]),
            ),
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[DimensionKeyDescription]),
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

    # The start time for the returned dimension keys, after alignment to a
    # granular boundary (as specified by `PeriodInSeconds`). `AlignedStartTime`
    # will be less than or equal to the value of the user-specified `StartTime`.
    aligned_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time for the returned dimension keys, after alignment to a granular
    # boundary (as specified by `PeriodInSeconds`). `AlignedEndTime` will be
    # greater than or equal to the value of the user-specified `Endtime`.
    aligned_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `PartitionBy` was present in the request, `PartitionKeys` contains the
    # breakdown of dimension keys by the specified partitions.
    partition_keys: typing.List["ResponsePartitionKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The dimension keys that were requested.
    keys: typing.List["DimensionKeyDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # token, up to the value specified by `MaxRecords`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DimensionGroup(ShapeBase):
    """
    A logical grouping of Performance Insights metrics for a related subject area.
    For example, the `db.sql` dimension group consists of the following dimensions:
    `db.sql.id`, `db.sql.db_id`, `db.sql.statement`, and `db.sql.tokenized_id`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group",
                "Group",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[str]),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The name of the dimension group. Valid values are:

    #   * `db.user`

    #   * `db.host`

    #   * `db.sql`

    #   * `db.sql_tokenized`

    #   * `db.wait_event`

    #   * `db.wait_event_type`
    group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of specific dimensions from a dimension group. If this parameter is
    # not present, then it signifies that all of the dimensions in the group were
    # requested, or are present in the response.

    # Valid values for elements in the `Dimensions` array are:

    #   * db.user.id

    #   * db.user.name

    #   * db.host.id

    #   * db.host.name

    #   * db.sql.id

    #   * db.sql.db_id

    #   * db.sql.statement

    #   * db.sql.tokenized_id

    #   * db.sql_tokenized.id

    #   * db.sql_tokenized.db_id

    #   * db.sql_tokenized.statement

    #   * db.wait_event.name

    #   * db.wait_event.type

    #   * db.wait_event_type.name
    dimensions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to fetch for this dimension group.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DimensionKeyDescription(ShapeBase):
    """
    An array of descriptions and aggregated values for each dimension within a
    dimension group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "total",
                "Total",
                TypeInfo(float),
            ),
            (
                "partitions",
                "Partitions",
                TypeInfo(typing.List[float]),
            ),
        ]

    # A map of name-value pairs for the dimensions in the group.
    dimensions: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The aggregated metric value for the dimension(s), over the requested time
    # range.
    total: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `PartitionBy` was specified, `PartitionKeys` contains the dimensions
    # that were.
    partitions: typing.List[float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetResourceMetricsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_type",
                "ServiceType",
                TypeInfo(typing.Union[str, ServiceType]),
            ),
            (
                "identifier",
                "Identifier",
                TypeInfo(str),
            ),
            (
                "metric_queries",
                "MetricQueries",
                TypeInfo(typing.List[MetricQuery]),
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
                "period_in_seconds",
                "PeriodInSeconds",
                TypeInfo(int),
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

    # The AWS service for which Performance Insights will return metrics. The
    # only valid value for _ServiceType_ is: `RDS`
    service_type: typing.Union[str, "ServiceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An immutable, AWS Region-unique identifier for a data source. Performance
    # Insights gathers metrics from this data source.

    # To use an Amazon RDS instance as a data source, you specify its
    # `DbiResourceId` value - for example: `db-FAIHNTYBKTGAUSUZQYPDS2GW4A`
    identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of one or more queries to perform. Each query must specify a
    # Performance Insights metric, and can optionally specify aggregation and
    # filtering criteria.
    metric_queries: typing.List["MetricQuery"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time specifying the beginning of the requested time series
    # data. You can't specify a `StartTime` that's earlier than 7 days ago. The
    # value specified is _inclusive_ \- data points equal to or greater than
    # `StartTime` will be returned.

    # The value for `StartTime` must be earlier than the value for `EndTime`.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time specifiying the end of the requested time series data.
    # The value specified is _exclusive_ \- data points less than (but not equal
    # to) `EndTime` will be returned.

    # The value for `EndTime` must be later than the value for `StartTime`.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The granularity, in seconds, of the data points returned from Performance
    # Insights. A period can be as short as one second, or as long as one day
    # (86400 seconds). Valid values are:

    #   * `1` (one second)

    #   * `60` (one minute)

    #   * `300` (five minutes)

    #   * `3600` (one hour)

    #   * `86400` (twenty-four hours)

    # If you don't specify `PeriodInSeconds`, then Performance Insights will
    # choose a value for you, with a goal of returning roughly 100-200 data
    # points in the response.
    period_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return in the response. If more items exist
    # than the specified `MaxRecords` value, a pagination token is included in
    # the response so that the remaining results can be retrieved.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # token, up to the value specified by `MaxRecords`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceMetricsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "aligned_start_time",
                "AlignedStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "aligned_end_time",
                "AlignedEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "identifier",
                "Identifier",
                TypeInfo(str),
            ),
            (
                "metric_list",
                "MetricList",
                TypeInfo(typing.List[MetricKeyDataPoints]),
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

    # The start time for the returned metrics, after alignment to a granular
    # boundary (as specified by `PeriodInSeconds`). `AlignedStartTime` will be
    # less than or equal to the value of the user-specified `StartTime`.
    aligned_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time for the returned metrics, after alignment to a granular
    # boundary (as specified by `PeriodInSeconds`). `AlignedEndTime` will be
    # greater than or equal to the value of the user-specified `Endtime`.
    aligned_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An immutable, AWS Region-unique identifier for a data source. Performance
    # Insights gathers metrics from this data source.

    # To use an Amazon RDS instance as a data source, you specify its
    # `DbiResourceId` value - for example: `db-FAIHNTYBKTGAUSUZQYPDS2GW4A`
    identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of metric results,, where each array element contains all of the
    # data points for a particular dimension.
    metric_list: typing.List["MetricKeyDataPoints"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional pagination token provided by a previous request. If this
    # parameter is specified, the response includes only records beyond the
    # token, up to the value specified by `MaxRecords`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceError(ShapeBase):
    """
    The request failed due to an unknown error.
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
class InvalidArgumentException(ShapeBase):
    """
    One of the arguments provided is invalid for this request.
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
class MetricKeyDataPoints(ShapeBase):
    """
    A time-ordered series of data points, correpsonding to a dimension of a
    Performance Insights metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(ResponseResourceMetricKey),
            ),
            (
                "data_points",
                "DataPoints",
                TypeInfo(typing.List[DataPoint]),
            ),
        ]

    # The dimension(s) to which the data points apply.
    key: "ResponseResourceMetricKey" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of timestamp-value pairs, representing measurements over a period
    # of time.
    data_points: typing.List["DataPoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricQuery(ShapeBase):
    """
    A single query to be processed. You must provide the metric to query. If no
    other parameters are specified, Performance Insights returns all of the data
    points for that metric. You can optionally request that the data points be
    aggregated by dimension group ( `GroupBy`), and return only those data points
    that match your criteria (`Filter`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric",
                "Metric",
                TypeInfo(str),
            ),
            (
                "group_by",
                "GroupBy",
                TypeInfo(DimensionGroup),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of a Performance Insights metric to be measured.

    # Valid values for `Metric` are:

    #   * `db.load.avg` \- a scaled representation of the number of active sessions for the database engine.

    #   * `db.sampledload.avg` \- the raw number of active sessions for the database engine.
    metric: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A specification for how to aggregate the data points from a query result.
    # You must specify a valid dimension group. Performance Insights will return
    # all of the dimensions within that group, unless you provide the names of
    # specific dimensions within that group. You can also request that
    # Performance Insights return a limited number of values for a dimension.
    group_by: "DimensionGroup" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more filters to apply in the request. Restrictions:

    #   * Any number of filters by the same dimension, as specified in the `GroupBy` parameter.

    #   * A single filter for any other dimension in this dimension group.
    filter: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotAuthorizedException(ShapeBase):
    """
    The user is not authorized to perform this request.
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
class ResponsePartitionKey(ShapeBase):
    """
    If `PartitionBy` was specified in a `DescribeDimensionKeys` request, the
    dimensions are returned in an array. Each element in the array specifies one
    dimension.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # A dimension map that contains the dimension(s) for this partition.
    dimensions: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResponseResourceMetricKey(ShapeBase):
    """
    An object describing a Performance Insights metric and one or more dimensions
    for that metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric",
                "Metric",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of a Performance Insights metric to be measured.

    # Valid values for `Metric` are:

    #   * `db.load.avg` \- a scaled representation of the number of active sessions for the database engine.

    #   * `db.sampledload.avg` \- the raw number of active sessions for the database engine.
    metric: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The valid dimensions for the metric.
    dimensions: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ServiceType(str):
    RDS = "RDS"
