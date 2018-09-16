import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class ArrayJobDependency(str):
    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


@dataclasses.dataclass
class ArrayProperties(ShapeBase):
    """
    An object representing an AWS Batch array job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "size",
                TypeInfo(int),
            ),
        ]

    # The size of the array job.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ArrayPropertiesDetail(ShapeBase):
    """
    An object representing the array properties of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status_summary",
                "statusSummary",
                TypeInfo(typing.Dict[str, int]),
            ),
            (
                "size",
                "size",
                TypeInfo(int),
            ),
            (
                "index",
                "index",
                TypeInfo(int),
            ),
        ]

    # A summary of the number of array job children in each available job status.
    # This parameter is returned for parent array jobs.
    status_summary: typing.Dict[str, int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the array job. This parameter is returned for parent array
    # jobs.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job index within the array that is associated with this job. This
    # parameter is returned for array job children.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ArrayPropertiesSummary(ShapeBase):
    """
    An object representing the array properties of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "size",
                "size",
                TypeInfo(int),
            ),
            (
                "index",
                "index",
                TypeInfo(int),
            ),
        ]

    # The size of the array job. This parameter is returned for parent array
    # jobs.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job index within the array that is associated with this job. This
    # parameter is returned for children of array jobs.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttemptContainerDetail(ShapeBase):
    """
    An object representing the details of a container that is part of a job attempt.
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
                "task_arn",
                "taskArn",
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
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon ECS container instance that
    # hosts the job attempt.
    container_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon ECS task that is associated
    # with the job attempt. Each container attempt receives a task ARN when they
    # reach the `STARTING` status.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The exit code for the job attempt. A non-zero exit code is considered a
    # failure.
    exit_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short (255 max characters) human-readable string to provide additional
    # details about a running or stopped container.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the CloudWatch Logs log stream associated with the container.
    # The log group for AWS Batch jobs is `/aws/batch/job`. Each container
    # attempt receives a log stream name when they reach the `RUNNING` status.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttemptDetail(ShapeBase):
    """
    An object representing a job attempt.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container",
                "container",
                TypeInfo(AttemptContainerDetail),
            ),
            (
                "started_at",
                "startedAt",
                TypeInfo(int),
            ),
            (
                "stopped_at",
                "stoppedAt",
                TypeInfo(int),
            ),
            (
                "status_reason",
                "statusReason",
                TypeInfo(str),
            ),
        ]

    # Details about the container in this job attempt.
    container: "AttemptContainerDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp (in seconds and milliseconds) for when the attempt was
    # started (when the attempt transitioned from the `STARTING` state to the
    # `RUNNING` state).
    started_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp (in seconds and milliseconds) for when the attempt was
    # stopped (when the attempt transitioned from the `RUNNING` state to a
    # terminal state, such as `SUCCEEDED` or `FAILED`).
    stopped_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short, human-readable string to provide additional details about the
    # current status of the job attempt.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CEState(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEStatus(str):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class CEType(str):
    MANAGED = "MANAGED"
    UNMANAGED = "UNMANAGED"


class CRType(str):
    EC2 = "EC2"
    SPOT = "SPOT"


@dataclasses.dataclass
class CancelJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
        ]

    # The AWS Batch job ID of the job to cancel.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message to attach to the job that explains the reason for canceling it.
    # This message is returned by future DescribeJobs operations on the job. This
    # message is also recorded in the AWS Batch activity logs.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


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
class ComputeEnvironmentDetail(ShapeBase):
    """
    An object representing an AWS Batch compute environment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_environment_name",
                "computeEnvironmentName",
                TypeInfo(str),
            ),
            (
                "compute_environment_arn",
                "computeEnvironmentArn",
                TypeInfo(str),
            ),
            (
                "ecs_cluster_arn",
                "ecsClusterArn",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, CEType]),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, CEState]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, CEStatus]),
            ),
            (
                "status_reason",
                "statusReason",
                TypeInfo(str),
            ),
            (
                "compute_resources",
                "computeResources",
                TypeInfo(ComputeResource),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
        ]

    # The name of the compute environment.
    compute_environment_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the compute environment.
    compute_environment_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by
    # the compute environment.
    ecs_cluster_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the compute environment.
    type: typing.Union[str, "CEType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the compute environment. The valid values are `ENABLED` or
    # `DISABLED`. An `ENABLED` state indicates that you can register instances
    # with the compute environment and that the associated instances can accept
    # jobs.
    state: typing.Union[str, "CEState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the compute environment (for example, `CREATING` or
    # `VALID`).
    status: typing.Union[str, "CEStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A short, human-readable string to provide additional details about the
    # current status of the compute environment.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute resources defined for the compute environment.
    compute_resources: "ComputeResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The service role associated with the compute environment that allows AWS
    # Batch to make calls to AWS API operations on your behalf.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComputeEnvironmentOrder(ShapeBase):
    """
    The order in which compute environments are tried for job placement within a
    queue. Compute environments are tried in ascending order. For example, if two
    compute environments are associated with a job queue, the compute environment
    with a lower order integer value is tried for job placement first.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "order",
                "order",
                TypeInfo(int),
            ),
            (
                "compute_environment",
                "computeEnvironment",
                TypeInfo(str),
            ),
        ]

    # The order of the compute environment.
    order: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the compute environment.
    compute_environment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComputeResource(ShapeBase):
    """
    An object representing an AWS Batch compute resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, CRType]),
            ),
            (
                "minv_cpus",
                "minvCpus",
                TypeInfo(int),
            ),
            (
                "maxv_cpus",
                "maxvCpus",
                TypeInfo(int),
            ),
            (
                "instance_types",
                "instanceTypes",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "subnets",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_ids",
                "securityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "instance_role",
                "instanceRole",
                TypeInfo(str),
            ),
            (
                "desiredv_cpus",
                "desiredvCpus",
                TypeInfo(int),
            ),
            (
                "image_id",
                "imageId",
                TypeInfo(str),
            ),
            (
                "ec2_key_pair",
                "ec2KeyPair",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bid_percentage",
                "bidPercentage",
                TypeInfo(int),
            ),
            (
                "spot_iam_fleet_role",
                "spotIamFleetRole",
                TypeInfo(str),
            ),
        ]

    # The type of compute environment.
    type: typing.Union[str, "CRType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum number of EC2 vCPUs that an environment should maintain.
    minv_cpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of EC2 vCPUs that an environment can reach.
    maxv_cpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instances types that may be launched. You can specify instance families
    # to launch any instance type within those families (for example, `c4` or
    # `p3`), or you can specify specific sizes within a family (such as
    # `c4.8xlarge`). You can also choose `optimal` to pick instance types (from
    # the latest C, M, and R instance families) on the fly that match the demand
    # of your job queues.
    instance_types: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VPC subnets into which the compute resources are launched.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 security group that is associated with instances launched in the
    # compute environment.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon ECS instance profile applied to Amazon EC2 instances in a
    # compute environment. You can specify the short name or full Amazon Resource
    # Name (ARN) of an instance profile. For example, `ecsInstanceRole` or
    # `arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole`. For more
    # information, see [Amazon ECS Instance
    # Role](http://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html)
    # in the _AWS Batch User Guide_.
    instance_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired number of EC2 vCPUS in the compute environment.
    desiredv_cpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Machine Image (AMI) ID used for instances launched in the
    # compute environment.
    image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The EC2 key pair that is used for instances launched in the compute
    # environment.
    ec2_key_pair: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key-value pair tags to be applied to resources that are launched in the
    # compute environment.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum percentage that a Spot Instance price must be when compared
    # with the On-Demand price for that instance type before instances are
    # launched. For example, if your bid percentage is 20%, then the Spot price
    # must be below 20% of the current On-Demand price for that EC2 instance.
    bid_percentage: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role
    # applied to a `SPOT` compute environment.
    spot_iam_fleet_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComputeResourceUpdate(ShapeBase):
    """
    An object representing the attributes of a compute environment that can be
    updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minv_cpus",
                "minvCpus",
                TypeInfo(int),
            ),
            (
                "maxv_cpus",
                "maxvCpus",
                TypeInfo(int),
            ),
            (
                "desiredv_cpus",
                "desiredvCpus",
                TypeInfo(int),
            ),
        ]

    # The minimum number of EC2 vCPUs that an environment should maintain.
    minv_cpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of EC2 vCPUs that an environment can reach.
    maxv_cpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired number of EC2 vCPUS in the compute environment.
    desiredv_cpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContainerDetail(ShapeBase):
    """
    An object representing the details of a container that is part of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "image",
                TypeInfo(str),
            ),
            (
                "vcpus",
                "vcpus",
                TypeInfo(int),
            ),
            (
                "memory",
                "memory",
                TypeInfo(int),
            ),
            (
                "command",
                "command",
                TypeInfo(typing.List[str]),
            ),
            (
                "job_role_arn",
                "jobRoleArn",
                TypeInfo(str),
            ),
            (
                "volumes",
                "volumes",
                TypeInfo(typing.List[Volume]),
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
                "readonly_root_filesystem",
                "readonlyRootFilesystem",
                TypeInfo(bool),
            ),
            (
                "ulimits",
                "ulimits",
                TypeInfo(typing.List[Ulimit]),
            ),
            (
                "privileged",
                "privileged",
                TypeInfo(bool),
            ),
            (
                "user",
                "user",
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
                "container_instance_arn",
                "containerInstanceArn",
                TypeInfo(str),
            ),
            (
                "task_arn",
                "taskArn",
                TypeInfo(str),
            ),
            (
                "log_stream_name",
                "logStreamName",
                TypeInfo(str),
            ),
        ]

    # The image used to start the container.
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of VCPUs allocated for the job.
    vcpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of MiB of memory reserved for the job.
    memory: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The command that is passed to the container.
    command: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) associated with the job upon execution.
    job_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of volumes associated with the job.
    volumes: typing.List["Volume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The environment variables to pass to a container.

    # Environment variables must not start with `AWS_BATCH`; this naming
    # convention is reserved for variables that are set by the AWS Batch service.
    environment: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The mount points for data volumes in your container.
    mount_points: typing.List["MountPoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When this parameter is true, the container is given read-only access to its
    # root file system.
    readonly_root_filesystem: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of `ulimit` values to set in the container.
    ulimits: typing.List["Ulimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When this parameter is true, the container is given elevated privileges on
    # the host container instance (similar to the `root` user).
    privileged: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name to use inside the container.
    user: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The exit code to return upon completion.
    exit_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short (255 max characters) human-readable string to provide additional
    # details about a running or stopped container.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the container instance on which the
    # container is running.
    container_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon ECS task that is associated
    # with the container job. Each container attempt receives a task ARN when
    # they reach the `STARTING` status.
    task_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the CloudWatch Logs log stream associated with the container.
    # The log group for AWS Batch jobs is `/aws/batch/job`. Each container
    # attempt receives a log stream name when they reach the `RUNNING` status.
    log_stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContainerOverrides(ShapeBase):
    """
    The overrides that should be sent to a container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vcpus",
                "vcpus",
                TypeInfo(int),
            ),
            (
                "memory",
                "memory",
                TypeInfo(int),
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
        ]

    # The number of vCPUs to reserve for the container. This value overrides the
    # value set in the job definition.
    vcpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of MiB of memory reserved for the job. This value overrides the
    # value set in the job definition.
    memory: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The command to send to the container that overrides the default command
    # from the Docker image or the job definition.
    command: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The environment variables to send to the container. You can add new
    # environment variables, which are added to the container at launch, or you
    # can override the existing environment variables from the Docker image or
    # the job definition.

    # Environment variables must not start with `AWS_BATCH`; this naming
    # convention is reserved for variables that are set by the AWS Batch service.
    environment: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContainerProperties(ShapeBase):
    """
    Container properties are used in job definitions to describe the container that
    is launched as part of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "image",
                TypeInfo(str),
            ),
            (
                "vcpus",
                "vcpus",
                TypeInfo(int),
            ),
            (
                "memory",
                "memory",
                TypeInfo(int),
            ),
            (
                "command",
                "command",
                TypeInfo(typing.List[str]),
            ),
            (
                "job_role_arn",
                "jobRoleArn",
                TypeInfo(str),
            ),
            (
                "volumes",
                "volumes",
                TypeInfo(typing.List[Volume]),
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
                "readonly_root_filesystem",
                "readonlyRootFilesystem",
                TypeInfo(bool),
            ),
            (
                "privileged",
                "privileged",
                TypeInfo(bool),
            ),
            (
                "ulimits",
                "ulimits",
                TypeInfo(typing.List[Ulimit]),
            ),
            (
                "user",
                "user",
                TypeInfo(str),
            ),
        ]

    # The image used to start a container. This string is passed directly to the
    # Docker daemon. Images in the Docker Hub registry are available by default.
    # Other repositories are specified with ` _repository-url_ / _image_ : _tag_
    # `. Up to 255 letters (uppercase and lowercase), numbers, hyphens,
    # underscores, colons, periods, forward slashes, and number signs are
    # allowed. This parameter maps to `Image` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `IMAGE` parameter of [docker
    # run](https://docs.docker.com/engine/reference/run/).

    #   * Images in Amazon ECR repositories use the full registry and repository URI (for example, `012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`).

    #   * Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo`).

    #   * Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent`).

    #   * Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu`).
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of vCPUs reserved for the container. This parameter maps to
    # `CpuShares` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--cpu-shares` option to [docker
    # run](https://docs.docker.com/engine/reference/run/). Each vCPU is
    # equivalent to 1,024 CPU shares. You must specify at least one vCPU.
    vcpus: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The hard limit (in MiB) of memory to present to the container. If your
    # container attempts to exceed the memory specified here, the container is
    # killed. This parameter maps to `Memory` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--memory` option to [docker
    # run](https://docs.docker.com/engine/reference/run/). You must specify at
    # least 4 MiB of memory for a job.

    # If you are trying to maximize your resource utilization by providing your
    # jobs as much memory as possible for a particular instance type, see [Memory
    # Management](http://docs.aws.amazon.com/batch/latest/userguide/memory-
    # management.html) in the _AWS Batch User Guide_.
    memory: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The command that is passed to the container. This parameter maps to `Cmd`
    # in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `COMMAND` parameter to [docker
    # run](https://docs.docker.com/engine/reference/run/). For more information,
    # see <https://docs.docker.com/engine/reference/builder/#cmd>.
    command: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the IAM role that the container can
    # assume for AWS permissions.
    job_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of data volumes used in a job.
    volumes: typing.List["Volume"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The environment variables to pass to a container. This parameter maps to
    # `Env` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--env` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).

    # We do not recommend using plaintext environment variables for sensitive
    # information, such as credential data.

    # Environment variables must not start with `AWS_BATCH`; this naming
    # convention is reserved for variables that are set by the AWS Batch service.
    environment: typing.List["KeyValuePair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The mount points for data volumes in your container. This parameter maps to
    # `Volumes` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--volume` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).
    mount_points: typing.List["MountPoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When this parameter is true, the container is given read-only access to its
    # root file system. This parameter maps to `ReadonlyRootfs` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--read-only` option to `docker run`.
    readonly_root_filesystem: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When this parameter is true, the container is given elevated privileges on
    # the host container instance (similar to the `root` user). This parameter
    # maps to `Privileged` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--privileged` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).
    privileged: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of `ulimits` to set in the container. This parameter maps to
    # `Ulimits` in the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--ulimit` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).
    ulimits: typing.List["Ulimit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The user name to use inside the container. This parameter maps to `User` in
    # the [Create a
    # container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-
    # a-container) section of the [Docker Remote
    # API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/)
    # and the `--user` option to [docker
    # run](https://docs.docker.com/engine/reference/run/).
    user: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContainerSummary(ShapeBase):
    """
    An object representing summary details of a container within a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
        ]

    # The exit code to return upon completion.
    exit_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A short (255 max characters) human-readable string to provide additional
    # details about a running or stopped container.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateComputeEnvironmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_environment_name",
                "computeEnvironmentName",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, CEType]),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, CEState]),
            ),
            (
                "compute_resources",
                "computeResources",
                TypeInfo(ComputeResource),
            ),
        ]

    # The name for your compute environment. Up to 128 letters (uppercase and
    # lowercase), numbers, hyphens, and underscores are allowed.
    compute_environment_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of the compute environment.
    type: typing.Union[str, "CEType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch
    # to make calls to other AWS services on your behalf.

    # If your specified role has a path other than `/`, then you must either
    # specify the full role ARN (this is recommended) or prefix the role name
    # with the path.

    # Depending on how you created your AWS Batch service role, its ARN may
    # contain the `service-role` path prefix. When you only specify the name of
    # the service role, AWS Batch assumes that your ARN does not use the
    # `service-role` path prefix. Because of this, we recommend that you specify
    # the full ARN of your service role when you create compute environments.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the compute environment. If the state is `ENABLED`, then the
    # compute environment accepts jobs from a queue and can scale out
    # automatically based on queues.
    state: typing.Union[str, "CEState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details of the compute resources managed by the compute environment. This
    # parameter is required for managed compute environments.
    compute_resources: "ComputeResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateComputeEnvironmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compute_environment_name",
                "computeEnvironmentName",
                TypeInfo(str),
            ),
            (
                "compute_environment_arn",
                "computeEnvironmentArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the compute environment.
    compute_environment_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the compute environment.
    compute_environment_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateJobQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_queue_name",
                "jobQueueName",
                TypeInfo(str),
            ),
            (
                "priority",
                "priority",
                TypeInfo(int),
            ),
            (
                "compute_environment_order",
                "computeEnvironmentOrder",
                TypeInfo(typing.List[ComputeEnvironmentOrder]),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, JQState]),
            ),
        ]

    # The name of the job queue.
    job_queue_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The priority of the job queue. Job queues with a higher priority (or a
    # higher integer value for the `priority` parameter) are evaluated first when
    # associated with same compute environment. Priority is determined in
    # descending order, for example, a job queue with a priority value of `10` is
    # given scheduling preference over a job queue with a priority value of `1`.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The set of compute environments mapped to a job queue and their order
    # relative to each other. The job scheduler uses this parameter to determine
    # which compute environment should execute a given job. Compute environments
    # must be in the `VALID` state before you can associate them with a job
    # queue. You can associate up to three compute environments with a job queue.
    compute_environment_order: typing.List["ComputeEnvironmentOrder"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The state of the job queue. If the job queue state is `ENABLED`, it is able
    # to accept jobs.
    state: typing.Union[str, "JQState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateJobQueueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_queue_name",
                "jobQueueName",
                TypeInfo(str),
            ),
            (
                "job_queue_arn",
                "jobQueueArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the job queue.
    job_queue_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the job queue.
    job_queue_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteComputeEnvironmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_environment",
                "computeEnvironment",
                TypeInfo(str),
            ),
        ]

    # The name or Amazon Resource Name (ARN) of the compute environment to
    # delete.
    compute_environment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteComputeEnvironmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteJobQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_queue",
                "jobQueue",
                TypeInfo(str),
            ),
        ]

    # The short name or full Amazon Resource Name (ARN) of the queue to delete.
    job_queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteJobQueueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeregisterJobDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_definition",
                "jobDefinition",
                TypeInfo(str),
            ),
        ]

    # The name and revision (`name:revision`) or full Amazon Resource Name (ARN)
    # of the job definition to deregister.
    job_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterJobDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeComputeEnvironmentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_environments",
                "computeEnvironments",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # A list of up to 100 compute environment names or full Amazon Resource Name
    # (ARN) entries.
    compute_environments: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of cluster results returned by
    # `DescribeComputeEnvironments` in paginated output. When this parameter is
    # used, `DescribeComputeEnvironments` only returns `maxResults` results in a
    # single page along with a `nextToken` response element. The remaining
    # results of the initial request can be seen by sending another
    # `DescribeComputeEnvironments` request with the returned `nextToken` value.
    # This value can be between 1 and 100. If this parameter is not used, then
    # `DescribeComputeEnvironments` returns up to 100 results and a `nextToken`
    # value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated
    # `DescribeComputeEnvironments` request where `maxResults` was used and the
    # results exceeded the value of that parameter. Pagination continues from the
    # end of the previous results that returned the `nextToken` value. This value
    # is `null` when there are no more results to return.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeComputeEnvironmentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compute_environments",
                "computeEnvironments",
                TypeInfo(typing.List[ComputeEnvironmentDetail]),
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

    # The list of compute environments.
    compute_environments: typing.List["ComputeEnvironmentDetail"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The `nextToken` value to include in a future `DescribeComputeEnvironments`
    # request. When the results of a `DescribeJobDefinitions` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_definitions",
                "jobDefinitions",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "job_definition_name",
                "jobDefinitionName",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # A space-separated list of up to 100 job definition names or full Amazon
    # Resource Name (ARN) entries.
    job_definitions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of results returned by `DescribeJobDefinitions` in
    # paginated output. When this parameter is used, `DescribeJobDefinitions`
    # only returns `maxResults` results in a single page along with a `nextToken`
    # response element. The remaining results of the initial request can be seen
    # by sending another `DescribeJobDefinitions` request with the returned
    # `nextToken` value. This value can be between 1 and 100. If this parameter
    # is not used, then `DescribeJobDefinitions` returns up to 100 results and a
    # `nextToken` value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the job definition to describe.
    job_definition_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status with which to filter job definitions.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated
    # `DescribeJobDefinitions` request where `maxResults` was used and the
    # results exceeded the value of that parameter. Pagination continues from the
    # end of the previous results that returned the `nextToken` value. This value
    # is `null` when there are no more results to return.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_definitions",
                "jobDefinitions",
                TypeInfo(typing.List[JobDefinition]),
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

    # The list of job definitions.
    job_definitions: typing.List["JobDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `DescribeJobDefinitions`
    # request. When the results of a `DescribeJobDefinitions` request exceed
    # `maxResults`, this value can be used to retrieve the next page of results.
    # This value is `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobQueuesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_queues",
                "jobQueues",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # A list of up to 100 queue names or full queue Amazon Resource Name (ARN)
    # entries.
    job_queues: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of results returned by `DescribeJobQueues` in paginated
    # output. When this parameter is used, `DescribeJobQueues` only returns
    # `maxResults` results in a single page along with a `nextToken` response
    # element. The remaining results of the initial request can be seen by
    # sending another `DescribeJobQueues` request with the returned `nextToken`
    # value. This value can be between 1 and 100. If this parameter is not used,
    # then `DescribeJobQueues` returns up to 100 results and a `nextToken` value
    # if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated
    # `DescribeJobQueues` request where `maxResults` was used and the results
    # exceeded the value of that parameter. Pagination continues from the end of
    # the previous results that returned the `nextToken` value. This value is
    # `null` when there are no more results to return.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobQueuesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_queues",
                "jobQueues",
                TypeInfo(typing.List[JobQueueDetail]),
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

    # The list of job queues.
    job_queues: typing.List["JobQueueDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `DescribeJobQueues` request.
    # When the results of a `DescribeJobQueues` request exceed `maxResults`, this
    # value can be used to retrieve the next page of results. This value is
    # `null` when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "jobs",
                "jobs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A space-separated list of up to 100 job IDs.
    jobs: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "jobs",
                "jobs",
                TypeInfo(typing.List[JobDetail]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of jobs.
    jobs: typing.List["JobDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Host(ShapeBase):
    """
    The contents of the `host` parameter determine whether your data volume persists
    on the host container instance and where it is stored. If the host parameter is
    empty, then the Docker daemon assigns a host path for your data volume, but the
    data is not guaranteed to persist after the containers associated with it stop
    running.
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

    # The path on the host container instance that is presented to the container.
    # If this parameter is empty, then the Docker daemon has assigned a host path
    # for you. If the `host` parameter contains a `sourcePath` file location,
    # then the data volume persists at the specified location on the host
    # container instance until you delete it manually. If the `sourcePath` value
    # does not exist on the host container instance, the Docker daemon creates
    # it. If the location does exist, the contents of the source path folder are
    # exported.
    source_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class JQState(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class JQStatus(str):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


@dataclasses.dataclass
class JobDefinition(ShapeBase):
    """
    An object representing an AWS Batch job definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_definition_name",
                "jobDefinitionName",
                TypeInfo(str),
            ),
            (
                "job_definition_arn",
                "jobDefinitionArn",
                TypeInfo(str),
            ),
            (
                "revision",
                "revision",
                TypeInfo(int),
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
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "retry_strategy",
                "retryStrategy",
                TypeInfo(RetryStrategy),
            ),
            (
                "container_properties",
                "containerProperties",
                TypeInfo(ContainerProperties),
            ),
            (
                "timeout",
                "timeout",
                TypeInfo(JobTimeout),
            ),
        ]

    # The name of the job definition.
    job_definition_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the job definition.
    job_definition_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The revision of the job definition.
    revision: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of job definition.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job definition.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default parameters or parameter substitution placeholders that are set in
    # the job definition. Parameters are specified as a key-value pair mapping.
    # Parameters in a `SubmitJob` request override any corresponding parameter
    # defaults from the job definition.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry strategy to use for failed jobs that are submitted with this job
    # definition.
    retry_strategy: "RetryStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object with various properties specific to container-based jobs.
    container_properties: "ContainerProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeout configuration for jobs that are submitted with this job
    # definition. You can specify a timeout duration after which AWS Batch
    # terminates your jobs if they have not finished.
    timeout: "JobTimeout" = dataclasses.field(default=ShapeBase.NOT_SET, )


class JobDefinitionType(str):
    container = "container"


@dataclasses.dataclass
class JobDependency(ShapeBase):
    """
    An object representing an AWS Batch job dependency.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ArrayJobDependency]),
            ),
        ]

    # The job ID of the AWS Batch job associated with this dependency.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the job dependency.
    type: typing.Union[str, "ArrayJobDependency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JobDetail(ShapeBase):
    """
    An object representing an AWS Batch job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "jobName",
                TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
            (
                "job_queue",
                "jobQueue",
                TypeInfo(str),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "started_at",
                "startedAt",
                TypeInfo(int),
            ),
            (
                "job_definition",
                "jobDefinition",
                TypeInfo(str),
            ),
            (
                "attempts",
                "attempts",
                TypeInfo(typing.List[AttemptDetail]),
            ),
            (
                "status_reason",
                "statusReason",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(int),
            ),
            (
                "retry_strategy",
                "retryStrategy",
                TypeInfo(RetryStrategy),
            ),
            (
                "stopped_at",
                "stoppedAt",
                TypeInfo(int),
            ),
            (
                "depends_on",
                "dependsOn",
                TypeInfo(typing.List[JobDependency]),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container",
                "container",
                TypeInfo(ContainerDetail),
            ),
            (
                "array_properties",
                "arrayProperties",
                TypeInfo(ArrayPropertiesDetail),
            ),
            (
                "timeout",
                "timeout",
                TypeInfo(JobTimeout),
            ),
        ]

    # The name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for the job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the job queue with which the job is
    # associated.
    job_queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status for the job.
    status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp (in seconds and milliseconds) for when the job was
    # started (when the job transitioned from the `STARTING` state to the
    # `RUNNING` state).
    started_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job definition that is used by this job.
    job_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of job attempts associated with this job.
    attempts: typing.List["AttemptDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A short, human-readable string to provide additional details about the
    # current status of the job.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp (in seconds and milliseconds) for when the job was
    # created. For non-array jobs and parent array jobs, this is when the job
    # entered the `SUBMITTED` state (at the time SubmitJob was called). For array
    # child jobs, this is when the child job was spawned by its parent and
    # entered the `PENDING` state.
    created_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The retry strategy to use for this job if an attempt fails.
    retry_strategy: "RetryStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unix time stamp (in seconds and milliseconds) for when the job was
    # stopped (when the job transitioned from the `RUNNING` state to a terminal
    # state, such as `SUCCEEDED` or `FAILED`).
    stopped_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of job names or IDs on which this job depends.
    depends_on: typing.List["JobDependency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional parameters passed to the job that replace parameter substitution
    # placeholders or override any corresponding parameter defaults from the job
    # definition.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object representing the details of the container that is associated with
    # the job.
    container: "ContainerDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The array properties of the job, if it is an array job.
    array_properties: "ArrayPropertiesDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeout configuration for the job.
    timeout: "JobTimeout" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class JobQueueDetail(ShapeBase):
    """
    An object representing the details of an AWS Batch job queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_queue_name",
                "jobQueueName",
                TypeInfo(str),
            ),
            (
                "job_queue_arn",
                "jobQueueArn",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, JQState]),
            ),
            (
                "priority",
                "priority",
                TypeInfo(int),
            ),
            (
                "compute_environment_order",
                "computeEnvironmentOrder",
                TypeInfo(typing.List[ComputeEnvironmentOrder]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, JQStatus]),
            ),
            (
                "status_reason",
                "statusReason",
                TypeInfo(str),
            ),
        ]

    # The name of the job queue.
    job_queue_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the job queue.
    job_queue_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the ability of the queue to accept new jobs.
    state: typing.Union[str, "JQState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The priority of the job queue.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The compute environments that are attached to the job queue and the order
    # in which job placement is preferred. Compute environments are selected for
    # job placement in ascending order.
    compute_environment_order: typing.List["ComputeEnvironmentOrder"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The status of the job queue (for example, `CREATING` or `VALID`).
    status: typing.Union[str, "JQStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A short, human-readable string to provide additional details about the
    # current status of the job queue.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class JobStatus(str):
    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    RUNNABLE = "RUNNABLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class JobSummary(ShapeBase):
    """
    An object representing summary details of a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
            (
                "job_name",
                "jobName",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(int),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "status_reason",
                "statusReason",
                TypeInfo(str),
            ),
            (
                "started_at",
                "startedAt",
                TypeInfo(int),
            ),
            (
                "stopped_at",
                "stoppedAt",
                TypeInfo(int),
            ),
            (
                "container",
                "container",
                TypeInfo(ContainerSummary),
            ),
            (
                "array_properties",
                "arrayProperties",
                TypeInfo(ArrayPropertiesSummary),
            ),
        ]

    # The ID of the job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp for when the job was created. For non-array jobs and
    # parent array jobs, this is when the job entered the `SUBMITTED` state (at
    # the time SubmitJob was called). For array child jobs, this is when the
    # child job was spawned by its parent and entered the `PENDING` state.
    created_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status for the job.
    status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A short, human-readable string to provide additional details about the
    # current status of the job.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp for when the job was started (when the job transitioned
    # from the `STARTING` state to the `RUNNING` state).
    started_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Unix time stamp for when the job was stopped (when the job transitioned
    # from the `RUNNING` state to a terminal state, such as `SUCCEEDED` or
    # `FAILED`).
    stopped_at: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object representing the details of the container that is associated with
    # the job.
    container: "ContainerSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The array properties of the job, if it is an array job.
    array_properties: "ArrayPropertiesSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JobTimeout(ShapeBase):
    """
    An object representing a job timeout configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attempt_duration_seconds",
                "attemptDurationSeconds",
                TypeInfo(int),
            ),
        ]

    # The time duration in seconds (measured from the job attempt's `startedAt`
    # timestamp) after which AWS Batch terminates your jobs if they have not
    # finished.
    attempt_duration_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class KeyValuePair(ShapeBase):
    """
    A key-value pair object.
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

    # The name of the key-value pair. For environment variables, this is the name
    # of the environment variable.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the key-value pair. For environment variables, this is the
    # value of the environment variable.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_queue",
                "jobQueue",
                TypeInfo(str),
            ),
            (
                "array_job_id",
                "arrayJobId",
                TypeInfo(str),
            ),
            (
                "job_status",
                "jobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The name or full Amazon Resource Name (ARN) of the job queue with which to
    # list jobs.
    job_queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job ID for an array job. Specifying an array job ID with this parameter
    # lists all child jobs from within the specified array.
    array_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job status with which to filter jobs in the specified queue. If you do
    # not specify a status, only `RUNNING` jobs are returned.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of results returned by `ListJobs` in paginated output.
    # When this parameter is used, `ListJobs` only returns `maxResults` results
    # in a single page along with a `nextToken` response element. The remaining
    # results of the initial request can be seen by sending another `ListJobs`
    # request with the returned `nextToken` value. This value can be between 1
    # and 100. If this parameter is not used, then `ListJobs` returns up to 100
    # results and a `nextToken` value if applicable.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `nextToken` value returned from a previous paginated `ListJobs` request
    # where `maxResults` was used and the results exceeded the value of that
    # parameter. Pagination continues from the end of the previous results that
    # returned the `nextToken` value. This value is `null` when there are no more
    # results to return.

    # This token should be treated as an opaque identifier that is only used to
    # retrieve the next items in a list and not for other programmatic purposes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_summary_list",
                "jobSummaryList",
                TypeInfo(typing.List[JobSummary]),
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

    # A list of job summaries that match the request.
    job_summary_list: typing.List["JobSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `nextToken` value to include in a future `ListJobs` request. When the
    # results of a `ListJobs` request exceed `maxResults`, this value can be used
    # to retrieve the next page of results. This value is `null` when there are
    # no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MountPoint(ShapeBase):
    """
    Details on a Docker volume mount point that is used in a job's container
    properties.
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
                "read_only",
                "readOnly",
                TypeInfo(bool),
            ),
            (
                "source_volume",
                "sourceVolume",
                TypeInfo(str),
            ),
        ]

    # The path on the container at which to mount the host volume.
    container_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this value is `true`, the container has read-only access to the volume;
    # otherwise, the container can write to the volume. The default value is
    # `false`.
    read_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the volume to mount.
    source_volume: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterJobDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_definition_name",
                "jobDefinitionName",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, JobDefinitionType]),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_properties",
                "containerProperties",
                TypeInfo(ContainerProperties),
            ),
            (
                "retry_strategy",
                "retryStrategy",
                TypeInfo(RetryStrategy),
            ),
            (
                "timeout",
                "timeout",
                TypeInfo(JobTimeout),
            ),
        ]

    # The name of the job definition to register. Up to 128 letters (uppercase
    # and lowercase), numbers, hyphens, and underscores are allowed.
    job_definition_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of job definition.
    type: typing.Union[str, "JobDefinitionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Default parameter substitution placeholders to set in the job definition.
    # Parameters are specified as a key-value pair mapping. Parameters in a
    # `SubmitJob` request override any corresponding parameter defaults from the
    # job definition.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object with various properties specific for container-based jobs. This
    # parameter is required if the `type` parameter is `container`.
    container_properties: "ContainerProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry strategy to use for failed jobs that are submitted with this job
    # definition. Any retry strategy that is specified during a SubmitJob
    # operation overrides the retry strategy defined here. If a job is terminated
    # due to a timeout, it is not retried.
    retry_strategy: "RetryStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeout configuration for jobs that are submitted with this job
    # definition, after which AWS Batch terminates your jobs if they have not
    # finished. If a job is terminated due to a timeout, it is not retried. The
    # minimum value for the timeout is 60 seconds. Any timeout configuration that
    # is specified during a SubmitJob operation overrides the timeout
    # configuration defined here. For more information, see [Job
    # Timeouts](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    timeout: "JobTimeout" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterJobDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_definition_name",
                "jobDefinitionName",
                TypeInfo(str),
            ),
            (
                "job_definition_arn",
                "jobDefinitionArn",
                TypeInfo(str),
            ),
            (
                "revision",
                "revision",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the job definition.
    job_definition_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the job definition.
    job_definition_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The revision of the job definition.
    revision: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RetryStrategy(ShapeBase):
    """
    The retry strategy associated with a job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attempts",
                "attempts",
                TypeInfo(int),
            ),
        ]

    # The number of times to move a job to the `RUNNABLE` status. You may specify
    # between 1 and 10 attempts. If the value of `attempts` is greater than one,
    # the job is retried if it fails until it has moved to `RUNNABLE` that many
    # times.
    attempts: int = dataclasses.field(default=ShapeBase.NOT_SET, )


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
class SubmitJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_name",
                "jobName",
                TypeInfo(str),
            ),
            (
                "job_queue",
                "jobQueue",
                TypeInfo(str),
            ),
            (
                "job_definition",
                "jobDefinition",
                TypeInfo(str),
            ),
            (
                "array_properties",
                "arrayProperties",
                TypeInfo(ArrayProperties),
            ),
            (
                "depends_on",
                "dependsOn",
                TypeInfo(typing.List[JobDependency]),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "container_overrides",
                "containerOverrides",
                TypeInfo(ContainerOverrides),
            ),
            (
                "retry_strategy",
                "retryStrategy",
                TypeInfo(RetryStrategy),
            ),
            (
                "timeout",
                "timeout",
                TypeInfo(JobTimeout),
            ),
        ]

    # The name of the job. The first character must be alphanumeric, and up to
    # 128 letters (uppercase and lowercase), numbers, hyphens, and underscores
    # are allowed.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job queue into which the job is submitted. You can specify either the
    # name or the Amazon Resource Name (ARN) of the queue.
    job_queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job definition used by this job. This value can be either a
    # `name:revision` or the Amazon Resource Name (ARN) for the job definition.
    job_definition: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The array properties for the submitted job, such as the size of the array.
    # The array size can be between 2 and 10,000. If you specify array properties
    # for a job, it becomes an array job. For more information, see [Array
    # Jobs](http://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html) in
    # the _AWS Batch User Guide_.
    array_properties: "ArrayProperties" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of dependencies for the job. A job can depend upon a maximum of 20
    # jobs. You can specify a `SEQUENTIAL` type dependency without specifying a
    # job ID for array jobs so that each child array job completes sequentially,
    # starting at index 0. You can also specify an `N_TO_N` type dependency with
    # a job ID for array jobs so that each index child of this job must wait for
    # the corresponding index child of each dependency to complete before it can
    # begin.
    depends_on: typing.List["JobDependency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional parameters passed to the job that replace parameter substitution
    # placeholders that are set in the job definition. Parameters are specified
    # as a key and value pair mapping. Parameters in a `SubmitJob` request
    # override any corresponding parameter defaults from the job definition.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of container overrides in JSON format that specify the name of a
    # container in the specified job definition and the overrides it should
    # receive. You can override the default command for a container (that is
    # specified in the job definition or the Docker image) with a `command`
    # override. You can also override existing environment variables (that are
    # specified in the job definition or Docker image) on a container or add new
    # environment variables to it with an `environment` override.
    container_overrides: "ContainerOverrides" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The retry strategy to use for failed jobs from this SubmitJob operation.
    # When a retry strategy is specified here, it overrides the retry strategy
    # defined in the job definition.
    retry_strategy: "RetryStrategy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timeout configuration for this SubmitJob operation. You can specify a
    # timeout duration after which AWS Batch terminates your jobs if they have
    # not finished. If a job is terminated due to a timeout, it is not retried.
    # The minimum value for the timeout is 60 seconds. This configuration
    # overrides any timeout configuration specified in the job definition. For
    # array jobs, child jobs have the same timeout configuration as the parent
    # job. For more information, see [Job
    # Timeouts](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html)
    # in the _Amazon Elastic Container Service Developer Guide_.
    timeout: "JobTimeout" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubmitJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_name",
                "jobName",
                TypeInfo(str),
            ),
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the job.
    job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "jobId",
                TypeInfo(str),
            ),
            (
                "reason",
                "reason",
                TypeInfo(str),
            ),
        ]

    # The AWS Batch job ID of the job to terminate.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message to attach to the job that explains the reason for canceling it.
    # This message is returned by future DescribeJobs operations on the job. This
    # message is also recorded in the AWS Batch activity logs.
    reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TerminateJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Ulimit(ShapeBase):
    """
    The `ulimit` settings to pass to the container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hard_limit",
                "hardLimit",
                TypeInfo(int),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "soft_limit",
                "softLimit",
                TypeInfo(int),
            ),
        ]

    # The hard limit for the `ulimit` type.
    hard_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `type` of the `ulimit`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The soft limit for the `ulimit` type.
    soft_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateComputeEnvironmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "compute_environment",
                "computeEnvironment",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, CEState]),
            ),
            (
                "compute_resources",
                "computeResources",
                TypeInfo(ComputeResourceUpdate),
            ),
            (
                "service_role",
                "serviceRole",
                TypeInfo(str),
            ),
        ]

    # The name or full Amazon Resource Name (ARN) of the compute environment to
    # update.
    compute_environment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the compute environment. Compute environments in the `ENABLED`
    # state can accept jobs from a queue and scale in or out automatically based
    # on the workload demand of its associated queues.
    state: typing.Union[str, "CEState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details of the compute resources managed by the compute environment.
    # Required for a managed compute environment.
    compute_resources: "ComputeResourceUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch
    # to make calls to other AWS services on your behalf.

    # If your specified role has a path other than `/`, then you must either
    # specify the full role ARN (this is recommended) or prefix the role name
    # with the path.

    # Depending on how you created your AWS Batch service role, its ARN may
    # contain the `service-role` path prefix. When you only specify the name of
    # the service role, AWS Batch assumes that your ARN does not use the
    # `service-role` path prefix. Because of this, we recommend that you specify
    # the full ARN of your service role when you create compute environments.
    service_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateComputeEnvironmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "compute_environment_name",
                "computeEnvironmentName",
                TypeInfo(str),
            ),
            (
                "compute_environment_arn",
                "computeEnvironmentArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of compute environment.
    compute_environment_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the compute environment.
    compute_environment_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateJobQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_queue",
                "jobQueue",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, JQState]),
            ),
            (
                "priority",
                "priority",
                TypeInfo(int),
            ),
            (
                "compute_environment_order",
                "computeEnvironmentOrder",
                TypeInfo(typing.List[ComputeEnvironmentOrder]),
            ),
        ]

    # The name or the Amazon Resource Name (ARN) of the job queue.
    job_queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the queue's ability to accept new jobs.
    state: typing.Union[str, "JQState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The priority of the job queue. Job queues with a higher priority (or a
    # higher integer value for the `priority` parameter) are evaluated first when
    # associated with same compute environment. Priority is determined in
    # descending order, for example, a job queue with a priority value of `10` is
    # given scheduling preference over a job queue with a priority value of `1`.
    priority: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details the set of compute environments mapped to a job queue and their
    # order relative to each other. This is one of the parameters used by the job
    # scheduler to determine which compute environment should execute a given
    # job.
    compute_environment_order: typing.List["ComputeEnvironmentOrder"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class UpdateJobQueueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_queue_name",
                "jobQueueName",
                TypeInfo(str),
            ),
            (
                "job_queue_arn",
                "jobQueueArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the job queue.
    job_queue_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the job queue.
    job_queue_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Volume(ShapeBase):
    """
    A data volume used in a job's container properties.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host",
                "host",
                TypeInfo(Host),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The contents of the `host` parameter determine whether your data volume
    # persists on the host container instance and where it is stored. If the host
    # parameter is empty, then the Docker daemon assigns a host path for your
    # data volume. However, the data is not guaranteed to persist after the
    # containers associated with it stop running.
    host: "Host" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the volume. Up to 255 letters (uppercase and lowercase),
    # numbers, hyphens, and underscores are allowed. This name is referenced in
    # the `sourceVolume` parameter of container definition `mountPoints`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
