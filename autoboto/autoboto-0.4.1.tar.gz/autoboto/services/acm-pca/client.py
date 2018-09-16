import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("acm-pca", *args, **kwargs)

    def create_certificate_authority(
        self,
        _request: shapes.CreateCertificateAuthorityRequest = None,
        *,
        certificate_authority_configuration: shapes.
        CertificateAuthorityConfiguration,
        certificate_authority_type: typing.Union[str, shapes.
                                                 CertificateAuthorityType],
        revocation_configuration: shapes.RevocationConfiguration = ShapeBase.
        NOT_SET,
        idempotency_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCertificateAuthorityResponse:
        """
        Creates a private subordinate certificate authority (CA). You must specify the
        CA configuration, the revocation configuration, the CA type, and an optional
        idempotency token. The CA configuration specifies the name of the algorithm and
        key size to be used to create the CA private key, the type of signing algorithm
        that the CA uses to sign, and X.500 subject information. The CRL (certificate
        revocation list) configuration specifies the CRL expiration period in days (the
        validity period of the CRL), the Amazon S3 bucket that will contain the CRL, and
        a CNAME alias for the S3 bucket that is included in certificates issued by the
        CA. If successful, this operation returns the Amazon Resource Name (ARN) of the
        CA.
        """
        if _request is None:
            _params = {}
            if certificate_authority_configuration is not ShapeBase.NOT_SET:
                _params['certificate_authority_configuration'
                       ] = certificate_authority_configuration
            if certificate_authority_type is not ShapeBase.NOT_SET:
                _params['certificate_authority_type'
                       ] = certificate_authority_type
            if revocation_configuration is not ShapeBase.NOT_SET:
                _params['revocation_configuration'] = revocation_configuration
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            _request = shapes.CreateCertificateAuthorityRequest(**_params)
        response = self._boto_client.create_certificate_authority(
            **_request.to_boto()
        )

        return shapes.CreateCertificateAuthorityResponse.from_boto(response)

    def create_certificate_authority_audit_report(
        self,
        _request: shapes.CreateCertificateAuthorityAuditReportRequest = None,
        *,
        certificate_authority_arn: str,
        s3_bucket_name: str,
        audit_report_response_format: typing.Union[str, shapes.
                                                   AuditReportResponseFormat],
    ) -> shapes.CreateCertificateAuthorityAuditReportResponse:
        """
        Creates an audit report that lists every time that the your CA private key is
        used. The report is saved in the Amazon S3 bucket that you specify on input. The
        IssueCertificate and RevokeCertificate operations use the private key. You can
        generate a new report every 30 minutes.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if s3_bucket_name is not ShapeBase.NOT_SET:
                _params['s3_bucket_name'] = s3_bucket_name
            if audit_report_response_format is not ShapeBase.NOT_SET:
                _params['audit_report_response_format'
                       ] = audit_report_response_format
            _request = shapes.CreateCertificateAuthorityAuditReportRequest(
                **_params
            )
        response = self._boto_client.create_certificate_authority_audit_report(
            **_request.to_boto()
        )

        return shapes.CreateCertificateAuthorityAuditReportResponse.from_boto(
            response
        )

    def delete_certificate_authority(
        self,
        _request: shapes.DeleteCertificateAuthorityRequest = None,
        *,
        certificate_authority_arn: str,
        permanent_deletion_time_in_days: int = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a private certificate authority (CA). You must provide the ARN (Amazon
        Resource Name) of the private CA that you want to delete. You can find the ARN
        by calling the ListCertificateAuthorities operation. Before you can delete a CA,
        you must disable it. Call the UpdateCertificateAuthority operation and set the
        **CertificateAuthorityStatus** parameter to `DISABLED`.

        Additionally, you can delete a CA if you are waiting for it to be created (the
        **Status** field of the CertificateAuthority is `CREATING`). You can also delete
        it if the CA has been created but you haven't yet imported the signed
        certificate (the **Status** is `PENDING_CERTIFICATE`) into ACM PCA.

        If the CA is in one of the aforementioned states and you call
        DeleteCertificateAuthority, the CA's status changes to `DELETED`. However, the
        CA won't be permentantly deleted until the restoration period has passed. By
        default, if you do not set the `PermanentDeletionTimeInDays` parameter, the CA
        remains restorable for 30 days. You can set the parameter from 7 to 30 days. The
        DescribeCertificateAuthority operation returns the time remaining in the
        restoration window of a Private CA in the `DELETED` state. To restore an
        eligable CA, call the RestoreCertificateAuthority operation.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if permanent_deletion_time_in_days is not ShapeBase.NOT_SET:
                _params['permanent_deletion_time_in_days'
                       ] = permanent_deletion_time_in_days
            _request = shapes.DeleteCertificateAuthorityRequest(**_params)
        response = self._boto_client.delete_certificate_authority(
            **_request.to_boto()
        )

    def describe_certificate_authority(
        self,
        _request: shapes.DescribeCertificateAuthorityRequest = None,
        *,
        certificate_authority_arn: str,
    ) -> shapes.DescribeCertificateAuthorityResponse:
        """
        Lists information about your private certificate authority (CA). You specify the
        private CA on input by its ARN (Amazon Resource Name). The output contains the
        status of your CA. This can be any of the following:

          * `CREATING` \- ACM PCA is creating your private certificate authority.

          * `PENDING_CERTIFICATE` \- The certificate is pending. You must use your on-premises root or subordinate CA to sign your private CA CSR and then import it into PCA. 

          * `ACTIVE` \- Your private CA is active.

          * `DISABLED` \- Your private CA has been disabled.

          * `EXPIRED` \- Your private CA certificate has expired.

          * `FAILED` \- Your private CA has failed. Your CA can fail because of problems such a network outage or backend AWS failure or other errors. A failed CA can never return to the pending state. You must create a new CA. 

          * `DELETED` \- Your private CA is within the restoration period, after which it will be permanently deleted. The length of time remaining in the CA's restoration period will also be included in this operation's output.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            _request = shapes.DescribeCertificateAuthorityRequest(**_params)
        response = self._boto_client.describe_certificate_authority(
            **_request.to_boto()
        )

        return shapes.DescribeCertificateAuthorityResponse.from_boto(response)

    def describe_certificate_authority_audit_report(
        self,
        _request: shapes.DescribeCertificateAuthorityAuditReportRequest = None,
        *,
        certificate_authority_arn: str,
        audit_report_id: str,
    ) -> shapes.DescribeCertificateAuthorityAuditReportResponse:
        """
        Lists information about a specific audit report created by calling the
        CreateCertificateAuthorityAuditReport operation. Audit information is created
        every time the certificate authority (CA) private key is used. The private key
        is used when you call the IssueCertificate operation or the RevokeCertificate
        operation.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if audit_report_id is not ShapeBase.NOT_SET:
                _params['audit_report_id'] = audit_report_id
            _request = shapes.DescribeCertificateAuthorityAuditReportRequest(
                **_params
            )
        response = self._boto_client.describe_certificate_authority_audit_report(
            **_request.to_boto()
        )

        return shapes.DescribeCertificateAuthorityAuditReportResponse.from_boto(
            response
        )

    def get_certificate(
        self,
        _request: shapes.GetCertificateRequest = None,
        *,
        certificate_authority_arn: str,
        certificate_arn: str,
    ) -> shapes.GetCertificateResponse:
        """
        Retrieves a certificate from your private CA. The ARN of the certificate is
        returned when you call the IssueCertificate operation. You must specify both the
        ARN of your private CA and the ARN of the issued certificate when calling the
        **GetCertificate** operation. You can retrieve the certificate if it is in the
        **ISSUED** state. You can call the CreateCertificateAuthorityAuditReport
        operation to create a report that contains information about all of the
        certificates issued and revoked by your private CA.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            _request = shapes.GetCertificateRequest(**_params)
        response = self._boto_client.get_certificate(**_request.to_boto())

        return shapes.GetCertificateResponse.from_boto(response)

    def get_certificate_authority_certificate(
        self,
        _request: shapes.GetCertificateAuthorityCertificateRequest = None,
        *,
        certificate_authority_arn: str,
    ) -> shapes.GetCertificateAuthorityCertificateResponse:
        """
        Retrieves the certificate and certificate chain for your private certificate
        authority (CA). Both the certificate and the chain are base64 PEM-encoded. The
        chain does not include the CA certificate. Each certificate in the chain signs
        the one before it.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            _request = shapes.GetCertificateAuthorityCertificateRequest(
                **_params
            )
        response = self._boto_client.get_certificate_authority_certificate(
            **_request.to_boto()
        )

        return shapes.GetCertificateAuthorityCertificateResponse.from_boto(
            response
        )

    def get_certificate_authority_csr(
        self,
        _request: shapes.GetCertificateAuthorityCsrRequest = None,
        *,
        certificate_authority_arn: str,
    ) -> shapes.GetCertificateAuthorityCsrResponse:
        """
        Retrieves the certificate signing request (CSR) for your private certificate
        authority (CA). The CSR is created when you call the CreateCertificateAuthority
        operation. Take the CSR to your on-premises X.509 infrastructure and sign it by
        using your root or a subordinate CA. Then import the signed certificate back
        into ACM PCA by calling the ImportCertificateAuthorityCertificate operation. The
        CSR is returned as a base64 PEM-encoded string.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            _request = shapes.GetCertificateAuthorityCsrRequest(**_params)
        response = self._boto_client.get_certificate_authority_csr(
            **_request.to_boto()
        )

        return shapes.GetCertificateAuthorityCsrResponse.from_boto(response)

    def import_certificate_authority_certificate(
        self,
        _request: shapes.ImportCertificateAuthorityCertificateRequest = None,
        *,
        certificate_authority_arn: str,
        certificate: typing.Any,
        certificate_chain: typing.Any,
    ) -> None:
        """
        Imports your signed private CA certificate into ACM PCA. Before you can call
        this operation, you must create the private certificate authority by calling the
        CreateCertificateAuthority operation. You must then generate a certificate
        signing request (CSR) by calling the GetCertificateAuthorityCsr operation. Take
        the CSR to your on-premises CA and use the root certificate or a subordinate
        certificate to sign it. Create a certificate chain and copy the signed
        certificate and the certificate chain to your working directory.

        Your certificate chain must not include the private CA certificate that you are
        importing.

        Your on-premises CA certificate must be the last certificate in your chain. The
        subordinate certificate, if any, that your root CA signed must be next to last.
        The subordinate certificate signed by the preceding subordinate CA must come
        next, and so on until your chain is built.

        The chain must be PEM-encoded.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if certificate is not ShapeBase.NOT_SET:
                _params['certificate'] = certificate
            if certificate_chain is not ShapeBase.NOT_SET:
                _params['certificate_chain'] = certificate_chain
            _request = shapes.ImportCertificateAuthorityCertificateRequest(
                **_params
            )
        response = self._boto_client.import_certificate_authority_certificate(
            **_request.to_boto()
        )

    def issue_certificate(
        self,
        _request: shapes.IssueCertificateRequest = None,
        *,
        certificate_authority_arn: str,
        csr: typing.Any,
        signing_algorithm: typing.Union[str, shapes.SigningAlgorithm],
        validity: shapes.Validity,
        idempotency_token: str = ShapeBase.NOT_SET,
    ) -> shapes.IssueCertificateResponse:
        """
        Uses your private certificate authority (CA) to issue a client certificate. This
        operation returns the Amazon Resource Name (ARN) of the certificate. You can
        retrieve the certificate by calling the GetCertificate operation and specifying
        the ARN.

        You cannot use the ACM **ListCertificateAuthorities** operation to retrieve the
        ARNs of the certificates that you issue by using ACM PCA.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if csr is not ShapeBase.NOT_SET:
                _params['csr'] = csr
            if signing_algorithm is not ShapeBase.NOT_SET:
                _params['signing_algorithm'] = signing_algorithm
            if validity is not ShapeBase.NOT_SET:
                _params['validity'] = validity
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            _request = shapes.IssueCertificateRequest(**_params)
        response = self._boto_client.issue_certificate(**_request.to_boto())

        return shapes.IssueCertificateResponse.from_boto(response)

    def list_certificate_authorities(
        self,
        _request: shapes.ListCertificateAuthoritiesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListCertificateAuthoritiesResponse:
        """
        Lists the private certificate authorities that you created by using the
        CreateCertificateAuthority operation.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListCertificateAuthoritiesRequest(**_params)
        response = self._boto_client.list_certificate_authorities(
            **_request.to_boto()
        )

        return shapes.ListCertificateAuthoritiesResponse.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        certificate_authority_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsResponse:
        """
        Lists the tags, if any, that are associated with your private CA. Tags are
        labels that you can use to identify and organize your CAs. Each tag consists of
        a key and an optional value. Call the TagCertificateAuthority operation to add
        one or more tags to your CA. Call the UntagCertificateAuthority operation to
        remove tags.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTagsRequest(**_params)
        response = self._boto_client.list_tags(**_request.to_boto())

        return shapes.ListTagsResponse.from_boto(response)

    def restore_certificate_authority(
        self,
        _request: shapes.RestoreCertificateAuthorityRequest = None,
        *,
        certificate_authority_arn: str,
    ) -> None:
        """
        Restores a certificate authority (CA) that is in the `DELETED` state. You can
        restore a CA during the period that you defined in the
        **PermanentDeletionTimeInDays** parameter of the DeleteCertificateAuthority
        operation. Currently, you can specify 7 to 30 days. If you did not specify a
        **PermanentDeletionTimeInDays** value, by default you can restore the CA at any
        time in a 30 day period. You can check the time remaining in the restoration
        period of a private CA in the `DELETED` state by calling the
        DescribeCertificateAuthority or ListCertificateAuthorities operations. The
        status of a restored CA is set to its pre-deletion status when the
        **RestoreCertificateAuthority** operation returns. To change its status to
        `ACTIVE`, call the UpdateCertificateAuthority operation. If the private CA was
        in the `PENDING_CERTIFICATE` state at deletion, you must use the
        ImportCertificateAuthorityCertificate operation to import a certificate
        authority into the private CA before it can be activated. You cannot restore a
        CA after the restoration period has ended.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            _request = shapes.RestoreCertificateAuthorityRequest(**_params)
        response = self._boto_client.restore_certificate_authority(
            **_request.to_boto()
        )

    def revoke_certificate(
        self,
        _request: shapes.RevokeCertificateRequest = None,
        *,
        certificate_authority_arn: str,
        certificate_serial: str,
        revocation_reason: typing.Union[str, shapes.RevocationReason],
    ) -> None:
        """
        Revokes a certificate that you issued by calling the IssueCertificate operation.
        If you enable a certificate revocation list (CRL) when you create or update your
        private CA, information about the revoked certificates will be included in the
        CRL. ACM PCA writes the CRL to an S3 bucket that you specify. For more
        information about revocation, see the CrlConfiguration structure. ACM PCA also
        writes revocation information to the audit report. For more information, see
        CreateCertificateAuthorityAuditReport.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if certificate_serial is not ShapeBase.NOT_SET:
                _params['certificate_serial'] = certificate_serial
            if revocation_reason is not ShapeBase.NOT_SET:
                _params['revocation_reason'] = revocation_reason
            _request = shapes.RevokeCertificateRequest(**_params)
        response = self._boto_client.revoke_certificate(**_request.to_boto())

    def tag_certificate_authority(
        self,
        _request: shapes.TagCertificateAuthorityRequest = None,
        *,
        certificate_authority_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Adds one or more tags to your private CA. Tags are labels that you can use to
        identify and organize your AWS resources. Each tag consists of a key and an
        optional value. You specify the private CA on input by its Amazon Resource Name
        (ARN). You specify the tag by using a key-value pair. You can apply a tag to
        just one private CA if you want to identify a specific characteristic of that
        CA, or you can apply the same tag to multiple private CAs if you want to filter
        for a common relationship among those CAs. To remove one or more tags, use the
        UntagCertificateAuthority operation. Call the ListTags operation to see what
        tags are associated with your CA.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagCertificateAuthorityRequest(**_params)
        response = self._boto_client.tag_certificate_authority(
            **_request.to_boto()
        )

    def untag_certificate_authority(
        self,
        _request: shapes.UntagCertificateAuthorityRequest = None,
        *,
        certificate_authority_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Remove one or more tags from your private CA. A tag consists of a key-value
        pair. If you do not specify the value portion of the tag when calling this
        operation, the tag will be removed regardless of value. If you specify a value,
        the tag is removed only if it is associated with the specified value. To add
        tags to a private CA, use the TagCertificateAuthority. Call the ListTags
        operation to see what tags are associated with your CA.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.UntagCertificateAuthorityRequest(**_params)
        response = self._boto_client.untag_certificate_authority(
            **_request.to_boto()
        )

    def update_certificate_authority(
        self,
        _request: shapes.UpdateCertificateAuthorityRequest = None,
        *,
        certificate_authority_arn: str,
        revocation_configuration: shapes.RevocationConfiguration = ShapeBase.
        NOT_SET,
        status: typing.Union[str, shapes.
                             CertificateAuthorityStatus] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates the status or configuration of a private certificate authority (CA).
        Your private CA must be in the `ACTIVE` or `DISABLED` state before you can
        update it. You can disable a private CA that is in the `ACTIVE` state or make a
        CA that is in the `DISABLED` state active again.
        """
        if _request is None:
            _params = {}
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            if revocation_configuration is not ShapeBase.NOT_SET:
                _params['revocation_configuration'] = revocation_configuration
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.UpdateCertificateAuthorityRequest(**_params)
        response = self._boto_client.update_certificate_authority(
            **_request.to_boto()
        )
