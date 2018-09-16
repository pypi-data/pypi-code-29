import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The request is not well formed. For example, a value is invalid or a required
    field is missing. Check the field values, and try again.
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


class Blob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class BotAliasMetadata(ShapeBase):
    """
    Provides information about a bot alias.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "bot_version",
                "botVersion",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    # The name of the bot alias.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the Amazon Lex bot to which the alias points.
    bot_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bot to which the alias points.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the bot alias was updated. When you create a resource, the
    # creation date and last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot alias was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Checksum of the bot alias.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BotChannelAssociation(ShapeBase):
    """
    Represents an association between an Amazon Lex bot and an external messaging
    platform.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "bot_alias",
                "botAlias",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "bot_configuration",
                "botConfiguration",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ChannelStatus]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
        ]

    # The name of the association between the bot and the channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A text description of the association you are creating.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An alias pointing to the specific version of the Amazon Lex bot to which
    # this association is being made.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon Lex bot to which this association is being made.

    # Currently, Amazon Lex supports associations with Facebook and Slack, and
    # Twilio.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the association between the Amazon Lex bot and the channel
    # was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the type of association by indicating the type of channel being
    # established between the Amazon Lex bot and the external messaging platform.
    type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides information necessary to communicate with the messaging platform.
    bot_configuration: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the bot channel.

    #   * `CREATED` \- The channel has been created and is ready for use.

    #   * `IN_PROGRESS` \- Channel creation is in progress.

    #   * `FAILED` \- There was an error creating the channel. For information about the reason for the failure, see the `failureReason` field.
    status: typing.Union[str, "ChannelStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `status` is `FAILED`, Amazon Lex provides the reason that it failed to
    # create the association.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BotMetadata(ShapeBase):
    """
    Provides information about a bot. .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "status",
                "status",
                TypeInfo(typing.Union[str, Status]),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the bot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the bot.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot was updated. When you create a bot, the creation date
    # and last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the bot. For a new bot, the version is always `$LATEST`.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BuiltinIntentMetadata(ShapeBase):
    """
    Provides metadata for a built-in intent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "signature",
                "signature",
                TypeInfo(str),
            ),
            (
                "supported_locales",
                "supportedLocales",
                TypeInfo(typing.List[typing.Union[str, Locale]]),
            ),
        ]

    # A unique identifier for the built-in intent. To find the signature for an
    # intent, see [Standard Built-in
    # Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-
    # kit/docs/built-in-intent-ref/standard-intents) in the _Alexa Skills Kit_.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of identifiers for the locales that the intent supports.
    supported_locales: typing.List[typing.Union[str, "Locale"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class BuiltinIntentSlot(ShapeBase):
    """
    Provides information about a slot used in a built-in intent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # A list of the slots defined for the intent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BuiltinSlotTypeMetadata(ShapeBase):
    """
    Provides information about a built in slot type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "signature",
                "signature",
                TypeInfo(str),
            ),
            (
                "supported_locales",
                "supportedLocales",
                TypeInfo(typing.List[typing.Union[str, Locale]]),
            ),
        ]

    # A unique identifier for the built-in slot type. To find the signature for a
    # slot type, see [Slot Type
    # Reference](https://developer.amazon.com/public/solutions/alexa/alexa-
    # skills-kit/docs/built-in-intent-ref/slot-type-reference) in the _Alexa
    # Skills Kit_.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of target locales for the slot.
    supported_locales: typing.List[typing.Union[str, "Locale"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


class ChannelStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    CREATED = "CREATED"
    FAILED = "FAILED"


class ChannelType(str):
    Facebook = "Facebook"
    Slack = "Slack"
    Twilio_Sms = "Twilio-Sms"
    Kik = "Kik"


@dataclasses.dataclass
class CodeHook(ShapeBase):
    """
    Specifies a Lambda function that verifies requests to a bot or fulfills the
    user's request to a bot..
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uri",
                "uri",
                TypeInfo(str),
            ),
            (
                "message_version",
                "messageVersion",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Lambda function.
    uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the request-response that you want Amazon Lex to use to
    # invoke your Lambda function. For more information, see using-lambda.
    message_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    There was a conflict processing the request. Try your request again.
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


class ContentType(str):
    PlainText = "PlainText"
    SSML = "SSML"
    CustomPayload = "CustomPayload"


@dataclasses.dataclass
class CreateBotVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    # The name of the bot that you want to create a new version of. The name is
    # case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies a specific revision of the `$LATEST` version of the bot. If you
    # specify a checksum and the `$LATEST` version of the bot has a different
    # checksum, a `PreconditionFailedException` exception is returned and Amazon
    # Lex doesn't publish a new version. If you don't specify a checksum, Amazon
    # Lex publishes the `$LATEST` version.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBotVersionResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[Intent]),
            ),
            (
                "clarification_prompt",
                "clarificationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "abort_statement",
                "abortStatement",
                TypeInfo(Statement),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, Status]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "idle_session_ttl_in_seconds",
                "idleSessionTTLInSeconds",
                TypeInfo(int),
            ),
            (
                "voice_id",
                "voiceId",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
            (
                "child_directed",
                "childDirected",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the bot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `Intent` objects. For more information, see PutBot.
    intents: typing.List["Intent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message that Amazon Lex uses when it doesn't understand the user's
    # request. For more information, see PutBot.
    clarification_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message that Amazon Lex uses to abort a conversation. For more
    # information, see PutBot.
    abort_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When you send a request to create or update a bot, Amazon Lex sets the
    # `status` response element to `BUILDING`. After Amazon Lex builds the bot,
    # it sets `status` to `READY`. If Amazon Lex can't build the bot, it sets
    # `status` to `FAILED`. Amazon Lex returns the reason for the failure in the
    # `failureReason` response element.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `status` is `FAILED`, Amazon Lex provides the reason that it failed to
    # build the bot.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the `$LATEST` version of this bot was updated.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the bot version was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum time in seconds that Amazon Lex retains the data gathered in a
    # conversation. For more information, see PutBot.
    idle_session_ttl_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Polly voice ID that Amazon Lex uses for voice interactions with
    # the user.
    voice_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum identifying the version of the bot that was created.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the target locale for the bot.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For each Amazon Lex bot created with the Amazon Lex Model Building Service,
    # you must specify whether your use of Amazon Lex is related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to the Children's Online Privacy
    # Protection Act (COPPA) by specifying `true` or `false` in the
    # `childDirected` field. By specifying `true` in the `childDirected` field,
    # you confirm that your use of Amazon Lex **is** related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to COPPA. By specifying `false`
    # in the `childDirected` field, you confirm that your use of Amazon Lex **is
    # not** related to a website, program, or other application that is directed
    # or targeted, in whole or in part, to children under age 13 and subject to
    # COPPA. You may not specify a default value for the `childDirected` field
    # that does not accurately reflect whether your use of Amazon Lex is related
    # to a website, program, or other application that is directed or targeted,
    # in whole or in part, to children under age 13 and subject to COPPA.

    # If your use of Amazon Lex relates to a website, program, or other
    # application that is directed in whole or in part, to children under age 13,
    # you must obtain any required verifiable parental consent under COPPA. For
    # information regarding the use of Amazon Lex in connection with websites,
    # programs, or other applications that are directed or targeted, in whole or
    # in part, to children under age 13, see the [Amazon Lex
    # FAQ.](https://aws.amazon.com/lex/faqs#data-security)
    child_directed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIntentVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    # The name of the intent that you want to create a new version of. The name
    # is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the `$LATEST` version of the intent that should be used to
    # create the new version. If you specify a checksum and the `$LATEST` version
    # of the intent has a different checksum, Amazon Lex returns a
    # `PreconditionFailedException` exception and doesn't publish a new version.
    # If you don't specify a checksum, Amazon Lex publishes the `$LATEST`
    # version.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIntentVersionResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "slots",
                "slots",
                TypeInfo(typing.List[Slot]),
            ),
            (
                "sample_utterances",
                "sampleUtterances",
                TypeInfo(typing.List[str]),
            ),
            (
                "confirmation_prompt",
                "confirmationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "rejection_statement",
                "rejectionStatement",
                TypeInfo(Statement),
            ),
            (
                "follow_up_prompt",
                "followUpPrompt",
                TypeInfo(FollowUpPrompt),
            ),
            (
                "conclusion_statement",
                "conclusionStatement",
                TypeInfo(Statement),
            ),
            (
                "dialog_code_hook",
                "dialogCodeHook",
                TypeInfo(CodeHook),
            ),
            (
                "fulfillment_activity",
                "fulfillmentActivity",
                TypeInfo(FulfillmentActivity),
            ),
            (
                "parent_intent_signature",
                "parentIntentSignature",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the intent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the intent.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of slot types that defines the information required to fulfill the
    # intent.
    slots: typing.List["Slot"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of sample utterances configured for the intent.
    sample_utterances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined, the prompt that Amazon Lex uses to confirm the user's intent
    # before fulfilling it.
    confirmation_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the user answers "no" to the question defined in `confirmationPrompt`,
    # Amazon Lex responds with this statement to acknowledge that the intent was
    # canceled.
    rejection_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined, Amazon Lex uses this prompt to solicit additional user activity
    # after the intent is fulfilled.
    follow_up_prompt: "FollowUpPrompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # After the Lambda function specified in the `fulfillmentActivity` field
    # fulfills the intent, Amazon Lex conveys this statement to the user.
    conclusion_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined, Amazon Lex invokes this Lambda function for each user input.
    dialog_code_hook: "CodeHook" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes how the intent is fulfilled.
    fulfillment_activity: "FulfillmentActivity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier for a built-in intent.
    parent_intent_signature: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was updated.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version number assigned to the new version of the intent.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the intent version created.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSlotTypeVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    # The name of the slot type that you want to create a new version for. The
    # name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum for the `$LATEST` version of the slot type that you want to
    # publish. If you specify a checksum and the `$LATEST` version of the slot
    # type has a different checksum, Amazon Lex returns a
    # `PreconditionFailedException` exception and doesn't publish the new
    # version. If you don't specify a checksum, Amazon Lex publishes the
    # `$LATEST` version.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSlotTypeVersionResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "enumeration_values",
                "enumerationValues",
                TypeInfo(typing.List[EnumerationValue]),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "value_selection_strategy",
                "valueSelectionStrategy",
                TypeInfo(typing.Union[str, SlotValueSelectionStrategy]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the slot type.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the slot type.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `EnumerationValue` objects that defines the values that the slot
    # type can take.
    enumeration_values: typing.List["EnumerationValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was updated. When you create a resource, the
    # creation date and last update date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version assigned to the new slot type version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the `$LATEST` version of the slot type.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The strategy that Amazon Lex uses to determine the value of the slot. For
    # more information, see PutSlotType.
    value_selection_strategy: typing.Union[str, "SlotValueSelectionStrategy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class DeleteBotAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
        ]

    # The name of the alias to delete. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bot that the alias points to.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBotChannelAssociationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "bot_alias",
                "botAlias",
                TypeInfo(str),
            ),
        ]

    # The name of the association. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon Lex bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An alias that points to the specific version of the Amazon Lex bot to which
    # this association is being made.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The name of the bot. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBotVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the bot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot to delete. You cannot delete the `$LATEST` version
    # of the bot. To delete the `$LATEST` version, use the DeleteBot operation.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIntentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The name of the intent. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteIntentVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the intent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the intent to delete. You cannot delete the `$LATEST`
    # version of the intent. To delete the `$LATEST` version, use the
    # DeleteIntent operation.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSlotTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The name of the slot type. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSlotTypeVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the slot type.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the slot type to delete. You cannot delete the `$LATEST`
    # version of the slot type. To delete the `$LATEST` version, use the
    # DeleteSlotType operation.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUtterancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "user_id",
                "userId",
                TypeInfo(str),
            ),
        ]

    # The name of the bot that stored the utterances.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the user that made the utterances. This is the
    # user ID that was sent in the
    # [PostContent](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html)
    # or
    # [PostText](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html)
    # operation request that contained the utterance.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnumerationValue(ShapeBase):
    """
    Each slot type can have a set of values. Each enumeration value represents a
    value the slot type can take.

    For example, a pizza ordering bot could have a slot type that specifies the type
    of crust that the pizza should have. The slot type could include the values

      * thick

      * thin

      * stuffed
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "synonyms",
                "synonyms",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The value of the slot type.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional values related to the slot type value.
    synonyms: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExportStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    READY = "READY"
    FAILED = "FAILED"


class ExportType(str):
    ALEXA_SKILLS_KIT = "ALEXA_SKILLS_KIT"
    LEX = "LEX"


@dataclasses.dataclass
class FollowUpPrompt(ShapeBase):
    """
    A prompt for additional activity after an intent is fulfilled. For example,
    after the `OrderPizza` intent is fulfilled, you might prompt the user to find
    out whether the user wants to order drinks.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "prompt",
                "prompt",
                TypeInfo(Prompt),
            ),
            (
                "rejection_statement",
                "rejectionStatement",
                TypeInfo(Statement),
            ),
        ]

    # Prompts for information from the user.
    prompt: "Prompt" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the user answers "no" to the question defined in the `prompt` field,
    # Amazon Lex responds with this statement to acknowledge that the intent was
    # canceled.
    rejection_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FulfillmentActivity(ShapeBase):
    """
    Describes how the intent is fulfilled after the user provides all of the
    information required for the intent. You can provide a Lambda function to
    process the intent, or you can return the intent information to the client
    application. We recommend that you use a Lambda function so that the relevant
    logic lives in the Cloud and limit the client-side code primarily to
    presentation. If you need to update the logic, you only update the Lambda
    function; you don't need to upgrade your client application.

    Consider the following examples:

      * In a pizza ordering application, after the user provides all of the information for placing an order, you use a Lambda function to place an order with a pizzeria. 

      * In a gaming application, when a user says "pick up a rock," this information must go back to the client application so that it can perform the operation and update the graphics. In this case, you want Amazon Lex to return the intent data to the client.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, FulfillmentActivityType]),
            ),
            (
                "code_hook",
                "codeHook",
                TypeInfo(CodeHook),
            ),
        ]

    # How the intent should be fulfilled, either by running a Lambda function or
    # by returning the slot data to the client application.
    type: typing.Union[str, "FulfillmentActivityType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the Lambda function that is run to fulfill the intent.
    code_hook: "CodeHook" = dataclasses.field(default=ShapeBase.NOT_SET, )


class FulfillmentActivityType(str):
    ReturnIntent = "ReturnIntent"
    CodeHook = "CodeHook"


@dataclasses.dataclass
class GetBotAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
        ]

    # The name of the bot alias. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotAliasResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "bot_version",
                "botVersion",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the bot alias.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot that the alias points to.
    bot_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bot that the alias points to.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the bot alias was updated. When you create a resource, the
    # creation date and the last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot alias was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Checksum of the bot alias.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotAliasesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bot_name",
                "botName",
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
            (
                "name_contains",
                "nameContains",
                TypeInfo(str),
            ),
        ]

    # The name of the bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for fetching the next page of aliases. If the response
    # to this call is truncated, Amazon Lex returns a pagination token in the
    # response. To fetch the next page of aliases, specify the pagination token
    # in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of aliases to return in the response. The default is 50.
    # .
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Substring to match in bot alias names. An alias will be returned if any
    # part of its name matches the substring. For example, "xyz" matches both
    # "xyzabc" and "abcxyz."
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotAliasesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bot_aliases",
                "BotAliases",
                TypeInfo(typing.List[BotAliasMetadata]),
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

    # An array of `BotAliasMetadata` objects, each describing a bot alias.
    bot_aliases: typing.List["BotAliasMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token for fetching next page of aliases. If the response to
    # this call is truncated, Amazon Lex returns a pagination token in the
    # response. To fetch the next page of aliases, specify the pagination token
    # in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetBotAliasesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBotChannelAssociationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "bot_alias",
                "botAlias",
                TypeInfo(str),
            ),
        ]

    # The name of the association between the bot and the channel. The name is
    # case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon Lex bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An alias pointing to the specific version of the Amazon Lex bot to which
    # this association is being made.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotChannelAssociationResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "bot_alias",
                "botAlias",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "bot_configuration",
                "botConfiguration",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ChannelStatus]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the association between the bot and the channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the association between the bot and the channel.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An alias pointing to the specific version of the Amazon Lex bot to which
    # this association is being made.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Amazon Lex bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the association between the bot and the channel was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the messaging platform.
    type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides information that the messaging platform needs to communicate with
    # the Amazon Lex bot.
    bot_configuration: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the bot channel.

    #   * `CREATED` \- The channel has been created and is ready for use.

    #   * `IN_PROGRESS` \- Channel creation is in progress.

    #   * `FAILED` \- There was an error creating the channel. For information about the reason for the failure, see the `failureReason` field.
    status: typing.Union[str, "ChannelStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `status` is `FAILED`, Amazon Lex provides the reason that it failed to
    # create the association.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotChannelAssociationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "bot_alias",
                "botAlias",
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
            (
                "name_contains",
                "nameContains",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon Lex bot in the association.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An alias pointing to the specific version of the Amazon Lex bot to which
    # this association is being made.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for fetching the next page of associations. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of associations, specify the
    # pagination token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of associations to return in the response. The default
    # is 50.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Substring to match in channel association names. An association will be
    # returned if any part of its name matches the substring. For example, "xyz"
    # matches both "xyzabc" and "abcxyz." To return all bot channel associations,
    # use a hyphen ("-") as the `nameContains` parameter.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotChannelAssociationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bot_channel_associations",
                "botChannelAssociations",
                TypeInfo(typing.List[BotChannelAssociation]),
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

    # An array of objects, one for each association, that provides information
    # about the Amazon Lex bot and its association with the channel.
    bot_channel_associations: typing.List["BotChannelAssociation"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # A pagination token that fetches the next page of associations. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of associations, specify the
    # pagination token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetBotChannelAssociationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version_or_alias",
                "versionOrAlias",
                TypeInfo(str),
            ),
        ]

    # The name of the bot. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version or alias of the bot.
    version_or_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[Intent]),
            ),
            (
                "clarification_prompt",
                "clarificationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "abort_statement",
                "abortStatement",
                TypeInfo(Statement),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, Status]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "idle_session_ttl_in_seconds",
                "idleSessionTTLInSeconds",
                TypeInfo(int),
            ),
            (
                "voice_id",
                "voiceId",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
            (
                "child_directed",
                "childDirected",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the bot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `intent` objects. For more information, see PutBot.
    intents: typing.List["Intent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message Amazon Lex uses when it doesn't understand the user's request.
    # For more information, see PutBot.
    clarification_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message that Amazon Lex returns when the user elects to end the
    # conversation without completing it. For more information, see PutBot.
    abort_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the bot. If the bot is ready to run, the status is `READY`.
    # If there was a problem with building the bot, the status is `FAILED` and
    # the `failureReason` explains why the bot did not build. If the bot was
    # saved but not built, the status is `NOT BUILT`.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `status` is `FAILED`, Amazon Lex explains why it failed to build the
    # bot.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the bot was updated. When you create a resource, the creation
    # date and last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum time in seconds that Amazon Lex retains the data gathered in a
    # conversation. For more information, see PutBot.
    idle_session_ttl_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Polly voice ID that Amazon Lex uses for voice interaction with
    # the user. For more information, see PutBot.
    voice_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the bot used to identify a specific revision of the bot's
    # `$LATEST` version.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot. For a new bot, the version is always `$LATEST`.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target locale for the bot.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For each Amazon Lex bot created with the Amazon Lex Model Building Service,
    # you must specify whether your use of Amazon Lex is related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to the Children's Online Privacy
    # Protection Act (COPPA) by specifying `true` or `false` in the
    # `childDirected` field. By specifying `true` in the `childDirected` field,
    # you confirm that your use of Amazon Lex **is** related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to COPPA. By specifying `false`
    # in the `childDirected` field, you confirm that your use of Amazon Lex **is
    # not** related to a website, program, or other application that is directed
    # or targeted, in whole or in part, to children under age 13 and subject to
    # COPPA. You may not specify a default value for the `childDirected` field
    # that does not accurately reflect whether your use of Amazon Lex is related
    # to a website, program, or other application that is directed or targeted,
    # in whole or in part, to children under age 13 and subject to COPPA.

    # If your use of Amazon Lex relates to a website, program, or other
    # application that is directed in whole or in part, to children under age 13,
    # you must obtain any required verifiable parental consent under COPPA. For
    # information regarding the use of Amazon Lex in connection with websites,
    # programs, or other applications that are directed or targeted, in whole or
    # in part, to children under age 13, see the [Amazon Lex
    # FAQ.](https://aws.amazon.com/lex/faqs#data-security)
    child_directed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
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

    # The name of the bot for which versions should be returned.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for fetching the next page of bot versions. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of versions, specify the pagination
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of bot versions to return in the response. The default
    # is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bots",
                "bots",
                TypeInfo(typing.List[BotMetadata]),
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

    # An array of `BotMetadata` objects, one for each numbered version of the bot
    # plus one for the `$LATEST` version.
    bots: typing.List["BotMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token for fetching the next page of bot versions. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of versions, specify the pagination
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetBotVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBotsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "name_contains",
                "nameContains",
                TypeInfo(str),
            ),
        ]

    # A pagination token that fetches the next page of bots. If the response to
    # this call is truncated, Amazon Lex returns a pagination token in the
    # response. To fetch the next page of bots, specify the pagination token in
    # the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of bots to return in the response that the request will
    # return. The default is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Substring to match in bot names. A bot will be returned if any part of its
    # name matches the substring. For example, "xyz" matches both "xyzabc" and
    # "abcxyz."
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBotsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bots",
                "bots",
                TypeInfo(typing.List[BotMetadata]),
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

    # An array of `botMetadata` objects, with one entry for each bot.
    bots: typing.List["BotMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, it includes a pagination token that you can
    # specify in your next request to fetch the next page of bots.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetBotsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBuiltinIntentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "signature",
                "signature",
                TypeInfo(str),
            ),
        ]

    # The unique identifier for a built-in intent. To find the signature for an
    # intent, see [Standard Built-in
    # Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-
    # kit/docs/built-in-intent-ref/standard-intents) in the _Alexa Skills Kit_.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBuiltinIntentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "signature",
                "signature",
                TypeInfo(str),
            ),
            (
                "supported_locales",
                "supportedLocales",
                TypeInfo(typing.List[typing.Union[str, Locale]]),
            ),
            (
                "slots",
                "slots",
                TypeInfo(typing.List[BuiltinIntentSlot]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier for a built-in intent.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of locales that the intent supports.
    supported_locales: typing.List[typing.Union[str, "Locale"]
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # An array of `BuiltinIntentSlot` objects, one entry for each slot type in
    # the intent.
    slots: typing.List["BuiltinIntentSlot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBuiltinIntentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
            (
                "signature_contains",
                "signatureContains",
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

    # A list of locales that the intent supports.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Substring to match in built-in intent signatures. An intent will be
    # returned if any part of its signature matches the substring. For example,
    # "xyz" matches both "xyzabc" and "abcxyz." To find the signature for an
    # intent, see [Standard Built-in
    # Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-
    # kit/docs/built-in-intent-ref/standard-intents) in the _Alexa Skills Kit_.
    signature_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token that fetches the next page of intents. If this API call
    # is truncated, Amazon Lex returns a pagination token in the response. To
    # fetch the next page of intents, use the pagination token in the next
    # request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of intents to return in the response. The default is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBuiltinIntentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[BuiltinIntentMetadata]),
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

    # An array of `builtinIntentMetadata` objects, one for each intent in the
    # response.
    intents: typing.List["BuiltinIntentMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token that fetches the next page of intents. If the response
    # to this API call is truncated, Amazon Lex returns a pagination token in the
    # response. To fetch the next page of intents, specify the pagination token
    # in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetBuiltinIntentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBuiltinSlotTypesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
            (
                "signature_contains",
                "signatureContains",
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

    # A list of locales that the slot type supports.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Substring to match in built-in slot type signatures. A slot type will be
    # returned if any part of its signature matches the substring. For example,
    # "xyz" matches both "xyzabc" and "abcxyz."
    signature_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token that fetches the next page of slot types. If the
    # response to this API call is truncated, Amazon Lex returns a pagination
    # token in the response. To fetch the next page of slot types, specify the
    # pagination token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of slot types to return in the response. The default is
    # 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBuiltinSlotTypesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "slot_types",
                "slotTypes",
                TypeInfo(typing.List[BuiltinSlotTypeMetadata]),
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

    # An array of `BuiltInSlotTypeMetadata` objects, one entry for each slot type
    # returned.
    slot_types: typing.List["BuiltinSlotTypeMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, the response includes a pagination token that
    # you can use in your next request to fetch the next page of slot types.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetBuiltinSlotTypesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetExportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "export_type",
                "exportType",
                TypeInfo(typing.Union[str, ExportType]),
            ),
        ]

    # The name of the bot to export.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot to export.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource to export.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the exported data.
    export_type: typing.Union[str, "ExportType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetExportResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "export_type",
                "exportType",
                TypeInfo(typing.Union[str, ExportType]),
            ),
            (
                "export_status",
                "exportStatus",
                TypeInfo(typing.Union[str, ExportStatus]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
            (
                "url",
                "url",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the bot being exported.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot being exported.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the exported resource.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The format of the exported data.
    export_type: typing.Union[str, "ExportType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the export.

    #   * `IN_PROGRESS` \- The export is in progress.

    #   * `READY` \- The export is complete.

    #   * `FAILED` \- The export could not be completed.
    export_status: typing.Union[str, "ExportStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `status` is `FAILED`, Amazon Lex provides the reason that it failed to
    # export the resource.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An S3 pre-signed URL that provides the location of the exported resource.
    # The exported resource is a ZIP archive that contains the exported resource
    # in JSON format. The structure of the archive may change. Your code should
    # not rely on the archive structure.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetImportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "import_id",
                "importId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the import job information to return.
    import_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetImportResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "merge_strategy",
                "mergeStrategy",
                TypeInfo(typing.Union[str, MergeStrategy]),
            ),
            (
                "import_id",
                "importId",
                TypeInfo(str),
            ),
            (
                "import_status",
                "importStatus",
                TypeInfo(typing.Union[str, ImportStatus]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(typing.List[str]),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name given to the import job.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource imported.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action taken when there was a conflict between an existing resource and
    # a resource in the import file.
    merge_strategy: typing.Union[str, "MergeStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the specific import job.
    import_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the import job. If the status is `FAILED`, you can get the
    # reason for the failure from the `failureReason` field.
    import_status: typing.Union[str, "ImportStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string that describes why an import job failed to complete.
    failure_reason: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp for the date and time that the import job was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetIntentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the intent. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the intent.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntentResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "slots",
                "slots",
                TypeInfo(typing.List[Slot]),
            ),
            (
                "sample_utterances",
                "sampleUtterances",
                TypeInfo(typing.List[str]),
            ),
            (
                "confirmation_prompt",
                "confirmationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "rejection_statement",
                "rejectionStatement",
                TypeInfo(Statement),
            ),
            (
                "follow_up_prompt",
                "followUpPrompt",
                TypeInfo(FollowUpPrompt),
            ),
            (
                "conclusion_statement",
                "conclusionStatement",
                TypeInfo(Statement),
            ),
            (
                "dialog_code_hook",
                "dialogCodeHook",
                TypeInfo(CodeHook),
            ),
            (
                "fulfillment_activity",
                "fulfillmentActivity",
                TypeInfo(FulfillmentActivity),
            ),
            (
                "parent_intent_signature",
                "parentIntentSignature",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the intent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the intent.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of intent slots configured for the intent.
    slots: typing.List["Slot"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of sample utterances configured for the intent.
    sample_utterances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the bot, Amazon Lex uses prompt to confirm the intent before
    # fulfilling the user's request. For more information, see PutIntent.
    confirmation_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the user answers "no" to the question defined in `confirmationPrompt`,
    # Amazon Lex responds with this statement to acknowledge that the intent was
    # canceled.
    rejection_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the bot, Amazon Lex uses this prompt to solicit additional
    # user activity after the intent is fulfilled. For more information, see
    # PutIntent.
    follow_up_prompt: "FollowUpPrompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # After the Lambda function specified in the `fulfillmentActivity` element
    # fulfills the intent, Amazon Lex conveys this statement to the user.
    conclusion_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the bot, Amazon Amazon Lex invokes this Lambda function for
    # each user input. For more information, see PutIntent.
    dialog_code_hook: "CodeHook" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes how the intent is fulfilled. For more information, see PutIntent.
    fulfillment_activity: "FulfillmentActivity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier for a built-in intent.
    parent_intent_signature: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was updated. When you create a resource, the
    # creation date and the last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the intent.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the intent.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntentVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
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

    # The name of the intent for which versions should be returned.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for fetching the next page of intent versions. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of versions, specify the pagination
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of intent versions to return in the response. The
    # default is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntentVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[IntentMetadata]),
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

    # An array of `IntentMetadata` objects, one for each numbered version of the
    # intent plus one for the `$LATEST` version.
    intents: typing.List["IntentMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token for fetching the next page of intent versions. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of versions, specify the pagination
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetIntentVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetIntentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "name_contains",
                "nameContains",
                TypeInfo(str),
            ),
        ]

    # A pagination token that fetches the next page of intents. If the response
    # to this API call is truncated, Amazon Lex returns a pagination token in the
    # response. To fetch the next page of intents, specify the pagination token
    # in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of intents to return in the response. The default is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Substring to match in intent names. An intent will be returned if any part
    # of its name matches the substring. For example, "xyz" matches both "xyzabc"
    # and "abcxyz."
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetIntentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[IntentMetadata]),
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

    # An array of `Intent` objects. For more information, see PutBot.
    intents: typing.List["IntentMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, the response includes a pagination token that
    # you can specify in your next request to fetch the next page of intents.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetIntentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetSlotTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the slot type. The name is case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the slot type.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSlotTypeResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "enumeration_values",
                "enumerationValues",
                TypeInfo(typing.List[EnumerationValue]),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "value_selection_strategy",
                "valueSelectionStrategy",
                TypeInfo(typing.Union[str, SlotValueSelectionStrategy]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the slot type.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the slot type.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `EnumerationValue` objects that defines the values that the slot
    # type can take.
    enumeration_values: typing.List["EnumerationValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was updated. When you create a resource, the
    # creation date and last update date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the slot type.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the `$LATEST` version of the slot type.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The strategy that Amazon Lex uses to determine the value of the slot. For
    # more information, see PutSlotType.
    value_selection_strategy: typing.Union[str, "SlotValueSelectionStrategy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class GetSlotTypeVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
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

    # The name of the slot type for which versions should be returned.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A pagination token for fetching the next page of slot type versions. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of versions, specify the pagination
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of slot type versions to return in the response. The
    # default is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSlotTypeVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "slot_types",
                "slotTypes",
                TypeInfo(typing.List[SlotTypeMetadata]),
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

    # An array of `SlotTypeMetadata` objects, one for each numbered version of
    # the slot type plus one for the `$LATEST` version.
    slot_types: typing.List["SlotTypeMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A pagination token for fetching the next page of slot type versions. If the
    # response to this call is truncated, Amazon Lex returns a pagination token
    # in the response. To fetch the next page of versions, specify the pagination
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["GetSlotTypeVersionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetSlotTypesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "name_contains",
                "nameContains",
                TypeInfo(str),
            ),
        ]

    # A pagination token that fetches the next page of slot types. If the
    # response to this API call is truncated, Amazon Lex returns a pagination
    # token in the response. To fetch next page of slot types, specify the
    # pagination token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of slot types to return in the response. The default is
    # 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Substring to match in slot type names. A slot type will be returned if any
    # part of its name matches the substring. For example, "xyz" matches both
    # "xyzabc" and "abcxyz."
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSlotTypesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "slot_types",
                "slotTypes",
                TypeInfo(typing.List[SlotTypeMetadata]),
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

    # An array of objects, one for each slot type, that provides information such
    # as the name of the slot type, the version, and a description.
    slot_types: typing.List["SlotTypeMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, it includes a pagination token that you can
    # specify in your next request to fetch the next page of slot types.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetSlotTypesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetUtterancesViewRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "bot_versions",
                "botVersions",
                TypeInfo(typing.List[str]),
            ),
            (
                "status_type",
                "statusType",
                TypeInfo(typing.Union[str, StatusType]),
            ),
        ]

    # The name of the bot for which utterance information should be returned.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of bot versions for which utterance information should be
    # returned. The limit is 5 versions per request.
    bot_versions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # To return utterances that were recognized and handled, use`Detected`. To
    # return utterances that were not recognized, use `Missed`.
    status_type: typing.Union[str, "StatusType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetUtterancesViewResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "utterances",
                "utterances",
                TypeInfo(typing.List[UtteranceList]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the bot for which utterance information was returned.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of UtteranceList objects, each containing a list of UtteranceData
    # objects describing the utterances that were processed by your bot. The
    # response contains a maximum of 100 `UtteranceData` objects for each
    # version.
    utterances: typing.List["UtteranceList"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ImportStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


@dataclasses.dataclass
class Intent(ShapeBase):
    """
    Identifies the specific version of an intent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "intent_name",
                "intentName",
                TypeInfo(str),
            ),
            (
                "intent_version",
                "intentVersion",
                TypeInfo(str),
            ),
        ]

    # The name of the intent.
    intent_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the intent.
    intent_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IntentMetadata(ShapeBase):
    """
    Provides information about an intent.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the intent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the intent.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the intent was updated. When you create an intent, the
    # creation date and last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the intent.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    An internal Amazon Lex error occurred. Try your request again.
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
class LimitExceededException(ShapeBase):
    """
    The request exceeded a limit. Try your request again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "retry_after_seconds",
                "retryAfterSeconds",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    retry_after_seconds: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Locale(str):
    en_US = "en-US"
    en_GB = "en-GB"
    de_DE = "de-DE"


class MergeStrategy(str):
    OVERWRITE_LATEST = "OVERWRITE_LATEST"
    FAIL_ON_CONFLICT = "FAIL_ON_CONFLICT"


@dataclasses.dataclass
class Message(ShapeBase):
    """
    The message object that provides the message text and its type.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content_type",
                "contentType",
                TypeInfo(typing.Union[str, ContentType]),
            ),
            (
                "content",
                "content",
                TypeInfo(str),
            ),
            (
                "group_number",
                "groupNumber",
                TypeInfo(int),
            ),
        ]

    # The content type of the message string.
    content_type: typing.Union[str, "ContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The text of the message.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies the message group that the message belongs to. When a group is
    # assigned to a message, Amazon Lex returns one message from each group in
    # the response.
    group_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The resource specified in the request was not found. Check the resource and try
    again.
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
class PreconditionFailedException(ShapeBase):
    """
    The checksum of the resource that you are trying to change does not match the
    checksum in the request. Check the resource's checksum and try again.
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


class ProcessBehavior(str):
    SAVE = "SAVE"
    BUILD = "BUILD"


@dataclasses.dataclass
class Prompt(ShapeBase):
    """
    Obtains information from the user. To define a prompt, provide one or more
    messages and specify the number of attempts to get information from the user. If
    you provide more than one message, Amazon Lex chooses one of the messages to use
    to prompt the user. For more information, see how-it-works.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "messages",
                "messages",
                TypeInfo(typing.List[Message]),
            ),
            (
                "max_attempts",
                "maxAttempts",
                TypeInfo(int),
            ),
            (
                "response_card",
                "responseCard",
                TypeInfo(str),
            ),
        ]

    # An array of objects, each of which provides a message string and its type.
    # You can specify the message string in plain text or in Speech Synthesis
    # Markup Language (SSML).
    messages: typing.List["Message"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of times to prompt the user for information.
    max_attempts: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A response card. Amazon Lex uses this prompt at runtime, in the `PostText`
    # API response. It substitutes session attributes and slot values for
    # placeholders in the response card. For more information, see ex-resp-card.
    response_card: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBotAliasRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "bot_version",
                "botVersion",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    # The name of the alias. The name is _not_ case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot.
    bot_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies a specific revision of the `$LATEST` version.

    # When you create a new bot alias, leave the `checksum` field blank. If you
    # specify a checksum you get a `BadRequestException` exception.

    # When you want to update a bot alias, set the `checksum` field to the
    # checksum of the most recent revision of the `$LATEST` version. If you don't
    # specify the ` checksum` field, or if the checksum does not match the
    # `$LATEST` version, you get a `PreconditionFailedException` exception.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBotAliasResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "bot_version",
                "botVersion",
                TypeInfo(str),
            ),
            (
                "bot_name",
                "botName",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the alias.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the alias.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot that the alias points to.
    bot_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the bot that the alias points to.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the bot alias was updated. When you create a resource, the
    # creation date and the last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot alias was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The checksum for the current version of the alias.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
            (
                "child_directed",
                "childDirected",
                TypeInfo(bool),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[Intent]),
            ),
            (
                "clarification_prompt",
                "clarificationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "abort_statement",
                "abortStatement",
                TypeInfo(Statement),
            ),
            (
                "idle_session_ttl_in_seconds",
                "idleSessionTTLInSeconds",
                TypeInfo(int),
            ),
            (
                "voice_id",
                "voiceId",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "process_behavior",
                "processBehavior",
                TypeInfo(typing.Union[str, ProcessBehavior]),
            ),
            (
                "create_version",
                "createVersion",
                TypeInfo(bool),
            ),
        ]

    # The name of the bot. The name is _not_ case sensitive.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the target locale for the bot. Any intent used in the bot must be
    # compatible with the locale of the bot.

    # The default is `en-US`.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For each Amazon Lex bot created with the Amazon Lex Model Building Service,
    # you must specify whether your use of Amazon Lex is related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to the Children's Online Privacy
    # Protection Act (COPPA) by specifying `true` or `false` in the
    # `childDirected` field. By specifying `true` in the `childDirected` field,
    # you confirm that your use of Amazon Lex **is** related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to COPPA. By specifying `false`
    # in the `childDirected` field, you confirm that your use of Amazon Lex **is
    # not** related to a website, program, or other application that is directed
    # or targeted, in whole or in part, to children under age 13 and subject to
    # COPPA. You may not specify a default value for the `childDirected` field
    # that does not accurately reflect whether your use of Amazon Lex is related
    # to a website, program, or other application that is directed or targeted,
    # in whole or in part, to children under age 13 and subject to COPPA.

    # If your use of Amazon Lex relates to a website, program, or other
    # application that is directed in whole or in part, to children under age 13,
    # you must obtain any required verifiable parental consent under COPPA. For
    # information regarding the use of Amazon Lex in connection with websites,
    # programs, or other applications that are directed or targeted, in whole or
    # in part, to children under age 13, see the [Amazon Lex
    # FAQ.](https://aws.amazon.com/lex/faqs#data-security)
    child_directed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `Intent` objects. Each intent represents a command that a user
    # can express. For example, a pizza ordering bot might support an OrderPizza
    # intent. For more information, see how-it-works.
    intents: typing.List["Intent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When Amazon Lex doesn't understand the user's intent, it uses this message
    # to get clarification. To specify how many times Amazon Lex should repeate
    # the clarification prompt, use the `maxAttempts` field. If Amazon Lex still
    # doesn't understand, it sends the message in the `abortStatement` field.

    # When you create a clarification prompt, make sure that it suggests the
    # correct response from the user. for example, for a bot that orders pizza
    # and drinks, you might create this clarification prompt: "What would you
    # like to do? You can say 'Order a pizza' or 'Order a drink.'"
    clarification_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When Amazon Lex can't understand the user's input in context, it tries to
    # elicit the information a few times. After that, Amazon Lex sends the
    # message defined in `abortStatement` to the user, and then aborts the
    # conversation. To set the number of retries, use the
    # `valueElicitationPrompt` field for the slot type.

    # For example, in a pizza ordering bot, Amazon Lex might ask a user "What
    # type of crust would you like?" If the user's response is not one of the
    # expected responses (for example, "thin crust, "deep dish," etc.), Amazon
    # Lex tries to elicit a correct response a few more times.

    # For example, in a pizza ordering application, `OrderPizza` might be one of
    # the intents. This intent might require the `CrustType` slot. You specify
    # the `valueElicitationPrompt` field when you create the `CrustType` slot.
    abort_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum time in seconds that Amazon Lex retains the data gathered in a
    # conversation.

    # A user interaction session remains active for the amount of time specified.
    # If no conversation occurs during this time, the session expires and Amazon
    # Lex deletes any data provided before the timeout.

    # For example, suppose that a user chooses the OrderPizza intent, but gets
    # sidetracked halfway through placing an order. If the user doesn't complete
    # the order within the specified time, Amazon Lex discards the slot
    # information that it gathered, and the user must start over.

    # If you don't include the `idleSessionTTLInSeconds` element in a `PutBot`
    # operation request, Amazon Lex uses the default value. This is also true if
    # the request replaces an existing bot.

    # The default is 300 seconds (5 minutes).
    idle_session_ttl_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Polly voice ID that you want Amazon Lex to use for voice
    # interactions with the user. The locale configured for the voice must match
    # the locale of the bot. For more information, see [Available
    # Voices](http://docs.aws.amazon.com/polly/latest/dg/voicelist.html) in the
    # _Amazon Polly Developer Guide_.
    voice_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies a specific revision of the `$LATEST` version.

    # When you create a new bot, leave the `checksum` field blank. If you specify
    # a checksum you get a `BadRequestException` exception.

    # When you want to update a bot, set the `checksum` field to the checksum of
    # the most recent revision of the `$LATEST` version. If you don't specify the
    # ` checksum` field, or if the checksum does not match the `$LATEST` version,
    # you get a `PreconditionFailedException` exception.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you set the `processBehavior` element to `BUILD`, Amazon Lex builds the
    # bot so that it can be run. If you set the element to `SAVE` Amazon Lex
    # saves the bot, but doesn't build it.

    # If you don't specify this value, the default value is `BUILD`.
    process_behavior: typing.Union[str, "ProcessBehavior"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    create_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutBotResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "intents",
                "intents",
                TypeInfo(typing.List[Intent]),
            ),
            (
                "clarification_prompt",
                "clarificationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "abort_statement",
                "abortStatement",
                TypeInfo(Statement),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, Status]),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "idle_session_ttl_in_seconds",
                "idleSessionTTLInSeconds",
                TypeInfo(int),
            ),
            (
                "voice_id",
                "voiceId",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "locale",
                "locale",
                TypeInfo(typing.Union[str, Locale]),
            ),
            (
                "child_directed",
                "childDirected",
                TypeInfo(bool),
            ),
            (
                "create_version",
                "createVersion",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the bot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the bot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `Intent` objects. For more information, see PutBot.
    intents: typing.List["Intent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The prompts that Amazon Lex uses when it doesn't understand the user's
    # intent. For more information, see PutBot.
    clarification_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message that Amazon Lex uses to abort a conversation. For more
    # information, see PutBot.
    abort_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When you send a request to create a bot with `processBehavior` set to
    # `BUILD`, Amazon Lex sets the `status` response element to `BUILDING`. After
    # Amazon Lex builds the bot, it sets `status` to `READY`. If Amazon Lex can't
    # build the bot, Amazon Lex sets `status` to `FAILED`. Amazon Lex returns the
    # reason for the failure in the `failureReason` response element.

    # When you set `processBehavior`to `SAVE`, Amazon Lex sets the status code to
    # `NOT BUILT`.
    status: typing.Union[str, "Status"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If `status` is `FAILED`, Amazon Lex provides the reason that it failed to
    # build the bot.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the bot was updated. When you create a resource, the creation
    # date and last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the bot was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum length of time that Amazon Lex retains the data gathered in a
    # conversation. For more information, see PutBot.
    idle_session_ttl_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Polly voice ID that Amazon Lex uses for voice interaction with
    # the user. For more information, see PutBot.
    voice_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the bot that you created.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the bot. For a new bot, the version is always `$LATEST`.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target locale for the bot.
    locale: typing.Union[str, "Locale"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For each Amazon Lex bot created with the Amazon Lex Model Building Service,
    # you must specify whether your use of Amazon Lex is related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to the Children's Online Privacy
    # Protection Act (COPPA) by specifying `true` or `false` in the
    # `childDirected` field. By specifying `true` in the `childDirected` field,
    # you confirm that your use of Amazon Lex **is** related to a website,
    # program, or other application that is directed or targeted, in whole or in
    # part, to children under age 13 and subject to COPPA. By specifying `false`
    # in the `childDirected` field, you confirm that your use of Amazon Lex **is
    # not** related to a website, program, or other application that is directed
    # or targeted, in whole or in part, to children under age 13 and subject to
    # COPPA. You may not specify a default value for the `childDirected` field
    # that does not accurately reflect whether your use of Amazon Lex is related
    # to a website, program, or other application that is directed or targeted,
    # in whole or in part, to children under age 13 and subject to COPPA.

    # If your use of Amazon Lex relates to a website, program, or other
    # application that is directed in whole or in part, to children under age 13,
    # you must obtain any required verifiable parental consent under COPPA. For
    # information regarding the use of Amazon Lex in connection with websites,
    # programs, or other applications that are directed or targeted, in whole or
    # in part, to children under age 13, see the [Amazon Lex
    # FAQ.](https://aws.amazon.com/lex/faqs#data-security)
    child_directed: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
    create_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutIntentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "slots",
                "slots",
                TypeInfo(typing.List[Slot]),
            ),
            (
                "sample_utterances",
                "sampleUtterances",
                TypeInfo(typing.List[str]),
            ),
            (
                "confirmation_prompt",
                "confirmationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "rejection_statement",
                "rejectionStatement",
                TypeInfo(Statement),
            ),
            (
                "follow_up_prompt",
                "followUpPrompt",
                TypeInfo(FollowUpPrompt),
            ),
            (
                "conclusion_statement",
                "conclusionStatement",
                TypeInfo(Statement),
            ),
            (
                "dialog_code_hook",
                "dialogCodeHook",
                TypeInfo(CodeHook),
            ),
            (
                "fulfillment_activity",
                "fulfillmentActivity",
                TypeInfo(FulfillmentActivity),
            ),
            (
                "parent_intent_signature",
                "parentIntentSignature",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "create_version",
                "createVersion",
                TypeInfo(bool),
            ),
        ]

    # The name of the intent. The name is _not_ case sensitive.

    # The name can't match a built-in intent name, or a built-in intent name with
    # "AMAZON." removed. For example, because there is a built-in intent called
    # `AMAZON.HelpIntent`, you can't create a custom intent called `HelpIntent`.

    # For a list of built-in intents, see [Standard Built-in
    # Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-
    # kit/docs/built-in-intent-ref/standard-intents) in the _Alexa Skills Kit_.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the intent.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of intent slots. At runtime, Amazon Lex elicits required slot
    # values from the user using prompts defined in the slots. For more
    # information, see how-it-works.
    slots: typing.List["Slot"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of utterances (strings) that a user might say to signal the
    # intent. For example, "I want {PizzaSize} pizza", "Order {Quantity}
    # {PizzaSize} pizzas".

    # In each utterance, a slot name is enclosed in curly braces.
    sample_utterances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Prompts the user to confirm the intent. This question should have a yes or
    # no answer.

    # Amazon Lex uses this prompt to ensure that the user acknowledges that the
    # intent is ready for fulfillment. For example, with the `OrderPizza` intent,
    # you might want to confirm that the order is correct before placing it. For
    # other intents, such as intents that simply respond to user questions, you
    # might not need to ask the user for confirmation before providing the
    # information.

    # You you must provide both the `rejectionStatement` and the
    # `confirmationPrompt`, or neither.
    confirmation_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the user answers "no" to the question defined in `confirmationPrompt`,
    # Amazon Lex responds with this statement to acknowledge that the intent was
    # canceled.

    # You must provide both the `rejectionStatement` and the
    # `confirmationPrompt`, or neither.
    rejection_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Lex uses this prompt to solicit additional activity after fulfilling
    # an intent. For example, after the `OrderPizza` intent is fulfilled, you
    # might prompt the user to order a drink.

    # The action that Amazon Lex takes depends on the user's response, as
    # follows:

    #   * If the user says "Yes" it responds with the clarification prompt that is configured for the bot.

    #   * if the user says "Yes" and continues with an utterance that triggers an intent it starts a conversation for the intent.

    #   * If the user says "No" it responds with the rejection statement configured for the the follow-up prompt.

    #   * If it doesn't recognize the utterance it repeats the follow-up prompt again.

    # The `followUpPrompt` field and the `conclusionStatement` field are mutually
    # exclusive. You can specify only one.
    follow_up_prompt: "FollowUpPrompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The statement that you want Amazon Lex to convey to the user after the
    # intent is successfully fulfilled by the Lambda function.

    # This element is relevant only if you provide a Lambda function in the
    # `fulfillmentActivity`. If you return the intent to the client application,
    # you can't specify this element.

    # The `followUpPrompt` and `conclusionStatement` are mutually exclusive. You
    # can specify only one.
    conclusion_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a Lambda function to invoke for each user input. You can invoke
    # this Lambda function to personalize user interaction.

    # For example, suppose your bot determines that the user is John. Your Lambda
    # function might retrieve John's information from a backend database and
    # prepopulate some of the values. For example, if you find that John is
    # gluten intolerant, you might set the corresponding intent slot,
    # `GlutenIntolerant`, to true. You might find John's phone number and set the
    # corresponding session attribute.
    dialog_code_hook: "CodeHook" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required. Describes how the intent is fulfilled. For example, after a user
    # provides all of the information for a pizza order, `fulfillmentActivity`
    # defines how the bot places an order with a local pizza store.

    # You might configure Amazon Lex to return all of the intent information to
    # the client application, or direct it to invoke a Lambda function that can
    # process the intent (for example, place an order with a pizzeria).
    fulfillment_activity: "FulfillmentActivity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier for the built-in intent to base this intent on. To find
    # the signature for an intent, see [Standard Built-in
    # Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-
    # kit/docs/built-in-intent-ref/standard-intents) in the _Alexa Skills Kit_.
    parent_intent_signature: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies a specific revision of the `$LATEST` version.

    # When you create a new intent, leave the `checksum` field blank. If you
    # specify a checksum you get a `BadRequestException` exception.

    # When you want to update a intent, set the `checksum` field to the checksum
    # of the most recent revision of the `$LATEST` version. If you don't specify
    # the ` checksum` field, or if the checksum does not match the `$LATEST`
    # version, you get a `PreconditionFailedException` exception.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    create_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutIntentResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "slots",
                "slots",
                TypeInfo(typing.List[Slot]),
            ),
            (
                "sample_utterances",
                "sampleUtterances",
                TypeInfo(typing.List[str]),
            ),
            (
                "confirmation_prompt",
                "confirmationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "rejection_statement",
                "rejectionStatement",
                TypeInfo(Statement),
            ),
            (
                "follow_up_prompt",
                "followUpPrompt",
                TypeInfo(FollowUpPrompt),
            ),
            (
                "conclusion_statement",
                "conclusionStatement",
                TypeInfo(Statement),
            ),
            (
                "dialog_code_hook",
                "dialogCodeHook",
                TypeInfo(CodeHook),
            ),
            (
                "fulfillment_activity",
                "fulfillmentActivity",
                TypeInfo(FulfillmentActivity),
            ),
            (
                "parent_intent_signature",
                "parentIntentSignature",
                TypeInfo(str),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "create_version",
                "createVersion",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the intent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the intent.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of intent slots that are configured for the intent.
    slots: typing.List["Slot"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of sample utterances that are configured for the intent.
    sample_utterances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the intent, Amazon Lex prompts the user to confirm the intent
    # before fulfilling it.
    confirmation_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the user answers "no" to the question defined in `confirmationPrompt`
    # Amazon Lex responds with this statement to acknowledge that the intent was
    # canceled.
    rejection_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the intent, Amazon Lex uses this prompt to solicit additional
    # user activity after the intent is fulfilled.
    follow_up_prompt: "FollowUpPrompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # After the Lambda function specified in the`fulfillmentActivity`intent
    # fulfills the intent, Amazon Lex conveys this statement to the user.
    conclusion_statement: "Statement" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the intent, Amazon Lex invokes this Lambda function for each
    # user input.
    dialog_code_hook: "CodeHook" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If defined in the intent, Amazon Lex invokes this Lambda function to
    # fulfill the intent after the user provides all of the information required
    # by the intent.
    fulfillment_activity: "FulfillmentActivity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier for the built-in intent that this intent is based on.
    parent_intent_signature: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was updated. When you create a resource, the
    # creation date and last update dates are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the intent was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the intent. For a new intent, the version is always
    # `$LATEST`.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the `$LATEST`version of the intent created or updated.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    create_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSlotTypeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "enumeration_values",
                "enumerationValues",
                TypeInfo(typing.List[EnumerationValue]),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "value_selection_strategy",
                "valueSelectionStrategy",
                TypeInfo(typing.Union[str, SlotValueSelectionStrategy]),
            ),
            (
                "create_version",
                "createVersion",
                TypeInfo(bool),
            ),
        ]

    # The name of the slot type. The name is _not_ case sensitive.

    # The name can't match a built-in slot type name, or a built-in slot type
    # name with "AMAZON." removed. For example, because there is a built-in slot
    # type called `AMAZON.DATE`, you can't create a custom slot type called
    # `DATE`.

    # For a list of built-in slot types, see [Slot Type
    # Reference](https://developer.amazon.com/public/solutions/alexa/alexa-
    # skills-kit/docs/built-in-intent-ref/slot-type-reference) in the _Alexa
    # Skills Kit_.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the slot type.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `EnumerationValue` objects that defines the values that the slot
    # type can take. Each value can have a list of `synonyms`, which are
    # additional values that help train the machine learning model about the
    # values that it resolves for a slot.

    # When Amazon Lex resolves a slot value, it generates a resolution list that
    # contains up to five possible values for the slot. If you are using a Lambda
    # function, this resolution list is passed to the function. If you are not
    # using a Lambda function you can choose to return the value that the user
    # entered or the first value in the resolution list as the slot value. The
    # `valueSelectionStrategy` field indicates the option to use.
    enumeration_values: typing.List["EnumerationValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies a specific revision of the `$LATEST` version.

    # When you create a new slot type, leave the `checksum` field blank. If you
    # specify a checksum you get a `BadRequestException` exception.

    # When you want to update a slot type, set the `checksum` field to the
    # checksum of the most recent revision of the `$LATEST` version. If you don't
    # specify the ` checksum` field, or if the checksum does not match the
    # `$LATEST` version, you get a `PreconditionFailedException` exception.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines the slot resolution strategy that Amazon Lex uses to return slot
    # type values. The field can be set to one of the following values:

    #   * `ORIGINAL_VALUE` \- Returns the value entered by the user, if the user value is similar to the slot value.

    #   * `TOP_RESOLUTION` \- If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

    # If you don't specify the `valueSelectionStrategy`, the default is
    # `ORIGINAL_VALUE`.
    value_selection_strategy: typing.Union[str, "SlotValueSelectionStrategy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )
    create_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSlotTypeResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "enumeration_values",
                "enumerationValues",
                TypeInfo(typing.List[EnumerationValue]),
            ),
            (
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "checksum",
                "checksum",
                TypeInfo(str),
            ),
            (
                "value_selection_strategy",
                "valueSelectionStrategy",
                TypeInfo(typing.Union[str, SlotValueSelectionStrategy]),
            ),
            (
                "create_version",
                "createVersion",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the slot type.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the slot type.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `EnumerationValue` objects that defines the values that the slot
    # type can take.
    enumeration_values: typing.List["EnumerationValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was updated. When you create a slot type, the
    # creation date and last update date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the slot type. For a new slot type, the version is always
    # `$LATEST`.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Checksum of the `$LATEST` version of the slot type.
    checksum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The slot resolution strategy that Amazon Lex uses to determine the value of
    # the slot. For more information, see PutSlotType.
    value_selection_strategy: typing.Union[str, "SlotValueSelectionStrategy"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )
    create_version: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class ReferenceType(str):
    Intent = "Intent"
    Bot = "Bot"
    BotAlias = "BotAlias"
    BotChannel = "BotChannel"


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The resource that you are attempting to delete is referred to by another
    resource. Use this information to remove references to the resource that you are
    trying to delete.

    The body of the exception contains a JSON object that describes the resource.

    `{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,`

    `"resourceReference": {`

    `"name": _string_ , "version": _string_ } }`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reference_type",
                "referenceType",
                TypeInfo(typing.Union[str, ReferenceType]),
            ),
            (
                "example_reference",
                "exampleReference",
                TypeInfo(ResourceReference),
            ),
        ]

    reference_type: typing.Union[str, "ReferenceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the resource that refers to the resource that you are attempting
    # to delete. This object is returned as part of the `ResourceInUseException`
    # exception.
    example_reference: "ResourceReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceReference(ShapeBase):
    """
    Describes the resource that refers to the resource that you are attempting to
    delete. This object is returned as part of the `ResourceInUseException`
    exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the resource that is using the resource that you are trying to
    # delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the resource that is using the resource that you are trying
    # to delete.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ResourceType(str):
    BOT = "BOT"
    INTENT = "INTENT"
    SLOT_TYPE = "SLOT_TYPE"


@dataclasses.dataclass
class Slot(ShapeBase):
    """
    Identifies the version of a specific slot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "slot_constraint",
                "slotConstraint",
                TypeInfo(typing.Union[str, SlotConstraint]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "slot_type",
                "slotType",
                TypeInfo(str),
            ),
            (
                "slot_type_version",
                "slotTypeVersion",
                TypeInfo(str),
            ),
            (
                "value_elicitation_prompt",
                "valueElicitationPrompt",
                TypeInfo(Prompt),
            ),
            (
                "priority",
                "priority",
                TypeInfo(int),
            ),
            (
                "sample_utterances",
                "sampleUtterances",
                TypeInfo(typing.List[str]),
            ),
            (
                "response_card",
                "responseCard",
                TypeInfo(str),
            ),
        ]

    # The name of the slot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the slot is required or optional.
    slot_constraint: typing.Union[str, "SlotConstraint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the slot.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the slot, either a custom slot type that you defined or one of
    # the built-in slot types.
    slot_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the slot type.
    slot_type_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prompt that Amazon Lex uses to elicit the slot value from the user.
    value_elicitation_prompt: "Prompt" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Directs Lex the order in which to elicit this slot value from the user. For
    # example, if the intent has two slots with priorities 1 and 2, AWS Lex first
    # elicits a value for the slot with priority 1.

    # If multiple slots share the same priority, the order in which Lex elicits
    # values is arbitrary.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you know a specific pattern with which users might respond to an Amazon
    # Lex request for a slot value, you can provide those utterances to improve
    # accuracy. This is optional. In most cases, Amazon Lex is capable of
    # understanding user utterances.
    sample_utterances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of possible responses for the slot type used by text-based clients. A
    # user chooses an option from the response card, instead of using text to
    # reply.
    response_card: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SlotConstraint(str):
    Required = "Required"
    Optional = "Optional"


@dataclasses.dataclass
class SlotTypeMetadata(ShapeBase):
    """
    Provides information about a slot type..
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "last_updated_date",
                "lastUpdatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The name of the slot type.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the slot type.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the slot type was updated. When you create a resource, the
    # creation date and last updated date are the same.
    last_updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the slot type was created.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the slot type.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SlotValueSelectionStrategy(str):
    ORIGINAL_VALUE = "ORIGINAL_VALUE"
    TOP_RESOLUTION = "TOP_RESOLUTION"


@dataclasses.dataclass
class StartImportRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "payload",
                "payload",
                TypeInfo(typing.Any),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "merge_strategy",
                "mergeStrategy",
                TypeInfo(typing.Union[str, MergeStrategy]),
            ),
        ]

    # A zip archive in binary format. The archive should contain one file, a JSON
    # file containing the resource to import. The resource should match the type
    # specified in the `resourceType` field.
    payload: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the type of resource to export. Each resource also exports any
    # resources that it depends on.

    #   * A bot exports dependent intents.

    #   * An intent exports dependent slot types.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the action that the `StartImport` operation should take when
    # there is an existing resource with the same name.

    #   * FAIL_ON_CONFLICT - The import operation is stopped on the first conflict between a resource in the import file and an existing resource. The name of the resource causing the conflict is in the `failureReason` field of the response to the `GetImport` operation.

    # OVERWRITE_LATEST - The import operation proceeds even if there is a
    # conflict with an existing resource. The $LASTEST version of the existing
    # resource is overwritten with the data from the import file.
    merge_strategy: typing.Union[str, "MergeStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartImportResponse(OutputShapeBase):
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
                "name",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "merge_strategy",
                "mergeStrategy",
                TypeInfo(typing.Union[str, MergeStrategy]),
            ),
            (
                "import_id",
                "importId",
                TypeInfo(str),
            ),
            (
                "import_status",
                "importStatus",
                TypeInfo(typing.Union[str, ImportStatus]),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name given to the import job.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of resource to import.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action to take when there is a merge conflict.
    merge_strategy: typing.Union[str, "MergeStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the specific import job.
    import_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the import job. If the status is `FAILED`, you can get the
    # reason for the failure using the `GetImport` operation.
    import_status: typing.Union[str, "ImportStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp for the date and time that the import job was requested.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Statement(ShapeBase):
    """
    A collection of messages that convey information to the user. At runtime, Amazon
    Lex selects the message to convey.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "messages",
                "messages",
                TypeInfo(typing.List[Message]),
            ),
            (
                "response_card",
                "responseCard",
                TypeInfo(str),
            ),
        ]

    # A collection of message objects.
    messages: typing.List["Message"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # At runtime, if the client is using the
    # [PostText](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html)
    # API, Amazon Lex includes the response card in the response. It substitutes
    # all of the session attributes and slot values for placeholders in the
    # response card.
    response_card: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Status(str):
    BUILDING = "BUILDING"
    READY = "READY"
    READY_BASIC_TESTING = "READY_BASIC_TESTING"
    FAILED = "FAILED"
    NOT_BUILT = "NOT_BUILT"


class StatusType(str):
    Detected = "Detected"
    Missed = "Missed"


@dataclasses.dataclass
class UtteranceData(ShapeBase):
    """
    Provides information about a single utterance that was made to your bot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "utterance_string",
                "utteranceString",
                TypeInfo(str),
            ),
            (
                "count",
                "count",
                TypeInfo(int),
            ),
            (
                "distinct_users",
                "distinctUsers",
                TypeInfo(int),
            ),
            (
                "first_uttered_date",
                "firstUtteredDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_uttered_date",
                "lastUtteredDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The text that was entered by the user or the text representation of an
    # audio clip.
    utterance_string: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of times that the utterance was processed.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of individuals that used the utterance.
    distinct_users: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the utterance was first recorded.
    first_uttered_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the utterance was last recorded.
    last_uttered_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UtteranceList(ShapeBase):
    """
    Provides a list of utterances that have been made to a specific version of your
    bot. The list contains a maximum of 100 utterances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bot_version",
                "botVersion",
                TypeInfo(str),
            ),
            (
                "utterances",
                "utterances",
                TypeInfo(typing.List[UtteranceData]),
            ),
        ]

    # The version of the bot that processed the list.
    bot_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more UtteranceData objects that contain information about the
    # utterances that have been made to a bot. The maximum number of object is
    # 100.
    utterances: typing.List["UtteranceData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
