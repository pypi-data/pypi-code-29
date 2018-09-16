import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddPermissionInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "aws_account_id",
                "AWSAccountId",
                TypeInfo(typing.List[str]),
            ),
            (
                "action_name",
                "ActionName",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ARN of the topic whose access control policy you wish to modify.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the new policy statement.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account IDs of the users (principals) who will be given access to
    # the specified actions. The users must have AWS accounts, but do not need to
    # be signed up for this service.
    aws_account_id: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action you want to allow for the specified principal(s).

    # Valid values: any Amazon SNS action name.
    action_name: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AuthorizationErrorException(ShapeBase):
    """
    Indicates that the user has been denied access to the requested resource.
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


class Binary(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CheckIfPhoneNumberIsOptedOutInput(ShapeBase):
    """
    The input for the `CheckIfPhoneNumberIsOptedOut` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "phone_number",
                "phoneNumber",
                TypeInfo(str),
            ),
        ]

    # The phone number for which you want to check the opt out status.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CheckIfPhoneNumberIsOptedOutResponse(OutputShapeBase):
    """
    The response from the `CheckIfPhoneNumberIsOptedOut` action.
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
                "is_opted_out",
                "isOptedOut",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the phone number is opted out:

    #   * `true` – The phone number is opted out, meaning you cannot publish SMS messages to it.

    #   * `false` – The phone number is opted in, meaning you can publish SMS messages to it.
    is_opted_out: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfirmSubscriptionInput(ShapeBase):
    """
    Input for ConfirmSubscription action.
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
                "token",
                "Token",
                TypeInfo(str),
            ),
            (
                "authenticate_on_unsubscribe",
                "AuthenticateOnUnsubscribe",
                TypeInfo(str),
            ),
        ]

    # The ARN of the topic for which you wish to confirm a subscription.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Short-lived token sent to an endpoint during the `Subscribe` action.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Disallows unauthenticated unsubscribes of the subscription. If the value of
    # this parameter is `true` and the request has an AWS signature, then only
    # the topic owner and the subscription owner can unsubscribe the endpoint.
    # The unsubscribe action requires AWS authentication.
    authenticate_on_unsubscribe: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfirmSubscriptionResponse(OutputShapeBase):
    """
    Response for ConfirmSubscriptions action.
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
                "subscription_arn",
                "SubscriptionArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the created subscription.
    subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointResponse(OutputShapeBase):
    """
    Response from CreateEndpoint action.
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
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # EndpointArn returned from CreateEndpoint action.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePlatformApplicationInput(ShapeBase):
    """
    Input for CreatePlatformApplication action.
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
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Application names must be made up of only uppercase and lowercase ASCII
    # letters, numbers, underscores, hyphens, and periods, and must be between 1
    # and 256 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The following platforms are supported: ADM (Amazon Device Messaging), APNS
    # (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud
    # Messaging).
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a list of attributes, see
    # [SetPlatformApplicationAttributes](http://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html)
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlatformApplicationResponse(OutputShapeBase):
    """
    Response from CreatePlatformApplication action.
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
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # PlatformApplicationArn is returned.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlatformEndpointInput(ShapeBase):
    """
    Input for CreatePlatformEndpoint action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
            (
                "custom_user_data",
                "CustomUserData",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # PlatformApplicationArn returned from CreatePlatformApplication is used to
    # create a an endpoint.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier created by the notification service for an app on a
    # device. The specific name for Token will vary, depending on which
    # notification service is being used. For example, when using APNS as the
    # notification service, you need the device token. Alternatively, when using
    # GCM or ADM, the device token equivalent is called the registration ID.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Arbitrary user data to associate with the endpoint. Amazon SNS does not use
    # this data. The data must be in UTF-8 format and less than 2KB.
    custom_user_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a list of attributes, see
    # [SetEndpointAttributes](http://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html).
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTopicInput(ShapeBase):
    """
    Input for CreateTopic action.
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

    # The name of the topic you want to create.

    # Constraints: Topic names must be made up of only uppercase and lowercase
    # ASCII letters, numbers, underscores, and hyphens, and must be between 1 and
    # 256 characters long.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTopicResponse(OutputShapeBase):
    """
    Response from CreateTopic action.
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
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) assigned to the created topic.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEndpointInput(ShapeBase):
    """
    Input for DeleteEndpoint action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    # EndpointArn of endpoint to delete.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePlatformApplicationInput(ShapeBase):
    """
    Input for DeletePlatformApplication action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
        ]

    # PlatformApplicationArn of platform application object to delete.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTopicInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the topic you want to delete.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    """
    Endpoint for mobile app and device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # EndpointArn for mobile app and device.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Attributes for endpoint.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EndpointDisabledException(ShapeBase):
    """
    Exception error indicating endpoint disabled.
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

    # Message for endpoint disabled.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FilterPolicyLimitExceededException(ShapeBase):
    """
    Indicates that the number of filter polices in your AWS account exceeds the
    limit. To add more filter polices, submit an SNS Limit Increase case in the AWS
    Support Center.
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
class GetEndpointAttributesInput(ShapeBase):
    """
    Input for GetEndpointAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    # EndpointArn for GetEndpointAttributes input.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEndpointAttributesResponse(OutputShapeBase):
    """
    Response from GetEndpointAttributes of the EndpointArn.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes include the following:

    #   * `CustomUserData` \-- arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.

    #   * `Enabled` \-- flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.

    #   * `Token` \-- device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPlatformApplicationAttributesInput(ShapeBase):
    """
    Input for GetPlatformApplicationAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
        ]

    # PlatformApplicationArn for GetPlatformApplicationAttributesInput.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPlatformApplicationAttributesResponse(OutputShapeBase):
    """
    Response for GetPlatformApplicationAttributes action.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes include the following:

    #   * `EventEndpointCreated` \-- Topic ARN to which EndpointCreated event notifications should be sent.

    #   * `EventEndpointDeleted` \-- Topic ARN to which EndpointDeleted event notifications should be sent.

    #   * `EventEndpointUpdated` \-- Topic ARN to which EndpointUpdate event notifications should be sent.

    #   * `EventDeliveryFailure` \-- Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSMSAttributesInput(ShapeBase):
    """
    The input for the `GetSMSAttributes` request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of the individual attribute names, such as `MonthlySpendLimit`, for
    # which you want values.

    # For all attribute names, see
    # [SetSMSAttributes](http://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html).

    # If you don't use this parameter, Amazon SNS returns all SMS attributes.
    attributes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSMSAttributesResponse(OutputShapeBase):
    """
    The response from the `GetSMSAttributes` request.
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
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The SMS attribute names and their values.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSubscriptionAttributesInput(ShapeBase):
    """
    Input for GetSubscriptionAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_arn",
                "SubscriptionArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the subscription whose properties you want to get.
    subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSubscriptionAttributesResponse(OutputShapeBase):
    """
    Response for GetSubscriptionAttributes action.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of the subscription's attributes. Attributes in this map include the
    # following:

    #   * `ConfirmationWasAuthenticated` \-- `true` if the subscription confirmation request was authenticated.

    #   * `DeliveryPolicy` \-- The JSON serialization of the subscription's delivery policy.

    #   * `EffectiveDeliveryPolicy` \-- The JSON serialization of the effective delivery policy that takes into account the topic delivery policy and account system defaults.

    #   * `FilterPolicy` \-- The filter policy JSON that is assigned to the subscription.

    #   * `Owner` \-- The AWS account ID of the subscription's owner.

    #   * `PendingConfirmation` \-- `true` if the subscription hasn't been confirmed. To confirm a pending subscription, call the `ConfirmSubscription` action with a confirmation token.

    #   * `RawMessageDelivery` \-- `true` if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints.

    #   * `SubscriptionArn` \-- The subscription's ARN.

    #   * `TopicArn` \-- The topic ARN that the subscription is associated with.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetTopicAttributesInput(ShapeBase):
    """
    Input for GetTopicAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the topic whose properties you want to get.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTopicAttributesResponse(OutputShapeBase):
    """
    Response for GetTopicAttributes action.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of the topic's attributes. Attributes in this map include the
    # following:

    #   * `TopicArn` \-- the topic's ARN

    #   * `Owner` \-- the AWS account ID of the topic's owner

    #   * `Policy` \-- the JSON serialization of the topic's access control policy

    #   * `DisplayName` \-- the human-readable name used in the "From" field for notifications to email and email-json endpoints

    #   * `SubscriptionsPending` \-- the number of subscriptions pending confirmation on this topic

    #   * `SubscriptionsConfirmed` \-- the number of confirmed subscriptions on this topic

    #   * `SubscriptionsDeleted` \-- the number of deleted subscriptions on this topic

    #   * `DeliveryPolicy` \-- the JSON serialization of the topic's delivery policy

    #   * `EffectiveDeliveryPolicy` \-- the JSON serialization of the effective delivery policy that takes into account system defaults
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalErrorException(ShapeBase):
    """
    Indicates an internal service error.
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
class InvalidParameterException(ShapeBase):
    """
    Indicates that a request parameter does not comply with the associated
    constraints.
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
class InvalidParameterValueException(ShapeBase):
    """
    Indicates that a request parameter does not comply with the associated
    constraints.
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

    # The parameter value is invalid.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEndpointsByPlatformApplicationInput(ShapeBase):
    """
    Input for ListEndpointsByPlatformApplication action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # NextToken string is used when calling ListEndpointsByPlatformApplication
    # action to retrieve additional records that are available after the first
    # page results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEndpointsByPlatformApplicationResponse(OutputShapeBase):
    """
    Response for ListEndpointsByPlatformApplication action.
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
                "endpoints",
                "Endpoints",
                TypeInfo(typing.List[Endpoint]),
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

    # Endpoints returned for ListEndpointsByPlatformApplication action.
    endpoints: typing.List["Endpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # NextToken string is returned when calling
    # ListEndpointsByPlatformApplication action if additional records are
    # available after the first page results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator[
        "ListEndpointsByPlatformApplicationResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPhoneNumbersOptedOutInput(ShapeBase):
    """
    The input for the `ListPhoneNumbersOptedOut` action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # A `NextToken` string is used when you call the `ListPhoneNumbersOptedOut`
    # action to retrieve additional records that are available after the first
    # page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPhoneNumbersOptedOutResponse(OutputShapeBase):
    """
    The response from the `ListPhoneNumbersOptedOut` action.
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
                "phone_numbers",
                "phoneNumbers",
                TypeInfo(typing.List[str]),
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

    # A list of phone numbers that are opted out of receiving SMS messages. The
    # list is paginated, and each page can contain up to 100 phone numbers.
    phone_numbers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A `NextToken` string is returned when you call the
    # `ListPhoneNumbersOptedOut` action if additional records are available after
    # the first page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlatformApplicationsInput(ShapeBase):
    """
    Input for ListPlatformApplications action.
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

    # NextToken string is used when calling ListPlatformApplications action to
    # retrieve additional records that are available after the first page
    # results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlatformApplicationsResponse(OutputShapeBase):
    """
    Response for ListPlatformApplications action.
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
                "platform_applications",
                "PlatformApplications",
                TypeInfo(typing.List[PlatformApplication]),
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

    # Platform applications returned when calling ListPlatformApplications
    # action.
    platform_applications: typing.List["PlatformApplication"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # NextToken string is returned when calling ListPlatformApplications action
    # if additional records are available after the first page results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListPlatformApplicationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListSubscriptionsByTopicInput(ShapeBase):
    """
    Input for ListSubscriptionsByTopic action.
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ARN of the topic for which you wish to find subscriptions.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token returned by the previous `ListSubscriptionsByTopic` request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionsByTopicResponse(OutputShapeBase):
    """
    Response for ListSubscriptionsByTopic action.
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
                "subscriptions",
                "Subscriptions",
                TypeInfo(typing.List[Subscription]),
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

    # A list of subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to pass along to the next `ListSubscriptionsByTopic` request. This
    # element is returned if there are more subscriptions to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListSubscriptionsByTopicResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListSubscriptionsInput(ShapeBase):
    """
    Input for ListSubscriptions action.
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

    # Token returned by the previous `ListSubscriptions` request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionsResponse(OutputShapeBase):
    """
    Response for ListSubscriptions action
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
                "subscriptions",
                "Subscriptions",
                TypeInfo(typing.List[Subscription]),
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

    # A list of subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to pass along to the next `ListSubscriptions` request. This element
    # is returned if there are more subscriptions to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListSubscriptionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTopicsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Token returned by the previous `ListTopics` request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTopicsResponse(OutputShapeBase):
    """
    Response for ListTopics action.
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
                "topics",
                "Topics",
                TypeInfo(typing.List[Topic]),
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

    # A list of topic ARNs.
    topics: typing.List["Topic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to pass along to the next `ListTopics` request. This element is
    # returned if there are additional topics to retrieve.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListTopicsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MessageAttributeValue(ShapeBase):
    """
    The user-specified message attribute value. For string data types, the value
    attribute has the same restrictions on the content as the message body. For more
    information, see
    [Publish](http://docs.aws.amazon.com/sns/latest/api/API_Publish.html).

    Name, type, and value must not be empty or null. In addition, the message body
    should not be empty or null. All parts of the message attribute, including name,
    type, and value, are included in the message size restriction, which is
    currently 256 KB (262,144 bytes). For more information, see [Using Amazon SNS
    Message
    Attributes](http://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_type",
                "DataType",
                TypeInfo(str),
            ),
            (
                "string_value",
                "StringValue",
                TypeInfo(str),
            ),
            (
                "binary_value",
                "BinaryValue",
                TypeInfo(typing.Any),
            ),
        ]

    # Amazon SNS supports the following logical data types: String, String.Array,
    # Number, and Binary. For more information, see [Message Attribute Data
    # Types](http://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes).
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Strings are Unicode with UTF8 binary encoding. For a list of code values,
    # see <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Binary type attributes can store any binary data, for example, compressed
    # data, encrypted data, or images.
    binary_value: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    Indicates that the requested resource does not exist.
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
class OptInPhoneNumberInput(ShapeBase):
    """
    Input for the OptInPhoneNumber action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "phone_number",
                "phoneNumber",
                TypeInfo(str),
            ),
        ]

    # The phone number to opt in.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OptInPhoneNumberResponse(OutputShapeBase):
    """
    The response for the OptInPhoneNumber action.
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
class PlatformApplication(ShapeBase):
    """
    Platform application object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # PlatformApplicationArn for platform application object.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes for platform application object.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlatformApplicationDisabledException(ShapeBase):
    """
    Exception error indicating platform application disabled.
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

    # Message for platform application disabled.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PublishInput(ShapeBase):
    """
    Input for Publish action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "target_arn",
                "TargetArn",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
            (
                "subject",
                "Subject",
                TypeInfo(str),
            ),
            (
                "message_structure",
                "MessageStructure",
                TypeInfo(str),
            ),
            (
                "message_attributes",
                "MessageAttributes",
                TypeInfo(typing.Dict[str, MessageAttributeValue]),
            ),
        ]

    # The message you want to send.

    # If you are publishing to a topic and you want to send the same message to
    # all transport protocols, include the text of the message as a String value.
    # If you want to send different messages for each transport protocol, set the
    # value of the `MessageStructure` parameter to `json` and use a JSON object
    # for the `Message` parameter.

    # Constraints:

    #   * With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262144 bytes, not 262144 characters).

    #   * For SMS, each message can contain up to 140 bytes, and the character limit depends on the encoding scheme. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds the size limit, Amazon SNS sends it as multiple messages, each fitting within the size limit. Messages are not cut off in the middle of a word but on whole-word boundaries. The total size limit for a single SMS publish action is 1600 bytes.

    # JSON-specific constraints:

    #   * Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.

    #   * The values will be parsed (unescaped) before they are used in outgoing messages.

    #   * Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).

    #   * Values have a minimum length of 0 (the empty string, "", is allowed).

    #   * Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).

    #   * Non-string values will cause the key to be ignored.

    #   * Keys that do not correspond to supported transport protocols are ignored.

    #   * Duplicate keys are not allowed.

    #   * Failure to parse or validate any key or value in the message will cause the `Publish` call to return an error (no partial delivery).
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The topic you want to publish to.

    # If you don't specify a value for the `TopicArn` parameter, you must specify
    # a value for the `PhoneNumber` or `TargetArn` parameters.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either TopicArn or EndpointArn, but not both.

    # If you don't specify a value for the `TargetArn` parameter, you must
    # specify a value for the `PhoneNumber` or `TopicArn` parameters.
    target_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number to which you want to deliver an SMS message. Use E.164
    # format.

    # If you don't specify a value for the `PhoneNumber` parameter, you must
    # specify a value for the `TargetArn` or `TopicArn` parameters.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional parameter to be used as the "Subject" line when the message is
    # delivered to email endpoints. This field will also be included, if present,
    # in the standard JSON messages delivered to other endpoints.

    # Constraints: Subjects must be ASCII text that begins with a letter, number,
    # or punctuation mark; must not include line breaks or control characters;
    # and must be less than 100 characters long.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set `MessageStructure` to `json` if you want to send a different message
    # for each protocol. For example, using one publish action, you can send a
    # short message to your SMS subscribers and a longer message to your email
    # subscribers. If you set `MessageStructure` to `json`, the value of the
    # `Message` parameter must:

    #   * be a syntactically valid JSON object; and

    #   * contain at least a top-level JSON key of "default" with a value that is a string.

    # You can define other top-level keys that define the message you want to
    # send to a specific transport protocol (e.g., "http").

    # For information about sending different messages for each protocol using
    # the AWS Management Console, go to [Create Different Messages for Each
    # Protocol](http://docs.aws.amazon.com/sns/latest/gsg/Publish.html#sns-
    # message-formatting-by-protocol) in the _Amazon Simple Notification Service
    # Getting Started Guide_.

    # Valid value: `json`
    message_structure: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Message attributes for Publish action.
    message_attributes: typing.Dict[str, "MessageAttributeValue"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class PublishResponse(OutputShapeBase):
    """
    Response for Publish action.
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

    # Unique identifier assigned to the published message.

    # Length Constraint: Maximum 100 characters
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemovePermissionInput(ShapeBase):
    """
    Input for RemovePermission action.
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
                "label",
                "Label",
                TypeInfo(str),
            ),
        ]

    # The ARN of the topic whose access control policy you wish to modify.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique label of the statement you want to remove.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetEndpointAttributesInput(ShapeBase):
    """
    Input for SetEndpointAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # EndpointArn used for SetEndpointAttributes action.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of the endpoint attributes. Attributes in this map include the
    # following:

    #   * `CustomUserData` \-- arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.

    #   * `Enabled` \-- flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.

    #   * `Token` \-- device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetPlatformApplicationAttributesInput(ShapeBase):
    """
    Input for SetPlatformApplicationAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "platform_application_arn",
                "PlatformApplicationArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # PlatformApplicationArn for SetPlatformApplicationAttributes action.
    platform_application_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of the platform application attributes. Attributes in this map
    # include the following:

    #   * `PlatformCredential` \-- The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret".

    #   * `PlatformPrincipal` \-- The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id".

    #   * `EventEndpointCreated` \-- Topic ARN to which EndpointCreated event notifications should be sent.

    #   * `EventEndpointDeleted` \-- Topic ARN to which EndpointDeleted event notifications should be sent.

    #   * `EventEndpointUpdated` \-- Topic ARN to which EndpointUpdate event notifications should be sent.

    #   * `EventDeliveryFailure` \-- Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.

    #   * `SuccessFeedbackRoleArn` \-- IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.

    #   * `FailureFeedbackRoleArn` \-- IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.

    #   * `SuccessFeedbackSampleRate` \-- Sample rate percentage (0-100) of successfully delivered messages.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetSMSAttributesInput(ShapeBase):
    """
    The input for the SetSMSAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The default settings for sending SMS messages from your account. You can
    # set values for the following attribute names:

    # `MonthlySpendLimit` – The maximum amount in USD that you are willing to
    # spend each month to send SMS messages. When Amazon SNS determines that
    # sending an SMS message would incur a cost that exceeds this limit, it stops
    # sending SMS messages within minutes.

    # Amazon SNS stops sending SMS messages within minutes of the limit being
    # crossed. During that interval, if you continue to send SMS messages, you
    # will incur costs that exceed your limit.

    # By default, the spend limit is set to the maximum allowed by Amazon SNS. If
    # you want to raise the limit, submit an [SNS Limit Increase
    # case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-
    # limit-increase&limitType=service-code-sns). For **New limit value** , enter
    # your desired monthly spend limit. In the **Use Case Description** field,
    # explain that you are requesting an SMS monthly spend limit increase.

    # `DeliveryStatusIAMRole` – The ARN of the IAM role that allows Amazon SNS to
    # write logs about SMS deliveries in CloudWatch Logs. For each SMS message
    # that you send, Amazon SNS writes a log that includes the message price, the
    # success or failure status, the reason for failure (if the message failed),
    # the message dwell time, and other information.

    # `DeliveryStatusSuccessSamplingRate` – The percentage of successful SMS
    # deliveries for which Amazon SNS will write logs in CloudWatch Logs. The
    # value can be an integer from 0 - 100. For example, to write logs only for
    # failed deliveries, set this value to `0`. To write logs for 10% of your
    # successful deliveries, set it to `10`.

    # `DefaultSenderID` – A string, such as your business brand, that is
    # displayed as the sender on the receiving device. Support for sender IDs
    # varies by country. The sender ID can be 1 - 11 alphanumeric characters, and
    # it must contain at least one letter.

    # `DefaultSMSType` – The type of SMS message that you will send by default.
    # You can assign the following values:

    #   * `Promotional` – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.

    #   * `Transactional` – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.

    # `UsageReportS3Bucket` – The name of the Amazon S3 bucket to receive daily
    # SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a
    # usage report as a CSV file to the bucket. The report includes the following
    # information for each SMS message that was successfully delivered by your
    # account:

    #   * Time that the message was published (in UTC)

    #   * Message ID

    #   * Destination phone number

    #   * Message type

    #   * Delivery status

    #   * Message price (in USD)

    #   * Part number (a message is split into multiple parts if it is too long for a single message)

    #   * Total number of parts

    # To receive the report, the bucket must have a policy that allows the Amazon
    # SNS service principle to perform the `s3:PutObject` and
    # `s3:GetBucketLocation` actions.

    # For an example bucket policy and usage report, see [Monitoring SMS
    # Activity](http://docs.aws.amazon.com/sns/latest/dg/sms_stats.html) in the
    # _Amazon SNS Developer Guide_.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SetSMSAttributesResponse(OutputShapeBase):
    """
    The response for the SetSMSAttributes action.
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
class SetSubscriptionAttributesInput(ShapeBase):
    """
    Input for SetSubscriptionAttributes action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_arn",
                "SubscriptionArn",
                TypeInfo(str),
            ),
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                TypeInfo(str),
            ),
        ]

    # The ARN of the subscription to modify.
    subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute you want to set. Only a subset of the
    # subscriptions attributes are mutable.

    # Valid values: `DeliveryPolicy` | `FilterPolicy` | `RawMessageDelivery`
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new value for the attribute in JSON format.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTopicAttributesInput(ShapeBase):
    """
    Input for SetTopicAttributes action.
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
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_value",
                "AttributeValue",
                TypeInfo(str),
            ),
        ]

    # The ARN of the topic to modify.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute you want to set. Only a subset of the topic's
    # attributes are mutable.

    # Valid values: `Policy` | `DisplayName` | `DeliveryPolicy`
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new value for the attribute.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubscribeInput(ShapeBase):
    """
    Input for Subscribe action.
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
                "protocol",
                "Protocol",
                TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "return_subscription_arn",
                "ReturnSubscriptionArn",
                TypeInfo(bool),
            ),
        ]

    # The ARN of the topic you want to subscribe to.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol you want to use. Supported protocols include:

    #   * `http` \-- delivery of JSON-encoded message via HTTP POST

    #   * `https` \-- delivery of JSON-encoded message via HTTPS POST

    #   * `email` \-- delivery of message via SMTP

    #   * `email-json` \-- delivery of JSON-encoded message via SMTP

    #   * `sms` \-- delivery of message via SMS

    #   * `sqs` \-- delivery of JSON-encoded message to an Amazon SQS queue

    #   * `application` \-- delivery of JSON-encoded message to an EndpointArn for a mobile app and device.

    #   * `lambda` \-- delivery of JSON-encoded message to an AWS Lambda function.
    protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint that you want to receive notifications. Endpoints vary by
    # protocol:

    #   * For the `http` protocol, the endpoint is an URL beginning with "http://"

    #   * For the `https` protocol, the endpoint is a URL beginning with "https://"

    #   * For the `email` protocol, the endpoint is an email address

    #   * For the `email-json` protocol, the endpoint is an email address

    #   * For the `sms` protocol, the endpoint is a phone number of an SMS-enabled device

    #   * For the `sqs` protocol, the endpoint is the ARN of an Amazon SQS queue

    #   * For the `application` protocol, the endpoint is the EndpointArn of a mobile app and device.

    #   * For the `lambda` protocol, the endpoint is the ARN of an AWS Lambda function.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Assigns attributes to the subscription as a map of key-value pairs. You can
    # assign any attribute that is supported by the `SetSubscriptionAttributes`
    # action.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets whether the response from the `Subscribe` request includes the
    # subscription ARN, even if the subscription is not yet confirmed.

    # If you set this parameter to `false`, the response includes the ARN for
    # confirmed subscriptions, but it includes an ARN value of "pending
    # subscription" for subscriptions that are not yet confirmed. A subscription
    # becomes confirmed when the subscriber calls the `ConfirmSubscription`
    # action with a confirmation token.

    # If you set this parameter to `true`, the response includes the ARN in all
    # cases, even if the subscription is not yet confirmed.

    # The default value is `false`.
    return_subscription_arn: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubscribeResponse(OutputShapeBase):
    """
    Response for Subscribe action.
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
                "subscription_arn",
                "SubscriptionArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the subscription if it is confirmed, or the string "pending
    # confirmation" if the subscription requires confirmation. However, if the
    # API request parameter `ReturnSubscriptionArn` is true, then the value is
    # always the subscription ARN, even if the subscription requires
    # confirmation.
    subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Subscription(ShapeBase):
    """
    A wrapper type for the attributes of an Amazon SNS subscription.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_arn",
                "SubscriptionArn",
                TypeInfo(str),
            ),
            (
                "owner",
                "Owner",
                TypeInfo(str),
            ),
            (
                "protocol",
                "Protocol",
                TypeInfo(str),
            ),
            (
                "endpoint",
                "Endpoint",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    # The subscription's ARN.
    subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subscription's owner.
    owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subscription's protocol.
    protocol: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subscription's endpoint (format depends on the protocol).
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the subscription's topic.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubscriptionLimitExceededException(ShapeBase):
    """
    Indicates that the customer already owns the maximum allowed number of
    subscriptions.
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
class ThrottledException(ShapeBase):
    """
    Indicates that the rate at which requests have been submitted for this action
    exceeds the limit for your account.
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

    # Throttled request.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Topic(ShapeBase):
    """
    A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
    attributes, use `GetTopicAttributes`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
        ]

    # The topic's ARN.
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TopicLimitExceededException(ShapeBase):
    """
    Indicates that the customer already owns the maximum allowed number of topics.
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
class UnsubscribeInput(ShapeBase):
    """
    Input for Unsubscribe action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_arn",
                "SubscriptionArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the subscription to be deleted.
    subscription_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )
