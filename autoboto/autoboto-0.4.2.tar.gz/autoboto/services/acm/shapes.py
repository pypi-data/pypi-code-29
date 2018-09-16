import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddTagsToCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # String that contains the ARN of the ACM certificate to which the tag is to
    # be applied. This must be of the form:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value pair that defines the tag. The tag value is optional.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class CertificateBodyBlob(botocore.response.StreamingBody):
    pass


class CertificateChainBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CertificateDetail(ShapeBase):
    """
    Contains metadata about an ACM certificate. This structure is returned in the
    response to a DescribeCertificate request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "subject_alternative_names",
                "SubjectAlternativeNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "domain_validation_options",
                "DomainValidationOptions",
                TypeInfo(typing.List[DomainValidation]),
            ),
            (
                "serial",
                "Serial",
                TypeInfo(str),
            ),
            (
                "subject",
                "Subject",
                TypeInfo(str),
            ),
            (
                "issuer",
                "Issuer",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "issued_at",
                "IssuedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "imported_at",
                "ImportedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, CertificateStatus]),
            ),
            (
                "revoked_at",
                "RevokedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "revocation_reason",
                "RevocationReason",
                TypeInfo(typing.Union[str, RevocationReason]),
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
                "key_algorithm",
                "KeyAlgorithm",
                TypeInfo(typing.Union[str, KeyAlgorithm]),
            ),
            (
                "signature_algorithm",
                "SignatureAlgorithm",
                TypeInfo(str),
            ),
            (
                "in_use_by",
                "InUseBy",
                TypeInfo(typing.List[str]),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(typing.Union[str, FailureReason]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, CertificateType]),
            ),
            (
                "renewal_summary",
                "RenewalSummary",
                TypeInfo(RenewalSummary),
            ),
            (
                "key_usages",
                "KeyUsages",
                TypeInfo(typing.List[KeyUsage]),
            ),
            (
                "extended_key_usages",
                "ExtendedKeyUsages",
                TypeInfo(typing.List[ExtendedKeyUsage]),
            ),
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "renewal_eligibility",
                "RenewalEligibility",
                TypeInfo(typing.Union[str, RenewalEligibility]),
            ),
            (
                "options",
                "Options",
                TypeInfo(CertificateOptions),
            ),
        ]

    # The Amazon Resource Name (ARN) of the certificate. For more information
    # about ARNs, see [Amazon Resource Names (ARNs) and AWS Service
    # Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) in the _AWS General Reference_.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain name for the certificate, such as
    # www.example.com or example.com.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more domain names (subject alternative names) included in the
    # certificate. This list contains the domain names that are bound to the
    # public key that is contained in the certificate. The subject alternative
    # names include the canonical domain name (CN) of the certificate and
    # additional domain names that can be used to connect to the website.
    subject_alternative_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains information about the initial validation of each domain name that
    # occurs as a result of the RequestCertificate request. This field exists
    # only when the certificate type is `AMAZON_ISSUED`.
    domain_validation_options: typing.List["DomainValidation"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The serial number of the certificate.
    serial: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the entity that is associated with the public key contained in
    # the certificate.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the certificate authority that issued and signed the
    # certificate.
    issuer: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time at which the certificate was requested. This value exists only
    # when the certificate type is `AMAZON_ISSUED`.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the certificate was issued. This value exists only when
    # the certificate type is `AMAZON_ISSUED`.
    issued_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time at which the certificate was imported. This value exists
    # only when the certificate type is `IMPORTED`.
    imported_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the certificate.
    status: typing.Union[str, "CertificateStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time at which the certificate was revoked. This value exists only when
    # the certificate status is `REVOKED`.
    revoked_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason the certificate was revoked. This value exists only when the
    # certificate status is `REVOKED`.
    revocation_reason: typing.Union[str, "RevocationReason"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The time before which the certificate is not valid.
    not_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time after which the certificate is not valid.
    not_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The algorithm that was used to generate the public-private key pair.
    key_algorithm: typing.Union[str, "KeyAlgorithm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The algorithm that was used to sign the certificate.
    signature_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ARNs for the AWS resources that are using the certificate. A
    # certificate can be used by multiple AWS resources.
    in_use_by: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason the certificate request failed. This value exists only when the
    # certificate status is `FAILED`. For more information, see [Certificate
    # Request
    # Failed](http://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-
    # failed) in the _AWS Certificate Manager User Guide_.
    failure_reason: typing.Union[str, "FailureReason"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The source of the certificate. For certificates provided by ACM, this value
    # is `AMAZON_ISSUED`. For certificates that you imported with
    # ImportCertificate, this value is `IMPORTED`. ACM does not provide [managed
    # renewal](http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html)
    # for imported certificates. For more information about the differences
    # between certificates that you import and those that ACM provides, see
    # [Importing
    # Certificates](http://docs.aws.amazon.com/acm/latest/userguide/import-
    # certificate.html) in the _AWS Certificate Manager User Guide_.
    type: typing.Union[str, "CertificateType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains information about the status of ACM's [managed
    # renewal](http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html)
    # for the certificate. This field exists only when the certificate type is
    # `AMAZON_ISSUED`.
    renewal_summary: "RenewalSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of Key Usage X.509 v3 extension objects. Each object is a string
    # value that identifies the purpose of the public key contained in the
    # certificate. Possible extension values include DIGITAL_SIGNATURE,
    # KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.
    key_usages: typing.List["KeyUsage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains a list of Extended Key Usage X.509 v3 extension objects. Each
    # object specifies a purpose for which the certificate public key can be used
    # and consists of a name and an object identifier (OID).
    extended_key_usages: typing.List["ExtendedKeyUsage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the ACM PCA private certificate authority
    # (CA) that issued the certificate. This has the following format:

    # `arn:aws:acm-pca:region:account:certificate-
    # authority/12345678-1234-1234-1234-123456789012`
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the certificate is eligible for renewal.
    renewal_eligibility: typing.Union[str, "RenewalEligibility"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Value that specifies whether to add the certificate to a transparency log.
    # Certificate transparency makes it possible to detect SSL certificates that
    # have been mistakenly or maliciously issued. A browser might respond to
    # certificate that has not been logged by showing an error message. The logs
    # are cryptographically secure.
    options: "CertificateOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CertificateOptions(ShapeBase):
    """
    Structure that contains options for your certificate. Currently, you can use
    this only to specify whether to opt in to or out of certificate transparency
    logging. Some browsers require that public certificates issued for your domain
    be recorded in a log. Certificates that are not logged typically generate a
    browser error. Transparency makes it possible for you to detect SSL/TLS
    certificates that have been mistakenly or maliciously issued for your domain.
    For general information, see [Certificate Transparency
    Logging](http://docs.aws.amazon.com/acm/latest/userguide/acm-
    concepts.html#concept-transparency).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_transparency_logging_preference",
                "CertificateTransparencyLoggingPreference",
                TypeInfo(
                    typing.Union[str, CertificateTransparencyLoggingPreference]
                ),
            ),
        ]

    # You can opt out of certificate transparency logging by specifying the
    # `DISABLED` option. Opt in by specifying `ENABLED`.
    certificate_transparency_logging_preference: typing.Union[
        str, "CertificateTransparencyLoggingPreference"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class CertificateStatus(str):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"


@dataclasses.dataclass
class CertificateSummary(ShapeBase):
    """
    This structure is returned in the response object of ListCertificates action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) of the certificate. This is of the form:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Fully qualified domain name (FQDN), such as www.example.com or example.com,
    # for the certificate.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CertificateTransparencyLoggingPreference(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CertificateType(str):
    IMPORTED = "IMPORTED"
    AMAZON_ISSUED = "AMAZON_ISSUED"
    PRIVATE = "PRIVATE"


@dataclasses.dataclass
class DeleteCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # String that contains the ARN of the ACM certificate to be deleted. This
    # must be of the form:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have
    # the following form:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCertificateResponse(OutputShapeBase):
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
                TypeInfo(CertificateDetail),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Metadata about an ACM certificate.
    certificate: "CertificateDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DomainStatus(str):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class DomainValidation(ShapeBase):
    """
    Contains information about the validation of each domain name in the
    certificate.
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
                "validation_emails",
                "ValidationEmails",
                TypeInfo(typing.List[str]),
            ),
            (
                "validation_domain",
                "ValidationDomain",
                TypeInfo(str),
            ),
            (
                "validation_status",
                "ValidationStatus",
                TypeInfo(typing.Union[str, DomainStatus]),
            ),
            (
                "resource_record",
                "ResourceRecord",
                TypeInfo(ResourceRecord),
            ),
            (
                "validation_method",
                "ValidationMethod",
                TypeInfo(typing.Union[str, ValidationMethod]),
            ),
        ]

    # A fully qualified domain name (FQDN) in the certificate. For example,
    # `www.example.com` or `example.com`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of email addresses that ACM used to send domain validation emails.
    validation_emails: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name that ACM used to send domain validation emails.
    validation_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The validation status of the domain name. This can be one of the following
    # values:

    #   * `PENDING_VALIDATION`

    #   * ``SUCCESS

    #   * ``FAILED
    validation_status: typing.Union[str, "DomainStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the CNAME record that you add to your DNS database for domain
    # validation. For more information, see [Use DNS to Validate Domain
    # Ownership](http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-
    # dns.html).
    resource_record: "ResourceRecord" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the domain validation method.
    validation_method: typing.Union[str, "ValidationMethod"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class DomainValidationOption(ShapeBase):
    """
    Contains information about the domain names that you want ACM to use to send you
    emails that enable you to validate domain ownership.
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
                "validation_domain",
                "ValidationDomain",
                TypeInfo(str),
            ),
        ]

    # A fully qualified domain name (FQDN) in the certificate request.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain name that you want ACM to use to send you validation emails.
    # This domain name is the suffix of the email addresses that you want ACM to
    # use. This must be the same as the `DomainName` value or a superdomain of
    # the `DomainName` value. For example, if you request a certificate for
    # `testing.example.com`, you can specify `example.com` for this value. In
    # that case, ACM sends domain validation emails to the following five
    # addresses:

    #   * admin@example.com

    #   * administrator@example.com

    #   * hostmaster@example.com

    #   * postmaster@example.com

    #   * webmaster@example.com
    validation_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "passphrase",
                "Passphrase",
                TypeInfo(typing.Any),
            ),
        ]

    # An Amazon Resource Name (ARN) of the issued certificate. This must be of
    # the form:

    # `arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Passphrase to associate with the encrypted exported private key. If you
    # want to later decrypt the private key, you must have the passphrase. You
    # can use the following OpenSSL command to decrypt a private key:

    # `openssl rsa -in encrypted_key.pem -out decrypted_key.pem`
    passphrase: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportCertificateResponse(OutputShapeBase):
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
            (
                "private_key",
                "PrivateKey",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The base64 PEM-encoded certificate.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base64 PEM-encoded certificate chain. This does not include the
    # certificate that you are exporting.
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The PEM-encoded private key associated with the public key in the
    # certificate.
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExtendedKeyUsage(ShapeBase):
    """
    The Extended Key Usage X.509 v3 extension defines one or more purposes for which
    the public key can be used. This is in addition to or in place of the basic
    purposes specified by the Key Usage extension.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, ExtendedKeyUsageName]),
            ),
            (
                "oid",
                "OID",
                TypeInfo(str),
            ),
        ]

    # The name of an Extended Key Usage value.
    name: typing.Union[str, "ExtendedKeyUsageName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object identifier (OID) for the extension value. OIDs are strings of
    # numbers separated by periods. The following OIDs are defined in RFC 3280
    # and RFC 5280.

    #   * `1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)`

    #   * `1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)`

    #   * `1.3.6.1.5.5.7.3.3 (CODE_SIGNING)`

    #   * `1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)`

    #   * `1.3.6.1.5.5.7.3.8 (TIME_STAMPING)`

    #   * `1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)`

    #   * `1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)`

    #   * `1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)`

    #   * `1.3.6.1.5.5.7.3.7 (IPSEC_USER)`
    oid: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExtendedKeyUsageName(str):
    TLS_WEB_SERVER_AUTHENTICATION = "TLS_WEB_SERVER_AUTHENTICATION"
    TLS_WEB_CLIENT_AUTHENTICATION = "TLS_WEB_CLIENT_AUTHENTICATION"
    CODE_SIGNING = "CODE_SIGNING"
    EMAIL_PROTECTION = "EMAIL_PROTECTION"
    TIME_STAMPING = "TIME_STAMPING"
    OCSP_SIGNING = "OCSP_SIGNING"
    IPSEC_END_SYSTEM = "IPSEC_END_SYSTEM"
    IPSEC_TUNNEL = "IPSEC_TUNNEL"
    IPSEC_USER = "IPSEC_USER"
    ANY = "ANY"
    NONE = "NONE"
    CUSTOM = "CUSTOM"


class FailureReason(str):
    NO_AVAILABLE_CONTACTS = "NO_AVAILABLE_CONTACTS"
    ADDITIONAL_VERIFICATION_REQUIRED = "ADDITIONAL_VERIFICATION_REQUIRED"
    DOMAIN_NOT_ALLOWED = "DOMAIN_NOT_ALLOWED"
    INVALID_PUBLIC_DOMAIN = "INVALID_PUBLIC_DOMAIN"
    CAA_ERROR = "CAA_ERROR"
    PCA_LIMIT_EXCEEDED = "PCA_LIMIT_EXCEEDED"
    PCA_INVALID_ARN = "PCA_INVALID_ARN"
    PCA_INVALID_STATE = "PCA_INVALID_STATE"
    PCA_REQUEST_FAILED = "PCA_REQUEST_FAILED"
    PCA_RESOURCE_NOT_FOUND = "PCA_RESOURCE_NOT_FOUND"
    PCA_INVALID_ARGS = "PCA_INVALID_ARGS"
    OTHER = "OTHER"


@dataclasses.dataclass
class Filters(ShapeBase):
    """
    This structure can be used in the ListCertificates action to filter the output
    of the certificate list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "extended_key_usage",
                "extendedKeyUsage",
                TypeInfo(typing.List[typing.Union[str, ExtendedKeyUsageName]]),
            ),
            (
                "key_usage",
                "keyUsage",
                TypeInfo(typing.List[typing.Union[str, KeyUsageName]]),
            ),
            (
                "key_types",
                "keyTypes",
                TypeInfo(typing.List[typing.Union[str, KeyAlgorithm]]),
            ),
        ]

    # Specify one or more ExtendedKeyUsage extension values.
    extended_key_usage: typing.List[typing.Union[str, "ExtendedKeyUsageName"]
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Specify one or more KeyUsage extension values.
    key_usage: typing.List[typing.Union[str, "KeyUsageName"]
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # Specify one or more algorithms that can be used to generate key pairs.
    key_types: typing.List[typing.Union[str, "KeyAlgorithm"]
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )


@dataclasses.dataclass
class GetCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # String that contains a certificate ARN in the following format:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
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

    # String that contains the ACM certificate represented by the ARN specified
    # at input.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate chain that contains the root certificate issued by the
    # certificate authority (CA).
    certificate_chain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate",
                "Certificate",
                TypeInfo(typing.Any),
            ),
            (
                "private_key",
                "PrivateKey",
                TypeInfo(typing.Any),
            ),
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "certificate_chain",
                "CertificateChain",
                TypeInfo(typing.Any),
            ),
        ]

    # The certificate to import.
    certificate: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private key that matches the public key in the certificate.
    private_key: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The [Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) of an imported certificate to replace. To import a new
    # certificate, omit this field.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The PEM encoded certificate chain.
    certificate_chain: typing.Any = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImportCertificateResponse(OutputShapeBase):
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

    # The [Amazon Resource Name
    # (ARN)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
    # namespaces.html) of the imported certificate.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


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
class InvalidDomainValidationOptionsException(ShapeBase):
    """
    One or more values in the DomainValidationOption structure is incorrect.
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
    Processing has reached an invalid state.
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
    One or both of the values that make up the key-value pair is not valid. For
    example, you cannot specify a tag value that begins with `aws:`.
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


class KeyAlgorithm(str):
    RSA_2048 = "RSA_2048"
    RSA_1024 = "RSA_1024"
    RSA_4096 = "RSA_4096"
    EC_prime256v1 = "EC_prime256v1"
    EC_secp384r1 = "EC_secp384r1"
    EC_secp521r1 = "EC_secp521r1"


@dataclasses.dataclass
class KeyUsage(ShapeBase):
    """
    The Key Usage X.509 v3 extension defines the purpose of the public key contained
    in the certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(typing.Union[str, KeyUsageName]),
            ),
        ]

    # A string value that contains a Key Usage extension name.
    name: typing.Union[str, "KeyUsageName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class KeyUsageName(str):
    DIGITAL_SIGNATURE = "DIGITAL_SIGNATURE"
    NON_REPUDIATION = "NON_REPUDIATION"
    KEY_ENCIPHERMENT = "KEY_ENCIPHERMENT"
    DATA_ENCIPHERMENT = "DATA_ENCIPHERMENT"
    KEY_AGREEMENT = "KEY_AGREEMENT"
    CERTIFICATE_SIGNING = "CERTIFICATE_SIGNING"
    CRL_SIGNING = "CRL_SIGNING"
    ENCIPHER_ONLY = "ENCIPHER_ONLY"
    DECIPHER_ONLY = "DECIPHER_ONLY"
    ANY = "ANY"
    CUSTOM = "CUSTOM"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    An ACM limit has been exceeded.
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
class ListCertificatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_statuses",
                "CertificateStatuses",
                TypeInfo(typing.List[typing.Union[str, CertificateStatus]]),
            ),
            (
                "includes",
                "Includes",
                TypeInfo(Filters),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
        ]

    # Filter the certificate list by status value.
    certificate_statuses: typing.List[typing.Union[str, "CertificateStatus"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Filter the certificate list. For more information, see the Filters
    # structure.
    includes: "Filters" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter only when paginating results and only in a subsequent
    # request after you receive a response with truncated results. Set it to the
    # value of `NextToken` from the response you just received.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter when paginating results to specify the maximum number of
    # items to return in the response. If additional items exist beyond the
    # number you specify, the `NextToken` element is sent in the response. Use
    # this `NextToken` value in a subsequent request to retrieve additional
    # items.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCertificatesResponse(OutputShapeBase):
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
                "certificate_summary_list",
                "CertificateSummaryList",
                TypeInfo(typing.List[CertificateSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the list is truncated, this value is present and contains the value to
    # use for the `NextToken` parameter in a subsequent pagination request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ACM certificates.
    certificate_summary_list: typing.List["CertificateSummary"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    def paginate(self,
                ) -> typing.Generator["ListCertificatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsForCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
        ]

    # String that contains the ARN of the ACM certificate for which you want to
    # list the tags. This must have the following form:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForCertificateResponse(OutputShapeBase):
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The key-value pairs that define the applied tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class PassphraseBlob(botocore.response.StreamingBody):
    pass


class PrivateKeyBlob(botocore.response.StreamingBody):
    pass


class RecordType(str):
    CNAME = "CNAME"


@dataclasses.dataclass
class RemoveTagsFromCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # String that contains the ARN of the ACM Certificate with one or more tags
    # that you want to remove. This must be of the form:

    # `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

    # For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS
    # Service Namespaces](http://docs.aws.amazon.com/general/latest/gr/aws-arns-
    # and-namespaces.html).
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key-value pair that defines the tag to remove.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


class RenewalEligibility(str):
    ELIGIBLE = "ELIGIBLE"
    INELIGIBLE = "INELIGIBLE"


class RenewalStatus(str):
    PENDING_AUTO_RENEWAL = "PENDING_AUTO_RENEWAL"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class RenewalSummary(ShapeBase):
    """
    Contains information about the status of ACM's [managed
    renewal](http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for
    the certificate. This structure exists only when the certificate type is
    `AMAZON_ISSUED`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "renewal_status",
                "RenewalStatus",
                TypeInfo(typing.Union[str, RenewalStatus]),
            ),
            (
                "domain_validation_options",
                "DomainValidationOptions",
                TypeInfo(typing.List[DomainValidation]),
            ),
        ]

    # The status of ACM's [managed
    # renewal](http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html)
    # of the certificate.
    renewal_status: typing.Union[str, "RenewalStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains information about the validation of each domain name in the
    # certificate, as it pertains to ACM's [managed
    # renewal](http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html).
    # This is different from the initial validation that occurs as a result of
    # the RequestCertificate request. This field exists only when the certificate
    # type is `AMAZON_ISSUED`.
    domain_validation_options: typing.List["DomainValidation"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class RequestCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "validation_method",
                "ValidationMethod",
                TypeInfo(typing.Union[str, ValidationMethod]),
            ),
            (
                "subject_alternative_names",
                "SubjectAlternativeNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "idempotency_token",
                "IdempotencyToken",
                TypeInfo(str),
            ),
            (
                "domain_validation_options",
                "DomainValidationOptions",
                TypeInfo(typing.List[DomainValidationOption]),
            ),
            (
                "options",
                "Options",
                TypeInfo(CertificateOptions),
            ),
            (
                "certificate_authority_arn",
                "CertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    # Fully qualified domain name (FQDN), such as www.example.com, that you want
    # to secure with an ACM certificate. Use an asterisk (*) to create a wildcard
    # certificate that protects several sites in the same domain. For example,
    # *.example.com protects www.example.com, site.example.com, and
    # images.example.com.

    # The first domain name you enter cannot exceed 63 octets, including periods.
    # Each subsequent Subject Alternative Name (SAN), however, can be up to 253
    # octets in length.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The method you want to use if you are requesting a public certificate to
    # validate that you own or control domain. You can [validate with
    # DNS](http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-
    # dns.html) or [validate with
    # email](http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-
    # email.html). We recommend that you use DNS validation.
    validation_method: typing.Union[str, "ValidationMethod"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Additional FQDNs to be included in the Subject Alternative Name extension
    # of the ACM certificate. For example, add the name www.example.net to a
    # certificate for which the `DomainName` field is www.example.com if users
    # can reach your site by using either name. The maximum number of domain
    # names that you can add to an ACM certificate is 100. However, the initial
    # limit is 10 domain names. If you need more than 10 names, you must request
    # a limit increase. For more information, see
    # [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html).

    # The maximum length of a SAN DNS name is 253 octets. The name is made up of
    # multiple labels separated by periods. No label can be longer than 63
    # octets. Consider the following examples:

    #   * `(63 octets).(63 octets).(63 octets).(61 octets)` is legal because the total length is 253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets.

    #   * `(64 octets).(63 octets).(63 octets).(61 octets)` is not legal because the total length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets.

    #   * `(63 octets).(63 octets).(63 octets).(62 octets)` is not legal because the total length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets.
    subject_alternative_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Customer chosen string that can be used to distinguish between calls to
    # `RequestCertificate`. Idempotency tokens time out after one hour.
    # Therefore, if you call `RequestCertificate` multiple times with the same
    # idempotency token within one hour, ACM recognizes that you are requesting
    # only one certificate and will issue only one. If you change the idempotency
    # token for each call, ACM recognizes that you are requesting multiple
    # certificates.
    idempotency_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain name that you want ACM to use to send you emails so that you can
    # validate domain ownership.
    domain_validation_options: typing.List["DomainValidationOption"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Currently, you can use this parameter to specify whether to add the
    # certificate to a certificate transparency log. Certificate transparency
    # makes it possible to detect SSL/TLS certificates that have been mistakenly
    # or maliciously issued. Certificates that have not been logged typically
    # produce an error message in a browser. For more information, see [Opting
    # Out of Certificate Transparency
    # Logging](http://docs.aws.amazon.com/acm/latest/userguide/acm-
    # bestpractices.html#best-practices-transparency).
    options: "CertificateOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the private certificate authority (CA)
    # that will be used to issue the certificate. If you do not provide an ARN
    # and you are trying to request a private certificate, ACM will attempt to
    # issue a public certificate. For more information about private CAs, see the
    # [AWS Certificate Manager Private Certificate Authority
    # (PCA)](http://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html)
    # user guide. The ARN must have the following form:

    # `arn:aws:acm-pca:region:account:certificate-
    # authority/12345678-1234-1234-1234-123456789012`
    certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RequestCertificateResponse(OutputShapeBase):
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

    # String that contains the ARN of the issued certificate. This must be of the
    # form:

    # `arn:aws:acm:us-
    # east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012`
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RequestInProgressException(ShapeBase):
    """
    The certificate request is in process and the certificate in your account has
    not yet been issued.
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
class ResendValidationEmailRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "domain",
                "Domain",
                TypeInfo(str),
            ),
            (
                "validation_domain",
                "ValidationDomain",
                TypeInfo(str),
            ),
        ]

    # String that contains the ARN of the requested certificate. The certificate
    # ARN is generated and returned by the RequestCertificate action as soon as
    # the request is made. By default, using this parameter causes email to be
    # sent to all top-level domains you specified in the certificate request. The
    # ARN must be of the form:

    # `arn:aws:acm:us-
    # east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012`
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain name (FQDN) of the certificate that needs to be
    # validated.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The base validation domain that will act as the suffix of the email
    # addresses that are used to send the emails. This must be the same as the
    # `Domain` value or a superdomain of the `Domain` value. For example, if you
    # requested a certificate for `site.subdomain.example.com` and specify a
    # **ValidationDomain** of `subdomain.example.com`, ACM sends email to the
    # domain registrant, technical contact, and administrative contact in WHOIS
    # and the following five addresses:

    #   * admin@subdomain.example.com

    #   * administrator@subdomain.example.com

    #   * hostmaster@subdomain.example.com

    #   * postmaster@subdomain.example.com

    #   * webmaster@subdomain.example.com
    validation_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The certificate is in use by another AWS service in the caller's account. Remove
    the association and try again.
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
    The specified certificate cannot be found in the caller's account or the
    caller's account cannot be found.
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
class ResourceRecord(ShapeBase):
    """
    Contains a DNS record value that you can use to can use to validate ownership or
    control of a domain. This is used by the DescribeCertificate action.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, RecordType]),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The name of the DNS record to create in your domain. This is supplied by
    # ACM.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of DNS record. Currently this can be `CNAME`.
    type: typing.Union[str, "RecordType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of the CNAME record to add to your DNS database. This is supplied
    # by ACM.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RevocationReason(str):
    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CA_COMPROMISE = "CA_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERCEDED = "SUPERCEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    CERTIFICATE_HOLD = "CERTIFICATE_HOLD"
    REMOVE_FROM_CRL = "REMOVE_FROM_CRL"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A key-value pair that identifies or specifies metadata about an ACM resource.
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

    # The key of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyTagsException(ShapeBase):
    """
    The request contains too many tags. Try the request again with fewer tags.
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
class UpdateCertificateOptionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "options",
                "Options",
                TypeInfo(CertificateOptions),
            ),
        ]

    # ARN of the requested certificate to update. This must be of the form:

    # `arn:aws:acm:us-east-1: _account_ :certificate/
    # _12345678-1234-1234-1234-123456789012_ `
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use to update the options for your certificate. Currently, you can specify
    # whether to add your certificate to a transparency log. Certificate
    # transparency makes it possible to detect SSL/TLS certificates that have
    # been mistakenly or maliciously issued. Certificates that have not been
    # logged typically produce an error message in a browser.
    options: "CertificateOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ValidationMethod(str):
    EMAIL = "EMAIL"
    DNS = "DNS"
