import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("events", *args, **kwargs)

    def delete_rule(
        self,
        _request: shapes.DeleteRuleRequest = None,
        *,
        name: str,
    ) -> None:
        """
        Deletes the specified rule.

        Before you can delete the rule, you must remove all targets, using
        RemoveTargets.

        When you delete a rule, incoming events might continue to match to the deleted
        rule. Allow a short period of time for changes to take effect.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteRuleRequest(**_params)
        response = self._boto_client.delete_rule(**_request.to_boto())

    def describe_event_bus(
        self,
        _request: shapes.DescribeEventBusRequest = None,
    ) -> shapes.DescribeEventBusResponse:
        """
        Displays the external AWS accounts that are permitted to write events to your
        account using your account's event bus, and the associated policy. To enable
        your account to receive events from other accounts, use PutPermission.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeEventBusRequest(**_params)
        response = self._boto_client.describe_event_bus(**_request.to_boto())

        return shapes.DescribeEventBusResponse.from_boto(response)

    def describe_rule(
        self,
        _request: shapes.DescribeRuleRequest = None,
        *,
        name: str,
    ) -> shapes.DescribeRuleResponse:
        """
        Describes the specified rule.

        DescribeRule does not list the targets of a rule. To see the targets associated
        with a rule, use ListTargetsByRule.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DescribeRuleRequest(**_params)
        response = self._boto_client.describe_rule(**_request.to_boto())

        return shapes.DescribeRuleResponse.from_boto(response)

    def disable_rule(
        self,
        _request: shapes.DisableRuleRequest = None,
        *,
        name: str,
    ) -> None:
        """
        Disables the specified rule. A disabled rule won't match any events, and won't
        self-trigger if it has a schedule expression.

        When you disable a rule, incoming events might continue to match to the disabled
        rule. Allow a short period of time for changes to take effect.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DisableRuleRequest(**_params)
        response = self._boto_client.disable_rule(**_request.to_boto())

    def enable_rule(
        self,
        _request: shapes.EnableRuleRequest = None,
        *,
        name: str,
    ) -> None:
        """
        Enables the specified rule. If the rule does not exist, the operation fails.

        When you enable a rule, incoming events might not immediately start matching to
        a newly enabled rule. Allow a short period of time for changes to take effect.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.EnableRuleRequest(**_params)
        response = self._boto_client.enable_rule(**_request.to_boto())

    def list_rule_names_by_target(
        self,
        _request: shapes.ListRuleNamesByTargetRequest = None,
        *,
        target_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRuleNamesByTargetResponse:
        """
        Lists the rules for the specified target. You can see which of the rules in
        Amazon CloudWatch Events can invoke a specific target in your account.
        """
        if _request is None:
            _params = {}
            if target_arn is not ShapeBase.NOT_SET:
                _params['target_arn'] = target_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRuleNamesByTargetRequest(**_params)
        response = self._boto_client.list_rule_names_by_target(
            **_request.to_boto()
        )

        return shapes.ListRuleNamesByTargetResponse.from_boto(response)

    def list_rules(
        self,
        _request: shapes.ListRulesRequest = None,
        *,
        name_prefix: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRulesResponse:
        """
        Lists your Amazon CloudWatch Events rules. You can either list all the rules or
        you can provide a prefix to match to the rule names.

        ListRules does not list the targets of a rule. To see the targets associated
        with a rule, use ListTargetsByRule.
        """
        if _request is None:
            _params = {}
            if name_prefix is not ShapeBase.NOT_SET:
                _params['name_prefix'] = name_prefix
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRulesRequest(**_params)
        response = self._boto_client.list_rules(**_request.to_boto())

        return shapes.ListRulesResponse.from_boto(response)

    def list_targets_by_rule(
        self,
        _request: shapes.ListTargetsByRuleRequest = None,
        *,
        rule: str,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTargetsByRuleResponse:
        """
        Lists the targets assigned to the specified rule.
        """
        if _request is None:
            _params = {}
            if rule is not ShapeBase.NOT_SET:
                _params['rule'] = rule
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListTargetsByRuleRequest(**_params)
        response = self._boto_client.list_targets_by_rule(**_request.to_boto())

        return shapes.ListTargetsByRuleResponse.from_boto(response)

    def put_events(
        self,
        _request: shapes.PutEventsRequest = None,
        *,
        entries: typing.List[shapes.PutEventsRequestEntry],
    ) -> shapes.PutEventsResponse:
        """
        Sends custom events to Amazon CloudWatch Events so that they can be matched to
        rules.
        """
        if _request is None:
            _params = {}
            if entries is not ShapeBase.NOT_SET:
                _params['entries'] = entries
            _request = shapes.PutEventsRequest(**_params)
        response = self._boto_client.put_events(**_request.to_boto())

        return shapes.PutEventsResponse.from_boto(response)

    def put_permission(
        self,
        _request: shapes.PutPermissionRequest = None,
        *,
        action: str,
        principal: str,
        statement_id: str,
    ) -> None:
        """
        Running `PutPermission` permits the specified AWS account to put events to your
        account's default _event bus_. CloudWatch Events rules in your account are
        triggered by these events arriving to your default event bus.

        For another account to send events to your account, that external account must
        have a CloudWatch Events rule with your account's default event bus as a target.

        To enable multiple AWS accounts to put events to your default event bus, run
        `PutPermission` once for each of these accounts.

        The permission policy on the default event bus cannot exceed 10 KB in size.
        """
        if _request is None:
            _params = {}
            if action is not ShapeBase.NOT_SET:
                _params['action'] = action
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            if statement_id is not ShapeBase.NOT_SET:
                _params['statement_id'] = statement_id
            _request = shapes.PutPermissionRequest(**_params)
        response = self._boto_client.put_permission(**_request.to_boto())

    def put_rule(
        self,
        _request: shapes.PutRuleRequest = None,
        *,
        name: str,
        schedule_expression: str = ShapeBase.NOT_SET,
        event_pattern: str = ShapeBase.NOT_SET,
        state: typing.Union[str, shapes.RuleState] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.PutRuleResponse:
        """
        Creates or updates the specified rule. Rules are enabled by default, or based on
        value of the state. You can disable a rule using DisableRule.

        If you are updating an existing rule, the rule is replaced with what you specify
        in this `PutRule` command. If you omit arguments in `PutRule`, the old values
        for those arguments are not kept. Instead, they are replaced with null values.

        When you create or update a rule, incoming events might not immediately start
        matching to new or updated rules. Allow a short period of time for changes to
        take effect.

        A rule must contain at least an EventPattern or ScheduleExpression. Rules with
        EventPatterns are triggered when a matching event is observed. Rules with
        ScheduleExpressions self-trigger based on the given schedule. A rule can have
        both an EventPattern and a ScheduleExpression, in which case the rule triggers
        on matching events as well as on a schedule.

        Most services in AWS treat : or / as the same character in Amazon Resource Names
        (ARNs). However, CloudWatch Events uses an exact match in event patterns and
        rules. Be sure to use the correct ARN characters when creating event patterns so
        that they match the ARN syntax in the event you want to match.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if schedule_expression is not ShapeBase.NOT_SET:
                _params['schedule_expression'] = schedule_expression
            if event_pattern is not ShapeBase.NOT_SET:
                _params['event_pattern'] = event_pattern
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.PutRuleRequest(**_params)
        response = self._boto_client.put_rule(**_request.to_boto())

        return shapes.PutRuleResponse.from_boto(response)

    def put_targets(
        self,
        _request: shapes.PutTargetsRequest = None,
        *,
        rule: str,
        targets: typing.List[shapes.Target],
    ) -> shapes.PutTargetsResponse:
        """
        Adds the specified targets to the specified rule, or updates the targets if they
        are already associated with the rule.

        Targets are the resources that are invoked when a rule is triggered.

        You can configure the following as targets for CloudWatch Events:

          * EC2 instances

          * SSM Run Command

          * SSM Automation

          * AWS Lambda functions

          * Data streams in Amazon Kinesis Data Streams

          * Data delivery streams in Amazon Kinesis Data Firehose

          * Amazon ECS tasks

          * AWS Step Functions state machines

          * AWS Batch jobs

          * AWS CodeBuild projects

          * Pipelines in AWS CodePipeline

          * Amazon Inspector assessment templates

          * Amazon SNS topics

          * Amazon SQS queues, including FIFO queues

          * The default event bus of another AWS account

        Creating rules with built-in targets is supported only in the AWS Management
        Console. The built-in targets are `EC2 CreateSnapshot API call`, `EC2
        RebootInstances API call`, `EC2 StopInstances API call`, and `EC2
        TerminateInstances API call`.

        For some target types, `PutTargets` provides target-specific parameters. If the
        target is a Kinesis data stream, you can optionally specify which shard the
        event goes to by using the `KinesisParameters` argument. To invoke a command on
        multiple EC2 instances with one rule, you can use the `RunCommandParameters`
        field.

        To be able to make API calls against the resources that you own, Amazon
        CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon
        SNS resources, CloudWatch Events relies on resource-based policies. For EC2
        instances, Kinesis data streams, and AWS Step Functions state machines,
        CloudWatch Events relies on IAM roles that you specify in the `RoleARN` argument
        in `PutTargets`. For more information, see [Authentication and Access
        Control](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/auth-and-
        access-control-cwe.html) in the _Amazon CloudWatch Events User Guide_.

        If another AWS account is in the same region and has granted you permission
        (using `PutPermission`), you can send events to that account. Set that account's
        event bus as a target of the rules in your account. To send the matched events
        to the other account, specify that account's event bus as the `Arn` value when
        you run `PutTargets`. If your account sends events to another account, your
        account is charged for each sent event. Each event sent to another account is
        charged as a custom event. The account receiving the event is not charged. For
        more information, see [Amazon CloudWatch
        Pricing](https://aws.amazon.com/cloudwatch/pricing/).

        For more information about enabling cross-account events, see PutPermission.

        **Input** , **InputPath** , and **InputTransformer** are mutually exclusive and
        optional parameters of a target. When a rule is triggered due to a matched
        event:

          * If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).

          * If **Input** is specified in the form of valid JSON, then the matched event is overridden with this constant.

          * If **InputPath** is specified in the form of JSONPath (for example, `$.detail`), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).

          * If **InputTransformer** is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.

        When you specify `InputPath` or `InputTransformer`, you must use JSON dot
        notation, not bracket notation.

        When you add targets to a rule and the associated rule triggers soon after, new
        or updated targets might not be immediately invoked. Allow a short period of
        time for changes to take effect.

        This action can partially fail if too many requests are made at the same time.
        If that happens, `FailedEntryCount` is non-zero in the response and each entry
        in `FailedEntries` provides the ID of the failed target and the error code.
        """
        if _request is None:
            _params = {}
            if rule is not ShapeBase.NOT_SET:
                _params['rule'] = rule
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            _request = shapes.PutTargetsRequest(**_params)
        response = self._boto_client.put_targets(**_request.to_boto())

        return shapes.PutTargetsResponse.from_boto(response)

    def remove_permission(
        self,
        _request: shapes.RemovePermissionRequest = None,
        *,
        statement_id: str,
    ) -> None:
        """
        Revokes the permission of another AWS account to be able to put events to your
        default event bus. Specify the account to revoke by the `StatementId` value that
        you associated with the account when you granted it permission with
        `PutPermission`. You can find the `StatementId` by using DescribeEventBus.
        """
        if _request is None:
            _params = {}
            if statement_id is not ShapeBase.NOT_SET:
                _params['statement_id'] = statement_id
            _request = shapes.RemovePermissionRequest(**_params)
        response = self._boto_client.remove_permission(**_request.to_boto())

    def remove_targets(
        self,
        _request: shapes.RemoveTargetsRequest = None,
        *,
        rule: str,
        ids: typing.List[str],
    ) -> shapes.RemoveTargetsResponse:
        """
        Removes the specified targets from the specified rule. When the rule is
        triggered, those targets are no longer be invoked.

        When you remove a target, when the associated rule triggers, removed targets
        might continue to be invoked. Allow a short period of time for changes to take
        effect.

        This action can partially fail if too many requests are made at the same time.
        If that happens, `FailedEntryCount` is non-zero in the response and each entry
        in `FailedEntries` provides the ID of the failed target and the error code.
        """
        if _request is None:
            _params = {}
            if rule is not ShapeBase.NOT_SET:
                _params['rule'] = rule
            if ids is not ShapeBase.NOT_SET:
                _params['ids'] = ids
            _request = shapes.RemoveTargetsRequest(**_params)
        response = self._boto_client.remove_targets(**_request.to_boto())

        return shapes.RemoveTargetsResponse.from_boto(response)

    def test_event_pattern(
        self,
        _request: shapes.TestEventPatternRequest = None,
        *,
        event_pattern: str,
        event: str,
    ) -> shapes.TestEventPatternResponse:
        """
        Tests whether the specified event pattern matches the provided event.

        Most services in AWS treat : or / as the same character in Amazon Resource Names
        (ARNs). However, CloudWatch Events uses an exact match in event patterns and
        rules. Be sure to use the correct ARN characters when creating event patterns so
        that they match the ARN syntax in the event you want to match.
        """
        if _request is None:
            _params = {}
            if event_pattern is not ShapeBase.NOT_SET:
                _params['event_pattern'] = event_pattern
            if event is not ShapeBase.NOT_SET:
                _params['event'] = event
            _request = shapes.TestEventPatternRequest(**_params)
        response = self._boto_client.test_event_pattern(**_request.to_boto())

        return shapes.TestEventPatternResponse.from_boto(response)
