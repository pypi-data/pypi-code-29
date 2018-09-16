import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mobile", *args, **kwargs)

    def create_project(
        self,
        _request: shapes.CreateProjectRequest = None,
        *,
        name: str = ShapeBase.NOT_SET,
        region: str = ShapeBase.NOT_SET,
        contents: typing.Any = ShapeBase.NOT_SET,
        snapshot_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateProjectResult:
        """
        Creates an AWS Mobile Hub project.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if region is not ShapeBase.NOT_SET:
                _params['region'] = region
            if contents is not ShapeBase.NOT_SET:
                _params['contents'] = contents
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            _request = shapes.CreateProjectRequest(**_params)
        response = self._boto_client.create_project(**_request.to_boto())

        return shapes.CreateProjectResult.from_boto(response)

    def delete_project(
        self,
        _request: shapes.DeleteProjectRequest = None,
        *,
        project_id: str,
    ) -> shapes.DeleteProjectResult:
        """
        Delets a project in AWS Mobile Hub.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            _request = shapes.DeleteProjectRequest(**_params)
        response = self._boto_client.delete_project(**_request.to_boto())

        return shapes.DeleteProjectResult.from_boto(response)

    def describe_bundle(
        self,
        _request: shapes.DescribeBundleRequest = None,
        *,
        bundle_id: str,
    ) -> shapes.DescribeBundleResult:
        """
        Get the bundle details for the requested bundle id.
        """
        if _request is None:
            _params = {}
            if bundle_id is not ShapeBase.NOT_SET:
                _params['bundle_id'] = bundle_id
            _request = shapes.DescribeBundleRequest(**_params)
        response = self._boto_client.describe_bundle(**_request.to_boto())

        return shapes.DescribeBundleResult.from_boto(response)

    def describe_project(
        self,
        _request: shapes.DescribeProjectRequest = None,
        *,
        project_id: str,
        sync_from_resources: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeProjectResult:
        """
        Gets details about a project in AWS Mobile Hub.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if sync_from_resources is not ShapeBase.NOT_SET:
                _params['sync_from_resources'] = sync_from_resources
            _request = shapes.DescribeProjectRequest(**_params)
        response = self._boto_client.describe_project(**_request.to_boto())

        return shapes.DescribeProjectResult.from_boto(response)

    def export_bundle(
        self,
        _request: shapes.ExportBundleRequest = None,
        *,
        bundle_id: str,
        project_id: str = ShapeBase.NOT_SET,
        platform: typing.Union[str, shapes.Platform] = ShapeBase.NOT_SET,
    ) -> shapes.ExportBundleResult:
        """
        Generates customized software development kit (SDK) and or tool packages used to
        integrate mobile web or mobile app clients with backend AWS resources.
        """
        if _request is None:
            _params = {}
            if bundle_id is not ShapeBase.NOT_SET:
                _params['bundle_id'] = bundle_id
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if platform is not ShapeBase.NOT_SET:
                _params['platform'] = platform
            _request = shapes.ExportBundleRequest(**_params)
        response = self._boto_client.export_bundle(**_request.to_boto())

        return shapes.ExportBundleResult.from_boto(response)

    def export_project(
        self,
        _request: shapes.ExportProjectRequest = None,
        *,
        project_id: str,
    ) -> shapes.ExportProjectResult:
        """
        Exports project configuration to a snapshot which can be downloaded and shared.
        Note that mobile app push credentials are encrypted in exported projects, so
        they can only be shared successfully within the same AWS account.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            _request = shapes.ExportProjectRequest(**_params)
        response = self._boto_client.export_project(**_request.to_boto())

        return shapes.ExportProjectResult.from_boto(response)

    def list_bundles(
        self,
        _request: shapes.ListBundlesRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBundlesResult:
        """
        List all available bundles.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListBundlesRequest(**_params)
        paginator = self.get_paginator("list_bundles").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListBundlesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListBundlesResult.from_boto(response)

    def list_projects(
        self,
        _request: shapes.ListProjectsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListProjectsResult:
        """
        Lists projects in AWS Mobile Hub.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListProjectsRequest(**_params)
        paginator = self.get_paginator("list_projects").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListProjectsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListProjectsResult.from_boto(response)

    def update_project(
        self,
        _request: shapes.UpdateProjectRequest = None,
        *,
        project_id: str,
        contents: typing.Any = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProjectResult:
        """
        Update an existing project.
        """
        if _request is None:
            _params = {}
            if project_id is not ShapeBase.NOT_SET:
                _params['project_id'] = project_id
            if contents is not ShapeBase.NOT_SET:
                _params['contents'] = contents
            _request = shapes.UpdateProjectRequest(**_params)
        response = self._boto_client.update_project(**_request.to_boto())

        return shapes.UpdateProjectResult.from_boto(response)
