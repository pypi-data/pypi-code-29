import json
import boto3
import time


def validate_carrier(carrier):
    """
    Checks for the presence of 'uber-trace-id' key in the carrier
    Dictionary.

    Parameters
    ----------
    carrier : dict
        An encoded SpanContext as defined by the OpenTracing specification.

    Returns
    ------
    boolean
        True if 'uber-trace-id' is present, false otherwise.
    """
    if not carrier.get('uber-trace-id'):
        return False
    return True


class EventPublisherError(Exception):
    """Base class for Event Publisher Exceptions."""
    pass


class CarrierError(EventPublisherError):
    """Exception raised if Carrier is invalid."""

    def __init__(self, message):
        self.message = message


class EventPublisher():
    """
    Class responsible for publishing event messages to a single topic.
    """

    def __init__(self, topic_arn, sns_client_params=None):
        """
        Initializes a Publisher object.

        Parameters
        ----------
        topic_arn : string
            Amazon resource identifier for a particular sns topic.
        sns_client_params : dict
            Dictionary containing parameters necessary for initializing a SNS
            client.
        """

        self.topic_arn = topic_arn
        if sns_client_params:
            self.sns_client = boto3.client('sns', **sns_client_params)
        else:
            self.sns_client = boto3.client('sns')

    def publish(self, carrier, uri, operation, before, after):
        """
        Publish an event message to the instance's SNS Topic.

        Parameters
        ----------
        carrier : dict
            An OpenTrace TEXT_MAP format carrier.
        uri : string
            The uri at which the event pertains to.
        operation : string
            The HTTP method which triggered the event.
        before : mixed
            The resource the event pertains to before it was modified. This can
            be None to represent Creation for example.
        after : mixed
            The resource the event pertains to after it was modified. This can
            be None to represent Deletion for example.

        Returns
        -------
        mixed
            A Dictionary containing an SNS MessageId if the message was
            published successfully, false otherwise.

        Raises
        ------
        CarrierError
        """

        if not validate_carrier(carrier):
            raise CarrierError('Carrier is not valid')

        body = {
            'default': {
                'carrier': carrier,
                'uri': uri,
                'operation': operation,
                'before': before,
                'after': after,
                'timestamp': time.time()
            }
        }
        payload = {'Message': json.dumps(body), 'MessageStructure': 'json'}
        response = self.sns_client.publish(TopicArn=self.topic_arn, **payload)

        return response
