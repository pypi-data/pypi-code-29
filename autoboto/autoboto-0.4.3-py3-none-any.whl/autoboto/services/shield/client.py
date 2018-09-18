import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("shield", *args, **kwargs)

    def associate_drt_log_bucket(
        self,
        _request: shapes.AssociateDRTLogBucketRequest = None,
        *,
        log_bucket: str,
    ) -> shapes.AssociateDRTLogBucketResponse:
        """
        Authorizes the DDoS Response team (DRT) to access the specified Amazon S3 bucket
        containing your flow logs. You can associate up to 10 Amazon S3 buckets with
        your subscription.

        To use the services of the DRT and make an `AssociateDRTLogBucket` request, you
        must be subscribed to the [Business Support
        plan](https://aws.amazon.com/premiumsupport/business-support/) or the
        [Enterprise Support plan](https://aws.amazon.com/premiumsupport/enterprise-
        support/).
        """
        if _request is None:
            _params = {}
            if log_bucket is not ShapeBase.NOT_SET:
                _params['log_bucket'] = log_bucket
            _request = shapes.AssociateDRTLogBucketRequest(**_params)
        response = self._boto_client.associate_drt_log_bucket(
            **_request.to_boto()
        )

        return shapes.AssociateDRTLogBucketResponse.from_boto(response)

    def associate_drt_role(
        self,
        _request: shapes.AssociateDRTRoleRequest = None,
        *,
        role_arn: str,
    ) -> shapes.AssociateDRTRoleResponse:
        """
        Authorizes the DDoS Response team (DRT), using the specified role, to access
        your AWS account to assist with DDoS attack mitigation during potential attacks.
        This enables the DRT to inspect your AWS WAF configuration and create or update
        AWS WAF rules and web ACLs.

        You can associate only one `RoleArn` with your subscription. If you submit an
        `AssociateDRTRole` request for an account that already has an associated role,
        the new `RoleArn` will replace the existing `RoleArn`.

        Prior to making the `AssociateDRTRole` request, you must attach the
        [AWSShieldDRTAccessPolicy](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-
        role/AWSShieldDRTAccessPolicy) managed policy to the role you will specify in
        the request. For more information see [Attaching and Detaching IAM Policies](
        https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-
        detach.html). The role must also trust the service principal `
        drt.shield.amazonaws.com`. For more information, see [IAM JSON Policy Elements:
        Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html).

        The DRT will have access only to your AWS WAF and Shield resources. By
        submitting this request, you authorize the DRT to inspect your AWS WAF and
        Shield configuration and create and update AWS WAF rules and web ACLs on your
        behalf. The DRT takes these actions only if explicitly authorized by you.

        You must have the `iam:PassRole` permission to make an `AssociateDRTRole`
        request. For more information, see [Granting a User Permissions to Pass a Role
        to an AWS
        Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).

        To use the services of the DRT and make an `AssociateDRTRole` request, you must
        be subscribed to the [Business Support
        plan](https://aws.amazon.com/premiumsupport/business-support/) or the
        [Enterprise Support plan](https://aws.amazon.com/premiumsupport/enterprise-
        support/).
        """
        if _request is None:
            _params = {}
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.AssociateDRTRoleRequest(**_params)
        response = self._boto_client.associate_drt_role(**_request.to_boto())

        return shapes.AssociateDRTRoleResponse.from_boto(response)

    def create_protection(
        self,
        _request: shapes.CreateProtectionRequest = None,
        *,
        name: str,
        resource_arn: str,
    ) -> shapes.CreateProtectionResponse:
        """
        Enables AWS Shield Advanced for a specific AWS resource. The resource can be an
        Amazon CloudFront distribution, Elastic Load Balancing load balancer, Elastic IP
        Address, or an Amazon Route 53 hosted zone.

        You can add protection to only a single resource with each CreateProtection
        request. If you want to add protection to multiple resources at once, use the
        [AWS WAF console](https://console.aws.amazon.com/waf/). For more information see
        [Getting Started with AWS Shield
        Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-
        ddos.html) and [Add AWS Shield Advanced Protection to more AWS
        Resources](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-
        protection.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.CreateProtectionRequest(**_params)
        response = self._boto_client.create_protection(**_request.to_boto())

        return shapes.CreateProtectionResponse.from_boto(response)

    def create_subscription(
        self,
        _request: shapes.CreateSubscriptionRequest = None,
    ) -> shapes.CreateSubscriptionResponse:
        """
        Activates AWS Shield Advanced for an account.

        As part of this request you can specify `EmergencySettings` that automaticaly
        grant the DDoS response team (DRT) needed permissions to assist you during a
        suspected DDoS attack. For more information see [Authorize the DDoS Response
        Team to Create Rules and Web ACLs on Your
        Behalf](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-
        DRT.html).

        When you initally create a subscription, your subscription is set to be
        automatically renewed at the end of the existing subscription period. You can
        change this by submitting an `UpdateSubscription` request.
        """
        if _request is None:
            _params = {}
            _request = shapes.CreateSubscriptionRequest(**_params)
        response = self._boto_client.create_subscription(**_request.to_boto())

        return shapes.CreateSubscriptionResponse.from_boto(response)

    def delete_protection(
        self,
        _request: shapes.DeleteProtectionRequest = None,
        *,
        protection_id: str,
    ) -> shapes.DeleteProtectionResponse:
        """
        Deletes an AWS Shield Advanced Protection.
        """
        if _request is None:
            _params = {}
            if protection_id is not ShapeBase.NOT_SET:
                _params['protection_id'] = protection_id
            _request = shapes.DeleteProtectionRequest(**_params)
        response = self._boto_client.delete_protection(**_request.to_boto())

        return shapes.DeleteProtectionResponse.from_boto(response)

    def delete_subscription(
        self,
        _request: shapes.DeleteSubscriptionRequest = None,
    ) -> shapes.DeleteSubscriptionResponse:
        """
        Removes AWS Shield Advanced from an account. AWS Shield Advanced requires a
        1-year subscription commitment. You cannot delete a subscription prior to the
        completion of that commitment.
        """
        if _request is None:
            _params = {}
            _request = shapes.DeleteSubscriptionRequest(**_params)
        response = self._boto_client.delete_subscription(**_request.to_boto())

        return shapes.DeleteSubscriptionResponse.from_boto(response)

    def describe_attack(
        self,
        _request: shapes.DescribeAttackRequest = None,
        *,
        attack_id: str,
    ) -> shapes.DescribeAttackResponse:
        """
        Describes the details of a DDoS attack.
        """
        if _request is None:
            _params = {}
            if attack_id is not ShapeBase.NOT_SET:
                _params['attack_id'] = attack_id
            _request = shapes.DescribeAttackRequest(**_params)
        response = self._boto_client.describe_attack(**_request.to_boto())

        return shapes.DescribeAttackResponse.from_boto(response)

    def describe_drt_access(
        self,
        _request: shapes.DescribeDRTAccessRequest = None,
    ) -> shapes.DescribeDRTAccessResponse:
        """
        Returns the current role and list of Amazon S3 log buckets used by the DDoS
        Response team (DRT) to access your AWS account while assisting with attack
        mitigation.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeDRTAccessRequest(**_params)
        response = self._boto_client.describe_drt_access(**_request.to_boto())

        return shapes.DescribeDRTAccessResponse.from_boto(response)

    def describe_emergency_contact_settings(
        self,
        _request: shapes.DescribeEmergencyContactSettingsRequest = None,
    ) -> shapes.DescribeEmergencyContactSettingsResponse:
        """
        Lists the email addresses that the DRT can use to contact you during a suspected
        attack.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeEmergencyContactSettingsRequest(**_params)
        response = self._boto_client.describe_emergency_contact_settings(
            **_request.to_boto()
        )

        return shapes.DescribeEmergencyContactSettingsResponse.from_boto(
            response
        )

    def describe_protection(
        self,
        _request: shapes.DescribeProtectionRequest = None,
        *,
        protection_id: str,
    ) -> shapes.DescribeProtectionResponse:
        """
        Lists the details of a Protection object.
        """
        if _request is None:
            _params = {}
            if protection_id is not ShapeBase.NOT_SET:
                _params['protection_id'] = protection_id
            _request = shapes.DescribeProtectionRequest(**_params)
        response = self._boto_client.describe_protection(**_request.to_boto())

        return shapes.DescribeProtectionResponse.from_boto(response)

    def describe_subscription(
        self,
        _request: shapes.DescribeSubscriptionRequest = None,
    ) -> shapes.DescribeSubscriptionResponse:
        """
        Provides details about the AWS Shield Advanced subscription for an account.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeSubscriptionRequest(**_params)
        response = self._boto_client.describe_subscription(**_request.to_boto())

        return shapes.DescribeSubscriptionResponse.from_boto(response)

    def disassociate_drt_log_bucket(
        self,
        _request: shapes.DisassociateDRTLogBucketRequest = None,
        *,
        log_bucket: str,
    ) -> shapes.DisassociateDRTLogBucketResponse:
        """
        Removes the DDoS Response team's (DRT) access to the specified Amazon S3 bucket
        containing your flow logs.

        To make a `DisassociateDRTLogBucket` request, you must be subscribed to the
        [Business Support plan](https://aws.amazon.com/premiumsupport/business-support/)
        or the [Enterprise Support
        plan](https://aws.amazon.com/premiumsupport/enterprise-support/). However, if
        you are not subscribed to one of these support plans, but had been previously
        and had granted the DRT access to your account, you can submit a
        `DisassociateDRTLogBucket` request to remove this access.
        """
        if _request is None:
            _params = {}
            if log_bucket is not ShapeBase.NOT_SET:
                _params['log_bucket'] = log_bucket
            _request = shapes.DisassociateDRTLogBucketRequest(**_params)
        response = self._boto_client.disassociate_drt_log_bucket(
            **_request.to_boto()
        )

        return shapes.DisassociateDRTLogBucketResponse.from_boto(response)

    def disassociate_drt_role(
        self,
        _request: shapes.DisassociateDRTRoleRequest = None,
    ) -> shapes.DisassociateDRTRoleResponse:
        """
        Removes the DDoS Response team's (DRT) access to your AWS account.

        To make a `DisassociateDRTRole` request, you must be subscribed to the [Business
        Support plan](https://aws.amazon.com/premiumsupport/business-support/) or the
        [Enterprise Support plan](https://aws.amazon.com/premiumsupport/enterprise-
        support/). However, if you are not subscribed to one of these support plans, but
        had been previously and had granted the DRT access to your account, you can
        submit a `DisassociateDRTRole` request to remove this access.
        """
        if _request is None:
            _params = {}
            _request = shapes.DisassociateDRTRoleRequest(**_params)
        response = self._boto_client.disassociate_drt_role(**_request.to_boto())

        return shapes.DisassociateDRTRoleResponse.from_boto(response)

    def get_subscription_state(
        self,
        _request: shapes.GetSubscriptionStateRequest = None,
    ) -> shapes.GetSubscriptionStateResponse:
        """
        Returns the `SubscriptionState`, either `Active` or `Inactive`.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetSubscriptionStateRequest(**_params)
        response = self._boto_client.get_subscription_state(
            **_request.to_boto()
        )

        return shapes.GetSubscriptionStateResponse.from_boto(response)

    def list_attacks(
        self,
        _request: shapes.ListAttacksRequest = None,
        *,
        resource_arns: typing.List[str] = ShapeBase.NOT_SET,
        start_time: shapes.TimeRange = ShapeBase.NOT_SET,
        end_time: shapes.TimeRange = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAttacksResponse:
        """
        Returns all ongoing DDoS attacks or all DDoS attacks during a specified time
        period.
        """
        if _request is None:
            _params = {}
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAttacksRequest(**_params)
        response = self._boto_client.list_attacks(**_request.to_boto())

        return shapes.ListAttacksResponse.from_boto(response)

    def list_protections(
        self,
        _request: shapes.ListProtectionsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListProtectionsResponse:
        """
        Lists all Protection objects for the account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListProtectionsRequest(**_params)
        paginator = self.get_paginator("list_protections").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListProtectionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListProtectionsResponse.from_boto(response)

    def update_emergency_contact_settings(
        self,
        _request: shapes.UpdateEmergencyContactSettingsRequest = None,
        *,
        emergency_contact_list: typing.List[shapes.EmergencyContact
                                           ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateEmergencyContactSettingsResponse:
        """
        Updates the details of the list of email addresses that the DRT can use to
        contact you during a suspected attack.
        """
        if _request is None:
            _params = {}
            if emergency_contact_list is not ShapeBase.NOT_SET:
                _params['emergency_contact_list'] = emergency_contact_list
            _request = shapes.UpdateEmergencyContactSettingsRequest(**_params)
        response = self._boto_client.update_emergency_contact_settings(
            **_request.to_boto()
        )

        return shapes.UpdateEmergencyContactSettingsResponse.from_boto(response)

    def update_subscription(
        self,
        _request: shapes.UpdateSubscriptionRequest = None,
        *,
        auto_renew: typing.Union[str, shapes.AutoRenew] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSubscriptionResponse:
        """
        Updates the details of an existing subscription. Only enter values for
        parameters you want to change. Empty parameters are not updated.
        """
        if _request is None:
            _params = {}
            if auto_renew is not ShapeBase.NOT_SET:
                _params['auto_renew'] = auto_renew
            _request = shapes.UpdateSubscriptionRequest(**_params)
        response = self._boto_client.update_subscription(**_request.to_boto())

        return shapes.UpdateSubscriptionResponse.from_boto(response)
