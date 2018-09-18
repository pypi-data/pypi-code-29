import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class ASN1Subject(ShapeBase):
    """
    Contains information about the certificate subject. The certificate can be one
    issued by your private certificate authority (CA) or it can be your private CA
    certificate. The **Subject** field in the certificate identifies the entity that
    owns or controls the public key in the certificate. The entity can be a user,
    computer, device, or service. The **Subject** must contain an X.500
    distinguished name (DN). A DN is a sequence of relative distinguished names
    (RDNs). The RDNs are separated by commas in the certificate. The DN must be
    unique for each entity, but your private CA can issue more than one certificate
    with the same DN to the same entity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "country",
                "Country",
                TypeInfo(str),
            ),
            (
                "organization",
                "Organization",
                TypeInfo(str),
            ),
            (
                "organizational_unit",
                "OrganizationalUnit",
                TypeInfo(str),
            ),
            (
                "distinguished_name_qualifier",
                "DistinguishedNameQualifier",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "common_name",
                "CommonName",
                TypeInfo(str),
            ),
            (
                "serial_number",
                "SerialNumber",
                TypeInfo(str),
            ),
            (
                "locality",
                "Locality",
                TypeInfo(str),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "surname",
                "Surname",
                TypeInfo(str),
            ),
            (
                "given_name",
                "GivenName",
                TypeInfo(str),
            ),
            (
                "initials",
                "Initials",
                TypeInfo(str),
            ),
            (
                "pseudonym",
                "Pseudonym",
                TypeInfo(str),
            ),
            (
                "generation_qualifier",
                "GenerationQualifier",
                TypeInfo(str),
            ),
        ]

    # Two-digit code that specifies the country in which the certificate subject
    # located.
    country: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Legal name of the organization with which the certificate subject is
    # affiliated.
    organization: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A subdivision or unit of the organization (such as sales or finance) with
    # which the certificate subject is affiliated.
    organizational_unit: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Disambiguating information for the certificate subject.
    distinguished_name_qualifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State in which the subject of the certificate is located.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Fully qualified domain name (FQDN) associated with the certificate subject.
    common_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate serial number.
    serial_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The locality (such as a city or town) in which the certificate subject is
    # located.
    locality: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A title such as Mr. or Ms., which is pre-pended to the name to refer
    # formally to the certificate subject.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Family name. In the US and the UK, for example, the surname of an
    # individual is ordered last. In Asian cultures the surname is typically
    # ordered first.
    surname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # First name.
    given_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Concatenation that typically contains the first letter of the **GivenName**
    # , the first letter of the middle name if one exists, and the first letter
    # of the **SurName**.
    initials: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Typically a shortened version of a longer **GivenName**. For example,
    # Jonathan is often shortened to John. Elizabeth is often shortened to Beth,
    # Liz, or Eliza.
    pseudonym: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Typically a qualifier appended to the name of an individual. Examples
    # include Jr. for junior, Sr. for senior, and III for third.
    generation_qualifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AuditReportResponseFormat(str):
    JSON = "JSON"
    CSV = "CSV"


class AuditReportStatus(str):
    CREATING = "CREATING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class CertificateAuthority(ShapeBase):
    """
    Contains information about your private certificate authority (CA). Your private
    CA can issue and revoke X.509 digital certificates. Digital certificates verify
    that the entity named in the certificate **Subject** field owns or controls the
    public key contained in the **Subject Public Key Info** field. Call the
    CreateCertificateAuthority operation to create your private CA. You must then
    call the GetCertificateAuthorityCertificate operation to retrieve a private CA
    certificate signing request (CSR). Take the CSR to your on-premises CA and sign
    it with the root CA certificate or a subordinate certificate. Call the
    ImportCertificateAuthorityCertificate operation to import the signed certificate
    into AWS Certificate Manager (ACM).
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
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_state_change_at",
                "LastStateChangeAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, CertificateAuthorityType]),
            ),
            (
                "serial",
                "Serial",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CertificateAuthorityStatus]),
            ),
            (
                "not_before",
                "NotBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "not_after",
                "NotAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(typing.Union[str, FailureReason]),
            ),
            (
                "certificate_authority_configuration",
                "CertificateAuthorityConfiguration",
                TypeInfo(CertificateAuthorityConfiguration),
            ),
            (
                "revocation_configuration",
                "RevocationConfiguration",
                TypeInfo(RevocationConfiguration),
            ),
            (
                "restorable_until",
                "RestorableUntil",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Amazon Resource Name (ARN) for your private certificate authority (CA). The
    # format is ` _12345678-1234-1234-1234-123456789012_ `.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time at which your private CA was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date and time at which your private CA was last updated.
    last_state_change_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of your private CA.
    type: typing.Union[str, "CertificateAuthorityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Serial number of your private CA.
    serial: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status of your private CA.
    status: typing.Union[str, "CertificateAuthorityStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date and time before which your private CA certificate is not valid.
    not_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Date and time after which your private CA certificate is not valid.
    not_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reason the request to create your private CA failed.
    failure_reason: typing.Union[str, "FailureReason"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Your private CA configuration.
    certificate_authority_configuration: "CertificateAuthorityConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the certificate revocation list (CRL) created and
    # maintained by your private CA.
    revocation_configuration: "RevocationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The period during which a deleted CA can be restored. For more information,
    # see the `PermanentDeletionTimeInDays` parameter of the
    # DeleteCertificateAuthorityRequest operation.
    restorable_until: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CertificateAuthorityConfiguration(ShapeBase):
    """
    Contains configuration information for your private certificate authority (CA).
    This includes information about the class of public key algorithm and the key
    pair that your private CA creates when it issues a certificate, the signature
    algorithm it uses used when issuing certificates, and its X.500 distinguished
    name. You must specify this information when you call the
    CreateCertificateAuthority operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_algorithm",
                "KeyAlgorithm",
                TypeInfo(typing.Union[str, KeyAlgorithm]),
            ),
            (
                "signing_algorithm",
                "SigningAlgorithm",
                TypeInfo(typing.Union[str, SigningAlgorithm]),
            ),
            (
                "subject",
                "Subject",
                TypeInfo(ASN1Subject),
            ),
        ]

    # Type of the public key algorithm and size, in bits, of the key pair that
    # your key pair creates when it issues a certificate.
    key_algorithm: typing.Union[str, "KeyAlgorithm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the algorithm your private CA uses to sign certificate requests.
    signing_algorithm: typing.Union[str, "SigningAlgorithm"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Structure that contains X.500 distinguished name information for your
    # private CA.
    subject: "ASN1Subject" = dataclasses.field(default=ShapeBase.NOT_SET, )


class CertificateAuthorityStatus(str):
    CREATING = "CREATING"
    PENDING_CERTIFICATE = "PENDING_CERTIFICATE"
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"


class CertificateAuthorityType(str):
    SUBORDINATE = "SUBORDINATE"


class CertificateBodyBlob(botocore.response.StreamingBody):
    pass


class CertificateChainBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CertificateMismatchException(ShapeBase):
    """
    The certificate authority certificate you are importing does not comply with
    conditions specified in the certificate that signed it.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConcurrentModificationException(ShapeBase):
    """
    A previous update to your private CA is still ongoing.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCertificateAuthorityAuditReportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "audit_report_response_format",
                "AuditReportResponseFormat",
                TypeInfo(typing.Union[str, AuditReportResponseFormat]),
            ),
        ]

    # Amazon Resource Name (ARN) of the CA to be audited. This is of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the S3 bucket that will contain the audit report.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Format in which to create the report. This can be either **JSON** or
    # **CSV**.
    audit_report_response_format: typing.Union[str, "AuditReportResponseFormat"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )


@dataclasses.dataclass
class CreateCertificateAuthorityAuditReportResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "audit_report_id",
                "AuditReportId",
                TypeInfo(str),
            ),
            (
                "s3_key",
                "S3Key",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An alphanumeric string that contains a report identifier.
    audit_report_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The **key** that uniquely identifies the report file in your S3 bucket.
    s3_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_configuration",
                "CertificateAuthorityConfiguration",
                TypeInfo(CertificateAuthorityConfiguration),
            ),
            (
                "certificate_authority_type",
                "CertificateAuthorityType",
                TypeInfo(typing.Union[str, CertificateAuthorityType]),
            ),
            (
                "revocation_configuration",
                "RevocationConfiguration",
                TypeInfo(RevocationConfiguration),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
        ]

    # Name and bit size of the private key algorithm, the name of the signing
    # algorithm, and X.500 certificate subject information.
    certificate_authority_configuration: "CertificateAuthorityConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the certificate authority. Currently, this must be
    # **SUBORDINATE**.
    certificate_authority_type: typing.Union[str, "CertificateAuthorityType"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # Contains a Boolean value that you can use to enable a certification
    # revocation list (CRL) for the CA, the name of the S3 bucket to which ACM
    # PCA will write the CRL, and an optional CNAME alias that you can use to
    # hide the name of your bucket in the **CRL Distribution Points** extension
    # of your CA certificate. For more information, see the CrlConfiguration
    # structure.
    revocation_configuration: "RevocationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Alphanumeric string that can be used to distinguish between calls to
    # **CreateCertificateAuthority**. Idempotency tokens time out after five
    # minutes. Therefore, if you call **CreateCertificateAuthority** multiple
    # times with the same idempotency token within a five minute period, ACM PCA
    # recognizes that you are requesting only one certificate. As a result, ACM
    # PCA issues only one. If you change the idempotency token for each call,
    # however, ACM PCA recognizes that you are requesting multiple certificates.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCertificateAuthorityResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If successful, the Amazon Resource Name (ARN) of the certificate authority
    # (CA). This is of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CrlConfiguration(ShapeBase):
    """
    Contains configuration information for a certificate revocation list (CRL). Your
    private certificate authority (CA) creates base CRLs. Delta CRLs are not
    supported. You can enable CRLs for your new or an existing private CA by setting
    the **Enabled** parameter to `true`. Your private CA writes CRLs to an S3 bucket
    that you specify in the **S3BucketName** parameter. You can hide the name of
    your bucket by specifying a value for the **CustomCname** parameter. Your
    private CA copies the CNAME or the S3 bucket name to the **CRL Distribution
    Points** extension of each certificate it issues. Your S3 bucket policy must
    give write permission to ACM PCA.

    Your private CA uses the value in the **ExpirationInDays** parameter to
    calculate the **nextUpdate** field in the CRL. The CRL is refreshed at 1/2 the
    age of next update or when a certificate is revoked. When a certificate is
    revoked, it is recorded in the next CRL that is generated and in the next audit
    report. Only time valid certificates are listed in the CRL. Expired certificates
    are not included.

    CRLs contain the following fields:

      * **Version** : The current version number defined in RFC 5280 is V2. The integer value is 0x1. 

      * **Signature Algorithm** : The name of the algorithm used to sign the CRL.

      * **Issuer** : The X.500 distinguished name of your private CA that issued the CRL.

      * **Last Update** : The issue date and time of this CRL.

      * **Next Update** : The day and time by which the next CRL will be issued.

      * **Revoked Certificates** : List of revoked certificates. Each list item contains the following information.

        * **Serial Number** : The serial number, in hexadecimal format, of the revoked certificate.

        * **Revocation Date** : Date and time the certificate was revoked.

        * **CRL Entry Extensions** : Optional extensions for the CRL entry.

          * **X509v3 CRL Reason Code** : Reason the certificate was revoked.

      * **CRL Extensions** : Optional extensions for the CRL.

        * **X509v3 Authority Key Identifier** : Identifies the public key associated with the private key used to sign the certificate.

        * **X509v3 CRL Number:** : Decimal sequence number for the CRL.

      * **Signature Algorithm** : Algorithm used by your private CA to sign the CRL.

      * **Signature Value** : Signature computed over the CRL.

    Certificate revocation lists created by ACM PCA are DER-encoded. You can use the
    following OpenSSL command to list a CRL.

    `openssl crl -inform DER -text -in _crl_path_ -noout`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "expiration_in_days",
                "ExpirationInDays",
                TypeInfo(int),
            ),
            (
                "custom_cname",
                "CustomCname",
                TypeInfo(str),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
        ]

    # Boolean value that specifies whether certificate revocation lists (CRLs)
    # are enabled. You can use this value to enable certificate revocation for a
    # new CA when you call the CreateCertificateAuthority operation or for an
    # existing CA when you call the UpdateCertificateAuthority operation.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of days until a certificate expires.
    expiration_in_days: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name inserted into the certificate **CRL Distribution Points** extension
    # that enables the use of an alias for the CRL distribution point. Use this
    # value if you don't want the name of your S3 bucket to be public.
    custom_cname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the S3 bucket that contains the CRL. If you do not provide a value
    # for the **CustomCname** argument, the name of your S3 bucket is placed into
    # the **CRL Distribution Points** extension of the issued certificate. You
    # can change the name of your bucket by calling the
    # UpdateCertificateAuthority operation. You must specify a bucket policy that
    # allows ACM PCA to write the CRL to your bucket.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CsrBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class DeleteCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "permanent_deletion_time_in_days",
                "PermanentDeletionTimeInDays",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must have the following form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of days to make a CA restorable after it has been deleted. This
    # can be anywhere from 7 to 30 days, with 30 being the default.
    permanent_deletion_time_in_days: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCertificateAuthorityAuditReportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "audit_report_id",
                "AuditReportId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the private CA. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The report ID returned by calling the CreateCertificateAuthorityAuditReport
    # operation.
    audit_report_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCertificateAuthorityAuditReportResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "audit_report_status",
                "AuditReportStatus",
                TypeInfo(typing.Union[str, AuditReportStatus]),
            ),
            (
                "s3_bucket_name",
                "S3BucketName",
                TypeInfo(str),
            ),
            (
                "s3_key",
                "S3Key",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether report creation is in progress, has succeeded, or has
    # failed.
    audit_report_status: typing.Union[str, "AuditReportStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Name of the S3 bucket that contains the report.
    s3_bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # S3 **key** that uniquely identifies the report file in your S3 bucket.
    s3_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time at which the report was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeCertificateAuthorityResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate_authority",
                "CertificateAuthority",
                TypeInfo(CertificateAuthority),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A CertificateAuthority structure that contains information about your
    # private CA.
    certificate_authority: "CertificateAuthority" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class FailureReason(str):
    REQUEST_TIMED_OUT = "REQUEST_TIMED_OUT"
    UNSUPPORTED_ALGORITHM = "UNSUPPORTED_ALGORITHM"
    OTHER = "OTHER"


@dataclasses.dataclass
class GetCertificateAuthorityCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of your private CA. This is of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCertificateAuthorityCertificateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "certificate_chain",
                "CertificateChain",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Base64-encoded certificate authority (CA) certificate.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Base64-encoded certificate chain that includes any intermediate
    # certificates and chains up to root on-premises certificate that you used to
    # sign your private CA certificate. The chain does not include your private
    # CA certificate.
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCertificateAuthorityCsrRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called the
    # CreateCertificateAuthority operation. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCertificateAuthorityCsrResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "csr",
                "Csr",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The base64 PEM-encoded certificate signing request (CSR) for your private
    # CA certificate.
    csr: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `.
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the issued certificate. The ARN contains the certificate serial
    # number and must be in the following form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ /certificate/
    # _286535153982981100925020015808220737245_ `
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCertificateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "certificate_chain",
                "CertificateChain",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The base64 PEM-encoded certificate specified by the `CertificateArn`
    # parameter.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base64 PEM-encoded certificate chain that chains up to the on-premises
    # root CA certificate that you used to sign your private CA certificate.
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportCertificateAuthorityCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(typing.Any),
            ),
            (
                "certificate_chain",
                "CertificateChain",
                TypeInfo(typing.Any),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The PEM-encoded certificate for your private CA. This must be signed by
    # using your on-premises CA.
    certificate: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A PEM-encoded file that contains all of your certificates, other than the
    # certificate you're importing, chaining up to your root CA. Your on-premises
    # root certificate is the last in the chain, and each certificate in the
    # chain signs the one preceding.
    certificate_chain: typing.Any = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidArgsException(ShapeBase):
    """
    One or more of the specified arguments was not valid.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidArnException(ShapeBase):
    """
    The requested Amazon Resource Name (ARN) does not refer to an existing resource.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    The token specified in the `NextToken` argument is not valid. Use the token
    returned from your previous call to ListCertificateAuthorities.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPolicyException(ShapeBase):
    """
    The S3 bucket policy is not valid. The policy must give ACM PCA rights to read
    from and write to the bucket and find the bucket location.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidStateException(ShapeBase):
    """
    The private CA is in a state during which a report cannot be generated.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTagException(ShapeBase):
    """
    The tag associated with the CA is not valid. The invalid argument is contained
    in the message field.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IssueCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "csr",
                "Csr",
                TypeInfo(typing.Any),
            ),
            (
                "signing_algorithm",
                "SigningAlgorithm",
                TypeInfo(typing.Union[str, SigningAlgorithm]),
            ),
            (
                "validity",
                "Validity",
                TypeInfo(Validity),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The certificate signing request (CSR) for the certificate you want to
    # issue. You can use the following OpenSSL command to create the CSR and a
    # 2048 bit RSA private key.

    # `openssl req -new -newkey rsa:2048 -days 365 -keyout
    # private/test_cert_priv_key.pem -out csr/test_cert_.csr`

    # If you have a configuration file, you can use the following OpenSSL
    # command. The `usr_cert` block in the configuration file contains your X509
    # version 3 extensions.

    # `openssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey
    # rsa:2048 -days -365 -keyout private/test_cert_priv_key.pem -out
    # csr/test_cert_.csr`
    csr: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the algorithm that will be used to sign the certificate to be
    # issued.
    signing_algorithm: typing.Union[str, "SigningAlgorithm"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The type of the validity period.
    validity: "Validity" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom string that can be used to distinguish between calls to the
    # **IssueCertificate** operation. Idempotency tokens time out after one hour.
    # Therefore, if you call **IssueCertificate** multiple times with the same
    # idempotency token within 5 minutes, ACM PCA recognizes that you are
    # requesting only one certificate and will issue only one. If you change the
    # idempotency token for each call, PCA recognizes that you are requesting
    # multiple certificates.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IssueCertificateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the issued certificate and the
    # certificate serial number. This is of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ /certificate/
    # _286535153982981100925020015808220737245_ `
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class KeyAlgorithm(str):
    RSA_2048 = "RSA_2048"
    RSA_4096 = "RSA_4096"
    EC_prime256v1 = "EC_prime256v1"
    EC_secp384r1 = "EC_secp384r1"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    An ACM PCA limit has been exceeded. See the exception message returned to
    determine the limit that was exceeded.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCertificateAuthoritiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # Use this parameter when paginating results in a subsequent request after
    # you receive a response with truncated results. Set it to the value of the
    # `NextToken` parameter from the response you just received.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter when paginating results to specify the maximum number of
    # items to return in the response on each page. If additional items exist
    # beyond the number you specify, the `NextToken` element is sent in the
    # response. Use this `NextToken` value in a subsequent request to retrieve
    # additional items.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCertificateAuthoritiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate_authorities",
                "CertificateAuthorities",
                TypeInfo(typing.List[CertificateAuthority]),
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

    # Summary information about each certificate authority you have created.
    certificate_authorities: typing.List["CertificateAuthority"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # When the list is truncated, this value is present and should be used for
    # the `NextToken` parameter in a subsequent pagination request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called the
    # CreateCertificateAuthority operation. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this parameter when paginating results in a subsequent request after
    # you receive a response with truncated results. Set it to the value of
    # **NextToken** from the response you just received.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter when paginating results to specify the maximum number of
    # items to return in the response. If additional items exist beyond the
    # number you specify, the **NextToken** element is sent in the response. Use
    # this **NextToken** value in a subsequent request to retrieve additional
    # items.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
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

    # The tags associated with your private CA.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the list is truncated, this value is present and should be used for
    # the **NextToken** parameter in a subsequent pagination request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MalformedCSRException(ShapeBase):
    """
    The certificate signing request is invalid.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MalformedCertificateException(ShapeBase):
    """
    One or more fields in the certificate are invalid.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestAlreadyProcessedException(ShapeBase):
    """
    Your request has already been completed.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestFailedException(ShapeBase):
    """
    The request has failed for an unspecified reason.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestInProgressException(ShapeBase):
    """
    Your request is already in progress.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    A resource such as a private CA, S3 bucket, certificate, or audit report cannot
    be found.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called the
    # CreateCertificateAuthority operation. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RevocationConfiguration(ShapeBase):
    """
    Certificate revocation information used by the CreateCertificateAuthority and
    UpdateCertificateAuthority operations. Your private certificate authority (CA)
    can create and maintain a certificate revocation list (CRL). A CRL contains
    information about certificates revoked by your CA. For more information, see
    RevokeCertificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "crl_configuration",
                "CrlConfiguration",
                TypeInfo(CrlConfiguration),
            ),
        ]

    # Configuration of the certificate revocation list (CRL), if any, maintained
    # by your private CA.
    crl_configuration: "CrlConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RevocationReason(str):
    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CERTIFICATE_AUTHORITY_COMPROMISE = "CERTIFICATE_AUTHORITY_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERSEDED = "SUPERSEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


@dataclasses.dataclass
class RevokeCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "certificate_serial",
                "CertificateSerial",
                TypeInfo(str),
            ),
            (
                "revocation_reason",
                "RevocationReason",
                TypeInfo(typing.Union[str, RevocationReason]),
            ),
        ]

    # Amazon Resource Name (ARN) of the private CA that issued the certificate to
    # be revoked. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Serial number of the certificate to be revoked. This must be in hexadecimal
    # format. You can retrieve the serial number by calling GetCertificate with
    # the Amazon Resource Name (ARN) of the certificate you want and the ARN of
    # your private CA. The **GetCertificate** operation retrieves the certificate
    # in the PEM format. You can use the following OpenSSL command to list the
    # certificate in text format and copy the hexadecimal serial number.

    # `openssl x509 -in _file_path_ -text -noout`

    # You can also copy the serial number from the console or use the
    # [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html)
    # operation in the _AWS Certificate Manager API Reference_.
    certificate_serial: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies why you revoked the certificate.
    revocation_reason: typing.Union[str, "RevocationReason"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


class SigningAlgorithm(str):
    SHA256WITHECDSA = "SHA256WITHECDSA"
    SHA384WITHECDSA = "SHA384WITHECDSA"
    SHA512WITHECDSA = "SHA512WITHECDSA"
    SHA256WITHRSA = "SHA256WITHRSA"
    SHA384WITHRSA = "SHA384WITHRSA"
    SHA512WITHRSA = "SHA512WITHRSA"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Tags are labels that you can use to identify and organize your private CAs. Each
    tag consists of a key and an optional value. You can associate up to 50 tags
    with a private CA. To add one or more tags to a private CA, call the
    TagCertificateAuthority operation. To remove a tag, call the
    UntagCertificateAuthority operation.
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

    # Key (name) of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of tags to be associated with the CA.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyTagsException(ShapeBase):
    """
    You can associate up to 50 tags with a private CA. Exception information is
    contained in the exception message field.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) that was returned when you called
    # CreateCertificateAuthority. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of tags to be removed from the CA.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "revocation_configuration",
                "RevocationConfiguration",
                TypeInfo(RevocationConfiguration),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CertificateAuthorityStatus]),
            ),
        ]

    # Amazon Resource Name (ARN) of the private CA that issued the certificate to
    # be revoked. This must be of the form:

    # `arn:aws:acm-pca: _region_ : _account_ :certificate-authority/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Revocation information for your private CA.
    revocation_configuration: "RevocationConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Status of your private CA.
    status: typing.Union[str, "CertificateAuthorityStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Validity(ShapeBase):
    """
    Length of time for which the certificate issued by your private certificate
    authority (CA), or by the private CA itself, is valid in days, months, or years.
    You can issue a certificate by calling the IssueCertificate operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(int),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, ValidityPeriodType]),
            ),
        ]

    # Time period.
    value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the `Value` parameter represents days, months, or years.
    type: typing.Union[str, "ValidityPeriodType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ValidityPeriodType(str):
    END_DATE = "END_DATE"
    ABSOLUTE = "ABSOLUTE"
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"
