import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ce", *args, **kwargs)

    def get_cost_and_usage(
        self,
        _request: shapes.GetCostAndUsageRequest = None,
        *,
        time_period: shapes.DateInterval = ShapeBase.NOT_SET,
        granularity: typing.Union[str, shapes.Granularity] = ShapeBase.NOT_SET,
        filter: shapes.Expression = ShapeBase.NOT_SET,
        metrics: typing.List[str] = ShapeBase.NOT_SET,
        group_by: typing.List[shapes.GroupDefinition] = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCostAndUsageResponse:
        """
        Retrieves cost and usage metrics for your account. You can specify which cost
        and usage-related metric, such as `BlendedCosts` or `UsageQuantity`, that you
        want the request to return. You can also filter and group your data by various
        dimensions, such as `SERVICE` or `AZ`, in a specific time range. For a complete
        list of valid dimensions, see the `
        [GetDimensionValues](http://docs.aws.amazon.com/aws-cost-
        management/latest/APIReference/API_GetDimensionValues.html) ` operation. Master
        accounts in an organization in AWS Organizations have access to all member
        accounts.
        """
        if _request is None:
            _params = {}
            if time_period is not ShapeBase.NOT_SET:
                _params['time_period'] = time_period
            if granularity is not ShapeBase.NOT_SET:
                _params['granularity'] = granularity
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if metrics is not ShapeBase.NOT_SET:
                _params['metrics'] = metrics
            if group_by is not ShapeBase.NOT_SET:
                _params['group_by'] = group_by
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            _request = shapes.GetCostAndUsageRequest(**_params)
        response = self._boto_client.get_cost_and_usage(**_request.to_boto())

        return shapes.GetCostAndUsageResponse.from_boto(response)

    def get_dimension_values(
        self,
        _request: shapes.GetDimensionValuesRequest = None,
        *,
        time_period: shapes.DateInterval,
        dimension: typing.Union[str, shapes.Dimension],
        search_string: str = ShapeBase.NOT_SET,
        context: typing.Union[str, shapes.Context] = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDimensionValuesResponse:
        """
        Retrieves all available filter values for a specified filter over a period of
        time. You can search the dimension values for an arbitrary string.
        """
        if _request is None:
            _params = {}
            if time_period is not ShapeBase.NOT_SET:
                _params['time_period'] = time_period
            if dimension is not ShapeBase.NOT_SET:
                _params['dimension'] = dimension
            if search_string is not ShapeBase.NOT_SET:
                _params['search_string'] = search_string
            if context is not ShapeBase.NOT_SET:
                _params['context'] = context
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            _request = shapes.GetDimensionValuesRequest(**_params)
        response = self._boto_client.get_dimension_values(**_request.to_boto())

        return shapes.GetDimensionValuesResponse.from_boto(response)

    def get_reservation_coverage(
        self,
        _request: shapes.GetReservationCoverageRequest = None,
        *,
        time_period: shapes.DateInterval,
        group_by: typing.List[shapes.GroupDefinition] = ShapeBase.NOT_SET,
        granularity: typing.Union[str, shapes.Granularity] = ShapeBase.NOT_SET,
        filter: shapes.Expression = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetReservationCoverageResponse:
        """
        Retrieves the reservation coverage for your account. This allows you to see how
        much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational
        Database Service, or Amazon Redshift usage is covered by a reservation. An
        organization's master account can see the coverage of the associated member
        accounts. For any time period, you can filter data about reservation usage by
        the following dimensions:

          * AZ

          * CACHE_ENGINE

          * DATABASE_ENGINE

          * DEPLOYMENT_OPTION

          * INSTANCE_TYPE

          * LINKED_ACCOUNT

          * OPERATING_SYSTEM

          * PLATFORM

          * REGION

          * SERVICE

          * TAG

          * TENANCY

        To determine valid values for a dimension, use the `GetDimensionValues`
        operation.
        """
        if _request is None:
            _params = {}
            if time_period is not ShapeBase.NOT_SET:
                _params['time_period'] = time_period
            if group_by is not ShapeBase.NOT_SET:
                _params['group_by'] = group_by
            if granularity is not ShapeBase.NOT_SET:
                _params['granularity'] = granularity
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            _request = shapes.GetReservationCoverageRequest(**_params)
        response = self._boto_client.get_reservation_coverage(
            **_request.to_boto()
        )

        return shapes.GetReservationCoverageResponse.from_boto(response)

    def get_reservation_purchase_recommendation(
        self,
        _request: shapes.GetReservationPurchaseRecommendationRequest = None,
        *,
        service: str,
        account_id: str = ShapeBase.NOT_SET,
        account_scope: typing.Union[str, shapes.
                                    AccountScope] = ShapeBase.NOT_SET,
        lookback_period_in_days: typing.
        Union[str, shapes.LookbackPeriodInDays] = ShapeBase.NOT_SET,
        term_in_years: typing.Union[str, shapes.
                                    TermInYears] = ShapeBase.NOT_SET,
        payment_option: typing.Union[str, shapes.
                                     PaymentOption] = ShapeBase.NOT_SET,
        service_specification: shapes.ServiceSpecification = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetReservationPurchaseRecommendationResponse:
        """
        Gets recommendations for which reservations to purchase. These recommendations
        could help you reduce your costs. Reservations provide a discounted hourly rate
        (up to 75%) compared to On-Demand pricing.

        AWS generates your recommendations by identifying your On-Demand usage during a
        specific time period and collecting your usage into categories that are eligible
        for a reservation. After AWS has these categories, it simulates every
        combination of reservations in each category of usage to identify the best
        number of each type of RI to purchase to maximize your estimated savings.

        For example, AWS automatically aggregates your EC2 Linux, shared tenancy, and c4
        family usage in the US West (Oregon) Region and recommends that you buy size-
        flexible regional reservations to apply to the c4 family usage. AWS recommends
        the smallest size instance in an instance family. This makes it easier to
        purchase a size-flexible RI. AWS also shows the equal number of normalized units
        so that you can purchase any instance size that you want. For this example, your
        RI recommendation would be for `c4.large`, because that is the smallest size
        instance in the c4 instance family.
        """
        if _request is None:
            _params = {}
            if service is not ShapeBase.NOT_SET:
                _params['service'] = service
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if account_scope is not ShapeBase.NOT_SET:
                _params['account_scope'] = account_scope
            if lookback_period_in_days is not ShapeBase.NOT_SET:
                _params['lookback_period_in_days'] = lookback_period_in_days
            if term_in_years is not ShapeBase.NOT_SET:
                _params['term_in_years'] = term_in_years
            if payment_option is not ShapeBase.NOT_SET:
                _params['payment_option'] = payment_option
            if service_specification is not ShapeBase.NOT_SET:
                _params['service_specification'] = service_specification
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            _request = shapes.GetReservationPurchaseRecommendationRequest(
                **_params
            )
        response = self._boto_client.get_reservation_purchase_recommendation(
            **_request.to_boto()
        )

        return shapes.GetReservationPurchaseRecommendationResponse.from_boto(
            response
        )

    def get_reservation_utilization(
        self,
        _request: shapes.GetReservationUtilizationRequest = None,
        *,
        time_period: shapes.DateInterval,
        group_by: typing.List[shapes.GroupDefinition] = ShapeBase.NOT_SET,
        granularity: typing.Union[str, shapes.Granularity] = ShapeBase.NOT_SET,
        filter: shapes.Expression = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetReservationUtilizationResponse:
        """
        Retrieves the reservation utilization for your account. Master accounts in an
        organization have access to member accounts. You can filter data by dimensions
        in a time period. You can use `GetDimensionValues` to determine the possible
        dimension values. Currently, you can group only by `SUBSCRIPTION_ID`.
        """
        if _request is None:
            _params = {}
            if time_period is not ShapeBase.NOT_SET:
                _params['time_period'] = time_period
            if group_by is not ShapeBase.NOT_SET:
                _params['group_by'] = group_by
            if granularity is not ShapeBase.NOT_SET:
                _params['granularity'] = granularity
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            _request = shapes.GetReservationUtilizationRequest(**_params)
        response = self._boto_client.get_reservation_utilization(
            **_request.to_boto()
        )

        return shapes.GetReservationUtilizationResponse.from_boto(response)

    def get_tags(
        self,
        _request: shapes.GetTagsRequest = None,
        *,
        time_period: shapes.DateInterval,
        search_string: str = ShapeBase.NOT_SET,
        tag_key: str = ShapeBase.NOT_SET,
        next_page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTagsResponse:
        """
        Queries for available tag keys and tag values for a specified period. You can
        search the tag values for an arbitrary string.
        """
        if _request is None:
            _params = {}
            if time_period is not ShapeBase.NOT_SET:
                _params['time_period'] = time_period
            if search_string is not ShapeBase.NOT_SET:
                _params['search_string'] = search_string
            if tag_key is not ShapeBase.NOT_SET:
                _params['tag_key'] = tag_key
            if next_page_token is not ShapeBase.NOT_SET:
                _params['next_page_token'] = next_page_token
            _request = shapes.GetTagsRequest(**_params)
        response = self._boto_client.get_tags(**_request.to_boto())

        return shapes.GetTagsResponse.from_boto(response)
