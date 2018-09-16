import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("xray", *args, **kwargs)

    def batch_get_traces(
        self,
        _request: shapes.BatchGetTracesRequest = None,
        *,
        trace_ids: typing.List[str],
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.BatchGetTracesResult:
        """
        Retrieves a list of traces specified by ID. Each trace is a collection of
        segment documents that originates from a single request. Use `GetTraceSummaries`
        to get a list of trace IDs.
        """
        if _request is None:
            _params = {}
            if trace_ids is not ShapeBase.NOT_SET:
                _params['trace_ids'] = trace_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.BatchGetTracesRequest(**_params)
        paginator = self.get_paginator("batch_get_traces").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.BatchGetTracesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.BatchGetTracesResult.from_boto(response)

    def create_sampling_rule(
        self,
        _request: shapes.CreateSamplingRuleRequest = None,
        *,
        sampling_rule: shapes.SamplingRule,
    ) -> shapes.CreateSamplingRuleResult:
        """
        Creates a rule to control sampling behavior for instrumented applications.
        Services retrieve rules with GetSamplingRules, and evaluate each rule in
        ascending order of _priority_ for each request. If a rule matches, the service
        records a trace, borrowing it from the reservoir size. After 10 seconds, the
        service reports back to X-Ray with GetSamplingTargets to get updated versions of
        each in-use rule. The updated rule contains a trace quota that the service can
        use instead of borrowing from the reservoir.
        """
        if _request is None:
            _params = {}
            if sampling_rule is not ShapeBase.NOT_SET:
                _params['sampling_rule'] = sampling_rule
            _request = shapes.CreateSamplingRuleRequest(**_params)
        response = self._boto_client.create_sampling_rule(**_request.to_boto())

        return shapes.CreateSamplingRuleResult.from_boto(response)

    def delete_sampling_rule(
        self,
        _request: shapes.DeleteSamplingRuleRequest = None,
        *,
        rule_name: str = ShapeBase.NOT_SET,
        rule_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteSamplingRuleResult:
        """
        Deletes a sampling rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            if rule_arn is not ShapeBase.NOT_SET:
                _params['rule_arn'] = rule_arn
            _request = shapes.DeleteSamplingRuleRequest(**_params)
        response = self._boto_client.delete_sampling_rule(**_request.to_boto())

        return shapes.DeleteSamplingRuleResult.from_boto(response)

    def get_encryption_config(
        self,
        _request: shapes.GetEncryptionConfigRequest = None,
    ) -> shapes.GetEncryptionConfigResult:
        """
        Retrieves the current encryption configuration for X-Ray data.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetEncryptionConfigRequest(**_params)
        response = self._boto_client.get_encryption_config(**_request.to_boto())

        return shapes.GetEncryptionConfigResult.from_boto(response)

    def get_sampling_rules(
        self,
        _request: shapes.GetSamplingRulesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSamplingRulesResult:
        """
        Retrieves all sampling rules.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetSamplingRulesRequest(**_params)
        response = self._boto_client.get_sampling_rules(**_request.to_boto())

        return shapes.GetSamplingRulesResult.from_boto(response)

    def get_sampling_statistic_summaries(
        self,
        _request: shapes.GetSamplingStatisticSummariesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSamplingStatisticSummariesResult:
        """
        Retrieves information about recent sampling results for all sampling rules.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetSamplingStatisticSummariesRequest(**_params)
        response = self._boto_client.get_sampling_statistic_summaries(
            **_request.to_boto()
        )

        return shapes.GetSamplingStatisticSummariesResult.from_boto(response)

    def get_sampling_targets(
        self,
        _request: shapes.GetSamplingTargetsRequest = None,
        *,
        sampling_statistics_documents: typing.List[shapes.
                                                   SamplingStatisticsDocument],
    ) -> shapes.GetSamplingTargetsResult:
        """
        Requests a sampling quota for rules that the service is using to sample
        requests.
        """
        if _request is None:
            _params = {}
            if sampling_statistics_documents is not ShapeBase.NOT_SET:
                _params['sampling_statistics_documents'
                       ] = sampling_statistics_documents
            _request = shapes.GetSamplingTargetsRequest(**_params)
        response = self._boto_client.get_sampling_targets(**_request.to_boto())

        return shapes.GetSamplingTargetsResult.from_boto(response)

    def get_service_graph(
        self,
        _request: shapes.GetServiceGraphRequest = None,
        *,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetServiceGraphResult:
        """
        Retrieves a document that describes services that process incoming requests, and
        downstream services that they call as a result. Root services process incoming
        requests and make calls to downstream services. Root services are applications
        that use the AWS X-Ray SDK. Downstream services can be other applications, AWS
        resources, HTTP web APIs, or SQL databases.
        """
        if _request is None:
            _params = {}
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetServiceGraphRequest(**_params)
        paginator = self.get_paginator("get_service_graph").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetServiceGraphResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetServiceGraphResult.from_boto(response)

    def get_trace_graph(
        self,
        _request: shapes.GetTraceGraphRequest = None,
        *,
        trace_ids: typing.List[str],
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTraceGraphResult:
        """
        Retrieves a service graph for one or more specific trace IDs.
        """
        if _request is None:
            _params = {}
            if trace_ids is not ShapeBase.NOT_SET:
                _params['trace_ids'] = trace_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetTraceGraphRequest(**_params)
        paginator = self.get_paginator("get_trace_graph").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTraceGraphResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTraceGraphResult.from_boto(response)

    def get_trace_summaries(
        self,
        _request: shapes.GetTraceSummariesRequest = None,
        *,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        sampling: bool = ShapeBase.NOT_SET,
        filter_expression: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetTraceSummariesResult:
        """
        Retrieves IDs and metadata for traces available for a specified time frame using
        an optional filter. To get the full traces, pass the trace IDs to
        `BatchGetTraces`.

        A filter expression can target traced requests that hit specific service nodes
        or edges, have errors, or come from a known user. For example, the following
        filter expression targets traces that pass through `api.example.com`:

        `service("api.example.com")`

        This filter expression finds traces that have an annotation named `account` with
        the value `12345`:

        `annotation.account = "12345"`

        For a full list of indexed fields and keywords that you can use in filter
        expressions, see [Using Filter
        Expressions](http://docs.aws.amazon.com/xray/latest/devguide/xray-console-
        filters.html) in the _AWS X-Ray Developer Guide_.
        """
        if _request is None:
            _params = {}
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if sampling is not ShapeBase.NOT_SET:
                _params['sampling'] = sampling
            if filter_expression is not ShapeBase.NOT_SET:
                _params['filter_expression'] = filter_expression
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetTraceSummariesRequest(**_params)
        paginator = self.get_paginator("get_trace_summaries").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetTraceSummariesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetTraceSummariesResult.from_boto(response)

    def put_encryption_config(
        self,
        _request: shapes.PutEncryptionConfigRequest = None,
        *,
        type: typing.Union[str, shapes.EncryptionType],
        key_id: str = ShapeBase.NOT_SET,
    ) -> shapes.PutEncryptionConfigResult:
        """
        Updates the encryption configuration for X-Ray data.
        """
        if _request is None:
            _params = {}
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            _request = shapes.PutEncryptionConfigRequest(**_params)
        response = self._boto_client.put_encryption_config(**_request.to_boto())

        return shapes.PutEncryptionConfigResult.from_boto(response)

    def put_telemetry_records(
        self,
        _request: shapes.PutTelemetryRecordsRequest = None,
        *,
        telemetry_records: typing.List[shapes.TelemetryRecord],
        ec2_instance_id: str = ShapeBase.NOT_SET,
        hostname: str = ShapeBase.NOT_SET,
        resource_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.PutTelemetryRecordsResult:
        """
        Used by the AWS X-Ray daemon to upload telemetry.
        """
        if _request is None:
            _params = {}
            if telemetry_records is not ShapeBase.NOT_SET:
                _params['telemetry_records'] = telemetry_records
            if ec2_instance_id is not ShapeBase.NOT_SET:
                _params['ec2_instance_id'] = ec2_instance_id
            if hostname is not ShapeBase.NOT_SET:
                _params['hostname'] = hostname
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.PutTelemetryRecordsRequest(**_params)
        response = self._boto_client.put_telemetry_records(**_request.to_boto())

        return shapes.PutTelemetryRecordsResult.from_boto(response)

    def put_trace_segments(
        self,
        _request: shapes.PutTraceSegmentsRequest = None,
        *,
        trace_segment_documents: typing.List[str],
    ) -> shapes.PutTraceSegmentsResult:
        """
        Uploads segment documents to AWS X-Ray. The X-Ray SDK generates segment
        documents and sends them to the X-Ray daemon, which uploads them in batches. A
        segment document can be a completed segment, an in-progress segment, or an array
        of subsegments.

        Segments must include the following fields. For the full segment document
        schema, see [AWS X-Ray Segment
        Documents](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-
        segmentdocuments.html) in the _AWS X-Ray Developer Guide_.

        **Required Segment Document Fields**

          * `name` \- The name of the service that handled the request.

          * `id` \- A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits.

          * `trace_id` \- A unique identifier that connects all segments and subsegments originating from a single client request.

          * `start_time` \- Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, `1480615200.010` or `1.480615200010E9`.

          * `end_time` \- Time the segment or subsegment was closed. For example, `1480615200.090` or `1.480615200090E9`. Specify either an `end_time` or `in_progress`.

          * `in_progress` \- Set to `true` instead of specifying an `end_time` to record that a segment has been started, but is not complete. Send an in progress segment when your application receives a request that will take a long time to serve, to trace the fact that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment.

        A `trace_id` consists of three numbers separated by hyphens. For example,
        1-58406520-a006649127e371903a2de979. This includes:

        **Trace ID Format**

          * The version number, i.e. `1`.

          * The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is `1480615200` seconds, or `58406520` in hexadecimal.

          * A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.
        """
        if _request is None:
            _params = {}
            if trace_segment_documents is not ShapeBase.NOT_SET:
                _params['trace_segment_documents'] = trace_segment_documents
            _request = shapes.PutTraceSegmentsRequest(**_params)
        response = self._boto_client.put_trace_segments(**_request.to_boto())

        return shapes.PutTraceSegmentsResult.from_boto(response)

    def update_sampling_rule(
        self,
        _request: shapes.UpdateSamplingRuleRequest = None,
        *,
        sampling_rule_update: shapes.SamplingRuleUpdate,
    ) -> shapes.UpdateSamplingRuleResult:
        """
        Modifies a sampling rule's configuration.
        """
        if _request is None:
            _params = {}
            if sampling_rule_update is not ShapeBase.NOT_SET:
                _params['sampling_rule_update'] = sampling_rule_update
            _request = shapes.UpdateSamplingRuleRequest(**_params)
        response = self._boto_client.update_sampling_rule(**_request.to_boto())

        return shapes.UpdateSamplingRuleResult.from_boto(response)
