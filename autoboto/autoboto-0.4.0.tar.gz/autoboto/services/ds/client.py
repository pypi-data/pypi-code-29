import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ds", *args, **kwargs)

    def add_ip_routes(
        self,
        _request: shapes.AddIpRoutesRequest = None,
        *,
        directory_id: str,
        ip_routes: typing.List[shapes.IpRoute],
        update_security_group_for_directory_controllers: bool = ShapeBase.
        NOT_SET,
    ) -> shapes.AddIpRoutesResult:
        """
        If the DNS server for your on-premises domain uses a publicly addressable IP
        address, you must add a CIDR address block to correctly route traffic to and
        from your Microsoft AD on Amazon Web Services. _AddIpRoutes_ adds this address
        block. You can also use _AddIpRoutes_ to facilitate routing traffic that uses
        public IP ranges from your Microsoft AD on AWS to a peer VPC.

        Before you call _AddIpRoutes_ , ensure that all of the required permissions have
        been explicitly granted through a policy. For details about what permissions are
        required to run the _AddIpRoutes_ operation, see [AWS Directory Service API
        Permissions: Actions, Resources, and Conditions
        Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/UsingWithDS_IAM_ResourcePermissions.html).
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if ip_routes is not ShapeBase.NOT_SET:
                _params['ip_routes'] = ip_routes
            if update_security_group_for_directory_controllers is not ShapeBase.NOT_SET:
                _params['update_security_group_for_directory_controllers'
                       ] = update_security_group_for_directory_controllers
            _request = shapes.AddIpRoutesRequest(**_params)
        response = self._boto_client.add_ip_routes(**_request.to_boto())

        return shapes.AddIpRoutesResult.from_boto(response)

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceRequest = None,
        *,
        resource_id: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsToResourceResult:
        """
        Adds or overwrites one or more tags for the specified directory. Each directory
        can have a maximum of 50 tags. Each tag consists of a key and optional value.
        Tag keys must be unique to each resource.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToResourceRequest(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

        return shapes.AddTagsToResourceResult.from_boto(response)

    def cancel_schema_extension(
        self,
        _request: shapes.CancelSchemaExtensionRequest = None,
        *,
        directory_id: str,
        schema_extension_id: str,
    ) -> shapes.CancelSchemaExtensionResult:
        """
        Cancels an in-progress schema extension to a Microsoft AD directory. Once a
        schema extension has started replicating to all domain controllers, the task can
        no longer be canceled. A schema extension can be canceled during any of the
        following states; `Initializing`, `CreatingSnapshot`, and `UpdatingSchema`.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if schema_extension_id is not ShapeBase.NOT_SET:
                _params['schema_extension_id'] = schema_extension_id
            _request = shapes.CancelSchemaExtensionRequest(**_params)
        response = self._boto_client.cancel_schema_extension(
            **_request.to_boto()
        )

        return shapes.CancelSchemaExtensionResult.from_boto(response)

    def connect_directory(
        self,
        _request: shapes.ConnectDirectoryRequest = None,
        *,
        name: str,
        password: str,
        size: typing.Union[str, shapes.DirectorySize],
        connect_settings: shapes.DirectoryConnectSettings,
        short_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.ConnectDirectoryResult:
        """
        Creates an AD Connector to connect to an on-premises directory.

        Before you call _ConnectDirectory_ , ensure that all of the required permissions
        have been explicitly granted through a policy. For details about what
        permissions are required to run the _ConnectDirectory_ operation, see [AWS
        Directory Service API Permissions: Actions, Resources, and Conditions
        Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/UsingWithDS_IAM_ResourcePermissions.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if size is not ShapeBase.NOT_SET:
                _params['size'] = size
            if connect_settings is not ShapeBase.NOT_SET:
                _params['connect_settings'] = connect_settings
            if short_name is not ShapeBase.NOT_SET:
                _params['short_name'] = short_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.ConnectDirectoryRequest(**_params)
        response = self._boto_client.connect_directory(**_request.to_boto())

        return shapes.ConnectDirectoryResult.from_boto(response)

    def create_alias(
        self,
        _request: shapes.CreateAliasRequest = None,
        *,
        directory_id: str,
        alias: str,
    ) -> shapes.CreateAliasResult:
        """
        Creates an alias for a directory and assigns the alias to the directory. The
        alias is used to construct the access URL for the directory, such as
        `http://<alias>.awsapps.com`.

        After an alias has been created, it cannot be deleted or reused, so this
        operation should only be used when absolutely necessary.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if alias is not ShapeBase.NOT_SET:
                _params['alias'] = alias
            _request = shapes.CreateAliasRequest(**_params)
        response = self._boto_client.create_alias(**_request.to_boto())

        return shapes.CreateAliasResult.from_boto(response)

    def create_computer(
        self,
        _request: shapes.CreateComputerRequest = None,
        *,
        directory_id: str,
        computer_name: str,
        password: str,
        organizational_unit_distinguished_name: str = ShapeBase.NOT_SET,
        computer_attributes: typing.List[shapes.Attribute] = ShapeBase.NOT_SET,
    ) -> shapes.CreateComputerResult:
        """
        Creates a computer account in the specified directory, and joins the computer to
        the directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if computer_name is not ShapeBase.NOT_SET:
                _params['computer_name'] = computer_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if organizational_unit_distinguished_name is not ShapeBase.NOT_SET:
                _params['organizational_unit_distinguished_name'
                       ] = organizational_unit_distinguished_name
            if computer_attributes is not ShapeBase.NOT_SET:
                _params['computer_attributes'] = computer_attributes
            _request = shapes.CreateComputerRequest(**_params)
        response = self._boto_client.create_computer(**_request.to_boto())

        return shapes.CreateComputerResult.from_boto(response)

    def create_conditional_forwarder(
        self,
        _request: shapes.CreateConditionalForwarderRequest = None,
        *,
        directory_id: str,
        remote_domain_name: str,
        dns_ip_addrs: typing.List[str],
    ) -> shapes.CreateConditionalForwarderResult:
        """
        Creates a conditional forwarder associated with your AWS directory. Conditional
        forwarders are required in order to set up a trust relationship with another
        domain. The conditional forwarder points to the trusted domain.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if remote_domain_name is not ShapeBase.NOT_SET:
                _params['remote_domain_name'] = remote_domain_name
            if dns_ip_addrs is not ShapeBase.NOT_SET:
                _params['dns_ip_addrs'] = dns_ip_addrs
            _request = shapes.CreateConditionalForwarderRequest(**_params)
        response = self._boto_client.create_conditional_forwarder(
            **_request.to_boto()
        )

        return shapes.CreateConditionalForwarderResult.from_boto(response)

    def create_directory(
        self,
        _request: shapes.CreateDirectoryRequest = None,
        *,
        name: str,
        password: str,
        size: typing.Union[str, shapes.DirectorySize],
        short_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        vpc_settings: shapes.DirectoryVpcSettings = ShapeBase.NOT_SET,
    ) -> shapes.CreateDirectoryResult:
        """
        Creates a Simple AD directory.

        Before you call _CreateDirectory_ , ensure that all of the required permissions
        have been explicitly granted through a policy. For details about what
        permissions are required to run the _CreateDirectory_ operation, see [AWS
        Directory Service API Permissions: Actions, Resources, and Conditions
        Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/UsingWithDS_IAM_ResourcePermissions.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if size is not ShapeBase.NOT_SET:
                _params['size'] = size
            if short_name is not ShapeBase.NOT_SET:
                _params['short_name'] = short_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if vpc_settings is not ShapeBase.NOT_SET:
                _params['vpc_settings'] = vpc_settings
            _request = shapes.CreateDirectoryRequest(**_params)
        response = self._boto_client.create_directory(**_request.to_boto())

        return shapes.CreateDirectoryResult.from_boto(response)

    def create_microsoft_ad(
        self,
        _request: shapes.CreateMicrosoftADRequest = None,
        *,
        name: str,
        password: str,
        vpc_settings: shapes.DirectoryVpcSettings,
        short_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        edition: typing.Union[str, shapes.DirectoryEdition] = ShapeBase.NOT_SET,
    ) -> shapes.CreateMicrosoftADResult:
        """
        Creates a Microsoft AD in the AWS cloud.

        Before you call _CreateMicrosoftAD_ , ensure that all of the required
        permissions have been explicitly granted through a policy. For details about
        what permissions are required to run the _CreateMicrosoftAD_ operation, see [AWS
        Directory Service API Permissions: Actions, Resources, and Conditions
        Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/UsingWithDS_IAM_ResourcePermissions.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            if vpc_settings is not ShapeBase.NOT_SET:
                _params['vpc_settings'] = vpc_settings
            if short_name is not ShapeBase.NOT_SET:
                _params['short_name'] = short_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if edition is not ShapeBase.NOT_SET:
                _params['edition'] = edition
            _request = shapes.CreateMicrosoftADRequest(**_params)
        response = self._boto_client.create_microsoft_ad(**_request.to_boto())

        return shapes.CreateMicrosoftADResult.from_boto(response)

    def create_snapshot(
        self,
        _request: shapes.CreateSnapshotRequest = None,
        *,
        directory_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSnapshotResult:
        """
        Creates a snapshot of a Simple AD or Microsoft AD directory in the AWS cloud.

        You cannot take snapshots of AD Connector directories.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateSnapshotRequest(**_params)
        response = self._boto_client.create_snapshot(**_request.to_boto())

        return shapes.CreateSnapshotResult.from_boto(response)

    def create_trust(
        self,
        _request: shapes.CreateTrustRequest = None,
        *,
        directory_id: str,
        remote_domain_name: str,
        trust_password: str,
        trust_direction: typing.Union[str, shapes.TrustDirection],
        trust_type: typing.Union[str, shapes.TrustType] = ShapeBase.NOT_SET,
        conditional_forwarder_ip_addrs: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateTrustResult:
        """
        AWS Directory Service for Microsoft Active Directory allows you to configure
        trust relationships. For example, you can establish a trust between your
        Microsoft AD in the AWS cloud, and your existing on-premises Microsoft Active
        Directory. This would allow you to provide users and groups access to resources
        in either domain, with a single set of credentials.

        This action initiates the creation of the AWS side of a trust relationship
        between a Microsoft AD in the AWS cloud and an external domain.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if remote_domain_name is not ShapeBase.NOT_SET:
                _params['remote_domain_name'] = remote_domain_name
            if trust_password is not ShapeBase.NOT_SET:
                _params['trust_password'] = trust_password
            if trust_direction is not ShapeBase.NOT_SET:
                _params['trust_direction'] = trust_direction
            if trust_type is not ShapeBase.NOT_SET:
                _params['trust_type'] = trust_type
            if conditional_forwarder_ip_addrs is not ShapeBase.NOT_SET:
                _params['conditional_forwarder_ip_addrs'
                       ] = conditional_forwarder_ip_addrs
            _request = shapes.CreateTrustRequest(**_params)
        response = self._boto_client.create_trust(**_request.to_boto())

        return shapes.CreateTrustResult.from_boto(response)

    def delete_conditional_forwarder(
        self,
        _request: shapes.DeleteConditionalForwarderRequest = None,
        *,
        directory_id: str,
        remote_domain_name: str,
    ) -> shapes.DeleteConditionalForwarderResult:
        """
        Deletes a conditional forwarder that has been set up for your AWS directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if remote_domain_name is not ShapeBase.NOT_SET:
                _params['remote_domain_name'] = remote_domain_name
            _request = shapes.DeleteConditionalForwarderRequest(**_params)
        response = self._boto_client.delete_conditional_forwarder(
            **_request.to_boto()
        )

        return shapes.DeleteConditionalForwarderResult.from_boto(response)

    def delete_directory(
        self,
        _request: shapes.DeleteDirectoryRequest = None,
        *,
        directory_id: str,
    ) -> shapes.DeleteDirectoryResult:
        """
        Deletes an AWS Directory Service directory.

        Before you call _DeleteDirectory_ , ensure that all of the required permissions
        have been explicitly granted through a policy. For details about what
        permissions are required to run the _DeleteDirectory_ operation, see [AWS
        Directory Service API Permissions: Actions, Resources, and Conditions
        Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/UsingWithDS_IAM_ResourcePermissions.html).
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            _request = shapes.DeleteDirectoryRequest(**_params)
        response = self._boto_client.delete_directory(**_request.to_boto())

        return shapes.DeleteDirectoryResult.from_boto(response)

    def delete_snapshot(
        self,
        _request: shapes.DeleteSnapshotRequest = None,
        *,
        snapshot_id: str,
    ) -> shapes.DeleteSnapshotResult:
        """
        Deletes a directory snapshot.
        """
        if _request is None:
            _params = {}
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            _request = shapes.DeleteSnapshotRequest(**_params)
        response = self._boto_client.delete_snapshot(**_request.to_boto())

        return shapes.DeleteSnapshotResult.from_boto(response)

    def delete_trust(
        self,
        _request: shapes.DeleteTrustRequest = None,
        *,
        trust_id: str,
        delete_associated_conditional_forwarder: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteTrustResult:
        """
        Deletes an existing trust relationship between your Microsoft AD in the AWS
        cloud and an external domain.
        """
        if _request is None:
            _params = {}
            if trust_id is not ShapeBase.NOT_SET:
                _params['trust_id'] = trust_id
            if delete_associated_conditional_forwarder is not ShapeBase.NOT_SET:
                _params['delete_associated_conditional_forwarder'
                       ] = delete_associated_conditional_forwarder
            _request = shapes.DeleteTrustRequest(**_params)
        response = self._boto_client.delete_trust(**_request.to_boto())

        return shapes.DeleteTrustResult.from_boto(response)

    def deregister_event_topic(
        self,
        _request: shapes.DeregisterEventTopicRequest = None,
        *,
        directory_id: str,
        topic_name: str,
    ) -> shapes.DeregisterEventTopicResult:
        """
        Removes the specified directory as a publisher to the specified SNS topic.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if topic_name is not ShapeBase.NOT_SET:
                _params['topic_name'] = topic_name
            _request = shapes.DeregisterEventTopicRequest(**_params)
        response = self._boto_client.deregister_event_topic(
            **_request.to_boto()
        )

        return shapes.DeregisterEventTopicResult.from_boto(response)

    def describe_conditional_forwarders(
        self,
        _request: shapes.DescribeConditionalForwardersRequest = None,
        *,
        directory_id: str,
        remote_domain_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConditionalForwardersResult:
        """
        Obtains information about the conditional forwarders for this account.

        If no input parameters are provided for RemoteDomainNames, this request
        describes all conditional forwarders for the specified directory ID.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if remote_domain_names is not ShapeBase.NOT_SET:
                _params['remote_domain_names'] = remote_domain_names
            _request = shapes.DescribeConditionalForwardersRequest(**_params)
        response = self._boto_client.describe_conditional_forwarders(
            **_request.to_boto()
        )

        return shapes.DescribeConditionalForwardersResult.from_boto(response)

    def describe_directories(
        self,
        _request: shapes.DescribeDirectoriesRequest = None,
        *,
        directory_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDirectoriesResult:
        """
        Obtains information about the directories that belong to this account.

        You can retrieve information about specific directories by passing the directory
        identifiers in the _DirectoryIds_ parameter. Otherwise, all directories that
        belong to the current account are returned.

        This operation supports pagination with the use of the _NextToken_ request and
        response parameters. If more results are available, the
        _DescribeDirectoriesResult.NextToken_ member contains a token that you pass in
        the next call to DescribeDirectories to retrieve the next set of items.

        You can also specify a maximum number of return results with the _Limit_
        parameter.
        """
        if _request is None:
            _params = {}
            if directory_ids is not ShapeBase.NOT_SET:
                _params['directory_ids'] = directory_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeDirectoriesRequest(**_params)
        response = self._boto_client.describe_directories(**_request.to_boto())

        return shapes.DescribeDirectoriesResult.from_boto(response)

    def describe_domain_controllers(
        self,
        _request: shapes.DescribeDomainControllersRequest = None,
        *,
        directory_id: str,
        domain_controller_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDomainControllersResult:
        """
        Provides information about any domain controllers in your directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if domain_controller_ids is not ShapeBase.NOT_SET:
                _params['domain_controller_ids'] = domain_controller_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeDomainControllersRequest(**_params)
        paginator = self.get_paginator("describe_domain_controllers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeDomainControllersResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeDomainControllersResult.from_boto(response)

    def describe_event_topics(
        self,
        _request: shapes.DescribeEventTopicsRequest = None,
        *,
        directory_id: str = ShapeBase.NOT_SET,
        topic_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEventTopicsResult:
        """
        Obtains information about which SNS topics receive status messages from the
        specified directory.

        If no input parameters are provided, such as DirectoryId or TopicName, this
        request describes all of the associations in the account.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if topic_names is not ShapeBase.NOT_SET:
                _params['topic_names'] = topic_names
            _request = shapes.DescribeEventTopicsRequest(**_params)
        response = self._boto_client.describe_event_topics(**_request.to_boto())

        return shapes.DescribeEventTopicsResult.from_boto(response)

    def describe_snapshots(
        self,
        _request: shapes.DescribeSnapshotsRequest = None,
        *,
        directory_id: str = ShapeBase.NOT_SET,
        snapshot_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSnapshotsResult:
        """
        Obtains information about the directory snapshots that belong to this account.

        This operation supports pagination with the use of the _NextToken_ request and
        response parameters. If more results are available, the
        _DescribeSnapshots.NextToken_ member contains a token that you pass in the next
        call to DescribeSnapshots to retrieve the next set of items.

        You can also specify a maximum number of return results with the _Limit_
        parameter.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if snapshot_ids is not ShapeBase.NOT_SET:
                _params['snapshot_ids'] = snapshot_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeSnapshotsRequest(**_params)
        response = self._boto_client.describe_snapshots(**_request.to_boto())

        return shapes.DescribeSnapshotsResult.from_boto(response)

    def describe_trusts(
        self,
        _request: shapes.DescribeTrustsRequest = None,
        *,
        directory_id: str = ShapeBase.NOT_SET,
        trust_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTrustsResult:
        """
        Obtains information about the trust relationships for this account.

        If no input parameters are provided, such as DirectoryId or TrustIds, this
        request describes all the trust relationships belonging to the account.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if trust_ids is not ShapeBase.NOT_SET:
                _params['trust_ids'] = trust_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeTrustsRequest(**_params)
        response = self._boto_client.describe_trusts(**_request.to_boto())

        return shapes.DescribeTrustsResult.from_boto(response)

    def disable_radius(
        self,
        _request: shapes.DisableRadiusRequest = None,
        *,
        directory_id: str,
    ) -> shapes.DisableRadiusResult:
        """
        Disables multi-factor authentication (MFA) with the Remote Authentication Dial
        In User Service (RADIUS) server for an AD Connector directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            _request = shapes.DisableRadiusRequest(**_params)
        response = self._boto_client.disable_radius(**_request.to_boto())

        return shapes.DisableRadiusResult.from_boto(response)

    def disable_sso(
        self,
        _request: shapes.DisableSsoRequest = None,
        *,
        directory_id: str,
        user_name: str = ShapeBase.NOT_SET,
        password: str = ShapeBase.NOT_SET,
    ) -> shapes.DisableSsoResult:
        """
        Disables single-sign on for a directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.DisableSsoRequest(**_params)
        response = self._boto_client.disable_sso(**_request.to_boto())

        return shapes.DisableSsoResult.from_boto(response)

    def enable_radius(
        self,
        _request: shapes.EnableRadiusRequest = None,
        *,
        directory_id: str,
        radius_settings: shapes.RadiusSettings,
    ) -> shapes.EnableRadiusResult:
        """
        Enables multi-factor authentication (MFA) with the Remote Authentication Dial In
        User Service (RADIUS) server for an AD Connector directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if radius_settings is not ShapeBase.NOT_SET:
                _params['radius_settings'] = radius_settings
            _request = shapes.EnableRadiusRequest(**_params)
        response = self._boto_client.enable_radius(**_request.to_boto())

        return shapes.EnableRadiusResult.from_boto(response)

    def enable_sso(
        self,
        _request: shapes.EnableSsoRequest = None,
        *,
        directory_id: str,
        user_name: str = ShapeBase.NOT_SET,
        password: str = ShapeBase.NOT_SET,
    ) -> shapes.EnableSsoResult:
        """
        Enables single sign-on for a directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.EnableSsoRequest(**_params)
        response = self._boto_client.enable_sso(**_request.to_boto())

        return shapes.EnableSsoResult.from_boto(response)

    def get_directory_limits(
        self,
        _request: shapes.GetDirectoryLimitsRequest = None,
    ) -> shapes.GetDirectoryLimitsResult:
        """
        Obtains directory limit information for the current region.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetDirectoryLimitsRequest(**_params)
        response = self._boto_client.get_directory_limits(**_request.to_boto())

        return shapes.GetDirectoryLimitsResult.from_boto(response)

    def get_snapshot_limits(
        self,
        _request: shapes.GetSnapshotLimitsRequest = None,
        *,
        directory_id: str,
    ) -> shapes.GetSnapshotLimitsResult:
        """
        Obtains the manual snapshot limits for a directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            _request = shapes.GetSnapshotLimitsRequest(**_params)
        response = self._boto_client.get_snapshot_limits(**_request.to_boto())

        return shapes.GetSnapshotLimitsResult.from_boto(response)

    def list_ip_routes(
        self,
        _request: shapes.ListIpRoutesRequest = None,
        *,
        directory_id: str,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListIpRoutesResult:
        """
        Lists the address blocks that you have added to a directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListIpRoutesRequest(**_params)
        response = self._boto_client.list_ip_routes(**_request.to_boto())

        return shapes.ListIpRoutesResult.from_boto(response)

    def list_schema_extensions(
        self,
        _request: shapes.ListSchemaExtensionsRequest = None,
        *,
        directory_id: str,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSchemaExtensionsResult:
        """
        Lists all schema extensions applied to a Microsoft AD Directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListSchemaExtensionsRequest(**_params)
        response = self._boto_client.list_schema_extensions(
            **_request.to_boto()
        )

        return shapes.ListSchemaExtensionsResult.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_id: str,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsForResourceResult:
        """
        Lists all tags on a directory.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResult.from_boto(response)

    def register_event_topic(
        self,
        _request: shapes.RegisterEventTopicRequest = None,
        *,
        directory_id: str,
        topic_name: str,
    ) -> shapes.RegisterEventTopicResult:
        """
        Associates a directory with an SNS topic. This establishes the directory as a
        publisher to the specified SNS topic. You can then receive email or text (SMS)
        messages when the status of your directory changes. You get notified if your
        directory goes from an Active status to an Impaired or Inoperable status. You
        also receive a notification when the directory returns to an Active status.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if topic_name is not ShapeBase.NOT_SET:
                _params['topic_name'] = topic_name
            _request = shapes.RegisterEventTopicRequest(**_params)
        response = self._boto_client.register_event_topic(**_request.to_boto())

        return shapes.RegisterEventTopicResult.from_boto(response)

    def remove_ip_routes(
        self,
        _request: shapes.RemoveIpRoutesRequest = None,
        *,
        directory_id: str,
        cidr_ips: typing.List[str],
    ) -> shapes.RemoveIpRoutesResult:
        """
        Removes IP address blocks from a directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if cidr_ips is not ShapeBase.NOT_SET:
                _params['cidr_ips'] = cidr_ips
            _request = shapes.RemoveIpRoutesRequest(**_params)
        response = self._boto_client.remove_ip_routes(**_request.to_boto())

        return shapes.RemoveIpRoutesResult.from_boto(response)

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceRequest = None,
        *,
        resource_id: str,
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsFromResourceResult:
        """
        Removes tags from a directory.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsFromResourceRequest(**_params)
        response = self._boto_client.remove_tags_from_resource(
            **_request.to_boto()
        )

        return shapes.RemoveTagsFromResourceResult.from_boto(response)

    def reset_user_password(
        self,
        _request: shapes.ResetUserPasswordRequest = None,
        *,
        directory_id: str,
        user_name: str,
        new_password: str,
    ) -> shapes.ResetUserPasswordResult:
        """
        Resets the password for any user in your AWS Managed Microsoft AD or Simple AD
        directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if new_password is not ShapeBase.NOT_SET:
                _params['new_password'] = new_password
            _request = shapes.ResetUserPasswordRequest(**_params)
        response = self._boto_client.reset_user_password(**_request.to_boto())

        return shapes.ResetUserPasswordResult.from_boto(response)

    def restore_from_snapshot(
        self,
        _request: shapes.RestoreFromSnapshotRequest = None,
        *,
        snapshot_id: str,
    ) -> shapes.RestoreFromSnapshotResult:
        """
        Restores a directory using an existing directory snapshot.

        When you restore a directory from a snapshot, any changes made to the directory
        after the snapshot date are overwritten.

        This action returns as soon as the restore operation is initiated. You can
        monitor the progress of the restore operation by calling the DescribeDirectories
        operation with the directory identifier. When the **DirectoryDescription.Stage**
        value changes to `Active`, the restore operation is complete.
        """
        if _request is None:
            _params = {}
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            _request = shapes.RestoreFromSnapshotRequest(**_params)
        response = self._boto_client.restore_from_snapshot(**_request.to_boto())

        return shapes.RestoreFromSnapshotResult.from_boto(response)

    def start_schema_extension(
        self,
        _request: shapes.StartSchemaExtensionRequest = None,
        *,
        directory_id: str,
        create_snapshot_before_schema_extension: bool,
        ldif_content: str,
        description: str,
    ) -> shapes.StartSchemaExtensionResult:
        """
        Applies a schema extension to a Microsoft AD directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if create_snapshot_before_schema_extension is not ShapeBase.NOT_SET:
                _params['create_snapshot_before_schema_extension'
                       ] = create_snapshot_before_schema_extension
            if ldif_content is not ShapeBase.NOT_SET:
                _params['ldif_content'] = ldif_content
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.StartSchemaExtensionRequest(**_params)
        response = self._boto_client.start_schema_extension(
            **_request.to_boto()
        )

        return shapes.StartSchemaExtensionResult.from_boto(response)

    def update_conditional_forwarder(
        self,
        _request: shapes.UpdateConditionalForwarderRequest = None,
        *,
        directory_id: str,
        remote_domain_name: str,
        dns_ip_addrs: typing.List[str],
    ) -> shapes.UpdateConditionalForwarderResult:
        """
        Updates a conditional forwarder that has been set up for your AWS directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if remote_domain_name is not ShapeBase.NOT_SET:
                _params['remote_domain_name'] = remote_domain_name
            if dns_ip_addrs is not ShapeBase.NOT_SET:
                _params['dns_ip_addrs'] = dns_ip_addrs
            _request = shapes.UpdateConditionalForwarderRequest(**_params)
        response = self._boto_client.update_conditional_forwarder(
            **_request.to_boto()
        )

        return shapes.UpdateConditionalForwarderResult.from_boto(response)

    def update_number_of_domain_controllers(
        self,
        _request: shapes.UpdateNumberOfDomainControllersRequest = None,
        *,
        directory_id: str,
        desired_number: int,
    ) -> shapes.UpdateNumberOfDomainControllersResult:
        """
        Adds or removes domain controllers to or from the directory. Based on the
        difference between current value and new value (provided through this API call),
        domain controllers will be added or removed. It may take up to 45 minutes for
        any new domain controllers to become fully active once the requested number of
        domain controllers is updated. During this time, you cannot make another update
        request.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if desired_number is not ShapeBase.NOT_SET:
                _params['desired_number'] = desired_number
            _request = shapes.UpdateNumberOfDomainControllersRequest(**_params)
        response = self._boto_client.update_number_of_domain_controllers(
            **_request.to_boto()
        )

        return shapes.UpdateNumberOfDomainControllersResult.from_boto(response)

    def update_radius(
        self,
        _request: shapes.UpdateRadiusRequest = None,
        *,
        directory_id: str,
        radius_settings: shapes.RadiusSettings,
    ) -> shapes.UpdateRadiusResult:
        """
        Updates the Remote Authentication Dial In User Service (RADIUS) server
        information for an AD Connector directory.
        """
        if _request is None:
            _params = {}
            if directory_id is not ShapeBase.NOT_SET:
                _params['directory_id'] = directory_id
            if radius_settings is not ShapeBase.NOT_SET:
                _params['radius_settings'] = radius_settings
            _request = shapes.UpdateRadiusRequest(**_params)
        response = self._boto_client.update_radius(**_request.to_boto())

        return shapes.UpdateRadiusResult.from_boto(response)

    def verify_trust(
        self,
        _request: shapes.VerifyTrustRequest = None,
        *,
        trust_id: str,
    ) -> shapes.VerifyTrustResult:
        """
        AWS Directory Service for Microsoft Active Directory allows you to configure and
        verify trust relationships.

        This action verifies a trust relationship between your Microsoft AD in the AWS
        cloud and an external domain.
        """
        if _request is None:
            _params = {}
            if trust_id is not ShapeBase.NOT_SET:
                _params['trust_id'] = trust_id
            _request = shapes.VerifyTrustRequest(**_params)
        response = self._boto_client.verify_trust(**_request.to_boto())

        return shapes.VerifyTrustResult.from_boto(response)
