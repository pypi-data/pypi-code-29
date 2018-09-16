import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("macie", *args, **kwargs)

    def associate_member_account(
        self,
        _request: shapes.AssociateMemberAccountRequest = None,
        *,
        member_account_id: str,
    ) -> None:
        """
        Associates a specified AWS account with Amazon Macie as a member account.
        """
        if _request is None:
            _params = {}
            if member_account_id is not ShapeBase.NOT_SET:
                _params['member_account_id'] = member_account_id
            _request = shapes.AssociateMemberAccountRequest(**_params)
        response = self._boto_client.associate_member_account(
            **_request.to_boto()
        )

    def associate_s3_resources(
        self,
        _request: shapes.AssociateS3ResourcesRequest = None,
        *,
        s3_resources: typing.List[shapes.S3ResourceClassification],
        member_account_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateS3ResourcesResult:
        """
        Associates specified S3 resources with Amazon Macie for monitoring and data
        classification. If memberAccountId isn't specified, the action associates
        specified S3 resources with Macie for the current master account. If
        memberAccountId is specified, the action associates specified S3 resources with
        Macie for the specified member account.
        """
        if _request is None:
            _params = {}
            if s3_resources is not ShapeBase.NOT_SET:
                _params['s3_resources'] = s3_resources
            if member_account_id is not ShapeBase.NOT_SET:
                _params['member_account_id'] = member_account_id
            _request = shapes.AssociateS3ResourcesRequest(**_params)
        response = self._boto_client.associate_s3_resources(
            **_request.to_boto()
        )

        return shapes.AssociateS3ResourcesResult.from_boto(response)

    def disassociate_member_account(
        self,
        _request: shapes.DisassociateMemberAccountRequest = None,
        *,
        member_account_id: str,
    ) -> None:
        """
        Removes the specified member account from Amazon Macie.
        """
        if _request is None:
            _params = {}
            if member_account_id is not ShapeBase.NOT_SET:
                _params['member_account_id'] = member_account_id
            _request = shapes.DisassociateMemberAccountRequest(**_params)
        response = self._boto_client.disassociate_member_account(
            **_request.to_boto()
        )

    def disassociate_s3_resources(
        self,
        _request: shapes.DisassociateS3ResourcesRequest = None,
        *,
        associated_s3_resources: typing.List[shapes.S3Resource],
        member_account_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateS3ResourcesResult:
        """
        Removes specified S3 resources from being monitored by Amazon Macie. If
        memberAccountId isn't specified, the action removes specified S3 resources from
        Macie for the current master account. If memberAccountId is specified, the
        action removes specified S3 resources from Macie for the specified member
        account.
        """
        if _request is None:
            _params = {}
            if associated_s3_resources is not ShapeBase.NOT_SET:
                _params['associated_s3_resources'] = associated_s3_resources
            if member_account_id is not ShapeBase.NOT_SET:
                _params['member_account_id'] = member_account_id
            _request = shapes.DisassociateS3ResourcesRequest(**_params)
        response = self._boto_client.disassociate_s3_resources(
            **_request.to_boto()
        )

        return shapes.DisassociateS3ResourcesResult.from_boto(response)

    def list_member_accounts(
        self,
        _request: shapes.ListMemberAccountsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListMemberAccountsResult:
        """
        Lists all Amazon Macie member accounts for the current Amazon Macie master
        account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListMemberAccountsRequest(**_params)
        response = self._boto_client.list_member_accounts(**_request.to_boto())

        return shapes.ListMemberAccountsResult.from_boto(response)

    def list_s3_resources(
        self,
        _request: shapes.ListS3ResourcesRequest = None,
        *,
        member_account_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListS3ResourcesResult:
        """
        Lists all the S3 resources associated with Amazon Macie. If memberAccountId
        isn't specified, the action lists the S3 resources associated with Amazon Macie
        for the current master account. If memberAccountId is specified, the action
        lists the S3 resources associated with Amazon Macie for the specified member
        account.
        """
        if _request is None:
            _params = {}
            if member_account_id is not ShapeBase.NOT_SET:
                _params['member_account_id'] = member_account_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListS3ResourcesRequest(**_params)
        response = self._boto_client.list_s3_resources(**_request.to_boto())

        return shapes.ListS3ResourcesResult.from_boto(response)

    def update_s3_resources(
        self,
        _request: shapes.UpdateS3ResourcesRequest = None,
        *,
        s3_resources_update: typing.List[shapes.S3ResourceClassificationUpdate],
        member_account_id: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateS3ResourcesResult:
        """
        Updates the classification types for the specified S3 resources. If
        memberAccountId isn't specified, the action updates the classification types of
        the S3 resources associated with Amazon Macie for the current master account. If
        memberAccountId is specified, the action updates the classification types of the
        S3 resources associated with Amazon Macie for the specified member account.
        """
        if _request is None:
            _params = {}
            if s3_resources_update is not ShapeBase.NOT_SET:
                _params['s3_resources_update'] = s3_resources_update
            if member_account_id is not ShapeBase.NOT_SET:
                _params['member_account_id'] = member_account_id
            _request = shapes.UpdateS3ResourcesRequest(**_params)
        response = self._boto_client.update_s3_resources(**_request.to_boto())

        return shapes.UpdateS3ResourcesResult.from_boto(response)
