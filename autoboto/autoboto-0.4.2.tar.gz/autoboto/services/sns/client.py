import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("sns", *args, **kwargs)

    def add_permission(
        self,
        _request: shapes.AddPermissionInput = None,
        *,
        topic_arn: str,
        label: str,
        aws_account_id: typing.List[str],
        action_name: typing.List[str],
    ) -> None:
        """
        Adds a statement to a topic's access control policy, granting access for the
        specified AWS accounts to the specified actions.
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            if aws_account_id is not ShapeBase.NOT_SET:
                _params['aws_account_id'] = aws_account_id
            if action_name is not ShapeBase.NOT_SET:
                _params['action_name'] = action_name
            _request = shapes.AddPermissionInput(**_params)
        response = self._boto_client.add_permission(**_request.to_boto())

    def check_if_phone_number_is_opted_out(
        self,
        _request: shapes.CheckIfPhoneNumberIsOptedOutInput = None,
        *,
        phone_number: str,
    ) -> shapes.CheckIfPhoneNumberIsOptedOutResponse:
        """
        Accepts a phone number and indicates whether the phone holder has opted out of
        receiving SMS messages from your account. You cannot send SMS messages to a
        number that is opted out.

        To resume sending messages, you can opt in the number by using the
        `OptInPhoneNumber` action.
        """
        if _request is None:
            _params = {}
            if phone_number is not ShapeBase.NOT_SET:
                _params['phone_number'] = phone_number
            _request = shapes.CheckIfPhoneNumberIsOptedOutInput(**_params)
        response = self._boto_client.check_if_phone_number_is_opted_out(
            **_request.to_boto()
        )

        return shapes.CheckIfPhoneNumberIsOptedOutResponse.from_boto(response)

    def confirm_subscription(
        self,
        _request: shapes.ConfirmSubscriptionInput = None,
        *,
        topic_arn: str,
        token: str,
        authenticate_on_unsubscribe: str = ShapeBase.NOT_SET,
    ) -> shapes.ConfirmSubscriptionResponse:
        """
        Verifies an endpoint owner's intent to receive messages by validating the token
        sent to the endpoint by an earlier `Subscribe` action. If the token is valid,
        the action creates a new subscription and returns its Amazon Resource Name
        (ARN). This call requires an AWS signature only when the
        `AuthenticateOnUnsubscribe` flag is set to "true".
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            if authenticate_on_unsubscribe is not ShapeBase.NOT_SET:
                _params['authenticate_on_unsubscribe'
                       ] = authenticate_on_unsubscribe
            _request = shapes.ConfirmSubscriptionInput(**_params)
        response = self._boto_client.confirm_subscription(**_request.to_boto())

        return shapes.ConfirmSubscriptionResponse.from_boto(response)

    def create_platform_application(
        self,
        _request: shapes.CreatePlatformApplicationInput = None,
        *,
        name: str,
        platform: str,
        attributes: typing.Dict[str, str],
    ) -> shapes.CreatePlatformApplicationResponse:
        """
        Creates a platform application object for one of the supported push notification
        services, such as APNS and GCM, to which devices and mobile apps may register.
        You must specify PlatformPrincipal and PlatformCredential attributes when using
        the `CreatePlatformApplication` action. The PlatformPrincipal is received from
        the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL
        certificate". For GCM, PlatformPrincipal is not applicable. For ADM,
        PlatformPrincipal is "client id". The PlatformCredential is also received from
        the notification service. For WNS, PlatformPrincipal is "Package Security
        Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu,
        PlatformPrincipal is "API key".

        For APNS/APNS_SANDBOX, PlatformCredential is "private key". For GCM,
        PlatformCredential is "API key". For ADM, PlatformCredential is "client secret".
        For WNS, PlatformCredential is "secret key". For MPNS, PlatformCredential is
        "private key". For Baidu, PlatformCredential is "secret key". The
        PlatformApplicationArn that is returned when using `CreatePlatformApplication`
        is then used as an attribute for the `CreatePlatformEndpoint` action. For more
        information, see [Using Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html). For
        more information about obtaining the PlatformPrincipal and PlatformCredential
        for each of the supported push notification services, see [Getting Started with
        Apple Push Notification
        Service](http://docs.aws.amazon.com/sns/latest/dg/mobile-push-apns.html),
        [Getting Started with Amazon Device
        Messaging](http://docs.aws.amazon.com/sns/latest/dg/mobile-push-adm.html),
        [Getting Started with Baidu Cloud
        Push](http://docs.aws.amazon.com/sns/latest/dg/mobile-push-baidu.html), [Getting
        Started with Google Cloud Messaging for
        Android](http://docs.aws.amazon.com/sns/latest/dg/mobile-push-gcm.html),
        [Getting Started with MPNS](http://docs.aws.amazon.com/sns/latest/dg/mobile-
        push-mpns.html), or [Getting Started with
        WNS](http://docs.aws.amazon.com/sns/latest/dg/mobile-push-wns.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if platform is not ShapeBase.NOT_SET:
                _params['platform'] = platform
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.CreatePlatformApplicationInput(**_params)
        response = self._boto_client.create_platform_application(
            **_request.to_boto()
        )

        return shapes.CreatePlatformApplicationResponse.from_boto(response)

    def create_platform_endpoint(
        self,
        _request: shapes.CreatePlatformEndpointInput = None,
        *,
        platform_application_arn: str,
        token: str,
        custom_user_data: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateEndpointResponse:
        """
        Creates an endpoint for a device and mobile app on one of the supported push
        notification services, such as GCM and APNS. `CreatePlatformEndpoint` requires
        the PlatformApplicationArn that is returned from `CreatePlatformApplication`.
        The EndpointArn that is returned when using `CreatePlatformEndpoint` can then be
        used by the `Publish` action to send a message to a mobile app or by the
        `Subscribe` action for subscription to a topic. The `CreatePlatformEndpoint`
        action is idempotent, so if the requester already owns an endpoint with the same
        device token and attributes, that endpoint's ARN is returned without creating a
        new endpoint. For more information, see [Using Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

        When using `CreatePlatformEndpoint` with Baidu, two attributes must be provided:
        ChannelId and UserId. The token field must also contain the ChannelId. For more
        information, see [Creating an Amazon SNS Endpoint for
        Baidu](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html).
        """
        if _request is None:
            _params = {}
            if platform_application_arn is not ShapeBase.NOT_SET:
                _params['platform_application_arn'] = platform_application_arn
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            if custom_user_data is not ShapeBase.NOT_SET:
                _params['custom_user_data'] = custom_user_data
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.CreatePlatformEndpointInput(**_params)
        response = self._boto_client.create_platform_endpoint(
            **_request.to_boto()
        )

        return shapes.CreateEndpointResponse.from_boto(response)

    def create_topic(
        self,
        _request: shapes.CreateTopicInput = None,
        *,
        name: str,
    ) -> shapes.CreateTopicResponse:
        """
        Creates a topic to which notifications can be published. Users can create at
        most 100,000 topics. For more information, see
        [http://aws.amazon.com/sns](http://aws.amazon.com/sns/). This action is
        idempotent, so if the requester already owns a topic with the specified name,
        that topic's ARN is returned without creating a new topic.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateTopicInput(**_params)
        response = self._boto_client.create_topic(**_request.to_boto())

        return shapes.CreateTopicResponse.from_boto(response)

    def delete_endpoint(
        self,
        _request: shapes.DeleteEndpointInput = None,
        *,
        endpoint_arn: str,
    ) -> None:
        """
        Deletes the endpoint for a device and mobile app from Amazon SNS. This action is
        idempotent. For more information, see [Using Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

        When you delete an endpoint that is also subscribed to a topic, then you must
        also unsubscribe the endpoint from the topic.
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            _request = shapes.DeleteEndpointInput(**_params)
        response = self._boto_client.delete_endpoint(**_request.to_boto())

    def delete_platform_application(
        self,
        _request: shapes.DeletePlatformApplicationInput = None,
        *,
        platform_application_arn: str,
    ) -> None:
        """
        Deletes a platform application object for one of the supported push notification
        services, such as APNS and GCM. For more information, see [Using Amazon SNS
        Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).
        """
        if _request is None:
            _params = {}
            if platform_application_arn is not ShapeBase.NOT_SET:
                _params['platform_application_arn'] = platform_application_arn
            _request = shapes.DeletePlatformApplicationInput(**_params)
        response = self._boto_client.delete_platform_application(
            **_request.to_boto()
        )

    def delete_topic(
        self,
        _request: shapes.DeleteTopicInput = None,
        *,
        topic_arn: str,
    ) -> None:
        """
        Deletes a topic and all its subscriptions. Deleting a topic might prevent some
        messages previously sent to the topic from being delivered to subscribers. This
        action is idempotent, so deleting a topic that does not exist does not result in
        an error.
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            _request = shapes.DeleteTopicInput(**_params)
        response = self._boto_client.delete_topic(**_request.to_boto())

    def get_endpoint_attributes(
        self,
        _request: shapes.GetEndpointAttributesInput = None,
        *,
        endpoint_arn: str,
    ) -> shapes.GetEndpointAttributesResponse:
        """
        Retrieves the endpoint attributes for a device on one of the supported push
        notification services, such as GCM and APNS. For more information, see [Using
        Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            _request = shapes.GetEndpointAttributesInput(**_params)
        response = self._boto_client.get_endpoint_attributes(
            **_request.to_boto()
        )

        return shapes.GetEndpointAttributesResponse.from_boto(response)

    def get_platform_application_attributes(
        self,
        _request: shapes.GetPlatformApplicationAttributesInput = None,
        *,
        platform_application_arn: str,
    ) -> shapes.GetPlatformApplicationAttributesResponse:
        """
        Retrieves the attributes of the platform application object for the supported
        push notification services, such as APNS and GCM. For more information, see
        [Using Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).
        """
        if _request is None:
            _params = {}
            if platform_application_arn is not ShapeBase.NOT_SET:
                _params['platform_application_arn'] = platform_application_arn
            _request = shapes.GetPlatformApplicationAttributesInput(**_params)
        response = self._boto_client.get_platform_application_attributes(
            **_request.to_boto()
        )

        return shapes.GetPlatformApplicationAttributesResponse.from_boto(
            response
        )

    def get_sms_attributes(
        self,
        _request: shapes.GetSMSAttributesInput = None,
        *,
        attributes: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.GetSMSAttributesResponse:
        """
        Returns the settings for sending SMS messages from your account.

        These settings are set with the `SetSMSAttributes` action.
        """
        if _request is None:
            _params = {}
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.GetSMSAttributesInput(**_params)
        response = self._boto_client.get_sms_attributes(**_request.to_boto())

        return shapes.GetSMSAttributesResponse.from_boto(response)

    def get_subscription_attributes(
        self,
        _request: shapes.GetSubscriptionAttributesInput = None,
        *,
        subscription_arn: str,
    ) -> shapes.GetSubscriptionAttributesResponse:
        """
        Returns all of the properties of a subscription.
        """
        if _request is None:
            _params = {}
            if subscription_arn is not ShapeBase.NOT_SET:
                _params['subscription_arn'] = subscription_arn
            _request = shapes.GetSubscriptionAttributesInput(**_params)
        response = self._boto_client.get_subscription_attributes(
            **_request.to_boto()
        )

        return shapes.GetSubscriptionAttributesResponse.from_boto(response)

    def get_topic_attributes(
        self,
        _request: shapes.GetTopicAttributesInput = None,
        *,
        topic_arn: str,
    ) -> shapes.GetTopicAttributesResponse:
        """
        Returns all of the properties of a topic. Topic properties returned might differ
        based on the authorization of the user.
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            _request = shapes.GetTopicAttributesInput(**_params)
        response = self._boto_client.get_topic_attributes(**_request.to_boto())

        return shapes.GetTopicAttributesResponse.from_boto(response)

    def list_endpoints_by_platform_application(
        self,
        _request: shapes.ListEndpointsByPlatformApplicationInput = None,
        *,
        platform_application_arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListEndpointsByPlatformApplicationResponse:
        """
        Lists the endpoints and endpoint attributes for devices in a supported push
        notification service, such as GCM and APNS. The results for
        `ListEndpointsByPlatformApplication` are paginated and return a limited list of
        endpoints, up to 100. If additional records are available after the first page
        results, then a NextToken string will be returned. To receive the next page, you
        call `ListEndpointsByPlatformApplication` again using the NextToken string
        received from the previous call. When there are no more records to return,
        NextToken will be null. For more information, see [Using Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

        This action is throttled at 30 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if platform_application_arn is not ShapeBase.NOT_SET:
                _params['platform_application_arn'] = platform_application_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListEndpointsByPlatformApplicationInput(**_params)
        paginator = self.get_paginator(
            "list_endpoints_by_platform_application"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListEndpointsByPlatformApplicationResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListEndpointsByPlatformApplicationResponse.from_boto(
            response
        )

    def list_phone_numbers_opted_out(
        self,
        _request: shapes.ListPhoneNumbersOptedOutInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPhoneNumbersOptedOutResponse:
        """
        Returns a list of phone numbers that are opted out, meaning you cannot send SMS
        messages to them.

        The results for `ListPhoneNumbersOptedOut` are paginated, and each page returns
        up to 100 phone numbers. If additional phone numbers are available after the
        first page of results, then a `NextToken` string will be returned. To receive
        the next page, you call `ListPhoneNumbersOptedOut` again using the `NextToken`
        string received from the previous call. When there are no more records to
        return, `NextToken` will be null.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPhoneNumbersOptedOutInput(**_params)
        response = self._boto_client.list_phone_numbers_opted_out(
            **_request.to_boto()
        )

        return shapes.ListPhoneNumbersOptedOutResponse.from_boto(response)

    def list_platform_applications(
        self,
        _request: shapes.ListPlatformApplicationsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPlatformApplicationsResponse:
        """
        Lists the platform application objects for the supported push notification
        services, such as APNS and GCM. The results for `ListPlatformApplications` are
        paginated and return a limited list of applications, up to 100. If additional
        records are available after the first page results, then a NextToken string will
        be returned. To receive the next page, you call `ListPlatformApplications` using
        the NextToken string received from the previous call. When there are no more
        records to return, NextToken will be null. For more information, see [Using
        Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

        This action is throttled at 15 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPlatformApplicationsInput(**_params)
        paginator = self.get_paginator("list_platform_applications").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPlatformApplicationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPlatformApplicationsResponse.from_boto(response)

    def list_subscriptions(
        self,
        _request: shapes.ListSubscriptionsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSubscriptionsResponse:
        """
        Returns a list of the requester's subscriptions. Each call returns a limited
        list of subscriptions, up to 100. If there are more subscriptions, a `NextToken`
        is also returned. Use the `NextToken` parameter in a new `ListSubscriptions`
        call to get further results.

        This action is throttled at 30 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSubscriptionsInput(**_params)
        paginator = self.get_paginator("list_subscriptions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSubscriptionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSubscriptionsResponse.from_boto(response)

    def list_subscriptions_by_topic(
        self,
        _request: shapes.ListSubscriptionsByTopicInput = None,
        *,
        topic_arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSubscriptionsByTopicResponse:
        """
        Returns a list of the subscriptions to a specific topic. Each call returns a
        limited list of subscriptions, up to 100. If there are more subscriptions, a
        `NextToken` is also returned. Use the `NextToken` parameter in a new
        `ListSubscriptionsByTopic` call to get further results.

        This action is throttled at 30 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSubscriptionsByTopicInput(**_params)
        paginator = self.get_paginator("list_subscriptions_by_topic").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSubscriptionsByTopicResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSubscriptionsByTopicResponse.from_boto(response)

    def list_topics(
        self,
        _request: shapes.ListTopicsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTopicsResponse:
        """
        Returns a list of the requester's topics. Each call returns a limited list of
        topics, up to 100. If there are more topics, a `NextToken` is also returned. Use
        the `NextToken` parameter in a new `ListTopics` call to get further results.

        This action is throttled at 30 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListTopicsInput(**_params)
        paginator = self.get_paginator("list_topics").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTopicsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTopicsResponse.from_boto(response)

    def opt_in_phone_number(
        self,
        _request: shapes.OptInPhoneNumberInput = None,
        *,
        phone_number: str,
    ) -> shapes.OptInPhoneNumberResponse:
        """
        Use this request to opt in a phone number that is opted out, which enables you
        to resume sending SMS messages to the number.

        You can opt in a phone number only once every 30 days.
        """
        if _request is None:
            _params = {}
            if phone_number is not ShapeBase.NOT_SET:
                _params['phone_number'] = phone_number
            _request = shapes.OptInPhoneNumberInput(**_params)
        response = self._boto_client.opt_in_phone_number(**_request.to_boto())

        return shapes.OptInPhoneNumberResponse.from_boto(response)

    def publish(
        self,
        _request: shapes.PublishInput = None,
        *,
        message: str,
        topic_arn: str = ShapeBase.NOT_SET,
        target_arn: str = ShapeBase.NOT_SET,
        phone_number: str = ShapeBase.NOT_SET,
        subject: str = ShapeBase.NOT_SET,
        message_structure: str = ShapeBase.NOT_SET,
        message_attributes: typing.
        Dict[str, shapes.MessageAttributeValue] = ShapeBase.NOT_SET,
    ) -> shapes.PublishResponse:
        """
        Sends a message to an Amazon SNS topic or sends a text message (SMS message)
        directly to a phone number.

        If you send a message to a topic, Amazon SNS delivers the message to each
        endpoint that is subscribed to the topic. The format of the message depends on
        the notification protocol for each subscribed endpoint.

        When a `messageId` is returned, the message has been saved and Amazon SNS will
        attempt to deliver it shortly.

        To use the `Publish` action for sending a message to a mobile endpoint, such as
        an app on a Kindle device or mobile phone, you must specify the EndpointArn for
        the TargetArn parameter. The EndpointArn is returned when making a call with the
        `CreatePlatformEndpoint` action.

        For more information about formatting messages, see [Send Custom Platform-
        Specific Payloads in Messages to Mobile
        Devices](http://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-
        custommessage.html).
        """
        if _request is None:
            _params = {}
            if message is not ShapeBase.NOT_SET:
                _params['message'] = message
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if target_arn is not ShapeBase.NOT_SET:
                _params['target_arn'] = target_arn
            if phone_number is not ShapeBase.NOT_SET:
                _params['phone_number'] = phone_number
            if subject is not ShapeBase.NOT_SET:
                _params['subject'] = subject
            if message_structure is not ShapeBase.NOT_SET:
                _params['message_structure'] = message_structure
            if message_attributes is not ShapeBase.NOT_SET:
                _params['message_attributes'] = message_attributes
            _request = shapes.PublishInput(**_params)
        response = self._boto_client.publish(**_request.to_boto())

        return shapes.PublishResponse.from_boto(response)

    def remove_permission(
        self,
        _request: shapes.RemovePermissionInput = None,
        *,
        topic_arn: str,
        label: str,
    ) -> None:
        """
        Removes a statement from a topic's access control policy.
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            _request = shapes.RemovePermissionInput(**_params)
        response = self._boto_client.remove_permission(**_request.to_boto())

    def set_endpoint_attributes(
        self,
        _request: shapes.SetEndpointAttributesInput = None,
        *,
        endpoint_arn: str,
        attributes: typing.Dict[str, str],
    ) -> None:
        """
        Sets the attributes for an endpoint for a device on one of the supported push
        notification services, such as GCM and APNS. For more information, see [Using
        Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).
        """
        if _request is None:
            _params = {}
            if endpoint_arn is not ShapeBase.NOT_SET:
                _params['endpoint_arn'] = endpoint_arn
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.SetEndpointAttributesInput(**_params)
        response = self._boto_client.set_endpoint_attributes(
            **_request.to_boto()
        )

    def set_platform_application_attributes(
        self,
        _request: shapes.SetPlatformApplicationAttributesInput = None,
        *,
        platform_application_arn: str,
        attributes: typing.Dict[str, str],
    ) -> None:
        """
        Sets the attributes of the platform application object for the supported push
        notification services, such as APNS and GCM. For more information, see [Using
        Amazon SNS Mobile Push
        Notifications](http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html). For
        information on configuring attributes for message delivery status, see [Using
        Amazon SNS Application Attributes for Message Delivery
        Status](http://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html).
        """
        if _request is None:
            _params = {}
            if platform_application_arn is not ShapeBase.NOT_SET:
                _params['platform_application_arn'] = platform_application_arn
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.SetPlatformApplicationAttributesInput(**_params)
        response = self._boto_client.set_platform_application_attributes(
            **_request.to_boto()
        )

    def set_sms_attributes(
        self,
        _request: shapes.SetSMSAttributesInput = None,
        *,
        attributes: typing.Dict[str, str],
    ) -> shapes.SetSMSAttributesResponse:
        """
        Use this request to set the default settings for sending SMS messages and
        receiving daily SMS usage reports.

        You can override some of these settings for a single message when you use the
        `Publish` action with the `MessageAttributes.entry.N` parameter. For more
        information, see [Sending an SMS
        Message](http://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html) in
        the _Amazon SNS Developer Guide_.
        """
        if _request is None:
            _params = {}
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.SetSMSAttributesInput(**_params)
        response = self._boto_client.set_sms_attributes(**_request.to_boto())

        return shapes.SetSMSAttributesResponse.from_boto(response)

    def set_subscription_attributes(
        self,
        _request: shapes.SetSubscriptionAttributesInput = None,
        *,
        subscription_arn: str,
        attribute_name: str,
        attribute_value: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Allows a subscription owner to set an attribute of the subscription to a new
        value.
        """
        if _request is None:
            _params = {}
            if subscription_arn is not ShapeBase.NOT_SET:
                _params['subscription_arn'] = subscription_arn
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if attribute_value is not ShapeBase.NOT_SET:
                _params['attribute_value'] = attribute_value
            _request = shapes.SetSubscriptionAttributesInput(**_params)
        response = self._boto_client.set_subscription_attributes(
            **_request.to_boto()
        )

    def set_topic_attributes(
        self,
        _request: shapes.SetTopicAttributesInput = None,
        *,
        topic_arn: str,
        attribute_name: str,
        attribute_value: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Allows a topic owner to set an attribute of the topic to a new value.
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if attribute_value is not ShapeBase.NOT_SET:
                _params['attribute_value'] = attribute_value
            _request = shapes.SetTopicAttributesInput(**_params)
        response = self._boto_client.set_topic_attributes(**_request.to_boto())

    def subscribe(
        self,
        _request: shapes.SubscribeInput = None,
        *,
        topic_arn: str,
        protocol: str,
        endpoint: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
        return_subscription_arn: bool = ShapeBase.NOT_SET,
    ) -> shapes.SubscribeResponse:
        """
        Prepares to subscribe an endpoint by sending the endpoint a confirmation
        message. To actually create a subscription, the endpoint owner must call the
        `ConfirmSubscription` action with the token from the confirmation message.
        Confirmation tokens are valid for three days.

        This action is throttled at 100 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if topic_arn is not ShapeBase.NOT_SET:
                _params['topic_arn'] = topic_arn
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if endpoint is not ShapeBase.NOT_SET:
                _params['endpoint'] = endpoint
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if return_subscription_arn is not ShapeBase.NOT_SET:
                _params['return_subscription_arn'] = return_subscription_arn
            _request = shapes.SubscribeInput(**_params)
        response = self._boto_client.subscribe(**_request.to_boto())

        return shapes.SubscribeResponse.from_boto(response)

    def unsubscribe(
        self,
        _request: shapes.UnsubscribeInput = None,
        *,
        subscription_arn: str,
    ) -> None:
        """
        Deletes a subscription. If the subscription requires authentication for
        deletion, only the owner of the subscription or the topic's owner can
        unsubscribe, and an AWS signature is required. If the `Unsubscribe` call does
        not require authentication and the requester is not the subscription owner, a
        final cancellation message is delivered to the endpoint, so that the endpoint
        owner can easily resubscribe to the topic if the `Unsubscribe` request was
        unintended.

        This action is throttled at 100 transactions per second (TPS).
        """
        if _request is None:
            _params = {}
            if subscription_arn is not ShapeBase.NOT_SET:
                _params['subscription_arn'] = subscription_arn
            _request = shapes.UnsubscribeInput(**_params)
        response = self._boto_client.unsubscribe(**_request.to_boto())
