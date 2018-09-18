import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("waf-regional", *args, **kwargs)

    def associate_web_acl(
        self,
        _request: shapes.AssociateWebACLRequest = None,
        *,
        web_acl_id: str,
        resource_arn: str,
    ) -> shapes.AssociateWebACLResponse:
        """
        Associates a web ACL with a resource.
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.AssociateWebACLRequest(**_params)
        response = self._boto_client.associate_web_acl(**_request.to_boto())

        return shapes.AssociateWebACLResponse.from_boto(response)

    def create_byte_match_set(
        self,
        _request: shapes.CreateByteMatchSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateByteMatchSetResponse:
        """
        Creates a `ByteMatchSet`. You then use UpdateByteMatchSet to identify the part
        of a web request that you want AWS WAF to inspect, such as the values of the
        `User-Agent` header or the query string. For example, you can create a
        `ByteMatchSet` that matches any requests with `User-Agent` headers that contain
        the string `BadBot`. You can then configure AWS WAF to reject those requests.

        To create and configure a `ByteMatchSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateByteMatchSet` request.

          2. Submit a `CreateByteMatchSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateByteMatchSet` request.

          4. Submit an UpdateByteMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateByteMatchSetRequest(**_params)
        response = self._boto_client.create_byte_match_set(**_request.to_boto())

        return shapes.CreateByteMatchSetResponse.from_boto(response)

    def create_geo_match_set(
        self,
        _request: shapes.CreateGeoMatchSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateGeoMatchSetResponse:
        """
        Creates an GeoMatchSet, which you use to specify which web requests you want to
        allow or block based on the country that the requests originate from. For
        example, if you're receiving a lot of requests from one or more countries and
        you want to block the requests, you can create an `GeoMatchSet` that contains
        those countries and then configure AWS WAF to block the requests.

        To create and configure a `GeoMatchSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateGeoMatchSet` request.

          2. Submit a `CreateGeoMatchSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateGeoMatchSet request.

          4. Submit an `UpdateGeoMatchSetSet` request to specify the countries that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateGeoMatchSetRequest(**_params)
        response = self._boto_client.create_geo_match_set(**_request.to_boto())

        return shapes.CreateGeoMatchSetResponse.from_boto(response)

    def create_ip_set(
        self,
        _request: shapes.CreateIPSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateIPSetResponse:
        """
        Creates an IPSet, which you use to specify which web requests you want to allow
        or block based on the IP addresses that the requests originate from. For
        example, if you're receiving a lot of requests from one or more individual IP
        addresses or one or more ranges of IP addresses and you want to block the
        requests, you can create an `IPSet` that contains those IP addresses and then
        configure AWS WAF to block the requests.

        To create and configure an `IPSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateIPSet` request.

          2. Submit a `CreateIPSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateIPSet request.

          4. Submit an `UpdateIPSet` request to specify the IP addresses that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateIPSetRequest(**_params)
        response = self._boto_client.create_ip_set(**_request.to_boto())

        return shapes.CreateIPSetResponse.from_boto(response)

    def create_rate_based_rule(
        self,
        _request: shapes.CreateRateBasedRuleRequest = None,
        *,
        name: str,
        metric_name: str,
        rate_key: typing.Union[str, shapes.RateKey],
        rate_limit: int,
        change_token: str,
    ) -> shapes.CreateRateBasedRuleResponse:
        """
        Creates a RateBasedRule. The `RateBasedRule` contains a `RateLimit`, which
        specifies the maximum number of requests that AWS WAF allows from a specified IP
        address in a five-minute period. The `RateBasedRule` also contains the `IPSet`
        objects, `ByteMatchSet` objects, and other predicates that identify the requests
        that you want to count or block if these requests exceed the `RateLimit`.

        If you add more than one predicate to a `RateBasedRule`, a request not only must
        exceed the `RateLimit`, but it also must match all the specifications to be
        counted or blocked. For example, suppose you add the following to a
        `RateBasedRule`:

          * An `IPSet` that matches the IP address `192.0.2.44/32`

          * A `ByteMatchSet` that matches `BadBot` in the `User-Agent` header

        Further, you specify a `RateLimit` of 15,000.

        You then add the `RateBasedRule` to a `WebACL` and specify that you want to
        block requests that meet the conditions in the rule. For a request to be
        blocked, it must come from the IP address 192.0.2.44 _and_ the `User-Agent`
        header in the request must contain the value `BadBot`. Further, requests that
        match these two conditions must be received at a rate of more than 15,000
        requests every five minutes. If both conditions are met and the rate is
        exceeded, AWS WAF blocks the requests. If the rate drops below 15,000 for a
        five-minute period, AWS WAF no longer blocks the requests.

        As a second example, suppose you want to limit requests to a particular page on
        your site. To do this, you could add the following to a `RateBasedRule`:

          * A `ByteMatchSet` with `FieldToMatch` of `URI`

          * A `PositionalConstraint` of `STARTS_WITH`

          * A `TargetString` of `login`

        Further, you specify a `RateLimit` of 15,000.

        By adding this `RateBasedRule` to a `WebACL`, you could limit requests to your
        login page without affecting the rest of your site.

        To create and configure a `RateBasedRule`, perform the following steps:

          1. Create and update the predicates that you want to include in the rule. For more information, see CreateByteMatchSet, CreateIPSet, and CreateSqlInjectionMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRule` request.

          3. Submit a `CreateRateBasedRule` request.

          4. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateRule request.

          5. Submit an `UpdateRateBasedRule` request to specify the predicates that you want to include in the rule.

          6. Create and update a `WebACL` that contains the `RateBasedRule`. For more information, see CreateWebACL.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if rate_key is not ShapeBase.NOT_SET:
                _params['rate_key'] = rate_key
            if rate_limit is not ShapeBase.NOT_SET:
                _params['rate_limit'] = rate_limit
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateRateBasedRuleRequest(**_params)
        response = self._boto_client.create_rate_based_rule(
            **_request.to_boto()
        )

        return shapes.CreateRateBasedRuleResponse.from_boto(response)

    def create_regex_match_set(
        self,
        _request: shapes.CreateRegexMatchSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateRegexMatchSetResponse:
        """
        Creates a RegexMatchSet. You then use UpdateRegexMatchSet to identify the part
        of a web request that you want AWS WAF to inspect, such as the values of the
        `User-Agent` header or the query string. For example, you can create a
        `RegexMatchSet` that contains a `RegexMatchTuple` that looks for any requests
        with `User-Agent` headers that match a `RegexPatternSet` with pattern
        `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

        To create and configure a `RegexMatchSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRegexMatchSet` request.

          2. Submit a `CreateRegexMatchSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexMatchSet` request.

          4. Submit an UpdateRegexMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value, using a `RegexPatternSet`, that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateRegexMatchSetRequest(**_params)
        response = self._boto_client.create_regex_match_set(
            **_request.to_boto()
        )

        return shapes.CreateRegexMatchSetResponse.from_boto(response)

    def create_regex_pattern_set(
        self,
        _request: shapes.CreateRegexPatternSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateRegexPatternSetResponse:
        """
        Creates a `RegexPatternSet`. You then use UpdateRegexPatternSet to specify the
        regular expression (regex) pattern that you want AWS WAF to search for, such as
        `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

        To create and configure a `RegexPatternSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRegexPatternSet` request.

          2. Submit a `CreateRegexPatternSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexPatternSet` request.

          4. Submit an UpdateRegexPatternSet request to specify the string that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateRegexPatternSetRequest(**_params)
        response = self._boto_client.create_regex_pattern_set(
            **_request.to_boto()
        )

        return shapes.CreateRegexPatternSetResponse.from_boto(response)

    def create_rule(
        self,
        _request: shapes.CreateRuleRequest = None,
        *,
        name: str,
        metric_name: str,
        change_token: str,
    ) -> shapes.CreateRuleResponse:
        """
        Creates a `Rule`, which contains the `IPSet` objects, `ByteMatchSet` objects,
        and other predicates that identify the requests that you want to block. If you
        add more than one predicate to a `Rule`, a request must match all of the
        specifications to be allowed or blocked. For example, suppose you add the
        following to a `Rule`:

          * An `IPSet` that matches the IP address `192.0.2.44/32`

          * A `ByteMatchSet` that matches `BadBot` in the `User-Agent` header

        You then add the `Rule` to a `WebACL` and specify that you want to blocks
        requests that satisfy the `Rule`. For a request to be blocked, it must come from
        the IP address 192.0.2.44 _and_ the `User-Agent` header in the request must
        contain the value `BadBot`.

        To create and configure a `Rule`, perform the following steps:

          1. Create and update the predicates that you want to include in the `Rule`. For more information, see CreateByteMatchSet, CreateIPSet, and CreateSqlInjectionMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRule` request.

          3. Submit a `CreateRule` request.

          4. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateRule request.

          5. Submit an `UpdateRule` request to specify the predicates that you want to include in the `Rule`.

          6. Create and update a `WebACL` that contains the `Rule`. For more information, see CreateWebACL.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateRuleRequest(**_params)
        response = self._boto_client.create_rule(**_request.to_boto())

        return shapes.CreateRuleResponse.from_boto(response)

    def create_rule_group(
        self,
        _request: shapes.CreateRuleGroupRequest = None,
        *,
        name: str,
        metric_name: str,
        change_token: str,
    ) -> shapes.CreateRuleGroupResponse:
        """
        Creates a `RuleGroup`. A rule group is a collection of predefined rules that you
        add to a web ACL. You use UpdateRuleGroup to add rules to the rule group.

        Rule groups are subject to the following limits:

          * Three rule groups per account. You can request an increase to this limit by contacting customer support.

          * One rule group per web ACL.

          * Ten rules per rule group.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateRuleGroupRequest(**_params)
        response = self._boto_client.create_rule_group(**_request.to_boto())

        return shapes.CreateRuleGroupResponse.from_boto(response)

    def create_size_constraint_set(
        self,
        _request: shapes.CreateSizeConstraintSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateSizeConstraintSetResponse:
        """
        Creates a `SizeConstraintSet`. You then use UpdateSizeConstraintSet to identify
        the part of a web request that you want AWS WAF to check for length, such as the
        length of the `User-Agent` header or the length of the query string. For
        example, you can create a `SizeConstraintSet` that matches any requests that
        have a query string that is longer than 100 bytes. You can then configure AWS
        WAF to reject those requests.

        To create and configure a `SizeConstraintSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateSizeConstraintSet` request.

          2. Submit a `CreateSizeConstraintSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateSizeConstraintSet` request.

          4. Submit an UpdateSizeConstraintSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateSizeConstraintSetRequest(**_params)
        response = self._boto_client.create_size_constraint_set(
            **_request.to_boto()
        )

        return shapes.CreateSizeConstraintSetResponse.from_boto(response)

    def create_sql_injection_match_set(
        self,
        _request: shapes.CreateSqlInjectionMatchSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateSqlInjectionMatchSetResponse:
        """
        Creates a SqlInjectionMatchSet, which you use to allow, block, or count requests
        that contain snippets of SQL code in a specified part of web requests. AWS WAF
        searches for character sequences that are likely to be malicious strings.

        To create and configure a `SqlInjectionMatchSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateSqlInjectionMatchSet` request.

          2. Submit a `CreateSqlInjectionMatchSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateSqlInjectionMatchSet request.

          4. Submit an UpdateSqlInjectionMatchSet request to specify the parts of web requests in which you want to allow, block, or count malicious SQL code.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateSqlInjectionMatchSetRequest(**_params)
        response = self._boto_client.create_sql_injection_match_set(
            **_request.to_boto()
        )

        return shapes.CreateSqlInjectionMatchSetResponse.from_boto(response)

    def create_web_acl(
        self,
        _request: shapes.CreateWebACLRequest = None,
        *,
        name: str,
        metric_name: str,
        default_action: shapes.WafAction,
        change_token: str,
    ) -> shapes.CreateWebACLResponse:
        """
        Creates a `WebACL`, which contains the `Rules` that identify the CloudFront web
        requests that you want to allow, block, or count. AWS WAF evaluates `Rules` in
        order based on the value of `Priority` for each `Rule`.

        You also specify a default action, either `ALLOW` or `BLOCK`. If a web request
        doesn't match any of the `Rules` in a `WebACL`, AWS WAF responds to the request
        with the default action.

        To create and configure a `WebACL`, perform the following steps:

          1. Create and update the `ByteMatchSet` objects and other predicates that you want to include in `Rules`. For more information, see CreateByteMatchSet, UpdateByteMatchSet, CreateIPSet, UpdateIPSet, CreateSqlInjectionMatchSet, and UpdateSqlInjectionMatchSet.

          2. Create and update the `Rules` that you want to include in the `WebACL`. For more information, see CreateRule and UpdateRule.

          3. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateWebACL` request.

          4. Submit a `CreateWebACL` request.

          5. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateWebACL request.

          6. Submit an UpdateWebACL request to specify the `Rules` that you want to include in the `WebACL`, to specify the default action, and to associate the `WebACL` with a CloudFront distribution.

        For more information about how to use the AWS WAF API, see the [AWS WAF
        Developer Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if default_action is not ShapeBase.NOT_SET:
                _params['default_action'] = default_action
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateWebACLRequest(**_params)
        response = self._boto_client.create_web_acl(**_request.to_boto())

        return shapes.CreateWebACLResponse.from_boto(response)

    def create_xss_match_set(
        self,
        _request: shapes.CreateXssMatchSetRequest = None,
        *,
        name: str,
        change_token: str,
    ) -> shapes.CreateXssMatchSetResponse:
        """
        Creates an XssMatchSet, which you use to allow, block, or count requests that
        contain cross-site scripting attacks in the specified part of web requests. AWS
        WAF searches for character sequences that are likely to be malicious strings.

        To create and configure an `XssMatchSet`, perform the following steps:

          1. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateXssMatchSet` request.

          2. Submit a `CreateXssMatchSet` request.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateXssMatchSet request.

          4. Submit an UpdateXssMatchSet request to specify the parts of web requests in which you want to allow, block, or count cross-site scripting attacks.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.CreateXssMatchSetRequest(**_params)
        response = self._boto_client.create_xss_match_set(**_request.to_boto())

        return shapes.CreateXssMatchSetResponse.from_boto(response)

    def delete_byte_match_set(
        self,
        _request: shapes.DeleteByteMatchSetRequest = None,
        *,
        byte_match_set_id: str,
        change_token: str,
    ) -> shapes.DeleteByteMatchSetResponse:
        """
        Permanently deletes a ByteMatchSet. You can't delete a `ByteMatchSet` if it's
        still used in any `Rules` or if it still includes any ByteMatchTuple objects
        (any filters).

        If you just want to remove a `ByteMatchSet` from a `Rule`, use UpdateRule.

        To permanently delete a `ByteMatchSet`, perform the following steps:

          1. Update the `ByteMatchSet` to remove filters, if any. For more information, see UpdateByteMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteByteMatchSet` request.

          3. Submit a `DeleteByteMatchSet` request.
        """
        if _request is None:
            _params = {}
            if byte_match_set_id is not ShapeBase.NOT_SET:
                _params['byte_match_set_id'] = byte_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteByteMatchSetRequest(**_params)
        response = self._boto_client.delete_byte_match_set(**_request.to_boto())

        return shapes.DeleteByteMatchSetResponse.from_boto(response)

    def delete_geo_match_set(
        self,
        _request: shapes.DeleteGeoMatchSetRequest = None,
        *,
        geo_match_set_id: str,
        change_token: str,
    ) -> shapes.DeleteGeoMatchSetResponse:
        """
        Permanently deletes a GeoMatchSet. You can't delete a `GeoMatchSet` if it's
        still used in any `Rules` or if it still includes any countries.

        If you just want to remove a `GeoMatchSet` from a `Rule`, use UpdateRule.

        To permanently delete a `GeoMatchSet` from AWS WAF, perform the following steps:

          1. Update the `GeoMatchSet` to remove any countries. For more information, see UpdateGeoMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteGeoMatchSet` request.

          3. Submit a `DeleteGeoMatchSet` request.
        """
        if _request is None:
            _params = {}
            if geo_match_set_id is not ShapeBase.NOT_SET:
                _params['geo_match_set_id'] = geo_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteGeoMatchSetRequest(**_params)
        response = self._boto_client.delete_geo_match_set(**_request.to_boto())

        return shapes.DeleteGeoMatchSetResponse.from_boto(response)

    def delete_ip_set(
        self,
        _request: shapes.DeleteIPSetRequest = None,
        *,
        ip_set_id: str,
        change_token: str,
    ) -> shapes.DeleteIPSetResponse:
        """
        Permanently deletes an IPSet. You can't delete an `IPSet` if it's still used in
        any `Rules` or if it still includes any IP addresses.

        If you just want to remove an `IPSet` from a `Rule`, use UpdateRule.

        To permanently delete an `IPSet` from AWS WAF, perform the following steps:

          1. Update the `IPSet` to remove IP address ranges, if any. For more information, see UpdateIPSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteIPSet` request.

          3. Submit a `DeleteIPSet` request.
        """
        if _request is None:
            _params = {}
            if ip_set_id is not ShapeBase.NOT_SET:
                _params['ip_set_id'] = ip_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteIPSetRequest(**_params)
        response = self._boto_client.delete_ip_set(**_request.to_boto())

        return shapes.DeleteIPSetResponse.from_boto(response)

    def delete_logging_configuration(
        self,
        _request: shapes.DeleteLoggingConfigurationRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.DeleteLoggingConfigurationResponse:
        """
        Permanently deletes the LoggingConfiguration from the specified web ACL.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.DeleteLoggingConfigurationRequest(**_params)
        response = self._boto_client.delete_logging_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteLoggingConfigurationResponse.from_boto(response)

    def delete_permission_policy(
        self,
        _request: shapes.DeletePermissionPolicyRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.DeletePermissionPolicyResponse:
        """
        Permanently deletes an IAM policy from the specified RuleGroup.

        The user making the request must be the owner of the RuleGroup.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.DeletePermissionPolicyRequest(**_params)
        response = self._boto_client.delete_permission_policy(
            **_request.to_boto()
        )

        return shapes.DeletePermissionPolicyResponse.from_boto(response)

    def delete_rate_based_rule(
        self,
        _request: shapes.DeleteRateBasedRuleRequest = None,
        *,
        rule_id: str,
        change_token: str,
    ) -> shapes.DeleteRateBasedRuleResponse:
        """
        Permanently deletes a RateBasedRule. You can't delete a rule if it's still used
        in any `WebACL` objects or if it still includes any predicates, such as
        `ByteMatchSet` objects.

        If you just want to remove a rule from a `WebACL`, use UpdateWebACL.

        To permanently delete a `RateBasedRule` from AWS WAF, perform the following
        steps:

          1. Update the `RateBasedRule` to remove predicates, if any. For more information, see UpdateRateBasedRule.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteRateBasedRule` request.

          3. Submit a `DeleteRateBasedRule` request.
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteRateBasedRuleRequest(**_params)
        response = self._boto_client.delete_rate_based_rule(
            **_request.to_boto()
        )

        return shapes.DeleteRateBasedRuleResponse.from_boto(response)

    def delete_regex_match_set(
        self,
        _request: shapes.DeleteRegexMatchSetRequest = None,
        *,
        regex_match_set_id: str,
        change_token: str,
    ) -> shapes.DeleteRegexMatchSetResponse:
        """
        Permanently deletes a RegexMatchSet. You can't delete a `RegexMatchSet` if it's
        still used in any `Rules` or if it still includes any `RegexMatchTuples` objects
        (any filters).

        If you just want to remove a `RegexMatchSet` from a `Rule`, use UpdateRule.

        To permanently delete a `RegexMatchSet`, perform the following steps:

          1. Update the `RegexMatchSet` to remove filters, if any. For more information, see UpdateRegexMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteRegexMatchSet` request.

          3. Submit a `DeleteRegexMatchSet` request.
        """
        if _request is None:
            _params = {}
            if regex_match_set_id is not ShapeBase.NOT_SET:
                _params['regex_match_set_id'] = regex_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteRegexMatchSetRequest(**_params)
        response = self._boto_client.delete_regex_match_set(
            **_request.to_boto()
        )

        return shapes.DeleteRegexMatchSetResponse.from_boto(response)

    def delete_regex_pattern_set(
        self,
        _request: shapes.DeleteRegexPatternSetRequest = None,
        *,
        regex_pattern_set_id: str,
        change_token: str,
    ) -> shapes.DeleteRegexPatternSetResponse:
        """
        Permanently deletes a RegexPatternSet. You can't delete a `RegexPatternSet` if
        it's still used in any `RegexMatchSet` or if the `RegexPatternSet` is not empty.
        """
        if _request is None:
            _params = {}
            if regex_pattern_set_id is not ShapeBase.NOT_SET:
                _params['regex_pattern_set_id'] = regex_pattern_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteRegexPatternSetRequest(**_params)
        response = self._boto_client.delete_regex_pattern_set(
            **_request.to_boto()
        )

        return shapes.DeleteRegexPatternSetResponse.from_boto(response)

    def delete_rule(
        self,
        _request: shapes.DeleteRuleRequest = None,
        *,
        rule_id: str,
        change_token: str,
    ) -> shapes.DeleteRuleResponse:
        """
        Permanently deletes a Rule. You can't delete a `Rule` if it's still used in any
        `WebACL` objects or if it still includes any predicates, such as `ByteMatchSet`
        objects.

        If you just want to remove a `Rule` from a `WebACL`, use UpdateWebACL.

        To permanently delete a `Rule` from AWS WAF, perform the following steps:

          1. Update the `Rule` to remove predicates, if any. For more information, see UpdateRule.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteRule` request.

          3. Submit a `DeleteRule` request.
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteRuleRequest(**_params)
        response = self._boto_client.delete_rule(**_request.to_boto())

        return shapes.DeleteRuleResponse.from_boto(response)

    def delete_rule_group(
        self,
        _request: shapes.DeleteRuleGroupRequest = None,
        *,
        rule_group_id: str,
        change_token: str,
    ) -> shapes.DeleteRuleGroupResponse:
        """
        Permanently deletes a RuleGroup. You can't delete a `RuleGroup` if it's still
        used in any `WebACL` objects or if it still includes any rules.

        If you just want to remove a `RuleGroup` from a `WebACL`, use UpdateWebACL.

        To permanently delete a `RuleGroup` from AWS WAF, perform the following steps:

          1. Update the `RuleGroup` to remove rules, if any. For more information, see UpdateRuleGroup.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteRuleGroup` request.

          3. Submit a `DeleteRuleGroup` request.
        """
        if _request is None:
            _params = {}
            if rule_group_id is not ShapeBase.NOT_SET:
                _params['rule_group_id'] = rule_group_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteRuleGroupRequest(**_params)
        response = self._boto_client.delete_rule_group(**_request.to_boto())

        return shapes.DeleteRuleGroupResponse.from_boto(response)

    def delete_size_constraint_set(
        self,
        _request: shapes.DeleteSizeConstraintSetRequest = None,
        *,
        size_constraint_set_id: str,
        change_token: str,
    ) -> shapes.DeleteSizeConstraintSetResponse:
        """
        Permanently deletes a SizeConstraintSet. You can't delete a `SizeConstraintSet`
        if it's still used in any `Rules` or if it still includes any SizeConstraint
        objects (any filters).

        If you just want to remove a `SizeConstraintSet` from a `Rule`, use UpdateRule.

        To permanently delete a `SizeConstraintSet`, perform the following steps:

          1. Update the `SizeConstraintSet` to remove filters, if any. For more information, see UpdateSizeConstraintSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteSizeConstraintSet` request.

          3. Submit a `DeleteSizeConstraintSet` request.
        """
        if _request is None:
            _params = {}
            if size_constraint_set_id is not ShapeBase.NOT_SET:
                _params['size_constraint_set_id'] = size_constraint_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteSizeConstraintSetRequest(**_params)
        response = self._boto_client.delete_size_constraint_set(
            **_request.to_boto()
        )

        return shapes.DeleteSizeConstraintSetResponse.from_boto(response)

    def delete_sql_injection_match_set(
        self,
        _request: shapes.DeleteSqlInjectionMatchSetRequest = None,
        *,
        sql_injection_match_set_id: str,
        change_token: str,
    ) -> shapes.DeleteSqlInjectionMatchSetResponse:
        """
        Permanently deletes a SqlInjectionMatchSet. You can't delete a
        `SqlInjectionMatchSet` if it's still used in any `Rules` or if it still contains
        any SqlInjectionMatchTuple objects.

        If you just want to remove a `SqlInjectionMatchSet` from a `Rule`, use
        UpdateRule.

        To permanently delete a `SqlInjectionMatchSet` from AWS WAF, perform the
        following steps:

          1. Update the `SqlInjectionMatchSet` to remove filters, if any. For more information, see UpdateSqlInjectionMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteSqlInjectionMatchSet` request.

          3. Submit a `DeleteSqlInjectionMatchSet` request.
        """
        if _request is None:
            _params = {}
            if sql_injection_match_set_id is not ShapeBase.NOT_SET:
                _params['sql_injection_match_set_id'
                       ] = sql_injection_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteSqlInjectionMatchSetRequest(**_params)
        response = self._boto_client.delete_sql_injection_match_set(
            **_request.to_boto()
        )

        return shapes.DeleteSqlInjectionMatchSetResponse.from_boto(response)

    def delete_web_acl(
        self,
        _request: shapes.DeleteWebACLRequest = None,
        *,
        web_acl_id: str,
        change_token: str,
    ) -> shapes.DeleteWebACLResponse:
        """
        Permanently deletes a WebACL. You can't delete a `WebACL` if it still contains
        any `Rules`.

        To delete a `WebACL`, perform the following steps:

          1. Update the `WebACL` to remove `Rules`, if any. For more information, see UpdateWebACL.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteWebACL` request.

          3. Submit a `DeleteWebACL` request.
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteWebACLRequest(**_params)
        response = self._boto_client.delete_web_acl(**_request.to_boto())

        return shapes.DeleteWebACLResponse.from_boto(response)

    def delete_xss_match_set(
        self,
        _request: shapes.DeleteXssMatchSetRequest = None,
        *,
        xss_match_set_id: str,
        change_token: str,
    ) -> shapes.DeleteXssMatchSetResponse:
        """
        Permanently deletes an XssMatchSet. You can't delete an `XssMatchSet` if it's
        still used in any `Rules` or if it still contains any XssMatchTuple objects.

        If you just want to remove an `XssMatchSet` from a `Rule`, use UpdateRule.

        To permanently delete an `XssMatchSet` from AWS WAF, perform the following
        steps:

          1. Update the `XssMatchSet` to remove filters, if any. For more information, see UpdateXssMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `DeleteXssMatchSet` request.

          3. Submit a `DeleteXssMatchSet` request.
        """
        if _request is None:
            _params = {}
            if xss_match_set_id is not ShapeBase.NOT_SET:
                _params['xss_match_set_id'] = xss_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.DeleteXssMatchSetRequest(**_params)
        response = self._boto_client.delete_xss_match_set(**_request.to_boto())

        return shapes.DeleteXssMatchSetResponse.from_boto(response)

    def disassociate_web_acl(
        self,
        _request: shapes.DisassociateWebACLRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.DisassociateWebACLResponse:
        """
        Removes a web ACL from the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.DisassociateWebACLRequest(**_params)
        response = self._boto_client.disassociate_web_acl(**_request.to_boto())

        return shapes.DisassociateWebACLResponse.from_boto(response)

    def get_byte_match_set(
        self,
        _request: shapes.GetByteMatchSetRequest = None,
        *,
        byte_match_set_id: str,
    ) -> shapes.GetByteMatchSetResponse:
        """
        Returns the ByteMatchSet specified by `ByteMatchSetId`.
        """
        if _request is None:
            _params = {}
            if byte_match_set_id is not ShapeBase.NOT_SET:
                _params['byte_match_set_id'] = byte_match_set_id
            _request = shapes.GetByteMatchSetRequest(**_params)
        response = self._boto_client.get_byte_match_set(**_request.to_boto())

        return shapes.GetByteMatchSetResponse.from_boto(response)

    def get_change_token(
        self,
        _request: shapes.GetChangeTokenRequest = None,
    ) -> shapes.GetChangeTokenResponse:
        """
        When you want to create, update, or delete AWS WAF objects, get a change token
        and include the change token in the create, update, or delete request. Change
        tokens ensure that your application doesn't submit conflicting requests to AWS
        WAF.

        Each create, update, or delete request must use a unique change token. If your
        application submits a `GetChangeToken` request and then submits a second
        `GetChangeToken` request before submitting a create, update, or delete request,
        the second `GetChangeToken` request returns the same value as the first
        `GetChangeToken` request.

        When you use a change token in a create, update, or delete request, the status
        of the change token changes to `PENDING`, which indicates that AWS WAF is
        propagating the change to all AWS WAF servers. Use `GetChangeTokenStatus` to
        determine the status of your change token.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetChangeTokenRequest(**_params)
        response = self._boto_client.get_change_token(**_request.to_boto())

        return shapes.GetChangeTokenResponse.from_boto(response)

    def get_change_token_status(
        self,
        _request: shapes.GetChangeTokenStatusRequest = None,
        *,
        change_token: str,
    ) -> shapes.GetChangeTokenStatusResponse:
        """
        Returns the status of a `ChangeToken` that you got by calling GetChangeToken.
        `ChangeTokenStatus` is one of the following values:

          * `PROVISIONED`: You requested the change token by calling `GetChangeToken`, but you haven't used it yet in a call to create, update, or delete an AWS WAF object.

          * `PENDING`: AWS WAF is propagating the create, update, or delete request to all AWS WAF servers.

          * `IN_SYNC`: Propagation is complete.
        """
        if _request is None:
            _params = {}
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.GetChangeTokenStatusRequest(**_params)
        response = self._boto_client.get_change_token_status(
            **_request.to_boto()
        )

        return shapes.GetChangeTokenStatusResponse.from_boto(response)

    def get_geo_match_set(
        self,
        _request: shapes.GetGeoMatchSetRequest = None,
        *,
        geo_match_set_id: str,
    ) -> shapes.GetGeoMatchSetResponse:
        """
        Returns the GeoMatchSet that is specified by `GeoMatchSetId`.
        """
        if _request is None:
            _params = {}
            if geo_match_set_id is not ShapeBase.NOT_SET:
                _params['geo_match_set_id'] = geo_match_set_id
            _request = shapes.GetGeoMatchSetRequest(**_params)
        response = self._boto_client.get_geo_match_set(**_request.to_boto())

        return shapes.GetGeoMatchSetResponse.from_boto(response)

    def get_ip_set(
        self,
        _request: shapes.GetIPSetRequest = None,
        *,
        ip_set_id: str,
    ) -> shapes.GetIPSetResponse:
        """
        Returns the IPSet that is specified by `IPSetId`.
        """
        if _request is None:
            _params = {}
            if ip_set_id is not ShapeBase.NOT_SET:
                _params['ip_set_id'] = ip_set_id
            _request = shapes.GetIPSetRequest(**_params)
        response = self._boto_client.get_ip_set(**_request.to_boto())

        return shapes.GetIPSetResponse.from_boto(response)

    def get_logging_configuration(
        self,
        _request: shapes.GetLoggingConfigurationRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.GetLoggingConfigurationResponse:
        """
        Returns the LoggingConfiguration for the specified web ACL.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.GetLoggingConfigurationRequest(**_params)
        response = self._boto_client.get_logging_configuration(
            **_request.to_boto()
        )

        return shapes.GetLoggingConfigurationResponse.from_boto(response)

    def get_permission_policy(
        self,
        _request: shapes.GetPermissionPolicyRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.GetPermissionPolicyResponse:
        """
        Returns the IAM policy attached to the RuleGroup.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.GetPermissionPolicyRequest(**_params)
        response = self._boto_client.get_permission_policy(**_request.to_boto())

        return shapes.GetPermissionPolicyResponse.from_boto(response)

    def get_rate_based_rule(
        self,
        _request: shapes.GetRateBasedRuleRequest = None,
        *,
        rule_id: str,
    ) -> shapes.GetRateBasedRuleResponse:
        """
        Returns the RateBasedRule that is specified by the `RuleId` that you included in
        the `GetRateBasedRule` request.
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            _request = shapes.GetRateBasedRuleRequest(**_params)
        response = self._boto_client.get_rate_based_rule(**_request.to_boto())

        return shapes.GetRateBasedRuleResponse.from_boto(response)

    def get_rate_based_rule_managed_keys(
        self,
        _request: shapes.GetRateBasedRuleManagedKeysRequest = None,
        *,
        rule_id: str,
        next_marker: str = ShapeBase.NOT_SET,
    ) -> shapes.GetRateBasedRuleManagedKeysResponse:
        """
        Returns an array of IP addresses currently being blocked by the RateBasedRule
        that is specified by the `RuleId`. The maximum number of managed keys that will
        be blocked is 10,000. If more than 10,000 addresses exceed the rate limit, the
        10,000 addresses with the highest rates will be blocked.
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            _request = shapes.GetRateBasedRuleManagedKeysRequest(**_params)
        response = self._boto_client.get_rate_based_rule_managed_keys(
            **_request.to_boto()
        )

        return shapes.GetRateBasedRuleManagedKeysResponse.from_boto(response)

    def get_regex_match_set(
        self,
        _request: shapes.GetRegexMatchSetRequest = None,
        *,
        regex_match_set_id: str,
    ) -> shapes.GetRegexMatchSetResponse:
        """
        Returns the RegexMatchSet specified by `RegexMatchSetId`.
        """
        if _request is None:
            _params = {}
            if regex_match_set_id is not ShapeBase.NOT_SET:
                _params['regex_match_set_id'] = regex_match_set_id
            _request = shapes.GetRegexMatchSetRequest(**_params)
        response = self._boto_client.get_regex_match_set(**_request.to_boto())

        return shapes.GetRegexMatchSetResponse.from_boto(response)

    def get_regex_pattern_set(
        self,
        _request: shapes.GetRegexPatternSetRequest = None,
        *,
        regex_pattern_set_id: str,
    ) -> shapes.GetRegexPatternSetResponse:
        """
        Returns the RegexPatternSet specified by `RegexPatternSetId`.
        """
        if _request is None:
            _params = {}
            if regex_pattern_set_id is not ShapeBase.NOT_SET:
                _params['regex_pattern_set_id'] = regex_pattern_set_id
            _request = shapes.GetRegexPatternSetRequest(**_params)
        response = self._boto_client.get_regex_pattern_set(**_request.to_boto())

        return shapes.GetRegexPatternSetResponse.from_boto(response)

    def get_rule(
        self,
        _request: shapes.GetRuleRequest = None,
        *,
        rule_id: str,
    ) -> shapes.GetRuleResponse:
        """
        Returns the Rule that is specified by the `RuleId` that you included in the
        `GetRule` request.
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            _request = shapes.GetRuleRequest(**_params)
        response = self._boto_client.get_rule(**_request.to_boto())

        return shapes.GetRuleResponse.from_boto(response)

    def get_rule_group(
        self,
        _request: shapes.GetRuleGroupRequest = None,
        *,
        rule_group_id: str,
    ) -> shapes.GetRuleGroupResponse:
        """
        Returns the RuleGroup that is specified by the `RuleGroupId` that you included
        in the `GetRuleGroup` request.

        To view the rules in a rule group, use ListActivatedRulesInRuleGroup.
        """
        if _request is None:
            _params = {}
            if rule_group_id is not ShapeBase.NOT_SET:
                _params['rule_group_id'] = rule_group_id
            _request = shapes.GetRuleGroupRequest(**_params)
        response = self._boto_client.get_rule_group(**_request.to_boto())

        return shapes.GetRuleGroupResponse.from_boto(response)

    def get_sampled_requests(
        self,
        _request: shapes.GetSampledRequestsRequest = None,
        *,
        web_acl_id: str,
        rule_id: str,
        time_window: shapes.TimeWindow,
        max_items: int,
    ) -> shapes.GetSampledRequestsResponse:
        """
        Gets detailed information about a specified number of requests--a sample--that
        AWS WAF randomly selects from among the first 5,000 requests that your AWS
        resource received during a time range that you choose. You can specify a sample
        size of up to 500 requests, and you can specify any time range in the previous
        three hours.

        `GetSampledRequests` returns a time range, which is usually the time range that
        you specified. However, if your resource (such as a CloudFront distribution)
        received 5,000 requests before the specified time range elapsed,
        `GetSampledRequests` returns an updated time range. This new time range
        indicates the actual period during which AWS WAF selected the requests in the
        sample.
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            if time_window is not ShapeBase.NOT_SET:
                _params['time_window'] = time_window
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.GetSampledRequestsRequest(**_params)
        response = self._boto_client.get_sampled_requests(**_request.to_boto())

        return shapes.GetSampledRequestsResponse.from_boto(response)

    def get_size_constraint_set(
        self,
        _request: shapes.GetSizeConstraintSetRequest = None,
        *,
        size_constraint_set_id: str,
    ) -> shapes.GetSizeConstraintSetResponse:
        """
        Returns the SizeConstraintSet specified by `SizeConstraintSetId`.
        """
        if _request is None:
            _params = {}
            if size_constraint_set_id is not ShapeBase.NOT_SET:
                _params['size_constraint_set_id'] = size_constraint_set_id
            _request = shapes.GetSizeConstraintSetRequest(**_params)
        response = self._boto_client.get_size_constraint_set(
            **_request.to_boto()
        )

        return shapes.GetSizeConstraintSetResponse.from_boto(response)

    def get_sql_injection_match_set(
        self,
        _request: shapes.GetSqlInjectionMatchSetRequest = None,
        *,
        sql_injection_match_set_id: str,
    ) -> shapes.GetSqlInjectionMatchSetResponse:
        """
        Returns the SqlInjectionMatchSet that is specified by `SqlInjectionMatchSetId`.
        """
        if _request is None:
            _params = {}
            if sql_injection_match_set_id is not ShapeBase.NOT_SET:
                _params['sql_injection_match_set_id'
                       ] = sql_injection_match_set_id
            _request = shapes.GetSqlInjectionMatchSetRequest(**_params)
        response = self._boto_client.get_sql_injection_match_set(
            **_request.to_boto()
        )

        return shapes.GetSqlInjectionMatchSetResponse.from_boto(response)

    def get_web_acl(
        self,
        _request: shapes.GetWebACLRequest = None,
        *,
        web_acl_id: str,
    ) -> shapes.GetWebACLResponse:
        """
        Returns the WebACL that is specified by `WebACLId`.
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            _request = shapes.GetWebACLRequest(**_params)
        response = self._boto_client.get_web_acl(**_request.to_boto())

        return shapes.GetWebACLResponse.from_boto(response)

    def get_web_acl_for_resource(
        self,
        _request: shapes.GetWebACLForResourceRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.GetWebACLForResourceResponse:
        """
        Returns the web ACL for the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.GetWebACLForResourceRequest(**_params)
        response = self._boto_client.get_web_acl_for_resource(
            **_request.to_boto()
        )

        return shapes.GetWebACLForResourceResponse.from_boto(response)

    def get_xss_match_set(
        self,
        _request: shapes.GetXssMatchSetRequest = None,
        *,
        xss_match_set_id: str,
    ) -> shapes.GetXssMatchSetResponse:
        """
        Returns the XssMatchSet that is specified by `XssMatchSetId`.
        """
        if _request is None:
            _params = {}
            if xss_match_set_id is not ShapeBase.NOT_SET:
                _params['xss_match_set_id'] = xss_match_set_id
            _request = shapes.GetXssMatchSetRequest(**_params)
        response = self._boto_client.get_xss_match_set(**_request.to_boto())

        return shapes.GetXssMatchSetResponse.from_boto(response)

    def list_activated_rules_in_rule_group(
        self,
        _request: shapes.ListActivatedRulesInRuleGroupRequest = None,
        *,
        rule_group_id: str = ShapeBase.NOT_SET,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListActivatedRulesInRuleGroupResponse:
        """
        Returns an array of ActivatedRule objects.
        """
        if _request is None:
            _params = {}
            if rule_group_id is not ShapeBase.NOT_SET:
                _params['rule_group_id'] = rule_group_id
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListActivatedRulesInRuleGroupRequest(**_params)
        response = self._boto_client.list_activated_rules_in_rule_group(
            **_request.to_boto()
        )

        return shapes.ListActivatedRulesInRuleGroupResponse.from_boto(response)

    def list_byte_match_sets(
        self,
        _request: shapes.ListByteMatchSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListByteMatchSetsResponse:
        """
        Returns an array of ByteMatchSetSummary objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListByteMatchSetsRequest(**_params)
        response = self._boto_client.list_byte_match_sets(**_request.to_boto())

        return shapes.ListByteMatchSetsResponse.from_boto(response)

    def list_geo_match_sets(
        self,
        _request: shapes.ListGeoMatchSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGeoMatchSetsResponse:
        """
        Returns an array of GeoMatchSetSummary objects in the response.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListGeoMatchSetsRequest(**_params)
        response = self._boto_client.list_geo_match_sets(**_request.to_boto())

        return shapes.ListGeoMatchSetsResponse.from_boto(response)

    def list_ip_sets(
        self,
        _request: shapes.ListIPSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListIPSetsResponse:
        """
        Returns an array of IPSetSummary objects in the response.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListIPSetsRequest(**_params)
        response = self._boto_client.list_ip_sets(**_request.to_boto())

        return shapes.ListIPSetsResponse.from_boto(response)

    def list_logging_configurations(
        self,
        _request: shapes.ListLoggingConfigurationsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListLoggingConfigurationsResponse:
        """
        Returns an array of LoggingConfiguration objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListLoggingConfigurationsRequest(**_params)
        response = self._boto_client.list_logging_configurations(
            **_request.to_boto()
        )

        return shapes.ListLoggingConfigurationsResponse.from_boto(response)

    def list_rate_based_rules(
        self,
        _request: shapes.ListRateBasedRulesRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRateBasedRulesResponse:
        """
        Returns an array of RuleSummary objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRateBasedRulesRequest(**_params)
        response = self._boto_client.list_rate_based_rules(**_request.to_boto())

        return shapes.ListRateBasedRulesResponse.from_boto(response)

    def list_regex_match_sets(
        self,
        _request: shapes.ListRegexMatchSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRegexMatchSetsResponse:
        """
        Returns an array of RegexMatchSetSummary objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRegexMatchSetsRequest(**_params)
        response = self._boto_client.list_regex_match_sets(**_request.to_boto())

        return shapes.ListRegexMatchSetsResponse.from_boto(response)

    def list_regex_pattern_sets(
        self,
        _request: shapes.ListRegexPatternSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRegexPatternSetsResponse:
        """
        Returns an array of RegexPatternSetSummary objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRegexPatternSetsRequest(**_params)
        response = self._boto_client.list_regex_pattern_sets(
            **_request.to_boto()
        )

        return shapes.ListRegexPatternSetsResponse.from_boto(response)

    def list_resources_for_web_acl(
        self,
        _request: shapes.ListResourcesForWebACLRequest = None,
        *,
        web_acl_id: str,
    ) -> shapes.ListResourcesForWebACLResponse:
        """
        Returns an array of resources associated with the specified web ACL.
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            _request = shapes.ListResourcesForWebACLRequest(**_params)
        response = self._boto_client.list_resources_for_web_acl(
            **_request.to_boto()
        )

        return shapes.ListResourcesForWebACLResponse.from_boto(response)

    def list_rule_groups(
        self,
        _request: shapes.ListRuleGroupsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRuleGroupsResponse:
        """
        Returns an array of RuleGroup objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRuleGroupsRequest(**_params)
        response = self._boto_client.list_rule_groups(**_request.to_boto())

        return shapes.ListRuleGroupsResponse.from_boto(response)

    def list_rules(
        self,
        _request: shapes.ListRulesRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListRulesResponse:
        """
        Returns an array of RuleSummary objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListRulesRequest(**_params)
        response = self._boto_client.list_rules(**_request.to_boto())

        return shapes.ListRulesResponse.from_boto(response)

    def list_size_constraint_sets(
        self,
        _request: shapes.ListSizeConstraintSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSizeConstraintSetsResponse:
        """
        Returns an array of SizeConstraintSetSummary objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListSizeConstraintSetsRequest(**_params)
        response = self._boto_client.list_size_constraint_sets(
            **_request.to_boto()
        )

        return shapes.ListSizeConstraintSetsResponse.from_boto(response)

    def list_sql_injection_match_sets(
        self,
        _request: shapes.ListSqlInjectionMatchSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSqlInjectionMatchSetsResponse:
        """
        Returns an array of SqlInjectionMatchSet objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListSqlInjectionMatchSetsRequest(**_params)
        response = self._boto_client.list_sql_injection_match_sets(
            **_request.to_boto()
        )

        return shapes.ListSqlInjectionMatchSetsResponse.from_boto(response)

    def list_subscribed_rule_groups(
        self,
        _request: shapes.ListSubscribedRuleGroupsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSubscribedRuleGroupsResponse:
        """
        Returns an array of RuleGroup objects that you are subscribed to.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListSubscribedRuleGroupsRequest(**_params)
        response = self._boto_client.list_subscribed_rule_groups(
            **_request.to_boto()
        )

        return shapes.ListSubscribedRuleGroupsResponse.from_boto(response)

    def list_web_acls(
        self,
        _request: shapes.ListWebACLsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListWebACLsResponse:
        """
        Returns an array of WebACLSummary objects in the response.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListWebACLsRequest(**_params)
        response = self._boto_client.list_web_acls(**_request.to_boto())

        return shapes.ListWebACLsResponse.from_boto(response)

    def list_xss_match_sets(
        self,
        _request: shapes.ListXssMatchSetsRequest = None,
        *,
        next_marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListXssMatchSetsResponse:
        """
        Returns an array of XssMatchSet objects.
        """
        if _request is None:
            _params = {}
            if next_marker is not ShapeBase.NOT_SET:
                _params['next_marker'] = next_marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListXssMatchSetsRequest(**_params)
        response = self._boto_client.list_xss_match_sets(**_request.to_boto())

        return shapes.ListXssMatchSetsResponse.from_boto(response)

    def put_logging_configuration(
        self,
        _request: shapes.PutLoggingConfigurationRequest = None,
        *,
        logging_configuration: shapes.LoggingConfiguration,
    ) -> shapes.PutLoggingConfigurationResponse:
        """
        Associates a LoggingConfiguration with a specified web ACL.

        You can access information about all traffic that AWS WAF inspects using the
        following steps:

          1. Create an Amazon Kinesis Data Firehose delivery stream. For more information, see [Creating an Amazon Kinesis Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html). 

          2. Associate that delivery stream to your web ACL using a `PutLoggingConfiguration` request.

        When you successfully enable logging using a `PutLoggingConfiguration` request,
        AWS WAF will create a service linked role with the necessary permissions to
        write logs to the Amazon Kinesis Data Firehose delivery stream. For more
        information, see [Logging Web ACL Traffic
        Information](http://docs.aws.amazon.com/waf/latest/developerguide/logging.html)
        in the _AWS WAF Developer Guide_.
        """
        if _request is None:
            _params = {}
            if logging_configuration is not ShapeBase.NOT_SET:
                _params['logging_configuration'] = logging_configuration
            _request = shapes.PutLoggingConfigurationRequest(**_params)
        response = self._boto_client.put_logging_configuration(
            **_request.to_boto()
        )

        return shapes.PutLoggingConfigurationResponse.from_boto(response)

    def put_permission_policy(
        self,
        _request: shapes.PutPermissionPolicyRequest = None,
        *,
        resource_arn: str,
        policy: str,
    ) -> shapes.PutPermissionPolicyResponse:
        """
        Attaches a IAM policy to the specified resource. The only supported use for this
        action is to share a RuleGroup across accounts.

        The `PutPermissionPolicy` is subject to the following restrictions:

          * You can attach only one policy with each `PutPermissionPolicy` request.

          * The policy must include an `Effect`, `Action` and `Principal`. 

          * `Effect` must specify `Allow`.

          * The `Action` in the policy must be `waf:UpdateWebACL`, `waf-regional:UpdateWebACL`, `waf:GetRuleGroup` and `waf-regional:GetRuleGroup` . Any extra or wildcard actions in the policy will be rejected.

          * The policy cannot include a `Resource` parameter.

          * The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must exist in the same region.

          * The user making the request must be the owner of the RuleGroup.

          * Your policy must be composed using IAM Policy version 2012-10-17.

        For more information, see [IAM
        Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

        An example of a valid policy parameter is shown in the Examples section below.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            _request = shapes.PutPermissionPolicyRequest(**_params)
        response = self._boto_client.put_permission_policy(**_request.to_boto())

        return shapes.PutPermissionPolicyResponse.from_boto(response)

    def update_byte_match_set(
        self,
        _request: shapes.UpdateByteMatchSetRequest = None,
        *,
        byte_match_set_id: str,
        change_token: str,
        updates: typing.List[shapes.ByteMatchSetUpdate],
    ) -> shapes.UpdateByteMatchSetResponse:
        """
        Inserts or deletes ByteMatchTuple objects (filters) in a ByteMatchSet. For each
        `ByteMatchTuple` object, you specify the following values:

          * Whether to insert or delete the object from the array. If you want to change a `ByteMatchSetUpdate` object, you delete the existing object and add a new one.

          * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header. 

          * The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to look for. For more information, including how you specify the values for the AWS WAF API and the AWS CLI or SDKs, see `TargetString` in the ByteMatchTuple data type. 

          * Where to look, such as at the beginning or the end of a query string.

          * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.

        For example, you can add a `ByteMatchSetUpdate` object that matches web requests
        in which `User-Agent` headers contain the string `BadBot`. You can then
        configure AWS WAF to block those requests.

        To create and configure a `ByteMatchSet`, perform the following steps:

          1. Create a `ByteMatchSet.` For more information, see CreateByteMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an `UpdateByteMatchSet` request.

          3. Submit an `UpdateByteMatchSet` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if byte_match_set_id is not ShapeBase.NOT_SET:
                _params['byte_match_set_id'] = byte_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateByteMatchSetRequest(**_params)
        response = self._boto_client.update_byte_match_set(**_request.to_boto())

        return shapes.UpdateByteMatchSetResponse.from_boto(response)

    def update_geo_match_set(
        self,
        _request: shapes.UpdateGeoMatchSetRequest = None,
        *,
        geo_match_set_id: str,
        change_token: str,
        updates: typing.List[shapes.GeoMatchSetUpdate],
    ) -> shapes.UpdateGeoMatchSetResponse:
        """
        Inserts or deletes GeoMatchConstraint objects in an `GeoMatchSet`. For each
        `GeoMatchConstraint` object, you specify the following values:

          * Whether to insert or delete the object from the array. If you want to change an `GeoMatchConstraint` object, you delete the existing object and add a new one.

          * The `Type`. The only valid value for `Type` is `Country`.

          * The `Value`, which is a two character code for the country to add to the `GeoMatchConstraint` object. Valid codes are listed in GeoMatchConstraint$Value.

        To create and configure an `GeoMatchSet`, perform the following steps:

          1. Submit a CreateGeoMatchSet request.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an UpdateGeoMatchSet request.

          3. Submit an `UpdateGeoMatchSet` request to specify the country that you want AWS WAF to watch for.

        When you update an `GeoMatchSet`, you specify the country that you want to add
        and/or the country that you want to delete. If you want to change a country, you
        delete the existing country and add the new one.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if geo_match_set_id is not ShapeBase.NOT_SET:
                _params['geo_match_set_id'] = geo_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateGeoMatchSetRequest(**_params)
        response = self._boto_client.update_geo_match_set(**_request.to_boto())

        return shapes.UpdateGeoMatchSetResponse.from_boto(response)

    def update_ip_set(
        self,
        _request: shapes.UpdateIPSetRequest = None,
        *,
        ip_set_id: str,
        change_token: str,
        updates: typing.List[shapes.IPSetUpdate],
    ) -> shapes.UpdateIPSetResponse:
        """
        Inserts or deletes IPSetDescriptor objects in an `IPSet`. For each
        `IPSetDescriptor` object, you specify the following values:

          * Whether to insert or delete the object from the array. If you want to change an `IPSetDescriptor` object, you delete the existing object and add a new one.

          * The IP address version, `IPv4` or `IPv6`. 

          * The IP address in CIDR notation, for example, `192.0.2.0/24` (for the range of IP addresses from `192.0.2.0` to `192.0.2.255`) or `192.0.2.44/32` (for the individual IP address `192.0.2.44`). 

        AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32.
        AWS WAF supports IPv6 address ranges: /16, /24, /32, /48, /56, /64, and /128.
        For more information about CIDR notation, see the Wikipedia entry [Classless
        Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-
        Domain_Routing).

        IPv6 addresses can be represented using any of the following formats:

          * 1111:0000:0000:0000:0000:0000:0000:0111/128

          * 1111:0:0:0:0:0:0:0111/128

          * 1111::0111/128

          * 1111::111/128

        You use an `IPSet` to specify which web requests you want to allow or block
        based on the IP addresses that the requests originated from. For example, if
        you're receiving a lot of requests from one or a small number of IP addresses
        and you want to block the requests, you can create an `IPSet` that specifies
        those IP addresses, and then configure AWS WAF to block the requests.

        To create and configure an `IPSet`, perform the following steps:

          1. Submit a CreateIPSet request.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an UpdateIPSet request.

          3. Submit an `UpdateIPSet` request to specify the IP addresses that you want AWS WAF to watch for.

        When you update an `IPSet`, you specify the IP addresses that you want to add
        and/or the IP addresses that you want to delete. If you want to change an IP
        address, you delete the existing IP address and add the new one.

        You can insert a maximum of 1000 addresses in a single request.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if ip_set_id is not ShapeBase.NOT_SET:
                _params['ip_set_id'] = ip_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateIPSetRequest(**_params)
        response = self._boto_client.update_ip_set(**_request.to_boto())

        return shapes.UpdateIPSetResponse.from_boto(response)

    def update_rate_based_rule(
        self,
        _request: shapes.UpdateRateBasedRuleRequest = None,
        *,
        rule_id: str,
        change_token: str,
        updates: typing.List[shapes.RuleUpdate],
        rate_limit: int,
    ) -> shapes.UpdateRateBasedRuleResponse:
        """
        Inserts or deletes Predicate objects in a rule and updates the `RateLimit` in
        the rule.

        Each `Predicate` object identifies a predicate, such as a ByteMatchSet or an
        IPSet, that specifies the web requests that you want to block or count. The
        `RateLimit` specifies the number of requests every five minutes that triggers
        the rule.

        If you add more than one predicate to a `RateBasedRule`, a request must match
        all the predicates and exceed the `RateLimit` to be counted or blocked. For
        example, suppose you add the following to a `RateBasedRule`:

          * An `IPSet` that matches the IP address `192.0.2.44/32`

          * A `ByteMatchSet` that matches `BadBot` in the `User-Agent` header

        Further, you specify a `RateLimit` of 15,000.

        You then add the `RateBasedRule` to a `WebACL` and specify that you want to
        block requests that satisfy the rule. For a request to be blocked, it must come
        from the IP address 192.0.2.44 _and_ the `User-Agent` header in the request must
        contain the value `BadBot`. Further, requests that match these two conditions
        much be received at a rate of more than 15,000 every five minutes. If the rate
        drops below this limit, AWS WAF no longer blocks the requests.

        As a second example, suppose you want to limit requests to a particular page on
        your site. To do this, you could add the following to a `RateBasedRule`:

          * A `ByteMatchSet` with `FieldToMatch` of `URI`

          * A `PositionalConstraint` of `STARTS_WITH`

          * A `TargetString` of `login`

        Further, you specify a `RateLimit` of 15,000.

        By adding this `RateBasedRule` to a `WebACL`, you could limit requests to your
        login page without affecting the rest of your site.
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            if rate_limit is not ShapeBase.NOT_SET:
                _params['rate_limit'] = rate_limit
            _request = shapes.UpdateRateBasedRuleRequest(**_params)
        response = self._boto_client.update_rate_based_rule(
            **_request.to_boto()
        )

        return shapes.UpdateRateBasedRuleResponse.from_boto(response)

    def update_regex_match_set(
        self,
        _request: shapes.UpdateRegexMatchSetRequest = None,
        *,
        regex_match_set_id: str,
        updates: typing.List[shapes.RegexMatchSetUpdate],
        change_token: str,
    ) -> shapes.UpdateRegexMatchSetResponse:
        """
        Inserts or deletes RegexMatchTuple objects (filters) in a RegexMatchSet. For
        each `RegexMatchSetUpdate` object, you specify the following values:

          * Whether to insert or delete the object from the array. If you want to change a `RegexMatchSetUpdate` object, you delete the existing object and add a new one.

          * The part of a web request that you want AWS WAF to inspectupdate, such as a query string or the value of the `User-Agent` header. 

          * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see RegexPatternSet. 

          * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.

        For example, you can create a `RegexPatternSet` that matches any requests with
        `User-Agent` headers that contain the string `B[a@]dB[o0]t`. You can then
        configure AWS WAF to reject those requests.

        To create and configure a `RegexMatchSet`, perform the following steps:

          1. Create a `RegexMatchSet.` For more information, see CreateRegexMatchSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexMatchSet` request.

          3. Submit an `UpdateRegexMatchSet` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the identifier of the `RegexPatternSet` that contain the regular expression patters you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if regex_match_set_id is not ShapeBase.NOT_SET:
                _params['regex_match_set_id'] = regex_match_set_id
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.UpdateRegexMatchSetRequest(**_params)
        response = self._boto_client.update_regex_match_set(
            **_request.to_boto()
        )

        return shapes.UpdateRegexMatchSetResponse.from_boto(response)

    def update_regex_pattern_set(
        self,
        _request: shapes.UpdateRegexPatternSetRequest = None,
        *,
        regex_pattern_set_id: str,
        updates: typing.List[shapes.RegexPatternSetUpdate],
        change_token: str,
    ) -> shapes.UpdateRegexPatternSetResponse:
        """
        Inserts or deletes `RegexPatternString` objects in a RegexPatternSet. For each
        `RegexPatternString` object, you specify the following values:

          * Whether to insert or delete the `RegexPatternString`.

          * The regular expression pattern that you want to insert or delete. For more information, see RegexPatternSet. 

        For example, you can create a `RegexPatternString` such as `B[a@]dB[o0]t`. AWS
        WAF will match this `RegexPatternString` to:

          * BadBot

          * BadB0t

          * B@dBot

          * B@dB0t

        To create and configure a `RegexPatternSet`, perform the following steps:

          1. Create a `RegexPatternSet.` For more information, see CreateRegexPatternSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexPatternSet` request.

          3. Submit an `UpdateRegexPatternSet` request to specify the regular expression pattern that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if regex_pattern_set_id is not ShapeBase.NOT_SET:
                _params['regex_pattern_set_id'] = regex_pattern_set_id
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.UpdateRegexPatternSetRequest(**_params)
        response = self._boto_client.update_regex_pattern_set(
            **_request.to_boto()
        )

        return shapes.UpdateRegexPatternSetResponse.from_boto(response)

    def update_rule(
        self,
        _request: shapes.UpdateRuleRequest = None,
        *,
        rule_id: str,
        change_token: str,
        updates: typing.List[shapes.RuleUpdate],
    ) -> shapes.UpdateRuleResponse:
        """
        Inserts or deletes Predicate objects in a `Rule`. Each `Predicate` object
        identifies a predicate, such as a ByteMatchSet or an IPSet, that specifies the
        web requests that you want to allow, block, or count. If you add more than one
        predicate to a `Rule`, a request must match all of the specifications to be
        allowed, blocked, or counted. For example, suppose you add the following to a
        `Rule`:

          * A `ByteMatchSet` that matches the value `BadBot` in the `User-Agent` header

          * An `IPSet` that matches the IP address `192.0.2.44`

        You then add the `Rule` to a `WebACL` and specify that you want to block
        requests that satisfy the `Rule`. For a request to be blocked, the `User-Agent`
        header in the request must contain the value `BadBot` _and_ the request must
        originate from the IP address 192.0.2.44.

        To create and configure a `Rule`, perform the following steps:

          1. Create and update the predicates that you want to include in the `Rule`.

          2. Create the `Rule`. See CreateRule.

          3. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateRule request.

          4. Submit an `UpdateRule` request to add predicates to the `Rule`.

          5. Create and update a `WebACL` that contains the `Rule`. See CreateWebACL.

        If you want to replace one `ByteMatchSet` or `IPSet` with another, you delete
        the existing one and add the new one.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if rule_id is not ShapeBase.NOT_SET:
                _params['rule_id'] = rule_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateRuleRequest(**_params)
        response = self._boto_client.update_rule(**_request.to_boto())

        return shapes.UpdateRuleResponse.from_boto(response)

    def update_rule_group(
        self,
        _request: shapes.UpdateRuleGroupRequest = None,
        *,
        rule_group_id: str,
        updates: typing.List[shapes.RuleGroupUpdate],
        change_token: str,
    ) -> shapes.UpdateRuleGroupResponse:
        """
        Inserts or deletes ActivatedRule objects in a `RuleGroup`.

        You can only insert `REGULAR` rules into a rule group.

        You can have a maximum of ten rules per rule group.

        To create and configure a `RuleGroup`, perform the following steps:

          1. Create and update the `Rules` that you want to include in the `RuleGroup`. See CreateRule.

          2. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateRuleGroup request.

          3. Submit an `UpdateRuleGroup` request to add `Rules` to the `RuleGroup`.

          4. Create and update a `WebACL` that contains the `RuleGroup`. See CreateWebACL.

        If you want to replace one `Rule` with another, you delete the existing one and
        add the new one.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if rule_group_id is not ShapeBase.NOT_SET:
                _params['rule_group_id'] = rule_group_id
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            _request = shapes.UpdateRuleGroupRequest(**_params)
        response = self._boto_client.update_rule_group(**_request.to_boto())

        return shapes.UpdateRuleGroupResponse.from_boto(response)

    def update_size_constraint_set(
        self,
        _request: shapes.UpdateSizeConstraintSetRequest = None,
        *,
        size_constraint_set_id: str,
        change_token: str,
        updates: typing.List[shapes.SizeConstraintSetUpdate],
    ) -> shapes.UpdateSizeConstraintSetResponse:
        """
        Inserts or deletes SizeConstraint objects (filters) in a SizeConstraintSet. For
        each `SizeConstraint` object, you specify the following values:

          * Whether to insert or delete the object from the array. If you want to change a `SizeConstraintSetUpdate` object, you delete the existing object and add a new one.

          * The part of a web request that you want AWS WAF to evaluate, such as the length of a query string or the length of the `User-Agent` header.

          * Whether to perform any transformations on the request, such as converting it to lowercase, before checking its length. Note that transformations of the request body are not supported because the AWS resource forwards only the first `8192` bytes of your request to AWS WAF.

        You can only specify a single type of TextTransformation.

          * A `ComparisonOperator` used for evaluating the selected part of the request against the specified `Size`, such as equals, greater than, less than, and so on.

          * The length, in bytes, that you want AWS WAF to watch for in selected part of the request. The length is computed after applying the transformation.

        For example, you can add a `SizeConstraintSetUpdate` object that matches web
        requests in which the length of the `User-Agent` header is greater than 100
        bytes. You can then configure AWS WAF to block those requests.

        To create and configure a `SizeConstraintSet`, perform the following steps:

          1. Create a `SizeConstraintSet.` For more information, see CreateSizeConstraintSet.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an `UpdateSizeConstraintSet` request.

          3. Submit an `UpdateSizeConstraintSet` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if size_constraint_set_id is not ShapeBase.NOT_SET:
                _params['size_constraint_set_id'] = size_constraint_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateSizeConstraintSetRequest(**_params)
        response = self._boto_client.update_size_constraint_set(
            **_request.to_boto()
        )

        return shapes.UpdateSizeConstraintSetResponse.from_boto(response)

    def update_sql_injection_match_set(
        self,
        _request: shapes.UpdateSqlInjectionMatchSetRequest = None,
        *,
        sql_injection_match_set_id: str,
        change_token: str,
        updates: typing.List[shapes.SqlInjectionMatchSetUpdate],
    ) -> shapes.UpdateSqlInjectionMatchSetResponse:
        """
        Inserts or deletes SqlInjectionMatchTuple objects (filters) in a
        SqlInjectionMatchSet. For each `SqlInjectionMatchTuple` object, you specify the
        following values:

          * `Action`: Whether to insert the object into or delete the object from the array. To change a `SqlInjectionMatchTuple`, you delete the existing object and add a new one.

          * `FieldToMatch`: The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.

          * `TextTransformation`: Which text transformation, if any, to perform on the web request before inspecting the request for snippets of malicious SQL code.

        You can only specify a single type of TextTransformation.

        You use `SqlInjectionMatchSet` objects to specify which CloudFront requests you
        want to allow, block, or count. For example, if you're receiving requests that
        contain snippets of SQL code in the query string and you want to block the
        requests, you can create a `SqlInjectionMatchSet` with the applicable settings,
        and then configure AWS WAF to block the requests.

        To create and configure a `SqlInjectionMatchSet`, perform the following steps:

          1. Submit a CreateSqlInjectionMatchSet request.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an UpdateIPSet request.

          3. Submit an `UpdateSqlInjectionMatchSet` request to specify the parts of web requests that you want AWS WAF to inspect for snippets of SQL code.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if sql_injection_match_set_id is not ShapeBase.NOT_SET:
                _params['sql_injection_match_set_id'
                       ] = sql_injection_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateSqlInjectionMatchSetRequest(**_params)
        response = self._boto_client.update_sql_injection_match_set(
            **_request.to_boto()
        )

        return shapes.UpdateSqlInjectionMatchSetResponse.from_boto(response)

    def update_web_acl(
        self,
        _request: shapes.UpdateWebACLRequest = None,
        *,
        web_acl_id: str,
        change_token: str,
        updates: typing.List[shapes.WebACLUpdate] = ShapeBase.NOT_SET,
        default_action: shapes.WafAction = ShapeBase.NOT_SET,
    ) -> shapes.UpdateWebACLResponse:
        """
        Inserts or deletes ActivatedRule objects in a `WebACL`. Each `Rule` identifies
        web requests that you want to allow, block, or count. When you update a
        `WebACL`, you specify the following values:

          * A default action for the `WebACL`, either `ALLOW` or `BLOCK`. AWS WAF performs the default action if a request doesn't match the criteria in any of the `Rules` in a `WebACL`.

          * The `Rules` that you want to add and/or delete. If you want to replace one `Rule` with another, you delete the existing `Rule` and add the new one.

          * For each `Rule`, whether you want AWS WAF to allow requests, block requests, or count requests that match the conditions in the `Rule`.

          * The order in which you want AWS WAF to evaluate the `Rules` in a `WebACL`. If you add more than one `Rule` to a `WebACL`, AWS WAF evaluates each request against the `Rules` in order based on the value of `Priority`. (The `Rule` that has the lowest value for `Priority` is evaluated first.) When a web request matches all of the predicates (such as `ByteMatchSets` and `IPSets`) in a `Rule`, AWS WAF immediately takes the corresponding action, allow or block, and doesn't evaluate the request against the remaining `Rules` in the `WebACL`, if any. 

        To create and configure a `WebACL`, perform the following steps:

          1. Create and update the predicates that you want to include in `Rules`. For more information, see CreateByteMatchSet, UpdateByteMatchSet, CreateIPSet, UpdateIPSet, CreateSqlInjectionMatchSet, and UpdateSqlInjectionMatchSet.

          2. Create and update the `Rules` that you want to include in the `WebACL`. For more information, see CreateRule and UpdateRule.

          3. Create a `WebACL`. See CreateWebACL.

          4. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an UpdateWebACL request.

          5. Submit an `UpdateWebACL` request to specify the `Rules` that you want to include in the `WebACL`, to specify the default action, and to associate the `WebACL` with a CloudFront distribution. 

        Be aware that if you try to add a RATE_BASED rule to a web ACL without setting
        the rule type when first creating the rule, the UpdateWebACL request will fail
        because the request tries to add a REGULAR rule (the default rule type) with the
        specified ID, which does not exist.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if web_acl_id is not ShapeBase.NOT_SET:
                _params['web_acl_id'] = web_acl_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            if default_action is not ShapeBase.NOT_SET:
                _params['default_action'] = default_action
            _request = shapes.UpdateWebACLRequest(**_params)
        response = self._boto_client.update_web_acl(**_request.to_boto())

        return shapes.UpdateWebACLResponse.from_boto(response)

    def update_xss_match_set(
        self,
        _request: shapes.UpdateXssMatchSetRequest = None,
        *,
        xss_match_set_id: str,
        change_token: str,
        updates: typing.List[shapes.XssMatchSetUpdate],
    ) -> shapes.UpdateXssMatchSetResponse:
        """
        Inserts or deletes XssMatchTuple objects (filters) in an XssMatchSet. For each
        `XssMatchTuple` object, you specify the following values:

          * `Action`: Whether to insert the object into or delete the object from the array. To change a `XssMatchTuple`, you delete the existing object and add a new one.

          * `FieldToMatch`: The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.

          * `TextTransformation`: Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.

        You can only specify a single type of TextTransformation.

        You use `XssMatchSet` objects to specify which CloudFront requests you want to
        allow, block, or count. For example, if you're receiving requests that contain
        cross-site scripting attacks in the request body and you want to block the
        requests, you can create an `XssMatchSet` with the applicable settings, and then
        configure AWS WAF to block the requests.

        To create and configure an `XssMatchSet`, perform the following steps:

          1. Submit a CreateXssMatchSet request.

          2. Use GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an UpdateIPSet request.

          3. Submit an `UpdateXssMatchSet` request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks.

        For more information about how to use the AWS WAF API to allow or block HTTP
        requests, see the [AWS WAF Developer
        Guide](http://docs.aws.amazon.com/waf/latest/developerguide/).
        """
        if _request is None:
            _params = {}
            if xss_match_set_id is not ShapeBase.NOT_SET:
                _params['xss_match_set_id'] = xss_match_set_id
            if change_token is not ShapeBase.NOT_SET:
                _params['change_token'] = change_token
            if updates is not ShapeBase.NOT_SET:
                _params['updates'] = updates
            _request = shapes.UpdateXssMatchSetRequest(**_params)
        response = self._boto_client.update_xss_match_set(**_request.to_boto())

        return shapes.UpdateXssMatchSetResponse.from_boto(response)
