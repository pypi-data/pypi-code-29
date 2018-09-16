import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("pi", *args, **kwargs)

    def describe_dimension_keys(
        self,
        _request: shapes.DescribeDimensionKeysRequest = None,
        *,
        service_type: typing.Union[str, shapes.ServiceType],
        identifier: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric: str,
        group_by: shapes.DimensionGroup,
        period_in_seconds: int = ShapeBase.NOT_SET,
        partition_by: shapes.DimensionGroup = ShapeBase.NOT_SET,
        filter: typing.Dict[str, str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDimensionKeysResponse:
        """
        For a specific time period, retrieve the top `N` dimension keys for a metric.
        """
        if _request is None:
            _params = {}
            if service_type is not ShapeBase.NOT_SET:
                _params['service_type'] = service_type
            if identifier is not ShapeBase.NOT_SET:
                _params['identifier'] = identifier
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if metric is not ShapeBase.NOT_SET:
                _params['metric'] = metric
            if group_by is not ShapeBase.NOT_SET:
                _params['group_by'] = group_by
            if period_in_seconds is not ShapeBase.NOT_SET:
                _params['period_in_seconds'] = period_in_seconds
            if partition_by is not ShapeBase.NOT_SET:
                _params['partition_by'] = partition_by
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeDimensionKeysRequest(**_params)
        response = self._boto_client.describe_dimension_keys(
            **_request.to_boto()
        )

        return shapes.DescribeDimensionKeysResponse.from_boto(response)

    def get_resource_metrics(
        self,
        _request: shapes.GetResourceMetricsRequest = None,
        *,
        service_type: typing.Union[str, shapes.ServiceType],
        identifier: str,
        metric_queries: typing.List[shapes.MetricQuery],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        period_in_seconds: int = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetResourceMetricsResponse:
        """
        Retrieve Performance Insights metrics for a set of data sources, over a time
        period. You can provide specific dimension groups and dimensions, and provide
        aggregation and filtering criteria for each group.
        """
        if _request is None:
            _params = {}
            if service_type is not ShapeBase.NOT_SET:
                _params['service_type'] = service_type
            if identifier is not ShapeBase.NOT_SET:
                _params['identifier'] = identifier
            if metric_queries is not ShapeBase.NOT_SET:
                _params['metric_queries'] = metric_queries
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if period_in_seconds is not ShapeBase.NOT_SET:
                _params['period_in_seconds'] = period_in_seconds
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetResourceMetricsRequest(**_params)
        response = self._boto_client.get_resource_metrics(**_request.to_boto())

        return shapes.GetResourceMetricsResponse.from_boto(response)
