import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("elasticbeanstalk", *args, **kwargs)

    def abort_environment_update(
        self,
        _request: shapes.AbortEnvironmentUpdateMessage = None,
        *,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Cancels in-progress environment configuration update or application version
        deployment.
        """
        if _request is None:
            _params = {}
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.AbortEnvironmentUpdateMessage(**_params)
        response = self._boto_client.abort_environment_update(
            **_request.to_boto()
        )

    def apply_environment_managed_action(
        self,
        _request: shapes.ApplyEnvironmentManagedActionRequest = None,
        *,
        action_id: str,
        environment_name: str = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ApplyEnvironmentManagedActionResult:
        """
        Applies a scheduled managed action immediately. A managed action can be applied
        only if its status is `Scheduled`. Get the status and action ID of a managed
        action with DescribeEnvironmentManagedActions.
        """
        if _request is None:
            _params = {}
            if action_id is not ShapeBase.NOT_SET:
                _params['action_id'] = action_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            _request = shapes.ApplyEnvironmentManagedActionRequest(**_params)
        response = self._boto_client.apply_environment_managed_action(
            **_request.to_boto()
        )

        return shapes.ApplyEnvironmentManagedActionResult.from_boto(response)

    def check_dns_availability(
        self,
        _request: shapes.CheckDNSAvailabilityMessage = None,
        *,
        cname_prefix: str,
    ) -> shapes.CheckDNSAvailabilityResultMessage:
        """
        Checks if the specified CNAME is available.
        """
        if _request is None:
            _params = {}
            if cname_prefix is not ShapeBase.NOT_SET:
                _params['cname_prefix'] = cname_prefix
            _request = shapes.CheckDNSAvailabilityMessage(**_params)
        response = self._boto_client.check_dns_availability(
            **_request.to_boto()
        )

        return shapes.CheckDNSAvailabilityResultMessage.from_boto(response)

    def compose_environments(
        self,
        _request: shapes.ComposeEnvironmentsMessage = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        version_labels: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.EnvironmentDescriptionsMessage:
        """
        Create or update a group of environments that each run a separate component of a
        single application. Takes a list of version labels that specify application
        source bundles for each of the environments to create or update. The name of
        each environment and other required information must be included in the source
        bundles in an environment manifest named `env.yaml`. See [Compose
        Environments](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-
        mgmt-compose.html) for details.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if version_labels is not ShapeBase.NOT_SET:
                _params['version_labels'] = version_labels
            _request = shapes.ComposeEnvironmentsMessage(**_params)
        response = self._boto_client.compose_environments(**_request.to_boto())

        return shapes.EnvironmentDescriptionsMessage.from_boto(response)

    def create_application(
        self,
        _request: shapes.CreateApplicationMessage = None,
        *,
        application_name: str,
        description: str = ShapeBase.NOT_SET,
        resource_lifecycle_config: shapes.
        ApplicationResourceLifecycleConfig = ShapeBase.NOT_SET,
    ) -> shapes.ApplicationDescriptionMessage:
        """
        Creates an application that has one configuration template named `default` and
        no application versions.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if resource_lifecycle_config is not ShapeBase.NOT_SET:
                _params['resource_lifecycle_config'] = resource_lifecycle_config
            _request = shapes.CreateApplicationMessage(**_params)
        response = self._boto_client.create_application(**_request.to_boto())

        return shapes.ApplicationDescriptionMessage.from_boto(response)

    def create_application_version(
        self,
        _request: shapes.CreateApplicationVersionMessage = None,
        *,
        application_name: str,
        version_label: str,
        description: str = ShapeBase.NOT_SET,
        source_build_information: shapes.SourceBuildInformation = ShapeBase.
        NOT_SET,
        source_bundle: shapes.S3Location = ShapeBase.NOT_SET,
        build_configuration: shapes.BuildConfiguration = ShapeBase.NOT_SET,
        auto_create_application: bool = ShapeBase.NOT_SET,
        process: bool = ShapeBase.NOT_SET,
    ) -> shapes.ApplicationVersionDescriptionMessage:
        """
        Creates an application version for the specified application. You can create an
        application version from a source bundle in Amazon S3, a commit in AWS
        CodeCommit, or the output of an AWS CodeBuild build as follows:

        Specify a commit in an AWS CodeCommit repository with `SourceBuildInformation`.

        Specify a build in an AWS CodeBuild with `SourceBuildInformation` and
        `BuildConfiguration`.

        Specify a source bundle in S3 with `SourceBundle`

        Omit both `SourceBuildInformation` and `SourceBundle` to use the default sample
        application.

        Once you create an application version with a specified Amazon S3 bucket and key
        location, you cannot change that Amazon S3 location. If you change the Amazon S3
        location, you receive an exception when you attempt to launch an environment
        from the application version.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if source_build_information is not ShapeBase.NOT_SET:
                _params['source_build_information'] = source_build_information
            if source_bundle is not ShapeBase.NOT_SET:
                _params['source_bundle'] = source_bundle
            if build_configuration is not ShapeBase.NOT_SET:
                _params['build_configuration'] = build_configuration
            if auto_create_application is not ShapeBase.NOT_SET:
                _params['auto_create_application'] = auto_create_application
            if process is not ShapeBase.NOT_SET:
                _params['process'] = process
            _request = shapes.CreateApplicationVersionMessage(**_params)
        response = self._boto_client.create_application_version(
            **_request.to_boto()
        )

        return shapes.ApplicationVersionDescriptionMessage.from_boto(response)

    def create_configuration_template(
        self,
        _request: shapes.CreateConfigurationTemplateMessage = None,
        *,
        application_name: str,
        template_name: str,
        solution_stack_name: str = ShapeBase.NOT_SET,
        platform_arn: str = ShapeBase.NOT_SET,
        source_configuration: shapes.SourceConfiguration = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        option_settings: typing.List[shapes.ConfigurationOptionSetting
                                    ] = ShapeBase.NOT_SET,
    ) -> shapes.ConfigurationSettingsDescription:
        """
        Creates a configuration template. Templates are associated with a specific
        application and are used to deploy different versions of the application with
        the same configuration settings.

        Templates aren't associated with any environment. The `EnvironmentName` response
        element is always `null`.

        Related Topics

          * DescribeConfigurationOptions

          * DescribeConfigurationSettings

          * ListAvailableSolutionStacks
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if solution_stack_name is not ShapeBase.NOT_SET:
                _params['solution_stack_name'] = solution_stack_name
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            if source_configuration is not ShapeBase.NOT_SET:
                _params['source_configuration'] = source_configuration
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if option_settings is not ShapeBase.NOT_SET:
                _params['option_settings'] = option_settings
            _request = shapes.CreateConfigurationTemplateMessage(**_params)
        response = self._boto_client.create_configuration_template(
            **_request.to_boto()
        )

        return shapes.ConfigurationSettingsDescription.from_boto(response)

    def create_environment(
        self,
        _request: shapes.CreateEnvironmentMessage = None,
        *,
        application_name: str,
        environment_name: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        cname_prefix: str = ShapeBase.NOT_SET,
        tier: shapes.EnvironmentTier = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        version_label: str = ShapeBase.NOT_SET,
        template_name: str = ShapeBase.NOT_SET,
        solution_stack_name: str = ShapeBase.NOT_SET,
        platform_arn: str = ShapeBase.NOT_SET,
        option_settings: typing.List[shapes.ConfigurationOptionSetting
                                    ] = ShapeBase.NOT_SET,
        options_to_remove: typing.List[shapes.OptionSpecification
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.EnvironmentDescription:
        """
        Launches an environment for the specified application using the specified
        configuration.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if cname_prefix is not ShapeBase.NOT_SET:
                _params['cname_prefix'] = cname_prefix
            if tier is not ShapeBase.NOT_SET:
                _params['tier'] = tier
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if solution_stack_name is not ShapeBase.NOT_SET:
                _params['solution_stack_name'] = solution_stack_name
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            if option_settings is not ShapeBase.NOT_SET:
                _params['option_settings'] = option_settings
            if options_to_remove is not ShapeBase.NOT_SET:
                _params['options_to_remove'] = options_to_remove
            _request = shapes.CreateEnvironmentMessage(**_params)
        response = self._boto_client.create_environment(**_request.to_boto())

        return shapes.EnvironmentDescription.from_boto(response)

    def create_platform_version(
        self,
        _request: shapes.CreatePlatformVersionRequest = None,
        *,
        platform_name: str,
        platform_version: str,
        platform_definition_bundle: shapes.S3Location,
        environment_name: str = ShapeBase.NOT_SET,
        option_settings: typing.List[shapes.ConfigurationOptionSetting
                                    ] = ShapeBase.NOT_SET,
    ) -> shapes.CreatePlatformVersionResult:
        """
        Create a new version of your custom platform.
        """
        if _request is None:
            _params = {}
            if platform_name is not ShapeBase.NOT_SET:
                _params['platform_name'] = platform_name
            if platform_version is not ShapeBase.NOT_SET:
                _params['platform_version'] = platform_version
            if platform_definition_bundle is not ShapeBase.NOT_SET:
                _params['platform_definition_bundle'
                       ] = platform_definition_bundle
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if option_settings is not ShapeBase.NOT_SET:
                _params['option_settings'] = option_settings
            _request = shapes.CreatePlatformVersionRequest(**_params)
        response = self._boto_client.create_platform_version(
            **_request.to_boto()
        )

        return shapes.CreatePlatformVersionResult.from_boto(response)

    def create_storage_location(
        self,
    ) -> shapes.CreateStorageLocationResultMessage:
        """
        Creates a bucket in Amazon S3 to store application versions, logs, and other
        files used by Elastic Beanstalk environments. The Elastic Beanstalk console and
        EB CLI call this API the first time you create an environment in a region. If
        the storage location already exists, `CreateStorageLocation` still returns the
        bucket name but does not create a new bucket.
        """
        response = self._boto_client.create_storage_location()

        return shapes.CreateStorageLocationResultMessage.from_boto(response)

    def delete_application(
        self,
        _request: shapes.DeleteApplicationMessage = None,
        *,
        application_name: str,
        terminate_env_by_force: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified application along with all associated versions and
        configurations. The application versions will not be deleted from your Amazon S3
        bucket.

        You cannot delete an application that has a running environment.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if terminate_env_by_force is not ShapeBase.NOT_SET:
                _params['terminate_env_by_force'] = terminate_env_by_force
            _request = shapes.DeleteApplicationMessage(**_params)
        response = self._boto_client.delete_application(**_request.to_boto())

    def delete_application_version(
        self,
        _request: shapes.DeleteApplicationVersionMessage = None,
        *,
        application_name: str,
        version_label: str,
        delete_source_bundle: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified version from the specified application.

        You cannot delete an application version that is associated with a running
        environment.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if delete_source_bundle is not ShapeBase.NOT_SET:
                _params['delete_source_bundle'] = delete_source_bundle
            _request = shapes.DeleteApplicationVersionMessage(**_params)
        response = self._boto_client.delete_application_version(
            **_request.to_boto()
        )

    def delete_configuration_template(
        self,
        _request: shapes.DeleteConfigurationTemplateMessage = None,
        *,
        application_name: str,
        template_name: str,
    ) -> None:
        """
        Deletes the specified configuration template.

        When you launch an environment using a configuration template, the environment
        gets a copy of the template. You can delete or modify the environment's copy of
        the template without affecting the running environment.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            _request = shapes.DeleteConfigurationTemplateMessage(**_params)
        response = self._boto_client.delete_configuration_template(
            **_request.to_boto()
        )

    def delete_environment_configuration(
        self,
        _request: shapes.DeleteEnvironmentConfigurationMessage = None,
        *,
        application_name: str,
        environment_name: str,
    ) -> None:
        """
        Deletes the draft configuration associated with the running environment.

        Updating a running environment with any configuration changes creates a draft
        configuration set. You can get the draft configuration using
        DescribeConfigurationSettings while the update is in progress or if the update
        fails. The `DeploymentStatus` for the draft configuration indicates whether the
        deployment is in process or has failed. The draft configuration remains in
        existence until it is deleted with this action.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.DeleteEnvironmentConfigurationMessage(**_params)
        response = self._boto_client.delete_environment_configuration(
            **_request.to_boto()
        )

    def delete_platform_version(
        self,
        _request: shapes.DeletePlatformVersionRequest = None,
        *,
        platform_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DeletePlatformVersionResult:
        """
        Deletes the specified version of a custom platform.
        """
        if _request is None:
            _params = {}
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            _request = shapes.DeletePlatformVersionRequest(**_params)
        response = self._boto_client.delete_platform_version(
            **_request.to_boto()
        )

        return shapes.DeletePlatformVersionResult.from_boto(response)

    def describe_account_attributes(
        self,
    ) -> shapes.DescribeAccountAttributesResult:
        """
        Returns attributes related to AWS Elastic Beanstalk that are associated with the
        calling AWS account.

        The result currently has one set of attributes—resource quotas.
        """
        response = self._boto_client.describe_account_attributes()

        return shapes.DescribeAccountAttributesResult.from_boto(response)

    def describe_application_versions(
        self,
        _request: shapes.DescribeApplicationVersionsMessage = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        version_labels: typing.List[str] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ApplicationVersionDescriptionsMessage:
        """
        Retrieve a list of application versions.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if version_labels is not ShapeBase.NOT_SET:
                _params['version_labels'] = version_labels
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeApplicationVersionsMessage(**_params)
        response = self._boto_client.describe_application_versions(
            **_request.to_boto()
        )

        return shapes.ApplicationVersionDescriptionsMessage.from_boto(response)

    def describe_applications(
        self,
        _request: shapes.DescribeApplicationsMessage = None,
        *,
        application_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ApplicationDescriptionsMessage:
        """
        Returns the descriptions of existing applications.
        """
        if _request is None:
            _params = {}
            if application_names is not ShapeBase.NOT_SET:
                _params['application_names'] = application_names
            _request = shapes.DescribeApplicationsMessage(**_params)
        response = self._boto_client.describe_applications(**_request.to_boto())

        return shapes.ApplicationDescriptionsMessage.from_boto(response)

    def describe_configuration_options(
        self,
        _request: shapes.DescribeConfigurationOptionsMessage = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        template_name: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
        solution_stack_name: str = ShapeBase.NOT_SET,
        platform_arn: str = ShapeBase.NOT_SET,
        options: typing.List[shapes.OptionSpecification] = ShapeBase.NOT_SET,
    ) -> shapes.ConfigurationOptionsDescription:
        """
        Describes the configuration options that are used in a particular configuration
        template or environment, or that a specified solution stack defines. The
        description includes the values the options, their default values, and an
        indication of the required action on a running environment if an option value is
        changed.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if solution_stack_name is not ShapeBase.NOT_SET:
                _params['solution_stack_name'] = solution_stack_name
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            if options is not ShapeBase.NOT_SET:
                _params['options'] = options
            _request = shapes.DescribeConfigurationOptionsMessage(**_params)
        response = self._boto_client.describe_configuration_options(
            **_request.to_boto()
        )

        return shapes.ConfigurationOptionsDescription.from_boto(response)

    def describe_configuration_settings(
        self,
        _request: shapes.DescribeConfigurationSettingsMessage = None,
        *,
        application_name: str,
        template_name: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ConfigurationSettingsDescriptions:
        """
        Returns a description of the settings for the specified configuration set, that
        is, either a configuration template or the configuration set associated with a
        running environment.

        When describing the settings for the configuration set associated with a running
        environment, it is possible to receive two sets of setting descriptions. One is
        the deployed configuration set, and the other is a draft configuration of an
        environment that is either in the process of deployment or that failed to
        deploy.

        Related Topics

          * DeleteEnvironmentConfiguration
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.DescribeConfigurationSettingsMessage(**_params)
        response = self._boto_client.describe_configuration_settings(
            **_request.to_boto()
        )

        return shapes.ConfigurationSettingsDescriptions.from_boto(response)

    def describe_environment_health(
        self,
        _request: shapes.DescribeEnvironmentHealthRequest = None,
        *,
        environment_name: str = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
        attribute_names: typing.List[typing.Union[str, shapes.
                                                  EnvironmentHealthAttribute]
                                    ] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEnvironmentHealthResult:
        """
        Returns information about the overall health of the specified environment. The
        **DescribeEnvironmentHealth** operation is only available with AWS Elastic
        Beanstalk Enhanced Health.
        """
        if _request is None:
            _params = {}
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            _request = shapes.DescribeEnvironmentHealthRequest(**_params)
        response = self._boto_client.describe_environment_health(
            **_request.to_boto()
        )

        return shapes.DescribeEnvironmentHealthResult.from_boto(response)

    def describe_environment_managed_action_history(
        self,
        _request: shapes.DescribeEnvironmentManagedActionHistoryRequest = None,
        *,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_items: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEnvironmentManagedActionHistoryResult:
        """
        Lists an environment's completed and failed managed actions.
        """
        if _request is None:
            _params = {}
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            _request = shapes.DescribeEnvironmentManagedActionHistoryRequest(
                **_params
            )
        response = self._boto_client.describe_environment_managed_action_history(
            **_request.to_boto()
        )

        return shapes.DescribeEnvironmentManagedActionHistoryResult.from_boto(
            response
        )

    def describe_environment_managed_actions(
        self,
        _request: shapes.DescribeEnvironmentManagedActionsRequest = None,
        *,
        environment_name: str = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.ActionStatus] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEnvironmentManagedActionsResult:
        """
        Lists an environment's upcoming and in-progress managed actions.
        """
        if _request is None:
            _params = {}
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.DescribeEnvironmentManagedActionsRequest(
                **_params
            )
        response = self._boto_client.describe_environment_managed_actions(
            **_request.to_boto()
        )

        return shapes.DescribeEnvironmentManagedActionsResult.from_boto(
            response
        )

    def describe_environment_resources(
        self,
        _request: shapes.DescribeEnvironmentResourcesMessage = None,
        *,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> shapes.EnvironmentResourceDescriptionsMessage:
        """
        Returns AWS resources for this environment.
        """
        if _request is None:
            _params = {}
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.DescribeEnvironmentResourcesMessage(**_params)
        response = self._boto_client.describe_environment_resources(
            **_request.to_boto()
        )

        return shapes.EnvironmentResourceDescriptionsMessage.from_boto(response)

    def describe_environments(
        self,
        _request: shapes.DescribeEnvironmentsMessage = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        version_label: str = ShapeBase.NOT_SET,
        environment_ids: typing.List[str] = ShapeBase.NOT_SET,
        environment_names: typing.List[str] = ShapeBase.NOT_SET,
        include_deleted: bool = ShapeBase.NOT_SET,
        included_deleted_back_to: datetime.datetime = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.EnvironmentDescriptionsMessage:
        """
        Returns descriptions for existing environments.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if environment_ids is not ShapeBase.NOT_SET:
                _params['environment_ids'] = environment_ids
            if environment_names is not ShapeBase.NOT_SET:
                _params['environment_names'] = environment_names
            if include_deleted is not ShapeBase.NOT_SET:
                _params['include_deleted'] = include_deleted
            if included_deleted_back_to is not ShapeBase.NOT_SET:
                _params['included_deleted_back_to'] = included_deleted_back_to
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEnvironmentsMessage(**_params)
        response = self._boto_client.describe_environments(**_request.to_boto())

        return shapes.EnvironmentDescriptionsMessage.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsMessage = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        version_label: str = ShapeBase.NOT_SET,
        template_name: str = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
        platform_arn: str = ShapeBase.NOT_SET,
        request_id: str = ShapeBase.NOT_SET,
        severity: typing.Union[str, shapes.EventSeverity] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.EventDescriptionsMessage:
        """
        Returns list of event descriptions matching criteria up to the last 6 weeks.

        This action returns the most recent 1,000 events from the specified `NextToken`.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            if request_id is not ShapeBase.NOT_SET:
                _params['request_id'] = request_id
            if severity is not ShapeBase.NOT_SET:
                _params['severity'] = severity
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEventsMessage(**_params)
        paginator = self.get_paginator("describe_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.EventDescriptionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.EventDescriptionsMessage.from_boto(response)

    def describe_instances_health(
        self,
        _request: shapes.DescribeInstancesHealthRequest = None,
        *,
        environment_name: str = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
        attribute_names: typing.List[typing.Union[str, shapes.
                                                  InstancesHealthAttribute]
                                    ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancesHealthResult:
        """
        Retrieves detailed information about the health of instances in your AWS Elastic
        Beanstalk. This operation requires [enhanced health
        reporting](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-
        enhanced.html).
        """
        if _request is None:
            _params = {}
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeInstancesHealthRequest(**_params)
        response = self._boto_client.describe_instances_health(
            **_request.to_boto()
        )

        return shapes.DescribeInstancesHealthResult.from_boto(response)

    def describe_platform_version(
        self,
        _request: shapes.DescribePlatformVersionRequest = None,
        *,
        platform_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePlatformVersionResult:
        """
        Describes the version of the platform.
        """
        if _request is None:
            _params = {}
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            _request = shapes.DescribePlatformVersionRequest(**_params)
        response = self._boto_client.describe_platform_version(
            **_request.to_boto()
        )

        return shapes.DescribePlatformVersionResult.from_boto(response)

    def list_available_solution_stacks(
        self,
    ) -> shapes.ListAvailableSolutionStacksResultMessage:
        """
        Returns a list of the available solution stack names, with the public version
        first and then in reverse chronological order.
        """
        response = self._boto_client.list_available_solution_stacks()

        return shapes.ListAvailableSolutionStacksResultMessage.from_boto(
            response
        )

    def list_platform_versions(
        self,
        _request: shapes.ListPlatformVersionsRequest = None,
        *,
        filters: typing.List[shapes.PlatformFilter] = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPlatformVersionsResult:
        """
        Lists the available platforms.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPlatformVersionsRequest(**_params)
        response = self._boto_client.list_platform_versions(
            **_request.to_boto()
        )

        return shapes.ListPlatformVersionsResult.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceMessage = None,
        *,
        resource_arn: str,
    ) -> shapes.ResourceTagsDescriptionMessage:
        """
        Returns the tags applied to an AWS Elastic Beanstalk resource. The response
        contains a list of tag key-value pairs.

        Currently, Elastic Beanstalk only supports tagging of Elastic Beanstalk
        environments. For details about environment tagging, see [Tagging Resources in
        Your Elastic Beanstalk
        Environment](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-
        features.tagging.html).
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.ListTagsForResourceMessage(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ResourceTagsDescriptionMessage.from_boto(response)

    def rebuild_environment(
        self,
        _request: shapes.RebuildEnvironmentMessage = None,
        *,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes and recreates all of the AWS resources (for example: the Auto Scaling
        group, load balancer, etc.) for a specified environment and forces a restart.
        """
        if _request is None:
            _params = {}
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.RebuildEnvironmentMessage(**_params)
        response = self._boto_client.rebuild_environment(**_request.to_boto())

    def request_environment_info(
        self,
        _request: shapes.RequestEnvironmentInfoMessage = None,
        *,
        info_type: typing.Union[str, shapes.EnvironmentInfoType],
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Initiates a request to compile the specified type of information of the deployed
        environment.

        Setting the `InfoType` to `tail` compiles the last lines from the application
        server log files of every Amazon EC2 instance in your environment.

        Setting the `InfoType` to `bundle` compresses the application server log files
        for every Amazon EC2 instance into a `.zip` file. Legacy and .NET containers do
        not support bundle logs.

        Use RetrieveEnvironmentInfo to obtain the set of logs.

        Related Topics

          * RetrieveEnvironmentInfo
        """
        if _request is None:
            _params = {}
            if info_type is not ShapeBase.NOT_SET:
                _params['info_type'] = info_type
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.RequestEnvironmentInfoMessage(**_params)
        response = self._boto_client.request_environment_info(
            **_request.to_boto()
        )

    def restart_app_server(
        self,
        _request: shapes.RestartAppServerMessage = None,
        *,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Causes the environment to restart the application container server running on
        each Amazon EC2 instance.
        """
        if _request is None:
            _params = {}
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.RestartAppServerMessage(**_params)
        response = self._boto_client.restart_app_server(**_request.to_boto())

    def retrieve_environment_info(
        self,
        _request: shapes.RetrieveEnvironmentInfoMessage = None,
        *,
        info_type: typing.Union[str, shapes.EnvironmentInfoType],
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> shapes.RetrieveEnvironmentInfoResultMessage:
        """
        Retrieves the compiled information from a RequestEnvironmentInfo request.

        Related Topics

          * RequestEnvironmentInfo
        """
        if _request is None:
            _params = {}
            if info_type is not ShapeBase.NOT_SET:
                _params['info_type'] = info_type
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.RetrieveEnvironmentInfoMessage(**_params)
        response = self._boto_client.retrieve_environment_info(
            **_request.to_boto()
        )

        return shapes.RetrieveEnvironmentInfoResultMessage.from_boto(response)

    def swap_environment_cnames(
        self,
        _request: shapes.SwapEnvironmentCNAMEsMessage = None,
        *,
        source_environment_id: str = ShapeBase.NOT_SET,
        source_environment_name: str = ShapeBase.NOT_SET,
        destination_environment_id: str = ShapeBase.NOT_SET,
        destination_environment_name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Swaps the CNAMEs of two environments.
        """
        if _request is None:
            _params = {}
            if source_environment_id is not ShapeBase.NOT_SET:
                _params['source_environment_id'] = source_environment_id
            if source_environment_name is not ShapeBase.NOT_SET:
                _params['source_environment_name'] = source_environment_name
            if destination_environment_id is not ShapeBase.NOT_SET:
                _params['destination_environment_id'
                       ] = destination_environment_id
            if destination_environment_name is not ShapeBase.NOT_SET:
                _params['destination_environment_name'
                       ] = destination_environment_name
            _request = shapes.SwapEnvironmentCNAMEsMessage(**_params)
        response = self._boto_client.swap_environment_cnames(
            **_request.to_boto()
        )

    def terminate_environment(
        self,
        _request: shapes.TerminateEnvironmentMessage = None,
        *,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
        terminate_resources: bool = ShapeBase.NOT_SET,
        force_terminate: bool = ShapeBase.NOT_SET,
    ) -> shapes.EnvironmentDescription:
        """
        Terminates the specified environment.
        """
        if _request is None:
            _params = {}
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if terminate_resources is not ShapeBase.NOT_SET:
                _params['terminate_resources'] = terminate_resources
            if force_terminate is not ShapeBase.NOT_SET:
                _params['force_terminate'] = force_terminate
            _request = shapes.TerminateEnvironmentMessage(**_params)
        response = self._boto_client.terminate_environment(**_request.to_boto())

        return shapes.EnvironmentDescription.from_boto(response)

    def update_application(
        self,
        _request: shapes.UpdateApplicationMessage = None,
        *,
        application_name: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.ApplicationDescriptionMessage:
        """
        Updates the specified application to have the specified properties.

        If a property (for example, `description`) is not provided, the value remains
        unchanged. To clear these properties, specify an empty string.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateApplicationMessage(**_params)
        response = self._boto_client.update_application(**_request.to_boto())

        return shapes.ApplicationDescriptionMessage.from_boto(response)

    def update_application_resource_lifecycle(
        self,
        _request: shapes.UpdateApplicationResourceLifecycleMessage = None,
        *,
        application_name: str,
        resource_lifecycle_config: shapes.ApplicationResourceLifecycleConfig,
    ) -> shapes.ApplicationResourceLifecycleDescriptionMessage:
        """
        Modifies lifecycle settings for an application.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if resource_lifecycle_config is not ShapeBase.NOT_SET:
                _params['resource_lifecycle_config'] = resource_lifecycle_config
            _request = shapes.UpdateApplicationResourceLifecycleMessage(
                **_params
            )
        response = self._boto_client.update_application_resource_lifecycle(
            **_request.to_boto()
        )

        return shapes.ApplicationResourceLifecycleDescriptionMessage.from_boto(
            response
        )

    def update_application_version(
        self,
        _request: shapes.UpdateApplicationVersionMessage = None,
        *,
        application_name: str,
        version_label: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.ApplicationVersionDescriptionMessage:
        """
        Updates the specified application version to have the specified properties.

        If a property (for example, `description`) is not provided, the value remains
        unchanged. To clear properties, specify an empty string.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateApplicationVersionMessage(**_params)
        response = self._boto_client.update_application_version(
            **_request.to_boto()
        )

        return shapes.ApplicationVersionDescriptionMessage.from_boto(response)

    def update_configuration_template(
        self,
        _request: shapes.UpdateConfigurationTemplateMessage = None,
        *,
        application_name: str,
        template_name: str,
        description: str = ShapeBase.NOT_SET,
        option_settings: typing.List[shapes.ConfigurationOptionSetting
                                    ] = ShapeBase.NOT_SET,
        options_to_remove: typing.List[shapes.OptionSpecification
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.ConfigurationSettingsDescription:
        """
        Updates the specified configuration template to have the specified properties or
        configuration option values.

        If a property (for example, `ApplicationName`) is not provided, its value
        remains unchanged. To clear such properties, specify an empty string.

        Related Topics

          * DescribeConfigurationOptions
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if option_settings is not ShapeBase.NOT_SET:
                _params['option_settings'] = option_settings
            if options_to_remove is not ShapeBase.NOT_SET:
                _params['options_to_remove'] = options_to_remove
            _request = shapes.UpdateConfigurationTemplateMessage(**_params)
        response = self._boto_client.update_configuration_template(
            **_request.to_boto()
        )

        return shapes.ConfigurationSettingsDescription.from_boto(response)

    def update_environment(
        self,
        _request: shapes.UpdateEnvironmentMessage = None,
        *,
        application_name: str = ShapeBase.NOT_SET,
        environment_id: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        tier: shapes.EnvironmentTier = ShapeBase.NOT_SET,
        version_label: str = ShapeBase.NOT_SET,
        template_name: str = ShapeBase.NOT_SET,
        solution_stack_name: str = ShapeBase.NOT_SET,
        platform_arn: str = ShapeBase.NOT_SET,
        option_settings: typing.List[shapes.ConfigurationOptionSetting
                                    ] = ShapeBase.NOT_SET,
        options_to_remove: typing.List[shapes.OptionSpecification
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.EnvironmentDescription:
        """
        Updates the environment description, deploys a new application version, updates
        the configuration settings to an entirely new configuration template, or updates
        select configuration option values in the running environment.

        Attempting to update both the release and configuration is not allowed and AWS
        Elastic Beanstalk returns an `InvalidParameterCombination` error.

        When updating the configuration settings to a new template or individual
        settings, a draft configuration is created and DescribeConfigurationSettings for
        this environment returns two setting descriptions with different
        `DeploymentStatus` values.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if environment_id is not ShapeBase.NOT_SET:
                _params['environment_id'] = environment_id
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tier is not ShapeBase.NOT_SET:
                _params['tier'] = tier
            if version_label is not ShapeBase.NOT_SET:
                _params['version_label'] = version_label
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if solution_stack_name is not ShapeBase.NOT_SET:
                _params['solution_stack_name'] = solution_stack_name
            if platform_arn is not ShapeBase.NOT_SET:
                _params['platform_arn'] = platform_arn
            if option_settings is not ShapeBase.NOT_SET:
                _params['option_settings'] = option_settings
            if options_to_remove is not ShapeBase.NOT_SET:
                _params['options_to_remove'] = options_to_remove
            _request = shapes.UpdateEnvironmentMessage(**_params)
        response = self._boto_client.update_environment(**_request.to_boto())

        return shapes.EnvironmentDescription.from_boto(response)

    def update_tags_for_resource(
        self,
        _request: shapes.UpdateTagsForResourceMessage = None,
        *,
        resource_arn: str,
        tags_to_add: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        tags_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Update the list of tags applied to an AWS Elastic Beanstalk resource. Two lists
        can be passed: `TagsToAdd` for tags to add or update, and `TagsToRemove`.

        Currently, Elastic Beanstalk only supports tagging of Elastic Beanstalk
        environments. For details about environment tagging, see [Tagging Resources in
        Your Elastic Beanstalk
        Environment](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-
        features.tagging.html).

        If you create a custom IAM user policy to control permission to this operation,
        specify one of the following two virtual actions (or both) instead of the API
        operation name:

        elasticbeanstalk:AddTags



        Controls permission to call `UpdateTagsForResource` and pass a list of tags to
        add in the `TagsToAdd` parameter.

        elasticbeanstalk:RemoveTags



        Controls permission to call `UpdateTagsForResource` and pass a list of tag keys
        to remove in the `TagsToRemove` parameter.

        For details about creating a custom user policy, see [Creating a Custom User
        Policy](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-
        policies.html#AWSHowTo.iam.policies).
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags_to_add is not ShapeBase.NOT_SET:
                _params['tags_to_add'] = tags_to_add
            if tags_to_remove is not ShapeBase.NOT_SET:
                _params['tags_to_remove'] = tags_to_remove
            _request = shapes.UpdateTagsForResourceMessage(**_params)
        response = self._boto_client.update_tags_for_resource(
            **_request.to_boto()
        )

    def validate_configuration_settings(
        self,
        _request: shapes.ValidateConfigurationSettingsMessage = None,
        *,
        application_name: str,
        option_settings: typing.List[shapes.ConfigurationOptionSetting],
        template_name: str = ShapeBase.NOT_SET,
        environment_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ConfigurationSettingsValidationMessages:
        """
        Takes a set of configuration settings and either a configuration template or
        environment, and determines whether those values are valid.

        This action returns a list of messages indicating any errors or warnings
        associated with the selection of option values.
        """
        if _request is None:
            _params = {}
            if application_name is not ShapeBase.NOT_SET:
                _params['application_name'] = application_name
            if option_settings is not ShapeBase.NOT_SET:
                _params['option_settings'] = option_settings
            if template_name is not ShapeBase.NOT_SET:
                _params['template_name'] = template_name
            if environment_name is not ShapeBase.NOT_SET:
                _params['environment_name'] = environment_name
            _request = shapes.ValidateConfigurationSettingsMessage(**_params)
        response = self._boto_client.validate_configuration_settings(
            **_request.to_boto()
        )

        return shapes.ConfigurationSettingsValidationMessages.from_boto(
            response
        )
