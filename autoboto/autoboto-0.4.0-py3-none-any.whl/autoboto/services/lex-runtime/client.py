import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("lex-runtime", *args, **kwargs)

    def post_content(
        self,
        _request: shapes.PostContentRequest = None,
        *,
        bot_name: str,
        bot_alias: str,
        user_id: str,
        content_type: str,
        input_stream: typing.Any,
        session_attributes: str = ShapeBase.NOT_SET,
        request_attributes: str = ShapeBase.NOT_SET,
        accept: str = ShapeBase.NOT_SET,
    ) -> shapes.PostContentResponse:
        """
        Sends user input (text or speech) to Amazon Lex. Clients use this API to send
        text and audio requests to Amazon Lex at runtime. Amazon Lex interprets the user
        input using the machine learning model that it built for the bot.

        The `PostContent` operation supports audio input at 8kHz and 16kHz. You can use
        8kHz audio to achieve higher speech recognition accuracy in telephone audio
        applications.

        In response, Amazon Lex returns the next message to convey to the user. Consider
        the following example messages:

          * For a user input "I would like a pizza," Amazon Lex might return a response with a message eliciting slot data (for example, `PizzaSize`): "What size pizza would you like?". 

          * After the user provides all of the pizza order information, Amazon Lex might return a response with a message to get user confirmation: "Order the pizza?". 

          * After the user replies "Yes" to the confirmation prompt, Amazon Lex might return a conclusion statement: "Thank you, your cheese pizza has been ordered.". 

        Not all Amazon Lex messages require a response from the user. For example,
        conclusion statements do not require a response. Some messages require only a
        yes or no response. In addition to the `message`, Amazon Lex provides additional
        context about the message in the response that you can use to enhance client
        behavior, such as displaying the appropriate client user interface. Consider the
        following examples:

          * If the message is to elicit slot data, Amazon Lex returns the following context information: 

            * `x-amz-lex-dialog-state` header set to `ElicitSlot`

            * `x-amz-lex-intent-name` header set to the intent name in the current context 

            * `x-amz-lex-slot-to-elicit` header set to the slot name for which the `message` is eliciting information 

            * `x-amz-lex-slots` header set to a map of slots configured for the intent with their current values 

          * If the message is a confirmation prompt, the `x-amz-lex-dialog-state` header is set to `Confirmation` and the `x-amz-lex-slot-to-elicit` header is omitted. 

          * If the message is a clarification prompt configured for the intent, indicating that the user intent is not understood, the `x-amz-dialog-state` header is set to `ElicitIntent` and the `x-amz-slot-to-elicit` header is omitted. 

        In addition, Amazon Lex also returns your application-specific
        `sessionAttributes`. For more information, see [Managing Conversation
        Context](http://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html).
        """
        if _request is None:
            _params = {}
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if bot_alias is not ShapeBase.NOT_SET:
                _params['bot_alias'] = bot_alias
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if input_stream is not ShapeBase.NOT_SET:
                _params['input_stream'] = input_stream
            if session_attributes is not ShapeBase.NOT_SET:
                _params['session_attributes'] = session_attributes
            if request_attributes is not ShapeBase.NOT_SET:
                _params['request_attributes'] = request_attributes
            if accept is not ShapeBase.NOT_SET:
                _params['accept'] = accept
            _request = shapes.PostContentRequest(**_params)
        response = self._boto_client.post_content(**_request.to_boto())

        return shapes.PostContentResponse.from_boto(response)

    def post_text(
        self,
        _request: shapes.PostTextRequest = None,
        *,
        bot_name: str,
        bot_alias: str,
        user_id: str,
        input_text: str,
        session_attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
        request_attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.PostTextResponse:
        """
        Sends user input (text-only) to Amazon Lex. Client applications can use this API
        to send requests to Amazon Lex at runtime. Amazon Lex then interprets the user
        input using the machine learning model it built for the bot.

        In response, Amazon Lex returns the next `message` to convey to the user an
        optional `responseCard` to display. Consider the following example messages:

          * For a user input "I would like a pizza", Amazon Lex might return a response with a message eliciting slot data (for example, PizzaSize): "What size pizza would you like?" 

          * After the user provides all of the pizza order information, Amazon Lex might return a response with a message to obtain user confirmation "Proceed with the pizza order?". 

          * After the user replies to a confirmation prompt with a "yes", Amazon Lex might return a conclusion statement: "Thank you, your cheese pizza has been ordered.". 

        Not all Amazon Lex messages require a user response. For example, a conclusion
        statement does not require a response. Some messages require only a "yes" or
        "no" user response. In addition to the `message`, Amazon Lex provides additional
        context about the message in the response that you might use to enhance client
        behavior, for example, to display the appropriate client user interface. These
        are the `slotToElicit`, `dialogState`, `intentName`, and `slots` fields in the
        response. Consider the following examples:

          * If the message is to elicit slot data, Amazon Lex returns the following context information:

            * `dialogState` set to ElicitSlot 

            * `intentName` set to the intent name in the current context 

            * `slotToElicit` set to the slot name for which the `message` is eliciting information 

            * `slots` set to a map of slots, configured for the intent, with currently known values 

          * If the message is a confirmation prompt, the `dialogState` is set to ConfirmIntent and `SlotToElicit` is set to null. 

          * If the message is a clarification prompt (configured for the intent) that indicates that user intent is not understood, the `dialogState` is set to ElicitIntent and `slotToElicit` is set to null. 

        In addition, Amazon Lex also returns your application-specific
        `sessionAttributes`. For more information, see [Managing Conversation
        Context](http://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html).
        """
        if _request is None:
            _params = {}
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if bot_alias is not ShapeBase.NOT_SET:
                _params['bot_alias'] = bot_alias
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if input_text is not ShapeBase.NOT_SET:
                _params['input_text'] = input_text
            if session_attributes is not ShapeBase.NOT_SET:
                _params['session_attributes'] = session_attributes
            if request_attributes is not ShapeBase.NOT_SET:
                _params['request_attributes'] = request_attributes
            _request = shapes.PostTextRequest(**_params)
        response = self._boto_client.post_text(**_request.to_boto())

        return shapes.PostTextResponse.from_boto(response)
