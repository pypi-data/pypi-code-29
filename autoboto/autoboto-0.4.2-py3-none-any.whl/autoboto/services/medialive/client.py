import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("medialive", *args, **kwargs)

    def batch_update_schedule(
        self,
        _request: shapes.BatchUpdateScheduleRequest = None,
        *,
        channel_id: str,
        creates: shapes.BatchScheduleActionCreateRequest = ShapeBase.NOT_SET,
        deletes: shapes.BatchScheduleActionDeleteRequest = ShapeBase.NOT_SET,
    ) -> shapes.BatchUpdateScheduleResponse:
        """
        Update a channel schedule
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            if creates is not ShapeBase.NOT_SET:
                _params['creates'] = creates
            if deletes is not ShapeBase.NOT_SET:
                _params['deletes'] = deletes
            _request = shapes.BatchUpdateScheduleRequest(**_params)
        response = self._boto_client.batch_update_schedule(**_request.to_boto())

        return shapes.BatchUpdateScheduleResponse.from_boto(response)

    def create_channel(
        self,
        _request: shapes.CreateChannelRequest = None,
        *,
        destinations: typing.List[shapes.OutputDestination] = ShapeBase.NOT_SET,
        encoder_settings: shapes.EncoderSettings = ShapeBase.NOT_SET,
        input_attachments: typing.List[shapes.InputAttachment
                                      ] = ShapeBase.NOT_SET,
        input_specification: shapes.InputSpecification = ShapeBase.NOT_SET,
        log_level: typing.Union[str, shapes.LogLevel] = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        request_id: str = ShapeBase.NOT_SET,
        reserved: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateChannelResponse:
        """
        Creates a new channel
        """
        if _request is None:
            _params = {}
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            if encoder_settings is not ShapeBase.NOT_SET:
                _params['encoder_settings'] = encoder_settings
            if input_attachments is not ShapeBase.NOT_SET:
                _params['input_attachments'] = input_attachments
            if input_specification is not ShapeBase.NOT_SET:
                _params['input_specification'] = input_specification
            if log_level is not ShapeBase.NOT_SET:
                _params['log_level'] = log_level
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if request_id is not ShapeBase.NOT_SET:
                _params['request_id'] = request_id
            if reserved is not ShapeBase.NOT_SET:
                _params['reserved'] = reserved
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.CreateChannelRequest(**_params)
        response = self._boto_client.create_channel(**_request.to_boto())

        return shapes.CreateChannelResponse.from_boto(response)

    def create_input(
        self,
        _request: shapes.CreateInputRequest = None,
        *,
        destinations: typing.List[shapes.InputDestinationRequest
                                 ] = ShapeBase.NOT_SET,
        input_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        request_id: str = ShapeBase.NOT_SET,
        sources: typing.List[shapes.InputSourceRequest] = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.InputType] = ShapeBase.NOT_SET,
    ) -> shapes.CreateInputResponse:
        """
        Create an input
        """
        if _request is None:
            _params = {}
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            if input_security_groups is not ShapeBase.NOT_SET:
                _params['input_security_groups'] = input_security_groups
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if request_id is not ShapeBase.NOT_SET:
                _params['request_id'] = request_id
            if sources is not ShapeBase.NOT_SET:
                _params['sources'] = sources
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            _request = shapes.CreateInputRequest(**_params)
        response = self._boto_client.create_input(**_request.to_boto())

        return shapes.CreateInputResponse.from_boto(response)

    def create_input_security_group(
        self,
        _request: shapes.CreateInputSecurityGroupRequest = None,
        *,
        whitelist_rules: typing.List[shapes.InputWhitelistRuleCidr
                                    ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateInputSecurityGroupResponse:
        """
        Creates a Input Security Group
        """
        if _request is None:
            _params = {}
            if whitelist_rules is not ShapeBase.NOT_SET:
                _params['whitelist_rules'] = whitelist_rules
            _request = shapes.CreateInputSecurityGroupRequest(**_params)
        response = self._boto_client.create_input_security_group(
            **_request.to_boto()
        )

        return shapes.CreateInputSecurityGroupResponse.from_boto(response)

    def delete_channel(
        self,
        _request: shapes.DeleteChannelRequest = None,
        *,
        channel_id: str,
    ) -> shapes.DeleteChannelResponse:
        """
        Starts deletion of channel. The associated outputs are also deleted.
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            _request = shapes.DeleteChannelRequest(**_params)
        response = self._boto_client.delete_channel(**_request.to_boto())

        return shapes.DeleteChannelResponse.from_boto(response)

    def delete_input(
        self,
        _request: shapes.DeleteInputRequest = None,
        *,
        input_id: str,
    ) -> shapes.DeleteInputResponse:
        """
        Deletes the input end point
        """
        if _request is None:
            _params = {}
            if input_id is not ShapeBase.NOT_SET:
                _params['input_id'] = input_id
            _request = shapes.DeleteInputRequest(**_params)
        response = self._boto_client.delete_input(**_request.to_boto())

        return shapes.DeleteInputResponse.from_boto(response)

    def delete_input_security_group(
        self,
        _request: shapes.DeleteInputSecurityGroupRequest = None,
        *,
        input_security_group_id: str,
    ) -> shapes.DeleteInputSecurityGroupResponse:
        """
        Deletes an Input Security Group
        """
        if _request is None:
            _params = {}
            if input_security_group_id is not ShapeBase.NOT_SET:
                _params['input_security_group_id'] = input_security_group_id
            _request = shapes.DeleteInputSecurityGroupRequest(**_params)
        response = self._boto_client.delete_input_security_group(
            **_request.to_boto()
        )

        return shapes.DeleteInputSecurityGroupResponse.from_boto(response)

    def delete_reservation(
        self,
        _request: shapes.DeleteReservationRequest = None,
        *,
        reservation_id: str,
    ) -> shapes.DeleteReservationResponse:
        """
        Delete an expired reservation.
        """
        if _request is None:
            _params = {}
            if reservation_id is not ShapeBase.NOT_SET:
                _params['reservation_id'] = reservation_id
            _request = shapes.DeleteReservationRequest(**_params)
        response = self._boto_client.delete_reservation(**_request.to_boto())

        return shapes.DeleteReservationResponse.from_boto(response)

    def describe_channel(
        self,
        _request: shapes.DescribeChannelRequest = None,
        *,
        channel_id: str,
    ) -> shapes.DescribeChannelResponse:
        """
        Gets details about a channel
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            _request = shapes.DescribeChannelRequest(**_params)
        response = self._boto_client.describe_channel(**_request.to_boto())

        return shapes.DescribeChannelResponse.from_boto(response)

    def describe_input(
        self,
        _request: shapes.DescribeInputRequest = None,
        *,
        input_id: str,
    ) -> shapes.DescribeInputResponse:
        """
        Produces details about an input
        """
        if _request is None:
            _params = {}
            if input_id is not ShapeBase.NOT_SET:
                _params['input_id'] = input_id
            _request = shapes.DescribeInputRequest(**_params)
        response = self._boto_client.describe_input(**_request.to_boto())

        return shapes.DescribeInputResponse.from_boto(response)

    def describe_input_security_group(
        self,
        _request: shapes.DescribeInputSecurityGroupRequest = None,
        *,
        input_security_group_id: str,
    ) -> shapes.DescribeInputSecurityGroupResponse:
        """
        Produces a summary of an Input Security Group
        """
        if _request is None:
            _params = {}
            if input_security_group_id is not ShapeBase.NOT_SET:
                _params['input_security_group_id'] = input_security_group_id
            _request = shapes.DescribeInputSecurityGroupRequest(**_params)
        response = self._boto_client.describe_input_security_group(
            **_request.to_boto()
        )

        return shapes.DescribeInputSecurityGroupResponse.from_boto(response)

    def describe_offering(
        self,
        _request: shapes.DescribeOfferingRequest = None,
        *,
        offering_id: str,
    ) -> shapes.DescribeOfferingResponse:
        """
        Get details for an offering.
        """
        if _request is None:
            _params = {}
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            _request = shapes.DescribeOfferingRequest(**_params)
        response = self._boto_client.describe_offering(**_request.to_boto())

        return shapes.DescribeOfferingResponse.from_boto(response)

    def describe_reservation(
        self,
        _request: shapes.DescribeReservationRequest = None,
        *,
        reservation_id: str,
    ) -> shapes.DescribeReservationResponse:
        """
        Get details for a reservation.
        """
        if _request is None:
            _params = {}
            if reservation_id is not ShapeBase.NOT_SET:
                _params['reservation_id'] = reservation_id
            _request = shapes.DescribeReservationRequest(**_params)
        response = self._boto_client.describe_reservation(**_request.to_boto())

        return shapes.DescribeReservationResponse.from_boto(response)

    def describe_schedule(
        self,
        _request: shapes.DescribeScheduleRequest = None,
        *,
        channel_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScheduleResponse:
        """
        Get a channel schedule
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScheduleRequest(**_params)
        paginator = self.get_paginator("describe_schedule").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeScheduleResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeScheduleResponse.from_boto(response)

    def list_channels(
        self,
        _request: shapes.ListChannelsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListChannelsResponse:
        """
        Produces list of channels that have been created
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListChannelsRequest(**_params)
        paginator = self.get_paginator("list_channels").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListChannelsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListChannelsResponse.from_boto(response)

    def list_input_security_groups(
        self,
        _request: shapes.ListInputSecurityGroupsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInputSecurityGroupsResponse:
        """
        Produces a list of Input Security Groups for an account
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListInputSecurityGroupsRequest(**_params)
        paginator = self.get_paginator("list_input_security_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInputSecurityGroupsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInputSecurityGroupsResponse.from_boto(response)

    def list_inputs(
        self,
        _request: shapes.ListInputsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInputsResponse:
        """
        Produces list of inputs that have been created
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListInputsRequest(**_params)
        paginator = self.get_paginator("list_inputs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListInputsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListInputsResponse.from_boto(response)

    def list_offerings(
        self,
        _request: shapes.ListOfferingsRequest = None,
        *,
        channel_configuration: str = ShapeBase.NOT_SET,
        codec: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        maximum_bitrate: str = ShapeBase.NOT_SET,
        maximum_framerate: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        resolution: str = ShapeBase.NOT_SET,
        resource_type: str = ShapeBase.NOT_SET,
        special_feature: str = ShapeBase.NOT_SET,
        video_quality: str = ShapeBase.NOT_SET,
    ) -> shapes.ListOfferingsResponse:
        """
        List offerings available for purchase.
        """
        if _request is None:
            _params = {}
            if channel_configuration is not ShapeBase.NOT_SET:
                _params['channel_configuration'] = channel_configuration
            if codec is not ShapeBase.NOT_SET:
                _params['codec'] = codec
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if maximum_bitrate is not ShapeBase.NOT_SET:
                _params['maximum_bitrate'] = maximum_bitrate
            if maximum_framerate is not ShapeBase.NOT_SET:
                _params['maximum_framerate'] = maximum_framerate
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if resolution is not ShapeBase.NOT_SET:
                _params['resolution'] = resolution
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if special_feature is not ShapeBase.NOT_SET:
                _params['special_feature'] = special_feature
            if video_quality is not ShapeBase.NOT_SET:
                _params['video_quality'] = video_quality
            _request = shapes.ListOfferingsRequest(**_params)
        paginator = self.get_paginator("list_offerings").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOfferingsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOfferingsResponse.from_boto(response)

    def list_reservations(
        self,
        _request: shapes.ListReservationsRequest = None,
        *,
        codec: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        maximum_bitrate: str = ShapeBase.NOT_SET,
        maximum_framerate: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        resolution: str = ShapeBase.NOT_SET,
        resource_type: str = ShapeBase.NOT_SET,
        special_feature: str = ShapeBase.NOT_SET,
        video_quality: str = ShapeBase.NOT_SET,
    ) -> shapes.ListReservationsResponse:
        """
        List purchased reservations.
        """
        if _request is None:
            _params = {}
            if codec is not ShapeBase.NOT_SET:
                _params['codec'] = codec
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if maximum_bitrate is not ShapeBase.NOT_SET:
                _params['maximum_bitrate'] = maximum_bitrate
            if maximum_framerate is not ShapeBase.NOT_SET:
                _params['maximum_framerate'] = maximum_framerate
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if resolution is not ShapeBase.NOT_SET:
                _params['resolution'] = resolution
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if special_feature is not ShapeBase.NOT_SET:
                _params['special_feature'] = special_feature
            if video_quality is not ShapeBase.NOT_SET:
                _params['video_quality'] = video_quality
            _request = shapes.ListReservationsRequest(**_params)
        paginator = self.get_paginator("list_reservations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListReservationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListReservationsResponse.from_boto(response)

    def purchase_offering(
        self,
        _request: shapes.PurchaseOfferingRequest = None,
        *,
        offering_id: str,
        count: int = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        request_id: str = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseOfferingResponse:
        """
        Purchase an offering and create a reservation.
        """
        if _request is None:
            _params = {}
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            if count is not ShapeBase.NOT_SET:
                _params['count'] = count
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if request_id is not ShapeBase.NOT_SET:
                _params['request_id'] = request_id
            _request = shapes.PurchaseOfferingRequest(**_params)
        response = self._boto_client.purchase_offering(**_request.to_boto())

        return shapes.PurchaseOfferingResponse.from_boto(response)

    def start_channel(
        self,
        _request: shapes.StartChannelRequest = None,
        *,
        channel_id: str,
    ) -> shapes.StartChannelResponse:
        """
        Starts an existing channel
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            _request = shapes.StartChannelRequest(**_params)
        response = self._boto_client.start_channel(**_request.to_boto())

        return shapes.StartChannelResponse.from_boto(response)

    def stop_channel(
        self,
        _request: shapes.StopChannelRequest = None,
        *,
        channel_id: str,
    ) -> shapes.StopChannelResponse:
        """
        Stops a running channel
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            _request = shapes.StopChannelRequest(**_params)
        response = self._boto_client.stop_channel(**_request.to_boto())

        return shapes.StopChannelResponse.from_boto(response)

    def update_channel(
        self,
        _request: shapes.UpdateChannelRequest = None,
        *,
        channel_id: str,
        destinations: typing.List[shapes.OutputDestination] = ShapeBase.NOT_SET,
        encoder_settings: shapes.EncoderSettings = ShapeBase.NOT_SET,
        input_attachments: typing.List[shapes.InputAttachment
                                      ] = ShapeBase.NOT_SET,
        input_specification: shapes.InputSpecification = ShapeBase.NOT_SET,
        log_level: typing.Union[str, shapes.LogLevel] = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateChannelResponse:
        """
        Updates a channel.
        """
        if _request is None:
            _params = {}
            if channel_id is not ShapeBase.NOT_SET:
                _params['channel_id'] = channel_id
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            if encoder_settings is not ShapeBase.NOT_SET:
                _params['encoder_settings'] = encoder_settings
            if input_attachments is not ShapeBase.NOT_SET:
                _params['input_attachments'] = input_attachments
            if input_specification is not ShapeBase.NOT_SET:
                _params['input_specification'] = input_specification
            if log_level is not ShapeBase.NOT_SET:
                _params['log_level'] = log_level
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.UpdateChannelRequest(**_params)
        response = self._boto_client.update_channel(**_request.to_boto())

        return shapes.UpdateChannelResponse.from_boto(response)

    def update_input(
        self,
        _request: shapes.UpdateInputRequest = None,
        *,
        input_id: str,
        destinations: typing.List[shapes.InputDestinationRequest
                                 ] = ShapeBase.NOT_SET,
        input_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        sources: typing.List[shapes.InputSourceRequest] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateInputResponse:
        """
        Updates an input.
        """
        if _request is None:
            _params = {}
            if input_id is not ShapeBase.NOT_SET:
                _params['input_id'] = input_id
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            if input_security_groups is not ShapeBase.NOT_SET:
                _params['input_security_groups'] = input_security_groups
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if sources is not ShapeBase.NOT_SET:
                _params['sources'] = sources
            _request = shapes.UpdateInputRequest(**_params)
        response = self._boto_client.update_input(**_request.to_boto())

        return shapes.UpdateInputResponse.from_boto(response)

    def update_input_security_group(
        self,
        _request: shapes.UpdateInputSecurityGroupRequest = None,
        *,
        input_security_group_id: str,
        whitelist_rules: typing.List[shapes.InputWhitelistRuleCidr
                                    ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateInputSecurityGroupResponse:
        """
        Update an Input Security Group's Whilelists.
        """
        if _request is None:
            _params = {}
            if input_security_group_id is not ShapeBase.NOT_SET:
                _params['input_security_group_id'] = input_security_group_id
            if whitelist_rules is not ShapeBase.NOT_SET:
                _params['whitelist_rules'] = whitelist_rules
            _request = shapes.UpdateInputSecurityGroupRequest(**_params)
        response = self._boto_client.update_input_security_group(
            **_request.to_boto()
        )

        return shapes.UpdateInputSecurityGroupResponse.from_boto(response)
