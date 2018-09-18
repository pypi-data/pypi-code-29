import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("support", *args, **kwargs)

    def add_attachments_to_set(
        self,
        _request: shapes.AddAttachmentsToSetRequest = None,
        *,
        attachments: typing.List[shapes.Attachment],
        attachment_set_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AddAttachmentsToSetResponse:
        """
        Adds one or more attachments to an attachment set. If an `attachmentSetId` is
        not specified, a new attachment set is created, and the ID of the set is
        returned in the response. If an `attachmentSetId` is specified, the attachments
        are added to the specified set, if it exists.

        An attachment set is a temporary container for attachments that are to be added
        to a case or case communication. The set is available for one hour after it is
        created; the `expiryTime` returned in the response indicates when the set
        expires. The maximum number of attachments in a set is 3, and the maximum size
        of any attachment in the set is 5 MB.
        """
        if _request is None:
            _params = {}
            if attachments is not ShapeBase.NOT_SET:
                _params['attachments'] = attachments
            if attachment_set_id is not ShapeBase.NOT_SET:
                _params['attachment_set_id'] = attachment_set_id
            _request = shapes.AddAttachmentsToSetRequest(**_params)
        response = self._boto_client.add_attachments_to_set(
            **_request.to_boto()
        )

        return shapes.AddAttachmentsToSetResponse.from_boto(response)

    def add_communication_to_case(
        self,
        _request: shapes.AddCommunicationToCaseRequest = None,
        *,
        communication_body: str,
        case_id: str = ShapeBase.NOT_SET,
        cc_email_addresses: typing.List[str] = ShapeBase.NOT_SET,
        attachment_set_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AddCommunicationToCaseResponse:
        """
        Adds additional customer communication to an AWS Support case. You use the
        `caseId` value to identify the case to add communication to. You can list a set
        of email addresses to copy on the communication using the `ccEmailAddresses`
        value. The `communicationBody` value contains the text of the communication.

        The response indicates the success or failure of the request.

        This operation implements a subset of the features of the AWS Support Center.
        """
        if _request is None:
            _params = {}
            if communication_body is not ShapeBase.NOT_SET:
                _params['communication_body'] = communication_body
            if case_id is not ShapeBase.NOT_SET:
                _params['case_id'] = case_id
            if cc_email_addresses is not ShapeBase.NOT_SET:
                _params['cc_email_addresses'] = cc_email_addresses
            if attachment_set_id is not ShapeBase.NOT_SET:
                _params['attachment_set_id'] = attachment_set_id
            _request = shapes.AddCommunicationToCaseRequest(**_params)
        response = self._boto_client.add_communication_to_case(
            **_request.to_boto()
        )

        return shapes.AddCommunicationToCaseResponse.from_boto(response)

    def create_case(
        self,
        _request: shapes.CreateCaseRequest = None,
        *,
        subject: str,
        communication_body: str,
        service_code: str = ShapeBase.NOT_SET,
        severity_code: str = ShapeBase.NOT_SET,
        category_code: str = ShapeBase.NOT_SET,
        cc_email_addresses: typing.List[str] = ShapeBase.NOT_SET,
        language: str = ShapeBase.NOT_SET,
        issue_type: str = ShapeBase.NOT_SET,
        attachment_set_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCaseResponse:
        """
        Creates a new case in the AWS Support Center. This operation is modeled on the
        behavior of the AWS Support Center [Create
        Case](https://console.aws.amazon.com/support/home#/case/create) page. Its
        parameters require you to specify the following information:

          * **issueType.** The type of issue for the case. You can specify either "customer-service" or "technical." If you do not indicate a value, the default is "technical." 

          * **serviceCode.** The code for an AWS service. You obtain the `serviceCode` by calling DescribeServices. 

          * **categoryCode.** The category for the service defined for the `serviceCode` value. You also obtain the category code for a service by calling DescribeServices. Each AWS service defines its own set of category codes. 

          * **severityCode.** A value that indicates the urgency of the case, which in turn determines the response time according to your service level agreement with AWS Support. You obtain the SeverityCode by calling DescribeSeverityLevels.

          * **subject.** The **Subject** field on the AWS Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.

          * **communicationBody.** The **Description** field on the AWS Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.

          * **attachmentSetId.** The ID of a set of attachments that has been created by using AddAttachmentsToSet.

          * **language.** The human language in which AWS Support handles the case. English and Japanese are currently supported.

          * **ccEmailAddresses.** The AWS Support Center **CC** field on the [Create Case](https://console.aws.amazon.com/support/home#/case/create) page. You can list email addresses to be copied on any correspondence about the case. The account that opens the case is already identified by passing the AWS Credentials in the HTTP POST method or in a method or function call from one of the programming languages supported by an [AWS SDK](http://aws.amazon.com/tools/). 

        To add additional communication or attachments to an existing case, use
        AddCommunicationToCase.

        A successful CreateCase request returns an AWS Support case number. Case numbers
        are used by the DescribeCases operation to retrieve existing AWS Support cases.
        """
        if _request is None:
            _params = {}
            if subject is not ShapeBase.NOT_SET:
                _params['subject'] = subject
            if communication_body is not ShapeBase.NOT_SET:
                _params['communication_body'] = communication_body
            if service_code is not ShapeBase.NOT_SET:
                _params['service_code'] = service_code
            if severity_code is not ShapeBase.NOT_SET:
                _params['severity_code'] = severity_code
            if category_code is not ShapeBase.NOT_SET:
                _params['category_code'] = category_code
            if cc_email_addresses is not ShapeBase.NOT_SET:
                _params['cc_email_addresses'] = cc_email_addresses
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            if issue_type is not ShapeBase.NOT_SET:
                _params['issue_type'] = issue_type
            if attachment_set_id is not ShapeBase.NOT_SET:
                _params['attachment_set_id'] = attachment_set_id
            _request = shapes.CreateCaseRequest(**_params)
        response = self._boto_client.create_case(**_request.to_boto())

        return shapes.CreateCaseResponse.from_boto(response)

    def describe_attachment(
        self,
        _request: shapes.DescribeAttachmentRequest = None,
        *,
        attachment_id: str,
    ) -> shapes.DescribeAttachmentResponse:
        """
        Returns the attachment that has the specified ID. Attachment IDs are generated
        by the case management system when you add an attachment to a case or case
        communication. Attachment IDs are returned in the AttachmentDetails objects that
        are returned by the DescribeCommunications operation.
        """
        if _request is None:
            _params = {}
            if attachment_id is not ShapeBase.NOT_SET:
                _params['attachment_id'] = attachment_id
            _request = shapes.DescribeAttachmentRequest(**_params)
        response = self._boto_client.describe_attachment(**_request.to_boto())

        return shapes.DescribeAttachmentResponse.from_boto(response)

    def describe_cases(
        self,
        _request: shapes.DescribeCasesRequest = None,
        *,
        case_id_list: typing.List[str] = ShapeBase.NOT_SET,
        display_id: str = ShapeBase.NOT_SET,
        after_time: str = ShapeBase.NOT_SET,
        before_time: str = ShapeBase.NOT_SET,
        include_resolved_cases: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        language: str = ShapeBase.NOT_SET,
        include_communications: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCasesResponse:
        """
        Returns a list of cases that you specify by passing one or more case IDs. In
        addition, you can filter the cases by date by setting values for the `afterTime`
        and `beforeTime` request parameters. You can set values for the
        `includeResolvedCases` and `includeCommunications` request parameters to control
        how much information is returned.

        Case data is available for 12 months after creation. If a case was created more
        than 12 months ago, a request for data might cause an error.

        The response returns the following in JSON format:

          * One or more CaseDetails data types. 

          * One or more `nextToken` values, which specify where to paginate the returned records represented by the `CaseDetails` objects.
        """
        if _request is None:
            _params = {}
            if case_id_list is not ShapeBase.NOT_SET:
                _params['case_id_list'] = case_id_list
            if display_id is not ShapeBase.NOT_SET:
                _params['display_id'] = display_id
            if after_time is not ShapeBase.NOT_SET:
                _params['after_time'] = after_time
            if before_time is not ShapeBase.NOT_SET:
                _params['before_time'] = before_time
            if include_resolved_cases is not ShapeBase.NOT_SET:
                _params['include_resolved_cases'] = include_resolved_cases
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            if include_communications is not ShapeBase.NOT_SET:
                _params['include_communications'] = include_communications
            _request = shapes.DescribeCasesRequest(**_params)
        paginator = self.get_paginator("describe_cases").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeCasesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeCasesResponse.from_boto(response)

    def describe_communications(
        self,
        _request: shapes.DescribeCommunicationsRequest = None,
        *,
        case_id: str,
        before_time: str = ShapeBase.NOT_SET,
        after_time: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCommunicationsResponse:
        """
        Returns communications (and attachments) for one or more support cases. You can
        use the `afterTime` and `beforeTime` parameters to filter by date. You can use
        the `caseId` parameter to restrict the results to a particular case.

        Case data is available for 12 months after creation. If a case was created more
        than 12 months ago, a request for data might cause an error.

        You can use the `maxResults` and `nextToken` parameters to control the
        pagination of the result set. Set `maxResults` to the number of cases you want
        displayed on each page, and use `nextToken` to specify the resumption of
        pagination.
        """
        if _request is None:
            _params = {}
            if case_id is not ShapeBase.NOT_SET:
                _params['case_id'] = case_id
            if before_time is not ShapeBase.NOT_SET:
                _params['before_time'] = before_time
            if after_time is not ShapeBase.NOT_SET:
                _params['after_time'] = after_time
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeCommunicationsRequest(**_params)
        paginator = self.get_paginator("describe_communications").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeCommunicationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeCommunicationsResponse.from_boto(response)

    def describe_services(
        self,
        _request: shapes.DescribeServicesRequest = None,
        *,
        service_code_list: typing.List[str] = ShapeBase.NOT_SET,
        language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeServicesResponse:
        """
        Returns the current list of AWS services and a list of service categories that
        applies to each one. You then use service names and categories in your
        CreateCase requests. Each AWS service has its own set of categories.

        The service codes and category codes correspond to the values that are displayed
        in the **Service** and **Category** drop-down lists on the AWS Support Center
        [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.
        The values in those fields, however, do not necessarily match the service codes
        and categories returned by the `DescribeServices` request. Always use the
        service codes and categories obtained programmatically. This practice ensures
        that you always have the most recent set of service and category codes.
        """
        if _request is None:
            _params = {}
            if service_code_list is not ShapeBase.NOT_SET:
                _params['service_code_list'] = service_code_list
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            _request = shapes.DescribeServicesRequest(**_params)
        response = self._boto_client.describe_services(**_request.to_boto())

        return shapes.DescribeServicesResponse.from_boto(response)

    def describe_severity_levels(
        self,
        _request: shapes.DescribeSeverityLevelsRequest = None,
        *,
        language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSeverityLevelsResponse:
        """
        Returns the list of severity levels that you can assign to an AWS Support case.
        The severity level for a case is also a field in the CaseDetails data type
        included in any CreateCase request.
        """
        if _request is None:
            _params = {}
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            _request = shapes.DescribeSeverityLevelsRequest(**_params)
        response = self._boto_client.describe_severity_levels(
            **_request.to_boto()
        )

        return shapes.DescribeSeverityLevelsResponse.from_boto(response)

    def describe_trusted_advisor_check_refresh_statuses(
        self,
        _request: shapes.
        DescribeTrustedAdvisorCheckRefreshStatusesRequest = None,
        *,
        check_ids: typing.List[str],
    ) -> shapes.DescribeTrustedAdvisorCheckRefreshStatusesResponse:
        """
        Returns the refresh status of the Trusted Advisor checks that have the specified
        check IDs. Check IDs can be obtained by calling DescribeTrustedAdvisorChecks.

        Some checks are refreshed automatically, and their refresh statuses cannot be
        retrieved by using this operation. Use of the
        `DescribeTrustedAdvisorCheckRefreshStatuses` operation for these checks causes
        an `InvalidParameterValue` error.
        """
        if _request is None:
            _params = {}
            if check_ids is not ShapeBase.NOT_SET:
                _params['check_ids'] = check_ids
            _request = shapes.DescribeTrustedAdvisorCheckRefreshStatusesRequest(
                **_params
            )
        response = self._boto_client.describe_trusted_advisor_check_refresh_statuses(
            **_request.to_boto()
        )

        return shapes.DescribeTrustedAdvisorCheckRefreshStatusesResponse.from_boto(
            response
        )

    def describe_trusted_advisor_check_result(
        self,
        _request: shapes.DescribeTrustedAdvisorCheckResultRequest = None,
        *,
        check_id: str,
        language: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTrustedAdvisorCheckResultResponse:
        """
        Returns the results of the Trusted Advisor check that has the specified check
        ID. Check IDs can be obtained by calling DescribeTrustedAdvisorChecks.

        The response contains a TrustedAdvisorCheckResult object, which contains these
        three objects:

          * TrustedAdvisorCategorySpecificSummary

          * TrustedAdvisorResourceDetail

          * TrustedAdvisorResourcesSummary

        In addition, the response contains these fields:

          * **status.** The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not_available".

          * **timestamp.** The time of the last refresh of the check.

          * **checkId.** The unique identifier for the check.
        """
        if _request is None:
            _params = {}
            if check_id is not ShapeBase.NOT_SET:
                _params['check_id'] = check_id
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            _request = shapes.DescribeTrustedAdvisorCheckResultRequest(
                **_params
            )
        response = self._boto_client.describe_trusted_advisor_check_result(
            **_request.to_boto()
        )

        return shapes.DescribeTrustedAdvisorCheckResultResponse.from_boto(
            response
        )

    def describe_trusted_advisor_check_summaries(
        self,
        _request: shapes.DescribeTrustedAdvisorCheckSummariesRequest = None,
        *,
        check_ids: typing.List[str],
    ) -> shapes.DescribeTrustedAdvisorCheckSummariesResponse:
        """
        Returns the summaries of the results of the Trusted Advisor checks that have the
        specified check IDs. Check IDs can be obtained by calling
        DescribeTrustedAdvisorChecks.

        The response contains an array of TrustedAdvisorCheckSummary objects.
        """
        if _request is None:
            _params = {}
            if check_ids is not ShapeBase.NOT_SET:
                _params['check_ids'] = check_ids
            _request = shapes.DescribeTrustedAdvisorCheckSummariesRequest(
                **_params
            )
        response = self._boto_client.describe_trusted_advisor_check_summaries(
            **_request.to_boto()
        )

        return shapes.DescribeTrustedAdvisorCheckSummariesResponse.from_boto(
            response
        )

    def describe_trusted_advisor_checks(
        self,
        _request: shapes.DescribeTrustedAdvisorChecksRequest = None,
        *,
        language: str,
    ) -> shapes.DescribeTrustedAdvisorChecksResponse:
        """
        Returns information about all available Trusted Advisor checks, including name,
        ID, category, description, and metadata. You must specify a language code;
        English ("en") and Japanese ("ja") are currently supported. The response
        contains a TrustedAdvisorCheckDescription for each check.
        """
        if _request is None:
            _params = {}
            if language is not ShapeBase.NOT_SET:
                _params['language'] = language
            _request = shapes.DescribeTrustedAdvisorChecksRequest(**_params)
        response = self._boto_client.describe_trusted_advisor_checks(
            **_request.to_boto()
        )

        return shapes.DescribeTrustedAdvisorChecksResponse.from_boto(response)

    def refresh_trusted_advisor_check(
        self,
        _request: shapes.RefreshTrustedAdvisorCheckRequest = None,
        *,
        check_id: str,
    ) -> shapes.RefreshTrustedAdvisorCheckResponse:
        """
        Requests a refresh of the Trusted Advisor check that has the specified check ID.
        Check IDs can be obtained by calling DescribeTrustedAdvisorChecks.

        Some checks are refreshed automatically, and they cannot be refreshed by using
        this operation. Use of the `RefreshTrustedAdvisorCheck` operation for these
        checks causes an `InvalidParameterValue` error.

        The response contains a TrustedAdvisorCheckRefreshStatus object, which contains
        these fields:

          * **status.** The refresh status of the check: "none", "enqueued", "processing", "success", or "abandoned".

          * **millisUntilNextRefreshable.** The amount of time, in milliseconds, until the check is eligible for refresh.

          * **checkId.** The unique identifier for the check.
        """
        if _request is None:
            _params = {}
            if check_id is not ShapeBase.NOT_SET:
                _params['check_id'] = check_id
            _request = shapes.RefreshTrustedAdvisorCheckRequest(**_params)
        response = self._boto_client.refresh_trusted_advisor_check(
            **_request.to_boto()
        )

        return shapes.RefreshTrustedAdvisorCheckResponse.from_boto(response)

    def resolve_case(
        self,
        _request: shapes.ResolveCaseRequest = None,
        *,
        case_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ResolveCaseResponse:
        """
        Takes a `caseId` and returns the initial state of the case along with the state
        of the case after the call to ResolveCase completed.
        """
        if _request is None:
            _params = {}
            if case_id is not ShapeBase.NOT_SET:
                _params['case_id'] = case_id
            _request = shapes.ResolveCaseRequest(**_params)
        response = self._boto_client.resolve_case(**_request.to_boto())

        return shapes.ResolveCaseResponse.from_boto(response)
