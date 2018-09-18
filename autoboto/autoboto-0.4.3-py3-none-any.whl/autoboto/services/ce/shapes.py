import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AccountScope(str):
    PAYER = "PAYER"
    LINKED = "LINKED"


@dataclasses.dataclass
class BillExpirationException(ShapeBase):
    """
    The requested report expired. Update the date interval and try again.
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


class Context(str):
    COST_AND_USAGE = "COST_AND_USAGE"
    RESERVATIONS = "RESERVATIONS"


@dataclasses.dataclass
class Coverage(ShapeBase):
    """
    The amount of instance usage that a reservation covered.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "coverage_hours",
                "CoverageHours",
                TypeInfo(CoverageHours),
            ),
        ]

    # The amount of instance usage that a reservation covered, in hours.
    coverage_hours: "CoverageHours" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CoverageByTime(ShapeBase):
    """
    Reservation coverage for a specified period, in hours.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[ReservationCoverageGroup]),
            ),
            (
                "total",
                "Total",
                TypeInfo(Coverage),
            ),
        ]

    # The period over which this coverage was used.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The groups of instances that are covered by a reservation.
    groups: typing.List["ReservationCoverageGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total reservation coverage, in hours.
    total: "Coverage" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CoverageHours(ShapeBase):
    """
    How long a running instance either used a reservation or was On-Demand.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "on_demand_hours",
                "OnDemandHours",
                TypeInfo(str),
            ),
            (
                "reserved_hours",
                "ReservedHours",
                TypeInfo(str),
            ),
            (
                "total_running_hours",
                "TotalRunningHours",
                TypeInfo(str),
            ),
            (
                "coverage_hours_percentage",
                "CoverageHoursPercentage",
                TypeInfo(str),
            ),
        ]

    # The number of instance running hours that are covered by On-Demand
    # Instances.
    on_demand_hours: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instance running hours that are covered by reservations.
    reserved_hours: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total instance usage, in hours.
    total_running_hours: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The percentage of instance hours that are covered by a reservation.
    coverage_hours_percentage: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DataUnavailableException(ShapeBase):
    """
    The requested data is unavailable.
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
class DateInterval(ShapeBase):
    """
    The time period that you want the usage and costs for.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
            (
                "end",
                "End",
                TypeInfo(str),
            ),
        ]

    # The beginning of the time period that you want the usage and costs for. The
    # start date is inclusive. For example, if `start` is `2017-01-01`, AWS
    # retrieves cost and usage data starting at `2017-01-01` up to the end date.
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end of the time period that you want the usage and costs for. The end
    # date is exclusive. For example, if `end` is `2017-05-01`, AWS retrieves
    # cost and usage data from the start date up to, but not including,
    # `2017-05-01`.
    end: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Dimension(str):
    AZ = "AZ"
    INSTANCE_TYPE = "INSTANCE_TYPE"
    LINKED_ACCOUNT = "LINKED_ACCOUNT"
    OPERATION = "OPERATION"
    PURCHASE_TYPE = "PURCHASE_TYPE"
    REGION = "REGION"
    SERVICE = "SERVICE"
    USAGE_TYPE = "USAGE_TYPE"
    USAGE_TYPE_GROUP = "USAGE_TYPE_GROUP"
    RECORD_TYPE = "RECORD_TYPE"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    TENANCY = "TENANCY"
    SCOPE = "SCOPE"
    PLATFORM = "PLATFORM"
    SUBSCRIPTION_ID = "SUBSCRIPTION_ID"
    LEGAL_ENTITY_NAME = "LEGAL_ENTITY_NAME"
    DEPLOYMENT_OPTION = "DEPLOYMENT_OPTION"
    DATABASE_ENGINE = "DATABASE_ENGINE"
    CACHE_ENGINE = "CACHE_ENGINE"
    INSTANCE_TYPE_FAMILY = "INSTANCE_TYPE_FAMILY"


@dataclasses.dataclass
class DimensionValues(ShapeBase):
    """
    The metadata that you can use to filter and group your results. You can use
    `GetDimensionValues` to find specific values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Union[str, Dimension]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The names of the metadata types that you can use to filter and group your
    # results. For example, `AZ` returns a list of Availability Zones.
    key: typing.Union[str, "Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata values that you can use to filter and group your results. You
    # can use `GetDimensionValues` to find specific values.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DimensionValuesWithAttributes(ShapeBase):
    """
    The metadata of a specific type that you can use to filter and group your
    results. You can use `GetDimensionValues` to find specific values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The value of a dimension with a specific attribute.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attribute that applies to a specific `Dimension`.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EC2InstanceDetails(ShapeBase):
    """
    Details about the EC2 instances that AWS recommends that you purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family",
                "Family",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "tenancy",
                "Tenancy",
                TypeInfo(str),
            ),
            (
                "current_generation",
                "CurrentGeneration",
                TypeInfo(bool),
            ),
            (
                "size_flex_eligible",
                "SizeFlexEligible",
                TypeInfo(bool),
            ),
        ]

    # The instance family of the recommended reservation.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of instance that AWS recommends.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region of the recommended reservation.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone of the recommended reservation.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform of the recommended reservation. The platform is the specific
    # combination of operating system, license model, and software on an
    # instance.
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommended reservation is dedicated or shared.
    tenancy: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommendation is for a current generation instance.
    current_generation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommended reservation is size flexible.
    size_flex_eligible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EC2Specification(ShapeBase):
    """
    The EC2 hardware specifications that you want AWS to provide recommendations
    for.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_class",
                "OfferingClass",
                TypeInfo(typing.Union[str, OfferingClass]),
            ),
        ]

    # Whether you want a recommendation for standard or convertible reservations.
    offering_class: typing.Union[str, "OfferingClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ESInstanceDetails(ShapeBase):
    """
    Details about the ES instances that AWS recommends that you purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_class",
                "InstanceClass",
                TypeInfo(str),
            ),
            (
                "instance_size",
                "InstanceSize",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "current_generation",
                "CurrentGeneration",
                TypeInfo(bool),
            ),
            (
                "size_flex_eligible",
                "SizeFlexEligible",
                TypeInfo(bool),
            ),
        ]

    # The class of instance that AWS recommends.
    instance_class: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of instance that AWS recommends.
    instance_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region of the recommended reservation.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommendation is for a current generation instance.
    current_generation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommended reservation is size flexible.
    size_flex_eligible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ElastiCacheInstanceDetails(ShapeBase):
    """
    Details about the ElastiCache instances that AWS recommends that you purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family",
                "Family",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "product_description",
                "ProductDescription",
                TypeInfo(str),
            ),
            (
                "current_generation",
                "CurrentGeneration",
                TypeInfo(bool),
            ),
            (
                "size_flex_eligible",
                "SizeFlexEligible",
                TypeInfo(bool),
            ),
        ]

    # The instance family of the recommended reservation.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of node that AWS recommends.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region of the recommended reservation.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the recommended reservation.
    product_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommendation is for a current generation instance.
    current_generation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommended reservation is size flexible.
    size_flex_eligible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Expression(ShapeBase):
    """
    Use `Expression` to filter by cost or by usage. There are two patterns:

      * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for `INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`. The `Expression` for that looks like this:

    `{ "Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "m4.xlarge", “c4.large” ]
    } }`

    The list of dimension values are OR'd together to retrieve cost or usage data.
    You can create `Expression` and `DimensionValues` objects using either `with*`
    methods or `set*` methods in multiple lines.

      * Compound dimension values with logical operations - You can use multiple `Expression` types and the logical operators `AND/OR/NOT` to create a list of one or more `Expression` objects. This allows you to filter on more advanced options. For example, you can filter on `((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`. The `Expression` for that looks like this:

    `{ "And": [ {"Or": [ {"Dimensions": { "Key": "INSTANCE_TYPE", "Values": [
    "m4.x.large", "c4.large" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"]
    } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"]
    }}} ] } `

    Because each `Expression` can have only one operator, the service returns an
    error if more than one is specified. The following example shows an `Expression`
    object that creates an error.

    ` { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
    "DataTransfer" ] } } `
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "or_",
                "Or",
                TypeInfo(typing.List[Expression]),
            ),
            (
                "and_",
                "And",
                TypeInfo(typing.List[Expression]),
            ),
            (
                "not_",
                "Not",
                TypeInfo(Expression),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(DimensionValues),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(TagValues),
            ),
        ]

    # Return results that match either `Dimension` object.
    or_: typing.List["Expression"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return results that match both `Dimension` objects.
    and_: typing.List["Expression"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return results that don't match a `Dimension` object.
    not_: "Expression" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific `Dimension` to use for `Expression`.
    dimensions: "DimensionValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The specific `Tag` to use for `Expression`.
    tags: "TagValues" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCostAndUsageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "granularity",
                "Granularity",
                TypeInfo(typing.Union[str, Granularity]),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(Expression),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.List[str]),
            ),
            (
                "group_by",
                "GroupBy",
                TypeInfo(typing.List[GroupDefinition]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    # Sets the start and end dates for retrieving AWS costs. The start date is
    # inclusive, but the end date is exclusive. For example, if `start` is
    # `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is
    # retrieved from `2017-01-01` up to and including `2017-04-30` but not
    # including `2017-05-01`.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the AWS cost granularity to `MONTHLY` or `DAILY`. If `Granularity`
    # isn't set, the response object doesn't include the `Granularity`, either
    # `MONTHLY` or `DAILY`.
    granularity: typing.Union[str, "Granularity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters AWS costs by different dimensions. For example, you can specify
    # `SERVICE` and `LINKED_ACCOUNT` and get the costs that are associated with
    # that account's usage of that service. You can nest `Expression` objects to
    # define any combination of dimension filters. For more information, see
    # [Expression](http://docs.aws.amazon.com/aws-cost-
    # management/latest/APIReference/API_Expression.html).
    filter: "Expression" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Which metrics are returned in the query. For more information about blended
    # and unblended rates, see [Why does the "blended" annotation appear on some
    # line items in my bill?](https://aws.amazon.com/premiumsupport/knowledge-
    # center/blended-rates-intro/).

    # Valid values are `AmortizedCost`, `BlendedCost`, `UnblendedCost`, and
    # `UsageQuantity`.

    # If you return the `UsageQuantity` metric, the service aggregates all usage
    # numbers without taking into account the units. For example, if you
    # aggregate `usageQuantity` across all of EC2, the results aren't meaningful
    # because EC2 compute hours and data transfer are measured in different units
    # (for example, hours vs. GB). To get more meaningful `UsageQuantity`
    # metrics, filter by `UsageType` or `UsageTypeGroups`.

    # `Metrics` is required for `GetCostAndUsage` requests.
    metrics: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can group AWS costs using up to two different groups, either
    # dimensions, tag keys, or both.

    # When you group by tag key, you get all tag values, including empty strings.

    # Valid values are `AZ`, `INSTANCE_TYPE`, `LEGAL_ENTITY_NAME`,
    # `LINKED_ACCOUNT`, `OPERATION`, `PLATFORM`, `PURCHASE_TYPE`, `SERVICE`,
    # `TAGS`, `TENANCY`, and `USAGE_TYPE`.
    group_by: typing.List["GroupDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to retrieve the next set of results. AWS provides the token when
    # the response from a previous call has more results than the maximum page
    # size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCostAndUsageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
            (
                "group_definitions",
                "GroupDefinitions",
                TypeInfo(typing.List[GroupDefinition]),
            ),
            (
                "results_by_time",
                "ResultsByTime",
                TypeInfo(typing.List[ResultByTime]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of retrievable results. AWS provides the token
    # when the response from a previous call has more results than the maximum
    # page size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The groups that are specified by the `Filter` or `GroupBy` parameters in
    # the request.
    group_definitions: typing.List["GroupDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time period that is covered by the results in the response.
    results_by_time: typing.List["ResultByTime"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDimensionValuesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "dimension",
                "Dimension",
                TypeInfo(typing.Union[str, Dimension]),
            ),
            (
                "search_string",
                "SearchString",
                TypeInfo(str),
            ),
            (
                "context",
                "Context",
                TypeInfo(typing.Union[str, Context]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    # The start and end dates for retrieving the dimension values. The start date
    # is inclusive, but the end date is exclusive. For example, if `start` is
    # `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is
    # retrieved from `2017-01-01` up to and including `2017-04-30` but not
    # including `2017-05-01`.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the dimension. Each `Dimension` is available for different a
    # `Context`. For more information, see `Context`.
    dimension: typing.Union[str, "Dimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value that you want to search the filter values for.
    search_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The context for the call to `GetDimensionValues`. This can be
    # `RESERVATIONS` or `COST_AND_USAGE`. The default value is `COST_AND_USAGE`.
    # If the context is set to `RESERVATIONS`, the resulting dimension values can
    # be used in the `GetReservationUtilization` operation. If the context is set
    # to `COST_AND_USAGE` the resulting dimension values can be used in the
    # `GetCostAndUsage` operation.

    # If you set the context to `COST_AND_USAGE`, you can use the following
    # dimensions for searching:

    #   * AZ - The Availability Zone. An example is `us-east-1a`.

    #   * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.

    #   * INSTANCE_TYPE - The type of EC2 instance. An example is `m4.xlarge`.

    #   * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.

    #   * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.

    #   * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.

    #   * OPERATION - The action performed. Examples include `RunInstance` and `CreateBucket`.

    #   * PLATFORM - The EC2 operating system. Examples are Windows or Linux.

    #   * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.

    #   * SERVICE - The AWS service such as Amazon DynamoDB.

    #   * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the `GetDimensionValues` operation includes a unit attribute. Examples include GB and Hrs.

    #   * USAGE_TYPE_GROUP - The grouping of common usage types. An example is EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.

    #   * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.

    # If you set the context to `RESERVATIONS`, you can use the following
    # dimensions for searching:

    #   * AZ - The Availability Zone. An example is `us-east-1a`.

    #   * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.

    #   * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ`.

    #   * INSTANCE_TYPE - The type of EC2 instance. An example is `m4.xlarge`.

    #   * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.

    #   * PLATFORM - The EC2 operating system. Examples are Windows or Linux.

    #   * REGION - The AWS Region.

    #   * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.

    #   * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).

    #   * TENANCY - The tenancy of a resource. Examples are shared or dedicated.
    context: typing.Union[str, "Context"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to retrieve the next set of results. AWS provides the token when
    # the response from a previous call has more results than the maximum page
    # size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDimensionValuesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "dimension_values",
                "DimensionValues",
                TypeInfo(typing.List[DimensionValuesWithAttributes]),
            ),
            (
                "return_size",
                "ReturnSize",
                TypeInfo(int),
            ),
            (
                "total_size",
                "TotalSize",
                TypeInfo(int),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The filters that you used to filter your request. Some dimensions are
    # available only for a specific context:

    # If you set the context to `COST_AND_USAGE`, you can use the following
    # dimensions for searching:

    #   * AZ - The Availability Zone. An example is `us-east-1a`.

    #   * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.

    #   * INSTANCE_TYPE - The type of EC2 instance. An example is `m4.xlarge`.

    #   * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.

    #   * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.

    #   * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.

    #   * OPERATION - The action performed. Examples include `RunInstance` and `CreateBucket`.

    #   * PLATFORM - The EC2 operating system. Examples are Windows or Linux.

    #   * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.

    #   * SERVICE - The AWS service such as Amazon DynamoDB.

    #   * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the `GetDimensionValues` operation includes a unit attribute. Examples include GB and Hrs.

    #   * USAGE_TYPE_GROUP - The grouping of common usage types. An example is EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.

    #   * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.

    # If you set the context to `RESERVATIONS`, you can use the following
    # dimensions for searching:

    #   * AZ - The Availability Zone. An example is `us-east-1a`.

    #   * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.

    #   * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ`.

    #   * INSTANCE_TYPE - The type of EC2 instance. An example is `m4.xlarge`.

    #   * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.

    #   * PLATFORM - The EC2 operating system. Examples are Windows or Linux.

    #   * REGION - The AWS Region.

    #   * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.

    #   * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).

    #   * TENANCY - The tenancy of a resource. Examples are shared or dedicated.
    dimension_values: typing.List["DimensionValuesWithAttributes"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # The number of results that AWS returned at one time.
    return_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of search results.
    total_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of retrievable results. AWS provides the token
    # when the response from a previous call has more results than the maximum
    # page size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservationCoverageRequest(ShapeBase):
    """
    You can use the following request parameters to query for how much of your
    instance usage is covered by a reservation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "group_by",
                "GroupBy",
                TypeInfo(typing.List[GroupDefinition]),
            ),
            (
                "granularity",
                "Granularity",
                TypeInfo(typing.Union[str, Granularity]),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(Expression),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    # The start and end dates of the period for which you want to retrieve data
    # about reservation coverage. You can retrieve data for a maximum of 13
    # months: the last 12 months and the current month. The start date is
    # inclusive, but the end date is exclusive. For example, if `start` is
    # `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is
    # retrieved from `2017-01-01` up to and including `2017-04-30` but not
    # including `2017-05-01`.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can group the data by the following attributes:

    #   * AZ

    #   * CACHE_ENGINE

    #   * DATABASE_ENGINE

    #   * DEPLOYMENT_OPTION

    #   * INSTANCE_TYPE

    #   * LINKED_ACCOUNT

    #   * OPERATING_SYSTEM

    #   * PLATFORM

    #   * REGION

    #   * TAG

    #   * TENANCY
    group_by: typing.List["GroupDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The granularity of the AWS cost data for the reservation. Valid values are
    # `MONTHLY` and `DAILY`.

    # If `GroupBy` is set, `Granularity` can't be set. If `Granularity` isn't
    # set, the response object doesn't include `Granularity`, either `MONTHLY` or
    # `DAILY`.
    granularity: typing.Union[str, "Granularity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters utilization data by dimensions. You can filter by the following
    # dimensions:

    #   * AZ

    #   * CACHE_ENGINE

    #   * DATABASE_ENGINE

    #   * DEPLOYMENT_OPTION

    #   * INSTANCE_TYPE

    #   * LINKED_ACCOUNT

    #   * OPERATING_SYSTEM

    #   * PLATFORM

    #   * REGION

    #   * SERVICE

    #   * TAG

    #   * TENANCY

    # `GetReservationCoverage` uses the same `
    # [Expression](http://docs.aws.amazon.com/aws-cost-
    # management/latest/APIReference/API_Expression.html) ` object as the other
    # operations, but only `AND` is supported among each dimension. You can nest
    # only one level deep. If there are multiple values for a dimension, they are
    # OR'd together.

    # If you don't provide a `SERVICE` filter, Cost Explorer defaults to EC2.
    filter: "Expression" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results. AWS provides the token when
    # the response from a previous call has more results than the maximum page
    # size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservationCoverageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "coverages_by_time",
                "CoveragesByTime",
                TypeInfo(typing.List[CoverageByTime]),
            ),
            (
                "total",
                "Total",
                TypeInfo(Coverage),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time that your reservations covered.
    coverages_by_time: typing.List["CoverageByTime"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total amount of instance usage that is covered by a reservation.
    total: "Coverage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of retrievable results. AWS provides the token
    # when the response from a previous call has more results than the maximum
    # page size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservationPurchaseRecommendationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service",
                "Service",
                TypeInfo(str),
            ),
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "account_scope",
                "AccountScope",
                TypeInfo(typing.Union[str, AccountScope]),
            ),
            (
                "lookback_period_in_days",
                "LookbackPeriodInDays",
                TypeInfo(typing.Union[str, LookbackPeriodInDays]),
            ),
            (
                "term_in_years",
                "TermInYears",
                TypeInfo(typing.Union[str, TermInYears]),
            ),
            (
                "payment_option",
                "PaymentOption",
                TypeInfo(typing.Union[str, PaymentOption]),
            ),
            (
                "service_specification",
                "ServiceSpecification",
                TypeInfo(ServiceSpecification),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(int),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    # The specific service that you want recommendations for.
    service: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The account ID that is associated with the recommendation.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The account scope that you want recommendations for. `PAYER` means that AWS
    # includes the master account and any member accounts when it calculates its
    # recommendations. `LINKED` means that AWS includes only member accounts when
    # it calculates its recommendations.

    # Valid values are `PAYER` and `LINKED`.
    account_scope: typing.Union[str, "AccountScope"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of previous days that you want AWS to consider when it
    # calculates your recommendations.
    lookback_period_in_days: typing.Union[str, "LookbackPeriodInDays"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The reservation term that you want recommendations for.
    term_in_years: typing.Union[str, "TermInYears"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reservation purchase option that you want recommendations for.
    payment_option: typing.Union[str, "PaymentOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The hardware specifications for the service instances that you want
    # recommendations for, such as standard or convertible EC2 instances.
    service_specification: "ServiceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of recommendations that you want returned in a single response
    # object.
    page_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token that indicates the next set of results that you want
    # to retrieve.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservationPurchaseRecommendationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(ReservationPurchaseRecommendationMetadata),
            ),
            (
                "recommendations",
                "Recommendations",
                TypeInfo(typing.List[ReservationPurchaseRecommendation]),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about this specific recommendation call, such as the time stamp
    # for when Cost Explorer generated this recommendation.
    metadata: "ReservationPurchaseRecommendationMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recommendations for reservations to purchase.
    recommendations: typing.List["ReservationPurchaseRecommendation"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The pagination token for the next set of retrievable results.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservationUtilizationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "group_by",
                "GroupBy",
                TypeInfo(typing.List[GroupDefinition]),
            ),
            (
                "granularity",
                "Granularity",
                TypeInfo(typing.Union[str, Granularity]),
            ),
            (
                "filter",
                "Filter",
                TypeInfo(Expression),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    # Sets the start and end dates for retrieving Reserved Instance (RI)
    # utilization. The start date is inclusive, but the end date is exclusive.
    # For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the
    # cost and usage data is retrieved from `2017-01-01` up to and including
    # `2017-04-30` but not including `2017-05-01`.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Groups only by `SUBSCRIPTION_ID`. Metadata is included.
    group_by: typing.List["GroupDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `GroupBy` is set, `Granularity` can't be set. If `Granularity` isn't
    # set, the response object doesn't include `Granularity`, either `MONTHLY` or
    # `DAILY`. If both `GroupBy` and `Granularity` aren't set,
    # `GetReservationUtilization` defaults to `DAILY`.
    granularity: typing.Union[str, "Granularity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Filters utilization data by dimensions. You can filter by the following
    # dimensions:

    #   * AZ

    #   * CACHE_ENGINE

    #   * DATABASE_ENGINE

    #   * DEPLOYMENT_OPTION

    #   * INSTANCE_TYPE

    #   * LINKED_ACCOUNT

    #   * OPERATING_SYSTEM

    #   * PLATFORM

    #   * REGION

    #   * SERVICE

    #   * SCOPE

    #   * TENANCY

    # `GetReservationUtilization` uses the same `
    # [Expression](http://docs.aws.amazon.com/aws-cost-
    # management/latest/APIReference/API_Expression.html) ` object as the other
    # operations, but only `AND` is supported among each dimension, and nesting
    # is supported up to only one level deep. If there are multiple values for a
    # dimension, they are OR'd together.
    filter: "Expression" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results. AWS provides the token when
    # the response from a previous call has more results than the maximum page
    # size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetReservationUtilizationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "utilizations_by_time",
                "UtilizationsByTime",
                TypeInfo(typing.List[UtilizationByTime]),
            ),
            (
                "total",
                "Total",
                TypeInfo(ReservationAggregates),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time that you utilized your RIs.
    utilizations_by_time: typing.List["UtilizationByTime"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total amount of time that you utilized your RIs.
    total: "ReservationAggregates" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of retrievable results. AWS provides the token
    # when the response from a previous call has more results than the maximum
    # page size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "search_string",
                "SearchString",
                TypeInfo(str),
            ),
            (
                "tag_key",
                "TagKey",
                TypeInfo(str),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    # The start and end dates for retrieving the dimension values. The start date
    # is inclusive, but the end date is exclusive. For example, if `start` is
    # `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is
    # retrieved from `2017-01-01` up to and including `2017-04-30` but not
    # including `2017-05-01`.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that you want to search for.
    search_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key of the tag that you want to return values for.
    tag_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results. AWS provides the token when
    # the response from a previous call has more results than the maximum page
    # size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTagsResponse(OutputShapeBase):
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
                TypeInfo(typing.List[str]),
            ),
            (
                "return_size",
                "ReturnSize",
                TypeInfo(int),
            ),
            (
                "total_size",
                "TotalSize",
                TypeInfo(int),
            ),
            (
                "next_page_token",
                "NextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags that match your request.
    tags: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of query results that AWS returns at a time.
    return_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of query results.
    total_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of retrievable results. AWS provides the token
    # when the response from a previous call has more results than the maximum
    # page size.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Granularity(str):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"


@dataclasses.dataclass
class Group(ShapeBase):
    """
    One level of grouped data within the results.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[str]),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, MetricValue]),
            ),
        ]

    # The keys that are included in this group.
    keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metrics that are included in this group.
    metrics: typing.Dict[str, "MetricValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GroupDefinition(ShapeBase):
    """
    Represents a group when you specify a group by criteria, or in the response to a
    query with a specific grouping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, GroupDefinitionType]),
            ),
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
        ]

    # The string that represents the type of group.
    type: typing.Union[str, "GroupDefinitionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The string that represents a key for a specified group.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class GroupDefinitionType(str):
    DIMENSION = "DIMENSION"
    TAG = "TAG"


@dataclasses.dataclass
class InstanceDetails(ShapeBase):
    """
    Details about the instances that AWS recommends that you purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ec2_instance_details",
                "EC2InstanceDetails",
                TypeInfo(EC2InstanceDetails),
            ),
            (
                "rds_instance_details",
                "RDSInstanceDetails",
                TypeInfo(RDSInstanceDetails),
            ),
            (
                "redshift_instance_details",
                "RedshiftInstanceDetails",
                TypeInfo(RedshiftInstanceDetails),
            ),
            (
                "elasti_cache_instance_details",
                "ElastiCacheInstanceDetails",
                TypeInfo(ElastiCacheInstanceDetails),
            ),
            (
                "es_instance_details",
                "ESInstanceDetails",
                TypeInfo(ESInstanceDetails),
            ),
        ]

    # The EC2 instances that AWS recommends that you purchase.
    ec2_instance_details: "EC2InstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The RDS instances that AWS recommends that you purchase.
    rds_instance_details: "RDSInstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Redshift instances that AWS recommends that you purchase.
    redshift_instance_details: "RedshiftInstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ElastiCache instances that AWS recommends that you purchase.
    elasti_cache_instance_details: "ElastiCacheInstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon ES instances that AWS recommends that you purchase.
    es_instance_details: "ESInstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    The pagination token is invalid. Try again without a pagination token.
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
class LimitExceededException(ShapeBase):
    """
    You made too many calls in a short period of time. Try again later.
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


class LookbackPeriodInDays(str):
    SEVEN_DAYS = "SEVEN_DAYS"
    THIRTY_DAYS = "THIRTY_DAYS"
    SIXTY_DAYS = "SIXTY_DAYS"


@dataclasses.dataclass
class MetricValue(ShapeBase):
    """
    The aggregated value for a metric.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amount",
                "Amount",
                TypeInfo(str),
            ),
            (
                "unit",
                "Unit",
                TypeInfo(str),
            ),
        ]

    # The actual number that represents the metric.
    amount: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unit that the metric is given in.
    unit: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OfferingClass(str):
    STANDARD = "STANDARD"
    CONVERTIBLE = "CONVERTIBLE"


class PaymentOption(str):
    NO_UPFRONT = "NO_UPFRONT"
    PARTIAL_UPFRONT = "PARTIAL_UPFRONT"
    ALL_UPFRONT = "ALL_UPFRONT"
    LIGHT_UTILIZATION = "LIGHT_UTILIZATION"
    MEDIUM_UTILIZATION = "MEDIUM_UTILIZATION"
    HEAVY_UTILIZATION = "HEAVY_UTILIZATION"


@dataclasses.dataclass
class RDSInstanceDetails(ShapeBase):
    """
    Details about the RDS instances that AWS recommends that you purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family",
                "Family",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "database_engine",
                "DatabaseEngine",
                TypeInfo(str),
            ),
            (
                "database_edition",
                "DatabaseEdition",
                TypeInfo(str),
            ),
            (
                "deployment_option",
                "DeploymentOption",
                TypeInfo(str),
            ),
            (
                "license_model",
                "LicenseModel",
                TypeInfo(str),
            ),
            (
                "current_generation",
                "CurrentGeneration",
                TypeInfo(bool),
            ),
            (
                "size_flex_eligible",
                "SizeFlexEligible",
                TypeInfo(bool),
            ),
        ]

    # The instance family of the recommended reservation.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of instance that AWS recommends.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region of the recommended reservation.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database engine that the recommended reservation supports.
    database_engine: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The database edition that the recommended reservation supports.
    database_edition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommendation is for a reservation in a single Availability
    # Zone or a reservation with a backup in a second Availability Zone.
    deployment_option: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The license model that the recommended reservation supports.
    license_model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommendation is for a current generation instance.
    current_generation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommended reservation is size flexible.
    size_flex_eligible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RedshiftInstanceDetails(ShapeBase):
    """
    Details about the Amazon Redshift instances that AWS recommends that you
    purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family",
                "Family",
                TypeInfo(str),
            ),
            (
                "node_type",
                "NodeType",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "current_generation",
                "CurrentGeneration",
                TypeInfo(bool),
            ),
            (
                "size_flex_eligible",
                "SizeFlexEligible",
                TypeInfo(bool),
            ),
        ]

    # The instance family of the recommended reservation.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of node that AWS recommends.
    node_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region of the recommended reservation.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommendation is for a current generation instance.
    current_generation: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the recommended reservation is size flexible.
    size_flex_eligible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestChangedException(ShapeBase):
    """
    Your request parameters changed between pages. Try again with the old parameters
    or without a pagination token.
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
class ReservationAggregates(ShapeBase):
    """
    The aggregated numbers for your Reserved Instance (RI) usage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "utilization_percentage",
                "UtilizationPercentage",
                TypeInfo(str),
            ),
            (
                "purchased_hours",
                "PurchasedHours",
                TypeInfo(str),
            ),
            (
                "total_actual_hours",
                "TotalActualHours",
                TypeInfo(str),
            ),
            (
                "unused_hours",
                "UnusedHours",
                TypeInfo(str),
            ),
            (
                "on_demand_cost_of_ri_hours_used",
                "OnDemandCostOfRIHoursUsed",
                TypeInfo(str),
            ),
            (
                "net_ri_savings",
                "NetRISavings",
                TypeInfo(str),
            ),
            (
                "total_potential_ri_savings",
                "TotalPotentialRISavings",
                TypeInfo(str),
            ),
            (
                "amortized_upfront_fee",
                "AmortizedUpfrontFee",
                TypeInfo(str),
            ),
            (
                "amortized_recurring_fee",
                "AmortizedRecurringFee",
                TypeInfo(str),
            ),
            (
                "total_amortized_fee",
                "TotalAmortizedFee",
                TypeInfo(str),
            ),
        ]

    # The percentage of RI time that you used.
    utilization_percentage: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How many RI hours that you purchased.
    purchased_hours: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of RI hours that you used.
    total_actual_hours: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of RI hours that you didn't use.
    unused_hours: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How much your RIs would cost if charged On-Demand rates.
    on_demand_cost_of_ri_hours_used: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much you saved due to purchasing and utilizing RIs. AWS calculates this
    # by subtracting `TotalAmortizedFee` from `OnDemandCostOfRIHoursUsed`.
    net_ri_savings: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How much you could save if you use your entire reservation.
    total_potential_ri_savings: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upfront cost of your RI, amortized over the RI period.
    amortized_upfront_fee: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The monthly cost of your RI, amortized over the RI period.
    amortized_recurring_fee: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total cost of your RI, amortized over the RI period.
    total_amortized_fee: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReservationCoverageGroup(ShapeBase):
    """
    A group of reservations that share a set of attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "coverage",
                "Coverage",
                TypeInfo(Coverage),
            ),
        ]

    # The attributes for this group of reservations.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much instance usage this group of reservations covered.
    coverage: "Coverage" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReservationPurchaseRecommendation(ShapeBase):
    """
    A specific reservation that AWS recommends for purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_scope",
                "AccountScope",
                TypeInfo(typing.Union[str, AccountScope]),
            ),
            (
                "lookback_period_in_days",
                "LookbackPeriodInDays",
                TypeInfo(typing.Union[str, LookbackPeriodInDays]),
            ),
            (
                "term_in_years",
                "TermInYears",
                TypeInfo(typing.Union[str, TermInYears]),
            ),
            (
                "payment_option",
                "PaymentOption",
                TypeInfo(typing.Union[str, PaymentOption]),
            ),
            (
                "service_specification",
                "ServiceSpecification",
                TypeInfo(ServiceSpecification),
            ),
            (
                "recommendation_details",
                "RecommendationDetails",
                TypeInfo(typing.List[ReservationPurchaseRecommendationDetail]),
            ),
            (
                "recommendation_summary",
                "RecommendationSummary",
                TypeInfo(ReservationPurchaseRecommendationSummary),
            ),
        ]

    # The account scope that AWS recommends that you purchase this instance for.
    # For example, you can purchase this reservation for an entire organization
    # in AWS Organizations.
    account_scope: typing.Union[str, "AccountScope"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How many days of previous usage that AWS considers when making this
    # recommendation.
    lookback_period_in_days: typing.Union[str, "LookbackPeriodInDays"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The term of the reservation that you want recommendations for, in years.
    term_in_years: typing.Union[str, "TermInYears"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The payment option for the reservation. For example, `AllUpfront` or
    # `NoUpfront`.
    payment_option: typing.Union[str, "PaymentOption"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Hardware specifications for the service that you want recommendations for.
    service_specification: "ServiceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about the recommended purchases.
    recommendation_details: typing.List[
        "ReservationPurchaseRecommendationDetail"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # A summary about the recommended purchase.
    recommendation_summary: "ReservationPurchaseRecommendationSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservationPurchaseRecommendationDetail(ShapeBase):
    """
    Details about your recommended reservation purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_details",
                "InstanceDetails",
                TypeInfo(InstanceDetails),
            ),
            (
                "recommended_number_of_instances_to_purchase",
                "RecommendedNumberOfInstancesToPurchase",
                TypeInfo(str),
            ),
            (
                "recommended_normalized_units_to_purchase",
                "RecommendedNormalizedUnitsToPurchase",
                TypeInfo(str),
            ),
            (
                "minimum_number_of_instances_used_per_hour",
                "MinimumNumberOfInstancesUsedPerHour",
                TypeInfo(str),
            ),
            (
                "minimum_normalized_units_used_per_hour",
                "MinimumNormalizedUnitsUsedPerHour",
                TypeInfo(str),
            ),
            (
                "maximum_number_of_instances_used_per_hour",
                "MaximumNumberOfInstancesUsedPerHour",
                TypeInfo(str),
            ),
            (
                "maximum_normalized_units_used_per_hour",
                "MaximumNormalizedUnitsUsedPerHour",
                TypeInfo(str),
            ),
            (
                "average_number_of_instances_used_per_hour",
                "AverageNumberOfInstancesUsedPerHour",
                TypeInfo(str),
            ),
            (
                "average_normalized_units_used_per_hour",
                "AverageNormalizedUnitsUsedPerHour",
                TypeInfo(str),
            ),
            (
                "average_utilization",
                "AverageUtilization",
                TypeInfo(str),
            ),
            (
                "estimated_break_even_in_months",
                "EstimatedBreakEvenInMonths",
                TypeInfo(str),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "estimated_monthly_savings_amount",
                "EstimatedMonthlySavingsAmount",
                TypeInfo(str),
            ),
            (
                "estimated_monthly_savings_percentage",
                "EstimatedMonthlySavingsPercentage",
                TypeInfo(str),
            ),
            (
                "estimated_monthly_on_demand_cost",
                "EstimatedMonthlyOnDemandCost",
                TypeInfo(str),
            ),
            (
                "estimated_reservation_cost_for_lookback_period",
                "EstimatedReservationCostForLookbackPeriod",
                TypeInfo(str),
            ),
            (
                "upfront_cost",
                "UpfrontCost",
                TypeInfo(str),
            ),
            (
                "recurring_standard_monthly_cost",
                "RecurringStandardMonthlyCost",
                TypeInfo(str),
            ),
        ]

    # Details about the instances that AWS recommends that you purchase.
    instance_details: "InstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instances that AWS recommends that you purchase.
    recommended_number_of_instances_to_purchase: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of normalized units that AWS recommends that you purchase.
    recommended_normalized_units_to_purchase: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum number of instances that you used in an hour during the
    # historical period. AWS uses this to calculate your recommended reservation
    # purchases.
    minimum_number_of_instances_used_per_hour: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum number of hours that you used in an hour during the historical
    # period. AWS uses this to calculate your recommended reservation purchases.
    minimum_normalized_units_used_per_hour: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of instances that you used in an hour during the
    # historical period. AWS uses this to calculate your recommended reservation
    # purchases.
    maximum_number_of_instances_used_per_hour: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of normalized units that you used in an hour during the
    # historical period. AWS uses this to calculate your recommended reservation
    # purchases.
    maximum_normalized_units_used_per_hour: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The average number of instances that you used in an hour during the
    # historical period. AWS uses this to calculate your recommended reservation
    # purchases.
    average_number_of_instances_used_per_hour: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The average number of normalized units that you used in an hour during the
    # historical period. AWS uses this to calculate your recommended reservation
    # purchases.
    average_normalized_units_used_per_hour: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The average utilization of your instances. AWS uses this to calculate your
    # recommended reservation purchases.
    average_utilization: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How long AWS estimates that it takes for this instance to start saving you
    # money, in months.
    estimated_break_even_in_months: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The currency code that AWS used to calculate the costs for this instance.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How much AWS estimates that this specific recommendation could save you in
    # a month.
    estimated_monthly_savings_amount: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much AWS estimates that this specific recommendation could save you in
    # a month, as a percentage of your overall costs.
    estimated_monthly_savings_percentage: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much AWS estimates that you spend on On-Demand Instances in a month.
    estimated_monthly_on_demand_cost: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much AWS estimates that you would have spent for all usage during the
    # specified historical period if you had had a reservation.
    estimated_reservation_cost_for_lookback_period: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much purchasing this instance costs you upfront.
    upfront_cost: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How much purchasing this instance costs you on a monthly basis.
    recurring_standard_monthly_cost: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReservationPurchaseRecommendationMetadata(ShapeBase):
    """
    Information about this specific recommendation, such as the time stamp for when
    AWS made a specific recommendation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "recommendation_id",
                "RecommendationId",
                TypeInfo(str),
            ),
            (
                "generation_timestamp",
                "GenerationTimestamp",
                TypeInfo(str),
            ),
        ]

    # The ID for this specific recommendation.
    recommendation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp for when AWS made this recommendation.
    generation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReservationPurchaseRecommendationSummary(ShapeBase):
    """
    A summary about this recommendation, such as the currency code, the amount that
    AWS estimates that you could save, and the total amount of reservation to
    purchase.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total_estimated_monthly_savings_amount",
                "TotalEstimatedMonthlySavingsAmount",
                TypeInfo(str),
            ),
            (
                "total_estimated_monthly_savings_percentage",
                "TotalEstimatedMonthlySavingsPercentage",
                TypeInfo(str),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
        ]

    # The total amount that AWS estimates that this recommendation could save you
    # in a month.
    total_estimated_monthly_savings_amount: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total amount that AWS estimates that this recommendation could save you
    # in a month, as a percentage of your costs.
    total_estimated_monthly_savings_percentage: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The currency code used for this recommendation.
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReservationUtilizationGroup(ShapeBase):
    """
    A group of Reserved Instances (RIs) that share a set of attributes.
    """

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
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "utilization",
                "Utilization",
                TypeInfo(ReservationAggregates),
            ),
        ]

    # The key for a specific RI attribute.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of a specific RI attribute.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes for this group of RIs.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # How much you used this group of RIs.
    utilization: "ReservationAggregates" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResultByTime(ShapeBase):
    """
    The result that is associated with a time period.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "total",
                "Total",
                TypeInfo(typing.Dict[str, MetricValue]),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[Group]),
            ),
            (
                "estimated",
                "Estimated",
                TypeInfo(bool),
            ),
        ]

    # The time period covered by a result.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total amount of cost or usage accrued during the time period.
    total: typing.Dict[str, "MetricValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The groups that are included in this time period.
    groups: typing.List["Group"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether this result is estimated.
    estimated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceSpecification(ShapeBase):
    """
    Hardware specifications for the service that you want recommendations for.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ec2_specification",
                "EC2Specification",
                TypeInfo(EC2Specification),
            ),
        ]

    # The EC2 hardware specifications that you want AWS to provide
    # recommendations for.
    ec2_specification: "EC2Specification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TagValues(ShapeBase):
    """
    The values that are available for a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The key for a tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific value of a tag.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class TermInYears(str):
    ONE_YEAR = "ONE_YEAR"
    THREE_YEARS = "THREE_YEARS"


@dataclasses.dataclass
class UtilizationByTime(ShapeBase):
    """
    The amount of utilization, in hours.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_period",
                "TimePeriod",
                TypeInfo(DateInterval),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[ReservationUtilizationGroup]),
            ),
            (
                "total",
                "Total",
                TypeInfo(ReservationAggregates),
            ),
        ]

    # The period of time over which this utilization was used.
    time_period: "DateInterval" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The groups that are included in this utilization result.
    groups: typing.List["ReservationUtilizationGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of RI hours that were used.
    total: "ReservationAggregates" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
