import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("appstream", *args, **kwargs)

    def associate_fleet(
        self,
        _request: shapes.AssociateFleetRequest = None,
        *,
        fleet_name: str,
        stack_name: str,
    ) -> shapes.AssociateFleetResult:
        """
        Associates the specified fleet with the specified stack.
        """
        if _request is None:
            _params = {}
            if fleet_name is not ShapeBase.NOT_SET:
                _params['fleet_name'] = fleet_name
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            _request = shapes.AssociateFleetRequest(**_params)
        response = self._boto_client.associate_fleet(**_request.to_boto())

        return shapes.AssociateFleetResult.from_boto(response)

    def copy_image(
        self,
        _request: shapes.CopyImageRequest = None,
        *,
        source_image_name: str,
        destination_image_name: str,
        destination_region: str,
        destination_image_description: str = ShapeBase.NOT_SET,
    ) -> shapes.CopyImageResponse:
        """
        Copies the image within the same region or to a new region within the same AWS
        account. Note that any tags you added to the image will not be copied.
        """
        if _request is None:
            _params = {}
            if source_image_name is not ShapeBase.NOT_SET:
                _params['source_image_name'] = source_image_name
            if destination_image_name is not ShapeBase.NOT_SET:
                _params['destination_image_name'] = destination_image_name
            if destination_region is not ShapeBase.NOT_SET:
                _params['destination_region'] = destination_region
            if destination_image_description is not ShapeBase.NOT_SET:
                _params['destination_image_description'
                       ] = destination_image_description
            _request = shapes.CopyImageRequest(**_params)
        response = self._boto_client.copy_image(**_request.to_boto())

        return shapes.CopyImageResponse.from_boto(response)

    def create_directory_config(
        self,
        _request: shapes.CreateDirectoryConfigRequest = None,
        *,
        directory_name: str,
        organizational_unit_distinguished_names: typing.List[str],
        service_account_credentials: shapes.ServiceAccountCredentials,
    ) -> shapes.CreateDirectoryConfigResult:
        """
        Creates a Directory Config object in AppStream 2.0. This object includes the
        information required to join streaming instances to an Active Directory domain.
        """
        if _request is None:
            _params = {}
            if directory_name is not ShapeBase.NOT_SET:
                _params['directory_name'] = directory_name
            if organizational_unit_distinguished_names is not ShapeBase.NOT_SET:
                _params['organizational_unit_distinguished_names'
                       ] = organizational_unit_distinguished_names
            if service_account_credentials is not ShapeBase.NOT_SET:
                _params['service_account_credentials'
                       ] = service_account_credentials
            _request = shapes.CreateDirectoryConfigRequest(**_params)
        response = self._boto_client.create_directory_config(
            **_request.to_boto()
        )

        return shapes.CreateDirectoryConfigResult.from_boto(response)

    def create_fleet(
        self,
        _request: shapes.CreateFleetRequest = None,
        *,
        name: str,
        instance_type: str,
        compute_capacity: shapes.ComputeCapacity,
        image_name: str = ShapeBase.NOT_SET,
        image_arn: str = ShapeBase.NOT_SET,
        fleet_type: typing.Union[str, shapes.FleetType] = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
        max_user_duration_in_seconds: int = ShapeBase.NOT_SET,
        disconnect_timeout_in_seconds: int = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        display_name: str = ShapeBase.NOT_SET,
        enable_default_internet_access: bool = ShapeBase.NOT_SET,
        domain_join_info: shapes.DomainJoinInfo = ShapeBase.NOT_SET,
    ) -> shapes.CreateFleetResult:
        """
        Creates a fleet. A fleet consists of streaming instances that run a specified
        image.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if compute_capacity is not ShapeBase.NOT_SET:
                _params['compute_capacity'] = compute_capacity
            if image_name is not ShapeBase.NOT_SET:
                _params['image_name'] = image_name
            if image_arn is not ShapeBase.NOT_SET:
                _params['image_arn'] = image_arn
            if fleet_type is not ShapeBase.NOT_SET:
                _params['fleet_type'] = fleet_type
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if max_user_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['max_user_duration_in_seconds'
                       ] = max_user_duration_in_seconds
            if disconnect_timeout_in_seconds is not ShapeBase.NOT_SET:
                _params['disconnect_timeout_in_seconds'
                       ] = disconnect_timeout_in_seconds
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if enable_default_internet_access is not ShapeBase.NOT_SET:
                _params['enable_default_internet_access'
                       ] = enable_default_internet_access
            if domain_join_info is not ShapeBase.NOT_SET:
                _params['domain_join_info'] = domain_join_info
            _request = shapes.CreateFleetRequest(**_params)
        response = self._boto_client.create_fleet(**_request.to_boto())

        return shapes.CreateFleetResult.from_boto(response)

    def create_image_builder(
        self,
        _request: shapes.CreateImageBuilderRequest = None,
        *,
        name: str,
        instance_type: str,
        image_name: str = ShapeBase.NOT_SET,
        image_arn: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        display_name: str = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
        enable_default_internet_access: bool = ShapeBase.NOT_SET,
        domain_join_info: shapes.DomainJoinInfo = ShapeBase.NOT_SET,
        appstream_agent_version: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateImageBuilderResult:
        """
        Creates an image builder. An image builder is a virtual machine that is used to
        create an image.

        The initial state of the builder is `PENDING`. When it is ready, the state is
        `RUNNING`.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if image_name is not ShapeBase.NOT_SET:
                _params['image_name'] = image_name
            if image_arn is not ShapeBase.NOT_SET:
                _params['image_arn'] = image_arn
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if enable_default_internet_access is not ShapeBase.NOT_SET:
                _params['enable_default_internet_access'
                       ] = enable_default_internet_access
            if domain_join_info is not ShapeBase.NOT_SET:
                _params['domain_join_info'] = domain_join_info
            if appstream_agent_version is not ShapeBase.NOT_SET:
                _params['appstream_agent_version'] = appstream_agent_version
            _request = shapes.CreateImageBuilderRequest(**_params)
        response = self._boto_client.create_image_builder(**_request.to_boto())

        return shapes.CreateImageBuilderResult.from_boto(response)

    def create_image_builder_streaming_url(
        self,
        _request: shapes.CreateImageBuilderStreamingURLRequest = None,
        *,
        name: str,
        validity: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateImageBuilderStreamingURLResult:
        """
        Creates a URL to start an image builder streaming session.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if validity is not ShapeBase.NOT_SET:
                _params['validity'] = validity
            _request = shapes.CreateImageBuilderStreamingURLRequest(**_params)
        response = self._boto_client.create_image_builder_streaming_url(
            **_request.to_boto()
        )

        return shapes.CreateImageBuilderStreamingURLResult.from_boto(response)

    def create_stack(
        self,
        _request: shapes.CreateStackRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        display_name: str = ShapeBase.NOT_SET,
        storage_connectors: typing.List[shapes.StorageConnector
                                       ] = ShapeBase.NOT_SET,
        redirect_url: str = ShapeBase.NOT_SET,
        feedback_url: str = ShapeBase.NOT_SET,
        user_settings: typing.List[shapes.UserSetting] = ShapeBase.NOT_SET,
        application_settings: shapes.ApplicationSettings = ShapeBase.NOT_SET,
    ) -> shapes.CreateStackResult:
        """
        Creates a stack to start streaming applications to users. A stack consists of an
        associated fleet, user access policies, and storage configurations.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if storage_connectors is not ShapeBase.NOT_SET:
                _params['storage_connectors'] = storage_connectors
            if redirect_url is not ShapeBase.NOT_SET:
                _params['redirect_url'] = redirect_url
            if feedback_url is not ShapeBase.NOT_SET:
                _params['feedback_url'] = feedback_url
            if user_settings is not ShapeBase.NOT_SET:
                _params['user_settings'] = user_settings
            if application_settings is not ShapeBase.NOT_SET:
                _params['application_settings'] = application_settings
            _request = shapes.CreateStackRequest(**_params)
        response = self._boto_client.create_stack(**_request.to_boto())

        return shapes.CreateStackResult.from_boto(response)

    def create_streaming_url(
        self,
        _request: shapes.CreateStreamingURLRequest = None,
        *,
        stack_name: str,
        fleet_name: str,
        user_id: str,
        application_id: str = ShapeBase.NOT_SET,
        validity: int = ShapeBase.NOT_SET,
        session_context: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateStreamingURLResult:
        """
        Creates a temporary URL to start an AppStream 2.0 streaming session for the
        specified user. A streaming URL enables application streaming to be tested
        without user setup.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if fleet_name is not ShapeBase.NOT_SET:
                _params['fleet_name'] = fleet_name
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if validity is not ShapeBase.NOT_SET:
                _params['validity'] = validity
            if session_context is not ShapeBase.NOT_SET:
                _params['session_context'] = session_context
            _request = shapes.CreateStreamingURLRequest(**_params)
        response = self._boto_client.create_streaming_url(**_request.to_boto())

        return shapes.CreateStreamingURLResult.from_boto(response)

    def delete_directory_config(
        self,
        _request: shapes.DeleteDirectoryConfigRequest = None,
        *,
        directory_name: str,
    ) -> shapes.DeleteDirectoryConfigResult:
        """
        Deletes the specified Directory Config object from AppStream 2.0. This object
        includes the information required to join streaming instances to an Active
        Directory domain.
        """
        if _request is None:
            _params = {}
            if directory_name is not ShapeBase.NOT_SET:
                _params['directory_name'] = directory_name
            _request = shapes.DeleteDirectoryConfigRequest(**_params)
        response = self._boto_client.delete_directory_config(
            **_request.to_boto()
        )

        return shapes.DeleteDirectoryConfigResult.from_boto(response)

    def delete_fleet(
        self,
        _request: shapes.DeleteFleetRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteFleetResult:
        """
        Deletes the specified fleet.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteFleetRequest(**_params)
        response = self._boto_client.delete_fleet(**_request.to_boto())

        return shapes.DeleteFleetResult.from_boto(response)

    def delete_image(
        self,
        _request: shapes.DeleteImageRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteImageResult:
        """
        Deletes the specified image. You cannot delete an image when it is in use. After
        you delete an image, you cannot provision new capacity using the image.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteImageRequest(**_params)
        response = self._boto_client.delete_image(**_request.to_boto())

        return shapes.DeleteImageResult.from_boto(response)

    def delete_image_builder(
        self,
        _request: shapes.DeleteImageBuilderRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteImageBuilderResult:
        """
        Deletes the specified image builder and releases the capacity.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteImageBuilderRequest(**_params)
        response = self._boto_client.delete_image_builder(**_request.to_boto())

        return shapes.DeleteImageBuilderResult.from_boto(response)

    def delete_image_permissions(
        self,
        _request: shapes.DeleteImagePermissionsRequest = None,
        *,
        name: str,
        shared_account_id: str,
    ) -> shapes.DeleteImagePermissionsResult:
        """
        Deletes permissions for the specified private image. After you delete
        permissions for an image, AWS accounts to which you previously granted these
        permissions can no longer use the image.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if shared_account_id is not ShapeBase.NOT_SET:
                _params['shared_account_id'] = shared_account_id
            _request = shapes.DeleteImagePermissionsRequest(**_params)
        response = self._boto_client.delete_image_permissions(
            **_request.to_boto()
        )

        return shapes.DeleteImagePermissionsResult.from_boto(response)

    def delete_stack(
        self,
        _request: shapes.DeleteStackRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteStackResult:
        """
        Deletes the specified stack. After the stack is deleted, the application
        streaming environment provided by the stack is no longer available to users.
        Also, any reservations made for application streaming sessions for the stack are
        released.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteStackRequest(**_params)
        response = self._boto_client.delete_stack(**_request.to_boto())

        return shapes.DeleteStackResult.from_boto(response)

    def describe_directory_configs(
        self,
        _request: shapes.DescribeDirectoryConfigsRequest = None,
        *,
        directory_names: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDirectoryConfigsResult:
        """
        Retrieves a list that describes one or more specified Directory Config objects
        for AppStream 2.0, if the names for these objects are provided. Otherwise, all
        Directory Config objects in the account are described. These objects include the
        information required to join streaming instances to an Active Directory domain.

        Although the response syntax in this topic includes the account password, this
        password is not returned in the actual response.
        """
        if _request is None:
            _params = {}
            if directory_names is not ShapeBase.NOT_SET:
                _params['directory_names'] = directory_names
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeDirectoryConfigsRequest(**_params)
        response = self._boto_client.describe_directory_configs(
            **_request.to_boto()
        )

        return shapes.DescribeDirectoryConfigsResult.from_boto(response)

    def describe_fleets(
        self,
        _request: shapes.DescribeFleetsRequest = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetsResult:
        """
        Retrieves a list that describes one or more specified fleets, if the fleet names
        are provided. Otherwise, all fleets in the account are described.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFleetsRequest(**_params)
        response = self._boto_client.describe_fleets(**_request.to_boto())

        return shapes.DescribeFleetsResult.from_boto(response)

    def describe_image_builders(
        self,
        _request: shapes.DescribeImageBuildersRequest = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImageBuildersResult:
        """
        Retrieves a list that describes one or more specified image builders, if the
        image builder names are provided. Otherwise, all image builders in the account
        are described.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeImageBuildersRequest(**_params)
        response = self._boto_client.describe_image_builders(
            **_request.to_boto()
        )

        return shapes.DescribeImageBuildersResult.from_boto(response)

    def describe_image_permissions(
        self,
        _request: shapes.DescribeImagePermissionsRequest = None,
        *,
        name: str,
        max_results: int = ShapeBase.NOT_SET,
        shared_aws_account_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImagePermissionsResult:
        """
        Retrieves a list that describes the permissions for shared AWS account IDs on a
        private image that you own.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if shared_aws_account_ids is not ShapeBase.NOT_SET:
                _params['shared_aws_account_ids'] = shared_aws_account_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeImagePermissionsRequest(**_params)
        response = self._boto_client.describe_image_permissions(
            **_request.to_boto()
        )

        return shapes.DescribeImagePermissionsResult.from_boto(response)

    def describe_images(
        self,
        _request: shapes.DescribeImagesRequest = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        arns: typing.List[str] = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.VisibilityType] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImagesResult:
        """
        Retrieves a list that describes one or more specified images, if the image names
        or image ARNs are provided. Otherwise, all images in the account are described.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if arns is not ShapeBase.NOT_SET:
                _params['arns'] = arns
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeImagesRequest(**_params)
        response = self._boto_client.describe_images(**_request.to_boto())

        return shapes.DescribeImagesResult.from_boto(response)

    def describe_sessions(
        self,
        _request: shapes.DescribeSessionsRequest = None,
        *,
        stack_name: str,
        fleet_name: str,
        user_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        authentication_type: typing.
        Union[str, shapes.AuthenticationType] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSessionsResult:
        """
        Retrieves a list that describes the streaming sessions for a specified stack and
        fleet. If a user ID is provided for the stack and fleet, only streaming sessions
        for that user are described. If an authentication type is not provided, the
        default is to authenticate users using a streaming URL.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if fleet_name is not ShapeBase.NOT_SET:
                _params['fleet_name'] = fleet_name
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if authentication_type is not ShapeBase.NOT_SET:
                _params['authentication_type'] = authentication_type
            _request = shapes.DescribeSessionsRequest(**_params)
        response = self._boto_client.describe_sessions(**_request.to_boto())

        return shapes.DescribeSessionsResult.from_boto(response)

    def describe_stacks(
        self,
        _request: shapes.DescribeStacksRequest = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStacksResult:
        """
        Retrieves a list that describes one or more specified stacks, if the stack names
        are provided. Otherwise, all stacks in the account are described.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeStacksRequest(**_params)
        response = self._boto_client.describe_stacks(**_request.to_boto())

        return shapes.DescribeStacksResult.from_boto(response)

    def disassociate_fleet(
        self,
        _request: shapes.DisassociateFleetRequest = None,
        *,
        fleet_name: str,
        stack_name: str,
    ) -> shapes.DisassociateFleetResult:
        """
        Disassociates the specified fleet from the specified stack.
        """
        if _request is None:
            _params = {}
            if fleet_name is not ShapeBase.NOT_SET:
                _params['fleet_name'] = fleet_name
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            _request = shapes.DisassociateFleetRequest(**_params)
        response = self._boto_client.disassociate_fleet(**_request.to_boto())

        return shapes.DisassociateFleetResult.from_boto(response)

    def expire_session(
        self,
        _request: shapes.ExpireSessionRequest = None,
        *,
        session_id: str,
    ) -> shapes.ExpireSessionResult:
        """
        Immediately stops the specified streaming session.
        """
        if _request is None:
            _params = {}
            if session_id is not ShapeBase.NOT_SET:
                _params['session_id'] = session_id
            _request = shapes.ExpireSessionRequest(**_params)
        response = self._boto_client.expire_session(**_request.to_boto())

        return shapes.ExpireSessionResult.from_boto(response)

    def list_associated_fleets(
        self,
        _request: shapes.ListAssociatedFleetsRequest = None,
        *,
        stack_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListAssociatedFleetsResult:
        """
        Retrieves the name of the fleet that is associated with the specified stack.
        """
        if _request is None:
            _params = {}
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListAssociatedFleetsRequest(**_params)
        response = self._boto_client.list_associated_fleets(
            **_request.to_boto()
        )

        return shapes.ListAssociatedFleetsResult.from_boto(response)

    def list_associated_stacks(
        self,
        _request: shapes.ListAssociatedStacksRequest = None,
        *,
        fleet_name: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListAssociatedStacksResult:
        """
        Retrieves the name of the stack with which the specified fleet is associated.
        """
        if _request is None:
            _params = {}
            if fleet_name is not ShapeBase.NOT_SET:
                _params['fleet_name'] = fleet_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListAssociatedStacksRequest(**_params)
        response = self._boto_client.list_associated_stacks(
            **_request.to_boto()
        )

        return shapes.ListAssociatedStacksResult.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.ListTagsForResourceResponse:
        """
        Retrieves a list of all tags for the specified AppStream 2.0 resource. You can
        tag AppStream 2.0 image builders, images, fleets, and stacks.

        For more information about tags, see [Tagging Your
        Resources](http://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-
        basic.html) in the _Amazon AppStream 2.0 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResponse.from_boto(response)

    def start_fleet(
        self,
        _request: shapes.StartFleetRequest = None,
        *,
        name: str,
    ) -> shapes.StartFleetResult:
        """
        Starts the specified fleet.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StartFleetRequest(**_params)
        response = self._boto_client.start_fleet(**_request.to_boto())

        return shapes.StartFleetResult.from_boto(response)

    def start_image_builder(
        self,
        _request: shapes.StartImageBuilderRequest = None,
        *,
        name: str,
        appstream_agent_version: str = ShapeBase.NOT_SET,
    ) -> shapes.StartImageBuilderResult:
        """
        Starts the specified image builder.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if appstream_agent_version is not ShapeBase.NOT_SET:
                _params['appstream_agent_version'] = appstream_agent_version
            _request = shapes.StartImageBuilderRequest(**_params)
        response = self._boto_client.start_image_builder(**_request.to_boto())

        return shapes.StartImageBuilderResult.from_boto(response)

    def stop_fleet(
        self,
        _request: shapes.StopFleetRequest = None,
        *,
        name: str,
    ) -> shapes.StopFleetResult:
        """
        Stops the specified fleet.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StopFleetRequest(**_params)
        response = self._boto_client.stop_fleet(**_request.to_boto())

        return shapes.StopFleetResult.from_boto(response)

    def stop_image_builder(
        self,
        _request: shapes.StopImageBuilderRequest = None,
        *,
        name: str,
    ) -> shapes.StopImageBuilderResult:
        """
        Stops the specified image builder.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StopImageBuilderRequest(**_params)
        response = self._boto_client.stop_image_builder(**_request.to_boto())

        return shapes.StopImageBuilderResult.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_arn: str,
        tags: typing.Dict[str, str],
    ) -> shapes.TagResourceResponse:
        """
        Adds or overwrites one or more tags for the specified AppStream 2.0 resource.
        You can tag AppStream 2.0 image builders, images, fleets, and stacks.

        Each tag consists of a key and an optional value. If a resource already has a
        tag with the same key, this operation updates its value.

        To list the current tags for your resources, use ListTagsForResource. To
        disassociate tags from your resources, use UntagResource.

        For more information about tags, see [Tagging Your
        Resources](http://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-
        basic.html) in the _Amazon AppStream 2.0 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        Disassociates one or more specified tags from the specified AppStream 2.0
        resource.

        To list the current tags for your resources, use ListTagsForResource.

        For more information about tags, see [Tagging Your
        Resources](http://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-
        basic.html) in the _Amazon AppStream 2.0 Developer Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)

    def update_directory_config(
        self,
        _request: shapes.UpdateDirectoryConfigRequest = None,
        *,
        directory_name: str,
        organizational_unit_distinguished_names: typing.List[str] = ShapeBase.
        NOT_SET,
        service_account_credentials: shapes.
        ServiceAccountCredentials = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDirectoryConfigResult:
        """
        Updates the specified Directory Config object in AppStream 2.0. This object
        includes the information required to join streaming instances to an Active
        Directory domain.
        """
        if _request is None:
            _params = {}
            if directory_name is not ShapeBase.NOT_SET:
                _params['directory_name'] = directory_name
            if organizational_unit_distinguished_names is not ShapeBase.NOT_SET:
                _params['organizational_unit_distinguished_names'
                       ] = organizational_unit_distinguished_names
            if service_account_credentials is not ShapeBase.NOT_SET:
                _params['service_account_credentials'
                       ] = service_account_credentials
            _request = shapes.UpdateDirectoryConfigRequest(**_params)
        response = self._boto_client.update_directory_config(
            **_request.to_boto()
        )

        return shapes.UpdateDirectoryConfigResult.from_boto(response)

    def update_fleet(
        self,
        _request: shapes.UpdateFleetRequest = None,
        *,
        image_name: str = ShapeBase.NOT_SET,
        image_arn: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        instance_type: str = ShapeBase.NOT_SET,
        compute_capacity: shapes.ComputeCapacity = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
        max_user_duration_in_seconds: int = ShapeBase.NOT_SET,
        disconnect_timeout_in_seconds: int = ShapeBase.NOT_SET,
        delete_vpc_config: bool = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        display_name: str = ShapeBase.NOT_SET,
        enable_default_internet_access: bool = ShapeBase.NOT_SET,
        domain_join_info: shapes.DomainJoinInfo = ShapeBase.NOT_SET,
        attributes_to_delete: typing.List[
            typing.Union[str, shapes.FleetAttribute]] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFleetResult:
        """
        Updates the specified fleet.

        If the fleet is in the `STOPPED` state, you can update any attribute except the
        fleet name. If the fleet is in the `RUNNING` state, you can update the
        `DisplayName` and `ComputeCapacity` attributes. If the fleet is in the
        `STARTING` or `STOPPING` state, you can't update it.
        """
        if _request is None:
            _params = {}
            if image_name is not ShapeBase.NOT_SET:
                _params['image_name'] = image_name
            if image_arn is not ShapeBase.NOT_SET:
                _params['image_arn'] = image_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if compute_capacity is not ShapeBase.NOT_SET:
                _params['compute_capacity'] = compute_capacity
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if max_user_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['max_user_duration_in_seconds'
                       ] = max_user_duration_in_seconds
            if disconnect_timeout_in_seconds is not ShapeBase.NOT_SET:
                _params['disconnect_timeout_in_seconds'
                       ] = disconnect_timeout_in_seconds
            if delete_vpc_config is not ShapeBase.NOT_SET:
                _params['delete_vpc_config'] = delete_vpc_config
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if enable_default_internet_access is not ShapeBase.NOT_SET:
                _params['enable_default_internet_access'
                       ] = enable_default_internet_access
            if domain_join_info is not ShapeBase.NOT_SET:
                _params['domain_join_info'] = domain_join_info
            if attributes_to_delete is not ShapeBase.NOT_SET:
                _params['attributes_to_delete'] = attributes_to_delete
            _request = shapes.UpdateFleetRequest(**_params)
        response = self._boto_client.update_fleet(**_request.to_boto())

        return shapes.UpdateFleetResult.from_boto(response)

    def update_image_permissions(
        self,
        _request: shapes.UpdateImagePermissionsRequest = None,
        *,
        name: str,
        shared_account_id: str,
        image_permissions: shapes.ImagePermissions,
    ) -> shapes.UpdateImagePermissionsResult:
        """
        Adds or updates permissions for the specified private image.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if shared_account_id is not ShapeBase.NOT_SET:
                _params['shared_account_id'] = shared_account_id
            if image_permissions is not ShapeBase.NOT_SET:
                _params['image_permissions'] = image_permissions
            _request = shapes.UpdateImagePermissionsRequest(**_params)
        response = self._boto_client.update_image_permissions(
            **_request.to_boto()
        )

        return shapes.UpdateImagePermissionsResult.from_boto(response)

    def update_stack(
        self,
        _request: shapes.UpdateStackRequest = None,
        *,
        name: str,
        display_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        storage_connectors: typing.List[shapes.StorageConnector
                                       ] = ShapeBase.NOT_SET,
        delete_storage_connectors: bool = ShapeBase.NOT_SET,
        redirect_url: str = ShapeBase.NOT_SET,
        feedback_url: str = ShapeBase.NOT_SET,
        attributes_to_delete: typing.List[
            typing.Union[str, shapes.StackAttribute]] = ShapeBase.NOT_SET,
        user_settings: typing.List[shapes.UserSetting] = ShapeBase.NOT_SET,
        application_settings: shapes.ApplicationSettings = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStackResult:
        """
        Updates the specified fields for the specified stack.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if display_name is not ShapeBase.NOT_SET:
                _params['display_name'] = display_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if storage_connectors is not ShapeBase.NOT_SET:
                _params['storage_connectors'] = storage_connectors
            if delete_storage_connectors is not ShapeBase.NOT_SET:
                _params['delete_storage_connectors'] = delete_storage_connectors
            if redirect_url is not ShapeBase.NOT_SET:
                _params['redirect_url'] = redirect_url
            if feedback_url is not ShapeBase.NOT_SET:
                _params['feedback_url'] = feedback_url
            if attributes_to_delete is not ShapeBase.NOT_SET:
                _params['attributes_to_delete'] = attributes_to_delete
            if user_settings is not ShapeBase.NOT_SET:
                _params['user_settings'] = user_settings
            if application_settings is not ShapeBase.NOT_SET:
                _params['application_settings'] = application_settings
            _request = shapes.UpdateStackRequest(**_params)
        response = self._boto_client.update_stack(**_request.to_boto())

        return shapes.UpdateStackResult.from_boto(response)
