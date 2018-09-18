import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AffectedEntity(ShapeBase):
    """
    Information about an entity that is affected by a Health event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entity_arn",
                "entityArn",
                TypeInfo(str),
            ),
            (
                "event_arn",
                "eventArn",
                TypeInfo(str),
            ),
            (
                "entity_value",
                "entityValue",
                TypeInfo(str),
            ),
            (
                "aws_account_id",
                "awsAccountId",
                TypeInfo(str),
            ),
            (
                "last_updated_time",
                "lastUpdatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(typing.Union[str, entityStatusCode]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The unique identifier for the entity. Format: `arn:aws:health: _entity-
    # region_ : _aws-account_ :entity/ _entity-id_ `. Example:
    # `arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K`
    entity_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    event_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the affected entity.
    entity_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The 12-digit AWS account number that contains the affected entity.
    aws_account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The most recent time that the entity was updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The most recent status of the entity affected by the event. The possible
    # values are `IMPAIRED`, `UNIMPAIRED`, and `UNKNOWN`.
    status_code: typing.Union[str, "entityStatusCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of entity tags attached to the affected entity.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DateTimeRange(ShapeBase):
    """
    A range of dates and times that is used by the EventFilter and EntityFilter
    objects. If `from` is set and `to` is set: match items where the timestamp
    (`startTime`, `endTime`, or `lastUpdatedTime`) is between `from` and `to`
    inclusive. If `from` is set and `to` is not set: match items where the timestamp
    value is equal to or after `from`. If `from` is not set and `to` is set: match
    items where the timestamp value is equal to or before `to`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_",
                "from",
                TypeInfo(datetime.datetime),
            ),
            (
                "to",
                "to",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The starting date and time of a time range.
    from_: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ending date and time of a time range.
    to: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAffectedEntitiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                TypeInfo(EntityFilter),
            ),
            (
                "locale",
                "locale",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # Values to narrow the results returned. At least one event ARN is required.
    filter: "EntityFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAffectedEntitiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entities",
                "entities",
                TypeInfo(typing.List[AffectedEntity]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The entities that match the filter criteria.
    entities: typing.List["AffectedEntity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeAffectedEntitiesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEntityAggregatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEntityAggregatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "entity_aggregates",
                "entityAggregates",
                TypeInfo(typing.List[EntityAggregate]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of entities that are affected by each of the specified events.
    entity_aggregates: typing.List["EntityAggregate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEventAggregatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aggregate_field",
                "aggregateField",
                TypeInfo(typing.Union[str, eventAggregateField]),
            ),
            (
                "filter",
                "filter",
                TypeInfo(EventFilter),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The only currently supported value is `eventTypeCategory`.
    aggregate_field: typing.Union[str, "eventAggregateField"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Values to narrow the results returned.
    filter: "EventFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventAggregatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_aggregates",
                "eventAggregates",
                TypeInfo(typing.List[EventAggregate]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of events in each category that meet the optional filter
    # criteria.
    event_aggregates: typing.List["EventAggregate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeEventAggregatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEventDetailsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                TypeInfo(str),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventDetailsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful_set",
                "successfulSet",
                TypeInfo(typing.List[EventDetails]),
            ),
            (
                "failed_set",
                "failedSet",
                TypeInfo(typing.List[EventDetailsErrorItem]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the events that could be retrieved.
    successful_set: typing.List["EventDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Error messages for any events that could not be retrieved.
    failed_set: typing.List["EventDetailsErrorItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEventTypesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                TypeInfo(EventTypeFilter),
            ),
            (
                "locale",
                "locale",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # Values to narrow the results returned.
    filter: "EventTypeFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventTypesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_types",
                "eventTypes",
                TypeInfo(typing.List[EventType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event types that match the filter criteria. Event types have a
    # category (`issue`, `accountNotification`, or `scheduledChange`), a service
    # (for example, `EC2`, `RDS`, `DATAPIPELINE`, `BILLING`), and a code (in the
    # format `AWS_ _SERVICE_ _ _DESCRIPTION_ `; for example,
    # `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`).
    event_types: typing.List["EventType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeEventTypesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                TypeInfo(EventFilter),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "locale",
                "locale",
                TypeInfo(str),
            ),
        ]

    # Values to narrow the results returned.
    filter: "EventFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events",
                "events",
                TypeInfo(typing.List[Event]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The events that match the specified filter criteria.
    events: typing.List["Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeEventsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class EntityAggregate(ShapeBase):
    """
    The number of entities that are affected by one or more events. Returned by the
    DescribeEntityAggregates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arn",
                "eventArn",
                TypeInfo(str),
            ),
            (
                "count",
                "count",
                TypeInfo(int),
            ),
        ]

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    event_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number entities that match the criteria for the specified events.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntityFilter(ShapeBase):
    """
    The values to use to filter results from the DescribeAffectedEntities operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "entity_arns",
                "entityArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "entity_values",
                "entityValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "last_updated_times",
                "lastUpdatedTimes",
                TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "status_codes",
                "statusCodes",
                TypeInfo(typing.List[typing.Union[str, entityStatusCode]]),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of entity ARNs (unique identifiers).
    entity_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IDs for affected entities.
    entity_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the most recent dates and times that the entity was updated.
    last_updated_times: typing.List["DateTimeRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of entity tags attached to the affected entity.
    tags: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of entity status codes (`IMPAIRED`, `UNIMPAIRED`, or `UNKNOWN`).
    status_codes: typing.List[typing.Union[str, "entityStatusCode"]
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )


@dataclasses.dataclass
class Event(ShapeBase):
    """
    Summary information about an event, returned by the DescribeEvents operation.
    The DescribeEventDetails operation also returns this information, as well as the
    EventDescription and additional event metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "service",
                "service",
                TypeInfo(str),
            ),
            (
                "event_type_code",
                "eventTypeCode",
                TypeInfo(str),
            ),
            (
                "event_type_category",
                "eventTypeCategory",
                TypeInfo(typing.Union[str, eventTypeCategory]),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_time",
                "lastUpdatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_code",
                "statusCode",
                TypeInfo(typing.Union[str, eventStatusCode]),
            ),
        ]

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS service that is affected by the event. For example, `EC2`, `RDS`.
    service: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the event type. The format is `AWS_ _SERVICE_ _
    # _DESCRIPTION_ `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
    event_type_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category of the event. Possible values are `issue`, `scheduledChange`,
    # and `accountNotification`.
    event_type_category: typing.Union[str, "eventTypeCategory"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The AWS region name of the event.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Availability Zone of the event. For example, us-east-1a.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the event began.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the event ended.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The most recent date and time that the event was updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The most recent status of the event. Possible values are `open`, `closed`,
    # and `upcoming`.
    status_code: typing.Union[str, "eventStatusCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventAggregate(ShapeBase):
    """
    The number of events of each issue type. Returned by the DescribeEventAggregates
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aggregate_value",
                "aggregateValue",
                TypeInfo(str),
            ),
            (
                "count",
                "count",
                TypeInfo(int),
            ),
        ]

    # The issue type for the associated count.
    aggregate_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of events of the associated issue type.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventDescription(ShapeBase):
    """
    The detailed description of the event. Included in the information returned by
    the DescribeEventDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "latest_description",
                "latestDescription",
                TypeInfo(str),
            ),
        ]

    # The most recent description of the event.
    latest_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventDetails(ShapeBase):
    """
    Detailed information about an event. A combination of an Event object, an
    EventDescription object, and additional metadata about the event. Returned by
    the DescribeEventDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event",
                "event",
                TypeInfo(Event),
            ),
            (
                "event_description",
                "eventDescription",
                TypeInfo(EventDescription),
            ),
            (
                "event_metadata",
                "eventMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Summary information about the event.
    event: "Event" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The most recent description of the event.
    event_description: "EventDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional metadata about the event.
    event_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventDetailsErrorItem(ShapeBase):
    """
    Error information returned when a DescribeEventDetails operation cannot find a
    specified event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arn",
                "eventArn",
                TypeInfo(str),
            ),
            (
                "error_name",
                "errorName",
                TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    event_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the error.
    error_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message that describes the error.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventFilter(ShapeBase):
    """
    The values to use to filter results from the DescribeEvents and
    DescribeEventAggregates operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_type_codes",
                "eventTypeCodes",
                TypeInfo(typing.List[str]),
            ),
            (
                "services",
                "services",
                TypeInfo(typing.List[str]),
            ),
            (
                "regions",
                "regions",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zones",
                "availabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "start_times",
                "startTimes",
                TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "end_times",
                "endTimes",
                TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "last_updated_times",
                "lastUpdatedTimes",
                TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "entity_arns",
                "entityArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "entity_values",
                "entityValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_type_categories",
                "eventTypeCategories",
                TypeInfo(typing.List[typing.Union[str, eventTypeCategory]]),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "event_status_codes",
                "eventStatusCodes",
                TypeInfo(typing.List[typing.Union[str, eventStatusCode]]),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of unique identifiers for event types. For example,
    # `"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"`
    event_type_codes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS services associated with the event. For example, `EC2`, `RDS`.
    services: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of AWS regions.
    regions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of AWS availability zones.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of dates and times that the event began.
    start_times: typing.List["DateTimeRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of dates and times that the event ended.
    end_times: typing.List["DateTimeRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of dates and times that the event was last updated.
    last_updated_times: typing.List["DateTimeRange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of entity ARNs (unique identifiers).
    entity_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of entity identifiers, such as EC2 instance IDs (`i-34ab692e`) or
    # EBS volumes (`vol-426ab23e`).
    entity_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event type category codes (`issue`, `scheduledChange`, or
    # `accountNotification`).
    event_type_categories: typing.List[typing.Union[str, "eventTypeCategory"]
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A map of entity tags attached to the affected entity.
    tags: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event status codes.
    event_status_codes: typing.List[typing.Union[str, "eventStatusCode"]
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class EventType(ShapeBase):
    """
    Metadata about a type of event that is reported by AWS Health. Data consists of
    the category (for example, `issue`), the service (for example, `EC2`), and the
    event type code (for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service",
                "service",
                TypeInfo(str),
            ),
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "category",
                "category",
                TypeInfo(typing.Union[str, eventTypeCategory]),
            ),
        ]

    # The AWS service that is affected by the event. For example, `EC2`, `RDS`.
    service: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the event type. The format is `AWS_ _SERVICE_ _
    # _DESCRIPTION_ `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event type category codes (`issue`, `scheduledChange`, or
    # `accountNotification`).
    category: typing.Union[str, "eventTypeCategory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventTypeFilter(ShapeBase):
    """
    The values to use to filter results from the DescribeEventTypes operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_type_codes",
                "eventTypeCodes",
                TypeInfo(typing.List[str]),
            ),
            (
                "services",
                "services",
                TypeInfo(typing.List[str]),
            ),
            (
                "event_type_categories",
                "eventTypeCategories",
                TypeInfo(typing.List[typing.Union[str, eventTypeCategory]]),
            ),
        ]

    # A list of event type codes.
    event_type_codes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS services associated with the event. For example, `EC2`, `RDS`.
    services: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of event type category codes (`issue`, `scheduledChange`, or
    # `accountNotification`).
    event_type_categories: typing.List[typing.Union[str, "eventTypeCategory"]
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class InvalidPaginationToken(ShapeBase):
    """
    The specified pagination token (`nextToken`) is not valid.
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
class UnsupportedLocale(ShapeBase):
    """
    The specified locale is not supported.
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


class entityStatusCode(str):
    IMPAIRED = "IMPAIRED"
    UNIMPAIRED = "UNIMPAIRED"
    UNKNOWN = "UNKNOWN"


class eventAggregateField(str):
    eventTypeCategory = "eventTypeCategory"


class eventStatusCode(str):
    open = "open"
    closed = "closed"
    upcoming = "upcoming"


class eventTypeCategory(str):
    issue = "issue"
    accountNotification = "accountNotification"
    scheduledChange = "scheduledChange"
