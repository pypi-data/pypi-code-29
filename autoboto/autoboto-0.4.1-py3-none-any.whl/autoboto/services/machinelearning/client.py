import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("machinelearning", *args, **kwargs)

    def add_tags(
        self,
        _request: shapes.AddTagsInput = None,
        *,
        tags: typing.List[shapes.Tag],
        resource_id: str,
        resource_type: typing.Union[str, shapes.TaggableResourceType],
    ) -> shapes.AddTagsOutput:
        """
        Adds one or more tags to an object, up to a limit of 10. Each tag consists of a
        key and an optional value. If you add a tag using a key that is already
        associated with the ML object, `AddTags` updates the tag's value.
        """
        if _request is None:
            _params = {}
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            _request = shapes.AddTagsInput(**_params)
        response = self._boto_client.add_tags(**_request.to_boto())

        return shapes.AddTagsOutput.from_boto(response)

    def create_batch_prediction(
        self,
        _request: shapes.CreateBatchPredictionInput = None,
        *,
        batch_prediction_id: str,
        ml_model_id: str,
        batch_prediction_data_source_id: str,
        output_uri: str,
        batch_prediction_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateBatchPredictionOutput:
        """
        Generates predictions for a group of observations. The observations to process
        exist in one or more data files referenced by a `DataSource`. This operation
        creates a new `BatchPrediction`, and uses an `MLModel` and the data files
        referenced by the `DataSource` as information sources.

        `CreateBatchPrediction` is an asynchronous operation. In response to
        `CreateBatchPrediction`, Amazon Machine Learning (Amazon ML) immediately returns
        and sets the `BatchPrediction` status to `PENDING`. After the `BatchPrediction`
        completes, Amazon ML sets the status to `COMPLETED`.

        You can poll for status updates by using the GetBatchPrediction operation and
        checking the `Status` parameter of the result. After the `COMPLETED` status
        appears, the results are available in the location specified by the `OutputUri`
        parameter.
        """
        if _request is None:
            _params = {}
            if batch_prediction_id is not ShapeBase.NOT_SET:
                _params['batch_prediction_id'] = batch_prediction_id
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            if batch_prediction_data_source_id is not ShapeBase.NOT_SET:
                _params['batch_prediction_data_source_id'
                       ] = batch_prediction_data_source_id
            if output_uri is not ShapeBase.NOT_SET:
                _params['output_uri'] = output_uri
            if batch_prediction_name is not ShapeBase.NOT_SET:
                _params['batch_prediction_name'] = batch_prediction_name
            _request = shapes.CreateBatchPredictionInput(**_params)
        response = self._boto_client.create_batch_prediction(
            **_request.to_boto()
        )

        return shapes.CreateBatchPredictionOutput.from_boto(response)

    def create_data_source_from_rds(
        self,
        _request: shapes.CreateDataSourceFromRDSInput = None,
        *,
        data_source_id: str,
        rds_data: shapes.RDSDataSpec,
        role_arn: str,
        data_source_name: str = ShapeBase.NOT_SET,
        compute_statistics: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDataSourceFromRDSOutput:
        """
        Creates a `DataSource` object from an [ Amazon Relational Database
        Service](http://aws.amazon.com/rds/) (Amazon RDS). A `DataSource` references
        data that can be used to perform `CreateMLModel`, `CreateEvaluation`, or
        `CreateBatchPrediction` operations.

        `CreateDataSourceFromRDS` is an asynchronous operation. In response to
        `CreateDataSourceFromRDS`, Amazon Machine Learning (Amazon ML) immediately
        returns and sets the `DataSource` status to `PENDING`. After the `DataSource` is
        created and ready for use, Amazon ML sets the `Status` parameter to `COMPLETED`.
        `DataSource` in the `COMPLETED` or `PENDING` state can be used only to perform
        `>CreateMLModel`>, `CreateEvaluation`, or `CreateBatchPrediction` operations.

        If Amazon ML cannot accept the input source, it sets the `Status` parameter to
        `FAILED` and includes an error message in the `Message` attribute of the
        `GetDataSource` operation response.
        """
        if _request is None:
            _params = {}
            if data_source_id is not ShapeBase.NOT_SET:
                _params['data_source_id'] = data_source_id
            if rds_data is not ShapeBase.NOT_SET:
                _params['rds_data'] = rds_data
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if data_source_name is not ShapeBase.NOT_SET:
                _params['data_source_name'] = data_source_name
            if compute_statistics is not ShapeBase.NOT_SET:
                _params['compute_statistics'] = compute_statistics
            _request = shapes.CreateDataSourceFromRDSInput(**_params)
        response = self._boto_client.create_data_source_from_rds(
            **_request.to_boto()
        )

        return shapes.CreateDataSourceFromRDSOutput.from_boto(response)

    def create_data_source_from_redshift(
        self,
        _request: shapes.CreateDataSourceFromRedshiftInput = None,
        *,
        data_source_id: str,
        data_spec: shapes.RedshiftDataSpec,
        role_arn: str,
        data_source_name: str = ShapeBase.NOT_SET,
        compute_statistics: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDataSourceFromRedshiftOutput:
        """
        Creates a `DataSource` from a database hosted on an Amazon Redshift cluster. A
        `DataSource` references data that can be used to perform either `CreateMLModel`,
        `CreateEvaluation`, or `CreateBatchPrediction` operations.

        `CreateDataSourceFromRedshift` is an asynchronous operation. In response to
        `CreateDataSourceFromRedshift`, Amazon Machine Learning (Amazon ML) immediately
        returns and sets the `DataSource` status to `PENDING`. After the `DataSource` is
        created and ready for use, Amazon ML sets the `Status` parameter to `COMPLETED`.
        `DataSource` in `COMPLETED` or `PENDING` states can be used to perform only
        `CreateMLModel`, `CreateEvaluation`, or `CreateBatchPrediction` operations.

        If Amazon ML can't accept the input source, it sets the `Status` parameter to
        `FAILED` and includes an error message in the `Message` attribute of the
        `GetDataSource` operation response.

        The observations should be contained in the database hosted on an Amazon
        Redshift cluster and should be specified by a `SelectSqlQuery` query. Amazon ML
        executes an `Unload` command in Amazon Redshift to transfer the result set of
        the `SelectSqlQuery` query to `S3StagingLocation`.

        After the `DataSource` has been created, it's ready for use in evaluations and
        batch predictions. If you plan to use the `DataSource` to train an `MLModel`,
        the `DataSource` also requires a recipe. A recipe describes how each input
        variable will be used in training an `MLModel`. Will the variable be included or
        excluded from training? Will the variable be manipulated; for example, will it
        be combined with another variable or will it be split apart into word
        combinations? The recipe provides answers to these questions.

        You can't change an existing datasource, but you can copy and modify the
        settings from an existing Amazon Redshift datasource to create a new datasource.
        To do so, call `GetDataSource` for an existing datasource and copy the values to
        a `CreateDataSource` call. Change the settings that you want to change and make
        sure that all required fields have the appropriate values.
        """
        if _request is None:
            _params = {}
            if data_source_id is not ShapeBase.NOT_SET:
                _params['data_source_id'] = data_source_id
            if data_spec is not ShapeBase.NOT_SET:
                _params['data_spec'] = data_spec
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if data_source_name is not ShapeBase.NOT_SET:
                _params['data_source_name'] = data_source_name
            if compute_statistics is not ShapeBase.NOT_SET:
                _params['compute_statistics'] = compute_statistics
            _request = shapes.CreateDataSourceFromRedshiftInput(**_params)
        response = self._boto_client.create_data_source_from_redshift(
            **_request.to_boto()
        )

        return shapes.CreateDataSourceFromRedshiftOutput.from_boto(response)

    def create_data_source_from_s3(
        self,
        _request: shapes.CreateDataSourceFromS3Input = None,
        *,
        data_source_id: str,
        data_spec: shapes.S3DataSpec,
        data_source_name: str = ShapeBase.NOT_SET,
        compute_statistics: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDataSourceFromS3Output:
        """
        Creates a `DataSource` object. A `DataSource` references data that can be used
        to perform `CreateMLModel`, `CreateEvaluation`, or `CreateBatchPrediction`
        operations.

        `CreateDataSourceFromS3` is an asynchronous operation. In response to
        `CreateDataSourceFromS3`, Amazon Machine Learning (Amazon ML) immediately
        returns and sets the `DataSource` status to `PENDING`. After the `DataSource`
        has been created and is ready for use, Amazon ML sets the `Status` parameter to
        `COMPLETED`. `DataSource` in the `COMPLETED` or `PENDING` state can be used to
        perform only `CreateMLModel`, `CreateEvaluation` or `CreateBatchPrediction`
        operations.

        If Amazon ML can't accept the input source, it sets the `Status` parameter to
        `FAILED` and includes an error message in the `Message` attribute of the
        `GetDataSource` operation response.

        The observation data used in a `DataSource` should be ready to use; that is, it
        should have a consistent structure, and missing data values should be kept to a
        minimum. The observation data must reside in one or more .csv files in an Amazon
        Simple Storage Service (Amazon S3) location, along with a schema that describes
        the data items by name and type. The same schema must be used for all of the
        data files referenced by the `DataSource`.

        After the `DataSource` has been created, it's ready to use in evaluations and
        batch predictions. If you plan to use the `DataSource` to train an `MLModel`,
        the `DataSource` also needs a recipe. A recipe describes how each input variable
        will be used in training an `MLModel`. Will the variable be included or excluded
        from training? Will the variable be manipulated; for example, will it be
        combined with another variable or will it be split apart into word combinations?
        The recipe provides answers to these questions.
        """
        if _request is None:
            _params = {}
            if data_source_id is not ShapeBase.NOT_SET:
                _params['data_source_id'] = data_source_id
            if data_spec is not ShapeBase.NOT_SET:
                _params['data_spec'] = data_spec
            if data_source_name is not ShapeBase.NOT_SET:
                _params['data_source_name'] = data_source_name
            if compute_statistics is not ShapeBase.NOT_SET:
                _params['compute_statistics'] = compute_statistics
            _request = shapes.CreateDataSourceFromS3Input(**_params)
        response = self._boto_client.create_data_source_from_s3(
            **_request.to_boto()
        )

        return shapes.CreateDataSourceFromS3Output.from_boto(response)

    def create_evaluation(
        self,
        _request: shapes.CreateEvaluationInput = None,
        *,
        evaluation_id: str,
        ml_model_id: str,
        evaluation_data_source_id: str,
        evaluation_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateEvaluationOutput:
        """
        Creates a new `Evaluation` of an `MLModel`. An `MLModel` is evaluated on a set
        of observations associated to a `DataSource`. Like a `DataSource` for an
        `MLModel`, the `DataSource` for an `Evaluation` contains values for the `Target
        Variable`. The `Evaluation` compares the predicted result for each observation
        to the actual outcome and provides a summary so that you know how effective the
        `MLModel` functions on the test data. Evaluation generates a relevant
        performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore
        based on the corresponding `MLModelType`: `BINARY`, `REGRESSION` or
        `MULTICLASS`.

        `CreateEvaluation` is an asynchronous operation. In response to
        `CreateEvaluation`, Amazon Machine Learning (Amazon ML) immediately returns and
        sets the evaluation status to `PENDING`. After the `Evaluation` is created and
        ready for use, Amazon ML sets the status to `COMPLETED`.

        You can use the `GetEvaluation` operation to check progress of the evaluation
        during the creation operation.
        """
        if _request is None:
            _params = {}
            if evaluation_id is not ShapeBase.NOT_SET:
                _params['evaluation_id'] = evaluation_id
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            if evaluation_data_source_id is not ShapeBase.NOT_SET:
                _params['evaluation_data_source_id'] = evaluation_data_source_id
            if evaluation_name is not ShapeBase.NOT_SET:
                _params['evaluation_name'] = evaluation_name
            _request = shapes.CreateEvaluationInput(**_params)
        response = self._boto_client.create_evaluation(**_request.to_boto())

        return shapes.CreateEvaluationOutput.from_boto(response)

    def create_ml_model(
        self,
        _request: shapes.CreateMLModelInput = None,
        *,
        ml_model_id: str,
        ml_model_type: typing.Union[str, shapes.MLModelType],
        training_data_source_id: str,
        ml_model_name: str = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
        recipe: str = ShapeBase.NOT_SET,
        recipe_uri: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateMLModelOutput:
        """
        Creates a new `MLModel` using the `DataSource` and the recipe as information
        sources.

        An `MLModel` is nearly immutable. Users can update only the `MLModelName` and
        the `ScoreThreshold` in an `MLModel` without creating a new `MLModel`.

        `CreateMLModel` is an asynchronous operation. In response to `CreateMLModel`,
        Amazon Machine Learning (Amazon ML) immediately returns and sets the `MLModel`
        status to `PENDING`. After the `MLModel` has been created and ready is for use,
        Amazon ML sets the status to `COMPLETED`.

        You can use the `GetMLModel` operation to check the progress of the `MLModel`
        during the creation operation.

        `CreateMLModel` requires a `DataSource` with computed statistics, which can be
        created by setting `ComputeStatistics` to `true` in `CreateDataSourceFromRDS`,
        `CreateDataSourceFromS3`, or `CreateDataSourceFromRedshift` operations.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            if ml_model_type is not ShapeBase.NOT_SET:
                _params['ml_model_type'] = ml_model_type
            if training_data_source_id is not ShapeBase.NOT_SET:
                _params['training_data_source_id'] = training_data_source_id
            if ml_model_name is not ShapeBase.NOT_SET:
                _params['ml_model_name'] = ml_model_name
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if recipe is not ShapeBase.NOT_SET:
                _params['recipe'] = recipe
            if recipe_uri is not ShapeBase.NOT_SET:
                _params['recipe_uri'] = recipe_uri
            _request = shapes.CreateMLModelInput(**_params)
        response = self._boto_client.create_ml_model(**_request.to_boto())

        return shapes.CreateMLModelOutput.from_boto(response)

    def create_realtime_endpoint(
        self,
        _request: shapes.CreateRealtimeEndpointInput = None,
        *,
        ml_model_id: str,
    ) -> shapes.CreateRealtimeEndpointOutput:
        """
        Creates a real-time endpoint for the `MLModel`. The endpoint contains the URI of
        the `MLModel`; that is, the location to send real-time prediction requests for
        the specified `MLModel`.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            _request = shapes.CreateRealtimeEndpointInput(**_params)
        response = self._boto_client.create_realtime_endpoint(
            **_request.to_boto()
        )

        return shapes.CreateRealtimeEndpointOutput.from_boto(response)

    def delete_batch_prediction(
        self,
        _request: shapes.DeleteBatchPredictionInput = None,
        *,
        batch_prediction_id: str,
    ) -> shapes.DeleteBatchPredictionOutput:
        """
        Assigns the DELETED status to a `BatchPrediction`, rendering it unusable.

        After using the `DeleteBatchPrediction` operation, you can use the
        GetBatchPrediction operation to verify that the status of the `BatchPrediction`
        changed to DELETED.

        **Caution:** The result of the `DeleteBatchPrediction` operation is
        irreversible.
        """
        if _request is None:
            _params = {}
            if batch_prediction_id is not ShapeBase.NOT_SET:
                _params['batch_prediction_id'] = batch_prediction_id
            _request = shapes.DeleteBatchPredictionInput(**_params)
        response = self._boto_client.delete_batch_prediction(
            **_request.to_boto()
        )

        return shapes.DeleteBatchPredictionOutput.from_boto(response)

    def delete_data_source(
        self,
        _request: shapes.DeleteDataSourceInput = None,
        *,
        data_source_id: str,
    ) -> shapes.DeleteDataSourceOutput:
        """
        Assigns the DELETED status to a `DataSource`, rendering it unusable.

        After using the `DeleteDataSource` operation, you can use the GetDataSource
        operation to verify that the status of the `DataSource` changed to DELETED.

        **Caution:** The results of the `DeleteDataSource` operation are irreversible.
        """
        if _request is None:
            _params = {}
            if data_source_id is not ShapeBase.NOT_SET:
                _params['data_source_id'] = data_source_id
            _request = shapes.DeleteDataSourceInput(**_params)
        response = self._boto_client.delete_data_source(**_request.to_boto())

        return shapes.DeleteDataSourceOutput.from_boto(response)

    def delete_evaluation(
        self,
        _request: shapes.DeleteEvaluationInput = None,
        *,
        evaluation_id: str,
    ) -> shapes.DeleteEvaluationOutput:
        """
        Assigns the `DELETED` status to an `Evaluation`, rendering it unusable.

        After invoking the `DeleteEvaluation` operation, you can use the `GetEvaluation`
        operation to verify that the status of the `Evaluation` changed to `DELETED`.

        Caution

        The results of the `DeleteEvaluation` operation are irreversible.
        """
        if _request is None:
            _params = {}
            if evaluation_id is not ShapeBase.NOT_SET:
                _params['evaluation_id'] = evaluation_id
            _request = shapes.DeleteEvaluationInput(**_params)
        response = self._boto_client.delete_evaluation(**_request.to_boto())

        return shapes.DeleteEvaluationOutput.from_boto(response)

    def delete_ml_model(
        self,
        _request: shapes.DeleteMLModelInput = None,
        *,
        ml_model_id: str,
    ) -> shapes.DeleteMLModelOutput:
        """
        Assigns the `DELETED` status to an `MLModel`, rendering it unusable.

        After using the `DeleteMLModel` operation, you can use the `GetMLModel`
        operation to verify that the status of the `MLModel` changed to DELETED.

        **Caution:** The result of the `DeleteMLModel` operation is irreversible.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            _request = shapes.DeleteMLModelInput(**_params)
        response = self._boto_client.delete_ml_model(**_request.to_boto())

        return shapes.DeleteMLModelOutput.from_boto(response)

    def delete_realtime_endpoint(
        self,
        _request: shapes.DeleteRealtimeEndpointInput = None,
        *,
        ml_model_id: str,
    ) -> shapes.DeleteRealtimeEndpointOutput:
        """
        Deletes a real time endpoint of an `MLModel`.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            _request = shapes.DeleteRealtimeEndpointInput(**_params)
        response = self._boto_client.delete_realtime_endpoint(
            **_request.to_boto()
        )

        return shapes.DeleteRealtimeEndpointOutput.from_boto(response)

    def delete_tags(
        self,
        _request: shapes.DeleteTagsInput = None,
        *,
        tag_keys: typing.List[str],
        resource_id: str,
        resource_type: typing.Union[str, shapes.TaggableResourceType],
    ) -> shapes.DeleteTagsOutput:
        """
        Deletes the specified tags associated with an ML object. After this operation is
        complete, you can't recover deleted tags.

        If you specify a tag that doesn't exist, Amazon ML ignores it.
        """
        if _request is None:
            _params = {}
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            _request = shapes.DeleteTagsInput(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

        return shapes.DeleteTagsOutput.from_boto(response)

    def describe_batch_predictions(
        self,
        _request: shapes.DescribeBatchPredictionsInput = None,
        *,
        filter_variable: typing.
        Union[str, shapes.BatchPredictionFilterVariable] = ShapeBase.NOT_SET,
        eq: str = ShapeBase.NOT_SET,
        gt: str = ShapeBase.NOT_SET,
        lt: str = ShapeBase.NOT_SET,
        ge: str = ShapeBase.NOT_SET,
        le: str = ShapeBase.NOT_SET,
        ne: str = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeBatchPredictionsOutput:
        """
        Returns a list of `BatchPrediction` operations that match the search criteria in
        the request.
        """
        if _request is None:
            _params = {}
            if filter_variable is not ShapeBase.NOT_SET:
                _params['filter_variable'] = filter_variable
            if eq is not ShapeBase.NOT_SET:
                _params['eq'] = eq
            if gt is not ShapeBase.NOT_SET:
                _params['gt'] = gt
            if lt is not ShapeBase.NOT_SET:
                _params['lt'] = lt
            if ge is not ShapeBase.NOT_SET:
                _params['ge'] = ge
            if le is not ShapeBase.NOT_SET:
                _params['le'] = le
            if ne is not ShapeBase.NOT_SET:
                _params['ne'] = ne
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeBatchPredictionsInput(**_params)
        paginator = self.get_paginator("describe_batch_predictions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeBatchPredictionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeBatchPredictionsOutput.from_boto(response)

    def describe_data_sources(
        self,
        _request: shapes.DescribeDataSourcesInput = None,
        *,
        filter_variable: typing.
        Union[str, shapes.DataSourceFilterVariable] = ShapeBase.NOT_SET,
        eq: str = ShapeBase.NOT_SET,
        gt: str = ShapeBase.NOT_SET,
        lt: str = ShapeBase.NOT_SET,
        ge: str = ShapeBase.NOT_SET,
        le: str = ShapeBase.NOT_SET,
        ne: str = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDataSourcesOutput:
        """
        Returns a list of `DataSource` that match the search criteria in the request.
        """
        if _request is None:
            _params = {}
            if filter_variable is not ShapeBase.NOT_SET:
                _params['filter_variable'] = filter_variable
            if eq is not ShapeBase.NOT_SET:
                _params['eq'] = eq
            if gt is not ShapeBase.NOT_SET:
                _params['gt'] = gt
            if lt is not ShapeBase.NOT_SET:
                _params['lt'] = lt
            if ge is not ShapeBase.NOT_SET:
                _params['ge'] = ge
            if le is not ShapeBase.NOT_SET:
                _params['le'] = le
            if ne is not ShapeBase.NOT_SET:
                _params['ne'] = ne
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeDataSourcesInput(**_params)
        paginator = self.get_paginator("describe_data_sources").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeDataSourcesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeDataSourcesOutput.from_boto(response)

    def describe_evaluations(
        self,
        _request: shapes.DescribeEvaluationsInput = None,
        *,
        filter_variable: typing.
        Union[str, shapes.EvaluationFilterVariable] = ShapeBase.NOT_SET,
        eq: str = ShapeBase.NOT_SET,
        gt: str = ShapeBase.NOT_SET,
        lt: str = ShapeBase.NOT_SET,
        ge: str = ShapeBase.NOT_SET,
        le: str = ShapeBase.NOT_SET,
        ne: str = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEvaluationsOutput:
        """
        Returns a list of `DescribeEvaluations` that match the search criteria in the
        request.
        """
        if _request is None:
            _params = {}
            if filter_variable is not ShapeBase.NOT_SET:
                _params['filter_variable'] = filter_variable
            if eq is not ShapeBase.NOT_SET:
                _params['eq'] = eq
            if gt is not ShapeBase.NOT_SET:
                _params['gt'] = gt
            if lt is not ShapeBase.NOT_SET:
                _params['lt'] = lt
            if ge is not ShapeBase.NOT_SET:
                _params['ge'] = ge
            if le is not ShapeBase.NOT_SET:
                _params['le'] = le
            if ne is not ShapeBase.NOT_SET:
                _params['ne'] = ne
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeEvaluationsInput(**_params)
        paginator = self.get_paginator("describe_evaluations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeEvaluationsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeEvaluationsOutput.from_boto(response)

    def describe_ml_models(
        self,
        _request: shapes.DescribeMLModelsInput = None,
        *,
        filter_variable: typing.
        Union[str, shapes.MLModelFilterVariable] = ShapeBase.NOT_SET,
        eq: str = ShapeBase.NOT_SET,
        gt: str = ShapeBase.NOT_SET,
        lt: str = ShapeBase.NOT_SET,
        ge: str = ShapeBase.NOT_SET,
        le: str = ShapeBase.NOT_SET,
        ne: str = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
        sort_order: typing.Union[str, shapes.SortOrder] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMLModelsOutput:
        """
        Returns a list of `MLModel` that match the search criteria in the request.
        """
        if _request is None:
            _params = {}
            if filter_variable is not ShapeBase.NOT_SET:
                _params['filter_variable'] = filter_variable
            if eq is not ShapeBase.NOT_SET:
                _params['eq'] = eq
            if gt is not ShapeBase.NOT_SET:
                _params['gt'] = gt
            if lt is not ShapeBase.NOT_SET:
                _params['lt'] = lt
            if ge is not ShapeBase.NOT_SET:
                _params['ge'] = ge
            if le is not ShapeBase.NOT_SET:
                _params['le'] = le
            if ne is not ShapeBase.NOT_SET:
                _params['ne'] = ne
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            if sort_order is not ShapeBase.NOT_SET:
                _params['sort_order'] = sort_order
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeMLModelsInput(**_params)
        paginator = self.get_paginator("describe_ml_models").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeMLModelsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeMLModelsOutput.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsInput = None,
        *,
        resource_id: str,
        resource_type: typing.Union[str, shapes.TaggableResourceType],
    ) -> shapes.DescribeTagsOutput:
        """
        Describes one or more of the tags for your Amazon ML object.
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            _request = shapes.DescribeTagsInput(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.DescribeTagsOutput.from_boto(response)

    def get_batch_prediction(
        self,
        _request: shapes.GetBatchPredictionInput = None,
        *,
        batch_prediction_id: str,
    ) -> shapes.GetBatchPredictionOutput:
        """
        Returns a `BatchPrediction` that includes detailed metadata, status, and data
        file information for a `Batch Prediction` request.
        """
        if _request is None:
            _params = {}
            if batch_prediction_id is not ShapeBase.NOT_SET:
                _params['batch_prediction_id'] = batch_prediction_id
            _request = shapes.GetBatchPredictionInput(**_params)
        response = self._boto_client.get_batch_prediction(**_request.to_boto())

        return shapes.GetBatchPredictionOutput.from_boto(response)

    def get_data_source(
        self,
        _request: shapes.GetDataSourceInput = None,
        *,
        data_source_id: str,
        verbose: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetDataSourceOutput:
        """
        Returns a `DataSource` that includes metadata and data file information, as well
        as the current status of the `DataSource`.

        `GetDataSource` provides results in normal or verbose format. The verbose format
        adds the schema description and the list of files pointed to by the DataSource
        to the normal format.
        """
        if _request is None:
            _params = {}
            if data_source_id is not ShapeBase.NOT_SET:
                _params['data_source_id'] = data_source_id
            if verbose is not ShapeBase.NOT_SET:
                _params['verbose'] = verbose
            _request = shapes.GetDataSourceInput(**_params)
        response = self._boto_client.get_data_source(**_request.to_boto())

        return shapes.GetDataSourceOutput.from_boto(response)

    def get_evaluation(
        self,
        _request: shapes.GetEvaluationInput = None,
        *,
        evaluation_id: str,
    ) -> shapes.GetEvaluationOutput:
        """
        Returns an `Evaluation` that includes metadata as well as the current status of
        the `Evaluation`.
        """
        if _request is None:
            _params = {}
            if evaluation_id is not ShapeBase.NOT_SET:
                _params['evaluation_id'] = evaluation_id
            _request = shapes.GetEvaluationInput(**_params)
        response = self._boto_client.get_evaluation(**_request.to_boto())

        return shapes.GetEvaluationOutput.from_boto(response)

    def get_ml_model(
        self,
        _request: shapes.GetMLModelInput = None,
        *,
        ml_model_id: str,
        verbose: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetMLModelOutput:
        """
        Returns an `MLModel` that includes detailed metadata, data source information,
        and the current status of the `MLModel`.

        `GetMLModel` provides results in normal or verbose format.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            if verbose is not ShapeBase.NOT_SET:
                _params['verbose'] = verbose
            _request = shapes.GetMLModelInput(**_params)
        response = self._boto_client.get_ml_model(**_request.to_boto())

        return shapes.GetMLModelOutput.from_boto(response)

    def predict(
        self,
        _request: shapes.PredictInput = None,
        *,
        ml_model_id: str,
        record: typing.Dict[str, str],
        predict_endpoint: str,
    ) -> shapes.PredictOutput:
        """
        Generates a prediction for the observation using the specified `ML Model`.

        Note

        Not all response parameters will be populated. Whether a response parameter is
        populated depends on the type of model requested.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            if record is not ShapeBase.NOT_SET:
                _params['record'] = record
            if predict_endpoint is not ShapeBase.NOT_SET:
                _params['predict_endpoint'] = predict_endpoint
            _request = shapes.PredictInput(**_params)
        response = self._boto_client.predict(**_request.to_boto())

        return shapes.PredictOutput.from_boto(response)

    def update_batch_prediction(
        self,
        _request: shapes.UpdateBatchPredictionInput = None,
        *,
        batch_prediction_id: str,
        batch_prediction_name: str,
    ) -> shapes.UpdateBatchPredictionOutput:
        """
        Updates the `BatchPredictionName` of a `BatchPrediction`.

        You can use the `GetBatchPrediction` operation to view the contents of the
        updated data element.
        """
        if _request is None:
            _params = {}
            if batch_prediction_id is not ShapeBase.NOT_SET:
                _params['batch_prediction_id'] = batch_prediction_id
            if batch_prediction_name is not ShapeBase.NOT_SET:
                _params['batch_prediction_name'] = batch_prediction_name
            _request = shapes.UpdateBatchPredictionInput(**_params)
        response = self._boto_client.update_batch_prediction(
            **_request.to_boto()
        )

        return shapes.UpdateBatchPredictionOutput.from_boto(response)

    def update_data_source(
        self,
        _request: shapes.UpdateDataSourceInput = None,
        *,
        data_source_id: str,
        data_source_name: str,
    ) -> shapes.UpdateDataSourceOutput:
        """
        Updates the `DataSourceName` of a `DataSource`.

        You can use the `GetDataSource` operation to view the contents of the updated
        data element.
        """
        if _request is None:
            _params = {}
            if data_source_id is not ShapeBase.NOT_SET:
                _params['data_source_id'] = data_source_id
            if data_source_name is not ShapeBase.NOT_SET:
                _params['data_source_name'] = data_source_name
            _request = shapes.UpdateDataSourceInput(**_params)
        response = self._boto_client.update_data_source(**_request.to_boto())

        return shapes.UpdateDataSourceOutput.from_boto(response)

    def update_evaluation(
        self,
        _request: shapes.UpdateEvaluationInput = None,
        *,
        evaluation_id: str,
        evaluation_name: str,
    ) -> shapes.UpdateEvaluationOutput:
        """
        Updates the `EvaluationName` of an `Evaluation`.

        You can use the `GetEvaluation` operation to view the contents of the updated
        data element.
        """
        if _request is None:
            _params = {}
            if evaluation_id is not ShapeBase.NOT_SET:
                _params['evaluation_id'] = evaluation_id
            if evaluation_name is not ShapeBase.NOT_SET:
                _params['evaluation_name'] = evaluation_name
            _request = shapes.UpdateEvaluationInput(**_params)
        response = self._boto_client.update_evaluation(**_request.to_boto())

        return shapes.UpdateEvaluationOutput.from_boto(response)

    def update_ml_model(
        self,
        _request: shapes.UpdateMLModelInput = None,
        *,
        ml_model_id: str,
        ml_model_name: str = ShapeBase.NOT_SET,
        score_threshold: float = ShapeBase.NOT_SET,
    ) -> shapes.UpdateMLModelOutput:
        """
        Updates the `MLModelName` and the `ScoreThreshold` of an `MLModel`.

        You can use the `GetMLModel` operation to view the contents of the updated data
        element.
        """
        if _request is None:
            _params = {}
            if ml_model_id is not ShapeBase.NOT_SET:
                _params['ml_model_id'] = ml_model_id
            if ml_model_name is not ShapeBase.NOT_SET:
                _params['ml_model_name'] = ml_model_name
            if score_threshold is not ShapeBase.NOT_SET:
                _params['score_threshold'] = score_threshold
            _request = shapes.UpdateMLModelInput(**_params)
        response = self._boto_client.update_ml_model(**_request.to_boto())

        return shapes.UpdateMLModelOutput.from_boto(response)
