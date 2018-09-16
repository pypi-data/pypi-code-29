import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddAttachmentsToSetRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachments",
                "attachments",
                TypeInfo(typing.List[Attachment]),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                TypeInfo(str),
            ),
        ]

    # One or more attachments to add to the set. The limit is 3 attachments per
    # set, and the size limit is 5 MB per attachment.
    attachments: typing.List["Attachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the attachment set. If an `attachmentSetId` is not specified, a
    # new attachment set is created, and the ID of the set is returned in the
    # response. If an `attachmentSetId` is specified, the attachments are added
    # to the specified set, if it exists.
    attachment_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddAttachmentsToSetResponse(OutputShapeBase):
    """
    The ID and expiry time of the attachment set returned by the AddAttachmentsToSet
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                TypeInfo(str),
            ),
            (
                "expiry_time",
                "expiryTime",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the attachment set. If an `attachmentSetId` was not specified, a
    # new attachment set is created, and the ID of the set is returned in the
    # response. If an `attachmentSetId` was specified, the attachments are added
    # to the specified set, if it exists.
    attachment_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time and date when the attachment set expires.
    expiry_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddCommunicationToCaseRequest(ShapeBase):
    """
    To be written.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "communication_body",
                "communicationBody",
                TypeInfo(str),
            ),
            (
                "case_id",
                "caseId",
                TypeInfo(str),
            ),
            (
                "cc_email_addresses",
                "ccEmailAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                TypeInfo(str),
            ),
        ]

    # The body of an email communication to add to the support case.
    communication_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email addresses in the CC line of an email to be added to the support
    # case.
    cc_email_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of a set of one or more attachments for the communication to add to
    # the case. Create the set by calling AddAttachmentsToSet
    attachment_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddCommunicationToCaseResponse(OutputShapeBase):
    """
    The result of the AddCommunicationToCase operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result",
                "result",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # True if AddCommunicationToCase succeeds. Otherwise, returns an error.
    result: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Attachment(ShapeBase):
    """
    An attachment to a case communication. The attachment consists of the file name
    and the content of the file.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "file_name",
                "fileName",
                TypeInfo(str),
            ),
            (
                "data",
                "data",
                TypeInfo(typing.Any),
            ),
        ]

    # The name of the attachment file.
    file_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the attachment file.
    data: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentDetails(ShapeBase):
    """
    The file name and ID of an attachment to a case communication. You can use the
    ID to retrieve the attachment with the DescribeAttachment operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_id",
                "attachmentId",
                TypeInfo(str),
            ),
            (
                "file_name",
                "fileName",
                TypeInfo(str),
            ),
        ]

    # The ID of the attachment.
    attachment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The file name of the attachment.
    file_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentIdNotFound(ShapeBase):
    """
    An attachment with the specified ID could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # An attachment with the specified ID could not be found.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentLimitExceeded(ShapeBase):
    """
    The limit for the number of attachment sets created in a short period of time
    has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The limit for the number of attachment sets created in a short period of
    # time has been exceeded.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentSetExpired(ShapeBase):
    """
    The expiration time of the attachment set has passed. The set expires 1 hour
    after it is created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The expiration time of the attachment set has passed. The set expires 1
    # hour after it is created.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentSetIdNotFound(ShapeBase):
    """
    An attachment set with the specified ID could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # An attachment set with the specified ID could not be found.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachmentSetSizeLimitExceeded(ShapeBase):
    """
    A limit for the size of an attachment set has been exceeded. The limits are 3
    attachments and 5 MB per attachment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # A limit for the size of an attachment set has been exceeded. The limits are
    # 3 attachments and 5 MB per attachment.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaseCreationLimitExceeded(ShapeBase):
    """
    The case creation limit for the account has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # An error message that indicates that you have exceeded the number of cases
    # you can have open.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaseDetails(ShapeBase):
    """
    A JSON-formatted object that contains the metadata for a support case. It is
    contained the response from a DescribeCases request. **CaseDetails** contains
    the following fields:

      * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case- _12345678910-2013-c4c1d2bf33c5cf47_.

      * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the CategoryCode values returned by a call to DescribeServices.

      * **displayId.** The identifier for the case on pages in the AWS Support Center.

      * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations that take them.

      * **recentCommunications.** One or more Communication objects. Fields of these objects are `attachments`, `body`, `caseId`, `submittedBy`, and `timeCreated`.

      * **nextToken.** A resumption point for pagination.

      * **serviceCode.** The identifier for the AWS service that corresponds to the service code defined in the call to DescribeServices.

      * **severityCode.** The severity code assigned to the case. Contains one of the values returned by the call to DescribeSeverityLevels.

      * **status.** The status of the case in the AWS Support Center.

      * **subject.** The subject line of the case.

      * **submittedBy.** The email address of the account that submitted the case.

      * **timeCreated.** The time the case was created, in ISO-8601 format.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                TypeInfo(str),
            ),
            (
                "display_id",
                "displayId",
                TypeInfo(str),
            ),
            (
                "subject",
                "subject",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "service_code",
                "serviceCode",
                TypeInfo(str),
            ),
            (
                "category_code",
                "categoryCode",
                TypeInfo(str),
            ),
            (
                "severity_code",
                "severityCode",
                TypeInfo(str),
            ),
            (
                "submitted_by",
                "submittedBy",
                TypeInfo(str),
            ),
            (
                "time_created",
                "timeCreated",
                TypeInfo(str),
            ),
            (
                "recent_communications",
                "recentCommunications",
                TypeInfo(RecentCaseCommunications),
            ),
            (
                "cc_email_addresses",
                "ccEmailAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "language",
                "language",
                TypeInfo(str),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID displayed for the case in the AWS Support Center. This is a numeric
    # string.
    display_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject line for the case in the AWS Support Center.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the case.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code for the AWS service returned by the call to DescribeServices.
    service_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category of problem for the AWS Support case.
    category_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code for the severity level returned by the call to
    # DescribeSeverityLevels.
    severity_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address of the account that submitted the case.
    submitted_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time that the case was case created in the AWS Support Center.
    time_created: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The five most recent communications between you and AWS Support Center,
    # including the IDs of any attachments to the communications. Also includes a
    # `nextToken` that you can use to retrieve earlier communications.
    recent_communications: "RecentCaseCommunications" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The email addresses that receive copies of communication about the case.
    cc_email_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaseIdNotFound(ShapeBase):
    """
    The requested `caseId` could not be located.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The requested `CaseId` could not be located.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Category(ShapeBase):
    """
    A JSON-formatted name/value pair that represents the category name and category
    code of the problem, selected from the DescribeServices response for each AWS
    service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The category code for the support case.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category name for the support case.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Communication(ShapeBase):
    """
    A communication associated with an AWS Support case. The communication consists
    of the case ID, the message body, attachment information, the account email
    address, and the date and time of the communication.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                TypeInfo(str),
            ),
            (
                "body",
                "body",
                TypeInfo(str),
            ),
            (
                "submitted_by",
                "submittedBy",
                TypeInfo(str),
            ),
            (
                "time_created",
                "timeCreated",
                TypeInfo(str),
            ),
            (
                "attachment_set",
                "attachmentSet",
                TypeInfo(typing.List[AttachmentDetails]),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text of the communication between the customer and AWS Support.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address of the account that submitted the AWS Support case.
    submitted_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the communication was created.
    time_created: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the attachments to the case communication.
    attachment_set: typing.List["AttachmentDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCaseRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subject",
                "subject",
                TypeInfo(str),
            ),
            (
                "communication_body",
                "communicationBody",
                TypeInfo(str),
            ),
            (
                "service_code",
                "serviceCode",
                TypeInfo(str),
            ),
            (
                "severity_code",
                "severityCode",
                TypeInfo(str),
            ),
            (
                "category_code",
                "categoryCode",
                TypeInfo(str),
            ),
            (
                "cc_email_addresses",
                "ccEmailAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "language",
                "language",
                TypeInfo(str),
            ),
            (
                "issue_type",
                "issueType",
                TypeInfo(str),
            ),
            (
                "attachment_set_id",
                "attachmentSetId",
                TypeInfo(str),
            ),
        ]

    # The title of the AWS Support case.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The communication body text when you create an AWS Support case by calling
    # CreateCase.
    communication_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code for the AWS service returned by the call to DescribeServices.
    service_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The code for the severity level returned by the call to
    # DescribeSeverityLevels.

    # The availability of severity levels depends on each customer's support
    # subscription. In other words, your subscription may not necessarily require
    # the urgent level of response time.
    severity_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category of problem for the AWS Support case.
    category_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of email addresses that AWS Support copies on case correspondence.
    cc_email_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of issue for the case. You can specify either "customer-service"
    # or "technical." If you do not indicate a value, the default is "technical."
    issue_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of a set of one or more attachments for the case. Create the set by
    # using AddAttachmentsToSet.
    attachment_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCaseResponse(OutputShapeBase):
    """
    The AWS Support case ID returned by a successful completion of the CreateCase
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "case_id",
                "caseId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Data(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DescribeAttachmentLimitExceeded(ShapeBase):
    """
    The limit for the number of DescribeAttachment requests in a short period of
    time has been exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The limit for the number of DescribeAttachment requests in a short period
    # of time has been exceeded.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAttachmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_id",
                "attachmentId",
                TypeInfo(str),
            ),
        ]

    # The ID of the attachment to return. Attachment IDs are returned by the
    # DescribeCommunications operation.
    attachment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeAttachmentResponse(OutputShapeBase):
    """
    The content and file name of the attachment returned by the DescribeAttachment
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attachment",
                "attachment",
                TypeInfo(Attachment),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attachment content and file name.
    attachment: "Attachment" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCasesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id_list",
                "caseIdList",
                TypeInfo(typing.List[str]),
            ),
            (
                "display_id",
                "displayId",
                TypeInfo(str),
            ),
            (
                "after_time",
                "afterTime",
                TypeInfo(str),
            ),
            (
                "before_time",
                "beforeTime",
                TypeInfo(str),
            ),
            (
                "include_resolved_cases",
                "includeResolvedCases",
                TypeInfo(bool),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "language",
                "language",
                TypeInfo(str),
            ),
            (
                "include_communications",
                "includeCommunications",
                TypeInfo(bool),
            ),
        ]

    # A list of ID numbers of the support cases you want returned. The maximum
    # number of cases is 100.
    case_id_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID displayed for a case in the AWS Support Center user interface.
    display_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    after_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    before_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether resolved support cases should be included in the
    # DescribeCases results. The default is _false_.
    include_resolved_cases: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return before paginating.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether communications should be included in the DescribeCases
    # results. The default is _true_.
    include_communications: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCasesResponse(OutputShapeBase):
    """
    Returns an array of CaseDetails objects and a `nextToken` that defines a point
    for pagination in the result set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cases",
                "cases",
                TypeInfo(typing.List[CaseDetails]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details for the cases that match the request.
    cases: typing.List["CaseDetails"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeCasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeCommunicationsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                TypeInfo(str),
            ),
            (
                "before_time",
                "beforeTime",
                TypeInfo(str),
            ),
            (
                "after_time",
                "afterTime",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    before_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start date for a filtered date search on support case communications.
    # Case communications are available for 12 months after creation.
    after_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return before paginating.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCommunicationsResponse(OutputShapeBase):
    """
    The communications returned by the DescribeCommunications operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "communications",
                "communications",
                TypeInfo(typing.List[Communication]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The communications for the case.
    communications: typing.List["Communication"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeCommunicationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeServicesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_code_list",
                "serviceCodeList",
                TypeInfo(typing.List[str]),
            ),
            (
                "language",
                "language",
                TypeInfo(str),
            ),
        ]

    # A JSON-formatted list of service codes available for AWS services.
    service_code_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServicesResponse(OutputShapeBase):
    """
    The list of AWS services returned by the DescribeServices operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "services",
                "services",
                TypeInfo(typing.List[Service]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A JSON-formatted list of AWS services.
    services: typing.List["Service"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSeverityLevelsRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language",
                "language",
                TypeInfo(str),
            ),
        ]

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSeverityLevelsResponse(OutputShapeBase):
    """
    The list of severity levels returned by the DescribeSeverityLevels operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "severity_levels",
                "severityLevels",
                TypeInfo(typing.List[SeverityLevel]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The available severity levels for the support case. Available severity
    # levels are defined by your service level agreement with AWS.
    severity_levels: typing.List["SeverityLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckRefreshStatusesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_ids",
                "checkIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the Trusted Advisor checks to get the status of. **Note:**
    # Specifying the check ID of a check that is automatically refreshed causes
    # an `InvalidParameterValue` error.
    check_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckRefreshStatusesResponse(OutputShapeBase):
    """
    The statuses of the Trusted Advisor checks returned by the
    DescribeTrustedAdvisorCheckRefreshStatuses operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "statuses",
                "statuses",
                TypeInfo(typing.List[TrustedAdvisorCheckRefreshStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The refresh status of the specified Trusted Advisor checks.
    statuses: typing.List["TrustedAdvisorCheckRefreshStatus"
                         ] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckResultRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                TypeInfo(str),
            ),
            (
                "language",
                "language",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckResultResponse(OutputShapeBase):
    """
    The result of the Trusted Advisor check returned by the
    DescribeTrustedAdvisorCheckResult operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "result",
                "result",
                TypeInfo(TrustedAdvisorCheckResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The detailed results of the Trusted Advisor check.
    result: "TrustedAdvisorCheckResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckSummariesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_ids",
                "checkIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the Trusted Advisor checks.
    check_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustedAdvisorCheckSummariesResponse(OutputShapeBase):
    """
    The summaries of the Trusted Advisor checks returned by the
    DescribeTrustedAdvisorCheckSummaries operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "summaries",
                "summaries",
                TypeInfo(typing.List[TrustedAdvisorCheckSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The summary information for the requested Trusted Advisor checks.
    summaries: typing.List["TrustedAdvisorCheckSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTrustedAdvisorChecksRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language",
                "language",
                TypeInfo(str),
            ),
        ]

    # The ISO 639-1 code for the language in which AWS provides support. AWS
    # Support currently supports English ("en") and Japanese ("ja"). Language
    # parameters must be passed explicitly for operations that take them.
    language: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustedAdvisorChecksResponse(OutputShapeBase):
    """
    Information about the Trusted Advisor checks returned by the
    DescribeTrustedAdvisorChecks operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "checks",
                "checks",
                TypeInfo(typing.List[TrustedAdvisorCheckDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about all available Trusted Advisor checks.
    checks: typing.List["TrustedAdvisorCheckDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    An internal server error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # An internal server error occurred.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecentCaseCommunications(ShapeBase):
    """
    The five most recent communications associated with the case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "communications",
                "communications",
                TypeInfo(typing.List[Communication]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The five most recent communications associated with the case.
    communications: typing.List["Communication"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A resumption point for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RefreshTrustedAdvisorCheckRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for the Trusted Advisor check to refresh. **Note:**
    # Specifying the check ID of a check that is automatically refreshed causes
    # an `InvalidParameterValue` error.
    check_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RefreshTrustedAdvisorCheckResponse(OutputShapeBase):
    """
    The current refresh status of a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(TrustedAdvisorCheckRefreshStatus),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current refresh status for a check, including the amount of time until
    # the check is eligible for refresh.
    status: "TrustedAdvisorCheckRefreshStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResolveCaseRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "case_id",
                "caseId",
                TypeInfo(str),
            ),
        ]

    # The AWS Support case ID requested or returned in the call. The case ID is
    # an alphanumeric string formatted as shown in this example: case-
    # _12345678910-2013-c4c1d2bf33c5cf47_
    case_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResolveCaseResponse(OutputShapeBase):
    """
    The status of the case returned by the ResolveCase operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "initial_case_status",
                "initialCaseStatus",
                TypeInfo(str),
            ),
            (
                "final_case_status",
                "finalCaseStatus",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the case when the ResolveCase request was sent.
    initial_case_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the case after the ResolveCase request was processed.
    final_case_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Service(ShapeBase):
    """
    Information about an AWS service returned by the DescribeServices operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "categories",
                "categories",
                TypeInfo(typing.List[Category]),
            ),
        ]

    # The code for an AWS service returned by the DescribeServices response. The
    # `name` element contains the corresponding friendly name.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name for an AWS service. The `code` element contains the
    # corresponding code.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of categories that describe the type of support issue a case
    # describes. Categories consist of a category name and a category code.
    # Category names and codes are passed to AWS Support when you call
    # CreateCase.
    categories: typing.List["Category"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SeverityLevel(ShapeBase):
    """
    A code and name pair that represent a severity level that can be applied to a
    support case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # One of four values: "low," "medium," "high," and "urgent". These values
    # correspond to response times returned to the caller in
    # `severityLevel.name`.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the severity level that corresponds to the severity level code.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedAdvisorCategorySpecificSummary(ShapeBase):
    """
    The container for summary information that relates to the category of the
    Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cost_optimizing",
                "costOptimizing",
                TypeInfo(TrustedAdvisorCostOptimizingSummary),
            ),
        ]

    # The summary information about cost savings for a Trusted Advisor check that
    # is in the Cost Optimizing category.
    cost_optimizing: "TrustedAdvisorCostOptimizingSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorCheckDescription(ShapeBase):
    """
    The description and metadata for a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "category",
                "category",
                TypeInfo(str),
            ),
            (
                "metadata",
                "metadata",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name for the Trusted Advisor check.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the Trusted Advisor check, which includes the alert
    # criteria and recommended actions (contains HTML markup).
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The category of the Trusted Advisor check.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The column headings for the data returned by the Trusted Advisor check. The
    # order of the headings corresponds to the order of the data in the
    # **Metadata** element of the TrustedAdvisorResourceDetail for the check.
    # **Metadata** contains all the data that is shown in the Excel download,
    # even in those cases where the UI shows just summary data.
    metadata: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedAdvisorCheckRefreshStatus(ShapeBase):
    """
    The refresh status of a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "millis_until_next_refreshable",
                "millisUntilNextRefreshable",
                TypeInfo(int),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the Trusted Advisor check for which a refresh has been
    # requested: "none", "enqueued", "processing", "success", or "abandoned".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in milliseconds, until the Trusted Advisor check is
    # eligible for refresh.
    millis_until_next_refreshable: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorCheckResult(ShapeBase):
    """
    The results of a Trusted Advisor check returned by
    DescribeTrustedAdvisorCheckResult.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "timestamp",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "resources_summary",
                "resourcesSummary",
                TypeInfo(TrustedAdvisorResourcesSummary),
            ),
            (
                "category_specific_summary",
                "categorySpecificSummary",
                TypeInfo(TrustedAdvisorCategorySpecificSummary),
            ),
            (
                "flagged_resources",
                "flaggedResources",
                TypeInfo(typing.List[TrustedAdvisorResourceDetail]),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time of the last refresh of the check.
    timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alert status of the check: "ok" (green), "warning" (yellow), "error"
    # (red), or "not_available".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about AWS resources that were analyzed in a call to Trusted Advisor
    # DescribeTrustedAdvisorCheckSummaries.
    resources_summary: "TrustedAdvisorResourcesSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information that relates to the category of the check. Cost
    # Optimizing is the only category that is currently supported.
    category_specific_summary: "TrustedAdvisorCategorySpecificSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details about each resource listed in the check result.
    flagged_resources: typing.List["TrustedAdvisorResourceDetail"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class TrustedAdvisorCheckSummary(ShapeBase):
    """
    A summary of a Trusted Advisor check result, including the alert status, last
    refresh, and number of resources examined.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "check_id",
                "checkId",
                TypeInfo(str),
            ),
            (
                "timestamp",
                "timestamp",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "resources_summary",
                "resourcesSummary",
                TypeInfo(TrustedAdvisorResourcesSummary),
            ),
            (
                "category_specific_summary",
                "categorySpecificSummary",
                TypeInfo(TrustedAdvisorCategorySpecificSummary),
            ),
            (
                "has_flagged_resources",
                "hasFlaggedResources",
                TypeInfo(bool),
            ),
        ]

    # The unique identifier for the Trusted Advisor check.
    check_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time of the last refresh of the check.
    timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alert status of the check: "ok" (green), "warning" (yellow), "error"
    # (red), or "not_available".
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about AWS resources that were analyzed in a call to Trusted Advisor
    # DescribeTrustedAdvisorCheckSummaries.
    resources_summary: "TrustedAdvisorResourcesSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Summary information that relates to the category of the check. Cost
    # Optimizing is the only category that is currently supported.
    category_specific_summary: "TrustedAdvisorCategorySpecificSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the Trusted Advisor check has flagged resources.
    has_flagged_resources: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedAdvisorCostOptimizingSummary(ShapeBase):
    """
    The estimated cost savings that might be realized if the recommended actions are
    taken.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "estimated_monthly_savings",
                "estimatedMonthlySavings",
                TypeInfo(float),
            ),
            (
                "estimated_percent_monthly_savings",
                "estimatedPercentMonthlySavings",
                TypeInfo(float),
            ),
        ]

    # The estimated monthly savings that might be realized if the recommended
    # actions are taken.
    estimated_monthly_savings: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The estimated percentage of savings that might be realized if the
    # recommended actions are taken.
    estimated_percent_monthly_savings: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TrustedAdvisorResourceDetail(ShapeBase):
    """
    Contains information about a resource identified by a Trusted Advisor check.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "resource_id",
                "resourceId",
                TypeInfo(str),
            ),
            (
                "metadata",
                "metadata",
                TypeInfo(typing.List[str]),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "is_suppressed",
                "isSuppressed",
                TypeInfo(bool),
            ),
        ]

    # The status code for the resource identified in the Trusted Advisor check.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the identified resource.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about the identified resource. The exact metadata
    # and its order can be obtained by inspecting the
    # TrustedAdvisorCheckDescription object returned by the call to
    # DescribeTrustedAdvisorChecks. **Metadata** contains all the data that is
    # shown in the Excel download, even in those cases where the UI shows just
    # summary data.
    metadata: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region in which the identified resource is located.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the AWS resource was ignored by Trusted Advisor because
    # it was marked as suppressed by the user.
    is_suppressed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedAdvisorResourcesSummary(ShapeBase):
    """
    Details about AWS resources that were analyzed in a call to Trusted Advisor
    DescribeTrustedAdvisorCheckSummaries.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resources_processed",
                "resourcesProcessed",
                TypeInfo(int),
            ),
            (
                "resources_flagged",
                "resourcesFlagged",
                TypeInfo(int),
            ),
            (
                "resources_ignored",
                "resourcesIgnored",
                TypeInfo(int),
            ),
            (
                "resources_suppressed",
                "resourcesSuppressed",
                TypeInfo(int),
            ),
        ]

    # The number of AWS resources that were analyzed by the Trusted Advisor
    # check.
    resources_processed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS resources that were flagged (listed) by the Trusted
    # Advisor check.
    resources_flagged: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS resources ignored by Trusted Advisor because information
    # was unavailable.
    resources_ignored: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of AWS resources ignored by Trusted Advisor because they were
    # marked as suppressed by the user.
    resources_suppressed: int = dataclasses.field(default=ShapeBase.NOT_SET, )
