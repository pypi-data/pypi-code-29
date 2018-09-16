import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("config", *args, **kwargs)

    def batch_get_resource_config(
        self,
        _request: shapes.BatchGetResourceConfigRequest = None,
        *,
        resource_keys: typing.List[shapes.ResourceKey],
    ) -> shapes.BatchGetResourceConfigResponse:
        """
        Returns the current configuration for one or more requested resources. The
        operation also returns a list of resources that are not processed in the current
        request. If there are no unprocessed resources, the operation returns an empty
        unprocessedResourceKeys list.

          * The API does not return results for deleted resources.

          * The API does not return any tags for the requested resources. This information is filtered out of the supplementaryConfiguration section of the API response.
        """
        if _request is None:
            _params = {}
            if resource_keys is not ShapeBase.NOT_SET:
                _params['resource_keys'] = resource_keys
            _request = shapes.BatchGetResourceConfigRequest(**_params)
        response = self._boto_client.batch_get_resource_config(
            **_request.to_boto()
        )

        return shapes.BatchGetResourceConfigResponse.from_boto(response)

    def delete_aggregation_authorization(
        self,
        _request: shapes.DeleteAggregationAuthorizationRequest = None,
        *,
        authorized_account_id: str,
        authorized_aws_region: str,
    ) -> None:
        """
        Deletes the authorization granted to the specified configuration aggregator
        account in a specified region.
        """
        if _request is None:
            _params = {}
            if authorized_account_id is not ShapeBase.NOT_SET:
                _params['authorized_account_id'] = authorized_account_id
            if authorized_aws_region is not ShapeBase.NOT_SET:
                _params['authorized_aws_region'] = authorized_aws_region
            _request = shapes.DeleteAggregationAuthorizationRequest(**_params)
        response = self._boto_client.delete_aggregation_authorization(
            **_request.to_boto()
        )

    def delete_config_rule(
        self,
        _request: shapes.DeleteConfigRuleRequest = None,
        *,
        config_rule_name: str,
    ) -> None:
        """
        Deletes the specified AWS Config rule and all of its evaluation results.

        AWS Config sets the state of a rule to `DELETING` until the deletion is
        complete. You cannot update a rule while it is in this state. If you make a
        `PutConfigRule` or `DeleteConfigRule` request for the rule, you will receive a
        `ResourceInUseException`.

        You can check the state of a rule by using the `DescribeConfigRules` request.
        """
        if _request is None:
            _params = {}
            if config_rule_name is not ShapeBase.NOT_SET:
                _params['config_rule_name'] = config_rule_name
            _request = shapes.DeleteConfigRuleRequest(**_params)
        response = self._boto_client.delete_config_rule(**_request.to_boto())

    def delete_configuration_aggregator(
        self,
        _request: shapes.DeleteConfigurationAggregatorRequest = None,
        *,
        configuration_aggregator_name: str,
    ) -> None:
        """
        Deletes the specified configuration aggregator and the aggregated data
        associated with the aggregator.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_name is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_name'
                       ] = configuration_aggregator_name
            _request = shapes.DeleteConfigurationAggregatorRequest(**_params)
        response = self._boto_client.delete_configuration_aggregator(
            **_request.to_boto()
        )

    def delete_configuration_recorder(
        self,
        _request: shapes.DeleteConfigurationRecorderRequest = None,
        *,
        configuration_recorder_name: str,
    ) -> None:
        """
        Deletes the configuration recorder.

        After the configuration recorder is deleted, AWS Config will not record resource
        configuration changes until you create a new configuration recorder.

        This action does not delete the configuration information that was previously
        recorded. You will be able to access the previously recorded information by
        using the `GetResourceConfigHistory` action, but you will not be able to access
        this information in the AWS Config console until you create a new configuration
        recorder.
        """
        if _request is None:
            _params = {}
            if configuration_recorder_name is not ShapeBase.NOT_SET:
                _params['configuration_recorder_name'
                       ] = configuration_recorder_name
            _request = shapes.DeleteConfigurationRecorderRequest(**_params)
        response = self._boto_client.delete_configuration_recorder(
            **_request.to_boto()
        )

    def delete_delivery_channel(
        self,
        _request: shapes.DeleteDeliveryChannelRequest = None,
        *,
        delivery_channel_name: str,
    ) -> None:
        """
        Deletes the delivery channel.

        Before you can delete the delivery channel, you must stop the configuration
        recorder by using the StopConfigurationRecorder action.
        """
        if _request is None:
            _params = {}
            if delivery_channel_name is not ShapeBase.NOT_SET:
                _params['delivery_channel_name'] = delivery_channel_name
            _request = shapes.DeleteDeliveryChannelRequest(**_params)
        response = self._boto_client.delete_delivery_channel(
            **_request.to_boto()
        )

    def delete_evaluation_results(
        self,
        _request: shapes.DeleteEvaluationResultsRequest = None,
        *,
        config_rule_name: str,
    ) -> shapes.DeleteEvaluationResultsResponse:
        """
        Deletes the evaluation results for the specified AWS Config rule. You can
        specify one AWS Config rule per request. After you delete the evaluation
        results, you can call the StartConfigRulesEvaluation API to start evaluating
        your AWS resources against the rule.
        """
        if _request is None:
            _params = {}
            if config_rule_name is not ShapeBase.NOT_SET:
                _params['config_rule_name'] = config_rule_name
            _request = shapes.DeleteEvaluationResultsRequest(**_params)
        response = self._boto_client.delete_evaluation_results(
            **_request.to_boto()
        )

        return shapes.DeleteEvaluationResultsResponse.from_boto(response)

    def delete_pending_aggregation_request(
        self,
        _request: shapes.DeletePendingAggregationRequestRequest = None,
        *,
        requester_account_id: str,
        requester_aws_region: str,
    ) -> None:
        """
        Deletes pending authorization requests for a specified aggregator account in a
        specified region.
        """
        if _request is None:
            _params = {}
            if requester_account_id is not ShapeBase.NOT_SET:
                _params['requester_account_id'] = requester_account_id
            if requester_aws_region is not ShapeBase.NOT_SET:
                _params['requester_aws_region'] = requester_aws_region
            _request = shapes.DeletePendingAggregationRequestRequest(**_params)
        response = self._boto_client.delete_pending_aggregation_request(
            **_request.to_boto()
        )

    def delete_retention_configuration(
        self,
        _request: shapes.DeleteRetentionConfigurationRequest = None,
        *,
        retention_configuration_name: str,
    ) -> None:
        """
        Deletes the retention configuration.
        """
        if _request is None:
            _params = {}
            if retention_configuration_name is not ShapeBase.NOT_SET:
                _params['retention_configuration_name'
                       ] = retention_configuration_name
            _request = shapes.DeleteRetentionConfigurationRequest(**_params)
        response = self._boto_client.delete_retention_configuration(
            **_request.to_boto()
        )

    def deliver_config_snapshot(
        self,
        _request: shapes.DeliverConfigSnapshotRequest = None,
        *,
        delivery_channel_name: str,
    ) -> shapes.DeliverConfigSnapshotResponse:
        """
        Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the
        specified delivery channel. After the delivery has started, AWS Config sends the
        following notifications using an Amazon SNS topic that you have specified.

          * Notification of the start of the delivery.

          * Notification of the completion of the delivery, if the delivery was successfully completed.

          * Notification of delivery failure, if the delivery failed.
        """
        if _request is None:
            _params = {}
            if delivery_channel_name is not ShapeBase.NOT_SET:
                _params['delivery_channel_name'] = delivery_channel_name
            _request = shapes.DeliverConfigSnapshotRequest(**_params)
        response = self._boto_client.deliver_config_snapshot(
            **_request.to_boto()
        )

        return shapes.DeliverConfigSnapshotResponse.from_boto(response)

    def describe_aggregate_compliance_by_config_rules(
        self,
        _request: shapes.DescribeAggregateComplianceByConfigRulesRequest = None,
        *,
        configuration_aggregator_name: str,
        filters: shapes.ConfigRuleComplianceFilters = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAggregateComplianceByConfigRulesResponse:
        """
        Returns a list of compliant and noncompliant rules with the number of resources
        for compliant and noncompliant rules.

        The results can return an empty result page, but if you have a nextToken, the
        results are displayed on the next page.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_name is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_name'
                       ] = configuration_aggregator_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAggregateComplianceByConfigRulesRequest(
                **_params
            )
        response = self._boto_client.describe_aggregate_compliance_by_config_rules(
            **_request.to_boto()
        )

        return shapes.DescribeAggregateComplianceByConfigRulesResponse.from_boto(
            response
        )

    def describe_aggregation_authorizations(
        self,
        _request: shapes.DescribeAggregationAuthorizationsRequest = None,
        *,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAggregationAuthorizationsResponse:
        """
        Returns a list of authorizations granted to various aggregator accounts and
        regions.
        """
        if _request is None:
            _params = {}
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAggregationAuthorizationsRequest(
                **_params
            )
        response = self._boto_client.describe_aggregation_authorizations(
            **_request.to_boto()
        )

        return shapes.DescribeAggregationAuthorizationsResponse.from_boto(
            response
        )

    def describe_compliance_by_config_rule(
        self,
        _request: shapes.DescribeComplianceByConfigRuleRequest = None,
        *,
        config_rule_names: typing.List[str] = ShapeBase.NOT_SET,
        compliance_types: typing.List[typing.Union[str, shapes.ComplianceType]
                                     ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeComplianceByConfigRuleResponse:
        """
        Indicates whether the specified AWS Config rules are compliant. If a rule is
        noncompliant, this action returns the number of AWS resources that do not comply
        with the rule.

        A rule is compliant if all of the evaluated resources comply with it. It is
        noncompliant if any of these resources do not comply.

        If AWS Config has no current evaluation results for the rule, it returns
        `INSUFFICIENT_DATA`. This result might indicate one of the following conditions:

          * AWS Config has never invoked an evaluation for the rule. To check whether it has, use the `DescribeConfigRuleEvaluationStatus` action to get the `LastSuccessfulInvocationTime` and `LastFailedInvocationTime`.

          * The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role you assigned to your configuration recorder includes the `config:PutEvaluations` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the `config:PutEvaluations` permission.

          * The rule's AWS Lambda function has returned `NOT_APPLICABLE` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope.
        """
        if _request is None:
            _params = {}
            if config_rule_names is not ShapeBase.NOT_SET:
                _params['config_rule_names'] = config_rule_names
            if compliance_types is not ShapeBase.NOT_SET:
                _params['compliance_types'] = compliance_types
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeComplianceByConfigRuleRequest(**_params)
        paginator = self.get_paginator("describe_compliance_by_config_rule"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeComplianceByConfigRuleResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeComplianceByConfigRuleResponse.from_boto(response)

    def describe_compliance_by_resource(
        self,
        _request: shapes.DescribeComplianceByResourceRequest = None,
        *,
        resource_type: str = ShapeBase.NOT_SET,
        resource_id: str = ShapeBase.NOT_SET,
        compliance_types: typing.List[typing.Union[str, shapes.ComplianceType]
                                     ] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeComplianceByResourceResponse:
        """
        Indicates whether the specified AWS resources are compliant. If a resource is
        noncompliant, this action returns the number of AWS Config rules that the
        resource does not comply with.

        A resource is compliant if it complies with all the AWS Config rules that
        evaluate it. It is noncompliant if it does not comply with one or more of these
        rules.

        If AWS Config has no current evaluation results for the resource, it returns
        `INSUFFICIENT_DATA`. This result might indicate one of the following conditions
        about the rules that evaluate the resource:

          * AWS Config has never invoked an evaluation for the rule. To check whether it has, use the `DescribeConfigRuleEvaluationStatus` action to get the `LastSuccessfulInvocationTime` and `LastFailedInvocationTime`.

          * The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role that you assigned to your configuration recorder includes the `config:PutEvaluations` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the `config:PutEvaluations` permission.

          * The rule's AWS Lambda function has returned `NOT_APPLICABLE` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if compliance_types is not ShapeBase.NOT_SET:
                _params['compliance_types'] = compliance_types
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeComplianceByResourceRequest(**_params)
        paginator = self.get_paginator("describe_compliance_by_resource"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeComplianceByResourceResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeComplianceByResourceResponse.from_boto(response)

    def describe_config_rule_evaluation_status(
        self,
        _request: shapes.DescribeConfigRuleEvaluationStatusRequest = None,
        *,
        config_rule_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigRuleEvaluationStatusResponse:
        """
        Returns status information for each of your AWS managed Config rules. The status
        includes information such as the last time AWS Config invoked the rule, the last
        time AWS Config failed to invoke the rule, and the related error for the last
        failure.
        """
        if _request is None:
            _params = {}
            if config_rule_names is not ShapeBase.NOT_SET:
                _params['config_rule_names'] = config_rule_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeConfigRuleEvaluationStatusRequest(
                **_params
            )
        response = self._boto_client.describe_config_rule_evaluation_status(
            **_request.to_boto()
        )

        return shapes.DescribeConfigRuleEvaluationStatusResponse.from_boto(
            response
        )

    def describe_config_rules(
        self,
        _request: shapes.DescribeConfigRulesRequest = None,
        *,
        config_rule_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigRulesResponse:
        """
        Returns details about your AWS Config rules.
        """
        if _request is None:
            _params = {}
            if config_rule_names is not ShapeBase.NOT_SET:
                _params['config_rule_names'] = config_rule_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeConfigRulesRequest(**_params)
        paginator = self.get_paginator("describe_config_rules").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeConfigRulesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeConfigRulesResponse.from_boto(response)

    def describe_configuration_aggregator_sources_status(
        self,
        _request: shapes.
        DescribeConfigurationAggregatorSourcesStatusRequest = None,
        *,
        configuration_aggregator_name: str,
        update_status: typing.List[typing.Union[str, shapes.
                                                AggregatedSourceStatusType]
                                  ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigurationAggregatorSourcesStatusResponse:
        """
        Returns status information for sources within an aggregator. The status includes
        information about the last time AWS Config aggregated data from source accounts
        or AWS Config failed to aggregate data from source accounts with the related
        error code or message.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_name is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_name'
                       ] = configuration_aggregator_name
            if update_status is not ShapeBase.NOT_SET:
                _params['update_status'] = update_status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeConfigurationAggregatorSourcesStatusRequest(
                **_params
            )
        response = self._boto_client.describe_configuration_aggregator_sources_status(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationAggregatorSourcesStatusResponse.from_boto(
            response
        )

    def describe_configuration_aggregators(
        self,
        _request: shapes.DescribeConfigurationAggregatorsRequest = None,
        *,
        configuration_aggregator_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigurationAggregatorsResponse:
        """
        Returns the details of one or more configuration aggregators. If the
        configuration aggregator is not specified, this action returns the details for
        all the configuration aggregators associated with the account.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_names is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_names'
                       ] = configuration_aggregator_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeConfigurationAggregatorsRequest(**_params)
        response = self._boto_client.describe_configuration_aggregators(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationAggregatorsResponse.from_boto(
            response
        )

    def describe_configuration_recorder_status(
        self,
        _request: shapes.DescribeConfigurationRecorderStatusRequest = None,
        *,
        configuration_recorder_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigurationRecorderStatusResponse:
        """
        Returns the current status of the specified configuration recorder. If a
        configuration recorder is not specified, this action returns the status of all
        configuration recorders associated with the account.

        Currently, you can specify only one configuration recorder per region in your
        account.
        """
        if _request is None:
            _params = {}
            if configuration_recorder_names is not ShapeBase.NOT_SET:
                _params['configuration_recorder_names'
                       ] = configuration_recorder_names
            _request = shapes.DescribeConfigurationRecorderStatusRequest(
                **_params
            )
        response = self._boto_client.describe_configuration_recorder_status(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationRecorderStatusResponse.from_boto(
            response
        )

    def describe_configuration_recorders(
        self,
        _request: shapes.DescribeConfigurationRecordersRequest = None,
        *,
        configuration_recorder_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigurationRecordersResponse:
        """
        Returns the details for the specified configuration recorders. If the
        configuration recorder is not specified, this action returns the details for all
        configuration recorders associated with the account.

        Currently, you can specify only one configuration recorder per region in your
        account.
        """
        if _request is None:
            _params = {}
            if configuration_recorder_names is not ShapeBase.NOT_SET:
                _params['configuration_recorder_names'
                       ] = configuration_recorder_names
            _request = shapes.DescribeConfigurationRecordersRequest(**_params)
        response = self._boto_client.describe_configuration_recorders(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationRecordersResponse.from_boto(response)

    def describe_delivery_channel_status(
        self,
        _request: shapes.DescribeDeliveryChannelStatusRequest = None,
        *,
        delivery_channel_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDeliveryChannelStatusResponse:
        """
        Returns the current status of the specified delivery channel. If a delivery
        channel is not specified, this action returns the current status of all delivery
        channels associated with the account.

        Currently, you can specify only one delivery channel per region in your account.
        """
        if _request is None:
            _params = {}
            if delivery_channel_names is not ShapeBase.NOT_SET:
                _params['delivery_channel_names'] = delivery_channel_names
            _request = shapes.DescribeDeliveryChannelStatusRequest(**_params)
        response = self._boto_client.describe_delivery_channel_status(
            **_request.to_boto()
        )

        return shapes.DescribeDeliveryChannelStatusResponse.from_boto(response)

    def describe_delivery_channels(
        self,
        _request: shapes.DescribeDeliveryChannelsRequest = None,
        *,
        delivery_channel_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDeliveryChannelsResponse:
        """
        Returns details about the specified delivery channel. If a delivery channel is
        not specified, this action returns the details of all delivery channels
        associated with the account.

        Currently, you can specify only one delivery channel per region in your account.
        """
        if _request is None:
            _params = {}
            if delivery_channel_names is not ShapeBase.NOT_SET:
                _params['delivery_channel_names'] = delivery_channel_names
            _request = shapes.DescribeDeliveryChannelsRequest(**_params)
        response = self._boto_client.describe_delivery_channels(
            **_request.to_boto()
        )

        return shapes.DescribeDeliveryChannelsResponse.from_boto(response)

    def describe_pending_aggregation_requests(
        self,
        _request: shapes.DescribePendingAggregationRequestsRequest = None,
        *,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePendingAggregationRequestsResponse:
        """
        Returns a list of all pending aggregation requests.
        """
        if _request is None:
            _params = {}
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribePendingAggregationRequestsRequest(
                **_params
            )
        response = self._boto_client.describe_pending_aggregation_requests(
            **_request.to_boto()
        )

        return shapes.DescribePendingAggregationRequestsResponse.from_boto(
            response
        )

    def describe_retention_configurations(
        self,
        _request: shapes.DescribeRetentionConfigurationsRequest = None,
        *,
        retention_configuration_names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRetentionConfigurationsResponse:
        """
        Returns the details of one or more retention configurations. If the retention
        configuration name is not specified, this action returns the details for all the
        retention configurations for that account.

        Currently, AWS Config supports only one retention configuration per region in
        your account.
        """
        if _request is None:
            _params = {}
            if retention_configuration_names is not ShapeBase.NOT_SET:
                _params['retention_configuration_names'
                       ] = retention_configuration_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeRetentionConfigurationsRequest(**_params)
        response = self._boto_client.describe_retention_configurations(
            **_request.to_boto()
        )

        return shapes.DescribeRetentionConfigurationsResponse.from_boto(
            response
        )

    def get_aggregate_compliance_details_by_config_rule(
        self,
        _request: shapes.
        GetAggregateComplianceDetailsByConfigRuleRequest = None,
        *,
        configuration_aggregator_name: str,
        config_rule_name: str,
        account_id: str,
        aws_region: str,
        compliance_type: typing.Union[str, shapes.
                                      ComplianceType] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetAggregateComplianceDetailsByConfigRuleResponse:
        """
        Returns the evaluation results for the specified AWS Config rule for a specific
        resource in a rule. The results indicate which AWS resources were evaluated by
        the rule, when each resource was last evaluated, and whether each resource
        complies with the rule.

        The results can return an empty result page. But if you have a nextToken, the
        results are displayed on the next page.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_name is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_name'
                       ] = configuration_aggregator_name
            if config_rule_name is not ShapeBase.NOT_SET:
                _params['config_rule_name'] = config_rule_name
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if aws_region is not ShapeBase.NOT_SET:
                _params['aws_region'] = aws_region
            if compliance_type is not ShapeBase.NOT_SET:
                _params['compliance_type'] = compliance_type
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetAggregateComplianceDetailsByConfigRuleRequest(
                **_params
            )
        response = self._boto_client.get_aggregate_compliance_details_by_config_rule(
            **_request.to_boto()
        )

        return shapes.GetAggregateComplianceDetailsByConfigRuleResponse.from_boto(
            response
        )

    def get_aggregate_config_rule_compliance_summary(
        self,
        _request: shapes.GetAggregateConfigRuleComplianceSummaryRequest = None,
        *,
        configuration_aggregator_name: str,
        filters: shapes.ConfigRuleComplianceSummaryFilters = ShapeBase.NOT_SET,
        group_by_key: typing.
        Union[str, shapes.
              ConfigRuleComplianceSummaryGroupKey] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetAggregateConfigRuleComplianceSummaryResponse:
        """
        Returns the number of compliant and noncompliant rules for one or more accounts
        and regions in an aggregator.

        The results can return an empty result page, but if you have a nextToken, the
        results are displayed on the next page.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_name is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_name'
                       ] = configuration_aggregator_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if group_by_key is not ShapeBase.NOT_SET:
                _params['group_by_key'] = group_by_key
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetAggregateConfigRuleComplianceSummaryRequest(
                **_params
            )
        response = self._boto_client.get_aggregate_config_rule_compliance_summary(
            **_request.to_boto()
        )

        return shapes.GetAggregateConfigRuleComplianceSummaryResponse.from_boto(
            response
        )

    def get_compliance_details_by_config_rule(
        self,
        _request: shapes.GetComplianceDetailsByConfigRuleRequest = None,
        *,
        config_rule_name: str,
        compliance_types: typing.List[typing.Union[str, shapes.ComplianceType]
                                     ] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetComplianceDetailsByConfigRuleResponse:
        """
        Returns the evaluation results for the specified AWS Config rule. The results
        indicate which AWS resources were evaluated by the rule, when each resource was
        last evaluated, and whether each resource complies with the rule.
        """
        if _request is None:
            _params = {}
            if config_rule_name is not ShapeBase.NOT_SET:
                _params['config_rule_name'] = config_rule_name
            if compliance_types is not ShapeBase.NOT_SET:
                _params['compliance_types'] = compliance_types
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetComplianceDetailsByConfigRuleRequest(**_params)
        paginator = self.get_paginator("get_compliance_details_by_config_rule"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetComplianceDetailsByConfigRuleResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.GetComplianceDetailsByConfigRuleResponse.from_boto(
            response
        )

    def get_compliance_details_by_resource(
        self,
        _request: shapes.GetComplianceDetailsByResourceRequest = None,
        *,
        resource_type: str,
        resource_id: str,
        compliance_types: typing.List[typing.Union[str, shapes.ComplianceType]
                                     ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetComplianceDetailsByResourceResponse:
        """
        Returns the evaluation results for the specified AWS resource. The results
        indicate which AWS Config rules were used to evaluate the resource, when each
        rule was last used, and whether the resource complies with each rule.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if compliance_types is not ShapeBase.NOT_SET:
                _params['compliance_types'] = compliance_types
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetComplianceDetailsByResourceRequest(**_params)
        paginator = self.get_paginator("get_compliance_details_by_resource"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetComplianceDetailsByResourceResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.GetComplianceDetailsByResourceResponse.from_boto(response)

    def get_compliance_summary_by_config_rule(
        self,
    ) -> shapes.GetComplianceSummaryByConfigRuleResponse:
        """
        Returns the number of AWS Config rules that are compliant and noncompliant, up
        to a maximum of 25 for each.
        """
        response = self._boto_client.get_compliance_summary_by_config_rule()

        return shapes.GetComplianceSummaryByConfigRuleResponse.from_boto(
            response
        )

    def get_compliance_summary_by_resource_type(
        self,
        _request: shapes.GetComplianceSummaryByResourceTypeRequest = None,
        *,
        resource_types: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GetComplianceSummaryByResourceTypeResponse:
        """
        Returns the number of resources that are compliant and the number that are
        noncompliant. You can specify one or more resource types to get these numbers
        for each resource type. The maximum number returned is 100.
        """
        if _request is None:
            _params = {}
            if resource_types is not ShapeBase.NOT_SET:
                _params['resource_types'] = resource_types
            _request = shapes.GetComplianceSummaryByResourceTypeRequest(
                **_params
            )
        response = self._boto_client.get_compliance_summary_by_resource_type(
            **_request.to_boto()
        )

        return shapes.GetComplianceSummaryByResourceTypeResponse.from_boto(
            response
        )

    def get_discovered_resource_counts(
        self,
        _request: shapes.GetDiscoveredResourceCountsRequest = None,
        *,
        resource_types: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDiscoveredResourceCountsResponse:
        """
        Returns the resource types, the number of each resource type, and the total
        number of resources that AWS Config is recording in this region for your AWS
        account.

        **Example**

          1. AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets.

          2. You make a call to the `GetDiscoveredResourceCounts` action and specify that you want all resource types. 

          3. AWS Config returns the following:

            * The resource types (EC2 instances, IAM users, and S3 buckets).

            * The number of each resource type (25, 20, and 15).

            * The total number of all resources (60).

        The response is paginated. By default, AWS Config lists 100 ResourceCount
        objects on each page. You can customize this number with the `limit` parameter.
        The response includes a `nextToken` string. To get the next page of results, run
        the request again and specify the string for the `nextToken` parameter.

        If you make a call to the GetDiscoveredResourceCounts action, you might not
        immediately receive resource counts in the following situations:

          * You are a new AWS Config customer.

          * You just enabled resource recording.

        It might take a few minutes for AWS Config to record and count your resources.
        Wait a few minutes and then retry the GetDiscoveredResourceCounts action.
        """
        if _request is None:
            _params = {}
            if resource_types is not ShapeBase.NOT_SET:
                _params['resource_types'] = resource_types
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetDiscoveredResourceCountsRequest(**_params)
        response = self._boto_client.get_discovered_resource_counts(
            **_request.to_boto()
        )

        return shapes.GetDiscoveredResourceCountsResponse.from_boto(response)

    def get_resource_config_history(
        self,
        _request: shapes.GetResourceConfigHistoryRequest = None,
        *,
        resource_type: typing.Union[str, shapes.ResourceType],
        resource_id: str,
        later_time: datetime.datetime = ShapeBase.NOT_SET,
        earlier_time: datetime.datetime = ShapeBase.NOT_SET,
        chronological_order: typing.
        Union[str, shapes.ChronologicalOrder] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetResourceConfigHistoryResponse:
        """
        Returns a list of configuration items for the specified resource. The list
        contains details about each state of the resource during the specified time
        interval. If you specified a retention period to retain your
        `ConfigurationItems` between a minimum of 30 days and a maximum of 7 years (2557
        days), AWS Config returns the `ConfigurationItems` for the specified retention
        period.

        The response is paginated. By default, AWS Config returns a limit of 10
        configuration items per page. You can customize this number with the `limit`
        parameter. The response includes a `nextToken` string. To get the next page of
        results, run the request again and specify the string for the `nextToken`
        parameter.

        Each call to the API is limited to span a duration of seven days. It is likely
        that the number of records returned is smaller than the specified `limit`. In
        such cases, you can make another call, using the `nextToken`.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if later_time is not ShapeBase.NOT_SET:
                _params['later_time'] = later_time
            if earlier_time is not ShapeBase.NOT_SET:
                _params['earlier_time'] = earlier_time
            if chronological_order is not ShapeBase.NOT_SET:
                _params['chronological_order'] = chronological_order
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetResourceConfigHistoryRequest(**_params)
        paginator = self.get_paginator("get_resource_config_history").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetResourceConfigHistoryResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetResourceConfigHistoryResponse.from_boto(response)

    def list_discovered_resources(
        self,
        _request: shapes.ListDiscoveredResourcesRequest = None,
        *,
        resource_type: typing.Union[str, shapes.ResourceType],
        resource_ids: typing.List[str] = ShapeBase.NOT_SET,
        resource_name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        include_deleted_resources: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDiscoveredResourcesResponse:
        """
        Accepts a resource type and returns a list of resource identifiers for the
        resources of that type. A resource identifier includes the resource type, ID,
        and (if available) the custom resource name. The results consist of resources
        that AWS Config has discovered, including those that AWS Config is not currently
        recording. You can narrow the results to include only resources that have
        specific resource IDs or a resource name.

        You can specify either resource IDs or a resource name, but not both, in the
        same request.

        The response is paginated. By default, AWS Config lists 100 resource identifiers
        on each page. You can customize this number with the `limit` parameter. The
        response includes a `nextToken` string. To get the next page of results, run the
        request again and specify the string for the `nextToken` parameter.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_ids is not ShapeBase.NOT_SET:
                _params['resource_ids'] = resource_ids
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if include_deleted_resources is not ShapeBase.NOT_SET:
                _params['include_deleted_resources'] = include_deleted_resources
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDiscoveredResourcesRequest(**_params)
        paginator = self.get_paginator("list_discovered_resources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDiscoveredResourcesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDiscoveredResourcesResponse.from_boto(response)

    def put_aggregation_authorization(
        self,
        _request: shapes.PutAggregationAuthorizationRequest = None,
        *,
        authorized_account_id: str,
        authorized_aws_region: str,
    ) -> shapes.PutAggregationAuthorizationResponse:
        """
        Authorizes the aggregator account and region to collect data from the source
        account and region.
        """
        if _request is None:
            _params = {}
            if authorized_account_id is not ShapeBase.NOT_SET:
                _params['authorized_account_id'] = authorized_account_id
            if authorized_aws_region is not ShapeBase.NOT_SET:
                _params['authorized_aws_region'] = authorized_aws_region
            _request = shapes.PutAggregationAuthorizationRequest(**_params)
        response = self._boto_client.put_aggregation_authorization(
            **_request.to_boto()
        )

        return shapes.PutAggregationAuthorizationResponse.from_boto(response)

    def put_config_rule(
        self,
        _request: shapes.PutConfigRuleRequest = None,
        *,
        config_rule: shapes.ConfigRule,
    ) -> None:
        """
        Adds or updates an AWS Config rule for evaluating whether your AWS resources
        comply with your desired configurations.

        You can use this action for custom AWS Config rules and AWS managed Config
        rules. A custom AWS Config rule is a rule that you develop and maintain. An AWS
        managed Config rule is a customizable, predefined rule that AWS Config provides.

        If you are adding a new custom AWS Config rule, you must first create the AWS
        Lambda function that the rule invokes to evaluate your resources. When you use
        the `PutConfigRule` action to add the rule to AWS Config, you must specify the
        Amazon Resource Name (ARN) that AWS Lambda assigns to the function. Specify the
        ARN for the `SourceIdentifier` key. This key is part of the `Source` object,
        which is part of the `ConfigRule` object.

        If you are adding an AWS managed Config rule, specify the rule's identifier for
        the `SourceIdentifier` key. To reference AWS managed Config rule identifiers,
        see [About AWS Managed Config
        Rules](http://docs.aws.amazon.com/config/latest/developerguide/evaluate-
        config_use-managed-rules.html).

        For any new rule that you add, specify the `ConfigRuleName` in the `ConfigRule`
        object. Do not specify the `ConfigRuleArn` or the `ConfigRuleId`. These values
        are generated by AWS Config for new rules.

        If you are updating a rule that you added previously, you can specify the rule
        by `ConfigRuleName`, `ConfigRuleId`, or `ConfigRuleArn` in the `ConfigRule` data
        type that you use in this request.

        The maximum number of rules that AWS Config supports is 50.

        For information about requesting a rule limit increase, see [AWS Config
        Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config)
        in the _AWS General Reference Guide_.

        For more information about developing and using AWS Config rules, see
        [Evaluating AWS Resource Configurations with AWS
        Config](http://docs.aws.amazon.com/config/latest/developerguide/evaluate-
        config.html) in the _AWS Config Developer Guide_.
        """
        if _request is None:
            _params = {}
            if config_rule is not ShapeBase.NOT_SET:
                _params['config_rule'] = config_rule
            _request = shapes.PutConfigRuleRequest(**_params)
        response = self._boto_client.put_config_rule(**_request.to_boto())

    def put_configuration_aggregator(
        self,
        _request: shapes.PutConfigurationAggregatorRequest = None,
        *,
        configuration_aggregator_name: str,
        account_aggregation_sources: typing.List[shapes.AccountAggregationSource
                                                ] = ShapeBase.NOT_SET,
        organization_aggregation_source: shapes.
        OrganizationAggregationSource = ShapeBase.NOT_SET,
    ) -> shapes.PutConfigurationAggregatorResponse:
        """
        Creates and updates the configuration aggregator with the selected source
        accounts and regions. The source account can be individual account(s) or an
        organization.

        AWS Config should be enabled in source accounts and regions you want to
        aggregate.

        If your source type is an organization, you must be signed in to the master
        account and all features must be enabled in your organization. AWS Config calls
        `EnableAwsServiceAccess` API to enable integration between AWS Config and AWS
        Organizations.
        """
        if _request is None:
            _params = {}
            if configuration_aggregator_name is not ShapeBase.NOT_SET:
                _params['configuration_aggregator_name'
                       ] = configuration_aggregator_name
            if account_aggregation_sources is not ShapeBase.NOT_SET:
                _params['account_aggregation_sources'
                       ] = account_aggregation_sources
            if organization_aggregation_source is not ShapeBase.NOT_SET:
                _params['organization_aggregation_source'
                       ] = organization_aggregation_source
            _request = shapes.PutConfigurationAggregatorRequest(**_params)
        response = self._boto_client.put_configuration_aggregator(
            **_request.to_boto()
        )

        return shapes.PutConfigurationAggregatorResponse.from_boto(response)

    def put_configuration_recorder(
        self,
        _request: shapes.PutConfigurationRecorderRequest = None,
        *,
        configuration_recorder: shapes.ConfigurationRecorder,
    ) -> None:
        """
        Creates a new configuration recorder to record the selected resource
        configurations.

        You can use this action to change the role `roleARN` or the `recordingGroup` of
        an existing recorder. To change the role, call the action on the existing
        configuration recorder and specify a role.

        Currently, you can specify only one configuration recorder per region in your
        account.

        If `ConfigurationRecorder` does not have the **recordingGroup** parameter
        specified, the default is to record all supported resource types.
        """
        if _request is None:
            _params = {}
            if configuration_recorder is not ShapeBase.NOT_SET:
                _params['configuration_recorder'] = configuration_recorder
            _request = shapes.PutConfigurationRecorderRequest(**_params)
        response = self._boto_client.put_configuration_recorder(
            **_request.to_boto()
        )

    def put_delivery_channel(
        self,
        _request: shapes.PutDeliveryChannelRequest = None,
        *,
        delivery_channel: shapes.DeliveryChannel,
    ) -> None:
        """
        Creates a delivery channel object to deliver configuration information to an
        Amazon S3 bucket and Amazon SNS topic.

        Before you can create a delivery channel, you must create a configuration
        recorder.

        You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of
        the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS
        topic, call this action and specify the changed values for the S3 bucket and the
        SNS topic. If you specify a different value for either the S3 bucket or the SNS
        topic, this action will keep the existing value for the parameter that is not
        changed.

        You can have only one delivery channel per region in your account.
        """
        if _request is None:
            _params = {}
            if delivery_channel is not ShapeBase.NOT_SET:
                _params['delivery_channel'] = delivery_channel
            _request = shapes.PutDeliveryChannelRequest(**_params)
        response = self._boto_client.put_delivery_channel(**_request.to_boto())

    def put_evaluations(
        self,
        _request: shapes.PutEvaluationsRequest = None,
        *,
        result_token: str,
        evaluations: typing.List[shapes.Evaluation] = ShapeBase.NOT_SET,
        test_mode: bool = ShapeBase.NOT_SET,
    ) -> shapes.PutEvaluationsResponse:
        """
        Used by an AWS Lambda function to deliver evaluation results to AWS Config. This
        action is required in every AWS Lambda function that is invoked by an AWS Config
        rule.
        """
        if _request is None:
            _params = {}
            if result_token is not ShapeBase.NOT_SET:
                _params['result_token'] = result_token
            if evaluations is not ShapeBase.NOT_SET:
                _params['evaluations'] = evaluations
            if test_mode is not ShapeBase.NOT_SET:
                _params['test_mode'] = test_mode
            _request = shapes.PutEvaluationsRequest(**_params)
        response = self._boto_client.put_evaluations(**_request.to_boto())

        return shapes.PutEvaluationsResponse.from_boto(response)

    def put_retention_configuration(
        self,
        _request: shapes.PutRetentionConfigurationRequest = None,
        *,
        retention_period_in_days: int,
    ) -> shapes.PutRetentionConfigurationResponse:
        """
        Creates and updates the retention configuration with details about retention
        period (number of days) that AWS Config stores your historical information. The
        API creates the `RetentionConfiguration` object and names the object as
        **default**. When you have a `RetentionConfiguration` object named **default** ,
        calling the API modifies the default object.

        Currently, AWS Config supports only one retention configuration per region in
        your account.
        """
        if _request is None:
            _params = {}
            if retention_period_in_days is not ShapeBase.NOT_SET:
                _params['retention_period_in_days'] = retention_period_in_days
            _request = shapes.PutRetentionConfigurationRequest(**_params)
        response = self._boto_client.put_retention_configuration(
            **_request.to_boto()
        )

        return shapes.PutRetentionConfigurationResponse.from_boto(response)

    def start_config_rules_evaluation(
        self,
        _request: shapes.StartConfigRulesEvaluationRequest = None,
        *,
        config_rule_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.StartConfigRulesEvaluationResponse:
        """
        Runs an on-demand evaluation for the specified AWS Config rules against the last
        known configuration state of the resources. Use `StartConfigRulesEvaluation`
        when you want to test that a rule you updated is working as expected.
        `StartConfigRulesEvaluation` does not re-record the latest configuration state
        for your resources. It re-runs an evaluation against the last known state of
        your resources.

        You can specify up to 25 AWS Config rules per request.

        An existing `StartConfigRulesEvaluation` call for the specified rules must
        complete before you can call the API again. If you chose to have AWS Config
        stream to an Amazon SNS topic, you will receive a `ConfigRuleEvaluationStarted`
        notification when the evaluation starts.

        You don't need to call the `StartConfigRulesEvaluation` API to run an evaluation
        for a new rule. When you create a rule, AWS Config evaluates your resources
        against the rule automatically.

        The `StartConfigRulesEvaluation` API is useful if you want to run on-demand
        evaluations, such as the following example:

          1. You have a custom rule that evaluates your IAM resources every 24 hours.

          2. You update your Lambda function to add additional conditions to your rule.

          3. Instead of waiting for the next periodic evaluation, you call the `StartConfigRulesEvaluation` API.

          4. AWS Config invokes your Lambda function and evaluates your IAM resources.

          5. Your custom rule will still run periodic evaluations every 24 hours.
        """
        if _request is None:
            _params = {}
            if config_rule_names is not ShapeBase.NOT_SET:
                _params['config_rule_names'] = config_rule_names
            _request = shapes.StartConfigRulesEvaluationRequest(**_params)
        response = self._boto_client.start_config_rules_evaluation(
            **_request.to_boto()
        )

        return shapes.StartConfigRulesEvaluationResponse.from_boto(response)

    def start_configuration_recorder(
        self,
        _request: shapes.StartConfigurationRecorderRequest = None,
        *,
        configuration_recorder_name: str,
    ) -> None:
        """
        Starts recording configurations of the AWS resources you have selected to record
        in your AWS account.

        You must have created at least one delivery channel to successfully start the
        configuration recorder.
        """
        if _request is None:
            _params = {}
            if configuration_recorder_name is not ShapeBase.NOT_SET:
                _params['configuration_recorder_name'
                       ] = configuration_recorder_name
            _request = shapes.StartConfigurationRecorderRequest(**_params)
        response = self._boto_client.start_configuration_recorder(
            **_request.to_boto()
        )

    def stop_configuration_recorder(
        self,
        _request: shapes.StopConfigurationRecorderRequest = None,
        *,
        configuration_recorder_name: str,
    ) -> None:
        """
        Stops recording configurations of the AWS resources you have selected to record
        in your AWS account.
        """
        if _request is None:
            _params = {}
            if configuration_recorder_name is not ShapeBase.NOT_SET:
                _params['configuration_recorder_name'
                       ] = configuration_recorder_name
            _request = shapes.StopConfigurationRecorderRequest(**_params)
        response = self._boto_client.stop_configuration_recorder(
            **_request.to_boto()
        )
