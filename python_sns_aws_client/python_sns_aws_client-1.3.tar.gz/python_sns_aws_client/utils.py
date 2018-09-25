#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import boto3
import boto3.data.sns
import json
from .exceptions import *
from .constans import *


class Client(object):

    def __init__(self):
        """

        :param aws_access_key_id: access key, subministrada por aws
        :param aws_secret_access_key: secret key, subministrada por aws
        :param region_name: region aws
        :return: Client-sns

        """

        self.client = boto3.client(
            'sns',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_DEFAULT_REGION
        )

    def publish(self, **request):
        """

        :param request: receive content post from framework and generate
                        new publish in topic
        :return:
        """
        try:
            response = self.client.publish(
                TargetArn=AWS_TOPIC,
                Message=request['message'],
                Subject=request['subject'],
            )
            return response
        except PublishError as publish_error:
            return publish_error

    @staticmethod
    def validator(request):
        """

        :param request: content body or data send from framework, receive param
                        from endpoint attached in topic.
        :return: one: Message full from topic
                 two: Send subscription from topic to client_subscription
        """

        body = json.loads(request)

        try:
            if 'MessageId' in body and body['Type'] == "Notification":
                return body
            elif 'TopicArn'in body and 'Token' in body:
                cli = Client()
                cli.subscription(
                    body['TopicArn'],
                    body['Token']
                )
        except RequestInvalidError as request_invalid:
            return request_invalid

    def subscription(self, topic, aws_token_session):
        """

        :param topic: topic from aws
        :param aws_token_session: token_session generate from aws
        :return: Subscription in topic
        """
        try:
            response = self.client.confirm_subscription(
                TopicArn=topic,
                Token=aws_token_session
            )
            return response
        except SubscriptionError as subscription_error:
            return subscription_error
