import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("guardduty", *args, **kwargs)

    def accept_invitation(
        self,
        _request: shapes.AcceptInvitationRequest = None,
        *,
        detector_id: str,
        invitation_id: str = ShapeBase.NOT_SET,
        master_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AcceptInvitationResponse:
        """
        Accepts the invitation to be monitored by a master GuardDuty account.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if invitation_id is not ShapeBase.NOT_SET:
                _params['invitation_id'] = invitation_id
            if master_id is not ShapeBase.NOT_SET:
                _params['master_id'] = master_id
            _request = shapes.AcceptInvitationRequest(**_params)
        response = self._boto_client.accept_invitation(**_request.to_boto())

        return shapes.AcceptInvitationResponse.from_boto(response)

    def archive_findings(
        self,
        _request: shapes.ArchiveFindingsRequest = None,
        *,
        detector_id: str,
        finding_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ArchiveFindingsResponse:
        """
        Archives Amazon GuardDuty findings specified by the list of finding IDs.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if finding_ids is not ShapeBase.NOT_SET:
                _params['finding_ids'] = finding_ids
            _request = shapes.ArchiveFindingsRequest(**_params)
        response = self._boto_client.archive_findings(**_request.to_boto())

        return shapes.ArchiveFindingsResponse.from_boto(response)

    def create_detector(
        self,
        _request: shapes.CreateDetectorRequest = None,
        *,
        enable: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDetectorResponse:
        """
        Creates a single Amazon GuardDuty detector. A detector is an object that
        represents the GuardDuty service. A detector must be created in order for
        GuardDuty to become operational.
        """
        if _request is None:
            _params = {}
            if enable is not ShapeBase.NOT_SET:
                _params['enable'] = enable
            _request = shapes.CreateDetectorRequest(**_params)
        response = self._boto_client.create_detector(**_request.to_boto())

        return shapes.CreateDetectorResponse.from_boto(response)

    def create_filter(
        self,
        _request: shapes.CreateFilterRequest = None,
        *,
        detector_id: str,
        action: typing.Union[str, shapes.FilterAction] = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        finding_criteria: shapes.FindingCriteria = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        rank: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateFilterResponse:
        """
        Creates a filter using the specified finding criteria.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if action is not ShapeBase.NOT_SET:
                _params['action'] = action
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if finding_criteria is not ShapeBase.NOT_SET:
                _params['finding_criteria'] = finding_criteria
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if rank is not ShapeBase.NOT_SET:
                _params['rank'] = rank
            _request = shapes.CreateFilterRequest(**_params)
        response = self._boto_client.create_filter(**_request.to_boto())

        return shapes.CreateFilterResponse.from_boto(response)

    def create_ip_set(
        self,
        _request: shapes.CreateIPSetRequest = None,
        *,
        detector_id: str,
        activate: bool = ShapeBase.NOT_SET,
        format: typing.Union[str, shapes.IpSetFormat] = ShapeBase.NOT_SET,
        location: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateIPSetResponse:
        """
        Creates a new IPSet - a list of trusted IP addresses that have been whitelisted
        for secure communication with AWS infrastructure and applications.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if activate is not ShapeBase.NOT_SET:
                _params['activate'] = activate
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateIPSetRequest(**_params)
        response = self._boto_client.create_ip_set(**_request.to_boto())

        return shapes.CreateIPSetResponse.from_boto(response)

    def create_members(
        self,
        _request: shapes.CreateMembersRequest = None,
        *,
        detector_id: str,
        account_details: typing.List[shapes.AccountDetail] = ShapeBase.NOT_SET,
    ) -> shapes.CreateMembersResponse:
        """
        Creates member accounts of the current AWS account by specifying a list of AWS
        account IDs. The current AWS account can then invite these members to manage
        GuardDuty in their accounts.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_details is not ShapeBase.NOT_SET:
                _params['account_details'] = account_details
            _request = shapes.CreateMembersRequest(**_params)
        response = self._boto_client.create_members(**_request.to_boto())

        return shapes.CreateMembersResponse.from_boto(response)

    def create_sample_findings(
        self,
        _request: shapes.CreateSampleFindingsRequest = None,
        *,
        detector_id: str,
        finding_types: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateSampleFindingsResponse:
        """
        Generates example findings of types specified by the list of finding types. If
        'NULL' is specified for findingTypes, the API generates example findings of all
        supported finding types.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if finding_types is not ShapeBase.NOT_SET:
                _params['finding_types'] = finding_types
            _request = shapes.CreateSampleFindingsRequest(**_params)
        response = self._boto_client.create_sample_findings(
            **_request.to_boto()
        )

        return shapes.CreateSampleFindingsResponse.from_boto(response)

    def create_threat_intel_set(
        self,
        _request: shapes.CreateThreatIntelSetRequest = None,
        *,
        detector_id: str,
        activate: bool = ShapeBase.NOT_SET,
        format: typing.Union[str, shapes.ThreatIntelSetFormat] = ShapeBase.
        NOT_SET,
        location: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateThreatIntelSetResponse:
        """
        Create a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP
        addresses. GuardDuty generates findings based on ThreatIntelSets.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if activate is not ShapeBase.NOT_SET:
                _params['activate'] = activate
            if format is not ShapeBase.NOT_SET:
                _params['format'] = format
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateThreatIntelSetRequest(**_params)
        response = self._boto_client.create_threat_intel_set(
            **_request.to_boto()
        )

        return shapes.CreateThreatIntelSetResponse.from_boto(response)

    def decline_invitations(
        self,
        _request: shapes.DeclineInvitationsRequest = None,
        *,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DeclineInvitationsResponse:
        """
        Declines invitations sent to the current member account by AWS account specified
        by their account IDs.
        """
        if _request is None:
            _params = {}
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.DeclineInvitationsRequest(**_params)
        response = self._boto_client.decline_invitations(**_request.to_boto())

        return shapes.DeclineInvitationsResponse.from_boto(response)

    def delete_detector(
        self,
        _request: shapes.DeleteDetectorRequest = None,
        *,
        detector_id: str,
    ) -> shapes.DeleteDetectorResponse:
        """
        Deletes a Amazon GuardDuty detector specified by the detector ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            _request = shapes.DeleteDetectorRequest(**_params)
        response = self._boto_client.delete_detector(**_request.to_boto())

        return shapes.DeleteDetectorResponse.from_boto(response)

    def delete_filter(
        self,
        _request: shapes.DeleteFilterRequest = None,
        *,
        detector_id: str,
        filter_name: str,
    ) -> shapes.DeleteFilterResponse:
        """
        Deletes the filter specified by the filter name.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            _request = shapes.DeleteFilterRequest(**_params)
        response = self._boto_client.delete_filter(**_request.to_boto())

        return shapes.DeleteFilterResponse.from_boto(response)

    def delete_ip_set(
        self,
        _request: shapes.DeleteIPSetRequest = None,
        *,
        detector_id: str,
        ip_set_id: str,
    ) -> shapes.DeleteIPSetResponse:
        """
        Deletes the IPSet specified by the IPSet ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if ip_set_id is not ShapeBase.NOT_SET:
                _params['ip_set_id'] = ip_set_id
            _request = shapes.DeleteIPSetRequest(**_params)
        response = self._boto_client.delete_ip_set(**_request.to_boto())

        return shapes.DeleteIPSetResponse.from_boto(response)

    def delete_invitations(
        self,
        _request: shapes.DeleteInvitationsRequest = None,
        *,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DeleteInvitationsResponse:
        """
        Deletes invitations sent to the current member account by AWS accounts specified
        by their account IDs.
        """
        if _request is None:
            _params = {}
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.DeleteInvitationsRequest(**_params)
        response = self._boto_client.delete_invitations(**_request.to_boto())

        return shapes.DeleteInvitationsResponse.from_boto(response)

    def delete_members(
        self,
        _request: shapes.DeleteMembersRequest = None,
        *,
        detector_id: str,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DeleteMembersResponse:
        """
        Deletes GuardDuty member accounts (to the current GuardDuty master account)
        specified by the account IDs.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.DeleteMembersRequest(**_params)
        response = self._boto_client.delete_members(**_request.to_boto())

        return shapes.DeleteMembersResponse.from_boto(response)

    def delete_threat_intel_set(
        self,
        _request: shapes.DeleteThreatIntelSetRequest = None,
        *,
        detector_id: str,
        threat_intel_set_id: str,
    ) -> shapes.DeleteThreatIntelSetResponse:
        """
        Deletes ThreatIntelSet specified by the ThreatIntelSet ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if threat_intel_set_id is not ShapeBase.NOT_SET:
                _params['threat_intel_set_id'] = threat_intel_set_id
            _request = shapes.DeleteThreatIntelSetRequest(**_params)
        response = self._boto_client.delete_threat_intel_set(
            **_request.to_boto()
        )

        return shapes.DeleteThreatIntelSetResponse.from_boto(response)

    def disassociate_from_master_account(
        self,
        _request: shapes.DisassociateFromMasterAccountRequest = None,
        *,
        detector_id: str,
    ) -> shapes.DisassociateFromMasterAccountResponse:
        """
        Disassociates the current GuardDuty member account from its master account.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            _request = shapes.DisassociateFromMasterAccountRequest(**_params)
        response = self._boto_client.disassociate_from_master_account(
            **_request.to_boto()
        )

        return shapes.DisassociateFromMasterAccountResponse.from_boto(response)

    def disassociate_members(
        self,
        _request: shapes.DisassociateMembersRequest = None,
        *,
        detector_id: str,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateMembersResponse:
        """
        Disassociates GuardDuty member accounts (to the current GuardDuty master
        account) specified by the account IDs.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.DisassociateMembersRequest(**_params)
        response = self._boto_client.disassociate_members(**_request.to_boto())

        return shapes.DisassociateMembersResponse.from_boto(response)

    def get_detector(
        self,
        _request: shapes.GetDetectorRequest = None,
        *,
        detector_id: str,
    ) -> shapes.GetDetectorResponse:
        """
        Retrieves an Amazon GuardDuty detector specified by the detectorId.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            _request = shapes.GetDetectorRequest(**_params)
        response = self._boto_client.get_detector(**_request.to_boto())

        return shapes.GetDetectorResponse.from_boto(response)

    def get_filter(
        self,
        _request: shapes.GetFilterRequest = None,
        *,
        detector_id: str,
        filter_name: str,
    ) -> shapes.GetFilterResponse:
        """
        Returns the details of the filter specified by the filter name.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            _request = shapes.GetFilterRequest(**_params)
        response = self._boto_client.get_filter(**_request.to_boto())

        return shapes.GetFilterResponse.from_boto(response)

    def get_findings(
        self,
        _request: shapes.GetFindingsRequest = None,
        *,
        detector_id: str,
        finding_ids: typing.List[str] = ShapeBase.NOT_SET,
        sort_criteria: shapes.SortCriteria = ShapeBase.NOT_SET,
    ) -> shapes.GetFindingsResponse:
        """
        Describes Amazon GuardDuty findings specified by finding IDs.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if finding_ids is not ShapeBase.NOT_SET:
                _params['finding_ids'] = finding_ids
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.GetFindingsRequest(**_params)
        response = self._boto_client.get_findings(**_request.to_boto())

        return shapes.GetFindingsResponse.from_boto(response)

    def get_findings_statistics(
        self,
        _request: shapes.GetFindingsStatisticsRequest = None,
        *,
        detector_id: str,
        finding_criteria: shapes.FindingCriteria = ShapeBase.NOT_SET,
        finding_statistic_types: typing.List[
            typing.Union[str, shapes.FindingStatisticType]] = ShapeBase.NOT_SET,
    ) -> shapes.GetFindingsStatisticsResponse:
        """
        Lists Amazon GuardDuty findings' statistics for the specified detector ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if finding_criteria is not ShapeBase.NOT_SET:
                _params['finding_criteria'] = finding_criteria
            if finding_statistic_types is not ShapeBase.NOT_SET:
                _params['finding_statistic_types'] = finding_statistic_types
            _request = shapes.GetFindingsStatisticsRequest(**_params)
        response = self._boto_client.get_findings_statistics(
            **_request.to_boto()
        )

        return shapes.GetFindingsStatisticsResponse.from_boto(response)

    def get_ip_set(
        self,
        _request: shapes.GetIPSetRequest = None,
        *,
        detector_id: str,
        ip_set_id: str,
    ) -> shapes.GetIPSetResponse:
        """
        Retrieves the IPSet specified by the IPSet ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if ip_set_id is not ShapeBase.NOT_SET:
                _params['ip_set_id'] = ip_set_id
            _request = shapes.GetIPSetRequest(**_params)
        response = self._boto_client.get_ip_set(**_request.to_boto())

        return shapes.GetIPSetResponse.from_boto(response)

    def get_invitations_count(
        self,
        _request: shapes.GetInvitationsCountRequest = None,
    ) -> shapes.GetInvitationsCountResponse:
        """
        Returns the count of all GuardDuty membership invitations that were sent to the
        current member account except the currently accepted invitation.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetInvitationsCountRequest(**_params)
        response = self._boto_client.get_invitations_count(**_request.to_boto())

        return shapes.GetInvitationsCountResponse.from_boto(response)

    def get_master_account(
        self,
        _request: shapes.GetMasterAccountRequest = None,
        *,
        detector_id: str,
    ) -> shapes.GetMasterAccountResponse:
        """
        Provides the details for the GuardDuty master account to the current GuardDuty
        member account.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            _request = shapes.GetMasterAccountRequest(**_params)
        response = self._boto_client.get_master_account(**_request.to_boto())

        return shapes.GetMasterAccountResponse.from_boto(response)

    def get_members(
        self,
        _request: shapes.GetMembersRequest = None,
        *,
        detector_id: str,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GetMembersResponse:
        """
        Retrieves GuardDuty member accounts (to the current GuardDuty master account)
        specified by the account IDs.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.GetMembersRequest(**_params)
        response = self._boto_client.get_members(**_request.to_boto())

        return shapes.GetMembersResponse.from_boto(response)

    def get_threat_intel_set(
        self,
        _request: shapes.GetThreatIntelSetRequest = None,
        *,
        detector_id: str,
        threat_intel_set_id: str,
    ) -> shapes.GetThreatIntelSetResponse:
        """
        Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if threat_intel_set_id is not ShapeBase.NOT_SET:
                _params['threat_intel_set_id'] = threat_intel_set_id
            _request = shapes.GetThreatIntelSetRequest(**_params)
        response = self._boto_client.get_threat_intel_set(**_request.to_boto())

        return shapes.GetThreatIntelSetResponse.from_boto(response)

    def invite_members(
        self,
        _request: shapes.InviteMembersRequest = None,
        *,
        detector_id: str,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
        disable_email_notification: bool = ShapeBase.NOT_SET,
        message: str = ShapeBase.NOT_SET,
    ) -> shapes.InviteMembersResponse:
        """
        Invites other AWS accounts (created as members of the current AWS account by
        CreateMembers) to enable GuardDuty and allow the current AWS account to view and
        manage these accounts' GuardDuty findings on their behalf as the master account.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            if disable_email_notification is not ShapeBase.NOT_SET:
                _params['disable_email_notification'
                       ] = disable_email_notification
            if message is not ShapeBase.NOT_SET:
                _params['message'] = message
            _request = shapes.InviteMembersRequest(**_params)
        response = self._boto_client.invite_members(**_request.to_boto())

        return shapes.InviteMembersResponse.from_boto(response)

    def list_detectors(
        self,
        _request: shapes.ListDetectorsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDetectorsResponse:
        """
        Lists detectorIds of all the existing Amazon GuardDuty detector resources.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDetectorsRequest(**_params)
        paginator = self.get_paginator("list_detectors").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDetectorsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDetectorsResponse.from_boto(response)

    def list_filters(
        self,
        _request: shapes.ListFiltersRequest = None,
        *,
        detector_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFiltersResponse:
        """
        Returns a paginated list of the current filters.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListFiltersRequest(**_params)
        paginator = self.get_paginator("list_filters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListFiltersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListFiltersResponse.from_boto(response)

    def list_findings(
        self,
        _request: shapes.ListFindingsRequest = None,
        *,
        detector_id: str,
        finding_criteria: shapes.FindingCriteria = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        sort_criteria: shapes.SortCriteria = ShapeBase.NOT_SET,
    ) -> shapes.ListFindingsResponse:
        """
        Lists Amazon GuardDuty findings for the specified detector ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if finding_criteria is not ShapeBase.NOT_SET:
                _params['finding_criteria'] = finding_criteria
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_criteria is not ShapeBase.NOT_SET:
                _params['sort_criteria'] = sort_criteria
            _request = shapes.ListFindingsRequest(**_params)
        paginator = self.get_paginator("list_findings").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListFindingsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListFindingsResponse.from_boto(response)

    def list_ip_sets(
        self,
        _request: shapes.ListIPSetsRequest = None,
        *,
        detector_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListIPSetsResponse:
        """
        Lists the IPSets of the GuardDuty service specified by the detector ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListIPSetsRequest(**_params)
        paginator = self.get_paginator("list_ip_sets").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListIPSetsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListIPSetsResponse.from_boto(response)

    def list_invitations(
        self,
        _request: shapes.ListInvitationsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInvitationsResponse:
        """
        Lists all GuardDuty membership invitations that were sent to the current AWS
        account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListInvitationsRequest(**_params)
        paginator = self.get_paginator("list_invitations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInvitationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInvitationsResponse.from_boto(response)

    def list_members(
        self,
        _request: shapes.ListMembersRequest = None,
        *,
        detector_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        only_associated: str = ShapeBase.NOT_SET,
    ) -> shapes.ListMembersResponse:
        """
        Lists details about all member accounts for the current GuardDuty master
        account.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if only_associated is not ShapeBase.NOT_SET:
                _params['only_associated'] = only_associated
            _request = shapes.ListMembersRequest(**_params)
        paginator = self.get_paginator("list_members").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListMembersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListMembersResponse.from_boto(response)

    def list_threat_intel_sets(
        self,
        _request: shapes.ListThreatIntelSetsRequest = None,
        *,
        detector_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListThreatIntelSetsResponse:
        """
        Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListThreatIntelSetsRequest(**_params)
        paginator = self.get_paginator("list_threat_intel_sets").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListThreatIntelSetsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListThreatIntelSetsResponse.from_boto(response)

    def start_monitoring_members(
        self,
        _request: shapes.StartMonitoringMembersRequest = None,
        *,
        detector_id: str,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.StartMonitoringMembersResponse:
        """
        Re-enables GuardDuty to monitor findings of the member accounts specified by the
        account IDs. A master GuardDuty account can run this command after disabling
        GuardDuty from monitoring these members' findings by running
        StopMonitoringMembers.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.StartMonitoringMembersRequest(**_params)
        response = self._boto_client.start_monitoring_members(
            **_request.to_boto()
        )

        return shapes.StartMonitoringMembersResponse.from_boto(response)

    def stop_monitoring_members(
        self,
        _request: shapes.StopMonitoringMembersRequest = None,
        *,
        detector_id: str,
        account_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.StopMonitoringMembersResponse:
        """
        Disables GuardDuty from monitoring findings of the member accounts specified by
        the account IDs. After running this command, a master GuardDuty account can run
        StartMonitoringMembers to re-enable GuardDuty to monitor these members’
        findings.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if account_ids is not ShapeBase.NOT_SET:
                _params['account_ids'] = account_ids
            _request = shapes.StopMonitoringMembersRequest(**_params)
        response = self._boto_client.stop_monitoring_members(
            **_request.to_boto()
        )

        return shapes.StopMonitoringMembersResponse.from_boto(response)

    def unarchive_findings(
        self,
        _request: shapes.UnarchiveFindingsRequest = None,
        *,
        detector_id: str,
        finding_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UnarchiveFindingsResponse:
        """
        Unarchives Amazon GuardDuty findings specified by the list of finding IDs.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if finding_ids is not ShapeBase.NOT_SET:
                _params['finding_ids'] = finding_ids
            _request = shapes.UnarchiveFindingsRequest(**_params)
        response = self._boto_client.unarchive_findings(**_request.to_boto())

        return shapes.UnarchiveFindingsResponse.from_boto(response)

    def update_detector(
        self,
        _request: shapes.UpdateDetectorRequest = None,
        *,
        detector_id: str,
        enable: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDetectorResponse:
        """
        Updates an Amazon GuardDuty detector specified by the detectorId.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if enable is not ShapeBase.NOT_SET:
                _params['enable'] = enable
            _request = shapes.UpdateDetectorRequest(**_params)
        response = self._boto_client.update_detector(**_request.to_boto())

        return shapes.UpdateDetectorResponse.from_boto(response)

    def update_filter(
        self,
        _request: shapes.UpdateFilterRequest = None,
        *,
        detector_id: str,
        filter_name: str,
        action: typing.Union[str, shapes.FilterAction] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        finding_criteria: shapes.FindingCriteria = ShapeBase.NOT_SET,
        rank: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFilterResponse:
        """
        Updates the filter specified by the filter name.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            if action is not ShapeBase.NOT_SET:
                _params['action'] = action
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if finding_criteria is not ShapeBase.NOT_SET:
                _params['finding_criteria'] = finding_criteria
            if rank is not ShapeBase.NOT_SET:
                _params['rank'] = rank
            _request = shapes.UpdateFilterRequest(**_params)
        response = self._boto_client.update_filter(**_request.to_boto())

        return shapes.UpdateFilterResponse.from_boto(response)

    def update_findings_feedback(
        self,
        _request: shapes.UpdateFindingsFeedbackRequest = None,
        *,
        detector_id: str,
        comments: str = ShapeBase.NOT_SET,
        feedback: typing.Union[str, shapes.Feedback] = ShapeBase.NOT_SET,
        finding_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFindingsFeedbackResponse:
        """
        Marks specified Amazon GuardDuty findings as useful or not useful.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if comments is not ShapeBase.NOT_SET:
                _params['comments'] = comments
            if feedback is not ShapeBase.NOT_SET:
                _params['feedback'] = feedback
            if finding_ids is not ShapeBase.NOT_SET:
                _params['finding_ids'] = finding_ids
            _request = shapes.UpdateFindingsFeedbackRequest(**_params)
        response = self._boto_client.update_findings_feedback(
            **_request.to_boto()
        )

        return shapes.UpdateFindingsFeedbackResponse.from_boto(response)

    def update_ip_set(
        self,
        _request: shapes.UpdateIPSetRequest = None,
        *,
        detector_id: str,
        ip_set_id: str,
        activate: bool = ShapeBase.NOT_SET,
        location: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateIPSetResponse:
        """
        Updates the IPSet specified by the IPSet ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if ip_set_id is not ShapeBase.NOT_SET:
                _params['ip_set_id'] = ip_set_id
            if activate is not ShapeBase.NOT_SET:
                _params['activate'] = activate
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateIPSetRequest(**_params)
        response = self._boto_client.update_ip_set(**_request.to_boto())

        return shapes.UpdateIPSetResponse.from_boto(response)

    def update_threat_intel_set(
        self,
        _request: shapes.UpdateThreatIntelSetRequest = None,
        *,
        detector_id: str,
        threat_intel_set_id: str,
        activate: bool = ShapeBase.NOT_SET,
        location: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateThreatIntelSetResponse:
        """
        Updates the ThreatIntelSet specified by ThreatIntelSet ID.
        """
        if _request is None:
            _params = {}
            if detector_id is not ShapeBase.NOT_SET:
                _params['detector_id'] = detector_id
            if threat_intel_set_id is not ShapeBase.NOT_SET:
                _params['threat_intel_set_id'] = threat_intel_set_id
            if activate is not ShapeBase.NOT_SET:
                _params['activate'] = activate
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateThreatIntelSetRequest(**_params)
        response = self._boto_client.update_threat_intel_set(
            **_request.to_boto()
        )

        return shapes.UpdateThreatIntelSetResponse.from_boto(response)
