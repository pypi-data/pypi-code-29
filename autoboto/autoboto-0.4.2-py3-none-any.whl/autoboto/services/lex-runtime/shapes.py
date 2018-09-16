import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class BadGatewayException(ShapeBase):
    """
    Either the Amazon Lex bot is still building, or one of the dependent services
    (Amazon Polly, AWS Lambda) failed with an internal service error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    Request validation failed, there is no usable message in the context, or the bot
    build failed, is still in progress, or contains unbuilt changes.
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


class BlobStream(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class Button(ShapeBase):
    """
    Represents an option to be shown on the client platform (Facebook, Slack, etc.)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "text",
                "text",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # Text that is visible to the user on the button.
    text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value sent to Amazon Lex when a user chooses the button. For example,
    # consider button text "NYC." When the user chooses the button, the value
    # sent can be "New York City."
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    Two clients are using the same AWS account, Amazon Lex bot, and user ID.
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
    application_vnd_amazonaws_card_generic = "application/vnd.amazonaws.card.generic"


@dataclasses.dataclass
class DependencyFailedException(ShapeBase):
    """
    One of the dependencies, such as AWS Lambda or Amazon Polly, threw an exception.
    For example,

      * If Amazon Lex does not have sufficient permissions to call a Lambda function.

      * If a Lambda function takes longer than 30 seconds to execute.

      * If a fulfillment Lambda function returns a `Delegate` dialog action without removing any slot values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DialogState(str):
    ElicitIntent = "ElicitIntent"
    ConfirmIntent = "ConfirmIntent"
    ElicitSlot = "ElicitSlot"
    Fulfilled = "Fulfilled"
    ReadyForFulfillment = "ReadyForFulfillment"
    Failed = "Failed"


@dataclasses.dataclass
class GenericAttachment(ShapeBase):
    """
    Represents an option rendered to the user when a prompt is shown. It could be an
    image, a button, a link, or text.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "title",
                "title",
                TypeInfo(str),
            ),
            (
                "sub_title",
                "subTitle",
                TypeInfo(str),
            ),
            (
                "attachment_link_url",
                "attachmentLinkUrl",
                TypeInfo(str),
            ),
            (
                "image_url",
                "imageUrl",
                TypeInfo(str),
            ),
            (
                "buttons",
                "buttons",
                TypeInfo(typing.List[Button]),
            ),
        ]

    # The title of the option.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subtitle shown below the title.
    sub_title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of an attachment to the response card.
    attachment_link_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of an image that is displayed to the user.
    image_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of options to show to the user.
    buttons: typing.List["Button"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """
    Internal service error. Retry the call.
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
    Exceeded a limit.
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


@dataclasses.dataclass
class LoopDetectedException(ShapeBase):
    """
    This exception is not used.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MessageFormatType(str):
    PlainText = "PlainText"
    CustomPayload = "CustomPayload"
    SSML = "SSML"
    Composite = "Composite"


@dataclasses.dataclass
class NotAcceptableException(ShapeBase):
    """
    The accept header in the request does not have a valid value.
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
class NotFoundException(ShapeBase):
    """
    The resource (such as the Amazon Lex bot or an alias) that is referred to is not
    found.
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
class PostContentRequest(ShapeBase):
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
                "user_id",
                "userId",
                TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "input_stream",
                "inputStream",
                TypeInfo(typing.Any),
            ),
            (
                "session_attributes",
                "sessionAttributes",
                TypeInfo(str),
            ),
            (
                "request_attributes",
                "requestAttributes",
                TypeInfo(str),
            ),
            (
                "accept",
                "accept",
                TypeInfo(str),
            ),
        ]

    # Name of the Amazon Lex bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Alias of the Amazon Lex bot.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the client application user. Amazon Lex uses this to identify a
    # user's conversation with your bot. At runtime, each request must contain
    # the `userID` field.

    # To decide the user ID to use for your application, consider the following
    # factors.

    #   * The `userID` field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.

    #   * If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.

    #   * If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.

    #   * A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You pass this value as the `Content-Type` HTTP header.

    # Indicates the audio format or text. The header value must start with one of
    # the following prefixes:

    #   * PCM format, audio data must be in little-endian byte order.

    #     * audio/l16; rate=16000; channels=1

    #     * audio/x-l16; sample-rate=16000; channel-count=1

    #     * audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false

    #   * Opus format

    #     * audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=256000; frame-size-milliseconds=4

    #   * Text format

    #     * text/plain; charset=utf-8
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User input in PCM or Opus audio format or text format as described in the
    # `Content-Type` HTTP header.

    # You can stream audio data to Amazon Lex or you can create a local buffer
    # that captures all of the audio data before sending. In general, you get
    # better performance if you stream audio data rather than buffering the data
    # locally.
    input_stream: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You pass this value as the `x-amz-lex-session-attributes` HTTP header.

    # Application-specific information passed between Amazon Lex and a client
    # application. The value must be a JSON serialized and base64 encoded map
    # with string keys and values. The total size of the `sessionAttributes` and
    # `requestAttributes` headers is limited to 12 KB.

    # For more information, see [Setting Session
    # Attributes](http://docs.aws.amazon.com/lex/latest/dg/context-
    # mgmt.html#context-mgmt-session-attribs).
    session_attributes: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You pass this value as the `x-amz-lex-request-attributes` HTTP header.

    # Request-specific information passed between Amazon Lex and a client
    # application. The value must be a JSON serialized and base64 encoded map
    # with string keys and values. The total size of the `requestAttributes` and
    # `sessionAttributes` headers is limited to 12 KB.

    # The namespace `x-amz-lex:` is reserved for special attributes. Don't create
    # any request attributes with the prefix `x-amz-lex:`.

    # For more information, see [Setting Request
    # Attributes](http://docs.aws.amazon.com/lex/latest/dg/context-
    # mgmt.html#context-mgmt-request-attribs).
    request_attributes: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You pass this value as the `Accept` HTTP header.

    # The message Amazon Lex returns in the response can be either text or speech
    # based on the `Accept` HTTP header value in the request.

    #   * If the value is `text/plain; charset=utf-8`, Amazon Lex returns text in the response.

    #   * If the value begins with `audio/`, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the `Accept` header). For example, if you specify `audio/mpeg` as the value, Amazon Lex returns speech in the MPEG format.

    # The following are the accepted values:

    #     * audio/mpeg

    #     * audio/ogg

    #     * audio/pcm

    #     * text/plain; charset=utf-8

    #     * audio/* (defaults to mpeg)
    accept: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostContentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "intent_name",
                "intentName",
                TypeInfo(str),
            ),
            (
                "slots",
                "slots",
                TypeInfo(str),
            ),
            (
                "session_attributes",
                "sessionAttributes",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "message_format",
                "messageFormat",
                TypeInfo(typing.Union[str, MessageFormatType]),
            ),
            (
                "dialog_state",
                "dialogState",
                TypeInfo(typing.Union[str, DialogState]),
            ),
            (
                "slot_to_elicit",
                "slotToElicit",
                TypeInfo(str),
            ),
            (
                "input_transcript",
                "inputTranscript",
                TypeInfo(str),
            ),
            (
                "audio_stream",
                "audioStream",
                TypeInfo(typing.Any),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Content type as specified in the `Accept` HTTP header in the request.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current user intent that Amazon Lex is aware of.
    intent_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Map of zero or more intent slots (name/value pairs) Amazon Lex detected
    # from the user input during the conversation.

    # Amazon Lex creates a resolution list containing likely values for a slot.
    # The value that it returns is determined by the `valueSelectionStrategy`
    # selected when the slot type was created or updated. If
    # `valueSelectionStrategy` is set to `ORIGINAL_VALUE`, the value provided by
    # the user is returned, if the user value is similar to the slot values. If
    # `valueSelectionStrategy` is set to `TOP_RESOLUTION` Amazon Lex returns the
    # first value in the resolution list or, if there is no resolution list,
    # null. If you don't specify a `valueSelectionStrategy`, the default is
    # `ORIGINAL_VALUE`.
    slots: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Map of key/value pairs representing the session-specific context
    # information.
    session_attributes: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message to convey to the user. The message can come from the bot's
    # configuration or from a Lambda function.

    # If the intent is not configured with a Lambda function, or if the Lambda
    # function returned `Delegate` as the `dialogAction.type` its response,
    # Amazon Lex decides on the next course of action and selects an appropriate
    # message from the bot's configuration based on the current interaction
    # context. For example, if Amazon Lex isn't able to understand user input, it
    # uses a clarification prompt message.

    # When you create an intent you can assign messages to groups. When messages
    # are assigned to groups Amazon Lex returns one message from each group in
    # the response. The message field is an escaped JSON string containing the
    # messages. For more information about the structure of the JSON string
    # returned, see msg-prompts-formats.

    # If the Lambda function returns a message, Amazon Lex passes it to the
    # client in its response.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the response message. One of the following values:

    #   * `PlainText` \- The message contains plain UTF-8 text.

    #   * `CustomPayload` \- The message is a custom format for the client.

    #   * `SSML` \- The message contains text formatted for voice output.

    #   * `Composite` \- The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.
    message_format: typing.Union[str, "MessageFormatType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the current state of the user interaction. Amazon Lex returns
    # one of the following values as `dialogState`. The client can optionally use
    # this information to customize the user interface.

    #   * `ElicitIntent` \- Amazon Lex wants to elicit the user's intent. Consider the following examples:

    # For example, a user might utter an intent ("I want to order a pizza"). If
    # Amazon Lex cannot infer the user intent from this utterance, it will return
    # this dialog state.

    #   * `ConfirmIntent` \- Amazon Lex is expecting a "yes" or "no" response.

    # For example, Amazon Lex wants user confirmation before fulfilling an
    # intent. Instead of a simple "yes" or "no" response, a user might respond
    # with additional information. For example, "yes, but make it a thick crust
    # pizza" or "no, I want to order a drink." Amazon Lex can process such
    # additional information (in these examples, update the crust type slot or
    # change the intent from OrderPizza to OrderDrink).

    #   * `ElicitSlot` \- Amazon Lex is expecting the value of a slot for the current intent.

    # For example, suppose that in the response Amazon Lex sends this message:
    # "What size pizza would you like?". A user might reply with the slot value
    # (e.g., "medium"). The user might also provide additional information in the
    # response (e.g., "medium thick crust pizza"). Amazon Lex can process such
    # additional information appropriately.

    #   * `Fulfilled` \- Conveys that the Lambda function has successfully fulfilled the intent.

    #   * `ReadyForFulfillment` \- Conveys that the client has to fulfill the request.

    #   * `Failed` \- Conveys that the conversation with the user failed.

    # This can happen for various reasons, including that the user does not
    # provide an appropriate response to prompts from the service (you can
    # configure how many times Amazon Lex can prompt a user for specific
    # information), or if the Lambda function fails to fulfill the intent.
    dialog_state: typing.Union[str, "DialogState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `dialogState` value is `ElicitSlot`, returns the name of the slot
    # for which Amazon Lex is eliciting a value.
    slot_to_elicit: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text used to process the request.

    # If the input was an audio stream, the `inputTranscript` field contains the
    # text extracted from the audio stream. This is the text that is actually
    # processed to recognize intents and slot values. You can use this
    # information to determine if Amazon Lex is correctly processing the audio
    # that you send.
    input_transcript: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The prompt (or statement) to convey to the user. This is based on the bot
    # configuration and context. For example, if Amazon Lex did not understand
    # the user intent, it sends the `clarificationPrompt` configured for the bot.
    # If the intent requires confirmation before taking the fulfillment action,
    # it sends the `confirmationPrompt`. Another example: Suppose that the Lambda
    # function successfully fulfilled the intent, and sent a message to convey to
    # the user. Then Amazon Lex sends that message in the response.
    audio_stream: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PostTextRequest(ShapeBase):
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
                "user_id",
                "userId",
                TypeInfo(str),
            ),
            (
                "input_text",
                "inputText",
                TypeInfo(str),
            ),
            (
                "session_attributes",
                "sessionAttributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "request_attributes",
                "requestAttributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the Amazon Lex bot.
    bot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias of the Amazon Lex bot.
    bot_alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the client application user. Amazon Lex uses this to identify a
    # user's conversation with your bot. At runtime, each request must contain
    # the `userID` field.

    # To decide the user ID to use for your application, consider the following
    # factors.

    #   * The `userID` field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.

    #   * If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.

    #   * If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.

    #   * A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The text that the user entered (Amazon Lex interprets this text).
    input_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Application-specific information passed between Amazon Lex and a client
    # application.

    # For more information, see [Setting Session
    # Attributes](http://docs.aws.amazon.com/lex/latest/dg/context-
    # mgmt.html#context-mgmt-session-attribs).
    session_attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Request-specific information passed between Amazon Lex and a client
    # application.

    # The namespace `x-amz-lex:` is reserved for special attributes. Don't create
    # any request attributes with the prefix `x-amz-lex:`.

    # For more information, see [Setting Request
    # Attributes](http://docs.aws.amazon.com/lex/latest/dg/context-
    # mgmt.html#context-mgmt-request-attribs).
    request_attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PostTextResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "intent_name",
                "intentName",
                TypeInfo(str),
            ),
            (
                "slots",
                "slots",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "session_attributes",
                "sessionAttributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "message_format",
                "messageFormat",
                TypeInfo(typing.Union[str, MessageFormatType]),
            ),
            (
                "dialog_state",
                "dialogState",
                TypeInfo(typing.Union[str, DialogState]),
            ),
            (
                "slot_to_elicit",
                "slotToElicit",
                TypeInfo(str),
            ),
            (
                "response_card",
                "responseCard",
                TypeInfo(ResponseCard),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current user intent that Amazon Lex is aware of.
    intent_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The intent slots that Amazon Lex detected from the user input in the
    # conversation.

    # Amazon Lex creates a resolution list containing likely values for a slot.
    # The value that it returns is determined by the `valueSelectionStrategy`
    # selected when the slot type was created or updated. If
    # `valueSelectionStrategy` is set to `ORIGINAL_VALUE`, the value provided by
    # the user is returned, if the user value is similar to the slot values. If
    # `valueSelectionStrategy` is set to `TOP_RESOLUTION` Amazon Lex returns the
    # first value in the resolution list or, if there is no resolution list,
    # null. If you don't specify a `valueSelectionStrategy`, the default is
    # `ORIGINAL_VALUE`.
    slots: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of key-value pairs representing the session-specific context
    # information.
    session_attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message to convey to the user. The message can come from the bot's
    # configuration or from a Lambda function.

    # If the intent is not configured with a Lambda function, or if the Lambda
    # function returned `Delegate` as the `dialogAction.type` its response,
    # Amazon Lex decides on the next course of action and selects an appropriate
    # message from the bot's configuration based on the current interaction
    # context. For example, if Amazon Lex isn't able to understand user input, it
    # uses a clarification prompt message.

    # When you create an intent you can assign messages to groups. When messages
    # are assigned to groups Amazon Lex returns one message from each group in
    # the response. The message field is an escaped JSON string containing the
    # messages. For more information about the structure of the JSON string
    # returned, see msg-prompts-formats.

    # If the Lambda function returns a message, Amazon Lex passes it to the
    # client in its response.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the response message. One of the following values:

    #   * `PlainText` \- The message contains plain UTF-8 text.

    #   * `CustomPayload` \- The message is a custom format defined by the Lambda function.

    #   * `SSML` \- The message contains text formatted for voice output.

    #   * `Composite` \- The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.
    message_format: typing.Union[str, "MessageFormatType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the current state of the user interaction. Amazon Lex returns
    # one of the following values as `dialogState`. The client can optionally use
    # this information to customize the user interface.

    #   * `ElicitIntent` \- Amazon Lex wants to elicit user intent.

    # For example, a user might utter an intent ("I want to order a pizza"). If
    # Amazon Lex cannot infer the user intent from this utterance, it will return
    # this dialogState.

    #   * `ConfirmIntent` \- Amazon Lex is expecting a "yes" or "no" response.

    # For example, Amazon Lex wants user confirmation before fulfilling an
    # intent.

    # Instead of a simple "yes" or "no," a user might respond with additional
    # information. For example, "yes, but make it thick crust pizza" or "no, I
    # want to order a drink". Amazon Lex can process such additional information
    # (in these examples, update the crust type slot value, or change intent from
    # OrderPizza to OrderDrink).

    #   * `ElicitSlot` \- Amazon Lex is expecting a slot value for the current intent.

    # For example, suppose that in the response Amazon Lex sends this message:
    # "What size pizza would you like?". A user might reply with the slot value
    # (e.g., "medium"). The user might also provide additional information in the
    # response (e.g., "medium thick crust pizza"). Amazon Lex can process such
    # additional information appropriately.

    #   * `Fulfilled` \- Conveys that the Lambda function configured for the intent has successfully fulfilled the intent.

    #   * `ReadyForFulfillment` \- Conveys that the client has to fulfill the intent.

    #   * `Failed` \- Conveys that the conversation with the user failed.

    # This can happen for various reasons including that the user did not provide
    # an appropriate response to prompts from the service (you can configure how
    # many times Amazon Lex can prompt a user for specific information), or the
    # Lambda function failed to fulfill the intent.
    dialog_state: typing.Union[str, "DialogState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `dialogState` value is `ElicitSlot`, returns the name of the slot
    # for which Amazon Lex is eliciting a value.
    slot_to_elicit: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the options that the user has to respond to the current prompt.
    # Response Card can come from the bot configuration (in the Amazon Lex
    # console, choose the settings button next to a slot) or from a code hook
    # (Lambda function).
    response_card: "ResponseCard" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RequestTimeoutException(ShapeBase):
    """
    The input speech is too long.
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
class ResponseCard(ShapeBase):
    """
    If you configure a response card when creating your bots, Amazon Lex substitutes
    the session attributes and slot values that are available, and then returns it.
    The response card can also come from a Lambda function ( `dialogCodeHook` and
    `fulfillmentActivity` on an intent).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(typing.Union[str, ContentType]),
            ),
            (
                "generic_attachments",
                "genericAttachments",
                TypeInfo(typing.List[GenericAttachment]),
            ),
        ]

    # The version of the response card format.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content type of the response.
    content_type: typing.Union[str, "ContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of attachment objects representing options.
    generic_attachments: typing.List["GenericAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnsupportedMediaTypeException(ShapeBase):
    """
    The Content-Type header (`PostContent` API) has an invalid value.
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
