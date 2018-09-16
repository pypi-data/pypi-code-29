import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudwatch", *args, **kwargs)

    def delete_alarms(
        self,
        _request: shapes.DeleteAlarmsInput = None,
        *,
        alarm_names: typing.List[str],
    ) -> None:
        """
        Deletes the specified alarms. In the event of an error, no alarms are deleted.
        """
        if _request is None:
            _params = {}
            if alarm_names is not ShapeBase.NOT_SET:
                _params['alarm_names'] = alarm_names
            _request = shapes.DeleteAlarmsInput(**_params)
        response = self._boto_client.delete_alarms(**_request.to_boto())

    def delete_dashboards(
        self,
        _request: shapes.DeleteDashboardsInput = None,
        *,
        dashboard_names: typing.List[str],
    ) -> shapes.DeleteDashboardsOutput:
        """
        Deletes all dashboards that you specify. You may specify up to 100 dashboards to
        delete. If there is an error during this call, no dashboards are deleted.
        """
        if _request is None:
            _params = {}
            if dashboard_names is not ShapeBase.NOT_SET:
                _params['dashboard_names'] = dashboard_names
            _request = shapes.DeleteDashboardsInput(**_params)
        response = self._boto_client.delete_dashboards(**_request.to_boto())

        return shapes.DeleteDashboardsOutput.from_boto(response)

    def describe_alarm_history(
        self,
        _request: shapes.DescribeAlarmHistoryInput = None,
        *,
        alarm_name: str = ShapeBase.NOT_SET,
        history_item_type: typing.Union[str, shapes.
                                        HistoryItemType] = ShapeBase.NOT_SET,
        start_date: datetime.datetime = ShapeBase.NOT_SET,
        end_date: datetime.datetime = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAlarmHistoryOutput:
        """
        Retrieves the history for the specified alarm. You can filter the results by
        date range or item type. If an alarm name is not specified, the histories for
        all alarms are returned.

        CloudWatch retains the history of an alarm even if you delete the alarm.
        """
        if _request is None:
            _params = {}
            if alarm_name is not ShapeBase.NOT_SET:
                _params['alarm_name'] = alarm_name
            if history_item_type is not ShapeBase.NOT_SET:
                _params['history_item_type'] = history_item_type
            if start_date is not ShapeBase.NOT_SET:
                _params['start_date'] = start_date
            if end_date is not ShapeBase.NOT_SET:
                _params['end_date'] = end_date
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAlarmHistoryInput(**_params)
        paginator = self.get_paginator("describe_alarm_history").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeAlarmHistoryOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeAlarmHistoryOutput.from_boto(response)

    def describe_alarms(
        self,
        _request: shapes.DescribeAlarmsInput = None,
        *,
        alarm_names: typing.List[str] = ShapeBase.NOT_SET,
        alarm_name_prefix: str = ShapeBase.NOT_SET,
        state_value: typing.Union[str, shapes.StateValue] = ShapeBase.NOT_SET,
        action_prefix: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAlarmsOutput:
        """
        Retrieves the specified alarms. If no alarms are specified, all alarms are
        returned. Alarms can be retrieved by using only a prefix for the alarm name, the
        alarm state, or a prefix for any action.
        """
        if _request is None:
            _params = {}
            if alarm_names is not ShapeBase.NOT_SET:
                _params['alarm_names'] = alarm_names
            if alarm_name_prefix is not ShapeBase.NOT_SET:
                _params['alarm_name_prefix'] = alarm_name_prefix
            if state_value is not ShapeBase.NOT_SET:
                _params['state_value'] = state_value
            if action_prefix is not ShapeBase.NOT_SET:
                _params['action_prefix'] = action_prefix
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAlarmsInput(**_params)
        paginator = self.get_paginator("describe_alarms").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeAlarmsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeAlarmsOutput.from_boto(response)

    def describe_alarms_for_metric(
        self,
        _request: shapes.DescribeAlarmsForMetricInput = None,
        *,
        metric_name: str,
        namespace: str,
        statistic: typing.Union[str, shapes.Statistic] = ShapeBase.NOT_SET,
        extended_statistic: str = ShapeBase.NOT_SET,
        dimensions: typing.List[shapes.Dimension] = ShapeBase.NOT_SET,
        period: int = ShapeBase.NOT_SET,
        unit: typing.Union[str, shapes.StandardUnit] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAlarmsForMetricOutput:
        """
        Retrieves the alarms for the specified metric. To filter the results, specify a
        statistic, period, or unit.
        """
        if _request is None:
            _params = {}
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if namespace is not ShapeBase.NOT_SET:
                _params['namespace'] = namespace
            if statistic is not ShapeBase.NOT_SET:
                _params['statistic'] = statistic
            if extended_statistic is not ShapeBase.NOT_SET:
                _params['extended_statistic'] = extended_statistic
            if dimensions is not ShapeBase.NOT_SET:
                _params['dimensions'] = dimensions
            if period is not ShapeBase.NOT_SET:
                _params['period'] = period
            if unit is not ShapeBase.NOT_SET:
                _params['unit'] = unit
            _request = shapes.DescribeAlarmsForMetricInput(**_params)
        response = self._boto_client.describe_alarms_for_metric(
            **_request.to_boto()
        )

        return shapes.DescribeAlarmsForMetricOutput.from_boto(response)

    def disable_alarm_actions(
        self,
        _request: shapes.DisableAlarmActionsInput = None,
        *,
        alarm_names: typing.List[str],
    ) -> None:
        """
        Disables the actions for the specified alarms. When an alarm's actions are
        disabled, the alarm actions do not execute when the alarm state changes.
        """
        if _request is None:
            _params = {}
            if alarm_names is not ShapeBase.NOT_SET:
                _params['alarm_names'] = alarm_names
            _request = shapes.DisableAlarmActionsInput(**_params)
        response = self._boto_client.disable_alarm_actions(**_request.to_boto())

    def enable_alarm_actions(
        self,
        _request: shapes.EnableAlarmActionsInput = None,
        *,
        alarm_names: typing.List[str],
    ) -> None:
        """
        Enables the actions for the specified alarms.
        """
        if _request is None:
            _params = {}
            if alarm_names is not ShapeBase.NOT_SET:
                _params['alarm_names'] = alarm_names
            _request = shapes.EnableAlarmActionsInput(**_params)
        response = self._boto_client.enable_alarm_actions(**_request.to_boto())

    def get_dashboard(
        self,
        _request: shapes.GetDashboardInput = None,
        *,
        dashboard_name: str,
    ) -> shapes.GetDashboardOutput:
        """
        Displays the details of the dashboard that you specify.

        To copy an existing dashboard, use `GetDashboard`, and then use the data
        returned within `DashboardBody` as the template for the new dashboard when you
        call `PutDashboard` to create the copy.
        """
        if _request is None:
            _params = {}
            if dashboard_name is not ShapeBase.NOT_SET:
                _params['dashboard_name'] = dashboard_name
            _request = shapes.GetDashboardInput(**_params)
        response = self._boto_client.get_dashboard(**_request.to_boto())

        return shapes.GetDashboardOutput.from_boto(response)

    def get_metric_data(
        self,
        _request: shapes.GetMetricDataInput = None,
        *,
        metric_data_queries: typing.List[shapes.MetricDataQuery],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        next_token: str = ShapeBase.NOT_SET,
        scan_by: typing.Union[str, shapes.ScanBy] = ShapeBase.NOT_SET,
        max_datapoints: int = ShapeBase.NOT_SET,
    ) -> shapes.GetMetricDataOutput:
        """
        You can use the `GetMetricData` API to retrieve as many as 100 different metrics
        in a single request, with a total of as many as 100,800 datapoints. You can also
        optionally perform math expressions on the values of the returned statistics, to
        create new time series that represent new insights into your data. For example,
        using Lambda metrics, you could divide the Errors metric by the Invocations
        metric to get an error rate time series. For more information about metric math
        expressions, see [Metric Math Syntax and
        Functions](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-
        metric-math.html#metric-math-syntax) in the _Amazon CloudWatch User Guide_.

        Calls to the `GetMetricData` API have a different pricing structure than calls
        to `GetMetricStatistics`. For more information about pricing, see [Amazon
        CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).
        """
        if _request is None:
            _params = {}
            if metric_data_queries is not ShapeBase.NOT_SET:
                _params['metric_data_queries'] = metric_data_queries
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if scan_by is not ShapeBase.NOT_SET:
                _params['scan_by'] = scan_by
            if max_datapoints is not ShapeBase.NOT_SET:
                _params['max_datapoints'] = max_datapoints
            _request = shapes.GetMetricDataInput(**_params)
        response = self._boto_client.get_metric_data(**_request.to_boto())

        return shapes.GetMetricDataOutput.from_boto(response)

    def get_metric_statistics(
        self,
        _request: shapes.GetMetricStatisticsInput = None,
        *,
        namespace: str,
        metric_name: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        period: int,
        dimensions: typing.List[shapes.Dimension] = ShapeBase.NOT_SET,
        statistics: typing.List[typing.Union[str, shapes.Statistic]
                               ] = ShapeBase.NOT_SET,
        extended_statistics: typing.List[str] = ShapeBase.NOT_SET,
        unit: typing.Union[str, shapes.StandardUnit] = ShapeBase.NOT_SET,
    ) -> shapes.GetMetricStatisticsOutput:
        """
        Gets statistics for the specified metric.

        The maximum number of data points returned from a single call is 1,440. If you
        request more than 1,440 data points, CloudWatch returns an error. To reduce the
        number of data points, you can narrow the specified time range and make multiple
        requests across adjacent time ranges, or you can increase the specified period.
        Data points are not returned in chronological order.

        CloudWatch aggregates data points based on the length of the period that you
        specify. For example, if you request statistics with a one-hour period,
        CloudWatch aggregates all data points with time stamps that fall within each
        one-hour period. Therefore, the number of values aggregated by CloudWatch is
        larger than the number of data points returned.

        CloudWatch needs raw data points to calculate percentile statistics. If you
        publish data using a statistic set instead, you can only retrieve percentile
        statistics for this data if one of the following conditions is true:

          * The SampleCount value of the statistic set is 1.

          * The Min and the Max values of the statistic set are equal.

        Amazon CloudWatch retains metric data as follows:

          * Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a `StorageResolution` of 1.

          * Data points with a period of 60 seconds (1-minute) are available for 15 days.

          * Data points with a period of 300 seconds (5-minute) are available for 63 days.

          * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).

        Data points that are initially published with a shorter period are aggregated
        together for long-term storage. For example, if you collect data using a period
        of 1 minute, the data remains available for 15 days with 1-minute resolution.
        After 15 days, this data is still available, but is aggregated and retrievable
        only with a resolution of 5 minutes. After 63 days, the data is further
        aggregated and is available with a resolution of 1 hour.

        CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.

        For information about metrics and dimensions supported by AWS services, see the
        [Amazon CloudWatch Metrics and Dimensions
        Reference](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
        in the _Amazon CloudWatch User Guide_.
        """
        if _request is None:
            _params = {}
            if namespace is not ShapeBase.NOT_SET:
                _params['namespace'] = namespace
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if period is not ShapeBase.NOT_SET:
                _params['period'] = period
            if dimensions is not ShapeBase.NOT_SET:
                _params['dimensions'] = dimensions
            if statistics is not ShapeBase.NOT_SET:
                _params['statistics'] = statistics
            if extended_statistics is not ShapeBase.NOT_SET:
                _params['extended_statistics'] = extended_statistics
            if unit is not ShapeBase.NOT_SET:
                _params['unit'] = unit
            _request = shapes.GetMetricStatisticsInput(**_params)
        response = self._boto_client.get_metric_statistics(**_request.to_boto())

        return shapes.GetMetricStatisticsOutput.from_boto(response)

    def list_dashboards(
        self,
        _request: shapes.ListDashboardsInput = None,
        *,
        dashboard_name_prefix: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDashboardsOutput:
        """
        Returns a list of the dashboards for your account. If you include
        `DashboardNamePrefix`, only those dashboards with names starting with the prefix
        are listed. Otherwise, all dashboards in your account are listed.
        """
        if _request is None:
            _params = {}
            if dashboard_name_prefix is not ShapeBase.NOT_SET:
                _params['dashboard_name_prefix'] = dashboard_name_prefix
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDashboardsInput(**_params)
        paginator = self.get_paginator("list_dashboards").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDashboardsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDashboardsOutput.from_boto(response)

    def list_metrics(
        self,
        _request: shapes.ListMetricsInput = None,
        *,
        namespace: str = ShapeBase.NOT_SET,
        metric_name: str = ShapeBase.NOT_SET,
        dimensions: typing.List[shapes.DimensionFilter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListMetricsOutput:
        """
        List the specified metrics. You can use the returned metrics with
        GetMetricStatistics to obtain statistical data.

        Up to 500 results are returned for any one call. To retrieve additional results,
        use the returned token with subsequent calls.

        After you create a metric, allow up to fifteen minutes before the metric
        appears. Statistics about the metric, however, are available sooner using
        GetMetricStatistics.
        """
        if _request is None:
            _params = {}
            if namespace is not ShapeBase.NOT_SET:
                _params['namespace'] = namespace
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if dimensions is not ShapeBase.NOT_SET:
                _params['dimensions'] = dimensions
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListMetricsInput(**_params)
        paginator = self.get_paginator("list_metrics").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListMetricsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListMetricsOutput.from_boto(response)

    def put_dashboard(
        self,
        _request: shapes.PutDashboardInput = None,
        *,
        dashboard_name: str,
        dashboard_body: str,
    ) -> shapes.PutDashboardOutput:
        """
        Creates a dashboard if it does not already exist, or updates an existing
        dashboard. If you update a dashboard, the entire contents are replaced with what
        you specify here.

        You can have up to 500 dashboards per account. All dashboards in your account
        are global, not region-specific.

        A simple way to create a dashboard using `PutDashboard` is to copy an existing
        dashboard. To copy an existing dashboard using the console, you can load the
        dashboard and then use the View/edit source command in the Actions menu to
        display the JSON block for that dashboard. Another way to copy a dashboard is to
        use `GetDashboard`, and then use the data returned within `DashboardBody` as the
        template for the new dashboard when you call `PutDashboard`.

        When you create a dashboard with `PutDashboard`, a good practice is to add a
        text widget at the top of the dashboard with a message that the dashboard was
        created by script and should not be changed in the console. This message could
        also point console users to the location of the `DashboardBody` script or the
        CloudFormation template used to create the dashboard.
        """
        if _request is None:
            _params = {}
            if dashboard_name is not ShapeBase.NOT_SET:
                _params['dashboard_name'] = dashboard_name
            if dashboard_body is not ShapeBase.NOT_SET:
                _params['dashboard_body'] = dashboard_body
            _request = shapes.PutDashboardInput(**_params)
        response = self._boto_client.put_dashboard(**_request.to_boto())

        return shapes.PutDashboardOutput.from_boto(response)

    def put_metric_alarm(
        self,
        _request: shapes.PutMetricAlarmInput = None,
        *,
        alarm_name: str,
        metric_name: str,
        namespace: str,
        period: int,
        evaluation_periods: int,
        threshold: float,
        comparison_operator: typing.Union[str, shapes.ComparisonOperator],
        alarm_description: str = ShapeBase.NOT_SET,
        actions_enabled: bool = ShapeBase.NOT_SET,
        ok_actions: typing.List[str] = ShapeBase.NOT_SET,
        alarm_actions: typing.List[str] = ShapeBase.NOT_SET,
        insufficient_data_actions: typing.List[str] = ShapeBase.NOT_SET,
        statistic: typing.Union[str, shapes.Statistic] = ShapeBase.NOT_SET,
        extended_statistic: str = ShapeBase.NOT_SET,
        dimensions: typing.List[shapes.Dimension] = ShapeBase.NOT_SET,
        unit: typing.Union[str, shapes.StandardUnit] = ShapeBase.NOT_SET,
        datapoints_to_alarm: int = ShapeBase.NOT_SET,
        treat_missing_data: str = ShapeBase.NOT_SET,
        evaluate_low_sample_count_percentile: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates or updates an alarm and associates it with the specified metric.
        Optionally, this operation can associate one or more Amazon SNS resources with
        the alarm.

        When this operation creates an alarm, the alarm state is immediately set to
        `INSUFFICIENT_DATA`. The alarm is evaluated and its state is set appropriately.
        Any actions associated with the state are then executed.

        When you update an existing alarm, its state is left unchanged, but the update
        completely overwrites the previous configuration of the alarm.

        If you are an IAM user, you must have Amazon EC2 permissions for some
        operations:

          * `iam:CreateServiceLinkedRole` for all alarms with EC2 actions

          * `ec2:DescribeInstanceStatus` and `ec2:DescribeInstances` for all alarms on EC2 instance status metrics

          * `ec2:StopInstances` for alarms with stop actions

          * `ec2:TerminateInstances` for alarms with terminate actions

          * `ec2:DescribeInstanceRecoveryAttribute` and `ec2:RecoverInstances` for alarms with recover actions

        If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2,
        you can still create an alarm, but the stop or terminate actions are not
        performed. However, if you are later granted the required permissions, the alarm
        actions that you created earlier are performed.

        If you are using an IAM role (for example, an EC2 instance profile), you cannot
        stop or terminate the instance using alarm actions. However, you can still see
        the alarm state and perform any other actions such as Amazon SNS notifications
        or Auto Scaling policies.

        If you are using temporary security credentials granted using AWS STS, you
        cannot stop or terminate an EC2 instance using alarm actions.

        You must create at least one stop, terminate, or reboot alarm using either the
        Amazon EC2 or CloudWatch consoles to create the **EC2ActionsAccess** IAM role.
        After this IAM role is created, you can create stop, terminate, or reboot alarms
        using a command-line interface or API.
        """
        if _request is None:
            _params = {}
            if alarm_name is not ShapeBase.NOT_SET:
                _params['alarm_name'] = alarm_name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if namespace is not ShapeBase.NOT_SET:
                _params['namespace'] = namespace
            if period is not ShapeBase.NOT_SET:
                _params['period'] = period
            if evaluation_periods is not ShapeBase.NOT_SET:
                _params['evaluation_periods'] = evaluation_periods
            if threshold is not ShapeBase.NOT_SET:
                _params['threshold'] = threshold
            if comparison_operator is not ShapeBase.NOT_SET:
                _params['comparison_operator'] = comparison_operator
            if alarm_description is not ShapeBase.NOT_SET:
                _params['alarm_description'] = alarm_description
            if actions_enabled is not ShapeBase.NOT_SET:
                _params['actions_enabled'] = actions_enabled
            if ok_actions is not ShapeBase.NOT_SET:
                _params['ok_actions'] = ok_actions
            if alarm_actions is not ShapeBase.NOT_SET:
                _params['alarm_actions'] = alarm_actions
            if insufficient_data_actions is not ShapeBase.NOT_SET:
                _params['insufficient_data_actions'] = insufficient_data_actions
            if statistic is not ShapeBase.NOT_SET:
                _params['statistic'] = statistic
            if extended_statistic is not ShapeBase.NOT_SET:
                _params['extended_statistic'] = extended_statistic
            if dimensions is not ShapeBase.NOT_SET:
                _params['dimensions'] = dimensions
            if unit is not ShapeBase.NOT_SET:
                _params['unit'] = unit
            if datapoints_to_alarm is not ShapeBase.NOT_SET:
                _params['datapoints_to_alarm'] = datapoints_to_alarm
            if treat_missing_data is not ShapeBase.NOT_SET:
                _params['treat_missing_data'] = treat_missing_data
            if evaluate_low_sample_count_percentile is not ShapeBase.NOT_SET:
                _params['evaluate_low_sample_count_percentile'
                       ] = evaluate_low_sample_count_percentile
            _request = shapes.PutMetricAlarmInput(**_params)
        response = self._boto_client.put_metric_alarm(**_request.to_boto())

    def put_metric_data(
        self,
        _request: shapes.PutMetricDataInput = None,
        *,
        namespace: str,
        metric_data: typing.List[shapes.MetricDatum],
    ) -> None:
        """
        Publishes metric data points to Amazon CloudWatch. CloudWatch associates the
        data points with the specified metric. If the specified metric does not exist,
        CloudWatch creates the metric. When CloudWatch creates a metric, it can take up
        to fifteen minutes for the metric to appear in calls to ListMetrics.

        Each `PutMetricData` request is limited to 40 KB in size for HTTP POST requests.

        Although the `Value` parameter accepts numbers of type `Double`, CloudWatch
        rejects values that are either too small or too large. Values must be in the
        range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
        In addition, special values (for example, NaN, +Infinity, -Infinity) are not
        supported.

        You can use up to 10 dimensions per metric to further clarify what data the
        metric collects. For more information about specifying dimensions, see
        [Publishing
        Metrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
        in the _Amazon CloudWatch User Guide_.

        Data points with time stamps from 24 hours ago or longer can take at least 48
        hours to become available for GetMetricStatistics from the time they are
        submitted.

        CloudWatch needs raw data points to calculate percentile statistics. If you
        publish data using a statistic set instead, you can only retrieve percentile
        statistics for this data if one of the following conditions is true:

          * The SampleCount value of the statistic set is 1

          * The Min and the Max values of the statistic set are equal
        """
        if _request is None:
            _params = {}
            if namespace is not ShapeBase.NOT_SET:
                _params['namespace'] = namespace
            if metric_data is not ShapeBase.NOT_SET:
                _params['metric_data'] = metric_data
            _request = shapes.PutMetricDataInput(**_params)
        response = self._boto_client.put_metric_data(**_request.to_boto())

    def set_alarm_state(
        self,
        _request: shapes.SetAlarmStateInput = None,
        *,
        alarm_name: str,
        state_value: typing.Union[str, shapes.StateValue],
        state_reason: str,
        state_reason_data: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Temporarily sets the state of an alarm for testing purposes. When the updated
        state differs from the previous value, the action configured for the appropriate
        state is invoked. For example, if your alarm is configured to send an Amazon SNS
        message when an alarm is triggered, temporarily changing the alarm state to
        `ALARM` sends an SNS message. The alarm returns to its actual state (often
        within seconds). Because the alarm state change happens quickly, it is typically
        only visible in the alarm's **History** tab in the Amazon CloudWatch console or
        through DescribeAlarmHistory.
        """
        if _request is None:
            _params = {}
            if alarm_name is not ShapeBase.NOT_SET:
                _params['alarm_name'] = alarm_name
            if state_value is not ShapeBase.NOT_SET:
                _params['state_value'] = state_value
            if state_reason is not ShapeBase.NOT_SET:
                _params['state_reason'] = state_reason
            if state_reason_data is not ShapeBase.NOT_SET:
                _params['state_reason_data'] = state_reason_data
            _request = shapes.SetAlarmStateInput(**_params)
        response = self._boto_client.set_alarm_state(**_request.to_boto())
