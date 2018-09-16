import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("greengrass", *args, **kwargs)

    def associate_role_to_group(
        self,
        _request: shapes.AssociateRoleToGroupRequest = None,
        *,
        group_id: str,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateRoleToGroupResponse:
        """
        Associates a role with a group. Your AWS Greengrass core will use the role to
        access AWS cloud services. The role's permissions should allow Greengrass core
        Lambda functions to perform actions against the cloud.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.AssociateRoleToGroupRequest(**_params)
        response = self._boto_client.associate_role_to_group(
            **_request.to_boto()
        )

        return shapes.AssociateRoleToGroupResponse.from_boto(response)

    def associate_service_role_to_account(
        self,
        _request: shapes.AssociateServiceRoleToAccountRequest = None,
        *,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateServiceRoleToAccountResponse:
        """
        Associates a role with your account. AWS Greengrass will use the role to access
        your Lambda functions and AWS IoT resources. This is necessary for deployments
        to succeed. The role must have at least minimum permissions in the policy
        ''AWSGreengrassResourceAccessRolePolicy''.
        """
        if _request is None:
            _params = {}
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.AssociateServiceRoleToAccountRequest(**_params)
        response = self._boto_client.associate_service_role_to_account(
            **_request.to_boto()
        )

        return shapes.AssociateServiceRoleToAccountResponse.from_boto(response)

    def create_core_definition(
        self,
        _request: shapes.CreateCoreDefinitionRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.CoreDefinitionVersion = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCoreDefinitionResponse:
        """
        Creates a core definition. You may provide the initial version of the core
        definition now or use ''CreateCoreDefinitionVersion'' at a later time. AWS
        Greengrass groups must each contain exactly one AWS Greengrass core.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateCoreDefinitionRequest(**_params)
        response = self._boto_client.create_core_definition(
            **_request.to_boto()
        )

        return shapes.CreateCoreDefinitionResponse.from_boto(response)

    def create_core_definition_version(
        self,
        _request: shapes.CreateCoreDefinitionVersionRequest = None,
        *,
        core_definition_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        cores: typing.List[shapes.Core] = ShapeBase.NOT_SET,
    ) -> shapes.CreateCoreDefinitionVersionResponse:
        """
        Creates a version of a core definition that has already been defined. AWS
        Greengrass groups must each contain exactly one AWS Greengrass core.
        """
        if _request is None:
            _params = {}
            if core_definition_id is not ShapeBase.NOT_SET:
                _params['core_definition_id'] = core_definition_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if cores is not ShapeBase.NOT_SET:
                _params['cores'] = cores
            _request = shapes.CreateCoreDefinitionVersionRequest(**_params)
        response = self._boto_client.create_core_definition_version(
            **_request.to_boto()
        )

        return shapes.CreateCoreDefinitionVersionResponse.from_boto(response)

    def create_deployment(
        self,
        _request: shapes.CreateDeploymentRequest = None,
        *,
        group_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        deployment_id: str = ShapeBase.NOT_SET,
        deployment_type: typing.Union[str, shapes.DeploymentType] = ShapeBase.
        NOT_SET,
        group_version_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeploymentResponse:
        """
        Creates a deployment.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if deployment_type is not ShapeBase.NOT_SET:
                _params['deployment_type'] = deployment_type
            if group_version_id is not ShapeBase.NOT_SET:
                _params['group_version_id'] = group_version_id
            _request = shapes.CreateDeploymentRequest(**_params)
        response = self._boto_client.create_deployment(**_request.to_boto())

        return shapes.CreateDeploymentResponse.from_boto(response)

    def create_device_definition(
        self,
        _request: shapes.CreateDeviceDefinitionRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.DeviceDefinitionVersion = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeviceDefinitionResponse:
        """
        Creates a device definition. You may provide the initial version of the device
        definition now or use ''CreateDeviceDefinitionVersion'' at a later time.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateDeviceDefinitionRequest(**_params)
        response = self._boto_client.create_device_definition(
            **_request.to_boto()
        )

        return shapes.CreateDeviceDefinitionResponse.from_boto(response)

    def create_device_definition_version(
        self,
        _request: shapes.CreateDeviceDefinitionVersionRequest = None,
        *,
        device_definition_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        devices: typing.List[shapes.Device] = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeviceDefinitionVersionResponse:
        """
        Creates a version of a device definition that has already been defined.
        """
        if _request is None:
            _params = {}
            if device_definition_id is not ShapeBase.NOT_SET:
                _params['device_definition_id'] = device_definition_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if devices is not ShapeBase.NOT_SET:
                _params['devices'] = devices
            _request = shapes.CreateDeviceDefinitionVersionRequest(**_params)
        response = self._boto_client.create_device_definition_version(
            **_request.to_boto()
        )

        return shapes.CreateDeviceDefinitionVersionResponse.from_boto(response)

    def create_function_definition(
        self,
        _request: shapes.CreateFunctionDefinitionRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.FunctionDefinitionVersion = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateFunctionDefinitionResponse:
        """
        Creates a Lambda function definition which contains a list of Lambda functions
        and their configurations to be used in a group. You can create an initial
        version of the definition by providing a list of Lambda functions and their
        configurations now, or use ''CreateFunctionDefinitionVersion'' later.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateFunctionDefinitionRequest(**_params)
        response = self._boto_client.create_function_definition(
            **_request.to_boto()
        )

        return shapes.CreateFunctionDefinitionResponse.from_boto(response)

    def create_function_definition_version(
        self,
        _request: shapes.CreateFunctionDefinitionVersionRequest = None,
        *,
        function_definition_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        functions: typing.List[shapes.Function] = ShapeBase.NOT_SET,
    ) -> shapes.CreateFunctionDefinitionVersionResponse:
        """
        Creates a version of a Lambda function definition that has already been defined.
        """
        if _request is None:
            _params = {}
            if function_definition_id is not ShapeBase.NOT_SET:
                _params['function_definition_id'] = function_definition_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if functions is not ShapeBase.NOT_SET:
                _params['functions'] = functions
            _request = shapes.CreateFunctionDefinitionVersionRequest(**_params)
        response = self._boto_client.create_function_definition_version(
            **_request.to_boto()
        )

        return shapes.CreateFunctionDefinitionVersionResponse.from_boto(
            response
        )

    def create_group(
        self,
        _request: shapes.CreateGroupRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.GroupVersion = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupResponse:
        """
        Creates a group. You may provide the initial version of the group or use
        ''CreateGroupVersion'' at a later time.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateGroupRequest(**_params)
        response = self._boto_client.create_group(**_request.to_boto())

        return shapes.CreateGroupResponse.from_boto(response)

    def create_group_certificate_authority(
        self,
        _request: shapes.CreateGroupCertificateAuthorityRequest = None,
        *,
        group_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupCertificateAuthorityResponse:
        """
        Creates a CA for the group. If a CA already exists, it will rotate the existing
        CA.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            _request = shapes.CreateGroupCertificateAuthorityRequest(**_params)
        response = self._boto_client.create_group_certificate_authority(
            **_request.to_boto()
        )

        return shapes.CreateGroupCertificateAuthorityResponse.from_boto(
            response
        )

    def create_group_version(
        self,
        _request: shapes.CreateGroupVersionRequest = None,
        *,
        group_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        core_definition_version_arn: str = ShapeBase.NOT_SET,
        device_definition_version_arn: str = ShapeBase.NOT_SET,
        function_definition_version_arn: str = ShapeBase.NOT_SET,
        logger_definition_version_arn: str = ShapeBase.NOT_SET,
        resource_definition_version_arn: str = ShapeBase.NOT_SET,
        subscription_definition_version_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateGroupVersionResponse:
        """
        Creates a version of a group which has already been defined.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if core_definition_version_arn is not ShapeBase.NOT_SET:
                _params['core_definition_version_arn'
                       ] = core_definition_version_arn
            if device_definition_version_arn is not ShapeBase.NOT_SET:
                _params['device_definition_version_arn'
                       ] = device_definition_version_arn
            if function_definition_version_arn is not ShapeBase.NOT_SET:
                _params['function_definition_version_arn'
                       ] = function_definition_version_arn
            if logger_definition_version_arn is not ShapeBase.NOT_SET:
                _params['logger_definition_version_arn'
                       ] = logger_definition_version_arn
            if resource_definition_version_arn is not ShapeBase.NOT_SET:
                _params['resource_definition_version_arn'
                       ] = resource_definition_version_arn
            if subscription_definition_version_arn is not ShapeBase.NOT_SET:
                _params['subscription_definition_version_arn'
                       ] = subscription_definition_version_arn
            _request = shapes.CreateGroupVersionRequest(**_params)
        response = self._boto_client.create_group_version(**_request.to_boto())

        return shapes.CreateGroupVersionResponse.from_boto(response)

    def create_logger_definition(
        self,
        _request: shapes.CreateLoggerDefinitionRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.LoggerDefinitionVersion = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateLoggerDefinitionResponse:
        """
        Creates a logger definition. You may provide the initial version of the logger
        definition now or use ''CreateLoggerDefinitionVersion'' at a later time.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateLoggerDefinitionRequest(**_params)
        response = self._boto_client.create_logger_definition(
            **_request.to_boto()
        )

        return shapes.CreateLoggerDefinitionResponse.from_boto(response)

    def create_logger_definition_version(
        self,
        _request: shapes.CreateLoggerDefinitionVersionRequest = None,
        *,
        logger_definition_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        loggers: typing.List[shapes.Logger] = ShapeBase.NOT_SET,
    ) -> shapes.CreateLoggerDefinitionVersionResponse:
        """
        Creates a version of a logger definition that has already been defined.
        """
        if _request is None:
            _params = {}
            if logger_definition_id is not ShapeBase.NOT_SET:
                _params['logger_definition_id'] = logger_definition_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if loggers is not ShapeBase.NOT_SET:
                _params['loggers'] = loggers
            _request = shapes.CreateLoggerDefinitionVersionRequest(**_params)
        response = self._boto_client.create_logger_definition_version(
            **_request.to_boto()
        )

        return shapes.CreateLoggerDefinitionVersionResponse.from_boto(response)

    def create_resource_definition(
        self,
        _request: shapes.CreateResourceDefinitionRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.ResourceDefinitionVersion = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateResourceDefinitionResponse:
        """
        Creates a resource definition which contains a list of resources to be used in a
        group. You can create an initial version of the definition by providing a list
        of resources now, or use ''CreateResourceDefinitionVersion'' later.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateResourceDefinitionRequest(**_params)
        response = self._boto_client.create_resource_definition(
            **_request.to_boto()
        )

        return shapes.CreateResourceDefinitionResponse.from_boto(response)

    def create_resource_definition_version(
        self,
        _request: shapes.CreateResourceDefinitionVersionRequest = None,
        *,
        resource_definition_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        resources: typing.List[shapes.Resource] = ShapeBase.NOT_SET,
    ) -> shapes.CreateResourceDefinitionVersionResponse:
        """
        Creates a version of a resource definition that has already been defined.
        """
        if _request is None:
            _params = {}
            if resource_definition_id is not ShapeBase.NOT_SET:
                _params['resource_definition_id'] = resource_definition_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            _request = shapes.CreateResourceDefinitionVersionRequest(**_params)
        response = self._boto_client.create_resource_definition_version(
            **_request.to_boto()
        )

        return shapes.CreateResourceDefinitionVersionResponse.from_boto(
            response
        )

    def create_software_update_job(
        self,
        _request: shapes.CreateSoftwareUpdateJobRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        s3_url_signer_role: str = ShapeBase.NOT_SET,
        software_to_update: typing.Union[str, shapes.
                                         SoftwareToUpdate] = ShapeBase.NOT_SET,
        update_agent_log_level: typing.
        Union[str, shapes.UpdateAgentLogLevel] = ShapeBase.NOT_SET,
        update_targets: typing.List[str] = ShapeBase.NOT_SET,
        update_targets_architecture: typing.
        Union[str, shapes.UpdateTargetsArchitecture] = ShapeBase.NOT_SET,
        update_targets_operating_system: typing.
        Union[str, shapes.UpdateTargetsOperatingSystem] = ShapeBase.NOT_SET,
    ) -> shapes.CreateSoftwareUpdateJobResponse:
        """
        Creates a software update for a core or group of cores (specified as an IoT
        thing group.) Use this to update the OTA Agent as well as the Greengrass core
        software. It makes use of the IoT Jobs feature which provides additional
        commands to manage a Greengrass core software update job.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if s3_url_signer_role is not ShapeBase.NOT_SET:
                _params['s3_url_signer_role'] = s3_url_signer_role
            if software_to_update is not ShapeBase.NOT_SET:
                _params['software_to_update'] = software_to_update
            if update_agent_log_level is not ShapeBase.NOT_SET:
                _params['update_agent_log_level'] = update_agent_log_level
            if update_targets is not ShapeBase.NOT_SET:
                _params['update_targets'] = update_targets
            if update_targets_architecture is not ShapeBase.NOT_SET:
                _params['update_targets_architecture'
                       ] = update_targets_architecture
            if update_targets_operating_system is not ShapeBase.NOT_SET:
                _params['update_targets_operating_system'
                       ] = update_targets_operating_system
            _request = shapes.CreateSoftwareUpdateJobRequest(**_params)
        response = self._boto_client.create_software_update_job(
            **_request.to_boto()
        )

        return shapes.CreateSoftwareUpdateJobResponse.from_boto(response)

    def create_subscription_definition(
        self,
        _request: shapes.CreateSubscriptionDefinitionRequest = None,
        *,
        amzn_client_token: str = ShapeBase.NOT_SET,
        initial_version: shapes.SubscriptionDefinitionVersion = ShapeBase.
        NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSubscriptionDefinitionResponse:
        """
        Creates a subscription definition. You may provide the initial version of the
        subscription definition now or use ''CreateSubscriptionDefinitionVersion'' at a
        later time.
        """
        if _request is None:
            _params = {}
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if initial_version is not ShapeBase.NOT_SET:
                _params['initial_version'] = initial_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateSubscriptionDefinitionRequest(**_params)
        response = self._boto_client.create_subscription_definition(
            **_request.to_boto()
        )

        return shapes.CreateSubscriptionDefinitionResponse.from_boto(response)

    def create_subscription_definition_version(
        self,
        _request: shapes.CreateSubscriptionDefinitionVersionRequest = None,
        *,
        subscription_definition_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        subscriptions: typing.List[shapes.Subscription] = ShapeBase.NOT_SET,
    ) -> shapes.CreateSubscriptionDefinitionVersionResponse:
        """
        Creates a version of a subscription definition which has already been defined.
        """
        if _request is None:
            _params = {}
            if subscription_definition_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_id'
                       ] = subscription_definition_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if subscriptions is not ShapeBase.NOT_SET:
                _params['subscriptions'] = subscriptions
            _request = shapes.CreateSubscriptionDefinitionVersionRequest(
                **_params
            )
        response = self._boto_client.create_subscription_definition_version(
            **_request.to_boto()
        )

        return shapes.CreateSubscriptionDefinitionVersionResponse.from_boto(
            response
        )

    def delete_core_definition(
        self,
        _request: shapes.DeleteCoreDefinitionRequest = None,
        *,
        core_definition_id: str,
    ) -> shapes.DeleteCoreDefinitionResponse:
        """
        Deletes a core definition.
        """
        if _request is None:
            _params = {}
            if core_definition_id is not ShapeBase.NOT_SET:
                _params['core_definition_id'] = core_definition_id
            _request = shapes.DeleteCoreDefinitionRequest(**_params)
        response = self._boto_client.delete_core_definition(
            **_request.to_boto()
        )

        return shapes.DeleteCoreDefinitionResponse.from_boto(response)

    def delete_device_definition(
        self,
        _request: shapes.DeleteDeviceDefinitionRequest = None,
        *,
        device_definition_id: str,
    ) -> shapes.DeleteDeviceDefinitionResponse:
        """
        Deletes a device definition.
        """
        if _request is None:
            _params = {}
            if device_definition_id is not ShapeBase.NOT_SET:
                _params['device_definition_id'] = device_definition_id
            _request = shapes.DeleteDeviceDefinitionRequest(**_params)
        response = self._boto_client.delete_device_definition(
            **_request.to_boto()
        )

        return shapes.DeleteDeviceDefinitionResponse.from_boto(response)

    def delete_function_definition(
        self,
        _request: shapes.DeleteFunctionDefinitionRequest = None,
        *,
        function_definition_id: str,
    ) -> shapes.DeleteFunctionDefinitionResponse:
        """
        Deletes a Lambda function definition.
        """
        if _request is None:
            _params = {}
            if function_definition_id is not ShapeBase.NOT_SET:
                _params['function_definition_id'] = function_definition_id
            _request = shapes.DeleteFunctionDefinitionRequest(**_params)
        response = self._boto_client.delete_function_definition(
            **_request.to_boto()
        )

        return shapes.DeleteFunctionDefinitionResponse.from_boto(response)

    def delete_group(
        self,
        _request: shapes.DeleteGroupRequest = None,
        *,
        group_id: str,
    ) -> shapes.DeleteGroupResponse:
        """
        Deletes a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.DeleteGroupRequest(**_params)
        response = self._boto_client.delete_group(**_request.to_boto())

        return shapes.DeleteGroupResponse.from_boto(response)

    def delete_logger_definition(
        self,
        _request: shapes.DeleteLoggerDefinitionRequest = None,
        *,
        logger_definition_id: str,
    ) -> shapes.DeleteLoggerDefinitionResponse:
        """
        Deletes a logger definition.
        """
        if _request is None:
            _params = {}
            if logger_definition_id is not ShapeBase.NOT_SET:
                _params['logger_definition_id'] = logger_definition_id
            _request = shapes.DeleteLoggerDefinitionRequest(**_params)
        response = self._boto_client.delete_logger_definition(
            **_request.to_boto()
        )

        return shapes.DeleteLoggerDefinitionResponse.from_boto(response)

    def delete_resource_definition(
        self,
        _request: shapes.DeleteResourceDefinitionRequest = None,
        *,
        resource_definition_id: str,
    ) -> shapes.DeleteResourceDefinitionResponse:
        """
        Deletes a resource definition.
        """
        if _request is None:
            _params = {}
            if resource_definition_id is not ShapeBase.NOT_SET:
                _params['resource_definition_id'] = resource_definition_id
            _request = shapes.DeleteResourceDefinitionRequest(**_params)
        response = self._boto_client.delete_resource_definition(
            **_request.to_boto()
        )

        return shapes.DeleteResourceDefinitionResponse.from_boto(response)

    def delete_subscription_definition(
        self,
        _request: shapes.DeleteSubscriptionDefinitionRequest = None,
        *,
        subscription_definition_id: str,
    ) -> shapes.DeleteSubscriptionDefinitionResponse:
        """
        Deletes a subscription definition.
        """
        if _request is None:
            _params = {}
            if subscription_definition_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_id'
                       ] = subscription_definition_id
            _request = shapes.DeleteSubscriptionDefinitionRequest(**_params)
        response = self._boto_client.delete_subscription_definition(
            **_request.to_boto()
        )

        return shapes.DeleteSubscriptionDefinitionResponse.from_boto(response)

    def disassociate_role_from_group(
        self,
        _request: shapes.DisassociateRoleFromGroupRequest = None,
        *,
        group_id: str,
    ) -> shapes.DisassociateRoleFromGroupResponse:
        """
        Disassociates the role from a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.DisassociateRoleFromGroupRequest(**_params)
        response = self._boto_client.disassociate_role_from_group(
            **_request.to_boto()
        )

        return shapes.DisassociateRoleFromGroupResponse.from_boto(response)

    def disassociate_service_role_from_account(
        self,
        _request: shapes.DisassociateServiceRoleFromAccountRequest = None,
    ) -> shapes.DisassociateServiceRoleFromAccountResponse:
        """
        Disassociates the service role from your account. Without a service role,
        deployments will not work.
        """
        if _request is None:
            _params = {}
            _request = shapes.DisassociateServiceRoleFromAccountRequest(
                **_params
            )
        response = self._boto_client.disassociate_service_role_from_account(
            **_request.to_boto()
        )

        return shapes.DisassociateServiceRoleFromAccountResponse.from_boto(
            response
        )

    def get_associated_role(
        self,
        _request: shapes.GetAssociatedRoleRequest = None,
        *,
        group_id: str,
    ) -> shapes.GetAssociatedRoleResponse:
        """
        Retrieves the role associated with a particular group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.GetAssociatedRoleRequest(**_params)
        response = self._boto_client.get_associated_role(**_request.to_boto())

        return shapes.GetAssociatedRoleResponse.from_boto(response)

    def get_connectivity_info(
        self,
        _request: shapes.GetConnectivityInfoRequest = None,
        *,
        thing_name: str,
    ) -> shapes.GetConnectivityInfoResponse:
        """
        Retrieves the connectivity information for a core.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.GetConnectivityInfoRequest(**_params)
        response = self._boto_client.get_connectivity_info(**_request.to_boto())

        return shapes.GetConnectivityInfoResponse.from_boto(response)

    def get_core_definition(
        self,
        _request: shapes.GetCoreDefinitionRequest = None,
        *,
        core_definition_id: str,
    ) -> shapes.GetCoreDefinitionResponse:
        """
        Retrieves information about a core definition version.
        """
        if _request is None:
            _params = {}
            if core_definition_id is not ShapeBase.NOT_SET:
                _params['core_definition_id'] = core_definition_id
            _request = shapes.GetCoreDefinitionRequest(**_params)
        response = self._boto_client.get_core_definition(**_request.to_boto())

        return shapes.GetCoreDefinitionResponse.from_boto(response)

    def get_core_definition_version(
        self,
        _request: shapes.GetCoreDefinitionVersionRequest = None,
        *,
        core_definition_id: str,
        core_definition_version_id: str,
    ) -> shapes.GetCoreDefinitionVersionResponse:
        """
        Retrieves information about a core definition version.
        """
        if _request is None:
            _params = {}
            if core_definition_id is not ShapeBase.NOT_SET:
                _params['core_definition_id'] = core_definition_id
            if core_definition_version_id is not ShapeBase.NOT_SET:
                _params['core_definition_version_id'
                       ] = core_definition_version_id
            _request = shapes.GetCoreDefinitionVersionRequest(**_params)
        response = self._boto_client.get_core_definition_version(
            **_request.to_boto()
        )

        return shapes.GetCoreDefinitionVersionResponse.from_boto(response)

    def get_deployment_status(
        self,
        _request: shapes.GetDeploymentStatusRequest = None,
        *,
        deployment_id: str,
        group_id: str,
    ) -> shapes.GetDeploymentStatusResponse:
        """
        Returns the status of a deployment.
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.GetDeploymentStatusRequest(**_params)
        response = self._boto_client.get_deployment_status(**_request.to_boto())

        return shapes.GetDeploymentStatusResponse.from_boto(response)

    def get_device_definition(
        self,
        _request: shapes.GetDeviceDefinitionRequest = None,
        *,
        device_definition_id: str,
    ) -> shapes.GetDeviceDefinitionResponse:
        """
        Retrieves information about a device definition.
        """
        if _request is None:
            _params = {}
            if device_definition_id is not ShapeBase.NOT_SET:
                _params['device_definition_id'] = device_definition_id
            _request = shapes.GetDeviceDefinitionRequest(**_params)
        response = self._boto_client.get_device_definition(**_request.to_boto())

        return shapes.GetDeviceDefinitionResponse.from_boto(response)

    def get_device_definition_version(
        self,
        _request: shapes.GetDeviceDefinitionVersionRequest = None,
        *,
        device_definition_id: str,
        device_definition_version_id: str,
    ) -> shapes.GetDeviceDefinitionVersionResponse:
        """
        Retrieves information about a device definition version.
        """
        if _request is None:
            _params = {}
            if device_definition_id is not ShapeBase.NOT_SET:
                _params['device_definition_id'] = device_definition_id
            if device_definition_version_id is not ShapeBase.NOT_SET:
                _params['device_definition_version_id'
                       ] = device_definition_version_id
            _request = shapes.GetDeviceDefinitionVersionRequest(**_params)
        response = self._boto_client.get_device_definition_version(
            **_request.to_boto()
        )

        return shapes.GetDeviceDefinitionVersionResponse.from_boto(response)

    def get_function_definition(
        self,
        _request: shapes.GetFunctionDefinitionRequest = None,
        *,
        function_definition_id: str,
    ) -> shapes.GetFunctionDefinitionResponse:
        """
        Retrieves information about a Lambda function definition, including its creation
        time and latest version.
        """
        if _request is None:
            _params = {}
            if function_definition_id is not ShapeBase.NOT_SET:
                _params['function_definition_id'] = function_definition_id
            _request = shapes.GetFunctionDefinitionRequest(**_params)
        response = self._boto_client.get_function_definition(
            **_request.to_boto()
        )

        return shapes.GetFunctionDefinitionResponse.from_boto(response)

    def get_function_definition_version(
        self,
        _request: shapes.GetFunctionDefinitionVersionRequest = None,
        *,
        function_definition_id: str,
        function_definition_version_id: str,
    ) -> shapes.GetFunctionDefinitionVersionResponse:
        """
        Retrieves information about a Lambda function definition version, including
        which Lambda functions are included in the version and their configurations.
        """
        if _request is None:
            _params = {}
            if function_definition_id is not ShapeBase.NOT_SET:
                _params['function_definition_id'] = function_definition_id
            if function_definition_version_id is not ShapeBase.NOT_SET:
                _params['function_definition_version_id'
                       ] = function_definition_version_id
            _request = shapes.GetFunctionDefinitionVersionRequest(**_params)
        response = self._boto_client.get_function_definition_version(
            **_request.to_boto()
        )

        return shapes.GetFunctionDefinitionVersionResponse.from_boto(response)

    def get_group(
        self,
        _request: shapes.GetGroupRequest = None,
        *,
        group_id: str,
    ) -> shapes.GetGroupResponse:
        """
        Retrieves information about a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.GetGroupRequest(**_params)
        response = self._boto_client.get_group(**_request.to_boto())

        return shapes.GetGroupResponse.from_boto(response)

    def get_group_certificate_authority(
        self,
        _request: shapes.GetGroupCertificateAuthorityRequest = None,
        *,
        certificate_authority_id: str,
        group_id: str,
    ) -> shapes.GetGroupCertificateAuthorityResponse:
        """
        Retreives the CA associated with a group. Returns the public key of the CA.
        """
        if _request is None:
            _params = {}
            if certificate_authority_id is not ShapeBase.NOT_SET:
                _params['certificate_authority_id'] = certificate_authority_id
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.GetGroupCertificateAuthorityRequest(**_params)
        response = self._boto_client.get_group_certificate_authority(
            **_request.to_boto()
        )

        return shapes.GetGroupCertificateAuthorityResponse.from_boto(response)

    def get_group_certificate_configuration(
        self,
        _request: shapes.GetGroupCertificateConfigurationRequest = None,
        *,
        group_id: str,
    ) -> shapes.GetGroupCertificateConfigurationResponse:
        """
        Retrieves the current configuration for the CA used by the group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.GetGroupCertificateConfigurationRequest(**_params)
        response = self._boto_client.get_group_certificate_configuration(
            **_request.to_boto()
        )

        return shapes.GetGroupCertificateConfigurationResponse.from_boto(
            response
        )

    def get_group_version(
        self,
        _request: shapes.GetGroupVersionRequest = None,
        *,
        group_id: str,
        group_version_id: str,
    ) -> shapes.GetGroupVersionResponse:
        """
        Retrieves information about a group version.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if group_version_id is not ShapeBase.NOT_SET:
                _params['group_version_id'] = group_version_id
            _request = shapes.GetGroupVersionRequest(**_params)
        response = self._boto_client.get_group_version(**_request.to_boto())

        return shapes.GetGroupVersionResponse.from_boto(response)

    def get_logger_definition(
        self,
        _request: shapes.GetLoggerDefinitionRequest = None,
        *,
        logger_definition_id: str,
    ) -> shapes.GetLoggerDefinitionResponse:
        """
        Retrieves information about a logger definition.
        """
        if _request is None:
            _params = {}
            if logger_definition_id is not ShapeBase.NOT_SET:
                _params['logger_definition_id'] = logger_definition_id
            _request = shapes.GetLoggerDefinitionRequest(**_params)
        response = self._boto_client.get_logger_definition(**_request.to_boto())

        return shapes.GetLoggerDefinitionResponse.from_boto(response)

    def get_logger_definition_version(
        self,
        _request: shapes.GetLoggerDefinitionVersionRequest = None,
        *,
        logger_definition_id: str,
        logger_definition_version_id: str,
    ) -> shapes.GetLoggerDefinitionVersionResponse:
        """
        Retrieves information about a logger definition version.
        """
        if _request is None:
            _params = {}
            if logger_definition_id is not ShapeBase.NOT_SET:
                _params['logger_definition_id'] = logger_definition_id
            if logger_definition_version_id is not ShapeBase.NOT_SET:
                _params['logger_definition_version_id'
                       ] = logger_definition_version_id
            _request = shapes.GetLoggerDefinitionVersionRequest(**_params)
        response = self._boto_client.get_logger_definition_version(
            **_request.to_boto()
        )

        return shapes.GetLoggerDefinitionVersionResponse.from_boto(response)

    def get_resource_definition(
        self,
        _request: shapes.GetResourceDefinitionRequest = None,
        *,
        resource_definition_id: str,
    ) -> shapes.GetResourceDefinitionResponse:
        """
        Retrieves information about a resource definition, including its creation time
        and latest version.
        """
        if _request is None:
            _params = {}
            if resource_definition_id is not ShapeBase.NOT_SET:
                _params['resource_definition_id'] = resource_definition_id
            _request = shapes.GetResourceDefinitionRequest(**_params)
        response = self._boto_client.get_resource_definition(
            **_request.to_boto()
        )

        return shapes.GetResourceDefinitionResponse.from_boto(response)

    def get_resource_definition_version(
        self,
        _request: shapes.GetResourceDefinitionVersionRequest = None,
        *,
        resource_definition_id: str,
        resource_definition_version_id: str,
    ) -> shapes.GetResourceDefinitionVersionResponse:
        """
        Retrieves information about a resource definition version, including which
        resources are included in the version.
        """
        if _request is None:
            _params = {}
            if resource_definition_id is not ShapeBase.NOT_SET:
                _params['resource_definition_id'] = resource_definition_id
            if resource_definition_version_id is not ShapeBase.NOT_SET:
                _params['resource_definition_version_id'
                       ] = resource_definition_version_id
            _request = shapes.GetResourceDefinitionVersionRequest(**_params)
        response = self._boto_client.get_resource_definition_version(
            **_request.to_boto()
        )

        return shapes.GetResourceDefinitionVersionResponse.from_boto(response)

    def get_service_role_for_account(
        self,
        _request: shapes.GetServiceRoleForAccountRequest = None,
    ) -> shapes.GetServiceRoleForAccountResponse:
        """
        Retrieves the service role that is attached to your account.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetServiceRoleForAccountRequest(**_params)
        response = self._boto_client.get_service_role_for_account(
            **_request.to_boto()
        )

        return shapes.GetServiceRoleForAccountResponse.from_boto(response)

    def get_subscription_definition(
        self,
        _request: shapes.GetSubscriptionDefinitionRequest = None,
        *,
        subscription_definition_id: str,
    ) -> shapes.GetSubscriptionDefinitionResponse:
        """
        Retrieves information about a subscription definition.
        """
        if _request is None:
            _params = {}
            if subscription_definition_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_id'
                       ] = subscription_definition_id
            _request = shapes.GetSubscriptionDefinitionRequest(**_params)
        response = self._boto_client.get_subscription_definition(
            **_request.to_boto()
        )

        return shapes.GetSubscriptionDefinitionResponse.from_boto(response)

    def get_subscription_definition_version(
        self,
        _request: shapes.GetSubscriptionDefinitionVersionRequest = None,
        *,
        subscription_definition_id: str,
        subscription_definition_version_id: str,
    ) -> shapes.GetSubscriptionDefinitionVersionResponse:
        """
        Retrieves information about a subscription definition version.
        """
        if _request is None:
            _params = {}
            if subscription_definition_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_id'
                       ] = subscription_definition_id
            if subscription_definition_version_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_version_id'
                       ] = subscription_definition_version_id
            _request = shapes.GetSubscriptionDefinitionVersionRequest(**_params)
        response = self._boto_client.get_subscription_definition_version(
            **_request.to_boto()
        )

        return shapes.GetSubscriptionDefinitionVersionResponse.from_boto(
            response
        )

    def list_core_definition_versions(
        self,
        _request: shapes.ListCoreDefinitionVersionsRequest = None,
        *,
        core_definition_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListCoreDefinitionVersionsResponse:
        """
        Lists the versions of a core definition.
        """
        if _request is None:
            _params = {}
            if core_definition_id is not ShapeBase.NOT_SET:
                _params['core_definition_id'] = core_definition_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListCoreDefinitionVersionsRequest(**_params)
        response = self._boto_client.list_core_definition_versions(
            **_request.to_boto()
        )

        return shapes.ListCoreDefinitionVersionsResponse.from_boto(response)

    def list_core_definitions(
        self,
        _request: shapes.ListCoreDefinitionsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListCoreDefinitionsResponse:
        """
        Retrieves a list of core definitions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListCoreDefinitionsRequest(**_params)
        response = self._boto_client.list_core_definitions(**_request.to_boto())

        return shapes.ListCoreDefinitionsResponse.from_boto(response)

    def list_deployments(
        self,
        _request: shapes.ListDeploymentsRequest = None,
        *,
        group_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeploymentsResponse:
        """
        Returns a history of deployments for the group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeploymentsRequest(**_params)
        response = self._boto_client.list_deployments(**_request.to_boto())

        return shapes.ListDeploymentsResponse.from_boto(response)

    def list_device_definition_versions(
        self,
        _request: shapes.ListDeviceDefinitionVersionsRequest = None,
        *,
        device_definition_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeviceDefinitionVersionsResponse:
        """
        Lists the versions of a device definition.
        """
        if _request is None:
            _params = {}
            if device_definition_id is not ShapeBase.NOT_SET:
                _params['device_definition_id'] = device_definition_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeviceDefinitionVersionsRequest(**_params)
        response = self._boto_client.list_device_definition_versions(
            **_request.to_boto()
        )

        return shapes.ListDeviceDefinitionVersionsResponse.from_boto(response)

    def list_device_definitions(
        self,
        _request: shapes.ListDeviceDefinitionsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeviceDefinitionsResponse:
        """
        Retrieves a list of device definitions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeviceDefinitionsRequest(**_params)
        response = self._boto_client.list_device_definitions(
            **_request.to_boto()
        )

        return shapes.ListDeviceDefinitionsResponse.from_boto(response)

    def list_function_definition_versions(
        self,
        _request: shapes.ListFunctionDefinitionVersionsRequest = None,
        *,
        function_definition_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFunctionDefinitionVersionsResponse:
        """
        Lists the versions of a Lambda function definition.
        """
        if _request is None:
            _params = {}
            if function_definition_id is not ShapeBase.NOT_SET:
                _params['function_definition_id'] = function_definition_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListFunctionDefinitionVersionsRequest(**_params)
        response = self._boto_client.list_function_definition_versions(
            **_request.to_boto()
        )

        return shapes.ListFunctionDefinitionVersionsResponse.from_boto(response)

    def list_function_definitions(
        self,
        _request: shapes.ListFunctionDefinitionsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFunctionDefinitionsResponse:
        """
        Retrieves a list of Lambda function definitions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListFunctionDefinitionsRequest(**_params)
        response = self._boto_client.list_function_definitions(
            **_request.to_boto()
        )

        return shapes.ListFunctionDefinitionsResponse.from_boto(response)

    def list_group_certificate_authorities(
        self,
        _request: shapes.ListGroupCertificateAuthoritiesRequest = None,
        *,
        group_id: str,
    ) -> shapes.ListGroupCertificateAuthoritiesResponse:
        """
        Retrieves the current CAs for a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            _request = shapes.ListGroupCertificateAuthoritiesRequest(**_params)
        response = self._boto_client.list_group_certificate_authorities(
            **_request.to_boto()
        )

        return shapes.ListGroupCertificateAuthoritiesResponse.from_boto(
            response
        )

    def list_group_versions(
        self,
        _request: shapes.ListGroupVersionsRequest = None,
        *,
        group_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupVersionsResponse:
        """
        Lists the versions of a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupVersionsRequest(**_params)
        response = self._boto_client.list_group_versions(**_request.to_boto())

        return shapes.ListGroupVersionsResponse.from_boto(response)

    def list_groups(
        self,
        _request: shapes.ListGroupsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListGroupsResponse:
        """
        Retrieves a list of groups.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListGroupsRequest(**_params)
        response = self._boto_client.list_groups(**_request.to_boto())

        return shapes.ListGroupsResponse.from_boto(response)

    def list_logger_definition_versions(
        self,
        _request: shapes.ListLoggerDefinitionVersionsRequest = None,
        *,
        logger_definition_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListLoggerDefinitionVersionsResponse:
        """
        Lists the versions of a logger definition.
        """
        if _request is None:
            _params = {}
            if logger_definition_id is not ShapeBase.NOT_SET:
                _params['logger_definition_id'] = logger_definition_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListLoggerDefinitionVersionsRequest(**_params)
        response = self._boto_client.list_logger_definition_versions(
            **_request.to_boto()
        )

        return shapes.ListLoggerDefinitionVersionsResponse.from_boto(response)

    def list_logger_definitions(
        self,
        _request: shapes.ListLoggerDefinitionsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListLoggerDefinitionsResponse:
        """
        Retrieves a list of logger definitions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListLoggerDefinitionsRequest(**_params)
        response = self._boto_client.list_logger_definitions(
            **_request.to_boto()
        )

        return shapes.ListLoggerDefinitionsResponse.from_boto(response)

    def list_resource_definition_versions(
        self,
        _request: shapes.ListResourceDefinitionVersionsRequest = None,
        *,
        resource_definition_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceDefinitionVersionsResponse:
        """
        Lists the versions of a resource definition.
        """
        if _request is None:
            _params = {}
            if resource_definition_id is not ShapeBase.NOT_SET:
                _params['resource_definition_id'] = resource_definition_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListResourceDefinitionVersionsRequest(**_params)
        response = self._boto_client.list_resource_definition_versions(
            **_request.to_boto()
        )

        return shapes.ListResourceDefinitionVersionsResponse.from_boto(response)

    def list_resource_definitions(
        self,
        _request: shapes.ListResourceDefinitionsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceDefinitionsResponse:
        """
        Retrieves a list of resource definitions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListResourceDefinitionsRequest(**_params)
        response = self._boto_client.list_resource_definitions(
            **_request.to_boto()
        )

        return shapes.ListResourceDefinitionsResponse.from_boto(response)

    def list_subscription_definition_versions(
        self,
        _request: shapes.ListSubscriptionDefinitionVersionsRequest = None,
        *,
        subscription_definition_id: str,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSubscriptionDefinitionVersionsResponse:
        """
        Lists the versions of a subscription definition.
        """
        if _request is None:
            _params = {}
            if subscription_definition_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_id'
                       ] = subscription_definition_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSubscriptionDefinitionVersionsRequest(
                **_params
            )
        response = self._boto_client.list_subscription_definition_versions(
            **_request.to_boto()
        )

        return shapes.ListSubscriptionDefinitionVersionsResponse.from_boto(
            response
        )

    def list_subscription_definitions(
        self,
        _request: shapes.ListSubscriptionDefinitionsRequest = None,
        *,
        max_results: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSubscriptionDefinitionsResponse:
        """
        Retrieves a list of subscription definitions.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSubscriptionDefinitionsRequest(**_params)
        response = self._boto_client.list_subscription_definitions(
            **_request.to_boto()
        )

        return shapes.ListSubscriptionDefinitionsResponse.from_boto(response)

    def reset_deployments(
        self,
        _request: shapes.ResetDeploymentsRequest = None,
        *,
        group_id: str,
        amzn_client_token: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.ResetDeploymentsResponse:
        """
        Resets a group's deployments.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if amzn_client_token is not ShapeBase.NOT_SET:
                _params['amzn_client_token'] = amzn_client_token
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.ResetDeploymentsRequest(**_params)
        response = self._boto_client.reset_deployments(**_request.to_boto())

        return shapes.ResetDeploymentsResponse.from_boto(response)

    def update_connectivity_info(
        self,
        _request: shapes.UpdateConnectivityInfoRequest = None,
        *,
        thing_name: str,
        connectivity_info: typing.List[shapes.ConnectivityInfo
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateConnectivityInfoResponse:
        """
        Updates the connectivity information for the core. Any devices that belong to
        the group which has this core will receive this information in order to find the
        location of the core and connect to it.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if connectivity_info is not ShapeBase.NOT_SET:
                _params['connectivity_info'] = connectivity_info
            _request = shapes.UpdateConnectivityInfoRequest(**_params)
        response = self._boto_client.update_connectivity_info(
            **_request.to_boto()
        )

        return shapes.UpdateConnectivityInfoResponse.from_boto(response)

    def update_core_definition(
        self,
        _request: shapes.UpdateCoreDefinitionRequest = None,
        *,
        core_definition_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateCoreDefinitionResponse:
        """
        Updates a core definition.
        """
        if _request is None:
            _params = {}
            if core_definition_id is not ShapeBase.NOT_SET:
                _params['core_definition_id'] = core_definition_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateCoreDefinitionRequest(**_params)
        response = self._boto_client.update_core_definition(
            **_request.to_boto()
        )

        return shapes.UpdateCoreDefinitionResponse.from_boto(response)

    def update_device_definition(
        self,
        _request: shapes.UpdateDeviceDefinitionRequest = None,
        *,
        device_definition_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDeviceDefinitionResponse:
        """
        Updates a device definition.
        """
        if _request is None:
            _params = {}
            if device_definition_id is not ShapeBase.NOT_SET:
                _params['device_definition_id'] = device_definition_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateDeviceDefinitionRequest(**_params)
        response = self._boto_client.update_device_definition(
            **_request.to_boto()
        )

        return shapes.UpdateDeviceDefinitionResponse.from_boto(response)

    def update_function_definition(
        self,
        _request: shapes.UpdateFunctionDefinitionRequest = None,
        *,
        function_definition_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFunctionDefinitionResponse:
        """
        Updates a Lambda function definition.
        """
        if _request is None:
            _params = {}
            if function_definition_id is not ShapeBase.NOT_SET:
                _params['function_definition_id'] = function_definition_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateFunctionDefinitionRequest(**_params)
        response = self._boto_client.update_function_definition(
            **_request.to_boto()
        )

        return shapes.UpdateFunctionDefinitionResponse.from_boto(response)

    def update_group(
        self,
        _request: shapes.UpdateGroupRequest = None,
        *,
        group_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGroupResponse:
        """
        Updates a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateGroupRequest(**_params)
        response = self._boto_client.update_group(**_request.to_boto())

        return shapes.UpdateGroupResponse.from_boto(response)

    def update_group_certificate_configuration(
        self,
        _request: shapes.UpdateGroupCertificateConfigurationRequest = None,
        *,
        group_id: str,
        certificate_expiry_in_milliseconds: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGroupCertificateConfigurationResponse:
        """
        Updates the Certificate expiry time for a group.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if certificate_expiry_in_milliseconds is not ShapeBase.NOT_SET:
                _params['certificate_expiry_in_milliseconds'
                       ] = certificate_expiry_in_milliseconds
            _request = shapes.UpdateGroupCertificateConfigurationRequest(
                **_params
            )
        response = self._boto_client.update_group_certificate_configuration(
            **_request.to_boto()
        )

        return shapes.UpdateGroupCertificateConfigurationResponse.from_boto(
            response
        )

    def update_logger_definition(
        self,
        _request: shapes.UpdateLoggerDefinitionRequest = None,
        *,
        logger_definition_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateLoggerDefinitionResponse:
        """
        Updates a logger definition.
        """
        if _request is None:
            _params = {}
            if logger_definition_id is not ShapeBase.NOT_SET:
                _params['logger_definition_id'] = logger_definition_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateLoggerDefinitionRequest(**_params)
        response = self._boto_client.update_logger_definition(
            **_request.to_boto()
        )

        return shapes.UpdateLoggerDefinitionResponse.from_boto(response)

    def update_resource_definition(
        self,
        _request: shapes.UpdateResourceDefinitionRequest = None,
        *,
        resource_definition_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateResourceDefinitionResponse:
        """
        Updates a resource definition.
        """
        if _request is None:
            _params = {}
            if resource_definition_id is not ShapeBase.NOT_SET:
                _params['resource_definition_id'] = resource_definition_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateResourceDefinitionRequest(**_params)
        response = self._boto_client.update_resource_definition(
            **_request.to_boto()
        )

        return shapes.UpdateResourceDefinitionResponse.from_boto(response)

    def update_subscription_definition(
        self,
        _request: shapes.UpdateSubscriptionDefinitionRequest = None,
        *,
        subscription_definition_id: str,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSubscriptionDefinitionResponse:
        """
        Updates a subscription definition.
        """
        if _request is None:
            _params = {}
            if subscription_definition_id is not ShapeBase.NOT_SET:
                _params['subscription_definition_id'
                       ] = subscription_definition_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateSubscriptionDefinitionRequest(**_params)
        response = self._boto_client.update_subscription_definition(
            **_request.to_boto()
        )

        return shapes.UpdateSubscriptionDefinitionResponse.from_boto(response)
