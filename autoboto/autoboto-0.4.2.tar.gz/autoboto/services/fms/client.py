import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("fms", *args, **kwargs)

    def associate_admin_account(
        self,
        _request: shapes.AssociateAdminAccountRequest = None,
        *,
        admin_account: str,
    ) -> None:
        """
        Sets the AWS Firewall Manager administrator account. AWS Firewall Manager must
        be associated with the master account your AWS organization or associated with a
        member account that has the appropriate permissions. If the account ID that you
        submit is not an AWS Organizations master account, AWS Firewall Manager will set
        the appropriate permissions for the given member account.

        The account that you associate with AWS Firewall Manager is called the AWS
        Firewall Manager administrator account.
        """
        if _request is None:
            _params = {}
            if admin_account is not ShapeBase.NOT_SET:
                _params['admin_account'] = admin_account
            _request = shapes.AssociateAdminAccountRequest(**_params)
        response = self._boto_client.associate_admin_account(
            **_request.to_boto()
        )

    def delete_notification_channel(
        self,
        _request: shapes.DeleteNotificationChannelRequest = None,
    ) -> None:
        """
        Deletes an AWS Firewall Manager association with the IAM role and the Amazon
        Simple Notification Service (SNS) topic that is used to record AWS Firewall
        Manager SNS logs.
        """
        if _request is None:
            _params = {}
            _request = shapes.DeleteNotificationChannelRequest(**_params)
        response = self._boto_client.delete_notification_channel(
            **_request.to_boto()
        )

    def delete_policy(
        self,
        _request: shapes.DeletePolicyRequest = None,
        *,
        policy_id: str,
    ) -> None:
        """
        Permanently deletes an AWS Firewall Manager policy.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            _request = shapes.DeletePolicyRequest(**_params)
        response = self._boto_client.delete_policy(**_request.to_boto())

    def disassociate_admin_account(
        self,
        _request: shapes.DisassociateAdminAccountRequest = None,
    ) -> None:
        """
        Disassociates the account that has been set as the AWS Firewall Manager
        administrator account. You will need to submit an `AssociateAdminAccount`
        request to set a new account as the AWS Firewall administrator.
        """
        if _request is None:
            _params = {}
            _request = shapes.DisassociateAdminAccountRequest(**_params)
        response = self._boto_client.disassociate_admin_account(
            **_request.to_boto()
        )

    def get_admin_account(
        self,
        _request: shapes.GetAdminAccountRequest = None,
    ) -> shapes.GetAdminAccountResponse:
        """
        Returns the AWS Organizations master account that is associated with AWS
        Firewall Manager as the AWS Firewall Manager administrator.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetAdminAccountRequest(**_params)
        response = self._boto_client.get_admin_account(**_request.to_boto())

        return shapes.GetAdminAccountResponse.from_boto(response)

    def get_compliance_detail(
        self,
        _request: shapes.GetComplianceDetailRequest = None,
        *,
        policy_id: str,
        member_account: str,
    ) -> shapes.GetComplianceDetailResponse:
        """
        Returns detailed compliance information about the specified member account.
        Details include resources that are in and out of compliance with the specified
        policy. Resources are considered non-compliant if the specified policy has not
        been applied to them.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            if member_account is not ShapeBase.NOT_SET:
                _params['member_account'] = member_account
            _request = shapes.GetComplianceDetailRequest(**_params)
        response = self._boto_client.get_compliance_detail(**_request.to_boto())

        return shapes.GetComplianceDetailResponse.from_boto(response)

    def get_notification_channel(
        self,
        _request: shapes.GetNotificationChannelRequest = None,
    ) -> shapes.GetNotificationChannelResponse:
        """
        Returns information about the Amazon Simple Notification Service (SNS) topic
        that is used to record AWS Firewall Manager SNS logs.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetNotificationChannelRequest(**_params)
        response = self._boto_client.get_notification_channel(
            **_request.to_boto()
        )

        return shapes.GetNotificationChannelResponse.from_boto(response)

    def get_policy(
        self,
        _request: shapes.GetPolicyRequest = None,
        *,
        policy_id: str,
    ) -> shapes.GetPolicyResponse:
        """
        Returns information about the specified AWS Firewall Manager policy.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            _request = shapes.GetPolicyRequest(**_params)
        response = self._boto_client.get_policy(**_request.to_boto())

        return shapes.GetPolicyResponse.from_boto(response)

    def list_compliance_status(
        self,
        _request: shapes.ListComplianceStatusRequest = None,
        *,
        policy_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListComplianceStatusResponse:
        """
        Returns an array of `PolicyComplianceStatus` objects in the response. Use
        `PolicyComplianceStatus` to get a summary of which member accounts are protected
        by the specified policy.
        """
        if _request is None:
            _params = {}
            if policy_id is not ShapeBase.NOT_SET:
                _params['policy_id'] = policy_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListComplianceStatusRequest(**_params)
        response = self._boto_client.list_compliance_status(
            **_request.to_boto()
        )

        return shapes.ListComplianceStatusResponse.from_boto(response)

    def list_member_accounts(
        self,
        _request: shapes.ListMemberAccountsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListMemberAccountsResponse:
        """
        Returns a `MemberAccounts` object that lists the member accounts in the
        administrator's AWS organization.

        The `ListMemberAccounts` must be submitted by the account that is set as the AWS
        Firewall Manager administrator.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListMemberAccountsRequest(**_params)
        response = self._boto_client.list_member_accounts(**_request.to_boto())

        return shapes.ListMemberAccountsResponse.from_boto(response)

    def list_policies(
        self,
        _request: shapes.ListPoliciesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPoliciesResponse:
        """
        Returns an array of `PolicySummary` objects in the response.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPoliciesRequest(**_params)
        response = self._boto_client.list_policies(**_request.to_boto())

        return shapes.ListPoliciesResponse.from_boto(response)

    def put_notification_channel(
        self,
        _request: shapes.PutNotificationChannelRequest = None,
        *,
        sns_topic_arn: str,
        sns_role_name: str,
    ) -> None:
        """
        Designates the IAM role and Amazon Simple Notification Service (SNS) topic that
        AWS Firewall Manager uses to record SNS logs.
        """
        if _request is None:
            _params = {}
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if sns_role_name is not ShapeBase.NOT_SET:
                _params['sns_role_name'] = sns_role_name
            _request = shapes.PutNotificationChannelRequest(**_params)
        response = self._boto_client.put_notification_channel(
            **_request.to_boto()
        )

    def put_policy(
        self,
        _request: shapes.PutPolicyRequest = None,
        *,
        policy: shapes.Policy,
    ) -> shapes.PutPolicyResponse:
        """
        Creates an AWS Firewall Manager policy.
        """
        if _request is None:
            _params = {}
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            _request = shapes.PutPolicyRequest(**_params)
        response = self._boto_client.put_policy(**_request.to_boto())

        return shapes.PutPolicyResponse.from_boto(response)
