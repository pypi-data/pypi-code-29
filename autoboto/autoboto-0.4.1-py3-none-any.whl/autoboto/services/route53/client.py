import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("route53", *args, **kwargs)

    def associate_vpc_with_hosted_zone(
        self,
        _request: shapes.AssociateVPCWithHostedZoneRequest = None,
        *,
        hosted_zone_id: str,
        vpc: shapes.VPC,
        comment: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateVPCWithHostedZoneResponse:
        """
        Associates an Amazon VPC with a private hosted zone.

        To perform the association, the VPC and the private hosted zone must already
        exist. You can't convert a public hosted zone into a private hosted zone.

        If you want to associate a VPC that was created by using one AWS account with a
        private hosted zone that was created by using a different account, the AWS
        account that created the private hosted zone must first submit a
        `CreateVPCAssociationAuthorization` request. Then the account that created the
        VPC must submit an `AssociateVPCWithHostedZone` request.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.AssociateVPCWithHostedZoneRequest(**_params)
        response = self._boto_client.associate_vpc_with_hosted_zone(
            **_request.to_boto()
        )

        return shapes.AssociateVPCWithHostedZoneResponse.from_boto(response)

    def change_resource_record_sets(
        self,
        _request: shapes.ChangeResourceRecordSetsRequest = None,
        *,
        hosted_zone_id: str,
        change_batch: shapes.ChangeBatch,
    ) -> shapes.ChangeResourceRecordSetsResponse:
        """
        Creates, changes, or deletes a resource record set, which contains authoritative
        DNS information for a specified domain name or subdomain name. For example, you
        can use `ChangeResourceRecordSets` to create a resource record set that routes
        traffic for test.example.com to a web server that has an IP address of
        192.0.2.44.

        **Change Batches and Transactional Changes**

        The request body must include a document with a
        `ChangeResourceRecordSetsRequest` element. The request body contains a list of
        change items, known as a change batch. Change batches are considered
        transactional changes. When using the Amazon Route 53 API to change resource
        record sets, Amazon Route 53 either makes all or none of the changes in a change
        batch request. This ensures that Amazon Route 53 never partially implements the
        intended changes to the resource record sets in a hosted zone.

        For example, a change batch request that deletes the `CNAME` record for
        www.example.com and creates an alias resource record set for www.example.com.
        Amazon Route 53 deletes the first resource record set and creates the second
        resource record set in a single operation. If either the `DELETE` or the
        `CREATE` action fails, then both changes (plus any other changes in the batch)
        fail, and the original `CNAME` record continues to exist.

        Due to the nature of transactional changes, you can't delete the same resource
        record set more than once in a single change batch. If you attempt to delete the
        same change batch more than once, Amazon Route 53 returns an
        `InvalidChangeBatch` error.

        **Traffic Flow**

        To create resource record sets for complex routing configurations, use either
        the traffic flow visual editor in the Amazon Route 53 console or the API actions
        for traffic policies and traffic policy instances. Save the configuration as a
        traffic policy, then associate the traffic policy with one or more domain names
        (such as example.com) or subdomain names (such as www.example.com), in the same
        hosted zone or in multiple hosted zones. You can roll back the updates if the
        new configuration isn't performing as expected. For more information, see [Using
        Traffic Flow to Route DNS
        Traffic](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-
        flow.html) in the _Amazon Route 53 Developer Guide_.

        **Create, Delete, and Upsert**

        Use `ChangeResourceRecordsSetsRequest` to perform the following actions:

          * `CREATE`: Creates a resource record set that has the specified values.

          * `DELETE`: Deletes an existing resource record set that has the specified values.

          * `UPSERT`: If a resource record set does not already exist, AWS creates it. If a resource set does exist, Amazon Route 53 updates it with the values in the request. 

        **Syntaxes for Creating, Updating, and Deleting Resource Record Sets**

        The syntax for a request depends on the type of resource record set that you
        want to create, delete, or update, such as weighted, alias, or failover. The XML
        elements in your request must appear in the order listed in the syntax.

        For an example for each type of resource record set, see "Examples."

        Don't refer to the syntax in the "Parameter Syntax" section, which includes all
        of the elements for every kind of resource record set that you can create,
        delete, or update by using `ChangeResourceRecordSets`.

        **Change Propagation to Amazon Route 53 DNS Servers**

        When you submit a `ChangeResourceRecordSets` request, Amazon Route 53 propagates
        your changes to all of the Amazon Route 53 authoritative DNS servers. While your
        changes are propagating, `GetChange` returns a status of `PENDING`. When
        propagation is complete, `GetChange` returns a status of `INSYNC`. Changes
        generally propagate to all Amazon Route 53 name servers within 60 seconds. For
        more information, see GetChange.

        **Limits on ChangeResourceRecordSets Requests**

        For information about the limits on a `ChangeResourceRecordSets` request, see
        [Limits](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html)
        in the _Amazon Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if change_batch is not ShapeBase.NOT_SET:
                _params['change_batch'] = change_batch
            _request = shapes.ChangeResourceRecordSetsRequest(**_params)
        response = self._boto_client.change_resource_record_sets(
            **_request.to_boto()
        )

        return shapes.ChangeResourceRecordSetsResponse.from_boto(response)

    def change_tags_for_resource(
        self,
        _request: shapes.ChangeTagsForResourceRequest = None,
        *,
        resource_type: typing.Union[str, shapes.TagResourceType],
        resource_id: str,
        add_tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        remove_tag_keys: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ChangeTagsForResourceResponse:
        """
        Adds, edits, or deletes tags for a health check or a hosted zone.

        For information about using tags for cost allocation, see [Using Cost Allocation
        Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-
        tags.html) in the _AWS Billing and Cost Management User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if add_tags is not ShapeBase.NOT_SET:
                _params['add_tags'] = add_tags
            if remove_tag_keys is not ShapeBase.NOT_SET:
                _params['remove_tag_keys'] = remove_tag_keys
            _request = shapes.ChangeTagsForResourceRequest(**_params)
        response = self._boto_client.change_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ChangeTagsForResourceResponse.from_boto(response)

    def create_health_check(
        self,
        _request: shapes.CreateHealthCheckRequest = None,
        *,
        caller_reference: str,
        health_check_config: shapes.HealthCheckConfig,
    ) -> shapes.CreateHealthCheckResponse:
        """
        Creates a new health check.

        For information about adding health checks to resource record sets, see
        ResourceRecordSet$HealthCheckId in ChangeResourceRecordSets.

        **ELB Load Balancers**

        If you're registering EC2 instances with an Elastic Load Balancing (ELB) load
        balancer, do not create Amazon Route 53 health checks for the EC2 instances.
        When you register an EC2 instance with a load balancer, you configure settings
        for an ELB health check, which performs a similar function to an Amazon Route 53
        health check.

        **Private Hosted Zones**

        You can associate health checks with failover resource record sets in a private
        hosted zone. Note the following:

          * Amazon Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.

          * You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server.

          * You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 `StatusCheckFailed` metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the [Amazon CloudWatch User Guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html).
        """
        if _request is None:
            _params = {}
            if caller_reference is not ShapeBase.NOT_SET:
                _params['caller_reference'] = caller_reference
            if health_check_config is not ShapeBase.NOT_SET:
                _params['health_check_config'] = health_check_config
            _request = shapes.CreateHealthCheckRequest(**_params)
        response = self._boto_client.create_health_check(**_request.to_boto())

        return shapes.CreateHealthCheckResponse.from_boto(response)

    def create_hosted_zone(
        self,
        _request: shapes.CreateHostedZoneRequest = None,
        *,
        name: str,
        caller_reference: str,
        vpc: shapes.VPC = ShapeBase.NOT_SET,
        hosted_zone_config: shapes.HostedZoneConfig = ShapeBase.NOT_SET,
        delegation_set_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateHostedZoneResponse:
        """
        Creates a new public hosted zone, which you use to specify how the Domain Name
        System (DNS) routes traffic on the Internet for a domain, such as example.com,
        and its subdomains.

        You can't convert a public hosted zones to a private hosted zone or vice versa.
        Instead, you must create a new hosted zone with the same name and create new
        resource record sets.

        For more information about charges for hosted zones, see [Amazon Route 53
        Pricing](http://aws.amazon.com/route53/pricing/).

        Note the following:

          * You can't create a hosted zone for a top-level domain (TLD).

          * Amazon Route 53 automatically creates a default SOA record and four NS records for the zone. For more information about SOA and NS records, see [NS and SOA Records that Amazon Route 53 Creates for a Hosted Zone](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html) in the _Amazon Route 53 Developer Guide_.

        If you want to use the same name servers for multiple hosted zones, you can
        optionally associate a reusable delegation set with the hosted zone. See the
        `DelegationSetId` element.

          * If your domain is registered with a registrar other than Amazon Route 53, you must update the name servers with your registrar to make Amazon Route 53 your DNS service. For more information, see [Configuring Amazon Route 53 as your DNS Service](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-migrating.html) in the _Amazon Route 53 Developer Guide_. 

        When you submit a `CreateHostedZone` request, the initial status of the hosted
        zone is `PENDING`. This means that the NS and SOA records are not yet available
        on all Amazon Route 53 DNS servers. When the NS and SOA records are available,
        the status of the zone changes to `INSYNC`.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if caller_reference is not ShapeBase.NOT_SET:
                _params['caller_reference'] = caller_reference
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            if hosted_zone_config is not ShapeBase.NOT_SET:
                _params['hosted_zone_config'] = hosted_zone_config
            if delegation_set_id is not ShapeBase.NOT_SET:
                _params['delegation_set_id'] = delegation_set_id
            _request = shapes.CreateHostedZoneRequest(**_params)
        response = self._boto_client.create_hosted_zone(**_request.to_boto())

        return shapes.CreateHostedZoneResponse.from_boto(response)

    def create_query_logging_config(
        self,
        _request: shapes.CreateQueryLoggingConfigRequest = None,
        *,
        hosted_zone_id: str,
        cloud_watch_logs_log_group_arn: str,
    ) -> shapes.CreateQueryLoggingConfigResponse:
        """
        Creates a configuration for DNS query logging. After you create a query logging
        configuration, Amazon Route 53 begins to publish log data to an Amazon
        CloudWatch Logs log group.

        DNS query logs contain information about the queries that Amazon Route 53
        receives for a specified public hosted zone, such as the following:

          * Amazon Route 53 edge location that responded to the DNS query

          * Domain or subdomain that was requested

          * DNS record type, such as A or AAAA

          * DNS response code, such as `NoError` or `ServFail`

        Log Group and Resource Policy



        Before you create a query logging configuration, perform the following
        operations.

        If you create a query logging configuration using the Amazon Route 53 console,
        Amazon Route 53 performs these operations automatically.

          1. Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following:

            * You must create the log group in the us-east-1 region.

            * You must use the same AWS account to create the log group and the hosted zone that you want to configure query logging for.

            * When you create log groups for query logging, we recommend that you use a consistent prefix, for example:

        `/aws/route53/ _hosted zone name_ `

        In the next step, you'll create a resource policy, which controls access to one
        or more log groups and the associated AWS resources, such as Amazon Route 53
        hosted zones. There's a limit on the number of resource policies that you can
        create, so we recommend that you use a consistent prefix so you can use the same
        resource policy for all the log groups that you create for query logging.

          2. Create a CloudWatch Logs resource policy, and give it the permissions that Amazon Route 53 needs to create log streams and to send query logs to log streams. For the value of `Resource`, specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with `*`, for example:

        `arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*`

        You can't use the CloudWatch console to create or edit a resource policy. You
        must use the CloudWatch API, one of the AWS SDKs, or the AWS CLI.

        Log Streams and Edge Locations



        When Amazon Route 53 finishes creating the configuration for DNS query logging,
        it does the following:

          * Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Amazon Route 53 responds to for that edge location.

          * Begins to send query logs to the applicable log stream.

        The name of each log stream is in the following format:

        ` _hosted zone ID_ / _edge location code_ `

        The edge location code is a three-letter code and an arbitrarily assigned
        number, for example, DFW3. The three-letter code typically corresponds with the
        International Air Transport Association airport code for an airport near the
        edge location. (These abbreviations might change in the future.) For a list of
        edge locations, see "The Amazon Route 53 Global Network" on the [Amazon Route 53
        Product Details](http://aws.amazon.com/route53/details/) page.

        Queries That Are Logged



        Query logs contain only the queries that DNS resolvers forward to Amazon Route
        53. If a DNS resolver has already cached the response to a query (such as the IP
        address for a load balancer for example.com), the resolver will continue to
        return the cached response. It doesn't forward another query to Amazon Route 53
        until the TTL for the corresponding resource record set expires. Depending on
        how many DNS queries are submitted for a resource record set, and depending on
        the TTL for that resource record set, query logs might contain information about
        only one query out of every several thousand queries that are submitted to DNS.
        For more information about how DNS works, see [Routing Internet Traffic to Your
        Website or Web
        Application](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-
        dns-service.html) in the _Amazon Route 53 Developer Guide_.

        Log File Format



        For a list of the values in each query log and the format of each value, see
        [Logging DNS
        Queries](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-
        logs.html) in the _Amazon Route 53 Developer Guide_.

        Pricing



        For information about charges for query logs, see [Amazon CloudWatch
        Pricing](http://aws.amazon.com/cloudwatch/pricing/).

        How to Stop Logging



        If you want Amazon Route 53 to stop sending query logs to CloudWatch Logs,
        delete the query logging configuration. For more information, see
        DeleteQueryLoggingConfig.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if cloud_watch_logs_log_group_arn is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_log_group_arn'
                       ] = cloud_watch_logs_log_group_arn
            _request = shapes.CreateQueryLoggingConfigRequest(**_params)
        response = self._boto_client.create_query_logging_config(
            **_request.to_boto()
        )

        return shapes.CreateQueryLoggingConfigResponse.from_boto(response)

    def create_reusable_delegation_set(
        self,
        _request: shapes.CreateReusableDelegationSetRequest = None,
        *,
        caller_reference: str,
        hosted_zone_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateReusableDelegationSetResponse:
        """
        Creates a delegation set (a group of four name servers) that can be reused by
        multiple hosted zones. If a hosted zoned ID is specified,
        `CreateReusableDelegationSet` marks the delegation set associated with that zone
        as reusable.

        You can't associate a reusable delegation set with a private hosted zone.

        For information about using a reusable delegation set to configure white label
        name servers, see [Configuring White Label Name
        Servers](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-
        name-servers.html).

        The process for migrating existing hosted zones to use a reusable delegation set
        is comparable to the process for configuring white label name servers. You need
        to perform the following steps:

          1. Create a reusable delegation set.

          2. Recreate hosted zones, and reduce the TTL to 60 seconds or less.

          3. Recreate resource record sets in the new hosted zones.

          4. Change the registrar's name servers to use the name servers for the new hosted zones.

          5. Monitor traffic for the website or application.

          6. Change TTLs back to their original values.

        If you want to migrate existing hosted zones to use a reusable delegation set,
        the existing hosted zones can't use any of the name servers that are assigned to
        the reusable delegation set. If one or more hosted zones do use one or more name
        servers that are assigned to the reusable delegation set, you can do one of the
        following:

          * For small numbers of hosted zones—up to a few hundred—it's relatively easy to create reusable delegation sets until you get one that has four name servers that don't overlap with any of the name servers in your hosted zones.

          * For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.

          * For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that don't have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.
        """
        if _request is None:
            _params = {}
            if caller_reference is not ShapeBase.NOT_SET:
                _params['caller_reference'] = caller_reference
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            _request = shapes.CreateReusableDelegationSetRequest(**_params)
        response = self._boto_client.create_reusable_delegation_set(
            **_request.to_boto()
        )

        return shapes.CreateReusableDelegationSetResponse.from_boto(response)

    def create_traffic_policy(
        self,
        _request: shapes.CreateTrafficPolicyRequest = None,
        *,
        name: str,
        document: str,
        comment: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateTrafficPolicyResponse:
        """
        Creates a traffic policy, which you use to create multiple DNS resource record
        sets for one domain name (such as example.com) or one subdomain name (such as
        www.example.com).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document is not ShapeBase.NOT_SET:
                _params['document'] = document
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.CreateTrafficPolicyRequest(**_params)
        response = self._boto_client.create_traffic_policy(**_request.to_boto())

        return shapes.CreateTrafficPolicyResponse.from_boto(response)

    def create_traffic_policy_instance(
        self,
        _request: shapes.CreateTrafficPolicyInstanceRequest = None,
        *,
        hosted_zone_id: str,
        name: str,
        ttl: int,
        traffic_policy_id: str,
        traffic_policy_version: int,
    ) -> shapes.CreateTrafficPolicyInstanceResponse:
        """
        Creates resource record sets in a specified hosted zone based on the settings in
        a specified traffic policy version. In addition, `CreateTrafficPolicyInstance`
        associates the resource record sets with a specified domain name (such as
        example.com) or subdomain name (such as www.example.com). Amazon Route 53
        responds to DNS queries for the domain or subdomain name by using the resource
        record sets that `CreateTrafficPolicyInstance` created.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if ttl is not ShapeBase.NOT_SET:
                _params['ttl'] = ttl
            if traffic_policy_id is not ShapeBase.NOT_SET:
                _params['traffic_policy_id'] = traffic_policy_id
            if traffic_policy_version is not ShapeBase.NOT_SET:
                _params['traffic_policy_version'] = traffic_policy_version
            _request = shapes.CreateTrafficPolicyInstanceRequest(**_params)
        response = self._boto_client.create_traffic_policy_instance(
            **_request.to_boto()
        )

        return shapes.CreateTrafficPolicyInstanceResponse.from_boto(response)

    def create_traffic_policy_version(
        self,
        _request: shapes.CreateTrafficPolicyVersionRequest = None,
        *,
        id: str,
        document: str,
        comment: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateTrafficPolicyVersionResponse:
        """
        Creates a new version of an existing traffic policy. When you create a new
        version of a traffic policy, you specify the ID of the traffic policy that you
        want to update and a JSON-formatted document that describes the new version. You
        use traffic policies to create multiple DNS resource record sets for one domain
        name (such as example.com) or one subdomain name (such as www.example.com). You
        can create a maximum of 1000 versions of a traffic policy. If you reach the
        limit and need to create another version, you'll need to start a new traffic
        policy.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if document is not ShapeBase.NOT_SET:
                _params['document'] = document
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.CreateTrafficPolicyVersionRequest(**_params)
        response = self._boto_client.create_traffic_policy_version(
            **_request.to_boto()
        )

        return shapes.CreateTrafficPolicyVersionResponse.from_boto(response)

    def create_vpc_association_authorization(
        self,
        _request: shapes.CreateVPCAssociationAuthorizationRequest = None,
        *,
        hosted_zone_id: str,
        vpc: shapes.VPC,
    ) -> shapes.CreateVPCAssociationAuthorizationResponse:
        """
        Authorizes the AWS account that created a specified VPC to submit an
        `AssociateVPCWithHostedZone` request to associate the VPC with a specified
        hosted zone that was created by a different account. To submit a
        `CreateVPCAssociationAuthorization` request, you must use the account that
        created the hosted zone. After you authorize the association, use the account
        that created the VPC to submit an `AssociateVPCWithHostedZone` request.

        If you want to associate multiple VPCs that you created by using one account
        with a hosted zone that you created by using a different account, you must
        submit one authorization request for each VPC.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            _request = shapes.CreateVPCAssociationAuthorizationRequest(
                **_params
            )
        response = self._boto_client.create_vpc_association_authorization(
            **_request.to_boto()
        )

        return shapes.CreateVPCAssociationAuthorizationResponse.from_boto(
            response
        )

    def delete_health_check(
        self,
        _request: shapes.DeleteHealthCheckRequest = None,
        *,
        health_check_id: str,
    ) -> shapes.DeleteHealthCheckResponse:
        """
        Deletes a health check.

        Amazon Route 53 does not prevent you from deleting a health check even if the
        health check is associated with one or more resource record sets. If you delete
        a health check and you don't update the associated resource record sets, the
        future status of the health check can't be predicted and may change. This will
        affect the routing of DNS queries for your DNS failover configuration. For more
        information, see [Replacing and Deleting Health
        Checks](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-
        creating-deleting.html#health-checks-deleting.html) in the _Amazon Route 53
        Developer Guide_.
        """
        if _request is None:
            _params = {}
            if health_check_id is not ShapeBase.NOT_SET:
                _params['health_check_id'] = health_check_id
            _request = shapes.DeleteHealthCheckRequest(**_params)
        response = self._boto_client.delete_health_check(**_request.to_boto())

        return shapes.DeleteHealthCheckResponse.from_boto(response)

    def delete_hosted_zone(
        self,
        _request: shapes.DeleteHostedZoneRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteHostedZoneResponse:
        """
        Deletes a hosted zone.

        If the name servers for the hosted zone are associated with a domain and if you
        want to make the domain unavailable on the Internet, we recommend that you
        delete the name servers from the domain to prevent future DNS queries from
        possibly being misrouted. If the domain is registered with Amazon Route 53, see
        `UpdateDomainNameservers`. If the domain is registered with another registrar,
        use the method provided by the registrar to delete name servers for the domain.

        Some domain registries don't allow you to remove all of the name servers for a
        domain. If the registry for your domain requires one or more name servers, we
        recommend that you delete the hosted zone only if you transfer DNS service to
        another service provider, and you replace the name servers for the domain with
        name servers from the new provider.

        You can delete a hosted zone only if it contains only the default SOA record and
        NS resource record sets. If the hosted zone contains other resource record sets,
        you must delete them before you can delete the hosted zone. If you try to delete
        a hosted zone that contains other resource record sets, the request fails, and
        Amazon Route 53 returns a `HostedZoneNotEmpty` error. For information about
        deleting records from your hosted zone, see ChangeResourceRecordSets.

        To verify that the hosted zone has been deleted, do one of the following:

          * Use the `GetHostedZone` action to request information about the hosted zone.

          * Use the `ListHostedZones` action to get a list of the hosted zones associated with the current AWS account.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteHostedZoneRequest(**_params)
        response = self._boto_client.delete_hosted_zone(**_request.to_boto())

        return shapes.DeleteHostedZoneResponse.from_boto(response)

    def delete_query_logging_config(
        self,
        _request: shapes.DeleteQueryLoggingConfigRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteQueryLoggingConfigResponse:
        """
        Deletes a configuration for DNS query logging. If you delete a configuration,
        Amazon Route 53 stops sending query logs to CloudWatch Logs. Amazon Route 53
        doesn't delete any logs that are already in CloudWatch Logs.

        For more information about DNS query logs, see CreateQueryLoggingConfig.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteQueryLoggingConfigRequest(**_params)
        response = self._boto_client.delete_query_logging_config(
            **_request.to_boto()
        )

        return shapes.DeleteQueryLoggingConfigResponse.from_boto(response)

    def delete_reusable_delegation_set(
        self,
        _request: shapes.DeleteReusableDelegationSetRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteReusableDelegationSetResponse:
        """
        Deletes a reusable delegation set.

        You can delete a reusable delegation set only if it isn't associated with any
        hosted zones.

        To verify that the reusable delegation set is not associated with any hosted
        zones, submit a GetReusableDelegationSet request and specify the ID of the
        reusable delegation set that you want to delete.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteReusableDelegationSetRequest(**_params)
        response = self._boto_client.delete_reusable_delegation_set(
            **_request.to_boto()
        )

        return shapes.DeleteReusableDelegationSetResponse.from_boto(response)

    def delete_traffic_policy(
        self,
        _request: shapes.DeleteTrafficPolicyRequest = None,
        *,
        id: str,
        version: int,
    ) -> shapes.DeleteTrafficPolicyResponse:
        """
        Deletes a traffic policy.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.DeleteTrafficPolicyRequest(**_params)
        response = self._boto_client.delete_traffic_policy(**_request.to_boto())

        return shapes.DeleteTrafficPolicyResponse.from_boto(response)

    def delete_traffic_policy_instance(
        self,
        _request: shapes.DeleteTrafficPolicyInstanceRequest = None,
        *,
        id: str,
    ) -> shapes.DeleteTrafficPolicyInstanceResponse:
        """
        Deletes a traffic policy instance and all of the resource record sets that
        Amazon Route 53 created when you created the instance.

        In the Amazon Route 53 console, traffic policy instances are known as policy
        records.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.DeleteTrafficPolicyInstanceRequest(**_params)
        response = self._boto_client.delete_traffic_policy_instance(
            **_request.to_boto()
        )

        return shapes.DeleteTrafficPolicyInstanceResponse.from_boto(response)

    def delete_vpc_association_authorization(
        self,
        _request: shapes.DeleteVPCAssociationAuthorizationRequest = None,
        *,
        hosted_zone_id: str,
        vpc: shapes.VPC,
    ) -> shapes.DeleteVPCAssociationAuthorizationResponse:
        """
        Removes authorization to submit an `AssociateVPCWithHostedZone` request to
        associate a specified VPC with a hosted zone that was created by a different
        account. You must use the account that created the hosted zone to submit a
        `DeleteVPCAssociationAuthorization` request.

        Sending this request only prevents the AWS account that created the VPC from
        associating the VPC with the Amazon Route 53 hosted zone in the future. If the
        VPC is already associated with the hosted zone,
        `DeleteVPCAssociationAuthorization` won't disassociate the VPC from the hosted
        zone. If you want to delete an existing association, use
        `DisassociateVPCFromHostedZone`.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            _request = shapes.DeleteVPCAssociationAuthorizationRequest(
                **_params
            )
        response = self._boto_client.delete_vpc_association_authorization(
            **_request.to_boto()
        )

        return shapes.DeleteVPCAssociationAuthorizationResponse.from_boto(
            response
        )

    def disassociate_vpc_from_hosted_zone(
        self,
        _request: shapes.DisassociateVPCFromHostedZoneRequest = None,
        *,
        hosted_zone_id: str,
        vpc: shapes.VPC,
        comment: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateVPCFromHostedZoneResponse:
        """
        Disassociates a VPC from a Amazon Route 53 private hosted zone.

        You can't disassociate the last VPC from a private hosted zone.

        You can't disassociate a VPC from a private hosted zone when only one VPC is
        associated with the hosted zone. You also can't convert a private hosted zone
        into a public hosted zone.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if vpc is not ShapeBase.NOT_SET:
                _params['vpc'] = vpc
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.DisassociateVPCFromHostedZoneRequest(**_params)
        response = self._boto_client.disassociate_vpc_from_hosted_zone(
            **_request.to_boto()
        )

        return shapes.DisassociateVPCFromHostedZoneResponse.from_boto(response)

    def get_account_limit(
        self,
        _request: shapes.GetAccountLimitRequest = None,
        *,
        type: typing.Union[str, shapes.AccountLimitType],
    ) -> shapes.GetAccountLimitResponse:
        """
        Gets the specified limit for the current account, for example, the maximum
        number of health checks that you can create using the account.

        For the default limit, see
        [Limits](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html)
        in the _Amazon Route 53 Developer Guide_. To request a higher limit, [open a
        case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-
        limit-increase&limitType=service-code-route53).
        """
        if _request is None:
            _params = {}
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            _request = shapes.GetAccountLimitRequest(**_params)
        response = self._boto_client.get_account_limit(**_request.to_boto())

        return shapes.GetAccountLimitResponse.from_boto(response)

    def get_change(
        self,
        _request: shapes.GetChangeRequest = None,
        *,
        id: str,
    ) -> shapes.GetChangeResponse:
        """
        Returns the current status of a change batch request. The status is one of the
        following values:

          * `PENDING` indicates that the changes in this request have not propagated to all Amazon Route 53 DNS servers. This is the initial status of all change batch requests.

          * `INSYNC` indicates that the changes have propagated to all Amazon Route 53 DNS servers.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetChangeRequest(**_params)
        response = self._boto_client.get_change(**_request.to_boto())

        return shapes.GetChangeResponse.from_boto(response)

    def get_checker_ip_ranges(
        self,
        _request: shapes.GetCheckerIpRangesRequest = None,
    ) -> shapes.GetCheckerIpRangesResponse:
        """
        `GetCheckerIpRanges` still works, but we recommend that you download ip-
        ranges.json, which includes IP address ranges for all AWS services. For more
        information, see [IP Address Ranges of Amazon Route 53
        Servers](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-
        addresses.html) in the _Amazon Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetCheckerIpRangesRequest(**_params)
        response = self._boto_client.get_checker_ip_ranges(**_request.to_boto())

        return shapes.GetCheckerIpRangesResponse.from_boto(response)

    def get_geo_location(
        self,
        _request: shapes.GetGeoLocationRequest = None,
        *,
        continent_code: str = ShapeBase.NOT_SET,
        country_code: str = ShapeBase.NOT_SET,
        subdivision_code: str = ShapeBase.NOT_SET,
    ) -> shapes.GetGeoLocationResponse:
        """
        Gets information about whether a specified geographic location is supported for
        Amazon Route 53 geolocation resource record sets.

        Use the following syntax to determine whether a continent is supported for
        geolocation:

        `GET /2013-04-01/geolocation?ContinentCode= _two-letter abbreviation for a
        continent_ `

        Use the following syntax to determine whether a country is supported for
        geolocation:

        `GET /2013-04-01/geolocation?CountryCode= _two-character country code_ `

        Use the following syntax to determine whether a subdivision of a country is
        supported for geolocation:

        `GET /2013-04-01/geolocation?CountryCode= _two-character country code_
        &SubdivisionCode= _subdivision code_ `
        """
        if _request is None:
            _params = {}
            if continent_code is not ShapeBase.NOT_SET:
                _params['continent_code'] = continent_code
            if country_code is not ShapeBase.NOT_SET:
                _params['country_code'] = country_code
            if subdivision_code is not ShapeBase.NOT_SET:
                _params['subdivision_code'] = subdivision_code
            _request = shapes.GetGeoLocationRequest(**_params)
        response = self._boto_client.get_geo_location(**_request.to_boto())

        return shapes.GetGeoLocationResponse.from_boto(response)

    def get_health_check(
        self,
        _request: shapes.GetHealthCheckRequest = None,
        *,
        health_check_id: str,
    ) -> shapes.GetHealthCheckResponse:
        """
        Gets information about a specified health check.
        """
        if _request is None:
            _params = {}
            if health_check_id is not ShapeBase.NOT_SET:
                _params['health_check_id'] = health_check_id
            _request = shapes.GetHealthCheckRequest(**_params)
        response = self._boto_client.get_health_check(**_request.to_boto())

        return shapes.GetHealthCheckResponse.from_boto(response)

    def get_health_check_count(
        self,
        _request: shapes.GetHealthCheckCountRequest = None,
    ) -> shapes.GetHealthCheckCountResponse:
        """
        Retrieves the number of health checks that are associated with the current AWS
        account.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetHealthCheckCountRequest(**_params)
        response = self._boto_client.get_health_check_count(
            **_request.to_boto()
        )

        return shapes.GetHealthCheckCountResponse.from_boto(response)

    def get_health_check_last_failure_reason(
        self,
        _request: shapes.GetHealthCheckLastFailureReasonRequest = None,
        *,
        health_check_id: str,
    ) -> shapes.GetHealthCheckLastFailureReasonResponse:
        """
        Gets the reason that a specified health check failed most recently.
        """
        if _request is None:
            _params = {}
            if health_check_id is not ShapeBase.NOT_SET:
                _params['health_check_id'] = health_check_id
            _request = shapes.GetHealthCheckLastFailureReasonRequest(**_params)
        response = self._boto_client.get_health_check_last_failure_reason(
            **_request.to_boto()
        )

        return shapes.GetHealthCheckLastFailureReasonResponse.from_boto(
            response
        )

    def get_health_check_status(
        self,
        _request: shapes.GetHealthCheckStatusRequest = None,
        *,
        health_check_id: str,
    ) -> shapes.GetHealthCheckStatusResponse:
        """
        Gets status of a specified health check.
        """
        if _request is None:
            _params = {}
            if health_check_id is not ShapeBase.NOT_SET:
                _params['health_check_id'] = health_check_id
            _request = shapes.GetHealthCheckStatusRequest(**_params)
        response = self._boto_client.get_health_check_status(
            **_request.to_boto()
        )

        return shapes.GetHealthCheckStatusResponse.from_boto(response)

    def get_hosted_zone(
        self,
        _request: shapes.GetHostedZoneRequest = None,
        *,
        id: str,
    ) -> shapes.GetHostedZoneResponse:
        """
        Gets information about a specified hosted zone including the four name servers
        assigned to the hosted zone.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetHostedZoneRequest(**_params)
        response = self._boto_client.get_hosted_zone(**_request.to_boto())

        return shapes.GetHostedZoneResponse.from_boto(response)

    def get_hosted_zone_count(
        self,
        _request: shapes.GetHostedZoneCountRequest = None,
    ) -> shapes.GetHostedZoneCountResponse:
        """
        Retrieves the number of hosted zones that are associated with the current AWS
        account.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetHostedZoneCountRequest(**_params)
        response = self._boto_client.get_hosted_zone_count(**_request.to_boto())

        return shapes.GetHostedZoneCountResponse.from_boto(response)

    def get_hosted_zone_limit(
        self,
        _request: shapes.GetHostedZoneLimitRequest = None,
        *,
        type: typing.Union[str, shapes.HostedZoneLimitType],
        hosted_zone_id: str,
    ) -> shapes.GetHostedZoneLimitResponse:
        """
        Gets the specified limit for a specified hosted zone, for example, the maximum
        number of records that you can create in the hosted zone.

        For the default limit, see
        [Limits](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html)
        in the _Amazon Route 53 Developer Guide_. To request a higher limit, [open a
        case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-
        limit-increase&limitType=service-code-route53).
        """
        if _request is None:
            _params = {}
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            _request = shapes.GetHostedZoneLimitRequest(**_params)
        response = self._boto_client.get_hosted_zone_limit(**_request.to_boto())

        return shapes.GetHostedZoneLimitResponse.from_boto(response)

    def get_query_logging_config(
        self,
        _request: shapes.GetQueryLoggingConfigRequest = None,
        *,
        id: str,
    ) -> shapes.GetQueryLoggingConfigResponse:
        """
        Gets information about a specified configuration for DNS query logging.

        For more information about DNS query logs, see CreateQueryLoggingConfig and
        [Logging DNS
        Queries](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-
        logs.html).
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetQueryLoggingConfigRequest(**_params)
        response = self._boto_client.get_query_logging_config(
            **_request.to_boto()
        )

        return shapes.GetQueryLoggingConfigResponse.from_boto(response)

    def get_reusable_delegation_set(
        self,
        _request: shapes.GetReusableDelegationSetRequest = None,
        *,
        id: str,
    ) -> shapes.GetReusableDelegationSetResponse:
        """
        Retrieves information about a specified reusable delegation set, including the
        four name servers that are assigned to the delegation set.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetReusableDelegationSetRequest(**_params)
        response = self._boto_client.get_reusable_delegation_set(
            **_request.to_boto()
        )

        return shapes.GetReusableDelegationSetResponse.from_boto(response)

    def get_reusable_delegation_set_limit(
        self,
        _request: shapes.GetReusableDelegationSetLimitRequest = None,
        *,
        type: typing.Union[str, shapes.ReusableDelegationSetLimitType],
        delegation_set_id: str,
    ) -> shapes.GetReusableDelegationSetLimitResponse:
        """
        Gets the maximum number of hosted zones that you can associate with the
        specified reusable delegation set.

        For the default limit, see
        [Limits](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html)
        in the _Amazon Route 53 Developer Guide_. To request a higher limit, [open a
        case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-
        limit-increase&limitType=service-code-route53).
        """
        if _request is None:
            _params = {}
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if delegation_set_id is not ShapeBase.NOT_SET:
                _params['delegation_set_id'] = delegation_set_id
            _request = shapes.GetReusableDelegationSetLimitRequest(**_params)
        response = self._boto_client.get_reusable_delegation_set_limit(
            **_request.to_boto()
        )

        return shapes.GetReusableDelegationSetLimitResponse.from_boto(response)

    def get_traffic_policy(
        self,
        _request: shapes.GetTrafficPolicyRequest = None,
        *,
        id: str,
        version: int,
    ) -> shapes.GetTrafficPolicyResponse:
        """
        Gets information about a specific traffic policy version.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetTrafficPolicyRequest(**_params)
        response = self._boto_client.get_traffic_policy(**_request.to_boto())

        return shapes.GetTrafficPolicyResponse.from_boto(response)

    def get_traffic_policy_instance(
        self,
        _request: shapes.GetTrafficPolicyInstanceRequest = None,
        *,
        id: str,
    ) -> shapes.GetTrafficPolicyInstanceResponse:
        """
        Gets information about a specified traffic policy instance.

        After you submit a `CreateTrafficPolicyInstance` or an
        `UpdateTrafficPolicyInstance` request, there's a brief delay while Amazon Route
        53 creates the resource record sets that are specified in the traffic policy
        definition. For more information, see the `State` response element.

        In the Amazon Route 53 console, traffic policy instances are known as policy
        records.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetTrafficPolicyInstanceRequest(**_params)
        response = self._boto_client.get_traffic_policy_instance(
            **_request.to_boto()
        )

        return shapes.GetTrafficPolicyInstanceResponse.from_boto(response)

    def get_traffic_policy_instance_count(
        self,
        _request: shapes.GetTrafficPolicyInstanceCountRequest = None,
    ) -> shapes.GetTrafficPolicyInstanceCountResponse:
        """
        Gets the number of traffic policy instances that are associated with the current
        AWS account.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetTrafficPolicyInstanceCountRequest(**_params)
        response = self._boto_client.get_traffic_policy_instance_count(
            **_request.to_boto()
        )

        return shapes.GetTrafficPolicyInstanceCountResponse.from_boto(response)

    def list_geo_locations(
        self,
        _request: shapes.ListGeoLocationsRequest = None,
        *,
        start_continent_code: str = ShapeBase.NOT_SET,
        start_country_code: str = ShapeBase.NOT_SET,
        start_subdivision_code: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGeoLocationsResponse:
        """
        Retrieves a list of supported geo locations.

        Countries are listed first, and continents are listed last. If Amazon Route 53
        supports subdivisions for a country (for example, states or provinces), the
        subdivisions for that country are listed in alphabetical order immediately after
        the corresponding country.
        """
        if _request is None:
            _params = {}
            if start_continent_code is not ShapeBase.NOT_SET:
                _params['start_continent_code'] = start_continent_code
            if start_country_code is not ShapeBase.NOT_SET:
                _params['start_country_code'] = start_country_code
            if start_subdivision_code is not ShapeBase.NOT_SET:
                _params['start_subdivision_code'] = start_subdivision_code
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListGeoLocationsRequest(**_params)
        response = self._boto_client.list_geo_locations(**_request.to_boto())

        return shapes.ListGeoLocationsResponse.from_boto(response)

    def list_health_checks(
        self,
        _request: shapes.ListHealthChecksRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListHealthChecksResponse:
        """
        Retrieve a list of the health checks that are associated with the current AWS
        account.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListHealthChecksRequest(**_params)
        paginator = self.get_paginator("list_health_checks").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListHealthChecksResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListHealthChecksResponse.from_boto(response)

    def list_hosted_zones(
        self,
        _request: shapes.ListHostedZonesRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
        delegation_set_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ListHostedZonesResponse:
        """
        Retrieves a list of the public and private hosted zones that are associated with
        the current AWS account. The response includes a `HostedZones` child element for
        each hosted zone.

        Amazon Route 53 returns a maximum of 100 items in each response. If you have a
        lot of hosted zones, you can use the `maxitems` parameter to list them in groups
        of up to 100.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            if delegation_set_id is not ShapeBase.NOT_SET:
                _params['delegation_set_id'] = delegation_set_id
            _request = shapes.ListHostedZonesRequest(**_params)
        paginator = self.get_paginator("list_hosted_zones").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListHostedZonesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListHostedZonesResponse.from_boto(response)

    def list_hosted_zones_by_name(
        self,
        _request: shapes.ListHostedZonesByNameRequest = None,
        *,
        dns_name: str = ShapeBase.NOT_SET,
        hosted_zone_id: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListHostedZonesByNameResponse:
        """
        Retrieves a list of your hosted zones in lexicographic order. The response
        includes a `HostedZones` child element for each hosted zone created by the
        current AWS account.

        `ListHostedZonesByName` sorts hosted zones by name with the labels reversed. For
        example:

        `com.example.www.`

        Note the trailing dot, which can change the sort order in some circumstances.

        If the domain name includes escape characters or Punycode,
        `ListHostedZonesByName` alphabetizes the domain name using the escaped or
        Punycoded value, which is the format that Amazon Route 53 saves in its database.
        For example, to create a hosted zone for exämple.com, you specify ex\344mple.com
        for the domain name. `ListHostedZonesByName` alphabetizes it as:

        `com.ex\344mple.`

        The labels are reversed and alphabetized using the escaped value. For more
        information about valid domain name formats, including internationalized domain
        names, see [DNS Domain Name
        Format](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html)
        in the _Amazon Route 53 Developer Guide_.

        Amazon Route 53 returns up to 100 items in each response. If you have a lot of
        hosted zones, use the `MaxItems` parameter to list them in groups of up to 100.
        The response includes values that help navigate from one group of `MaxItems`
        hosted zones to the next:

          * The `DNSName` and `HostedZoneId` elements in the response contain the values, if any, specified for the `dnsname` and `hostedzoneid` parameters in the request that produced the current response.

          * The `MaxItems` element in the response contains the value, if any, that you specified for the `maxitems` parameter in the request that produced the current response.

          * If the value of `IsTruncated` in the response is true, there are more hosted zones associated with the current AWS account. 

        If `IsTruncated` is false, this response includes the last hosted zone that is
        associated with the current account. The `NextDNSName` element and
        `NextHostedZoneId` elements are omitted from the response.

          * The `NextDNSName` and `NextHostedZoneId` elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current AWS account. If you want to list more hosted zones, make another call to `ListHostedZonesByName`, and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.
        """
        if _request is None:
            _params = {}
            if dns_name is not ShapeBase.NOT_SET:
                _params['dns_name'] = dns_name
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListHostedZonesByNameRequest(**_params)
        response = self._boto_client.list_hosted_zones_by_name(
            **_request.to_boto()
        )

        return shapes.ListHostedZonesByNameResponse.from_boto(response)

    def list_query_logging_configs(
        self,
        _request: shapes.ListQueryLoggingConfigsRequest = None,
        *,
        hosted_zone_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: str = ShapeBase.NOT_SET,
    ) -> shapes.ListQueryLoggingConfigsResponse:
        """
        Lists the configurations for DNS query logging that are associated with the
        current AWS account or the configuration that is associated with a specified
        hosted zone.

        For more information about DNS query logs, see CreateQueryLoggingConfig.
        Additional information, including the format of DNS query logs, appears in
        [Logging DNS
        Queries](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-
        logs.html) in the _Amazon Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListQueryLoggingConfigsRequest(**_params)
        response = self._boto_client.list_query_logging_configs(
            **_request.to_boto()
        )

        return shapes.ListQueryLoggingConfigsResponse.from_boto(response)

    def list_resource_record_sets(
        self,
        _request: shapes.ListResourceRecordSetsRequest = None,
        *,
        hosted_zone_id: str,
        start_record_name: str = ShapeBase.NOT_SET,
        start_record_type: typing.Union[str, shapes.RRType] = ShapeBase.NOT_SET,
        start_record_identifier: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceRecordSetsResponse:
        """
        Lists the resource record sets in a specified hosted zone.

        `ListResourceRecordSets` returns up to 100 resource record sets at a time in
        ASCII order, beginning at a position specified by the `name` and `type`
        elements. The action sorts results first by DNS name with the labels reversed,
        for example:

        `com.example.www.`

        Note the trailing dot, which can change the sort order in some circumstances.

        When multiple records have the same DNS name, the action sorts results by the
        record type.

        You can use the name and type elements to adjust the beginning position of the
        list of resource record sets returned:

        If you do not specify Name or Type



        The results begin with the first resource record set that the hosted zone
        contains.

        If you specify Name but not Type



        The results begin with the first resource record set in the list whose name is
        greater than or equal to `Name`.

        If you specify Type but not Name



        Amazon Route 53 returns the `InvalidInput` error.

        If you specify both Name and Type



        The results begin with the first resource record set in the list whose name is
        greater than or equal to `Name`, and whose type is greater than or equal to
        `Type`.

        This action returns the most current version of the records. This includes
        records that are `PENDING`, and that are not yet available on all Amazon Route
        53 DNS servers.

        To ensure that you get an accurate listing of the resource record sets for a
        hosted zone at a point in time, do not submit a `ChangeResourceRecordSets`
        request while you're paging through the results of a `ListResourceRecordSets`
        request. If you do, some pages may display results without the latest changes
        while other pages display results with the latest changes.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if start_record_name is not ShapeBase.NOT_SET:
                _params['start_record_name'] = start_record_name
            if start_record_type is not ShapeBase.NOT_SET:
                _params['start_record_type'] = start_record_type
            if start_record_identifier is not ShapeBase.NOT_SET:
                _params['start_record_identifier'] = start_record_identifier
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListResourceRecordSetsRequest(**_params)
        paginator = self.get_paginator("list_resource_record_sets").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListResourceRecordSetsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListResourceRecordSetsResponse.from_boto(response)

    def list_reusable_delegation_sets(
        self,
        _request: shapes.ListReusableDelegationSetsRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListReusableDelegationSetsResponse:
        """
        Retrieves a list of the reusable delegation sets that are associated with the
        current AWS account.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListReusableDelegationSetsRequest(**_params)
        response = self._boto_client.list_reusable_delegation_sets(
            **_request.to_boto()
        )

        return shapes.ListReusableDelegationSetsResponse.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_type: typing.Union[str, shapes.TagResourceType],
        resource_id: str,
    ) -> shapes.ListTagsForResourceResponse:
        """
        Lists tags for one health check or hosted zone.

        For information about using tags for cost allocation, see [Using Cost Allocation
        Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-
        tags.html) in the _AWS Billing and Cost Management User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResponse.from_boto(response)

    def list_tags_for_resources(
        self,
        _request: shapes.ListTagsForResourcesRequest = None,
        *,
        resource_type: typing.Union[str, shapes.TagResourceType],
        resource_ids: typing.List[str],
    ) -> shapes.ListTagsForResourcesResponse:
        """
        Lists tags for up to 10 health checks or hosted zones.

        For information about using tags for cost allocation, see [Using Cost Allocation
        Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-
        tags.html) in the _AWS Billing and Cost Management User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_ids is not ShapeBase.NOT_SET:
                _params['resource_ids'] = resource_ids
            _request = shapes.ListTagsForResourcesRequest(**_params)
        response = self._boto_client.list_tags_for_resources(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourcesResponse.from_boto(response)

    def list_traffic_policies(
        self,
        _request: shapes.ListTrafficPoliciesRequest = None,
        *,
        traffic_policy_id_marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTrafficPoliciesResponse:
        """
        Gets information about the latest version for every traffic policy that is
        associated with the current AWS account. Policies are listed in the order in
        which they were created.
        """
        if _request is None:
            _params = {}
            if traffic_policy_id_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_id_marker'] = traffic_policy_id_marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListTrafficPoliciesRequest(**_params)
        response = self._boto_client.list_traffic_policies(**_request.to_boto())

        return shapes.ListTrafficPoliciesResponse.from_boto(response)

    def list_traffic_policy_instances(
        self,
        _request: shapes.ListTrafficPolicyInstancesRequest = None,
        *,
        hosted_zone_id_marker: str = ShapeBase.NOT_SET,
        traffic_policy_instance_name_marker: str = ShapeBase.NOT_SET,
        traffic_policy_instance_type_marker: typing.
        Union[str, shapes.RRType] = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTrafficPolicyInstancesResponse:
        """
        Gets information about the traffic policy instances that you created by using
        the current AWS account.

        After you submit an `UpdateTrafficPolicyInstance` request, there's a brief delay
        while Amazon Route 53 creates the resource record sets that are specified in the
        traffic policy definition. For more information, see the `State` response
        element.

        Amazon Route 53 returns a maximum of 100 items in each response. If you have a
        lot of traffic policy instances, you can use the `MaxItems` parameter to list
        them in groups of up to 100.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id_marker is not ShapeBase.NOT_SET:
                _params['hosted_zone_id_marker'] = hosted_zone_id_marker
            if traffic_policy_instance_name_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_instance_name_marker'
                       ] = traffic_policy_instance_name_marker
            if traffic_policy_instance_type_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_instance_type_marker'
                       ] = traffic_policy_instance_type_marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListTrafficPolicyInstancesRequest(**_params)
        response = self._boto_client.list_traffic_policy_instances(
            **_request.to_boto()
        )

        return shapes.ListTrafficPolicyInstancesResponse.from_boto(response)

    def list_traffic_policy_instances_by_hosted_zone(
        self,
        _request: shapes.ListTrafficPolicyInstancesByHostedZoneRequest = None,
        *,
        hosted_zone_id: str,
        traffic_policy_instance_name_marker: str = ShapeBase.NOT_SET,
        traffic_policy_instance_type_marker: typing.
        Union[str, shapes.RRType] = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTrafficPolicyInstancesByHostedZoneResponse:
        """
        Gets information about the traffic policy instances that you created in a
        specified hosted zone.

        After you submit a `CreateTrafficPolicyInstance` or an
        `UpdateTrafficPolicyInstance` request, there's a brief delay while Amazon Route
        53 creates the resource record sets that are specified in the traffic policy
        definition. For more information, see the `State` response element.

        Amazon Route 53 returns a maximum of 100 items in each response. If you have a
        lot of traffic policy instances, you can use the `MaxItems` parameter to list
        them in groups of up to 100.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if traffic_policy_instance_name_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_instance_name_marker'
                       ] = traffic_policy_instance_name_marker
            if traffic_policy_instance_type_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_instance_type_marker'
                       ] = traffic_policy_instance_type_marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListTrafficPolicyInstancesByHostedZoneRequest(
                **_params
            )
        response = self._boto_client.list_traffic_policy_instances_by_hosted_zone(
            **_request.to_boto()
        )

        return shapes.ListTrafficPolicyInstancesByHostedZoneResponse.from_boto(
            response
        )

    def list_traffic_policy_instances_by_policy(
        self,
        _request: shapes.ListTrafficPolicyInstancesByPolicyRequest = None,
        *,
        traffic_policy_id: str,
        traffic_policy_version: int,
        hosted_zone_id_marker: str = ShapeBase.NOT_SET,
        traffic_policy_instance_name_marker: str = ShapeBase.NOT_SET,
        traffic_policy_instance_type_marker: typing.
        Union[str, shapes.RRType] = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTrafficPolicyInstancesByPolicyResponse:
        """
        Gets information about the traffic policy instances that you created by using a
        specify traffic policy version.

        After you submit a `CreateTrafficPolicyInstance` or an
        `UpdateTrafficPolicyInstance` request, there's a brief delay while Amazon Route
        53 creates the resource record sets that are specified in the traffic policy
        definition. For more information, see the `State` response element.

        Amazon Route 53 returns a maximum of 100 items in each response. If you have a
        lot of traffic policy instances, you can use the `MaxItems` parameter to list
        them in groups of up to 100.
        """
        if _request is None:
            _params = {}
            if traffic_policy_id is not ShapeBase.NOT_SET:
                _params['traffic_policy_id'] = traffic_policy_id
            if traffic_policy_version is not ShapeBase.NOT_SET:
                _params['traffic_policy_version'] = traffic_policy_version
            if hosted_zone_id_marker is not ShapeBase.NOT_SET:
                _params['hosted_zone_id_marker'] = hosted_zone_id_marker
            if traffic_policy_instance_name_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_instance_name_marker'
                       ] = traffic_policy_instance_name_marker
            if traffic_policy_instance_type_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_instance_type_marker'
                       ] = traffic_policy_instance_type_marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListTrafficPolicyInstancesByPolicyRequest(
                **_params
            )
        response = self._boto_client.list_traffic_policy_instances_by_policy(
            **_request.to_boto()
        )

        return shapes.ListTrafficPolicyInstancesByPolicyResponse.from_boto(
            response
        )

    def list_traffic_policy_versions(
        self,
        _request: shapes.ListTrafficPolicyVersionsRequest = None,
        *,
        id: str,
        traffic_policy_version_marker: str = ShapeBase.NOT_SET,
        max_items: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTrafficPolicyVersionsResponse:
        """
        Gets information about all of the versions for a specified traffic policy.

        Traffic policy versions are listed in numerical order by `VersionNumber`.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if traffic_policy_version_marker is not ShapeBase.NOT_SET:
                _params['traffic_policy_version_marker'
                       ] = traffic_policy_version_marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListTrafficPolicyVersionsRequest(**_params)
        response = self._boto_client.list_traffic_policy_versions(
            **_request.to_boto()
        )

        return shapes.ListTrafficPolicyVersionsResponse.from_boto(response)

    def list_vpc_association_authorizations(
        self,
        _request: shapes.ListVPCAssociationAuthorizationsRequest = None,
        *,
        hosted_zone_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: str = ShapeBase.NOT_SET,
    ) -> shapes.ListVPCAssociationAuthorizationsResponse:
        """
        Gets a list of the VPCs that were created by other accounts and that can be
        associated with a specified hosted zone because you've submitted one or more
        `CreateVPCAssociationAuthorization` requests.

        The response includes a `VPCs` element with a `VPC` child element for each VPC
        that can be associated with the hosted zone.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListVPCAssociationAuthorizationsRequest(**_params)
        response = self._boto_client.list_vpc_association_authorizations(
            **_request.to_boto()
        )

        return shapes.ListVPCAssociationAuthorizationsResponse.from_boto(
            response
        )

    def test_dns_answer(
        self,
        _request: shapes.TestDNSAnswerRequest = None,
        *,
        hosted_zone_id: str,
        record_name: str,
        record_type: typing.Union[str, shapes.RRType],
        resolver_ip: str = ShapeBase.NOT_SET,
        edns0_client_subnet_ip: str = ShapeBase.NOT_SET,
        edns0_client_subnet_mask: str = ShapeBase.NOT_SET,
    ) -> shapes.TestDNSAnswerResponse:
        """
        Gets the value that Amazon Route 53 returns in response to a DNS request for a
        specified record name and type. You can optionally specify the IP address of a
        DNS resolver, an EDNS0 client subnet IP address, and a subnet mask.
        """
        if _request is None:
            _params = {}
            if hosted_zone_id is not ShapeBase.NOT_SET:
                _params['hosted_zone_id'] = hosted_zone_id
            if record_name is not ShapeBase.NOT_SET:
                _params['record_name'] = record_name
            if record_type is not ShapeBase.NOT_SET:
                _params['record_type'] = record_type
            if resolver_ip is not ShapeBase.NOT_SET:
                _params['resolver_ip'] = resolver_ip
            if edns0_client_subnet_ip is not ShapeBase.NOT_SET:
                _params['edns0_client_subnet_ip'] = edns0_client_subnet_ip
            if edns0_client_subnet_mask is not ShapeBase.NOT_SET:
                _params['edns0_client_subnet_mask'] = edns0_client_subnet_mask
            _request = shapes.TestDNSAnswerRequest(**_params)
        response = self._boto_client.test_dns_answer(**_request.to_boto())

        return shapes.TestDNSAnswerResponse.from_boto(response)

    def update_health_check(
        self,
        _request: shapes.UpdateHealthCheckRequest = None,
        *,
        health_check_id: str,
        health_check_version: int = ShapeBase.NOT_SET,
        ip_address: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        resource_path: str = ShapeBase.NOT_SET,
        fully_qualified_domain_name: str = ShapeBase.NOT_SET,
        search_string: str = ShapeBase.NOT_SET,
        failure_threshold: int = ShapeBase.NOT_SET,
        inverted: bool = ShapeBase.NOT_SET,
        health_threshold: int = ShapeBase.NOT_SET,
        child_health_checks: typing.List[str] = ShapeBase.NOT_SET,
        enable_sni: bool = ShapeBase.NOT_SET,
        regions: typing.List[typing.Union[str, shapes.HealthCheckRegion]
                            ] = ShapeBase.NOT_SET,
        alarm_identifier: shapes.AlarmIdentifier = ShapeBase.NOT_SET,
        insufficient_data_health_status: typing.
        Union[str, shapes.InsufficientDataHealthStatus] = ShapeBase.NOT_SET,
        reset_elements: typing.List[typing.Union[str, shapes.
                                                 ResettableElementName]
                                   ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateHealthCheckResponse:
        """
        Updates an existing health check. Note that some values can't be updated.

        For more information about updating health checks, see [Creating, Updating, and
        Deleting Health
        Checks](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-
        creating-deleting.html) in the _Amazon Route 53 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if health_check_id is not ShapeBase.NOT_SET:
                _params['health_check_id'] = health_check_id
            if health_check_version is not ShapeBase.NOT_SET:
                _params['health_check_version'] = health_check_version
            if ip_address is not ShapeBase.NOT_SET:
                _params['ip_address'] = ip_address
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if resource_path is not ShapeBase.NOT_SET:
                _params['resource_path'] = resource_path
            if fully_qualified_domain_name is not ShapeBase.NOT_SET:
                _params['fully_qualified_domain_name'
                       ] = fully_qualified_domain_name
            if search_string is not ShapeBase.NOT_SET:
                _params['search_string'] = search_string
            if failure_threshold is not ShapeBase.NOT_SET:
                _params['failure_threshold'] = failure_threshold
            if inverted is not ShapeBase.NOT_SET:
                _params['inverted'] = inverted
            if health_threshold is not ShapeBase.NOT_SET:
                _params['health_threshold'] = health_threshold
            if child_health_checks is not ShapeBase.NOT_SET:
                _params['child_health_checks'] = child_health_checks
            if enable_sni is not ShapeBase.NOT_SET:
                _params['enable_sni'] = enable_sni
            if regions is not ShapeBase.NOT_SET:
                _params['regions'] = regions
            if alarm_identifier is not ShapeBase.NOT_SET:
                _params['alarm_identifier'] = alarm_identifier
            if insufficient_data_health_status is not ShapeBase.NOT_SET:
                _params['insufficient_data_health_status'
                       ] = insufficient_data_health_status
            if reset_elements is not ShapeBase.NOT_SET:
                _params['reset_elements'] = reset_elements
            _request = shapes.UpdateHealthCheckRequest(**_params)
        response = self._boto_client.update_health_check(**_request.to_boto())

        return shapes.UpdateHealthCheckResponse.from_boto(response)

    def update_hosted_zone_comment(
        self,
        _request: shapes.UpdateHostedZoneCommentRequest = None,
        *,
        id: str,
        comment: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateHostedZoneCommentResponse:
        """
        Updates the comment for a specified hosted zone.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.UpdateHostedZoneCommentRequest(**_params)
        response = self._boto_client.update_hosted_zone_comment(
            **_request.to_boto()
        )

        return shapes.UpdateHostedZoneCommentResponse.from_boto(response)

    def update_traffic_policy_comment(
        self,
        _request: shapes.UpdateTrafficPolicyCommentRequest = None,
        *,
        id: str,
        version: int,
        comment: str,
    ) -> shapes.UpdateTrafficPolicyCommentResponse:
        """
        Updates the comment for a specified traffic policy version.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.UpdateTrafficPolicyCommentRequest(**_params)
        response = self._boto_client.update_traffic_policy_comment(
            **_request.to_boto()
        )

        return shapes.UpdateTrafficPolicyCommentResponse.from_boto(response)

    def update_traffic_policy_instance(
        self,
        _request: shapes.UpdateTrafficPolicyInstanceRequest = None,
        *,
        id: str,
        ttl: int,
        traffic_policy_id: str,
        traffic_policy_version: int,
    ) -> shapes.UpdateTrafficPolicyInstanceResponse:
        """
        Updates the resource record sets in a specified hosted zone that were created
        based on the settings in a specified traffic policy version.

        When you update a traffic policy instance, Amazon Route 53 continues to respond
        to DNS queries for the root resource record set name (such as example.com) while
        it replaces one group of resource record sets with another. Amazon Route 53
        performs the following operations:

          1. Amazon Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets. 

          2. When all of the new resource record sets have been created, Amazon Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets.

          3. Amazon Route 53 deletes the old group of resource record sets that are associated with the root resource record set name.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            if ttl is not ShapeBase.NOT_SET:
                _params['ttl'] = ttl
            if traffic_policy_id is not ShapeBase.NOT_SET:
                _params['traffic_policy_id'] = traffic_policy_id
            if traffic_policy_version is not ShapeBase.NOT_SET:
                _params['traffic_policy_version'] = traffic_policy_version
            _request = shapes.UpdateTrafficPolicyInstanceRequest(**_params)
        response = self._boto_client.update_traffic_policy_instance(
            **_request.to_boto()
        )

        return shapes.UpdateTrafficPolicyInstanceResponse.from_boto(response)
