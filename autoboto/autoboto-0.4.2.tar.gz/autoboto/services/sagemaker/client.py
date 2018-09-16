import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("sagemaker", *args, **kwargs)

    def add_tags(
        self,
        _request: shapes.AddTagsInput = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsOutput:
        """
        Adds or overwrites one or more tags for the specified Amazon SageMaker resource.
        You can add tags to notebook instances, training jobs, models, endpoint
        configurations, and endpoints.

        Each tag consists of a key and an optional value. Tag keys must be unique per
        resource. For more information about tags, see [Using Cost Allocation
        Tags](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-
        tags.html#allocation-what) in the _AWS Billing and Cost Management User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsInput(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsOutput.from_boto(response)

    def create_endpoint(
        self,
        _request: shapes.CreateEndpointInput = None,
        *,
        endpoint_name: str,
        endpoint_config_name: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateEndpointOutput:
        """
        Creates an endpoint using the endpoint configuration specified in the request.
        Amazon SageMaker uses the endpoint to provision resources and deploy models. You
        create the endpoint configuration with the
        [CreateEndpointConfig](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html)
        API.

        Use this API only for hosting models using Amazon SageMaker hosting services.

        The endpoint name must be unique within an AWS Region in your AWS account.

        When it receives the request, Amazon SageMaker creates the endpoint, launches
        the resources (ML compute instances), and deploys the model(s) on them.

        When Amazon SageMaker receives the request, it sets the endpoint status to
        `Creating`. After it creates the endpoint, it sets the status to `InService`.
        Amazon SageMaker can then process incoming requests for inferences. To check the
        status of an endpoint, use the
        [DescribeEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html)
        API.

        For an example, see [Exercise 1: Using the K-Means Algorithm Provided by Amazon
        SageMaker](http://docs.aws.amazon.com/sagemaker/latest/dg/ex1.html).

        If any of the models hosted at this endpoint get model data from an Amazon S3
        location, Amazon SageMaker uses AWS Security Token Service to download model
        artifacts from the S3 path you provided. AWS STS is activated in your IAM user
        account by default. If you previously deactivated AWS STS for a region, you need
        to reactivate AWS STS for that region. For more information, see [Activating and
        Deactivating AWS STS i an AWS
        Region](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-
        regions.html) in the _AWS Identity and Access Management User Guide_.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if endpoint_config_name is not ShapeBase.NOT_SET:
                _params['endpoint_config_name'] = endpoint_config_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateEndpointInput(**_params)
        response = self._boto_client.create_endpoint(**_request.to_boto())

        return shapes.CreateEndpointOutput.from_boto(response)

    def create_endpoint_config(
        self,
        _request: shapes.CreateEndpointConfigInput = None,
        *,
        endpoint_config_name: str,
        production_variants: typing.List[shapes.ProductionVariant],
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateEndpointConfigOutput:
        """
        Creates an endpoint configuration that Amazon SageMaker hosting services uses to
        deploy models. In the configuration, you identify one or more models, created
        using the `CreateModel` API, to deploy and the resources that you want Amazon
        SageMaker to provision. Then you call the
        [CreateEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html)
        API.

        Use this API only if you want to use Amazon SageMaker hosting services to deploy
        models into production.

        In the request, you define one or more `ProductionVariant`s, each of which
        identifies a model. Each `ProductionVariant` parameter also describes the
        resources that you want Amazon SageMaker to provision. This includes the number
        and type of ML compute instances to deploy.

        If you are hosting multiple models, you also assign a `VariantWeight` to specify
        how much traffic you want to allocate to each model. For example, suppose that
        you want to host two models, A and B, and you assign traffic weight 2 for model
        A and 1 for model B. Amazon SageMaker distributes two-thirds of the traffic to
        Model A, and one-third to model B.
        """
        if _request is None:
            _params = {}
            if endpoint_config_name is not ShapeBase.NOT_SET:
                _params['endpoint_config_name'] = endpoint_config_name
            if production_variants is not ShapeBase.NOT_SET:
                _params['production_variants'] = production_variants
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            _request = shapes.CreateEndpointConfigInput(**_params)
        response = self._boto_client.create_endpoint_config(
            **_request.to_boto()
        )

        return shapes.CreateEndpointConfigOutput.from_boto(response)

    def create_hyper_parameter_tuning_job(
        self,
        _request: shapes.CreateHyperParameterTuningJobRequest = None,
        *,
        hyper_parameter_tuning_job_name: str,
        hyper_parameter_tuning_job_config: shapes.HyperParameterTuningJobConfig,
        training_job_definition: shapes.HyperParameterTrainingJobDefinition,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateHyperParameterTuningJobResponse:
        """
        Starts a hyperparameter tuning job.
        """
        if _request is None:
            _params = {}
            if hyper_parameter_tuning_job_name is not ShapeBase.NOT_SET:
                _params['hyper_parameter_tuning_job_name'
                       ] = hyper_parameter_tuning_job_name
            if hyper_parameter_tuning_job_config is not ShapeBase.NOT_SET:
                _params['hyper_parameter_tuning_job_config'
                       ] = hyper_parameter_tuning_job_config
            if training_job_definition is not ShapeBase.NOT_SET:
                _params['training_job_definition'] = training_job_definition
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateHyperParameterTuningJobRequest(**_params)
        response = self._boto_client.create_hyper_parameter_tuning_job(
            **_request.to_boto()
        )

        return shapes.CreateHyperParameterTuningJobResponse.from_boto(response)

    def create_model(
        self,
        _request: shapes.CreateModelInput = None,
        *,
        model_name: str,
        primary_container: shapes.ContainerDefinition,
        execution_role_arn: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
    ) -> shapes.CreateModelOutput:
        """
        Creates a model in Amazon SageMaker. In the request, you name the model and
        describe a primary container. For the primary container, you specify the docker
        image containing inference code, artifacts (from prior training), and custom
        environment map that the inference code uses when you deploy the model for
        predictions.

        Use this API to create a model if you want to use Amazon SageMaker hosting
        services or run a batch transform job.

        To host your model, you create an endpoint configuration with the
        `CreateEndpointConfig` API, and then create an endpoint with the
        `CreateEndpoint` API. Amazon SageMaker then deploys all of the containers that
        you defined for the model in the hosting environment.

        To run a batch transform using your model, you start a job with the
        `CreateTransformJob` API. Amazon SageMaker uses your model and your dataset to
        get inferences which are then saved to a specified S3 location.

        In the `CreateModel` request, you must define a container with the
        `PrimaryContainer` parameter.

        In the request, you also provide an IAM role that Amazon SageMaker can assume to
        access model artifacts and docker image for deployment on ML compute hosting
        instances or for batch transform jobs. In addition, you also use the IAM role to
        manage permissions the inference code needs. For example, if the inference code
        access any other AWS resources, you grant necessary permissions via this role.
        """
        if _request is None:
            _params = {}
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            if primary_container is not ShapeBase.NOT_SET:
                _params['primary_container'] = primary_container
            if execution_role_arn is not ShapeBase.NOT_SET:
                _params['execution_role_arn'] = execution_role_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            _request = shapes.CreateModelInput(**_params)
        response = self._boto_client.create_model(**_request.to_boto())

        return shapes.CreateModelOutput.from_boto(response)

    def create_notebook_instance(
        self,
        _request: shapes.CreateNotebookInstanceInput = None,
        *,
        notebook_instance_name: str,
        instance_type: typing.Union[str, shapes.InstanceType],
        role_arn: str,
        subnet_id: str = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        lifecycle_config_name: str = ShapeBase.NOT_SET,
        direct_internet_access: typing.
        Union[str, shapes.DirectInternetAccess] = ShapeBase.NOT_SET,
    ) -> shapes.CreateNotebookInstanceOutput:
        """
        Creates an Amazon SageMaker notebook instance. A notebook instance is a machine
        learning (ML) compute instance running on a Jupyter notebook.

        In a `CreateNotebookInstance` request, specify the type of ML compute instance
        that you want to run. Amazon SageMaker launches the instance, installs common
        libraries that you can use to explore datasets for model training, and attaches
        an ML storage volume to the notebook instance.

        Amazon SageMaker also provides a set of example notebooks. Each notebook
        demonstrates how to use Amazon SageMaker with a specific algorithm or with a
        machine learning framework.

        After receiving the request, Amazon SageMaker does the following:

          1. Creates a network interface in the Amazon SageMaker VPC.

          2. (Option) If you specified `SubnetId`, Amazon SageMaker creates a network interface in your own VPC, which is inferred from the subnet ID that you provide in the input. When creating this network interface, Amazon SageMaker attaches the security group that you specified in the request to the network interface that it creates in your VPC.

          3. Launches an EC2 instance of the type specified in the request in the Amazon SageMaker VPC. If you specified `SubnetId` of your VPC, Amazon SageMaker specifies both network interfaces when launching this instance. This enables inbound traffic from your own VPC to the notebook instance, assuming that the security groups allow it.

        After creating the notebook instance, Amazon SageMaker returns its Amazon
        Resource Name (ARN).

        After Amazon SageMaker creates the notebook instance, you can connect to the
        Jupyter server and work in Jupyter notebooks. For example, you can write code to
        explore a dataset that you can use for model training, train a model, host
        models by creating Amazon SageMaker endpoints, and validate hosted models.

        For more information, see [How It
        Works](http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html).
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if lifecycle_config_name is not ShapeBase.NOT_SET:
                _params['lifecycle_config_name'] = lifecycle_config_name
            if direct_internet_access is not ShapeBase.NOT_SET:
                _params['direct_internet_access'] = direct_internet_access
            _request = shapes.CreateNotebookInstanceInput(**_params)
        response = self._boto_client.create_notebook_instance(
            **_request.to_boto()
        )

        return shapes.CreateNotebookInstanceOutput.from_boto(response)

    def create_notebook_instance_lifecycle_config(
        self,
        _request: shapes.CreateNotebookInstanceLifecycleConfigInput = None,
        *,
        notebook_instance_lifecycle_config_name: str,
        on_create: typing.List[shapes.NotebookInstanceLifecycleHook
                              ] = ShapeBase.NOT_SET,
        on_start: typing.List[shapes.NotebookInstanceLifecycleHook
                             ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateNotebookInstanceLifecycleConfigOutput:
        """
        Creates a lifecycle configuration that you can associate with a notebook
        instance. A _lifecycle configuration_ is a collection of shell scripts that run
        when you create or start a notebook instance.

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
        if _request is None:
            _params = {}
            if notebook_instance_lifecycle_config_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_lifecycle_config_name'
                       ] = notebook_instance_lifecycle_config_name
            if on_create is not ShapeBase.NOT_SET:
                _params['on_create'] = on_create
            if on_start is not ShapeBase.NOT_SET:
                _params['on_start'] = on_start
            _request = shapes.CreateNotebookInstanceLifecycleConfigInput(
                **_params
            )
        response = self._boto_client.create_notebook_instance_lifecycle_config(
            **_request.to_boto()
        )

        return shapes.CreateNotebookInstanceLifecycleConfigOutput.from_boto(
            response
        )

    def create_presigned_notebook_instance_url(
        self,
        _request: shapes.CreatePresignedNotebookInstanceUrlInput = None,
        *,
        notebook_instance_name: str,
        session_expiration_duration_in_seconds: int = ShapeBase.NOT_SET,
    ) -> shapes.CreatePresignedNotebookInstanceUrlOutput:
        """
        Returns a URL that you can use to connect to the Jupyter server from a notebook
        instance. In the Amazon SageMaker console, when you choose `Open` next to a
        notebook instance, Amazon SageMaker opens a new tab showing the Jupyter server
        home page from the notebook instance. The console uses this API to get the URL
        and show the page.

        You can restrict access to this API and to the URL that it returns to a list of
        IP addresses that you specify. To restrict access, attach an IAM policy that
        denies access to this API unless the call comes from an IP address in the
        specified list to every AWS Identity and Access Management user, group, or role
        used to access the notebook instance. Use the `NotIpAddress` condition operator
        and the `aws:SourceIP` condition context key to specify the list of IP addresses
        that you want to have access to the notebook instance. For more information, see
        nbi-ip-filter.
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            if session_expiration_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['session_expiration_duration_in_seconds'
                       ] = session_expiration_duration_in_seconds
            _request = shapes.CreatePresignedNotebookInstanceUrlInput(**_params)
        response = self._boto_client.create_presigned_notebook_instance_url(
            **_request.to_boto()
        )

        return shapes.CreatePresignedNotebookInstanceUrlOutput.from_boto(
            response
        )

    def create_training_job(
        self,
        _request: shapes.CreateTrainingJobRequest = None,
        *,
        training_job_name: str,
        algorithm_specification: shapes.AlgorithmSpecification,
        role_arn: str,
        input_data_config: typing.List[shapes.Channel],
        output_data_config: shapes.OutputDataConfig,
        resource_config: shapes.ResourceConfig,
        stopping_condition: shapes.StoppingCondition,
        hyper_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        vpc_config: shapes.VpcConfig = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateTrainingJobResponse:
        """
        Starts a model training job. After training completes, Amazon SageMaker saves
        the resulting model artifacts to an Amazon S3 location that you specify.

        If you choose to host your model using Amazon SageMaker hosting services, you
        can use the resulting model artifacts as part of the model. You can also use the
        artifacts in a deep learning service other than Amazon SageMaker, provided that
        you know how to use them for inferences.

        In the request body, you provide the following:

          * `AlgorithmSpecification` \- Identifies the training algorithm to use. 

          * `HyperParameters` \- Specify these algorithm-specific parameters to influence the quality of the final model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see [Algorithms](http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). 

          * `InputDataConfig` \- Describes the training dataset and the Amazon S3 location where it is stored.

          * `OutputDataConfig` \- Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training. 

          * `ResourceConfig` \- Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training. In distributed training, you specify more than one instance. 

          * `RoleARN` \- The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during model training. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete model training. 

          * `StoppingCondition` \- Sets a duration for training. Use this parameter to cap model training costs. 

        For more information about Amazon SageMaker, see [How It
        Works](http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html).
        """
        if _request is None:
            _params = {}
            if training_job_name is not ShapeBase.NOT_SET:
                _params['training_job_name'] = training_job_name
            if algorithm_specification is not ShapeBase.NOT_SET:
                _params['algorithm_specification'] = algorithm_specification
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if input_data_config is not ShapeBase.NOT_SET:
                _params['input_data_config'] = input_data_config
            if output_data_config is not ShapeBase.NOT_SET:
                _params['output_data_config'] = output_data_config
            if resource_config is not ShapeBase.NOT_SET:
                _params['resource_config'] = resource_config
            if stopping_condition is not ShapeBase.NOT_SET:
                _params['stopping_condition'] = stopping_condition
            if hyper_parameters is not ShapeBase.NOT_SET:
                _params['hyper_parameters'] = hyper_parameters
            if vpc_config is not ShapeBase.NOT_SET:
                _params['vpc_config'] = vpc_config
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateTrainingJobRequest(**_params)
        response = self._boto_client.create_training_job(**_request.to_boto())

        return shapes.CreateTrainingJobResponse.from_boto(response)

    def create_transform_job(
        self,
        _request: shapes.CreateTransformJobRequest = None,
        *,
        transform_job_name: str,
        model_name: str,
        transform_input: shapes.TransformInput,
        transform_output: shapes.TransformOutput,
        transform_resources: shapes.TransformResources,
        max_concurrent_transforms: int = ShapeBase.NOT_SET,
        max_payload_in_mb: int = ShapeBase.NOT_SET,
        batch_strategy: typing.Union[str, shapes.BatchStrategy] = ShapeBase.
        NOT_SET,
        environment: typing.Dict[str, str] = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateTransformJobResponse:
        """
        Starts a transform job. A transform job uses a trained model to get inferences
        on a dataset and saves these results to an Amazon S3 location that you specify.

        To perform batch transformations, you create a transform job and use the data
        that you have readily available.

        In the request body, you provide the following:

          * `TransformJobName` \- Identifies the transform job. The name must be unique within an AWS Region in an AWS account.

          * `ModelName` \- Identifies the model to use. `ModelName` must be the name of an existing Amazon SageMaker model in the same AWS Region and AWS account. For information on creating a model, see CreateModel.

          * `TransformInput` \- Describes the dataset to be transformed and the Amazon S3 location where it is stored.

          * `TransformOutput` \- Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.

          * `TransformResources` \- Identifies the ML compute instances for the transform job.

        For more information about how batch transformation works Amazon SageMaker, see
        [How It Works](http://docs.aws.amazon.com/sagemaker/latest/dg/batch-
        transform.html).
        """
        if _request is None:
            _params = {}
            if transform_job_name is not ShapeBase.NOT_SET:
                _params['transform_job_name'] = transform_job_name
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            if transform_input is not ShapeBase.NOT_SET:
                _params['transform_input'] = transform_input
            if transform_output is not ShapeBase.NOT_SET:
                _params['transform_output'] = transform_output
            if transform_resources is not ShapeBase.NOT_SET:
                _params['transform_resources'] = transform_resources
            if max_concurrent_transforms is not ShapeBase.NOT_SET:
                _params['max_concurrent_transforms'] = max_concurrent_transforms
            if max_payload_in_mb is not ShapeBase.NOT_SET:
                _params['max_payload_in_mb'] = max_payload_in_mb
            if batch_strategy is not ShapeBase.NOT_SET:
                _params['batch_strategy'] = batch_strategy
            if environment is not ShapeBase.NOT_SET:
                _params['environment'] = environment
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateTransformJobRequest(**_params)
        response = self._boto_client.create_transform_job(**_request.to_boto())

        return shapes.CreateTransformJobResponse.from_boto(response)

    def delete_endpoint(
        self,
        _request: shapes.DeleteEndpointInput = None,
        *,
        endpoint_name: str,
    ) -> None:
        """
        Deletes an endpoint. Amazon SageMaker frees up all of the resources that were
        deployed when the endpoint was created.

        Amazon SageMaker retires any custom KMS key grants associated with the endpoint,
        meaning you don't need to use the
        [RevokeGrant](http://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html)
        API call.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            _request = shapes.DeleteEndpointInput(**_params)
        response = self._boto_client.delete_endpoint(**_request.to_boto())

    def delete_endpoint_config(
        self,
        _request: shapes.DeleteEndpointConfigInput = None,
        *,
        endpoint_config_name: str,
    ) -> None:
        """
        Deletes an endpoint configuration. The `DeleteEndpointConfig` API deletes only
        the specified configuration. It does not delete endpoints created using the
        configuration.
        """
        if _request is None:
            _params = {}
            if endpoint_config_name is not ShapeBase.NOT_SET:
                _params['endpoint_config_name'] = endpoint_config_name
            _request = shapes.DeleteEndpointConfigInput(**_params)
        response = self._boto_client.delete_endpoint_config(
            **_request.to_boto()
        )

    def delete_model(
        self,
        _request: shapes.DeleteModelInput = None,
        *,
        model_name: str,
    ) -> None:
        """
        Deletes a model. The `DeleteModel` API deletes only the model entry that was
        created in Amazon SageMaker when you called the
        [CreateModel](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateModel.html)
        API. It does not delete model artifacts, inference code, or the IAM role that
        you specified when creating the model.
        """
        if _request is None:
            _params = {}
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            _request = shapes.DeleteModelInput(**_params)
        response = self._boto_client.delete_model(**_request.to_boto())

    def delete_notebook_instance(
        self,
        _request: shapes.DeleteNotebookInstanceInput = None,
        *,
        notebook_instance_name: str,
    ) -> None:
        """
        Deletes an Amazon SageMaker notebook instance. Before you can delete a notebook
        instance, you must call the `StopNotebookInstance` API.

        When you delete a notebook instance, you lose all of your data. Amazon SageMaker
        removes the ML compute instance, and deletes the ML storage volume and the
        network interface associated with the notebook instance.
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            _request = shapes.DeleteNotebookInstanceInput(**_params)
        response = self._boto_client.delete_notebook_instance(
            **_request.to_boto()
        )

    def delete_notebook_instance_lifecycle_config(
        self,
        _request: shapes.DeleteNotebookInstanceLifecycleConfigInput = None,
        *,
        notebook_instance_lifecycle_config_name: str,
    ) -> None:
        """
        Deletes a notebook instance lifecycle configuration.
        """
        if _request is None:
            _params = {}
            if notebook_instance_lifecycle_config_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_lifecycle_config_name'
                       ] = notebook_instance_lifecycle_config_name
            _request = shapes.DeleteNotebookInstanceLifecycleConfigInput(
                **_params
            )
        response = self._boto_client.delete_notebook_instance_lifecycle_config(
            **_request.to_boto()
        )

    def delete_tags(
        self,
        _request: shapes.DeleteTagsInput = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.DeleteTagsOutput:
        """
        Deletes the specified tags from an Amazon SageMaker resource.

        To list a resource's tags, use the `ListTags` API.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.DeleteTagsInput(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

        return shapes.DeleteTagsOutput.from_boto(response)

    def describe_endpoint(
        self,
        _request: shapes.DescribeEndpointInput = None,
        *,
        endpoint_name: str,
    ) -> shapes.DescribeEndpointOutput:
        """
        Returns the description of an endpoint.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            _request = shapes.DescribeEndpointInput(**_params)
        response = self._boto_client.describe_endpoint(**_request.to_boto())

        return shapes.DescribeEndpointOutput.from_boto(response)

    def describe_endpoint_config(
        self,
        _request: shapes.DescribeEndpointConfigInput = None,
        *,
        endpoint_config_name: str,
    ) -> shapes.DescribeEndpointConfigOutput:
        """
        Returns the description of an endpoint configuration created using the
        `CreateEndpointConfig` API.
        """
        if _request is None:
            _params = {}
            if endpoint_config_name is not ShapeBase.NOT_SET:
                _params['endpoint_config_name'] = endpoint_config_name
            _request = shapes.DescribeEndpointConfigInput(**_params)
        response = self._boto_client.describe_endpoint_config(
            **_request.to_boto()
        )

        return shapes.DescribeEndpointConfigOutput.from_boto(response)

    def describe_hyper_parameter_tuning_job(
        self,
        _request: shapes.DescribeHyperParameterTuningJobRequest = None,
        *,
        hyper_parameter_tuning_job_name: str,
    ) -> shapes.DescribeHyperParameterTuningJobResponse:
        """
        Gets a description of a hyperparameter tuning job.
        """
        if _request is None:
            _params = {}
            if hyper_parameter_tuning_job_name is not ShapeBase.NOT_SET:
                _params['hyper_parameter_tuning_job_name'
                       ] = hyper_parameter_tuning_job_name
            _request = shapes.DescribeHyperParameterTuningJobRequest(**_params)
        response = self._boto_client.describe_hyper_parameter_tuning_job(
            **_request.to_boto()
        )

        return shapes.DescribeHyperParameterTuningJobResponse.from_boto(
            response
        )

    def describe_model(
        self,
        _request: shapes.DescribeModelInput = None,
        *,
        model_name: str,
    ) -> shapes.DescribeModelOutput:
        """
        Describes a model that you created using the `CreateModel` API.
        """
        if _request is None:
            _params = {}
            if model_name is not ShapeBase.NOT_SET:
                _params['model_name'] = model_name
            _request = shapes.DescribeModelInput(**_params)
        response = self._boto_client.describe_model(**_request.to_boto())

        return shapes.DescribeModelOutput.from_boto(response)

    def describe_notebook_instance(
        self,
        _request: shapes.DescribeNotebookInstanceInput = None,
        *,
        notebook_instance_name: str,
    ) -> shapes.DescribeNotebookInstanceOutput:
        """
        Returns information about a notebook instance.
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            _request = shapes.DescribeNotebookInstanceInput(**_params)
        response = self._boto_client.describe_notebook_instance(
            **_request.to_boto()
        )

        return shapes.DescribeNotebookInstanceOutput.from_boto(response)

    def describe_notebook_instance_lifecycle_config(
        self,
        _request: shapes.DescribeNotebookInstanceLifecycleConfigInput = None,
        *,
        notebook_instance_lifecycle_config_name: str,
    ) -> shapes.DescribeNotebookInstanceLifecycleConfigOutput:
        """
        Returns a description of a notebook instance lifecycle configuration.

        For information about notebook instance lifestyle configurations, see notebook-
        lifecycle-config.
        """
        if _request is None:
            _params = {}
            if notebook_instance_lifecycle_config_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_lifecycle_config_name'
                       ] = notebook_instance_lifecycle_config_name
            _request = shapes.DescribeNotebookInstanceLifecycleConfigInput(
                **_params
            )
        response = self._boto_client.describe_notebook_instance_lifecycle_config(
            **_request.to_boto()
        )

        return shapes.DescribeNotebookInstanceLifecycleConfigOutput.from_boto(
            response
        )

    def describe_training_job(
        self,
        _request: shapes.DescribeTrainingJobRequest = None,
        *,
        training_job_name: str,
    ) -> shapes.DescribeTrainingJobResponse:
        """
        Returns information about a training job.
        """
        if _request is None:
            _params = {}
            if training_job_name is not ShapeBase.NOT_SET:
                _params['training_job_name'] = training_job_name
            _request = shapes.DescribeTrainingJobRequest(**_params)
        response = self._boto_client.describe_training_job(**_request.to_boto())

        return shapes.DescribeTrainingJobResponse.from_boto(response)

    def describe_transform_job(
        self,
        _request: shapes.DescribeTransformJobRequest = None,
        *,
        transform_job_name: str,
    ) -> shapes.DescribeTransformJobResponse:
        """
        Returns information about a transform job.
        """
        if _request is None:
            _params = {}
            if transform_job_name is not ShapeBase.NOT_SET:
                _params['transform_job_name'] = transform_job_name
            _request = shapes.DescribeTransformJobRequest(**_params)
        response = self._boto_client.describe_transform_job(
            **_request.to_boto()
        )

        return shapes.DescribeTransformJobResponse.from_boto(response)

    def list_endpoint_configs(
        self,
        _request: shapes.ListEndpointConfigsInput = None,
        *,
        sort_by: typing.Union[str, shapes.EndpointConfigSortKey] = ShapeBase.
        NOT_SET,
        sort_order: typing.Union[str, shapes.OrderKey] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.ListEndpointConfigsOutput:
        """
        Lists endpoint configurations.
        """
        if _request is None:
            _params = {}
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            _request = shapes.ListEndpointConfigsInput(**_params)
        paginator = self.get_paginator("list_endpoint_configs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListEndpointConfigsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListEndpointConfigsOutput.from_boto(response)

    def list_endpoints(
        self,
        _request: shapes.ListEndpointsInput = None,
        *,
        sort_by: typing.Union[str, shapes.EndpointSortKey] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.OrderKey] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_before: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_after: datetime.datetime = ShapeBase.NOT_SET,
        status_equals: typing.Union[str, shapes.EndpointStatus] = ShapeBase.
        NOT_SET,
    ) -> shapes.ListEndpointsOutput:
        """
        Lists endpoints.
        """
        if _request is None:
            _params = {}
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            if last_modified_time_before is not ShapeBase.NOT_SET:
                _params['last_modified_time_before'] = last_modified_time_before
            if last_modified_time_after is not ShapeBase.NOT_SET:
                _params['last_modified_time_after'] = last_modified_time_after
            if status_equals is not ShapeBase.NOT_SET:
                _params['status_equals'] = status_equals
            _request = shapes.ListEndpointsInput(**_params)
        paginator = self.get_paginator("list_endpoints").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListEndpointsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListEndpointsOutput.from_boto(response)

    def list_hyper_parameter_tuning_jobs(
        self,
        _request: shapes.ListHyperParameterTuningJobsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.HyperParameterTuningJobSortByOptions
                             ] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_after: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_before: datetime.datetime = ShapeBase.NOT_SET,
        status_equals: typing.
        Union[str, shapes.HyperParameterTuningJobStatus] = ShapeBase.NOT_SET,
    ) -> shapes.ListHyperParameterTuningJobsResponse:
        """
        Gets a list of HyperParameterTuningJobSummary objects that describe the
        hyperparameter tuning jobs launched in your account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if last_modified_time_after is not ShapeBase.NOT_SET:
                _params['last_modified_time_after'] = last_modified_time_after
            if last_modified_time_before is not ShapeBase.NOT_SET:
                _params['last_modified_time_before'] = last_modified_time_before
            if status_equals is not ShapeBase.NOT_SET:
                _params['status_equals'] = status_equals
            _request = shapes.ListHyperParameterTuningJobsRequest(**_params)
        response = self._boto_client.list_hyper_parameter_tuning_jobs(
            **_request.to_boto()
        )

        return shapes.ListHyperParameterTuningJobsResponse.from_boto(response)

    def list_models(
        self,
        _request: shapes.ListModelsInput = None,
        *,
        sort_by: typing.Union[str, shapes.ModelSortKey] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.OrderKey] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.ListModelsOutput:
        """
        Lists models created with the
        [CreateModel](http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateModel.html)
        API.
        """
        if _request is None:
            _params = {}
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            _request = shapes.ListModelsInput(**_params)
        paginator = self.get_paginator("list_models").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListModelsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListModelsOutput.from_boto(response)

    def list_notebook_instance_lifecycle_configs(
        self,
        _request: shapes.ListNotebookInstanceLifecycleConfigsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.NotebookInstanceLifecycleConfigSortKey
                             ] = ShapeBase.NOT_SET,
        sort_order: typing.
        Union[str, shapes.
              NotebookInstanceLifecycleConfigSortOrder] = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_before: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_after: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.ListNotebookInstanceLifecycleConfigsOutput:
        """
        Lists notebook instance lifestyle configurations created with the
        CreateNotebookInstanceLifecycleConfig API.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            if last_modified_time_before is not ShapeBase.NOT_SET:
                _params['last_modified_time_before'] = last_modified_time_before
            if last_modified_time_after is not ShapeBase.NOT_SET:
                _params['last_modified_time_after'] = last_modified_time_after
            _request = shapes.ListNotebookInstanceLifecycleConfigsInput(
                **_params
            )
        response = self._boto_client.list_notebook_instance_lifecycle_configs(
            **_request.to_boto()
        )

        return shapes.ListNotebookInstanceLifecycleConfigsOutput.from_boto(
            response
        )

    def list_notebook_instances(
        self,
        _request: shapes.ListNotebookInstancesInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.
                              NotebookInstanceSortKey] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.
                                 NotebookInstanceSortOrder] = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_before: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_after: datetime.datetime = ShapeBase.NOT_SET,
        status_equals: typing.Union[str, shapes.
                                    NotebookInstanceStatus] = ShapeBase.NOT_SET,
        notebook_instance_lifecycle_config_name_contains: str = ShapeBase.
        NOT_SET,
    ) -> shapes.ListNotebookInstancesOutput:
        """
        Returns a list of the Amazon SageMaker notebook instances in the requester's
        account in an AWS Region.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            if last_modified_time_before is not ShapeBase.NOT_SET:
                _params['last_modified_time_before'] = last_modified_time_before
            if last_modified_time_after is not ShapeBase.NOT_SET:
                _params['last_modified_time_after'] = last_modified_time_after
            if status_equals is not ShapeBase.NOT_SET:
                _params['status_equals'] = status_equals
            if notebook_instance_lifecycle_config_name_contains is not ShapeBase.NOT_SET:
                _params['notebook_instance_lifecycle_config_name_contains'
                       ] = notebook_instance_lifecycle_config_name_contains
            _request = shapes.ListNotebookInstancesInput(**_params)
        paginator = self.get_paginator("list_notebook_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListNotebookInstancesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListNotebookInstancesOutput.from_boto(response)

    def list_tags(
        self,
        _request: shapes.ListTagsInput = None,
        *,
        resource_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsOutput:
        """
        Returns the tags for the specified Amazon SageMaker resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTagsInput(**_params)
        paginator = self.get_paginator("list_tags").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTagsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTagsOutput.from_boto(response)

    def list_training_jobs(
        self,
        _request: shapes.ListTrainingJobsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_after: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_before: datetime.datetime = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        status_equals: typing.Union[str, shapes.TrainingJobStatus] = ShapeBase.
        NOT_SET,
        sort_by: typing.Union[str, shapes.SortBy] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
    ) -> shapes.ListTrainingJobsResponse:
        """
        Lists training jobs.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if last_modified_time_after is not ShapeBase.NOT_SET:
                _params['last_modified_time_after'] = last_modified_time_after
            if last_modified_time_before is not ShapeBase.NOT_SET:
                _params['last_modified_time_before'] = last_modified_time_before
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if status_equals is not ShapeBase.NOT_SET:
                _params['status_equals'] = status_equals
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            _request = shapes.ListTrainingJobsRequest(**_params)
        paginator = self.get_paginator("list_training_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTrainingJobsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTrainingJobsResponse.from_boto(response)

    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        _request: shapes.
        ListTrainingJobsForHyperParameterTuningJobRequest = None,
        *,
        hyper_parameter_tuning_job_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        status_equals: typing.Union[str, shapes.
                                    TrainingJobStatus] = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.
                              TrainingJobSortByOptions] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
    ) -> shapes.ListTrainingJobsForHyperParameterTuningJobResponse:
        """
        Gets a list of TrainingJobSummary objects that describe the training jobs that a
        hyperparameter tuning job launched.
        """
        if _request is None:
            _params = {}
            if hyper_parameter_tuning_job_name is not ShapeBase.NOT_SET:
                _params['hyper_parameter_tuning_job_name'
                       ] = hyper_parameter_tuning_job_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if status_equals is not ShapeBase.NOT_SET:
                _params['status_equals'] = status_equals
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            _request = shapes.ListTrainingJobsForHyperParameterTuningJobRequest(
                **_params
            )
        response = self._boto_client.list_training_jobs_for_hyper_parameter_tuning_job(
            **_request.to_boto()
        )

        return shapes.ListTrainingJobsForHyperParameterTuningJobResponse.from_boto(
            response
        )

    def list_transform_jobs(
        self,
        _request: shapes.ListTransformJobsRequest = None,
        *,
        creation_time_after: datetime.datetime = ShapeBase.NOT_SET,
        creation_time_before: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_after: datetime.datetime = ShapeBase.NOT_SET,
        last_modified_time_before: datetime.datetime = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
        status_equals: typing.Union[str, shapes.TransformJobStatus] = ShapeBase.
        NOT_SET,
        sort_by: typing.Union[str, shapes.SortBy] = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTransformJobsResponse:
        """
        Lists transform jobs.
        """
        if _request is None:
            _params = {}
            if creation_time_after is not ShapeBase.NOT_SET:
                _params['creation_time_after'] = creation_time_after
            if creation_time_before is not ShapeBase.NOT_SET:
                _params['creation_time_before'] = creation_time_before
            if last_modified_time_after is not ShapeBase.NOT_SET:
                _params['last_modified_time_after'] = last_modified_time_after
            if last_modified_time_before is not ShapeBase.NOT_SET:
                _params['last_modified_time_before'] = last_modified_time_before
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            if status_equals is not ShapeBase.NOT_SET:
                _params['status_equals'] = status_equals
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTransformJobsRequest(**_params)
        response = self._boto_client.list_transform_jobs(**_request.to_boto())

        return shapes.ListTransformJobsResponse.from_boto(response)

    def start_notebook_instance(
        self,
        _request: shapes.StartNotebookInstanceInput = None,
        *,
        notebook_instance_name: str,
    ) -> None:
        """
        Launches an ML compute instance with the latest version of the libraries and
        attaches your ML storage volume. After configuring the notebook instance, Amazon
        SageMaker sets the notebook instance status to `InService`. A notebook
        instance's status must be `InService` before you can connect to your Jupyter
        notebook.
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            _request = shapes.StartNotebookInstanceInput(**_params)
        response = self._boto_client.start_notebook_instance(
            **_request.to_boto()
        )

    def stop_hyper_parameter_tuning_job(
        self,
        _request: shapes.StopHyperParameterTuningJobRequest = None,
        *,
        hyper_parameter_tuning_job_name: str,
    ) -> None:
        """
        Stops a running hyperparameter tuning job and all running training jobs that the
        tuning job launched.

        All model artifacts output from the training jobs are stored in Amazon Simple
        Storage Service (Amazon S3). All data that the training jobs write to Amazon
        CloudWatch Logs are still available in CloudWatch. After the tuning job moves to
        the `Stopped` state, it releases all reserved resources for the tuning job.
        """
        if _request is None:
            _params = {}
            if hyper_parameter_tuning_job_name is not ShapeBase.NOT_SET:
                _params['hyper_parameter_tuning_job_name'
                       ] = hyper_parameter_tuning_job_name
            _request = shapes.StopHyperParameterTuningJobRequest(**_params)
        response = self._boto_client.stop_hyper_parameter_tuning_job(
            **_request.to_boto()
        )

    def stop_notebook_instance(
        self,
        _request: shapes.StopNotebookInstanceInput = None,
        *,
        notebook_instance_name: str,
    ) -> None:
        """
        Terminates the ML compute instance. Before terminating the instance, Amazon
        SageMaker disconnects the ML storage volume from it. Amazon SageMaker preserves
        the ML storage volume.

        To access data on the ML storage volume for a notebook instance that has been
        terminated, call the `StartNotebookInstance` API. `StartNotebookInstance`
        launches another ML compute instance, configures it, and attaches the preserved
        ML storage volume so you can continue your work.
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            _request = shapes.StopNotebookInstanceInput(**_params)
        response = self._boto_client.stop_notebook_instance(
            **_request.to_boto()
        )

    def stop_training_job(
        self,
        _request: shapes.StopTrainingJobRequest = None,
        *,
        training_job_name: str,
    ) -> None:
        """
        Stops a training job. To stop a job, Amazon SageMaker sends the algorithm the
        `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms might
        use this 120-second window to save the model artifacts, so the results of the
        training is not lost.

        Training algorithms provided by Amazon SageMaker save the intermediate results
        of a model training job. This intermediate data is a valid model artifact. You
        can use the model artifacts that are saved when Amazon SageMaker stops a
        training job to create a model.

        When it receives a `StopTrainingJob` request, Amazon SageMaker changes the
        status of the job to `Stopping`. After Amazon SageMaker stops the job, it sets
        the status to `Stopped`.
        """
        if _request is None:
            _params = {}
            if training_job_name is not ShapeBase.NOT_SET:
                _params['training_job_name'] = training_job_name
            _request = shapes.StopTrainingJobRequest(**_params)
        response = self._boto_client.stop_training_job(**_request.to_boto())

    def stop_transform_job(
        self,
        _request: shapes.StopTransformJobRequest = None,
        *,
        transform_job_name: str,
    ) -> None:
        """
        Stops a transform job.

        When Amazon SageMaker receives a `StopTransformJob` request, the status of the
        job changes to `Stopping`. After Amazon SageMaker stops the job, the status is
        set to `Stopped`. When you stop a transform job before it is completed, Amazon
        SageMaker doesn't store the job's output in Amazon S3.
        """
        if _request is None:
            _params = {}
            if transform_job_name is not ShapeBase.NOT_SET:
                _params['transform_job_name'] = transform_job_name
            _request = shapes.StopTransformJobRequest(**_params)
        response = self._boto_client.stop_transform_job(**_request.to_boto())

    def update_endpoint(
        self,
        _request: shapes.UpdateEndpointInput = None,
        *,
        endpoint_name: str,
        endpoint_config_name: str,
    ) -> shapes.UpdateEndpointOutput:
        """
        Deploys the new `EndpointConfig` specified in the request, switches to using
        newly created endpoint, and then deletes resources provisioned for the endpoint
        using the previous `EndpointConfig` (there is no availability loss).

        When Amazon SageMaker receives the request, it sets the endpoint status to
        `Updating`. After updating the endpoint, it sets the status to `InService`. To
        check the status of an endpoint, use the
        [DescribeEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html)
        API.

        You cannot update an endpoint with the current `EndpointConfig`. To update an
        endpoint, you must create a new `EndpointConfig`.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if endpoint_config_name is not ShapeBase.NOT_SET:
                _params['endpoint_config_name'] = endpoint_config_name
            _request = shapes.UpdateEndpointInput(**_params)
        response = self._boto_client.update_endpoint(**_request.to_boto())

        return shapes.UpdateEndpointOutput.from_boto(response)

    def update_endpoint_weights_and_capacities(
        self,
        _request: shapes.UpdateEndpointWeightsAndCapacitiesInput = None,
        *,
        endpoint_name: str,
        desired_weights_and_capacities: typing.List[shapes.
                                                    DesiredWeightAndCapacity],
    ) -> shapes.UpdateEndpointWeightsAndCapacitiesOutput:
        """
        Updates variant weight of one or more variants associated with an existing
        endpoint, or capacity of one variant associated with an existing endpoint. When
        it receives the request, Amazon SageMaker sets the endpoint status to
        `Updating`. After updating the endpoint, it sets the status to `InService`. To
        check the status of an endpoint, use the
        [DescribeEndpoint](http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html)
        API.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if desired_weights_and_capacities is not ShapeBase.NOT_SET:
                _params['desired_weights_and_capacities'
                       ] = desired_weights_and_capacities
            _request = shapes.UpdateEndpointWeightsAndCapacitiesInput(**_params)
        response = self._boto_client.update_endpoint_weights_and_capacities(
            **_request.to_boto()
        )

        return shapes.UpdateEndpointWeightsAndCapacitiesOutput.from_boto(
            response
        )

    def update_notebook_instance(
        self,
        _request: shapes.UpdateNotebookInstanceInput = None,
        *,
        notebook_instance_name: str,
        instance_type: typing.Union[str, shapes.InstanceType] = ShapeBase.
        NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
        lifecycle_config_name: str = ShapeBase.NOT_SET,
        disassociate_lifecycle_config: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateNotebookInstanceOutput:
        """
        Updates a notebook instance. NotebookInstance updates include upgrading or
        downgrading the ML compute instance used for your notebook instance to
        accommodate changes in your workload requirements. You can also update the VPC
        security groups.
        """
        if _request is None:
            _params = {}
            if notebook_instance_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_name'] = notebook_instance_name
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if lifecycle_config_name is not ShapeBase.NOT_SET:
                _params['lifecycle_config_name'] = lifecycle_config_name
            if disassociate_lifecycle_config is not ShapeBase.NOT_SET:
                _params['disassociate_lifecycle_config'
                       ] = disassociate_lifecycle_config
            _request = shapes.UpdateNotebookInstanceInput(**_params)
        response = self._boto_client.update_notebook_instance(
            **_request.to_boto()
        )

        return shapes.UpdateNotebookInstanceOutput.from_boto(response)

    def update_notebook_instance_lifecycle_config(
        self,
        _request: shapes.UpdateNotebookInstanceLifecycleConfigInput = None,
        *,
        notebook_instance_lifecycle_config_name: str,
        on_create: typing.List[shapes.NotebookInstanceLifecycleHook
                              ] = ShapeBase.NOT_SET,
        on_start: typing.List[shapes.NotebookInstanceLifecycleHook
                             ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateNotebookInstanceLifecycleConfigOutput:
        """
        Updates a notebook instance lifecycle configuration created with the
        CreateNotebookInstanceLifecycleConfig API.
        """
        if _request is None:
            _params = {}
            if notebook_instance_lifecycle_config_name is not ShapeBase.NOT_SET:
                _params['notebook_instance_lifecycle_config_name'
                       ] = notebook_instance_lifecycle_config_name
            if on_create is not ShapeBase.NOT_SET:
                _params['on_create'] = on_create
            if on_start is not ShapeBase.NOT_SET:
                _params['on_start'] = on_start
            _request = shapes.UpdateNotebookInstanceLifecycleConfigInput(
                **_params
            )
        response = self._boto_client.update_notebook_instance_lifecycle_config(
            **_request.to_boto()
        )

        return shapes.UpdateNotebookInstanceLifecycleConfigOutput.from_boto(
            response
        )
