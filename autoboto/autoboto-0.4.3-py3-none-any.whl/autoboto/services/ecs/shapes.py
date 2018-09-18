import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    You do not have authorization to perform the requested action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class AgentUpdateStatus(str):
    PENDING = "PENDING"
    STAGING = "STAGING"
    STAGED = "STAGED"
    UPDATING = "UPDATING"
    UPDATED = "UPDATED"
    FAILED = "FAILED"


class AssignPublicIp(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class Attachment(ShapeBase):
    """
    An object representing a container instance or task attachment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "details",
                "details",
                TypeInfo(typing.List[KeyValuePair]),
            ),
        ]

    # The unique identifier for the attachment.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the attachment, such as `ElasticNetworkInterface`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the attachment. Valid values are `PRECREATED`, `CREATED`,
    # `ATTACHING`, `ATTACHED`, `DETACHING`, `DETACHED`, and `DELETED`.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details of the attachment. For elastic network interfaces, this includes
    # the network interface ID, the MAC address, the subnet ID, and the private
    # IPv4 address.
    details: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachmentStateChange(ShapeBase):
    """
    An object representing a change in state for a task attachment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_arn",
                "attachmentArn",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the attachment.
    attachment_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the attachment.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Attribute(ShapeBase):
    """
    An attribute is a name-value pair associated with an Amazon ECS object.
    Attributes enable you to extend the Amazon ECS data model by adding custom
    metadata to your resources. For more information, see
    [Attributes](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    placement-constraints.html#attributes) in the _Amazon Elastic Container Service
    Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "target_type",
                "targetType",
                TypeInfo(typing.Union[str, TargetType]),
            ),
            (
                "target_id",
                "targetId",
                TypeInfo(str),
            ),
        ]

    # The name of the attribute. Up to 128 letters (uppercase and lowercase),
    # numbers, hyphens, underscores, and periods are allowed.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute. Up to 128 letters (uppercase and lowercase),
    # numbers, hyphens, underscores, periods, at signs (@), forward slashes,
    # colons, and spaces are allowed.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the target with which to attach the attribute. This parameter
    # is required if you use the short form ID for a resource instead of the full
    # ARN.
    target_type: typing.Union[str, "TargetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the target. You can specify the short form ID for a resource or
    # the full Amazon Resource Name (ARN).
    target_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttributeLimitExceededException(ShapeBase):
    """
    You can apply up to 10 custom attributes per resource. You can view the
    attributes of a resource with ListAttributes. You can remove existing attributes
    on a resource with DeleteAttributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AwsVpcConfiguration(ShapeBase):
    """
    An object representing the networking details for a task or service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subnets",
                "subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_groups",
                "securityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "assign_public_ip",
                "assignPublicIp",
                TypeInfo(typing.Union[str, AssignPublicIp]),
            ),
        ]

    # The subnets associated with the task or service. There is a limit of 10
    # subnets able to be specified per `AwsVpcConfiguration`.

    # All specified subnets must be from the same VPC.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security groups associated with the task or service. If you do not
    # specify a security group, the default security group for the VPC is used.
    # There is a limit of 5 security groups able to be specified per
    # `AwsVpcConfiguration`.

    # All specified security groups must be from the same VPC.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the task's elastic network interface receives a public IP address.
    # The default value is `DISABLED`.
    assign_public_ip: typing.Union[str, "AssignPublicIp"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BlockedException(ShapeBase):
    """
    Your AWS account has been blocked. [Contact AWS
    Support](http://aws.amazon.com/contact-us/) for more information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClientException(ShapeBase):
    """
    These errors are usually caused by a client action, such as using an action or
    resource on behalf of a user that doesn't have permissions to use the action or
    resource, or specifying an identifier that is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Cluster(ShapeBase):
    """
    A regional grouping of one or more container instances on which you can run task
    requests. Each account receives a default cluster the first time you use the
    Amazon ECS service, but you may also create other clusters. Clusters may contain
    more than one instance type simultaneously.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_arn",
                "clusterArn",
                TypeInfo(str),
            ),
            (
                "cluster_name",
                "clusterName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "registered_container_instances_count",
                "registeredContainerInstancesCount",
                TypeInfo(int),
            ),
            (
                "running_tasks_count",
                "runningTasksCount",
                TypeInfo(int),
            ),
            (
                "pending_tasks_count",
                "pendingTasksCount",
                TypeInfo(int),
            ),
            (
                "active_services_count",
                "activeServicesCount",
                TypeInfo(int),
            ),
            (
                "statistics",
                "statistics",
                TypeInfo(typing.List[KeyValuePair]),
            ),
        ]

    # The Amazon Resource Name (ARN) that identifies the cluster. The ARN
    # contains the `arn:aws:ecs` namespace, followed by the Region of the
    # cluster, the AWS account ID of the cluster owner, the `cluster` namespace,
    # and then the cluster name. For example, `arn:aws:ecs: _region_ :
    # _012345678910_ :cluster/ _test_ `..
    cluster_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A user-generated string that you use to identify your cluster.
    cluster_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the cluster. The valid values are `ACTIVE` or `INACTIVE`.
    # `ACTIVE` indicates that you can register container instances with the
    # cluster and the associated instances can accept tasks.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of container instances registered into the cluster. This
    # includes container instances in both `ACTIVE` and `DRAINING` status.
    registered_container_instances_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of tasks in the cluster that are in the `RUNNING` state.
    running_tasks_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks in the cluster that are in the `PENDING` state.
    pending_tasks_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of services that are running on the cluster in an `ACTIVE`
    # state. You can view these services with ListServices.
    active_services_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about your clusters that are separated by launch
    # type, including:

    #   * runningEC2TasksCount

    #   * RunningFargateTasksCount

    #   * pendingEC2TasksCount

    #   * pendingFargateTasksCount

    #   * activeEC2ServiceCount

    #   * activeFargateServiceCount

    #   * drainingEC2ServiceCount

    #   * drainingFargateServiceCount
    statistics: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ClusterContainsContainerInstancesException(ShapeBase):
    """
    You cannot delete a cluster that has registered container instances. You must
    first deregister the container instances before you can delete the cluster. For
    more information, see DeregisterContainerInstance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterContainsServicesException(ShapeBase):
    """
    You cannot delete a cluster that contains services. You must first update the
    service to reduce its desired task count to 0 and then delete the service. For
    more information, see UpdateService and DeleteService.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ClusterContainsTasksException(ShapeBase):
    """
    You cannot delete a cluster that has active tasks.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class ClusterField(str):
    STATISTICS = "STATISTICS"


@dataclasses.dataclass
class ClusterNotFoundException(ShapeBase):
    """
    The specified cluster could not be found. You can view your available clusters
    with ListClusters. Amazon ECS clusters are region-specific.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class Compatibility(str):
    EC2 = "EC2"
    FARGATE = "FARGATE"


class Connectivity(str):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"


@dataclasses.dataclass
class Container(ShapeBase):
    """
    A Docker container that is part of a task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_arn",
                "containerArn",
                TypeInfo(str),
            ),
            (
                "task_arn",
                "taskArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "last_status",
                "lastStatus",
                TypeInfo(str),
            ),
            (
                "exit_code",
                "exitCode",
                TypeInfo(int),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
            (
                "network_bindings",
                "networkBindings",
                TypeInfo(typing.List[NetworkBinding]),
            ),
            (
                "network_interfaces",
                "networkInterfaces",
                TypeInfo(typing.List[NetworkInterface]),
            ),
            (
                "health_status",
                "healthStatus",
                TypeInfo(typing.Union[str, HealthStatus]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the container.
    container_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the task.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the container.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last known status of the container.
    last_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The exit code returned from the container.
    exit_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short (255 max characters) human-readable string to provide additional
    # details about a running or stopped container.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network bindings associated with the container.
    network_bindings: typing.List["NetworkBinding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The network interfaces associated with the container.
    network_interfaces: typing.List["NetworkInterface"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The health status of the container. If health checks are not configured for
    # this container in its task definition, then it reports health status as
    # `UNKNOWN`.
    health_status: typing.Union[str, "HealthStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContainerDefinition(ShapeBase):
    """
    Container definitions are used in task definitions to describe the different
    containers that are launched as part of a task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "image",
                "image",
                TypeInfo(str),
            ),
            (
                "repository_credentials",
                "repositoryCredentials",
                TypeInfo(RepositoryCredentials),
            ),
            (
                "cpu",
                "cpu",
                TypeInfo(int),
            ),
            (
                "memory",
                "memory",
                TypeInfo(int),
            ),
            (
                "memory_reservation",
                "memoryReservation",
                TypeInfo(int),
            ),
            (
                "links",
                "links",
                TypeInfo(typing.List[str]),
            ),
            (
                "port_mappings",
                "portMappings",
                TypeInfo(typing.List[PortMapping]),
            ),
            (
                "essential",
                "essential",
                TypeInfo(bool),
            ),
            (
                "entry_point",
                "entryPoint",
                TypeInfo(typing.List[str]),
            ),
            (
                "command",
                "command",
                TypeInfo(typing.List[str]),
            ),
            (
                "environment",
                "environment",
                TypeInfo(typing.List[KeyValuePair]),
            ),
            (
                "mount_points",
                "mountPoints",
                TypeInfo(typing.List[MountPoint]),
            ),
            (
                "volumes_from",
                "volumesFrom",
                TypeInfo(typing.List[VolumeFrom]),
            ),
            (
                "linux_parameters",
                "linuxParameters",
                TypeInfo(LinuxParameters),
            ),
            (
                "hostname",
                "hostname",
                TypeInfo(str),
            ),
            (
                "user",
                "user",
                TypeInfo(str),
            ),
            (
                "working_directory",
                "workingDirectory",
                TypeInfo(str),
            ),
            (
                "disable_networking",
                "disableNetworking",
                TypeInfo(bool),
            ),
            (
                "privileged",
                "privileged",
                TypeInfo(bool),
            ),
            (
                "readonly_root_filesystem",
                "readonlyRootFilesystem",
                TypeInfo(bool),
            ),
            (
                "dns_servers",
                "dnsServers",
                TypeInfo(typing.List[str]),
            ),
            (
                "dns_search_domains",
                "dnsSearchDomains",
                TypeInfo(typing.List[str]),
            ),
            (
                "extra_hosts",
                "extraHosts",
                TypeInfo(typing.List[HostEntry]),
            ),
            (
                "docker_security_options",
                "dockerSecurityOptions",
                TypeInfo(typing.List[str]),
            ),
            (
                "docker_labels",
                "dockerLabels",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ulimits",
                "ulimits",
                TypeInfo(typing.List[Ulimit]),
            ),
            (
                "log_configuration",
                "logConfiguration",
                TypeInfo(LogConfiguration),
            ),
            (
                "health_check",
                "healthCheck",
                TypeInfo(HealthCheck),
            ),
        ]

    # The name of a container. If you are linking multiple containers together in
    # a task definition, the `name` of one container can be entered in the
    # `links` of another container to connect the containers. Up to 255 letters
    # (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    # This parameter maps to `name` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--name` option to
    # [docker run](https://docs.docker.com/engine/reference/run/).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The image used to start a container. This string is passed directly to the
    # Docker daemon. Images in the Docker Hub registry are available by default.
    # Other repositories are specified with either ` _repository-url_ / _image_ :
    # _tag_ ` or ` _repository-url_ / _image_ @ _digest_ `. Up to 255 letters
    # (uppercase and lowercase), numbers, hyphens, underscores, colons, periods,
    # forward slashes, and number signs are allowed. This parameter maps to
    # `Image` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `IMAGE` parameter
    # of [docker run](https://docs.docker.com/engine/reference/run/).

    #   * When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.

    #   * Images in Amazon ECR repositories can be specified by either using the full `registry/repository:tag` or `registry/repository@digest`. For example, `012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest` or `012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`.

    #   * Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo`).

    #   * Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent`).

    #   * Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu`).
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private repository authentication credentials to use.
    repository_credentials: "RepositoryCredentials" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of `cpu` units reserved for the container. This parameter maps
    # to `CpuShares` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--cpu-shares`
    # option to [docker run](https://docs.docker.com/engine/reference/run/).

    # This field is optional for tasks using the Fargate launch type, and the
    # only requirement is that the total amount of CPU reserved for all
    # containers within a task be lower than the task-level `cpu` value.

    # You can determine the number of CPU units that are available per EC2
    # instance type by multiplying the vCPUs listed for that instance type on the
    # [Amazon EC2 Instances](http://aws.amazon.com/ec2/instance-types/) detail
    # page by 1,024.

    # For example, if you run a single-container task on a single-core instance
    # type with 512 CPU units specified for that container, and that is the only
    # task running on the container instance, that container could use the full
    # 1,024 CPU unit share at any given time. However, if you launched another
    # copy of the same task on that container instance, each task would be
    # guaranteed a minimum of 512 CPU units when needed, and each container could
    # float to higher CPU usage if the other container was not using it, but if
    # both tasks were 100% active all of the time, they would be limited to 512
    # CPU units.

    # Linux containers share unallocated CPU units with other containers on the
    # container instance with the same ratio as their allocated amount. For
    # example, if you run a single-container task on a single-core instance type
    # with 512 CPU units specified for that container, and that is the only task
    # running on the container instance, that container could use the full 1,024
    # CPU unit share at any given time. However, if you launched another copy of
    # the same task on that container instance, each task would be guaranteed a
    # minimum of 512 CPU units when needed, and each container could float to
    # higher CPU usage if the other container was not using it, but if both tasks
    # were 100% active all of the time, they would be limited to 512 CPU units.

    # On Linux container instances, the Docker daemon on the container instance
    # uses the CPU value to calculate the relative CPU share ratios for running
    # containers. For more information, see [CPU share
    # constraint](https://docs.docker.com/engine/reference/run/#cpu-share-
    # constraint) in the Docker documentation. The minimum valid CPU share value
    # that the Linux kernel allows is 2; however, the CPU parameter is not
    # required, and you can use CPU values below 2 in your container definitions.
    # For CPU values below 2 (including null), the behavior varies based on your
    # Amazon ECS container agent version:

    #   * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to 2 CPU shares.

    #   * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2.

    # On Windows container instances, the CPU limit is enforced as an absolute
    # limit, or a quota. Windows containers only have access to the specified
    # amount of CPU that is described in the task definition.
    cpu: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hard limit (in MiB) of memory to present to the container. If your
    # container attempts to exceed the memory specified here, the container is
    # killed. This parameter maps to `Memory` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--memory` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # If your containers are part of a task using the Fargate launch type, this
    # field is optional and the only requirement is that the total amount of
    # memory reserved for all containers within a task be lower than the task
    # `memory` value.

    # For containers that are part of a task using the EC2 launch type, you must
    # specify a non-zero integer for one or both of `memory` or
    # `memoryReservation` in container definitions. If you specify both, `memory`
    # must be greater than `memoryReservation`. If you specify
    # `memoryReservation`, then that value is subtracted from the available
    # memory resources for the container instance on which the container is
    # placed; otherwise, the value of `memory` is used.

    # The Docker daemon reserves a minimum of 4 MiB of memory for a container, so
    # you should not specify fewer than 4 MiB of memory for your containers.
    memory: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The soft limit (in MiB) of memory to reserve for the container. When system
    # memory is under heavy contention, Docker attempts to keep the container
    # memory to this soft limit; however, your container can consume more memory
    # when it needs to, up to either the hard limit specified with the `memory`
    # parameter (if applicable), or all of the available memory on the container
    # instance, whichever comes first. This parameter maps to `MemoryReservation`
    # in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--memory-
    # reservation` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).

    # You must specify a non-zero integer for one or both of `memory` or
    # `memoryReservation` in container definitions. If you specify both, `memory`
    # must be greater than `memoryReservation`. If you specify
    # `memoryReservation`, then that value is subtracted from the available
    # memory resources for the container instance on which the container is
    # placed; otherwise, the value of `memory` is used.

    # For example, if your container normally uses 128 MiB of memory, but
    # occasionally bursts to 256 MiB of memory for short periods of time, you can
    # set a `memoryReservation` of 128 MiB, and a `memory` hard limit of 300 MiB.
    # This configuration would allow the container to only reserve 128 MiB of
    # memory from the remaining resources on the container instance, but also
    # allow the container to consume more memory resources when needed.

    # The Docker daemon reserves a minimum of 4 MiB of memory for a container, so
    # you should not specify fewer than 4 MiB of memory for your containers.
    memory_reservation: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `link` parameter allows containers to communicate with each other
    # without the need for port mappings. Only supported if the network mode of a
    # task definition is set to `bridge`. The `name:internalName` construct is
    # analogous to `name:alias` in Docker links. Up to 255 letters (uppercase and
    # lowercase), numbers, hyphens, and underscores are allowed. For more
    # information about linking Docker containers, go to
    # <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>.
    # This parameter maps to `Links` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--link` option to
    # [ `docker run`
    # ](https://docs.docker.com/engine/reference/commandline/run/).

    # This parameter is not supported for Windows containers.

    # Containers that are collocated on a single container instance may be able
    # to communicate with each other without requiring links or host port
    # mappings. Network isolation is achieved on the container instance using
    # security groups and VPC settings.
    links: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of port mappings for the container. Port mappings allow containers
    # to access ports on the host container instance to send or receive traffic.

    # For task definitions that use the `awsvpc` network mode, you should only
    # specify the `containerPort`. The `hostPort` can be left blank or it must be
    # the same value as the `containerPort`.

    # Port mappings on Windows use the `NetNAT` gateway address rather than
    # `localhost`. There is no loopback for port mappings on Windows, so you
    # cannot access a container's mapped port from the host itself.

    # This parameter maps to `PortBindings` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--publish` option
    # to [docker run](https://docs.docker.com/engine/reference/run/). If the
    # network mode of a task definition is set to `none`, then you can't specify
    # port mappings. If the network mode of a task definition is set to `host`,
    # then host ports must either be undefined or they must match the container
    # port in the port mapping.

    # After a task reaches the `RUNNING` status, manual and automatic host and
    # container port assignments are visible in the **Network Bindings** section
    # of a container description for a selected task in the Amazon ECS console.
    # The assignments are also visible in the `networkBindings` section
    # DescribeTasks responses.
    port_mappings: typing.List["PortMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the `essential` parameter of a container is marked as `true`, and that
    # container fails or stops for any reason, all other containers that are part
    # of the task are stopped. If the `essential` parameter of a container is
    # marked as `false`, then its failure does not affect the rest of the
    # containers in a task. If this parameter is omitted, a container is assumed
    # to be essential.

    # All tasks must have at least one essential container. If you have an
    # application that is composed of multiple containers, you should group
    # containers that are used for a common purpose into components, and separate
    # the different components into multiple task definitions. For more
    # information, see [Application
    # Architecture](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    essential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Early versions of the Amazon ECS container agent do not properly handle
    # `entryPoint` parameters. If you have problems using `entryPoint`, update
    # your container agent or enter your commands and arguments as `command`
    # array items instead.

    # The entry point that is passed to the container. This parameter maps to
    # `Entrypoint` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--entrypoint`
    # option to [docker run](https://docs.docker.com/engine/reference/run/). For
    # more information, see
    # <https://docs.docker.com/engine/reference/builder/#entrypoint>.
    entry_point: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The command that is passed to the container. This parameter maps to `Cmd`
    # in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `COMMAND` parameter
    # to [docker run](https://docs.docker.com/engine/reference/run/). For more
    # information, see <https://docs.docker.com/engine/reference/builder/#cmd>.
    command: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The environment variables to pass to a container. This parameter maps to
    # `Env` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--env` option to
    # [docker run](https://docs.docker.com/engine/reference/run/).

    # We do not recommend using plaintext environment variables for sensitive
    # information, such as credential data.
    environment: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The mount points for data volumes in your container.

    # This parameter maps to `Volumes` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--volume` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # Windows containers can mount whole directories on the same drive as
    # `$env:ProgramData`. Windows containers cannot mount directories on a
    # different drive, and mount point cannot be across drives.
    mount_points: typing.List["MountPoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Data volumes to mount from another container. This parameter maps to
    # `VolumesFrom` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--volumes-from`
    # option to [docker run](https://docs.docker.com/engine/reference/run/).
    volumes_from: typing.List["VolumeFrom"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Linux-specific modifications that are applied to the container, such as
    # Linux KernelCapabilities.

    # This parameter is not supported for Windows containers.
    linux_parameters: "LinuxParameters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The hostname to use for your container. This parameter maps to `Hostname`
    # in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--hostname` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # The `hostname` parameter is not supported if using the `awsvpc`
    # networkMode.
    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name to use inside the container. This parameter maps to `User` in
    # the [Create a container](https://docs.docker.com/engine/api/v1.35/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--user` option to
    # [docker run](https://docs.docker.com/engine/reference/run/).

    # This parameter is not supported for Windows containers.
    user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The working directory in which to run commands inside the container. This
    # parameter maps to `WorkingDir` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--workdir` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).
    working_directory: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When this parameter is true, networking is disabled within the container.
    # This parameter maps to `NetworkDisabled` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/).

    # This parameter is not supported for Windows containers.
    disable_networking: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When this parameter is true, the container is given elevated privileges on
    # the host container instance (similar to the `root` user). This parameter
    # maps to `Privileged` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--privileged`
    # option to [docker run](https://docs.docker.com/engine/reference/run/).

    # This parameter is not supported for Windows containers or tasks using the
    # Fargate launch type.
    privileged: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When this parameter is true, the container is given read-only access to its
    # root file system. This parameter maps to `ReadonlyRootfs` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--read-only`
    # option to `docker run`.

    # This parameter is not supported for Windows containers.
    readonly_root_filesystem: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of DNS servers that are presented to the container. This parameter
    # maps to `Dns` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--dns` option to
    # [docker run](https://docs.docker.com/engine/reference/run/).

    # This parameter is not supported for Windows containers.
    dns_servers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of DNS search domains that are presented to the container. This
    # parameter maps to `DnsSearch` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--dns-search`
    # option to [docker run](https://docs.docker.com/engine/reference/run/).

    # This parameter is not supported for Windows containers.
    dns_search_domains: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of hostnames and IP address mappings to append to the `/etc/hosts`
    # file on the container. If using the Fargate launch type, this may be used
    # to list non-Fargate hosts to which the container can talk. This parameter
    # maps to `ExtraHosts` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--add-host` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # This parameter is not supported for Windows containers.
    extra_hosts: typing.List["HostEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of strings to provide custom labels for SELinux and AppArmor multi-
    # level security systems. This field is not valid for containers in tasks
    # using the Fargate launch type.

    # This parameter maps to `SecurityOpt` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--security-opt`
    # option to [docker run](https://docs.docker.com/engine/reference/run/).

    # The Amazon ECS container agent running on a container instance must
    # register with the `ECS_SELINUX_CAPABLE=true` or `ECS_APPARMOR_CAPABLE=true`
    # environment variables before containers placed on that instance can use
    # these security options. For more information, see [Amazon ECS Container
    # Agent
    # Configuration](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-
    # agent-config.html) in the _Amazon Elastic Container Service Developer
    # Guide_.

    # This parameter is not supported for Windows containers.
    docker_security_options: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A key/value map of labels to add to the container. This parameter maps to
    # `Labels` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--label` option to
    # [docker run](https://docs.docker.com/engine/reference/run/). This parameter
    # requires version 1.18 of the Docker Remote API or greater on your container
    # instance. To check the Docker Remote API version on your container
    # instance, log in to your container instance and run the following command:
    # `sudo docker version | grep "Server API version"`
    docker_labels: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `ulimits` to set in the container. This parameter maps to
    # `Ulimits` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--ulimit` option
    # to [docker run](https://docs.docker.com/engine/reference/run/). Valid
    # naming values are displayed in the Ulimit data type. This parameter
    # requires version 1.18 of the Docker Remote API or greater on your container
    # instance. To check the Docker Remote API version on your container
    # instance, log in to your container instance and run the following command:
    # `sudo docker version | grep "Server API version"`

    # This parameter is not supported for Windows containers.
    ulimits: typing.List["Ulimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log configuration specification for the container.

    # If using the Fargate launch type, the only supported value is `awslogs`.

    # This parameter maps to `LogConfig` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--log-driver`
    # option to [docker run](https://docs.docker.com/engine/reference/run/). By
    # default, containers use the same logging driver that the Docker daemon
    # uses; however the container may use a different logging driver than the
    # Docker daemon by specifying a log driver with this parameter in the
    # container definition. To use a different logging driver for a container,
    # the log system must be configured properly on the container instance (or on
    # a different log server for remote logging options). For more information on
    # the options for different supported log drivers, see [Configure logging
    # drivers](https://docs.docker.com/engine/admin/logging/overview/) in the
    # Docker documentation.

    # Amazon ECS currently supports a subset of the logging drivers available to
    # the Docker daemon (shown in the LogConfiguration data type). Additional log
    # drivers may be available in future releases of the Amazon ECS container
    # agent.

    # This parameter requires version 1.18 of the Docker Remote API or greater on
    # your container instance. To check the Docker Remote API version on your
    # container instance, log in to your container instance and run the following
    # command: `sudo docker version | grep "Server API version"`

    # The Amazon ECS container agent running on a container instance must
    # register the logging drivers available on that instance with the
    # `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers
    # placed on that instance can use these log configuration options. For more
    # information, see [Amazon ECS Container Agent
    # Configuration](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-
    # agent-config.html) in the _Amazon Elastic Container Service Developer
    # Guide_.
    log_configuration: "LogConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The health check command and associated configuration parameters for the
    # container. This parameter maps to `HealthCheck` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `HEALTHCHECK`
    # parameter of [docker run](https://docs.docker.com/engine/reference/run/).
    health_check: "HealthCheck" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContainerInstance(ShapeBase):
    """
    An EC2 instance that is running the Amazon ECS agent and has been registered
    with a cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_instance_arn",
                "containerInstanceArn",
                TypeInfo(str),
            ),
            (
                "ec2_instance_id",
                "ec2InstanceId",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(int),
            ),
            (
                "version_info",
                "versionInfo",
                TypeInfo(VersionInfo),
            ),
            (
                "remaining_resources",
                "remainingResources",
                TypeInfo(typing.List[Resource]),
            ),
            (
                "registered_resources",
                "registeredResources",
                TypeInfo(typing.List[Resource]),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "agent_connected",
                "agentConnected",
                TypeInfo(bool),
            ),
            (
                "running_tasks_count",
                "runningTasksCount",
                TypeInfo(int),
            ),
            (
                "pending_tasks_count",
                "pendingTasksCount",
                TypeInfo(int),
            ),
            (
                "agent_update_status",
                "agentUpdateStatus",
                TypeInfo(typing.Union[str, AgentUpdateStatus]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "registered_at",
                "registeredAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "attachments",
                "attachments",
                TypeInfo(typing.List[Attachment]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the container instance. The ARN contains
    # the `arn:aws:ecs` namespace, followed by the Region of the container
    # instance, the AWS account ID of the container instance owner, the
    # `container-instance` namespace, and then the container instance ID. For
    # example, `arn:aws:ecs: _region_ : _aws_account_id_ :container-instance/
    # _container_instance_ID_ `.
    container_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 instance ID of the container instance.
    ec2_instance_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version counter for the container instance. Every time a container
    # instance experiences a change that triggers a CloudWatch event, the version
    # counter is incremented. If you are replicating your Amazon ECS container
    # instance state with CloudWatch Events, you can compare the version of a
    # container instance reported by the Amazon ECS APIs with the version
    # reported in CloudWatch Events for the container instance (inside the
    # `detail` object) to verify that the version in your event stream is
    # current.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version information for the Amazon ECS container agent and Docker
    # daemon running on the container instance.
    version_info: "VersionInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For CPU and memory resource types, this parameter describes the remaining
    # CPU and memory that has not already been allocated to tasks and is
    # therefore available for new tasks. For port resource types, this parameter
    # describes the ports that were reserved by the Amazon ECS container agent
    # (at instance registration time) and any task containers that have reserved
    # port mappings on the host (with the `host` or `bridge` network mode). Any
    # port that is not specified here is available for new tasks.
    remaining_resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For CPU and memory resource types, this parameter describes the amount of
    # each resource that was available on the container instance when the
    # container agent registered it with Amazon ECS; this value represents the
    # total amount of CPU and memory that can be allocated on this container
    # instance to tasks. For port resource types, this parameter describes the
    # ports that were reserved by the Amazon ECS container agent when it
    # registered the container instance with Amazon ECS.
    registered_resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the container instance. The valid values are `ACTIVE`,
    # `INACTIVE`, or `DRAINING`. `ACTIVE` indicates that the container instance
    # can accept tasks. `DRAINING` indicates that new tasks are not placed on the
    # container instance and any service tasks running on the container instance
    # are removed if possible. For more information, see [Container Instance
    # Draining](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-
    # instance-draining.html) in the _Amazon Elastic Container Service Developer
    # Guide_.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter returns `true` if the agent is connected to Amazon ECS.
    # Registered instances with an agent that may be unhealthy or stopped return
    # `false`. Only instances connected to an agent can accept placement
    # requests.
    agent_connected: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks on the container instance that are in the `RUNNING`
    # status.
    running_tasks_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks on the container instance that are in the `PENDING`
    # status.
    pending_tasks_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the most recent agent update. If an update has never been
    # requested, this value is `NULL`.
    agent_update_status: typing.Union[str, "AgentUpdateStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The attributes set for the container instance, either by the Amazon ECS
    # container agent at instance registration or manually with the PutAttributes
    # operation.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the container instance was registered.
    registered_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The elastic network interfaces associated with the container instance.
    attachments: typing.List["Attachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ContainerInstanceStatus(str):
    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"


@dataclasses.dataclass
class ContainerOverride(ShapeBase):
    """
    The overrides that should be sent to a container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "command",
                "command",
                TypeInfo(typing.List[str]),
            ),
            (
                "environment",
                "environment",
                TypeInfo(typing.List[KeyValuePair]),
            ),
            (
                "cpu",
                "cpu",
                TypeInfo(int),
            ),
            (
                "memory",
                "memory",
                TypeInfo(int),
            ),
            (
                "memory_reservation",
                "memoryReservation",
                TypeInfo(int),
            ),
        ]

    # The name of the container that receives the override. This parameter is
    # required if any override is specified.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The command to send to the container that overrides the default command
    # from the Docker image or the task definition. You must also specify a
    # container name.
    command: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The environment variables to send to the container. You can add new
    # environment variables, which are added to the container at launch, or you
    # can override the existing environment variables from the Docker image or
    # the task definition. You must also specify a container name.
    environment: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of `cpu` units reserved for the container, instead of the
    # default value from the task definition. You must also specify a container
    # name.
    cpu: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hard limit (in MiB) of memory to present to the container, instead of
    # the default value from the task definition. If your container attempts to
    # exceed the memory specified here, the container is killed. You must also
    # specify a container name.
    memory: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The soft limit (in MiB) of memory to reserve for the container, instead of
    # the default value from the task definition. You must also specify a
    # container name.
    memory_reservation: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContainerStateChange(ShapeBase):
    """
    An object representing a change in state for a container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_name",
                "containerName",
                TypeInfo(str),
            ),
            (
                "exit_code",
                "exitCode",
                TypeInfo(int),
            ),
            (
                "network_bindings",
                "networkBindings",
                TypeInfo(typing.List[NetworkBinding]),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
        ]

    # The name of the container.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The exit code for the container, if the state change is a result of the
    # container exiting.
    exit_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any network bindings associated with the container.
    network_bindings: typing.List["NetworkBinding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the state change.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the container.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster_name",
                "clusterName",
                TypeInfo(str),
            ),
        ]

    # The name of your cluster. If you do not specify a name for your cluster,
    # you create a cluster named `default`. Up to 255 letters (uppercase and
    # lowercase), numbers, hyphens, and underscores are allowed.
    cluster_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateClusterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(Cluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of your new cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_name",
                "serviceName",
                TypeInfo(str),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "load_balancers",
                "loadBalancers",
                TypeInfo(typing.List[LoadBalancer]),
            ),
            (
                "service_registries",
                "serviceRegistries",
                TypeInfo(typing.List[ServiceRegistry]),
            ),
            (
                "desired_count",
                "desiredCount",
                TypeInfo(int),
            ),
            (
                "client_token",
                "clientToken",
                TypeInfo(str),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "platform_version",
                "platformVersion",
                TypeInfo(str),
            ),
            (
                "role",
                "role",
                TypeInfo(str),
            ),
            (
                "deployment_configuration",
                "deploymentConfiguration",
                TypeInfo(DeploymentConfiguration),
            ),
            (
                "placement_constraints",
                "placementConstraints",
                TypeInfo(typing.List[PlacementConstraint]),
            ),
            (
                "placement_strategy",
                "placementStrategy",
                TypeInfo(typing.List[PlacementStrategy]),
            ),
            (
                "network_configuration",
                "networkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
            (
                "health_check_grace_period_seconds",
                "healthCheckGracePeriodSeconds",
                TypeInfo(int),
            ),
            (
                "scheduling_strategy",
                "schedulingStrategy",
                TypeInfo(typing.Union[str, SchedulingStrategy]),
            ),
        ]

    # The name of your service. Up to 255 letters (uppercase and lowercase),
    # numbers, hyphens, and underscores are allowed. Service names must be unique
    # within a cluster, but you can have similarly named services in multiple
    # clusters within a Region or across multiple Regions.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `family` and `revision` (`family:revision`) or full ARN of the task
    # definition to run in your service. If a `revision` is not specified, the
    # latest `ACTIVE` revision is used.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster on which
    # to run your service. If you do not specify a cluster, the default cluster
    # is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A load balancer object representing the load balancer to use with your
    # service. Currently, you are limited to one load balancer or target group
    # per service. After you create a service, the load balancer name or target
    # group ARN, container name, and container port specified in the service
    # definition are immutable.

    # For Classic Load Balancers, this object must contain the load balancer
    # name, the container name (as it appears in a container definition), and the
    # container port to access from the load balancer. When a task from this
    # service is placed on a container instance, the container instance is
    # registered with the load balancer specified here.

    # For Application Load Balancers and Network Load Balancers, this object must
    # contain the load balancer target group ARN, the container name (as it
    # appears in a container definition), and the container port to access from
    # the load balancer. When a task from this service is placed on a container
    # instance, the container instance and port combination is registered as a
    # target in the target group specified here.

    # Services with tasks that use the `awsvpc` network mode (for example, those
    # with the Fargate launch type) only support Application Load Balancers and
    # Network Load Balancers; Classic Load Balancers are not supported. Also,
    # when you create any target groups for these services, you must choose `ip`
    # as the target type, not `instance`, because tasks that use the `awsvpc`
    # network mode are associated with an elastic network interface, not an
    # Amazon EC2 instance.
    load_balancers: typing.List["LoadBalancer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The details of the service discovery registries to assign to this service.
    # For more information, see [Service
    # Discovery](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-
    # discovery.html).

    # Service discovery is supported for Fargate tasks if using platform version
    # v1.1.0 or later. For more information, see [AWS Fargate Platform
    # Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
    service_registries: typing.List["ServiceRegistry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of instantiations of the specified task definition to place and
    # keep running on your cluster.
    desired_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique, case-sensitive identifier that you provide to ensure the
    # idempotency of the request. Up to 32 ASCII characters are allowed.
    client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The launch type on which to run your service.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform version on which to run your service. If one is not specified,
    # the latest version is used by default.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or full Amazon Resource Name (ARN) of the IAM role that allows
    # Amazon ECS to make calls to your load balancer on your behalf. This
    # parameter is only permitted if you are using a load balancer with your
    # service and your task definition does not use the `awsvpc` network mode. If
    # you specify the `role` parameter, you must also specify a load balancer
    # object with the `loadBalancers` parameter.

    # If your account has already created the Amazon ECS service-linked role,
    # that role is used by default for your service unless you specify a role
    # here. The service-linked role is required if your task definition uses the
    # `awsvpc` network mode, in which case you should not specify a role here.
    # For more information, see [Using Service-Linked Roles for Amazon
    # ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-
    # service-linked-roles.html) in the _Amazon Elastic Container Service
    # Developer Guide_.

    # If your specified role has a path other than `/`, then you must either
    # specify the full role ARN (this is recommended) or prefix the role name
    # with the path. For example, if a role with the name `bar` has a path of
    # `/foo/` then you would specify `/foo/bar` as the role name. For more
    # information, see [Friendly Names and
    # Paths](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-
    # friendly-names) in the _IAM User Guide_.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional deployment parameters that control how many tasks run during the
    # deployment and the ordering of stopping and starting tasks.
    deployment_configuration: "DeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of placement constraint objects to use for tasks in your service.
    # You can specify a maximum of 10 constraints per task (this limit includes
    # constraints in the task definition and those specified at run time).
    placement_constraints: typing.List["PlacementConstraint"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The placement strategy objects to use for tasks in your service. You can
    # specify a maximum of five strategy rules per service.
    placement_strategy: typing.List["PlacementStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The network configuration for the service. This parameter is required for
    # task definitions that use the `awsvpc` network mode to receive their own
    # Elastic Network Interface, and it is not supported for other network modes.
    # For more information, see [Task
    # Networking](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    # networking.html) in the _Amazon Elastic Container Service Developer Guide_.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The period of time, in seconds, that the Amazon ECS service scheduler
    # should ignore unhealthy Elastic Load Balancing target health checks after a
    # task has first started. This is only valid if your service is configured to
    # use a load balancer. If your service's tasks take a while to start and
    # respond to Elastic Load Balancing health checks, you can specify a health
    # check grace period of up to 7,200 seconds during which the ECS service
    # scheduler ignores health check status. This grace period can prevent the
    # ECS service scheduler from marking tasks as unhealthy and stopping them
    # before they have time to come up.
    health_check_grace_period_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scheduling strategy to use for the service. For more information, see
    # [Services](http://docs.aws.amazon.com/AmazonECS/latest/developerguideecs_services.html).

    # There are two service scheduler strategies available:

    #   * `REPLICA`-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.

    #   * `DAEMON`-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When using this strategy, there is no need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.

    # Fargate tasks do not support the `DAEMON` scheduling strategy.
    scheduling_strategy: typing.Union[str, "SchedulingStrategy"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class CreateServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service",
                "service",
                TypeInfo(Service),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of your service following the create call.
    service: "Service" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # The attributes to delete from your resource. You can specify up to 10
    # attributes per request. For custom attributes, specify the attribute name
    # and target ID, but do not specify the value. If you specify the target ID
    # using the short form, you must also specify the target type.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name or full Amazon Resource Name (ARN) of the cluster that
    # contains the resource to delete attributes. If you do not specify a
    # cluster, the default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of attribute objects that were successfully deleted from your
    # resource.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteClusterRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the cluster to delete.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteClusterResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(Cluster),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of the deleted cluster.
    cluster: "Cluster" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service",
                "service",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "force",
                "force",
                TypeInfo(bool),
            ),
        ]

    # The name of the service to delete.
    service: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the service to delete. If you do not specify a cluster, the default cluster
    # is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `true`, allows you to delete a service even if it has not been scaled
    # down to zero tasks. It is only necessary to use this if the service is
    # using the `REPLICA` scheduling strategy.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service",
                "service",
                TypeInfo(Service),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of the deleted service.
    service: "Service" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Deployment(ShapeBase):
    """
    The details of an Amazon ECS service deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
            (
                "desired_count",
                "desiredCount",
                TypeInfo(int),
            ),
            (
                "pending_count",
                "pendingCount",
                TypeInfo(int),
            ),
            (
                "running_count",
                "runningCount",
                TypeInfo(int),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_at",
                "updatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "platform_version",
                "platformVersion",
                TypeInfo(str),
            ),
            (
                "network_configuration",
                "networkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
        ]

    # The ID of the deployment.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the deployment. Valid values are `PRIMARY` (for the most
    # recent deployment), `ACTIVE` (for previous deployments that still have
    # tasks running, but are being replaced with the `PRIMARY` deployment), and
    # `INACTIVE` (for deployments that have been completely replaced).
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The most recent task definition that was specified for the service to use.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The most recent desired count of tasks that was specified for the service
    # to deploy or maintain.
    desired_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks in the deployment that are in the `PENDING` status.
    pending_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks in the deployment that are in the `RUNNING` status.
    running_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp for when the service was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the service was last updated.
    updated_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch type on which your service is running.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform version on which your service is running.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC subnet and security group configuration for tasks that receive
    # their own elastic network interface by using the `awsvpc` networking mode.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeploymentConfiguration(ShapeBase):
    """
    Optional deployment parameters that control how many tasks run during the
    deployment and the ordering of stopping and starting tasks.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "maximum_percent",
                "maximumPercent",
                TypeInfo(int),
            ),
            (
                "minimum_healthy_percent",
                "minimumHealthyPercent",
                TypeInfo(int),
            ),
        ]

    # The upper limit (as a percentage of the service's `desiredCount`) of the
    # number of tasks that are allowed in the `RUNNING` or `PENDING` state in a
    # service during a deployment. The maximum number of tasks during a
    # deployment is the `desiredCount` multiplied by `maximumPercent`/100,
    # rounded down to the nearest integer value.
    maximum_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The lower limit (as a percentage of the service's `desiredCount`) of the
    # number of running tasks that must remain in the `RUNNING` state in a
    # service during a deployment. The minimum number of healthy tasks during a
    # deployment is the `desiredCount` multiplied by `minimumHealthyPercent`/100,
    # rounded up to the nearest integer value.
    minimum_healthy_percent: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterContainerInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_instance",
                "containerInstance",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "force",
                "force",
                TypeInfo(bool),
            ),
        ]

    # The container instance ID or full ARN of the container instance to
    # deregister. The ARN contains the `arn:aws:ecs` namespace, followed by the
    # Region of the container instance, the AWS account ID of the container
    # instance owner, the `container-instance` namespace, and then the container
    # instance ID. For example, `arn:aws:ecs: _region_ : _aws_account_id_
    # :container-instance/ _container_instance_ID_ `.
    container_instance: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the container instance to deregister. If you do not specify a cluster, the
    # default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Forces the deregistration of the container instance. If you have tasks
    # running on the container instance when you deregister it with the `force`
    # option, these tasks remain running until you terminate the instance or the
    # tasks stop through some other means, but they are orphaned (no longer
    # monitored or accounted for by Amazon ECS). If an orphaned task on your
    # container instance is part of an Amazon ECS service, then the service
    # scheduler starts another copy of that task, on a different container
    # instance if possible.

    # Any containers in orphaned service tasks that are registered with a Classic
    # Load Balancer or an Application Load Balancer target group are
    # deregistered. They begin connection draining according to the settings on
    # the load balancer or target group.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterContainerInstanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_instance",
                "containerInstance",
                TypeInfo(ContainerInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The container instance that was deregistered.
    container_instance: "ContainerInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterTaskDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
        ]

    # The `family` and `revision` (`family:revision`) or full Amazon Resource
    # Name (ARN) of the task definition to deregister. You must specify a
    # `revision`.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterTaskDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(TaskDefinition),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of the deregistered task.
    task_definition: "TaskDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeClustersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "clusters",
                "clusters",
                TypeInfo(typing.List[str]),
            ),
            (
                "include",
                "include",
                TypeInfo(typing.List[typing.Union[str, ClusterField]]),
            ),
        ]

    # A list of up to 100 cluster names or full cluster Amazon Resource Name
    # (ARN) entries. If you do not specify a cluster, the default cluster is
    # assumed.
    clusters: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional information about your clusters to be separated by launch type,
    # including:

    #   * runningEC2TasksCount

    #   * runningFargateTasksCount

    #   * pendingEC2TasksCount

    #   * pendingFargateTasksCount

    #   * activeEC2ServiceCount

    #   * activeFargateServiceCount

    #   * drainingEC2ServiceCount

    #   * drainingFargateServiceCount
    include: typing.List[typing.Union[str, "ClusterField"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeClustersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "clusters",
                "clusters",
                TypeInfo(typing.List[Cluster]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of clusters.
    clusters: typing.List["Cluster"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeContainerInstancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_instances",
                "containerInstances",
                TypeInfo(typing.List[str]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # A list of up to 100 container instance IDs or full Amazon Resource Name
    # (ARN) entries.
    container_instances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the container instances to describe. If you do not specify a cluster, the
    # default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeContainerInstancesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_instances",
                "containerInstances",
                TypeInfo(typing.List[ContainerInstance]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of container instances.
    container_instances: typing.List["ContainerInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeServicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "services",
                "services",
                TypeInfo(typing.List[str]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # A list of services to describe. You may specify up to 10 services to
    # describe in a single operation.
    services: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN)the cluster that hosts the
    # service to describe. If you do not specify a cluster, the default cluster
    # is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeServicesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "services",
                "services",
                TypeInfo(typing.List[Service]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of services described.
    services: typing.List["Service"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTaskDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
        ]

    # The `family` for the latest `ACTIVE` revision, `family` and `revision`
    # (`family:revision`) for a specific revision in the family, or full Amazon
    # Resource Name (ARN) of the task definition to describe.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTaskDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(TaskDefinition),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full task definition description.
    task_definition: "TaskDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTasksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tasks",
                "tasks",
                TypeInfo(typing.List[str]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # A list of up to 100 task IDs or full ARN entries.
    tasks: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the task to describe. If you do not specify a cluster, the default cluster
    # is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTasksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tasks",
                "tasks",
                TypeInfo(typing.List[Task]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of tasks.
    tasks: typing.List["Task"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DesiredStatus(str):
    RUNNING = "RUNNING"
    PENDING = "PENDING"
    STOPPED = "STOPPED"


@dataclasses.dataclass
class Device(ShapeBase):
    """
    An object representing a container instance host device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_path",
                "hostPath",
                TypeInfo(str),
            ),
            (
                "container_path",
                "containerPath",
                TypeInfo(str),
            ),
            (
                "permissions",
                "permissions",
                TypeInfo(
                    typing.List[typing.Union[str, DeviceCgroupPermission]]
                ),
            ),
        ]

    # The path for the device on the host container instance.
    host_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path inside the container at which to expose the host device.
    container_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The explicit permissions to provide to the container for the device. By
    # default, the container has permissions for `read`, `write`, and `mknod` for
    # the device.
    permissions: typing.List[typing.Union[str, "DeviceCgroupPermission"]
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )


class DeviceCgroupPermission(str):
    read = "read"
    write = "write"
    mknod = "mknod"


@dataclasses.dataclass
class DiscoverPollEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_instance",
                "containerInstance",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # The container instance ID or full ARN of the container instance. The ARN
    # contains the `arn:aws:ecs` namespace, followed by the Region of the
    # container instance, the AWS account ID of the container instance owner, the
    # `container-instance` namespace, and then the container instance ID. For
    # example, `arn:aws:ecs: _region_ : _aws_account_id_ :container-instance/
    # _container_instance_ID_ `.
    container_instance: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that the
    # container instance belongs to.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DiscoverPollEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint",
                "endpoint",
                TypeInfo(str),
            ),
            (
                "telemetry_endpoint",
                "telemetryEndpoint",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint for the Amazon ECS agent to poll.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The telemetry endpoint for the Amazon ECS agent.
    telemetry_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DockerVolumeConfiguration(ShapeBase):
    """
    The configuration for the Docker volume. This parameter is specified when using
    Docker volumes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scope",
                "scope",
                TypeInfo(typing.Union[str, Scope]),
            ),
            (
                "autoprovision",
                "autoprovision",
                TypeInfo(bool),
            ),
            (
                "driver",
                "driver",
                TypeInfo(str),
            ),
            (
                "driver_opts",
                "driverOpts",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "labels",
                "labels",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The scope for the Docker volume which determines it's lifecycle. Docker
    # volumes that are scoped to a `task` are automatically provisioned when the
    # task starts and destroyed when the task stops. Docker volumes that are
    # scoped as `shared` persist after the task stops.
    scope: typing.Union[str, "Scope"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If this value is `true`, the Docker volume is created if it does not
    # already exist.

    # This field is only used if the `scope` is `shared`.
    autoprovision: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Docker volume driver to use. The driver value must match the driver
    # name provided by Docker because it is used for task placement. If the
    # driver was installed using the Docker plugin CLI, use `docker plugin ls` to
    # retrieve the driver name from your container instance. If the driver was
    # installed using another method, use Docker plugin discovery to retrieve the
    # driver name. For more information, see [Docker plugin
    # discovery](https://docs.docker.com/engine/extend/plugin_api/#plugin-
    # discovery). This parameter maps to `Driver` in the [Create a
    # volume](https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `xxdriver` option
    # to [ `docker volume create`
    # ](https://docs.docker.com/engine/reference/commandline/volume_create/).
    driver: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of Docker driver specific options passed through. This parameter maps
    # to `DriverOpts` in the [Create a
    # volume](https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `xxopt` option to [
    # `docker volume create`
    # ](https://docs.docker.com/engine/reference/commandline/volume_create/).
    driver_opts: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom metadata to add to your Docker volume. This parameter maps to
    # `Labels` in the [Create a
    # volume](https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `xxlabel` option to
    # [ `docker volume create`
    # ](https://docs.docker.com/engine/reference/commandline/volume_create/).
    labels: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Failure(ShapeBase):
    """
    A failed resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the failed resource.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason for the failure.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HealthCheck(ShapeBase):
    """
    An object representing a container health check. Health check parameters that
    are specified in a container definition override any Docker health checks that
    exist in the container image (such as those specified in a parent image or from
    the image's Dockerfile).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "command",
                "command",
                TypeInfo(typing.List[str]),
            ),
            (
                "interval",
                "interval",
                TypeInfo(int),
            ),
            (
                "timeout",
                "timeout",
                TypeInfo(int),
            ),
            (
                "retries",
                "retries",
                TypeInfo(int),
            ),
            (
                "start_period",
                "startPeriod",
                TypeInfo(int),
            ),
        ]

    # A string array representing the command that the container runs to
    # determine if it is healthy. The string array must start with `CMD` to
    # execute the command arguments directly, or `CMD-SHELL` to run the command
    # with the container's default shell. For example:

    # `[ "CMD-SHELL", "curl -f http://localhost/ || exit 1" ]`

    # An exit code of 0 indicates success, and non-zero exit code indicates
    # failure. For more information, see `HealthCheck` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/).
    command: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time period in seconds between each health check execution. You may
    # specify between 5 and 300 seconds. The default value is 30 seconds.
    interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time period in seconds to wait for a health check to succeed before it
    # is considered a failure. You may specify between 2 and 60 seconds. The
    # default value is 5.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of times to retry a failed health check before the container is
    # considered unhealthy. You may specify between 1 and 10 retries. The default
    # value is 3.
    retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The optional grace period within which to provide containers time to
    # bootstrap before failed health checks count towards the maximum number of
    # retries. You may specify between 0 and 300 seconds. The `startPeriod` is
    # disabled by default.

    # If a health check succeeds within the `startPeriod`, then the container is
    # considered healthy and any subsequent failures count toward the maximum
    # number of retries.
    start_period: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class HealthStatus(str):
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class HostEntry(ShapeBase):
    """
    Hostnames and IP address entries that are added to the `/etc/hosts` file of a
    container via the `extraHosts` parameter of its ContainerDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hostname",
                "hostname",
                TypeInfo(str),
            ),
            (
                "ip_address",
                "ipAddress",
                TypeInfo(str),
            ),
        ]

    # The hostname to use in the `/etc/hosts` entry.
    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address to use in the `/etc/hosts` entry.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HostVolumeProperties(ShapeBase):
    """
    Details on a container instance bind mount host volume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_path",
                "sourcePath",
                TypeInfo(str),
            ),
        ]

    # When the `host` parameter is used, specify a `sourcePath` to declare the
    # path on the host container instance that is presented to the container. If
    # this parameter is empty, then the Docker daemon has assigned a host path
    # for you. If the `host` parameter contains a `sourcePath` file location,
    # then the data volume persists at the specified location on the host
    # container instance until you delete it manually. If the `sourcePath` value
    # does not exist on the host container instance, the Docker daemon creates
    # it. If the location does exist, the contents of the source path folder are
    # exported.

    # If you are using the Fargate launch type, the `sourcePath` parameter is not
    # supported.
    source_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KernelCapabilities(ShapeBase):
    """
    The Linux capabilities for the container that are added to or dropped from the
    default configuration provided by Docker. For more information on the default
    capabilities and the non-default available capabilities, see [Runtime privilege
    and Linux capabilities](https://docs.docker.com/engine/reference/run/#runtime-
    privilege-and-linux-capabilities) in the _Docker run reference_. For more
    detailed information on these Linux capabilities, see the
    [capabilities(7)](http://man7.org/linux/man-pages/man7/capabilities.7.html)
    Linux manual page.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "add",
                "add",
                TypeInfo(typing.List[str]),
            ),
            (
                "drop",
                "drop",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Linux capabilities for the container that have been added to the
    # default configuration provided by Docker. This parameter maps to `CapAdd`
    # in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--cap-add` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # If you are using tasks that use the Fargate launch type, the `add`
    # parameter is not supported.

    # Valid values: `"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" |
    # "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" |
    # "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" |
    # "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" |
    # "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" |
    # "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" |
    # "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" |
    # "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"`
    add: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Linux capabilities for the container that have been removed from the
    # default configuration provided by Docker. This parameter maps to `CapDrop`
    # in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--cap-drop` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # Valid values: `"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" |
    # "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" |
    # "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" |
    # "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" |
    # "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" |
    # "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" |
    # "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" |
    # "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"`
    drop: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyValuePair(ShapeBase):
    """
    A key and value pair object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The name of the key value pair. For environment variables, this is the name
    # of the environment variable.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the key value pair. For environment variables, this is the
    # value of the environment variable.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LaunchType(str):
    EC2 = "EC2"
    FARGATE = "FARGATE"


@dataclasses.dataclass
class LinuxParameters(ShapeBase):
    """
    Linux-specific options that are applied to the container, such as Linux
    KernelCapabilities.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capabilities",
                "capabilities",
                TypeInfo(KernelCapabilities),
            ),
            (
                "devices",
                "devices",
                TypeInfo(typing.List[Device]),
            ),
            (
                "init_process_enabled",
                "initProcessEnabled",
                TypeInfo(bool),
            ),
            (
                "shared_memory_size",
                "sharedMemorySize",
                TypeInfo(int),
            ),
            (
                "tmpfs",
                "tmpfs",
                TypeInfo(typing.List[Tmpfs]),
            ),
        ]

    # The Linux capabilities for the container that are added to or dropped from
    # the default configuration provided by Docker.

    # If you are using tasks that use the Fargate launch type, `capabilities` is
    # supported but the `add` parameter is not supported.
    capabilities: "KernelCapabilities" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any host devices to expose to the container. This parameter maps to
    # `Devices` in the [Create a
    # container](https://docs.docker.com/engine/api/v1.35/#create-a-container)
    # section of the [Docker Remote
    # API](https://docs.docker.com/engine/api/v1.35/) and the `--device` option
    # to [docker run](https://docs.docker.com/engine/reference/run/).

    # If you are using tasks that use the Fargate launch type, the `devices`
    # parameter is not supported.
    devices: typing.List["Device"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Run an `init` process inside the container that forwards signals and reaps
    # processes. This parameter maps to the `--init` option to [docker
    # run](https://docs.docker.com/engine/reference/run/). This parameter
    # requires version 1.25 of the Docker Remote API or greater on your container
    # instance. To check the Docker Remote API version on your container
    # instance, log in to your container instance and run the following command:
    # `sudo docker version | grep "Server API version"`
    init_process_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the size (in MiB) of the `/dev/shm` volume. This parameter
    # maps to the `--shm-size` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).

    # If you are using tasks that use the Fargate launch type, the
    # `sharedMemorySize` parameter is not supported.
    shared_memory_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The container path, mount options, and size (in MiB) of the tmpfs mount.
    # This parameter maps to the `--tmpfs` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).

    # If you are using tasks that use the Fargate launch type, the `tmpfs`
    # parameter is not supported.
    tmpfs: typing.List["Tmpfs"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_type",
                "targetType",
                TypeInfo(typing.Union[str, TargetType]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "attribute_name",
                "attributeName",
                TypeInfo(str),
            ),
            (
                "attribute_value",
                "attributeValue",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The type of the target with which to list attributes.
    target_type: typing.Union[str, "TargetType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name or full Amazon Resource Name (ARN) of the cluster to list
    # attributes. If you do not specify a cluster, the default cluster is
    # assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute with which to filter the results.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute with which to filter results. You must also
    # specify an attribute name to use this parameter.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListAttributes`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of cluster results returned by `ListAttributes` in
    # paginated output. When this parameter is used, `ListAttributes` only
    # returns `maxResults` results in a single page along with a `nextToken`
    # response element. The remaining results of the initial request can be seen
    # by sending another `ListAttributes` request with the returned `nextToken`
    # value. This value can be between 1 and 100. If this parameter is not used,
    # then `ListAttributes` returns up to 100 results and a `nextToken` value if
    # applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of attribute objects that meet the criteria of the request.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListAttributes` request. When
    # the results of a `ListAttributes` request exceed `maxResults`, this value
    # can be used to retrieve the next page of results. This value is `null` when
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The `nextToken` value returned from a previous paginated `ListClusters`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of cluster results returned by `ListClusters` in
    # paginated output. When this parameter is used, `ListClusters` only returns
    # `maxResults` results in a single page along with a `nextToken` response
    # element. The remaining results of the initial request can be seen by
    # sending another `ListClusters` request with the returned `nextToken` value.
    # This value can be between 1 and 100. If this parameter is not used, then
    # `ListClusters` returns up to 100 results and a `nextToken` value if
    # applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListClustersResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cluster_arns",
                "clusterArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of full Amazon Resource Name (ARN) entries for each cluster
    # associated with your account.
    cluster_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListClusters` request. When
    # the results of a `ListClusters` request exceed `maxResults`, this value can
    # be used to retrieve the next page of results. This value is `null` when
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListClustersResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListContainerInstancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "filter",
                "filter",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ContainerInstanceStatus]),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the container instances to list. If you do not specify a cluster, the
    # default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can filter the results of a `ListContainerInstances` operation with
    # cluster query language statements. For more information, see [Cluster Query
    # Language](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-
    # query-language.html) in the _Amazon Elastic Container Service Developer
    # Guide_.
    filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated
    # `ListContainerInstances` request where `maxResults` was used and the
    # results exceeded the value of that parameter. Pagination continues from the
    # end of the previous results that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of container instance results returned by
    # `ListContainerInstances` in paginated output. When this parameter is used,
    # `ListContainerInstances` only returns `maxResults` results in a single page
    # along with a `nextToken` response element. The remaining results of the
    # initial request can be seen by sending another `ListContainerInstances`
    # request with the returned `nextToken` value. This value can be between 1
    # and 100. If this parameter is not used, then `ListContainerInstances`
    # returns up to 100 results and a `nextToken` value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filters the container instances by status. For example, if you specify the
    # `DRAINING` status, the results include only container instances that have
    # been set to `DRAINING` using UpdateContainerInstancesState. If you do not
    # specify this parameter, the default is to include container instances set
    # to `ACTIVE` and `DRAINING`.
    status: typing.Union[str, "ContainerInstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListContainerInstancesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_instance_arns",
                "containerInstanceArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of container instances with full ARN entries for each container
    # instance associated with the specified cluster.
    container_instance_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListContainerInstances`
    # request. When the results of a `ListContainerInstances` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListContainerInstancesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListServicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "scheduling_strategy",
                "schedulingStrategy",
                TypeInfo(typing.Union[str, SchedulingStrategy]),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the services to list. If you do not specify a cluster, the default cluster
    # is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListServices`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of service results returned by `ListServices` in
    # paginated output. When this parameter is used, `ListServices` only returns
    # `maxResults` results in a single page along with a `nextToken` response
    # element. The remaining results of the initial request can be seen by
    # sending another `ListServices` request with the returned `nextToken` value.
    # This value can be between 1 and 10. If this parameter is not used, then
    # `ListServices` returns up to 10 results and a `nextToken` value if
    # applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The launch type for the services to list.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scheduling strategy for services to list.
    scheduling_strategy: typing.Union[str, "SchedulingStrategy"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class ListServicesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service_arns",
                "serviceArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of full ARN entries for each service associated with the specified
    # cluster.
    service_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListServices` request. When
    # the results of a `ListServices` request exceed `maxResults`, this value can
    # be used to retrieve the next page of results. This value is `null` when
    # there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListServicesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTaskDefinitionFamiliesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family_prefix",
                "familyPrefix",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, TaskDefinitionFamilyStatus]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The `familyPrefix` is a string that is used to filter the results of
    # `ListTaskDefinitionFamilies`. If you specify a `familyPrefix`, only task
    # definition family names that begin with the `familyPrefix` string are
    # returned.
    family_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task definition family status with which to filter the
    # `ListTaskDefinitionFamilies` results. By default, both `ACTIVE` and
    # `INACTIVE` task definition families are listed. If this parameter is set to
    # `ACTIVE`, only task definition families that have an `ACTIVE` task
    # definition revision are returned. If this parameter is set to `INACTIVE`,
    # only task definition families that do not have any `ACTIVE` task definition
    # revisions are returned. If you paginate the resulting output, be sure to
    # keep the `status` value constant in each subsequent request.
    status: typing.Union[str, "TaskDefinitionFamilyStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value returned from a previous paginated
    # `ListTaskDefinitionFamilies` request where `maxResults` was used and the
    # results exceeded the value of that parameter. Pagination continues from the
    # end of the previous results that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of task definition family results returned by
    # `ListTaskDefinitionFamilies` in paginated output. When this parameter is
    # used, `ListTaskDefinitions` only returns `maxResults` results in a single
    # page along with a `nextToken` response element. The remaining results of
    # the initial request can be seen by sending another
    # `ListTaskDefinitionFamilies` request with the returned `nextToken` value.
    # This value can be between 1 and 100. If this parameter is not used, then
    # `ListTaskDefinitionFamilies` returns up to 100 results and a `nextToken`
    # value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTaskDefinitionFamiliesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "families",
                "families",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of task definition family names that match the
    # `ListTaskDefinitionFamilies` request.
    families: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value to include in a future `ListTaskDefinitionFamilies`
    # request. When the results of a `ListTaskDefinitionFamilies` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTaskDefinitionFamiliesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTaskDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family_prefix",
                "familyPrefix",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, TaskDefinitionStatus]),
            ),
            (
                "sort",
                "sort",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The full family name with which to filter the `ListTaskDefinitions`
    # results. Specifying a `familyPrefix` limits the listed task definitions to
    # task definition revisions that belong to that family.
    family_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task definition status with which to filter the `ListTaskDefinitions`
    # results. By default, only `ACTIVE` task definitions are listed. By setting
    # this parameter to `INACTIVE`, you can view task definitions that are
    # `INACTIVE` as long as an active task or service still references them. If
    # you paginate the resulting output, be sure to keep the `status` value
    # constant in each subsequent request.
    status: typing.Union[str, "TaskDefinitionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order in which to sort the results. Valid values are `ASC` and `DESC`.
    # By default (`ASC`), task definitions are listed lexicographically by family
    # name and in ascending numerical order by revision so that the newest task
    # definitions in a family are listed last. Setting this parameter to `DESC`
    # reverses the sort order on family name and revision so that the newest task
    # definitions in a family are listed first.
    sort: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value returned from a previous paginated
    # `ListTaskDefinitions` request where `maxResults` was used and the results
    # exceeded the value of that parameter. Pagination continues from the end of
    # the previous results that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of task definition results returned by
    # `ListTaskDefinitions` in paginated output. When this parameter is used,
    # `ListTaskDefinitions` only returns `maxResults` results in a single page
    # along with a `nextToken` response element. The remaining results of the
    # initial request can be seen by sending another `ListTaskDefinitions`
    # request with the returned `nextToken` value. This value can be between 1
    # and 100. If this parameter is not used, then `ListTaskDefinitions` returns
    # up to 100 results and a `nextToken` value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTaskDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_definition_arns",
                "taskDefinitionArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of task definition Amazon Resource Name (ARN) entries for the
    # `ListTaskDefinitions` request.
    task_definition_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListTaskDefinitions` request.
    # When the results of a `ListTaskDefinitions` request exceed `maxResults`,
    # this value can be used to retrieve the next page of results. This value is
    # `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTaskDefinitionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTasksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "container_instance",
                "containerInstance",
                TypeInfo(str),
            ),
            (
                "family",
                "family",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "started_by",
                "startedBy",
                TypeInfo(str),
            ),
            (
                "service_name",
                "serviceName",
                TypeInfo(str),
            ),
            (
                "desired_status",
                "desiredStatus",
                TypeInfo(typing.Union[str, DesiredStatus]),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the tasks to list. If you do not specify a cluster, the default cluster is
    # assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The container instance ID or full ARN of the container instance with which
    # to filter the `ListTasks` results. Specifying a `containerInstance` limits
    # the results to tasks that belong to that container instance.
    container_instance: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the family with which to filter the `ListTasks` results.
    # Specifying a `family` limits the results to tasks that belong to that
    # family.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListTasks`
    # request where `maxResults` was used and the results exceeded the value of
    # that parameter. Pagination continues from the end of the previous results
    # that returned the `nextToken` value.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of task results returned by `ListTasks` in paginated
    # output. When this parameter is used, `ListTasks` only returns `maxResults`
    # results in a single page along with a `nextToken` response element. The
    # remaining results of the initial request can be seen by sending another
    # `ListTasks` request with the returned `nextToken` value. This value can be
    # between 1 and 100. If this parameter is not used, then `ListTasks` returns
    # up to 100 results and a `nextToken` value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `startedBy` value with which to filter the task results. Specifying a
    # `startedBy` value limits the results to tasks that were started with that
    # value.
    started_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the service with which to filter the `ListTasks` results.
    # Specifying a `serviceName` limits the results to tasks that belong to that
    # service.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task desired status with which to filter the `ListTasks` results.
    # Specifying a `desiredStatus` of `STOPPED` limits the results to tasks that
    # Amazon ECS has set the desired status to `STOPPED`, which can be useful for
    # debugging tasks that are not starting properly or have died or finished.
    # The default status filter is `RUNNING`, which shows tasks that Amazon ECS
    # has set the desired status to `RUNNING`.

    # Although you can filter results based on a desired status of `PENDING`,
    # this does not return any results because Amazon ECS never sets the desired
    # status of a task to that value (only a task's `lastStatus` may have a value
    # of `PENDING`).
    desired_status: typing.Union[str, "DesiredStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch type for services to list.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTasksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_arns",
                "taskArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of task ARN entries for the `ListTasks` request.
    task_arns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value to include in a future `ListTasks` request. When the
    # results of a `ListTasks` request exceed `maxResults`, this value can be
    # used to retrieve the next page of results. This value is `null` when there
    # are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListTasksResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class LoadBalancer(ShapeBase):
    """
    Details on a load balancer that is used with a service.

    Services with tasks that use the `awsvpc` network mode (for example, those with
    the Fargate launch type) only support Application Load Balancers and Network
    Load Balancers; Classic Load Balancers are not supported. Also, when you create
    any target groups for these services, you must choose `ip` as the target type,
    not `instance`, because tasks that use the `awsvpc` network mode are associated
    with an elastic network interface, not an Amazon EC2 instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_group_arn",
                "targetGroupArn",
                TypeInfo(str),
            ),
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "container_name",
                "containerName",
                TypeInfo(str),
            ),
            (
                "container_port",
                "containerPort",
                TypeInfo(int),
            ),
        ]

    # The full Amazon Resource Name (ARN) of the Elastic Load Balancing target
    # group associated with a service.

    # If your service's task definition uses the `awsvpc` network mode (which is
    # required for the Fargate launch type), you must choose `ip` as the target
    # type, not `instance`, because tasks that use the `awsvpc` network mode are
    # associated with an elastic network interface, not an Amazon EC2 instance.
    target_group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the container (as it appears in a container definition) to
    # associate with the load balancer.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port on the container to associate with the load balancer. This port
    # must correspond to a `containerPort` in the service's task definition. Your
    # container instances must allow ingress traffic on the `hostPort` of the
    # port mapping.
    container_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LogConfiguration(ShapeBase):
    """
    Log configuration options to send to a custom log driver for the container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "log_driver",
                "logDriver",
                TypeInfo(typing.Union[str, LogDriver]),
            ),
            (
                "options",
                "options",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The log driver to use for the container. The valid values listed for this
    # parameter are log drivers that the Amazon ECS container agent can
    # communicate with by default. If using the Fargate launch type, the only
    # supported value is `awslogs`. For more information about using the
    # `awslogs` driver, see [Using the awslogs Log
    # Driver](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html)
    # in the _Amazon Elastic Container Service Developer Guide_.

    # If you have a custom driver that is not listed above that you would like to
    # work with the Amazon ECS container agent, you can fork the Amazon ECS
    # container agent project that is [available on
    # GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work
    # with that driver. We encourage you to submit pull requests for changes that
    # you would like to have included. However, Amazon Web Services does not
    # currently support running modified copies of this software.

    # This parameter requires version 1.18 of the Docker Remote API or greater on
    # your container instance. To check the Docker Remote API version on your
    # container instance, log in to your container instance and run the following
    # command: `sudo docker version | grep "Server API version"`
    log_driver: typing.Union[str, "LogDriver"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration options to send to the log driver. This parameter
    # requires version 1.19 of the Docker Remote API or greater on your container
    # instance. To check the Docker Remote API version on your container
    # instance, log in to your container instance and run the following command:
    # `sudo docker version | grep "Server API version"`
    options: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LogDriver(str):
    json_file = "json-file"
    syslog = "syslog"
    journald = "journald"
    gelf = "gelf"
    fluentd = "fluentd"
    awslogs = "awslogs"
    splunk = "splunk"


@dataclasses.dataclass
class MissingVersionException(ShapeBase):
    """
    Amazon ECS is unable to determine the current version of the Amazon ECS
    container agent on the container instance and does not have enough information
    to proceed with an update. This could be because the agent running on the
    container instance is an older or custom version that does not use our version
    information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class MountPoint(ShapeBase):
    """
    Details on a volume mount point that is used in a container definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_volume",
                "sourceVolume",
                TypeInfo(str),
            ),
            (
                "container_path",
                "containerPath",
                TypeInfo(str),
            ),
            (
                "read_only",
                "readOnly",
                TypeInfo(bool),
            ),
        ]

    # The name of the volume to mount. Must be a volume name referenced in the
    # `name` parameter of task definition `volume`.
    source_volume: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path on the container to mount the host volume at.
    container_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this value is `true`, the container has read-only access to the volume.
    # If this value is `false`, then the container can write to the volume. The
    # default value is `false`.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NetworkBinding(ShapeBase):
    """
    Details on the network bindings between a container and its host container
    instance. After a task reaches the `RUNNING` status, manual and automatic host
    and container port assignments are visible in the `networkBindings` section of
    DescribeTasks API responses.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bind_ip",
                "bindIP",
                TypeInfo(str),
            ),
            (
                "container_port",
                "containerPort",
                TypeInfo(int),
            ),
            (
                "host_port",
                "hostPort",
                TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, TransportProtocol]),
            ),
        ]

    # The IP address that the container is bound to on the container instance.
    bind_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on the container that is used with the network binding.
    container_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on the host that is used with the network binding.
    host_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol used for the network binding.
    protocol: typing.Union[str, "TransportProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NetworkConfiguration(ShapeBase):
    """
    An object representing the network configuration for a task or service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "awsvpc_configuration",
                "awsvpcConfiguration",
                TypeInfo(AwsVpcConfiguration),
            ),
        ]

    # The VPC subnets and security groups associated with a task.

    # All specified subnets and security groups must be from the same VPC.
    awsvpc_configuration: "AwsVpcConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NetworkInterface(ShapeBase):
    """
    An object representing the elastic network interface for tasks that use the
    `awsvpc` network mode.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attachment_id",
                "attachmentId",
                TypeInfo(str),
            ),
            (
                "private_ipv4_address",
                "privateIpv4Address",
                TypeInfo(str),
            ),
            (
                "ipv6_address",
                "ipv6Address",
                TypeInfo(str),
            ),
        ]

    # The attachment ID for the network interface.
    attachment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private IPv4 address for the network interface.
    private_ipv4_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private IPv6 address for the network interface.
    ipv6_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class NetworkMode(str):
    bridge = "bridge"
    host = "host"
    awsvpc = "awsvpc"
    none = "none"


@dataclasses.dataclass
class NoUpdateAvailableException(ShapeBase):
    """
    There is no update available for this Amazon ECS container agent. This could be
    because the agent is already running the latest version, or it is so old that
    there is no update path to the current version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PlacementConstraint(ShapeBase):
    """
    An object representing a constraint on task placement. For more information, see
    [Task Placement
    Constraints](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    placement-constraints.html) in the _Amazon Elastic Container Service Developer
    Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, PlacementConstraintType]),
            ),
            (
                "expression",
                "expression",
                TypeInfo(str),
            ),
        ]

    # The type of constraint. Use `distinctInstance` to ensure that each task in
    # a particular group is running on a different container instance. Use
    # `memberOf` to restrict the selection to a group of valid candidates. The
    # value `distinctInstance` is not supported in task definitions.
    type: typing.Union[str, "PlacementConstraintType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A cluster query language expression to apply to the constraint. You cannot
    # specify an expression if the constraint type is `distinctInstance`. For
    # more information, see [Cluster Query
    # Language](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-
    # query-language.html) in the _Amazon Elastic Container Service Developer
    # Guide_.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PlacementConstraintType(str):
    distinctInstance = "distinctInstance"
    memberOf = "memberOf"


@dataclasses.dataclass
class PlacementStrategy(ShapeBase):
    """
    The task placement strategy for a task or service. For more information, see
    [Task Placement
    Strategies](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    placement-strategies.html) in the _Amazon Elastic Container Service Developer
    Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, PlacementStrategyType]),
            ),
            (
                "field",
                "field",
                TypeInfo(str),
            ),
        ]

    # The type of placement strategy. The `random` placement strategy randomly
    # places tasks on available candidates. The `spread` placement strategy
    # spreads placement across available candidates evenly based on the `field`
    # parameter. The `binpack` strategy places tasks on available candidates that
    # have the least available amount of the resource that is specified with the
    # `field` parameter. For example, if you binpack on memory, a task is placed
    # on the instance with the least amount of remaining memory (but still enough
    # to run the task).
    type: typing.Union[str, "PlacementStrategyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The field to apply the placement strategy against. For the `spread`
    # placement strategy, valid values are `instanceId` (or `host`, which has the
    # same effect), or any platform or custom attribute that is applied to a
    # container instance, such as `attribute:ecs.availability-zone`. For the
    # `binpack` placement strategy, valid values are `cpu` and `memory`. For the
    # `random` placement strategy, this field is not used.
    field: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PlacementStrategyType(str):
    random = "random"
    spread = "spread"
    binpack = "binpack"


@dataclasses.dataclass
class PlatformTaskDefinitionIncompatibilityException(ShapeBase):
    """
    The specified platform version does not satisfy the task definition's required
    capabilities.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PlatformUnknownException(ShapeBase):
    """
    The specified platform version does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PortMapping(ShapeBase):
    """
    Port mappings allow containers to access ports on the host container instance to
    send or receive traffic. Port mappings are specified as part of the container
    definition.

    If using containers in a task with the `awsvpc` or `host` network mode, exposed
    ports should be specified using `containerPort`. The `hostPort` can be left
    blank or it must be the same value as the `containerPort`.

    After a task reaches the `RUNNING` status, manual and automatic host and
    container port assignments are visible in the `networkBindings` section of
    DescribeTasks API responses.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_port",
                "containerPort",
                TypeInfo(int),
            ),
            (
                "host_port",
                "hostPort",
                TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, TransportProtocol]),
            ),
        ]

    # The port number on the container that is bound to the user-specified or
    # automatically assigned host port.

    # If using containers in a task with the `awsvpc` or `host` network mode,
    # exposed ports should be specified using `containerPort`.

    # If using containers in a task with the `bridge` network mode and you
    # specify a container port and not a host port, your container automatically
    # receives a host port in the ephemeral port range (for more information, see
    # `hostPort`). Port mappings that are automatically assigned in this way do
    # not count toward the 100 reserved ports limit of a container instance.
    container_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number on the container instance to reserve for your container.

    # If using containers in a task with the `awsvpc` or `host` network mode, the
    # `hostPort` can either be left blank or set to the same value as the
    # `containerPort`.

    # If using containers in a task with the `bridge` network mode, you can
    # specify a non-reserved host port for your container port mapping, or you
    # can omit the `hostPort` (or set it to `0`) while specifying a
    # `containerPort` and your container automatically receives a port in the
    # ephemeral port range for your container instance operating system and
    # Docker version.

    # The default ephemeral port range for Docker version 1.6.0 and later is
    # listed on the instance under `/proc/sys/net/ipv4/ip_local_port_range`; if
    # this kernel parameter is unavailable, the default ephemeral port range from
    # 49153 through 65535 is used. You should not attempt to specify a host port
    # in the ephemeral port range as these are reserved for automatic assignment.
    # In general, ports below 32768 are outside of the ephemeral port range.

    # The default ephemeral port range from 49153 through 65535 is always used
    # for Docker versions before 1.6.0.

    # The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376,
    # and the Amazon ECS container agent ports 51678 and 51679. Any host port
    # that was previously specified in a running task is also reserved while the
    # task is running (after a task stops, the host port is released). The
    # current reserved ports are displayed in the `remainingResources` of
    # DescribeContainerInstances output, and a container instance may have up to
    # 100 reserved ports at a time, including the default reserved ports
    # (automatically assigned ports do not count toward the 100 reserved ports
    # limit).
    host_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol used for the port mapping. Valid values are `tcp` and `udp`.
    # The default is `tcp`.
    protocol: typing.Union[str, "TransportProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # The attributes to apply to your resource. You can specify up to 10 custom
    # attributes per resource. You can specify up to 10 attributes in a single
    # call.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name or full Amazon Resource Name (ARN) of the cluster that
    # contains the resource to apply attributes. If you do not specify a cluster,
    # the default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes applied to your resource.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterContainerInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "instance_identity_document",
                "instanceIdentityDocument",
                TypeInfo(str),
            ),
            (
                "instance_identity_document_signature",
                "instanceIdentityDocumentSignature",
                TypeInfo(str),
            ),
            (
                "total_resources",
                "totalResources",
                TypeInfo(typing.List[Resource]),
            ),
            (
                "version_info",
                "versionInfo",
                TypeInfo(VersionInfo),
            ),
            (
                "container_instance_arn",
                "containerInstanceArn",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the cluster with which
    # to register your container instance. If you do not specify a cluster, the
    # default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance identity document for the EC2 instance to register. This
    # document can be found by running the following command from the instance:
    # `curl http://169.254.169.254/latest/dynamic/instance-identity/document/`
    instance_identity_document: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance identity document signature for the EC2 instance to register.
    # This signature can be found by running the following command from the
    # instance: `curl http://169.254.169.254/latest/dynamic/instance-
    # identity/signature/`
    instance_identity_document_signature: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resources available on the instance.
    total_resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version information for the Amazon ECS container agent and Docker
    # daemon running on the container instance.
    version_info: "VersionInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the container instance (if it was previously registered).
    container_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The container instance attributes that this container instance supports.
    attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterContainerInstanceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_instance",
                "containerInstance",
                TypeInfo(ContainerInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The container instance that was registered.
    container_instance: "ContainerInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RegisterTaskDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "family",
                "family",
                TypeInfo(str),
            ),
            (
                "container_definitions",
                "containerDefinitions",
                TypeInfo(typing.List[ContainerDefinition]),
            ),
            (
                "task_role_arn",
                "taskRoleArn",
                TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "executionRoleArn",
                TypeInfo(str),
            ),
            (
                "network_mode",
                "networkMode",
                TypeInfo(typing.Union[str, NetworkMode]),
            ),
            (
                "volumes",
                "volumes",
                TypeInfo(typing.List[Volume]),
            ),
            (
                "placement_constraints",
                "placementConstraints",
                TypeInfo(typing.List[TaskDefinitionPlacementConstraint]),
            ),
            (
                "requires_compatibilities",
                "requiresCompatibilities",
                TypeInfo(typing.List[typing.Union[str, Compatibility]]),
            ),
            (
                "cpu",
                "cpu",
                TypeInfo(str),
            ),
            (
                "memory",
                "memory",
                TypeInfo(str),
            ),
        ]

    # You must specify a `family` for a task definition, which allows you to
    # track multiple versions of the same task definition. The `family` is used
    # as a name for your task definition. Up to 255 letters (uppercase and
    # lowercase), numbers, hyphens, and underscores are allowed.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of container definitions in JSON format that describe the different
    # containers that make up your task.
    container_definitions: typing.List["ContainerDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The short name or full Amazon Resource Name (ARN) of the IAM role that
    # containers in this task can assume. All containers in this task are granted
    # the permissions that are specified in this role. For more information, see
    # [IAM Roles for
    # Tasks](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-
    # roles.html) in the _Amazon Elastic Container Service Developer Guide_.
    task_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the task execution role that the Amazon
    # ECS container agent and the Docker daemon can assume.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Docker networking mode to use for the containers in the task. The valid
    # values are `none`, `bridge`, `awsvpc`, and `host`. The default Docker
    # network mode is `bridge`. If using the Fargate launch type, the `awsvpc`
    # network mode is required. If using the EC2 launch type, any network mode
    # can be used. If the network mode is set to `none`, you can't specify port
    # mappings in your container definitions, and the task's containers do not
    # have external connectivity. The `host` and `awsvpc` network modes offer the
    # highest networking performance for containers because they use the EC2
    # network stack instead of the virtualized network stack provided by the
    # `bridge` mode.

    # With the `host` and `awsvpc` network modes, exposed container ports are
    # mapped directly to the corresponding host port (for the `host` network
    # mode) or the attached elastic network interface port (for the `awsvpc`
    # network mode), so you cannot take advantage of dynamic host port mappings.

    # If the network mode is `awsvpc`, the task is allocated an Elastic Network
    # Interface, and you must specify a NetworkConfiguration when you create a
    # service or run a task with the task definition. For more information, see
    # [Task
    # Networking](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    # networking.html) in the _Amazon Elastic Container Service Developer Guide_.

    # If the network mode is `host`, you can't run multiple instantiations of the
    # same task on a single container instance when port mappings are used.

    # Docker for Windows uses different network modes than Docker for Linux. When
    # you register a task definition with Windows containers, you must not
    # specify a network mode.

    # For more information, see [Network
    # settings](https://docs.docker.com/engine/reference/run/#network-settings)
    # in the _Docker run reference_.
    network_mode: typing.Union[str, "NetworkMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of volume definitions in JSON format that containers in your task
    # may use.
    volumes: typing.List["Volume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of placement constraint objects to use for the task. You can
    # specify a maximum of 10 constraints per task (this limit includes
    # constraints in the task definition and those specified at run time).
    placement_constraints: typing.List["TaskDefinitionPlacementConstraint"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The launch type required by the task. If no value is specified, it defaults
    # to `EC2`.
    requires_compatibilities: typing.List[typing.Union[str, "Compatibility"]
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The number of CPU units used by the task. It can be expressed as an integer
    # using CPU units, for example `1024`, or as a string using vCPUs, for
    # example `1 vCPU` or `1 vcpu`, in a task definition. String values are
    # converted to an integer indicating the CPU units when the task definition
    # is registered.

    # Task-level CPU and memory parameters are ignored for Windows containers. We
    # recommend specifying container-level resources for Windows containers.

    # If using the EC2 launch type, this field is optional. Supported values are
    # between `128` CPU units (`0.125` vCPUs) and `10240` CPU units (`10` vCPUs).

    # If using the Fargate launch type, this field is required and you must use
    # one of the following values, which determines your range of supported
    # values for the `memory` parameter:

    #   * 256 (.25 vCPU) - Available `memory` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)

    #   * 512 (.5 vCPU) - Available `memory` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)

    #   * 1024 (1 vCPU) - Available `memory` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

    #   * 2048 (2 vCPU) - Available `memory` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

    #   * 4096 (4 vCPU) - Available `memory` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)
    cpu: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of memory (in MiB) used by the task. It can be expressed as an
    # integer using MiB, for example `1024`, or as a string using GB, for example
    # `1GB` or `1 GB`, in a task definition. String values are converted to an
    # integer indicating the MiB when the task definition is registered.

    # Task-level CPU and memory parameters are ignored for Windows containers. We
    # recommend specifying container-level resources for Windows containers.

    # If using the EC2 launch type, this field is optional.

    # If using the Fargate launch type, this field is required and you must use
    # one of the following values, which determines your range of supported
    # values for the `cpu` parameter:

    #   * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)

    #   * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)

    #   * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)

    #   * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)

    #   * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
    memory: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterTaskDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(TaskDefinition),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of the registered task definition.
    task_definition: "TaskDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RepositoryCredentials(ShapeBase):
    """
    The repository credentials for private registry authentication.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "credentials_parameter",
                "credentialsParameter",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) or name of the secret containing the private
    # repository credentials.
    credentials_parameter: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(ShapeBase):
    """
    Describes the resources available for a container instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(str),
            ),
            (
                "double_value",
                "doubleValue",
                TypeInfo(float),
            ),
            (
                "long_value",
                "longValue",
                TypeInfo(int),
            ),
            (
                "integer_value",
                "integerValue",
                TypeInfo(int),
            ),
            (
                "string_set_value",
                "stringSetValue",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the resource, such as `CPU`, `MEMORY`, `PORTS`, `PORTS_UDP`, or
    # a user-defined resource.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the resource, such as `INTEGER`, `DOUBLE`, `LONG`, or
    # `STRINGSET`.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the `doubleValue` type is set, the value of the resource must be a
    # double precision floating-point type.
    double_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the `longValue` type is set, the value of the resource must be an
    # extended precision floating-point type.
    long_value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the `integerValue` type is set, the value of the resource must be an
    # integer.
    integer_value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the `stringSetValue` type is set, the value of the resource must be a
    # string type.
    string_set_value: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RunTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "overrides",
                "overrides",
                TypeInfo(TaskOverride),
            ),
            (
                "count",
                "count",
                TypeInfo(int),
            ),
            (
                "started_by",
                "startedBy",
                TypeInfo(str),
            ),
            (
                "group",
                "group",
                TypeInfo(str),
            ),
            (
                "placement_constraints",
                "placementConstraints",
                TypeInfo(typing.List[PlacementConstraint]),
            ),
            (
                "placement_strategy",
                "placementStrategy",
                TypeInfo(typing.List[PlacementStrategy]),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "platform_version",
                "platformVersion",
                TypeInfo(str),
            ),
            (
                "network_configuration",
                "networkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
        ]

    # The `family` and `revision` (`family:revision`) or full ARN of the task
    # definition to run. If a `revision` is not specified, the latest `ACTIVE`
    # revision is used.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster on which
    # to run your task. If you do not specify a cluster, the default cluster is
    # assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of container overrides in JSON format that specify the name of a
    # container in the specified task definition and the overrides it should
    # receive. You can override the default command for a container (that is
    # specified in the task definition or Docker image) with a `command`
    # override. You can also override existing environment variables (that are
    # specified in the task definition or Docker image) on a container or add new
    # environment variables to it with an `environment` override.

    # A total of 8192 characters are allowed for overrides. This limit includes
    # the JSON formatting characters of the override structure.
    overrides: "TaskOverride" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instantiations of the specified task to place on your
    # cluster. You can specify up to 10 tasks per call.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional tag specified when a task is started. For example if you
    # automatically trigger a task to run a batch process job, you could apply a
    # unique identifier for that job to your task with the `startedBy` parameter.
    # You can then identify which tasks belong to that job by filtering the
    # results of a ListTasks call with the `startedBy` value. Up to 36 letters
    # (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

    # If a task is started by an Amazon ECS service, then the `startedBy`
    # parameter contains the deployment ID of the service that starts it.
    started_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the task group to associate with the task. The default value is
    # the family name of the task definition (for example, family:my-family-
    # name).
    group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of placement constraint objects to use for the task. You can
    # specify up to 10 constraints per task (including constraints in the task
    # definition and those specified at run time).
    placement_constraints: typing.List["PlacementConstraint"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The placement strategy objects to use for the task. You can specify a
    # maximum of five strategy rules per task.
    placement_strategy: typing.List["PlacementStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The launch type on which to run your task.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform version on which to run your task. If one is not specified,
    # the latest version is used by default.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network configuration for the task. This parameter is required for task
    # definitions that use the `awsvpc` network mode to receive their own Elastic
    # Network Interface, and it is not supported for other network modes. For
    # more information, see [Task
    # Networking](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    # networking.html) in the _Amazon Elastic Container Service Developer Guide_.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RunTaskResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tasks",
                "tasks",
                TypeInfo(typing.List[Task]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A full description of the tasks that were run. The tasks that were
    # successfully placed on your cluster are described here.
    tasks: typing.List["Task"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SchedulingStrategy(str):
    REPLICA = "REPLICA"
    DAEMON = "DAEMON"


class Scope(str):
    task = "task"
    shared = "shared"


@dataclasses.dataclass
class ServerException(ShapeBase):
    """
    These errors are usually caused by a server issue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Service(ShapeBase):
    """
    Details on a service within a cluster
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service_arn",
                "serviceArn",
                TypeInfo(str),
            ),
            (
                "service_name",
                "serviceName",
                TypeInfo(str),
            ),
            (
                "cluster_arn",
                "clusterArn",
                TypeInfo(str),
            ),
            (
                "load_balancers",
                "loadBalancers",
                TypeInfo(typing.List[LoadBalancer]),
            ),
            (
                "service_registries",
                "serviceRegistries",
                TypeInfo(typing.List[ServiceRegistry]),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "desired_count",
                "desiredCount",
                TypeInfo(int),
            ),
            (
                "running_count",
                "runningCount",
                TypeInfo(int),
            ),
            (
                "pending_count",
                "pendingCount",
                TypeInfo(int),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "platform_version",
                "platformVersion",
                TypeInfo(str),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
            (
                "deployment_configuration",
                "deploymentConfiguration",
                TypeInfo(DeploymentConfiguration),
            ),
            (
                "deployments",
                "deployments",
                TypeInfo(typing.List[Deployment]),
            ),
            (
                "role_arn",
                "roleArn",
                TypeInfo(str),
            ),
            (
                "events",
                "events",
                TypeInfo(typing.List[ServiceEvent]),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "placement_constraints",
                "placementConstraints",
                TypeInfo(typing.List[PlacementConstraint]),
            ),
            (
                "placement_strategy",
                "placementStrategy",
                TypeInfo(typing.List[PlacementStrategy]),
            ),
            (
                "network_configuration",
                "networkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
            (
                "health_check_grace_period_seconds",
                "healthCheckGracePeriodSeconds",
                TypeInfo(int),
            ),
            (
                "scheduling_strategy",
                "schedulingStrategy",
                TypeInfo(typing.Union[str, SchedulingStrategy]),
            ),
        ]

    # The ARN that identifies the service. The ARN contains the `arn:aws:ecs`
    # namespace, followed by the Region of the service, the AWS account ID of the
    # service owner, the `service` namespace, and then the service name. For
    # example, `arn:aws:ecs: _region_ : _012345678910_ :service/ _my-service_ `.
    service_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of your service. Up to 255 letters (uppercase and lowercase),
    # numbers, hyphens, and underscores are allowed. Service names must be unique
    # within a cluster, but you can have similarly named services in multiple
    # clusters within a Region or across multiple Regions.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the cluster that hosts the service.
    cluster_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Elastic Load Balancing load balancer objects, containing the load
    # balancer name, the container name (as it appears in a container
    # definition), and the container port to access from the load balancer.

    # Services with tasks that use the `awsvpc` network mode (for example, those
    # with the Fargate launch type) only support Application Load Balancers and
    # Network Load Balancers; Classic Load Balancers are not supported. Also,
    # when you create any target groups for these services, you must choose `ip`
    # as the target type, not `instance`, because tasks that use the `awsvpc`
    # network mode are associated with an elastic network interface, not an
    # Amazon EC2 instance.
    load_balancers: typing.List["LoadBalancer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    service_registries: typing.List["ServiceRegistry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the service. The valid values are `ACTIVE`, `DRAINING`, or
    # `INACTIVE`.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired number of instantiations of the task definition to keep running
    # on the service. This value is specified when the service is created with
    # CreateService, and it can be modified with UpdateService.
    desired_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks in the cluster that are in the `RUNNING` state.
    running_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of tasks in the cluster that are in the `PENDING` state.
    pending_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The launch type on which your service is running.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform version on which your task is running. For more information,
    # see [AWS Fargate Platform
    # Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task definition to use for tasks in the service. This value is
    # specified when the service is created with CreateService, and it can be
    # modified with UpdateService.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional deployment parameters that control how many tasks run during the
    # deployment and the ordering of stopping and starting tasks.
    deployment_configuration: "DeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of deployments for the service.
    deployments: typing.List["Deployment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the IAM role associated with the service that allows the Amazon
    # ECS container agent to register container instances with an Elastic Load
    # Balancing load balancer.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The event stream for your service. A maximum of 100 of the latest events
    # are displayed.
    events: typing.List["ServiceEvent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the service was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The placement constraints for the tasks in the service.
    placement_constraints: typing.List["PlacementConstraint"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The placement strategy that determines how tasks for the service are
    # placed.
    placement_strategy: typing.List["PlacementStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC subnet and security group configuration for tasks that receive
    # their own elastic network interface by using the `awsvpc` networking mode.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The period of time, in seconds, that the Amazon ECS service scheduler
    # ignores unhealthy Elastic Load Balancing target health checks after a task
    # has first started.
    health_check_grace_period_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The scheduling strategy to use for the service. For more information, see
    # [Services](http://docs.aws.amazon.com/AmazonECS/latest/developerguideecs_services.html).

    # There are two service scheduler strategies available:

    #   * `REPLICA`-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.

    #   * `DAEMON`-The daemon scheduling strategy deploys exactly one task on each container instance in your cluster. When using this strategy, do not specify a desired number of tasks or any task placement strategies.

    # Fargate tasks do not support the `DAEMON` scheduling strategy.
    scheduling_strategy: typing.Union[str, "SchedulingStrategy"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class ServiceEvent(ShapeBase):
    """
    Details on an event associated with a service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The ID string of the event.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp for when the event was triggered.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The event message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ServiceNotActiveException(ShapeBase):
    """
    The specified service is not active. You can't update a service that is
    inactive. If you have previously deleted a service, you can re-create it with
    CreateService.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ServiceNotFoundException(ShapeBase):
    """
    The specified service could not be found. You can view your available services
    with ListServices. Amazon ECS services are cluster-specific and region-specific.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ServiceRegistry(ShapeBase):
    """
    Details of the service registry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registry_arn",
                "registryArn",
                TypeInfo(str),
            ),
            (
                "port",
                "port",
                TypeInfo(int),
            ),
            (
                "container_name",
                "containerName",
                TypeInfo(str),
            ),
            (
                "container_port",
                "containerPort",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the service registry. The currently
    # supported service registry is Amazon Route 53 Auto Naming. For more
    # information, see
    # [Service](https://docs.aws.amazon.com/Route53/latest/APIReference/API_autonaming_Service.html).
    registry_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port value used if your service discovery service specified an SRV
    # record. This field is required if both the `awsvpc` network mode and SRV
    # records are used.
    port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The container name value, already specified in the task definition, to be
    # used for your service discovery service. If the task definition that your
    # service task specifies uses the `bridge` or `host` network mode, you must
    # specify a `containerName` and `containerPort` combination from the task
    # definition. If the task definition that your service task specifies uses
    # the `awsvpc` network mode and a type SRV DNS record is used, you must
    # specify either a `containerName` and `containerPort` combination or a
    # `port` value, but not both.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port value, already specified in the task definition, to be used for
    # your service discovery service. If the task definition your service task
    # specifies uses the `bridge` or `host` network mode, you must specify a
    # `containerName` and `containerPort` combination from the task definition.
    # If the task definition your service task specifies uses the `awsvpc`
    # network mode and a type SRV DNS record is used, you must specify either a
    # `containerName` and `containerPort` combination or a `port` value, but not
    # both.
    container_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class SortOrder(str):
    ASC = "ASC"
    DESC = "DESC"


@dataclasses.dataclass
class StartTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
            (
                "container_instances",
                "containerInstances",
                TypeInfo(typing.List[str]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "overrides",
                "overrides",
                TypeInfo(TaskOverride),
            ),
            (
                "started_by",
                "startedBy",
                TypeInfo(str),
            ),
            (
                "group",
                "group",
                TypeInfo(str),
            ),
            (
                "network_configuration",
                "networkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
        ]

    # The `family` and `revision` (`family:revision`) or full ARN of the task
    # definition to start. If a `revision` is not specified, the latest `ACTIVE`
    # revision is used.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The container instance IDs or full ARN entries for the container instances
    # on which you would like to place your task. You can specify up to 10
    # container instances.
    container_instances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name or full Amazon Resource Name (ARN) of the cluster on which
    # to start your task. If you do not specify a cluster, the default cluster is
    # assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of container overrides in JSON format that specify the name of a
    # container in the specified task definition and the overrides it should
    # receive. You can override the default command for a container (that is
    # specified in the task definition or Docker image) with a `command`
    # override. You can also override existing environment variables (that are
    # specified in the task definition or Docker image) on a container or add new
    # environment variables to it with an `environment` override.

    # A total of 8192 characters are allowed for overrides. This limit includes
    # the JSON formatting characters of the override structure.
    overrides: "TaskOverride" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional tag specified when a task is started. For example if you
    # automatically trigger a task to run a batch process job, you could apply a
    # unique identifier for that job to your task with the `startedBy` parameter.
    # You can then identify which tasks belong to that job by filtering the
    # results of a ListTasks call with the `startedBy` value. Up to 36 letters
    # (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

    # If a task is started by an Amazon ECS service, then the `startedBy`
    # parameter contains the deployment ID of the service that starts it.
    started_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the task group to associate with the task. The default value is
    # the family name of the task definition (for example, family:my-family-
    # name).
    group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC subnet and security group configuration for tasks that receive
    # their own elastic network interface by using the `awsvpc` networking mode.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StartTaskResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tasks",
                "tasks",
                TypeInfo(typing.List[Task]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A full description of the tasks that were started. Each task that was
    # successfully placed on your container instances is described.
    tasks: typing.List["Task"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopTaskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task",
                "task",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
        ]

    # The task ID or full ARN entry of the task to stop.
    task: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the task to stop. If you do not specify a cluster, the default cluster is
    # assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional message specified when a task is stopped. For example, if you
    # are using a custom scheduler, you can use this parameter to specify the
    # reason for stopping the task here, and the message appears in subsequent
    # DescribeTasks API operations on this task. Up to 255 characters are allowed
    # in this message.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopTaskResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task",
                "task",
                TypeInfo(Task),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The task that was stopped.
    task: "Task" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubmitContainerStateChangeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "task",
                "task",
                TypeInfo(str),
            ),
            (
                "container_name",
                "containerName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "exit_code",
                "exitCode",
                TypeInfo(int),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
            (
                "network_bindings",
                "networkBindings",
                TypeInfo(typing.List[NetworkBinding]),
            ),
        ]

    # The short name or full ARN of the cluster that hosts the container.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task ID or full Amazon Resource Name (ARN) of the task that hosts the
    # container.
    task: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the container.
    container_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the state change request.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The exit code returned for the state change request.
    exit_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason for the state change request.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network bindings of the container.
    network_bindings: typing.List["NetworkBinding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubmitContainerStateChangeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "acknowledgment",
                "acknowledgment",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Acknowledgement of the state change.
    acknowledgment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubmitTaskStateChangeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "task",
                "task",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
            (
                "containers",
                "containers",
                TypeInfo(typing.List[ContainerStateChange]),
            ),
            (
                "attachments",
                "attachments",
                TypeInfo(typing.List[AttachmentStateChange]),
            ),
            (
                "pull_started_at",
                "pullStartedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "pull_stopped_at",
                "pullStoppedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_stopped_at",
                "executionStoppedAt",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the task.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The task ID or full ARN of the task in the state change request.
    task: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the state change request.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason for the state change request.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any containers associated with the state change request.
    containers: typing.List["ContainerStateChange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any attachments associated with the state change request.
    attachments: typing.List["AttachmentStateChange"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the container image pull began.
    pull_started_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the container image pull completed.
    pull_stopped_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task execution stopped.
    execution_stopped_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SubmitTaskStateChangeResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "acknowledgment",
                "acknowledgment",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Acknowledgement of the state change.
    acknowledgment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TargetNotFoundException(ShapeBase):
    """
    The specified target could not be found. You can view your available container
    instances with ListContainerInstances. Amazon ECS container instances are
    cluster-specific and region-specific.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class TargetType(str):
    container_instance = "container-instance"


@dataclasses.dataclass
class Task(ShapeBase):
    """
    Details on a task in a cluster.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_arn",
                "taskArn",
                TypeInfo(str),
            ),
            (
                "cluster_arn",
                "clusterArn",
                TypeInfo(str),
            ),
            (
                "task_definition_arn",
                "taskDefinitionArn",
                TypeInfo(str),
            ),
            (
                "container_instance_arn",
                "containerInstanceArn",
                TypeInfo(str),
            ),
            (
                "overrides",
                "overrides",
                TypeInfo(TaskOverride),
            ),
            (
                "last_status",
                "lastStatus",
                TypeInfo(str),
            ),
            (
                "desired_status",
                "desiredStatus",
                TypeInfo(str),
            ),
            (
                "cpu",
                "cpu",
                TypeInfo(str),
            ),
            (
                "memory",
                "memory",
                TypeInfo(str),
            ),
            (
                "containers",
                "containers",
                TypeInfo(typing.List[Container]),
            ),
            (
                "started_by",
                "startedBy",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(int),
            ),
            (
                "stopped_reason",
                "stoppedReason",
                TypeInfo(str),
            ),
            (
                "connectivity",
                "connectivity",
                TypeInfo(typing.Union[str, Connectivity]),
            ),
            (
                "connectivity_at",
                "connectivityAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "pull_started_at",
                "pullStartedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "pull_stopped_at",
                "pullStoppedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "execution_stopped_at",
                "executionStoppedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "started_at",
                "startedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopping_at",
                "stoppingAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopped_at",
                "stoppedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "group",
                "group",
                TypeInfo(str),
            ),
            (
                "launch_type",
                "launchType",
                TypeInfo(typing.Union[str, LaunchType]),
            ),
            (
                "platform_version",
                "platformVersion",
                TypeInfo(str),
            ),
            (
                "attachments",
                "attachments",
                TypeInfo(typing.List[Attachment]),
            ),
            (
                "health_status",
                "healthStatus",
                TypeInfo(typing.Union[str, HealthStatus]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the task.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the cluster that hosts the task.
    cluster_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the task definition that creates the task.
    task_definition_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the container instances that host the task.
    container_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more container overrides.
    overrides: "TaskOverride" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last known status of the task. For more information, see [Task
    # Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html).
    last_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired status of the task. For more information, see [Task
    # Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html).
    desired_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of CPU units used by the task. It can be expressed as an integer
    # using CPU units, for example `1024`, or as a string using vCPUs, for
    # example `1 vCPU` or `1 vcpu`, in a task definition. String values are
    # converted to an integer indicating the CPU units when the task definition
    # is registered.

    # If using the EC2 launch type, this field is optional. Supported values are
    # between `128` CPU units (`0.125` vCPUs) and `10240` CPU units (`10` vCPUs).

    # If using the Fargate launch type, this field is required and you must use
    # one of the following values, which determines your range of supported
    # values for the `memory` parameter:

    #   * 256 (.25 vCPU) - Available `memory` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)

    #   * 512 (.5 vCPU) - Available `memory` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)

    #   * 1024 (1 vCPU) - Available `memory` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

    #   * 2048 (2 vCPU) - Available `memory` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

    #   * 4096 (4 vCPU) - Available `memory` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)
    cpu: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of memory (in MiB) used by the task. It can be expressed as an
    # integer using MiB, for example `1024`, or as a string using GB, for example
    # `1GB` or `1 GB`, in a task definition. String values are converted to an
    # integer indicating the MiB when the task definition is registered.

    # If using the EC2 launch type, this field is optional.

    # If using the Fargate launch type, this field is required and you must use
    # one of the following values, which determines your range of supported
    # values for the `cpu` parameter:

    #   * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)

    #   * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)

    #   * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)

    #   * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)

    #   * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
    memory: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The containers associated with the task.
    containers: typing.List["Container"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tag specified when a task is started. If the task is started by an
    # Amazon ECS service, then the `startedBy` parameter contains the deployment
    # ID of the service that starts it.
    started_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version counter for the task. Every time a task experiences a change
    # that triggers a CloudWatch event, the version counter is incremented. If
    # you are replicating your Amazon ECS task state with CloudWatch Events, you
    # can compare the version of a task reported by the Amazon ECS APIs with the
    # version reported in CloudWatch Events for the task (inside the `detail`
    # object) to verify that the version in your event stream is current.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reason the task was stopped.
    stopped_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The connectivity status of a task.
    connectivity: typing.Union[str, "Connectivity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task last went into `CONNECTED` status.
    connectivity_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the container image pull began.
    pull_started_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the container image pull completed.
    pull_stopped_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task execution stopped.
    execution_stopped_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task was created (the task entered the
    # `PENDING` state).
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task started (the task transitioned from
    # the `PENDING` state to the `RUNNING` state).
    started_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task stops (transitions from the `RUNNING`
    # state to `STOPPED`).
    stopping_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp for when the task was stopped (the task transitioned
    # from the `RUNNING` state to the `STOPPED` state).
    stopped_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the task group associated with the task.
    group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The launch type on which your task is running.
    launch_type: typing.Union[str, "LaunchType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform version on which your task is running. For more information,
    # see [AWS Fargate Platform
    # Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The elastic network adapter associated with the task if the task uses the
    # `awsvpc` network mode.
    attachments: typing.List["Attachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The health status for the task, which is determined by the health of the
    # essential containers in the task. If all essential containers in the task
    # are reporting as `HEALTHY`, then the task status also reports as `HEALTHY`.
    # If any essential containers in the task are reporting as `UNHEALTHY` or
    # `UNKNOWN`, then the task status also reports as `UNHEALTHY` or `UNKNOWN`,
    # accordingly.

    # The Amazon ECS container agent does not monitor or report on Docker health
    # checks that are embedded in a container image (such as those specified in a
    # parent image or from the image's Dockerfile) and not specified in the
    # container definition. Health check parameters that are specified in a
    # container definition override any Docker health checks that exist in the
    # container image.
    health_status: typing.Union[str, "HealthStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TaskDefinition(ShapeBase):
    """
    Details of a task definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_definition_arn",
                "taskDefinitionArn",
                TypeInfo(str),
            ),
            (
                "container_definitions",
                "containerDefinitions",
                TypeInfo(typing.List[ContainerDefinition]),
            ),
            (
                "family",
                "family",
                TypeInfo(str),
            ),
            (
                "task_role_arn",
                "taskRoleArn",
                TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "executionRoleArn",
                TypeInfo(str),
            ),
            (
                "network_mode",
                "networkMode",
                TypeInfo(typing.Union[str, NetworkMode]),
            ),
            (
                "revision",
                "revision",
                TypeInfo(int),
            ),
            (
                "volumes",
                "volumes",
                TypeInfo(typing.List[Volume]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, TaskDefinitionStatus]),
            ),
            (
                "requires_attributes",
                "requiresAttributes",
                TypeInfo(typing.List[Attribute]),
            ),
            (
                "placement_constraints",
                "placementConstraints",
                TypeInfo(typing.List[TaskDefinitionPlacementConstraint]),
            ),
            (
                "compatibilities",
                "compatibilities",
                TypeInfo(typing.List[typing.Union[str, Compatibility]]),
            ),
            (
                "requires_compatibilities",
                "requiresCompatibilities",
                TypeInfo(typing.List[typing.Union[str, Compatibility]]),
            ),
            (
                "cpu",
                "cpu",
                TypeInfo(str),
            ),
            (
                "memory",
                "memory",
                TypeInfo(str),
            ),
        ]

    # The full Amazon Resource Name (ARN) of the task definition.
    task_definition_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of container definitions in JSON format that describe the different
    # containers that make up your task. For more information about container
    # definition parameters and defaults, see [Amazon ECS Task
    # Definitions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    container_definitions: typing.List["ContainerDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The family of your task definition, used as the definition name.
    family: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the IAM role that containers in this task can assume. All
    # containers in this task are granted the permissions that are specified in
    # this role.

    # IAM roles for tasks on Windows require that the `-EnableTaskIAMRole` option
    # is set when you launch the Amazon ECS-optimized Windows AMI. Your
    # containers must also run some configuration code in order to take advantage
    # of the feature. For more information, see [Windows IAM Roles for
    # Tasks](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    task_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the task execution role that the Amazon
    # ECS container agent and the Docker daemon can assume.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Docker networking mode to use for the containers in the task. The valid
    # values are `none`, `bridge`, `awsvpc`, and `host`. The default Docker
    # network mode is `bridge`. If using the Fargate launch type, the `awsvpc`
    # network mode is required. If using the EC2 launch type, any network mode
    # can be used. If the network mode is set to `none`, you can't specify port
    # mappings in your container definitions, and the task's containers do not
    # have external connectivity. The `host` and `awsvpc` network modes offer the
    # highest networking performance for containers because they use the EC2
    # network stack instead of the virtualized network stack provided by the
    # `bridge` mode.

    # With the `host` and `awsvpc` network modes, exposed container ports are
    # mapped directly to the corresponding host port (for the `host` network
    # mode) or the attached elastic network interface port (for the `awsvpc`
    # network mode), so you cannot take advantage of dynamic host port mappings.

    # If the network mode is `awsvpc`, the task is allocated an Elastic Network
    # Interface, and you must specify a NetworkConfiguration when you create a
    # service or run a task with the task definition. For more information, see
    # [Task
    # Networking](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    # networking.html) in the _Amazon Elastic Container Service Developer Guide_.

    # Currently, only the Amazon ECS-optimized AMI, other Amazon Linux variants
    # with the `ecs-init` package, or AWS Fargate infrastructure support the
    # `awsvpc` network mode.

    # If the network mode is `host`, you can't run multiple instantiations of the
    # same task on a single container instance when port mappings are used.

    # Docker for Windows uses different network modes than Docker for Linux. When
    # you register a task definition with Windows containers, you must not
    # specify a network mode. If you use the console to register a task
    # definition with Windows containers, you must choose the `<default>` network
    # mode object.

    # For more information, see [Network
    # settings](https://docs.docker.com/engine/reference/run/#network-settings)
    # in the _Docker run reference_.
    network_mode: typing.Union[str, "NetworkMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The revision of the task in a particular family. The revision is a version
    # number of a task definition in a family. When you register a task
    # definition for the first time, the revision is `1`; each time you register
    # a new revision of a task definition in the same family, the revision value
    # always increases by one (even if you have deregistered previous revisions
    # in this family).
    revision: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of volumes in a task.

    # If you are using the Fargate launch type, the `host` and `sourcePath`
    # parameters are not supported.

    # For more information about volume definition parameters and defaults, see
    # [Amazon ECS Task
    # Definitions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    volumes: typing.List["Volume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the task definition.
    status: typing.Union[str, "TaskDefinitionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The container instance attributes required by your task. This field is not
    # valid if using the Fargate launch type for your task.
    requires_attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of placement constraint objects to use for tasks. This field is
    # not valid if using the Fargate launch type for your task.
    placement_constraints: typing.List["TaskDefinitionPlacementConstraint"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The launch type to use with your task. For more information, see [Amazon
    # ECS Launch
    # Types](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    compatibilities: typing.List[typing.Union[str, "Compatibility"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The launch type the task is using.
    requires_compatibilities: typing.List[typing.Union[str, "Compatibility"]
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The number of `cpu` units used by the task. If using the EC2 launch type,
    # this field is optional and any value can be used. If using the Fargate
    # launch type, this field is required and you must use one of the following
    # values, which determines your range of valid values for the `memory`
    # parameter:

    #   * 256 (.25 vCPU) - Available `memory` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)

    #   * 512 (.5 vCPU) - Available `memory` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)

    #   * 1024 (1 vCPU) - Available `memory` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

    #   * 2048 (2 vCPU) - Available `memory` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

    #   * 4096 (4 vCPU) - Available `memory` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)
    cpu: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount (in MiB) of memory used by the task. If using the EC2 launch
    # type, this field is optional and any value can be used. If using the
    # Fargate launch type, this field is required and you must use one of the
    # following values, which determines your range of valid values for the `cpu`
    # parameter:

    #   * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)

    #   * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)

    #   * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)

    #   * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)

    #   * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
    memory: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TaskDefinitionFamilyStatus(str):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ALL = "ALL"


@dataclasses.dataclass
class TaskDefinitionPlacementConstraint(ShapeBase):
    """
    An object representing a constraint on task placement in the task definition.

    If you are using the Fargate launch type, task placement constraints are not
    supported.

    For more information, see [Task Placement
    Constraints](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    placement-constraints.html) in the _Amazon Elastic Container Service Developer
    Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(
                    typing.Union[str, TaskDefinitionPlacementConstraintType]
                ),
            ),
            (
                "expression",
                "expression",
                TypeInfo(str),
            ),
        ]

    # The type of constraint. The `DistinctInstance` constraint ensures that each
    # task in a particular group is running on a different container instance.
    # The `MemberOf` constraint restricts selection to be from a group of valid
    # candidates.
    type: typing.Union[str, "TaskDefinitionPlacementConstraintType"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # A cluster query language expression to apply to the constraint. For more
    # information, see [Cluster Query
    # Language](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-
    # query-language.html) in the _Amazon Elastic Container Service Developer
    # Guide_.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TaskDefinitionPlacementConstraintType(str):
    memberOf = "memberOf"


class TaskDefinitionStatus(str):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class TaskOverride(ShapeBase):
    """
    The overrides associated with a task.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_overrides",
                "containerOverrides",
                TypeInfo(typing.List[ContainerOverride]),
            ),
            (
                "task_role_arn",
                "taskRoleArn",
                TypeInfo(str),
            ),
            (
                "execution_role_arn",
                "executionRoleArn",
                TypeInfo(str),
            ),
        ]

    # One or more container overrides sent to a task.
    container_overrides: typing.List["ContainerOverride"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that containers in this task
    # can assume. All containers in this task are granted the permissions that
    # are specified in this role.
    task_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the task execution role that the Amazon
    # ECS container agent and the Docker daemon can assume.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tmpfs(ShapeBase):
    """
    The container path, mount options, and size of the tmpfs mount.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_path",
                "containerPath",
                TypeInfo(str),
            ),
            (
                "size",
                "size",
                TypeInfo(int),
            ),
            (
                "mount_options",
                "mountOptions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The absolute file path where the tmpfs volume is to be mounted.
    container_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size (in MiB) of the tmpfs volume.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tmpfs volume mount options.

    # Valid values: `"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" |
    # "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" |
    # "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" |
    # "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" |
    # "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" |
    # "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" |
    # "nr_blocks" | "mpol"`
    mount_options: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TransportProtocol(str):
    tcp = "tcp"
    udp = "udp"


@dataclasses.dataclass
class Ulimit(ShapeBase):
    """
    The `ulimit` settings to pass to the container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(typing.Union[str, UlimitName]),
            ),
            (
                "soft_limit",
                "softLimit",
                TypeInfo(int),
            ),
            (
                "hard_limit",
                "hardLimit",
                TypeInfo(int),
            ),
        ]

    # The `type` of the `ulimit`.
    name: typing.Union[str, "UlimitName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The soft limit for the ulimit type.
    soft_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hard limit for the ulimit type.
    hard_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class UlimitName(str):
    core = "core"
    cpu = "cpu"
    data = "data"
    fsize = "fsize"
    locks = "locks"
    memlock = "memlock"
    msgqueue = "msgqueue"
    nice = "nice"
    nofile = "nofile"
    nproc = "nproc"
    rss = "rss"
    rtprio = "rtprio"
    rttime = "rttime"
    sigpending = "sigpending"
    stack = "stack"


@dataclasses.dataclass
class UnsupportedFeatureException(ShapeBase):
    """
    The specified task is not supported in this region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateContainerAgentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_instance",
                "containerInstance",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # The container instance ID or full ARN entries for the container instance on
    # which you would like to update the Amazon ECS container agent.
    container_instance: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that your
    # container instance is running on. If you do not specify a cluster, the
    # default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateContainerAgentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_instance",
                "containerInstance",
                TypeInfo(ContainerInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The container instance for which the container agent was updated.
    container_instance: "ContainerInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateContainerInstancesStateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_instances",
                "containerInstances",
                TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ContainerInstanceStatus]),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
        ]

    # A list of container instance IDs or full ARN entries.
    container_instances: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The container instance state with which to update the container instance.
    status: typing.Union[str, "ContainerInstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name or full Amazon Resource Name (ARN) of the cluster that hosts
    # the container instance to update. If you do not specify a cluster, the
    # default cluster is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateContainerInstancesStateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_instances",
                "containerInstances",
                TypeInfo(typing.List[ContainerInstance]),
            ),
            (
                "failures",
                "failures",
                TypeInfo(typing.List[Failure]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of container instances.
    container_instances: typing.List["ContainerInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any failures associated with the call.
    failures: typing.List["Failure"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateInProgressException(ShapeBase):
    """
    There is already a current Amazon ECS container agent update in progress on the
    specified container instance. If the container agent becomes disconnected while
    it is in a transitional stage, such as `PENDING` or `STAGING`, the update
    process can get stuck in that state. However, when the agent reconnects, it
    resumes where it stopped previously.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateServiceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service",
                "service",
                TypeInfo(str),
            ),
            (
                "cluster",
                "cluster",
                TypeInfo(str),
            ),
            (
                "desired_count",
                "desiredCount",
                TypeInfo(int),
            ),
            (
                "task_definition",
                "taskDefinition",
                TypeInfo(str),
            ),
            (
                "deployment_configuration",
                "deploymentConfiguration",
                TypeInfo(DeploymentConfiguration),
            ),
            (
                "network_configuration",
                "networkConfiguration",
                TypeInfo(NetworkConfiguration),
            ),
            (
                "platform_version",
                "platformVersion",
                TypeInfo(str),
            ),
            (
                "force_new_deployment",
                "forceNewDeployment",
                TypeInfo(bool),
            ),
            (
                "health_check_grace_period_seconds",
                "healthCheckGracePeriodSeconds",
                TypeInfo(int),
            ),
        ]

    # The name of the service to update.
    service: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name or full Amazon Resource Name (ARN) of the cluster that your
    # service is running on. If you do not specify a cluster, the default cluster
    # is assumed.
    cluster: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instantiations of the task to place and keep running in your
    # service.
    desired_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `family` and `revision` (`family:revision`) or full ARN of the task
    # definition to run in your service. If a `revision` is not specified, the
    # latest `ACTIVE` revision is used. If you modify the task definition with
    # `UpdateService`, Amazon ECS spawns a task with the new version of the task
    # definition and then stops an old task after the new version is running.
    task_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional deployment parameters that control how many tasks run during the
    # deployment and the ordering of stopping and starting tasks.
    deployment_configuration: "DeploymentConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The network configuration for the service. This parameter is required for
    # task definitions that use the `awsvpc` network mode to receive their own
    # elastic network interface, and it is not supported for other network modes.
    # For more information, see [Task
    # Networking](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-
    # networking.html) in the _Amazon Elastic Container Service Developer Guide_.

    # Updating a service to add a subnet to a list of existing subnets does not
    # trigger a service deployment. For example, if your network configuration
    # change is to keep the existing subnets and simply add another subnet to the
    # network configuration, this does not trigger a new service deployment.
    network_configuration: "NetworkConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform version that your service should run.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to force a new deployment of the service. Deployments are not
    # forced by default. You can use this option to trigger a new deployment with
    # no service definition changes. For example, you can update a service's
    # tasks to use a newer Docker image with the same image/tag combination
    # (`my_image:latest`) or to roll Fargate tasks onto a newer platform version.
    force_new_deployment: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The period of time, in seconds, that the Amazon ECS service scheduler
    # should ignore unhealthy Elastic Load Balancing target health checks after a
    # task has first started. This is only valid if your service is configured to
    # use a load balancer. If your service's tasks take a while to start and
    # respond to Elastic Load Balancing health checks, you can specify a health
    # check grace period of up to 1,800 seconds during which the ECS service
    # scheduler ignores the Elastic Load Balancing health check status. This
    # grace period can prevent the ECS service scheduler from marking tasks as
    # unhealthy and stopping them before they have time to come up.
    health_check_grace_period_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateServiceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "service",
                "service",
                TypeInfo(Service),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full description of your service following the update call.
    service: "Service" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VersionInfo(ShapeBase):
    """
    The Docker and Amazon ECS container agent version information about a container
    instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "agent_version",
                "agentVersion",
                TypeInfo(str),
            ),
            (
                "agent_hash",
                "agentHash",
                TypeInfo(str),
            ),
            (
                "docker_version",
                "dockerVersion",
                TypeInfo(str),
            ),
        ]

    # The version number of the Amazon ECS container agent.
    agent_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Git commit hash for the Amazon ECS container agent build on the
    # [amazon-ecs-agent ](https://github.com/aws/amazon-ecs-agent/commits/master)
    # GitHub repository.
    agent_hash: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Docker version running on the container instance.
    docker_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Volume(ShapeBase):
    """
    A data volume used in a task definition. For tasks that use a Docker volume,
    specify a `DockerVolumeConfiguration`. For tasks that use a bind mount host
    volume, specify a `host` and optional `sourcePath`. For more information, see
    [Using Data Volumes in
    Tasks](http://docs.aws.amazon.com/AmazonECS/latest/developerguideusing_data_volumes.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "host",
                "host",
                TypeInfo(HostVolumeProperties),
            ),
            (
                "docker_volume_configuration",
                "dockerVolumeConfiguration",
                TypeInfo(DockerVolumeConfiguration),
            ),
        ]

    # The name of the volume. Up to 255 letters (uppercase and lowercase),
    # numbers, hyphens, and underscores are allowed. This name is referenced in
    # the `sourceVolume` parameter of container definition `mountPoints`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is specified when using bind mount host volumes. Bind mount
    # host volumes are supported when using either the EC2 or Fargate launch
    # types. The contents of the `host` parameter determine whether your bind
    # mount host volume persists on the host container instance and where it is
    # stored. If the `host` parameter is empty, then the Docker daemon assigns a
    # host path for your data volume, but the data is not guaranteed to persist
    # after the containers associated with it stop running.

    # Windows containers can mount whole directories on the same drive as
    # `$env:ProgramData`. Windows containers cannot mount directories on a
    # different drive, and mount point cannot be across drives. For example, you
    # can mount `C:\my\path:C:\my\path` and `D:\:D:\`, but not
    # `D:\my\path:C:\my\path` or `D:\:C:\my\path`.
    host: "HostVolumeProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration for the Docker volume. This parameter is specified when
    # using Docker volumes.
    docker_volume_configuration: "DockerVolumeConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VolumeFrom(ShapeBase):
    """
    Details on a data volume from another container in the same task definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_container",
                "sourceContainer",
                TypeInfo(str),
            ),
            (
                "read_only",
                "readOnly",
                TypeInfo(bool),
            ),
        ]

    # The name of another container within the same task definition to mount
    # volumes from.
    source_container: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this value is `true`, the container has read-only access to the volume.
    # If this value is `false`, then the container can write to the volume. The
    # default value is `false`.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )
