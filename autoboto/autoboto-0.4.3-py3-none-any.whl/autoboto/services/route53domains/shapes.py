import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class BillingRecord(ShapeBase):
    """
    Information for one billing record.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "operation",
                "Operation",
                TypeInfo(typing.Union[str, OperationType]),
            ),
            (
                "invoice_id",
                "InvoiceId",
                TypeInfo(str),
            ),
            (
                "bill_date",
                "BillDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "price",
                "Price",
                TypeInfo(float),
            ),
        ]

    # The name of the domain that the billing record applies to. If the domain
    # name contains characters other than a-z, 0-9, and - (hyphen), such as an
    # internationalized domain name, then this value is in Punycode. For more
    # information, see [DNS Domain Name
    # Format](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html)
    # in the _Amazon Route 53 Developer Guidezzz_.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operation that you were charged for.
    operation: typing.Union[str, "OperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the invoice that is associated with the billing record.
    invoice_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the operation was billed, in Unix format.
    bill_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The price that you were charged for the operation, in US dollars.

    # Example value: 12.0
    price: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CheckDomainAvailabilityRequest(ShapeBase):
    """
    The CheckDomainAvailability request contains the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "idn_lang_code",
                "IdnLangCode",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to get availability for.

    # Constraints: The domain name can contain only the letters a through z, the
    # numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not
    # supported.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    idn_lang_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CheckDomainAvailabilityResponse(OutputShapeBase):
    """
    The CheckDomainAvailability response includes the following elements.
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
                "availability",
                "Availability",
                TypeInfo(typing.Union[str, DomainAvailability]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the domain name is available for registering.

    # You can register only domains designated as `AVAILABLE`.

    # Valid values:

    # AVAILABLE

    # The domain name is available.

    # AVAILABLE_RESERVED

    # The domain name is reserved under specific conditions.

    # AVAILABLE_PREORDER

    # The domain name is available and can be preordered.

    # DONT_KNOW

    # The TLD registry didn't reply with a definitive answer about whether the
    # domain name is available. Amazon Route 53 can return this response for a
    # variety of reasons, for example, the registry is performing maintenance.
    # Try again later.

    # PENDING

    # The TLD registry didn't return a response in the expected amount of time.
    # When the response is delayed, it usually takes just a few extra seconds.
    # You can resubmit the request immediately.

    # RESERVED

    # The domain name has been reserved for another person or organization.

    # UNAVAILABLE

    # The domain name is not available.

    # UNAVAILABLE_PREMIUM

    # The domain name is not available.

    # UNAVAILABLE_RESTRICTED

    # The domain name is forbidden.
    availability: typing.Union[str, "DomainAvailability"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CheckDomainTransferabilityRequest(ShapeBase):
    """
    The CheckDomainTransferability request contains the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "auth_code",
                "AuthCode",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to transfer to Amazon Route 53.

    # Constraints: The domain name can contain only the letters a through z, the
    # numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not
    # supported.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the registrar for the top-level domain (TLD) requires an authorization
    # code to transfer the domain, the code that you got from the current
    # registrar for the domain.
    auth_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CheckDomainTransferabilityResponse(OutputShapeBase):
    """
    The CheckDomainTransferability response includes the following elements.
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
                "transferability",
                "Transferability",
                TypeInfo(DomainTransferability),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about whether the specified domain
    # can be transferred to Amazon Route 53.
    transferability: "DomainTransferability" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContactDetail(ShapeBase):
    """
    ContactDetail includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "first_name",
                "FirstName",
                TypeInfo(str),
            ),
            (
                "last_name",
                "LastName",
                TypeInfo(str),
            ),
            (
                "contact_type",
                "ContactType",
                TypeInfo(typing.Union[str, ContactType]),
            ),
            (
                "organization_name",
                "OrganizationName",
                TypeInfo(str),
            ),
            (
                "address_line1",
                "AddressLine1",
                TypeInfo(str),
            ),
            (
                "address_line2",
                "AddressLine2",
                TypeInfo(str),
            ),
            (
                "city",
                "City",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "country_code",
                "CountryCode",
                TypeInfo(typing.Union[str, CountryCode]),
            ),
            (
                "zip_code",
                "ZipCode",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
            (
                "email",
                "Email",
                TypeInfo(str),
            ),
            (
                "fax",
                "Fax",
                TypeInfo(str),
            ),
            (
                "extra_params",
                "ExtraParams",
                TypeInfo(typing.List[ExtraParam]),
            ),
        ]

    # First name of contact.
    first_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last name of contact.
    last_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the contact is a person, company, association, or public
    # organization. If you choose an option other than `PERSON`, you must enter
    # an organization name, and you can't enable privacy protection for the
    # contact.
    contact_type: typing.Union[str, "ContactType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the organization for contact types other than `PERSON`.
    organization_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # First line of the contact's address.
    address_line1: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Second line of contact's address, if any.
    address_line2: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The city of the contact's address.
    city: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state or province of the contact's city.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Code for the country of the contact's address.
    country_code: typing.Union[str, "CountryCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The zip or postal code of the contact's address.
    zip_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number of the contact.

    # Constraints: Phone number must be specified in the format "+[country
    # dialing code].[number including any area code>]". For example, a US phone
    # number might appear as `"+1.1234567890"`.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Email address of the contact.
    email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Fax number of the contact.

    # Constraints: Phone number must be specified in the format "+[country
    # dialing code].[number including any area code]". For example, a US phone
    # number might appear as `"+1.1234567890"`.
    fax: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of name-value pairs for parameters required by certain top-level
    # domains.
    extra_params: typing.List["ExtraParam"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ContactType(str):
    PERSON = "PERSON"
    COMPANY = "COMPANY"
    ASSOCIATION = "ASSOCIATION"
    PUBLIC_BODY = "PUBLIC_BODY"
    RESELLER = "RESELLER"


class CountryCode(str):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GQ = "GQ"
    GR = "GR"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    ST = "ST"
    SV = "SV"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


@dataclasses.dataclass
class DeleteTagsForDomainRequest(ShapeBase):
    """
    The DeleteTagsForDomainRequest includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "tags_to_delete",
                "TagsToDelete",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The domain for which you want to delete one or more tags.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag keys to delete.
    tags_to_delete: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagsForDomainResponse(OutputShapeBase):
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
class DisableDomainAutoRenewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to disable automatic renewal for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableDomainAutoRenewResponse(OutputShapeBase):
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
class DisableDomainTransferLockRequest(ShapeBase):
    """
    The DisableDomainTransferLock request includes the following element.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to remove the transfer lock for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableDomainTransferLockResponse(OutputShapeBase):
    """
    The DisableDomainTransferLock response includes the following element.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DomainAvailability(str):
    AVAILABLE = "AVAILABLE"
    AVAILABLE_RESERVED = "AVAILABLE_RESERVED"
    AVAILABLE_PREORDER = "AVAILABLE_PREORDER"
    UNAVAILABLE = "UNAVAILABLE"
    UNAVAILABLE_PREMIUM = "UNAVAILABLE_PREMIUM"
    UNAVAILABLE_RESTRICTED = "UNAVAILABLE_RESTRICTED"
    RESERVED = "RESERVED"
    DONT_KNOW = "DONT_KNOW"


@dataclasses.dataclass
class DomainLimitExceeded(ShapeBase):
    """
    The number of domains has exceeded the allowed threshold for the account.
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

    # The number of domains has exceeded the allowed threshold for the account.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainSuggestion(ShapeBase):
    """
    Information about one suggested domain name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "availability",
                "Availability",
                TypeInfo(str),
            ),
        ]

    # A suggested domain name.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the domain name is available for registering.

    # You can register only the domains that are designated as `AVAILABLE`.

    # Valid values:

    # AVAILABLE

    # The domain name is available.

    # AVAILABLE_RESERVED

    # The domain name is reserved under specific conditions.

    # AVAILABLE_PREORDER

    # The domain name is available and can be preordered.

    # DONT_KNOW

    # The TLD registry didn't reply with a definitive answer about whether the
    # domain name is available. Amazon Route 53 can return this response for a
    # variety of reasons, for example, the registry is performing maintenance.
    # Try again later.

    # PENDING

    # The TLD registry didn't return a response in the expected amount of time.
    # When the response is delayed, it usually takes just a few extra seconds.
    # You can resubmit the request immediately.

    # RESERVED

    # The domain name has been reserved for another person or organization.

    # UNAVAILABLE

    # The domain name is not available.

    # UNAVAILABLE_PREMIUM

    # The domain name is not available.

    # UNAVAILABLE_RESTRICTED

    # The domain name is forbidden.
    availability: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainSummary(ShapeBase):
    """
    Summary information about one domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "auto_renew",
                "AutoRenew",
                TypeInfo(bool),
            ),
            (
                "transfer_lock",
                "TransferLock",
                TypeInfo(bool),
            ),
            (
                "expiry",
                "Expiry",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the domain that the summary information applies to.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the domain is automatically renewed upon expiration.
    auto_renew: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether a domain is locked from unauthorized transfer to another
    # party.
    transfer_lock: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Expiration date of the domain in Coordinated Universal Time (UTC).
    expiry: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DomainTransferability(ShapeBase):
    """
    A complex type that contains information about whether the specified domain can
    be transferred to Amazon Route 53.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transferable",
                "Transferable",
                TypeInfo(typing.Union[str, Transferable]),
            ),
        ]

    # Whether the domain name can be transferred to Amazon Route 53.

    # You can transfer only domains that have a value of `TRANSFERABLE` for
    # `Transferable`.

    # Valid values:

    # TRANSFERABLE

    # The domain name can be transferred to Amazon Route 53.

    # UNTRANSFERRABLE

    # The domain name can't be transferred to Amazon Route 53.

    # DONT_KNOW

    # Reserved for future use.
    transferable: typing.Union[str, "Transferable"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DuplicateRequest(ShapeBase):
    """
    The request is already in progress for the domain.
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

    # The request is already in progress for the domain.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableDomainAutoRenewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to enable automatic renewal for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableDomainAutoRenewResponse(OutputShapeBase):
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
class EnableDomainTransferLockRequest(ShapeBase):
    """
    A request to set the transfer lock for the specified domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to set the transfer lock for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableDomainTransferLockResponse(OutputShapeBase):
    """
    The EnableDomainTransferLock response includes the following elements.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExtraParam(ShapeBase):
    """
    ExtraParam includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, ExtraParamName]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # Name of the additional parameter required by the top-level domain. Here are
    # the top-level domains that require additional parameters and which
    # parameters they require:

    #   * **.com.au and .net.au:** `AU_ID_NUMBER` and `AU_ID_TYPE`

    #   * **.ca:** `BRAND_NUMBER`, `CA_LEGAL_TYPE`, and `CA_BUSINESS_ENTITY_TYPE`

    #   * **.es:** `ES_IDENTIFICATION`, `ES_IDENTIFICATION_TYPE`, and `ES_LEGAL_FORM`

    #   * **.fi:** `BIRTH_DATE_IN_YYYY_MM_DD`, `FI_BUSINESS_NUMBER`, `FI_ID_NUMBER`, `FI_NATIONALITY`, and `FI_ORGANIZATION_TYPE`

    #   * **.fr:** `BRAND_NUMBER`, `BIRTH_DEPARTMENT`, `BIRTH_DATE_IN_YYYY_MM_DD`, `BIRTH_COUNTRY`, and `BIRTH_CITY`

    #   * **.it:** `BIRTH_COUNTRY`, `IT_PIN`, and `IT_REGISTRANT_ENTITY_TYPE`

    #   * **.ru:** `BIRTH_DATE_IN_YYYY_MM_DD` and `RU_PASSPORT_DATA`

    #   * **.se:** `BIRTH_COUNTRY` and `SE_ID_NUMBER`

    #   * **.sg:** `SG_ID_NUMBER`

    #   * **.co.uk, .me.uk, and .org.uk:** `UK_CONTACT_TYPE` and `UK_COMPANY_NUMBER`

    # In addition, many TLDs require `VAT_NUMBER`.
    name: typing.Union[str, "ExtraParamName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Values corresponding to the additional parameter names required by some
    # top-level domains.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExtraParamName(str):
    DUNS_NUMBER = "DUNS_NUMBER"
    BRAND_NUMBER = "BRAND_NUMBER"
    BIRTH_DEPARTMENT = "BIRTH_DEPARTMENT"
    BIRTH_DATE_IN_YYYY_MM_DD = "BIRTH_DATE_IN_YYYY_MM_DD"
    BIRTH_COUNTRY = "BIRTH_COUNTRY"
    BIRTH_CITY = "BIRTH_CITY"
    DOCUMENT_NUMBER = "DOCUMENT_NUMBER"
    AU_ID_NUMBER = "AU_ID_NUMBER"
    AU_ID_TYPE = "AU_ID_TYPE"
    CA_LEGAL_TYPE = "CA_LEGAL_TYPE"
    CA_BUSINESS_ENTITY_TYPE = "CA_BUSINESS_ENTITY_TYPE"
    ES_IDENTIFICATION = "ES_IDENTIFICATION"
    ES_IDENTIFICATION_TYPE = "ES_IDENTIFICATION_TYPE"
    ES_LEGAL_FORM = "ES_LEGAL_FORM"
    FI_BUSINESS_NUMBER = "FI_BUSINESS_NUMBER"
    FI_ID_NUMBER = "FI_ID_NUMBER"
    FI_NATIONALITY = "FI_NATIONALITY"
    FI_ORGANIZATION_TYPE = "FI_ORGANIZATION_TYPE"
    IT_PIN = "IT_PIN"
    IT_REGISTRANT_ENTITY_TYPE = "IT_REGISTRANT_ENTITY_TYPE"
    RU_PASSPORT_DATA = "RU_PASSPORT_DATA"
    SE_ID_NUMBER = "SE_ID_NUMBER"
    SG_ID_NUMBER = "SG_ID_NUMBER"
    VAT_NUMBER = "VAT_NUMBER"
    UK_CONTACT_TYPE = "UK_CONTACT_TYPE"
    UK_COMPANY_NUMBER = "UK_COMPANY_NUMBER"


@dataclasses.dataclass
class GetContactReachabilityStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain for which you want to know whether the registrant
    # contact has confirmed that the email address is valid.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetContactReachabilityStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ReachabilityStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name for which you requested the reachability status.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the registrant contact has responded. Values include the following:

    # PENDING

    # We sent the confirmation email and haven't received a response yet.

    # DONE

    # We sent the email and got confirmation from the registrant contact.

    # EXPIRED

    # The time limit expired before the registrant contact responded.
    status: typing.Union[str, "ReachabilityStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDomainDetailRequest(ShapeBase):
    """
    The GetDomainDetail request includes the following element.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to get detailed information about.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainDetailResponse(OutputShapeBase):
    """
    The GetDomainDetail response includes the following elements.
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
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "nameservers",
                "Nameservers",
                TypeInfo(typing.List[Nameserver]),
            ),
            (
                "admin_contact",
                "AdminContact",
                TypeInfo(ContactDetail),
            ),
            (
                "registrant_contact",
                "RegistrantContact",
                TypeInfo(ContactDetail),
            ),
            (
                "tech_contact",
                "TechContact",
                TypeInfo(ContactDetail),
            ),
            (
                "auto_renew",
                "AutoRenew",
                TypeInfo(bool),
            ),
            (
                "admin_privacy",
                "AdminPrivacy",
                TypeInfo(bool),
            ),
            (
                "registrant_privacy",
                "RegistrantPrivacy",
                TypeInfo(bool),
            ),
            (
                "tech_privacy",
                "TechPrivacy",
                TypeInfo(bool),
            ),
            (
                "registrar_name",
                "RegistrarName",
                TypeInfo(str),
            ),
            (
                "who_is_server",
                "WhoIsServer",
                TypeInfo(str),
            ),
            (
                "registrar_url",
                "RegistrarUrl",
                TypeInfo(str),
            ),
            (
                "abuse_contact_email",
                "AbuseContactEmail",
                TypeInfo(str),
            ),
            (
                "abuse_contact_phone",
                "AbuseContactPhone",
                TypeInfo(str),
            ),
            (
                "registry_domain_id",
                "RegistryDomainId",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "UpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "expiration_date",
                "ExpirationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "reseller",
                "Reseller",
                TypeInfo(str),
            ),
            (
                "dns_sec",
                "DnsSec",
                TypeInfo(str),
            ),
            (
                "status_list",
                "StatusList",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a domain.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the domain.
    nameservers: typing.List["Nameserver"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides details about the domain administrative contact.
    admin_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides details about the domain registrant.
    registrant_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides details about the domain technical contact.
    tech_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the domain registration is set to renew automatically.
    auto_renew: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether contact information is concealed from WHOIS queries. If
    # the value is `true`, WHOIS ("who is") queries return contact information
    # either for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If the value is `false`,
    # WHOIS queries return the information that you entered for the admin
    # contact.
    admin_privacy: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether contact information is concealed from WHOIS queries. If
    # the value is `true`, WHOIS ("who is") queries return contact information
    # either for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If the value is `false`,
    # WHOIS queries return the information that you entered for the registrant
    # contact (domain owner).
    registrant_privacy: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether contact information is concealed from WHOIS queries. If
    # the value is `true`, WHOIS ("who is") queries return contact information
    # either for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If the value is `false`,
    # WHOIS queries return the information that you entered for the technical
    # contact.
    tech_privacy: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the registrar of the domain as identified in the registry. Domains
    # with a .com, .net, or .org TLD are registered by Amazon Registrar. All
    # other domains are registered by our registrar associate, Gandi. The value
    # for domains that are registered by Gandi is `"GANDI SAS"`.
    registrar_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified name of the WHOIS server that can answer the WHOIS
    # query for the domain.
    who_is_server: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Web address of the registrar.
    registrar_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Email address to contact to report incorrect contact information for a
    # domain, to report that the domain is being used to send spam, to report
    # that someone is cybersquatting on a domain name, or report some other type
    # of abuse.
    abuse_contact_email: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Phone number for reporting abuse.
    abuse_contact_phone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    registry_domain_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the domain was created as found in the response to a WHOIS
    # query. The date and time is in Coordinated Universal time (UTC).
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last updated date of the domain as found in the response to a WHOIS
    # query. The date and time is in Coordinated Universal time (UTC).
    updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the registration for the domain is set to expire. The date
    # and time is in Coordinated Universal time (UTC).
    expiration_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reseller of the domain. Domains registered or transferred using Amazon
    # Route 53 domains will have `"Amazon"` as the reseller.
    reseller: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    dns_sec: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of domain name status codes, also known as Extensible Provisioning
    # Protocol (EPP) status codes.

    # ICANN, the organization that maintains a central database of domain names,
    # has developed a set of domain name status codes that tell you the status of
    # a variety of operations on a domain name, for example, registering a domain
    # name, transferring a domain name to another registrar, renewing the
    # registration for a domain name, and so on. All registrars use this same set
    # of status codes.

    # For a current list of domain name status codes and an explanation of what
    # each code means, go to the [ICANN website](https://www.icann.org/) and
    # search for `epp status codes`. (Search on the ICANN website; web searches
    # sometimes return an old version of the document.)
    status_list: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDomainSuggestionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "suggestion_count",
                "SuggestionCount",
                TypeInfo(int),
            ),
            (
                "only_available",
                "OnlyAvailable",
                TypeInfo(bool),
            ),
        ]

    # A domain name that you want to use as the basis for a list of possible
    # domain names. The domain name must contain a top-level domain (TLD), such
    # as .com, that Amazon Route 53 supports. For a list of TLDs, see [Domains
    # that You Can Register with Amazon Route
    # 53](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-
    # list.html) in the _Amazon Route 53 Developer Guide_.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of suggested domain names that you want Amazon Route 53 to
    # return.
    suggestion_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `OnlyAvailable` is `true`, Amazon Route 53 returns only domain names
    # that are available. If `OnlyAvailable` is `false`, Amazon Route 53 returns
    # domain names without checking whether they're available to be registered.
    # To determine whether the domain is available, you can call
    # `checkDomainAvailability` for each suggestion.
    only_available: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainSuggestionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "suggestions_list",
                "SuggestionsList",
                TypeInfo(typing.List[DomainSuggestion]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of possible domain names. If you specified `true` for
    # `OnlyAvailable` in the request, the list contains only domains that are
    # available for registration.
    suggestions_list: typing.List["DomainSuggestion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOperationDetailRequest(ShapeBase):
    """
    The GetOperationDetail request includes the following element.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    # The identifier for the operation for which you want to get the status.
    # Amazon Route 53 returned the identifier in the response to the original
    # request.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationDetailResponse(OutputShapeBase):
    """
    The GetOperationDetail response includes the following elements.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, OperationStatus]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, OperationType]),
            ),
            (
                "submitted_date",
                "SubmittedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the requested operation in the system.
    status: typing.Union[str, "OperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed information on the status including possible errors.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a domain.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of operation that was requested.
    type: typing.Union[str, "OperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the request was submitted.
    submitted_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidInput(ShapeBase):
    """
    The requested item is not acceptable. For example, for an OperationId it might
    refer to the ID of an operation that is already completed. For a domain name, it
    might not be a valid domain name or belong to the requester account.
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

    # The requested item is not acceptable. For example, for an OperationId it
    # might refer to the ID of an operation that is already completed. For a
    # domain name, it might not be a valid domain name or belong to the requester
    # account.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDomainsRequest(ShapeBase):
    """
    The ListDomains request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # For an initial request for a list of domains, omit this element. If the
    # number of domains that are associated with the current AWS account is
    # greater than the value that you specified for `MaxItems`, you can use
    # `Marker` to return additional domains. Get the value of `NextPageMarker`
    # from the previous response, and submit another request that includes the
    # value of `NextPageMarker` in the `Marker` element.

    # Constraints: The marker must match the value specified in the previous
    # request.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of domains to be returned.

    # Default: 20
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDomainsResponse(OutputShapeBase):
    """
    The ListDomains response includes the following elements.
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
                "domains",
                "Domains",
                TypeInfo(typing.List[DomainSummary]),
            ),
            (
                "next_page_marker",
                "NextPageMarker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A summary of domains.
    domains: typing.List["DomainSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If there are more domains than you specified for `MaxItems` in the request,
    # submit another request and include the value of `NextPageMarker` in the
    # value of `Marker`.
    next_page_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListDomainsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOperationsRequest(ShapeBase):
    """
    The ListOperations request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "submitted_since",
                "SubmittedSince",
                TypeInfo(datetime.datetime),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # An optional parameter that lets you get information about all the
    # operations that you submitted after a specified date and time. Specify the
    # date and time in Coordinated Universal time (UTC).
    submitted_since: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For an initial request for a list of operations, omit this element. If the
    # number of operations that are not yet complete is greater than the value
    # that you specified for `MaxItems`, you can use `Marker` to return
    # additional operations. Get the value of `NextPageMarker` from the previous
    # response, and submit another request that includes the value of
    # `NextPageMarker` in the `Marker` element.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of domains to be returned.

    # Default: 20
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOperationsResponse(OutputShapeBase):
    """
    The ListOperations response includes the following elements.
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
                "operations",
                "Operations",
                TypeInfo(typing.List[OperationSummary]),
            ),
            (
                "next_page_marker",
                "NextPageMarker",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists summaries of the operations.
    operations: typing.List["OperationSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If there are more operations than you specified for `MaxItems` in the
    # request, submit another request and include the value of `NextPageMarker`
    # in the value of `Marker`.
    next_page_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListOperationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsForDomainRequest(ShapeBase):
    """
    The ListTagsForDomainRequest includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The domain for which you want to get a list of tags.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForDomainResponse(OutputShapeBase):
    """
    The ListTagsForDomain response includes the following elements.
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
                "tag_list",
                "TagList",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the tags that are associated with the specified domain.
    tag_list: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Nameserver(ShapeBase):
    """
    Nameserver includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "glue_ips",
                "GlueIps",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The fully qualified host name of the name server.

    # Constraint: Maximum 255 characters
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Glue IP address of a name server entry. Glue IP addresses are required only
    # when the name of the name server is a subdomain of the domain. For example,
    # if your domain is example.com and the name server for the domain is
    # ns.example.com, you need to specify the IP address for ns.example.com.

    # Constraints: The list can contain only one IPv4 and one IPv6 address.
    glue_ips: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationLimitExceeded(ShapeBase):
    """
    The number of operations or jobs running exceeded the allowed threshold for the
    account.
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

    # The number of operations or jobs running exceeded the allowed threshold for
    # the account.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OperationStatus(str):
    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    ERROR = "ERROR"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"


@dataclasses.dataclass
class OperationSummary(ShapeBase):
    """
    OperationSummary includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, OperationStatus]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, OperationType]),
            ),
            (
                "submitted_date",
                "SubmittedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Identifier returned to track the requested action.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the requested operation in the system.
    status: typing.Union[str, "OperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of the action requested.
    type: typing.Union[str, "OperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the request was submitted.
    submitted_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class OperationType(str):
    REGISTER_DOMAIN = "REGISTER_DOMAIN"
    DELETE_DOMAIN = "DELETE_DOMAIN"
    TRANSFER_IN_DOMAIN = "TRANSFER_IN_DOMAIN"
    UPDATE_DOMAIN_CONTACT = "UPDATE_DOMAIN_CONTACT"
    UPDATE_NAMESERVER = "UPDATE_NAMESERVER"
    CHANGE_PRIVACY_PROTECTION = "CHANGE_PRIVACY_PROTECTION"
    DOMAIN_LOCK = "DOMAIN_LOCK"
    ENABLE_AUTORENEW = "ENABLE_AUTORENEW"
    DISABLE_AUTORENEW = "DISABLE_AUTORENEW"
    ADD_DNSSEC = "ADD_DNSSEC"
    REMOVE_DNSSEC = "REMOVE_DNSSEC"
    EXPIRE_DOMAIN = "EXPIRE_DOMAIN"
    TRANSFER_OUT_DOMAIN = "TRANSFER_OUT_DOMAIN"
    CHANGE_DOMAIN_OWNER = "CHANGE_DOMAIN_OWNER"
    RENEW_DOMAIN = "RENEW_DOMAIN"
    PUSH_DOMAIN = "PUSH_DOMAIN"


class ReachabilityStatus(str):
    PENDING = "PENDING"
    DONE = "DONE"
    EXPIRED = "EXPIRED"


@dataclasses.dataclass
class RegisterDomainRequest(ShapeBase):
    """
    The RegisterDomain request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "duration_in_years",
                "DurationInYears",
                TypeInfo(int),
            ),
            (
                "admin_contact",
                "AdminContact",
                TypeInfo(ContactDetail),
            ),
            (
                "registrant_contact",
                "RegistrantContact",
                TypeInfo(ContactDetail),
            ),
            (
                "tech_contact",
                "TechContact",
                TypeInfo(ContactDetail),
            ),
            (
                "idn_lang_code",
                "IdnLangCode",
                TypeInfo(str),
            ),
            (
                "auto_renew",
                "AutoRenew",
                TypeInfo(bool),
            ),
            (
                "privacy_protect_admin_contact",
                "PrivacyProtectAdminContact",
                TypeInfo(bool),
            ),
            (
                "privacy_protect_registrant_contact",
                "PrivacyProtectRegistrantContact",
                TypeInfo(bool),
            ),
            (
                "privacy_protect_tech_contact",
                "PrivacyProtectTechContact",
                TypeInfo(bool),
            ),
        ]

    # The domain name that you want to register.

    # Constraints: The domain name can contain only the letters a through z, the
    # numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not
    # supported.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of years that you want to register the domain for. Domains are
    # registered for a minimum of one year. The maximum period depends on the
    # top-level domain. For the range of valid values for your domain, see
    # [Domains that You Can Register with Amazon Route
    # 53](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-
    # list.html) in the _Amazon Route 53 Developer Guide_.

    # Default: 1
    duration_in_years: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides detailed contact information.
    admin_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides detailed contact information.
    registrant_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides detailed contact information.
    tech_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    idn_lang_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the domain will be automatically renewed (`true`) or not
    # (`false`). Autorenewal only takes effect after the account is charged.

    # Default: `true`
    auto_renew: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the admin
    # contact.

    # Default: `true`
    privacy_protect_admin_contact: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the registrant
    # contact (the domain owner).

    # Default: `true`
    privacy_protect_registrant_contact: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the technical
    # contact.

    # Default: `true`
    privacy_protect_tech_contact: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterDomainResponse(OutputShapeBase):
    """
    The RegisterDomain response includes the following element.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RenewDomainRequest(ShapeBase):
    """
    A `RenewDomain` request includes the number of years that you want to renew for
    and the current expiration year.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "current_expiry_year",
                "CurrentExpiryYear",
                TypeInfo(int),
            ),
            (
                "duration_in_years",
                "DurationInYears",
                TypeInfo(int),
            ),
        ]

    # The name of the domain that you want to renew.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The year when the registration for the domain is set to expire. This value
    # must match the current expiration date for the domain.
    current_expiry_year: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of years that you want to renew the domain for. The maximum
    # number of years depends on the top-level domain. For the range of valid
    # values for your domain, see [Domains that You Can Register with Amazon
    # Route
    # 53](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-
    # list.html) in the _Amazon Route 53 Developer Guide_.

    # Default: 1
    duration_in_years: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RenewDomainResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResendContactReachabilityEmailRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain for which you want Amazon Route 53 to resend a
    # confirmation email to the registrant contact.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResendContactReachabilityEmailResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "email_address",
                "emailAddress",
                TypeInfo(str),
            ),
            (
                "is_already_verified",
                "isAlreadyVerified",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name for which you requested a confirmation email.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address for the registrant contact at the time that we sent the
    # verification email.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # `True` if the email address for the registrant contact has already been
    # verified, and `false` otherwise. If the email address has already been
    # verified, we don't send another confirmation email.
    is_already_verified: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetrieveDomainAuthCodeRequest(ShapeBase):
    """
    A request for the authorization code for the specified domain. To transfer a
    domain to another registrar, you provide this value to the new registrar.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to get an authorization code for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetrieveDomainAuthCodeResponse(OutputShapeBase):
    """
    The RetrieveDomainAuthCode response includes the following element.
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
                "auth_code",
                "AuthCode",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authorization code for the domain.
    auth_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TLDRulesViolation(ShapeBase):
    """
    The top-level domain does not support this operation.
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

    # The top-level domain does not support this operation.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Each tag includes the following elements.
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

    # The key (name) of a tag.

    # Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

    # Constraints: Each key can be 1-128 characters long.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of a tag.

    # Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"

    # Constraints: Each value can be 0-256 characters long.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TransferDomainRequest(ShapeBase):
    """
    The TransferDomain request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "duration_in_years",
                "DurationInYears",
                TypeInfo(int),
            ),
            (
                "admin_contact",
                "AdminContact",
                TypeInfo(ContactDetail),
            ),
            (
                "registrant_contact",
                "RegistrantContact",
                TypeInfo(ContactDetail),
            ),
            (
                "tech_contact",
                "TechContact",
                TypeInfo(ContactDetail),
            ),
            (
                "idn_lang_code",
                "IdnLangCode",
                TypeInfo(str),
            ),
            (
                "nameservers",
                "Nameservers",
                TypeInfo(typing.List[Nameserver]),
            ),
            (
                "auth_code",
                "AuthCode",
                TypeInfo(str),
            ),
            (
                "auto_renew",
                "AutoRenew",
                TypeInfo(bool),
            ),
            (
                "privacy_protect_admin_contact",
                "PrivacyProtectAdminContact",
                TypeInfo(bool),
            ),
            (
                "privacy_protect_registrant_contact",
                "PrivacyProtectRegistrantContact",
                TypeInfo(bool),
            ),
            (
                "privacy_protect_tech_contact",
                "PrivacyProtectTechContact",
                TypeInfo(bool),
            ),
        ]

    # The name of the domain that you want to transfer to Amazon Route 53.

    # Constraints: The domain name can contain only the letters a through z, the
    # numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not
    # supported.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of years that you want to register the domain for. Domains are
    # registered for a minimum of one year. The maximum period depends on the
    # top-level domain.

    # Default: 1
    duration_in_years: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides detailed contact information.
    admin_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides detailed contact information.
    registrant_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides detailed contact information.
    tech_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved for future use.
    idn_lang_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains details for the host and glue IP addresses.
    nameservers: typing.List["Nameserver"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authorization code for the domain. You get this value from the current
    # registrar.
    auth_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the domain will be automatically renewed (true) or not
    # (false). Autorenewal only takes effect after the account is charged.

    # Default: true
    auto_renew: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the admin
    # contact.

    # Default: `true`
    privacy_protect_admin_contact: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the registrant
    # contact (domain owner).

    # Default: `true`
    privacy_protect_registrant_contact: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the technical
    # contact.

    # Default: `true`
    privacy_protect_tech_contact: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TransferDomainResponse(OutputShapeBase):
    """
    The TranserDomain response includes the following element.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Transferable(str):
    """
    Whether the domain name can be transferred to Amazon Route 53.

    You can transfer only domains that have a value of `TRANSFERABLE` for
    `Transferable`.

    Valid values:

    TRANSFERABLE



    The domain name can be transferred to Amazon Route 53.

    UNTRANSFERRABLE



    The domain name can't be transferred to Amazon Route 53.

    DONT_KNOW



    Reserved for future use.
    """
    TRANSFERABLE = "TRANSFERABLE"
    UNTRANSFERABLE = "UNTRANSFERABLE"
    DONT_KNOW = "DONT_KNOW"


@dataclasses.dataclass
class UnsupportedTLD(ShapeBase):
    """
    Amazon Route 53 does not support this top-level domain (TLD).
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

    # Amazon Route 53 does not support this top-level domain (TLD).
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainContactPrivacyRequest(ShapeBase):
    """
    The UpdateDomainContactPrivacy request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "admin_privacy",
                "AdminPrivacy",
                TypeInfo(bool),
            ),
            (
                "registrant_privacy",
                "RegistrantPrivacy",
                TypeInfo(bool),
            ),
            (
                "tech_privacy",
                "TechPrivacy",
                TypeInfo(bool),
            ),
        ]

    # The name of the domain that you want to update the privacy setting for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the admin
    # contact.
    admin_privacy: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the registrant
    # contact (domain owner).
    registrant_privacy: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want to conceal contact information from WHOIS queries. If you
    # specify `true`, WHOIS ("who is") queries return contact information either
    # for Amazon Registrar (for .com, .net, and .org domains) or for our
    # registrar associate, Gandi (for all other TLDs). If you specify `false`,
    # WHOIS queries return the information that you entered for the technical
    # contact.
    tech_privacy: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainContactPrivacyResponse(OutputShapeBase):
    """
    The UpdateDomainContactPrivacy response includes the following element.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainContactRequest(ShapeBase):
    """
    The UpdateDomainContact request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "admin_contact",
                "AdminContact",
                TypeInfo(ContactDetail),
            ),
            (
                "registrant_contact",
                "RegistrantContact",
                TypeInfo(ContactDetail),
            ),
            (
                "tech_contact",
                "TechContact",
                TypeInfo(ContactDetail),
            ),
        ]

    # The name of the domain that you want to update contact information for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides detailed contact information.
    admin_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides detailed contact information.
    registrant_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides detailed contact information.
    tech_contact: "ContactDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDomainContactResponse(OutputShapeBase):
    """
    The UpdateDomainContact response includes the following element.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainNameserversRequest(ShapeBase):
    """
    Replaces the current set of name servers for the domain with the specified set
    of name servers. If you use Amazon Route 53 as your DNS service, specify the
    four name servers in the delegation set for the hosted zone for the domain.

    If successful, this operation returns an operation ID that you can use to track
    the progress and completion of the action. If the request is not completed
    successfully, the domain registrant will be notified by email.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "nameservers",
                "Nameservers",
                TypeInfo(typing.List[Nameserver]),
            ),
            (
                "fi_auth_key",
                "FIAuthKey",
                TypeInfo(str),
            ),
        ]

    # The name of the domain that you want to change name servers for.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of new name servers for the domain.
    nameservers: typing.List["Nameserver"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The authorization key for .fi domains
    fi_auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainNameserversResponse(OutputShapeBase):
    """
    The UpdateDomainNameservers response includes the following element.
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
                "operation_id",
                "OperationId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for tracking the progress of the request. To use this ID to
    # query the operation status, use GetOperationDetail.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTagsForDomainRequest(ShapeBase):
    """
    The UpdateTagsForDomainRequest includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "tags_to_update",
                "TagsToUpdate",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The domain for which you want to add or update tags.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the tag keys and values that you want to add or update. If you
    # specify a key that already exists, the corresponding value will be
    # replaced.
    tags_to_update: typing.List["Tag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTagsForDomainResponse(OutputShapeBase):
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
class ViewBillingRequest(ShapeBase):
    """
    The ViewBilling request includes the following elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start",
                "Start",
                TypeInfo(datetime.datetime),
            ),
            (
                "end",
                "End",
                TypeInfo(datetime.datetime),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # The beginning date and time for the time period for which you want a list
    # of billing records. Specify the date and time in Coordinated Universal time
    # (UTC).
    start: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end date and time for the time period for which you want a list of
    # billing records. Specify the date and time in Coordinated Universal time
    # (UTC).
    end: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For an initial request for a list of billing records, omit this element. If
    # the number of billing records that are associated with the current AWS
    # account during the specified period is greater than the value that you
    # specified for `MaxItems`, you can use `Marker` to return additional billing
    # records. Get the value of `NextPageMarker` from the previous response, and
    # submit another request that includes the value of `NextPageMarker` in the
    # `Marker` element.

    # Constraints: The marker must match the value of `NextPageMarker` that was
    # returned in the previous response.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of billing records to be returned.

    # Default: 20
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ViewBillingResponse(OutputShapeBase):
    """
    The ViewBilling response includes the following elements.
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
                "next_page_marker",
                "NextPageMarker",
                TypeInfo(str),
            ),
            (
                "billing_records",
                "BillingRecords",
                TypeInfo(typing.List[BillingRecord]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If there are more billing records than you specified for `MaxItems` in the
    # request, submit another request and include the value of `NextPageMarker`
    # in the value of `Marker`.
    next_page_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of billing records.
    billing_records: typing.List["BillingRecord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
