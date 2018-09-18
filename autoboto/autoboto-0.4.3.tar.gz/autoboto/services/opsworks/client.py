import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("opsworks", *args, **kwargs)

    def assign_instance(
        self,
        _request: shapes.AssignInstanceRequest = None,
        *,
        instance_id: str,
        layer_ids: typing.List[str],
    ) -> None:
        """
        Assign a registered instance to a layer.

          * You can assign registered on-premises instances to any layer type.

          * You can assign registered Amazon EC2 instances only to custom layers.

          * You cannot use this action with instances that were created with AWS OpsWorks Stacks.

        **Required Permissions** : To use this action, an AWS Identity and Access
        Management (IAM) user must have a Manage permissions level for the stack or an
        attached policy that explicitly grants permissions. For more information on user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            _request = shapes.AssignInstanceRequest(**_params)
        response = self._boto_client.assign_instance(**_request.to_boto())

    def assign_volume(
        self,
        _request: shapes.AssignVolumeRequest = None,
        *,
        volume_id: str,
        instance_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Assigns one of the stack's registered Amazon EBS volumes to a specified
        instance. The volume must first be registered with the stack by calling
        RegisterVolume. After you register the volume, you must call UpdateVolume to
        specify a mount point before calling `AssignVolume`. For more information, see
        [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.AssignVolumeRequest(**_params)
        response = self._boto_client.assign_volume(**_request.to_boto())

    def associate_elastic_ip(
        self,
        _request: shapes.AssociateElasticIpRequest = None,
        *,
        elastic_ip: str,
        instance_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Associates one of the stack's registered Elastic IP addresses with a specified
        instance. The address must first be registered with the stack by calling
        RegisterElasticIp. For more information, see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.AssociateElasticIpRequest(**_params)
        response = self._boto_client.associate_elastic_ip(**_request.to_boto())

    def attach_elastic_load_balancer(
        self,
        _request: shapes.AttachElasticLoadBalancerRequest = None,
        *,
        elastic_load_balancer_name: str,
        layer_id: str,
    ) -> None:
        """
        Attaches an Elastic Load Balancing load balancer to a specified layer. AWS
        OpsWorks Stacks does not support Application Load Balancer. You can only use
        Classic Load Balancer with AWS OpsWorks Stacks. For more information, see
        [Elastic Load
        Balancing](http://docs.aws.amazon.com/opsworks/latest/userguide/layers-
        elb.html).

        You must create the Elastic Load Balancing instance separately, by using the
        Elastic Load Balancing console, API, or CLI. For more information, see [ Elastic
        Load Balancing Developer
        Guide](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/Welcome.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_load_balancer_name is not ShapeBase.NOT_SET:
                _params['elastic_load_balancer_name'
                       ] = elastic_load_balancer_name
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            _request = shapes.AttachElasticLoadBalancerRequest(**_params)
        response = self._boto_client.attach_elastic_load_balancer(
            **_request.to_boto()
        )

    def clone_stack(
        self,
        _request: shapes.CloneStackRequest = None,
        *,
        source_stack_id: str,
        service_role_arn: str,
        name: str = ShapeBase.NOT_SET,
        region: str = ShapeBase.NOT_SET,
        vpc_id: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[typing.Union[str, shapes.StackAttributesKeys],
                                str] = ShapeBase.NOT_SET,
        default_instance_profile_arn: str = ShapeBase.NOT_SET,
        default_os: str = ShapeBase.NOT_SET,
        hostname_theme: str = ShapeBase.NOT_SET,
        default_availability_zone: str = ShapeBase.NOT_SET,
        default_subnet_id: str = ShapeBase.NOT_SET,
        custom_json: str = ShapeBase.NOT_SET,
        configuration_manager: shapes.StackConfigurationManager = ShapeBase.
        NOT_SET,
        chef_configuration: shapes.ChefConfiguration = ShapeBase.NOT_SET,
        use_custom_cookbooks: bool = ShapeBase.NOT_SET,
        use_opsworks_security_groups: bool = ShapeBase.NOT_SET,
        custom_cookbooks_source: shapes.Source = ShapeBase.NOT_SET,
        default_ssh_key_name: str = ShapeBase.NOT_SET,
        clone_permissions: bool = ShapeBase.NOT_SET,
        clone_app_ids: typing.List[str] = ShapeBase.NOT_SET,
        default_root_device_type: typing.
        Union[str, shapes.RootDeviceType] = ShapeBase.NOT_SET,
        agent_version: str = ShapeBase.NOT_SET,
    ) -> shapes.CloneStackResult:
        """
        Creates a clone of a specified stack. For more information, see [Clone a
        Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
        cloning.html). By default, all parameters are set to the values used by the
        parent stack.

        **Required Permissions** : To use this action, an IAM user must have an attached
        policy that explicitly grants permissions. For more information about user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if source_stack_id is not ShapeBase.NOT_SET:
                _params['source_stack_id'] = source_stack_id
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if region is not ShapeBase.NOT_SET:
                _params['region'] = region
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if default_instance_profile_arn is not ShapeBase.NOT_SET:
                _params['default_instance_profile_arn'
                       ] = default_instance_profile_arn
            if default_os is not ShapeBase.NOT_SET:
                _params['default_os'] = default_os
            if hostname_theme is not ShapeBase.NOT_SET:
                _params['hostname_theme'] = hostname_theme
            if default_availability_zone is not ShapeBase.NOT_SET:
                _params['default_availability_zone'] = default_availability_zone
            if default_subnet_id is not ShapeBase.NOT_SET:
                _params['default_subnet_id'] = default_subnet_id
            if custom_json is not ShapeBase.NOT_SET:
                _params['custom_json'] = custom_json
            if configuration_manager is not ShapeBase.NOT_SET:
                _params['configuration_manager'] = configuration_manager
            if chef_configuration is not ShapeBase.NOT_SET:
                _params['chef_configuration'] = chef_configuration
            if use_custom_cookbooks is not ShapeBase.NOT_SET:
                _params['use_custom_cookbooks'] = use_custom_cookbooks
            if use_opsworks_security_groups is not ShapeBase.NOT_SET:
                _params['use_opsworks_security_groups'
                       ] = use_opsworks_security_groups
            if custom_cookbooks_source is not ShapeBase.NOT_SET:
                _params['custom_cookbooks_source'] = custom_cookbooks_source
            if default_ssh_key_name is not ShapeBase.NOT_SET:
                _params['default_ssh_key_name'] = default_ssh_key_name
            if clone_permissions is not ShapeBase.NOT_SET:
                _params['clone_permissions'] = clone_permissions
            if clone_app_ids is not ShapeBase.NOT_SET:
                _params['clone_app_ids'] = clone_app_ids
            if default_root_device_type is not ShapeBase.NOT_SET:
                _params['default_root_device_type'] = default_root_device_type
            if agent_version is not ShapeBase.NOT_SET:
                _params['agent_version'] = agent_version
            _request = shapes.CloneStackRequest(**_params)
        response = self._boto_client.clone_stack(**_request.to_boto())

        return shapes.CloneStackResult.from_boto(response)

    def create_app(
        self,
        _request: shapes.CreateAppRequest = None,
        *,
        stack_id: str,
        name: str,
        type: typing.Union[str, shapes.AppType],
        shortname: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        data_sources: typing.List[shapes.DataSource] = ShapeBase.NOT_SET,
        app_source: shapes.Source = ShapeBase.NOT_SET,
        domains: typing.List[str] = ShapeBase.NOT_SET,
        enable_ssl: bool = ShapeBase.NOT_SET,
        ssl_configuration: shapes.SslConfiguration = ShapeBase.NOT_SET,
        attributes: typing.Dict[typing.Union[str, shapes.AppAttributesKeys], str
                               ] = ShapeBase.NOT_SET,
        environment: typing.List[shapes.EnvironmentVariable
                                ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateAppResult:
        """
        Creates an app for a specified stack. For more information, see [Creating
        Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
        creating.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if shortname is not ShapeBase.NOT_SET:
                _params['shortname'] = shortname
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if data_sources is not ShapeBase.NOT_SET:
                _params['data_sources'] = data_sources
            if app_source is not ShapeBase.NOT_SET:
                _params['app_source'] = app_source
            if domains is not ShapeBase.NOT_SET:
                _params['domains'] = domains
            if enable_ssl is not ShapeBase.NOT_SET:
                _params['enable_ssl'] = enable_ssl
            if ssl_configuration is not ShapeBase.NOT_SET:
                _params['ssl_configuration'] = ssl_configuration
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if environment is not ShapeBase.NOT_SET:
                _params['environment'] = environment
            _request = shapes.CreateAppRequest(**_params)
        response = self._boto_client.create_app(**_request.to_boto())

        return shapes.CreateAppResult.from_boto(response)

    def create_deployment(
        self,
        _request: shapes.CreateDeploymentRequest = None,
        *,
        stack_id: str,
        command: shapes.DeploymentCommand,
        app_id: str = ShapeBase.NOT_SET,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        layer_ids: typing.List[str] = ShapeBase.NOT_SET,
        comment: str = ShapeBase.NOT_SET,
        custom_json: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDeploymentResult:
        """
        Runs deployment or stack commands. For more information, see [Deploying
        Apps](http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-
        deploying.html) and [Run Stack
        Commands](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
        commands.html).

        **Required Permissions** : To use this action, an IAM user must have a Deploy or
        Manage permissions level for the stack, or an attached policy that explicitly
        grants permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if command is not ShapeBase.NOT_SET:
                _params['command'] = command
            if app_id is not ShapeBase.NOT_SET:
                _params['app_id'] = app_id
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            if custom_json is not ShapeBase.NOT_SET:
                _params['custom_json'] = custom_json
            _request = shapes.CreateDeploymentRequest(**_params)
        response = self._boto_client.create_deployment(**_request.to_boto())

        return shapes.CreateDeploymentResult.from_boto(response)

    def create_instance(
        self,
        _request: shapes.CreateInstanceRequest = None,
        *,
        stack_id: str,
        layer_ids: typing.List[str],
        instance_type: str,
        auto_scaling_type: typing.Union[str, shapes.
                                        AutoScalingType] = ShapeBase.NOT_SET,
        hostname: str = ShapeBase.NOT_SET,
        os: str = ShapeBase.NOT_SET,
        ami_id: str = ShapeBase.NOT_SET,
        ssh_key_name: str = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        virtualization_type: str = ShapeBase.NOT_SET,
        subnet_id: str = ShapeBase.NOT_SET,
        architecture: typing.Union[str, shapes.
                                   Architecture] = ShapeBase.NOT_SET,
        root_device_type: typing.Union[str, shapes.RootDeviceType] = ShapeBase.
        NOT_SET,
        block_device_mappings: typing.List[shapes.BlockDeviceMapping
                                          ] = ShapeBase.NOT_SET,
        install_updates_on_boot: bool = ShapeBase.NOT_SET,
        ebs_optimized: bool = ShapeBase.NOT_SET,
        agent_version: str = ShapeBase.NOT_SET,
        tenancy: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateInstanceResult:
        """
        Creates an instance in a specified stack. For more information, see [Adding an
        Instance to a
        Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        add.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if auto_scaling_type is not ShapeBase.NOT_SET:
                _params['auto_scaling_type'] = auto_scaling_type
            if hostname is not ShapeBase.NOT_SET:
                _params['hostname'] = hostname
            if os is not ShapeBase.NOT_SET:
                _params['os'] = os
            if ami_id is not ShapeBase.NOT_SET:
                _params['ami_id'] = ami_id
            if ssh_key_name is not ShapeBase.NOT_SET:
                _params['ssh_key_name'] = ssh_key_name
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if virtualization_type is not ShapeBase.NOT_SET:
                _params['virtualization_type'] = virtualization_type
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if architecture is not ShapeBase.NOT_SET:
                _params['architecture'] = architecture
            if root_device_type is not ShapeBase.NOT_SET:
                _params['root_device_type'] = root_device_type
            if block_device_mappings is not ShapeBase.NOT_SET:
                _params['block_device_mappings'] = block_device_mappings
            if install_updates_on_boot is not ShapeBase.NOT_SET:
                _params['install_updates_on_boot'] = install_updates_on_boot
            if ebs_optimized is not ShapeBase.NOT_SET:
                _params['ebs_optimized'] = ebs_optimized
            if agent_version is not ShapeBase.NOT_SET:
                _params['agent_version'] = agent_version
            if tenancy is not ShapeBase.NOT_SET:
                _params['tenancy'] = tenancy
            _request = shapes.CreateInstanceRequest(**_params)
        response = self._boto_client.create_instance(**_request.to_boto())

        return shapes.CreateInstanceResult.from_boto(response)

    def create_layer(
        self,
        _request: shapes.CreateLayerRequest = None,
        *,
        stack_id: str,
        type: typing.Union[str, shapes.LayerType],
        name: str,
        shortname: str,
        attributes: typing.Dict[typing.Union[str, shapes.LayerAttributesKeys],
                                str] = ShapeBase.NOT_SET,
        cloud_watch_logs_configuration: shapes.
        CloudWatchLogsConfiguration = ShapeBase.NOT_SET,
        custom_instance_profile_arn: str = ShapeBase.NOT_SET,
        custom_json: str = ShapeBase.NOT_SET,
        custom_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        packages: typing.List[str] = ShapeBase.NOT_SET,
        volume_configurations: typing.List[shapes.VolumeConfiguration
                                          ] = ShapeBase.NOT_SET,
        enable_auto_healing: bool = ShapeBase.NOT_SET,
        auto_assign_elastic_ips: bool = ShapeBase.NOT_SET,
        auto_assign_public_ips: bool = ShapeBase.NOT_SET,
        custom_recipes: shapes.Recipes = ShapeBase.NOT_SET,
        install_updates_on_boot: bool = ShapeBase.NOT_SET,
        use_ebs_optimized_instances: bool = ShapeBase.NOT_SET,
        lifecycle_event_configuration: shapes.
        LifecycleEventConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.CreateLayerResult:
        """
        Creates a layer. For more information, see [How to Create a
        Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
        basics-create.html).

        You should use **CreateLayer** for noncustom layer types such as PHP App Server
        only if the stack does not have an existing layer of that type. A stack can have
        at most one instance of each noncustom layer; if you attempt to create a second
        instance, **CreateLayer** fails. A stack can have an arbitrary number of custom
        layers, so you can call **CreateLayer** as many times as you like for that layer
        type.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if shortname is not ShapeBase.NOT_SET:
                _params['shortname'] = shortname
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if cloud_watch_logs_configuration is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_configuration'
                       ] = cloud_watch_logs_configuration
            if custom_instance_profile_arn is not ShapeBase.NOT_SET:
                _params['custom_instance_profile_arn'
                       ] = custom_instance_profile_arn
            if custom_json is not ShapeBase.NOT_SET:
                _params['custom_json'] = custom_json
            if custom_security_group_ids is not ShapeBase.NOT_SET:
                _params['custom_security_group_ids'] = custom_security_group_ids
            if packages is not ShapeBase.NOT_SET:
                _params['packages'] = packages
            if volume_configurations is not ShapeBase.NOT_SET:
                _params['volume_configurations'] = volume_configurations
            if enable_auto_healing is not ShapeBase.NOT_SET:
                _params['enable_auto_healing'] = enable_auto_healing
            if auto_assign_elastic_ips is not ShapeBase.NOT_SET:
                _params['auto_assign_elastic_ips'] = auto_assign_elastic_ips
            if auto_assign_public_ips is not ShapeBase.NOT_SET:
                _params['auto_assign_public_ips'] = auto_assign_public_ips
            if custom_recipes is not ShapeBase.NOT_SET:
                _params['custom_recipes'] = custom_recipes
            if install_updates_on_boot is not ShapeBase.NOT_SET:
                _params['install_updates_on_boot'] = install_updates_on_boot
            if use_ebs_optimized_instances is not ShapeBase.NOT_SET:
                _params['use_ebs_optimized_instances'
                       ] = use_ebs_optimized_instances
            if lifecycle_event_configuration is not ShapeBase.NOT_SET:
                _params['lifecycle_event_configuration'
                       ] = lifecycle_event_configuration
            _request = shapes.CreateLayerRequest(**_params)
        response = self._boto_client.create_layer(**_request.to_boto())

        return shapes.CreateLayerResult.from_boto(response)

    def create_stack(
        self,
        _request: shapes.CreateStackRequest = None,
        *,
        name: str,
        region: str,
        service_role_arn: str,
        default_instance_profile_arn: str,
        vpc_id: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[typing.Union[str, shapes.StackAttributesKeys],
                                str] = ShapeBase.NOT_SET,
        default_os: str = ShapeBase.NOT_SET,
        hostname_theme: str = ShapeBase.NOT_SET,
        default_availability_zone: str = ShapeBase.NOT_SET,
        default_subnet_id: str = ShapeBase.NOT_SET,
        custom_json: str = ShapeBase.NOT_SET,
        configuration_manager: shapes.StackConfigurationManager = ShapeBase.
        NOT_SET,
        chef_configuration: shapes.ChefConfiguration = ShapeBase.NOT_SET,
        use_custom_cookbooks: bool = ShapeBase.NOT_SET,
        use_opsworks_security_groups: bool = ShapeBase.NOT_SET,
        custom_cookbooks_source: shapes.Source = ShapeBase.NOT_SET,
        default_ssh_key_name: str = ShapeBase.NOT_SET,
        default_root_device_type: typing.
        Union[str, shapes.RootDeviceType] = ShapeBase.NOT_SET,
        agent_version: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateStackResult:
        """
        Creates a new stack. For more information, see [Create a New
        Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
        edit.html).

        **Required Permissions** : To use this action, an IAM user must have an attached
        policy that explicitly grants permissions. For more information about user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if region is not ShapeBase.NOT_SET:
                _params['region'] = region
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if default_instance_profile_arn is not ShapeBase.NOT_SET:
                _params['default_instance_profile_arn'
                       ] = default_instance_profile_arn
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if default_os is not ShapeBase.NOT_SET:
                _params['default_os'] = default_os
            if hostname_theme is not ShapeBase.NOT_SET:
                _params['hostname_theme'] = hostname_theme
            if default_availability_zone is not ShapeBase.NOT_SET:
                _params['default_availability_zone'] = default_availability_zone
            if default_subnet_id is not ShapeBase.NOT_SET:
                _params['default_subnet_id'] = default_subnet_id
            if custom_json is not ShapeBase.NOT_SET:
                _params['custom_json'] = custom_json
            if configuration_manager is not ShapeBase.NOT_SET:
                _params['configuration_manager'] = configuration_manager
            if chef_configuration is not ShapeBase.NOT_SET:
                _params['chef_configuration'] = chef_configuration
            if use_custom_cookbooks is not ShapeBase.NOT_SET:
                _params['use_custom_cookbooks'] = use_custom_cookbooks
            if use_opsworks_security_groups is not ShapeBase.NOT_SET:
                _params['use_opsworks_security_groups'
                       ] = use_opsworks_security_groups
            if custom_cookbooks_source is not ShapeBase.NOT_SET:
                _params['custom_cookbooks_source'] = custom_cookbooks_source
            if default_ssh_key_name is not ShapeBase.NOT_SET:
                _params['default_ssh_key_name'] = default_ssh_key_name
            if default_root_device_type is not ShapeBase.NOT_SET:
                _params['default_root_device_type'] = default_root_device_type
            if agent_version is not ShapeBase.NOT_SET:
                _params['agent_version'] = agent_version
            _request = shapes.CreateStackRequest(**_params)
        response = self._boto_client.create_stack(**_request.to_boto())

        return shapes.CreateStackResult.from_boto(response)

    def create_user_profile(
        self,
        _request: shapes.CreateUserProfileRequest = None,
        *,
        iam_user_arn: str,
        ssh_username: str = ShapeBase.NOT_SET,
        ssh_public_key: str = ShapeBase.NOT_SET,
        allow_self_management: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateUserProfileResult:
        """
        Creates a new user profile.

        **Required Permissions** : To use this action, an IAM user must have an attached
        policy that explicitly grants permissions. For more information about user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if iam_user_arn is not ShapeBase.NOT_SET:
                _params['iam_user_arn'] = iam_user_arn
            if ssh_username is not ShapeBase.NOT_SET:
                _params['ssh_username'] = ssh_username
            if ssh_public_key is not ShapeBase.NOT_SET:
                _params['ssh_public_key'] = ssh_public_key
            if allow_self_management is not ShapeBase.NOT_SET:
                _params['allow_self_management'] = allow_self_management
            _request = shapes.CreateUserProfileRequest(**_params)
        response = self._boto_client.create_user_profile(**_request.to_boto())

        return shapes.CreateUserProfileResult.from_boto(response)

    def delete_app(
        self,
        _request: shapes.DeleteAppRequest = None,
        *,
        app_id: str,
    ) -> None:
        """
        Deletes a specified app.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if app_id is not ShapeBase.NOT_SET:
                _params['app_id'] = app_id
            _request = shapes.DeleteAppRequest(**_params)
        response = self._boto_client.delete_app(**_request.to_boto())

    def delete_instance(
        self,
        _request: shapes.DeleteInstanceRequest = None,
        *,
        instance_id: str,
        delete_elastic_ip: bool = ShapeBase.NOT_SET,
        delete_volumes: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a specified instance, which terminates the associated Amazon EC2
        instance. You must stop an instance before you can delete it.

        For more information, see [Deleting
        Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        delete.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if delete_elastic_ip is not ShapeBase.NOT_SET:
                _params['delete_elastic_ip'] = delete_elastic_ip
            if delete_volumes is not ShapeBase.NOT_SET:
                _params['delete_volumes'] = delete_volumes
            _request = shapes.DeleteInstanceRequest(**_params)
        response = self._boto_client.delete_instance(**_request.to_boto())

    def delete_layer(
        self,
        _request: shapes.DeleteLayerRequest = None,
        *,
        layer_id: str,
    ) -> None:
        """
        Deletes a specified layer. You must first stop and then delete all associated
        instances or unassign registered instances. For more information, see [How to
        Delete a
        Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
        basics-delete.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            _request = shapes.DeleteLayerRequest(**_params)
        response = self._boto_client.delete_layer(**_request.to_boto())

    def delete_stack(
        self,
        _request: shapes.DeleteStackRequest = None,
        *,
        stack_id: str,
    ) -> None:
        """
        Deletes a specified stack. You must first delete all instances, layers, and apps
        or deregister registered instances. For more information, see [Shut Down a
        Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-
        shutting.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.DeleteStackRequest(**_params)
        response = self._boto_client.delete_stack(**_request.to_boto())

    def delete_user_profile(
        self,
        _request: shapes.DeleteUserProfileRequest = None,
        *,
        iam_user_arn: str,
    ) -> None:
        """
        Deletes a user profile.

        **Required Permissions** : To use this action, an IAM user must have an attached
        policy that explicitly grants permissions. For more information about user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if iam_user_arn is not ShapeBase.NOT_SET:
                _params['iam_user_arn'] = iam_user_arn
            _request = shapes.DeleteUserProfileRequest(**_params)
        response = self._boto_client.delete_user_profile(**_request.to_boto())

    def deregister_ecs_cluster(
        self,
        _request: shapes.DeregisterEcsClusterRequest = None,
        *,
        ecs_cluster_arn: str,
    ) -> None:
        """
        Deregisters a specified Amazon ECS cluster from a stack. For more information,
        see [ Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
        ecscluster.html#workinglayers-ecscluster-delete).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack or an attached policy that explicitly grants
        permissions. For more information on user permissions, see
        <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-
        users.html>.
        """
        if _request is None:
            _params = {}
            if ecs_cluster_arn is not ShapeBase.NOT_SET:
                _params['ecs_cluster_arn'] = ecs_cluster_arn
            _request = shapes.DeregisterEcsClusterRequest(**_params)
        response = self._boto_client.deregister_ecs_cluster(
            **_request.to_boto()
        )

    def deregister_elastic_ip(
        self,
        _request: shapes.DeregisterElasticIpRequest = None,
        *,
        elastic_ip: str,
    ) -> None:
        """
        Deregisters a specified Elastic IP address. The address can then be registered
        by another stack. For more information, see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            _request = shapes.DeregisterElasticIpRequest(**_params)
        response = self._boto_client.deregister_elastic_ip(**_request.to_boto())

    def deregister_instance(
        self,
        _request: shapes.DeregisterInstanceRequest = None,
        *,
        instance_id: str,
    ) -> None:
        """
        Deregister a registered Amazon EC2 or on-premises instance. This action removes
        the instance from the stack and returns it to your control. This action cannot
        be used with instances that were created with AWS OpsWorks Stacks.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.DeregisterInstanceRequest(**_params)
        response = self._boto_client.deregister_instance(**_request.to_boto())

    def deregister_rds_db_instance(
        self,
        _request: shapes.DeregisterRdsDbInstanceRequest = None,
        *,
        rds_db_instance_arn: str,
    ) -> None:
        """
        Deregisters an Amazon RDS instance.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if rds_db_instance_arn is not ShapeBase.NOT_SET:
                _params['rds_db_instance_arn'] = rds_db_instance_arn
            _request = shapes.DeregisterRdsDbInstanceRequest(**_params)
        response = self._boto_client.deregister_rds_db_instance(
            **_request.to_boto()
        )

    def deregister_volume(
        self,
        _request: shapes.DeregisterVolumeRequest = None,
        *,
        volume_id: str,
    ) -> None:
        """
        Deregisters an Amazon EBS volume. The volume can then be registered by another
        stack. For more information, see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            _request = shapes.DeregisterVolumeRequest(**_params)
        response = self._boto_client.deregister_volume(**_request.to_boto())

    def describe_agent_versions(
        self,
        _request: shapes.DescribeAgentVersionsRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        configuration_manager: shapes.StackConfigurationManager = ShapeBase.
        NOT_SET,
    ) -> shapes.DescribeAgentVersionsResult:
        """
        Describes the available AWS OpsWorks Stacks agent versions. You must specify a
        stack ID or a configuration manager. `DescribeAgentVersions` returns a list of
        available agent versions for the specified stack or configuration manager.
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if configuration_manager is not ShapeBase.NOT_SET:
                _params['configuration_manager'] = configuration_manager
            _request = shapes.DescribeAgentVersionsRequest(**_params)
        response = self._boto_client.describe_agent_versions(
            **_request.to_boto()
        )

        return shapes.DescribeAgentVersionsResult.from_boto(response)

    def describe_apps(
        self,
        _request: shapes.DescribeAppsRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        app_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAppsResult:
        """
        Requests a description of a specified set of apps.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if app_ids is not ShapeBase.NOT_SET:
                _params['app_ids'] = app_ids
            _request = shapes.DescribeAppsRequest(**_params)
        response = self._boto_client.describe_apps(**_request.to_boto())

        return shapes.DescribeAppsResult.from_boto(response)

    def describe_commands(
        self,
        _request: shapes.DescribeCommandsRequest = None,
        *,
        deployment_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        command_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCommandsResult:
        """
        Describes the results of specified commands.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if deployment_id is not ShapeBase.NOT_SET:
                _params['deployment_id'] = deployment_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if command_ids is not ShapeBase.NOT_SET:
                _params['command_ids'] = command_ids
            _request = shapes.DescribeCommandsRequest(**_params)
        response = self._boto_client.describe_commands(**_request.to_boto())

        return shapes.DescribeCommandsResult.from_boto(response)

    def describe_deployments(
        self,
        _request: shapes.DescribeDeploymentsRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        app_id: str = ShapeBase.NOT_SET,
        deployment_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDeploymentsResult:
        """
        Requests a description of a specified set of deployments.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if app_id is not ShapeBase.NOT_SET:
                _params['app_id'] = app_id
            if deployment_ids is not ShapeBase.NOT_SET:
                _params['deployment_ids'] = deployment_ids
            _request = shapes.DescribeDeploymentsRequest(**_params)
        response = self._boto_client.describe_deployments(**_request.to_boto())

        return shapes.DescribeDeploymentsResult.from_boto(response)

    def describe_ecs_clusters(
        self,
        _request: shapes.DescribeEcsClustersRequest = None,
        *,
        ecs_cluster_arns: typing.List[str] = ShapeBase.NOT_SET,
        stack_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEcsClustersResult:
        """
        Describes Amazon ECS clusters that are registered with a stack. If you specify
        only a stack ID, you can use the `MaxResults` and `NextToken` parameters to
        paginate the response. However, AWS OpsWorks Stacks currently supports only one
        cluster per layer, so the result set has a maximum of one element.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack or an attached policy that
        explicitly grants permission. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).

        This call accepts only one resource-identifying parameter.
        """
        if _request is None:
            _params = {}
            if ecs_cluster_arns is not ShapeBase.NOT_SET:
                _params['ecs_cluster_arns'] = ecs_cluster_arns
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeEcsClustersRequest(**_params)
        paginator = self.get_paginator("describe_ecs_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEcsClustersResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEcsClustersResult.from_boto(response)

    def describe_elastic_ips(
        self,
        _request: shapes.DescribeElasticIpsRequest = None,
        *,
        instance_id: str = ShapeBase.NOT_SET,
        stack_id: str = ShapeBase.NOT_SET,
        ips: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeElasticIpsResult:
        """
        Describes [Elastic IP
        addresses](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
        addresses-eip.html).

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if ips is not ShapeBase.NOT_SET:
                _params['ips'] = ips
            _request = shapes.DescribeElasticIpsRequest(**_params)
        response = self._boto_client.describe_elastic_ips(**_request.to_boto())

        return shapes.DescribeElasticIpsResult.from_boto(response)

    def describe_elastic_load_balancers(
        self,
        _request: shapes.DescribeElasticLoadBalancersRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        layer_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeElasticLoadBalancersResult:
        """
        Describes a stack's Elastic Load Balancing instances.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            _request = shapes.DescribeElasticLoadBalancersRequest(**_params)
        response = self._boto_client.describe_elastic_load_balancers(
            **_request.to_boto()
        )

        return shapes.DescribeElasticLoadBalancersResult.from_boto(response)

    def describe_instances(
        self,
        _request: shapes.DescribeInstancesRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        layer_id: str = ShapeBase.NOT_SET,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancesResult:
        """
        Requests a description of a set of instances.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.DescribeInstancesRequest(**_params)
        response = self._boto_client.describe_instances(**_request.to_boto())

        return shapes.DescribeInstancesResult.from_boto(response)

    def describe_layers(
        self,
        _request: shapes.DescribeLayersRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        layer_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLayersResult:
        """
        Requests a description of one or more layers in a specified stack.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            _request = shapes.DescribeLayersRequest(**_params)
        response = self._boto_client.describe_layers(**_request.to_boto())

        return shapes.DescribeLayersResult.from_boto(response)

    def describe_load_based_auto_scaling(
        self,
        _request: shapes.DescribeLoadBasedAutoScalingRequest = None,
        *,
        layer_ids: typing.List[str],
    ) -> shapes.DescribeLoadBasedAutoScalingResult:
        """
        Describes load-based auto scaling configurations for specified layers.

        You must specify at least one of the parameters.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            _request = shapes.DescribeLoadBasedAutoScalingRequest(**_params)
        response = self._boto_client.describe_load_based_auto_scaling(
            **_request.to_boto()
        )

        return shapes.DescribeLoadBasedAutoScalingResult.from_boto(response)

    def describe_my_user_profile(self, ) -> shapes.DescribeMyUserProfileResult:
        """
        Describes a user's SSH information.

        **Required Permissions** : To use this action, an IAM user must have self-
        management enabled or an attached policy that explicitly grants permissions. For
        more information about user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        response = self._boto_client.describe_my_user_profile()

        return shapes.DescribeMyUserProfileResult.from_boto(response)

    def describe_operating_systems(
        self,
    ) -> shapes.DescribeOperatingSystemsResponse:
        """
        Describes the operating systems that are supported by AWS OpsWorks Stacks.
        """
        response = self._boto_client.describe_operating_systems()

        return shapes.DescribeOperatingSystemsResponse.from_boto(response)

    def describe_permissions(
        self,
        _request: shapes.DescribePermissionsRequest = None,
        *,
        iam_user_arn: str = ShapeBase.NOT_SET,
        stack_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePermissionsResult:
        """
        Describes the permissions for a specified stack.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if iam_user_arn is not ShapeBase.NOT_SET:
                _params['iam_user_arn'] = iam_user_arn
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.DescribePermissionsRequest(**_params)
        response = self._boto_client.describe_permissions(**_request.to_boto())

        return shapes.DescribePermissionsResult.from_boto(response)

    def describe_raid_arrays(
        self,
        _request: shapes.DescribeRaidArraysRequest = None,
        *,
        instance_id: str = ShapeBase.NOT_SET,
        stack_id: str = ShapeBase.NOT_SET,
        raid_array_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRaidArraysResult:
        """
        Describe an instance's RAID arrays.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if raid_array_ids is not ShapeBase.NOT_SET:
                _params['raid_array_ids'] = raid_array_ids
            _request = shapes.DescribeRaidArraysRequest(**_params)
        response = self._boto_client.describe_raid_arrays(**_request.to_boto())

        return shapes.DescribeRaidArraysResult.from_boto(response)

    def describe_rds_db_instances(
        self,
        _request: shapes.DescribeRdsDbInstancesRequest = None,
        *,
        stack_id: str,
        rds_db_instance_arns: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRdsDbInstancesResult:
        """
        Describes Amazon RDS instances.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).

        This call accepts only one resource-identifying parameter.
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if rds_db_instance_arns is not ShapeBase.NOT_SET:
                _params['rds_db_instance_arns'] = rds_db_instance_arns
            _request = shapes.DescribeRdsDbInstancesRequest(**_params)
        response = self._boto_client.describe_rds_db_instances(
            **_request.to_boto()
        )

        return shapes.DescribeRdsDbInstancesResult.from_boto(response)

    def describe_service_errors(
        self,
        _request: shapes.DescribeServiceErrorsRequest = None,
        *,
        stack_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        service_error_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeServiceErrorsResult:
        """
        Describes AWS OpsWorks Stacks service errors.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).

        This call accepts only one resource-identifying parameter.
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if service_error_ids is not ShapeBase.NOT_SET:
                _params['service_error_ids'] = service_error_ids
            _request = shapes.DescribeServiceErrorsRequest(**_params)
        response = self._boto_client.describe_service_errors(
            **_request.to_boto()
        )

        return shapes.DescribeServiceErrorsResult.from_boto(response)

    def describe_stack_provisioning_parameters(
        self,
        _request: shapes.DescribeStackProvisioningParametersRequest = None,
        *,
        stack_id: str,
    ) -> shapes.DescribeStackProvisioningParametersResult:
        """
        Requests a description of a stack's provisioning parameters.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.DescribeStackProvisioningParametersRequest(
                **_params
            )
        response = self._boto_client.describe_stack_provisioning_parameters(
            **_request.to_boto()
        )

        return shapes.DescribeStackProvisioningParametersResult.from_boto(
            response
        )

    def describe_stack_summary(
        self,
        _request: shapes.DescribeStackSummaryRequest = None,
        *,
        stack_id: str,
    ) -> shapes.DescribeStackSummaryResult:
        """
        Describes the number of layers and apps in a specified stack, and the number of
        instances in each state, such as `running_setup` or `online`.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.DescribeStackSummaryRequest(**_params)
        response = self._boto_client.describe_stack_summary(
            **_request.to_boto()
        )

        return shapes.DescribeStackSummaryResult.from_boto(response)

    def describe_stacks(
        self,
        _request: shapes.DescribeStacksRequest = None,
        *,
        stack_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStacksResult:
        """
        Requests a description of one or more stacks.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_ids is not ShapeBase.NOT_SET:
                _params['stack_ids'] = stack_ids
            _request = shapes.DescribeStacksRequest(**_params)
        response = self._boto_client.describe_stacks(**_request.to_boto())

        return shapes.DescribeStacksResult.from_boto(response)

    def describe_time_based_auto_scaling(
        self,
        _request: shapes.DescribeTimeBasedAutoScalingRequest = None,
        *,
        instance_ids: typing.List[str],
    ) -> shapes.DescribeTimeBasedAutoScalingResult:
        """
        Describes time-based auto scaling configurations for specified instances.

        You must specify at least one of the parameters.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.DescribeTimeBasedAutoScalingRequest(**_params)
        response = self._boto_client.describe_time_based_auto_scaling(
            **_request.to_boto()
        )

        return shapes.DescribeTimeBasedAutoScalingResult.from_boto(response)

    def describe_user_profiles(
        self,
        _request: shapes.DescribeUserProfilesRequest = None,
        *,
        iam_user_arns: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeUserProfilesResult:
        """
        Describe specified users.

        **Required Permissions** : To use this action, an IAM user must have an attached
        policy that explicitly grants permissions. For more information about user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if iam_user_arns is not ShapeBase.NOT_SET:
                _params['iam_user_arns'] = iam_user_arns
            _request = shapes.DescribeUserProfilesRequest(**_params)
        response = self._boto_client.describe_user_profiles(
            **_request.to_boto()
        )

        return shapes.DescribeUserProfilesResult.from_boto(response)

    def describe_volumes(
        self,
        _request: shapes.DescribeVolumesRequest = None,
        *,
        instance_id: str = ShapeBase.NOT_SET,
        stack_id: str = ShapeBase.NOT_SET,
        raid_array_id: str = ShapeBase.NOT_SET,
        volume_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVolumesResult:
        """
        Describes an instance's Amazon EBS volumes.

        This call accepts only one resource-identifying parameter.

        **Required Permissions** : To use this action, an IAM user must have a Show,
        Deploy, or Manage permissions level for the stack, or an attached policy that
        explicitly grants permissions. For more information about user permissions, see
        [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if raid_array_id is not ShapeBase.NOT_SET:
                _params['raid_array_id'] = raid_array_id
            if volume_ids is not ShapeBase.NOT_SET:
                _params['volume_ids'] = volume_ids
            _request = shapes.DescribeVolumesRequest(**_params)
        response = self._boto_client.describe_volumes(**_request.to_boto())

        return shapes.DescribeVolumesResult.from_boto(response)

    def detach_elastic_load_balancer(
        self,
        _request: shapes.DetachElasticLoadBalancerRequest = None,
        *,
        elastic_load_balancer_name: str,
        layer_id: str,
    ) -> None:
        """
        Detaches a specified Elastic Load Balancing instance from its layer.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_load_balancer_name is not ShapeBase.NOT_SET:
                _params['elastic_load_balancer_name'
                       ] = elastic_load_balancer_name
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            _request = shapes.DetachElasticLoadBalancerRequest(**_params)
        response = self._boto_client.detach_elastic_load_balancer(
            **_request.to_boto()
        )

    def disassociate_elastic_ip(
        self,
        _request: shapes.DisassociateElasticIpRequest = None,
        *,
        elastic_ip: str,
    ) -> None:
        """
        Disassociates an Elastic IP address from its instance. The address remains
        registered with the stack. For more information, see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            _request = shapes.DisassociateElasticIpRequest(**_params)
        response = self._boto_client.disassociate_elastic_ip(
            **_request.to_boto()
        )

    def get_hostname_suggestion(
        self,
        _request: shapes.GetHostnameSuggestionRequest = None,
        *,
        layer_id: str,
    ) -> shapes.GetHostnameSuggestionResult:
        """
        Gets a generated host name for the specified layer, based on the current host
        name theme.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            _request = shapes.GetHostnameSuggestionRequest(**_params)
        response = self._boto_client.get_hostname_suggestion(
            **_request.to_boto()
        )

        return shapes.GetHostnameSuggestionResult.from_boto(response)

    def grant_access(
        self,
        _request: shapes.GrantAccessRequest = None,
        *,
        instance_id: str,
        valid_for_in_minutes: int = ShapeBase.NOT_SET,
    ) -> shapes.GrantAccessResult:
        """
        This action can be used only with Windows stacks.

        Grants RDP access to a Windows instance for a specified time period.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if valid_for_in_minutes is not ShapeBase.NOT_SET:
                _params['valid_for_in_minutes'] = valid_for_in_minutes
            _request = shapes.GrantAccessRequest(**_params)
        response = self._boto_client.grant_access(**_request.to_boto())

        return shapes.GrantAccessResult.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsRequest = None,
        *,
        resource_arn: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsResult:
        """
        Returns a list of tags that are applied to the specified stack or layer.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListTagsRequest(**_params)
        response = self._boto_client.list_tags(**_request.to_boto())

        return shapes.ListTagsResult.from_boto(response)

    def reboot_instance(
        self,
        _request: shapes.RebootInstanceRequest = None,
        *,
        instance_id: str,
    ) -> None:
        """
        Reboots a specified instance. For more information, see [Starting, Stopping, and
        Rebooting
        Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        starting.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.RebootInstanceRequest(**_params)
        response = self._boto_client.reboot_instance(**_request.to_boto())

    def register_ecs_cluster(
        self,
        _request: shapes.RegisterEcsClusterRequest = None,
        *,
        ecs_cluster_arn: str,
        stack_id: str,
    ) -> shapes.RegisterEcsClusterResult:
        """
        Registers a specified Amazon ECS cluster with a stack. You can register only one
        cluster with a stack. A cluster can be registered with only one stack. For more
        information, see [ Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-
        ecscluster.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [ Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if ecs_cluster_arn is not ShapeBase.NOT_SET:
                _params['ecs_cluster_arn'] = ecs_cluster_arn
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.RegisterEcsClusterRequest(**_params)
        response = self._boto_client.register_ecs_cluster(**_request.to_boto())

        return shapes.RegisterEcsClusterResult.from_boto(response)

    def register_elastic_ip(
        self,
        _request: shapes.RegisterElasticIpRequest = None,
        *,
        elastic_ip: str,
        stack_id: str,
    ) -> shapes.RegisterElasticIpResult:
        """
        Registers an Elastic IP address with a specified stack. An address can be
        registered with only one stack at a time. If the address is already registered,
        you must first deregister it by calling DeregisterElasticIp. For more
        information, see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.RegisterElasticIpRequest(**_params)
        response = self._boto_client.register_elastic_ip(**_request.to_boto())

        return shapes.RegisterElasticIpResult.from_boto(response)

    def register_instance(
        self,
        _request: shapes.RegisterInstanceRequest = None,
        *,
        stack_id: str,
        hostname: str = ShapeBase.NOT_SET,
        public_ip: str = ShapeBase.NOT_SET,
        private_ip: str = ShapeBase.NOT_SET,
        rsa_public_key: str = ShapeBase.NOT_SET,
        rsa_public_key_fingerprint: str = ShapeBase.NOT_SET,
        instance_identity: shapes.InstanceIdentity = ShapeBase.NOT_SET,
    ) -> shapes.RegisterInstanceResult:
        """
        Registers instances that were created outside of AWS OpsWorks Stacks with a
        specified stack.

        We do not recommend using this action to register instances. The complete
        registration operation includes two tasks: installing the AWS OpsWorks Stacks
        agent on the instance, and registering the instance with the stack.
        `RegisterInstance` handles only the second step. You should instead use the AWS
        CLI `register` command, which performs the entire registration operation. For
        more information, see [ Registering an Instance with an AWS OpsWorks Stacks
        Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/registered-
        instances-register.html).

        Registered instances have the same requirements as instances that are created by
        using the CreateInstance API. For example, registered instances must be running
        a supported Linux-based operating system, and they must have a supported
        instance type. For more information about requirements for instances that you
        want to register, see [ Preparing the
        Instance](http://docs.aws.amazon.com/opsworks/latest/userguide/registered-
        instances-register-registering-preparer.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if hostname is not ShapeBase.NOT_SET:
                _params['hostname'] = hostname
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if private_ip is not ShapeBase.NOT_SET:
                _params['private_ip'] = private_ip
            if rsa_public_key is not ShapeBase.NOT_SET:
                _params['rsa_public_key'] = rsa_public_key
            if rsa_public_key_fingerprint is not ShapeBase.NOT_SET:
                _params['rsa_public_key_fingerprint'
                       ] = rsa_public_key_fingerprint
            if instance_identity is not ShapeBase.NOT_SET:
                _params['instance_identity'] = instance_identity
            _request = shapes.RegisterInstanceRequest(**_params)
        response = self._boto_client.register_instance(**_request.to_boto())

        return shapes.RegisterInstanceResult.from_boto(response)

    def register_rds_db_instance(
        self,
        _request: shapes.RegisterRdsDbInstanceRequest = None,
        *,
        stack_id: str,
        rds_db_instance_arn: str,
        db_user: str,
        db_password: str,
    ) -> None:
        """
        Registers an Amazon RDS instance with a stack.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if rds_db_instance_arn is not ShapeBase.NOT_SET:
                _params['rds_db_instance_arn'] = rds_db_instance_arn
            if db_user is not ShapeBase.NOT_SET:
                _params['db_user'] = db_user
            if db_password is not ShapeBase.NOT_SET:
                _params['db_password'] = db_password
            _request = shapes.RegisterRdsDbInstanceRequest(**_params)
        response = self._boto_client.register_rds_db_instance(
            **_request.to_boto()
        )

    def register_volume(
        self,
        _request: shapes.RegisterVolumeRequest = None,
        *,
        stack_id: str,
        ec2_volume_id: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterVolumeResult:
        """
        Registers an Amazon EBS volume with a specified stack. A volume can be
        registered with only one stack at a time. If the volume is already registered,
        you must first deregister it by calling DeregisterVolume. For more information,
        see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if ec2_volume_id is not ShapeBase.NOT_SET:
                _params['ec2_volume_id'] = ec2_volume_id
            _request = shapes.RegisterVolumeRequest(**_params)
        response = self._boto_client.register_volume(**_request.to_boto())

        return shapes.RegisterVolumeResult.from_boto(response)

    def set_load_based_auto_scaling(
        self,
        _request: shapes.SetLoadBasedAutoScalingRequest = None,
        *,
        layer_id: str,
        enable: bool = ShapeBase.NOT_SET,
        up_scaling: shapes.AutoScalingThresholds = ShapeBase.NOT_SET,
        down_scaling: shapes.AutoScalingThresholds = ShapeBase.NOT_SET,
    ) -> None:
        """
        Specify the load-based auto scaling configuration for a specified layer. For
        more information, see [Managing Load with Time-based and Load-based
        Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        autoscaling.html).

        To use load-based auto scaling, you must create a set of load-based auto scaling
        instances. Load-based auto scaling operates only on the instances from that set,
        so you must ensure that you have created enough instances to handle the maximum
        anticipated load.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            if enable is not ShapeBase.NOT_SET:
                _params['enable'] = enable
            if up_scaling is not ShapeBase.NOT_SET:
                _params['up_scaling'] = up_scaling
            if down_scaling is not ShapeBase.NOT_SET:
                _params['down_scaling'] = down_scaling
            _request = shapes.SetLoadBasedAutoScalingRequest(**_params)
        response = self._boto_client.set_load_based_auto_scaling(
            **_request.to_boto()
        )

    def set_permission(
        self,
        _request: shapes.SetPermissionRequest = None,
        *,
        stack_id: str,
        iam_user_arn: str,
        allow_ssh: bool = ShapeBase.NOT_SET,
        allow_sudo: bool = ShapeBase.NOT_SET,
        level: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Specifies a user's permissions. For more information, see [Security and
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/workingsecurity.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if iam_user_arn is not ShapeBase.NOT_SET:
                _params['iam_user_arn'] = iam_user_arn
            if allow_ssh is not ShapeBase.NOT_SET:
                _params['allow_ssh'] = allow_ssh
            if allow_sudo is not ShapeBase.NOT_SET:
                _params['allow_sudo'] = allow_sudo
            if level is not ShapeBase.NOT_SET:
                _params['level'] = level
            _request = shapes.SetPermissionRequest(**_params)
        response = self._boto_client.set_permission(**_request.to_boto())

    def set_time_based_auto_scaling(
        self,
        _request: shapes.SetTimeBasedAutoScalingRequest = None,
        *,
        instance_id: str,
        auto_scaling_schedule: shapes.WeeklyAutoScalingSchedule = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Specify the time-based auto scaling configuration for a specified instance. For
        more information, see [Managing Load with Time-based and Load-based
        Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        autoscaling.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if auto_scaling_schedule is not ShapeBase.NOT_SET:
                _params['auto_scaling_schedule'] = auto_scaling_schedule
            _request = shapes.SetTimeBasedAutoScalingRequest(**_params)
        response = self._boto_client.set_time_based_auto_scaling(
            **_request.to_boto()
        )

    def start_instance(
        self,
        _request: shapes.StartInstanceRequest = None,
        *,
        instance_id: str,
    ) -> None:
        """
        Starts a specified instance. For more information, see [Starting, Stopping, and
        Rebooting
        Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        starting.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.StartInstanceRequest(**_params)
        response = self._boto_client.start_instance(**_request.to_boto())

    def start_stack(
        self,
        _request: shapes.StartStackRequest = None,
        *,
        stack_id: str,
    ) -> None:
        """
        Starts a stack's instances.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.StartStackRequest(**_params)
        response = self._boto_client.start_stack(**_request.to_boto())

    def stop_instance(
        self,
        _request: shapes.StopInstanceRequest = None,
        *,
        instance_id: str,
        force: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Stops a specified instance. When you stop a standard instance, the data
        disappears and must be reinstalled when you restart the instance. You can stop
        an Amazon EBS-backed instance without losing data. For more information, see
        [Starting, Stopping, and Rebooting
        Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-
        starting.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.StopInstanceRequest(**_params)
        response = self._boto_client.stop_instance(**_request.to_boto())

    def stop_stack(
        self,
        _request: shapes.StopStackRequest = None,
        *,
        stack_id: str,
    ) -> None:
        """
        Stops a specified stack.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            _request = shapes.StopStackRequest(**_params)
        response = self._boto_client.stop_stack(**_request.to_boto())

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_arn: str,
        tags: typing.Dict[str, str],
    ) -> None:
        """
        Apply cost-allocation tags to a specified stack or layer in AWS OpsWorks Stacks.
        For more information about how tagging works, see
        [Tags](http://docs.aws.amazon.com/opsworks/latest/userguide/tagging.html) in the
        AWS OpsWorks User Guide.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

    def unassign_instance(
        self,
        _request: shapes.UnassignInstanceRequest = None,
        *,
        instance_id: str,
    ) -> None:
        """
        Unassigns a registered instance from all layers that are using the instance. The
        instance remains in the stack as an unassigned instance, and can be assigned to
        another layer as needed. You cannot use this action with instances that were
        created with AWS OpsWorks Stacks.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack or an attached policy that explicitly grants
        permissions. For more information about user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.UnassignInstanceRequest(**_params)
        response = self._boto_client.unassign_instance(**_request.to_boto())

    def unassign_volume(
        self,
        _request: shapes.UnassignVolumeRequest = None,
        *,
        volume_id: str,
    ) -> None:
        """
        Unassigns an assigned Amazon EBS volume. The volume remains registered with the
        stack. For more information, see [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            _request = shapes.UnassignVolumeRequest(**_params)
        response = self._boto_client.unassign_volume(**_request.to_boto())

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Removes tags from a specified stack or layer.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

    def update_app(
        self,
        _request: shapes.UpdateAppRequest = None,
        *,
        app_id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        data_sources: typing.List[shapes.DataSource] = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.AppType] = ShapeBase.NOT_SET,
        app_source: shapes.Source = ShapeBase.NOT_SET,
        domains: typing.List[str] = ShapeBase.NOT_SET,
        enable_ssl: bool = ShapeBase.NOT_SET,
        ssl_configuration: shapes.SslConfiguration = ShapeBase.NOT_SET,
        attributes: typing.Dict[typing.Union[str, shapes.AppAttributesKeys], str
                               ] = ShapeBase.NOT_SET,
        environment: typing.List[shapes.EnvironmentVariable
                                ] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a specified app.

        **Required Permissions** : To use this action, an IAM user must have a Deploy or
        Manage permissions level for the stack, or an attached policy that explicitly
        grants permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if app_id is not ShapeBase.NOT_SET:
                _params['app_id'] = app_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if data_sources is not ShapeBase.NOT_SET:
                _params['data_sources'] = data_sources
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if app_source is not ShapeBase.NOT_SET:
                _params['app_source'] = app_source
            if domains is not ShapeBase.NOT_SET:
                _params['domains'] = domains
            if enable_ssl is not ShapeBase.NOT_SET:
                _params['enable_ssl'] = enable_ssl
            if ssl_configuration is not ShapeBase.NOT_SET:
                _params['ssl_configuration'] = ssl_configuration
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if environment is not ShapeBase.NOT_SET:
                _params['environment'] = environment
            _request = shapes.UpdateAppRequest(**_params)
        response = self._boto_client.update_app(**_request.to_boto())

    def update_elastic_ip(
        self,
        _request: shapes.UpdateElasticIpRequest = None,
        *,
        elastic_ip: str,
        name: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a registered Elastic IP address's name. For more information, see
        [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateElasticIpRequest(**_params)
        response = self._boto_client.update_elastic_ip(**_request.to_boto())

    def update_instance(
        self,
        _request: shapes.UpdateInstanceRequest = None,
        *,
        instance_id: str,
        layer_ids: typing.List[str] = ShapeBase.NOT_SET,
        instance_type: str = ShapeBase.NOT_SET,
        auto_scaling_type: typing.Union[str, shapes.
                                        AutoScalingType] = ShapeBase.NOT_SET,
        hostname: str = ShapeBase.NOT_SET,
        os: str = ShapeBase.NOT_SET,
        ami_id: str = ShapeBase.NOT_SET,
        ssh_key_name: str = ShapeBase.NOT_SET,
        architecture: typing.Union[str, shapes.Architecture] = ShapeBase.
        NOT_SET,
        install_updates_on_boot: bool = ShapeBase.NOT_SET,
        ebs_optimized: bool = ShapeBase.NOT_SET,
        agent_version: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a specified instance.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if layer_ids is not ShapeBase.NOT_SET:
                _params['layer_ids'] = layer_ids
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if auto_scaling_type is not ShapeBase.NOT_SET:
                _params['auto_scaling_type'] = auto_scaling_type
            if hostname is not ShapeBase.NOT_SET:
                _params['hostname'] = hostname
            if os is not ShapeBase.NOT_SET:
                _params['os'] = os
            if ami_id is not ShapeBase.NOT_SET:
                _params['ami_id'] = ami_id
            if ssh_key_name is not ShapeBase.NOT_SET:
                _params['ssh_key_name'] = ssh_key_name
            if architecture is not ShapeBase.NOT_SET:
                _params['architecture'] = architecture
            if install_updates_on_boot is not ShapeBase.NOT_SET:
                _params['install_updates_on_boot'] = install_updates_on_boot
            if ebs_optimized is not ShapeBase.NOT_SET:
                _params['ebs_optimized'] = ebs_optimized
            if agent_version is not ShapeBase.NOT_SET:
                _params['agent_version'] = agent_version
            _request = shapes.UpdateInstanceRequest(**_params)
        response = self._boto_client.update_instance(**_request.to_boto())

    def update_layer(
        self,
        _request: shapes.UpdateLayerRequest = None,
        *,
        layer_id: str,
        name: str = ShapeBase.NOT_SET,
        shortname: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[typing.Union[str, shapes.LayerAttributesKeys],
                                str] = ShapeBase.NOT_SET,
        cloud_watch_logs_configuration: shapes.
        CloudWatchLogsConfiguration = ShapeBase.NOT_SET,
        custom_instance_profile_arn: str = ShapeBase.NOT_SET,
        custom_json: str = ShapeBase.NOT_SET,
        custom_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        packages: typing.List[str] = ShapeBase.NOT_SET,
        volume_configurations: typing.List[shapes.VolumeConfiguration
                                          ] = ShapeBase.NOT_SET,
        enable_auto_healing: bool = ShapeBase.NOT_SET,
        auto_assign_elastic_ips: bool = ShapeBase.NOT_SET,
        auto_assign_public_ips: bool = ShapeBase.NOT_SET,
        custom_recipes: shapes.Recipes = ShapeBase.NOT_SET,
        install_updates_on_boot: bool = ShapeBase.NOT_SET,
        use_ebs_optimized_instances: bool = ShapeBase.NOT_SET,
        lifecycle_event_configuration: shapes.
        LifecycleEventConfiguration = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a specified layer.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if layer_id is not ShapeBase.NOT_SET:
                _params['layer_id'] = layer_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if shortname is not ShapeBase.NOT_SET:
                _params['shortname'] = shortname
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if cloud_watch_logs_configuration is not ShapeBase.NOT_SET:
                _params['cloud_watch_logs_configuration'
                       ] = cloud_watch_logs_configuration
            if custom_instance_profile_arn is not ShapeBase.NOT_SET:
                _params['custom_instance_profile_arn'
                       ] = custom_instance_profile_arn
            if custom_json is not ShapeBase.NOT_SET:
                _params['custom_json'] = custom_json
            if custom_security_group_ids is not ShapeBase.NOT_SET:
                _params['custom_security_group_ids'] = custom_security_group_ids
            if packages is not ShapeBase.NOT_SET:
                _params['packages'] = packages
            if volume_configurations is not ShapeBase.NOT_SET:
                _params['volume_configurations'] = volume_configurations
            if enable_auto_healing is not ShapeBase.NOT_SET:
                _params['enable_auto_healing'] = enable_auto_healing
            if auto_assign_elastic_ips is not ShapeBase.NOT_SET:
                _params['auto_assign_elastic_ips'] = auto_assign_elastic_ips
            if auto_assign_public_ips is not ShapeBase.NOT_SET:
                _params['auto_assign_public_ips'] = auto_assign_public_ips
            if custom_recipes is not ShapeBase.NOT_SET:
                _params['custom_recipes'] = custom_recipes
            if install_updates_on_boot is not ShapeBase.NOT_SET:
                _params['install_updates_on_boot'] = install_updates_on_boot
            if use_ebs_optimized_instances is not ShapeBase.NOT_SET:
                _params['use_ebs_optimized_instances'
                       ] = use_ebs_optimized_instances
            if lifecycle_event_configuration is not ShapeBase.NOT_SET:
                _params['lifecycle_event_configuration'
                       ] = lifecycle_event_configuration
            _request = shapes.UpdateLayerRequest(**_params)
        response = self._boto_client.update_layer(**_request.to_boto())

    def update_my_user_profile(
        self,
        _request: shapes.UpdateMyUserProfileRequest = None,
        *,
        ssh_public_key: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a user's SSH public key.

        **Required Permissions** : To use this action, an IAM user must have self-
        management enabled or an attached policy that explicitly grants permissions. For
        more information about user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if ssh_public_key is not ShapeBase.NOT_SET:
                _params['ssh_public_key'] = ssh_public_key
            _request = shapes.UpdateMyUserProfileRequest(**_params)
        response = self._boto_client.update_my_user_profile(
            **_request.to_boto()
        )

    def update_rds_db_instance(
        self,
        _request: shapes.UpdateRdsDbInstanceRequest = None,
        *,
        rds_db_instance_arn: str,
        db_user: str = ShapeBase.NOT_SET,
        db_password: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates an Amazon RDS instance.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if rds_db_instance_arn is not ShapeBase.NOT_SET:
                _params['rds_db_instance_arn'] = rds_db_instance_arn
            if db_user is not ShapeBase.NOT_SET:
                _params['db_user'] = db_user
            if db_password is not ShapeBase.NOT_SET:
                _params['db_password'] = db_password
            _request = shapes.UpdateRdsDbInstanceRequest(**_params)
        response = self._boto_client.update_rds_db_instance(
            **_request.to_boto()
        )

    def update_stack(
        self,
        _request: shapes.UpdateStackRequest = None,
        *,
        stack_id: str,
        name: str = ShapeBase.NOT_SET,
        attributes: typing.Dict[typing.Union[str, shapes.StackAttributesKeys],
                                str] = ShapeBase.NOT_SET,
        service_role_arn: str = ShapeBase.NOT_SET,
        default_instance_profile_arn: str = ShapeBase.NOT_SET,
        default_os: str = ShapeBase.NOT_SET,
        hostname_theme: str = ShapeBase.NOT_SET,
        default_availability_zone: str = ShapeBase.NOT_SET,
        default_subnet_id: str = ShapeBase.NOT_SET,
        custom_json: str = ShapeBase.NOT_SET,
        configuration_manager: shapes.StackConfigurationManager = ShapeBase.
        NOT_SET,
        chef_configuration: shapes.ChefConfiguration = ShapeBase.NOT_SET,
        use_custom_cookbooks: bool = ShapeBase.NOT_SET,
        custom_cookbooks_source: shapes.Source = ShapeBase.NOT_SET,
        default_ssh_key_name: str = ShapeBase.NOT_SET,
        default_root_device_type: typing.
        Union[str, shapes.RootDeviceType] = ShapeBase.NOT_SET,
        use_opsworks_security_groups: bool = ShapeBase.NOT_SET,
        agent_version: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a specified stack.

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if stack_id is not ShapeBase.NOT_SET:
                _params['stack_id'] = stack_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if default_instance_profile_arn is not ShapeBase.NOT_SET:
                _params['default_instance_profile_arn'
                       ] = default_instance_profile_arn
            if default_os is not ShapeBase.NOT_SET:
                _params['default_os'] = default_os
            if hostname_theme is not ShapeBase.NOT_SET:
                _params['hostname_theme'] = hostname_theme
            if default_availability_zone is not ShapeBase.NOT_SET:
                _params['default_availability_zone'] = default_availability_zone
            if default_subnet_id is not ShapeBase.NOT_SET:
                _params['default_subnet_id'] = default_subnet_id
            if custom_json is not ShapeBase.NOT_SET:
                _params['custom_json'] = custom_json
            if configuration_manager is not ShapeBase.NOT_SET:
                _params['configuration_manager'] = configuration_manager
            if chef_configuration is not ShapeBase.NOT_SET:
                _params['chef_configuration'] = chef_configuration
            if use_custom_cookbooks is not ShapeBase.NOT_SET:
                _params['use_custom_cookbooks'] = use_custom_cookbooks
            if custom_cookbooks_source is not ShapeBase.NOT_SET:
                _params['custom_cookbooks_source'] = custom_cookbooks_source
            if default_ssh_key_name is not ShapeBase.NOT_SET:
                _params['default_ssh_key_name'] = default_ssh_key_name
            if default_root_device_type is not ShapeBase.NOT_SET:
                _params['default_root_device_type'] = default_root_device_type
            if use_opsworks_security_groups is not ShapeBase.NOT_SET:
                _params['use_opsworks_security_groups'
                       ] = use_opsworks_security_groups
            if agent_version is not ShapeBase.NOT_SET:
                _params['agent_version'] = agent_version
            _request = shapes.UpdateStackRequest(**_params)
        response = self._boto_client.update_stack(**_request.to_boto())

    def update_user_profile(
        self,
        _request: shapes.UpdateUserProfileRequest = None,
        *,
        iam_user_arn: str,
        ssh_username: str = ShapeBase.NOT_SET,
        ssh_public_key: str = ShapeBase.NOT_SET,
        allow_self_management: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a specified user profile.

        **Required Permissions** : To use this action, an IAM user must have an attached
        policy that explicitly grants permissions. For more information about user
        permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if iam_user_arn is not ShapeBase.NOT_SET:
                _params['iam_user_arn'] = iam_user_arn
            if ssh_username is not ShapeBase.NOT_SET:
                _params['ssh_username'] = ssh_username
            if ssh_public_key is not ShapeBase.NOT_SET:
                _params['ssh_public_key'] = ssh_public_key
            if allow_self_management is not ShapeBase.NOT_SET:
                _params['allow_self_management'] = allow_self_management
            _request = shapes.UpdateUserProfileRequest(**_params)
        response = self._boto_client.update_user_profile(**_request.to_boto())

    def update_volume(
        self,
        _request: shapes.UpdateVolumeRequest = None,
        *,
        volume_id: str,
        name: str = ShapeBase.NOT_SET,
        mount_point: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates an Amazon EBS volume's name or mount point. For more information, see
        [Resource
        Management](http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html).

        **Required Permissions** : To use this action, an IAM user must have a Manage
        permissions level for the stack, or an attached policy that explicitly grants
        permissions. For more information on user permissions, see [Managing User
        Permissions](http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-
        security-users.html).
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if mount_point is not ShapeBase.NOT_SET:
                _params['mount_point'] = mount_point
            _request = shapes.UpdateVolumeRequest(**_params)
        response = self._boto_client.update_volume(**_request.to_boto())
