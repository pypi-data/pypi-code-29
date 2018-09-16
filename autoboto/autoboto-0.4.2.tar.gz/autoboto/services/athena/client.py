import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("athena", *args, **kwargs)

    def batch_get_named_query(
        self,
        _request: shapes.BatchGetNamedQueryInput = None,
        *,
        named_query_ids: typing.List[str],
    ) -> shapes.BatchGetNamedQueryOutput:
        """
        Returns the details of a single named query or a list of up to 50 queries, which
        you provide as an array of query ID strings. Use ListNamedQueries to get the
        list of named query IDs. If information could not be retrieved for a submitted
        query ID, information about the query ID submitted is listed under
        UnprocessedNamedQueryId. Named queries are different from executed queries. Use
        BatchGetQueryExecution to get details about each unique query execution, and
        ListQueryExecutions to get a list of query execution IDs.
        """
        if _request is None:
            _params = {}
            if named_query_ids is not ShapeBase.NOT_SET:
                _params['named_query_ids'] = named_query_ids
            _request = shapes.BatchGetNamedQueryInput(**_params)
        response = self._boto_client.batch_get_named_query(**_request.to_boto())

        return shapes.BatchGetNamedQueryOutput.from_boto(response)

    def batch_get_query_execution(
        self,
        _request: shapes.BatchGetQueryExecutionInput = None,
        *,
        query_execution_ids: typing.List[str],
    ) -> shapes.BatchGetQueryExecutionOutput:
        """
        Returns the details of a single query execution or a list of up to 50 query
        executions, which you provide as an array of query execution ID strings. To get
        a list of query execution IDs, use ListQueryExecutions. Query executions are
        different from named (saved) queries. Use BatchGetNamedQuery to get details
        about named queries.
        """
        if _request is None:
            _params = {}
            if query_execution_ids is not ShapeBase.NOT_SET:
                _params['query_execution_ids'] = query_execution_ids
            _request = shapes.BatchGetQueryExecutionInput(**_params)
        response = self._boto_client.batch_get_query_execution(
            **_request.to_boto()
        )

        return shapes.BatchGetQueryExecutionOutput.from_boto(response)

    def create_named_query(
        self,
        _request: shapes.CreateNamedQueryInput = None,
        *,
        name: str,
        database: str,
        query_string: str,
        description: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateNamedQueryOutput:
        """
        Creates a named query.

        For code samples using the AWS SDK for Java, see [Examples and Code
        Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the
        _Amazon Athena User Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if database is not ShapeBase.NOT_SET:
                _params['database'] = database
            if query_string is not ShapeBase.NOT_SET:
                _params['query_string'] = query_string
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateNamedQueryInput(**_params)
        response = self._boto_client.create_named_query(**_request.to_boto())

        return shapes.CreateNamedQueryOutput.from_boto(response)

    def delete_named_query(
        self,
        _request: shapes.DeleteNamedQueryInput = None,
        *,
        named_query_id: str,
    ) -> shapes.DeleteNamedQueryOutput:
        """
        Deletes a named query.

        For code samples using the AWS SDK for Java, see [Examples and Code
        Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the
        _Amazon Athena User Guide_.
        """
        if _request is None:
            _params = {}
            if named_query_id is not ShapeBase.NOT_SET:
                _params['named_query_id'] = named_query_id
            _request = shapes.DeleteNamedQueryInput(**_params)
        response = self._boto_client.delete_named_query(**_request.to_boto())

        return shapes.DeleteNamedQueryOutput.from_boto(response)

    def get_named_query(
        self,
        _request: shapes.GetNamedQueryInput = None,
        *,
        named_query_id: str,
    ) -> shapes.GetNamedQueryOutput:
        """
        Returns information about a single query.
        """
        if _request is None:
            _params = {}
            if named_query_id is not ShapeBase.NOT_SET:
                _params['named_query_id'] = named_query_id
            _request = shapes.GetNamedQueryInput(**_params)
        response = self._boto_client.get_named_query(**_request.to_boto())

        return shapes.GetNamedQueryOutput.from_boto(response)

    def get_query_execution(
        self,
        _request: shapes.GetQueryExecutionInput = None,
        *,
        query_execution_id: str,
    ) -> shapes.GetQueryExecutionOutput:
        """
        Returns information about a single execution of a query. Each time a query
        executes, information about the query execution is saved with a unique ID.
        """
        if _request is None:
            _params = {}
            if query_execution_id is not ShapeBase.NOT_SET:
                _params['query_execution_id'] = query_execution_id
            _request = shapes.GetQueryExecutionInput(**_params)
        response = self._boto_client.get_query_execution(**_request.to_boto())

        return shapes.GetQueryExecutionOutput.from_boto(response)

    def get_query_results(
        self,
        _request: shapes.GetQueryResultsInput = None,
        *,
        query_execution_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetQueryResultsOutput:
        """
        Returns the results of a single query execution specified by `QueryExecutionId`.
        This request does not execute the query but returns results. Use
        StartQueryExecution to run a query.
        """
        if _request is None:
            _params = {}
            if query_execution_id is not ShapeBase.NOT_SET:
                _params['query_execution_id'] = query_execution_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetQueryResultsInput(**_params)
        paginator = self.get_paginator("get_query_results").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetQueryResultsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetQueryResultsOutput.from_boto(response)

    def list_named_queries(
        self,
        _request: shapes.ListNamedQueriesInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListNamedQueriesOutput:
        """
        Provides a list of all available query IDs.

        For code samples using the AWS SDK for Java, see [Examples and Code
        Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the
        _Amazon Athena User Guide_.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListNamedQueriesInput(**_params)
        paginator = self.get_paginator("list_named_queries").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListNamedQueriesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListNamedQueriesOutput.from_boto(response)

    def list_query_executions(
        self,
        _request: shapes.ListQueryExecutionsInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListQueryExecutionsOutput:
        """
        Provides a list of all available query execution IDs.

        For code samples using the AWS SDK for Java, see [Examples and Code
        Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the
        _Amazon Athena User Guide_.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListQueryExecutionsInput(**_params)
        paginator = self.get_paginator("list_query_executions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListQueryExecutionsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListQueryExecutionsOutput.from_boto(response)

    def start_query_execution(
        self,
        _request: shapes.StartQueryExecutionInput = None,
        *,
        query_string: str,
        result_configuration: shapes.ResultConfiguration,
        client_request_token: str = ShapeBase.NOT_SET,
        query_execution_context: shapes.QueryExecutionContext = ShapeBase.
        NOT_SET,
    ) -> shapes.StartQueryExecutionOutput:
        """
        Runs (executes) the SQL query statements contained in the `Query` string.

        For code samples using the AWS SDK for Java, see [Examples and Code
        Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the
        _Amazon Athena User Guide_.
        """
        if _request is None:
            _params = {}
            if query_string is not ShapeBase.NOT_SET:
                _params['query_string'] = query_string
            if result_configuration is not ShapeBase.NOT_SET:
                _params['result_configuration'] = result_configuration
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if query_execution_context is not ShapeBase.NOT_SET:
                _params['query_execution_context'] = query_execution_context
            _request = shapes.StartQueryExecutionInput(**_params)
        response = self._boto_client.start_query_execution(**_request.to_boto())

        return shapes.StartQueryExecutionOutput.from_boto(response)

    def stop_query_execution(
        self,
        _request: shapes.StopQueryExecutionInput = None,
        *,
        query_execution_id: str,
    ) -> shapes.StopQueryExecutionOutput:
        """
        Stops a query execution.

        For code samples using the AWS SDK for Java, see [Examples and Code
        Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the
        _Amazon Athena User Guide_.
        """
        if _request is None:
            _params = {}
            if query_execution_id is not ShapeBase.NOT_SET:
                _params['query_execution_id'] = query_execution_id
            _request = shapes.StopQueryExecutionInput(**_params)
        response = self._boto_client.stop_query_execution(**_request.to_boto())

        return shapes.StopQueryExecutionOutput.from_boto(response)
