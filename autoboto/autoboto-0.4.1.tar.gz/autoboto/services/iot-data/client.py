import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iot-data", *args, **kwargs)

    def delete_thing_shadow(
        self,
        _request: shapes.DeleteThingShadowRequest = None,
        *,
        thing_name: str,
    ) -> shapes.DeleteThingShadowResponse:
        """
        Deletes the thing shadow for the specified thing.

        For more information, see
        [DeleteThingShadow](http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html)
        in the _AWS IoT Developer Guide_.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.DeleteThingShadowRequest(**_params)
        response = self._boto_client.delete_thing_shadow(**_request.to_boto())

        return shapes.DeleteThingShadowResponse.from_boto(response)

    def get_thing_shadow(
        self,
        _request: shapes.GetThingShadowRequest = None,
        *,
        thing_name: str,
    ) -> shapes.GetThingShadowResponse:
        """
        Gets the thing shadow for the specified thing.

        For more information, see
        [GetThingShadow](http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html)
        in the _AWS IoT Developer Guide_.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.GetThingShadowRequest(**_params)
        response = self._boto_client.get_thing_shadow(**_request.to_boto())

        return shapes.GetThingShadowResponse.from_boto(response)

    def publish(
        self,
        _request: shapes.PublishRequest = None,
        *,
        topic: str,
        qos: int = ShapeBase.NOT_SET,
        payload: typing.Any = ShapeBase.NOT_SET,
    ) -> None:
        """
        Publishes state information.

        For more information, see [HTTP
        Protocol](http://docs.aws.amazon.com/iot/latest/developerguide/protocols.html#http)
        in the _AWS IoT Developer Guide_.
        """
        if _request is None:
            _params = {}
            if topic is not ShapeBase.NOT_SET:
                _params['topic'] = topic
            if qos is not ShapeBase.NOT_SET:
                _params['qos'] = qos
            if payload is not ShapeBase.NOT_SET:
                _params['payload'] = payload
            _request = shapes.PublishRequest(**_params)
        response = self._boto_client.publish(**_request.to_boto())

    def update_thing_shadow(
        self,
        _request: shapes.UpdateThingShadowRequest = None,
        *,
        thing_name: str,
        payload: typing.Any,
    ) -> shapes.UpdateThingShadowResponse:
        """
        Updates the thing shadow for the specified thing.

        For more information, see
        [UpdateThingShadow](http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html)
        in the _AWS IoT Developer Guide_.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if payload is not ShapeBase.NOT_SET:
                _params['payload'] = payload
            _request = shapes.UpdateThingShadowRequest(**_params)
        response = self._boto_client.update_thing_shadow(**_request.to_boto())

        return shapes.UpdateThingShadowResponse.from_boto(response)
