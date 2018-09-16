import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ses", *args, **kwargs)

    def clone_receipt_rule_set(
        self,
        _request: shapes.CloneReceiptRuleSetRequest = None,
        *,
        rule_set_name: str,
        original_rule_set_name: str,
    ) -> shapes.CloneReceiptRuleSetResponse:
        """
        Creates a receipt rule set by cloning an existing one. All receipt rules and
        configurations are copied to the new receipt rule set and are completely
        independent of the source rule set.

        For information about setting up rule sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        receipt-rule-set.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if original_rule_set_name is not ShapeBase.NOT_SET:
                _params['original_rule_set_name'] = original_rule_set_name
            _request = shapes.CloneReceiptRuleSetRequest(**_params)
        response = self._boto_client.clone_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.CloneReceiptRuleSetResponse.from_boto(response)

    def create_configuration_set(
        self,
        _request: shapes.CreateConfigurationSetRequest = None,
        *,
        configuration_set: shapes.ConfigurationSet,
    ) -> shapes.CreateConfigurationSetResponse:
        """
        Creates a configuration set.

        Configuration sets enable you to publish email sending events. For information
        about using configuration sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set is not ShapeBase.NOT_SET:
                _params['configuration_set'] = configuration_set
            _request = shapes.CreateConfigurationSetRequest(**_params)
        response = self._boto_client.create_configuration_set(
            **_request.to_boto()
        )

        return shapes.CreateConfigurationSetResponse.from_boto(response)

    def create_configuration_set_event_destination(
        self,
        _request: shapes.CreateConfigurationSetEventDestinationRequest = None,
        *,
        configuration_set_name: str,
        event_destination: shapes.EventDestination,
    ) -> shapes.CreateConfigurationSetEventDestinationResponse:
        """
        Creates a configuration set event destination.

        When you create or update an event destination, you must provide one, and only
        one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or
        Amazon Simple Notification Service (Amazon SNS).

        An event destination is the AWS service to which Amazon SES publishes the email
        sending events associated with a configuration set. For information about using
        configuration sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if event_destination is not ShapeBase.NOT_SET:
                _params['event_destination'] = event_destination
            _request = shapes.CreateConfigurationSetEventDestinationRequest(
                **_params
            )
        response = self._boto_client.create_configuration_set_event_destination(
            **_request.to_boto()
        )

        return shapes.CreateConfigurationSetEventDestinationResponse.from_boto(
            response
        )

    def create_configuration_set_tracking_options(
        self,
        _request: shapes.CreateConfigurationSetTrackingOptionsRequest = None,
        *,
        configuration_set_name: str,
        tracking_options: shapes.TrackingOptions,
    ) -> shapes.CreateConfigurationSetTrackingOptionsResponse:
        """
        Creates an association between a configuration set and a custom domain for open
        and click event tracking.

        By default, images and links used for tracking open and click events are hosted
        on domains operated by Amazon SES. You can configure a subdomain of your own to
        handle these events. For information about using custom domains, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-
        open-click-domains.html).
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if tracking_options is not ShapeBase.NOT_SET:
                _params['tracking_options'] = tracking_options
            _request = shapes.CreateConfigurationSetTrackingOptionsRequest(
                **_params
            )
        response = self._boto_client.create_configuration_set_tracking_options(
            **_request.to_boto()
        )

        return shapes.CreateConfigurationSetTrackingOptionsResponse.from_boto(
            response
        )

    def create_custom_verification_email_template(
        self,
        _request: shapes.CreateCustomVerificationEmailTemplateRequest = None,
        *,
        template_name: str,
        from_email_address: str,
        template_subject: str,
        template_content: str,
        success_redirection_url: str,
        failure_redirection_url: str,
    ) -> None:
        """
        Creates a new custom verification email template.

        For more information about custom verification email templates, see [Using
        Custom Verification Email
        Templates](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
        verification-emails.html) in the _Amazon SES Developer Guide_.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if from_email_address is not ShapeBase.NOT_SET:
                _params['from_email_address'] = from_email_address
            if template_subject is not ShapeBase.NOT_SET:
                _params['template_subject'] = template_subject
            if template_content is not ShapeBase.NOT_SET:
                _params['template_content'] = template_content
            if success_redirection_url is not ShapeBase.NOT_SET:
                _params['success_redirection_url'] = success_redirection_url
            if failure_redirection_url is not ShapeBase.NOT_SET:
                _params['failure_redirection_url'] = failure_redirection_url
            _request = shapes.CreateCustomVerificationEmailTemplateRequest(
                **_params
            )
        response = self._boto_client.create_custom_verification_email_template(
            **_request.to_boto()
        )

    def create_receipt_filter(
        self,
        _request: shapes.CreateReceiptFilterRequest = None,
        *,
        filter: shapes.ReceiptFilter,
    ) -> shapes.CreateReceiptFilterResponse:
        """
        Creates a new IP address filter.

        For information about setting up IP address filters, see the [Amazon SES
        Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
        email-ip-filters.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            _request = shapes.CreateReceiptFilterRequest(**_params)
        response = self._boto_client.create_receipt_filter(**_request.to_boto())

        return shapes.CreateReceiptFilterResponse.from_boto(response)

    def create_receipt_rule(
        self,
        _request: shapes.CreateReceiptRuleRequest = None,
        *,
        rule_set_name: str,
        rule: shapes.ReceiptRule,
        after: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateReceiptRuleResponse:
        """
        Creates a receipt rule.

        For information about setting up receipt rules, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        receipt-rules.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if rule is not ShapeBase.NOT_SET:
                _params['rule'] = rule
            if after is not ShapeBase.NOT_SET:
                _params['after'] = after
            _request = shapes.CreateReceiptRuleRequest(**_params)
        response = self._boto_client.create_receipt_rule(**_request.to_boto())

        return shapes.CreateReceiptRuleResponse.from_boto(response)

    def create_receipt_rule_set(
        self,
        _request: shapes.CreateReceiptRuleSetRequest = None,
        *,
        rule_set_name: str,
    ) -> shapes.CreateReceiptRuleSetResponse:
        """
        Creates an empty receipt rule set.

        For information about setting up receipt rule sets, see the [Amazon SES
        Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
        email-receipt-rule-set.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            _request = shapes.CreateReceiptRuleSetRequest(**_params)
        response = self._boto_client.create_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.CreateReceiptRuleSetResponse.from_boto(response)

    def create_template(
        self,
        _request: shapes.CreateTemplateRequest = None,
        *,
        template: shapes.Template,
    ) -> shapes.CreateTemplateResponse:
        """
        Creates an email template. Email templates enable you to send personalized email
        to one or more destinations in a single API operation. For more information, see
        the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
        email-api.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template is not ShapeBase.NOT_SET:
                _params['template'] = template
            _request = shapes.CreateTemplateRequest(**_params)
        response = self._boto_client.create_template(**_request.to_boto())

        return shapes.CreateTemplateResponse.from_boto(response)

    def delete_configuration_set(
        self,
        _request: shapes.DeleteConfigurationSetRequest = None,
        *,
        configuration_set_name: str,
    ) -> shapes.DeleteConfigurationSetResponse:
        """
        Deletes a configuration set. Configuration sets enable you to publish email
        sending events. For information about using configuration sets, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            _request = shapes.DeleteConfigurationSetRequest(**_params)
        response = self._boto_client.delete_configuration_set(
            **_request.to_boto()
        )

        return shapes.DeleteConfigurationSetResponse.from_boto(response)

    def delete_configuration_set_event_destination(
        self,
        _request: shapes.DeleteConfigurationSetEventDestinationRequest = None,
        *,
        configuration_set_name: str,
        event_destination_name: str,
    ) -> shapes.DeleteConfigurationSetEventDestinationResponse:
        """
        Deletes a configuration set event destination. Configuration set event
        destinations are associated with configuration sets, which enable you to publish
        email sending events. For information about using configuration sets, see the
        [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if event_destination_name is not ShapeBase.NOT_SET:
                _params['event_destination_name'] = event_destination_name
            _request = shapes.DeleteConfigurationSetEventDestinationRequest(
                **_params
            )
        response = self._boto_client.delete_configuration_set_event_destination(
            **_request.to_boto()
        )

        return shapes.DeleteConfigurationSetEventDestinationResponse.from_boto(
            response
        )

    def delete_configuration_set_tracking_options(
        self,
        _request: shapes.DeleteConfigurationSetTrackingOptionsRequest = None,
        *,
        configuration_set_name: str,
    ) -> shapes.DeleteConfigurationSetTrackingOptionsResponse:
        """
        Deletes an association between a configuration set and a custom domain for open
        and click event tracking.

        By default, images and links used for tracking open and click events are hosted
        on domains operated by Amazon SES. You can configure a subdomain of your own to
        handle these events. For information about using custom domains, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-
        open-click-domains.html).

        Deleting this kind of association will result in emails sent using the specified
        configuration set to capture open and click events using the standard, Amazon
        SES-operated domains.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            _request = shapes.DeleteConfigurationSetTrackingOptionsRequest(
                **_params
            )
        response = self._boto_client.delete_configuration_set_tracking_options(
            **_request.to_boto()
        )

        return shapes.DeleteConfigurationSetTrackingOptionsResponse.from_boto(
            response
        )

    def delete_custom_verification_email_template(
        self,
        _request: shapes.DeleteCustomVerificationEmailTemplateRequest = None,
        *,
        template_name: str,
    ) -> None:
        """
        Deletes an existing custom verification email template.

        For more information about custom verification email templates, see [Using
        Custom Verification Email
        Templates](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
        verification-emails.html) in the _Amazon SES Developer Guide_.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            _request = shapes.DeleteCustomVerificationEmailTemplateRequest(
                **_params
            )
        response = self._boto_client.delete_custom_verification_email_template(
            **_request.to_boto()
        )

    def delete_identity(
        self,
        _request: shapes.DeleteIdentityRequest = None,
        *,
        identity: str,
    ) -> shapes.DeleteIdentityResponse:
        """
        Deletes the specified identity (an email address or a domain) from the list of
        verified identities.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            _request = shapes.DeleteIdentityRequest(**_params)
        response = self._boto_client.delete_identity(**_request.to_boto())

        return shapes.DeleteIdentityResponse.from_boto(response)

    def delete_identity_policy(
        self,
        _request: shapes.DeleteIdentityPolicyRequest = None,
        *,
        identity: str,
        policy_name: str,
    ) -> shapes.DeleteIdentityPolicyResponse:
        """
        Deletes the specified sending authorization policy for the given identity (an
        email address or a domain). This API returns successfully even if a policy with
        the specified name does not exist.

        This API is for the identity owner only. If you have not verified the identity,
        this API will return an error.

        Sending authorization is a feature that enables an identity owner to authorize
        other senders to use its identities. For information about using sending
        authorization, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
        authorization.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeleteIdentityPolicyRequest(**_params)
        response = self._boto_client.delete_identity_policy(
            **_request.to_boto()
        )

        return shapes.DeleteIdentityPolicyResponse.from_boto(response)

    def delete_receipt_filter(
        self,
        _request: shapes.DeleteReceiptFilterRequest = None,
        *,
        filter_name: str,
    ) -> shapes.DeleteReceiptFilterResponse:
        """
        Deletes the specified IP address filter.

        For information about managing IP address filters, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-ip-filters.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if filter_name is not ShapeBase.NOT_SET:
                _params['filter_name'] = filter_name
            _request = shapes.DeleteReceiptFilterRequest(**_params)
        response = self._boto_client.delete_receipt_filter(**_request.to_boto())

        return shapes.DeleteReceiptFilterResponse.from_boto(response)

    def delete_receipt_rule(
        self,
        _request: shapes.DeleteReceiptRuleRequest = None,
        *,
        rule_set_name: str,
        rule_name: str,
    ) -> shapes.DeleteReceiptRuleResponse:
        """
        Deletes the specified receipt rule.

        For information about managing receipt rules, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rules.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            _request = shapes.DeleteReceiptRuleRequest(**_params)
        response = self._boto_client.delete_receipt_rule(**_request.to_boto())

        return shapes.DeleteReceiptRuleResponse.from_boto(response)

    def delete_receipt_rule_set(
        self,
        _request: shapes.DeleteReceiptRuleSetRequest = None,
        *,
        rule_set_name: str,
    ) -> shapes.DeleteReceiptRuleSetResponse:
        """
        Deletes the specified receipt rule set and all of the receipt rules it contains.

        The currently active rule set cannot be deleted.

        For information about managing receipt rule sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rule-sets.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            _request = shapes.DeleteReceiptRuleSetRequest(**_params)
        response = self._boto_client.delete_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.DeleteReceiptRuleSetResponse.from_boto(response)

    def delete_template(
        self,
        _request: shapes.DeleteTemplateRequest = None,
        *,
        template_name: str,
    ) -> shapes.DeleteTemplateResponse:
        """
        Deletes an email template.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            _request = shapes.DeleteTemplateRequest(**_params)
        response = self._boto_client.delete_template(**_request.to_boto())

        return shapes.DeleteTemplateResponse.from_boto(response)

    def delete_verified_email_address(
        self,
        _request: shapes.DeleteVerifiedEmailAddressRequest = None,
        *,
        email_address: str,
    ) -> None:
        """
        Deprecated. Use the `DeleteIdentity` operation to delete email addresses and
        domains.
        """
        if _request is None:
            _params = {}
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            _request = shapes.DeleteVerifiedEmailAddressRequest(**_params)
        response = self._boto_client.delete_verified_email_address(
            **_request.to_boto()
        )

    def describe_active_receipt_rule_set(
        self,
        _request: shapes.DescribeActiveReceiptRuleSetRequest = None,
    ) -> shapes.DescribeActiveReceiptRuleSetResponse:
        """
        Returns the metadata and receipt rules for the receipt rule set that is
        currently active.

        For information about setting up receipt rule sets, see the [Amazon SES
        Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
        email-receipt-rule-set.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeActiveReceiptRuleSetRequest(**_params)
        response = self._boto_client.describe_active_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.DescribeActiveReceiptRuleSetResponse.from_boto(response)

    def describe_configuration_set(
        self,
        _request: shapes.DescribeConfigurationSetRequest = None,
        *,
        configuration_set_name: str,
        configuration_set_attribute_names: typing.
        List[typing.Union[str, shapes.ConfigurationSetAttribute]
            ] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConfigurationSetResponse:
        """
        Returns the details of the specified configuration set. For information about
        using configuration sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if configuration_set_attribute_names is not ShapeBase.NOT_SET:
                _params['configuration_set_attribute_names'
                       ] = configuration_set_attribute_names
            _request = shapes.DescribeConfigurationSetRequest(**_params)
        response = self._boto_client.describe_configuration_set(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationSetResponse.from_boto(response)

    def describe_receipt_rule(
        self,
        _request: shapes.DescribeReceiptRuleRequest = None,
        *,
        rule_set_name: str,
        rule_name: str,
    ) -> shapes.DescribeReceiptRuleResponse:
        """
        Returns the details of the specified receipt rule.

        For information about setting up receipt rules, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        receipt-rules.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            _request = shapes.DescribeReceiptRuleRequest(**_params)
        response = self._boto_client.describe_receipt_rule(**_request.to_boto())

        return shapes.DescribeReceiptRuleResponse.from_boto(response)

    def describe_receipt_rule_set(
        self,
        _request: shapes.DescribeReceiptRuleSetRequest = None,
        *,
        rule_set_name: str,
    ) -> shapes.DescribeReceiptRuleSetResponse:
        """
        Returns the details of the specified receipt rule set.

        For information about managing receipt rule sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rule-sets.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            _request = shapes.DescribeReceiptRuleSetRequest(**_params)
        response = self._boto_client.describe_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.DescribeReceiptRuleSetResponse.from_boto(response)

    def get_account_sending_enabled(
        self,
    ) -> shapes.GetAccountSendingEnabledResponse:
        """
        Returns the email sending status of the Amazon SES account for the current
        region.

        You can execute this operation no more than once per second.
        """
        response = self._boto_client.get_account_sending_enabled()

        return shapes.GetAccountSendingEnabledResponse.from_boto(response)

    def get_custom_verification_email_template(
        self,
        _request: shapes.GetCustomVerificationEmailTemplateRequest = None,
        *,
        template_name: str,
    ) -> shapes.GetCustomVerificationEmailTemplateResponse:
        """
        Returns the custom email verification template for the template name you
        specify.

        For more information about custom verification email templates, see [Using
        Custom Verification Email
        Templates](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
        verification-emails.html) in the _Amazon SES Developer Guide_.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            _request = shapes.GetCustomVerificationEmailTemplateRequest(
                **_params
            )
        response = self._boto_client.get_custom_verification_email_template(
            **_request.to_boto()
        )

        return shapes.GetCustomVerificationEmailTemplateResponse.from_boto(
            response
        )

    def get_identity_dkim_attributes(
        self,
        _request: shapes.GetIdentityDkimAttributesRequest = None,
        *,
        identities: typing.List[str],
    ) -> shapes.GetIdentityDkimAttributesResponse:
        """
        Returns the current status of Easy DKIM signing for an entity. For domain name
        identities, this operation also returns the DKIM tokens that are required for
        Easy DKIM signing, and whether Amazon SES has successfully verified that these
        tokens have been published.

        This operation takes a list of identities as input and returns the following
        information for each:

          * Whether Easy DKIM signing is enabled or disabled.

          * A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.

          * Whether Amazon SES has successfully verified the DKIM tokens published in the domain's DNS. This information is only returned for domain name identities, not for email addresses.

        This operation is throttled at one request per second and can only get DKIM
        attributes for up to 100 identities at a time.

        For more information about creating DNS records using DKIM tokens, go to the
        [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-
        records.html).
        """
        if _request is None:
            _params = {}
            if identities is not ShapeBase.NOT_SET:
                _params['identities'] = identities
            _request = shapes.GetIdentityDkimAttributesRequest(**_params)
        response = self._boto_client.get_identity_dkim_attributes(
            **_request.to_boto()
        )

        return shapes.GetIdentityDkimAttributesResponse.from_boto(response)

    def get_identity_mail_from_domain_attributes(
        self,
        _request: shapes.GetIdentityMailFromDomainAttributesRequest = None,
        *,
        identities: typing.List[str],
    ) -> shapes.GetIdentityMailFromDomainAttributesResponse:
        """
        Returns the custom MAIL FROM attributes for a list of identities (email
        addresses : domains).

        This operation is throttled at one request per second and can only get custom
        MAIL FROM attributes for up to 100 identities at a time.
        """
        if _request is None:
            _params = {}
            if identities is not ShapeBase.NOT_SET:
                _params['identities'] = identities
            _request = shapes.GetIdentityMailFromDomainAttributesRequest(
                **_params
            )
        response = self._boto_client.get_identity_mail_from_domain_attributes(
            **_request.to_boto()
        )

        return shapes.GetIdentityMailFromDomainAttributesResponse.from_boto(
            response
        )

    def get_identity_notification_attributes(
        self,
        _request: shapes.GetIdentityNotificationAttributesRequest = None,
        *,
        identities: typing.List[str],
    ) -> shapes.GetIdentityNotificationAttributesResponse:
        """
        Given a list of verified identities (email addresses and/or domains), returns a
        structure describing identity notification attributes.

        This operation is throttled at one request per second and can only get
        notification attributes for up to 100 identities at a time.

        For more information about using notifications with Amazon SES, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html).
        """
        if _request is None:
            _params = {}
            if identities is not ShapeBase.NOT_SET:
                _params['identities'] = identities
            _request = shapes.GetIdentityNotificationAttributesRequest(
                **_params
            )
        response = self._boto_client.get_identity_notification_attributes(
            **_request.to_boto()
        )

        return shapes.GetIdentityNotificationAttributesResponse.from_boto(
            response
        )

    def get_identity_policies(
        self,
        _request: shapes.GetIdentityPoliciesRequest = None,
        *,
        identity: str,
        policy_names: typing.List[str],
    ) -> shapes.GetIdentityPoliciesResponse:
        """
        Returns the requested sending authorization policies for the given identity (an
        email address or a domain). The policies are returned as a map of policy names
        to policy contents. You can retrieve a maximum of 20 policies at a time.

        This API is for the identity owner only. If you have not verified the identity,
        this API will return an error.

        Sending authorization is a feature that enables an identity owner to authorize
        other senders to use its identities. For information about using sending
        authorization, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
        authorization.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if policy_names is not ShapeBase.NOT_SET:
                _params['policy_names'] = policy_names
            _request = shapes.GetIdentityPoliciesRequest(**_params)
        response = self._boto_client.get_identity_policies(**_request.to_boto())

        return shapes.GetIdentityPoliciesResponse.from_boto(response)

    def get_identity_verification_attributes(
        self,
        _request: shapes.GetIdentityVerificationAttributesRequest = None,
        *,
        identities: typing.List[str],
    ) -> shapes.GetIdentityVerificationAttributesResponse:
        """
        Given a list of identities (email addresses and/or domains), returns the
        verification status and (for domain identities) the verification token for each
        identity.

        The verification status of an email address is "Pending" until the email address
        owner clicks the link within the verification email that Amazon SES sent to that
        address. If the email address owner clicks the link within 24 hours, the
        verification status of the email address changes to "Success". If the link is
        not clicked within 24 hours, the verification status changes to "Failed." In
        that case, if you still want to verify the email address, you must restart the
        verification process from the beginning.

        For domain identities, the domain's verification status is "Pending" as Amazon
        SES searches for the required TXT record in the DNS settings of the domain. When
        Amazon SES detects the record, the domain's verification status changes to
        "Success". If Amazon SES is unable to detect the record within 72 hours, the
        domain's verification status changes to "Failed." In that case, if you still
        want to verify the domain, you must restart the verification process from the
        beginning.

        This operation is throttled at one request per second and can only get
        verification attributes for up to 100 identities at a time.
        """
        if _request is None:
            _params = {}
            if identities is not ShapeBase.NOT_SET:
                _params['identities'] = identities
            _request = shapes.GetIdentityVerificationAttributesRequest(
                **_params
            )
        response = self._boto_client.get_identity_verification_attributes(
            **_request.to_boto()
        )

        return shapes.GetIdentityVerificationAttributesResponse.from_boto(
            response
        )

    def get_send_quota(self) -> shapes.GetSendQuotaResponse:
        """
        Provides the sending limits for the Amazon SES account.

        You can execute this operation no more than once per second.
        """
        response = self._boto_client.get_send_quota()

        return shapes.GetSendQuotaResponse.from_boto(response)

    def get_send_statistics(self, ) -> shapes.GetSendStatisticsResponse:
        """
        Provides sending statistics for the current AWS Region. The result is a list of
        data points, representing the last two weeks of sending activity. Each data
        point in the list contains statistics for a 15-minute period of time.

        You can execute this operation no more than once per second.
        """
        response = self._boto_client.get_send_statistics()

        return shapes.GetSendStatisticsResponse.from_boto(response)

    def get_template(
        self,
        _request: shapes.GetTemplateRequest = None,
        *,
        template_name: str,
    ) -> shapes.GetTemplateResponse:
        """
        Displays the template object (which includes the Subject line, HTML part and
        text part) for the template you specify.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            _request = shapes.GetTemplateRequest(**_params)
        response = self._boto_client.get_template(**_request.to_boto())

        return shapes.GetTemplateResponse.from_boto(response)

    def list_configuration_sets(
        self,
        _request: shapes.ListConfigurationSetsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListConfigurationSetsResponse:
        """
        Provides a list of the configuration sets associated with your Amazon SES
        account in the current AWS Region. For information about using configuration
        sets, see [Monitoring Your Amazon SES Sending
        Activity](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html) in the _Amazon SES Developer Guide._

        You can execute this operation no more than once per second. This operation will
        return up to 1,000 configuration sets each time it is run. If your Amazon SES
        account has more than 1,000 configuration sets, this operation will also return
        a NextToken element. You can then execute the `ListConfigurationSets` operation
        again, passing the `NextToken` parameter and the value of the NextToken element
        to retrieve additional results.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListConfigurationSetsRequest(**_params)
        response = self._boto_client.list_configuration_sets(
            **_request.to_boto()
        )

        return shapes.ListConfigurationSetsResponse.from_boto(response)

    def list_custom_verification_email_templates(
        self,
        _request: shapes.ListCustomVerificationEmailTemplatesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListCustomVerificationEmailTemplatesResponse:
        """
        Lists the existing custom verification email templates for your account in the
        current AWS Region.

        For more information about custom verification email templates, see [Using
        Custom Verification Email
        Templates](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
        verification-emails.html) in the _Amazon SES Developer Guide_.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListCustomVerificationEmailTemplatesRequest(
                **_params
            )
        paginator = self.get_paginator(
            "list_custom_verification_email_templates"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCustomVerificationEmailTemplatesResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListCustomVerificationEmailTemplatesResponse.from_boto(
            response
        )

    def list_identities(
        self,
        _request: shapes.ListIdentitiesRequest = None,
        *,
        identity_type: typing.Union[str, shapes.IdentityType] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListIdentitiesResponse:
        """
        Returns a list containing all of the identities (email addresses and domains)
        for your AWS account in the current AWS Region, regardless of verification
        status.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity_type is not ShapeBase.NOT_SET:
                _params['identity_type'] = identity_type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListIdentitiesRequest(**_params)
        paginator = self.get_paginator("list_identities").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListIdentitiesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListIdentitiesResponse.from_boto(response)

    def list_identity_policies(
        self,
        _request: shapes.ListIdentityPoliciesRequest = None,
        *,
        identity: str,
    ) -> shapes.ListIdentityPoliciesResponse:
        """
        Returns a list of sending authorization policies that are attached to the given
        identity (an email address or a domain). This API returns only a list. If you
        want the actual policy content, you can use `GetIdentityPolicies`.

        This API is for the identity owner only. If you have not verified the identity,
        this API will return an error.

        Sending authorization is a feature that enables an identity owner to authorize
        other senders to use its identities. For information about using sending
        authorization, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
        authorization.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            _request = shapes.ListIdentityPoliciesRequest(**_params)
        response = self._boto_client.list_identity_policies(
            **_request.to_boto()
        )

        return shapes.ListIdentityPoliciesResponse.from_boto(response)

    def list_receipt_filters(
        self,
        _request: shapes.ListReceiptFiltersRequest = None,
    ) -> shapes.ListReceiptFiltersResponse:
        """
        Lists the IP address filters associated with your AWS account in the current AWS
        Region.

        For information about managing IP address filters, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-ip-filters.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            _request = shapes.ListReceiptFiltersRequest(**_params)
        response = self._boto_client.list_receipt_filters(**_request.to_boto())

        return shapes.ListReceiptFiltersResponse.from_boto(response)

    def list_receipt_rule_sets(
        self,
        _request: shapes.ListReceiptRuleSetsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListReceiptRuleSetsResponse:
        """
        Lists the receipt rule sets that exist under your AWS account in the current AWS
        Region. If there are additional receipt rule sets to be retrieved, you will
        receive a `NextToken` that you can provide to the next call to
        `ListReceiptRuleSets` to retrieve the additional entries.

        For information about managing receipt rule sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rule-sets.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListReceiptRuleSetsRequest(**_params)
        response = self._boto_client.list_receipt_rule_sets(
            **_request.to_boto()
        )

        return shapes.ListReceiptRuleSetsResponse.from_boto(response)

    def list_templates(
        self,
        _request: shapes.ListTemplatesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTemplatesResponse:
        """
        Lists the email templates present in your Amazon SES account in the current AWS
        Region.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.ListTemplatesRequest(**_params)
        response = self._boto_client.list_templates(**_request.to_boto())

        return shapes.ListTemplatesResponse.from_boto(response)

    def list_verified_email_addresses(
        self,
    ) -> shapes.ListVerifiedEmailAddressesResponse:
        """
        Deprecated. Use the `ListIdentities` operation to list the email addresses and
        domains associated with your account.
        """
        response = self._boto_client.list_verified_email_addresses()

        return shapes.ListVerifiedEmailAddressesResponse.from_boto(response)

    def put_identity_policy(
        self,
        _request: shapes.PutIdentityPolicyRequest = None,
        *,
        identity: str,
        policy_name: str,
        policy: str,
    ) -> shapes.PutIdentityPolicyResponse:
        """
        Adds or updates a sending authorization policy for the specified identity (an
        email address or a domain).

        This API is for the identity owner only. If you have not verified the identity,
        this API will return an error.

        Sending authorization is a feature that enables an identity owner to authorize
        other senders to use its identities. For information about using sending
        authorization, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
        authorization.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            _request = shapes.PutIdentityPolicyRequest(**_params)
        response = self._boto_client.put_identity_policy(**_request.to_boto())

        return shapes.PutIdentityPolicyResponse.from_boto(response)

    def reorder_receipt_rule_set(
        self,
        _request: shapes.ReorderReceiptRuleSetRequest = None,
        *,
        rule_set_name: str,
        rule_names: typing.List[str],
    ) -> shapes.ReorderReceiptRuleSetResponse:
        """
        Reorders the receipt rules within a receipt rule set.

        All of the rules in the rule set must be represented in this request. That is,
        this API will return an error if the reorder request doesn't explicitly position
        all of the rules.

        For information about managing receipt rule sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rule-sets.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if rule_names is not ShapeBase.NOT_SET:
                _params['rule_names'] = rule_names
            _request = shapes.ReorderReceiptRuleSetRequest(**_params)
        response = self._boto_client.reorder_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.ReorderReceiptRuleSetResponse.from_boto(response)

    def send_bounce(
        self,
        _request: shapes.SendBounceRequest = None,
        *,
        original_message_id: str,
        bounce_sender: str,
        bounced_recipient_info_list: typing.List[shapes.BouncedRecipientInfo],
        explanation: str = ShapeBase.NOT_SET,
        message_dsn: shapes.MessageDsn = ShapeBase.NOT_SET,
        bounce_sender_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.SendBounceResponse:
        """
        Generates and sends a bounce message to the sender of an email you received
        through Amazon SES. You can only use this API on an email up to 24 hours after
        you receive it.

        You cannot use this API to send generic bounces for mail that was not received
        by Amazon SES.

        For information about receiving email through Amazon SES, see the [Amazon SES
        Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
        email.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if original_message_id is not ShapeBase.NOT_SET:
                _params['original_message_id'] = original_message_id
            if bounce_sender is not ShapeBase.NOT_SET:
                _params['bounce_sender'] = bounce_sender
            if bounced_recipient_info_list is not ShapeBase.NOT_SET:
                _params['bounced_recipient_info_list'
                       ] = bounced_recipient_info_list
            if explanation is not ShapeBase.NOT_SET:
                _params['explanation'] = explanation
            if message_dsn is not ShapeBase.NOT_SET:
                _params['message_dsn'] = message_dsn
            if bounce_sender_arn is not ShapeBase.NOT_SET:
                _params['bounce_sender_arn'] = bounce_sender_arn
            _request = shapes.SendBounceRequest(**_params)
        response = self._boto_client.send_bounce(**_request.to_boto())

        return shapes.SendBounceResponse.from_boto(response)

    def send_bulk_templated_email(
        self,
        _request: shapes.SendBulkTemplatedEmailRequest = None,
        *,
        source: str,
        template: str,
        destinations: typing.List[shapes.BulkEmailDestination],
        source_arn: str = ShapeBase.NOT_SET,
        reply_to_addresses: typing.List[str] = ShapeBase.NOT_SET,
        return_path: str = ShapeBase.NOT_SET,
        return_path_arn: str = ShapeBase.NOT_SET,
        configuration_set_name: str = ShapeBase.NOT_SET,
        default_tags: typing.List[shapes.MessageTag] = ShapeBase.NOT_SET,
        template_arn: str = ShapeBase.NOT_SET,
        default_template_data: str = ShapeBase.NOT_SET,
    ) -> shapes.SendBulkTemplatedEmailResponse:
        """
        Composes an email message to multiple destinations. The message body is created
        using an email template.

        In order to send email using the `SendBulkTemplatedEmail` operation, your call
        to the API must meet the following requirements:

          * The call must refer to an existing email template. You can create email templates using the CreateTemplate operation.

          * The message must be sent from a verified email address or domain.

          * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) in the _Amazon SES Developer Guide._

          * The maximum message size is 10 MB.

          * Each `Destination` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format _UserName@[SubDomain.]Domain.TopLevelDomain_ ), the entire message will be rejected, even if the message contains other recipients that are valid.

          * The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the `SendBulkTemplatedEmail` operation several times to send the message to each group.

          * The number of destinations you can contact in a single call to the API may be limited by your account's maximum sending rate.
        """
        if _request is None:
            _params = {}
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if template is not ShapeBase.NOT_SET:
                _params['template'] = template
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            if source_arn is not ShapeBase.NOT_SET:
                _params['source_arn'] = source_arn
            if reply_to_addresses is not ShapeBase.NOT_SET:
                _params['reply_to_addresses'] = reply_to_addresses
            if return_path is not ShapeBase.NOT_SET:
                _params['return_path'] = return_path
            if return_path_arn is not ShapeBase.NOT_SET:
                _params['return_path_arn'] = return_path_arn
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if default_tags is not ShapeBase.NOT_SET:
                _params['default_tags'] = default_tags
            if template_arn is not ShapeBase.NOT_SET:
                _params['template_arn'] = template_arn
            if default_template_data is not ShapeBase.NOT_SET:
                _params['default_template_data'] = default_template_data
            _request = shapes.SendBulkTemplatedEmailRequest(**_params)
        response = self._boto_client.send_bulk_templated_email(
            **_request.to_boto()
        )

        return shapes.SendBulkTemplatedEmailResponse.from_boto(response)

    def send_custom_verification_email(
        self,
        _request: shapes.SendCustomVerificationEmailRequest = None,
        *,
        email_address: str,
        template_name: str,
        configuration_set_name: str = ShapeBase.NOT_SET,
    ) -> shapes.SendCustomVerificationEmailResponse:
        """
        Adds an email address to the list of identities for your Amazon SES account in
        the current AWS Region and attempts to verify it. As a result of executing this
        operation, a customized verification email is sent to the specified address.

        To use this operation, you must first create a custom verification email
        template. For more information about creating and using custom verification
        email templates, see [Using Custom Verification Email
        Templates](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
        verification-emails.html) in the _Amazon SES Developer Guide_.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            _request = shapes.SendCustomVerificationEmailRequest(**_params)
        response = self._boto_client.send_custom_verification_email(
            **_request.to_boto()
        )

        return shapes.SendCustomVerificationEmailResponse.from_boto(response)

    def send_email(
        self,
        _request: shapes.SendEmailRequest = None,
        *,
        source: str,
        destination: shapes.Destination,
        message: shapes.Message,
        reply_to_addresses: typing.List[str] = ShapeBase.NOT_SET,
        return_path: str = ShapeBase.NOT_SET,
        source_arn: str = ShapeBase.NOT_SET,
        return_path_arn: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.MessageTag] = ShapeBase.NOT_SET,
        configuration_set_name: str = ShapeBase.NOT_SET,
    ) -> shapes.SendEmailResponse:
        """
        Composes an email message and immediately queues it for sending. In order to
        send email using the `SendEmail` operation, your message must meet the following
        requirements:

          * The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an "Email address not verified" error. 

          * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) in the _Amazon SES Developer Guide._

          * The maximum message size is 10 MB.

          * The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format _UserName@[SubDomain.]Domain.TopLevelDomain_ ), the entire message will be rejected, even if the message contains other recipients that are valid.

          * The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the `SendEmail` operation several times to send the message to each group.

        For every message that you send, the total number of recipients (including each
        recipient in the To:, CC: and BCC: fields) is counted against the maximum number
        of emails you can send in a 24-hour period (your _sending quota_ ). For more
        information about sending quotas in Amazon SES, see [Managing Your Amazon SES
        Sending Limits](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-
        sending-limits.html) in the _Amazon SES Developer Guide._
        """
        if _request is None:
            _params = {}
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if destination is not ShapeBase.NOT_SET:
                _params['destination'] = destination
            if message is not ShapeBase.NOT_SET:
                _params['message'] = message
            if reply_to_addresses is not ShapeBase.NOT_SET:
                _params['reply_to_addresses'] = reply_to_addresses
            if return_path is not ShapeBase.NOT_SET:
                _params['return_path'] = return_path
            if source_arn is not ShapeBase.NOT_SET:
                _params['source_arn'] = source_arn
            if return_path_arn is not ShapeBase.NOT_SET:
                _params['return_path_arn'] = return_path_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            _request = shapes.SendEmailRequest(**_params)
        response = self._boto_client.send_email(**_request.to_boto())

        return shapes.SendEmailResponse.from_boto(response)

    def send_raw_email(
        self,
        _request: shapes.SendRawEmailRequest = None,
        *,
        raw_message: shapes.RawMessage,
        source: str = ShapeBase.NOT_SET,
        destinations: typing.List[str] = ShapeBase.NOT_SET,
        from_arn: str = ShapeBase.NOT_SET,
        source_arn: str = ShapeBase.NOT_SET,
        return_path_arn: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.MessageTag] = ShapeBase.NOT_SET,
        configuration_set_name: str = ShapeBase.NOT_SET,
    ) -> shapes.SendRawEmailResponse:
        """
        Composes an email message and immediately queues it for sending.

        This operation is more flexible than the `SendEmail` API operation. When you use
        the `SendRawEmail` operation, you can specify the headers of the message as well
        as its content. This flexibility is useful, for example, when you want to send a
        multipart MIME email (such a message that contains both a text and an HTML
        version). You can also use this operation to send messages that include
        attachments.

        The `SendRawEmail` operation has the following requirements:

          * You can only send email from [verified email addresses or domains](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html). If you try to send email from an address that isn't verified, the operation results in an "Email address not verified" error.

          * If your account is still in the [Amazon SES sandbox](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html), you can only send email to other verified addresses in your account, or to addresses that are associated with the [Amazon SES mailbox simulator](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mailbox-simulator.html).

          * The maximum message size, including attachments, is 10 MB.

          * Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.

          * If you send a single message to more than one recipient address, and one of the recipient addresses isn't in a valid format (that is, it's not in the format _UserName@[SubDomain.]Domain.TopLevelDomain_ ), Amazon SES rejects the entire message, even if the other addresses are valid.

          * Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.

          * Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isn't preserved. For this reason, we highly recommend that you encode all content that isn't 7-bit ASCII. For more information, see [MIME Encoding](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html#send-email-mime-encoding) in the _Amazon SES Developer Guide_.

        Additionally, keep the following considerations in mind when using the
        `SendRawEmail` operation:

          * Although you can customize the message headers when using the `SendRawEmail` operation, Amazon SES will automatically apply its own `Message-ID` and `Date` headers; if you passed these headers when creating the message, they will be overwritten by the values that Amazon SES provides.

          * If you are using sending authorization to send on behalf of another user, `SendRawEmail` enables you to specify the cross-account identity for the email's Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters `SourceArn`, `FromArn`, and/or `ReturnPathArn` to the API, or you can include the following X-headers in the header of your raw email:

            * `X-SES-SOURCE-ARN`

            * `X-SES-FROM-ARN`

            * `X-SES-RETURN-PATH-ARN`

        Do not include these X-headers in the DKIM signature; Amazon SES will remove
        them before sending the email.

        For most common sending authorization scenarios, we recommend that you specify
        the `SourceIdentityArn` parameter and not the `FromIdentityArn` or
        `ReturnPathIdentityArn` parameters. If you only specify the `SourceIdentityArn`
        parameter, Amazon SES will set the From and Return Path addresses to the
        identity specified in `SourceIdentityArn`. For more information about sending
        authorization, see the [Using Sending Authorization with Amazon
        SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
        authorization.html) in the _Amazon SES Developer Guide._

          * For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your _sending quota_ ). For more information about sending quotas in Amazon SES, see [Managing Your Amazon SES Sending Limits](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html) in the _Amazon SES Developer Guide._
        """
        if _request is None:
            _params = {}
            if raw_message is not ShapeBase.NOT_SET:
                _params['raw_message'] = raw_message
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            if from_arn is not ShapeBase.NOT_SET:
                _params['from_arn'] = from_arn
            if source_arn is not ShapeBase.NOT_SET:
                _params['source_arn'] = source_arn
            if return_path_arn is not ShapeBase.NOT_SET:
                _params['return_path_arn'] = return_path_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            _request = shapes.SendRawEmailRequest(**_params)
        response = self._boto_client.send_raw_email(**_request.to_boto())

        return shapes.SendRawEmailResponse.from_boto(response)

    def send_templated_email(
        self,
        _request: shapes.SendTemplatedEmailRequest = None,
        *,
        source: str,
        destination: shapes.Destination,
        template: str,
        template_data: str,
        reply_to_addresses: typing.List[str] = ShapeBase.NOT_SET,
        return_path: str = ShapeBase.NOT_SET,
        source_arn: str = ShapeBase.NOT_SET,
        return_path_arn: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.MessageTag] = ShapeBase.NOT_SET,
        configuration_set_name: str = ShapeBase.NOT_SET,
        template_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.SendTemplatedEmailResponse:
        """
        Composes an email message using an email template and immediately queues it for
        sending.

        In order to send email using the `SendTemplatedEmail` operation, your call to
        the API must meet the following requirements:

          * The call must refer to an existing email template. You can create email templates using the CreateTemplate operation.

          * The message must be sent from a verified email address or domain.

          * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) in the _Amazon SES Developer Guide._

          * The maximum message size is 10 MB.

          * Calls to the `SendTemplatedEmail` operation may only include one `Destination` parameter. A destination is a set of recipients who will receive the same version of the email. The `Destination` parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.

          * The `Destination` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format _UserName@[SubDomain.]Domain.TopLevelDomain_ ), the entire message will be rejected, even if the message contains other recipients that are valid.

        If your call to the `SendTemplatedEmail` operation includes all of the required
        parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon
        SES can't render the email because the template contains errors, it doesn't send
        the email. Additionally, because it already accepted the message, Amazon SES
        doesn't return a message stating that it was unable to send the email.

        For these reasons, we highly recommend that you set up Amazon SES to send you
        notifications when Rendering Failure events occur. For more information, see
        [Sending Personalized Email Using the Amazon SES
        API](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
        email-api.html) in the _Amazon Simple Email Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if destination is not ShapeBase.NOT_SET:
                _params['destination'] = destination
            if template is not ShapeBase.NOT_SET:
                _params['template'] = template
            if template_data is not ShapeBase.NOT_SET:
                _params['template_data'] = template_data
            if reply_to_addresses is not ShapeBase.NOT_SET:
                _params['reply_to_addresses'] = reply_to_addresses
            if return_path is not ShapeBase.NOT_SET:
                _params['return_path'] = return_path
            if source_arn is not ShapeBase.NOT_SET:
                _params['source_arn'] = source_arn
            if return_path_arn is not ShapeBase.NOT_SET:
                _params['return_path_arn'] = return_path_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if template_arn is not ShapeBase.NOT_SET:
                _params['template_arn'] = template_arn
            _request = shapes.SendTemplatedEmailRequest(**_params)
        response = self._boto_client.send_templated_email(**_request.to_boto())

        return shapes.SendTemplatedEmailResponse.from_boto(response)

    def set_active_receipt_rule_set(
        self,
        _request: shapes.SetActiveReceiptRuleSetRequest = None,
        *,
        rule_set_name: str = ShapeBase.NOT_SET,
    ) -> shapes.SetActiveReceiptRuleSetResponse:
        """
        Sets the specified receipt rule set as the active receipt rule set.

        To disable your email-receiving through Amazon SES completely, you can call this
        API with RuleSetName set to null.

        For information about managing receipt rule sets, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rule-sets.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            _request = shapes.SetActiveReceiptRuleSetRequest(**_params)
        response = self._boto_client.set_active_receipt_rule_set(
            **_request.to_boto()
        )

        return shapes.SetActiveReceiptRuleSetResponse.from_boto(response)

    def set_identity_dkim_enabled(
        self,
        _request: shapes.SetIdentityDkimEnabledRequest = None,
        *,
        identity: str,
        dkim_enabled: bool,
    ) -> shapes.SetIdentityDkimEnabledResponse:
        """
        Enables or disables Easy DKIM signing of email sent from an identity:

          * If Easy DKIM signing is enabled for a domain name identity (such as `example.com`), then Amazon SES will DKIM-sign all email sent by addresses under that domain name (for example, `user@example.com`).

          * If Easy DKIM signing is enabled for an email address, then Amazon SES will DKIM-sign all email sent by that email address.

        For email addresses (for example, `user@example.com`), you can only enable Easy
        DKIM signing if the corresponding domain (in this case, `example.com`) has been
        set up for Easy DKIM using the AWS Console or the `VerifyDomainDkim` operation.

        You can execute this operation no more than once per second.

        For more information about Easy DKIM signing, go to the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html).
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if dkim_enabled is not ShapeBase.NOT_SET:
                _params['dkim_enabled'] = dkim_enabled
            _request = shapes.SetIdentityDkimEnabledRequest(**_params)
        response = self._boto_client.set_identity_dkim_enabled(
            **_request.to_boto()
        )

        return shapes.SetIdentityDkimEnabledResponse.from_boto(response)

    def set_identity_feedback_forwarding_enabled(
        self,
        _request: shapes.SetIdentityFeedbackForwardingEnabledRequest = None,
        *,
        identity: str,
        forwarding_enabled: bool,
    ) -> shapes.SetIdentityFeedbackForwardingEnabledResponse:
        """
        Given an identity (an email address or a domain), enables or disables whether
        Amazon SES forwards bounce and complaint notifications as email. Feedback
        forwarding can only be disabled when Amazon Simple Notification Service (Amazon
        SNS) topics are specified for both bounces and complaints.

        Feedback forwarding does not apply to delivery notifications. Delivery
        notifications are only available through Amazon SNS.

        You can execute this operation no more than once per second.

        For more information about using notifications with Amazon SES, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html).
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if forwarding_enabled is not ShapeBase.NOT_SET:
                _params['forwarding_enabled'] = forwarding_enabled
            _request = shapes.SetIdentityFeedbackForwardingEnabledRequest(
                **_params
            )
        response = self._boto_client.set_identity_feedback_forwarding_enabled(
            **_request.to_boto()
        )

        return shapes.SetIdentityFeedbackForwardingEnabledResponse.from_boto(
            response
        )

    def set_identity_headers_in_notifications_enabled(
        self,
        _request: shapes.SetIdentityHeadersInNotificationsEnabledRequest = None,
        *,
        identity: str,
        notification_type: typing.Union[str, shapes.NotificationType],
        enabled: bool,
    ) -> shapes.SetIdentityHeadersInNotificationsEnabledResponse:
        """
        Given an identity (an email address or a domain), sets whether Amazon SES
        includes the original email headers in the Amazon Simple Notification Service
        (Amazon SNS) notifications of a specified type.

        You can execute this operation no more than once per second.

        For more information about using notifications with Amazon SES, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html).
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if notification_type is not ShapeBase.NOT_SET:
                _params['notification_type'] = notification_type
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.SetIdentityHeadersInNotificationsEnabledRequest(
                **_params
            )
        response = self._boto_client.set_identity_headers_in_notifications_enabled(
            **_request.to_boto()
        )

        return shapes.SetIdentityHeadersInNotificationsEnabledResponse.from_boto(
            response
        )

    def set_identity_mail_from_domain(
        self,
        _request: shapes.SetIdentityMailFromDomainRequest = None,
        *,
        identity: str,
        mail_from_domain: str = ShapeBase.NOT_SET,
        behavior_on_mx_failure: typing.
        Union[str, shapes.BehaviorOnMXFailure] = ShapeBase.NOT_SET,
    ) -> shapes.SetIdentityMailFromDomainResponse:
        """
        Enables or disables the custom MAIL FROM domain setup for a verified identity
        (an email address or a domain).

        To send emails using the specified MAIL FROM domain, you must add an MX record
        to your MAIL FROM domain's DNS settings. If you want your emails to pass Sender
        Policy Framework (SPF) checks, you must also add or update an SPF record. For
        more information, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if mail_from_domain is not ShapeBase.NOT_SET:
                _params['mail_from_domain'] = mail_from_domain
            if behavior_on_mx_failure is not ShapeBase.NOT_SET:
                _params['behavior_on_mx_failure'] = behavior_on_mx_failure
            _request = shapes.SetIdentityMailFromDomainRequest(**_params)
        response = self._boto_client.set_identity_mail_from_domain(
            **_request.to_boto()
        )

        return shapes.SetIdentityMailFromDomainResponse.from_boto(response)

    def set_identity_notification_topic(
        self,
        _request: shapes.SetIdentityNotificationTopicRequest = None,
        *,
        identity: str,
        notification_type: typing.Union[str, shapes.NotificationType],
        sns_topic: str = ShapeBase.NOT_SET,
    ) -> shapes.SetIdentityNotificationTopicResponse:
        """
        Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when
        delivering notifications. When you use this operation, you specify a verified
        identity, such as an email address or domain. When you send an email that uses
        the chosen identity in the Source field, Amazon SES sends notifications to the
        topic you specified. You can send bounce, complaint, or delivery notifications
        (or any combination of the three) to the Amazon SNS topic that you specify.

        You can execute this operation no more than once per second.

        For more information about feedback notification, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html).
        """
        if _request is None:
            _params = {}
            if identity is not ShapeBase.NOT_SET:
                _params['identity'] = identity
            if notification_type is not ShapeBase.NOT_SET:
                _params['notification_type'] = notification_type
            if sns_topic is not ShapeBase.NOT_SET:
                _params['sns_topic'] = sns_topic
            _request = shapes.SetIdentityNotificationTopicRequest(**_params)
        response = self._boto_client.set_identity_notification_topic(
            **_request.to_boto()
        )

        return shapes.SetIdentityNotificationTopicResponse.from_boto(response)

    def set_receipt_rule_position(
        self,
        _request: shapes.SetReceiptRulePositionRequest = None,
        *,
        rule_set_name: str,
        rule_name: str,
        after: str = ShapeBase.NOT_SET,
    ) -> shapes.SetReceiptRulePositionResponse:
        """
        Sets the position of the specified receipt rule in the receipt rule set.

        For information about managing receipt rules, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rules.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            if after is not ShapeBase.NOT_SET:
                _params['after'] = after
            _request = shapes.SetReceiptRulePositionRequest(**_params)
        response = self._boto_client.set_receipt_rule_position(
            **_request.to_boto()
        )

        return shapes.SetReceiptRulePositionResponse.from_boto(response)

    def test_render_template(
        self,
        _request: shapes.TestRenderTemplateRequest = None,
        *,
        template_name: str,
        template_data: str,
    ) -> shapes.TestRenderTemplateResponse:
        """
        Creates a preview of the MIME content of an email when provided with a template
        and a set of replacement data.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if template_data is not ShapeBase.NOT_SET:
                _params['template_data'] = template_data
            _request = shapes.TestRenderTemplateRequest(**_params)
        response = self._boto_client.test_render_template(**_request.to_boto())

        return shapes.TestRenderTemplateResponse.from_boto(response)

    def update_account_sending_enabled(
        self,
        _request: shapes.UpdateAccountSendingEnabledRequest = None,
        *,
        enabled: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Enables or disables email sending across your entire Amazon SES account in the
        current AWS Region. You can use this operation in conjunction with Amazon
        CloudWatch alarms to temporarily pause email sending across your Amazon SES
        account in a given AWS Region when reputation metrics (such as your bounce or
        complaint rates) reach certain thresholds.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.UpdateAccountSendingEnabledRequest(**_params)
        response = self._boto_client.update_account_sending_enabled(
            **_request.to_boto()
        )

    def update_configuration_set_event_destination(
        self,
        _request: shapes.UpdateConfigurationSetEventDestinationRequest = None,
        *,
        configuration_set_name: str,
        event_destination: shapes.EventDestination,
    ) -> shapes.UpdateConfigurationSetEventDestinationResponse:
        """
        Updates the event destination of a configuration set. Event destinations are
        associated with configuration sets, which enable you to publish email sending
        events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple
        Notification Service (Amazon SNS). For information about using configuration
        sets, see [Monitoring Your Amazon SES Sending
        Activity](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
        activity.html) in the _Amazon SES Developer Guide._

        When you create or update an event destination, you must provide one, and only
        one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis
        Firehose, or Amazon Simple Notification Service (Amazon SNS).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if event_destination is not ShapeBase.NOT_SET:
                _params['event_destination'] = event_destination
            _request = shapes.UpdateConfigurationSetEventDestinationRequest(
                **_params
            )
        response = self._boto_client.update_configuration_set_event_destination(
            **_request.to_boto()
        )

        return shapes.UpdateConfigurationSetEventDestinationResponse.from_boto(
            response
        )

    def update_configuration_set_reputation_metrics_enabled(
        self,
        _request: shapes.
        UpdateConfigurationSetReputationMetricsEnabledRequest = None,
        *,
        configuration_set_name: str,
        enabled: bool,
    ) -> None:
        """
        Enables or disables the publishing of reputation metrics for emails sent using a
        specific configuration set in a given AWS Region. Reputation metrics include
        bounce and complaint rates. These metrics are published to Amazon CloudWatch. By
        using CloudWatch, you can create alarms when bounce or complaint rates exceed
        certain thresholds.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.UpdateConfigurationSetReputationMetricsEnabledRequest(
                **_params
            )
        response = self._boto_client.update_configuration_set_reputation_metrics_enabled(
            **_request.to_boto()
        )

    def update_configuration_set_sending_enabled(
        self,
        _request: shapes.UpdateConfigurationSetSendingEnabledRequest = None,
        *,
        configuration_set_name: str,
        enabled: bool,
    ) -> None:
        """
        Enables or disables email sending for messages sent using a specific
        configuration set in a given AWS Region. You can use this operation in
        conjunction with Amazon CloudWatch alarms to temporarily pause email sending for
        a configuration set when the reputation metrics for that configuration set (such
        as your bounce on complaint rate) exceed certain thresholds.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.UpdateConfigurationSetSendingEnabledRequest(
                **_params
            )
        response = self._boto_client.update_configuration_set_sending_enabled(
            **_request.to_boto()
        )

    def update_configuration_set_tracking_options(
        self,
        _request: shapes.UpdateConfigurationSetTrackingOptionsRequest = None,
        *,
        configuration_set_name: str,
        tracking_options: shapes.TrackingOptions,
    ) -> shapes.UpdateConfigurationSetTrackingOptionsResponse:
        """
        Modifies an association between a configuration set and a custom domain for open
        and click event tracking.

        By default, images and links used for tracking open and click events are hosted
        on domains operated by Amazon SES. You can configure a subdomain of your own to
        handle these events. For information about using custom domains, see the [Amazon
        SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-
        open-click-domains.html).
        """
        if _request is None:
            _params = {}
            if configuration_set_name is not ShapeBase.NOT_SET:
                _params['configuration_set_name'] = configuration_set_name
            if tracking_options is not ShapeBase.NOT_SET:
                _params['tracking_options'] = tracking_options
            _request = shapes.UpdateConfigurationSetTrackingOptionsRequest(
                **_params
            )
        response = self._boto_client.update_configuration_set_tracking_options(
            **_request.to_boto()
        )

        return shapes.UpdateConfigurationSetTrackingOptionsResponse.from_boto(
            response
        )

    def update_custom_verification_email_template(
        self,
        _request: shapes.UpdateCustomVerificationEmailTemplateRequest = None,
        *,
        template_name: str,
        from_email_address: str = ShapeBase.NOT_SET,
        template_subject: str = ShapeBase.NOT_SET,
        template_content: str = ShapeBase.NOT_SET,
        success_redirection_url: str = ShapeBase.NOT_SET,
        failure_redirection_url: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates an existing custom verification email template.

        For more information about custom verification email templates, see [Using
        Custom Verification Email
        Templates](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
        verification-emails.html) in the _Amazon SES Developer Guide_.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if from_email_address is not ShapeBase.NOT_SET:
                _params['from_email_address'] = from_email_address
            if template_subject is not ShapeBase.NOT_SET:
                _params['template_subject'] = template_subject
            if template_content is not ShapeBase.NOT_SET:
                _params['template_content'] = template_content
            if success_redirection_url is not ShapeBase.NOT_SET:
                _params['success_redirection_url'] = success_redirection_url
            if failure_redirection_url is not ShapeBase.NOT_SET:
                _params['failure_redirection_url'] = failure_redirection_url
            _request = shapes.UpdateCustomVerificationEmailTemplateRequest(
                **_params
            )
        response = self._boto_client.update_custom_verification_email_template(
            **_request.to_boto()
        )

    def update_receipt_rule(
        self,
        _request: shapes.UpdateReceiptRuleRequest = None,
        *,
        rule_set_name: str,
        rule: shapes.ReceiptRule,
    ) -> shapes.UpdateReceiptRuleResponse:
        """
        Updates a receipt rule.

        For information about managing receipt rules, see the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
        managing-receipt-rules.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if rule is not ShapeBase.NOT_SET:
                _params['rule'] = rule
            _request = shapes.UpdateReceiptRuleRequest(**_params)
        response = self._boto_client.update_receipt_rule(**_request.to_boto())

        return shapes.UpdateReceiptRuleResponse.from_boto(response)

    def update_template(
        self,
        _request: shapes.UpdateTemplateRequest = None,
        *,
        template: shapes.Template,
    ) -> shapes.UpdateTemplateResponse:
        """
        Updates an email template. Email templates enable you to send personalized email
        to one or more destinations in a single API operation. For more information, see
        the [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
        email-api.html).

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if template is not ShapeBase.NOT_SET:
                _params['template'] = template
            _request = shapes.UpdateTemplateRequest(**_params)
        response = self._boto_client.update_template(**_request.to_boto())

        return shapes.UpdateTemplateResponse.from_boto(response)

    def verify_domain_dkim(
        self,
        _request: shapes.VerifyDomainDkimRequest = None,
        *,
        domain: str,
    ) -> shapes.VerifyDomainDkimResponse:
        """
        Returns a set of DKIM tokens for a domain. DKIM _tokens_ are character strings
        that represent your domain's identity. Using these tokens, you will need to
        create DNS CNAME records that point to DKIM public keys hosted by Amazon SES.
        Amazon Web Services will eventually detect that you have updated your DNS
        records; this detection process may take up to 72 hours. Upon successful
        detection, Amazon SES will be able to DKIM-sign email originating from that
        domain.

        You can execute this operation no more than once per second.

        To enable or disable Easy DKIM signing for a domain, use the
        `SetIdentityDkimEnabled` operation.

        For more information about creating DNS records using DKIM tokens, go to the
        [Amazon SES Developer
        Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-
        records.html).
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            _request = shapes.VerifyDomainDkimRequest(**_params)
        response = self._boto_client.verify_domain_dkim(**_request.to_boto())

        return shapes.VerifyDomainDkimResponse.from_boto(response)

    def verify_domain_identity(
        self,
        _request: shapes.VerifyDomainIdentityRequest = None,
        *,
        domain: str,
    ) -> shapes.VerifyDomainIdentityResponse:
        """
        Adds a domain to the list of identities for your Amazon SES account in the
        current AWS Region and attempts to verify it. For more information about
        verifying domains, see [Verifying Email Addresses and
        Domains](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-
        and-domains.html) in the _Amazon SES Developer Guide._

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            _request = shapes.VerifyDomainIdentityRequest(**_params)
        response = self._boto_client.verify_domain_identity(
            **_request.to_boto()
        )

        return shapes.VerifyDomainIdentityResponse.from_boto(response)

    def verify_email_address(
        self,
        _request: shapes.VerifyEmailAddressRequest = None,
        *,
        email_address: str,
    ) -> None:
        """
        Deprecated. Use the `VerifyEmailIdentity` operation to verify a new email
        address.
        """
        if _request is None:
            _params = {}
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            _request = shapes.VerifyEmailAddressRequest(**_params)
        response = self._boto_client.verify_email_address(**_request.to_boto())

    def verify_email_identity(
        self,
        _request: shapes.VerifyEmailIdentityRequest = None,
        *,
        email_address: str,
    ) -> shapes.VerifyEmailIdentityResponse:
        """
        Adds an email address to the list of identities for your Amazon SES account in
        the current AWS region and attempts to verify it. As a result of executing this
        operation, a verification email is sent to the specified address.

        You can execute this operation no more than once per second.
        """
        if _request is None:
            _params = {}
            if email_address is not ShapeBase.NOT_SET:
                _params['email_address'] = email_address
            _request = shapes.VerifyEmailIdentityRequest(**_params)
        response = self._boto_client.verify_email_identity(**_request.to_boto())

        return shapes.VerifyEmailIdentityResponse.from_boto(response)
