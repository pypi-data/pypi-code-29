import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AddTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource that you want to tag.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `Tag` objects. Each tag is a key-value pair. Only the `key`
    # parameter is required. If you don't specify a value, Amazon SageMaker sets
    # the value to an empty string.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of tags associated with the Amazon SageMaker resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AlgorithmSpecification(ShapeBase):
    """
    Specifies the training algorithm to use in a
    [CreateTrainingJob](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateTrainingJob.html)
    request.

    For more information about algorithms provided by Amazon SageMaker, see
    [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). For
    information about using your own algorithms, see your-algorithms.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_image",
                "TrainingImage",
                TypeInfo(str),
            ),
            (
                "training_input_mode",
                "TrainingInputMode",
                TypeInfo(typing.Union[str, TrainingInputMode]),
            ),
        ]

    # The registry path of the Docker image that contains the training algorithm.
    # For information about docker registry paths for built-in algorithms, see
    # sagemaker-algo-docker-registry-paths.
    training_image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input mode that the algorithm supports. For the input modes that Amazon
    # SageMaker algorithms support, see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). If
    # an algorithm supports the `File` input mode, Amazon SageMaker downloads the
    # training data from S3 to the provisioned ML storage Volume, and mounts the
    # directory to docker volume for training container. If an algorithm supports
    # the `Pipe` input mode, Amazon SageMaker streams data directly from S3 to
    # the container.

    # In File mode, make sure you provision ML storage volume with sufficient
    # capacity to accommodate the data download from S3. In addition to the
    # training data, the ML storage volume also stores the output model. The
    # algorithm container use ML storage volume to also store intermediate
    # information, if any.

    # For distributed algorithms using File mode, training data is distributed
    # uniformly, and your training duration is predictable if the input data
    # objects size is approximately same. Amazon SageMaker does not split the
    # files any further for model training. If the object sizes are skewed,
    # training won't be optimal as the data distribution is also skewed where one
    # host in a training cluster is overloaded, thus becoming bottleneck in
    # training.
    training_input_mode: typing.Union[str, "TrainingInputMode"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


class AssemblyType(str):
    NONE = "None"
    LINE = "Line"


class BatchStrategy(str):
    MultiRecord = "MultiRecord"
    SingleRecord = "SingleRecord"


@dataclasses.dataclass
class CategoricalParameterRange(ShapeBase):
    """
    A list of categorical hyperparameters to tune.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the categorical hyperparameter to tune.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the categories for the hyperparameter.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Channel(ShapeBase):
    """
    A channel is a named input source that training algorithms can consume.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_name",
                "ChannelName",
                TypeInfo(str),
            ),
            (
                "data_source",
                "DataSource",
                TypeInfo(DataSource),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "compression_type",
                "CompressionType",
                TypeInfo(typing.Union[str, CompressionType]),
            ),
            (
                "record_wrapper_type",
                "RecordWrapperType",
                TypeInfo(typing.Union[str, RecordWrapper]),
            ),
        ]

    # The name of the channel.
    channel_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the channel data.
    data_source: "DataSource" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MIME type of the data.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If training data is compressed, the compression type. The default value is
    # `None`. `CompressionType` is used only in Pipe input mode. In File mode,
    # leave this field unset or set it to None.
    compression_type: typing.Union[str, "CompressionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify RecordIO as the value when input data is in raw format but the
    # training algorithm requires the RecordIO format, in which case, Amazon
    # SageMaker wraps each individual S3 object in a RecordIO record. If the
    # input data is already in RecordIO format, you don't need to set this
    # attribute. For more information, see [Create a Dataset Using
    # RecordIO](https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-
    # format).

    # In FILE mode, leave this field unset or set it to None.
    record_wrapper_type: typing.Union[str, "RecordWrapper"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CompressionType(str):
    NONE = "None"
    GZIP = "Gzip"


@dataclasses.dataclass
class ContainerDefinition(ShapeBase):
    """
    Describes the container, as part of model definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(str),
            ),
            (
                "container_hostname",
                "ContainerHostname",
                TypeInfo(str),
            ),
            (
                "model_data_url",
                "ModelDataUrl",
                TypeInfo(str),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Amazon EC2 Container Registry (Amazon ECR) path where inference code is
    # stored. If you are using your own custom algorithm instead of an algorithm
    # provided by Amazon SageMaker, the inference code must meet Amazon SageMaker
    # requirements. Amazon SageMaker supports both `registry/repository[:tag]`
    # and `registry/repository[@digest]` image path formats. For more
    # information, see [Using Your Own Algorithms with Amazon
    # SageMaker](http://docs.aws.amazon.com/sagemaker/latest/dg/your-
    # algorithms.html)
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS host name for the container after Amazon SageMaker deploys it.
    container_hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 path where the model artifacts, which result from model training,
    # are stored. This path must point to a single gzip compressed tar archive
    # (.tar.gz suffix).

    # If you provide a value for this parameter, Amazon SageMaker uses AWS
    # Security Token Service to download model artifacts from the S3 path you
    # provide. AWS STS is activated in your IAM user account by default. If you
    # previously deactivated AWS STS for a region, you need to reactivate AWS STS
    # for that region. For more information, see [Activating and Deactivating AWS
    # STS i an AWS
    # Region](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-
    # regions.html) in the _AWS Identity and Access Management User Guide_.
    model_data_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The environment variables to set in the Docker container. Each key and
    # value in the `Environment` string to string map can have length of up to
    # 1024. We support up to 16 entries in the map.
    environment: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContinuousParameterRange(ShapeBase):
    """
    A list of continuous hyperparameters to tune.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "min_value",
                "MinValue",
                TypeInfo(str),
            ),
            (
                "max_value",
                "MaxValue",
                TypeInfo(str),
            ),
        ]

    # The name of the continuous hyperparameter to tune.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum value for the hyperparameter. The tuning job uses floating-
    # point values between this value and `MaxValue`for tuning.
    min_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value for the hyperparameter. The tuning job uses floating-
    # point values between `MinValue` value and this value for tuning.
    max_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
            (
                "production_variants",
                "ProductionVariants",
                TypeInfo(typing.List[ProductionVariant]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The name of the endpoint configuration. You specify this name in a
    # [CreateEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html)
    # request.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProductionVariant` objects, one for each model that you want
    # to host at this endpoint.
    production_variants: typing.List["ProductionVariant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of a AWS Key Management Service key that
    # Amazon SageMaker uses to encrypt data on the storage volume attached to the
    # ML compute instance that hosts the endpoint.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointConfigOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_config_arn",
                "EndpointConfigArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint configuration.
    endpoint_config_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the endpoint. The name must be unique within an AWS Region in
    # your AWS account.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an endpoint configuration. For more information, see
    # [CreateEndpointConfig](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html).
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what)in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateEndpointOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHyperParameterTuningJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_config",
                "HyperParameterTuningJobConfig",
                TypeInfo(HyperParameterTuningJobConfig),
            ),
            (
                "training_job_definition",
                "TrainingJobDefinition",
                TypeInfo(HyperParameterTrainingJobDefinition),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the tuning job. This name is the prefix for the names of all
    # training jobs that this tuning job launches. The name must be unique within
    # the same AWS account and AWS Region. Names are not case sensitive, and must
    # be between 1-32 characters.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HyperParameterTuningJobConfig object that describes the tuning job,
    # including the search strategy, metric used to evaluate training jobs,
    # ranges of parameters to search, and resource limits for the tuning job.
    hyper_parameter_tuning_job_config: "HyperParameterTuningJobConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HyperParameterTrainingJobDefinition object that describes the training
    # jobs that this tuning job launches, including static hyperparameters, input
    # data configuration, output data configuration, resource configuration, and
    # stopping condition.
    training_job_definition: "HyperParameterTrainingJobDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs. You can use tags to categorize your AWS
    # resources in different ways, for example, by purpose, owner, or
    # environment. For more information, see [Using Cost Allocation
    # Tags](http://docs.aws.amazon.com//awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateHyperParameterTuningJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hyper_parameter_tuning_job_arn",
                "HyperParameterTuningJobArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tuning job.
    hyper_parameter_tuning_job_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateModelInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
            (
                "primary_container",
                "PrimaryContainer",
                TypeInfo(ContainerDefinition),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
        ]

    # The name of the new model.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the primary docker image containing inference code,
    # associated artifacts, and custom environment map that the inference code
    # uses when the model is deployed for predictions.
    primary_container: "ContainerDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can
    # assume to access model artifacts and docker image for deployment on ML
    # compute instances or for batch transform jobs. Deploying on ML compute
    # instances is part of model hosting. For more information, see [Amazon
    # SageMaker Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A VpcConfig object that specifies the VPC that you want your model to
    # connect to. Control access to and from your model container by configuring
    # the VPC. `VpcConfig` is currently used in hosting services but not in batch
    # transform. For more information, see host-vpc.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateModelOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "model_arn",
                "ModelArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the model created in Amazon SageMaker.
    model_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateNotebookInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, InstanceType]),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "lifecycle_config_name",
                "LifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "direct_internet_access",
                "DirectInternetAccess",
                TypeInfo(typing.Union[str, DirectInternetAccess]),
            ),
        ]

    # The name of the new notebook instance.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of ML compute instance to launch for the notebook instance.
    instance_type: typing.Union[str, "InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When you send any requests to AWS resources from the notebook instance,
    # Amazon SageMaker assumes this role to perform tasks on your behalf. You
    # must grant this role necessary permissions so Amazon SageMaker can perform
    # these tasks. The policy must allow the Amazon SageMaker service principal
    # (sagemaker.amazonaws.com) permissions to assume this role. For more
    # information, see [Amazon SageMaker
    # Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the subnet in a VPC to which you would like to have a
    # connectivity from your ML compute instance.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VPC security group IDs, in the form sg-xxxxxxxx. The security groups
    # must be for the same VPC as specified in the subnet.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data
    # at rest on the ML storage volume that is attached to your notebook
    # instance.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to associate with the notebook instance. You can add tags
    # later by using the `CreateTags` API.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a lifecycle configuration to associate with the notebook
    # instance. For information about lifestyle configurations, see notebook-
    # lifecycle-config.
    lifecycle_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets whether Amazon SageMaker provides internet access to the notebook
    # instance. If you set this to `Disabled` this notebook instance will be able
    # to access resources only in your VPC, and will not be able to connect to
    # Amazon SageMaker training and endpoint services unless your configure a NAT
    # Gateway in your VPC.

    # For more information, see appendix-notebook-and-internet-access. You can
    # set the value of this parameter to `Disabled` only if you set a value for
    # the `SubnetId` parameter.
    direct_internet_access: typing.Union[str, "DirectInternetAccess"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class CreateNotebookInstanceLifecycleConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "on_create",
                "OnCreate",
                TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "on_start",
                "OnStart",
                TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
        ]

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A shell script that runs only once, when you create a notebook instance.
    on_create: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A shell script that runs every time you start a notebook instance,
    # including when you create the notebook instance.
    on_start: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateNotebookInstanceLifecycleConfigOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_lifecycle_config_arn",
                "NotebookInstanceLifecycleConfigArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the lifecycle configuration.
    notebook_instance_lifecycle_config_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateNotebookInstanceOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_arn",
                "NotebookInstanceArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the notebook instance.
    notebook_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePresignedNotebookInstanceUrlInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
            (
                "session_expiration_duration_in_seconds",
                "SessionExpirationDurationInSeconds",
                TypeInfo(int),
            ),
        ]

    # The name of the notebook instance.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration of the session, in seconds. The default is 12 hours.
    session_expiration_duration_in_seconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePresignedNotebookInstanceUrlOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "authorized_url",
                "AuthorizedUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A JSON object that contains the URL string.
    authorized_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTrainingJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                TypeInfo(str),
            ),
            (
                "algorithm_specification",
                "AlgorithmSpecification",
                TypeInfo(AlgorithmSpecification),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(typing.List[Channel]),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "resource_config",
                "ResourceConfig",
                TypeInfo(ResourceConfig),
            ),
            (
                "stopping_condition",
                "StoppingCondition",
                TypeInfo(StoppingCondition),
            ),
            (
                "hyper_parameters",
                "HyperParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the training job. The name must be unique within an AWS Region
    # in an AWS account.
    training_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The registry path of the Docker image that contains the training algorithm
    # and algorithm-specific metadata, including the input mode. For more
    # information about algorithms provided by Amazon SageMaker, see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
    # For information about providing your own algorithms, see your-algorithms.
    algorithm_specification: "AlgorithmSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can
    # assume to perform tasks on your behalf.

    # During model training, Amazon SageMaker needs your permission to read input
    # data from an S3 bucket, download a Docker image that contains training
    # code, write model artifacts to an S3 bucket, write logs to Amazon
    # CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant
    # permissions for all of these tasks to an IAM role. For more information,
    # see [Amazon SageMaker
    # Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `Channel` objects. Each channel is a named input source.
    # `InputDataConfig` describes the input data and its location.

    # Algorithms can accept input data from one or more channels. For example, an
    # algorithm might have two channels of input data, `training_data` and
    # `validation_data`. The configuration for each channel provides the S3
    # location where the input data is stored. It also provides information about
    # the stored data: the MIME type, compression method, and whether the data is
    # wrapped in RecordIO format.

    # Depending on the input mode that the algorithm supports, Amazon SageMaker
    # either copies input data files from an S3 bucket to a local directory in
    # the Docker container, or makes it available as input streams.
    input_data_config: typing.List["Channel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the path to the S3 bucket where you want to store model
    # artifacts. Amazon SageMaker creates subfolders for the artifacts.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resources, including the ML compute instances and ML storage volumes,
    # to use for model training.

    # ML storage volumes store model artifacts and incremental states. Training
    # algorithms might also use ML storage volumes for scratch space. If you want
    # Amazon SageMaker to use the ML storage volume to store the training data,
    # choose `File` as the `TrainingInputMode` in the algorithm specification.
    # For distributed training algorithms, specify an instance count greater than
    # 1.
    resource_config: "ResourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets a duration for training. Use this parameter to cap model training
    # costs. To stop a job, Amazon SageMaker sends the algorithm the `SIGTERM`
    # signal, which delays job termination for 120 seconds. Algorithms might use
    # this 120-second window to save the model artifacts.

    # When Amazon SageMaker terminates a job because the stopping condition has
    # been met, training algorithms provided by Amazon SageMaker save the
    # intermediate results of the job. This intermediate data is a valid model
    # artifact. You can use it to create a model using the `CreateModel` API.
    stopping_condition: "StoppingCondition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Algorithm-specific parameters that influence the quality of the model. You
    # set hyperparameters before you start the learning process. For a list of
    # hyperparameters for each training algorithm provided by Amazon SageMaker,
    # see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).

    # You can specify a maximum of 100 hyperparameters. Each hyperparameter is a
    # key-value pair. Each key and value is limited to 256 characters, as
    # specified by the `Length Constraint`.
    hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A VpcConfig object that specifies the VPC that you want your training job
    # to connect to. Control access to and from your training container by
    # configuring the VPC. For more information, see train-vpc
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs. For more information, see [Using Cost
    # Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTrainingJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTransformJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                TypeInfo(str),
            ),
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
            (
                "transform_input",
                "TransformInput",
                TypeInfo(TransformInput),
            ),
            (
                "transform_output",
                "TransformOutput",
                TypeInfo(TransformOutput),
            ),
            (
                "transform_resources",
                "TransformResources",
                TypeInfo(TransformResources),
            ),
            (
                "max_concurrent_transforms",
                "MaxConcurrentTransforms",
                TypeInfo(int),
            ),
            (
                "max_payload_in_mb",
                "MaxPayloadInMB",
                TypeInfo(int),
            ),
            (
                "batch_strategy",
                "BatchStrategy",
                TypeInfo(typing.Union[str, BatchStrategy]),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name of the transform job. The name must be unique within an AWS Region
    # in an AWS account.
    transform_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the model that you want to use for the transform job.
    # `ModelName` must be the name of an existing Amazon SageMaker model within
    # an AWS Region in an AWS account.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the input source and the way the transform job consumes it.
    transform_input: "TransformInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the results of the transform job.
    transform_output: "TransformOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the resources, including ML instance types and ML instance count,
    # to use for the transform job.
    transform_resources: "TransformResources" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of parallel requests that can be sent to each instance
    # in a transform job. This is good for algorithms that implement multiple
    # workers on larger instances . The default value is `1`. To allow Amazon
    # SageMaker to determine the appropriate number for
    # `MaxConcurrentTransforms`, set the value to `0`.
    max_concurrent_transforms: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum payload size allowed, in MB. A payload is the data portion of a
    # record (without metadata). The value in `MaxPayloadInMB` must be greater or
    # equal to the size of a single record. You can approximate the size of a
    # record by dividing the size of your dataset by the number of records. Then
    # multiply this value by the number of records you want in a mini-batch. It
    # is recommended to enter a value slightly larger than this to ensure the
    # records fit within the maximum payload size. The default value is `6` MB.
    # For an unlimited payload size, set the value to `0`.
    max_payload_in_mb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines the number of records included in a single mini-batch.
    # `SingleRecord` means only one record is used per mini-batch. `MultiRecord`
    # means a mini-batch is set to contain as many records that can fit within
    # the `MaxPayloadInMB` limit.

    # Batch transform will automatically split your input data into whatever
    # payload size is specified if you set `SplitType` to `Line` and
    # `BatchStrategy` to `MultiRecord`. There's no need to split the dataset into
    # smaller files or to use larger payload sizes unless the records in your
    # dataset are very large.
    batch_strategy: typing.Union[str, "BatchStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The environment variables to set in the Docker container. We support up to
    # 16 key and values entries in the map.
    environment: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs. Adding tags is optional. For more information,
    # see [Using Cost Allocation
    # Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-
    # alloc-tags.html#allocation-what) in the _AWS Billing and Cost Management
    # User Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTransformJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_job_arn",
                "TransformJobArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the transform job.
    transform_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DataSource(ShapeBase):
    """
    Describes the location of the channel data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_source",
                "S3DataSource",
                TypeInfo(S3DataSource),
            ),
        ]

    # The S3 location of the data source that is associated with a channel.
    s3_data_source: "S3DataSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEndpointConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of the endpoint configuration that you want to delete.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEndpointInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
        ]

    # The name of the endpoint that you want to delete.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteModelInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
        ]

    # The name of the model to delete.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNotebookInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the Amazon SageMaker notebook instance to delete.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNotebookInstanceLifecycleConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle configuration to delete.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource whose tags you want to
    # delete.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array or one or more tag keys to delete.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTagsOutput(OutputShapeBase):
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
class DeployedImage(ShapeBase):
    """
    Gets the Amazon EC2 Container Registry path of the docker image of the model
    that is hosted in this ProductionVariant.

    If you used the `registry/repository[:tag]` form to to specify the image path of
    the primary container when you created the model hosted in this
    `ProductionVariant`, the path resolves to a path of the form
    `registry/repository[@digest]`. A digest is a hash value that identifies a
    specific version of an image. For information about Amazon ECR paths, see
    [Pulling an
    Image](http://docs.aws.amazon.com//AmazonECR/latest/userguide/docker-pull-ecr-
    image.html) in the _Amazon ECR User Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "specified_image",
                "SpecifiedImage",
                TypeInfo(str),
            ),
            (
                "resolved_image",
                "ResolvedImage",
                TypeInfo(str),
            ),
            (
                "resolution_time",
                "ResolutionTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The image path you specified when you created the model.
    specified_image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific digest path of the image hosted in this `ProductionVariant`.
    resolved_image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the image path for the model resolved to the
    # `ResolvedImage`
    resolution_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEndpointConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of the endpoint configuration.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndpointConfigOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
            (
                "endpoint_config_arn",
                "EndpointConfigArn",
                TypeInfo(str),
            ),
            (
                "production_variants",
                "ProductionVariants",
                TypeInfo(typing.List[ProductionVariant]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the Amazon SageMaker endpoint configuration.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the endpoint configuration.
    endpoint_config_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `ProductionVariant` objects, one for each model that you want
    # to host at this endpoint.
    production_variants: typing.List["ProductionVariant"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the
    # ML storage volume attached to the instance.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndpointInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
        ]

    # The name of the endpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndpointOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                TypeInfo(typing.Union[str, EndpointStatus]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "production_variants",
                "ProductionVariants",
                TypeInfo(typing.List[ProductionVariantSummary]),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the endpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the endpoint configuration associated with this endpoint.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the endpoint.
    endpoint_status: typing.Union[str, "EndpointStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of ProductionVariantSummary objects, one for each model hosted
    # behind this endpoint.
    production_variants: typing.List["ProductionVariantSummary"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # If the status of the endpoint is `Failed`, the reason why it failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHyperParameterTuningJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the tuning job to describe.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeHyperParameterTuningJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_arn",
                "HyperParameterTuningJobArn",
                TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_config",
                "HyperParameterTuningJobConfig",
                TypeInfo(HyperParameterTuningJobConfig),
            ),
            (
                "training_job_definition",
                "TrainingJobDefinition",
                TypeInfo(HyperParameterTrainingJobDefinition),
            ),
            (
                "hyper_parameter_tuning_job_status",
                "HyperParameterTuningJobStatus",
                TypeInfo(typing.Union[str, HyperParameterTuningJobStatus]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status_counters",
                "TrainingJobStatusCounters",
                TypeInfo(TrainingJobStatusCounters),
            ),
            (
                "objective_status_counters",
                "ObjectiveStatusCounters",
                TypeInfo(ObjectiveStatusCounters),
            ),
            (
                "hyper_parameter_tuning_end_time",
                "HyperParameterTuningEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "best_training_job",
                "BestTrainingJob",
                TypeInfo(HyperParameterTrainingJobSummary),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the tuning job.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tuning job.
    hyper_parameter_tuning_job_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HyperParameterTuningJobConfig object that specifies the configuration
    # of the tuning job.
    hyper_parameter_tuning_job_config: "HyperParameterTuningJobConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HyperParameterTrainingJobDefinition object that specifies the
    # definition of the training jobs that this tuning job launches.
    training_job_definition: "HyperParameterTrainingJobDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the tuning job: InProgress, Completed, Failed, Stopping, or
    # Stopped.
    hyper_parameter_tuning_job_status: typing.Union[
        str, "HyperParameterTuningJobStatus"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The date and time that the tuning job started.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The TrainingJobStatusCounters object that specifies the number of training
    # jobs, categorized by status, that this tuning job launched.
    training_job_status_counters: "TrainingJobStatusCounters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ObjectiveStatusCounters object that specifies the number of training
    # jobs, categorized by the status of their final objective metric, that this
    # tuning job launched.
    objective_status_counters: "ObjectiveStatusCounters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the tuning job ended.
    hyper_parameter_tuning_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the status of the tuning job was modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A TrainingJobSummary object that describes the training job that completed
    # with the best current HyperParameterTuningJobObjective.
    best_training_job: "HyperParameterTrainingJobSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the tuning job failed, the reason it failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeModelInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
        ]

    # The name of the model.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeModelOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
            (
                "primary_container",
                "PrimaryContainer",
                TypeInfo(ContainerDefinition),
            ),
            (
                "execution_role_arn",
                "ExecutionRoleArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "model_arn",
                "ModelArn",
                TypeInfo(str),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the Amazon SageMaker model.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the primary inference code, associated artifacts, and
    # custom environment map that the inference code uses when it is deployed in
    # production.
    primary_container: "ContainerDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that you specified for the
    # model.
    execution_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the model was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the model.
    model_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A VpcConfig object that specifies the VPC that this model has access to.
    # For more information, see host-vpc
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNotebookInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the notebook instance that you want information about.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeNotebookInstanceLifecycleConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of the lifecycle configuration to describe.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNotebookInstanceLifecycleConfigOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_lifecycle_config_arn",
                "NotebookInstanceLifecycleConfigArn",
                TypeInfo(str),
            ),
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "on_create",
                "OnCreate",
                TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "on_start",
                "OnStart",
                TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the lifecycle configuration.
    notebook_instance_lifecycle_config_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shell script that runs only once, when you create a notebook instance.
    on_create: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shell script that runs every time you start a notebook instance,
    # including when you create the notebook instance.
    on_start: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeNotebookInstanceOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "notebook_instance_arn",
                "NotebookInstanceArn",
                TypeInfo(str),
            ),
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
            (
                "notebook_instance_status",
                "NotebookInstanceStatus",
                TypeInfo(typing.Union[str, NotebookInstanceStatus]),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, InstanceType]),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
            (
                "network_interface_id",
                "NetworkInterfaceId",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "direct_internet_access",
                "DirectInternetAccess",
                TypeInfo(typing.Union[str, DirectInternetAccess]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the notebook instance.
    notebook_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the Amazon SageMaker notebook instance.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the notebook instance.
    notebook_instance_status: typing.Union[str, "NotebookInstanceStatus"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # If status is failed, the reason it failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that you use to connect to the Jupyter notebook that is running in
    # your notebook instance.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of ML compute instance running on the notebook instance.
    instance_type: typing.Union[str, "InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the VPC subnet.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the VPC security groups.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Resource Name (ARN) of the IAM role associated with the instance.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the
    # ML storage volume attached to the instance.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Network interface IDs that Amazon SageMaker created at the time of creating
    # the instance.
    network_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp. Use this parameter to retrieve the time when the notebook
    # instance was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp. Use this parameter to return the time when the notebook
    # instance was created
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns the name of a notebook instance lifecycle configuration.

    # For information about notebook instance lifestyle configurations, see
    # notebook-lifecycle-config.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes whether Amazon SageMaker provides internet access to the notebook
    # instance. If this value is set to _Disabled, he notebook instance does not
    # have internet access, and cannot connect to Amazon SageMaker training and
    # endpoint services_.

    # For more information, see appendix-notebook-and-internet-access.
    direct_internet_access: typing.Union[str, "DirectInternetAccess"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class DescribeTrainingJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the training job.
    training_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrainingJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_name",
                "TrainingJobName",
                TypeInfo(str),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                TypeInfo(str),
            ),
            (
                "model_artifacts",
                "ModelArtifacts",
                TypeInfo(ModelArtifacts),
            ),
            (
                "training_job_status",
                "TrainingJobStatus",
                TypeInfo(typing.Union[str, TrainingJobStatus]),
            ),
            (
                "secondary_status",
                "SecondaryStatus",
                TypeInfo(typing.Union[str, SecondaryStatus]),
            ),
            (
                "algorithm_specification",
                "AlgorithmSpecification",
                TypeInfo(AlgorithmSpecification),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(typing.List[Channel]),
            ),
            (
                "resource_config",
                "ResourceConfig",
                TypeInfo(ResourceConfig),
            ),
            (
                "stopping_condition",
                "StoppingCondition",
                TypeInfo(StoppingCondition),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "tuning_job_arn",
                "TuningJobArn",
                TypeInfo(str),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "hyper_parameters",
                "HyperParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
            (
                "training_start_time",
                "TrainingStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "training_end_time",
                "TrainingEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "secondary_status_transitions",
                "SecondaryStatusTransitions",
                TypeInfo(typing.List[SecondaryStatusTransition]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the model training job.
    training_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the Amazon S3 location that is configured for storing
    # model artifacts.
    model_artifacts: "ModelArtifacts" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the training job.

    # For the `InProgress` status, Amazon SageMaker can return these secondary
    # statuses:

    #   * Starting - Preparing for training.

    #   * Downloading - Optional stage for algorithms that support File training input mode. It indicates data is being downloaded to ML storage volumes.

    #   * Training - Training is in progress.

    #   * Uploading - Training is complete and model upload is in progress.

    # For the `Stopped` training status, Amazon SageMaker can return these
    # secondary statuses:

    #   * MaxRuntimeExceeded - Job stopped as a result of maximum allowed runtime exceeded.
    training_job_status: typing.Union[str, "TrainingJobStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Provides granular information about the system state. For more information,
    # see `TrainingJobStatus`.

    #   * `Starting` \- starting the training job.

    #   * `Downloading` \- downloading the input data.

    #   * `Training` \- model training is in progress.

    #   * `Uploading` \- uploading the trained model.

    #   * `Stopping` \- stopping the training job.

    #   * `Stopped` \- the training job has stopped.

    #   * `MaxRuntimeExceeded` \- the training job exceeded the specified max run time and has been stopped.

    #   * `Completed` \- the training job has completed.

    #   * `Failed` \- the training job has failed. The failure reason is stored in the `FailureReason` field of `DescribeTrainingJobResponse`.

    # The valid values for `SecondaryStatus` are subject to change. They
    # primarily provide information on the progress of the training job.
    secondary_status: typing.Union[str, "SecondaryStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the algorithm used for training, and algorithm metadata.
    algorithm_specification: "AlgorithmSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `Channel` objects that describes each data input channel.
    input_data_config: typing.List["Channel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Resources, including ML compute instances and ML storage volumes, that are
    # configured for model training.
    resource_config: "ResourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The condition under which to stop the training job.
    stopping_condition: "StoppingCondition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that indicates when the training job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the associated hyperparameter tuning job
    # if the training job was launched by a hyperparameter tuning job.
    tuning_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the training job failed, the reason it failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Algorithm-specific parameters.
    hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Identity and Access Management (IAM) role configured for the
    # training job.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The S3 path where model artifacts that you configured when creating the job
    # are stored. Amazon SageMaker creates subfolders for model artifacts.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A VpcConfig object that specifies the VPC that this training job has access
    # to. For more information, see train-vpc.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the time when the training job starts on training instances. You
    # are billed for the time interval between this time and the value of
    # `TrainingEndTime`. The start time in CloudWatch Logs might be later than
    # this time. The difference is due to the time it takes to download the
    # training data and to the size of the training container.
    training_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the time when the training job ends on training instances. You
    # are billed for the time interval between the value of `TrainingStartTime`
    # and this time. For successful jobs and stopped jobs, this is the time after
    # model artifacts are uploaded. For failed jobs, this is the time when Amazon
    # SageMaker detects a job failure.
    training_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that indicates when the status of the training job was last
    # modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # To give an overview of the training job lifecycle,
    # `SecondaryStatusTransitions` is a log of time-ordered secondary statuses
    # that a training job has transitioned.
    secondary_status_transitions: typing.List["SecondaryStatusTransition"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class DescribeTransformJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the transform job that you want to view details of.
    transform_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTransformJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_job_name",
                "TransformJobName",
                TypeInfo(str),
            ),
            (
                "transform_job_arn",
                "TransformJobArn",
                TypeInfo(str),
            ),
            (
                "transform_job_status",
                "TransformJobStatus",
                TypeInfo(typing.Union[str, TransformJobStatus]),
            ),
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
            (
                "transform_input",
                "TransformInput",
                TypeInfo(TransformInput),
            ),
            (
                "transform_resources",
                "TransformResources",
                TypeInfo(TransformResources),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "max_concurrent_transforms",
                "MaxConcurrentTransforms",
                TypeInfo(int),
            ),
            (
                "max_payload_in_mb",
                "MaxPayloadInMB",
                TypeInfo(int),
            ),
            (
                "batch_strategy",
                "BatchStrategy",
                TypeInfo(typing.Union[str, BatchStrategy]),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_output",
                "TransformOutput",
                TypeInfo(TransformOutput),
            ),
            (
                "transform_start_time",
                "TransformStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "transform_end_time",
                "TransformEndTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the transform job.
    transform_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the transform job.
    transform_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the transform job. If the transform job failed, the reason is
    # returned in the `FailureReason` field.
    transform_job_status: typing.Union[str, "TransformJobStatus"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The name of the model used in the transform job.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the dataset to be transformed and the Amazon S3 location where it
    # is stored.
    transform_input: "TransformInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes the resources, including ML instance types and ML instance count,
    # to use for the transform job.
    transform_resources: "TransformResources" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the transform Job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the transform job failed, the reason that it failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of parallel requests on each instance node that can be
    # launched in a transform job. The default value is 1.
    max_concurrent_transforms: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum payload size , in MB used in the transform job.
    max_payload_in_mb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SingleRecord means only one record was used per a batch. `MultiRecord`
    # means batches contained as many records that could possibly fit within the
    # `MaxPayloadInMB` limit.
    batch_strategy: typing.Union[str, "BatchStrategy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    environment: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the Amazon S3 location where you want Amazon SageMaker to save
    # the results from the transform job.
    transform_output: "TransformOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when the transform job starts on ML instances. You are billed for
    # the time interval between this time and the value of `TransformEndTime`.
    transform_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when the transform job is `Completed`, `Stopped`, or `Failed`.
    # You are billed for the time interval between this time and the value of
    # `TransformStartTime`.
    transform_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DesiredWeightAndCapacity(ShapeBase):
    """
    Specifies weight and capacity values for a production variant.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variant_name",
                "VariantName",
                TypeInfo(str),
            ),
            (
                "desired_weight",
                "DesiredWeight",
                TypeInfo(float),
            ),
            (
                "desired_instance_count",
                "DesiredInstanceCount",
                TypeInfo(int),
            ),
        ]

    # The name of the variant to update.
    variant_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The variant's weight.
    desired_weight: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The variant's capacity.
    desired_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class DirectInternetAccess(str):
    Enabled = "Enabled"
    Disabled = "Disabled"


class EndpointConfigSortKey(str):
    Name = "Name"
    CreationTime = "CreationTime"


@dataclasses.dataclass
class EndpointConfigSummary(ShapeBase):
    """
    Provides summary information for an endpoint configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
            (
                "endpoint_config_arn",
                "EndpointConfigArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the endpoint configuration.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the endpoint configuration.
    endpoint_config_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the endpoint configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EndpointSortKey(str):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class EndpointStatus(str):
    OutOfService = "OutOfService"
    Creating = "Creating"
    Updating = "Updating"
    SystemUpdating = "SystemUpdating"
    RollingBack = "RollingBack"
    InService = "InService"
    Deleting = "Deleting"
    Failed = "Failed"


@dataclasses.dataclass
class EndpointSummary(ShapeBase):
    """
    Provides summary information for an endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                TypeInfo(typing.Union[str, EndpointStatus]),
            ),
        ]

    # The name of the endpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the endpoint was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the endpoint was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the endpoint.
    endpoint_status: typing.Union[str, "EndpointStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FinalHyperParameterTuningJobObjectiveMetric(ShapeBase):
    """
    Shows the final value for the objective metric for a training job that was
    launched by a hyperparameter tuning job. You define the objective metric in the
    `HyperParameterTuningJobObjective` parameter of HyperParameterTuningJobConfig.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(float),
            ),
            (
                "type",
                "Type",
                TypeInfo(
                    typing.Union[str, HyperParameterTuningJobObjectiveType]
                ),
            ),
        ]

    # The name of the objective metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the objective metric.
    value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to minimize or maximize the objective metric. Valid values are
    # Minimize and Maximize.
    type: typing.Union[str, "HyperParameterTuningJobObjectiveType"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )


@dataclasses.dataclass
class HyperParameterAlgorithmSpecification(ShapeBase):
    """
    Specifies which training algorithm to use for training jobs that a
    hyperparameter tuning job launches and the metrics to monitor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_image",
                "TrainingImage",
                TypeInfo(str),
            ),
            (
                "training_input_mode",
                "TrainingInputMode",
                TypeInfo(typing.Union[str, TrainingInputMode]),
            ),
            (
                "metric_definitions",
                "MetricDefinitions",
                TypeInfo(typing.List[MetricDefinition]),
            ),
        ]

    # The registry path of the Docker image that contains the training algorithm.
    # For information about Docker registry paths for built-in algorithms, see
    # sagemaker-algo-docker-registry-paths.
    training_image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input mode that the algorithm supports: File or Pipe. In File input
    # mode, Amazon SageMaker downloads the training data from Amazon S3 to the
    # storage volume that is attached to the training instance and mounts the
    # directory to the Docker volume for the training container. In Pipe input
    # mode, Amazon SageMaker streams data directly from Amazon S3 to the
    # container.

    # If you specify File mode, make sure that you provision the storage volume
    # that is attached to the training instance with enough capacity to
    # accommodate the training data downloaded from Amazon S3, the model
    # artifacts, and intermediate information.

    # For more information about input modes, see
    # [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
    training_input_mode: typing.Union[str, "TrainingInputMode"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # An array of MetricDefinition objects that specify the metrics that the
    # algorithm emits.
    metric_definitions: typing.List["MetricDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HyperParameterTrainingJobDefinition(ShapeBase):
    """
    Defines the training jobs launched by a hyperparameter tuning job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "algorithm_specification",
                "AlgorithmSpecification",
                TypeInfo(HyperParameterAlgorithmSpecification),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "input_data_config",
                "InputDataConfig",
                TypeInfo(typing.List[Channel]),
            ),
            (
                "output_data_config",
                "OutputDataConfig",
                TypeInfo(OutputDataConfig),
            ),
            (
                "resource_config",
                "ResourceConfig",
                TypeInfo(ResourceConfig),
            ),
            (
                "stopping_condition",
                "StoppingCondition",
                TypeInfo(StoppingCondition),
            ),
            (
                "static_hyper_parameters",
                "StaticHyperParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpc_config",
                "VpcConfig",
                TypeInfo(VpcConfig),
            ),
        ]

    # The HyperParameterAlgorithmSpecification object that specifies the
    # algorithm to use for the training jobs that the tuning job launches.
    algorithm_specification: "HyperParameterAlgorithmSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role associated with the training
    # jobs that the tuning job launches.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of Channel objects that specify the input for the training jobs
    # that the tuning job launches.
    input_data_config: typing.List["Channel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the path to the Amazon S3 bucket where you store model artifacts
    # from the training jobs that the tuning job launches.
    output_data_config: "OutputDataConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resources, including the compute instances and storage volumes, to use
    # for the training jobs that the tuning job launches.

    # Storage volumes store model artifacts and incremental states. Training
    # algorithms might also use storage volumes for scratch space. If you want
    # Amazon SageMaker to use the storage volume to store the training data,
    # choose `File` as the `TrainingInputMode` in the algorithm specification.
    # For distributed training algorithms, specify an instance count greater than
    # 1.
    resource_config: "ResourceConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets a maximum duration for the training jobs that the tuning job launches.
    # Use this parameter to limit model training costs.

    # To stop a job, Amazon SageMaker sends the algorithm the `SIGTERM` signal.
    # This delays job termination for 120 seconds. Algorithms might use this
    # 120-second window to save the model artifacts.

    # When Amazon SageMaker terminates a job because the stopping condition has
    # been met, training algorithms provided by Amazon SageMaker save the
    # intermediate results of the job.
    stopping_condition: "StoppingCondition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the values of hyperparameters that do not change for the tuning
    # job.
    static_hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The VpcConfig object that specifies the VPC that you want the training jobs
    # that this hyperparameter tuning job launches to connect to. Control access
    # to and from your training container by configuring the VPC. For more
    # information, see train-vpc.
    vpc_config: "VpcConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HyperParameterTrainingJobSummary(ShapeBase):
    """
    Specifies summary information about a training job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                TypeInfo(str),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status",
                "TrainingJobStatus",
                TypeInfo(typing.Union[str, TrainingJobStatus]),
            ),
            (
                "tuned_hyper_parameters",
                "TunedHyperParameters",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_start_time",
                "TrainingStartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "training_end_time",
                "TrainingEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
            (
                "final_hyper_parameter_tuning_job_objective_metric",
                "FinalHyperParameterTuningJobObjectiveMetric",
                TypeInfo(FinalHyperParameterTuningJobObjectiveMetric),
            ),
            (
                "objective_status",
                "ObjectiveStatus",
                TypeInfo(typing.Union[str, ObjectiveStatus]),
            ),
        ]

    # The name of the training job.
    training_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the training job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the training job.
    training_job_status: typing.Union[str, "TrainingJobStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # A list of the hyperparameters for which you specified ranges to search.
    tuned_hyper_parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the training job started.
    training_start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the training job ended.
    training_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason that the training job failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The FinalHyperParameterTuningJobObjectiveMetric object that specifies the
    # value of the objective metric of the tuning job that launched this training
    # job.
    final_hyper_parameter_tuning_job_objective_metric: "FinalHyperParameterTuningJobObjectiveMetric" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the objective metric for the training job:

    #   * Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.

    #   * Pending: The training job is in progress and evaluation of its final objective metric is pending.

    #   * Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
    objective_status: typing.Union[str, "ObjectiveStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HyperParameterTuningJobConfig(ShapeBase):
    """
    Configures a hyperparameter tuning job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "strategy",
                "Strategy",
                TypeInfo(
                    typing.Union[str, HyperParameterTuningJobStrategyType]
                ),
            ),
            (
                "hyper_parameter_tuning_job_objective",
                "HyperParameterTuningJobObjective",
                TypeInfo(HyperParameterTuningJobObjective),
            ),
            (
                "resource_limits",
                "ResourceLimits",
                TypeInfo(ResourceLimits),
            ),
            (
                "parameter_ranges",
                "ParameterRanges",
                TypeInfo(ParameterRanges),
            ),
        ]

    # Specifies the search strategy for hyperparameters. Currently, the only
    # valid value is `Bayesian`.
    strategy: typing.Union[str, "HyperParameterTuningJobStrategyType"
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # The HyperParameterTuningJobObjective object that specifies the objective
    # metric for this tuning job.
    hyper_parameter_tuning_job_objective: "HyperParameterTuningJobObjective" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ResourceLimits object that specifies the maximum number of training
    # jobs and parallel training jobs for this tuning job.
    resource_limits: "ResourceLimits" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ParameterRanges object that specifies the ranges of hyperparameters
    # that this tuning job searches.
    parameter_ranges: "ParameterRanges" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HyperParameterTuningJobObjective(ShapeBase):
    """
    Defines the objective metric for a hyperparameter tuning job. Hyperparameter
    tuning uses the value of this metric to evaluate the training jobs it launches,
    and returns the training job that results in either the highest or lowest value
    for this metric, depending on the value you specify for the `Type` parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(
                    typing.Union[str, HyperParameterTuningJobObjectiveType]
                ),
            ),
            (
                "metric_name",
                "MetricName",
                TypeInfo(str),
            ),
        ]

    # Whether to minimize or maximize the objective metric.
    type: typing.Union[str, "HyperParameterTuningJobObjectiveType"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )

    # The name of the metric to use for the objective metric.
    metric_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class HyperParameterTuningJobObjectiveType(str):
    Maximize = "Maximize"
    Minimize = "Minimize"


class HyperParameterTuningJobSortByOptions(str):
    Name = "Name"
    Status = "Status"
    CreationTime = "CreationTime"


class HyperParameterTuningJobStatus(str):
    Completed = "Completed"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"


class HyperParameterTuningJobStrategyType(str):
    """
    The strategy hyperparameter tuning uses to find the best combination of
    hyperparameters for your model. Currently, the only supported value is
    `Bayesian`.
    """
    Bayesian = "Bayesian"


@dataclasses.dataclass
class HyperParameterTuningJobSummary(ShapeBase):
    """
    Provides summary information about a hyperparameter tuning job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_arn",
                "HyperParameterTuningJobArn",
                TypeInfo(str),
            ),
            (
                "hyper_parameter_tuning_job_status",
                "HyperParameterTuningJobStatus",
                TypeInfo(typing.Union[str, HyperParameterTuningJobStatus]),
            ),
            (
                "strategy",
                "Strategy",
                TypeInfo(
                    typing.Union[str, HyperParameterTuningJobStrategyType]
                ),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status_counters",
                "TrainingJobStatusCounters",
                TypeInfo(TrainingJobStatusCounters),
            ),
            (
                "objective_status_counters",
                "ObjectiveStatusCounters",
                TypeInfo(ObjectiveStatusCounters),
            ),
            (
                "hyper_parameter_tuning_end_time",
                "HyperParameterTuningEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "resource_limits",
                "ResourceLimits",
                TypeInfo(ResourceLimits),
            ),
        ]

    # The name of the tuning job.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the tuning job.
    hyper_parameter_tuning_job_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the tuning job.
    hyper_parameter_tuning_job_status: typing.Union[
        str, "HyperParameterTuningJobStatus"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Specifies the search strategy hyperparameter tuning uses to choose which
    # hyperparameters to use for each iteration. Currently, the only valid value
    # is Bayesian.
    strategy: typing.Union[str, "HyperParameterTuningJobStrategyType"
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # The date and time that the tuning job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The TrainingJobStatusCounters object that specifies the numbers of training
    # jobs, categorized by status, that this tuning job launched.
    training_job_status_counters: "TrainingJobStatusCounters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ObjectiveStatusCounters object that specifies the numbers of training
    # jobs, categorized by objective metric status, that this tuning job
    # launched.
    objective_status_counters: "ObjectiveStatusCounters" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the tuning job ended.
    hyper_parameter_tuning_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the tuning job was modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ResourceLimits object that specifies the maximum number of training
    # jobs and parallel training jobs allowed for this tuning job.
    resource_limits: "ResourceLimits" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstanceType(str):
    ml_t2_medium = "ml.t2.medium"
    ml_t2_large = "ml.t2.large"
    ml_t2_xlarge = "ml.t2.xlarge"
    ml_t2_2xlarge = "ml.t2.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"


@dataclasses.dataclass
class IntegerParameterRange(ShapeBase):
    """
    For a hyperparameter of the integer type, specifies the range that a
    hyperparameter tuning job searches.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "min_value",
                "MinValue",
                TypeInfo(str),
            ),
            (
                "max_value",
                "MaxValue",
                TypeInfo(str),
            ),
        ]

    # The name of the hyperparameter to search.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum value of the hyperparameter to search.
    min_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum value of the hyperparameter to search.
    max_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListEndpointConfigsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, EndpointConfigSortKey]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, OrderKey]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The field to sort results by. The default is `CreationTime`.
    sort_by: typing.Union[str, "EndpointConfigSortKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: typing.Union[str, "OrderKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the result of the previous `ListEndpointConfig` request was truncated,
    # the response includes a `NextToken`. To retrieve the next set of endpoint
    # configurations, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of training jobs to return in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string in the endpoint configuration name. This filter returns only
    # endpoint configurations whose name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only endpoint configurations created before the
    # specified time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoint configurations created after the
    # specified time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListEndpointConfigsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_configs",
                "EndpointConfigs",
                TypeInfo(typing.List[EndpointConfigSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of endpoint configurations.
    endpoint_configs: typing.List["EndpointConfigSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of endpoint configurations, use it in the subsequent
    # request
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListEndpointConfigsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListEndpointsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, EndpointSortKey]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, OrderKey]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_equals",
                "StatusEquals",
                TypeInfo(typing.Union[str, EndpointStatus]),
            ),
        ]

    # Sorts the list of results. The default is `CreationTime`.
    sort_by: typing.Union[str, "EndpointSortKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: typing.Union[str, "OrderKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the result of a `ListEndpoints` request was truncated, the response
    # includes a `NextToken`. To retrieve the next set of endpoints, use the
    # token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of endpoints to return in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string in endpoint names. This filter returns only endpoints whose name
    # contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only endpoints that were created before the specified
    # time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints that were created after the specified
    # time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints that were modified before the
    # specified timestamp.
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints that were modified after the specified
    # timestamp.
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only endpoints with the specified status.
    status_equals: typing.Union[str, "EndpointStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListEndpointsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints",
                "Endpoints",
                TypeInfo(typing.List[EndpointSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array or endpoint objects.
    endpoints: typing.List["EndpointSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of training jobs, use it in the subsequent request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListEndpointsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListHyperParameterTuningJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(
                    typing.Union[str, HyperParameterTuningJobSortByOptions]
                ),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_equals",
                "StatusEquals",
                TypeInfo(typing.Union[str, HyperParameterTuningJobStatus]),
            ),
        ]

    # If the result of the previous `ListHyperParameterTuningJobs` request was
    # truncated, the response includes a `NextToken`. To retrieve the next set of
    # tuning jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of tuning jobs to return. The default value is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field to sort results by. The default is `Name`.
    sort_by: typing.Union[str, "HyperParameterTuningJobSortByOptions"
                         ] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )

    # The sort order for results. The default is `Ascending`.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string in the tuning job name. This filter returns only tuning jobs whose
    # name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only tuning jobs that were created after the
    # specified time.
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs that were created before the
    # specified time.
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs that were modified after the
    # specified time.
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs that were modified before the
    # specified time.
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only tuning jobs with the specified status.
    status_equals: typing.Union[str, "HyperParameterTuningJobStatus"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


@dataclasses.dataclass
class ListHyperParameterTuningJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "hyper_parameter_tuning_job_summaries",
                "HyperParameterTuningJobSummaries",
                TypeInfo(typing.List[HyperParameterTuningJobSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of HyperParameterTuningJobSummary objects that describe the tuning
    # jobs that the `ListHyperParameterTuningJobs` request returned.
    hyper_parameter_tuning_job_summaries: typing.List[
        "HyperParameterTuningJobSummary"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # If the result of this `ListHyperParameterTuningJobs` request was truncated,
    # the response includes a `NextToken`. To retrieve the next set of tuning
    # jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListModelsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, ModelSortKey]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, OrderKey]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Sorts the list of results. The default is `CreationTime`.
    sort_by: typing.Union[str, "ModelSortKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: typing.Union[str, "OrderKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response to a previous `ListModels` request was truncated, the
    # response includes a `NextToken`. To retrieve the next set of models, use
    # the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of models to return in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string in the training job name. This filter returns only models in the
    # training job whose name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only models created before the specified time
    # (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only models created after the specified time
    # (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListModelsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "models",
                "Models",
                TypeInfo(typing.List[ModelSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `ModelSummary` objects, each of which lists a model.
    models: typing.List["ModelSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of models, use it in the subsequent request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListModelsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListNotebookInstanceLifecycleConfigsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(
                    typing.Union[str, NotebookInstanceLifecycleConfigSortKey]
                ),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(
                    typing.Union[str, NotebookInstanceLifecycleConfigSortOrder]
                ),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                TypeInfo(datetime.datetime),
            ),
        ]

    # If the result of a `ListNotebookInstanceLifecycleConfigs` request was
    # truncated, the response includes a `NextToken`. To get the next set of
    # lifecycle configurations, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of lifecycle configurations to return in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sorts the list of results. The default is `CreationTime`.
    sort_by: typing.Union[str, "NotebookInstanceLifecycleConfigSortKey"
                         ] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )

    # The sort order for results.
    sort_order: typing.Union[str, "NotebookInstanceLifecycleConfigSortOrder"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A string in the lifecycle configuration name. This filter returns only
    # lifecycle configurations whose name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only lifecycle configurations that were created
    # before the specified time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only lifecycle configurations that were created after
    # the specified time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only lifecycle configurations that were modified
    # before the specified time (timestamp).
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only lifecycle configurations that were modified
    # after the specified time (timestamp).
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListNotebookInstanceLifecycleConfigsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "notebook_instance_lifecycle_configs",
                "NotebookInstanceLifecycleConfigs",
                TypeInfo(typing.List[NotebookInstanceLifecycleConfigSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon SageMaker returns this token. To get
    # the next set of lifecycle configurations, use it in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `NotebookInstanceLifecycleConfiguration` objects, each listing
    # a lifecycle configuration.
    notebook_instance_lifecycle_configs: typing.List[
        "NotebookInstanceLifecycleConfigSummary"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ListNotebookInstancesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, NotebookInstanceSortKey]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, NotebookInstanceSortOrder]),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_equals",
                "StatusEquals",
                TypeInfo(typing.Union[str, NotebookInstanceStatus]),
            ),
            (
                "notebook_instance_lifecycle_config_name_contains",
                "NotebookInstanceLifecycleConfigNameContains",
                TypeInfo(str),
            ),
        ]

    # If the previous call to the `ListNotebookInstances` is truncated, the
    # response includes a `NextToken`. You can use this token in your subsequent
    # `ListNotebookInstances` request to fetch the next set of notebook
    # instances.

    # You might specify a filter or a sort order in your request. When response
    # is truncated, you must use the same values for the filer and sort order in
    # the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of notebook instances to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field to sort results by. The default is `Name`.
    sort_by: typing.Union[str, "NotebookInstanceSortKey"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results.
    sort_order: typing.Union[str, "NotebookInstanceSortOrder"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # A string in the notebook instances' name. This filter returns only notebook
    # instances whose name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only notebook instances that were created before the
    # specified time (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances that were created after the
    # specified time (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances that were modified before the
    # specified time (timestamp).
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances that were modified after the
    # specified time (timestamp).
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only notebook instances with the specified status.
    status_equals: typing.Union[str, "NotebookInstanceStatus"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # A string in the name of a notebook instances lifecycle configuration
    # associated with this notebook instance. This filter returns only notebook
    # instances associated with a lifecycle configuration with a name that
    # contains the specified string.
    notebook_instance_lifecycle_config_name_contains: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListNotebookInstancesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "notebook_instances",
                "NotebookInstances",
                TypeInfo(typing.List[NotebookInstanceSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response to the previous `ListNotebookInstances` request was
    # truncated, Amazon SageMaker returns this token. To retrieve the next set of
    # notebook instances, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `NotebookInstanceSummary` objects, one for each notebook
    # instance.
    notebook_instances: typing.List["NotebookInstanceSummary"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    def paginate(
        self,
    ) -> typing.Generator["ListNotebookInstancesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource whose tags you want to
    # retrieve.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the response to the previous `ListTags` request is truncated, Amazon
    # SageMaker returns this token. To retrieve the next set of tags, use it in
    # the subsequent request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of tags to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `Tag` objects, each with a tag key and a value.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If response is truncated, Amazon SageMaker includes a token in the
    # response. You can use this token in your subsequent request to fetch next
    # set of tokens.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListTagsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTrainingJobsForHyperParameterTuningJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "status_equals",
                "StatusEquals",
                TypeInfo(typing.Union[str, TrainingJobStatus]),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, TrainingJobSortByOptions]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
        ]

    # The name of the tuning job whose training jobs you want to list.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the result of the previous `ListTrainingJobsForHyperParameterTuningJob`
    # request was truncated, the response includes a `NextToken`. To retrieve the
    # next set of training jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of training jobs to return. The default value is 10.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only training jobs with the specified status.
    status_equals: typing.Union[str, "TrainingJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The field to sort results by. The default is `Name`.

    # If the value of this field is `FinalObjectiveMetricValue`, any training
    # jobs that did not return an objective metric are not listed.
    sort_by: typing.Union[str, "TrainingJobSortByOptions"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTrainingJobsForHyperParameterTuningJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_summaries",
                "TrainingJobSummaries",
                TypeInfo(typing.List[HyperParameterTrainingJobSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of TrainingJobSummary objects that describe the training jobs that
    # the `ListTrainingJobsForHyperParameterTuningJob` request returned.
    training_job_summaries: typing.List["HyperParameterTrainingJobSummary"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # If the result of this `ListTrainingJobsForHyperParameterTuningJob` request
    # was truncated, the response includes a `NextToken`. To retrieve the next
    # set of training jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTrainingJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "status_equals",
                "StatusEquals",
                TypeInfo(typing.Union[str, TrainingJobStatus]),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, SortBy]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
        ]

    # If the result of the previous `ListTrainingJobs` request was truncated, the
    # response includes a `NextToken`. To retrieve the next set of training jobs,
    # use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of training jobs to return in the response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that returns only training jobs created after the specified time
    # (timestamp).
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only training jobs created before the specified time
    # (timestamp).
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only training jobs modified after the specified time
    # (timestamp).
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only training jobs modified before the specified time
    # (timestamp).
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string in the training job name. This filter returns only training jobs
    # whose name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that retrieves only training jobs with a specific status.
    status_equals: typing.Union[str, "TrainingJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The field to sort results by. The default is `CreationTime`.
    sort_by: typing.Union[str, "SortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Ascending`.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTrainingJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "training_job_summaries",
                "TrainingJobSummaries",
                TypeInfo(typing.List[TrainingJobSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `TrainingJobSummary` objects, each listing a training job.
    training_job_summaries: typing.List["TrainingJobSummary"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of training jobs, use it in the subsequent request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListTrainingJobsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTransformJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creation_time_after",
                "CreationTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "creation_time_before",
                "CreationTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_after",
                "LastModifiedTimeAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time_before",
                "LastModifiedTimeBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "name_contains",
                "NameContains",
                TypeInfo(str),
            ),
            (
                "status_equals",
                "StatusEquals",
                TypeInfo(typing.Union[str, TransformJobStatus]),
            ),
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, SortBy]),
            ),
            (
                "sort_order",
                "SortOrder",
                TypeInfo(typing.Union[str, SortOrder]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # A filter that returns only transform jobs created after the specified time.
    creation_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only transform jobs created before the specified
    # time.
    creation_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only transform jobs modified after the specified
    # time.
    last_modified_time_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A filter that returns only transform jobs modified before the specified
    # time.
    last_modified_time_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string in the transform job name. This filter returns only transform jobs
    # whose name contains the specified string.
    name_contains: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A filter that retrieves only transform jobs with a specific status.
    status_equals: typing.Union[str, "TransformJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The field to sort results by. The default is `CreationTime`.
    sort_by: typing.Union[str, "SortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The sort order for results. The default is `Descending`.
    sort_order: typing.Union[str, "SortOrder"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the result of the previous `ListTransformJobs` request was truncated,
    # the response includes a `NextToken`. To retrieve the next set of transform
    # jobs, use the token in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of transform jobs to return in the response. The default
    # value is `10`.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTransformJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "transform_job_summaries",
                "TransformJobSummaries",
                TypeInfo(typing.List[TransformJobSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `TransformJobSummary` objects.
    transform_job_summaries: typing.List["TransformJobSummary"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # If the response is truncated, Amazon SageMaker returns this token. To
    # retrieve the next set of transform jobs, use it in the next request.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDefinition(ShapeBase):
    """
    Specifies a metric that the training algorithm writes to `stderr` or `stdout`.
    Amazon SageMakerHyperparamter tuning captures all defined metrics. You specify
    one metric that a hyperparameter tuning job uses as its objective metric to
    choose the best training job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "regex",
                "Regex",
                TypeInfo(str),
            ),
        ]

    # The name of the metric.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A regular expression that searches the output of a training job and gets
    # the value of the metric. For more information about using regular
    # expressions to define metrics, see automatic-model-tuning-define-metrics.
    regex: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ModelArtifacts(ShapeBase):
    """
    Provides information about the location that is configured for storing model
    artifacts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_model_artifacts",
                "S3ModelArtifacts",
                TypeInfo(str),
            ),
        ]

    # The path of the S3 object that contains the model artifacts. For example,
    # `s3://bucket-name/keynameprefix/model.tar.gz`.
    s3_model_artifacts: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ModelSortKey(str):
    Name = "Name"
    CreationTime = "CreationTime"


@dataclasses.dataclass
class ModelSummary(ShapeBase):
    """
    Provides summary information about a model.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
            (
                "model_arn",
                "ModelArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the model that you want a summary for.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the model.
    model_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that indicates when the model was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class NotebookInstanceLifecycleConfigSortKey(str):
    Name = "Name"
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"


class NotebookInstanceLifecycleConfigSortOrder(str):
    Ascending = "Ascending"
    Descending = "Descending"


@dataclasses.dataclass
class NotebookInstanceLifecycleConfigSummary(ShapeBase):
    """
    Provides a summary of a notebook instance lifecycle configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "notebook_instance_lifecycle_config_arn",
                "NotebookInstanceLifecycleConfigArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the lifecycle configuration.
    notebook_instance_lifecycle_config_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that tells when the lifecycle configuration was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NotebookInstanceLifecycleHook(ShapeBase):
    """
    Contains the notebook instance lifecycle configuration script.

    Each lifecycle configuration script has a limit of 16384 characters.

    The value of the `$PATH` environment variable that is available to both scripts
    is `/sbin:bin:/usr/sbin:/usr/bin`.

    View CloudWatch Logs for notebook instance lifecycle configurations in log group
    `/aws/sagemaker/NotebookInstances` in log stream `[notebook-instance-
    name]/[LifecycleConfigHook]`.

    Lifecycle configuration scripts cannot run for longer than 5 minutes. If a
    script runs for longer than 5 minutes, it fails and the notebook instance is not
    created or started.

    For information about notebook instance lifestyle configurations, see notebook-
    lifecycle-config.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "content",
                "Content",
                TypeInfo(str),
            ),
        ]

    # A base64-encoded string that contains a shell script for a notebook
    # instance lifecycle configuration.
    content: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class NotebookInstanceSortKey(str):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class NotebookInstanceSortOrder(str):
    Ascending = "Ascending"
    Descending = "Descending"


class NotebookInstanceStatus(str):
    Pending = "Pending"
    InService = "InService"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Failed = "Failed"
    Deleting = "Deleting"
    Updating = "Updating"


@dataclasses.dataclass
class NotebookInstanceSummary(ShapeBase):
    """
    Provides summary information for an Amazon SageMaker notebook instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
            (
                "notebook_instance_arn",
                "NotebookInstanceArn",
                TypeInfo(str),
            ),
            (
                "notebook_instance_status",
                "NotebookInstanceStatus",
                TypeInfo(typing.Union[str, NotebookInstanceStatus]),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, InstanceType]),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of the notebook instance that you want a summary for.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the notebook instance.
    notebook_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the notebook instance.
    notebook_instance_status: typing.Union[str, "NotebookInstanceStatus"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # The URL that you use to connect to the Jupyter instance running in your
    # notebook instance.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of ML compute instance that the notebook instance is running on.
    instance_type: typing.Union[str, "InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the notebook instance was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the notebook instance was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of a notebook instance lifecycle configuration associated with
    # this notebook instance.

    # For information about notebook instance lifestyle configurations, see
    # notebook-lifecycle-config.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ObjectiveStatus(str):
    Succeeded = "Succeeded"
    Pending = "Pending"
    Failed = "Failed"


@dataclasses.dataclass
class ObjectiveStatusCounters(ShapeBase):
    """
    Specifies the number of training jobs that this hyperparameter tuning job
    launched, categorized by the status of their objective metric. The objective
    metric status shows whether the final objective metric for the training job has
    been evaluated by the tuning job and used in the hyperparameter tuning process.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "succeeded",
                "Succeeded",
                TypeInfo(int),
            ),
            (
                "pending",
                "Pending",
                TypeInfo(int),
            ),
            (
                "failed",
                "Failed",
                TypeInfo(int),
            ),
        ]

    # The number of training jobs whose final objective metric was evaluated by
    # the hyperparameter tuning job and used in the hyperparameter tuning
    # process.
    succeeded: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of training jobs that are in progress and pending evaluation of
    # their final objective metric.
    pending: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of training jobs whose final objective metric was not evaluated
    # and used in the hyperparameter tuning process. This typically occurs when
    # the training job failed or did not emit an objective metric.
    failed: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class OrderKey(str):
    Ascending = "Ascending"
    Descending = "Descending"


@dataclasses.dataclass
class OutputDataConfig(ShapeBase):
    """
    Provides information about how to store model training results (model
    artifacts).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_path",
                "S3OutputPath",
                TypeInfo(str),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # Identifies the S3 path where you want Amazon SageMaker to store the model
    # artifacts. For example, `s3://bucket-name/key-name-prefix`.
    s3_output_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to
    # encrypt the model artifacts at rest using Amazon S3 server-side encryption.

    # If you don't provide the KMS key ID, Amazon SageMaker uses the default KMS
    # key for Amazon S3 for your role's account. For more information, see [KMS-
    # Managed Encryption
    # Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html)
    # in Amazon Simple Storage Service developer guide.

    # The KMS key policy must grant permission to the IAM role you specify in
    # your `CreateTrainingJob` request. [Using Key Policies in AWS
    # KMS](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html) in the AWS Key Management Service Developer Guide.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterRanges(ShapeBase):
    """
    Specifies ranges of integer, continuous, and categorical hyperparameters that a
    hyperparameter tuning job searches.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "integer_parameter_ranges",
                "IntegerParameterRanges",
                TypeInfo(typing.List[IntegerParameterRange]),
            ),
            (
                "continuous_parameter_ranges",
                "ContinuousParameterRanges",
                TypeInfo(typing.List[ContinuousParameterRange]),
            ),
            (
                "categorical_parameter_ranges",
                "CategoricalParameterRanges",
                TypeInfo(typing.List[CategoricalParameterRange]),
            ),
        ]

    # The array of IntegerParameterRange objects that specify ranges of integer
    # hyperparameters that a hyperparameter tuning job searches.
    integer_parameter_ranges: typing.List["IntegerParameterRange"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The array of ContinuousParameterRange objects that specify ranges of
    # continuous hyperparameters that a hyperparameter tuning job searches.
    continuous_parameter_ranges: typing.List["ContinuousParameterRange"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # The array of CategoricalParameterRange objects that specify ranges of
    # categorical hyperparameters that a hyperparameter tuning job searches.
    categorical_parameter_ranges: typing.List["CategoricalParameterRange"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )


@dataclasses.dataclass
class ProductionVariant(ShapeBase):
    """
    Identifies a model that you want to host and the resources to deploy for hosting
    it. If you are deploying multiple models, tell Amazon SageMaker how to
    distribute traffic among the models by specifying variant weights.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variant_name",
                "VariantName",
                TypeInfo(str),
            ),
            (
                "model_name",
                "ModelName",
                TypeInfo(str),
            ),
            (
                "initial_instance_count",
                "InitialInstanceCount",
                TypeInfo(int),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, ProductionVariantInstanceType]),
            ),
            (
                "initial_variant_weight",
                "InitialVariantWeight",
                TypeInfo(float),
            ),
        ]

    # The name of the production variant.
    variant_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the model that you want to host. This is the name that you
    # specified when creating the model.
    model_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of instances to launch initially.
    initial_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ML compute instance type.
    instance_type: typing.Union[str, "ProductionVariantInstanceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Determines initial traffic distribution among all of the models that you
    # specify in the endpoint configuration. The traffic to a production variant
    # is determined by the ratio of the `VariantWeight` to the sum of all
    # `VariantWeight` values across all ProductionVariants. If unspecified, it
    # defaults to 1.0.
    initial_variant_weight: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProductionVariantInstanceType(str):
    ml_t2_medium = "ml.t2.medium"
    ml_t2_large = "ml.t2.large"
    ml_t2_xlarge = "ml.t2.xlarge"
    ml_t2_2xlarge = "ml.t2.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_c4_large = "ml.c4.large"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_large = "ml.c5.large"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"


@dataclasses.dataclass
class ProductionVariantSummary(ShapeBase):
    """
    Describes weight and capacities for a production variant associated with an
    endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API
    and the endpoint status is `Updating`, you get different desired and current
    values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "variant_name",
                "VariantName",
                TypeInfo(str),
            ),
            (
                "deployed_images",
                "DeployedImages",
                TypeInfo(typing.List[DeployedImage]),
            ),
            (
                "current_weight",
                "CurrentWeight",
                TypeInfo(float),
            ),
            (
                "desired_weight",
                "DesiredWeight",
                TypeInfo(float),
            ),
            (
                "current_instance_count",
                "CurrentInstanceCount",
                TypeInfo(int),
            ),
            (
                "desired_instance_count",
                "DesiredInstanceCount",
                TypeInfo(int),
            ),
        ]

    # The name of the variant.
    variant_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of `DeployedImage` objects that specify the Amazon EC2 Container
    # Registry paths of the inference images deployed on instances of this
    # `ProductionVariant`.
    deployed_images: typing.List["DeployedImage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The weight associated with the variant.
    current_weight: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The requested weight, as specified in the
    # `UpdateEndpointWeightsAndCapacities` request.
    desired_weight: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances associated with the variant.
    current_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of instances requested in the
    # `UpdateEndpointWeightsAndCapacities` request.
    desired_instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class RecordWrapper(str):
    NONE = "None"
    RECORDIO = "RecordIO"


@dataclasses.dataclass
class ResourceConfig(ShapeBase):
    """
    Describes the resources, including ML compute instances and ML storage volumes,
    to use for model training.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, TrainingInstanceType]),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "volume_size_in_gb",
                "VolumeSizeInGB",
                TypeInfo(int),
            ),
            (
                "volume_kms_key_id",
                "VolumeKmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The ML compute instance type.
    instance_type: typing.Union[str, "TrainingInstanceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The number of ML compute instances to use. For distributed training,
    # provide a value greater than 1.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the ML storage volume that you want to provision.

    # ML storage volumes store model artifacts and incremental states. Training
    # algorithms might also use the ML storage volume for scratch space. If you
    # want to store the training data in the ML storage volume, choose `File` as
    # the `TrainingInputMode` in the algorithm specification.

    # You must specify sufficient ML storage for your scenario.

    # Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage
    # volume type.
    volume_size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of a AWS Key Management Service key that
    # Amazon SageMaker uses to encrypt data on the storage volume attached to the
    # ML compute instance(s) that run the training job.
    volume_kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceInUse(ShapeBase):
    """
    Resource being accessed is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceLimitExceeded(ShapeBase):
    """
    You have exceeded an Amazon SageMaker resource limit. For example, you might
    have too many training jobs created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceLimits(ShapeBase):
    """
    Specifies the maximum number of training jobs and parallel training jobs that a
    hyperparameter tuning job can launch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_number_of_training_jobs",
                "MaxNumberOfTrainingJobs",
                TypeInfo(int),
            ),
            (
                "max_parallel_training_jobs",
                "MaxParallelTrainingJobs",
                TypeInfo(int),
            ),
        ]

    # The maximum number of training jobs that a hyperparameter tuning job can
    # launch.
    max_number_of_training_jobs: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of concurrent training jobs that a hyperparameter tuning
    # job can launch.
    max_parallel_training_jobs: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceNotFound(ShapeBase):
    """
    Resource being access is not found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class S3DataDistribution(str):
    FullyReplicated = "FullyReplicated"
    ShardedByS3Key = "ShardedByS3Key"


@dataclasses.dataclass
class S3DataSource(ShapeBase):
    """
    Describes the S3 data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_type",
                "S3DataType",
                TypeInfo(typing.Union[str, S3DataType]),
            ),
            (
                "s3_uri",
                "S3Uri",
                TypeInfo(str),
            ),
            (
                "s3_data_distribution_type",
                "S3DataDistributionType",
                TypeInfo(typing.Union[str, S3DataDistribution]),
            ),
        ]

    # If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon
    # SageMaker uses all objects with the specified key name prefix for model
    # training.

    # If you choose `ManifestFile`, `S3Uri` identifies an object that is a
    # manifest file containing a list of object keys that you want Amazon
    # SageMaker to use for model training.
    s3_data_type: typing.Union[str, "S3DataType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Depending on the value specified for the `S3DataType`, identifies either a
    # key name prefix or a manifest. For example:

    #   * A key name prefix might look like this: `s3://bucketname/exampleprefix`.

    #   * A manifest might look like this: `s3://bucketname/example.manifest`

    # The manifest is an S3 object which is a JSON file with the following
    # format:

    # `[`

    # ` {"prefix": "s3://customer_bucket/some/prefix/"},`

    # ` "relative/path/to/custdata-1",`

    # ` "relative/path/custdata-2",`

    # ` ...`

    # ` ]`

    # The preceding JSON matches the following `s3Uris`:

    # `s3://customer_bucket/some/prefix/relative/path/to/custdata-1`

    # `s3://customer_bucket/some/prefix/relative/path/custdata-1`

    # `...`

    # The complete set of `s3uris` in this manifest constitutes the input data
    # for the channel for this datasource. The object that each `s3uris` points
    # to must readable by the IAM role that Amazon SageMaker uses to perform
    # tasks on your behalf.
    s3_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you want Amazon SageMaker to replicate the entire dataset on each ML
    # compute instance that is launched for model training, specify
    # `FullyReplicated`.

    # If you want Amazon SageMaker to replicate a subset of data on each ML
    # compute instance that is launched for model training, specify
    # `ShardedByS3Key`. If there are _n_ ML compute instances launched for a
    # training job, each instance gets approximately 1/ _n_ of the number of S3
    # objects. In this case, model training on each machine uses only the subset
    # of training data.

    # Don't choose more ML compute instances for training than available S3
    # objects. If you do, some nodes won't get any data and you will pay for
    # nodes that aren't getting any training data. This applies in both FILE and
    # PIPE modes. Keep this in mind when developing algorithms.

    # In distributed training, where you use multiple ML compute EC2 instances,
    # you might choose `ShardedByS3Key`. If the algorithm requires copying
    # training data to the ML storage volume (when `TrainingInputMode` is set to
    # `File`), this copies 1/ _n_ of the number of objects.
    s3_data_distribution_type: typing.Union[str, "S3DataDistribution"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


class S3DataType(str):
    ManifestFile = "ManifestFile"
    S3Prefix = "S3Prefix"


class SecondaryStatus(str):
    Starting = "Starting"
    LaunchingMLInstances = "LaunchingMLInstances"
    PreparingTrainingStack = "PreparingTrainingStack"
    Downloading = "Downloading"
    DownloadingTrainingImage = "DownloadingTrainingImage"
    Training = "Training"
    Uploading = "Uploading"
    Stopping = "Stopping"
    Stopped = "Stopped"
    MaxRuntimeExceeded = "MaxRuntimeExceeded"
    Completed = "Completed"
    Failed = "Failed"


@dataclasses.dataclass
class SecondaryStatusTransition(ShapeBase):
    """
    Specifies a secondary status the job has transitioned into. It includes a start
    timestamp and later an end timestamp. The end timestamp is added either after
    the job transitions to a different secondary status or after the job has ended.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, SecondaryStatus]),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "EndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
        ]

    # Provides granular information about the system state. For more information,
    # see `SecondaryStatus` under the DescribeTrainingJob response elements.
    status: typing.Union[str, "SecondaryStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the training job has entered this secondary
    # status.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp that shows when the secondary status has ended and the job has
    # transitioned into another secondary status. The `EndTime` timestamp is also
    # set after the training job has ended.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Shows a brief description and other information about the secondary status.
    # For example, the `LaunchingMLInstances` secondary status could show a
    # status message of "Insufficent capacity error while launching instances".
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SortBy(str):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class SortOrder(str):
    Ascending = "Ascending"
    Descending = "Descending"


class SplitType(str):
    NONE = "None"
    LINE = "Line"
    RECORDIO = "RecordIO"


@dataclasses.dataclass
class StartNotebookInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the notebook instance to start.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopHyperParameterTuningJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hyper_parameter_tuning_job_name",
                "HyperParameterTuningJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the tuning job to stop.
    hyper_parameter_tuning_job_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopNotebookInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the notebook instance to terminate.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopTrainingJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the training job to stop.
    training_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopTransformJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                TypeInfo(str),
            ),
        ]

    # The name of the transform job to stop.
    transform_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StoppingCondition(ShapeBase):
    """
    Specifies how long model training can run. When model training reaches the
    limit, Amazon SageMaker ends the training job. Use this API to cap model
    training cost.

    To stop a job, Amazon SageMaker sends the algorithm the `SIGTERM` signal, which
    delays job termination for120 seconds. Algorithms might use this 120-second
    window to save the model artifacts, so the results of training is not lost.

    Training algorithms provided by Amazon SageMaker automatically saves the
    intermediate results of a model training job (it is best effort case, as model
    might not be ready to save as some stages, for example training just started).
    This intermediate data is a valid model artifact. You can use it to create a
    model (`CreateModel`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_runtime_in_seconds",
                "MaxRuntimeInSeconds",
                TypeInfo(int),
            ),
        ]

    # The maximum length of time, in seconds, that the training job can run. If
    # model training does not complete during this time, Amazon SageMaker ends
    # the job. If value is not specified, default value is 1 day. Maximum value
    # is 5 days.
    max_runtime_in_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Describes a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The tag key.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TrainingInputMode(str):
    Pipe = "Pipe"
    File = "File"


class TrainingInstanceType(str):
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"


class TrainingJobSortByOptions(str):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"
    FinalObjectiveMetricValue = "FinalObjectiveMetricValue"


class TrainingJobStatus(str):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


@dataclasses.dataclass
class TrainingJobStatusCounters(ShapeBase):
    """
    The numbers of training jobs launched by a hyperparameter tuning job,
    categorized by status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "completed",
                "Completed",
                TypeInfo(int),
            ),
            (
                "in_progress",
                "InProgress",
                TypeInfo(int),
            ),
            (
                "retryable_error",
                "RetryableError",
                TypeInfo(int),
            ),
            (
                "non_retryable_error",
                "NonRetryableError",
                TypeInfo(int),
            ),
            (
                "stopped",
                "Stopped",
                TypeInfo(int),
            ),
        ]

    # The number of completed training jobs launched by a hyperparameter tuning
    # job.
    completed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of in-progress training jobs launched by a hyperparameter tuning
    # job.
    in_progress: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of training jobs that failed, but can be retried. A failed
    # training job can be retried only if it failed because an internal service
    # error occurred.
    retryable_error: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of training jobs that failed and can't be retried. A failed
    # training job can't be retried if it failed because a client error occurred.
    non_retryable_error: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of training jobs launched by a hyperparameter tuning job that
    # were manually stopped.
    stopped: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrainingJobSummary(ShapeBase):
    """
    Provides summary information about a training job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "training_job_name",
                "TrainingJobName",
                TypeInfo(str),
            ),
            (
                "training_job_arn",
                "TrainingJobArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "training_job_status",
                "TrainingJobStatus",
                TypeInfo(typing.Union[str, TrainingJobStatus]),
            ),
            (
                "training_end_time",
                "TrainingEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the training job that you want a summary for.
    training_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the training job.
    training_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the training job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the training job.
    training_job_status: typing.Union[str, "TrainingJobStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # A timestamp that shows when the training job ended. This field is set only
    # if the training job has one of the terminal statuses (`Completed`,
    # `Failed`, or `Stopped`).
    training_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timestamp when the training job was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TransformDataSource(ShapeBase):
    """
    Describes the location of the channel data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_source",
                "S3DataSource",
                TypeInfo(TransformS3DataSource),
            ),
        ]

    # The S3 location of the data source that is associated with a channel.
    s3_data_source: "TransformS3DataSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TransformInput(ShapeBase):
    """
    Describes the input source of a transform job and the way the transform job
    consumes it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_source",
                "DataSource",
                TypeInfo(TransformDataSource),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "compression_type",
                "CompressionType",
                TypeInfo(typing.Union[str, CompressionType]),
            ),
            (
                "split_type",
                "SplitType",
                TypeInfo(typing.Union[str, SplitType]),
            ),
        ]

    # Describes the location of the channel data, meaning the S3 location of the
    # input data that the model can consume.
    data_source: "TransformDataSource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The multipurpose internet mail extension (MIME) type of the data. Amazon
    # SageMaker uses the MIME type with each http call to transfer data to the
    # transform job.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Compressing data helps save on storage space. If your transform data is
    # compressed, specify the compression type.and Amazon SageMaker will
    # automatically decompress the data for the transform job accordingly. The
    # default value is `None`.
    compression_type: typing.Union[str, "CompressionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The method to use to split the transform job's data into smaller batches.
    # The default value is `None`. If you don't want to split the data, specify
    # `None`. If you want to split records on a newline character boundary,
    # specify `Line`. To split records according to the RecordIO format, specify
    # `RecordIO`.

    # Amazon SageMaker will send maximum number of records per batch in each
    # request up to the MaxPayloadInMB limit. For more information, see [RecordIO
    # data format](http://mxnet.io/architecture/note_data_loading.html#data-
    # format).

    # For information about the `RecordIO` format, see [Data
    # Format](http://mxnet.io/architecture/note_data_loading.html#data-format).
    split_type: typing.Union[str, "SplitType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TransformInstanceType(str):
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"


class TransformJobStatus(str):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


@dataclasses.dataclass
class TransformJobSummary(ShapeBase):
    """
    Provides a summary information for a transform job. Multiple TransformJobSummary
    objects are returned as a list after calling ListTransformJobs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "transform_job_name",
                "TransformJobName",
                TypeInfo(str),
            ),
            (
                "transform_job_arn",
                "TransformJobArn",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "transform_job_status",
                "TransformJobStatus",
                TypeInfo(typing.Union[str, TransformJobStatus]),
            ),
            (
                "transform_end_time",
                "TransformEndTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "failure_reason",
                "FailureReason",
                TypeInfo(str),
            ),
        ]

    # The name of the transform job.
    transform_job_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the transform job.
    transform_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A timestamp that shows when the transform Job was created.
    creation_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the transform job.
    transform_job_status: typing.Union[str, "TransformJobStatus"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Indicates when the transform job ends on compute instances. For successful
    # jobs and stopped jobs, this is the exact time recorded after the results
    # are uploaded. For failed jobs, this is when Amazon SageMaker detected that
    # the job failed.
    transform_end_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates when the transform job was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the transform job failed, the reason it failed.
    failure_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TransformOutput(ShapeBase):
    """
    Describes the results of a transform job output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_output_path",
                "S3OutputPath",
                TypeInfo(str),
            ),
            (
                "accept",
                "Accept",
                TypeInfo(str),
            ),
            (
                "assemble_with",
                "AssembleWith",
                TypeInfo(typing.Union[str, AssemblyType]),
            ),
            (
                "kms_key_id",
                "KmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The Amazon S3 path where you want Amazon SageMaker to store the results of
    # the transform job. For example, `s3://bucket-name/key-name-prefix`.

    # For every S3 object used as input for the transform job, the transformed
    # data is stored in a corresponding subfolder in the location under the
    # output prefix. For example, the input data `s3://bucket-name/input-name-
    # prefix/dataset01/data.csv` will have the transformed data stored at
    # `s3://bucket-name/key-name-prefix/dataset01/`, based on the original name,
    # as a series of .part files (.part0001, part0002, etc).
    s3_output_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MIME type used to specify the output data. Amazon SageMaker uses the
    # MIME type with each http call to transfer data from the transform job.
    accept: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Defines how to assemble the results of the transform job as a single S3
    # object. You should select a format that is most convenient to you. To
    # concatenate the results in binary format, specify `None`. To add a newline
    # character at the end of every transformed record, specify `Line`. To
    # assemble the output in RecordIO format, specify `RecordIO`. The default
    # value is `None`.

    # For information about the `RecordIO` format, see [Data
    # Format](http://mxnet.io/architecture/note_data_loading.html#data-format).
    assemble_with: typing.Union[str, "AssemblyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Key Management Service (AWS KMS) key for Amazon S3 server-side
    # encryption that Amazon SageMaker uses to encrypt the transformed data.

    # If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS
    # key for Amazon S3 for your role's account. For more information, see [KMS-
    # Managed Encryption
    # Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html)
    # in the _Amazon Simple Storage Service Developer Guide._

    # The KMS key policy must grant permission to the IAM role that you specify
    # in your `CreateTramsformJob` request. For more information, see [Using Key
    # Policies in AWS
    # KMS](http://docs.aws.amazon.com/kms/latest/developerguide/key-
    # policies.html) in the _AWS Key Management Service Developer Guide_.
    kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TransformResources(ShapeBase):
    """
    Describes the resources, including ML instance types and ML instance count, to
    use for transform job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, TransformInstanceType]),
            ),
            (
                "instance_count",
                "InstanceCount",
                TypeInfo(int),
            ),
            (
                "volume_kms_key_id",
                "VolumeKmsKeyId",
                TypeInfo(str),
            ),
        ]

    # The ML compute instance type for the transform job. For using built-in
    # algorithms to transform moderately sized datasets, ml.m4.xlarge or
    # `ml.m5.large` should suffice. There is no default value for `InstanceType`.
    instance_type: typing.Union[str, "TransformInstanceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # The number of ML compute instances to use in the transform job. For
    # distributed transform, provide a value greater than 1. The default value is
    # `1`.
    instance_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of a AWS Key Management Service key that
    # Amazon SageMaker uses to encrypt data on the storage volume attached to the
    # ML compute instance(s) that run the batch transform job.
    volume_kms_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TransformS3DataSource(ShapeBase):
    """
    Describes the S3 data source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_data_type",
                "S3DataType",
                TypeInfo(typing.Union[str, S3DataType]),
            ),
            (
                "s3_uri",
                "S3Uri",
                TypeInfo(str),
            ),
        ]

    # If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon
    # SageMaker uses all objects with the specified key name prefix for batch
    # transform.

    # If you choose `ManifestFile`, `S3Uri` identifies an object that is a
    # manifest file containing a list of object keys that you want Amazon
    # SageMaker to use for batch transform.
    s3_data_type: typing.Union[str, "S3DataType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Depending on the value specified for the `S3DataType`, identifies either a
    # key name prefix or a manifest. For example:

    #   * A key name prefix might look like this: `s3://bucketname/exampleprefix`.

    #   * A manifest might look like this: `s3://bucketname/example.manifest`

    # The manifest is an S3 object which is a JSON file with the following
    # format:

    # `[`

    # ` {"prefix": "s3://customer_bucket/some/prefix/"},`

    # ` "relative/path/to/custdata-1",`

    # ` "relative/path/custdata-2",`

    # ` ...`

    # ` ]`

    # The preceding JSON matches the following `S3Uris`:

    # `s3://customer_bucket/some/prefix/relative/path/to/custdata-1`

    # `s3://customer_bucket/some/prefix/relative/path/custdata-1`

    # `...`

    # The complete set of `S3Uris` in this manifest constitutes the input data
    # for the channel for this datasource. The object that each `S3Uris` points
    # to must be readable by the IAM role that Amazon SageMaker uses to perform
    # tasks on your behalf.
    s3_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEndpointInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "endpoint_config_name",
                "EndpointConfigName",
                TypeInfo(str),
            ),
        ]

    # The name of the endpoint whose configuration you want to update.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the new endpoint configuration.
    endpoint_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEndpointOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEndpointWeightsAndCapacitiesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_name",
                "EndpointName",
                TypeInfo(str),
            ),
            (
                "desired_weights_and_capacities",
                "DesiredWeightsAndCapacities",
                TypeInfo(typing.List[DesiredWeightAndCapacity]),
            ),
        ]

    # The name of an existing Amazon SageMaker endpoint.
    endpoint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object that provides new capacity and weight values for a variant.
    desired_weights_and_capacities: typing.List["DesiredWeightAndCapacity"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )


@dataclasses.dataclass
class UpdateEndpointWeightsAndCapacitiesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_arn",
                "EndpointArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the updated endpoint.
    endpoint_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNotebookInstanceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_name",
                "NotebookInstanceName",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "InstanceType",
                TypeInfo(typing.Union[str, InstanceType]),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "lifecycle_config_name",
                "LifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "disassociate_lifecycle_config",
                "DisassociateLifecycleConfig",
                TypeInfo(bool),
            ),
        ]

    # The name of the notebook instance to update.
    notebook_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon ML compute instance type.
    instance_type: typing.Union[str, "InstanceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can
    # assume to access the notebook instance. For more information, see [Amazon
    # SageMaker Roles](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-
    # roles.html).

    # To be able to pass this role to Amazon SageMaker, the caller of this API
    # must have the `iam:PassRole` permission.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a lifecycle configuration to associate with the notebook
    # instance. For information about lifestyle configurations, see notebook-
    # lifecycle-config.
    lifecycle_config_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to `true` to remove the notebook instance lifecycle configuration
    # currently associated with the notebook instance.
    disassociate_lifecycle_config: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateNotebookInstanceLifecycleConfigInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notebook_instance_lifecycle_config_name",
                "NotebookInstanceLifecycleConfigName",
                TypeInfo(str),
            ),
            (
                "on_create",
                "OnCreate",
                TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
            (
                "on_start",
                "OnStart",
                TypeInfo(typing.List[NotebookInstanceLifecycleHook]),
            ),
        ]

    # The name of the lifecycle configuration.
    notebook_instance_lifecycle_config_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shell script that runs only once, when you create a notebook instance
    on_create: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The shell script that runs every time you start a notebook instance,
    # including when you create the notebook instance.
    on_start: typing.List["NotebookInstanceLifecycleHook"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateNotebookInstanceLifecycleConfigOutput(OutputShapeBase):
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
class UpdateNotebookInstanceOutput(OutputShapeBase):
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
class VpcConfig(ShapeBase):
    """
    Specifies a VPC that your training jobs and hosted models have access to.
    Control access to and from your training and model containers by configuring the
    VPC. For more information, see host-vpc and train-vpc.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group_ids",
                "SecurityGroupIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "subnets",
                "Subnets",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security
    # groups for the VPC that is specified in the `Subnets` field.
    security_group_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the subnets in the VPC to which you want to connect your training
    # job or model.
    subnets: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
