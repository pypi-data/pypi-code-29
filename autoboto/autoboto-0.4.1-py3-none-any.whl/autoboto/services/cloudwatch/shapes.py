import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AlarmHistoryItem(ShapeBase):
    """
    Represents the history of a specific alarm.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_name",
                "AlarmName",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "history_item_type",
                "HistoryItemType",
                TypeInfo(typing.Union[str, HistoryItemType]),
            ),
            (
                "history_summary",
                "HistorySummary",
                TypeInfo(str),
            ),
            (
                "history_data",
                "HistoryData",
                TypeInfo(str),
            ),
        ]

    # The descriptive name for the alarm.
    alarm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp for the alarm history item.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of alarm history item.
    history_item_type: typing.Union[str, "HistoryItemType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A summary of the alarm history, in text format.
    history_summary: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Data about the alarm, in JSON format.
    history_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ComparisonOperator(str):
    GreaterThanOrEqualToThreshold = "GreaterThanOrEqualToThreshold"
    GreaterThanThreshold = "GreaterThanThreshold"
    LessThanThreshold = "LessThanThreshold"
    LessThanOrEqualToThreshold = "LessThanOrEqualToThreshold"


@dataclasses.dataclass
class DashboardEntry(ShapeBase):
    """
    Represents a specific dashboard.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dashboard_name",
                "DashboardName",
                TypeInfo(str),
            ),
            (
                "dashboard_arn",
                "DashboardArn",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
        ]

    # The name of the dashboard.
    dashboard_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the dashboard.
    dashboard_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp of when the dashboard was last modified, either by an API
    # call or through the console. This number is expressed as the number of
    # milliseconds since Jan 1, 1970 00:00:00 UTC.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the dashboard, in bytes.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DashboardInvalidInputError(ShapeBase):
    """
    Some part of the dashboard data is invalid.
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
                "dashboard_validation_messages",
                "dashboardValidationMessages",
                TypeInfo(typing.List[DashboardValidationMessage]),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    dashboard_validation_messages: typing.List["DashboardValidationMessage"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class DashboardNotFoundError(ShapeBase):
    """
    The specified dashboard does not exist.
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
class DashboardValidationMessage(ShapeBase):
    """
    An error or warning for the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_path",
                "DataPath",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The data path related to the message.
    data_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message describing the error or warning.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Datapoint(ShapeBase):
    """
    Encapsulates the statistical data that CloudWatch computes from metric data.
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
                "sample_count",
                "SampleCount",
                TypeInfo(float),
            ),
            (
                "average",
                "Average",
                TypeInfo(float),
            ),
            (
                "sum",
                "Sum",
                TypeInfo(float),
            ),
            (
                "minimum",
                "Minimum",
                TypeInfo(float),
            ),
            (
                "maximum",
                "Maximum",
                TypeInfo(float),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
            (
                "extended_statistics",
                "ExtendedStatistics",
                TypeInfo(typing.Dict[str, float]),
            ),
        ]

    # The time stamp used for the data point.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of metric values that contributed to the aggregate value of this
    # data point.
    sample_count: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The average of the metric values that correspond to the data point.
    average: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sum of the metric values for the data point.
    sum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum metric value for the data point.
    minimum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum metric value for the data point.
    maximum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The standard unit for the data point.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The percentile statistic for the data point.
    extended_statistics: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAlarmsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_names",
                "AlarmNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The alarms to be deleted.
    alarm_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDashboardsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dashboard_names",
                "DashboardNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The dashboards to be deleted. This parameter is required.
    dashboard_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDashboardsOutput(OutputShapeBase):
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
class DescribeAlarmHistoryInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_name",
                "AlarmName",
                TypeInfo(str),
            ),
            (
                "history_item_type",
                "HistoryItemType",
                TypeInfo(typing.Union[str, HistoryItemType]),
            ),
            (
                "start_date",
                "StartDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date",
                "EndDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The name of the alarm.
    alarm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of alarm histories to retrieve.
    history_item_type: typing.Union[str, "HistoryItemType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The starting date to retrieve alarm history.
    start_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ending date to retrieve alarm history.
    end_date: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of alarm history records to retrieve.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned by a previous call to indicate that there is more data
    # available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAlarmHistoryOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "alarm_history_items",
                "AlarmHistoryItems",
                TypeInfo(typing.List[AlarmHistoryItem]),
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

    # The alarm histories, in JSON format.
    alarm_history_items: typing.List["AlarmHistoryItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token that marks the start of the next batch of returned results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeAlarmHistoryOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeAlarmsForMetricInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "statistic",
                "Statistic",
                TypeInfo(typing.Union[str, Statistic]),
            ),
            (
                "extended_statistic",
                "ExtendedStatistic",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[Dimension]),
            ),
            (
                "period",
                "Period",
                TypeInfo(int),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
        ]

    # The name of the metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the metric.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistic for the metric, other than percentiles. For percentile
    # statistics, use `ExtendedStatistics`.
    statistic: typing.Union[str, "Statistic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The percentile statistic for the metric. Specify a value between p0.0 and
    # p100.
    extended_statistic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions associated with the metric. If the metric has any associated
    # dimensions, you must specify them in order for the call to succeed.
    dimensions: typing.List["Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The period, in seconds, over which the statistic is applied.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unit for the metric.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAlarmsForMetricOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_alarms",
                "MetricAlarms",
                TypeInfo(typing.List[MetricAlarm]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information for each alarm with the specified metric.
    metric_alarms: typing.List["MetricAlarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeAlarmsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_names",
                "AlarmNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "alarm_name_prefix",
                "AlarmNamePrefix",
                TypeInfo(str),
            ),
            (
                "state_value",
                "StateValue",
                TypeInfo(typing.Union[str, StateValue]),
            ),
            (
                "action_prefix",
                "ActionPrefix",
                TypeInfo(str),
            ),
            (
                "max_records",
                "MaxRecords",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The names of the alarms.
    alarm_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The alarm name prefix. If this parameter is specified, you cannot specify
    # `AlarmNames`.
    alarm_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state value to be used in matching alarms.
    state_value: typing.Union[str, "StateValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action name prefix.
    action_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of alarm descriptions to retrieve.
    max_records: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned by a previous call to indicate that there is more data
    # available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAlarmsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_alarms",
                "MetricAlarms",
                TypeInfo(typing.List[MetricAlarm]),
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

    # The information for the specified alarms.
    metric_alarms: typing.List["MetricAlarm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token that marks the start of the next batch of returned results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeAlarmsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Dimension(ShapeBase):
    """
    Expands the identity of a metric.
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

    # The name of the dimension.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value representing the dimension measurement.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DimensionFilter(ShapeBase):
    """
    Represents filters for a dimension.
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

    # The dimension name to be matched.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the dimension to be matched.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableAlarmActionsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_names",
                "AlarmNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the alarms.
    alarm_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnableAlarmActionsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_names",
                "AlarmNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the alarms.
    alarm_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDashboardInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dashboard_name",
                "DashboardName",
                TypeInfo(str),
            ),
        ]

    # The name of the dashboard to be described.
    dashboard_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDashboardOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dashboard_arn",
                "DashboardArn",
                TypeInfo(str),
            ),
            (
                "dashboard_body",
                "DashboardBody",
                TypeInfo(str),
            ),
            (
                "dashboard_name",
                "DashboardName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the dashboard.
    dashboard_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The detailed information about the dashboard, including what widgets are
    # included and their location on the dashboard. For more information about
    # the `DashboardBody` syntax, see CloudWatch-Dashboard-Body-Structure.
    dashboard_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the dashboard.
    dashboard_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMetricDataInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_data_queries",
                "MetricDataQueries",
                TypeInfo(typing.List[MetricDataQuery]),
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "scan_by",
                "ScanBy",
                TypeInfo(typing.Union[str, ScanBy]),
            ),
            (
                "max_datapoints",
                "MaxDatapoints",
                TypeInfo(int),
            ),
        ]

    # The metric queries to be returned. A single `GetMetricData` call can
    # include as many as 100 `MetricDataQuery` structures. Each of these
    # structures can specify either a metric to retrieve, or a math expression to
    # perform on retrieved data.
    metric_data_queries: typing.List["MetricDataQuery"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp indicating the earliest data to be returned.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp indicating the latest data to be returned.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Include this value, if it was returned by the previous call, to get the
    # next set of data points.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The order in which data points should be returned. `TimestampDescending`
    # returns the newest data first and paginates when the `MaxDatapoints` limit
    # is reached. `TimestampAscending` returns the oldest data first and
    # paginates when the `MaxDatapoints` limit is reached.
    scan_by: typing.Union[str, "ScanBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of data points the request should return before
    # paginating. If you omit this, the default of 100,800 is used.
    max_datapoints: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMetricDataOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_data_results",
                "MetricDataResults",
                TypeInfo(typing.List[MetricDataResult]),
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

    # The metrics that are returned, including the metric name, namespace, and
    # dimensions.
    metric_data_results: typing.List["MetricDataResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token that marks the next batch of returned results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMetricStatisticsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
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
                "period",
                "Period",
                TypeInfo(int),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[Dimension]),
            ),
            (
                "statistics",
                "Statistics",
                TypeInfo(typing.List[typing.Union[str, Statistic]]),
            ),
            (
                "extended_statistics",
                "ExtendedStatistics",
                TypeInfo(typing.List[str]),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
        ]

    # The namespace of the metric, with or without spaces.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the metric, with or without spaces.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp that determines the first data point to return. Start times
    # are evaluated relative to the time that CloudWatch receives the request.

    # The value specified is inclusive; results include data points with the
    # specified time stamp. The time stamp must be in ISO 8601 UTC format (for
    # example, 2016-10-03T23:00:00Z).

    # CloudWatch rounds the specified time stamp as follows:

    #   * Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.

    #   * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.

    #   * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.

    # If you set `Period` to 5, 10, or 30, the start time of your request is
    # rounded down to the nearest time that corresponds to even 5-, 10-, or
    # 30-second divisions of a minute. For example, if you make a query at
    # (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of
    # your request is rounded down and you receive data from 01:05:10 to
    # 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of
    # data, using a period of 5 seconds, you receive data timestamped between
    # 15:02:15 and 15:07:15.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time stamp that determines the last data point to return.

    # The value specified is exclusive; results include data points up to the
    # specified time stamp. The time stamp must be in ISO 8601 UTC format (for
    # example, 2016-10-10T23:00:00Z).
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The granularity, in seconds, of the returned data points. For metrics with
    # regular resolution, a period can be as short as one minute (60 seconds) and
    # must be a multiple of 60. For high-resolution metrics that are collected at
    # intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or
    # any multiple of 60. High-resolution metrics are those metrics stored by a
    # `PutMetricData` call that includes a `StorageResolution` of 1 second.

    # If the `StartTime` parameter specifies a time stamp that is greater than 3
    # hours ago, you must specify the period as follows or no data points in that
    # time range is returned:

    #   * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).

    #   * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

    #   * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions. If the metric contains multiple dimensions, you must
    # include a value for each dimension. CloudWatch treats each unique
    # combination of dimensions as a separate metric. If a specific combination
    # of dimensions was not published, you can't retrieve statistics for it. You
    # must specify the same dimensions that were used when the metrics were
    # created. For an example, see [Dimension
    # Combinations](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-
    # combinations) in the _Amazon CloudWatch User Guide_. For more information
    # about specifying dimensions, see [Publishing
    # Metrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
    # in the _Amazon CloudWatch User Guide_.
    dimensions: typing.List["Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metric statistics, other than percentile. For percentile statistics,
    # use `ExtendedStatistics`. When calling `GetMetricStatistics`, you must
    # specify either `Statistics` or `ExtendedStatistics`, but not both.
    statistics: typing.List[typing.Union[str, "Statistic"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The percentile statistics. Specify values between p0.0 and p100. When
    # calling `GetMetricStatistics`, you must specify either `Statistics` or
    # `ExtendedStatistics`, but not both.
    extended_statistics: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unit for a given metric. Metrics may be reported in multiple units. Not
    # supplying a unit results in all units being returned. If you specify only a
    # unit that the metric does not report, the results of the call are null.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMetricStatisticsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "datapoints",
                "Datapoints",
                TypeInfo(typing.List[Datapoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A label for the specified metric.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data points for the specified metric.
    datapoints: typing.List["Datapoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HistoryItemType(str):
    ConfigurationUpdate = "ConfigurationUpdate"
    StateUpdate = "StateUpdate"
    Action = "Action"


@dataclasses.dataclass
class InternalServiceFault(ShapeBase):
    """
    Request processing has failed due to some unknown error, exception, or failure.
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
class InvalidFormatFault(ShapeBase):
    """
    Data was not syntactically valid JSON.
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
class InvalidNextToken(ShapeBase):
    """
    The next token specified is invalid.
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
class InvalidParameterCombinationException(ShapeBase):
    """
    Parameters were used together that cannot be used together.
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
class InvalidParameterValueException(ShapeBase):
    """
    The value of an input parameter is bad or out-of-range.
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
class LimitExceededFault(ShapeBase):
    """
    The quota for alarms for this customer has already been reached.
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
class ListDashboardsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dashboard_name_prefix",
                "DashboardNamePrefix",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # If you specify this parameter, only the dashboards with names starting with
    # the specified string are listed. The maximum length is 255, and valid
    # characters are A-Z, a-z, 0-9, ".", "-", and "_".
    dashboard_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token returned by a previous call to indicate that there is more data
    # available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDashboardsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dashboard_entries",
                "DashboardEntries",
                TypeInfo(typing.List[DashboardEntry]),
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

    # The list of matching dashboards.
    dashboard_entries: typing.List["DashboardEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token that marks the start of the next batch of returned results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDashboardsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListMetricsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[DimensionFilter]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The namespace to filter against.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the metric to filter against.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions to filter against.
    dimensions: typing.List["DimensionFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token returned by a previous call to indicate that there is more data
    # available.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMetricsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.List[Metric]),
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

    # The metrics.
    metrics: typing.List["Metric"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token that marks the start of the next batch of returned results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListMetricsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MessageData(ShapeBase):
    """
    A message returned by the `GetMetricData`API, including a code and a
    description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The error code or status code associated with the message.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message text.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Metric(ShapeBase):
    """
    Represents a specific metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[Dimension]),
            ),
        ]

    # The namespace of the metric.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions for the metric.
    dimensions: typing.List["Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricAlarm(ShapeBase):
    """
    Represents an alarm.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_name",
                "AlarmName",
                TypeInfo(str),
            ),
            (
                "alarm_arn",
                "AlarmArn",
                TypeInfo(str),
            ),
            (
                "alarm_description",
                "AlarmDescription",
                TypeInfo(str),
            ),
            (
                "alarm_configuration_updated_timestamp",
                "AlarmConfigurationUpdatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "actions_enabled",
                "ActionsEnabled",
                TypeInfo(bool),
            ),
            (
                "ok_actions",
                "OKActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "alarm_actions",
                "AlarmActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "insufficient_data_actions",
                "InsufficientDataActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "state_value",
                "StateValue",
                TypeInfo(typing.Union[str, StateValue]),
            ),
            (
                "state_reason",
                "StateReason",
                TypeInfo(str),
            ),
            (
                "state_reason_data",
                "StateReasonData",
                TypeInfo(str),
            ),
            (
                "state_updated_timestamp",
                "StateUpdatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "statistic",
                "Statistic",
                TypeInfo(typing.Union[str, Statistic]),
            ),
            (
                "extended_statistic",
                "ExtendedStatistic",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[Dimension]),
            ),
            (
                "period",
                "Period",
                TypeInfo(int),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
            (
                "evaluation_periods",
                "EvaluationPeriods",
                TypeInfo(int),
            ),
            (
                "datapoints_to_alarm",
                "DatapointsToAlarm",
                TypeInfo(int),
            ),
            (
                "threshold",
                "Threshold",
                TypeInfo(float),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperator]),
            ),
            (
                "treat_missing_data",
                "TreatMissingData",
                TypeInfo(str),
            ),
            (
                "evaluate_low_sample_count_percentile",
                "EvaluateLowSampleCountPercentile",
                TypeInfo(str),
            ),
        ]

    # The name of the alarm.
    alarm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the alarm.
    alarm_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the alarm.
    alarm_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp of the last update to the alarm configuration.
    alarm_configuration_updated_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether actions should be executed during any changes to the
    # alarm state.
    actions_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions to execute when this alarm transitions to the `OK` state from
    # any other state. Each action is specified as an Amazon Resource Name (ARN).
    ok_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions to execute when this alarm transitions to the `ALARM` state
    # from any other state. Each action is specified as an Amazon Resource Name
    # (ARN).
    alarm_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions to execute when this alarm transitions to the
    # `INSUFFICIENT_DATA` state from any other state. Each action is specified as
    # an Amazon Resource Name (ARN).
    insufficient_data_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state value for the alarm.
    state_value: typing.Union[str, "StateValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An explanation for the alarm state, in text format.
    state_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An explanation for the alarm state, in JSON format.
    state_reason_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp of the last update to the alarm state.
    state_updated_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the metric associated with the alarm.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace of the metric associated with the alarm.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistic for the metric associated with the alarm, other than
    # percentile. For percentile statistics, use `ExtendedStatistic`.
    statistic: typing.Union[str, "Statistic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The percentile statistic for the metric associated with the alarm. Specify
    # a value between p0.0 and p100.
    extended_statistic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions for the metric associated with the alarm.
    dimensions: typing.List["Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The period, in seconds, over which the statistic is applied.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unit of the metric associated with the alarm.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of periods over which data is compared to the specified
    # threshold.
    evaluation_periods: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of datapoints that must be breaching to trigger the alarm.
    datapoints_to_alarm: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value to compare with the specified statistic.
    threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The arithmetic operation to use when comparing the specified statistic and
    # threshold. The specified statistic value is used as the first operand.
    comparison_operator: typing.Union[str, "ComparisonOperator"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Sets how this alarm is to handle missing data points. If this parameter is
    # omitted, the default behavior of `missing` is used.
    treat_missing_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used only for alarms based on percentiles. If `ignore`, the alarm state
    # does not change during periods with too few data points to be statistically
    # significant. If `evaluate` or this parameter is not used, the alarm is
    # always evaluated and possibly changes state no matter how many data points
    # are available.
    evaluate_low_sample_count_percentile: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricDataQuery(ShapeBase):
    """
    This structure indicates the metric data to return, and whether this call is
    just retrieving a batch set of data for one metric, or is performing a math
    expression on metric data. A single `GetMetricData` call can include up to 100
    `MetricDataQuery` structures.
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
                "metric_stat",
                "MetricStat",
                TypeInfo(MetricStat),
            ),
            (
                "expression",
                "Expression",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "return_data",
                "ReturnData",
                TypeInfo(bool),
            ),
        ]

    # A short name used to tie this structure to the results in the response.
    # This name must be unique within a single call to `GetMetricData`. If you
    # are performing math expressions on this set of data, this name represents
    # that data and can serve as a variable in the mathematical expression. The
    # valid characters are letters, numbers, and underscore. The first character
    # must be a lowercase letter.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metric to be returned, along with statistics, period, and units. Use
    # this parameter only if this structure is performing a data retrieval and
    # not performing a math expression on the returned data.

    # Within one MetricDataQuery structure, you must specify either `Expression`
    # or `MetricStat` but not both.
    metric_stat: "MetricStat" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The math expression to be performed on the returned data, if this structure
    # is performing a math expression. For more information about metric math
    # expressions, see [Metric Math Syntax and
    # Functions](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-
    # metric-math.html#metric-math-syntax) in the _Amazon CloudWatch User Guide_.

    # Within one MetricDataQuery structure, you must specify either `Expression`
    # or `MetricStat` but not both.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A human-readable label for this metric or expression. This is especially
    # useful if this is an expression, so that you know what the value
    # represents. If the metric or expression is shown in a CloudWatch dashboard
    # widget, the label is shown. If Label is omitted, CloudWatch generates a
    # default.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether to return the time stamps and raw data values of this
    # metric. If you are performing this call just to do math expressions and do
    # not also need the raw data returned, you can specify `False`. If you omit
    # this, the default of `True` is used.
    return_data: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDataResult(ShapeBase):
    """
    A `GetMetricData` call returns an array of `MetricDataResult` structures. Each
    of these structures includes the data points for that metric, along with the
    time stamps of those data points and other identifying information.
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
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "timestamps",
                "Timestamps",
                TypeInfo(typing.List[datetime.datetime]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[float]),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(typing.Union[str, StatusCode]),
            ),
            (
                "messages",
                "Messages",
                TypeInfo(typing.List[MessageData]),
            ),
        ]

    # The short name you specified to represent this metric.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The human-readable label associated with the data.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamps for the data points, formatted in Unix timestamp format.
    # The number of time stamps always matches the number of values and the value
    # for Timestamps[x] is Values[x].
    timestamps: typing.List[datetime.datetime] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data points for the metric corresponding to `Timestamps`. The number of
    # values always matches the number of time stamps and the time stamp for
    # Values[x] is Timestamps[x].
    values: typing.List[float] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the returned data. `Complete` indicates that all data points
    # in the requested time range were returned. `PartialData` means that an
    # incomplete set of data points were returned. You can use the `NextToken`
    # value that was returned and repeat your request to get more data points.
    # `NextToken` is not returned if you are performing a math expression.
    # `InternalError` indicates that an error occurred. Retry your request using
    # `NextToken`, if present.
    status_code: typing.Union[str, "StatusCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of messages with additional information about the data returned.
    messages: typing.List["MessageData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MetricDatum(ShapeBase):
    """
    Encapsulates the information sent to either create a metric or add new values to
    be aggregated into an existing metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[Dimension]),
            ),
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
            (
                "statistic_values",
                "StatisticValues",
                TypeInfo(StatisticSet),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
            (
                "storage_resolution",
                "StorageResolution",
                TypeInfo(int),
            ),
        ]

    # The name of the metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions associated with the metric.
    dimensions: typing.List["Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time the metric data was received, expressed as the number of
    # milliseconds since Jan 1, 1970 00:00:00 UTC.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value for the metric.

    # Although the parameter accepts numbers of type Double, CloudWatch rejects
    # values that are either too small or too large. Values must be in the range
    # of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In
    # addition, special values (for example, NaN, +Infinity, -Infinity) are not
    # supported.
    value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistical values for the metric.
    statistic_values: "StatisticSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unit of the metric.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Valid values are 1 and 60. Setting this to 1 specifies this metric as a
    # high-resolution metric, so that CloudWatch stores the metric with sub-
    # minute resolution down to one second. Setting this to 60 specifies this
    # metric as a regular-resolution metric, which CloudWatch stores at 1-minute
    # resolution. Currently, high resolution is available only for custom
    # metrics. For more information about high-resolution metrics, see [High-
    # Resolution
    # Metrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-
    # resolution-metrics) in the _Amazon CloudWatch User Guide_.

    # This field is optional, if you do not specify it the default of 60 is used.
    storage_resolution: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricStat(ShapeBase):
    """
    This structure defines the metric to be returned, along with the statistics,
    period, and units.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric",
                "Metric",
                TypeInfo(Metric),
            ),
            (
                "period",
                "Period",
                TypeInfo(int),
            ),
            (
                "stat",
                "Stat",
                TypeInfo(str),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
        ]

    # The metric to return, including the metric name, namespace, and dimensions.
    metric: "Metric" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The period to use when retrieving the metric.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The statistic to return. It can include any CloudWatch statistic or
    # extended statistic.
    stat: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unit to use for the returned data points.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MissingRequiredParameterException(ShapeBase):
    """
    An input parameter that is required is missing.
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
class PutDashboardInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dashboard_name",
                "DashboardName",
                TypeInfo(str),
            ),
            (
                "dashboard_body",
                "DashboardBody",
                TypeInfo(str),
            ),
        ]

    # The name of the dashboard. If a dashboard with this name already exists,
    # this call modifies that dashboard, replacing its current contents.
    # Otherwise, a new dashboard is created. The maximum length is 255, and valid
    # characters are A-Z, a-z, 0-9, "-", and "_". This parameter is required.
    dashboard_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The detailed information about the dashboard in JSON format, including the
    # widgets to include and their location on the dashboard. This parameter is
    # required.

    # For more information about the syntax, see CloudWatch-Dashboard-Body-
    # Structure.
    dashboard_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutDashboardOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dashboard_validation_messages",
                "DashboardValidationMessages",
                TypeInfo(typing.List[DashboardValidationMessage]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the input for `PutDashboard` was correct and the dashboard was
    # successfully created or modified, this result is empty.

    # If this result includes only warning messages, then the input was valid
    # enough for the dashboard to be created or modified, but some elements of
    # the dashboard may not render.

    # If this result includes error messages, the input was not valid and the
    # operation failed.
    dashboard_validation_messages: typing.List["DashboardValidationMessage"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class PutMetricAlarmInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_name",
                "AlarmName",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "period",
                "Period",
                TypeInfo(int),
            ),
            (
                "evaluation_periods",
                "EvaluationPeriods",
                TypeInfo(int),
            ),
            (
                "threshold",
                "Threshold",
                TypeInfo(float),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperator]),
            ),
            (
                "alarm_description",
                "AlarmDescription",
                TypeInfo(str),
            ),
            (
                "actions_enabled",
                "ActionsEnabled",
                TypeInfo(bool),
            ),
            (
                "ok_actions",
                "OKActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "alarm_actions",
                "AlarmActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "insufficient_data_actions",
                "InsufficientDataActions",
                TypeInfo(typing.List[str]),
            ),
            (
                "statistic",
                "Statistic",
                TypeInfo(typing.Union[str, Statistic]),
            ),
            (
                "extended_statistic",
                "ExtendedStatistic",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[Dimension]),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(typing.Union[str, StandardUnit]),
            ),
            (
                "datapoints_to_alarm",
                "DatapointsToAlarm",
                TypeInfo(int),
            ),
            (
                "treat_missing_data",
                "TreatMissingData",
                TypeInfo(str),
            ),
            (
                "evaluate_low_sample_count_percentile",
                "EvaluateLowSampleCountPercentile",
                TypeInfo(str),
            ),
        ]

    # The name for the alarm. This name must be unique within the AWS account.
    alarm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the metric associated with the alarm.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The namespace for the metric associated with the alarm.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The period, in seconds, over which the specified statistic is applied.
    # Valid values are 10, 30, and any multiple of 60.

    # Be sure to specify 10 or 30 only for metrics that are stored by a
    # `PutMetricData` call with a `StorageResolution` of 1. If you specify a
    # period of 10 or 30 for a metric that does not have sub-minute resolution,
    # the alarm still attempts to gather data at the period rate that you
    # specify. In this case, it does not receive data for the attempts that do
    # not correspond to a one-minute data resolution, and the alarm may often
    # lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this
    # alarm as a high-resolution alarm, which has a higher charge than other
    # alarms. For more information about pricing, see [Amazon CloudWatch
    # Pricing](https://aws.amazon.com/cloudwatch/pricing/).

    # An alarm's total current evaluation period can be no longer than one day,
    # so `Period` multiplied by `EvaluationPeriods` cannot be more than 86,400
    # seconds.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of periods over which data is compared to the specified
    # threshold. If you are setting an alarm which requires that a number of
    # consecutive data points be breaching to trigger the alarm, this value
    # specifies that number. If you are setting an "M out of N" alarm, this value
    # is the N.

    # An alarm's total current evaluation period can be no longer than one day,
    # so this number multiplied by `Period` cannot be more than 86,400 seconds.
    evaluation_periods: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value against which the specified statistic is compared.
    threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The arithmetic operation to use when comparing the specified statistic and
    # threshold. The specified statistic value is used as the first operand.
    comparison_operator: typing.Union[str, "ComparisonOperator"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The description for the alarm.
    alarm_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether actions should be executed during any changes to the
    # alarm state.
    actions_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actions to execute when this alarm transitions to an `OK` state from
    # any other state. Each action is specified as an Amazon Resource Name (ARN).

    # Valid Values: arn:aws:automate: _region_ :ec2:stop | arn:aws:automate:
    # _region_ :ec2:terminate | arn:aws:automate: _region_ :ec2:recover |
    # arn:aws:sns: _region_ : _account-id_ : _sns-topic-name_ |
    # arn:aws:autoscaling: _region_ : _account-id_ :scalingPolicy: _policy-id_
    # autoScalingGroupName/ _group-friendly-name_ :policyName/ _policy-friendly-
    # name_

    # Valid Values (for use with IAM roles): arn:aws:swf: _region_ :{ _account-
    # id_ }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf: _region_ :{
    # _account-id_ }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 |
    # arn:aws:swf: _region_ :{ _account-id_
    # }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    ok_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions to execute when this alarm transitions to the `ALARM` state
    # from any other state. Each action is specified as an Amazon Resource Name
    # (ARN).

    # Valid Values: arn:aws:automate: _region_ :ec2:stop | arn:aws:automate:
    # _region_ :ec2:terminate | arn:aws:automate: _region_ :ec2:recover |
    # arn:aws:sns: _region_ : _account-id_ : _sns-topic-name_ |
    # arn:aws:autoscaling: _region_ : _account-id_ :scalingPolicy: _policy-id_
    # autoScalingGroupName/ _group-friendly-name_ :policyName/ _policy-friendly-
    # name_

    # Valid Values (for use with IAM roles): arn:aws:swf: _region_ :{ _account-
    # id_ }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf: _region_ :{
    # _account-id_ }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 |
    # arn:aws:swf: _region_ :{ _account-id_
    # }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    alarm_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The actions to execute when this alarm transitions to the
    # `INSUFFICIENT_DATA` state from any other state. Each action is specified as
    # an Amazon Resource Name (ARN).

    # Valid Values: arn:aws:automate: _region_ :ec2:stop | arn:aws:automate:
    # _region_ :ec2:terminate | arn:aws:automate: _region_ :ec2:recover |
    # arn:aws:sns: _region_ : _account-id_ : _sns-topic-name_ |
    # arn:aws:autoscaling: _region_ : _account-id_ :scalingPolicy: _policy-id_
    # autoScalingGroupName/ _group-friendly-name_ :policyName/ _policy-friendly-
    # name_

    # Valid Values (for use with IAM roles): arn:aws:swf: _region_ :{ _account-
    # id_ }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf: _region_ :{
    # _account-id_ }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 |
    # arn:aws:swf: _region_ :{ _account-id_
    # }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    insufficient_data_actions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The statistic for the metric associated with the alarm, other than
    # percentile. For percentile statistics, use `ExtendedStatistic`. When you
    # call `PutMetricAlarm`, you must specify either `Statistic` or
    # `ExtendedStatistic,` but not both.
    statistic: typing.Union[str, "Statistic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The percentile statistic for the metric associated with the alarm. Specify
    # a value between p0.0 and p100. When you call `PutMetricAlarm`, you must
    # specify either `Statistic` or `ExtendedStatistic,` but not both.
    extended_statistic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dimensions for the metric associated with the alarm.
    dimensions: typing.List["Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unit of measure for the statistic. For example, the units for the
    # Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number
    # of bytes that an instance receives on all network interfaces. You can also
    # specify a unit when you create a custom metric. Units help provide
    # conceptual meaning to your data. Metric data points that specify a unit of
    # measure, such as Percent, are aggregated separately.

    # If you specify a unit, you must use a unit that is appropriate for the
    # metric. Otherwise, the CloudWatch alarm can get stuck in the `INSUFFICIENT
    # DATA` state.
    unit: typing.Union[str, "StandardUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of datapoints that must be breaching to trigger the alarm. This
    # is used only if you are setting an "M out of N" alarm. In that case, this
    # value is the M. For more information, see [Evaluating an
    # Alarm](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-
    # evaluation) in the _Amazon CloudWatch User Guide_.
    datapoints_to_alarm: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets how this alarm is to handle missing data points. If `TreatMissingData`
    # is omitted, the default behavior of `missing` is used. For more
    # information, see [Configuring How CloudWatch Alarms Treats Missing
    # Data](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-
    # and-missing-data).

    # Valid Values: `breaching | notBreaching | ignore | missing`
    treat_missing_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used only for alarms based on percentiles. If you specify `ignore`, the
    # alarm state does not change during periods with too few data points to be
    # statistically significant. If you specify `evaluate` or omit this
    # parameter, the alarm is always evaluated and possibly changes state no
    # matter how many data points are available. For more information, see
    # [Percentile-Based CloudWatch Alarms and Low Data
    # Samples](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-
    # with-low-samples).

    # Valid Values: `evaluate | ignore`
    evaluate_low_sample_count_percentile: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutMetricDataInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "namespace",
                "Namespace",
                TypeInfo(str),
            ),
            (
                "metric_data",
                "MetricData",
                TypeInfo(typing.List[MetricDatum]),
            ),
        ]

    # The namespace for the metric data.

    # You cannot specify a namespace that begins with "AWS/". Namespaces that
    # begin with "AWS/" are reserved for use by Amazon Web Services products.
    namespace: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data for the metric.
    metric_data: typing.List["MetricDatum"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFound(ShapeBase):
    """
    The named resource does not exist.
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


class ScanBy(str):
    TimestampDescending = "TimestampDescending"
    TimestampAscending = "TimestampAscending"


@dataclasses.dataclass
class SetAlarmStateInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alarm_name",
                "AlarmName",
                TypeInfo(str),
            ),
            (
                "state_value",
                "StateValue",
                TypeInfo(typing.Union[str, StateValue]),
            ),
            (
                "state_reason",
                "StateReason",
                TypeInfo(str),
            ),
            (
                "state_reason_data",
                "StateReasonData",
                TypeInfo(str),
            ),
        ]

    # The name for the alarm. This name must be unique within the AWS account.
    # The maximum length is 255 characters.
    alarm_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the state.
    state_value: typing.Union[str, "StateValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason that this alarm is set to this specific state, in text format.
    state_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason that this alarm is set to this specific state, in JSON format.
    state_reason_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StandardUnit(str):
    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


class StateValue(str):
    OK = "OK"
    ALARM = "ALARM"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class Statistic(str):
    SampleCount = "SampleCount"
    Average = "Average"
    Sum = "Sum"
    Minimum = "Minimum"
    Maximum = "Maximum"


@dataclasses.dataclass
class StatisticSet(ShapeBase):
    """
    Represents a set of statistics that describes a specific metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sample_count",
                "SampleCount",
                TypeInfo(float),
            ),
            (
                "sum",
                "Sum",
                TypeInfo(float),
            ),
            (
                "minimum",
                "Minimum",
                TypeInfo(float),
            ),
            (
                "maximum",
                "Maximum",
                TypeInfo(float),
            ),
        ]

    # The number of samples used for the statistic set.
    sample_count: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sum of values for the sample set.
    sum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum value of the sample set.
    minimum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value of the sample set.
    maximum: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class StatusCode(str):
    Complete = "Complete"
    InternalError = "InternalError"
    PartialData = "PartialData"
