import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccountSendingPausedException(ShapeBase):
    """
    Indicates that email sending is disabled for your entire Amazon SES account.

    You can enable or disable email sending for your Amazon SES account using
    UpdateAccountSendingEnabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AddHeaderAction(ShapeBase):
    """
    When included in a receipt rule, this action adds a header to the received
    email.

    For information about adding a header using a receipt rule, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-action-add-header.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "header_name",
                "HeaderName",
                TypeInfo(str),
            ),
            (
                "header_value",
                "HeaderValue",
                TypeInfo(str),
            ),
        ]

    # The name of the header to add. Must be between 1 and 50 characters,
    # inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and
    # dashes only.
    header_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Must be less than 2048 characters, and must not contain newline characters
    # ("\r" or "\n").
    header_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlreadyExistsException(ShapeBase):
    """
    Indicates that a resource could not be created because of a naming conflict.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Indicates that a resource could not be created because the resource name
    # already exists.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BehaviorOnMXFailure(str):
    UseDefaultValue = "UseDefaultValue"
    RejectMessage = "RejectMessage"


@dataclasses.dataclass
class Body(ShapeBase):
    """
    Represents the body of the message. You can specify text, HTML, or both. If you
    use both, then the message should display correctly in the widest variety of
    email clients.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "Text",
                TypeInfo(Content),
            ),
            (
                "html",
                "Html",
                TypeInfo(Content),
            ),
        ]

    # The content of the message, in text format. Use this for text-based email
    # clients, or clients on high-latency networks (such as mobile devices).
    text: "Content" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the message, in HTML format. Use this for email clients that
    # can process HTML. You can include clickable links, formatted text, and much
    # more in an HTML message.
    html: "Content" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BounceAction(ShapeBase):
    """
    When included in a receipt rule, this action rejects the received email by
    returning a bounce response to the sender and, optionally, publishes a
    notification to Amazon Simple Notification Service (Amazon SNS).

    For information about sending a bounce message in response to a received email,
    see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    action-bounce.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "smtp_reply_code",
                "SmtpReplyCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "sender",
                "Sender",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(str),
            ),
        ]

    # The SMTP reply code, as defined by [RFC
    # 5321](https://tools.ietf.org/html/rfc5321).
    smtp_reply_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Human-readable text to include in the bounce message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address of the sender of the bounced email. This is the address
    # from which the bounce message will be sent.
    sender: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the
    # bounce action is taken. An example of an Amazon SNS topic ARN is
    # `arn:aws:sns:us-west-2:123456789012:MyTopic`. For more information about
    # Amazon SNS topics, see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SMTP enhanced status code, as defined by [RFC
    # 3463](https://tools.ietf.org/html/rfc3463).
    status_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BounceType(str):
    DoesNotExist = "DoesNotExist"
    MessageTooLarge = "MessageTooLarge"
    ExceededQuota = "ExceededQuota"
    ContentRejected = "ContentRejected"
    Undefined = "Undefined"
    TemporaryFailure = "TemporaryFailure"


@dataclasses.dataclass
class BouncedRecipientInfo(ShapeBase):
    """
    Recipient-related information to include in the Delivery Status Notification
    (DSN) when an email that Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "recipient",
                "Recipient",
                TypeInfo(str),
            ),
            (
                "recipient_arn",
                "RecipientArn",
                TypeInfo(str),
            ),
            (
                "bounce_type",
                "BounceType",
                TypeInfo(typing.Union[str, BounceType]),
            ),
            (
                "recipient_dsn_fields",
                "RecipientDsnFields",
                TypeInfo(RecipientDsnFields),
            ),
        ]

    # The email address of the recipient of the bounced email.
    recipient: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to receive email for the recipient of the bounced email. For
    # more information about sending authorization, see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    recipient_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason for the bounce. You must provide either this parameter or
    # `RecipientDsnFields`.
    bounce_type: typing.Union[str, "BounceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recipient-related DSN fields, most of which would normally be filled in
    # automatically when provided with a `BounceType`. You must provide either
    # this parameter or `BounceType`.
    recipient_dsn_fields: "RecipientDsnFields" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BulkEmailDestination(ShapeBase):
    """
    An array that contains one or more Destinations, as well as the tags and
    replacement data associated with each of those Destinations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(Destination),
            ),
            (
                "replacement_tags",
                "ReplacementTags",
                TypeInfo(typing.List[MessageTag]),
            ),
            (
                "replacement_template_data",
                "ReplacementTemplateData",
                TypeInfo(str),
            ),
        ]

    # Represents the destination of the message, consisting of To:, CC:, and BCC:
    # fields.

    # Amazon SES does not support the SMTPUTF8 extension, as described in
    # [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the _local
    # part_ of a destination email address (the part of the email address that
    # precedes the @ sign) may only contain [7-bit ASCII
    # characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the
    # _domain part_ of an address (the part after the @ sign) contains non-ASCII
    # characters, they must be encoded using Punycode, as described in
    # [RFC3492](https://tools.ietf.org/html/rfc3492.html).
    destination: "Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags, in the form of name/value pairs, to apply to an email that
    # you send using `SendBulkTemplatedEmail`. Tags correspond to characteristics
    # of the email that you define, so that you can publish email sending events.
    replacement_tags: typing.List["MessageTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of replacement values to apply to the template. This parameter is a
    # JSON object, typically consisting of key-value pairs in which the keys
    # correspond to replacement tags in the email template.
    replacement_template_data: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BulkEmailDestinationStatus(ShapeBase):
    """
    An object that contains the response from the `SendBulkTemplatedEmail`
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, BulkEmailStatus]),
            ),
            (
                "error",
                "Error",
                TypeInfo(str),
            ),
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
        ]

    # The status of a message sent using the `SendBulkTemplatedEmail` operation.

    # Possible values for this parameter include:

    #   * `Success`: Amazon SES accepted the message, and will attempt to deliver it to the recipients.

    #   * `MessageRejected`: The message was rejected because it contained a virus.

    #   * `MailFromDomainNotVerified`: The sender's email address or domain was not verified.

    #   * `ConfigurationSetDoesNotExist`: The configuration set you specified does not exist.

    #   * `TemplateDoesNotExist`: The template you specified does not exist.

    #   * `AccountSuspended`: Your account has been shut down because of issues related to your email sending practices.

    #   * `AccountThrottled`: The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.

    #   * `AccountDailyQuotaExceeded`: You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.

    #   * `InvalidSendingPoolName`: The configuration set you specified refers to an IP pool that does not exist.

    #   * `AccountSendingPaused`: Email sending for the Amazon SES account was disabled using the UpdateAccountSendingEnabled operation.

    #   * `ConfigurationSetSendingPaused`: Email sending for this configuration set was disabled using the UpdateConfigurationSetSendingEnabled operation.

    #   * `InvalidParameterValue`: One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.

    #   * `TransientFailure`: Amazon SES was unable to process your request because of a temporary issue.

    #   * `Failed`: Amazon SES was unable to process your request. See the error message for additional information.
    status: typing.Union[str, "BulkEmailStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of an error that prevented a message being sent using the
    # `SendBulkTemplatedEmail` operation.
    error: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message identifier returned from the `SendBulkTemplatedEmail`
    # operation.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BulkEmailStatus(str):
    Success = "Success"
    MessageRejected = "MessageRejected"
    MailFromDomainNotVerified = "MailFromDomainNotVerified"
    ConfigurationSetDoesNotExist = "ConfigurationSetDoesNotExist"
    TemplateDoesNotExist = "TemplateDoesNotExist"
    AccountSuspended = "AccountSuspended"
    AccountThrottled = "AccountThrottled"
    AccountDailyQuotaExceeded = "AccountDailyQuotaExceeded"
    InvalidSendingPoolName = "InvalidSendingPoolName"
    AccountSendingPaused = "AccountSendingPaused"
    ConfigurationSetSendingPaused = "ConfigurationSetSendingPaused"
    InvalidParameterValue = "InvalidParameterValue"
    TransientFailure = "TransientFailure"
    Failed = "Failed"


@dataclasses.dataclass
class CannotDeleteException(ShapeBase):
    """
    Indicates that the delete operation could not be completed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Indicates that a resource could not be deleted because no resource with the
    # specified name exists.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloneReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to create a receipt rule set by cloning an existing one.
    You use receipt rule sets to receive email with Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "original_rule_set_name",
                "OriginalRuleSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the rule set to create. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Start and end with a letter or number.

    #   * Contain less than 64 characters.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the rule set to clone.
    original_rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloneReceiptRuleSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CloudWatchDestination(ShapeBase):
    """
    Contains information associated with an Amazon CloudWatch event destination to
    which email sending events are published.

    Event destinations, such as Amazon CloudWatch, are associated with configuration
    sets, which enable you to publish email sending events. For information about
    using configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimension_configurations",
                "DimensionConfigurations",
                TypeInfo(typing.List[CloudWatchDimensionConfiguration]),
            ),
        ]

    # A list of dimensions upon which to categorize your emails when you publish
    # email sending events to Amazon CloudWatch.
    dimension_configurations: typing.List["CloudWatchDimensionConfiguration"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class CloudWatchDimensionConfiguration(ShapeBase):
    """
    Contains the dimension configuration to use when you publish email sending
    events to Amazon CloudWatch.

    For information about publishing email sending events to Amazon CloudWatch, see
    the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimension_name",
                "DimensionName",
                TypeInfo(str),
            ),
            (
                "dimension_value_source",
                "DimensionValueSource",
                TypeInfo(typing.Union[str, DimensionValueSource]),
            ),
            (
                "default_dimension_value",
                "DefaultDimensionValue",
                TypeInfo(str),
            ),
        ]

    # The name of an Amazon CloudWatch dimension associated with an email sending
    # metric. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Contain less than 256 characters.
    dimension_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The place where Amazon SES finds the value of a dimension to publish to
    # Amazon CloudWatch. If you want Amazon SES to use the message tags that you
    # specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the
    # `SendEmail`/`SendRawEmail` API, choose `messageTag`. If you want Amazon SES
    # to use your own email headers, choose `emailHeader`.
    dimension_value_source: typing.Union[str, "DimensionValueSource"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The default value of the dimension that is published to Amazon CloudWatch
    # if you do not provide the value of the dimension when you send an email.
    # The default value must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Contain less than 256 characters.
    default_dimension_value: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfigurationSet(ShapeBase):
    """
    The name of the configuration set.

    Configuration sets let you create groups of rules that you can apply to the
    emails you send using Amazon SES. For more information about using configuration
    sets, see [Using Amazon SES Configuration
    Sets](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-
    sets.html) in the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration set. The name must meet the following
    # requirements:

    #   * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Contain 64 characters or fewer.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfigurationSetAlreadyExistsException(ShapeBase):
    """
    Indicates that the configuration set could not be created because of a naming
    conflict.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ConfigurationSetAttribute(str):
    eventDestinations = "eventDestinations"
    trackingOptions = "trackingOptions"
    reputationOptions = "reputationOptions"


@dataclasses.dataclass
class ConfigurationSetDoesNotExistException(ShapeBase):
    """
    Indicates that the configuration set does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfigurationSetSendingPausedException(ShapeBase):
    """
    Indicates that email sending is disabled for the configuration set.

    You can enable or disable email sending for a configuration set using
    UpdateConfigurationSetSendingEnabled.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration set for which email sending is disabled.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Content(ShapeBase):
    """
    Represents textual data, plus an optional character set specification.

    By default, the text must be 7-bit ASCII, due to the constraints of the SMTP
    protocol. If the text must contain any other characters, then you must also
    specify a character set. Examples include UTF-8, ISO-8859-1, and Shift_JIS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                TypeInfo(str),
            ),
            (
                "charset",
                "Charset",
                TypeInfo(str),
            ),
        ]

    # The textual data of the content.
    data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The character set of the content.
    charset: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConfigurationSetEventDestinationRequest(ShapeBase):
    """
    Represents a request to create a configuration set event destination. A
    configuration set event destination, which can be either Amazon CloudWatch or
    Amazon Kinesis Firehose, describes an AWS service in which Amazon SES publishes
    the email sending events associated with a configuration set. For information
    about using configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination",
                "EventDestination",
                TypeInfo(EventDestination),
            ),
        ]

    # The name of the configuration set that the event destination should be
    # associated with.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object that describes the AWS service that email sending event
    # information will be published to.
    event_destination: "EventDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateConfigurationSetEventDestinationResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CreateConfigurationSetRequest(ShapeBase):
    """
    Represents a request to create a configuration set. Configuration sets enable
    you to publish email sending events. For information about using configuration
    sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set",
                "ConfigurationSet",
                TypeInfo(ConfigurationSet),
            ),
        ]

    # A data structure that contains the name of the configuration set.
    configuration_set: "ConfigurationSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateConfigurationSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CreateConfigurationSetTrackingOptionsRequest(ShapeBase):
    """
    Represents a request to create an open and click tracking option object in a
    configuration set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "tracking_options",
                "TrackingOptions",
                TypeInfo(TrackingOptions),
            ),
        ]

    # The name of the configuration set that the tracking options should be
    # associated with.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A domain that is used to redirect email recipients to an Amazon SES-
    # operated domain. This domain captures open and click events generated by
    # Amazon SES emails.

    # For more information, see [Configuring Custom Domains to Handle Open and
    # Click Tracking](ses/latest/DeveloperGuide/configure-custom-open-click-
    # domains.html) in the _Amazon SES Developer Guide_.
    tracking_options: "TrackingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateConfigurationSetTrackingOptionsResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CreateCustomVerificationEmailTemplateRequest(ShapeBase):
    """
    Represents a request to create a custom verification email template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "from_email_address",
                "FromEmailAddress",
                TypeInfo(str),
            ),
            (
                "template_subject",
                "TemplateSubject",
                TypeInfo(str),
            ),
            (
                "template_content",
                "TemplateContent",
                TypeInfo(str),
            ),
            (
                "success_redirection_url",
                "SuccessRedirectionURL",
                TypeInfo(str),
            ),
            (
                "failure_redirection_url",
                "FailureRedirectionURL",
                TypeInfo(str),
            ),
        ]

    # The name of the custom verification email template.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that the custom verification email is sent from.
    from_email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject line of the custom verification email.
    template_subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the custom verification email. The total size of the email
    # must be less than 10 MB. The message body may contain HTML, with some
    # limitations. For more information, see [Custom Verification Email
    # Frequently Asked
    # Questions](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
    # verification-emails.html#custom-verification-emails-faq) in the _Amazon SES
    # Developer Guide_.
    template_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is successfully verified.
    success_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is not successfully verified.
    failure_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReceiptFilterRequest(ShapeBase):
    """
    Represents a request to create a new IP address filter. You use IP address
    filters when you receive email with Amazon SES. For more information, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(ReceiptFilter),
            ),
        ]

    # A data structure that describes the IP address filter to create, which
    # consists of a name, an IP address range, and whether to allow or block mail
    # from it.
    filter: "ReceiptFilter" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReceiptFilterResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CreateReceiptRuleRequest(ShapeBase):
    """
    Represents a request to create a receipt rule. You use receipt rules to receive
    email with Amazon SES. For more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "rule",
                "Rule",
                TypeInfo(ReceiptRule),
            ),
            (
                "after",
                "After",
                TypeInfo(str),
            ),
        ]

    # The name of the rule set that the receipt rule will be added to.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A data structure that contains the specified rule's name, actions,
    # recipients, domains, enabled status, scan status, and TLS policy.
    rule: "ReceiptRule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an existing rule after which the new rule will be placed. If
    # this parameter is null, the new rule will be inserted at the beginning of
    # the rule list.
    after: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReceiptRuleResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CreateReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to create an empty receipt rule set. You use receipt rule
    sets to receive email with Amazon SES. For more information, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the rule set to create. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Start and end with a letter or number.

    #   * Contain less than 64 characters.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateReceiptRuleSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class CreateTemplateRequest(ShapeBase):
    """
    Represents a request to create an email template. For more information, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
    email-api.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template",
                "Template",
                TypeInfo(Template),
            ),
        ]

    # The content of the email, composed of a subject line, an HTML part, and a
    # text-only part.
    template: "Template" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTemplateResponse(OutputShapeBase):
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


class CustomMailFromStatus(str):
    Pending = "Pending"
    Success = "Success"
    Failed = "Failed"
    TemporaryFailure = "TemporaryFailure"


@dataclasses.dataclass
class CustomVerificationEmailInvalidContentException(ShapeBase):
    """
    Indicates that custom verification email template provided content is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CustomVerificationEmailTemplate(ShapeBase):
    """
    Contains information about a custom verification email template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "from_email_address",
                "FromEmailAddress",
                TypeInfo(str),
            ),
            (
                "template_subject",
                "TemplateSubject",
                TypeInfo(str),
            ),
            (
                "success_redirection_url",
                "SuccessRedirectionURL",
                TypeInfo(str),
            ),
            (
                "failure_redirection_url",
                "FailureRedirectionURL",
                TypeInfo(str),
            ),
        ]

    # The name of the custom verification email template.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that the custom verification email is sent from.
    from_email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject line of the custom verification email.
    template_subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is successfully verified.
    success_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is not successfully verified.
    failure_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CustomVerificationEmailTemplateAlreadyExistsException(ShapeBase):
    """
    Indicates that a custom verification email template with the name you specified
    already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_verification_email_template_name",
                "CustomVerificationEmailTemplateName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the provided custom verification email template with the
    # specified template name already exists.
    custom_verification_email_template_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CustomVerificationEmailTemplateDoesNotExistException(ShapeBase):
    """
    Indicates that a custom verification email template with the name you specified
    does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_verification_email_template_name",
                "CustomVerificationEmailTemplateName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the provided custom verification email template does not
    # exist.
    custom_verification_email_template_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConfigurationSetEventDestinationRequest(ShapeBase):
    """
    Represents a request to delete a configuration set event destination.
    Configuration set event destinations are associated with configuration sets,
    which enable you to publish email sending events. For information about using
    configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination_name",
                "EventDestinationName",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration set from which to delete the event
    # destination.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the event destination to delete.
    event_destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConfigurationSetEventDestinationResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteConfigurationSetRequest(ShapeBase):
    """
    Represents a request to delete a configuration set. Configuration sets enable
    you to publish email sending events. For information about using configuration
    sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration set to delete.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConfigurationSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteConfigurationSetTrackingOptionsRequest(ShapeBase):
    """
    Represents a request to delete open and click tracking options in a
    configuration set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the configuration set from which you want to delete the
    # tracking options.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConfigurationSetTrackingOptionsResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteCustomVerificationEmailTemplateRequest(ShapeBase):
    """
    Represents a request to delete an existing custom verification email template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    # The name of the custom verification email template that you want to delete.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIdentityPolicyRequest(ShapeBase):
    """
    Represents a request to delete a sending authorization policy for an identity.
    Sending authorization is an Amazon SES feature that enables you to authorize
    other senders to use your identities. For information, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    authorization.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # The identity that is associated with the policy that you want to delete.
    # You can specify the identity by using its name or by using its Amazon
    # Resource Name (ARN). Examples: `user@example.com`, `example.com`,
    # `arn:aws:ses:us-east-1:123456789012:identity/example.com`.

    # To successfully call this API, you must own the identity.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy to be deleted.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIdentityPolicyResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteIdentityRequest(ShapeBase):
    """
    Represents a request to delete one of your Amazon SES identities (an email
    address or domain).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
        ]

    # The identity to be removed from the list of identities for the AWS Account.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIdentityResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteReceiptFilterRequest(ShapeBase):
    """
    Represents a request to delete an IP address filter. You use IP address filters
    when you receive email with Amazon SES. For more information, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter_name",
                "FilterName",
                TypeInfo(str),
            ),
        ]

    # The name of the IP address filter to delete.
    filter_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReceiptFilterResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteReceiptRuleRequest(ShapeBase):
    """
    Represents a request to delete a receipt rule. You use receipt rules to receive
    email with Amazon SES. For more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
        ]

    # The name of the receipt rule set that contains the receipt rule to delete.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the receipt rule to delete.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReceiptRuleResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to delete a receipt rule set and all of the receipt rules
    it contains. You use receipt rule sets to receive email with Amazon SES. For
    more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the receipt rule set to delete.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReceiptRuleSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class DeleteTemplateRequest(ShapeBase):
    """
    Represents a request to delete an email template. For more information, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
    email-api.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    # The name of the template to be deleted.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTemplateResponse(OutputShapeBase):
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
class DeleteVerifiedEmailAddressRequest(ShapeBase):
    """
    Represents a request to delete an email address from the list of email addresses
    you have attempted to verify under your AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
        ]

    # An email address to be removed from the list of verified addresses.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeActiveReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to return the metadata and receipt rules for the receipt
    rule set that is currently active. You use receipt rule sets to receive email
    with Amazon SES. For more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeActiveReceiptRuleSetResponse(OutputShapeBase):
    """
    Represents the metadata and receipt rules for the receipt rule set that is
    currently active.
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
                "metadata",
                "Metadata",
                TypeInfo(ReceiptRuleSetMetadata),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[ReceiptRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata for the currently active receipt rule set. The metadata
    # consists of the rule set name and a timestamp of when the rule set was
    # created.
    metadata: "ReceiptRuleSetMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The receipt rules that belong to the active rule set.
    rules: typing.List["ReceiptRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConfigurationSetRequest(ShapeBase):
    """
    Represents a request to return the details of a configuration set. Configuration
    sets enable you to publish email sending events. For information about using
    configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "configuration_set_attribute_names",
                "ConfigurationSetAttributeNames",
                TypeInfo(
                    typing.List[typing.Union[str, ConfigurationSetAttribute]]
                ),
            ),
        ]

    # The name of the configuration set to describe.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of configuration set attributes to return.
    configuration_set_attribute_names: typing.List[
        typing.Union[str, "ConfigurationSetAttribute"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class DescribeConfigurationSetResponse(OutputShapeBase):
    """
    Represents the details of a configuration set. Configuration sets enable you to
    publish email sending events. For information about using configuration sets,
    see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
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
                "configuration_set",
                "ConfigurationSet",
                TypeInfo(ConfigurationSet),
            ),
            (
                "event_destinations",
                "EventDestinations",
                TypeInfo(typing.List[EventDestination]),
            ),
            (
                "tracking_options",
                "TrackingOptions",
                TypeInfo(TrackingOptions),
            ),
            (
                "reputation_options",
                "ReputationOptions",
                TypeInfo(ReputationOptions),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration set object associated with the specified configuration
    # set.
    configuration_set: "ConfigurationSet" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of event destinations associated with the configuration set.
    event_destinations: typing.List["EventDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the custom open and click tracking domain associated with the
    # configuration set.
    tracking_options: "TrackingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that represents the reputation settings for the configuration
    # set.
    reputation_options: "ReputationOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeReceiptRuleRequest(ShapeBase):
    """
    Represents a request to return the details of a receipt rule. You use receipt
    rules to receive email with Amazon SES. For more information, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
        ]

    # The name of the receipt rule set that the receipt rule belongs to.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the receipt rule.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReceiptRuleResponse(OutputShapeBase):
    """
    Represents the details of a receipt rule.
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
                "rule",
                "Rule",
                TypeInfo(ReceiptRule),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A data structure that contains the specified receipt rule's name, actions,
    # recipients, domains, enabled status, scan status, and Transport Layer
    # Security (TLS) policy.
    rule: "ReceiptRule" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to return the details of a receipt rule set. You use
    receipt rule sets to receive email with Amazon SES. For more information, see
    the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the receipt rule set to describe.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReceiptRuleSetResponse(OutputShapeBase):
    """
    Represents the details of the specified receipt rule set.
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
                "metadata",
                "Metadata",
                TypeInfo(ReceiptRuleSetMetadata),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.List[ReceiptRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metadata for the receipt rule set, which consists of the rule set name
    # and the timestamp of when the rule set was created.
    metadata: "ReceiptRuleSetMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the receipt rules that belong to the specified receipt rule set.
    rules: typing.List["ReceiptRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Destination(ShapeBase):
    """
    Represents the destination of the message, consisting of To:, CC:, and BCC:
    fields.

    Amazon SES does not support the SMTPUTF8 extension, as described in
    [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the _local
    part_ of a destination email address (the part of the email address that
    precedes the @ sign) may only contain [7-bit ASCII
    characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the
    _domain part_ of an address (the part after the @ sign) contains non-ASCII
    characters, they must be encoded using Punycode, as described in
    [RFC3492](https://tools.ietf.org/html/rfc3492.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "to_addresses",
                "ToAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "cc_addresses",
                "CcAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "bcc_addresses",
                "BccAddresses",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The To: field(s) of the message.
    to_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CC: field(s) of the message.
    cc_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The BCC: field(s) of the message.
    bcc_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DimensionValueSource(str):
    messageTag = "messageTag"
    emailHeader = "emailHeader"
    linkTag = "linkTag"


class DsnAction(str):
    failed = "failed"
    delayed = "delayed"
    delivered = "delivered"
    relayed = "relayed"
    expanded = "expanded"


@dataclasses.dataclass
class EventDestination(ShapeBase):
    """
    Contains information about the event destination that the specified email
    sending events will be published to.

    When you create or update an event destination, you must provide one, and only
    one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis
    Firehose or Amazon Simple Notification Service (Amazon SNS).

    Event destinations are associated with configuration sets, which enable you to
    publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or
    Amazon Simple Notification Service (Amazon SNS). For information about using
    configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
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
                "matching_event_types",
                "MatchingEventTypes",
                TypeInfo(typing.List[typing.Union[str, EventType]]),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "kinesis_firehose_destination",
                "KinesisFirehoseDestination",
                TypeInfo(KinesisFirehoseDestination),
            ),
            (
                "cloud_watch_destination",
                "CloudWatchDestination",
                TypeInfo(CloudWatchDestination),
            ),
            (
                "sns_destination",
                "SNSDestination",
                TypeInfo(SNSDestination),
            ),
        ]

    # The name of the event destination. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Contain less than 64 characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of email sending events to publish to the event destination.
    matching_event_types: typing.List[typing.Union[str, "EventType"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Sets whether Amazon SES publishes events to this destination when you send
    # an email with the associated configuration set. Set to `true` to enable
    # publishing to this destination; set to `false` to prevent publishing to
    # this destination. The default value is `false`.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object that contains the delivery stream ARN and the IAM role ARN
    # associated with an Amazon Kinesis Firehose event destination.
    kinesis_firehose_destination: "KinesisFirehoseDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the names, default values, and sources of the
    # dimensions associated with an Amazon CloudWatch event destination.
    cloud_watch_destination: "CloudWatchDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object that contains the topic ARN associated with an Amazon Simple
    # Notification Service (Amazon SNS) event destination.
    sns_destination: "SNSDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventDestinationAlreadyExistsException(ShapeBase):
    """
    Indicates that the event destination could not be created because of a naming
    conflict.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination_name",
                "EventDestinationName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the event destination does not exist.
    event_destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventDestinationDoesNotExistException(ShapeBase):
    """
    Indicates that the event destination does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination_name",
                "EventDestinationName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the event destination does not exist.
    event_destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class EventType(str):
    send = "send"
    reject = "reject"
    bounce = "bounce"
    complaint = "complaint"
    delivery = "delivery"
    open = "open"
    click = "click"
    renderingFailure = "renderingFailure"


@dataclasses.dataclass
class ExtensionField(ShapeBase):
    """
    Additional X-headers to include in the Delivery Status Notification (DSN) when
    an email that Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email.html).
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
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The name of the header to add. Must be between 1 and 50 characters,
    # inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and
    # dashes only.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the header to add. Must be less than 2048 characters, and must
    # not contain newline characters ("\r" or "\n").
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FromEmailAddressNotVerifiedException(ShapeBase):
    """
    Indicates that the sender address specified for a custom verification email is
    not verified, and is therefore not eligible to send the custom verification
    email.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_email_address",
                "FromEmailAddress",
                TypeInfo(str),
            ),
        ]

    # Indicates that the from email address associated with the custom
    # verification email template is not verified.
    from_email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAccountSendingEnabledResponse(OutputShapeBase):
    """
    Represents a request to return the email sending status for your Amazon SES
    account in the current AWS Region.
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
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes whether email sending is enabled or disabled for your Amazon SES
    # account in the current AWS Region.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCustomVerificationEmailTemplateRequest(ShapeBase):
    """
    Represents a request to retrieve an existing custom verification email template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    # The name of the custom verification email template that you want to
    # retrieve.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCustomVerificationEmailTemplateResponse(OutputShapeBase):
    """
    The content of the custom verification email template.
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
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "from_email_address",
                "FromEmailAddress",
                TypeInfo(str),
            ),
            (
                "template_subject",
                "TemplateSubject",
                TypeInfo(str),
            ),
            (
                "template_content",
                "TemplateContent",
                TypeInfo(str),
            ),
            (
                "success_redirection_url",
                "SuccessRedirectionURL",
                TypeInfo(str),
            ),
            (
                "failure_redirection_url",
                "FailureRedirectionURL",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the custom verification email template.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that the custom verification email is sent from.
    from_email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject line of the custom verification email.
    template_subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the custom verification email.
    template_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is successfully verified.
    success_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is not successfully verified.
    failure_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityDkimAttributesRequest(ShapeBase):
    """
    Represents a request for the status of Amazon SES Easy DKIM signing for an
    identity. For domain identities, this request also returns the DKIM tokens that
    are required for Easy DKIM signing, and whether Amazon SES successfully verified
    that these tokens were published. For more information about Easy DKIM, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identities",
                "Identities",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of one or more verified identities - email addresses, domains, or
    # both.
    identities: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityDkimAttributesResponse(OutputShapeBase):
    """
    Represents the status of Amazon SES Easy DKIM signing for an identity. For
    domain identities, this response also contains the DKIM tokens that are required
    for Easy DKIM signing, and whether Amazon SES successfully verified that these
    tokens were published.
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
                "dkim_attributes",
                "DkimAttributes",
                TypeInfo(typing.Dict[str, IdentityDkimAttributes]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DKIM attributes for an email address or a domain.
    dkim_attributes: typing.Dict[str, "IdentityDkimAttributes"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class GetIdentityMailFromDomainAttributesRequest(ShapeBase):
    """
    Represents a request to return the Amazon SES custom MAIL FROM attributes for a
    list of identities. For information about using a custom MAIL FROM domain, see
    the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identities",
                "Identities",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of one or more identities.
    identities: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityMailFromDomainAttributesResponse(OutputShapeBase):
    """
    Represents the custom MAIL FROM attributes for a list of identities.
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
                "mail_from_domain_attributes",
                "MailFromDomainAttributes",
                TypeInfo(typing.Dict[str, IdentityMailFromDomainAttributes]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of identities to custom MAIL FROM attributes.
    mail_from_domain_attributes: typing.Dict[
        str, "IdentityMailFromDomainAttributes"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class GetIdentityNotificationAttributesRequest(ShapeBase):
    """
    Represents a request to return the notification attributes for a list of
    identities you verified with Amazon SES. For information about Amazon SES
    notifications, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identities",
                "Identities",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of one or more identities. You can specify an identity by using its
    # name or by using its Amazon Resource Name (ARN). Examples:
    # `user@example.com`, `example.com`, `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`.
    identities: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityNotificationAttributesResponse(OutputShapeBase):
    """
    Represents the notification attributes for a list of identities.
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
                "notification_attributes",
                "NotificationAttributes",
                TypeInfo(typing.Dict[str, IdentityNotificationAttributes]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of Identity to IdentityNotificationAttributes.
    notification_attributes: typing.Dict[str, "IdentityNotificationAttributes"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class GetIdentityPoliciesRequest(ShapeBase):
    """
    Represents a request to return the requested sending authorization policies for
    an identity. Sending authorization is an Amazon SES feature that enables you to
    authorize other senders to use your identities. For information, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    authorization.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identity for which the policies will be retrieved. You can specify an
    # identity by using its name or by using its Amazon Resource Name (ARN).
    # Examples: `user@example.com`, `example.com`, `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`.

    # To successfully call this API, you must own the identity.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the names of policies to be retrieved. You can retrieve a maximum
    # of 20 policies at a time. If you do not know the names of the policies that
    # are attached to the identity, you can use `ListIdentityPolicies`.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityPoliciesResponse(OutputShapeBase):
    """
    Represents the requested sending authorization policies.
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
                "policies",
                "Policies",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of policy names to policies.
    policies: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityVerificationAttributesRequest(ShapeBase):
    """
    Represents a request to return the Amazon SES verification status of a list of
    identities. For domain identities, this request also returns the verification
    token. For information about verifying identities with Amazon SES, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-
    and-domains.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identities",
                "Identities",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of identities.
    identities: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIdentityVerificationAttributesResponse(OutputShapeBase):
    """
    The Amazon SES verification status of a list of identities. For domain
    identities, this response also contains the verification token.
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
                "verification_attributes",
                "VerificationAttributes",
                TypeInfo(typing.Dict[str, IdentityVerificationAttributes]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of Identities to IdentityVerificationAttributes objects.
    verification_attributes: typing.Dict[str, "IdentityVerificationAttributes"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class GetSendQuotaResponse(OutputShapeBase):
    """
    Represents your Amazon SES daily sending quota, maximum send rate, and the
    number of emails you have sent in the last 24 hours.
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
                "max24_hour_send",
                "Max24HourSend",
                TypeInfo(float),
            ),
            (
                "max_send_rate",
                "MaxSendRate",
                TypeInfo(float),
            ),
            (
                "sent_last24_hours",
                "SentLast24Hours",
                TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of emails the user is allowed to send in a 24-hour
    # interval. A value of -1 signifies an unlimited quota.
    max24_hour_send: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of emails that Amazon SES can accept from the user's
    # account per second.

    # The rate at which Amazon SES accepts the user's messages might be less than
    # the maximum send rate.
    max_send_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of emails sent during the previous 24 hours.
    sent_last24_hours: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSendStatisticsResponse(OutputShapeBase):
    """
    Represents a list of data points. This list contains aggregated data from the
    previous two weeks of your sending activity with Amazon SES.
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
                "send_data_points",
                "SendDataPoints",
                TypeInfo(typing.List[SendDataPoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of data points, each of which represents 15 minutes of activity.
    send_data_points: typing.List["SendDataPoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    # The name of the template you want to retrieve.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTemplateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "template",
                "Template",
                TypeInfo(Template),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content of the email, composed of a subject line, an HTML part, and a
    # text-only part.
    template: "Template" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IdentityDkimAttributes(ShapeBase):
    """
    Represents the DKIM attributes of a verified email address or a domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dkim_enabled",
                "DkimEnabled",
                TypeInfo(bool),
            ),
            (
                "dkim_verification_status",
                "DkimVerificationStatus",
                TypeInfo(typing.Union[str, VerificationStatus]),
            ),
            (
                "dkim_tokens",
                "DkimTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    # True if DKIM signing is enabled for email sent from the identity; false
    # otherwise. The default value is true.
    dkim_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes whether Amazon SES has successfully verified the DKIM DNS records
    # (tokens) published in the domain name's DNS. (This only applies to domain
    # identities, not email address identities.)
    dkim_verification_status: typing.Union[str, "VerificationStatus"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # A set of character strings that represent the domain's identity. Using
    # these tokens, you will need to create DNS CNAME records that point to DKIM
    # public keys hosted by Amazon SES. Amazon Web Services will eventually
    # detect that you have updated your DNS records; this detection process may
    # take up to 72 hours. Upon successful detection, Amazon SES will be able to
    # DKIM-sign email originating from that domain. (This only applies to domain
    # identities, not email address identities.)

    # For more information about creating DNS records using DKIM tokens, go to
    # the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-
    # records.html).
    dkim_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdentityMailFromDomainAttributes(ShapeBase):
    """
    Represents the custom MAIL FROM domain attributes of a verified identity (email
    address or domain).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "mail_from_domain",
                "MailFromDomain",
                TypeInfo(str),
            ),
            (
                "mail_from_domain_status",
                "MailFromDomainStatus",
                TypeInfo(typing.Union[str, CustomMailFromStatus]),
            ),
            (
                "behavior_on_mx_failure",
                "BehaviorOnMXFailure",
                TypeInfo(typing.Union[str, BehaviorOnMXFailure]),
            ),
        ]

    # The custom MAIL FROM domain that the identity is configured to use.
    mail_from_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state that indicates whether Amazon SES has successfully read the MX
    # record required for custom MAIL FROM domain setup. If the state is
    # `Success`, Amazon SES uses the specified custom MAIL FROM domain when the
    # verified identity sends an email. All other states indicate that Amazon SES
    # takes the action described by `BehaviorOnMXFailure`.
    mail_from_domain_status: typing.Union[str, "CustomMailFromStatus"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The action that Amazon SES takes if it cannot successfully read the
    # required MX record when you send an email. A value of `UseDefaultValue`
    # indicates that if Amazon SES cannot read the required MX record, it uses
    # amazonses.com (or a subdomain of that) as the MAIL FROM domain. A value of
    # `RejectMessage` indicates that if Amazon SES cannot read the required MX
    # record, Amazon SES returns a `MailFromDomainNotVerified` error and does not
    # send the email.

    # The custom MAIL FROM setup states that result in this behavior are
    # `Pending`, `Failed`, and `TemporaryFailure`.
    behavior_on_mx_failure: typing.Union[str, "BehaviorOnMXFailure"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class IdentityNotificationAttributes(ShapeBase):
    """
    Represents the notification attributes of an identity, including whether an
    identity has Amazon Simple Notification Service (Amazon SNS) topics set for
    bounce, complaint, and/or delivery notifications, and whether feedback
    forwarding is enabled for bounce and complaint notifications.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bounce_topic",
                "BounceTopic",
                TypeInfo(str),
            ),
            (
                "complaint_topic",
                "ComplaintTopic",
                TypeInfo(str),
            ),
            (
                "delivery_topic",
                "DeliveryTopic",
                TypeInfo(str),
            ),
            (
                "forwarding_enabled",
                "ForwardingEnabled",
                TypeInfo(bool),
            ),
            (
                "headers_in_bounce_notifications_enabled",
                "HeadersInBounceNotificationsEnabled",
                TypeInfo(bool),
            ),
            (
                "headers_in_complaint_notifications_enabled",
                "HeadersInComplaintNotificationsEnabled",
                TypeInfo(bool),
            ),
            (
                "headers_in_delivery_notifications_enabled",
                "HeadersInDeliveryNotificationsEnabled",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES
    # will publish bounce notifications.
    bounce_topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES
    # will publish complaint notifications.
    complaint_topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES
    # will publish delivery notifications.
    delivery_topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes whether Amazon SES will forward bounce and complaint
    # notifications as email. `true` indicates that Amazon SES will forward
    # bounce and complaint notifications as email, while `false` indicates that
    # bounce and complaint notifications will be published only to the specified
    # bounce and complaint Amazon SNS topics.
    forwarding_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes whether Amazon SES includes the original email headers in Amazon
    # SNS notifications of type `Bounce`. A value of `true` specifies that Amazon
    # SES will include headers in bounce notifications, and a value of `false`
    # specifies that Amazon SES will not include headers in bounce notifications.
    headers_in_bounce_notifications_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes whether Amazon SES includes the original email headers in Amazon
    # SNS notifications of type `Complaint`. A value of `true` specifies that
    # Amazon SES will include headers in complaint notifications, and a value of
    # `false` specifies that Amazon SES will not include headers in complaint
    # notifications.
    headers_in_complaint_notifications_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes whether Amazon SES includes the original email headers in Amazon
    # SNS notifications of type `Delivery`. A value of `true` specifies that
    # Amazon SES will include headers in delivery notifications, and a value of
    # `false` specifies that Amazon SES will not include headers in delivery
    # notifications.
    headers_in_delivery_notifications_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class IdentityType(str):
    EmailAddress = "EmailAddress"
    Domain = "Domain"


@dataclasses.dataclass
class IdentityVerificationAttributes(ShapeBase):
    """
    Represents the verification attributes of a single identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "verification_status",
                "VerificationStatus",
                TypeInfo(typing.Union[str, VerificationStatus]),
            ),
            (
                "verification_token",
                "VerificationToken",
                TypeInfo(str),
            ),
        ]

    # The verification status of the identity: "Pending", "Success", "Failed", or
    # "TemporaryFailure".
    verification_status: typing.Union[str, "VerificationStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The verification token for a domain identity. Null for email address
    # identities.
    verification_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidCloudWatchDestinationException(ShapeBase):
    """
    Indicates that the Amazon CloudWatch destination is invalid. See the error
    message for details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination_name",
                "EventDestinationName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the event destination does not exist.
    event_destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidConfigurationSetException(ShapeBase):
    """
    Indicates that the configuration set is invalid. See the error message for
    details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidFirehoseDestinationException(ShapeBase):
    """
    Indicates that the Amazon Kinesis Firehose destination is invalid. See the error
    message for details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination_name",
                "EventDestinationName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the event destination does not exist.
    event_destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLambdaFunctionException(ShapeBase):
    """
    Indicates that the provided AWS Lambda function is invalid, or that Amazon SES
    could not execute the provided function, possibly due to permissions issues. For
    information about giving permissions, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    permissions.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_arn",
                "FunctionArn",
                TypeInfo(str),
            ),
        ]

    # Indicates that the ARN of the function was not found.
    function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPolicyException(ShapeBase):
    """
    Indicates that the provided policy is invalid. Check the error stack for more
    information about what caused the error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidRenderingParameterException(ShapeBase):
    """
    Indicates that one or more of the replacement values you provided is invalid.
    This error may occur when the TemplateData object contains invalid JSON.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidS3ConfigurationException(ShapeBase):
    """
    Indicates that the provided Amazon S3 bucket or AWS KMS encryption key is
    invalid, or that Amazon SES could not publish to the bucket, possibly due to
    permissions issues. For information about giving permissions, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    permissions.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
        ]

    # Indicated that the S3 Bucket was not found.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSNSDestinationException(ShapeBase):
    """
    Indicates that the Amazon Simple Notification Service (Amazon SNS) destination
    is invalid. See the error message for details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination_name",
                "EventDestinationName",
                TypeInfo(str),
            ),
        ]

    # Indicates that the configuration set does not exist.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates that the event destination does not exist.
    event_destination_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidSnsTopicException(ShapeBase):
    """
    Indicates that the provided Amazon SNS topic is invalid, or that Amazon SES
    could not publish to the topic, possibly due to permissions issues. For
    information about giving permissions, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    permissions.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic",
                "Topic",
                TypeInfo(str),
            ),
        ]

    # Indicates that the topic does not exist.
    topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTemplateException(ShapeBase):
    """
    Indicates that the template that you specified could not be rendered. This issue
    may occur when a template refers to a partial that does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTrackingOptionsException(ShapeBase):
    """
    Indicates that the custom domain to be used for open and click tracking
    redirects is invalid. This error appears most often in the following situations:

      * When the tracking domain you specified is not verified in Amazon SES.

      * When the tracking domain you specified is not a valid domain or subdomain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class InvocationType(str):
    Event = "Event"
    RequestResponse = "RequestResponse"


@dataclasses.dataclass
class KinesisFirehoseDestination(ShapeBase):
    """
    Contains the delivery stream ARN and the IAM role ARN associated with an Amazon
    Kinesis Firehose event destination.

    Event destinations, such as Amazon Kinesis Firehose, are associated with
    configuration sets, which enable you to publish email sending events. For
    information about using configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iam_role_arn",
                "IAMRoleARN",
                TypeInfo(str),
            ),
            (
                "delivery_stream_arn",
                "DeliveryStreamARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the IAM role under which Amazon SES publishes email sending
    # events to the Amazon Kinesis Firehose stream.
    iam_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon Kinesis Firehose stream that email sending events
    # should be published to.
    delivery_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaAction(ShapeBase):
    """
    When included in a receipt rule, this action calls an AWS Lambda function and,
    optionally, publishes a notification to Amazon Simple Notification Service
    (Amazon SNS).

    To enable Amazon SES to call your AWS Lambda function or to publish to an Amazon
    SNS topic of another account, Amazon SES must have permission to access those
    resources. For information about giving permissions, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-permissions.html).

    For information about using AWS Lambda actions in receipt rules, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    action-lambda.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_arn",
                "FunctionArn",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "invocation_type",
                "InvocationType",
                TypeInfo(typing.Union[str, InvocationType]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an
    # AWS Lambda function ARN is `arn:aws:lambda:us-west-2:account-
    # id:function:MyFunction`. For more information about AWS Lambda, see the
    # [AWS Lambda Developer
    # Guide](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html).
    function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the
    # Lambda action is taken. An example of an Amazon SNS topic ARN is
    # `arn:aws:sns:us-west-2:123456789012:MyTopic`. For more information about
    # Amazon SNS topics, see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The invocation type of the AWS Lambda function. An invocation type of
    # `RequestResponse` means that the execution of the function will immediately
    # result in a response, and a value of `Event` means that the function will
    # be invoked asynchronously. The default value is `Event`. For information
    # about AWS Lambda invocation types, see the [AWS Lambda Developer
    # Guide](http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html).

    # There is a 30-second timeout on `RequestResponse` invocations. You should
    # use `Event` invocation in most cases. Use `RequestResponse` only when you
    # want to make a mail flow decision, such as whether to stop the receipt rule
    # or the receipt rule set.
    invocation_type: typing.Union[str, "InvocationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    Indicates that a resource could not be created because of service limits. For a
    list of Amazon SES limits, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListConfigurationSetsRequest(ShapeBase):
    """
    Represents a request to list the configuration sets associated with your AWS
    account. Configuration sets enable you to publish email sending events. For
    information about using configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # A token returned from a previous call to `ListConfigurationSets` to
    # indicate the position of the configuration set in the configuration set
    # list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of configuration sets to return.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListConfigurationSetsResponse(OutputShapeBase):
    """
    A list of configuration sets associated with your AWS account. Configuration
    sets enable you to publish email sending events. For information about using
    configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
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
                "configuration_sets",
                "ConfigurationSets",
                TypeInfo(typing.List[ConfigurationSet]),
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

    # A list of configuration sets.
    configuration_sets: typing.List["ConfigurationSet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token indicating that there are additional configuration sets available
    # to be listed. Pass this token to successive calls of
    # `ListConfigurationSets`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCustomVerificationEmailTemplatesRequest(ShapeBase):
    """
    Represents a request to list the existing custom verification email templates
    for your account.

    For more information about custom verification email templates, see [Using
    Custom Verification Email Templates](ses/latest/DeveloperGuide/custom-
    verification-emails.html) in the _Amazon SES Developer Guide_.
    """

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

    # An array the contains the name and creation time stamp for each template in
    # your Amazon SES account.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of custom verification email templates to return. This
    # value must be at least 1 and less than or equal to 50. If you do not
    # specify a value, or if you specify a value less than 1 or greater than 50,
    # the operation will return up to 50 results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCustomVerificationEmailTemplatesResponse(OutputShapeBase):
    """
    A paginated list of custom verification email templates.
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
                "custom_verification_email_templates",
                "CustomVerificationEmailTemplates",
                TypeInfo(typing.List[CustomVerificationEmailTemplate]),
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

    # A list of the custom verification email templates that exist in your
    # account.
    custom_verification_email_templates: typing.List[
        "CustomVerificationEmailTemplate"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # A token indicating that there are additional custom verification email
    # templates available to be listed. Pass this token to a subsequent call to
    # `ListTemplates` to retrieve the next 50 custom verification email
    # templates.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator[
        "ListCustomVerificationEmailTemplatesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListIdentitiesRequest(ShapeBase):
    """
    Represents a request to return a list of all identities (email addresses and
    domains) that you have attempted to verify under your AWS account, regardless of
    verification status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity_type",
                "IdentityType",
                TypeInfo(typing.Union[str, IdentityType]),
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

    # The type of the identities to list. Possible values are "EmailAddress" and
    # "Domain". If this parameter is omitted, then all identities will be listed.
    identity_type: typing.Union[str, "IdentityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to use for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of identities per page. Possible values are 1-1000
    # inclusive.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentitiesResponse(OutputShapeBase):
    """
    A list of all identities that you have attempted to verify under your AWS
    account, regardless of verification status.
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
                "identities",
                "Identities",
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

    # A list of identities.
    identities: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token used for pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListIdentitiesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListIdentityPoliciesRequest(ShapeBase):
    """
    Represents a request to return a list of sending authorization policies that are
    attached to an identity. Sending authorization is an Amazon SES feature that
    enables you to authorize other senders to use your identities. For information,
    see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    authorization.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
        ]

    # The identity that is associated with the policy for which the policies will
    # be listed. You can specify an identity by using its name or by using its
    # Amazon Resource Name (ARN). Examples: `user@example.com`, `example.com`,
    # `arn:aws:ses:us-east-1:123456789012:identity/example.com`.

    # To successfully call this API, you must own the identity.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIdentityPoliciesResponse(OutputShapeBase):
    """
    A list of names of sending authorization policies that apply to an identity.
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
                "policy_names",
                "PolicyNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of names of policies that apply to the specified identity.
    policy_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListReceiptFiltersRequest(ShapeBase):
    """
    Represents a request to list the IP address filters that exist under your AWS
    account. You use IP address filters when you receive email with Amazon SES. For
    more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListReceiptFiltersResponse(OutputShapeBase):
    """
    A list of IP address filters that exist under your AWS account.
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
                "filters",
                "Filters",
                TypeInfo(typing.List[ReceiptFilter]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IP address filter data structures, which each consist of a name,
    # an IP address range, and whether to allow or block mail from it.
    filters: typing.List["ReceiptFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListReceiptRuleSetsRequest(ShapeBase):
    """
    Represents a request to list the receipt rule sets that exist under your AWS
    account. You use receipt rule sets to receive email with Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A token returned from a previous call to `ListReceiptRuleSets` to indicate
    # the position in the receipt rule set list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListReceiptRuleSetsResponse(OutputShapeBase):
    """
    A list of receipt rule sets that exist under your AWS account.
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
                "rule_sets",
                "RuleSets",
                TypeInfo(typing.List[ReceiptRuleSetMetadata]),
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

    # The metadata for the currently active receipt rule set. The metadata
    # consists of the rule set name and the timestamp of when the rule set was
    # created.
    rule_sets: typing.List["ReceiptRuleSetMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token indicating that there are additional receipt rule sets available to
    # be listed. Pass this token to successive calls of `ListReceiptRuleSets` to
    # retrieve up to 100 receipt rule sets at a time.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTemplatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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

    # A token returned from a previous call to `ListTemplates` to indicate the
    # position in the list of email templates.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of templates to return. This value must be at least 1
    # and less than or equal to 10. If you do not specify a value, or if you
    # specify a value less than 1 or greater than 10, the operation will return
    # up to 10 results.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTemplatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "templates_metadata",
                "TemplatesMetadata",
                TypeInfo(typing.List[TemplateMetadata]),
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

    # An array the contains the name and creation time stamp for each template in
    # your Amazon SES account.
    templates_metadata: typing.List["TemplateMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token indicating that there are additional email templates available to
    # be listed. Pass this token to a subsequent call to `ListTemplates` to
    # retrieve the next 50 email templates.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVerifiedEmailAddressesResponse(OutputShapeBase):
    """
    A list of email addresses that you have verified with Amazon SES under your AWS
    account.
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
                "verified_email_addresses",
                "VerifiedEmailAddresses",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of email addresses that have been verified.
    verified_email_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MailFromDomainNotVerifiedException(ShapeBase):
    """
    Indicates that the message could not be sent because Amazon SES could not read
    the MX record required to use the specified MAIL FROM domain. For information
    about editing the custom MAIL FROM domain settings for an identity, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-
    edit.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Message(ShapeBase):
    """
    Represents the message to be sent, composed of a subject and a body.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subject",
                "Subject",
                TypeInfo(Content),
            ),
            (
                "body",
                "Body",
                TypeInfo(Body),
            ),
        ]

    # The subject of the message: A short summary of the content, which will
    # appear in the recipient's inbox.
    subject: "Content" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message body.
    body: "Body" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MessageDsn(ShapeBase):
    """
    Message-related information to include in the Delivery Status Notification (DSN)
    when an email that Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reporting_mta",
                "ReportingMta",
                TypeInfo(str),
            ),
            (
                "arrival_date",
                "ArrivalDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "extension_fields",
                "ExtensionFields",
                TypeInfo(typing.List[ExtensionField]),
            ),
        ]

    # The reporting MTA that attempted to deliver the message, formatted as
    # specified in [RFC 3464](https://tools.ietf.org/html/rfc3464) (`mta-name-
    # type; mta-name`). The default value is `dns; inbound-
    # smtp.[region].amazonaws.com`.
    reporting_mta: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the message was received by the reporting mail transfer agent (MTA),
    # in [RFC 822](https://www.ietf.org/rfc/rfc0822.txt) date-time format.
    arrival_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional X-headers to include in the DSN.
    extension_fields: typing.List["ExtensionField"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MessageRejected(ShapeBase):
    """
    Indicates that the action failed, and the message could not be sent. Check the
    error stack for more information about what caused the error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MessageTag(ShapeBase):
    """
    Contains the name and value of a tag that you can provide to `SendEmail` or
    `SendRawEmail` to apply to an email.

    Message tags, which you use with configuration sets, enable you to publish email
    sending events. For information about using configuration sets, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
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
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The name of the tag. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Contain less than 256 characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag. The value must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Contain less than 256 characters.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MissingRenderingAttributeException(ShapeBase):
    """
    Indicates that one or more of the replacement values for the specified template
    was not specified. Ensure that the TemplateData object contains references to
    all of the replacement tags in the specified template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class NotificationType(str):
    Bounce = "Bounce"
    Complaint = "Complaint"
    Delivery = "Delivery"


@dataclasses.dataclass
class ProductionAccessNotGrantedException(ShapeBase):
    """
    Indicates that the account has not been granted production access.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PutIdentityPolicyRequest(ShapeBase):
    """
    Represents a request to add or update a sending authorization policy for an
    identity. Sending authorization is an Amazon SES feature that enables you to
    authorize other senders to use your identities. For information, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    authorization.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "policy",
                "Policy",
                TypeInfo(str),
            ),
        ]

    # The identity that the policy will apply to. You can specify an identity by
    # using its name or by using its Amazon Resource Name (ARN). Examples:
    # `user@example.com`, `example.com`, `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`.

    # To successfully call this API, you must own the identity.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the policy.

    # The policy name cannot exceed 64 characters and can only include
    # alphanumeric characters, dashes, and underscores.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text of the policy in JSON format. The policy cannot exceed 4 KB.

    # For information about the syntax of sending authorization policies, see the
    # [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization-policies.html).
    policy: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutIdentityPolicyResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class RawMessage(ShapeBase):
    """
    Represents the raw data of the message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data",
                "Data",
                TypeInfo(typing.Any),
            ),
        ]

    # The raw data of the message. This data needs to base64-encoded if you are
    # accessing Amazon SES directly through the HTTPS interface. If you are
    # accessing Amazon SES using an AWS SDK, the SDK takes care of the base
    # 64-encoding for you. In all cases, the client must ensure that the message
    # format complies with Internet email standards regarding email header
    # fields, MIME types, and MIME encoding.

    # The To:, CC:, and BCC: headers in the raw message can contain a group list.

    # If you are using `SendRawEmail` with sending authorization, you can include
    # X-headers in the raw message to specify the "Source," "From," and "Return-
    # Path" addresses. For more information, see the documentation for
    # `SendRawEmail`.

    # Do not include these X-headers in the DKIM signature, because they are
    # removed by Amazon SES before sending the email.

    # For more information, go to the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-
    # raw.html).
    data: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


class RawMessageData(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ReceiptAction(ShapeBase):
    """
    An action that Amazon SES can take when it receives an email on behalf of one or
    more email addresses or domains that you own. An instance of this data type can
    represent only one action.

    For information about setting up receipt rules, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    receipt-rules.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_action",
                "S3Action",
                TypeInfo(S3Action),
            ),
            (
                "bounce_action",
                "BounceAction",
                TypeInfo(BounceAction),
            ),
            (
                "workmail_action",
                "WorkmailAction",
                TypeInfo(WorkmailAction),
            ),
            (
                "lambda_action",
                "LambdaAction",
                TypeInfo(LambdaAction),
            ),
            (
                "stop_action",
                "StopAction",
                TypeInfo(StopAction),
            ),
            (
                "add_header_action",
                "AddHeaderAction",
                TypeInfo(AddHeaderAction),
            ),
            (
                "sns_action",
                "SNSAction",
                TypeInfo(SNSAction),
            ),
        ]

    # Saves the received message to an Amazon Simple Storage Service (Amazon S3)
    # bucket and, optionally, publishes a notification to Amazon SNS.
    s3_action: "S3Action" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Rejects the received email by returning a bounce response to the sender
    # and, optionally, publishes a notification to Amazon Simple Notification
    # Service (Amazon SNS).
    bounce_action: "BounceAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Calls Amazon WorkMail and, optionally, publishes a notification to Amazon
    # Amazon SNS.
    workmail_action: "WorkmailAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Calls an AWS Lambda function, and optionally, publishes a notification to
    # Amazon SNS.
    lambda_action: "LambdaAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Terminates the evaluation of the receipt rule set and optionally publishes
    # a notification to Amazon SNS.
    stop_action: "StopAction" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Adds a header to the received email.
    add_header_action: "AddHeaderAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Publishes the email content within a notification to Amazon SNS.
    sns_action: "SNSAction" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReceiptFilter(ShapeBase):
    """
    A receipt IP address filter enables you to specify whether to accept or reject
    mail originating from an IP address or range of IP addresses.

    For information about setting up IP address filters, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-ip-filters.html).
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
                "ip_filter",
                "IpFilter",
                TypeInfo(ReceiptIpFilter),
            ),
        ]

    # The name of the IP address filter. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Start and end with a letter or number.

    #   * Contain less than 64 characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A structure that provides the IP addresses to block or allow, and whether
    # to block or allow incoming mail from them.
    ip_filter: "ReceiptIpFilter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReceiptFilterPolicy(str):
    Block = "Block"
    Allow = "Allow"


@dataclasses.dataclass
class ReceiptIpFilter(ShapeBase):
    """
    A receipt IP address filter enables you to specify whether to accept or reject
    mail originating from an IP address or range of IP addresses.

    For information about setting up IP address filters, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-ip-filters.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy",
                "Policy",
                TypeInfo(typing.Union[str, ReceiptFilterPolicy]),
            ),
            (
                "cidr",
                "Cidr",
                TypeInfo(str),
            ),
        ]

    # Indicates whether to block or allow incoming mail from the specified IP
    # addresses.
    policy: typing.Union[str, "ReceiptFilterPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A single IP address or a range of IP addresses that you want to block or
    # allow, specified in Classless Inter-Domain Routing (CIDR) notation. An
    # example of a single email address is 10.0.0.1. An example of a range of IP
    # addresses is 10.0.0.1/24. For more information about CIDR notation, see
    # [RFC 2317](https://tools.ietf.org/html/rfc2317).
    cidr: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReceiptRule(ShapeBase):
    """
    Receipt rules enable you to specify which actions Amazon SES should take when it
    receives mail on behalf of one or more email addresses or domains that you own.

    Each receipt rule defines a set of email addresses or domains that it applies
    to. If the email addresses or domains match at least one recipient address of
    the message, Amazon SES executes all of the receipt rule's actions on the
    message.

    For information about setting up receipt rules, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    receipt-rules.html).
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
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "tls_policy",
                "TlsPolicy",
                TypeInfo(typing.Union[str, TlsPolicy]),
            ),
            (
                "recipients",
                "Recipients",
                TypeInfo(typing.List[str]),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[ReceiptAction]),
            ),
            (
                "scan_enabled",
                "ScanEnabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the receipt rule. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Start and end with a letter or number.

    #   * Contain less than 64 characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, the receipt rule is active. The default value is `false`.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether Amazon SES should require that incoming email is
    # delivered over a connection encrypted with Transport Layer Security (TLS).
    # If this parameter is set to `Require`, Amazon SES will bounce emails that
    # are not received over TLS. The default is `Optional`.
    tls_policy: typing.Union[str, "TlsPolicy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The recipient domains and email addresses that the receipt rule applies to.
    # If this field is not specified, this rule will match all recipients under
    # all verified domains.
    recipients: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An ordered list of actions to perform on messages that match at least one
    # of the recipient email addresses or domains specified in the receipt rule.
    actions: typing.List["ReceiptAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `true`, then messages that this receipt rule applies to are scanned for
    # spam and viruses. The default value is `false`.
    scan_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReceiptRuleSetMetadata(ShapeBase):
    """
    Information about a receipt rule set.

    A receipt rule set is a collection of rules that specify what Amazon SES should
    do with mail it receives on behalf of your account's verified domains.

    For information about setting up receipt rule sets, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-receipt-rule-set.html).
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
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the receipt rule set. The name must:

    #   * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

    #   * Start and end with a letter or number.

    #   * Contain less than 64 characters.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the receipt rule set was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RecipientDsnFields(ShapeBase):
    """
    Recipient-related information to include in the Delivery Status Notification
    (DSN) when an email that Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, DsnAction]),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "final_recipient",
                "FinalRecipient",
                TypeInfo(str),
            ),
            (
                "remote_mta",
                "RemoteMta",
                TypeInfo(str),
            ),
            (
                "diagnostic_code",
                "DiagnosticCode",
                TypeInfo(str),
            ),
            (
                "last_attempt_date",
                "LastAttemptDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "extension_fields",
                "ExtensionFields",
                TypeInfo(typing.List[ExtensionField]),
            ),
        ]

    # The action performed by the reporting mail transfer agent (MTA) as a result
    # of its attempt to deliver the message to the recipient address. This is
    # required by [RFC 3464](https://tools.ietf.org/html/rfc3464).
    action: typing.Union[str, "DsnAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status code that indicates what went wrong. This is required by [RFC
    # 3464](https://tools.ietf.org/html/rfc3464).
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that the message was ultimately delivered to. This
    # corresponds to the `Final-Recipient` in the DSN. If not specified,
    # `FinalRecipient` will be set to the `Recipient` specified in the
    # `BouncedRecipientInfo` structure. Either `FinalRecipient` or the recipient
    # in `BouncedRecipientInfo` must be a recipient of the original bounced
    # message.

    # Do not prepend the `FinalRecipient` email address with `rfc 822;`, as
    # described in [RFC 3798](https://tools.ietf.org/html/rfc3798).
    final_recipient: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MTA to which the remote MTA attempted to deliver the message, formatted
    # as specified in [RFC 3464](https://tools.ietf.org/html/rfc3464) (`mta-name-
    # type; mta-name`). This parameter typically applies only to propagating
    # synchronous bounces.
    remote_mta: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An extended explanation of what went wrong; this is usually an SMTP
    # response. See [RFC 3463](https://tools.ietf.org/html/rfc3463) for the
    # correct formatting of this parameter.
    diagnostic_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time the final delivery attempt was made, in [RFC
    # 822](https://www.ietf.org/rfc/rfc0822.txt) date-time format.
    last_attempt_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional X-headers to include in the DSN.
    extension_fields: typing.List["ExtensionField"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReorderReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to reorder the receipt rules within a receipt rule set. You
    use receipt rule sets to receive email with Amazon SES. For more information,
    see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "rule_names",
                "RuleNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the receipt rule set to reorder.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the specified receipt rule set's receipt rules in the order that
    # you want to put them.
    rule_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReorderReceiptRuleSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class ReputationOptions(ShapeBase):
    """
    Contains information about the reputation settings for a configuration set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sending_enabled",
                "SendingEnabled",
                TypeInfo(bool),
            ),
            (
                "reputation_metrics_enabled",
                "ReputationMetricsEnabled",
                TypeInfo(bool),
            ),
            (
                "last_fresh_start",
                "LastFreshStart",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Describes whether email sending is enabled or disabled for the
    # configuration set. If the value is `true`, then Amazon SES will send emails
    # that use the configuration set. If the value is `false`, Amazon SES will
    # not send emails that use the configuration set. The default value is
    # `true`. You can change this setting using
    # UpdateConfigurationSetSendingEnabled.
    sending_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes whether or not Amazon SES publishes reputation metrics for the
    # configuration set, such as bounce and complaint rates, to Amazon
    # CloudWatch.

    # If the value is `true`, reputation metrics are published. If the value is
    # `false`, reputation metrics are not published. The default value is
    # `false`.
    reputation_metrics_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time at which the reputation metrics for the configuration set
    # were last reset. Resetting these metrics is known as a _fresh start_.

    # When you disable email sending for a configuration set using
    # UpdateConfigurationSetSendingEnabled and later re-enable it, the reputation
    # metrics for the configuration set (but not for the entire Amazon SES
    # account) are reset.

    # If email sending for the configuration set has never been disabled and
    # later re-enabled, the value of this attribute is `null`.
    last_fresh_start: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RuleDoesNotExistException(ShapeBase):
    """
    Indicates that the provided receipt rule does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Indicates that the named receipt rule does not exist.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RuleSetDoesNotExistException(ShapeBase):
    """
    Indicates that the provided receipt rule set does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Indicates that the named receipt rule set does not exist.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3Action(ShapeBase):
    """
    When included in a receipt rule, this action saves the received message to an
    Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a
    notification to Amazon Simple Notification Service (Amazon SNS).

    To enable Amazon SES to write emails to your Amazon S3 bucket, use an AWS KMS
    key to encrypt your emails, or publish to an Amazon SNS topic of another
    account, Amazon SES must have permission to access those resources. For
    information about giving permissions, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    permissions.html).

    When you save your emails to an Amazon S3 bucket, the maximum email size
    (including headers) is 30 MB. Emails larger than that will bounce.

    For information about specifying Amazon S3 actions in receipt rules, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    action-s3.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket_name",
                "BucketName",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "object_key_prefix",
                "ObjectKeyPrefix",
                TypeInfo(str),
            ),
            (
                "kms_key_arn",
                "KmsKeyArn",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon S3 bucket that incoming email will be saved to.
    bucket_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon SNS topic to notify when the message is saved to the
    # Amazon S3 bucket. An example of an Amazon SNS topic ARN is `arn:aws:sns:us-
    # west-2:123456789012:MyTopic`. For more information about Amazon SNS topics,
    # see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key prefix of the Amazon S3 bucket. The key prefix is similar to a
    # directory name that enables you to store similar data under the same
    # directory in a bucket.
    object_key_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The customer master key that Amazon SES should use to encrypt your emails
    # before saving them to the Amazon S3 bucket. You can use the default master
    # key or a custom master key you created in AWS KMS as follows:

    #   * To use the default master key, provide an ARN in the form of `arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`. For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be `arn:aws:kms:us-west-2:123456789012:alias/aws/ses`. If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.

    #   * To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the [Amazon SES Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html).

    # For more information about key policies, see the [AWS KMS Developer
    # Guide](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).
    # If you do not specify a master key, Amazon SES will not encrypt your
    # emails.

    # Your mail is encrypted by Amazon SES using the Amazon S3 encryption client
    # before the mail is submitted to Amazon S3 for storage. It is not encrypted
    # using Amazon S3 server-side encryption. This means that you must use the
    # Amazon S3 encryption client to decrypt the email after retrieving it from
    # Amazon S3, as the service has no access to use your AWS KMS keys for
    # decryption. This encryption client is currently available with the [AWS SDK
    # for Java](http://aws.amazon.com/sdk-for-java/) and [AWS SDK for
    # Ruby](http://aws.amazon.com/sdk-for-ruby/) only. For more information about
    # client-side encryption using AWS KMS master keys, see the [Amazon S3
    # Developer
    # Guide](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html).
    kms_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SNSAction(ShapeBase):
    """
    When included in a receipt rule, this action publishes a notification to Amazon
    Simple Notification Service (Amazon SNS). This action includes a complete copy
    of the email content in the Amazon SNS notifications. Amazon SNS notifications
    for all other actions simply provide information about the email. They do not
    include the email content itself.

    If you own the Amazon SNS topic, you don't need to do anything to give Amazon
    SES permission to publish emails to it. However, if you don't own the Amazon SNS
    topic, you need to attach a policy to the topic to give Amazon SES permissions
    to access it. For information about giving permissions, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-
    email-permissions.html).

    You can only publish emails that are 150 KB or less (including the header) to
    Amazon SNS. Larger emails will bounce. If you anticipate emails larger than 150
    KB, use the S3 action instead.

    For information about using a receipt rule to publish an Amazon SNS
    notification, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    action-sns.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "encoding",
                "Encoding",
                TypeInfo(typing.Union[str, SNSActionEncoding]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An
    # example of an Amazon SNS topic ARN is `arn:aws:sns:us-
    # west-2:123456789012:MyTopic`. For more information about Amazon SNS topics,
    # see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encoding to use for the email within the Amazon SNS notification. UTF-8
    # is easier to use, but may not preserve all special characters when a
    # message was encoded with a different encoding format. Base64 preserves all
    # special characters. The default value is UTF-8.
    encoding: typing.Union[str, "SNSActionEncoding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SNSActionEncoding(str):
    UTF_8 = "UTF-8"
    Base64 = "Base64"


@dataclasses.dataclass
class SNSDestination(ShapeBase):
    """
    Contains the topic ARN associated with an Amazon Simple Notification Service
    (Amazon SNS) event destination.

    Event destinations, such as Amazon SNS, are associated with configuration sets,
    which enable you to publish email sending events. For information about using
    configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicARN",
                TypeInfo(str),
            ),
        ]

    # The ARN of the Amazon SNS topic that email sending events will be published
    # to. An example of an Amazon SNS topic ARN is `arn:aws:sns:us-
    # west-2:123456789012:MyTopic`. For more information about Amazon SNS topics,
    # see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendBounceRequest(ShapeBase):
    """
    Represents a request to send a bounce message to the sender of an email you
    received through Amazon SES.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "original_message_id",
                "OriginalMessageId",
                TypeInfo(str),
            ),
            (
                "bounce_sender",
                "BounceSender",
                TypeInfo(str),
            ),
            (
                "bounced_recipient_info_list",
                "BouncedRecipientInfoList",
                TypeInfo(typing.List[BouncedRecipientInfo]),
            ),
            (
                "explanation",
                "Explanation",
                TypeInfo(str),
            ),
            (
                "message_dsn",
                "MessageDsn",
                TypeInfo(MessageDsn),
            ),
            (
                "bounce_sender_arn",
                "BounceSenderArn",
                TypeInfo(str),
            ),
        ]

    # The message ID of the message to be bounced.
    original_message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The address to use in the "From" header of the bounce message. This must be
    # an identity that you have verified with Amazon SES.
    bounce_sender: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of recipients of the bounced message, including the information
    # required to create the Delivery Status Notifications (DSNs) for the
    # recipients. You must specify at least one `BouncedRecipientInfo` in the
    # list.
    bounced_recipient_info_list: typing.List["BouncedRecipientInfo"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # Human-readable text for the bounce message to explain the failure. If not
    # specified, the text will be auto-generated based on the bounced recipient
    # information.
    explanation: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Message-related DSN fields. If not specified, Amazon SES will choose the
    # values.
    message_dsn: "MessageDsn" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to use the address in the "From" header of the bounce. For more
    # information about sending authorization, see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    bounce_sender_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendBounceResponse(OutputShapeBase):
    """
    Represents a unique message ID.
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
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message ID of the bounce message.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendBulkTemplatedEmailRequest(ShapeBase):
    """
    Represents a request to send a templated email to multiple destinations using
    Amazon SES. For more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
    email-api.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "template",
                "Template",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[BulkEmailDestination]),
            ),
            (
                "source_arn",
                "SourceArn",
                TypeInfo(str),
            ),
            (
                "reply_to_addresses",
                "ReplyToAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "return_path",
                "ReturnPath",
                TypeInfo(str),
            ),
            (
                "return_path_arn",
                "ReturnPathArn",
                TypeInfo(str),
            ),
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "default_tags",
                "DefaultTags",
                TypeInfo(typing.List[MessageTag]),
            ),
            (
                "template_arn",
                "TemplateArn",
                TypeInfo(str),
            ),
            (
                "default_template_data",
                "DefaultTemplateData",
                TypeInfo(str),
            ),
        ]

    # The email address that is sending the email. This email address must be
    # either individually verified with Amazon SES, or from a domain that has
    # been verified with Amazon SES. For information about verifying identities,
    # see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-
    # addresses-and-domains.html).

    # If you are sending on behalf of another user and have been permitted to do
    # so by a sending authorization policy, then you must also specify the
    # `SourceArn` parameter. For more information about sending authorization,
    # see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).

    # Amazon SES does not support the SMTPUTF8 extension, as described in
    # [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the _local
    # part_ of a source email address (the part of the email address that
    # precedes the @ sign) may only contain [7-bit ASCII
    # characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the
    # _domain part_ of an address (the part after the @ sign) contains non-ASCII
    # characters, they must be encoded using Punycode, as described in
    # [RFC3492](https://tools.ietf.org/html/rfc3492.html). The sender name (also
    # known as the _friendly name_ ) may contain non-ASCII characters. These
    # characters must be encoded using MIME encoded-word syntax, as described in
    # [RFC 2047](https://tools.ietf.org/html/rfc2047). MIME encoded-word syntax
    # uses the following form: `=?charset?encoding?encoded-text?=`.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The template to use when sending this email.
    template: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more `Destination` objects. All of the recipients in a `Destination`
    # will receive the same version of the email. You can specify up to 50
    # `Destination` objects within a `Destinations` array.
    destinations: typing.List["BulkEmailDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to send for the email address specified in the `Source`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to send from `user@example.com`, then you would specify the
    # `SourceArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `Source` to be
    # `user@example.com`.

    # For more information about sending authorization, see the [Amazon SES
    # Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reply-to email address(es) for the message. If the recipient replies to
    # the message, each reply-to address will receive the reply.
    reply_to_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The email address that bounces and complaints will be forwarded to when
    # feedback forwarding is enabled. If the message cannot be delivered to the
    # recipient, then an error message will be returned from the recipient's ISP;
    # this message will then be forwarded to the email address specified by the
    # `ReturnPath` parameter. The `ReturnPath` parameter is never overwritten.
    # This email address must be either individually verified with Amazon SES, or
    # from a domain that has been verified with Amazon SES.
    return_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to use the email address specified in the `ReturnPath`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to use `feedback@example.com`, then you would specify the
    # `ReturnPathArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `ReturnPath` to be
    # `feedback@example.com`.

    # For more information about sending authorization, see the [Amazon SES
    # Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    return_path_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the configuration set to use when you send an email using
    # `SendBulkTemplatedEmail`.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags, in the form of name/value pairs, to apply to an email that
    # you send to a destination using `SendBulkTemplatedEmail`.
    default_tags: typing.List["MessageTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the template to use when sending this email.
    template_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of replacement values to apply to the template when replacement data
    # is not specified in a Destination object. These values act as a default or
    # fallback option when no other data is available.

    # The template data is a JSON object, typically consisting of key-value pairs
    # in which the keys correspond to replacement tags in the email template.
    default_template_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendBulkTemplatedEmailResponse(OutputShapeBase):
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
                "Status",
                TypeInfo(typing.List[BulkEmailDestinationStatus]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique message identifier returned from the `SendBulkTemplatedEmail`
    # action.
    status: typing.List["BulkEmailDestinationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendCustomVerificationEmailRequest(ShapeBase):
    """
    Represents a request to send a custom verification email to a specified
    recipient.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # The email address to verify.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the custom verification email template to use when sending the
    # verification email.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of a configuration set to use when sending the verification email.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendCustomVerificationEmailResponse(OutputShapeBase):
    """
    The response received when attempting to send the custom verification email.
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
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique message identifier returned from the
    # `SendCustomVerificationEmail` operation.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendDataPoint(ShapeBase):
    """
    Represents sending statistics data. Each `SendDataPoint` contains statistics for
    a 15-minute period of sending activity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "delivery_attempts",
                "DeliveryAttempts",
                TypeInfo(int),
            ),
            (
                "bounces",
                "Bounces",
                TypeInfo(int),
            ),
            (
                "complaints",
                "Complaints",
                TypeInfo(int),
            ),
            (
                "rejects",
                "Rejects",
                TypeInfo(int),
            ),
        ]

    # Time of the data point.
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of emails that have been sent.
    delivery_attempts: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of emails that have bounced.
    bounces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of unwanted emails that were rejected by recipients.
    complaints: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of emails rejected by Amazon SES.
    rejects: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendEmailRequest(ShapeBase):
    """
    Represents a request to send a single formatted email using Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-
    formatted.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(Destination),
            ),
            (
                "message",
                "Message",
                TypeInfo(Message),
            ),
            (
                "reply_to_addresses",
                "ReplyToAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "return_path",
                "ReturnPath",
                TypeInfo(str),
            ),
            (
                "source_arn",
                "SourceArn",
                TypeInfo(str),
            ),
            (
                "return_path_arn",
                "ReturnPathArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[MessageTag]),
            ),
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # The email address that is sending the email. This email address must be
    # either individually verified with Amazon SES, or from a domain that has
    # been verified with Amazon SES. For information about verifying identities,
    # see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-
    # addresses-and-domains.html).

    # If you are sending on behalf of another user and have been permitted to do
    # so by a sending authorization policy, then you must also specify the
    # `SourceArn` parameter. For more information about sending authorization,
    # see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).

    # Amazon SES does not support the SMTPUTF8 extension, as described in
    # [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the _local
    # part_ of a source email address (the part of the email address that
    # precedes the @ sign) may only contain [7-bit ASCII
    # characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the
    # _domain part_ of an address (the part after the @ sign) contains non-ASCII
    # characters, they must be encoded using Punycode, as described in
    # [RFC3492](https://tools.ietf.org/html/rfc3492.html). The sender name (also
    # known as the _friendly name_ ) may contain non-ASCII characters. These
    # characters must be encoded using MIME encoded-word syntax, as described in
    # [RFC 2047](https://tools.ietf.org/html/rfc2047). MIME encoded-word syntax
    # uses the following form: `=?charset?encoding?encoded-text?=`.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination for this email, composed of To:, CC:, and BCC: fields.
    destination: "Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message to be sent.
    message: "Message" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reply-to email address(es) for the message. If the recipient replies to
    # the message, each reply-to address will receive the reply.
    reply_to_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The email address that bounces and complaints will be forwarded to when
    # feedback forwarding is enabled. If the message cannot be delivered to the
    # recipient, then an error message will be returned from the recipient's ISP;
    # this message will then be forwarded to the email address specified by the
    # `ReturnPath` parameter. The `ReturnPath` parameter is never overwritten.
    # This email address must be either individually verified with Amazon SES, or
    # from a domain that has been verified with Amazon SES.
    return_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to send for the email address specified in the `Source`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to send from `user@example.com`, then you would specify the
    # `SourceArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `Source` to be
    # `user@example.com`.

    # For more information about sending authorization, see the [Amazon SES
    # Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to use the email address specified in the `ReturnPath`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to use `feedback@example.com`, then you would specify the
    # `ReturnPathArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `ReturnPath` to be
    # `feedback@example.com`.

    # For more information about sending authorization, see the [Amazon SES
    # Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    return_path_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags, in the form of name/value pairs, to apply to an email that
    # you send using `SendEmail`. Tags correspond to characteristics of the email
    # that you define, so that you can publish email sending events.
    tags: typing.List["MessageTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the configuration set to use when you send an email using
    # `SendEmail`.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendEmailResponse(OutputShapeBase):
    """
    Represents a unique message ID.
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
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique message identifier returned from the `SendEmail` action.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendRawEmailRequest(ShapeBase):
    """
    Represents a request to send a single raw email using Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-
    raw.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "raw_message",
                "RawMessage",
                TypeInfo(RawMessage),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[str]),
            ),
            (
                "from_arn",
                "FromArn",
                TypeInfo(str),
            ),
            (
                "source_arn",
                "SourceArn",
                TypeInfo(str),
            ),
            (
                "return_path_arn",
                "ReturnPathArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[MessageTag]),
            ),
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # The raw email message itself. The message has to meet the following
    # criteria:

    #   * The message has to contain a header and a body, separated by a blank line.

    #   * All of the required header fields must be present in the message.

    #   * Each part of a multipart MIME message must be formatted properly.

    #   * Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see [Unsupported Attachment Types](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types.html) in the _Amazon SES Developer Guide_.

    #   * The entire message must be base64-encoded.

    #   * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see [Sending Raw Email](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html) in the _Amazon SES Developer Guide_.

    #   * Per [RFC 5321](https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6), the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters.
    raw_message: "RawMessage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identity's email address. If you do not provide a value for this
    # parameter, you must specify a "From" address in the raw text of the
    # message. (You can also specify both.)

    # Amazon SES does not support the SMTPUTF8 extension, as described
    # in[RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the
    # _local part_ of a source email address (the part of the email address that
    # precedes the @ sign) may only contain [7-bit ASCII
    # characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the
    # _domain part_ of an address (the part after the @ sign) contains non-ASCII
    # characters, they must be encoded using Punycode, as described in
    # [RFC3492](https://tools.ietf.org/html/rfc3492.html). The sender name (also
    # known as the _friendly name_ ) may contain non-ASCII characters. These
    # characters must be encoded using MIME encoded-word syntax, as described in
    # [RFC 2047](https://tools.ietf.org/html/rfc2047). MIME encoded-word syntax
    # uses the following form: `=?charset?encoding?encoded-text?=`.

    # If you specify the `Source` parameter and have feedback forwarding enabled,
    # then bounces and complaints will be sent to this email address. This takes
    # precedence over any Return-Path header that you might include in the raw
    # text of the message.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations for the message, consisting of To:, CC:, and BCC:
    # addresses.
    destinations: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to specify a particular "From" address in the header of the raw
    # email.

    # Instead of using this parameter, you can use the X-header `X-SES-FROM-ARN`
    # in the raw message of the email. If you use both the `FromArn` parameter
    # and the corresponding X-header, Amazon SES uses the value of the `FromArn`
    # parameter.

    # For information about when to use this parameter, see the description of
    # `SendRawEmail` in this guide, or see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization-delegate-sender-tasks-email.html).
    from_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to send for the email address specified in the `Source`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to send from `user@example.com`, then you would specify the
    # `SourceArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `Source` to be
    # `user@example.com`.

    # Instead of using this parameter, you can use the X-header `X-SES-SOURCE-
    # ARN` in the raw message of the email. If you use both the `SourceArn`
    # parameter and the corresponding X-header, Amazon SES uses the value of the
    # `SourceArn` parameter.

    # For information about when to use this parameter, see the description of
    # `SendRawEmail` in this guide, or see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization-delegate-sender-tasks-email.html).
    source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to use the email address specified in the `ReturnPath`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to use `feedback@example.com`, then you would specify the
    # `ReturnPathArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `ReturnPath` to be
    # `feedback@example.com`.

    # Instead of using this parameter, you can use the X-header `X-SES-RETURN-
    # PATH-ARN` in the raw message of the email. If you use both the
    # `ReturnPathArn` parameter and the corresponding X-header, Amazon SES uses
    # the value of the `ReturnPathArn` parameter.

    # For information about when to use this parameter, see the description of
    # `SendRawEmail` in this guide, or see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization-delegate-sender-tasks-email.html).
    return_path_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags, in the form of name/value pairs, to apply to an email that
    # you send using `SendRawEmail`. Tags correspond to characteristics of the
    # email that you define, so that you can publish email sending events.
    tags: typing.List["MessageTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the configuration set to use when you send an email using
    # `SendRawEmail`.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendRawEmailResponse(OutputShapeBase):
    """
    Represents a unique message ID.
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
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique message identifier returned from the `SendRawEmail` action.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendTemplatedEmailRequest(ShapeBase):
    """
    Represents a request to send a templated email using Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-
    email-api.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(Destination),
            ),
            (
                "template",
                "Template",
                TypeInfo(str),
            ),
            (
                "template_data",
                "TemplateData",
                TypeInfo(str),
            ),
            (
                "reply_to_addresses",
                "ReplyToAddresses",
                TypeInfo(typing.List[str]),
            ),
            (
                "return_path",
                "ReturnPath",
                TypeInfo(str),
            ),
            (
                "source_arn",
                "SourceArn",
                TypeInfo(str),
            ),
            (
                "return_path_arn",
                "ReturnPathArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[MessageTag]),
            ),
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "template_arn",
                "TemplateArn",
                TypeInfo(str),
            ),
        ]

    # The email address that is sending the email. This email address must be
    # either individually verified with Amazon SES, or from a domain that has
    # been verified with Amazon SES. For information about verifying identities,
    # see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-
    # addresses-and-domains.html).

    # If you are sending on behalf of another user and have been permitted to do
    # so by a sending authorization policy, then you must also specify the
    # `SourceArn` parameter. For more information about sending authorization,
    # see the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).

    # Amazon SES does not support the SMTPUTF8 extension, as described in
    # [RFC6531](https://tools.ietf.org/html/rfc6531). For this reason, the _local
    # part_ of a source email address (the part of the email address that
    # precedes the @ sign) may only contain [7-bit ASCII
    # characters](https://en.wikipedia.org/wiki/Email_address#Local-part). If the
    # _domain part_ of an address (the part after the @ sign) contains non-ASCII
    # characters, they must be encoded using Punycode, as described in
    # [RFC3492](https://tools.ietf.org/html/rfc3492.html). The sender name (also
    # known as the _friendly name_ ) may contain non-ASCII characters. These
    # characters must be encoded using MIME encoded-word syntax, as described
    # in[RFC 2047](https://tools.ietf.org/html/rfc2047). MIME encoded-word syntax
    # uses the following form: `=?charset?encoding?encoded-text?=`.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The destination for this email, composed of To:, CC:, and BCC: fields. A
    # Destination can include up to 50 recipients across these three fields.
    destination: "Destination" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The template to use when sending this email.
    template: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of replacement values to apply to the template. This parameter is a
    # JSON object, typically consisting of key-value pairs in which the keys
    # correspond to replacement tags in the email template.
    template_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reply-to email address(es) for the message. If the recipient replies to
    # the message, each reply-to address will receive the reply.
    reply_to_addresses: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The email address that bounces and complaints will be forwarded to when
    # feedback forwarding is enabled. If the message cannot be delivered to the
    # recipient, then an error message will be returned from the recipient's ISP;
    # this message will then be forwarded to the email address specified by the
    # `ReturnPath` parameter. The `ReturnPath` parameter is never overwritten.
    # This email address must be either individually verified with Amazon SES, or
    # from a domain that has been verified with Amazon SES.
    return_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to send for the email address specified in the `Source`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to send from `user@example.com`, then you would specify the
    # `SourceArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `Source` to be
    # `user@example.com`.

    # For more information about sending authorization, see the [Amazon SES
    # Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    source_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is used only for sending authorization. It is the ARN of the
    # identity that is associated with the sending authorization policy that
    # permits you to use the email address specified in the `ReturnPath`
    # parameter.

    # For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`) attaches a policy to it that
    # authorizes you to use `feedback@example.com`, then you would specify the
    # `ReturnPathArn` to be `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`, and the `ReturnPath` to be
    # `feedback@example.com`.

    # For more information about sending authorization, see the [Amazon SES
    # Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-
    # authorization.html).
    return_path_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags, in the form of name/value pairs, to apply to an email that
    # you send using `SendTemplatedEmail`. Tags correspond to characteristics of
    # the email that you define, so that you can publish email sending events.
    tags: typing.List["MessageTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the configuration set to use when you send an email using
    # `SendTemplatedEmail`.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the template to use when sending this email.
    template_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendTemplatedEmailResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique message identifier returned from the `SendTemplatedEmail`
    # action.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetActiveReceiptRuleSetRequest(ShapeBase):
    """
    Represents a request to set a receipt rule set as the active receipt rule set.
    You use receipt rule sets to receive email with Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
        ]

    # The name of the receipt rule set to make active. Setting this value to null
    # disables all email receiving.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetActiveReceiptRuleSetResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class SetIdentityDkimEnabledRequest(ShapeBase):
    """
    Represents a request to enable or disable Amazon SES Easy DKIM signing for an
    identity. For more information about setting up Easy DKIM, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-
    dkim.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "dkim_enabled",
                "DkimEnabled",
                TypeInfo(bool),
            ),
        ]

    # The identity for which DKIM signing should be enabled or disabled.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets whether DKIM signing is enabled for an identity. Set to `true` to
    # enable DKIM signing for this identity; `false` to disable it.
    dkim_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetIdentityDkimEnabledResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class SetIdentityFeedbackForwardingEnabledRequest(ShapeBase):
    """
    Represents a request to enable or disable whether Amazon SES forwards you bounce
    and complaint notifications through email. For information about email feedback
    forwarding, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications-via-
    email.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "forwarding_enabled",
                "ForwardingEnabled",
                TypeInfo(bool),
            ),
        ]

    # The identity for which to set bounce and complaint notification forwarding.
    # Examples: `user@example.com`, `example.com`.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets whether Amazon SES will forward bounce and complaint notifications as
    # email. `true` specifies that Amazon SES will forward bounce and complaint
    # notifications as email, in addition to any Amazon SNS topic publishing
    # otherwise specified. `false` specifies that Amazon SES will publish bounce
    # and complaint notifications only through Amazon SNS. This value can only be
    # set to `false` when Amazon SNS topics are set for both `Bounce` and
    # `Complaint` notification types.
    forwarding_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetIdentityFeedbackForwardingEnabledResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class SetIdentityHeadersInNotificationsEnabledRequest(ShapeBase):
    """
    Represents a request to set whether Amazon SES includes the original email
    headers in the Amazon SNS notifications of a specified type. For information
    about notifications, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications-via-
    sns.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "notification_type",
                "NotificationType",
                TypeInfo(typing.Union[str, NotificationType]),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The identity for which to enable or disable headers in notifications.
    # Examples: `user@example.com`, `example.com`.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The notification type for which to enable or disable headers in
    # notifications.
    notification_type: typing.Union[str, "NotificationType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Sets whether Amazon SES includes the original email headers in Amazon SNS
    # notifications of the specified notification type. A value of `true`
    # specifies that Amazon SES will include headers in notifications, and a
    # value of `false` specifies that Amazon SES will not include headers in
    # notifications.

    # This value can only be set when `NotificationType` is already set to use a
    # particular Amazon SNS topic.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetIdentityHeadersInNotificationsEnabledResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class SetIdentityMailFromDomainRequest(ShapeBase):
    """
    Represents a request to enable or disable the Amazon SES custom MAIL FROM domain
    setup for a verified identity. For information about using a custom MAIL FROM
    domain, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "mail_from_domain",
                "MailFromDomain",
                TypeInfo(str),
            ),
            (
                "behavior_on_mx_failure",
                "BehaviorOnMXFailure",
                TypeInfo(typing.Union[str, BehaviorOnMXFailure]),
            ),
        ]

    # The verified identity for which you want to enable or disable the specified
    # custom MAIL FROM domain.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The custom MAIL FROM domain that you want the verified identity to use. The
    # MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be
    # used in a "From" address if the MAIL FROM domain is the destination of
    # email feedback forwarding (for more information, see the [Amazon SES
    # Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-
    # from.html)), and 3) not be used to receive emails. A value of `null`
    # disables the custom MAIL FROM setting for the identity.
    mail_from_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action that you want Amazon SES to take if it cannot successfully read
    # the required MX record when you send an email. If you choose
    # `UseDefaultValue`, Amazon SES will use amazonses.com (or a subdomain of
    # that) as the MAIL FROM domain. If you choose `RejectMessage`, Amazon SES
    # will return a `MailFromDomainNotVerified` error and not send the email.

    # The action specified in `BehaviorOnMXFailure` is taken when the custom MAIL
    # FROM domain setup is in the `Pending`, `Failed`, and `TemporaryFailure`
    # states.
    behavior_on_mx_failure: typing.Union[str, "BehaviorOnMXFailure"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class SetIdentityMailFromDomainResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class SetIdentityNotificationTopicRequest(ShapeBase):
    """
    Represents a request to specify the Amazon SNS topic to which Amazon SES will
    publish bounce, complaint, or delivery notifications for emails sent with that
    identity as the Source. For information about Amazon SES notifications, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications-via-
    sns.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "notification_type",
                "NotificationType",
                TypeInfo(typing.Union[str, NotificationType]),
            ),
            (
                "sns_topic",
                "SnsTopic",
                TypeInfo(str),
            ),
        ]

    # The identity (email address or domain) that you want to set the Amazon SNS
    # topic for.

    # You can only specify a verified identity for this parameter.

    # You can specify an identity by using its name or by using its Amazon
    # Resource Name (ARN). The following examples are all valid identities:
    # `sender@example.com`, `example.com`, `arn:aws:ses:us-
    # east-1:123456789012:identity/example.com`.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of notifications that will be published to the specified Amazon
    # SNS topic.
    notification_type: typing.Union[str, "NotificationType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is
    # omitted from the request or a null value is passed, `SnsTopic` is cleared
    # and publishing is disabled.
    sns_topic: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetIdentityNotificationTopicResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class SetReceiptRulePositionRequest(ShapeBase):
    """
    Represents a request to set the position of a receipt rule in a receipt rule
    set. You use receipt rule sets to receive email with Amazon SES. For more
    information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "rule_name",
                "RuleName",
                TypeInfo(str),
            ),
            (
                "after",
                "After",
                TypeInfo(str),
            ),
        ]

    # The name of the receipt rule set that contains the receipt rule to
    # reposition.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the receipt rule to reposition.
    rule_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the receipt rule after which to place the specified receipt
    # rule.
    after: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetReceiptRulePositionResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class StopAction(ShapeBase):
    """
    When included in a receipt rule, this action terminates the evaluation of the
    receipt rule set and, optionally, publishes a notification to Amazon Simple
    Notification Service (Amazon SNS).

    For information about setting a stop action in a receipt rule, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    action-stop.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scope",
                "Scope",
                TypeInfo(typing.Union[str, StopScope]),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    # The name of the RuleSet that is being stopped.
    scope: typing.Union[str, "StopScope"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the
    # stop action is taken. An example of an Amazon SNS topic ARN is
    # `arn:aws:sns:us-west-2:123456789012:MyTopic`. For more information about
    # Amazon SNS topics, see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class StopScope(str):
    RuleSet = "RuleSet"


@dataclasses.dataclass
class Template(ShapeBase):
    """
    The content of the email, composed of a subject line, an HTML part, and a text-
    only part.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "subject_part",
                "SubjectPart",
                TypeInfo(str),
            ),
            (
                "text_part",
                "TextPart",
                TypeInfo(str),
            ),
            (
                "html_part",
                "HtmlPart",
                TypeInfo(str),
            ),
        ]

    # The name of the template. You will refer to this name when you send email
    # using the `SendTemplatedEmail` or `SendBulkTemplatedEmail` operations.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject line of the email.
    subject_part: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email body that will be visible to recipients whose email clients do
    # not display HTML.
    text_part: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTML body of the email.
    html_part: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TemplateDoesNotExistException(ShapeBase):
    """
    Indicates that the Template object you specified does not exist in your Amazon
    SES account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
        ]

    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TemplateMetadata(ShapeBase):
    """
    Contains information about an email template.
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
                "created_timestamp",
                "CreatedTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the template.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time and date the template was created.
    created_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TestRenderTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "template_data",
                "TemplateData",
                TypeInfo(str),
            ),
        ]

    # The name of the template that you want to render.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of replacement values to apply to the template. This parameter is a
    # JSON object, typically consisting of key-value pairs in which the keys
    # correspond to replacement tags in the email template.
    template_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TestRenderTemplateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "rendered_template",
                "RenderedTemplate",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The complete MIME message rendered by applying the data in the TemplateData
    # parameter to the template specified in the TemplateName parameter.
    rendered_template: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TlsPolicy(str):
    Require = "Require"
    Optional = "Optional"


@dataclasses.dataclass
class TrackingOptions(ShapeBase):
    """
    A domain that is used to redirect email recipients to an Amazon SES-operated
    domain. This domain captures open and click events generated by Amazon SES
    emails.

    For more information, see [Configuring Custom Domains to Handle Open and Click
    Tracking](ses/latest/DeveloperGuide/configure-custom-open-click-domains.html) in
    the _Amazon SES Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_redirect_domain",
                "CustomRedirectDomain",
                TypeInfo(str),
            ),
        ]

    # The custom subdomain that will be used to redirect email recipients to the
    # Amazon SES event tracking domain.
    custom_redirect_domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrackingOptionsAlreadyExistsException(ShapeBase):
    """
    Indicates that the configuration set you specified already contains a
    TrackingOptions object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # Indicates that a TrackingOptions object already exists in the specified
    # configuration set.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrackingOptionsDoesNotExistException(ShapeBase):
    """
    Indicates that the TrackingOptions object you specified does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
        ]

    # Indicates that a TrackingOptions object does not exist in the specified
    # configuration set.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAccountSendingEnabledRequest(ShapeBase):
    """
    Represents a request to enable or disable the email sending capabilities for
    your entire Amazon SES account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # Describes whether email sending is enabled or disabled for your Amazon SES
    # account in the current AWS Region.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConfigurationSetEventDestinationRequest(ShapeBase):
    """
    Represents a request to update the event destination of a configuration set.
    Configuration sets enable you to publish email sending events. For information
    about using configuration sets, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-
    activity.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "event_destination",
                "EventDestination",
                TypeInfo(EventDestination),
            ),
        ]

    # The name of the configuration set that contains the event destination that
    # you want to update.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event destination object that you want to apply to the specified
    # configuration set.
    event_destination: "EventDestination" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateConfigurationSetEventDestinationResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class UpdateConfigurationSetReputationMetricsEnabledRequest(ShapeBase):
    """
    Represents a request to modify the reputation metric publishing settings for a
    configuration set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the configuration set that you want to update.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes whether or not Amazon SES will publish reputation metrics for the
    # configuration set, such as bounce and complaint rates, to Amazon
    # CloudWatch.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConfigurationSetSendingEnabledRequest(ShapeBase):
    """
    Represents a request to enable or disable the email sending capabilities for a
    specific configuration set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The name of the configuration set that you want to update.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes whether email sending is enabled or disabled for the
    # configuration set.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConfigurationSetTrackingOptionsRequest(ShapeBase):
    """
    Represents a request to update the tracking options for a configuration set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "configuration_set_name",
                "ConfigurationSetName",
                TypeInfo(str),
            ),
            (
                "tracking_options",
                "TrackingOptions",
                TypeInfo(TrackingOptions),
            ),
        ]

    # The name of the configuration set for which you want to update the custom
    # tracking domain.
    configuration_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A domain that is used to redirect email recipients to an Amazon SES-
    # operated domain. This domain captures open and click events generated by
    # Amazon SES emails.

    # For more information, see [Configuring Custom Domains to Handle Open and
    # Click Tracking](ses/latest/DeveloperGuide/configure-custom-open-click-
    # domains.html) in the _Amazon SES Developer Guide_.
    tracking_options: "TrackingOptions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateConfigurationSetTrackingOptionsResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class UpdateCustomVerificationEmailTemplateRequest(ShapeBase):
    """
    Represents a request to update an existing custom verification email template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template_name",
                "TemplateName",
                TypeInfo(str),
            ),
            (
                "from_email_address",
                "FromEmailAddress",
                TypeInfo(str),
            ),
            (
                "template_subject",
                "TemplateSubject",
                TypeInfo(str),
            ),
            (
                "template_content",
                "TemplateContent",
                TypeInfo(str),
            ),
            (
                "success_redirection_url",
                "SuccessRedirectionURL",
                TypeInfo(str),
            ),
            (
                "failure_redirection_url",
                "FailureRedirectionURL",
                TypeInfo(str),
            ),
        ]

    # The name of the custom verification email template that you want to update.
    template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address that the custom verification email is sent from.
    from_email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject line of the custom verification email.
    template_subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content of the custom verification email. The total size of the email
    # must be less than 10 MB. The message body may contain HTML, with some
    # limitations. For more information, see [Custom Verification Email
    # Frequently Asked
    # Questions](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-
    # verification-emails.html#custom-verification-emails-faq) in the _Amazon SES
    # Developer Guide_.
    template_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is successfully verified.
    success_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL that the recipient of the verification email is sent to if his or
    # her address is not successfully verified.
    failure_redirection_url: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateReceiptRuleRequest(ShapeBase):
    """
    Represents a request to update a receipt rule. You use receipt rules to receive
    email with Amazon SES. For more information, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    concepts.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rule_set_name",
                "RuleSetName",
                TypeInfo(str),
            ),
            (
                "rule",
                "Rule",
                TypeInfo(ReceiptRule),
            ),
        ]

    # The name of the receipt rule set that the receipt rule belongs to.
    rule_set_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A data structure that contains the updated receipt rule information.
    rule: "ReceiptRule" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateReceiptRuleResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class UpdateTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "template",
                "Template",
                TypeInfo(Template),
            ),
        ]

    # The content of the email, composed of a subject line, an HTML part, and a
    # text-only part.
    template: "Template" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTemplateResponse(OutputShapeBase):
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


class VerificationStatus(str):
    Pending = "Pending"
    Success = "Success"
    Failed = "Failed"
    TemporaryFailure = "TemporaryFailure"
    NotStarted = "NotStarted"


@dataclasses.dataclass
class VerifyDomainDkimRequest(ShapeBase):
    """
    Represents a request to generate the CNAME records needed to set up Easy DKIM
    with Amazon SES. For more information about setting up Easy DKIM, see the
    [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html).
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

    # The name of the domain to be verified for Easy DKIM signing.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyDomainDkimResponse(OutputShapeBase):
    """
    Returns CNAME records that you must publish to the DNS server of your domain to
    set up Easy DKIM with Amazon SES.
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
                "dkim_tokens",
                "DkimTokens",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of character strings that represent the domain's identity. If the
    # identity is an email address, the tokens represent the domain of that
    # address.

    # Using these tokens, you will need to create DNS CNAME records that point to
    # DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually
    # detect that you have updated your DNS records; this detection process may
    # take up to 72 hours. Upon successful detection, Amazon SES will be able to
    # DKIM-sign emails originating from that domain.

    # For more information about creating DNS records using DKIM tokens, go to
    # the [Amazon SES Developer
    # Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-
    # records.html).
    dkim_tokens: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VerifyDomainIdentityRequest(ShapeBase):
    """
    Represents a request to begin Amazon SES domain verification and to generate the
    TXT records that you must publish to the DNS server of your domain to complete
    the verification. For information about domain verification, see the [Amazon SES
    Developer Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-
    domains.html).
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

    # The domain to be verified.
    domain: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyDomainIdentityResponse(OutputShapeBase):
    """
    Returns a TXT record that you must publish to the DNS server of your domain to
    complete domain verification with Amazon SES.
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
                "verification_token",
                "VerificationToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A TXT record that you must place in the DNS settings of the domain to
    # complete domain verification with Amazon SES.

    # As Amazon SES searches for the TXT record, the domain's verification status
    # is "Pending". When Amazon SES detects the record, the domain's verification
    # status changes to "Success". If Amazon SES is unable to detect the record
    # within 72 hours, the domain's verification status changes to "Failed." In
    # that case, if you still want to verify the domain, you must restart the
    # verification process from the beginning.
    verification_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyEmailAddressRequest(ShapeBase):
    """
    Represents a request to begin email address verification with Amazon SES. For
    information about email address verification, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-
    addresses.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
        ]

    # The email address to be verified.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyEmailIdentityRequest(ShapeBase):
    """
    Represents a request to begin email address verification with Amazon SES. For
    information about email address verification, see the [Amazon SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-
    addresses.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "email_address",
                "EmailAddress",
                TypeInfo(str),
            ),
        ]

    # The email address to be verified.
    email_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyEmailIdentityResponse(OutputShapeBase):
    """
    An empty element returned on a successful request.
    """

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
class WorkmailAction(ShapeBase):
    """
    When included in a receipt rule, this action calls Amazon WorkMail and,
    optionally, publishes a notification to Amazon Simple Notification Service
    (Amazon SNS). You will typically not use this action directly because Amazon
    WorkMail adds the rule automatically during its setup procedure.

    For information using a receipt rule to call Amazon WorkMail, see the [Amazon
    SES Developer
    Guide](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-
    action-workmail.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "organization_arn",
                "OrganizationArn",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the Amazon WorkMail organization. An example of an Amazon
    # WorkMail organization ARN is `arn:aws:workmail:us-
    # west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7`. For
    # information about Amazon WorkMail organizations, see the [Amazon WorkMail
    # Administrator
    # Guide](http://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html).
    organization_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the
    # WorkMail action is called. An example of an Amazon SNS topic ARN is
    # `arn:aws:sns:us-west-2:123456789012:MyTopic`. For more information about
    # Amazon SNS topics, see the [Amazon SNS Developer
    # Guide](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
