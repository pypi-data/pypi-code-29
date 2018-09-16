import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AcceptInvitationRequest(ShapeBase):
    """
    AcceptInvitation request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "invitation_id",
                "InvitationId",
                TypeInfo(str),
            ),
            (
                "master_id",
                "MasterId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty member account.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is used to validate the master account to the member account.
    invitation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The account ID of the master GuardDuty account whose invitation you're
    # accepting.
    master_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AcceptInvitationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AccessKeyDetails(ShapeBase):
    """
    The IAM access key details (IAM user information) of a user that engaged in the
    activity that prompted GuardDuty to generate a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_id",
                "AccessKeyId",
                TypeInfo(str),
            ),
            (
                "principal_id",
                "PrincipalId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "user_type",
                "UserType",
                TypeInfo(str),
            ),
        ]

    # Access key ID of the user.
    access_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The principal ID of the user.
    principal_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the user.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the user.
    user_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AccountDetail(ShapeBase):
    """
    An object containing the member's accountId and email address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
        ]

    # Member account ID.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Member account's email address.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Action(ShapeBase):
    """
    Information about the activity described in a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_type",
                "ActionType",
                TypeInfo(str),
            ),
            (
                "aws_api_call_action",
                "AwsApiCallAction",
                TypeInfo(AwsApiCallAction),
            ),
            (
                "dns_request_action",
                "DnsRequestAction",
                TypeInfo(DnsRequestAction),
            ),
            (
                "network_connection_action",
                "NetworkConnectionAction",
                TypeInfo(NetworkConnectionAction),
            ),
            (
                "port_probe_action",
                "PortProbeAction",
                TypeInfo(PortProbeAction),
            ),
        ]

    # GuardDuty Finding activity type.
    action_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the AWS_API_CALL action described in this finding.
    aws_api_call_action: "AwsApiCallAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the DNS_REQUEST action described in this finding.
    dns_request_action: "DnsRequestAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the NETWORK_CONNECTION action described in this finding.
    network_connection_action: "NetworkConnectionAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the PORT_PROBE action described in this finding.
    port_probe_action: "PortProbeAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ArchiveFindingsRequest(ShapeBase):
    """
    ArchiveFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "finding_ids",
                "FindingIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to archive.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IDs of the findings that you want to archive.
    finding_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ArchiveFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AwsApiCallAction(ShapeBase):
    """
    Information about the AWS_API_CALL action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api",
                "Api",
                TypeInfo(str),
            ),
            (
                "caller_type",
                "CallerType",
                TypeInfo(str),
            ),
            (
                "domain_details",
                "DomainDetails",
                TypeInfo(DomainDetails),
            ),
            (
                "remote_ip_details",
                "RemoteIpDetails",
                TypeInfo(RemoteIpDetails),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
        ]

    # AWS API name.
    api: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS API caller type.
    caller_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Domain information for the AWS API call.
    domain_details: "DomainDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Remote IP information of the connection.
    remote_ip_details: "RemoteIpDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS service name whose API was invoked.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    Error response object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class City(ShapeBase):
    """
    City information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "city_name",
                "CityName",
                TypeInfo(str),
            ),
        ]

    # City name of the remote IP address.
    city_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Condition(ShapeBase):
    """
    Finding attribute (for example, accountId) for which conditions and values must
    be specified when querying findings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "eq",
                "Eq",
                TypeInfo(typing.List[str]),
            ),
            (
                "gt",
                "Gt",
                TypeInfo(int),
            ),
            (
                "gte",
                "Gte",
                TypeInfo(int),
            ),
            (
                "lt",
                "Lt",
                TypeInfo(int),
            ),
            (
                "lte",
                "Lte",
                TypeInfo(int),
            ),
            (
                "neq",
                "Neq",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Represents the equal condition to be applied to a single field when
    # querying for findings.
    eq: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the greater than condition to be applied to a single field when
    # querying for findings.
    gt: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the greater than equal condition to be applied to a single field
    # when querying for findings.
    gte: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the less than condition to be applied to a single field when
    # querying for findings.
    lt: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the less than equal condition to be applied to a single field
    # when querying for findings.
    lte: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the not equal condition to be applied to a single field when
    # querying for findings.
    neq: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Country(ShapeBase):
    """
    Country information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "country_code",
                "CountryCode",
                TypeInfo(str),
            ),
            (
                "country_name",
                "CountryName",
                TypeInfo(str),
            ),
        ]

    # Country code of the remote IP address.
    country_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Country name of the remote IP address.
    country_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDetectorRequest(ShapeBase):
    """
    CreateDetector request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enable",
                "Enable",
                TypeInfo(bool),
            ),
        ]

    # A boolean value that specifies whether the detector is to be enabled.
    enable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDetectorResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of the created detector.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFilterRequest(ShapeBase):
    """
    CreateFilterRequest request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, FilterAction]),
            ),
            (
                "client_token",
                "ClientToken",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                TypeInfo(FindingCriteria),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "rank",
                "Rank",
                TypeInfo(int),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the action that is to be applied to the findings that match the
    # filter.
    action: typing.Union[str, "FilterAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The idempotency token for the create request.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the filter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the criteria to be used in the filter for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the position of the filter in the list of current filters. Also
    # specifies the order in which this filter is applied to the findings.
    rank: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFilterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the successfully created filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIPSetRequest(ShapeBase):
    """
    CreateIPSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                TypeInfo(bool),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, IpSetFormat]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value that indicates whether GuardDuty is to start using the
    # uploaded IPSet.
    activate: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the file that contains the IPSet.
    format: typing.Union[str, "IpSetFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URI of the file that contains the IPSet. For example (https://s3.us-
    # west-2.amazonaws.com/my-bucket/my-object-key)
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user friendly name to identify the IPSet. This name is displayed in all
    # findings that are triggered by activity that involves IP addresses included
    # in this IPSet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIPSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ip_set_id",
                "IpSetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for an IP Set
    ip_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMembersRequest(ShapeBase):
    """
    CreateMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_details",
                "AccountDetails",
                TypeInfo(typing.List[AccountDetail]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account with which you want
    # to associate member accounts.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account ID and email address pairs of the accounts that you want
    # to associate with the master GuardDuty account.
    account_details: typing.List["AccountDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSampleFindingsRequest(ShapeBase):
    """
    CreateSampleFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "finding_types",
                "FindingTypes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector to create sample findings for.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Types of sample findings that you want to generate.
    finding_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSampleFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateThreatIntelSetRequest(ShapeBase):
    """
    CreateThreatIntelSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                TypeInfo(bool),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, ThreatIntelSetFormat]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A boolean value that indicates whether GuardDuty is to start using the
    # uploaded ThreatIntelSet.
    activate: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the file that contains the ThreatIntelSet.
    format: typing.Union[str, "ThreatIntelSetFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URI of the file that contains the ThreatIntelSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-friendly ThreatIntelSet name that is displayed in all finding
    # generated by activity that involves IP addresses included in this
    # ThreatIntelSet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateThreatIntelSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for an threat intel set
    threat_intel_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeclineInvitationsRequest(ShapeBase):
    """
    DeclineInvitations request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of account IDs of the AWS accounts that sent invitations to the
    # current member account that you want to decline invitations from.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeclineInvitationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDetectorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
        ]

    # The unique ID that specifies the detector that you want to delete.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDetectorResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "FilterName",
                TypeInfo(str),
            ),
        ]

    # The unique ID that specifies the detector where you want to delete a
    # filter.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFilterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteIPSetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "ip_set_id",
                "IpSetId",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose IPSet you want to
    # delete.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the IPSet that you want to delete.
    ip_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIPSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInvitationsRequest(ShapeBase):
    """
    DeleteInvitations request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of account IDs of the AWS accounts that sent invitations to the
    # current member account that you want to delete invitations from.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInvitationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteMembersRequest(ShapeBase):
    """
    DeleteMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to delete.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts that you want to
    # delete.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteThreatIntelSetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSet
    # you want to delete.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to delete.
    threat_intel_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteThreatIntelSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DetectorStatus(str):
    """
    The status of detector.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class DisassociateFromMasterAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty member account.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateFromMasterAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateMembersRequest(ShapeBase):
    """
    DisassociateMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to disassociate from master.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts that you want to
    # disassociate from master.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DnsRequestAction(ShapeBase):
    """
    Information about the DNS_REQUEST action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
        ]

    # Domain information for the DNS request.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainDetails(ShapeBase):
    """
    Domain information for the AWS API call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ErrorResponse(ShapeBase):
    """
    Error response object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Feedback(str):
    """
    Finding Feedback Value
    """
    USEFUL = "USEFUL"
    NOT_USEFUL = "NOT_USEFUL"


class FilterAction(str):
    """
    The action associated with a filter.
    """
    NOOP = "NOOP"
    ARCHIVE = "ARCHIVE"


@dataclasses.dataclass
class Finding(ShapeBase):
    """
    Representation of a abnormal or suspicious activity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "resource",
                "Resource",
                TypeInfo(Resource),
            ),
            (
                "schema_version",
                "SchemaVersion",
                TypeInfo(str),
            ),
            (
                "severity",
                "Severity",
                TypeInfo(float),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
            (
                "updated_at",
                "UpdatedAt",
                TypeInfo(str),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "partition",
                "Partition",
                TypeInfo(str),
            ),
            (
                "service",
                "Service",
                TypeInfo(Service),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
        ]

    # AWS account ID where the activity occurred that prompted GuardDuty to
    # generate a finding.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of a finding described by the action.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp at which a finding was generated.
    created_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier that corresponds to a finding described by the action.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region where the activity occurred that prompted GuardDuty to
    # generate a finding.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS resource associated with the activity that prompted GuardDuty to
    # generate a finding.
    resource: "Resource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Findings' schema version.
    schema_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The severity of a finding.
    severity: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of a finding described by the action.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time stamp at which a finding was last updated.
    updated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The confidence level of a finding.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of a finding.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS resource partition.
    partition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information assigned to the generated finding by GuardDuty.
    service: "Service" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The title of a finding.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FindingCriteria(ShapeBase):
    """
    Represents the criteria used for querying findings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "criterion",
                "Criterion",
                TypeInfo(typing.Dict[str, Condition]),
            ),
        ]

    # Represents a map of finding properties that match specified conditions and
    # values when querying findings.
    criterion: typing.Dict[str, "Condition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class FindingStatisticType(str):
    """
    The types of finding statistics.
    """
    COUNT_BY_SEVERITY = "COUNT_BY_SEVERITY"


@dataclasses.dataclass
class FindingStatistics(ShapeBase):
    """
    Finding statistics object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count_by_severity",
                "CountBySeverity",
                TypeInfo(typing.Dict[str, int]),
            ),
        ]

    # Represents a map of severity to count statistic for a set of findings
    count_by_severity: typing.Dict[str, int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GeoLocation(ShapeBase):
    """
    Location information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lat",
                "Lat",
                TypeInfo(float),
            ),
            (
                "lon",
                "Lon",
                TypeInfo(float),
            ),
        ]

    # Latitude information of remote IP address.
    lat: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Longitude information of remote IP address.
    lon: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDetectorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to retrieve.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDetectorResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(str),
            ),
            (
                "service_role",
                "ServiceRole",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, DetectorStatus]),
            ),
            (
                "updated_at",
                "UpdatedAt",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The first time a resource was created. The format will be ISO-8601.
    created_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Customer serviceRole name or ARN for accessing customer resources
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of detector.
    status: typing.Union[str, "DetectorStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The first time a resource was created. The format will be ISO-8601.
    updated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFilterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "FilterName",
                TypeInfo(str),
            ),
        ]

    # The detector ID that specifies the GuardDuty service where you want to list
    # the details of the specified filter.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the filter whose details you want to get.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFilterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, FilterAction]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                TypeInfo(FindingCriteria),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "rank",
                "Rank",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the action that is to be applied to the findings that match the
    # filter.
    action: typing.Union[str, "FilterAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the filter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the criteria to be used in the filter for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the position of the filter in the list of current filters. Also
    # specifies the order in which this filter is applied to the findings.
    rank: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFindingsRequest(ShapeBase):
    """
    GetFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "finding_ids",
                "FindingIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(SortCriteria),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to retrieve.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IDs of the findings that you want to retrieve.
    finding_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the criteria used for sorting findings.
    sort_criteria: "SortCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "findings",
                "Findings",
                TypeInfo(typing.List[Finding]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of findings.
    findings: typing.List["Finding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFindingsStatisticsRequest(ShapeBase):
    """
    GetFindingsStatistics request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                TypeInfo(FindingCriteria),
            ),
            (
                "finding_statistic_types",
                "FindingStatisticTypes",
                TypeInfo(typing.List[typing.Union[str, FindingStatisticType]]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings'
    # statistics you want to retrieve.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the criteria used for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Types of finding statistics to retrieve.
    finding_statistic_types: typing.List[
        typing.Union[str, "FindingStatisticType"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class GetFindingsStatisticsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "finding_statistics",
                "FindingStatistics",
                TypeInfo(FindingStatistics),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Finding statistics object.
    finding_statistics: "FindingStatistics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIPSetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "ip_set_id",
                "IpSetId",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose IPSet you want to
    # retrieve.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the IPSet that you want to describe.
    ip_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIPSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, IpSetFormat]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, IpSetStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the file that contains the IPSet.
    format: typing.Union[str, "IpSetFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URI of the file that contains the IPSet. For example (https://s3.us-
    # west-2.amazonaws.com/my-bucket/my-object-key)
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user friendly name to identify the IPSet. This name is displayed in all
    # findings that are triggered by activity that involves IP addresses included
    # in this IPSet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of ipSet file uploaded.
    status: typing.Union[str, "IpSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInvitationsCountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetInvitationsCountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "invitations_count",
                "InvitationsCount",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of received invitations.
    invitations_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMasterAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty member account.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMasterAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "master",
                "Master",
                TypeInfo(Master),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains details about the master account.
    master: "Master" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetMembersRequest(ShapeBase):
    """
    GetMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to retrieve.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts that you want to
    # describe.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "members",
                "Members",
                TypeInfo(typing.List[Member]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of member descriptions.
    members: typing.List["Member"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetThreatIntelSetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSet
    # you want to describe.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to describe.
    threat_intel_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetThreatIntelSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, ThreatIntelSetFormat]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, ThreatIntelSetStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the threatIntelSet.
    format: typing.Union[str, "ThreatIntelSetFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URI of the file that contains the ThreatIntelSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-friendly ThreatIntelSet name that is displayed in all finding
    # generated by activity that involves IP addresses included in this
    # ThreatIntelSet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of threatIntelSet file uploaded.
    status: typing.Union[str, "ThreatIntelSetStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IamInstanceProfile(ShapeBase):
    """
    The profile information of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # AWS EC2 instance profile ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS EC2 instance profile ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceDetails(ShapeBase):
    """
    The information about the EC2 instance associated with the activity that
    prompted GuardDuty to generate a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "iam_instance_profile",
                "IamInstanceProfile",
                TypeInfo(IamInstanceProfile),
            ),
            (
                "image_description",
                "ImageDescription",
                TypeInfo(str),
            ),
            (
                "image_id",
                "ImageId",
                TypeInfo(str),
            ),
            (
                "instance_id",
                "InstanceId",
                TypeInfo(str),
            ),
            (
                "instance_state",
                "InstanceState",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(str),
            ),
            (
                "launch_time",
                "LaunchTime",
                TypeInfo(str),
            ),
            (
                "network_interfaces",
                "NetworkInterfaces",
                TypeInfo(typing.List[NetworkInterface]),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "product_codes",
                "ProductCodes",
                TypeInfo(typing.List[ProductCode]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The availability zone of the EC2 instance.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The profile information of the EC2 instance.
    iam_instance_profile: "IamInstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The image description of the EC2 instance.
    image_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image ID of the EC2 instance.
    image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the EC2 instance.
    instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the EC2 instance.
    instance_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the EC2 instance.
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The launch time of the EC2 instance.
    launch_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network interface information of the EC2 instance.
    network_interfaces: typing.List["NetworkInterface"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform of the EC2 instance.
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product code of the EC2 instance.
    product_codes: typing.List["ProductCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags of the EC2 instance.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    Error response object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error type.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Invitation(ShapeBase):
    """
    Invitation from an AWS account to become the current account's master.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "invitation_id",
                "InvitationId",
                TypeInfo(str),
            ),
            (
                "invited_at",
                "InvitedAt",
                TypeInfo(str),
            ),
            (
                "relationship_status",
                "RelationshipStatus",
                TypeInfo(str),
            ),
        ]

    # Inviter account ID
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is used to validate the inviter account to the member account.
    invitation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp at which the invitation was sent
    invited_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the relationship between the inviter and invitee accounts.
    relationship_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InviteMembersRequest(ShapeBase):
    """
    InviteMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "disable_email_notification",
                "DisableEmailNotification",
                TypeInfo(bool),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account with which you want
    # to invite members.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account IDs of the accounts that you want to invite to GuardDuty
    # as members.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A boolean value that specifies whether you want to disable email
    # notification to the accounts that you’re inviting to GuardDuty as members.
    disable_email_notification: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The invitation message that you want to send to the accounts that you’re
    # inviting to GuardDuty as members.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InviteMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class IpSetFormat(str):
    """
    The format of the ipSet.
    """
    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class IpSetStatus(str):
    """
    The status of ipSet file uploaded.
    """
    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


@dataclasses.dataclass
class ListDetectorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # You can use this parameter to indicate the maximum number of detectors that
    # you want in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListDetectors action. For
    # subsequent calls to the action fill nextToken in the request with the value
    # of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDetectorsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "detector_ids",
                "DetectorIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of detector Ids.
    detector_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDetectorsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFiltersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service where you want
    # to list filters.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the maximum number of items that you want in the response. The
    # maximum value is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Paginates results. Set the value of this parameter to NULL on your first
    # call to the ListFilters operation.For subsequent calls to the operation,
    # fill nextToken in the request with the value of nextToken from the previous
    # response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFiltersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "filter_names",
                "FilterNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of filter names
    filter_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListFiltersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFindingsRequest(ShapeBase):
    """
    ListFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                TypeInfo(FindingCriteria),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "sort_criteria",
                "SortCriteria",
                TypeInfo(SortCriteria),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to list.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the criteria used for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 50. The maximum value is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListFindings action. For
    # subsequent calls to the action fill nextToken in the request with the value
    # of nextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the criteria used for sorting findings.
    sort_criteria: "SortCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "finding_ids",
                "FindingIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of the Findings.
    finding_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListFindingsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListIPSetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector that you want to retrieve.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 7. The maximum value is 7.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListIPSet action. For
    # subsequent calls to the action fill nextToken in the request with the value
    # of NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIPSetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ip_set_ids",
                "IpSetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the IP set IDs
    ip_set_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListIPSetsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInvitationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # You can use this parameter to indicate the maximum number of invitations
    # you want in the response. The default value is 50. The maximum value is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListInvitations action.
    # Subsequent calls to the action fill nextToken in the request with the value
    # of NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInvitationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "invitations",
                "Invitations",
                TypeInfo(typing.List[Invitation]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of invitation descriptions.
    invitations: typing.List["Invitation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListInvitationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListMembersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "only_associated",
                "OnlyAssociated",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whose members you
    # want to list.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items you want
    # in the response. The default value is 1. The maximum value is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the ListMembers action. Subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies what member accounts the response is to include based on their
    # relationship status with the master account. The default value is TRUE. If
    # onlyAssociated is set to TRUE, the response will include member accounts
    # whose relationship status with the master is set to Enabled, Disabled. If
    # onlyAssociated is set to FALSE, the response will include all existing
    # member accounts.
    only_associated: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "members",
                "Members",
                TypeInfo(typing.List[Member]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of member descriptions.
    members: typing.List["Member"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListMembersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListThreatIntelSetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSets
    # you want to list.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can use this parameter to indicate the maximum number of items that you
    # want in the response. The default value is 7. The maximum value is 7.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pagination token to start retrieving threat intel sets from.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListThreatIntelSetsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "threat_intel_set_ids",
                "ThreatIntelSetIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can use this parameter when paginating results. Set the value of this
    # parameter to null on your first call to the list action. For subsequent
    # calls to the action fill nextToken in the request with the value of
    # NextToken from the previous response to continue listing data.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of the threat intel set IDs
    threat_intel_set_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["ListThreatIntelSetsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class LocalPortDetails(ShapeBase):
    """
    Local port information of the connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "port_name",
                "PortName",
                TypeInfo(str),
            ),
        ]

    # Port number of the local connection.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Port name of the local connection.
    port_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Master(ShapeBase):
    """
    Contains details about the master account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "invitation_id",
                "InvitationId",
                TypeInfo(str),
            ),
            (
                "invited_at",
                "InvitedAt",
                TypeInfo(str),
            ),
            (
                "relationship_status",
                "RelationshipStatus",
                TypeInfo(str),
            ),
        ]

    # Master account ID
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is used to validate the master account to the member account.
    invitation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp at which the invitation was sent
    invited_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the relationship between the master and member accounts.
    relationship_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Member(ShapeBase):
    """
    Contains details about the member account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "master_id",
                "MasterId",
                TypeInfo(str),
            ),
            (
                "relationship_status",
                "RelationshipStatus",
                TypeInfo(str),
            ),
            (
                "updated_at",
                "UpdatedAt",
                TypeInfo(str),
            ),
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "invited_at",
                "InvitedAt",
                TypeInfo(str),
            ),
        ]

    # AWS account ID.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Member account's email address.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The master account ID.
    master_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the relationship between the member and the master.
    relationship_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The first time a resource was created. The format will be ISO-8601.
    updated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for a detector.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp at which the invitation was sent
    invited_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkConnectionAction(ShapeBase):
    """
    Information about the NETWORK_CONNECTION action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blocked",
                "Blocked",
                TypeInfo(bool),
            ),
            (
                "connection_direction",
                "ConnectionDirection",
                TypeInfo(str),
            ),
            (
                "local_port_details",
                "LocalPortDetails",
                TypeInfo(LocalPortDetails),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(str),
            ),
            (
                "remote_ip_details",
                "RemoteIpDetails",
                TypeInfo(RemoteIpDetails),
            ),
            (
                "remote_port_details",
                "RemotePortDetails",
                TypeInfo(RemotePortDetails),
            ),
        ]

    # Network connection blocked information.
    blocked: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Network connection direction.
    connection_direction: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Local port information of the connection.
    local_port_details: "LocalPortDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Network connection protocol.
    protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Remote IP information of the connection.
    remote_ip_details: "RemoteIpDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Remote port information of the connection.
    remote_port_details: "RemotePortDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NetworkInterface(ShapeBase):
    """
    The network interface information of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ipv6_addresses",
                "Ipv6Addresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
            (
                "private_dns_name",
                "PrivateDnsName",
                TypeInfo(str),
            ),
            (
                "private_ip_address",
                "PrivateIpAddress",
                TypeInfo(str),
            ),
            (
                "private_ip_addresses",
                "PrivateIpAddresses",
                TypeInfo(typing.List[PrivateIpAddressDetails]),
            ),
            (
                "public_dns_name",
                "PublicDnsName",
                TypeInfo(str),
            ),
            (
                "public_ip",
                "PublicIp",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[SecurityGroup]),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
        ]

    # A list of EC2 instance IPv6 address information.
    ipv6_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the network interface
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Private DNS name of the EC2 instance.
    private_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Private IP address of the EC2 instance.
    private_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Other private IP address information of the EC2 instance.
    private_ip_addresses: typing.List["PrivateIpAddressDetails"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Public DNS name of the EC2 instance.
    public_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Public IP address of the EC2 instance.
    public_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Security groups associated with the EC2 instance.
    security_groups: typing.List["SecurityGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The subnet ID of the EC2 instance.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC ID of the EC2 instance.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OrderBy(str):
    ASC = "ASC"
    DESC = "DESC"


@dataclasses.dataclass
class Organization(ShapeBase):
    """
    ISP Organization information of the remote IP address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "asn",
                "Asn",
                TypeInfo(str),
            ),
            (
                "asn_org",
                "AsnOrg",
                TypeInfo(str),
            ),
            (
                "isp",
                "Isp",
                TypeInfo(str),
            ),
            (
                "org",
                "Org",
                TypeInfo(str),
            ),
        ]

    # Autonomous system number of the internet provider of the remote IP address.
    asn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Organization that registered this ASN.
    asn_org: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ISP information for the internet provider.
    isp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the internet provider.
    org: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PortProbeAction(ShapeBase):
    """
    Information about the PORT_PROBE action described in this finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blocked",
                "Blocked",
                TypeInfo(bool),
            ),
            (
                "port_probe_details",
                "PortProbeDetails",
                TypeInfo(typing.List[PortProbeDetail]),
            ),
        ]

    # Port probe blocked information.
    blocked: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of port probe details objects.
    port_probe_details: typing.List["PortProbeDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PortProbeDetail(ShapeBase):
    """
    Details about the port probe finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "local_port_details",
                "LocalPortDetails",
                TypeInfo(LocalPortDetails),
            ),
            (
                "remote_ip_details",
                "RemoteIpDetails",
                TypeInfo(RemoteIpDetails),
            ),
        ]

    # Local port information of the connection.
    local_port_details: "LocalPortDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Remote IP information of the connection.
    remote_ip_details: "RemoteIpDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PrivateIpAddressDetails(ShapeBase):
    """
    Other private IP address information of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "private_dns_name",
                "PrivateDnsName",
                TypeInfo(str),
            ),
            (
                "private_ip_address",
                "PrivateIpAddress",
                TypeInfo(str),
            ),
        ]

    # Private DNS name of the EC2 instance.
    private_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Private IP address of the EC2 instance.
    private_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProductCode(ShapeBase):
    """
    The product code of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "product_type",
                "ProductType",
                TypeInfo(str),
            ),
        ]

    # Product code information.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Product code type.
    product_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoteIpDetails(ShapeBase):
    """
    Remote IP information of the connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "city",
                "City",
                TypeInfo(City),
            ),
            (
                "country",
                "Country",
                TypeInfo(Country),
            ),
            (
                "geo_location",
                "GeoLocation",
                TypeInfo(GeoLocation),
            ),
            (
                "ip_address_v4",
                "IpAddressV4",
                TypeInfo(str),
            ),
            (
                "organization",
                "Organization",
                TypeInfo(Organization),
            ),
        ]

    # City information of the remote IP address.
    city: "City" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Country code of the remote IP address.
    country: "Country" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Location information of the remote IP address.
    geo_location: "GeoLocation" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IPV4 remote address of the connection.
    ip_address_v4: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ISP Organization information of the remote IP address.
    organization: "Organization" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemotePortDetails(ShapeBase):
    """
    Remote port information of the connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port",
                "Port",
                TypeInfo(int),
            ),
            (
                "port_name",
                "PortName",
                TypeInfo(str),
            ),
        ]

    # Port number of the remote connection.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Port name of the remote connection.
    port_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(ShapeBase):
    """
    The AWS resource associated with the activity that prompted GuardDuty to
    generate a finding.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_key_details",
                "AccessKeyDetails",
                TypeInfo(AccessKeyDetails),
            ),
            (
                "instance_details",
                "InstanceDetails",
                TypeInfo(InstanceDetails),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
        ]

    # The IAM access key details (IAM user information) of a user that engaged in
    # the activity that prompted GuardDuty to generate a finding.
    access_key_details: "AccessKeyDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information about the EC2 instance associated with the activity that
    # prompted GuardDuty to generate a finding.
    instance_details: "InstanceDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the AWS resource.
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SecurityGroup(ShapeBase):
    """
    Security groups associated with the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "group_name",
                "GroupName",
                TypeInfo(str),
            ),
        ]

    # EC2 instance's security group ID.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # EC2 instance's security group name.
    group_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Service(ShapeBase):
    """
    Additional information assigned to the generated finding by GuardDuty.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(Action),
            ),
            (
                "archived",
                "Archived",
                TypeInfo(bool),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "event_first_seen",
                "EventFirstSeen",
                TypeInfo(str),
            ),
            (
                "event_last_seen",
                "EventLastSeen",
                TypeInfo(str),
            ),
            (
                "resource_role",
                "ResourceRole",
                TypeInfo(str),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
            (
                "user_feedback",
                "UserFeedback",
                TypeInfo(str),
            ),
        ]

    # Information about the activity described in a finding.
    action: "Action" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether this finding is archived.
    archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Total count of the occurrences of this finding type.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detector ID for the GuardDuty service.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # First seen timestamp of the activity that prompted GuardDuty to generate
    # this finding.
    event_first_seen: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last seen timestamp of the activity that prompted GuardDuty to generate
    # this finding.
    event_last_seen: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Resource role information for this finding.
    resource_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS service (GuardDuty) that generated a finding.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Feedback left about the finding.
    user_feedback: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SortCriteria(ShapeBase):
    """
    Represents the criteria used for sorting findings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "order_by",
                "OrderBy",
                TypeInfo(typing.Union[str, OrderBy]),
            ),
        ]

    # Represents the finding attribute (for example, accountId) by which to sort
    # findings.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Order by which the sorted findings are to be displayed.
    order_by: typing.Union[str, "OrderBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartMonitoringMembersRequest(ShapeBase):
    """
    StartMonitoringMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account whom you want to re-
    # enable to monitor members' findings.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts whose findings you
    # want the master account to monitor.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartMonitoringMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopMonitoringMembersRequest(ShapeBase):
    """
    StopMonitoringMembers request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "account_ids",
                "AccountIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID of the detector of the GuardDuty account that you want to
    # stop from monitor members' findings.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of account IDs of the GuardDuty member accounts whose findings you
    # want the master account to stop monitoring.
    account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopMonitoringMembersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "unprocessed_accounts",
                "UnprocessedAccounts",
                TypeInfo(typing.List[UnprocessedAccount]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of objects containing the unprocessed account and a result string
    # explaining why it was unprocessed.
    unprocessed_accounts: typing.List["UnprocessedAccount"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A tag of the EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # EC2 instance tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # EC2 instance tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ThreatIntelSetFormat(str):
    """
    The format of the threatIntelSet.
    """
    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class ThreatIntelSetStatus(str):
    """
    The status of threatIntelSet file uploaded.
    """
    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


@dataclasses.dataclass
class UnarchiveFindingsRequest(ShapeBase):
    """
    UnarchiveFindings request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "finding_ids",
                "FindingIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to unarchive.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IDs of the findings that you want to unarchive.
    finding_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnarchiveFindingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnprocessedAccount(ShapeBase):
    """
    An object containing the unprocessed account and a result string explaining why
    it was unprocessed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                TypeInfo(str),
            ),
            (
                "result",
                "Result",
                TypeInfo(str),
            ),
        ]

    # AWS Account ID.
    account_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reason why the account hasn't been processed.
    result: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDetectorRequest(ShapeBase):
    """
    UpdateDetector request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "enable",
                "Enable",
                TypeInfo(bool),
            ),
        ]

    # The unique ID of the detector that you want to update.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Updated boolean value for the detector that specifies whether the detector
    # is enabled.
    enable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDetectorResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateFilterRequest(ShapeBase):
    """
    UpdateFilterRequest request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "filter_name",
                "FilterName",
                TypeInfo(str),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, FilterAction]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "finding_criteria",
                "FindingCriteria",
                TypeInfo(FindingCriteria),
            ),
            (
                "rank",
                "Rank",
                TypeInfo(int),
            ),
        ]

    # The unique ID of the detector that specifies the GuardDuty service where
    # you want to update a filter.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the filter.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the action that is to be applied to the findings that match the
    # filter.
    action: typing.Union[str, "FilterAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the filter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the criteria to be used in the filter for querying findings.
    finding_criteria: "FindingCriteria" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the position of the filter in the list of current filters. Also
    # specifies the order in which this filter is applied to the findings.
    rank: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFilterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the filter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFindingsFeedbackRequest(ShapeBase):
    """
    UpdateFindingsFeedback request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "comments",
                "Comments",
                TypeInfo(str),
            ),
            (
                "feedback",
                "Feedback",
                TypeInfo(typing.Union[str, Feedback]),
            ),
            (
                "finding_ids",
                "FindingIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the detector that specifies the GuardDuty service whose findings
    # you want to mark as useful or not useful.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional feedback about the GuardDuty findings.
    comments: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Valid values: USEFUL | NOT_USEFUL
    feedback: typing.Union[str, "Feedback"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IDs of the findings that you want to mark as useful or not useful.
    finding_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateFindingsFeedbackResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateIPSetRequest(ShapeBase):
    """
    UpdateIPSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "ip_set_id",
                "IpSetId",
                TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                TypeInfo(bool),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose IPSet you want to
    # update.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the IPSet that you want to update.
    ip_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated boolean value that specifies whether the IPSet is active or
    # not.
    activate: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated URI of the file that contains the IPSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the IPSet that you want to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateIPSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateThreatIntelSetRequest(ShapeBase):
    """
    UpdateThreatIntelSet request body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detector_id",
                "DetectorId",
                TypeInfo(str),
            ),
            (
                "threat_intel_set_id",
                "ThreatIntelSetId",
                TypeInfo(str),
            ),
            (
                "activate",
                "Activate",
                TypeInfo(bool),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The detectorID that specifies the GuardDuty service whose ThreatIntelSet
    # you want to update.
    detector_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to update.
    threat_intel_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated boolean value that specifies whether the ThreateIntelSet is
    # active or not.
    activate: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated URI of the file that contains the ThreateIntelSet. For example
    # (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that specifies the ThreatIntelSet that you want to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateThreatIntelSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
