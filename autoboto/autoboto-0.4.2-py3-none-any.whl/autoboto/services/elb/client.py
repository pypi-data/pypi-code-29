import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("elb", *args, **kwargs)

    def add_tags(
        self,
        _request: shapes.AddTagsInput = None,
        *,
        load_balancer_names: typing.List[str],
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsOutput:
        """
        Adds the specified tags to the specified load balancer. Each load balancer can
        have a maximum of 10 tags.

        Each tag consists of a key and an optional value. If a tag with the same key is
        already associated with the load balancer, `AddTags` updates its value.

        For more information, see [Tag Your Classic Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-
        remove-tags.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsInput(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsOutput.from_boto(response)

    def apply_security_groups_to_load_balancer(
        self,
        _request: shapes.ApplySecurityGroupsToLoadBalancerInput = None,
        *,
        load_balancer_name: str,
        security_groups: typing.List[str],
    ) -> shapes.ApplySecurityGroupsToLoadBalancerOutput:
        """
        Associates one or more security groups with your load balancer in a virtual
        private cloud (VPC). The specified security groups override the previously
        associated security groups.

        For more information, see [Security Groups for Load Balancers in a
        VPC](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        security-groups.html#elb-vpc-security-groups) in the _Classic Load Balancers
        Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            _request = shapes.ApplySecurityGroupsToLoadBalancerInput(**_params)
        response = self._boto_client.apply_security_groups_to_load_balancer(
            **_request.to_boto()
        )

        return shapes.ApplySecurityGroupsToLoadBalancerOutput.from_boto(
            response
        )

    def attach_load_balancer_to_subnets(
        self,
        _request: shapes.AttachLoadBalancerToSubnetsInput = None,
        *,
        load_balancer_name: str,
        subnets: typing.List[str],
    ) -> shapes.AttachLoadBalancerToSubnetsOutput:
        """
        Adds one or more subnets to the set of configured subnets for the specified load
        balancer.

        The load balancer evenly distributes requests across all registered subnets. For
        more information, see [Add or Remove Subnets for Your Load Balancer in a
        VPC](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-
        subnets.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if subnets is not ShapeBase.NOT_SET:
                _params['subnets'] = subnets
            _request = shapes.AttachLoadBalancerToSubnetsInput(**_params)
        response = self._boto_client.attach_load_balancer_to_subnets(
            **_request.to_boto()
        )

        return shapes.AttachLoadBalancerToSubnetsOutput.from_boto(response)

    def configure_health_check(
        self,
        _request: shapes.ConfigureHealthCheckInput = None,
        *,
        load_balancer_name: str,
        health_check: shapes.HealthCheck,
    ) -> shapes.ConfigureHealthCheckOutput:
        """
        Specifies the health check settings to use when evaluating the health state of
        your EC2 instances.

        For more information, see [Configure Health Checks for Your Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        healthchecks.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if health_check is not ShapeBase.NOT_SET:
                _params['health_check'] = health_check
            _request = shapes.ConfigureHealthCheckInput(**_params)
        response = self._boto_client.configure_health_check(
            **_request.to_boto()
        )

        return shapes.ConfigureHealthCheckOutput.from_boto(response)

    def create_app_cookie_stickiness_policy(
        self,
        _request: shapes.CreateAppCookieStickinessPolicyInput = None,
        *,
        load_balancer_name: str,
        policy_name: str,
        cookie_name: str,
    ) -> shapes.CreateAppCookieStickinessPolicyOutput:
        """
        Generates a stickiness policy with sticky session lifetimes that follow that of
        an application-generated cookie. This policy can be associated only with
        HTTP/HTTPS listeners.

        This policy is similar to the policy created by CreateLBCookieStickinessPolicy,
        except that the lifetime of the special Elastic Load Balancing cookie, `AWSELB`,
        follows the lifetime of the application-generated cookie specified in the policy
        configuration. The load balancer only inserts a new stickiness cookie when the
        application response includes a new application cookie.

        If the application cookie is explicitly removed or expires, the session stops
        being sticky until a new application cookie is issued.

        For more information, see [Application-Controlled Session
        Stickiness](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        sticky-sessions.html#enable-sticky-sessions-application) in the _Classic Load
        Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if cookie_name is not ShapeBase.NOT_SET:
                _params['cookie_name'] = cookie_name
            _request = shapes.CreateAppCookieStickinessPolicyInput(**_params)
        response = self._boto_client.create_app_cookie_stickiness_policy(
            **_request.to_boto()
        )

        return shapes.CreateAppCookieStickinessPolicyOutput.from_boto(response)

    def create_lb_cookie_stickiness_policy(
        self,
        _request: shapes.CreateLBCookieStickinessPolicyInput = None,
        *,
        load_balancer_name: str,
        policy_name: str,
        cookie_expiration_period: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateLBCookieStickinessPolicyOutput:
        """
        Generates a stickiness policy with sticky session lifetimes controlled by the
        lifetime of the browser (user-agent) or a specified expiration period. This
        policy can be associated only with HTTP/HTTPS listeners.

        When a load balancer implements this policy, the load balancer uses a special
        cookie to track the instance for each request. When the load balancer receives a
        request, it first checks to see if this cookie is present in the request. If so,
        the load balancer sends the request to the application server specified in the
        cookie. If not, the load balancer sends the request to a server that is chosen
        based on the existing load-balancing algorithm.

        A cookie is inserted into the response for binding subsequent requests from the
        same user to that server. The validity of the cookie is based on the cookie
        expiration time, which is specified in the policy configuration.

        For more information, see [Duration-Based Session
        Stickiness](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        sticky-sessions.html#enable-sticky-sessions-duration) in the _Classic Load
        Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if cookie_expiration_period is not ShapeBase.NOT_SET:
                _params['cookie_expiration_period'] = cookie_expiration_period
            _request = shapes.CreateLBCookieStickinessPolicyInput(**_params)
        response = self._boto_client.create_lb_cookie_stickiness_policy(
            **_request.to_boto()
        )

        return shapes.CreateLBCookieStickinessPolicyOutput.from_boto(response)

    def create_load_balancer(
        self,
        _request: shapes.CreateAccessPointInput = None,
        *,
        load_balancer_name: str,
        listeners: typing.List[shapes.Listener],
        availability_zones: typing.List[str] = ShapeBase.NOT_SET,
        subnets: typing.List[str] = ShapeBase.NOT_SET,
        security_groups: typing.List[str] = ShapeBase.NOT_SET,
        scheme: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateAccessPointOutput:
        """
        Creates a Classic Load Balancer.

        You can add listeners, security groups, subnets, and tags when you create your
        load balancer, or you can add them later using CreateLoadBalancerListeners,
        ApplySecurityGroupsToLoadBalancer, AttachLoadBalancerToSubnets, and AddTags.

        To describe your current load balancers, see DescribeLoadBalancers. When you are
        finished with a load balancer, you can delete it using DeleteLoadBalancer.

        You can create up to 20 load balancers per region per account. You can request
        an increase for the number of load balancers for your account. For more
        information, see [Limits for Your Classic Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        limits.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if listeners is not ShapeBase.NOT_SET:
                _params['listeners'] = listeners
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            if subnets is not ShapeBase.NOT_SET:
                _params['subnets'] = subnets
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            if scheme is not ShapeBase.NOT_SET:
                _params['scheme'] = scheme
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateAccessPointInput(**_params)
        response = self._boto_client.create_load_balancer(**_request.to_boto())

        return shapes.CreateAccessPointOutput.from_boto(response)

    def create_load_balancer_listeners(
        self,
        _request: shapes.CreateLoadBalancerListenerInput = None,
        *,
        load_balancer_name: str,
        listeners: typing.List[shapes.Listener],
    ) -> shapes.CreateLoadBalancerListenerOutput:
        """
        Creates one or more listeners for the specified load balancer. If a listener
        with the specified port does not already exist, it is created; otherwise, the
        properties of the new listener must match the properties of the existing
        listener.

        For more information, see [Listeners for Your Classic Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        listener-config.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if listeners is not ShapeBase.NOT_SET:
                _params['listeners'] = listeners
            _request = shapes.CreateLoadBalancerListenerInput(**_params)
        response = self._boto_client.create_load_balancer_listeners(
            **_request.to_boto()
        )

        return shapes.CreateLoadBalancerListenerOutput.from_boto(response)

    def create_load_balancer_policy(
        self,
        _request: shapes.CreateLoadBalancerPolicyInput = None,
        *,
        load_balancer_name: str,
        policy_name: str,
        policy_type_name: str,
        policy_attributes: typing.List[shapes.PolicyAttribute
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateLoadBalancerPolicyOutput:
        """
        Creates a policy with the specified attributes for the specified load balancer.

        Policies are settings that are saved for your load balancer and that can be
        applied to the listener or the application server, depending on the policy type.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_type_name is not ShapeBase.NOT_SET:
                _params['policy_type_name'] = policy_type_name
            if policy_attributes is not ShapeBase.NOT_SET:
                _params['policy_attributes'] = policy_attributes
            _request = shapes.CreateLoadBalancerPolicyInput(**_params)
        response = self._boto_client.create_load_balancer_policy(
            **_request.to_boto()
        )

        return shapes.CreateLoadBalancerPolicyOutput.from_boto(response)

    def delete_load_balancer(
        self,
        _request: shapes.DeleteAccessPointInput = None,
        *,
        load_balancer_name: str,
    ) -> shapes.DeleteAccessPointOutput:
        """
        Deletes the specified load balancer.

        If you are attempting to recreate a load balancer, you must reconfigure all
        settings. The DNS name associated with a deleted load balancer are no longer
        usable. The name and associated DNS record of the deleted load balancer no
        longer exist and traffic sent to any of its IP addresses is no longer delivered
        to your instances.

        If the load balancer does not exist or has already been deleted, the call to
        `DeleteLoadBalancer` still succeeds.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            _request = shapes.DeleteAccessPointInput(**_params)
        response = self._boto_client.delete_load_balancer(**_request.to_boto())

        return shapes.DeleteAccessPointOutput.from_boto(response)

    def delete_load_balancer_listeners(
        self,
        _request: shapes.DeleteLoadBalancerListenerInput = None,
        *,
        load_balancer_name: str,
        load_balancer_ports: typing.List[int],
    ) -> shapes.DeleteLoadBalancerListenerOutput:
        """
        Deletes the specified listeners from the specified load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if load_balancer_ports is not ShapeBase.NOT_SET:
                _params['load_balancer_ports'] = load_balancer_ports
            _request = shapes.DeleteLoadBalancerListenerInput(**_params)
        response = self._boto_client.delete_load_balancer_listeners(
            **_request.to_boto()
        )

        return shapes.DeleteLoadBalancerListenerOutput.from_boto(response)

    def delete_load_balancer_policy(
        self,
        _request: shapes.DeleteLoadBalancerPolicyInput = None,
        *,
        load_balancer_name: str,
        policy_name: str,
    ) -> shapes.DeleteLoadBalancerPolicyOutput:
        """
        Deletes the specified policy from the specified load balancer. This policy must
        not be enabled for any listeners.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeleteLoadBalancerPolicyInput(**_params)
        response = self._boto_client.delete_load_balancer_policy(
            **_request.to_boto()
        )

        return shapes.DeleteLoadBalancerPolicyOutput.from_boto(response)

    def deregister_instances_from_load_balancer(
        self,
        _request: shapes.DeregisterEndPointsInput = None,
        *,
        load_balancer_name: str,
        instances: typing.List[shapes.Instance],
    ) -> shapes.DeregisterEndPointsOutput:
        """
        Deregisters the specified instances from the specified load balancer. After the
        instance is deregistered, it no longer receives traffic from the load balancer.

        You can use DescribeLoadBalancers to verify that the instance is deregistered
        from the load balancer.

        For more information, see [Register or De-Register EC2
        Instances](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        deregister-register-instances.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instances is not ShapeBase.NOT_SET:
                _params['instances'] = instances
            _request = shapes.DeregisterEndPointsInput(**_params)
        response = self._boto_client.deregister_instances_from_load_balancer(
            **_request.to_boto()
        )

        return shapes.DeregisterEndPointsOutput.from_boto(response)

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

        For more information, see [Limits for Your Classic Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        limits.html) in the _Classic Load Balancers Guide_.
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

    def describe_instance_health(
        self,
        _request: shapes.DescribeEndPointStateInput = None,
        *,
        load_balancer_name: str,
        instances: typing.List[shapes.Instance] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEndPointStateOutput:
        """
        Describes the state of the specified instances with respect to the specified
        load balancer. If no instances are specified, the call describes the state of
        all instances that are currently registered with the load balancer. If instances
        are specified, their state is returned even if they are no longer registered
        with the load balancer. The state of terminated instances is not returned.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instances is not ShapeBase.NOT_SET:
                _params['instances'] = instances
            _request = shapes.DescribeEndPointStateInput(**_params)
        response = self._boto_client.describe_instance_health(
            **_request.to_boto()
        )

        return shapes.DescribeEndPointStateOutput.from_boto(response)

    def describe_load_balancer_attributes(
        self,
        _request: shapes.DescribeLoadBalancerAttributesInput = None,
        *,
        load_balancer_name: str,
    ) -> shapes.DescribeLoadBalancerAttributesOutput:
        """
        Describes the attributes for the specified load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            _request = shapes.DescribeLoadBalancerAttributesInput(**_params)
        response = self._boto_client.describe_load_balancer_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBalancerAttributesOutput.from_boto(response)

    def describe_load_balancer_policies(
        self,
        _request: shapes.DescribeLoadBalancerPoliciesInput = None,
        *,
        load_balancer_name: str = ShapeBase.NOT_SET,
        policy_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLoadBalancerPoliciesOutput:
        """
        Describes the specified policies.

        If you specify a load balancer name, the action returns the descriptions of all
        policies created for the load balancer. If you specify a policy name associated
        with your load balancer, the action returns the description of that policy. If
        you don't specify a load balancer name, the action returns descriptions of the
        specified sample policies, or descriptions of all sample policies. The names of
        the sample policies have the `ELBSample-` prefix.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if policy_names is not ShapeBase.NOT_SET:
                _params['policy_names'] = policy_names
            _request = shapes.DescribeLoadBalancerPoliciesInput(**_params)
        response = self._boto_client.describe_load_balancer_policies(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBalancerPoliciesOutput.from_boto(response)

    def describe_load_balancer_policy_types(
        self,
        _request: shapes.DescribeLoadBalancerPolicyTypesInput = None,
        *,
        policy_type_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLoadBalancerPolicyTypesOutput:
        """
        Describes the specified load balancer policy types or all load balancer policy
        types.

        The description of each type indicates how it can be used. For example, some
        policies can be used only with layer 7 listeners, some policies can be used only
        with layer 4 listeners, and some policies can be used only with your EC2
        instances.

        You can use CreateLoadBalancerPolicy to create a policy configuration for any of
        these policy types. Then, depending on the policy type, use either
        SetLoadBalancerPoliciesOfListener or SetLoadBalancerPoliciesForBackendServer to
        set the policy.
        """
        if _request is None:
            _params = {}
            if policy_type_names is not ShapeBase.NOT_SET:
                _params['policy_type_names'] = policy_type_names
            _request = shapes.DescribeLoadBalancerPolicyTypesInput(**_params)
        response = self._boto_client.describe_load_balancer_policy_types(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBalancerPolicyTypesOutput.from_boto(response)

    def describe_load_balancers(
        self,
        _request: shapes.DescribeAccessPointsInput = None,
        *,
        load_balancer_names: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAccessPointsOutput:
        """
        Describes the specified the load balancers. If no load balancers are specified,
        the call describes all of your load balancers.
        """
        if _request is None:
            _params = {}
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.DescribeAccessPointsInput(**_params)
        paginator = self.get_paginator("describe_load_balancers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeAccessPointsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeAccessPointsOutput.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsInput = None,
        *,
        load_balancer_names: typing.List[str],
    ) -> shapes.DescribeTagsOutput:
        """
        Describes the tags associated with the specified load balancers.
        """
        if _request is None:
            _params = {}
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            _request = shapes.DescribeTagsInput(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.DescribeTagsOutput.from_boto(response)

    def detach_load_balancer_from_subnets(
        self,
        _request: shapes.DetachLoadBalancerFromSubnetsInput = None,
        *,
        load_balancer_name: str,
        subnets: typing.List[str],
    ) -> shapes.DetachLoadBalancerFromSubnetsOutput:
        """
        Removes the specified subnets from the set of configured subnets for the load
        balancer.

        After a subnet is removed, all EC2 instances registered with the load balancer
        in the removed subnet go into the `OutOfService` state. Then, the load balancer
        balances the traffic among the remaining routable subnets.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if subnets is not ShapeBase.NOT_SET:
                _params['subnets'] = subnets
            _request = shapes.DetachLoadBalancerFromSubnetsInput(**_params)
        response = self._boto_client.detach_load_balancer_from_subnets(
            **_request.to_boto()
        )

        return shapes.DetachLoadBalancerFromSubnetsOutput.from_boto(response)

    def disable_availability_zones_for_load_balancer(
        self,
        _request: shapes.RemoveAvailabilityZonesInput = None,
        *,
        load_balancer_name: str,
        availability_zones: typing.List[str],
    ) -> shapes.RemoveAvailabilityZonesOutput:
        """
        Removes the specified Availability Zones from the set of Availability Zones for
        the specified load balancer in EC2-Classic or a default VPC.

        For load balancers in a non-default VPC, use DetachLoadBalancerFromSubnets.

        There must be at least one Availability Zone registered with a load balancer at
        all times. After an Availability Zone is removed, all instances registered with
        the load balancer that are in the removed Availability Zone go into the
        `OutOfService` state. Then, the load balancer attempts to equally balance the
        traffic among its remaining Availability Zones.

        For more information, see [Add or Remove Availability
        Zones](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
        disable-az.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            _request = shapes.RemoveAvailabilityZonesInput(**_params)
        response = self._boto_client.disable_availability_zones_for_load_balancer(
            **_request.to_boto()
        )

        return shapes.RemoveAvailabilityZonesOutput.from_boto(response)

    def enable_availability_zones_for_load_balancer(
        self,
        _request: shapes.AddAvailabilityZonesInput = None,
        *,
        load_balancer_name: str,
        availability_zones: typing.List[str],
    ) -> shapes.AddAvailabilityZonesOutput:
        """
        Adds the specified Availability Zones to the set of Availability Zones for the
        specified load balancer in EC2-Classic or a default VPC.

        For load balancers in a non-default VPC, use AttachLoadBalancerToSubnets.

        The load balancer evenly distributes requests across all its registered
        Availability Zones that contain instances. For more information, see [Add or
        Remove Availability
        Zones](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
        disable-az.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if availability_zones is not ShapeBase.NOT_SET:
                _params['availability_zones'] = availability_zones
            _request = shapes.AddAvailabilityZonesInput(**_params)
        response = self._boto_client.enable_availability_zones_for_load_balancer(
            **_request.to_boto()
        )

        return shapes.AddAvailabilityZonesOutput.from_boto(response)

    def modify_load_balancer_attributes(
        self,
        _request: shapes.ModifyLoadBalancerAttributesInput = None,
        *,
        load_balancer_name: str,
        load_balancer_attributes: shapes.LoadBalancerAttributes,
    ) -> shapes.ModifyLoadBalancerAttributesOutput:
        """
        Modifies the attributes of the specified load balancer.

        You can modify the load balancer attributes, such as `AccessLogs`,
        `ConnectionDraining`, and `CrossZoneLoadBalancing` by either enabling or
        disabling them. Or, you can modify the load balancer attribute
        `ConnectionSettings` by specifying an idle connection timeout value for your
        load balancer.

        For more information, see the following in the _Classic Load Balancers Guide_ :

          * [Cross-Zone Load Balancing](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html)

          * [Connection Draining](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html)

          * [Access Logs](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html)

          * [Idle Connection Timeout](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html)
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if load_balancer_attributes is not ShapeBase.NOT_SET:
                _params['load_balancer_attributes'] = load_balancer_attributes
            _request = shapes.ModifyLoadBalancerAttributesInput(**_params)
        response = self._boto_client.modify_load_balancer_attributes(
            **_request.to_boto()
        )

        return shapes.ModifyLoadBalancerAttributesOutput.from_boto(response)

    def register_instances_with_load_balancer(
        self,
        _request: shapes.RegisterEndPointsInput = None,
        *,
        load_balancer_name: str,
        instances: typing.List[shapes.Instance],
    ) -> shapes.RegisterEndPointsOutput:
        """
        Adds the specified instances to the specified load balancer.

        The instance must be a running instance in the same network as the load balancer
        (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load
        balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic
        instances to that VPC and then register the linked EC2-Classic instances with
        the load balancer in the VPC.

        Note that `RegisterInstanceWithLoadBalancer` completes when the request has been
        registered. Instance registration takes a little time to complete. To check the
        state of the registered instances, use DescribeLoadBalancers or
        DescribeInstanceHealth.

        After the instance is registered, it starts receiving traffic and requests from
        the load balancer. Any instance that is not in one of the Availability Zones
        registered for the load balancer is moved to the `OutOfService` state. If an
        Availability Zone is added to the load balancer later, any instances registered
        with the load balancer move to the `InService` state.

        To deregister instances from a load balancer, use
        DeregisterInstancesFromLoadBalancer.

        For more information, see [Register or De-Register EC2
        Instances](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        deregister-register-instances.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instances is not ShapeBase.NOT_SET:
                _params['instances'] = instances
            _request = shapes.RegisterEndPointsInput(**_params)
        response = self._boto_client.register_instances_with_load_balancer(
            **_request.to_boto()
        )

        return shapes.RegisterEndPointsOutput.from_boto(response)

    def remove_tags(
        self,
        _request: shapes.RemoveTagsInput = None,
        *,
        load_balancer_names: typing.List[str],
        tags: typing.List[shapes.TagKeyOnly],
    ) -> shapes.RemoveTagsOutput:
        """
        Removes one or more tags from the specified load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_names is not ShapeBase.NOT_SET:
                _params['load_balancer_names'] = load_balancer_names
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.RemoveTagsInput(**_params)
        response = self._boto_client.remove_tags(**_request.to_boto())

        return shapes.RemoveTagsOutput.from_boto(response)

    def set_load_balancer_listener_ssl_certificate(
        self,
        _request: shapes.SetLoadBalancerListenerSSLCertificateInput = None,
        *,
        load_balancer_name: str,
        load_balancer_port: int,
        ssl_certificate_id: str,
    ) -> shapes.SetLoadBalancerListenerSSLCertificateOutput:
        """
        Sets the certificate that terminates the specified listener's SSL connections.
        The specified certificate replaces any prior certificate that was used on the
        same load balancer and port.

        For more information about updating your SSL certificate, see [Replace the SSL
        Certificate for Your Load
        Balancer](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        update-ssl-cert.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if load_balancer_port is not ShapeBase.NOT_SET:
                _params['load_balancer_port'] = load_balancer_port
            if ssl_certificate_id is not ShapeBase.NOT_SET:
                _params['ssl_certificate_id'] = ssl_certificate_id
            _request = shapes.SetLoadBalancerListenerSSLCertificateInput(
                **_params
            )
        response = self._boto_client.set_load_balancer_listener_ssl_certificate(
            **_request.to_boto()
        )

        return shapes.SetLoadBalancerListenerSSLCertificateOutput.from_boto(
            response
        )

    def set_load_balancer_policies_for_backend_server(
        self,
        _request: shapes.SetLoadBalancerPoliciesForBackendServerInput = None,
        *,
        load_balancer_name: str,
        instance_port: int,
        policy_names: typing.List[str],
    ) -> shapes.SetLoadBalancerPoliciesForBackendServerOutput:
        """
        Replaces the set of policies associated with the specified port on which the EC2
        instance is listening with a new set of policies. At this time, only the back-
        end server authentication policy type can be applied to the instance ports; this
        policy type is composed of multiple public key policies.

        Each time you use `SetLoadBalancerPoliciesForBackendServer` to enable the
        policies, use the `PolicyNames` parameter to list the policies that you want to
        enable.

        You can use DescribeLoadBalancers or DescribeLoadBalancerPolicies to verify that
        the policy is associated with the EC2 instance.

        For more information about enabling back-end instance authentication, see
        [Configure Back-end Instance
        Authentication](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        create-https-ssl-load-balancer.html#configure_backendauth_clt) in the _Classic
        Load Balancers Guide_. For more information about Proxy Protocol, see [Configure
        Proxy Protocol
        Support](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-
        proxy-protocol.html) in the _Classic Load Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instance_port is not ShapeBase.NOT_SET:
                _params['instance_port'] = instance_port
            if policy_names is not ShapeBase.NOT_SET:
                _params['policy_names'] = policy_names
            _request = shapes.SetLoadBalancerPoliciesForBackendServerInput(
                **_params
            )
        response = self._boto_client.set_load_balancer_policies_for_backend_server(
            **_request.to_boto()
        )

        return shapes.SetLoadBalancerPoliciesForBackendServerOutput.from_boto(
            response
        )

    def set_load_balancer_policies_of_listener(
        self,
        _request: shapes.SetLoadBalancerPoliciesOfListenerInput = None,
        *,
        load_balancer_name: str,
        load_balancer_port: int,
        policy_names: typing.List[str],
    ) -> shapes.SetLoadBalancerPoliciesOfListenerOutput:
        """
        Replaces the current set of policies for the specified load balancer port with
        the specified set of policies.

        To enable back-end server authentication, use
        SetLoadBalancerPoliciesForBackendServer.

        For more information about setting policies, see [Update the SSL Negotiation
        Configuration](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-
        config-update.html), [Duration-Based Session
        Stickiness](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        sticky-sessions.html#enable-sticky-sessions-duration), and [Application-
        Controlled Session
        Stickiness](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-
        sticky-sessions.html#enable-sticky-sessions-application) in the _Classic Load
        Balancers Guide_.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if load_balancer_port is not ShapeBase.NOT_SET:
                _params['load_balancer_port'] = load_balancer_port
            if policy_names is not ShapeBase.NOT_SET:
                _params['policy_names'] = policy_names
            _request = shapes.SetLoadBalancerPoliciesOfListenerInput(**_params)
        response = self._boto_client.set_load_balancer_policies_of_listener(
            **_request.to_boto()
        )

        return shapes.SetLoadBalancerPoliciesOfListenerOutput.from_boto(
            response
        )
