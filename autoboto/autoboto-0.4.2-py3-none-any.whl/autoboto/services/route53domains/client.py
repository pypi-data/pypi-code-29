import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("route53domains", *args, **kwargs)

    def check_domain_availability(
        self,
        _request: shapes.CheckDomainAvailabilityRequest = None,
        *,
        domain_name: str,
        idn_lang_code: str = ShapeBase.NOT_SET,
    ) -> shapes.CheckDomainAvailabilityResponse:
        """
        This operation checks the availability of one domain name. Note that if the
        availability status of a domain is pending, you must submit another request to
        determine the availability of the domain name.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if idn_lang_code is not ShapeBase.NOT_SET:
                _params['idn_lang_code'] = idn_lang_code
            _request = shapes.CheckDomainAvailabilityRequest(**_params)
        response = self._boto_client.check_domain_availability(
            **_request.to_boto()
        )

        return shapes.CheckDomainAvailabilityResponse.from_boto(response)

    def check_domain_transferability(
        self,
        _request: shapes.CheckDomainTransferabilityRequest = None,
        *,
        domain_name: str,
        auth_code: str = ShapeBase.NOT_SET,
    ) -> shapes.CheckDomainTransferabilityResponse:
        """
        Checks whether a domain name can be transferred to Amazon Route 53.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if auth_code is not ShapeBase.NOT_SET:
                _params['auth_code'] = auth_code
            _request = shapes.CheckDomainTransferabilityRequest(**_params)
        response = self._boto_client.check_domain_transferability(
            **_request.to_boto()
        )

        return shapes.CheckDomainTransferabilityResponse.from_boto(response)

    def delete_tags_for_domain(
        self,
        _request: shapes.DeleteTagsForDomainRequest = None,
        *,
        domain_name: str,
        tags_to_delete: typing.List[str],
    ) -> shapes.DeleteTagsForDomainResponse:
        """
        This operation deletes the specified tags for a domain.

        All tag operations are eventually consistent; subsequent operations might not
        immediately represent all issued operations.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if tags_to_delete is not ShapeBase.NOT_SET:
                _params['tags_to_delete'] = tags_to_delete
            _request = shapes.DeleteTagsForDomainRequest(**_params)
        response = self._boto_client.delete_tags_for_domain(
            **_request.to_boto()
        )

        return shapes.DeleteTagsForDomainResponse.from_boto(response)

    def disable_domain_auto_renew(
        self,
        _request: shapes.DisableDomainAutoRenewRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DisableDomainAutoRenewResponse:
        """
        This operation disables automatic renewal of domain registration for the
        specified domain.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DisableDomainAutoRenewRequest(**_params)
        response = self._boto_client.disable_domain_auto_renew(
            **_request.to_boto()
        )

        return shapes.DisableDomainAutoRenewResponse.from_boto(response)

    def disable_domain_transfer_lock(
        self,
        _request: shapes.DisableDomainTransferLockRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DisableDomainTransferLockResponse:
        """
        This operation removes the transfer lock on the domain (specifically the
        `clientTransferProhibited` status) to allow domain transfers. We recommend you
        refrain from performing this action unless you intend to transfer the domain to
        a different registrar. Successful submission returns an operation ID that you
        can use to track the progress and completion of the action. If the request is
        not completed successfully, the domain registrant will be notified by email.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DisableDomainTransferLockRequest(**_params)
        response = self._boto_client.disable_domain_transfer_lock(
            **_request.to_boto()
        )

        return shapes.DisableDomainTransferLockResponse.from_boto(response)

    def enable_domain_auto_renew(
        self,
        _request: shapes.EnableDomainAutoRenewRequest = None,
        *,
        domain_name: str,
    ) -> shapes.EnableDomainAutoRenewResponse:
        """
        This operation configures Amazon Route 53 to automatically renew the specified
        domain before the domain registration expires. The cost of renewing your domain
        registration is billed to your AWS account.

        The period during which you can renew a domain name varies by TLD. For a list of
        TLDs and their renewal policies, see ["Renewal, restoration, and deletion
        times"](http://wiki.gandi.net/en/domains/renew#renewal_restoration_and_deletion_times)
        on the website for our registrar associate, Gandi. Amazon Route 53 requires that
        you renew before the end of the renewal period that is listed on the Gandi
        website so we can complete processing before the deadline.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.EnableDomainAutoRenewRequest(**_params)
        response = self._boto_client.enable_domain_auto_renew(
            **_request.to_boto()
        )

        return shapes.EnableDomainAutoRenewResponse.from_boto(response)

    def enable_domain_transfer_lock(
        self,
        _request: shapes.EnableDomainTransferLockRequest = None,
        *,
        domain_name: str,
    ) -> shapes.EnableDomainTransferLockResponse:
        """
        This operation sets the transfer lock on the domain (specifically the
        `clientTransferProhibited` status) to prevent domain transfers. Successful
        submission returns an operation ID that you can use to track the progress and
        completion of the action. If the request is not completed successfully, the
        domain registrant will be notified by email.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.EnableDomainTransferLockRequest(**_params)
        response = self._boto_client.enable_domain_transfer_lock(
            **_request.to_boto()
        )

        return shapes.EnableDomainTransferLockResponse.from_boto(response)

    def get_contact_reachability_status(
        self,
        _request: shapes.GetContactReachabilityStatusRequest = None,
        *,
        domain_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetContactReachabilityStatusResponse:
        """
        For operations that require confirmation that the email address for the
        registrant contact is valid, such as registering a new domain, this operation
        returns information about whether the registrant contact has responded.

        If you want us to resend the email, use the `ResendContactReachabilityEmail`
        operation.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.GetContactReachabilityStatusRequest(**_params)
        response = self._boto_client.get_contact_reachability_status(
            **_request.to_boto()
        )

        return shapes.GetContactReachabilityStatusResponse.from_boto(response)

    def get_domain_detail(
        self,
        _request: shapes.GetDomainDetailRequest = None,
        *,
        domain_name: str,
    ) -> shapes.GetDomainDetailResponse:
        """
        This operation returns detailed information about a specified domain that is
        associated with the current AWS account. Contact information for the domain is
        also returned as part of the output.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.GetDomainDetailRequest(**_params)
        response = self._boto_client.get_domain_detail(**_request.to_boto())

        return shapes.GetDomainDetailResponse.from_boto(response)

    def get_domain_suggestions(
        self,
        _request: shapes.GetDomainSuggestionsRequest = None,
        *,
        domain_name: str,
        suggestion_count: int,
        only_available: bool,
    ) -> shapes.GetDomainSuggestionsResponse:
        """
        The GetDomainSuggestions operation returns a list of suggested domain names
        given a string, which can either be a domain name or simply a word or phrase
        (without spaces).
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if suggestion_count is not ShapeBase.NOT_SET:
                _params['suggestion_count'] = suggestion_count
            if only_available is not ShapeBase.NOT_SET:
                _params['only_available'] = only_available
            _request = shapes.GetDomainSuggestionsRequest(**_params)
        response = self._boto_client.get_domain_suggestions(
            **_request.to_boto()
        )

        return shapes.GetDomainSuggestionsResponse.from_boto(response)

    def get_operation_detail(
        self,
        _request: shapes.GetOperationDetailRequest = None,
        *,
        operation_id: str,
    ) -> shapes.GetOperationDetailResponse:
        """
        This operation returns the current status of an operation that is not completed.
        """
        if _request is None:
            _params = {}
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.GetOperationDetailRequest(**_params)
        response = self._boto_client.get_operation_detail(**_request.to_boto())

        return shapes.GetOperationDetailResponse.from_boto(response)

    def list_domains(
        self,
        _request: shapes.ListDomainsRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDomainsResponse:
        """
        This operation returns all the domain names registered with Amazon Route 53 for
        the current AWS account.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListDomainsRequest(**_params)
        paginator = self.get_paginator("list_domains").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDomainsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDomainsResponse.from_boto(response)

    def list_operations(
        self,
        _request: shapes.ListOperationsRequest = None,
        *,
        submitted_since: datetime.datetime = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListOperationsResponse:
        """
        This operation returns the operation IDs of operations that are not yet
        complete.
        """
        if _request is None:
            _params = {}
            if submitted_since is not ShapeBase.NOT_SET:
                _params['submitted_since'] = submitted_since
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListOperationsRequest(**_params)
        paginator = self.get_paginator("list_operations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOperationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOperationsResponse.from_boto(response)

    def list_tags_for_domain(
        self,
        _request: shapes.ListTagsForDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.ListTagsForDomainResponse:
        """
        This operation returns all of the tags that are associated with the specified
        domain.

        All tag operations are eventually consistent; subsequent operations might not
        immediately represent all issued operations.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.ListTagsForDomainRequest(**_params)
        response = self._boto_client.list_tags_for_domain(**_request.to_boto())

        return shapes.ListTagsForDomainResponse.from_boto(response)

    def register_domain(
        self,
        _request: shapes.RegisterDomainRequest = None,
        *,
        domain_name: str,
        duration_in_years: int,
        admin_contact: shapes.ContactDetail,
        registrant_contact: shapes.ContactDetail,
        tech_contact: shapes.ContactDetail,
        idn_lang_code: str = ShapeBase.NOT_SET,
        auto_renew: bool = ShapeBase.NOT_SET,
        privacy_protect_admin_contact: bool = ShapeBase.NOT_SET,
        privacy_protect_registrant_contact: bool = ShapeBase.NOT_SET,
        privacy_protect_tech_contact: bool = ShapeBase.NOT_SET,
    ) -> shapes.RegisterDomainResponse:
        """
        This operation registers a domain. Domains are registered either by Amazon
        Registrar (for .com, .net, and .org domains) or by our registrar associate,
        Gandi (for all other domains). For some top-level domains (TLDs), this operation
        requires extra parameters.

        When you register a domain, Amazon Route 53 does the following:

          * Creates a Amazon Route 53 hosted zone that has the same name as the domain. Amazon Route 53 assigns four name servers to your hosted zone and automatically updates your domain registration with the names of these name servers.

          * Enables autorenew, so your domain registration will renew automatically each year. We'll notify you in advance of the renewal date so you can choose whether to renew the registration.

          * Optionally enables privacy protection, so WHOIS queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you don't enable privacy protection, WHOIS queries return the information that you entered for the registrant, admin, and tech contacts.

          * If registration is successful, returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant is notified by email.

          * Charges your AWS account an amount based on the top-level domain. For more information, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/).
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if duration_in_years is not ShapeBase.NOT_SET:
                _params['duration_in_years'] = duration_in_years
            if admin_contact is not ShapeBase.NOT_SET:
                _params['admin_contact'] = admin_contact
            if registrant_contact is not ShapeBase.NOT_SET:
                _params['registrant_contact'] = registrant_contact
            if tech_contact is not ShapeBase.NOT_SET:
                _params['tech_contact'] = tech_contact
            if idn_lang_code is not ShapeBase.NOT_SET:
                _params['idn_lang_code'] = idn_lang_code
            if auto_renew is not ShapeBase.NOT_SET:
                _params['auto_renew'] = auto_renew
            if privacy_protect_admin_contact is not ShapeBase.NOT_SET:
                _params['privacy_protect_admin_contact'
                       ] = privacy_protect_admin_contact
            if privacy_protect_registrant_contact is not ShapeBase.NOT_SET:
                _params['privacy_protect_registrant_contact'
                       ] = privacy_protect_registrant_contact
            if privacy_protect_tech_contact is not ShapeBase.NOT_SET:
                _params['privacy_protect_tech_contact'
                       ] = privacy_protect_tech_contact
            _request = shapes.RegisterDomainRequest(**_params)
        response = self._boto_client.register_domain(**_request.to_boto())

        return shapes.RegisterDomainResponse.from_boto(response)

    def renew_domain(
        self,
        _request: shapes.RenewDomainRequest = None,
        *,
        domain_name: str,
        current_expiry_year: int,
        duration_in_years: int = ShapeBase.NOT_SET,
    ) -> shapes.RenewDomainResponse:
        """
        This operation renews a domain for the specified number of years. The cost of
        renewing your domain is billed to your AWS account.

        We recommend that you renew your domain several weeks before the expiration
        date. Some TLD registries delete domains before the expiration date if you
        haven't renewed far enough in advance. For more information about renewing
        domain registration, see [Renewing Registration for a
        Domain](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-
        renew.html) in the Amazon Route 53 Developer Guide.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if current_expiry_year is not ShapeBase.NOT_SET:
                _params['current_expiry_year'] = current_expiry_year
            if duration_in_years is not ShapeBase.NOT_SET:
                _params['duration_in_years'] = duration_in_years
            _request = shapes.RenewDomainRequest(**_params)
        response = self._boto_client.renew_domain(**_request.to_boto())

        return shapes.RenewDomainResponse.from_boto(response)

    def resend_contact_reachability_email(
        self,
        _request: shapes.ResendContactReachabilityEmailRequest = None,
        *,
        domain_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ResendContactReachabilityEmailResponse:
        """
        For operations that require confirmation that the email address for the
        registrant contact is valid, such as registering a new domain, this operation
        resends the confirmation email to the current email address for the registrant
        contact.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.ResendContactReachabilityEmailRequest(**_params)
        response = self._boto_client.resend_contact_reachability_email(
            **_request.to_boto()
        )

        return shapes.ResendContactReachabilityEmailResponse.from_boto(response)

    def retrieve_domain_auth_code(
        self,
        _request: shapes.RetrieveDomainAuthCodeRequest = None,
        *,
        domain_name: str,
    ) -> shapes.RetrieveDomainAuthCodeResponse:
        """
        This operation returns the AuthCode for the domain. To transfer a domain to
        another registrar, you provide this value to the new registrar.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.RetrieveDomainAuthCodeRequest(**_params)
        response = self._boto_client.retrieve_domain_auth_code(
            **_request.to_boto()
        )

        return shapes.RetrieveDomainAuthCodeResponse.from_boto(response)

    def transfer_domain(
        self,
        _request: shapes.TransferDomainRequest = None,
        *,
        domain_name: str,
        duration_in_years: int,
        admin_contact: shapes.ContactDetail,
        registrant_contact: shapes.ContactDetail,
        tech_contact: shapes.ContactDetail,
        idn_lang_code: str = ShapeBase.NOT_SET,
        nameservers: typing.List[shapes.Nameserver] = ShapeBase.NOT_SET,
        auth_code: str = ShapeBase.NOT_SET,
        auto_renew: bool = ShapeBase.NOT_SET,
        privacy_protect_admin_contact: bool = ShapeBase.NOT_SET,
        privacy_protect_registrant_contact: bool = ShapeBase.NOT_SET,
        privacy_protect_tech_contact: bool = ShapeBase.NOT_SET,
    ) -> shapes.TransferDomainResponse:
        """
        This operation transfers a domain from another registrar to Amazon Route 53.
        When the transfer is complete, the domain is registered either with Amazon
        Registrar (for .com, .net, and .org domains) or with our registrar associate,
        Gandi (for all other TLDs).

        For transfer requirements, a detailed procedure, and information about viewing
        the status of a domain transfer, see [Transferring Registration for a Domain to
        Amazon Route
        53](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-
        route-53.html) in the _Amazon Route 53 Developer Guide_.

        If the registrar for your domain is also the DNS service provider for the
        domain, we highly recommend that you consider transferring your DNS service to
        Amazon Route 53 or to another DNS service provider before you transfer your
        registration. Some registrars provide free DNS service when you purchase a
        domain registration. When you transfer the registration, the previous registrar
        will not renew your domain registration and could end your DNS service at any
        time.

        If the registrar for your domain is also the DNS service provider for the domain
        and you don't transfer DNS service to another provider, your website, email, and
        the web applications associated with the domain might become unavailable.

        If the transfer is successful, this method returns an operation ID that you can
        use to track the progress and completion of the action. If the transfer doesn't
        complete successfully, the domain registrant will be notified by email.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if duration_in_years is not ShapeBase.NOT_SET:
                _params['duration_in_years'] = duration_in_years
            if admin_contact is not ShapeBase.NOT_SET:
                _params['admin_contact'] = admin_contact
            if registrant_contact is not ShapeBase.NOT_SET:
                _params['registrant_contact'] = registrant_contact
            if tech_contact is not ShapeBase.NOT_SET:
                _params['tech_contact'] = tech_contact
            if idn_lang_code is not ShapeBase.NOT_SET:
                _params['idn_lang_code'] = idn_lang_code
            if nameservers is not ShapeBase.NOT_SET:
                _params['nameservers'] = nameservers
            if auth_code is not ShapeBase.NOT_SET:
                _params['auth_code'] = auth_code
            if auto_renew is not ShapeBase.NOT_SET:
                _params['auto_renew'] = auto_renew
            if privacy_protect_admin_contact is not ShapeBase.NOT_SET:
                _params['privacy_protect_admin_contact'
                       ] = privacy_protect_admin_contact
            if privacy_protect_registrant_contact is not ShapeBase.NOT_SET:
                _params['privacy_protect_registrant_contact'
                       ] = privacy_protect_registrant_contact
            if privacy_protect_tech_contact is not ShapeBase.NOT_SET:
                _params['privacy_protect_tech_contact'
                       ] = privacy_protect_tech_contact
            _request = shapes.TransferDomainRequest(**_params)
        response = self._boto_client.transfer_domain(**_request.to_boto())

        return shapes.TransferDomainResponse.from_boto(response)

    def update_domain_contact(
        self,
        _request: shapes.UpdateDomainContactRequest = None,
        *,
        domain_name: str,
        admin_contact: shapes.ContactDetail = ShapeBase.NOT_SET,
        registrant_contact: shapes.ContactDetail = ShapeBase.NOT_SET,
        tech_contact: shapes.ContactDetail = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDomainContactResponse:
        """
        This operation updates the contact information for a particular domain. You must
        specify information for at least one contact: registrant, administrator, or
        technical.

        If the update is successful, this method returns an operation ID that you can
        use to track the progress and completion of the action. If the request is not
        completed successfully, the domain registrant will be notified by email.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if admin_contact is not ShapeBase.NOT_SET:
                _params['admin_contact'] = admin_contact
            if registrant_contact is not ShapeBase.NOT_SET:
                _params['registrant_contact'] = registrant_contact
            if tech_contact is not ShapeBase.NOT_SET:
                _params['tech_contact'] = tech_contact
            _request = shapes.UpdateDomainContactRequest(**_params)
        response = self._boto_client.update_domain_contact(**_request.to_boto())

        return shapes.UpdateDomainContactResponse.from_boto(response)

    def update_domain_contact_privacy(
        self,
        _request: shapes.UpdateDomainContactPrivacyRequest = None,
        *,
        domain_name: str,
        admin_privacy: bool = ShapeBase.NOT_SET,
        registrant_privacy: bool = ShapeBase.NOT_SET,
        tech_privacy: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDomainContactPrivacyResponse:
        """
        This operation updates the specified domain contact's privacy setting. When
        privacy protection is enabled, contact information such as email address is
        replaced either with contact information for Amazon Registrar (for .com, .net,
        and .org domains) or with contact information for our registrar associate,
        Gandi.

        This operation affects only the contact information for the specified contact
        type (registrant, administrator, or tech). If the request succeeds, Amazon Route
        53 returns an operation ID that you can use with GetOperationDetail to track the
        progress and completion of the action. If the request doesn't complete
        successfully, the domain registrant will be notified by email.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if admin_privacy is not ShapeBase.NOT_SET:
                _params['admin_privacy'] = admin_privacy
            if registrant_privacy is not ShapeBase.NOT_SET:
                _params['registrant_privacy'] = registrant_privacy
            if tech_privacy is not ShapeBase.NOT_SET:
                _params['tech_privacy'] = tech_privacy
            _request = shapes.UpdateDomainContactPrivacyRequest(**_params)
        response = self._boto_client.update_domain_contact_privacy(
            **_request.to_boto()
        )

        return shapes.UpdateDomainContactPrivacyResponse.from_boto(response)

    def update_domain_nameservers(
        self,
        _request: shapes.UpdateDomainNameserversRequest = None,
        *,
        domain_name: str,
        nameservers: typing.List[shapes.Nameserver],
        fi_auth_key: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDomainNameserversResponse:
        """
        This operation replaces the current set of name servers for the domain with the
        specified set of name servers. If you use Amazon Route 53 as your DNS service,
        specify the four name servers in the delegation set for the hosted zone for the
        domain.

        If successful, this operation returns an operation ID that you can use to track
        the progress and completion of the action. If the request is not completed
        successfully, the domain registrant will be notified by email.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if nameservers is not ShapeBase.NOT_SET:
                _params['nameservers'] = nameservers
            if fi_auth_key is not ShapeBase.NOT_SET:
                _params['fi_auth_key'] = fi_auth_key
            _request = shapes.UpdateDomainNameserversRequest(**_params)
        response = self._boto_client.update_domain_nameservers(
            **_request.to_boto()
        )

        return shapes.UpdateDomainNameserversResponse.from_boto(response)

    def update_tags_for_domain(
        self,
        _request: shapes.UpdateTagsForDomainRequest = None,
        *,
        domain_name: str,
        tags_to_update: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateTagsForDomainResponse:
        """
        This operation adds or updates tags for a specified domain.

        All tag operations are eventually consistent; subsequent operations might not
        immediately represent all issued operations.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if tags_to_update is not ShapeBase.NOT_SET:
                _params['tags_to_update'] = tags_to_update
            _request = shapes.UpdateTagsForDomainRequest(**_params)
        response = self._boto_client.update_tags_for_domain(
            **_request.to_boto()
        )

        return shapes.UpdateTagsForDomainResponse.from_boto(response)

    def view_billing(
        self,
        _request: shapes.ViewBillingRequest = None,
        *,
        start: datetime.datetime = ShapeBase.NOT_SET,
        end: datetime.datetime = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ViewBillingResponse:
        """
        Returns all the domain-related billing records for the current AWS account for a
        specified period
        """
        if _request is None:
            _params = {}
            if start is not ShapeBase.NOT_SET:
                _params['start'] = start
            if end is not ShapeBase.NOT_SET:
                _params['end'] = end
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ViewBillingRequest(**_params)
        response = self._boto_client.view_billing(**_request.to_boto())

        return shapes.ViewBillingResponse.from_boto(response)
