import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("elbv2", *args, **kwargs)

    def add_listener_certificates(
        self,
        _request: shapes.AddListenerCertificatesInput = None,
        *,
        listener_arn: str,
        certificates: typing.List[shapes.Certificate],
    ) -> shapes.AddListenerCertificatesOutput:
        """
        Adds the specified certificate to the specified secure listener.

        If the certificate was already added, the call is successful but the certificate
        is not added again.

        To list the certificates for your listener, use DescribeListenerCertificates. To
        remove certificates from your listener, use RemoveListenerCertificates.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            if certificates is not ShapeBase.NOT_SET:
                _params['certificates'] = certificates
            _request = shapes.AddListenerCertificatesInput(**_params)
        response = self._boto_client.add_listener_certificates(
            **_request.to_boto()
        )

        return shapes.AddListenerCertificatesOutput.from_boto(response)

    def add_tags(
        self,
        _request: shapes.AddTagsInput = None,
        *,
        resource_arns: typing.List[str],
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsOutput:
        """
        Adds the specified tags to the specified Elastic Load Balancing resource. You
        can tag your Application Load Balancers, Network Load Balancers, and your target
        groups.

        Each tag consists of a key and an optional value. If a resource already has a
        tag with the same key, `AddTags` updates its value.

        To list the current tags for your resources, use DescribeTags. To remove tags
        from your resources, use RemoveTags.
        """
        if _request is None:
            _params = {}
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsInput(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsOutput.from_boto(response)

    def create_listener(
        self,
        _request: shapes.CreateListenerInput = None,
        *,
        load_balancer_arn: str,
        protocol: typing.Union[str, shapes.ProtocolEnum],
        port: int,
        default_actions: typing.List[shapes.Action],
        ssl_policy: str = ShapeBase.NOT_SET,
        certificates: typing.List[shapes.Certificate] = ShapeBase.NOT_SET,
    ) -> shapes.CreateListenerOutput:
        """
        Creates a listener for the specified Application Load Balancer or Network Load
        Balancer.

        To update a listener, use ModifyListener. When you are finished with a listener,
        you can delete it using DeleteListener. If you are finished with both the
        listener and the load balancer, you can delete them both using
        DeleteLoadBalancer.

        This operation is idempotent, which means that it completes at most one time. If
        you attempt to create multiple listeners with the same settings, each call
        succeeds.

        For more information, see [Listeners for Your Application Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-
        balancer-listeners.html) in the _Application Load Balancers Guide_ and
        [Listeners for Your Network Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-
        balancer-listeners.html) in the _Network Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if default_actions is not ShapeBase.NOT_SET:
                _params['default_actions'] = default_actions
            if ssl_policy is not ShapeBase.NOT_SET:
                _params['ssl_policy'] = ssl_policy
            if certificates is not ShapeBase.NOT_SET:
                _params['certificates'] = certificates
            _request = shapes.CreateListenerInput(**_params)
        response = self._boto_client.create_listener(**_request.to_boto())

        return shapes.CreateListenerOutput.from_boto(response)

    def create_load_balancer(
        self,
        _request: shapes.CreateLoadBalancerInput = None,
        *,
        name: str,
        subnets: typing.List[str] = ShapeBase.NOT_SET,
        subnet_mappings: typing.List[shapes.SubnetMapping] = ShapeBase.NOT_SET,
        security_groups: typing.List[str] = ShapeBase.NOT_SET,
        scheme: typing.Union[str, shapes.
                             LoadBalancerSchemeEnum] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.
                           LoadBalancerTypeEnum] = ShapeBase.NOT_SET,
        ip_address_type: typing.Union[str, shapes.IpAddressType] = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateLoadBalancerOutput:
        """
        Creates an Application Load Balancer or a Network Load Balancer.

        When you create a load balancer, you can specify security groups, public
        subnets, IP address type, and tags. Otherwise, you could do so later using
        SetSecurityGroups, SetSubnets, SetIpAddressType, and AddTags.

        To create listeners for your load balancer, use CreateListener. To describe your
        current load balancers, see DescribeLoadBalancers. When you are finished with a
        load balancer, you can delete it using DeleteLoadBalancer.

        For limit information, see [Limits for Your Application Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-
        balancer-limits.html) in the _Application Load Balancers Guide_ and [Limits for
        Your Network Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-
        balancer-limits.html) in the _Network Load Balancers Guide_.

        This operation is idempotent, which means that it completes at most one time. If
        you attempt to create multiple load balancers with the same settings, each call
        succeeds.

        For more information, see [Application Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-
        load-balancers.html) in the _Application Load Balancers Guide_ and [Network Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-
        load-balancers.html) in the _Network Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if subnets is not ShapeBase.NOT_SET:
                _params['subnets'] = subnets
            if subnet_mappings is not ShapeBase.NOT_SET:
                _params['subnet_mappings'] = subnet_mappings
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            if scheme is not ShapeBase.NOT_SET:
                _params['scheme'] = scheme
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if ip_address_type is not ShapeBase.NOT_SET:
                _params['ip_address_type'] = ip_address_type
            _request = shapes.CreateLoadBalancerInput(**_params)
        response = self._boto_client.create_load_balancer(**_request.to_boto())

        return shapes.CreateLoadBalancerOutput.from_boto(response)

    def create_rule(
        self,
        _request: shapes.CreateRuleInput = None,
        *,
        listener_arn: str,
        conditions: typing.List[shapes.RuleCondition],
        priority: int,
        actions: typing.List[shapes.Action],
    ) -> shapes.CreateRuleOutput:
        """
        Creates a rule for the specified listener. The listener must be associated with
        an Application Load Balancer.

        Rules are evaluated in priority order, from the lowest value to the highest
        value. When the conditions for a rule are met, its actions are performed. If the
        conditions for no rules are met, the actions for the default rule are performed.
        For more information, see [Listener
        Rules](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-
        balancer-listeners.html#listener-rules) in the _Application Load Balancers
        Guide_.

        To view your current rules, use DescribeRules. To update a rule, use ModifyRule.
        To set the priorities of your rules, use SetRulePriorities. To delete a rule,
        use DeleteRule.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            if conditions is not ShapeBase.NOT_SET:
                _params['conditions'] = conditions
            if priority is not ShapeBase.NOT_SET:
                _params['priority'] = priority
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            _request = shapes.CreateRuleInput(**_params)
        response = self._boto_client.create_rule(**_request.to_boto())

        return shapes.CreateRuleOutput.from_boto(response)

    def create_target_group(
        self,
        _request: shapes.CreateTargetGroupInput = None,
        *,
        name: str,
        protocol: typing.Union[str, shapes.ProtocolEnum],
        port: int,
        vpc_id: str,
        health_check_protocol: typing.Union[str, shapes.
                                            ProtocolEnum] = ShapeBase.NOT_SET,
        health_check_port: str = ShapeBase.NOT_SET,
        health_check_path: str = ShapeBase.NOT_SET,
        health_check_interval_seconds: int = ShapeBase.NOT_SET,
        health_check_timeout_seconds: int = ShapeBase.NOT_SET,
        healthy_threshold_count: int = ShapeBase.NOT_SET,
        unhealthy_threshold_count: int = ShapeBase.NOT_SET,
        matcher: shapes.Matcher = ShapeBase.NOT_SET,
        target_type: typing.Union[str, shapes.TargetTypeEnum] = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateTargetGroupOutput:
        """
        Creates a target group.

        To register targets with the target group, use RegisterTargets. To update the
        health check settings for the target group, use ModifyTargetGroup. To monitor
        the health of targets in the target group, use DescribeTargetHealth.

        To route traffic to the targets in a target group, specify the target group in
        an action using CreateListener or CreateRule.

        To delete a target group, use DeleteTargetGroup.

        This operation is idempotent, which means that it completes at most one time. If
        you attempt to create multiple target groups with the same settings, each call
        succeeds.

        For more information, see [Target Groups for Your Application Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-
        balancer-target-groups.html) in the _Application Load Balancers Guide_ or
        [Target Groups for Your Network Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-
        balancer-target-groups.html) in the _Network Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if health_check_protocol is not ShapeBase.NOT_SET:
                _params['health_check_protocol'] = health_check_protocol
            if health_check_port is not ShapeBase.NOT_SET:
                _params['health_check_port'] = health_check_port
            if health_check_path is not ShapeBase.NOT_SET:
                _params['health_check_path'] = health_check_path
            if health_check_interval_seconds is not ShapeBase.NOT_SET:
                _params['health_check_interval_seconds'
                       ] = health_check_interval_seconds
            if health_check_timeout_seconds is not ShapeBase.NOT_SET:
                _params['health_check_timeout_seconds'
                       ] = health_check_timeout_seconds
            if healthy_threshold_count is not ShapeBase.NOT_SET:
                _params['healthy_threshold_count'] = healthy_threshold_count
            if unhealthy_threshold_count is not ShapeBase.NOT_SET:
                _params['unhealthy_threshold_count'] = unhealthy_threshold_count
            if matcher is not ShapeBase.NOT_SET:
                _params['matcher'] = matcher
            if target_type is not ShapeBase.NOT_SET:
                _params['target_type'] = target_type
            _request = shapes.CreateTargetGroupInput(**_params)
        response = self._boto_client.create_target_group(**_request.to_boto())

        return shapes.CreateTargetGroupOutput.from_boto(response)

    def delete_listener(
        self,
        _request: shapes.DeleteListenerInput = None,
        *,
        listener_arn: str,
    ) -> shapes.DeleteListenerOutput:
        """
        Deletes the specified listener.

        Alternatively, your listener is deleted when you delete the load balancer to
        which it is attached, using DeleteLoadBalancer.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            _request = shapes.DeleteListenerInput(**_params)
        response = self._boto_client.delete_listener(**_request.to_boto())

        return shapes.DeleteListenerOutput.from_boto(response)

    def delete_load_balancer(
        self,
        _request: shapes.DeleteLoadBalancerInput = None,
        *,
        load_balancer_arn: str,
    ) -> shapes.DeleteLoadBalancerOutput:
        """
        Deletes the specified Application Load Balancer or Network Load Balancer and its
        attached listeners.

        You can't delete a load balancer if deletion protection is enabled. If the load
        balancer does not exist or has already been deleted, the call succeeds.

        Deleting a load balancer does not affect its registered targets. For example,
        your EC2 instances continue to run and are still registered to their target
        groups. If you no longer need these EC2 instances, you can stop or terminate
        them.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            _request = shapes.DeleteLoadBalancerInput(**_params)
        response = self._boto_client.delete_load_balancer(**_request.to_boto())

        return shapes.DeleteLoadBalancerOutput.from_boto(response)

    def delete_rule(
        self,
        _request: shapes.DeleteRuleInput = None,
        *,
        rule_arn: str,
    ) -> shapes.DeleteRuleOutput:
        """
        Deletes the specified rule.
        """
        if _request is None:
            _params = {}
            if rule_arn is not ShapeBase.NOT_SET:
                _params['rule_arn'] = rule_arn
            _request = shapes.DeleteRuleInput(**_params)
        response = self._boto_client.delete_rule(**_request.to_boto())

        return shapes.DeleteRuleOutput.from_boto(response)

    def delete_target_group(
        self,
        _request: shapes.DeleteTargetGroupInput = None,
        *,
        target_group_arn: str,
    ) -> shapes.DeleteTargetGroupOutput:
        """
        Deletes the specified target group.

        You can delete a target group if it is not referenced by any actions. Deleting a
        target group also deletes any associated health checks.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            _request = shapes.DeleteTargetGroupInput(**_params)
        response = self._boto_client.delete_target_group(**_request.to_boto())

        return shapes.DeleteTargetGroupOutput.from_boto(response)

    def deregister_targets(
        self,
        _request: shapes.DeregisterTargetsInput = None,
        *,
        target_group_arn: str,
        targets: typing.List[shapes.TargetDescription],
    ) -> shapes.DeregisterTargetsOutput:
        """
        Deregisters the specified targets from the specified target group. After the
        targets are deregistered, they no longer receive traffic from the load balancer.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            _request = shapes.DeregisterTargetsInput(**_params)
        response = self._boto_client.deregister_targets(**_request.to_boto())

        return shapes.DeregisterTargetsOutput.from_boto(response)

    def describe_account_limits(
        self,
        _request: shapes.DescribeAccountLimitsInput = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAccountLimitsOutput:
        """
        Describes the current Elastic Load Balancing resource limits for your AWS
        account.

        For more information, see [Limits for Your Application Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-
        balancer-limits.html) in the _Application Load Balancer Guide_ or [Limits for
        Your Network Load
        Balancers](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-
        balancer-limits.html) in the _Network Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeAccountLimitsInput(**_params)
        response = self._boto_client.describe_account_limits(
            **_request.to_boto()
        )

        return shapes.DescribeAccountLimitsOutput.from_boto(response)

    def describe_listener_certificates(
        self,
        _request: shapes.DescribeListenerCertificatesInput = None,
        *,
        listener_arn: str,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeListenerCertificatesOutput:
        """
        Describes the certificates for the specified secure listener.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeListenerCertificatesInput(**_params)
        response = self._boto_client.describe_listener_certificates(
            **_request.to_boto()
        )

        return shapes.DescribeListenerCertificatesOutput.from_boto(response)

    def describe_listeners(
        self,
        _request: shapes.DescribeListenersInput = None,
        *,
        load_balancer_arn: str = ShapeBase.NOT_SET,
        listener_arns: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeListenersOutput:
        """
        Describes the specified listeners or the listeners for the specified Application
        Load Balancer or Network Load Balancer. You must specify either a load balancer
        or one or more listeners.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if listener_arns is not ShapeBase.NOT_SET:
                _params['listener_arns'] = listener_arns
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeListenersInput(**_params)
        paginator = self.get_paginator("describe_listeners").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeListenersOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeListenersOutput.from_boto(response)

    def describe_load_balancer_attributes(
        self,
        _request: shapes.DescribeLoadBalancerAttributesInput = None,
        *,
        load_balancer_arn: str,
    ) -> shapes.DescribeLoadBalancerAttributesOutput:
        """
        Describes the attributes for the specified Application Load Balancer or Network
        Load Balancer.

        For more information, see [Load Balancer
        Attributes](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-
        load-balancers.html#load-balancer-attributes) in the _Application Load Balancers
        Guide_ or [Load Balancer
        Attributes](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-
        load-balancers.html#load-balancer-attributes) in the _Network Load Balancers
        Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            _request = shapes.DescribeLoadBalancerAttributesInput(**_params)
        response = self._boto_client.describe_load_balancer_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBalancerAttributesOutput.from_boto(response)

    def describe_load_balancers(
        self,
        _request: shapes.DescribeLoadBalancersInput = None,
        *,
        load_balancer_arns: typing.List[str] = ShapeBase.NOT_SET,
        names: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLoadBalancersOutput:
        """
        Describes the specified load balancers or all of your load balancers.

        To describe the listeners for a load balancer, use DescribeListeners. To
        describe the attributes for a load balancer, use DescribeLoadBalancerAttributes.
        """
        if _request is None:
            _params = {}
            if load_balancer_arns is not ShapeBase.NOT_SET:
                _params['load_balancer_arns'] = load_balancer_arns
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeLoadBalancersInput(**_params)
        paginator = self.get_paginator("describe_load_balancers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeLoadBalancersOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeLoadBalancersOutput.from_boto(response)

    def describe_rules(
        self,
        _request: shapes.DescribeRulesInput = None,
        *,
        listener_arn: str = ShapeBase.NOT_SET,
        rule_arns: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRulesOutput:
        """
        Describes the specified rules or the rules for the specified listener. You must
        specify either a listener or one or more rules.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            if rule_arns is not ShapeBase.NOT_SET:
                _params['rule_arns'] = rule_arns
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeRulesInput(**_params)
        response = self._boto_client.describe_rules(**_request.to_boto())

        return shapes.DescribeRulesOutput.from_boto(response)

    def describe_ssl_policies(
        self,
        _request: shapes.DescribeSSLPoliciesInput = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSSLPoliciesOutput:
        """
        Describes the specified policies or all policies used for SSL negotiation.

        For more information, see [Security
        Policies](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-
        https-listener.html#describe-ssl-policies) in the _Application Load Balancers
        Guide_.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeSSLPoliciesInput(**_params)
        response = self._boto_client.describe_ssl_policies(**_request.to_boto())

        return shapes.DescribeSSLPoliciesOutput.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsInput = None,
        *,
        resource_arns: typing.List[str],
    ) -> shapes.DescribeTagsOutput:
        """
        Describes the tags for the specified resources. You can describe the tags for
        one or more Application Load Balancers, Network Load Balancers, and target
        groups.
        """
        if _request is None:
            _params = {}
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            _request = shapes.DescribeTagsInput(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.DescribeTagsOutput.from_boto(response)

    def describe_target_group_attributes(
        self,
        _request: shapes.DescribeTargetGroupAttributesInput = None,
        *,
        target_group_arn: str,
    ) -> shapes.DescribeTargetGroupAttributesOutput:
        """
        Describes the attributes for the specified target group.

        For more information, see [Target Group
        Attributes](http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-
        balancer-target-groups.html#target-group-attributes) in the _Application Load
        Balancers Guide_ or [Target Group
        Attributes](http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-
        balancer-target-groups.html#target-group-attributes) in the _Network Load
        Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            _request = shapes.DescribeTargetGroupAttributesInput(**_params)
        response = self._boto_client.describe_target_group_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeTargetGroupAttributesOutput.from_boto(response)

    def describe_target_groups(
        self,
        _request: shapes.DescribeTargetGroupsInput = None,
        *,
        load_balancer_arn: str = ShapeBase.NOT_SET,
        target_group_arns: typing.List[str] = ShapeBase.NOT_SET,
        names: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTargetGroupsOutput:
        """
        Describes the specified target groups or all of your target groups. By default,
        all target groups are described. Alternatively, you can specify one of the
        following to filter the results: the ARN of the load balancer, the names of one
        or more target groups, or the ARNs of one or more target groups.

        To describe the targets for a target group, use DescribeTargetHealth. To
        describe the attributes of a target group, use DescribeTargetGroupAttributes.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if target_group_arns is not ShapeBase.NOT_SET:
                _params['target_group_arns'] = target_group_arns
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeTargetGroupsInput(**_params)
        paginator = self.get_paginator("describe_target_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeTargetGroupsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeTargetGroupsOutput.from_boto(response)

    def describe_target_health(
        self,
        _request: shapes.DescribeTargetHealthInput = None,
        *,
        target_group_arn: str,
        targets: typing.List[shapes.TargetDescription] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTargetHealthOutput:
        """
        Describes the health of the specified targets or all of your targets.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            _request = shapes.DescribeTargetHealthInput(**_params)
        response = self._boto_client.describe_target_health(
            **_request.to_boto()
        )

        return shapes.DescribeTargetHealthOutput.from_boto(response)

    def modify_listener(
        self,
        _request: shapes.ModifyListenerInput = None,
        *,
        listener_arn: str,
        port: int = ShapeBase.NOT_SET,
        protocol: typing.Union[str, shapes.ProtocolEnum] = ShapeBase.NOT_SET,
        ssl_policy: str = ShapeBase.NOT_SET,
        certificates: typing.List[shapes.Certificate] = ShapeBase.NOT_SET,
        default_actions: typing.List[shapes.Action] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyListenerOutput:
        """
        Modifies the specified properties of the specified listener.

        Any properties that you do not specify retain their current values. However,
        changing the protocol from HTTPS to HTTP removes the security policy and SSL
        certificate properties. If you change the protocol from HTTP to HTTPS, you must
        add the security policy and server certificate.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if ssl_policy is not ShapeBase.NOT_SET:
                _params['ssl_policy'] = ssl_policy
            if certificates is not ShapeBase.NOT_SET:
                _params['certificates'] = certificates
            if default_actions is not ShapeBase.NOT_SET:
                _params['default_actions'] = default_actions
            _request = shapes.ModifyListenerInput(**_params)
        response = self._boto_client.modify_listener(**_request.to_boto())

        return shapes.ModifyListenerOutput.from_boto(response)

    def modify_load_balancer_attributes(
        self,
        _request: shapes.ModifyLoadBalancerAttributesInput = None,
        *,
        load_balancer_arn: str,
        attributes: typing.List[shapes.LoadBalancerAttribute],
    ) -> shapes.ModifyLoadBalancerAttributesOutput:
        """
        Modifies the specified attributes of the specified Application Load Balancer or
        Network Load Balancer.

        If any of the specified attributes can't be modified as requested, the call
        fails. Any existing attributes that you do not modify retain their current
        values.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.ModifyLoadBalancerAttributesInput(**_params)
        response = self._boto_client.modify_load_balancer_attributes(
            **_request.to_boto()
        )

        return shapes.ModifyLoadBalancerAttributesOutput.from_boto(response)

    def modify_rule(
        self,
        _request: shapes.ModifyRuleInput = None,
        *,
        rule_arn: str,
        conditions: typing.List[shapes.RuleCondition] = ShapeBase.NOT_SET,
        actions: typing.List[shapes.Action] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyRuleOutput:
        """
        Modifies the specified rule.

        Any existing properties that you do not modify retain their current values.

        To modify the actions for the default rule, use ModifyListener.
        """
        if _request is None:
            _params = {}
            if rule_arn is not ShapeBase.NOT_SET:
                _params['rule_arn'] = rule_arn
            if conditions is not ShapeBase.NOT_SET:
                _params['conditions'] = conditions
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            _request = shapes.ModifyRuleInput(**_params)
        response = self._boto_client.modify_rule(**_request.to_boto())

        return shapes.ModifyRuleOutput.from_boto(response)

    def modify_target_group(
        self,
        _request: shapes.ModifyTargetGroupInput = None,
        *,
        target_group_arn: str,
        health_check_protocol: typing.Union[str, shapes.
                                            ProtocolEnum] = ShapeBase.NOT_SET,
        health_check_port: str = ShapeBase.NOT_SET,
        health_check_path: str = ShapeBase.NOT_SET,
        health_check_interval_seconds: int = ShapeBase.NOT_SET,
        health_check_timeout_seconds: int = ShapeBase.NOT_SET,
        healthy_threshold_count: int = ShapeBase.NOT_SET,
        unhealthy_threshold_count: int = ShapeBase.NOT_SET,
        matcher: shapes.Matcher = ShapeBase.NOT_SET,
    ) -> shapes.ModifyTargetGroupOutput:
        """
        Modifies the health checks used when evaluating the health state of the targets
        in the specified target group.

        To monitor the health of the targets, use DescribeTargetHealth.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            if health_check_protocol is not ShapeBase.NOT_SET:
                _params['health_check_protocol'] = health_check_protocol
            if health_check_port is not ShapeBase.NOT_SET:
                _params['health_check_port'] = health_check_port
            if health_check_path is not ShapeBase.NOT_SET:
                _params['health_check_path'] = health_check_path
            if health_check_interval_seconds is not ShapeBase.NOT_SET:
                _params['health_check_interval_seconds'
                       ] = health_check_interval_seconds
            if health_check_timeout_seconds is not ShapeBase.NOT_SET:
                _params['health_check_timeout_seconds'
                       ] = health_check_timeout_seconds
            if healthy_threshold_count is not ShapeBase.NOT_SET:
                _params['healthy_threshold_count'] = healthy_threshold_count
            if unhealthy_threshold_count is not ShapeBase.NOT_SET:
                _params['unhealthy_threshold_count'] = unhealthy_threshold_count
            if matcher is not ShapeBase.NOT_SET:
                _params['matcher'] = matcher
            _request = shapes.ModifyTargetGroupInput(**_params)
        response = self._boto_client.modify_target_group(**_request.to_boto())

        return shapes.ModifyTargetGroupOutput.from_boto(response)

    def modify_target_group_attributes(
        self,
        _request: shapes.ModifyTargetGroupAttributesInput = None,
        *,
        target_group_arn: str,
        attributes: typing.List[shapes.TargetGroupAttribute],
    ) -> shapes.ModifyTargetGroupAttributesOutput:
        """
        Modifies the specified attributes of the specified target group.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.ModifyTargetGroupAttributesInput(**_params)
        response = self._boto_client.modify_target_group_attributes(
            **_request.to_boto()
        )

        return shapes.ModifyTargetGroupAttributesOutput.from_boto(response)

    def register_targets(
        self,
        _request: shapes.RegisterTargetsInput = None,
        *,
        target_group_arn: str,
        targets: typing.List[shapes.TargetDescription],
    ) -> shapes.RegisterTargetsOutput:
        """
        Registers the specified targets with the specified target group.

        You can register targets by instance ID or by IP address. If the target is an
        EC2 instance, it must be in the `running` state when you register it.

        By default, the load balancer routes requests to registered targets using the
        protocol and port for the target group. Alternatively, you can override the port
        for a target when you register it. You can register each EC2 instance or IP
        address with the same target group multiple times using different ports.

        With a Network Load Balancer, you cannot register instances by instance ID if
        they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1,
        G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by
        IP address.

        To remove a target from a target group, use DeregisterTargets.
        """
        if _request is None:
            _params = {}
            if target_group_arn is not ShapeBase.NOT_SET:
                _params['target_group_arn'] = target_group_arn
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            _request = shapes.RegisterTargetsInput(**_params)
        response = self._boto_client.register_targets(**_request.to_boto())

        return shapes.RegisterTargetsOutput.from_boto(response)

    def remove_listener_certificates(
        self,
        _request: shapes.RemoveListenerCertificatesInput = None,
        *,
        listener_arn: str,
        certificates: typing.List[shapes.Certificate],
    ) -> shapes.RemoveListenerCertificatesOutput:
        """
        Removes the specified certificate from the specified secure listener.

        You can't remove the default certificate for a listener. To replace the default
        certificate, call ModifyListener.

        To list the certificates for your listener, use DescribeListenerCertificates.
        """
        if _request is None:
            _params = {}
            if listener_arn is not ShapeBase.NOT_SET:
                _params['listener_arn'] = listener_arn
            if certificates is not ShapeBase.NOT_SET:
                _params['certificates'] = certificates
            _request = shapes.RemoveListenerCertificatesInput(**_params)
        response = self._boto_client.remove_listener_certificates(
            **_request.to_boto()
        )

        return shapes.RemoveListenerCertificatesOutput.from_boto(response)

    def remove_tags(
        self,
        _request: shapes.RemoveTagsInput = None,
        *,
        resource_arns: typing.List[str],
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsOutput:
        """
        Removes the specified tags from the specified Elastic Load Balancing resource.

        To list the current tags for your resources, use DescribeTags.
        """
        if _request is None:
            _params = {}
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsInput(**_params)
        response = self._boto_client.remove_tags(**_request.to_boto())

        return shapes.RemoveTagsOutput.from_boto(response)

    def set_ip_address_type(
        self,
        _request: shapes.SetIpAddressTypeInput = None,
        *,
        load_balancer_arn: str,
        ip_address_type: typing.Union[str, shapes.IpAddressType],
    ) -> shapes.SetIpAddressTypeOutput:
        """
        Sets the type of IP addresses used by the subnets of the specified Application
        Load Balancer or Network Load Balancer.

        Network Load Balancers must use `ipv4`.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if ip_address_type is not ShapeBase.NOT_SET:
                _params['ip_address_type'] = ip_address_type
            _request = shapes.SetIpAddressTypeInput(**_params)
        response = self._boto_client.set_ip_address_type(**_request.to_boto())

        return shapes.SetIpAddressTypeOutput.from_boto(response)

    def set_rule_priorities(
        self,
        _request: shapes.SetRulePrioritiesInput = None,
        *,
        rule_priorities: typing.List[shapes.RulePriorityPair],
    ) -> shapes.SetRulePrioritiesOutput:
        """
        Sets the priorities of the specified rules.

        You can reorder the rules as long as there are no priority conflicts in the new
        order. Any existing rules that you do not specify retain their current priority.
        """
        if _request is None:
            _params = {}
            if rule_priorities is not ShapeBase.NOT_SET:
                _params['rule_priorities'] = rule_priorities
            _request = shapes.SetRulePrioritiesInput(**_params)
        response = self._boto_client.set_rule_priorities(**_request.to_boto())

        return shapes.SetRulePrioritiesOutput.from_boto(response)

    def set_security_groups(
        self,
        _request: shapes.SetSecurityGroupsInput = None,
        *,
        load_balancer_arn: str,
        security_groups: typing.List[str],
    ) -> shapes.SetSecurityGroupsOutput:
        """
        Associates the specified security groups with the specified Application Load
        Balancer. The specified security groups override the previously associated
        security groups.

        You can't specify a security group for a Network Load Balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            _request = shapes.SetSecurityGroupsInput(**_params)
        response = self._boto_client.set_security_groups(**_request.to_boto())

        return shapes.SetSecurityGroupsOutput.from_boto(response)

    def set_subnets(
        self,
        _request: shapes.SetSubnetsInput = None,
        *,
        load_balancer_arn: str,
        subnets: typing.List[str] = ShapeBase.NOT_SET,
        subnet_mappings: typing.List[shapes.SubnetMapping] = ShapeBase.NOT_SET,
    ) -> shapes.SetSubnetsOutput:
        """
        Enables the Availability Zone for the specified public subnets for the specified
        Application Load Balancer. The specified subnets replace the previously enabled
        subnets.

        You can't change the subnets for a Network Load Balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_arn is not ShapeBase.NOT_SET:
                _params['load_balancer_arn'] = load_balancer_arn
            if subnets is not ShapeBase.NOT_SET:
                _params['subnets'] = subnets
            if subnet_mappings is not ShapeBase.NOT_SET:
                _params['subnet_mappings'] = subnet_mappings
            _request = shapes.SetSubnetsInput(**_params)
        response = self._boto_client.set_subnets(**_request.to_boto())

        return shapes.SetSubnetsOutput.from_boto(response)
