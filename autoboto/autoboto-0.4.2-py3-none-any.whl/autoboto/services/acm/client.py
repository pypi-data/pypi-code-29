import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("acm", *args, **kwargs)

    def add_tags_to_certificate(
        self,
        _request: shapes.AddTagsToCertificateRequest = None,
        *,
        certificate_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Adds one or more tags to an ACM certificate. Tags are labels that you can use to
        identify and organize your AWS resources. Each tag consists of a `key` and an
        optional `value`. You specify the certificate on input by its Amazon Resource
        Name (ARN). You specify the tag by using a key-value pair.

        You can apply a tag to just one certificate if you want to identify a specific
        characteristic of that certificate, or you can apply the same tag to multiple
        certificates if you want to filter for a common relationship among those
        certificates. Similarly, you can apply the same tag to multiple resources if you
        want to specify a relationship among those resources. For example, you can add
        the same tag to an ACM certificate and an Elastic Load Balancing load balancer
        to indicate that they are both used by the same website. For more information,
        see [Tagging ACM
        certificates](http://docs.aws.amazon.com/acm/latest/userguide/tags.html).

        To remove one or more tags, use the RemoveTagsFromCertificate action. To view
        all of the tags that have been applied to the certificate, use the
        ListTagsForCertificate action.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToCertificateRequest(**_params)
        response = self._boto_client.add_tags_to_certificate(
            **_request.to_boto()
        )

    def delete_certificate(
        self,
        _request: shapes.DeleteCertificateRequest = None,
        *,
        certificate_arn: str,
    ) -> None:
        """
        Deletes a certificate and its associated private key. If this action succeeds,
        the certificate no longer appears in the list that can be displayed by calling
        the ListCertificates action or be retrieved by calling the GetCertificate
        action. The certificate will not be available for use by AWS services integrated
        with ACM.

        You cannot delete an ACM certificate that is being used by another AWS service.
        To delete a certificate that is in use, the certificate association must first
        be removed.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            _request = shapes.DeleteCertificateRequest(**_params)
        response = self._boto_client.delete_certificate(**_request.to_boto())

    def describe_certificate(
        self,
        _request: shapes.DescribeCertificateRequest = None,
        *,
        certificate_arn: str,
    ) -> shapes.DescribeCertificateResponse:
        """
        Returns detailed metadata about the specified ACM certificate.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            _request = shapes.DescribeCertificateRequest(**_params)
        response = self._boto_client.describe_certificate(**_request.to_boto())

        return shapes.DescribeCertificateResponse.from_boto(response)

    def export_certificate(
        self,
        _request: shapes.ExportCertificateRequest = None,
        *,
        certificate_arn: str,
        passphrase: typing.Any,
    ) -> shapes.ExportCertificateResponse:
        """
        Exports a private certificate issued by a private certificate authority (CA) for
        use anywhere. You can export the certificate, the certificate chain, and the
        encrypted private key associated with the public key embedded in the
        certificate. You must store the private key securely. The private key is a 2048
        bit RSA key. You must provide a passphrase for the private key when exporting
        it. You can use the following OpenSSL command to decrypt it later. Provide the
        passphrase when prompted.

        `openssl rsa -in encrypted_key.pem -out decrypted_key.pem`
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if passphrase is not ShapeBase.NOT_SET:
                _params['passphrase'] = passphrase
            _request = shapes.ExportCertificateRequest(**_params)
        response = self._boto_client.export_certificate(**_request.to_boto())

        return shapes.ExportCertificateResponse.from_boto(response)

    def get_certificate(
        self,
        _request: shapes.GetCertificateRequest = None,
        *,
        certificate_arn: str,
    ) -> shapes.GetCertificateResponse:
        """
        Retrieves a certificate specified by an ARN and its certificate chain . The
        chain is an ordered list of certificates that contains the end entity
        certificate, intermediate certificates of subordinate CAs, and the root
        certificate in that order. The certificate and certificate chain are base64
        encoded. If you want to decode the certificate to see the individual fields, you
        can use OpenSSL.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            _request = shapes.GetCertificateRequest(**_params)
        response = self._boto_client.get_certificate(**_request.to_boto())

        return shapes.GetCertificateResponse.from_boto(response)

    def import_certificate(
        self,
        _request: shapes.ImportCertificateRequest = None,
        *,
        certificate: typing.Any,
        private_key: typing.Any,
        certificate_arn: str = ShapeBase.NOT_SET,
        certificate_chain: typing.Any = ShapeBase.NOT_SET,
    ) -> shapes.ImportCertificateResponse:
        """
        Imports a certificate into AWS Certificate Manager (ACM) to use with services
        that are integrated with ACM. Note that [integrated
        services](http://docs.aws.amazon.com/acm/latest/userguide/acm-services.html)
        allow only certificate types and keys they support to be associated with their
        resources. Further, their support differs depending on whether the certificate
        is imported into IAM or into ACM. For more information, see the documentation
        for each service. For more information about importing certificates into ACM,
        see [Importing
        Certificates](http://docs.aws.amazon.com/acm/latest/userguide/import-
        certificate.html) in the _AWS Certificate Manager User Guide_.

        ACM does not provide [managed
        renewal](http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for
        certificates that you import.

        Note the following guidelines when importing third party certificates:

          * You must enter the private key that matches the certificate you are importing.

          * The private key must be unencrypted. You cannot import a private key that is protected by a password or a passphrase.

          * If the certificate you are importing is not self-signed, you must enter its certificate chain.

          * If a certificate chain is included, the issuer must be the subject of one of the certificates in the chain.

          * The certificate, private key, and certificate chain must be PEM-encoded.

          * The current time must be between the `Not Before` and `Not After` certificate fields.

          * The `Issuer` field must not be empty.

          * The OCSP authority URL, if present, must not exceed 1000 characters.

          * To import a new certificate, omit the `CertificateArn` argument. Include this argument only when you want to replace a previously imported certificate.

          * When you import a certificate by using the CLI, you must specify the certificate, the certificate chain, and the private key by their file names preceded by `file://`. For example, you can specify a certificate saved in the `C:\temp` folder as `file://C:\temp\certificate_to_import.pem`. If you are making an HTTP or HTTPS Query request, include these arguments as BLOBs. 

          * When you import a certificate by using an SDK, you must specify the certificate, the certificate chain, and the private key files in the manner required by the programming language you're using. 

        This operation returns the [Amazon Resource Name
        (ARN)](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-
        namespaces.html) of the imported certificate.
        """
        if _request is None:
            _params = {}
            if certificate is not ShapeBase.NOT_SET:
                _params['certificate'] = certificate
            if private_key is not ShapeBase.NOT_SET:
                _params['private_key'] = private_key
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if certificate_chain is not ShapeBase.NOT_SET:
                _params['certificate_chain'] = certificate_chain
            _request = shapes.ImportCertificateRequest(**_params)
        response = self._boto_client.import_certificate(**_request.to_boto())

        return shapes.ImportCertificateResponse.from_boto(response)

    def list_certificates(
        self,
        _request: shapes.ListCertificatesRequest = None,
        *,
        certificate_statuses: typing.List[
            typing.Union[str, shapes.CertificateStatus]] = ShapeBase.NOT_SET,
        includes: shapes.Filters = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListCertificatesResponse:
        """
        Retrieves a list of certificate ARNs and domain names. You can request that only
        certificates that match a specific status be listed. You can also filter by
        specific attributes of the certificate.
        """
        if _request is None:
            _params = {}
            if certificate_statuses is not ShapeBase.NOT_SET:
                _params['certificate_statuses'] = certificate_statuses
            if includes is not ShapeBase.NOT_SET:
                _params['includes'] = includes
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListCertificatesRequest(**_params)
        paginator = self.get_paginator("list_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCertificatesResponse.from_boto(response)

    def list_tags_for_certificate(
        self,
        _request: shapes.ListTagsForCertificateRequest = None,
        *,
        certificate_arn: str,
    ) -> shapes.ListTagsForCertificateResponse:
        """
        Lists the tags that have been applied to the ACM certificate. Use the
        certificate's Amazon Resource Name (ARN) to specify the certificate. To add a
        tag to an ACM certificate, use the AddTagsToCertificate action. To delete a tag,
        use the RemoveTagsFromCertificate action.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            _request = shapes.ListTagsForCertificateRequest(**_params)
        response = self._boto_client.list_tags_for_certificate(
            **_request.to_boto()
        )

        return shapes.ListTagsForCertificateResponse.from_boto(response)

    def remove_tags_from_certificate(
        self,
        _request: shapes.RemoveTagsFromCertificateRequest = None,
        *,
        certificate_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Remove one or more tags from an ACM certificate. A tag consists of a key-value
        pair. If you do not specify the value portion of the tag when calling this
        function, the tag will be removed regardless of value. If you specify a value,
        the tag is removed only if it is associated with the specified value.

        To add tags to a certificate, use the AddTagsToCertificate action. To view all
        of the tags that have been applied to a specific ACM certificate, use the
        ListTagsForCertificate action.
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.RemoveTagsFromCertificateRequest(**_params)
        response = self._boto_client.remove_tags_from_certificate(
            **_request.to_boto()
        )

    def request_certificate(
        self,
        _request: shapes.RequestCertificateRequest = None,
        *,
        domain_name: str,
        validation_method: typing.Union[str, shapes.
                                        ValidationMethod] = ShapeBase.NOT_SET,
        subject_alternative_names: typing.List[str] = ShapeBase.NOT_SET,
        idempotency_token: str = ShapeBase.NOT_SET,
        domain_validation_options: typing.List[shapes.DomainValidationOption
                                              ] = ShapeBase.NOT_SET,
        options: shapes.CertificateOptions = ShapeBase.NOT_SET,
        certificate_authority_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.RequestCertificateResponse:
        """
        Requests an ACM certificate for use with other AWS services. To request an ACM
        certificate, you must specify a fully qualified domain name (FQDN) in the
        `DomainName` parameter. You can also specify additional FQDNs in the
        `SubjectAlternativeNames` parameter.

        If you are requesting a private certificate, domain validation is not required.
        If you are requesting a public certificate, each domain name that you specify
        must be validated to verify that you own or control the domain. You can use [DNS
        validation](http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-
        dns.html) or [email
        validation](http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-
        email.html). We recommend that you use DNS validation. ACM issues public
        certificates after receiving approval from the domain owner.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if validation_method is not ShapeBase.NOT_SET:
                _params['validation_method'] = validation_method
            if subject_alternative_names is not ShapeBase.NOT_SET:
                _params['subject_alternative_names'] = subject_alternative_names
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if domain_validation_options is not ShapeBase.NOT_SET:
                _params['domain_validation_options'] = domain_validation_options
            if options is not ShapeBase.NOT_SET:
                _params['options'] = options
            if certificate_authority_arn is not ShapeBase.NOT_SET:
                _params['certificate_authority_arn'] = certificate_authority_arn
            _request = shapes.RequestCertificateRequest(**_params)
        response = self._boto_client.request_certificate(**_request.to_boto())

        return shapes.RequestCertificateResponse.from_boto(response)

    def resend_validation_email(
        self,
        _request: shapes.ResendValidationEmailRequest = None,
        *,
        certificate_arn: str,
        domain: str,
        validation_domain: str,
    ) -> None:
        """
        Resends the email that requests domain ownership validation. The domain owner or
        an authorized representative must approve the ACM certificate before it can be
        issued. The certificate can be approved by clicking a link in the mail to
        navigate to the Amazon certificate approval website and then clicking **I
        Approve**. However, the validation email can be blocked by spam filters.
        Therefore, if you do not receive the original mail, you can request that the
        mail be resent within 72 hours of requesting the ACM certificate. If more than
        72 hours have elapsed since your original request or since your last attempt to
        resend validation mail, you must request a new certificate. For more information
        about setting up your contact email addresses, see [Configure Email for your
        Domain](http://docs.aws.amazon.com/acm/latest/userguide/setup-email.html).
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if validation_domain is not ShapeBase.NOT_SET:
                _params['validation_domain'] = validation_domain
            _request = shapes.ResendValidationEmailRequest(**_params)
        response = self._boto_client.resend_validation_email(
            **_request.to_boto()
        )

    def update_certificate_options(
        self,
        _request: shapes.UpdateCertificateOptionsRequest = None,
        *,
        certificate_arn: str,
        options: shapes.CertificateOptions,
    ) -> None:
        """
        Updates a certificate. Currently, you can use this function to specify whether
        to opt in to or out of recording your certificate in a certificate transparency
        log. For more information, see [ Opting Out of Certificate Transparency
        Logging](http://docs.aws.amazon.com/acm/latest/userguide/acm-
        bestpractices.html#best-practices-transparency).
        """
        if _request is None:
            _params = {}
            if certificate_arn is not ShapeBase.NOT_SET:
                _params['certificate_arn'] = certificate_arn
            if options is not ShapeBase.NOT_SET:
                _params['options'] = options
            _request = shapes.UpdateCertificateOptionsRequest(**_params)
        response = self._boto_client.update_certificate_options(
            **_request.to_boto()
        )
