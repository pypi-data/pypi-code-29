import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class ActivatePipelineInput(ShapeBase):
    """
    Contains the parameters for ActivatePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "parameter_values",
                "parameterValues",
                TypeInfo(typing.List[ParameterValue]),
            ),
            (
                "start_timestamp",
                "startTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of parameter values to pass to the pipeline at activation.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time to resume the pipeline. By default, the pipeline resumes
    # from the last completed execution.
    start_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ActivatePipelineOutput(OutputShapeBase):
    """
    Contains the output of ActivatePipeline.
    """

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
class AddTagsInput(ShapeBase):
    """
    Contains the parameters for AddTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to add, as key/value pairs.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsOutput(OutputShapeBase):
    """
    Contains the output of AddTags.
    """

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
class CreatePipelineInput(ShapeBase):
    """
    Contains the parameters for CreatePipeline.
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
                "unique_id",
                "uniqueId",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The name for the pipeline. You can use the same name for multiple pipelines
    # associated with your AWS account, because AWS Data Pipeline assigns each
    # pipeline a unique pipeline identifier.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier. This identifier is not the same as the pipeline
    # identifier assigned by AWS Data Pipeline. You are responsible for defining
    # the format and ensuring the uniqueness of this identifier. You use this
    # parameter to ensure idempotency during repeated calls to `CreatePipeline`.
    # For example, if the first call to `CreatePipeline` does not succeed, you
    # can pass in the same unique identifier and pipeline name combination on a
    # subsequent call to `CreatePipeline`. `CreatePipeline` ensures that if a
    # pipeline already exists with the same name and unique identifier, a new
    # pipeline is not created. Instead, you'll receive the pipeline identifier
    # from the previous attempt. The uniqueness of the name and unique identifier
    # combination is scoped to the AWS account or IAM user credentials.
    unique_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description for the pipeline.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to associate with the pipeline at creation. Tags let you
    # control access to pipelines. For more information, see [Controlling User
    # Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePipelineOutput(OutputShapeBase):
    """
    Contains the output of CreatePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID that AWS Data Pipeline assigns the newly created pipeline. For
    # example, `df-06372391ZG65EXAMPLE`.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeactivatePipelineInput(ShapeBase):
    """
    Contains the parameters for DeactivatePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "cancel_active",
                "cancelActive",
                TypeInfo(bool),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether to cancel any running objects. The default is true, which
    # sets the state of any running objects to `CANCELED`. If this value is
    # false, the pipeline is deactivated after all running objects finish.
    cancel_active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeactivatePipelineOutput(OutputShapeBase):
    """
    Contains the output of DeactivatePipeline.
    """

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
class DeletePipelineInput(ShapeBase):
    """
    Contains the parameters for DeletePipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeObjectsInput(ShapeBase):
    """
    Contains the parameters for DescribeObjects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "object_ids",
                "objectIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "evaluate_expressions",
                "evaluateExpressions",
                TypeInfo(bool),
            ),
            (
                "marker",
                "marker",
                TypeInfo(str),
            ),
        ]

    # The ID of the pipeline that contains the object definitions.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the pipeline objects that contain the definitions to be
    # described. You can pass as many as 25 identifiers in a single call to
    # `DescribeObjects`.
    object_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether any expressions in the object should be evaluated when
    # the object descriptions are returned.
    evaluate_expressions: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting point for the results to be returned. For the first call, this
    # value should be empty. As long as there are more results, continue to call
    # `DescribeObjects` with the marker value from the previous call to retrieve
    # the next set of results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeObjectsOutput(OutputShapeBase):
    """
    Contains the output of DescribeObjects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_objects",
                "pipelineObjects",
                TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "marker",
                "marker",
                TypeInfo(str),
            ),
            (
                "has_more_results",
                "hasMoreResults",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of object definitions.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The starting point for the next page of results. To view the next page of
    # results, call `DescribeObjects` again with this marker value. If the value
    # is null, there are no more results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether there are more results to return.
    has_more_results: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["DescribeObjectsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribePipelinesInput(ShapeBase):
    """
    Contains the parameters for DescribePipelines.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_ids",
                "pipelineIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The IDs of the pipelines to describe. You can pass as many as 25
    # identifiers in a single call. To obtain pipeline IDs, call ListPipelines.
    pipeline_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribePipelinesOutput(OutputShapeBase):
    """
    Contains the output of DescribePipelines.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_description_list",
                "pipelineDescriptionList",
                TypeInfo(typing.List[PipelineDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of descriptions for the specified pipelines.
    pipeline_description_list: typing.List["PipelineDescription"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class EvaluateExpressionInput(ShapeBase):
    """
    Contains the parameters for EvaluateExpression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "object_id",
                "objectId",
                TypeInfo(str),
            ),
            (
                "expression",
                "expression",
                TypeInfo(str),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the object.
    object_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The expression to evaluate.
    expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EvaluateExpressionOutput(OutputShapeBase):
    """
    Contains the output of EvaluateExpression.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "evaluated_expression",
                "evaluatedExpression",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The evaluated expression.
    evaluated_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Field(ShapeBase):
    """
    A key-value pair that describes a property of a pipeline object. The value is
    specified as either a string value (`StringValue`) or a reference to another
    object (`RefValue`) but not as both.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "string_value",
                "stringValue",
                TypeInfo(str),
            ),
            (
                "ref_value",
                "refValue",
                TypeInfo(str),
            ),
        ]

    # The field identifier.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field value, expressed as a String.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field value, expressed as the identifier of another object.
    ref_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPipelineDefinitionInput(ShapeBase):
    """
    Contains the parameters for GetPipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the pipeline definition to retrieve. Set this parameter to
    # `latest` (default) to use the last definition saved to the pipeline or
    # `active` to use the last definition that was activated.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPipelineDefinitionOutput(OutputShapeBase):
    """
    Contains the output of GetPipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_objects",
                "pipelineObjects",
                TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "parameter_objects",
                "parameterObjects",
                TypeInfo(typing.List[ParameterObject]),
            ),
            (
                "parameter_values",
                "parameterValues",
                TypeInfo(typing.List[ParameterValue]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The objects defined in the pipeline.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter objects used in the pipeline definition.
    parameter_objects: typing.List["ParameterObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter values used in the pipeline definition.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceIdentity(ShapeBase):
    """
    Identity information for the EC2 instance that is hosting the task runner. You
    can get this value by calling a metadata URI from the EC2 instance. For more
    information, see [Instance
    Metadata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-
    instancedata.html) in the _Amazon Elastic Compute Cloud User Guide._ Passing in
    this value proves that your task runner is running on an EC2 instance, and
    ensures the proper AWS Data Pipeline service charges are applied to your
    pipeline.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "document",
                "document",
                TypeInfo(str),
            ),
            (
                "signature",
                "signature",
                TypeInfo(str),
            ),
        ]

    # A description of an EC2 instance that is generated when the instance is
    # launched and exposed to the instance via the instance metadata service in
    # the form of a JSON representation of an object.
    document: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A signature which can be used to verify the accuracy and authenticity of
    # the information provided in the instance identity document.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceError(ShapeBase):
    """
    An internal service error occurred.
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

    # Description of the error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """
    The request was not valid. Verify that your request was properly formatted, that
    the signature was generated with the correct credentials, and that you haven't
    exceeded any of the service limits for your account.
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

    # Description of the error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelinesInput(ShapeBase):
    """
    Contains the parameters for ListPipelines.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "marker",
                TypeInfo(str),
            ),
        ]

    # The starting point for the results to be returned. For the first call, this
    # value should be empty. As long as there are more results, continue to call
    # `ListPipelines` with the marker value from the previous call to retrieve
    # the next set of results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPipelinesOutput(OutputShapeBase):
    """
    Contains the output of ListPipelines.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "pipeline_id_list",
                "pipelineIdList",
                TypeInfo(typing.List[PipelineIdName]),
            ),
            (
                "marker",
                "marker",
                TypeInfo(str),
            ),
            (
                "has_more_results",
                "hasMoreResults",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pipeline identifiers. If you require additional information about the
    # pipelines, you can use these identifiers to call DescribePipelines and
    # GetPipelineDefinition.
    pipeline_id_list: typing.List["PipelineIdName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The starting point for the next page of results. To view the next page of
    # results, call `ListPipelinesOutput` again with this marker value. If the
    # value is null, there are no more results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether there are more results that can be obtained by a
    # subsequent call.
    has_more_results: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListPipelinesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Operator(ShapeBase):
    """
    Contains a logical operation for comparing the value of a field with a specified
    value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, OperatorType]),
            ),
            (
                "values",
                "values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The logical operation to be performed: equal (`EQ`), equal reference
    # (`REF_EQ`), less than or equal (`LE`), greater than or equal (`GE`), or
    # between (`BETWEEN`). Equal reference (`REF_EQ`) can be used only with
    # reference fields. The other comparison types can be used only with String
    # fields. The comparison types you can use apply only to certain object
    # fields, as detailed below.

    # The comparison operators EQ and REF_EQ act on the following fields:

    #   * name
    #   * @sphere
    #   * parent
    #   * @componentParent
    #   * @instanceParent
    #   * @status
    #   * @scheduledStartTime
    #   * @scheduledEndTime
    #   * @actualStartTime
    #   * @actualEndTime

    # The comparison operators `GE`, `LE`, and `BETWEEN` act on the following
    # fields:

    #   * @scheduledStartTime
    #   * @scheduledEndTime
    #   * @actualStartTime
    #   * @actualEndTime

    # Note that fields beginning with the at sign (@) are read-only and set by
    # the web service. When you name fields, you should choose names containing
    # only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline.
    # User-defined fields that you add to a pipeline should prefix their name
    # with the string "my".
    type: typing.Union[str, "OperatorType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value that the actual field value will be compared with.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class OperatorType(str):
    EQ = "EQ"
    REF_EQ = "REF_EQ"
    LE = "LE"
    GE = "GE"
    BETWEEN = "BETWEEN"


@dataclasses.dataclass
class ParameterAttribute(ShapeBase):
    """
    The attributes allowed or specified with a parameter object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "string_value",
                "stringValue",
                TypeInfo(str),
            ),
        ]

    # The field identifier.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field value, expressed as a String.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterObject(ShapeBase):
    """
    Contains information about a parameter object.
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
                "attributes",
                "attributes",
                TypeInfo(typing.List[ParameterAttribute]),
            ),
        ]

    # The ID of the parameter object.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes of the parameter object.
    attributes: typing.List["ParameterAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ParameterValue(ShapeBase):
    """
    A value or list of parameter values.
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
                "string_value",
                "stringValue",
                TypeInfo(str),
            ),
        ]

    # The ID of the parameter value.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field value, expressed as a String.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineDeletedException(ShapeBase):
    """
    The specified pipeline has been deleted.
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

    # Description of the error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineDescription(ShapeBase):
    """
    Contains pipeline metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "fields",
                "fields",
                TypeInfo(typing.List[Field]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The pipeline identifier that was assigned by AWS Data Pipeline. This is a
    # string of the form `df-297EG78HU43EEXAMPLE`.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the pipeline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of read-only fields that contain metadata about the pipeline:
    # @userId, @accountId, and @pipelineState.
    fields: typing.List["Field"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Description of the pipeline.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tags to associated with a pipeline. Tags let you control access
    # to pipelines. For more information, see [Controlling User Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineIdName(ShapeBase):
    """
    Contains the name and identifier of a pipeline.
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
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The ID of the pipeline that was assigned by AWS Data Pipeline. This is a
    # string of the form `df-297EG78HU43EEXAMPLE`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the pipeline.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineNotFoundException(ShapeBase):
    """
    The specified pipeline was not found. Verify that you used the correct user and
    account identifiers.
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

    # Description of the error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PipelineObject(ShapeBase):
    """
    Contains information about a pipeline object. This can be a logical, physical,
    or physical attempt pipeline object. The complete set of components of a
    pipeline defines the pipeline.
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
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "fields",
                "fields",
                TypeInfo(typing.List[Field]),
            ),
        ]

    # The ID of the object.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the object.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key-value pairs that define the properties of the object.
    fields: typing.List["Field"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PollForTaskInput(ShapeBase):
    """
    Contains the parameters for PollForTask.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "worker_group",
                "workerGroup",
                TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                TypeInfo(str),
            ),
            (
                "instance_identity",
                "instanceIdentity",
                TypeInfo(InstanceIdentity),
            ),
        ]

    # The type of task the task runner is configured to accept and process. The
    # worker group is set as a field on objects in the pipeline when they are
    # created. You can only specify a single value for `workerGroup` in the call
    # to `PollForTask`. There are no wildcard values permitted in `workerGroup`;
    # the string must be an exact, case-sensitive, match.
    worker_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public DNS name of the calling task runner.
    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identity information for the EC2 instance that is hosting the task runner.
    # You can get this value from the instance using
    # `http://169.254.169.254/latest/meta-data/instance-id`. For more
    # information, see [Instance
    # Metadata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-
    # instancedata.html) in the _Amazon Elastic Compute Cloud User Guide._
    # Passing in this value proves that your task runner is running on an EC2
    # instance, and ensures the proper AWS Data Pipeline service charges are
    # applied to your pipeline.
    instance_identity: "InstanceIdentity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PollForTaskOutput(OutputShapeBase):
    """
    Contains the output of PollForTask.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "task_object",
                "taskObject",
                TypeInfo(TaskObject),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The information needed to complete the task that is being assigned to the
    # task runner. One of the fields returned in this object is `taskId`, which
    # contains an identifier for the task being assigned. The calling task runner
    # uses `taskId` in subsequent calls to ReportTaskProgress and SetTaskStatus.
    task_object: "TaskObject" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutPipelineDefinitionInput(ShapeBase):
    """
    Contains the parameters for PutPipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "pipeline_objects",
                "pipelineObjects",
                TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "parameter_objects",
                "parameterObjects",
                TypeInfo(typing.List[ParameterObject]),
            ),
            (
                "parameter_values",
                "parameterValues",
                TypeInfo(typing.List[ParameterValue]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The objects that define the pipeline. These objects overwrite the existing
    # pipeline definition.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter objects used with the pipeline.
    parameter_objects: typing.List["ParameterObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter values used with the pipeline.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutPipelineDefinitionOutput(OutputShapeBase):
    """
    Contains the output of PutPipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "errored",
                "errored",
                TypeInfo(bool),
            ),
            (
                "validation_errors",
                "validationErrors",
                TypeInfo(typing.List[ValidationError]),
            ),
            (
                "validation_warnings",
                "validationWarnings",
                TypeInfo(typing.List[ValidationWarning]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether there were validation errors, and the pipeline definition
    # is stored but cannot be activated until you correct the pipeline and call
    # `PutPipelineDefinition` to commit the corrected pipeline.
    errored: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The validation errors that are associated with the objects defined in
    # `pipelineObjects`.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The validation warnings that are associated with the objects defined in
    # `pipelineObjects`.
    validation_warnings: typing.List["ValidationWarning"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Query(ShapeBase):
    """
    Defines the query to run against an object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "selectors",
                "selectors",
                TypeInfo(typing.List[Selector]),
            ),
        ]

    # List of selectors that define the query. An object must satisfy all of the
    # selectors to match the query.
    selectors: typing.List["Selector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QueryObjectsInput(ShapeBase):
    """
    Contains the parameters for QueryObjects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "sphere",
                "sphere",
                TypeInfo(str),
            ),
            (
                "query",
                "query",
                TypeInfo(Query),
            ),
            (
                "marker",
                "marker",
                TypeInfo(str),
            ),
            (
                "limit",
                "limit",
                TypeInfo(int),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the query applies to components or instances. The
    # possible values are: `COMPONENT`, `INSTANCE`, and `ATTEMPT`.
    sphere: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The query that defines the objects to be returned. The `Query` object can
    # contain a maximum of ten selectors. The conditions in the query are limited
    # to top-level String fields in the object. These filters can be applied to
    # components, instances, and attempts.
    query: "Query" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting point for the results to be returned. For the first call, this
    # value should be empty. As long as there are more results, continue to call
    # `QueryObjects` with the marker value from the previous call to retrieve the
    # next set of results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of object names that `QueryObjects` will return in a
    # single call. The default value is 100.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryObjectsOutput(OutputShapeBase):
    """
    Contains the output of QueryObjects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ids",
                "ids",
                TypeInfo(typing.List[str]),
            ),
            (
                "marker",
                "marker",
                TypeInfo(str),
            ),
            (
                "has_more_results",
                "hasMoreResults",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifiers that match the query selectors.
    ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting point for the next page of results. To view the next page of
    # results, call `QueryObjects` again with this marker value. If the value is
    # null, there are no more results.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether there are more results that can be obtained by a
    # subsequent call.
    has_more_results: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["QueryObjectsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class RemoveTagsInput(ShapeBase):
    """
    Contains the parameters for RemoveTags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "tagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The keys of the tags to remove.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsOutput(OutputShapeBase):
    """
    Contains the output of RemoveTags.
    """

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
class ReportTaskProgressInput(ShapeBase):
    """
    Contains the parameters for ReportTaskProgress.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
            (
                "fields",
                "fields",
                TypeInfo(typing.List[Field]),
            ),
        ]

    # The ID of the task assigned to the task runner. This value is provided in
    # the response for PollForTask.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Key-value pairs that define the properties of the ReportTaskProgressInput
    # object.
    fields: typing.List["Field"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReportTaskProgressOutput(OutputShapeBase):
    """
    Contains the output of ReportTaskProgress.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "canceled",
                "canceled",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If true, the calling task runner should cancel processing of the task. The
    # task runner does not need to call SetTaskStatus for canceled tasks.
    canceled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReportTaskRunnerHeartbeatInput(ShapeBase):
    """
    Contains the parameters for ReportTaskRunnerHeartbeat.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "taskrunner_id",
                "taskrunnerId",
                TypeInfo(str),
            ),
            (
                "worker_group",
                "workerGroup",
                TypeInfo(str),
            ),
            (
                "hostname",
                "hostname",
                TypeInfo(str),
            ),
        ]

    # The ID of the task runner. This value should be unique across your AWS
    # account. In the case of AWS Data Pipeline Task Runner launched on a
    # resource managed by AWS Data Pipeline, the web service provides a unique
    # identifier when it launches the application. If you have written a custom
    # task runner, you should assign a unique identifier for the task runner.
    taskrunner_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of task the task runner is configured to accept and process. The
    # worker group is set as a field on objects in the pipeline when they are
    # created. You can only specify a single value for `workerGroup`. There are
    # no wildcard values permitted in `workerGroup`; the string must be an exact,
    # case-sensitive, match.
    worker_group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public DNS name of the task runner.
    hostname: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReportTaskRunnerHeartbeatOutput(OutputShapeBase):
    """
    Contains the output of ReportTaskRunnerHeartbeat.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "terminate",
                "terminate",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the calling task runner should terminate.
    terminate: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Selector(ShapeBase):
    """
    A comparision that is used to determine whether a query should return this
    object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_name",
                "fieldName",
                TypeInfo(str),
            ),
            (
                "operator",
                "operator",
                TypeInfo(Operator),
            ),
        ]

    # The name of the field that the operator will be applied to. The field name
    # is the "key" portion of the field definition in the pipeline definition
    # syntax that is used by the AWS Data Pipeline API. If the field is not set
    # on the object, the condition fails.
    field_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains a logical operation for comparing the value of a field with a
    # specified value.
    operator: "Operator" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetStatusInput(ShapeBase):
    """
    Contains the parameters for SetStatus.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "object_ids",
                "objectIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "status",
                TypeInfo(str),
            ),
        ]

    # The ID of the pipeline that contains the objects.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IDs of the objects. The corresponding objects can be either physical or
    # components, but not a mix of both types.
    object_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status to be set on all the objects specified in `objectIds`. For
    # components, use `PAUSE` or `RESUME`. For instances, use `TRY_CANCEL`,
    # `RERUN`, or `MARK_FINISHED`.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTaskStatusInput(ShapeBase):
    """
    Contains the parameters for SetTaskStatus.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
            (
                "task_status",
                "taskStatus",
                TypeInfo(typing.Union[str, TaskStatus]),
            ),
            (
                "error_id",
                "errorId",
                TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                TypeInfo(str),
            ),
            (
                "error_stack_trace",
                "errorStackTrace",
                TypeInfo(str),
            ),
        ]

    # The ID of the task assigned to the task runner. This value is provided in
    # the response for PollForTask.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `FINISHED`, the task successfully completed. If `FAILED`, the task ended
    # unsuccessfully. Preconditions use false.
    task_status: typing.Union[str, "TaskStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If an error occurred during the task, this value specifies the error code.
    # This value is set on the physical attempt object. It is used to display
    # error information to the user. It should not start with string "Service_"
    # which is reserved by the system.
    error_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If an error occurred during the task, this value specifies a text
    # description of the error. This value is set on the physical attempt object.
    # It is used to display error information to the user. The web service does
    # not parse this value.
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If an error occurred during the task, this value specifies the stack trace
    # associated with the error. This value is set on the physical attempt
    # object. It is used to display error information to the user. The web
    # service does not parse this value.
    error_stack_trace: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetTaskStatusOutput(OutputShapeBase):
    """
    Contains the output of SetTaskStatus.
    """

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
class Tag(ShapeBase):
    """
    Tags are key/value pairs defined by a user and associated with a pipeline to
    control access. AWS Data Pipeline allows you to associate ten tags per pipeline.
    For more information, see [Controlling User Access to
    Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    control-access.html) in the _AWS Data Pipeline Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The key name of a tag defined by a user. For more information, see
    # [Controlling User Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The optional value portion of a tag defined by a user. For more
    # information, see [Controlling User Access to
    # Pipelines](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-
    # control-access.html) in the _AWS Data Pipeline Developer Guide_.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TaskNotFoundException(ShapeBase):
    """
    The specified task was not found.
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

    # Description of the error message.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TaskObject(ShapeBase):
    """
    Contains information about a pipeline task that is assigned to a task runner.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "task_id",
                "taskId",
                TypeInfo(str),
            ),
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "attempt_id",
                "attemptId",
                TypeInfo(str),
            ),
            (
                "objects",
                "objects",
                TypeInfo(typing.Dict[str, PipelineObject]),
            ),
        ]

    # An internal identifier for the task. This ID is passed to the SetTaskStatus
    # and ReportTaskProgress actions.
    task_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the pipeline that provided the task.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the pipeline task attempt object. AWS Data Pipeline uses this
    # value to track how many times a task is attempted.
    attempt_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Connection information for the location where the task runner will publish
    # the output of the task.
    objects: typing.Dict[str, "PipelineObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TaskStatus(str):
    FINISHED = "FINISHED"
    FAILED = "FAILED"
    FALSE = "FALSE"


@dataclasses.dataclass
class ValidatePipelineDefinitionInput(ShapeBase):
    """
    Contains the parameters for ValidatePipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pipeline_id",
                "pipelineId",
                TypeInfo(str),
            ),
            (
                "pipeline_objects",
                "pipelineObjects",
                TypeInfo(typing.List[PipelineObject]),
            ),
            (
                "parameter_objects",
                "parameterObjects",
                TypeInfo(typing.List[ParameterObject]),
            ),
            (
                "parameter_values",
                "parameterValues",
                TypeInfo(typing.List[ParameterValue]),
            ),
        ]

    # The ID of the pipeline.
    pipeline_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The objects that define the pipeline changes to validate against the
    # pipeline.
    pipeline_objects: typing.List["PipelineObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter objects used with the pipeline.
    parameter_objects: typing.List["ParameterObject"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameter values used with the pipeline.
    parameter_values: typing.List["ParameterValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidatePipelineDefinitionOutput(OutputShapeBase):
    """
    Contains the output of ValidatePipelineDefinition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "errored",
                "errored",
                TypeInfo(bool),
            ),
            (
                "validation_errors",
                "validationErrors",
                TypeInfo(typing.List[ValidationError]),
            ),
            (
                "validation_warnings",
                "validationWarnings",
                TypeInfo(typing.List[ValidationWarning]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether there were validation errors.
    errored: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any validation errors that were found.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any validation warnings that were found.
    validation_warnings: typing.List["ValidationWarning"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationError(ShapeBase):
    """
    Defines a validation error. Validation errors prevent pipeline activation. The
    set of validation errors that can be returned are defined by AWS Data Pipeline.
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
                "errors",
                "errors",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the object that contains the validation error.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the validation error.
    errors: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidationWarning(ShapeBase):
    """
    Defines a validation warning. Validation warnings do not prevent pipeline
    activation. The set of validation warnings that can be returned are defined by
    AWS Data Pipeline.
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
                "warnings",
                "warnings",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the object that contains the validation warning.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the validation warning.
    warnings: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
