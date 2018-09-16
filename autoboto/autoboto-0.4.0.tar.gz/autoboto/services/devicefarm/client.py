import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("devicefarm", *args, **kwargs)

    def create_device_pool(
        self,
        _request: shapes.CreateDevicePoolRequest = None,
        *,
        project_arn: str,
        name: str,
        rules: typing.List[shapes.Rule],
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDevicePoolResult:
        """
        Creates a device pool.
        """
        if _request is None:
            _params = {}
            if project_arn is not ShapeBase.NOT_SET:
                _params['project_arn'] = project_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if rules is not ShapeBase.NOT_SET:
                _params['rules'] = rules
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateDevicePoolRequest(**_params)
        response = self._boto_client.create_device_pool(**_request.to_boto())

        return shapes.CreateDevicePoolResult.from_boto(response)

    def create_instance_profile(
        self,
        _request: shapes.CreateInstanceProfileRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        package_cleanup: bool = ShapeBase.NOT_SET,
        exclude_app_packages_from_cleanup: typing.List[str] = ShapeBase.NOT_SET,
        reboot_after_use: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateInstanceProfileResult:
        """
        Creates a profile that can be applied to one or more private fleet device
        instances.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if package_cleanup is not ShapeBase.NOT_SET:
                _params['package_cleanup'] = package_cleanup
            if exclude_app_packages_from_cleanup is not ShapeBase.NOT_SET:
                _params['exclude_app_packages_from_cleanup'
                       ] = exclude_app_packages_from_cleanup
            if reboot_after_use is not ShapeBase.NOT_SET:
                _params['reboot_after_use'] = reboot_after_use
            _request = shapes.CreateInstanceProfileRequest(**_params)
        response = self._boto_client.create_instance_profile(
            **_request.to_boto()
        )

        return shapes.CreateInstanceProfileResult.from_boto(response)

    def create_network_profile(
        self,
        _request: shapes.CreateNetworkProfileRequest = None,
        *,
        project_arn: str,
        name: str,
        description: str = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.NetworkProfileType] = ShapeBase.NOT_SET,
        uplink_bandwidth_bits: int = ShapeBase.NOT_SET,
        downlink_bandwidth_bits: int = ShapeBase.NOT_SET,
        uplink_delay_ms: int = ShapeBase.NOT_SET,
        downlink_delay_ms: int = ShapeBase.NOT_SET,
        uplink_jitter_ms: int = ShapeBase.NOT_SET,
        downlink_jitter_ms: int = ShapeBase.NOT_SET,
        uplink_loss_percent: int = ShapeBase.NOT_SET,
        downlink_loss_percent: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateNetworkProfileResult:
        """
        Creates a network profile.
        """
        if _request is None:
            _params = {}
            if project_arn is not ShapeBase.NOT_SET:
                _params['project_arn'] = project_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if uplink_bandwidth_bits is not ShapeBase.NOT_SET:
                _params['uplink_bandwidth_bits'] = uplink_bandwidth_bits
            if downlink_bandwidth_bits is not ShapeBase.NOT_SET:
                _params['downlink_bandwidth_bits'] = downlink_bandwidth_bits
            if uplink_delay_ms is not ShapeBase.NOT_SET:
                _params['uplink_delay_ms'] = uplink_delay_ms
            if downlink_delay_ms is not ShapeBase.NOT_SET:
                _params['downlink_delay_ms'] = downlink_delay_ms
            if uplink_jitter_ms is not ShapeBase.NOT_SET:
                _params['uplink_jitter_ms'] = uplink_jitter_ms
            if downlink_jitter_ms is not ShapeBase.NOT_SET:
                _params['downlink_jitter_ms'] = downlink_jitter_ms
            if uplink_loss_percent is not ShapeBase.NOT_SET:
                _params['uplink_loss_percent'] = uplink_loss_percent
            if downlink_loss_percent is not ShapeBase.NOT_SET:
                _params['downlink_loss_percent'] = downlink_loss_percent
            _request = shapes.CreateNetworkProfileRequest(**_params)
        response = self._boto_client.create_network_profile(
            **_request.to_boto()
        )

        return shapes.CreateNetworkProfileResult.from_boto(response)

    def create_project(
        self,
        _request: shapes.CreateProjectRequest = None,
        *,
        name: str,
        default_job_timeout_minutes: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateProjectResult:
        """
        Creates a new project.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if default_job_timeout_minutes is not ShapeBase.NOT_SET:
                _params['default_job_timeout_minutes'
                       ] = default_job_timeout_minutes
            _request = shapes.CreateProjectRequest(**_params)
        response = self._boto_client.create_project(**_request.to_boto())

        return shapes.CreateProjectResult.from_boto(response)

    def create_remote_access_session(
        self,
        _request: shapes.CreateRemoteAccessSessionRequest = None,
        *,
        project_arn: str,
        device_arn: str,
        instance_arn: str = ShapeBase.NOT_SET,
        ssh_public_key: str = ShapeBase.NOT_SET,
        remote_debug_enabled: bool = ShapeBase.NOT_SET,
        remote_record_enabled: bool = ShapeBase.NOT_SET,
        remote_record_app_arn: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        client_id: str = ShapeBase.NOT_SET,
        configuration: shapes.
        CreateRemoteAccessSessionConfiguration = ShapeBase.NOT_SET,
        interaction_mode: typing.Union[str, shapes.
                                       InteractionMode] = ShapeBase.NOT_SET,
        skip_app_resign: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateRemoteAccessSessionResult:
        """
        Specifies and starts a remote access session.
        """
        if _request is None:
            _params = {}
            if project_arn is not ShapeBase.NOT_SET:
                _params['project_arn'] = project_arn
            if device_arn is not ShapeBase.NOT_SET:
                _params['device_arn'] = device_arn
            if instance_arn is not ShapeBase.NOT_SET:
                _params['instance_arn'] = instance_arn
            if ssh_public_key is not ShapeBase.NOT_SET:
                _params['ssh_public_key'] = ssh_public_key
            if remote_debug_enabled is not ShapeBase.NOT_SET:
                _params['remote_debug_enabled'] = remote_debug_enabled
            if remote_record_enabled is not ShapeBase.NOT_SET:
                _params['remote_record_enabled'] = remote_record_enabled
            if remote_record_app_arn is not ShapeBase.NOT_SET:
                _params['remote_record_app_arn'] = remote_record_app_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            if interaction_mode is not ShapeBase.NOT_SET:
                _params['interaction_mode'] = interaction_mode
            if skip_app_resign is not ShapeBase.NOT_SET:
                _params['skip_app_resign'] = skip_app_resign
            _request = shapes.CreateRemoteAccessSessionRequest(**_params)
        response = self._boto_client.create_remote_access_session(
            **_request.to_boto()
        )

        return shapes.CreateRemoteAccessSessionResult.from_boto(response)

    def create_upload(
        self,
        _request: shapes.CreateUploadRequest = None,
        *,
        project_arn: str,
        name: str,
        type: typing.Union[str, shapes.UploadType],
        content_type: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateUploadResult:
        """
        Uploads an app or test scripts.
        """
        if _request is None:
            _params = {}
            if project_arn is not ShapeBase.NOT_SET:
                _params['project_arn'] = project_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            _request = shapes.CreateUploadRequest(**_params)
        response = self._boto_client.create_upload(**_request.to_boto())

        return shapes.CreateUploadResult.from_boto(response)

    def create_vpce_configuration(
        self,
        _request: shapes.CreateVPCEConfigurationRequest = None,
        *,
        vpce_configuration_name: str,
        vpce_service_name: str,
        service_dns_name: str,
        vpce_configuration_description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateVPCEConfigurationResult:
        """
        Creates a configuration record in Device Farm for your Amazon Virtual Private
        Cloud (VPC) endpoint.
        """
        if _request is None:
            _params = {}
            if vpce_configuration_name is not ShapeBase.NOT_SET:
                _params['vpce_configuration_name'] = vpce_configuration_name
            if vpce_service_name is not ShapeBase.NOT_SET:
                _params['vpce_service_name'] = vpce_service_name
            if service_dns_name is not ShapeBase.NOT_SET:
                _params['service_dns_name'] = service_dns_name
            if vpce_configuration_description is not ShapeBase.NOT_SET:
                _params['vpce_configuration_description'
                       ] = vpce_configuration_description
            _request = shapes.CreateVPCEConfigurationRequest(**_params)
        response = self._boto_client.create_vpce_configuration(
            **_request.to_boto()
        )

        return shapes.CreateVPCEConfigurationResult.from_boto(response)

    def delete_device_pool(
        self,
        _request: shapes.DeleteDevicePoolRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteDevicePoolResult:
        """
        Deletes a device pool given the pool ARN. Does not allow deletion of curated
        pools owned by the system.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteDevicePoolRequest(**_params)
        response = self._boto_client.delete_device_pool(**_request.to_boto())

        return shapes.DeleteDevicePoolResult.from_boto(response)

    def delete_instance_profile(
        self,
        _request: shapes.DeleteInstanceProfileRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteInstanceProfileResult:
        """
        Deletes a profile that can be applied to one or more private device instances.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteInstanceProfileRequest(**_params)
        response = self._boto_client.delete_instance_profile(
            **_request.to_boto()
        )

        return shapes.DeleteInstanceProfileResult.from_boto(response)

    def delete_network_profile(
        self,
        _request: shapes.DeleteNetworkProfileRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteNetworkProfileResult:
        """
        Deletes a network profile.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteNetworkProfileRequest(**_params)
        response = self._boto_client.delete_network_profile(
            **_request.to_boto()
        )

        return shapes.DeleteNetworkProfileResult.from_boto(response)

    def delete_project(
        self,
        _request: shapes.DeleteProjectRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteProjectResult:
        """
        Deletes an AWS Device Farm project, given the project ARN.

        **Note** Deleting this resource does not stop an in-progress run.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteProjectRequest(**_params)
        response = self._boto_client.delete_project(**_request.to_boto())

        return shapes.DeleteProjectResult.from_boto(response)

    def delete_remote_access_session(
        self,
        _request: shapes.DeleteRemoteAccessSessionRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteRemoteAccessSessionResult:
        """
        Deletes a completed remote access session and its results.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteRemoteAccessSessionRequest(**_params)
        response = self._boto_client.delete_remote_access_session(
            **_request.to_boto()
        )

        return shapes.DeleteRemoteAccessSessionResult.from_boto(response)

    def delete_run(
        self,
        _request: shapes.DeleteRunRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteRunResult:
        """
        Deletes the run, given the run ARN.

        **Note** Deleting this resource does not stop an in-progress run.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteRunRequest(**_params)
        response = self._boto_client.delete_run(**_request.to_boto())

        return shapes.DeleteRunResult.from_boto(response)

    def delete_upload(
        self,
        _request: shapes.DeleteUploadRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteUploadResult:
        """
        Deletes an upload given the upload ARN.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteUploadRequest(**_params)
        response = self._boto_client.delete_upload(**_request.to_boto())

        return shapes.DeleteUploadResult.from_boto(response)

    def delete_vpce_configuration(
        self,
        _request: shapes.DeleteVPCEConfigurationRequest = None,
        *,
        arn: str,
    ) -> shapes.DeleteVPCEConfigurationResult:
        """
        Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.DeleteVPCEConfigurationRequest(**_params)
        response = self._boto_client.delete_vpce_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteVPCEConfigurationResult.from_boto(response)

    def get_account_settings(
        self,
        _request: shapes.GetAccountSettingsRequest = None,
    ) -> shapes.GetAccountSettingsResult:
        """
        Returns the number of unmetered iOS and/or unmetered Android devices that have
        been purchased by the account.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetAccountSettingsRequest(**_params)
        response = self._boto_client.get_account_settings(**_request.to_boto())

        return shapes.GetAccountSettingsResult.from_boto(response)

    def get_device(
        self,
        _request: shapes.GetDeviceRequest = None,
        *,
        arn: str,
    ) -> shapes.GetDeviceResult:
        """
        Gets information about a unique device type.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetDeviceRequest(**_params)
        response = self._boto_client.get_device(**_request.to_boto())

        return shapes.GetDeviceResult.from_boto(response)

    def get_device_instance(
        self,
        _request: shapes.GetDeviceInstanceRequest = None,
        *,
        arn: str,
    ) -> shapes.GetDeviceInstanceResult:
        """
        Returns information about a device instance belonging to a private device fleet.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetDeviceInstanceRequest(**_params)
        response = self._boto_client.get_device_instance(**_request.to_boto())

        return shapes.GetDeviceInstanceResult.from_boto(response)

    def get_device_pool(
        self,
        _request: shapes.GetDevicePoolRequest = None,
        *,
        arn: str,
    ) -> shapes.GetDevicePoolResult:
        """
        Gets information about a device pool.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetDevicePoolRequest(**_params)
        response = self._boto_client.get_device_pool(**_request.to_boto())

        return shapes.GetDevicePoolResult.from_boto(response)

    def get_device_pool_compatibility(
        self,
        _request: shapes.GetDevicePoolCompatibilityRequest = None,
        *,
        device_pool_arn: str,
        app_arn: str = ShapeBase.NOT_SET,
        test_type: typing.Union[str, shapes.TestType] = ShapeBase.NOT_SET,
        test: shapes.ScheduleRunTest = ShapeBase.NOT_SET,
        configuration: shapes.ScheduleRunConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.GetDevicePoolCompatibilityResult:
        """
        Gets information about compatibility with a device pool.
        """
        if _request is None:
            _params = {}
            if device_pool_arn is not ShapeBase.NOT_SET:
                _params['device_pool_arn'] = device_pool_arn
            if app_arn is not ShapeBase.NOT_SET:
                _params['app_arn'] = app_arn
            if test_type is not ShapeBase.NOT_SET:
                _params['test_type'] = test_type
            if test is not ShapeBase.NOT_SET:
                _params['test'] = test
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            _request = shapes.GetDevicePoolCompatibilityRequest(**_params)
        response = self._boto_client.get_device_pool_compatibility(
            **_request.to_boto()
        )

        return shapes.GetDevicePoolCompatibilityResult.from_boto(response)

    def get_instance_profile(
        self,
        _request: shapes.GetInstanceProfileRequest = None,
        *,
        arn: str,
    ) -> shapes.GetInstanceProfileResult:
        """
        Returns information about the specified instance profile.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetInstanceProfileRequest(**_params)
        response = self._boto_client.get_instance_profile(**_request.to_boto())

        return shapes.GetInstanceProfileResult.from_boto(response)

    def get_job(
        self,
        _request: shapes.GetJobRequest = None,
        *,
        arn: str,
    ) -> shapes.GetJobResult:
        """
        Gets information about a job.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetJobRequest(**_params)
        response = self._boto_client.get_job(**_request.to_boto())

        return shapes.GetJobResult.from_boto(response)

    def get_network_profile(
        self,
        _request: shapes.GetNetworkProfileRequest = None,
        *,
        arn: str,
    ) -> shapes.GetNetworkProfileResult:
        """
        Returns information about a network profile.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetNetworkProfileRequest(**_params)
        response = self._boto_client.get_network_profile(**_request.to_boto())

        return shapes.GetNetworkProfileResult.from_boto(response)

    def get_offering_status(
        self,
        _request: shapes.GetOfferingStatusRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetOfferingStatusResult:
        """
        Gets the current status and future status of all offerings purchased by an AWS
        account. The response indicates how many offerings are currently available and
        the offerings that will be available in the next period. The API returns a
        `NotEligible` error if the user is not permitted to invoke the operation. Please
        contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-
        support@amazon.com) if you believe that you should be able to invoke this
        operation.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetOfferingStatusRequest(**_params)
        paginator = self.get_paginator("get_offering_status").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetOfferingStatusResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetOfferingStatusResult.from_boto(response)

    def get_project(
        self,
        _request: shapes.GetProjectRequest = None,
        *,
        arn: str,
    ) -> shapes.GetProjectResult:
        """
        Gets information about a project.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetProjectRequest(**_params)
        response = self._boto_client.get_project(**_request.to_boto())

        return shapes.GetProjectResult.from_boto(response)

    def get_remote_access_session(
        self,
        _request: shapes.GetRemoteAccessSessionRequest = None,
        *,
        arn: str,
    ) -> shapes.GetRemoteAccessSessionResult:
        """
        Returns a link to a currently running remote access session.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetRemoteAccessSessionRequest(**_params)
        response = self._boto_client.get_remote_access_session(
            **_request.to_boto()
        )

        return shapes.GetRemoteAccessSessionResult.from_boto(response)

    def get_run(
        self,
        _request: shapes.GetRunRequest = None,
        *,
        arn: str,
    ) -> shapes.GetRunResult:
        """
        Gets information about a run.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetRunRequest(**_params)
        response = self._boto_client.get_run(**_request.to_boto())

        return shapes.GetRunResult.from_boto(response)

    def get_suite(
        self,
        _request: shapes.GetSuiteRequest = None,
        *,
        arn: str,
    ) -> shapes.GetSuiteResult:
        """
        Gets information about a suite.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetSuiteRequest(**_params)
        response = self._boto_client.get_suite(**_request.to_boto())

        return shapes.GetSuiteResult.from_boto(response)

    def get_test(
        self,
        _request: shapes.GetTestRequest = None,
        *,
        arn: str,
    ) -> shapes.GetTestResult:
        """
        Gets information about a test.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetTestRequest(**_params)
        response = self._boto_client.get_test(**_request.to_boto())

        return shapes.GetTestResult.from_boto(response)

    def get_upload(
        self,
        _request: shapes.GetUploadRequest = None,
        *,
        arn: str,
    ) -> shapes.GetUploadResult:
        """
        Gets information about an upload.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetUploadRequest(**_params)
        response = self._boto_client.get_upload(**_request.to_boto())

        return shapes.GetUploadResult.from_boto(response)

    def get_vpce_configuration(
        self,
        _request: shapes.GetVPCEConfigurationRequest = None,
        *,
        arn: str,
    ) -> shapes.GetVPCEConfigurationResult:
        """
        Returns information about the configuration settings for your Amazon Virtual
        Private Cloud (VPC) endpoint.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.GetVPCEConfigurationRequest(**_params)
        response = self._boto_client.get_vpce_configuration(
            **_request.to_boto()
        )

        return shapes.GetVPCEConfigurationResult.from_boto(response)

    def install_to_remote_access_session(
        self,
        _request: shapes.InstallToRemoteAccessSessionRequest = None,
        *,
        remote_access_session_arn: str,
        app_arn: str,
    ) -> shapes.InstallToRemoteAccessSessionResult:
        """
        Installs an application to the device in a remote access session. For Android
        applications, the file must be in .apk format. For iOS applications, the file
        must be in .ipa format.
        """
        if _request is None:
            _params = {}
            if remote_access_session_arn is not ShapeBase.NOT_SET:
                _params['remote_access_session_arn'] = remote_access_session_arn
            if app_arn is not ShapeBase.NOT_SET:
                _params['app_arn'] = app_arn
            _request = shapes.InstallToRemoteAccessSessionRequest(**_params)
        response = self._boto_client.install_to_remote_access_session(
            **_request.to_boto()
        )

        return shapes.InstallToRemoteAccessSessionResult.from_boto(response)

    def list_artifacts(
        self,
        _request: shapes.ListArtifactsRequest = None,
        *,
        arn: str,
        type: typing.Union[str, shapes.ArtifactCategory],
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListArtifactsResult:
        """
        Gets information about artifacts.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListArtifactsRequest(**_params)
        paginator = self.get_paginator("list_artifacts").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListArtifactsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListArtifactsResult.from_boto(response)

    def list_device_instances(
        self,
        _request: shapes.ListDeviceInstancesRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDeviceInstancesResult:
        """
        Returns information about the private device instances associated with one or
        more AWS accounts.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDeviceInstancesRequest(**_params)
        response = self._boto_client.list_device_instances(**_request.to_boto())

        return shapes.ListDeviceInstancesResult.from_boto(response)

    def list_device_pools(
        self,
        _request: shapes.ListDevicePoolsRequest = None,
        *,
        arn: str,
        type: typing.Union[str, shapes.DevicePoolType] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDevicePoolsResult:
        """
        Gets information about device pools.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDevicePoolsRequest(**_params)
        paginator = self.get_paginator("list_device_pools").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDevicePoolsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDevicePoolsResult.from_boto(response)

    def list_devices(
        self,
        _request: shapes.ListDevicesRequest = None,
        *,
        arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDevicesResult:
        """
        Gets information about unique device types.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDevicesRequest(**_params)
        paginator = self.get_paginator("list_devices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDevicesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDevicesResult.from_boto(response)

    def list_instance_profiles(
        self,
        _request: shapes.ListInstanceProfilesRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListInstanceProfilesResult:
        """
        Returns information about all the instance profiles in an AWS account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListInstanceProfilesRequest(**_params)
        response = self._boto_client.list_instance_profiles(
            **_request.to_boto()
        )

        return shapes.ListInstanceProfilesResult.from_boto(response)

    def list_jobs(
        self,
        _request: shapes.ListJobsRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsResult:
        """
        Gets information about jobs for a given test run.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListJobsRequest(**_params)
        paginator = self.get_paginator("list_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListJobsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListJobsResult.from_boto(response)

    def list_network_profiles(
        self,
        _request: shapes.ListNetworkProfilesRequest = None,
        *,
        arn: str,
        type: typing.Union[str, shapes.NetworkProfileType] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListNetworkProfilesResult:
        """
        Returns the list of available network profiles.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListNetworkProfilesRequest(**_params)
        response = self._boto_client.list_network_profiles(**_request.to_boto())

        return shapes.ListNetworkProfilesResult.from_boto(response)

    def list_offering_promotions(
        self,
        _request: shapes.ListOfferingPromotionsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListOfferingPromotionsResult:
        """
        Returns a list of offering promotions. Each offering promotion record contains
        the ID and description of the promotion. The API returns a `NotEligible` error
        if the caller is not permitted to invoke the operation. Contact [aws-devicefarm-
        support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you believe
        that you should be able to invoke this operation.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListOfferingPromotionsRequest(**_params)
        response = self._boto_client.list_offering_promotions(
            **_request.to_boto()
        )

        return shapes.ListOfferingPromotionsResult.from_boto(response)

    def list_offering_transactions(
        self,
        _request: shapes.ListOfferingTransactionsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListOfferingTransactionsResult:
        """
        Returns a list of all historical purchases, renewals, and system renewal
        transactions for an AWS account. The list is paginated and ordered by a
        descending timestamp (most recent transactions are first). The API returns a
        `NotEligible` error if the user is not permitted to invoke the operation. Please
        contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-
        support@amazon.com) if you believe that you should be able to invoke this
        operation.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListOfferingTransactionsRequest(**_params)
        paginator = self.get_paginator("list_offering_transactions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOfferingTransactionsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOfferingTransactionsResult.from_boto(response)

    def list_offerings(
        self,
        _request: shapes.ListOfferingsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListOfferingsResult:
        """
        Returns a list of products or offerings that the user can manage through the
        API. Each offering record indicates the recurring price per unit and the
        frequency for that offering. The API returns a `NotEligible` error if the user
        is not permitted to invoke the operation. Please contact [aws-devicefarm-
        support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you believe
        that you should be able to invoke this operation.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListOfferingsRequest(**_params)
        paginator = self.get_paginator("list_offerings").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOfferingsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOfferingsResult.from_boto(response)

    def list_projects(
        self,
        _request: shapes.ListProjectsRequest = None,
        *,
        arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListProjectsResult:
        """
        Gets information about projects.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListProjectsRequest(**_params)
        paginator = self.get_paginator("list_projects").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListProjectsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListProjectsResult.from_boto(response)

    def list_remote_access_sessions(
        self,
        _request: shapes.ListRemoteAccessSessionsRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListRemoteAccessSessionsResult:
        """
        Returns a list of all currently running remote access sessions.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListRemoteAccessSessionsRequest(**_params)
        response = self._boto_client.list_remote_access_sessions(
            **_request.to_boto()
        )

        return shapes.ListRemoteAccessSessionsResult.from_boto(response)

    def list_runs(
        self,
        _request: shapes.ListRunsRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListRunsResult:
        """
        Gets information about runs, given an AWS Device Farm project ARN.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListRunsRequest(**_params)
        paginator = self.get_paginator("list_runs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListRunsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListRunsResult.from_boto(response)

    def list_samples(
        self,
        _request: shapes.ListSamplesRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSamplesResult:
        """
        Gets information about samples, given an AWS Device Farm project ARN
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSamplesRequest(**_params)
        paginator = self.get_paginator("list_samples").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSamplesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSamplesResult.from_boto(response)

    def list_suites(
        self,
        _request: shapes.ListSuitesRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListSuitesResult:
        """
        Gets information about test suites for a given job.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListSuitesRequest(**_params)
        paginator = self.get_paginator("list_suites").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListSuitesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListSuitesResult.from_boto(response)

    def list_tests(
        self,
        _request: shapes.ListTestsRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTestsResult:
        """
        Gets information about tests in a given test suite.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListTestsRequest(**_params)
        paginator = self.get_paginator("list_tests").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTestsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTestsResult.from_boto(response)

    def list_unique_problems(
        self,
        _request: shapes.ListUniqueProblemsRequest = None,
        *,
        arn: str,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUniqueProblemsResult:
        """
        Gets information about unique problems.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListUniqueProblemsRequest(**_params)
        paginator = self.get_paginator("list_unique_problems").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListUniqueProblemsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListUniqueProblemsResult.from_boto(response)

    def list_uploads(
        self,
        _request: shapes.ListUploadsRequest = None,
        *,
        arn: str,
        type: typing.Union[str, shapes.UploadType] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListUploadsResult:
        """
        Gets information about uploads, given an AWS Device Farm project ARN.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListUploadsRequest(**_params)
        paginator = self.get_paginator("list_uploads").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListUploadsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListUploadsResult.from_boto(response)

    def list_vpce_configurations(
        self,
        _request: shapes.ListVPCEConfigurationsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListVPCEConfigurationsResult:
        """
        Returns information about all Amazon Virtual Private Cloud (VPC) endpoint
        configurations in the AWS account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListVPCEConfigurationsRequest(**_params)
        response = self._boto_client.list_vpce_configurations(
            **_request.to_boto()
        )

        return shapes.ListVPCEConfigurationsResult.from_boto(response)

    def purchase_offering(
        self,
        _request: shapes.PurchaseOfferingRequest = None,
        *,
        offering_id: str = ShapeBase.NOT_SET,
        quantity: int = ShapeBase.NOT_SET,
        offering_promotion_id: str = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseOfferingResult:
        """
        Immediately purchases offerings for an AWS account. Offerings renew with the
        latest total purchased quantity for an offering, unless the renewal was
        overridden. The API returns a `NotEligible` error if the user is not permitted
        to invoke the operation. Please contact [aws-devicefarm-
        support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you believe
        that you should be able to invoke this operation.
        """
        if _request is None:
            _params = {}
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            if quantity is not ShapeBase.NOT_SET:
                _params['quantity'] = quantity
            if offering_promotion_id is not ShapeBase.NOT_SET:
                _params['offering_promotion_id'] = offering_promotion_id
            _request = shapes.PurchaseOfferingRequest(**_params)
        response = self._boto_client.purchase_offering(**_request.to_boto())

        return shapes.PurchaseOfferingResult.from_boto(response)

    def renew_offering(
        self,
        _request: shapes.RenewOfferingRequest = None,
        *,
        offering_id: str = ShapeBase.NOT_SET,
        quantity: int = ShapeBase.NOT_SET,
    ) -> shapes.RenewOfferingResult:
        """
        Explicitly sets the quantity of devices to renew for an offering, starting from
        the `effectiveDate` of the next period. The API returns a `NotEligible` error if
        the user is not permitted to invoke the operation. Please contact [aws-
        devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you
        believe that you should be able to invoke this operation.
        """
        if _request is None:
            _params = {}
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            if quantity is not ShapeBase.NOT_SET:
                _params['quantity'] = quantity
            _request = shapes.RenewOfferingRequest(**_params)
        response = self._boto_client.renew_offering(**_request.to_boto())

        return shapes.RenewOfferingResult.from_boto(response)

    def schedule_run(
        self,
        _request: shapes.ScheduleRunRequest = None,
        *,
        project_arn: str,
        device_pool_arn: str,
        test: shapes.ScheduleRunTest,
        app_arn: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        configuration: shapes.ScheduleRunConfiguration = ShapeBase.NOT_SET,
        execution_configuration: shapes.ExecutionConfiguration = ShapeBase.
        NOT_SET,
    ) -> shapes.ScheduleRunResult:
        """
        Schedules a run.
        """
        if _request is None:
            _params = {}
            if project_arn is not ShapeBase.NOT_SET:
                _params['project_arn'] = project_arn
            if device_pool_arn is not ShapeBase.NOT_SET:
                _params['device_pool_arn'] = device_pool_arn
            if test is not ShapeBase.NOT_SET:
                _params['test'] = test
            if app_arn is not ShapeBase.NOT_SET:
                _params['app_arn'] = app_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if configuration is not ShapeBase.NOT_SET:
                _params['configuration'] = configuration
            if execution_configuration is not ShapeBase.NOT_SET:
                _params['execution_configuration'] = execution_configuration
            _request = shapes.ScheduleRunRequest(**_params)
        response = self._boto_client.schedule_run(**_request.to_boto())

        return shapes.ScheduleRunResult.from_boto(response)

    def stop_job(
        self,
        _request: shapes.StopJobRequest = None,
        *,
        arn: str,
    ) -> shapes.StopJobResult:
        """
        Initiates a stop request for the current job. AWS Device Farm will immediately
        stop the job on the device where tests have not started executing, and you will
        not be billed for this device. On the device where tests have started executing,
        Setup Suite and Teardown Suite tests will run to completion before stopping
        execution on the device. You will be billed for Setup, Teardown, and any tests
        that were in progress or already completed.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.StopJobRequest(**_params)
        response = self._boto_client.stop_job(**_request.to_boto())

        return shapes.StopJobResult.from_boto(response)

    def stop_remote_access_session(
        self,
        _request: shapes.StopRemoteAccessSessionRequest = None,
        *,
        arn: str,
    ) -> shapes.StopRemoteAccessSessionResult:
        """
        Ends a specified remote access session.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.StopRemoteAccessSessionRequest(**_params)
        response = self._boto_client.stop_remote_access_session(
            **_request.to_boto()
        )

        return shapes.StopRemoteAccessSessionResult.from_boto(response)

    def stop_run(
        self,
        _request: shapes.StopRunRequest = None,
        *,
        arn: str,
    ) -> shapes.StopRunResult:
        """
        Initiates a stop request for the current test run. AWS Device Farm will
        immediately stop the run on devices where tests have not started executing, and
        you will not be billed for these devices. On devices where tests have started
        executing, Setup Suite and Teardown Suite tests will run to completion before
        stopping execution on those devices. You will be billed for Setup, Teardown, and
        any tests that were in progress or already completed.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            _request = shapes.StopRunRequest(**_params)
        response = self._boto_client.stop_run(**_request.to_boto())

        return shapes.StopRunResult.from_boto(response)

    def update_device_instance(
        self,
        _request: shapes.UpdateDeviceInstanceRequest = None,
        *,
        arn: str,
        profile_arn: str = ShapeBase.NOT_SET,
        labels: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDeviceInstanceResult:
        """
        Updates information about an existing private device instance.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if profile_arn is not ShapeBase.NOT_SET:
                _params['profile_arn'] = profile_arn
            if labels is not ShapeBase.NOT_SET:
                _params['labels'] = labels
            _request = shapes.UpdateDeviceInstanceRequest(**_params)
        response = self._boto_client.update_device_instance(
            **_request.to_boto()
        )

        return shapes.UpdateDeviceInstanceResult.from_boto(response)

    def update_device_pool(
        self,
        _request: shapes.UpdateDevicePoolRequest = None,
        *,
        arn: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        rules: typing.List[shapes.Rule] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDevicePoolResult:
        """
        Modifies the name, description, and rules in a device pool given the attributes
        and the pool ARN. Rule updates are all-or-nothing, meaning they can only be
        updated as a whole (or not at all).
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if rules is not ShapeBase.NOT_SET:
                _params['rules'] = rules
            _request = shapes.UpdateDevicePoolRequest(**_params)
        response = self._boto_client.update_device_pool(**_request.to_boto())

        return shapes.UpdateDevicePoolResult.from_boto(response)

    def update_instance_profile(
        self,
        _request: shapes.UpdateInstanceProfileRequest = None,
        *,
        arn: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        package_cleanup: bool = ShapeBase.NOT_SET,
        exclude_app_packages_from_cleanup: typing.List[str] = ShapeBase.NOT_SET,
        reboot_after_use: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateInstanceProfileResult:
        """
        Updates information about an existing private device instance profile.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if package_cleanup is not ShapeBase.NOT_SET:
                _params['package_cleanup'] = package_cleanup
            if exclude_app_packages_from_cleanup is not ShapeBase.NOT_SET:
                _params['exclude_app_packages_from_cleanup'
                       ] = exclude_app_packages_from_cleanup
            if reboot_after_use is not ShapeBase.NOT_SET:
                _params['reboot_after_use'] = reboot_after_use
            _request = shapes.UpdateInstanceProfileRequest(**_params)
        response = self._boto_client.update_instance_profile(
            **_request.to_boto()
        )

        return shapes.UpdateInstanceProfileResult.from_boto(response)

    def update_network_profile(
        self,
        _request: shapes.UpdateNetworkProfileRequest = None,
        *,
        arn: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.NetworkProfileType] = ShapeBase.NOT_SET,
        uplink_bandwidth_bits: int = ShapeBase.NOT_SET,
        downlink_bandwidth_bits: int = ShapeBase.NOT_SET,
        uplink_delay_ms: int = ShapeBase.NOT_SET,
        downlink_delay_ms: int = ShapeBase.NOT_SET,
        uplink_jitter_ms: int = ShapeBase.NOT_SET,
        downlink_jitter_ms: int = ShapeBase.NOT_SET,
        uplink_loss_percent: int = ShapeBase.NOT_SET,
        downlink_loss_percent: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateNetworkProfileResult:
        """
        Updates the network profile with specific settings.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if uplink_bandwidth_bits is not ShapeBase.NOT_SET:
                _params['uplink_bandwidth_bits'] = uplink_bandwidth_bits
            if downlink_bandwidth_bits is not ShapeBase.NOT_SET:
                _params['downlink_bandwidth_bits'] = downlink_bandwidth_bits
            if uplink_delay_ms is not ShapeBase.NOT_SET:
                _params['uplink_delay_ms'] = uplink_delay_ms
            if downlink_delay_ms is not ShapeBase.NOT_SET:
                _params['downlink_delay_ms'] = downlink_delay_ms
            if uplink_jitter_ms is not ShapeBase.NOT_SET:
                _params['uplink_jitter_ms'] = uplink_jitter_ms
            if downlink_jitter_ms is not ShapeBase.NOT_SET:
                _params['downlink_jitter_ms'] = downlink_jitter_ms
            if uplink_loss_percent is not ShapeBase.NOT_SET:
                _params['uplink_loss_percent'] = uplink_loss_percent
            if downlink_loss_percent is not ShapeBase.NOT_SET:
                _params['downlink_loss_percent'] = downlink_loss_percent
            _request = shapes.UpdateNetworkProfileRequest(**_params)
        response = self._boto_client.update_network_profile(
            **_request.to_boto()
        )

        return shapes.UpdateNetworkProfileResult.from_boto(response)

    def update_project(
        self,
        _request: shapes.UpdateProjectRequest = None,
        *,
        arn: str,
        name: str = ShapeBase.NOT_SET,
        default_job_timeout_minutes: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProjectResult:
        """
        Modifies the specified project name, given the project ARN and a new name.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if default_job_timeout_minutes is not ShapeBase.NOT_SET:
                _params['default_job_timeout_minutes'
                       ] = default_job_timeout_minutes
            _request = shapes.UpdateProjectRequest(**_params)
        response = self._boto_client.update_project(**_request.to_boto())

        return shapes.UpdateProjectResult.from_boto(response)

    def update_upload(
        self,
        _request: shapes.UpdateUploadRequest = None,
        *,
        arn: str,
        name: str = ShapeBase.NOT_SET,
        content_type: str = ShapeBase.NOT_SET,
        edit_content: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateUploadResult:
        """
        Update an uploaded test specification (test spec).
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if edit_content is not ShapeBase.NOT_SET:
                _params['edit_content'] = edit_content
            _request = shapes.UpdateUploadRequest(**_params)
        response = self._boto_client.update_upload(**_request.to_boto())

        return shapes.UpdateUploadResult.from_boto(response)

    def update_vpce_configuration(
        self,
        _request: shapes.UpdateVPCEConfigurationRequest = None,
        *,
        arn: str,
        vpce_configuration_name: str = ShapeBase.NOT_SET,
        vpce_service_name: str = ShapeBase.NOT_SET,
        service_dns_name: str = ShapeBase.NOT_SET,
        vpce_configuration_description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateVPCEConfigurationResult:
        """
        Updates information about an existing Amazon Virtual Private Cloud (VPC)
        endpoint configuration.
        """
        if _request is None:
            _params = {}
            if arn is not ShapeBase.NOT_SET:
                _params['arn'] = arn
            if vpce_configuration_name is not ShapeBase.NOT_SET:
                _params['vpce_configuration_name'] = vpce_configuration_name
            if vpce_service_name is not ShapeBase.NOT_SET:
                _params['vpce_service_name'] = vpce_service_name
            if service_dns_name is not ShapeBase.NOT_SET:
                _params['service_dns_name'] = service_dns_name
            if vpce_configuration_description is not ShapeBase.NOT_SET:
                _params['vpce_configuration_description'
                       ] = vpce_configuration_description
            _request = shapes.UpdateVPCEConfigurationRequest(**_params)
        response = self._boto_client.update_vpce_configuration(
            **_request.to_boto()
        )

        return shapes.UpdateVPCEConfigurationResult.from_boto(response)
