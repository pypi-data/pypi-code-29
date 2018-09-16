import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cur", *args, **kwargs)

    def delete_report_definition(
        self,
        _request: shapes.DeleteReportDefinitionRequest = None,
        *,
        report_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteReportDefinitionResponse:
        """
        Delete a specified report definition
        """
        if _request is None:
            _params = {}
            if report_name is not ShapeBase.NOT_SET:
                _params['report_name'] = report_name
            _request = shapes.DeleteReportDefinitionRequest(**_params)
        response = self._boto_client.delete_report_definition(
            **_request.to_boto()
        )

        return shapes.DeleteReportDefinitionResponse.from_boto(response)

    def describe_report_definitions(
        self,
        _request: shapes.DescribeReportDefinitionsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReportDefinitionsResponse:
        """
        Describe a list of report definitions owned by the account
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeReportDefinitionsRequest(**_params)
        paginator = self.get_paginator("describe_report_definitions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReportDefinitionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReportDefinitionsResponse.from_boto(response)

    def put_report_definition(
        self,
        _request: shapes.PutReportDefinitionRequest = None,
        *,
        report_definition: shapes.ReportDefinition,
    ) -> shapes.PutReportDefinitionResponse:
        """
        Create a new report definition
        """
        if _request is None:
            _params = {}
            if report_definition is not ShapeBase.NOT_SET:
                _params['report_definition'] = report_definition
            _request = shapes.PutReportDefinitionRequest(**_params)
        response = self._boto_client.put_report_definition(**_request.to_boto())

        return shapes.PutReportDefinitionResponse.from_boto(response)
