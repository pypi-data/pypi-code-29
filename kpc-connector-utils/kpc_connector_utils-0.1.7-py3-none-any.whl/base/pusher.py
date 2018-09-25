from kpc_connector_utils.common.types import EventType
import boto3


class Pusher:
    def __init__(self, config):
        self._config = config

    def push_event(self):

        lambda_client = boto3.client('lambda')
        if self._config.event_type == EventType.Event:
            lambda_client.invoke(FunctionName=self._config.func_name,
                                 InvocationType=self._config.event_type,
                                 LogType='None',
                                 Payload=self._config.__str__().encode())

        elif self._config.event_type == EventType.RequestResponse:
            return lambda_client.invoke(FunctionName=self._config.func_name,
                                        InvocationType=self._config.event_type,
                                        LogType='None',
                                        Payload=self._config.__str__().encode())

        else:
            raise ValueError('Not specify event type or it is not available')
