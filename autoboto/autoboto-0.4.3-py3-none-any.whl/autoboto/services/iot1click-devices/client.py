import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iot1click-devices", *args, **kwargs)

    def claim_devices_by_claim_code(
        self,
        _request: shapes.ClaimDevicesByClaimCodeRequest = None,
        *,
        claim_code: str,
    ) -> shapes.ClaimDevicesByClaimCodeResponse:
        """
        Adds device(s) to your account (i.e., claim one or more devices) if and only if
        you received a claim code with the device(s).
        """
        if _request is None:
            _params = {}
            if claim_code is not ShapeBase.NOT_SET:
                _params['claim_code'] = claim_code
            _request = shapes.ClaimDevicesByClaimCodeRequest(**_params)
        response = self._boto_client.claim_devices_by_claim_code(
            **_request.to_boto()
        )

        return shapes.ClaimDevicesByClaimCodeResponse.from_boto(response)

    def describe_device(
        self,
        _request: shapes.DescribeDeviceRequest = None,
        *,
        device_id: str,
    ) -> shapes.DescribeDeviceResponse:
        """
        Given a device ID, returns a DescribeDeviceResponse object describing the
        details of the device.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.DescribeDeviceRequest(**_params)
        response = self._boto_client.describe_device(**_request.to_boto())

        return shapes.DescribeDeviceResponse.from_boto(response)

    def finalize_device_claim(
        self,
        _request: shapes.FinalizeDeviceClaimRequest = None,
        *,
        device_id: str,
    ) -> shapes.FinalizeDeviceClaimResponse:
        """
        Given a device ID, finalizes the claim request for the associated device.

        Claiming a device consists of initiating a claim, then publishing a device
        event, and finalizing the claim. For a device of type button, a device event can
        be published by simply clicking the device.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.FinalizeDeviceClaimRequest(**_params)
        response = self._boto_client.finalize_device_claim(**_request.to_boto())

        return shapes.FinalizeDeviceClaimResponse.from_boto(response)

    def get_device_methods(
        self,
        _request: shapes.GetDeviceMethodsRequest = None,
        *,
        device_id: str,
    ) -> shapes.GetDeviceMethodsResponse:
        """
        Given a device ID, returns the invokable methods associated with the device.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.GetDeviceMethodsRequest(**_params)
        response = self._boto_client.get_device_methods(**_request.to_boto())

        return shapes.GetDeviceMethodsResponse.from_boto(response)

    def initiate_device_claim(
        self,
        _request: shapes.InitiateDeviceClaimRequest = None,
        *,
        device_id: str,
    ) -> shapes.InitiateDeviceClaimResponse:
        """
        Given a device ID, initiates a claim request for the associated device.

        Claiming a device consists of initiating a claim, then publishing a device
        event, and finalizing the claim. For a device of type button, a device event can
        be published by simply clicking the device.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.InitiateDeviceClaimRequest(**_params)
        response = self._boto_client.initiate_device_claim(**_request.to_boto())

        return shapes.InitiateDeviceClaimResponse.from_boto(response)

    def invoke_device_method(
        self,
        _request: shapes.InvokeDeviceMethodRequest = None,
        *,
        device_id: str,
        device_method: shapes.DeviceMethod = ShapeBase.NOT_SET,
        device_method_parameters: str = ShapeBase.NOT_SET,
    ) -> shapes.InvokeDeviceMethodResponse:
        """
        Given a device ID, issues a request to invoke a named device method (with
        possible parameters). See the "Example POST" code snippet below.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            if device_method is not ShapeBase.NOT_SET:
                _params['device_method'] = device_method
            if device_method_parameters is not ShapeBase.NOT_SET:
                _params['device_method_parameters'] = device_method_parameters
            _request = shapes.InvokeDeviceMethodRequest(**_params)
        response = self._boto_client.invoke_device_method(**_request.to_boto())

        return shapes.InvokeDeviceMethodResponse.from_boto(response)

    def list_device_events(
        self,
        _request: shapes.ListDeviceEventsRequest = None,
        *,
        device_id: str,
        from_time_stamp: datetime.datetime,
        to_time_stamp: datetime.datetime,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeviceEventsResponse:
        """
        Using a device ID, returns a DeviceEventsResponse object containing an array of
        events for the device.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            if from_time_stamp is not ShapeBase.NOT_SET:
                _params['from_time_stamp'] = from_time_stamp
            if to_time_stamp is not ShapeBase.NOT_SET:
                _params['to_time_stamp'] = to_time_stamp
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeviceEventsRequest(**_params)
        response = self._boto_client.list_device_events(**_request.to_boto())

        return shapes.ListDeviceEventsResponse.from_boto(response)

    def list_devices(
        self,
        _request: shapes.ListDevicesRequest = None,
        *,
        device_type: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDevicesResponse:
        """
        Lists the 1-Click compatible devices associated with your AWS account.
        """
        if _request is None:
            _params = {}
            if device_type is not ShapeBase.NOT_SET:
                _params['device_type'] = device_type
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDevicesRequest(**_params)
        response = self._boto_client.list_devices(**_request.to_boto())

        return shapes.ListDevicesResponse.from_boto(response)

    def unclaim_device(
        self,
        _request: shapes.UnclaimDeviceRequest = None,
        *,
        device_id: str,
    ) -> shapes.UnclaimDeviceResponse:
        """
        Disassociates a device from your AWS account using its device ID.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            _request = shapes.UnclaimDeviceRequest(**_params)
        response = self._boto_client.unclaim_device(**_request.to_boto())

        return shapes.UnclaimDeviceResponse.from_boto(response)

    def update_device_state(
        self,
        _request: shapes.UpdateDeviceStateRequest = None,
        *,
        device_id: str,
        enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDeviceStateResponse:
        """
        Using a Boolean value (true or false), this operation enables or disables the
        device given a device ID.
        """
        if _request is None:
            _params = {}
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.UpdateDeviceStateRequest(**_params)
        response = self._boto_client.update_device_state(**_request.to_boto())

        return shapes.UpdateDeviceStateResponse.from_boto(response)
