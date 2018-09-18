import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mq", *args, **kwargs)

    def create_broker(
        self,
        _request: shapes.CreateBrokerRequest = None,
        *,
        auto_minor_version_upgrade: bool = ShapeBase.NOT_SET,
        broker_name: str = ShapeBase.NOT_SET,
        configuration: shapes.ConfigurationId = ShapeBase.NOT_SET,
        creator_request_id: str = ShapeBase.NOT_SET,
        deployment_mode: typing.Union[str, shapes.
                                      DeploymentMode] = ShapeBase.NOT_SET,
        engine_type: typing.Union[str, shapes.EngineType] = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        host_instance_type: str = ShapeBase.NOT_SET,
        logs: shapes.Logs = ShapeBase.NOT_SET,
        maintenance_window_start_time: shapes.WeeklyStartTime = ShapeBase.
        NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        security_groups: typing.List[str] = ShapeBase.NOT_SET,
        subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
        users: typing.List[shapes.User] = ShapeBase.NOT_SET,
    ) -> shapes.CreateBrokerResponse:
        """
        Creates a broker. Note: This API is asynchronous.
        """
        if _request is None:
            _params = {}
            if auto_minor_version_upgrade is not ShapeBase.NOT_SET:
                _params['auto_minor_version_upgrade'
                       ] = auto_minor_version_upgrade
            if broker_name is not ShapeBase.NOT_SET:
                _params['broker_name'] = broker_name
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            if creator_request_id is not ShapeBase.NOT_SET:
                _params['creator_request_id'] = creator_request_id
            if deployment_mode is not ShapeBase.NOT_SET:
                _params['deployment_mode'] = deployment_mode
            if engine_type is not ShapeBase.NOT_SET:
                _params['engine_type'] = engine_type
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if host_instance_type is not ShapeBase.NOT_SET:
                _params['host_instance_type'] = host_instance_type
            if logs is not ShapeBase.NOT_SET:
                _params['logs'] = logs
            if maintenance_window_start_time is not ShapeBase.NOT_SET:
                _params['maintenance_window_start_time'
                       ] = maintenance_window_start_time
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if users is not ShapeBase.NOT_SET:
                _params['users'] = users
            _request = shapes.CreateBrokerRequest(**_params)
        response = self._boto_client.create_broker(**_request.to_boto())

        return shapes.CreateBrokerResponse.from_boto(response)

    def create_configuration(
        self,
        _request: shapes.CreateConfigurationRequest = None,
        *,
        engine_type: typing.Union[str, shapes.EngineType] = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateConfigurationResponse:
        """
        Creates a new configuration for the specified configuration name. Amazon MQ uses
        the default configuration (the engine type and version).
        """
        if _request is None:
            _params = {}
            if engine_type is not ShapeBase.NOT_SET:
                _params['engine_type'] = engine_type
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateConfigurationRequest(**_params)
        response = self._boto_client.create_configuration(**_request.to_boto())

        return shapes.CreateConfigurationResponse.from_boto(response)

    def create_user(
        self,
        _request: shapes.CreateUserRequest = None,
        *,
        broker_id: str,
        username: str,
        console_access: bool = ShapeBase.NOT_SET,
        groups: typing.List[str] = ShapeBase.NOT_SET,
        password: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserResponse:
        """
        Creates an ActiveMQ user.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if console_access is not ShapeBase.NOT_SET:
                _params['console_access'] = console_access
            if groups is not ShapeBase.NOT_SET:
                _params['groups'] = groups
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.CreateUserRequest(**_params)
        response = self._boto_client.create_user(**_request.to_boto())

        return shapes.CreateUserResponse.from_boto(response)

    def delete_broker(
        self,
        _request: shapes.DeleteBrokerRequest = None,
        *,
        broker_id: str,
    ) -> shapes.DeleteBrokerResponse:
        """
        Deletes a broker. Note: This API is asynchronous.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            _request = shapes.DeleteBrokerRequest(**_params)
        response = self._boto_client.delete_broker(**_request.to_boto())

        return shapes.DeleteBrokerResponse.from_boto(response)

    def delete_user(
        self,
        _request: shapes.DeleteUserRequest = None,
        *,
        broker_id: str,
        username: str,
    ) -> shapes.DeleteUserResponse:
        """
        Deletes an ActiveMQ user.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.DeleteUserRequest(**_params)
        response = self._boto_client.delete_user(**_request.to_boto())

        return shapes.DeleteUserResponse.from_boto(response)

    def describe_broker(
        self,
        _request: shapes.DescribeBrokerRequest = None,
        *,
        broker_id: str,
    ) -> shapes.DescribeBrokerResponse:
        """
        Returns information about the specified broker.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            _request = shapes.DescribeBrokerRequest(**_params)
        response = self._boto_client.describe_broker(**_request.to_boto())

        return shapes.DescribeBrokerResponse.from_boto(response)

    def describe_configuration(
        self,
        _request: shapes.DescribeConfigurationRequest = None,
        *,
        configuration_id: str,
    ) -> shapes.DescribeConfigurationResponse:
        """
        Returns information about the specified configuration.
        """
        if _request is None:
            _params = {}
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            _request = shapes.DescribeConfigurationRequest(**_params)
        response = self._boto_client.describe_configuration(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationResponse.from_boto(response)

    def describe_configuration_revision(
        self,
        _request: shapes.DescribeConfigurationRevisionRequest = None,
        *,
        configuration_id: str,
        configuration_revision: str,
    ) -> shapes.DescribeConfigurationRevisionResponse:
        """
        Returns the specified configuration revision for the specified configuration.
        """
        if _request is None:
            _params = {}
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            if configuration_revision is not ShapeBase.NOT_SET:
                _params['configuration_revision'] = configuration_revision
            _request = shapes.DescribeConfigurationRevisionRequest(**_params)
        response = self._boto_client.describe_configuration_revision(
            **_request.to_boto()
        )

        return shapes.DescribeConfigurationRevisionResponse.from_boto(response)

    def describe_user(
        self,
        _request: shapes.DescribeUserRequest = None,
        *,
        broker_id: str,
        username: str,
    ) -> shapes.DescribeUserResponse:
        """
        Returns information about an ActiveMQ user.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            _request = shapes.DescribeUserRequest(**_params)
        response = self._boto_client.describe_user(**_request.to_boto())

        return shapes.DescribeUserResponse.from_boto(response)

    def list_brokers(
        self,
        _request: shapes.ListBrokersRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBrokersResponse:
        """
        Returns a list of all brokers.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListBrokersRequest(**_params)
        response = self._boto_client.list_brokers(**_request.to_boto())

        return shapes.ListBrokersResponse.from_boto(response)

    def list_configuration_revisions(
        self,
        _request: shapes.ListConfigurationRevisionsRequest = None,
        *,
        configuration_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListConfigurationRevisionsResponse:
        """
        Returns a list of all revisions for the specified configuration.
        """
        if _request is None:
            _params = {}
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListConfigurationRevisionsRequest(**_params)
        response = self._boto_client.list_configuration_revisions(
            **_request.to_boto()
        )

        return shapes.ListConfigurationRevisionsResponse.from_boto(response)

    def list_configurations(
        self,
        _request: shapes.ListConfigurationsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListConfigurationsResponse:
        """
        Returns a list of all configurations.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListConfigurationsRequest(**_params)
        response = self._boto_client.list_configurations(**_request.to_boto())

        return shapes.ListConfigurationsResponse.from_boto(response)

    def list_users(
        self,
        _request: shapes.ListUsersRequest = None,
        *,
        broker_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUsersResponse:
        """
        Returns a list of all ActiveMQ users.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListUsersRequest(**_params)
        response = self._boto_client.list_users(**_request.to_boto())

        return shapes.ListUsersResponse.from_boto(response)

    def reboot_broker(
        self,
        _request: shapes.RebootBrokerRequest = None,
        *,
        broker_id: str,
    ) -> shapes.RebootBrokerResponse:
        """
        Reboots a broker. Note: This API is asynchronous.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            _request = shapes.RebootBrokerRequest(**_params)
        response = self._boto_client.reboot_broker(**_request.to_boto())

        return shapes.RebootBrokerResponse.from_boto(response)

    def update_broker(
        self,
        _request: shapes.UpdateBrokerRequest = None,
        *,
        broker_id: str,
        configuration: shapes.ConfigurationId = ShapeBase.NOT_SET,
        logs: shapes.Logs = ShapeBase.NOT_SET,
    ) -> shapes.UpdateBrokerResponse:
        """
        Adds a pending configuration change to a broker.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            if logs is not ShapeBase.NOT_SET:
                _params['logs'] = logs
            _request = shapes.UpdateBrokerRequest(**_params)
        response = self._boto_client.update_broker(**_request.to_boto())

        return shapes.UpdateBrokerResponse.from_boto(response)

    def update_configuration(
        self,
        _request: shapes.UpdateConfigurationRequest = None,
        *,
        configuration_id: str,
        data: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateConfigurationResponse:
        """
        Updates the specified configuration.
        """
        if _request is None:
            _params = {}
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            if data is not ShapeBase.NOT_SET:
                _params['data'] = data
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateConfigurationRequest(**_params)
        response = self._boto_client.update_configuration(**_request.to_boto())

        return shapes.UpdateConfigurationResponse.from_boto(response)

    def update_user(
        self,
        _request: shapes.UpdateUserRequest = None,
        *,
        broker_id: str,
        username: str,
        console_access: bool = ShapeBase.NOT_SET,
        groups: typing.List[str] = ShapeBase.NOT_SET,
        password: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateUserResponse:
        """
        Updates the information for an ActiveMQ user.
        """
        if _request is None:
            _params = {}
            if broker_id is not ShapeBase.NOT_SET:
                _params['broker_id'] = broker_id
            if username is not ShapeBase.NOT_SET:
                _params['username'] = username
            if console_access is not ShapeBase.NOT_SET:
                _params['console_access'] = console_access
            if groups is not ShapeBase.NOT_SET:
                _params['groups'] = groups
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.UpdateUserRequest(**_params)
        response = self._boto_client.update_user(**_request.to_boto())

        return shapes.UpdateUserResponse.from_boto(response)
